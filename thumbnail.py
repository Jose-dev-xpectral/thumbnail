from PIL import Image

image = Image.open('test1.jpg')

file_prefix = '_compressed.jpg'

current_resolution = image.size

print(f"Current image resolution: {current_resolution}")

image.save(file_prefix, optimize=True, quality=60)

compressed = Image.open(file_prefix)

thumbnail = compressed.resize((200, 200))

thumbnail.save('thumb.jpeg')

image.thumbnail((200, 200))

image.save('thumbnail_2.jpg')


