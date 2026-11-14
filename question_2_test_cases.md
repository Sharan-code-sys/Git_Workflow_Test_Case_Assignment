# Question 2: Test Case Design for Login System

| Test Case ID | Test Scenario | Input Data | Expected Output |
|---|---|---|---|
| TC_01 | Valid login with correct username and password | Username = user1, Password = pass123 | Login successful |
| TC_02 | Empty username | Username = "" , Password = pass123 | Error message: Username is required |
| TC_03 | Empty password | Username = user1, Password = "" | Error message: Password is required |
| TC_04 | Password shorter than 6 characters | Username = user1, Password = abc12 | Error message: Password must be at least 6 characters long |
| TC_05 | Password length exactly 6 characters | Username = user1, Password = pass12 | Login successful |
| TC_06 | Invalid credentials | Username = user1, Password = wrongpw | Error message: Invalid username or password |
| TC_07 | Locked account after 3 failed login attempts | Attempt 1: Username = user1, Password = wrong1; Attempt 2: Username = user1, Password = wrong2; Attempt 3: Username = user1, Password = wrong3 | After the third failed attempt, the account is locked and a lock message is shown |

## Coverage Summary
- Valid and invalid login attempts are included.
- Required edge cases are covered: empty username, empty password, password shorter than 6, password exactly 6 characters.
- Failed attempts are tested to confirm the account-lock rule after three consecutive failed attempts.
