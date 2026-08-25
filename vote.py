from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def voting():
    message = ''

    if request.method == 'POST':
        age = int(request.form['age'])

        if age >= 18:
            message = 'You are eligible to vote!'
        else:
            message = 'You are not eligible to vote yet.'

    return render_template('login.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)