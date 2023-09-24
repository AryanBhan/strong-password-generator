from flask import Flask, render_template, request
import string
import secrets

app = Flask(__name__)

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    try:
        if request.method == 'POST':
            length = int(request.form.get('length', '12')) 
            password = generate_password(length)
    except Exception:
        length=12
        password = generate_password(length)
    return render_template('index.html', password=password)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True,port=8000)
