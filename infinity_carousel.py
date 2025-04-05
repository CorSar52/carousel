from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

upload_folder = os.path.join('static', 'img')

app.config['UPLOAD'] = upload_folder
count = 4

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global count
    if request.method == 'POST':
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)
        count += 1
        return render_template('inf_carousel.html', img=img, count=count)
    return render_template('inf_carousel.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)