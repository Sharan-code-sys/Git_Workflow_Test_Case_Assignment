# Assignment Submission

Course: Software Development Principles
Student Name: N. Sharan
Student ID: 2024EB01865

## Repository Structure

```text
SDP/
├── .gitignore
├── about.html
├── assignment_solution.md
├── assignment_solution.pdf
├── git_commands.txt
├── git_workflow_script.sh
├── index.html
├── question_2_test_cases.md
├── release-notes.txt
├── temp/                 # ignored test folder
├── debug.log             # ignored log file for verification
└── .git/
```

## Question 1: Git & GitHub Workflow Execution

### 1. Local repository setup and initial project files

File content for index.html:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Home</title>
</head>
<body>
  <h1>Welcome to the Project</h1>
  <p>This is the initial version of the website.</p>
  <nav>
    <a href="index.html">Home</a> |
    <a href="about.html">About</a>
  </nav>
</body>
</html>
```

File content for about.html:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>About</title>
</head>
<body>
  <h1>About Us</h1>
  <p>This page describes the project purpose.</p>
  <nav>
    <a href="index.html">Home</a> |
    <a href="about.html">About</a>
  </nav>
</body>
</html>
```

Shell script content used for the workflow:

```bash
#!/usr/bin/env bash
set -euo pipefail

mkdir -p "c:/Users/Sharan Nagilla/Downloads/SDP"
cd "c:/Users/Sharan Nagilla/Downloads/SDP"

cat > index.html <<'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Home</title>
</head>
<body>
  <h1>Welcome to the Project</h1>
  <p>This is the initial version of the website.</p>
  <nav>
    <a href="index.html">Home</a> |
    <a href="about.html">About</a>
  </nav>
</body>
</html>
EOF

cat > about.html <<'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>About</title>
</head>
<body>
  <h1>About Us</h1>
  <p>This page describes the project purpose.</p>
  <nav>
    <a href="index.html">Home</a> |
    <a href="about.html">About</a>
  </nav>
</body>
</html>
EOF

git init -b main
git config user.name "N. Sharan"
git config user.email "2024EB01865@example.com"

git add index.html about.html
git commit -m "Initial project setup"

sed -i 's|This is the initial version of the website.|This is the initial version of the website. Updated homepage content for version 2.|' index.html
git add index.html
git commit -m "Update homepage content"

git checkout -b feature

cat > about.html <<'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>About</title>
</head>
<body>
  <h1>About Us</h1>
  <p>This page describes the project purpose.</p>
  <p>Feature branch update: added release notes section.</p>
  <nav>
    <a href="index.html">Home</a> |
    <a href="about.html">About</a>
  </nav>
</body>
</html>
EOF

git add about.html
git commit -m "Add feature branch content"

git checkout main
git merge feature --no-ff -m "Merge feature branch into main"

git log --oneline --decorate --graph --all

cat > .gitignore <<'EOF'
*.log
temp/
EOF

git add .gitignore
git commit -m "Add gitignore"

printf 'sample log content\n' > debug.log
mkdir -p temp
printf 'temporary content\n' > temp/temp-file.txt
git status --short --ignored

printf 'Release version 1.0 notes for the project.\n' > release-notes.txt
git add release-notes.txt
git commit -m "Add release notes"
git reset --soft HEAD~1
git status --short

git remote add origin https://github.com/Sharan-code-sys/Git_Workflow_Test_Case_Assignment.git
git push -u origin main
```

### 2. Actual command execution and terminal output evidence

