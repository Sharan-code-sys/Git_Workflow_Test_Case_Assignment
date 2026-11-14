# Assignment Solution

## Question 1: Git & GitHub Workflow

### Local repository setup
- Project folder created locally.
- Files created: `index.html`, `about.html`.
- Git repository initialized with `git init -b main`.

### Workflow performed
1. Initial project state committed: `Initial project setup`
2. Homepage updated and second commit created: `Update homepage content`
3. Branch created: `feature`
4. Switched to the feature branch and modified content
5. Feature commit created: `Add feature branch content`
6. Switched back to `main`
7. Merged feature into main with a merge commit: `Merge feature branch into main`
8. Full branch history was checked using `git log --oneline --decorate --graph --all`

### .gitignore
The repository includes a `.gitignore` file with the following rules:
- `*.log`
- `temp/`

### Undo operation using Git
- An additional commit was created: `Add release notes`
- The last commit was undone using `git reset --soft HEAD~1`
- The effect was that the changes stayed staged, and `git status` showed the file as added but not committed.

### GitHub integration
- Remote URL configured: `https://github.com/yourusername/sdp-assignment.git`
- This should be replaced with the actual public GitHub repository URL after creating the public repository.

### Git command documentation
See the file `git_commands.txt` for the full list of commands and one-line explanations.

## Question 2: Test Case Design

| Test Case ID | Test Scenario | Input Data | Expected Output |
|---|---|---|---|
| TC_01 | Valid login with correct username and password | Username = user1, Password = pass123 | Login successful |
| TC_02 | Empty username | Username = "" , Password = pass123 | Error message: Username is required |
| TC_03 | Empty password | Username = user1, Password = "" | Error message: Password is required |
| TC_04 | Password shorter than 6 characters | Username = user1, Password = abc12 | Error message: Password must be at least 6 characters long |
| TC_05 | Password length exactly 6 characters | Username = user1, Password = pass12 | Login successful |
| TC_06 | Invalid credentials | Username = user1, Password = wrongpw | Error message: Invalid username or password |
| TC_07 | Locked account after 3 failed login attempts | Attempt 1: Username = user1, Password = wrong1; Attempt 2: Username = user1, Password = wrong2; Attempt 3: Username = user1, Password = wrong3 | After the third failed attempt, the account is locked and a lock message is shown |

These test cases cover all functional requirements, including valid and invalid scenarios and required edge cases.
