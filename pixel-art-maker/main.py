from flask import Flask, request, send_file, render_template
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pixelate', methods=['POST'])
def pixelate_image():
    if 'image' not in request.files:
        return 'No image file found', 400

    file = request.files['image']
    
    pixel_size = 25

    img = Image.open(file.stream).convert("RGBA")

    small_width = img.width // pixel_size
    small_height = img.height // pixel_size
    
    if small_width == 0: small_width = 1
    if small_height == 0: small_height = 1

    small_img = img.resize((small_width, small_height), Image.NEAREST)

    bw_img = small_img.convert('L')
    threshold = 128
    threshold_img = bw_img.point(lambda p: 255 if p > threshold else 0, '1')

    final_img = threshold_img.resize(img.size, Image.NEAREST)
    
    final_img = final_img.convert("RGBA")

    buffer = io.BytesIO()
    final_img.save(buffer, 'PNG')
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png')
