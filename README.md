# 🦁 WildLens — AI Species Classifier

An elegant, AI-powered web application that identifies lions and cheetahs from image uploads using deep learning technology.

---

## 📋 Overview

**WildLens** is a Flask-based web application that leverages a pre-trained TensorFlow/Keras neural network model to classify wildlife images. The application provides users with an intuitive, immersive interface to upload images and receive instant predictions with confidence scores.

Whether you're a wildlife enthusiast, educator, or researcher, WildLens makes AI-powered species identification accessible and engaging.

---

## ✨ Features

- **🎨 Stunning UI**: Savanna-themed interface with animated backgrounds, starry skies, and swaying trees
- **📤 Drag-and-Drop Upload**: Intuitive image upload with drag-and-drop support
- **⚡ Real-Time Predictions**: Instant species classification with confidence scores
- **🔒 Secure File Handling**: Restricted file types (PNG, JPG, JPEG, GIF, WebP) and size limits
- **📱 Responsive Design**: Fully responsive layout that works on desktop and mobile devices
- **🌐 RESTful API**: JSON-based API for programmatic access
- **♿ Accessible**: Clean, accessible markup with proper semantic HTML

---

## 🏗️ Project Structure

```
lion_tiger_/
├── app.py                  # Flask application with ML prediction logic
├── lion_tiger.keras        # Pre-trained Keras model
├── README.md              # This file
├── static/
│   └── uploads/           # Directory for uploaded images
└── templates/
    └── index.html         # Frontend UI
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone or download the repository**
   ```bash
   cd lion_tiger_
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```
   - **Windows**: `venv\Scripts\activate`
   - **macOS/Linux**: `source venv/bin/activate`

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Required packages:
   - Flask
   - TensorFlow/Keras
   - OpenCV (cv2)
   - NumPy
   - Werkzeug

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

---

## 📖 Usage

### Web Interface

1. **Upload an Image**
   - Drag and drop an image onto the drop zone, or
   - Click to browse and select an image

2. **Supported Formats**
   - PNG, JPG, JPEG, GIF, WebP
   - Maximum file size: 16 MB

3. **View Results**
   - The model will classify the animal as **Lion** or **Cheetah**
   - Confidence percentage is displayed (0-100%)

### API Endpoint

**POST** `/predict`

**Request:**
```bash
curl -X POST -F "file=@image.jpg" http://localhost:5000/predict
```

**Response (Success):**
```json
{
  "prediction": "Lion",
  "confidence": 87.5,
  "image_url": "/static/uploads/image.jpg"
}
```

**Response (Error):**
```json
{
  "error": "Invalid file type"
}
```

---

## 🔧 Technical Details

### Model Architecture

- **Model Type**: Convolutional Neural Network (CNN)
- **Framework**: TensorFlow/Keras
- **Input Size**: 256×256 pixels (RGB)
- **Output**: Binary classification (Lion vs. Cheetah)
- **Confidence Threshold**: 0.5

### Image Processing Pipeline

1. Read image using OpenCV
2. Convert BGR to RGB color space
3. Resize to 256×256 pixels
4. Normalize pixel values (0-1 range)
5. Add batch dimension
6. Pass through neural network for prediction

### Confidence Calculation

- **Prediction ≥ 0.5**: Lion (confidence = prediction value)
- **Prediction < 0.5**: Cheetah (confidence = 1 - prediction value)

### Custom Layer Handling

The application includes a custom `FixedDense` layer to handle quantization configuration compatibility issues during model loading.

---

## 🛡️ Security Features

- **File Validation**: Only allowed image extensions are processed
- **File Size Limit**: 16 MB maximum upload size
- **Secure Filenames**: Uses `secure_filename()` to prevent directory traversal attacks
- **Sandboxed Uploads**: Files are stored in a dedicated `static/uploads/` directory

---

## 🎨 UI/UX Highlights

### Design Elements
- **Color Palette**: Gold (#c8973a), Amber (#e8b86d), Dark (#0d0b07)
- **Typography**: Playfair Display (headers), DM Sans (body)
- **Animations**: Pulsing glow, twinkling stars, swaying trees, floating icons
- **Effects**: Glassmorphism panels, smooth transitions, interactive hover states

### Responsive Features
- Mobile-first responsive design
- Clamp font sizing for fluid typography
- Flexible layouts with CSS Grid and Flexbox

---

## 🔍 Configuration

### Flask Configuration (app.py)

```python
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Upload directory
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max file size (16MB)
```

Modify these values to adjust upload behavior.

---

## 🐛 Troubleshooting

### Model Loading Errors
**Issue**: `quantization_config` error when loading model
**Solution**: The application includes a custom `FixedDense` layer to handle this automatically.

### File Upload Failures
- Ensure the file is in a supported format (PNG, JPG, JPEG, GIF, WebP)
- Check that the file size is under 16 MB
- Verify the `static/uploads/` directory has write permissions

### Port Already in Use
- Change the port in `app.py`: `app.run(host="0.0.0.0", port=5001)`

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| Flask | Web framework |
| TensorFlow/Keras | Deep learning model |
| OpenCV (cv2) | Image processing |
| NumPy | Numerical computing |
| Werkzeug | WSGI utilities |

---

## 🚢 Deployment

### Development Server
```bash
python app.py
```

### Production Deployment

For production environments, use a production WSGI server:

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## 📝 License

This project is provided as-is for educational and research purposes.

---

## 🤝 Contributing

Improvements and contributions are welcome! Consider:
- Expanding to classify additional animal species
- Improving model accuracy with additional training data
- Enhancing the UI with additional features
- Adding batch upload capabilities

---

## 📞 Support

For issues, questions, or suggestions, please review the troubleshooting section or check the code comments for more details.

---

## 🌍 About the Model

The `lion_tiger.keras` model is a trained convolutional neural network designed to distinguish between:
- **Lions**: Large felids with distinctive manes
- **Cheetahs**: Slender, swift predators with spotted patterns

The model achieves reliable classification on diverse image conditions and lighting scenarios.

---

**Last Updated**: March 2026  
**Version**: 1.0.0
