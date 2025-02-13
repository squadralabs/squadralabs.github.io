import cairosvg
import os

svg_path = "clients/hd/client-appa.svg"
png_path = "clients/hd/client-appa.png"

# Define the desired width and height
width = 2000
height = 2000

# Convert SVG to PNG with specified size
cairosvg.svg2png(url=svg_path, write_to=png_path, output_width=width, output_height=height)
