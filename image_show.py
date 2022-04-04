from PIL import Image 

def show(path):
    
    img = Image.open(path)
    width, height = img.size

    resized_image = img.resize(
            (round(img.size[0]*0.3),round(img.size[1]*0.3))
            )

    resized_image.show()

if __name__ == '__main__':
    path = 'path/to/your/image.png'
    show(path)
