# gitbranchdemo

The goal is:

                         feature-login
                        /
main ------------------+-------------
                        \
                         feature-profile
                          \
                           feature-dashboard


Create Branch ↓ Switch to Branch ↓ Develop Feature ↓ Commit Changes ↓ Switch to main ↓ Merge Feature ↓ Test ↓ Push to GitHub


| Command                 | explanation                                       |
| --------------------------------- | --------------------------------------------------------- |
| `git branch`                      | Lists the branches in the repository.                     |
| `git switch main`                 | Switches to the existing `main` branch.                   |
| `git switch -c feature-login`     | Creates and switches to a new feature branch.             |
| `git checkout -b feature-login`   | Older alternative for creating and switching to a branch. |
| `git merge feature-login`         | Merges the login branch into the current branch.          |
| `git push -u origin main`         | Pushes `main` to GitHub and sets its upstream branch.     |
| `git push --all origin`           | Pushes all local branches to GitHub.                      |
| `git branch -d feature-login`     | Safely deletes the local login branch after merging.      |
| `git log --oneline --graph --all` | Shows the complete commit and branch history visually.    |

# gitbranchexample
