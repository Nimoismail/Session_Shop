from flask import Flask,session,make_response, request, render_template,redirect,url_for
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'super_secret_key'

PRODUCT = {
    1:{"name": 'Laptop', 'Price': '700'},
    2:{"name": 'Phone', 'Price': '300'},
    3:{"name": 'Headphones', 'Price': '600'},
    4:{"name": 'Mouse', 'Price': '800'},
}

# @app.route('/')
# def home():
#     res = make_response("<h1>This is the response page yu will get</h1>")
#     session['username'] = 'john'
#     return res


@app.route('/')
def index():
    usename = session.get('username')
    last_visit = request.cookie.get("last Visit")

    resp = make_response(render_template('index.html', usename = usename, last_visit = last_visit ))
    resp.set_cookie('last_visit', )


@app.route('/login', methods = ['GET', 'POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == '123':
        session['username'] = username
        session['cart'] = {}
        return redirect(url_for('shop'))
    else:
        return render_template('login.html', error = 'Invalid credentials')
    
    return render_template('login')
    





if __name__ == '__main__':
    app.run(debug=True, port=53000)