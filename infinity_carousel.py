from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

upload_folder = os.path.join('static', 'img')

app.config['UPLOAD'] = upload_folder
my_imgs = [os.path.join(app.config['UPLOAD'], 'second.jpg'), os.path.join(app.config['UPLOAD'], 'third.jpg')]

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global my_imgs
    if request.method == 'POST':
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)
        my_imgs.append(img)
        return render_template('inf_carousel.html', my_imgs=my_imgs)
    return render_template('inf_carousel.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)