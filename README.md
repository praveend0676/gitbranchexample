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


* 8adb6c8 (HEAD -> main, origin/main) first commit
* 6e85772 all changes+1
* fd00263 all changes
*   f7d78a9 Resolving 2nd merge conflit
|\  
| * b4d5e18 (feature-dashboard) Update from feature-dashboard brach
* |   692f981 Resolving main.py merge conflicts
|\ \  
| * | 6d279ff (feature-profile) Update from eature-profile branch
| |/  
* / 254d295 (feature-login) Update from feafeature-login branch
|/  
* d7fbef5 Initial Learning platform for git branching
