import autosklearn.classification
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2
from imblearn.over_sampling import SMOTE

feature_types = {
    "project_metrics": ["num_commits", "project_age_days", "num_issues", "num_pull", 
                        "num_stargazers", "num_watchers", "num_forks", "num_subscribers", 
                        "num_contributors", "project_size(kB)"],
    "security_practice_scores": ["ssf0_Binary-Artifacts", "ssf1_Branch-Protection",
                          "ssf3_CII-Best-Practices", "ssf7_Dependency-Update-Tool",
                          "ssf8_Fuzzing", "ssf9_License", "ssf10_Maintained", "ssf13_SAST",
                          "ssf17_Vulnerabilities"],
    "code_quality_metrics": ['num_sonarQube_BUG_HIGH', 'num_sonarQube_BUG_MEDIUM', 'num_sonarQube_BUG_LOW', 'num_sonarQube_BUG_BLOCKER',
            'num_sonarQube_VULNERABILITY_HIGH', 'num_sonarQube_VULNERABILITY_MEDIUM', 'num_sonarQube_VULNERABILITY_LOW',
            'num_sonarQube_VULNERABILITY_BLOCKER', 'num_sonarQube_CODE_SMELL_HIGH', 'num_sonarQube_CODE_SMELL_MEDIUM',
            'num_sonarQube_CODE_SMELL_LOW', 'num_sonarQube_CODE_SMELL_BLOCKER'],
}
categories = ["Generic policy", "Reporting mechanism", "Scope of practice", "User guideline"]

def select_top_features(features, target_column, features_list):
    print(f"Finding top 5 features for {features_list}")
    X = features
    y = target_column
    selector = SelectKBest(chi2, k=min(5, X.shape[1]))
    selector.fit(X, y)
    top_features = X.columns[selector.get_support()].tolist()
    print(f"Selected features: {top_features}")
    return top_features

def model(feature , target_column):
    X = feature
    y = data[target_column]
    smote = SMOTE()
    X_resampled, y_resampled = smote.fit_resample(X, y)
    X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3)
    classifier = autosklearn.classification.AutoSklearnClassifier(
        time_left_for_this_task=3600,
        per_run_time_limit=300
        )
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    pred_proba = classifier.predict_proba(X_test)[:, 1]
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_pred, y_test, output_dict=True)
    report1 = classification_report(y_pred, y_test)
    macro_avg_f1 = report['macro avg']['f1-score']
    auc = roc_auc_score(y_test, pred_proba) if pred_proba is not None else "N/A"
    print(f"Accuracy: {accuracy}")
    print(f"Macro avg: {macro_avg_f1}")
    print(f"AUC score: {auc}")
    print("Classification report:")
    print(report1)
    return accuracy, auc, macro_avg_f1, classifier, X_train, X_test, y_train, y_test, X

def get_best_model(models_dict):
    if not models_dict:
        return None
    for model_info in models_dict.values():
        if model_info.get('rank') == 1:
            best_model = model_info.get('sklearn_classifier', None)
            print(best_model)
            return best_model
    return None

if __name__ == "__main__":
    print("\ ---------------------------------------------------------------- \n")
    data = pd.read_csv('Dataset.csv')  
    results = []
    for target_column in categories:
        for feature_set_name, features in feature_types.items():
            print(f"\nProcessing {target_column} with {feature_set_name} features...")
            selected_features = select_top_features(data[features], data[target_column], features)
            accuracy, auc, macro_avg_f1, classifier, X_train, X_test, y_train, y_test, X = model(data[selected_features], target_column)
            models_dict = classifier.show_models()
            sklearn_regressor = get_best_model(models_dict)
            print(f"finish: The best model for {target_column} ({feature_set_name}) is {sklearn_regressor}")
            results.append([target_column, feature_set_name, selected_features, accuracy, auc, macro_avg_f1, sklearn_regressor])
    results_df = pd.DataFrame(results, columns=['Target Column', 'feature_types', 'selected_features', 'Accuracy', 'AUC', 'Macro Avg F1', 'Best Model'])
    results_df.to_csv('results/model_results.csv', index=False)
    print("All processing complete. Results saved to model_results.csv.")
