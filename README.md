
# QA54_iCarro_SergeyPatrashok

Automated test for successful login on the iCarro website.

## Website
https://icarro-v1.netlify.app/

## Technologies
- Python
- Selenium
- Pytest

## Test Description
The test checks successful user authorization:
1. Opens the login page.
2. Enters a registered user's email and password.
3. Clicks the login button.
4. Confirms successful login.
5. Verifies that the "Log out" button is displayed.

## How to Run
Install the required libraries:

pip install -r requirements.txt

Create a credentials.py file in the project folder:

EMAIL = "your_email"
PASSWORD = "your_password"

Run the test:

pytest test_login.py -v

## Security
The credentials.py file is excluded from Git using .gitignore.
