Feature: Login to the project 
    Scenario: 
        The user should be able to login into the social networking site if the username and the password are correct.
The user should be shown the error message if the username and the password are incorrect.
The user should be navigated to the home page, if the username and password are correct.
Example: 
def login():
email = input(“Enter email: “)
 pwd = input(“Enter password: “)
    
    if email == stored_email and pwd == stored_pwd:
         print(“Logged in Successfully!”)
     else:
         print(“Login failed!”)
