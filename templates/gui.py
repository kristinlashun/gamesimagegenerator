import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

def fetch_image():
    try:
        response = requests.get("http://127.0.0.1:5001/api/generate")
        response.raise_for_status()  # Check for HTTP request errors
        data = response.json()
        if 'image_path' in data:
            image_url = f"http://127.0.0.1:5001{data['image_path']}"
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            image_data = Image.open(BytesIO(image_response.content))
            img = ImageTk.PhotoImage(image_data)
            panel.config(image=img)
            panel.image = img
        else:
            messagebox.showerror("Error", data.get("error", "Unknown error"))
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch image: {e}")

# Create the main window
root = tk.Tk()
root.title("Random Game Image Generator")

# Create a button to fetch the image
button = tk.Button(root, text="Generate Image", command=fetch_image)
button.pack(pady=20)

# Create a label to display the image
panel = tk.Label(root)
panel.pack(pady=20)

# Start the GUI event loop
root.mainloop()
