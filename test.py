def read_image_path():
    with open('image_path.txt', 'r') as file:
        image_path = file.read()
    return image_path

def display_image():
    image_path = read_image_path()
    print(f"The generated image path is: {image_path}")

display_image()
