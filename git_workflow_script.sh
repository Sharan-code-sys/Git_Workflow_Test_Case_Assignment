#!/usr/bin/env bash
set -euo pipefail

cd "C:/Users/Sharan Nagilla/Downloads/SDP"

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

python - <<'PY'
from pathlib import Path
p = Path('index.html')
text = p.read_text(encoding='utf-8')
text = text.replace('This is the initial version of the website.', 'This is the initial version of the website. Updated homepage content for version 2.')
p.write_text(text, encoding='utf-8')
PY

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
