from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': "Tom K.",
        'title': 'The Backend day',
        'date_posted': 'April 20, 2020',
    },
    {
        'author': "Tomas G.",
        'title': 'The Frontend Day',
        'date_posted': 'April 19, 2020',
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)