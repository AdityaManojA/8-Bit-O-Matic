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
    
  

   
    
    num_colors = 16

   
    img = Image.open(file.stream).convert("RGBA")

    
    base_width = 45
    w_percent = (base_width / float(img.size[0]))
    h_size = int((float(img.size[1]) * float(w_percent)))
    small_img = img.resize((base_width, h_size), Image.NEAREST)

   
    quantized_img = small_img.quantize(colors=num_colors)

   
    final_img = quantized_img.resize(img.size, Image.NEAREST)

   
    final_img = final_img.convert("RGBA")
    
   

   
    buffer = io.BytesIO()
    final_img.save(buffer, 'PNG')
    buffer.seek(0)

    
    return send_file(buffer, mimetype='image/png')
