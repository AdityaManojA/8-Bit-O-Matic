import functions_framework
from flask import request, send_file
from PIL import Image, ImageOps
import io

# This decorator tells Firebase this is an HTTP-triggered function
@functions_framework.http
def pixelateImage(req):
    """
    HTTP Cloud Function that receives an image, pixelates it,
    and sends it back.
    """
    # Set up CORS to allow requests from any origin
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    
    # Handle preflight requests for CORS
    if req.method == 'OPTIONS':
        # Allows GET, POST and OPTIONS.
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)


    # Check if an image was uploaded
    if 'image' not in request.files:
        return ('No image file found', 400, headers)
    
    file = request.files['image']

    # --- YOUR ORIGINAL IMAGE PROCESSING LOGIC ---
    img = Image.open(file.stream).convert("L")
    target_size = (44, 47)
    img_resized = img.resize(target_size, Image.NEAREST)

    def pixelate(image, pixel_size=3):
        small = image.resize((image.width // pixel_size, image.height // pixel_size), Image.NEAREST)
        return small.resize(image.size, Image.NEAREST)

    img_pixelated = pixelate(img_resized, pixel_size=3)
    threshold = 128
    img_bw = img_pixelated.point(lambda x: 255 if x > threshold else 0, mode='1')

    img_final = ImageOps.invert(img_bw.convert("L")).convert("RGBA")
    datas = img_final.getdata()
    new_data = []
    for item in datas:
        if item[:3] == (255, 255, 255):
            new_data.append((255, 255, 255, 0)) # Make white transparent
        else:
            new_data.append(item)
    img_final.putdata(new_data)
    # --- END OF YOUR LOGIC ---

    # Save the processed image to an in-memory buffer
    buffer = io.BytesIO()
    img_final.save(buffer, 'PNG')
    buffer.seek(0)

    # Send the image data back to the browser
    return send_file(buffer, mimetype='image/png', extra_headers=headers)