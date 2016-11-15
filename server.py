from flask import Flask,  render_template,request,redirect,session,flash
import re
app = Flask(__name__)
app.secret_key = 'secret'
email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
name_regex = re.compile(r'^[a-zA-Z]+$')
password_regex = re.compile(r'^(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
birthdate_regex = re.compile(r'((?:0[1-9])|(?:1[0-2]))\/((?:0[0-9])|(?:[1-2][0-9])|(?:3[0-1]))\/(\d{4})')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if len(request.form['email']) < 1:
        flash("All fields are required and must not be blank", 'Email')
    elif len(request.form['first_name']) <1:
        flash("All fields are required and must not be blank", 'First Name')
    elif len(request.form['last_name']) < 1:
        flash("All fields are required and must not be blank", 'Last Name')
    elif len(request.form['birth_date']) <1:
        flash("All fields are required and must not be blank", 'Birth Date')
    elif len(request.form['password']) < 1:
        flash("All fields are required and must not be blank", 'Password')
    elif len(request.form['confirm_password']) < 1:
        flash("All fields are required and must not be blank", 'Confirm Password')
    elif not name_regex.match(request.form['first_name']):
        flash('First Name cannot contain any numbers!','Must contain only letters!')
    elif not name_regex.match(request.form['last_name']):
        flash('Last Name cannot contain any numbers!','Must contain only letters!')
    elif not email_regex.match(request.form['email']):
        flash('Email should be a valid email!','error:EMAIL')
    elif not password_regex.match(request.form['password']):
        flash('Password should be more than 8 characters','should contain at least 1 uppercase letter and 1 numeric value!')
    elif request.form['password'] != request.form['confirm_password']:
        flash('Password and Password Confirmation do not match!','error:MISMATCH')
    elif not birthdate_regex.match(request.form['birthdate']):
        flash('Birth-date field must be validated as a valid date!','error:DATE')
    else:
        flash('Success!')
    return redirect('/')

app.run(debug=True)
