from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

form='''
<html>
    <head>
        <!-- Header -->
    </head>

    <body>

        <!-- USERNAME INPUT -->
        <form action = '' method = 'post'>
            <label for = 'user'> Username: </label>
            <input id = 'user' type = 'text' name = 'username' />
            <input type = 'submit'/>
        <form> 
        
        <br><br>
        
        <!-- PASSWORD INPUT -->
        <form action = '' method = 'post'>
            <label for = 'password'> Password: </label>
            <input id = "password" type = 'password' name = 'password'/>
            <input type = 'submit'/>
        </form>

        <br>

        <!-- VALIDATE PASSWORD -->
        <form action = '' method = 'post'>
            <label for = 'validate'> Re-enter password: </label>
            <input id = 'validate' type = 'password' name = 'validate_password'/>
            <input type = 'submit'/>
        </form>

        <br>

        <!-- EMAIL INPUT -->
        <form action = '' method = 'post'>
            <label for = 'email'> Email *(optional): </label>
            <input id = 'email' type = 'text' name = 'email'/>
            <input type = 'submit'/>
        </form>

    </body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return form