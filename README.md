# Characterizing Security Policies in Python Libraries (2025)


This dataset is supplementary to our research article submitted to *Empirical Software Engineering (EMSE)*, titled **"Security by Documentation? Characterizing GitHub SECURITY.md policy and their Adoption in Python Libraries"**


## Overview

This dataset includes metadata and content collected from public GitHub repositories that contain a `SECURITY.md` file. The study explores how open-source projects adopt and document their security policies, focusing on practices related to vulnerability disclosure, contact information, and update frequency.

## Contents

- `RQ1/`: Directory containing the analysis scripts and data used for addressing RQ1.
    - `Content_Categories.csv`: The content of the document and the classified content.
    - `rq1.ipynb`: A script for data analysis for RQ1
- `RQ2/`: Directory containing the analysis scripts and data used for addressing RQ2.
    - `rq2.ipynb`: A script for data analysis in RQ2
- `RQ3/`: Directory containing the analysis scripts and data used for addressing RQ3.
    - `SSF.ipynb`: A script for security practices assessment using OpenSSF Scorecard.
    - `rq3`: A script for data analysis in RQ3.
- `RQ4/`: Directory containing the analysis scripts and data used for addressing RQ4.
    - `rq4.ipynb`:  A script for data analysis in RQ4.
- `Project_withPolicy.csv`: Dataset containing feature information of PyPI projects that include a security policy.
- `Project_withoutPolicy.csv`: Dataset containing feature information of PyPI projects that do not include a security policy.
- `README.md`: This documentation file.
- `Security_Issues.json`: Collection of security-related issues from PyPI projects that include a security policy.
- `feature_description.md`: The feature descriptions of data collection used in the analysis.



## Format Summary
- **Security_Issues.json**
- **Project_withPolicy.csv**
- **Project_withoutPolicy.csv**

The feature descriptions for the dataset are described in `feature_description.md`.

- **RQ1** Includes the dataset and script for data analysis technique:
    - `Content_Categories.csv` : Data set contains the content of the document and the classified content.
        - Category: Categories are selected for the content by classifier
        - Document: Raw text extracted from SECURITY.md files.
    - `rq1.ipynb`: A script for data analysis for RQ1 include:
        - Association rules
        - Frequent Itemsets
        - Topic model

- **RQ2** Includes script for data analysis technique:
    - `rq2.ipynb`: A script for data analysis of the projects with Reporting mechanism.

- **RQ3** Includes the dataset and script for data analysis technique:
    - `SSF.ipynb`: A script for security practices assessment using OpenSSF Scorecard.
    - `rq3.ipynb`: A script for statistical analysis used in RQ3.
        - Normality test
        - Statistical test
- **RQ4** Includes script for data analysis technique:
	- `rq4.ipynb`: A script for statistical analysis used in RQ4
        - Models
        - SHAP

## Usage

This dataset is intended to support replication, secondary analysis, and further studies in software security, open-source practices, and empirical software engineering. It can be used to explore trends, evaluate documentation practices, or develop automated tools for classifying security-related content.


## Citation

Please cite this dataset as:

> Choetkiertikul, M. (2025). *Dataset of Security Policies in GitHub Projects* [Data set]. GitHub. https://github.com/sswpka/Characterizing-Security-Policy-Python-Libraries

This dataset supports:

> Choetkiertikul, M. et al. (2025). *Security by Documentation? Characterizing GitHub SECURITY.md policy and their Adoption in Python Libraries
*. Submitted to *Empirical Software Engineering (EMSE)*.


## License

This dataset is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. You may use, share, and adapt the data with appropriate credit.

## Contact


For questions or collaborations, contact:


**Morakot Choetkiertikul**  
Email: morakot.c@mahidol.edu
