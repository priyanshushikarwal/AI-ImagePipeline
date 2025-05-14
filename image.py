from rembg import remove
from PIL import Image

input_path = 'ford_scenic.jpg'
output_path = 'ford_nobg.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        o.write(remove(i.read()))

