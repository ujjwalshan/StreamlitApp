from PIL import Image
filename = r"D:\Data\v126852\Documents\My Pictures\Saved Pictures\images.jpg"
image = Image.open(filename)

print(image)
image.show