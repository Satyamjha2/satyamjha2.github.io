from flask import Flask, render_template, url_for, request
from randomwalk import polar
from random import randint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config[''] = ''

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    polar.gen_polar_picture(randint(10,30), randint(2,5))
    return render_template('index.html')

def redirect_url(default='home'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

if __name__ == '__main__':
    app.run(debug=True)