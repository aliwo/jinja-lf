from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def homePage():

    pageType = 'Controller'
    btn1 = False

    if request.method == 'POST':
        if request.form['lamp'] == 'on':
            btn1 = True
        elif request.form['lamp'] == 'off':
            btn1 = False

    return render_template("index.html", pageType = pageType, btn1 = btn1)

@app.route('/rainbow', methods = ['GET', 'POST'])
def make_rainbow():
    return render_template('for_textcolor.html')


if __name__ == "__main__":
    app.debug = True
    app.run()