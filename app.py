from flask import Flask, request, render_template
app = Flask(__name__)

//vijdshwd
@app.route('/')
def hello():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
