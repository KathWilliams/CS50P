import sys # so we can use command line arguments
from PIL import Image
# pillow.readthedocs.io
# let's create an animated gif
# ie lots of images very similar which when run together look like it's moving
images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True,append_images=[images[1]], duration=200, loop=0
)