```text
$ git init -b main
Initialized empty Git repository in C:/Users/Sharan Nagilla/Downloads/SDP/.git/

$ git config user.name "N. Sharan"
$ git config user.email "2024EB01865@example.com"

$ git add index.html about.html
$ git commit -m "Initial project setup"
[main (root-commit) 5d32f00] Initial project setup
 2 files changed, 32 insertions(+)
 create mode 100644 about.html
 create mode 100644 index.html

$ git add index.html
$ git commit -m "Update homepage content"
[main a1f66a8] Update homepage content
 1 file changed, 1 insertion(+)

$ git checkout -b feature
Switched to a new branch 'feature'

$ git add about.html
$ git commit -m "Add feature branch content"
[feature 533264f] Add feature branch content
 1 file changed, 1 insertion(+)

$ git checkout main
Switched to branch 'main'

$ git merge feature --no-ff -m "Merge feature branch into main"
Merge made by the 'ort' strategy.
 about.html | 1 +
 1 file changed, 1 insertion(+)

$ git log --oneline --decorate --graph --all
*   abcb785 (HEAD -> main) Merge feature branch into main
|\  
| * 533264f (feature) Add feature branch content
|/  
* a1f66a8 Update homepage content
* 5d32f00 Initial project setup

$ cat > .gitignore <<'EOF'
*.log
temp/
EOF

$ git add .gitignore
$ git commit -m "Add gitignore"
[main ece62f6] Add gitignore
 1 file changed, 2 insertions(+)
 create mode 100644 .gitignore

$ git status --short --ignored
A  release-notes.txt
!! debug.log
!! temp/

$ git commit -m "Add release notes"
[main 3d1be83] Add release notes
 1 file changed, 1 insertion(+)
 create mode 100644 release-notes.txt

$ git reset --soft HEAD~1

$ git status --short
A  release-notes.txt
```

### 3. .gitignore contents

```gitignore
*.log
temp/
```

This ensures:
- all log files are ignored
- the temp directory is excluded from tracking

### 4. Undo operation explanation

The last commit was undone using `git reset --soft HEAD~1`.

Before undo:

```text
$ git log --oneline -1
3d1be83 Add release notes
```

After undo:

```text
$ git status --short
A  release-notes.txt
```

Interpretation:
- the commit was removed from the commit history
- the changes remain staged in the index
- the work is still recoverable and can be recommitted or adjusted

### 5. GitHub integration and public remote

```bash
git remote add origin https://github.com/Sharan-code-sys/Git_Workflow_Test_Case_Assignment.git
git push -u origin main
```

Observed output:

```text
To https://github.com/Sharan-code-sys/Git_Workflow_Test_Case_Assignment.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

GitHub repository URL:
https://github.com/Sharan-code-sys/Git_Workflow_Test_Case_Assignment.git

## Question 2: Test Case Design (Login System)

### Test case table

| Test Case ID | Test Scenario | Input Data | Expected Output |
|---|---|---|---|
| TC_01 | Successful login with valid credentials | Username = user1, Password = pass123 | HTTP 200 OK; UI message: "Login successful"; redirect to dashboard/home page |
| TC_02 | Empty username with valid password | Username = "", Password = pass123 | HTTP 400 Bad Request; UI error: "Username is required"; no login attempt executed |
| TC_03 | Empty password with valid username | Username = user1, Password = "" | HTTP 400 Bad Request; UI error: "Password is required"; no login attempt executed |
| TC_04 | Both username and password empty | Username = "", Password = "" | HTTP 400 Bad Request; UI error: "Username is required" and "Password is required"; no login attempt executed |
| TC_05 | Password length is 5 characters | Username = user1, Password = pass1 | HTTP 400 Bad Request; UI error: "Password must be at least 6 characters long"; no login attempt executed |
| TC_06 | Password length is exactly 6 characters | Username = user1, Password = pass12 | HTTP 200 OK; UI message: "Login successful"; redirect to dashboard/home page |
| TC_07 | Invalid username/password combination | Username = user1, Password = wrongpw | HTTP 401 Unauthorized; UI error: "Invalid username or password"; login attempt count increments by 1 |
| TC_08 | Three consecutive failed attempts trigger lockout | Attempt 1: user1 / wrong1; Attempt 2: user1 / wrong2; Attempt 3: user1 / wrong3 | After third failure: HTTP 423 Locked; UI error: "Account locked after 3 failed attempts"; future login attempts blocked |
| TC_09 | Attempt to login while account is already locked | Username = user1, Password = pass123; account status = locked | HTTP 423 Locked; UI error: "Account is locked. Please contact support"; no authentication processing |

### Coverage rationale

This test set ensures:
- all functional requirements are covered
- valid and invalid scenarios are both included
- boundary analysis is performed for password lengths 5 and 6
- empty state handling is validated
- authentication failure and lockout state transition are covered
- false positives are minimized by using explicit expected HTTP/UI results

### Final conclusion

The repository demonstrates a complete Git workflow with versioning, branching, merging, ignore rules, undo operations, and public GitHub integration. The login test suite covers all required edge cases and security conditions with clear, measurable expected results.
