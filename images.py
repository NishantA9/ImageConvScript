#pip3 install Pillow

from PIL import Image, ImageFilter

img = Image.open('./Pokedex/astro.jpg')
print(img.size)

#comment below line to keep the aspect ratio
new_img = img.resize((400, 400))
new_img.save('thumbnail.jpg')
#to keep the aspect ratio
img.thumbnail((400, 400))
img.save('thumbnail2.jpg')


# print(img)

# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img = img.filter(ImageFilter.SMOOTH)

# filtered_img.save("blur.png", 'png')

#converting image and saving it
# filtered_img = img.convert('L')
# filtered_img.save("grey.png", 'png')

# #showing image
# filtered_img.show()

# #cropping image
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save("cropped.png", 'png')
# region.show()

# #rotating image
# rotated = filtered_img.rotate(90)
# rotated.save("rotated.png", 'png')

# #resizing image
# resize = filtered_img.resize((300, 300))
# resize.save("resized.png", 'png')

