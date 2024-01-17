from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np
 
app = Flask(__name__)
 
upload_folder = os.path.join('static', 'uploads')
 
app.config['UPLOAD'] = upload_folder
 
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)

        img = cv2.imread(img)
        imgWidth = np.size(img,1)
        imgHeight = np.size(img,0)
        #If you only use / for division you get a floating point, // gives a rounded down value
        mid = imgWidth//2
        midLinePixels = []
        grayLinePixels = []

        for px in range(imgHeight):
            midLinePixel = img[px, mid]
            midLinePixels.append(midLinePixel)

        for px in range(len(midLinePixels)):
            grayLinePixels.append(int(sum(midLinePixels[px])//3))

        minPxVal = np.argmin(grayLinePixels)
        maxPxVal = np.argmax(grayLinePixels)

        window_size = 3
        center = (mid, float(minPxVal))
        region = cv2.getRectSubPix(img, (window_size, window_size), center)
        resize = cv2.resize(region,(400,400),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('static/processedImg.png',resize)

        return render_template('index.html', img_path='processedImg.png')
    
    return render_template('index.html')
 
 
if __name__ == '__main__':
    app.run(debug=True, port=5000)