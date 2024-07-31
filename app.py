from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    photos = [
        {'url': '/static/fotobangunan.png', 'alt': 'Photo 1'},
        {'url': '/static/images/photo2.jpg', 'alt': 'Photo 2'},
        {'url': '/static/images/photo3.jpg', 'alt': 'Photo 3'}
    ]
    return render_template('index.html', photos=photos)

if __name__ == '__main__':
    app.run(debug=True)
