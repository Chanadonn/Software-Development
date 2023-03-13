from flask import Flask, render_template, request
from flask import Flask, render_template, request, redirect, session

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_authenticated(self, username, password):
        return username == self.username and password == self.password

    def __repr__(self):
        return f'<User {self.username}>'

# Create some users
users = [User('user1', 'password1'), User('user2', 'password2')]

# Route for home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Check if the user is in the list of users
        user = None
        for u in users:
            if u.is_authenticated(username, password):
                user = u
                break

        # If the user is authenticated, redirect to the avatar page
        if user is not None:
            return render_template('avatar.html', user=user)

        # Otherwise, show an error message
        error = 'Invalid username or password'
        return render_template('login.html', error=error)

    # If it's a GET request, show the login page
    return render_template('login.html')

# Route for avatar page
@app.route('/avatar')
def avatar():
    # Get the user from the query string
    username = request.args.get('user')

    # If the user is not provided or not in the list of users, redirect to the login page
    user = None
    for u in users:
        if u.username == username:
            user = u
            break
    if user is None:
        return redirect('/login')

    # Get the path to the user's avatar image
    avatar_path = os.path.join('static', 'avatars', f'{username}.png')

    # Render the avatar page with the user's avatar image
    return render_template('avatar.html', user=user, avatar_path=avatar_path)

if __name__ == '__main__':
    app.run(debug=True)
