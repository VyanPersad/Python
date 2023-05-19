from flask import Flask, render_template

#Render accesses an html file and renders it.

#This instantiates the class object
app = Flask(__name__)


#@app.route('/')
#def home():
#    return "Your content here"
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    return render_template('about.html')


#Python assigns the name main
if __name__ == "__main__":
    app.run(debug=True)
