# 👾 8-Bit-O-Matic: The Pixel Art Creator 🎨

Turn any image into a retro, 8-bit style piece of art! This simple web application takes your uploaded images and transforms them into pixelated versions, offering both full-color and classic black & white styles. Perfect for NFT artwork creations ✨

---

## 🚀 Live Demo

Check out the live application here:

### 👉 [https://eight-bit-o-matic.onrender.com/](https://eight-bit-o-matic.onrender.com/) 👈

---
## 🖼️ Project Showcase

Here are some examples of images transformed by the 8-Bit-O-Matic!

### Character Set 1

| Original | Pixelated (Color) | Pixelated (B&W) |
| :------: | :---------------: | :-------------: |
| ![Original d1](./Demo-Images/d1.jpg) | ![Color d1](./Demo-Images/d1(2).png) | ![B&W d1](./Demo-Images/d1(1).png) |

<br>

### Character Set 2

| Original | Pixelated (Color) | Pixelated (B&W) |
| :------: | :---------------: | :-------------: |
| ![Original d2](./Demo-Images/d2.jpg) | ![Color d2](./Demo-Images/d2(1).png) | ![B&W d2](./Demo-Images/d2(2).png) |

---

## 🌟 Features

-   **🖼️ Easy Image Upload:** Select any image file from your computer.
-   **🎨 Color Pixelation:** Converts your image into a 16-color, pixelated version.
-   **🎬 Black & White Pixelation:** Creates a classic, monochrome pixel art effect.
-   **🚀 Instant Preview:** See your generated 8-bit character immediately on the page.
-   **🕹️ Retro UI:** A fun, 8-bit themed interface.

---

## 🛠️ Tech Stack

-   **🐍 Backend:** Python with **Flask**
-   **🖼️ Image Processing:** **Pillow** (Python Imaging Library)
-   **🌐 Frontend:** HTML, CSS, and vanilla JavaScript

---

## 🚀 Setup and Installation

Follow these steps to get the application running on your local machine.

### 1. Prerequisites ✅

Make sure you have **Python 3** and **pip** installed on your system. You can check by running:

```bash
python --version
pip --version
````

### 2\. Get the Project Files 📁

Get the project files onto your machine. You will need two files: `app.py` and `index.html`.

### 3\. Create the Project Structure 🏗️

For Flask to find the HTML file, you must place it in a specific folder structure:

```
your-project-folder/
├── app.py
└── templates/
    └── index.html
```

  - Create a folder for your project.
  - Place `app.py` inside it.
  - Create a sub-folder named `templates`.
  - Place `index.html` inside the `templates` folder.

### 4\. Create a Virtual Environment 🌿 (Recommended)

It's best practice to create a virtual environment to manage project dependencies.

```bash
# Create the virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 5\. Install Dependencies 📦

The project requires `Flask` and `Pillow`. Install them using pip:

```bash
pip install Flask Pillow
```

### 6\. Run the Application ▶️

With your virtual environment active and dependencies installed, run the Flask app:

```bash
python app.py
```

You should see output like this, indicating the server is running:

```
 * Running on [http://127.0.0.1:5000](http://127.0.0.1:5000)
```

Open a web browser and navigate to **http://127.0.0.1:5000** to use the application.

-----

## 🎮 How to Use

1.  Open the application in your browser.
2.  Click the **"Select File..."** button to upload an image.
3.  Once an image is selected, the pixelation buttons will become active.
4.  Click **"Pixelate Color"** for a 16-color version.
5.  Click **"Pixelate B\&W"** for a black and white version.

-----

## 🔮 Future Scope

### Automating NFT Collection Generation 🤖

The core logic of this tool can be extended to automatically generate entire NFT collections with a consistent, retro pixel art style. This is a common and powerful technique used for large-scale PFP (Profile Picture) projects.

The workflow would involve:

1.  **Creating Layered Artwork:** Design character traits in separate, transparent `.png` layers (e.g., backgrounds, bodies, heads, accessories).
2.  **Combining and Pixelating:** A Python script can randomly select one file from each layer category, stack them into a single composite image, and then run that image through the pixelation logic from this project.
3.  **Generating Thousands of Variations:** By running this script in a loop, you can generate a collection of 10,000 (or more\!) unique NFTs, each with a different combination of traits.

Here’s a simplified Python snippet to illustrate the concept:

```python
from PIL import Image
import random

# Assume pixelation logic is in a function:
# def pixelate_image(image_to_process):
#     # ... (your image processing code) ...
#     return final_pixelated_image

# Paths to your layered artwork
backgrounds = ["layers/bg_blue.png", "layers/bg_red.png"]
bodies = ["layers/body.png"]
accessories = ["layers/hat.png", "layers/sunglasses.png", None]

# Generation Loop
for i in range(100): # Generate 100 unique images
    # 1. Randomly choose layers
    bg_path = random.choice(backgrounds)
    acc_path = random.choice(accessories)
    
    # 2. Combine layers
    background = Image.open(bg_path).convert("RGBA")
    body = Image.open("layers/body.png").convert("RGBA")
    combined = Image.alpha_composite(background, body)
    
    if acc_path:
        accessory = Image.open(acc_path).convert("RGBA")
        combined = Image.alpha_composite(combined, accessory)
        
    # 3. Run final image through the pixelator
    # final_nft = pixelate_image(combined)
    
    # 4. Save the result
    # final_nft.save(f"output_collection/nft_{i+1}.png")
    print(f"Generated NFT #{i+1}!")
```

By building on this project, you can create a powerful generator for your own unique NFT collection\! 💎

-----

