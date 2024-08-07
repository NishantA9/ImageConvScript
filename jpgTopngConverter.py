import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
# loop through Pokedex/ and convert images to png and save to the new/ folder and accept user input

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')

# run this code in terminal
# python3 jpgTopngConverter.py Pokedex/ new/
# python3 jpgTopngConverter.py Pokedex/ new/    
# python3 jpgTopngConverter.py Pokedex/ new/

#------------------------------------------------------------

# import os

# def rename_files(directory, prefix):
#     for filename in os.listdir(directory):
#         old_name = os.path.join(directory, filename)
#         new_name = os.path.join(directory, f"{prefix}_{filename}")
#         os.rename(old_name, new_name)
#     print("Files renamed successfully.")

# directory = '/path/to/your/directory'
# prefix = 'new_prefix'
# rename_files(directory, prefix)
