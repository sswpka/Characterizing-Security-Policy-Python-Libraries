## Feature description

The feature descriptions of data collection used in the analysis.

| **Feature**              | **Description** |
| --- | --- |
| project_name | The name of the project. |
| SecurityPolicy_content | The raw content of the project’s security policy. |
| num_commits | The number of commits made in the project. |
| project_age_days | The age of the project, counted in days. |
| num_contributors | The number of contributors who have contributed to the project. |
| num_pull | The number of pull requests in the project. |
| num_issues | The number of issues created in the project. |
| project_size | The size of the project repository in kilobytes. |
| num_stargazers | The number of users who have starred the project. |
| num_watchers | The number of users watching the project for updates. |
| num_forks | The number of times the project has been forked. |
| num_subscribers | The number of users subscribed to project notifications. |
| security_issues | The information about reported security issues in the project. |
| issue_created_date  | The date when the security issue was created. |
| issue_author | The username of the author who reported the security issue. |
| issue_author_association | The relationship of the author to the project (e.g., contributor, member, owner). |
| issue_labels | The labels used to classify types of issues. |
| Aggregate                | The overall SSF (Security Scorecard Framework) score of the project. |
| Binary-Artifacts         | The metric checks the presence of binary artifacts within the project. |
| Branch-Protection        | The metric evaluates the branch protection settings and the enforcement of branch protection rules in the GitHub project. |
| CI-Tests                 | The metric indicates whether the project runs tests before merging pull requests by using continuous integration (CI) to detect bugs or vulnerabilities in the development process. |
| CII-Best-Practices       | The metric assesses a project's compliance with the CII Best Practices badge, indicating whether the project follows a set of security-focused best development practices for open-source software. |
| Code-Review              | The metric assesses whether the project performs code reviews before merging pull requests. It checks for the presence of Branch-Protection with at least one required reviewer, approval reviews in the last 30 commits, or the use of tools such as Prow or Gerrit. |
| Contributors             | The metric assesses whether a project has contributors from multiple organizations, as identified by the Company field on their GitHub profiles. |
| Dangerous-Workflow       | The metric determines if there are dangerous patterns in the package's GitHub workflows due to misconfigured GitHub Actions. |
| Dependency-Update-Tool   | The metric evaluates whether an automated dependency update tool, such as Dependabot, Renovate Bot, or PyUp, is enabled within the project. |
| Fuzzing                  | The metric verifies whether fuzzing is implemented in the project by checking if its name appears in the OSS-Fuzz project list. |
| License                  | The metric indicates whether the project has published a license by checking standard locations for a file named according to common conventions for licenses. |
| Maintained               | The metric assesses whether the project is actively maintained by checking commit and issue activities from collaborators, members, or project owners within the past 90 days. |
| Packaging                | The metric determines whether the project has language-specific packaging workflows that upload relevant files for project distribution. |
| Pinned-Dependencies      | The metric checks whether a project pins its dependencies during the build and release processes by detecting unpinned dependencies in Dockerfiles, shell scripts, and GitHub workflows. |
| SAST                     | The metric checks whether Static Application Security Testing (SAST) is implemented in a project by detecting the use of GitHub applications such as CodeQL, SonarCloud, or LGTM, or by checking for the presence of the `github/codeql-action` in the workflows of recently merged pull requests. |
| Security-Policy          | The metric assesses the presence of a `SECURITY.md` file by checking well-known directories and evaluates whether the security policy details provided are sufficient. |
| Signed-Releases          | The metric determines if the project has signed release artifacts in GitHub by looking for the filenames .minisig, .asc (pgp), .sig, .sign, .sigstore, or .intoto.jsonl in the project's last five releases. |
| Token-Permissions        | The metric evaluates whether the project's automated workflow adheres to the principle of least privilege by ensuring read-only permissions at the top level, with any required write permissions explicitly declared at the run level. |
| Vulnerabilities          | The metric checks the presence of unfixed vulnerabilities of a project or its dependencies in the Open Source Vulnerabilities (OSV) database. |
| bug_blocker               | The number of SonarQube-reported blocker-level bugs. |
| bug_high                  | The number of SonarQube-reported high-severity bugs. |
| bug_medium                | The number of SonarQube-reported medium-severity bugs. |
| bug_low                   | The number of SonarQube-reported low-severity bugs. |
| vulnerability_blocker     | The number of blocker-level security vulnerabilities detected by SonarQube. |
| vulnerability_high        | The number of high-severity security vulnerabilities detected by SonarQube. |
| vulnerability_medium      | The number of medium-severity security vulnerabilities detected by SonarQube. |
| vulnerability_low         | The number of low-severity security vulnerabilities detected by SonarQube. |
| code_smell_blocker        | The number of blocker-level code smells detected by SonarQube. |
| code_smell_high           | The number of high-severity code smells detected by SonarQube. |
| code_smell_medium         | The number of medium-severity code smells detected by SonarQube. |
| code_smell_low            | The number of low-severity code smells detected by SonarQube. |
