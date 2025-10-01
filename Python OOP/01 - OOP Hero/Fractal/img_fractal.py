# # Import necessary libraries
# from PIL import Image
# import numpy as np
# import colorsys

# # Setting the width of the output image as 1024
# WIDTH = 1024

# # A function to return a tuple of colors as integer values of RGB
# def rgb_conv(i):
#     color = 255 * np.array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
#     return tuple(color.astype(int))

# # Function defining a Mandelbrot
# def mandelbrot(x, y):
#     c0 = complex(x, y)
#     c = 0
#     for i in range(1, 1000):
#         if abs(c) > 2:
#             return rgb_conv(i)
#         c = c * c + c0
#     return (0, 0, 0)

# # Creating the new image in RGB mode
# img = Image.new('RGB', (WIDTH, int(WIDTH / 2)))
# pixels = img.load()

# for x in range(img.size[0]):
#     # Displaying the progress as percentage
#     print("%.2f %%" % (x / WIDTH * 100.0)) 
#     for y in range(img.size[1]):
#         pixels[x, y] = mandelbrot((x - (0.75 * WIDTH)) / (WIDTH / 4),
#                                   (y - (WIDTH / 4)) / (WIDTH / 4))

# # To display the created fractal after completing the given number of iterations
# img.show()
