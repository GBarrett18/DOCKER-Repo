from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
  return 'Index Page'

@app.route(/hello)
def hello():
  return 'Hello World'

@app.route('/login',methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    do_the_login()
    else:
      show_the_login_form()

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
