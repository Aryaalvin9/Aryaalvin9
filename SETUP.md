# Installation

1. Ensure the public profile repository is named exactly `Aryaalvin9` under account `Aryaalvin9` and its default branch is `main`.
2. Upload `README.md`, `scripts/update_activity.py`, and `.github/workflows/profile.yml` preserving their directory paths.
3. Under Settings → Actions → General → Workflow permissions, select Read and write permissions.
4. Open Actions → Refresh GitHub profile → Run workflow on `main`.
5. Verify both `activity` and `snake` jobs succeed, and an `output` branch exists.
6. Refresh your profile. GitHub stats and activity graph depend on third-party providers and can temporarily fail independently of your workflow.

The active repositories section shows the latest pushed *public* repositories (not necessarily projects currently in development). It excludes forks, archived repos, and the profile repository. Private repository activity is not displayed.

If your actual GitHub login or profile repository differs from `Aryaalvin9`, update the username in README, workflow, and the Python script before running.
