from flask import Flask, render_template
from simulate import main

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/infra/main.py')
def my_link():
    print('I got clicked!')
    main.simulate_all()
    return 'Click.'


if __name__ == '__main__':
    app.run(debug=False)
