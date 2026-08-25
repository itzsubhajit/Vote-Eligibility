Voting Eligibility Checker

A simple Flask web application that checks whether a person is eligible to vote based on their age.

Features

Simple and user-friendly web interface

Accepts the user's age

Checks voting eligibility

Displays the eligibility result

Responsive HTML/CSS design

Built using Flask and Jinja2

Eligibility Rule

A person is eligible to vote if their age is 18 years or older.

Age >= 18  → Eligible to vote
Age < 18   → Not eligible to vote

Technologies Used

Python

Flask

HTML

CSS

Jinja2

Project Structure

VotingProject/
│
├── app.py
│
└── templates/
    └── login.html

Installation

First, install Flask:

pip install flask

Running the Application

Run the Flask application:

python app.py

Then open the following address in your browser:

http://127.0.0.1:5000/

How It Works

The user opens the Voting Eligibility Checker.

The user enters their age.

The form sends the age to the Flask server using a POST request.

Flask retrieves the age using request.form['age'].

The application checks whether the age is 18 or above.

The result is displayed on the webpage.

Example

Eligible

Input:

Age: 20

Result:

You are eligible to vote!

Not Eligible

Input:

Age: 16

Result:

You are not eligible to vote yet.

Future Improvements

Add name and date-of-birth fields

Add better input validation

Add a reset button

Store results in a database

Add additional eligibility conditions

License

This project is created for educational purposes.
