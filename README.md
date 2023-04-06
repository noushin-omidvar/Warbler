# Warbler - A Twitter Clone
Warbler is a web application built using Flask, a Python web framework, that allows users to create accounts, post messages (limited to 140 characters), follow other users, and view their feeds.

## Installation
1. Clone the repository to your local machine:
```
git clone https://github.com/noushin-omidvar/warbler.git
```
2. Install the required packages:
```
pip install -r requirements.txt
```
3. Create a database:
```
createdb warbler
```
4. Create the tables in the database:
```
python3 seed.py
```
5. Start the server:
```
flask run
```
The server should now be running on http://localhost:5000/.

## Usage
### Creating an account
To create an account, navigate to the registration page (http://localhost:5000/signup) and fill out the form with your information. Once you submit the form, you will be redirected to the home page (http://localhost:5000/) where you can begin using Warbler.

### Posting a message
To post a message, click on the "New Message" button on the home page. You will be redirected to a form where you can enter your message (limited to 140 characters). Once you submit the form, your message will be visible on your profile and the home page.

### Following other users
To follow another user, navigate to their profile and click on the "Follow" button. You will now see their messages on your home page.

### Viewing your feed
To view your feed, navigate to the home page (http://localhost:5000/). You will see a list of messages posted by users that you follow.

### Notes
For more information about the Warbler database schema, please see the `docs/database.md` file.


### Contributing
If you would like to contribute to Warbler, please fork the repository and create a pull request. We welcome all contributions!

### Credits
Warbler was created by Noushin Omidvar as a project for Springboard bootcamp. Special thanks to Renish for his guidance and support.

