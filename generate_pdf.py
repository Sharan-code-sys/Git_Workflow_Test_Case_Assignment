from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


def build_pdf(output_path):
    doc = SimpleDocTemplate(output_path, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('Title2', parent=styles['Title'], fontSize=18, leading=24, alignment=1)
    heading_style = ParagraphStyle('Heading2', parent=styles['Heading2'], fontSize=13, leading=18, spaceBefore=12, spaceAfter=8)
    body_style = ParagraphStyle('Body', parent=styles['BodyText'], fontSize=10, leading=14)
    bullet_style = ParagraphStyle('Bullet', parent=styles['BodyText'], fontSize=10, leading=14, leftIndent=18)

    story = []
    story.append(Paragraph('Assignment Solution', title_style))
    story.append(Spacer(1, 0.25 * inch))

    story.append(Paragraph('Question 1: Git & GitHub Workflow', heading_style))
    story.append(Paragraph('Local repository setup: project folder created locally; index.html and about.html created; Git repository initialized with git init -b main.', body_style))
    story.append(Paragraph('Workflow performed:', body_style))
    workflow = [
        '1. Initial project state committed: Initial project setup',
        '2. Homepage updated and second commit created: Update homepage content',
        '3. Feature branch created and checked out: feature',
        '4. Feature branch changes committed: Add feature branch content',
        '5. Switched back to main and merged feature with: Merge feature branch into main',
        '6. Repository history checked using git log --oneline --decorate --graph --all',
        '7. .gitignore created with *.log and temp/ entries',
        '8. Additional commit created, then undone with git reset --soft HEAD~1',
    ]
    for item in workflow:
        story.append(Paragraph(item, bullet_style))
    story.append(Paragraph('GitHub integration: remote configured as https://github.com/yourusername/sdp-assignment.git. This is the required repository URL placeholder for the public GitHub repository.', body_style))
    story.append(Paragraph('Git command documentation: see git_commands.txt for all commands and one-line explanations.', body_style))

    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph('Question 2: Test Case Design for Login System', heading_style))

    data = [
        ['Test Case ID', 'Test Scenario', 'Input Data', 'Expected Output'],
        ['TC_01', 'Valid login with correct username and password', 'Username = user1, Password = pass123', 'Login successful'],
        ['TC_02', 'Empty username', 'Username = "" , Password = pass123', 'Error message: Username is required'],
        ['TC_03', 'Empty password', 'Username = user1, Password = ""', 'Error message: Password is required'],
        ['TC_04', 'Password shorter than 6 characters', 'Username = user1, Password = abc12', 'Error message: Password must be at least 6 characters long'],
        ['TC_05', 'Password length exactly 6 characters', 'Username = user1, Password = pass12', 'Login successful'],
        ['TC_06', 'Invalid credentials', 'Username = user1, Password = wrongpw', 'Error message: Invalid username or password'],
        ['TC_07', 'Locked account after 3 failed login attempts', 'Attempt 1: wrong1; Attempt 2: wrong2; Attempt 3: wrong3', 'After the third failed attempt, the account is locked and a lock message is shown'],
    ]
    table = Table(data, colWidths=[70, 150, 160, 150])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#D9E2F3')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.white]),
    ]))
    story.append(table)

    story.append(Spacer(1, 0.25 * inch))
    story.append(Paragraph('Coverage summary: valid and invalid login attempts are included, and edge cases for empty username, empty password, password shorter than 6, and password length equal to 6 are covered.', body_style))

    doc.build(story)

if __name__ == '__main__':
    build_pdf('assignment_solution.pdf')
    print('PDF created: assignment_solution.pdf')
