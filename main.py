from flask import Flask, request, redirect, render_template
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def validate():
    username = request.form["username"]
    username_error =""

    if " " in username:
        username_error= "Spaces are not allowed"
    elif len(username)<3 or len(username)>20:
        username_error ="Name must be in between 3-20 characters long"
    else:
        username_error= ""

    #for password
    password=request.form["password"]
    password_error = ""

    if " " in password:
        password_error = "Spaces are not allowed"
    elif len(password)<3 or len(password)>20:
        password_error ="Password must be 3-20 characters long"
    else:
        password_error =""

    #email
    email =request.form["email"]
    email_error=""

    if email !="":
        if "@" not in email or "." not in email:
            email_error = "Must be valid email"
        elif len(email)<3 or len(email)>20:
            email_error ="Email must be 3 to 20 characters long"
        else:
            email_error=""

    #verification
    verify = request.form["verify"]
    verify_error =""

    if password != verify:
        verify_error="Passwords are not matching, try again"
    else:
        verify_error=""

    if not username_error and not verify_error and not password_error and not email_error:
        return render_template("welcome.html", username = username)
    else:
        return render_template ("index.html", username = username, username_error = username_error, password_error = password_error, verify_error = verify_error, email = email, email_error = email_error)

@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template("welcome.html", username = username)

    

if __name__ == "__main__":
    app.run()