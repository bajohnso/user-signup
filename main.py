from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)
app.config['DEBUG'] = True


def valid_user_pass(userpass):
    if len(userpass) < 3 or len(userpass) > 20:
        return False   
    elif ' ' in userpass:
        return False
    else: 
        return True

def valid_confirm(password, confirm):
    if password == confirm:
        return True
    else:
        return False

def valid_email(address):
    if address == '':
        return True
    if not valid_user_pass(address): 
        return False
    if address.count('@') != 1:
        return False
    if address.count('.') != 1:
        return False
    else:
        return True

@app.route("/", methods=['GET', 'POST'])

def index():
#DISPLAY FORM ON LANDING PAGE--
    if request.method == 'GET':
        return render_template('index.html')

    else:
        u = request.form['username']
        p = request.form['password']
        c = request.form['confirm']
        e = request.form['email']

        u_error = ''
        p_error = ''
        c_error = ''
        e_error = ''

        if not valid_user_pass(request.form['username']):
            u_error = 'Username must have 3-20 characters and no spaces.'
            u = ''

        if not valid_user_pass(p):
            p_error = 'Password must have 3-20 characters and no spaces.'
            p = ''

        if not valid_confirm(p,c):
            c_error = "Password entries don't match."
            c = ''
        
        if not valid_email(e):
            e_error = 'Email address not valid.'
            e = ''

    #IF ALL INPUTS VALID, REDIRECT TO WELCOME PAGE
    if not u_error and not p_error and not c_error and not e_error:
        u = request.form['username']
        return redirect('/welcome?u={0}'.format(u))
    #IF AN INPUT IS INVALID, RETURN FORM WITH ERROR MESSAGES
    else:
        return render_template('index.html', u_error=u_error, p_error=p_error, c_error=c_error, e_error=e_error, username=u, email=e)


@app.route("/welcome")

def valid_inputs():
    u = request.args.get('u')
    return render_template('welcome.html',username=u)


app.run()