# Question 2: Test Case Design for Login System

Course: Software Development Principles
Student Name: N. Sharan
Student ID: 2024EB01865

## Test Case Matrix

| Test Case ID | Test Scenario | Input Data | Expected Output |
|---|---|---|---|
| TC_01 | Successful login with valid credentials | Username = user1, Password = pass123 | HTTP 200 OK; UI message: "Login successful"; redirect to dashboard/home page |
| TC_02 | Empty username with valid password | Username = "" , Password = pass123 | HTTP 400 Bad Request; UI error: "Username is required"; no login attempt executed |
| TC_03 | Empty password with valid username | Username = user1, Password = "" | HTTP 400 Bad Request; UI error: "Password is required"; no login attempt executed |
| TC_04 | Both username and password empty | Username = "", Password = "" | HTTP 400 Bad Request; UI error: "Username is required" and "Password is required"; no login attempt executed |
| TC_05 | Password length is 5 characters | Username = user1, Password = pass1 | HTTP 400 Bad Request; UI error: "Password must be at least 6 characters long"; no login attempt executed |
| TC_06 | Password length is exactly 6 characters | Username = user1, Password = pass12 | HTTP 200 OK; UI message: "Login successful"; redirect to dashboard/home page |
| TC_07 | Invalid username/password combination | Username = user1, Password = wrongpw | HTTP 401 Unauthorized; UI error: "Invalid username or password"; login attempt count increments by 1 |
| TC_08 | Three consecutive failed attempts trigger lockout | Attempt 1: user1 / wrong1; Attempt 2: user1 / wrong2; Attempt 3: user1 / wrong3 | After third failure: HTTP 423 Locked; UI error: "Account locked after 3 failed attempts"; future login attempts blocked |
| TC_09 | Attempt to login while account is already locked | Username = user1, Password = pass123; account status = locked | HTTP 423 Locked; UI error: "Account is locked. Please contact support"; no authentication processing |

## Boundary and Equivalence Coverage Summary

- Valid credentials partition: TC_01, TC_06
- Empty username partition: TC_02, TC_04
- Empty password partition: TC_03, TC_04
- Password length below minimum: TC_05
- Password length equal to minimum threshold: TC_06
- Authentication failure partition: TC_07
- Lockout state transition: TC_08
- Locked-state validation: TC_09

## Expected System Behavior

1. Username validation: reject empty username before performing credential lookup.
2. Password validation: enforce minimum length of 6 characters.
3. Successful authentication: only valid username and password combination allows login.
4. Failed authentication: invalid credentials return an explicit error message and counter increments.
5. Lockout rule: after exactly three consecutive failed attempts, the account enters a locked state.
6. Locked state enforcement: any additional attempt is denied until the account is reset or unlocked by an administrator.
