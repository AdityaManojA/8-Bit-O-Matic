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
    
    mode = request.form.get('mode', 'color')
    
    try:
        img = Image.open(file.stream)

        
        if mode == 'bw':
           
            img = img.convert('L')
        else:
           
            img = img.convert('RGB')

       
        base_width = 45
        w_percent = (base_width / float(img.size[0]))
        h_size = int((float(img.size[1]) * float(w_percent)))
        small_img = img.resize((base_width, h_size), Image.NEAREST)

        
        if mode == 'color':
            quantized_img = small_img.quantize(colors=16)
        else:
            
            quantized_img = small_img

      
        final_img = quantized_img.resize(img.size, Image.NEAREST)
        
       
        final_img = final_img.convert("RGBA")

       
        buffer = io.BytesIO()
        final_img.save(buffer, 'PNG')
        buffer.seek(0)

        return send_file(buffer, mimetype='image/png')

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error processing image.", 500

if __name__ == '__main__':
    app.run(debug=True)
