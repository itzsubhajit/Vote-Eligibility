Voting Eligibility Checker

A simple web-based voting eligibility checker built with Python and Flask.

The application allows a user to enter their age and checks whether they meet the minimum age requirement of 18 years.

✨ Features

Clean and simple user interface

Age-based voting eligibility check

Instant result displayed on the webpage

Responsive HTML and CSS design

Flask backend with Jinja2 templating

Basic form validation

🛠️ Technologies Used

Technology

Purpose

Python

Backend programming

Flask

Web framework

HTML

Webpage structure

CSS

Webpage styling

Jinja2

Dynamic result display

📁 Project Structure

VotingProject/
│
├── app.py
│
└── templates/
    └── login.html

🚀 Getting Started

1. Install Flask

Install Flask using pip:

pip install flask

2. Run the Application

Run the Python file:

python app.py

3. Use the Application

After starting the application, open it through the address provided by Flask and use the voting eligibility form.

⚙️ How It Works

The user enters their age.

The form sends the entered age to the Flask backend.

Flask reads the submitted age.

The application checks whether the age is 18 or above.

The appropriate eligibility message is displayed on the webpage.

Eligibility Logic

if age >= 18:
    message = "You are eligible to vote!"
else:
    message = "You are not eligible to vote yet."

📌 Example

Age

Result

20

Eligible to vote

18

Eligible to vote

16

Not eligible to vote

12

Not eligible to vote

🔮 Future Improvements

Add name and date of birth

Improve validation and error handling

Add a reset option

Store results using a database

Add additional eligibility checks

🎓 Purpose

This project is intended as a beginner-level Flask project for learning how HTML forms communicate with a Python Flask backend and how server-side results can be displayed using Jinja2.

📄 License

This project is created for educational purposes.
