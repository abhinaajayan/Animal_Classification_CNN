import numpy as np
import cv2
import os
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from keras.layers import Dense

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Fix for quantization_config issue
class FixedDense(Dense):
    def __init__(self, *args, **kwargs):
        kwargs.pop("quantization_config", None)
        super().__init__(*args, **kwargs)

# Load model
model = load_model(
    "lion_tiger.keras",
    custom_objects={"Dense": FixedDense},
    compile=False
)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predict_image(img_path):
    img = cv2.imread(img_path)
    if img is None:
        return None, None
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (256, 256))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    yhat = model.predict(img)
    confidence = float(yhat[0][0])
    if confidence > 0.5:
        label = "Lion"
        prob = confidence
    else:
        label = "Cheetah"
        prob = 1 - confidence
    return label, round(prob * 100, 2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        label, confidence = predict_image(filepath)
        if label is None:
            return jsonify({'error': 'Could not process image'}), 500
        return jsonify({
            'prediction': label,
            'confidence': confidence,
            'image_url': f'/static/uploads/{filename}'
        })
    return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0")