"""
This module used to convert image to appropriate size given by user. You can also do bulk resizing.
Usages:
    $ python imageResize.py [filename, "all" for allfiles "<FILENAME>" for specific file] [mode , t for thumbnail or r for resize] [width] [height] [destination]
Note : t here refers to the img.thumbnail() function 
and r refers to the img.resize() 
Thumbnail maintains the aspect raio of the image while resize function doesn't maintain the aspect ratio

Advantages:
    if the destination doesn't exist, it will automatically make the folder 
"""

from PIL import Image
import os
import sys


class Image_resolve:
    def __init__(self, filename, mode, width, height, dest):
        """
        Collecting data from the user like :
            Filename
            Mode
            Width
            Height
            Destination
        """
        self.filename = filename
        self.mode = mode
        self.width = width
        self.height = height
        self.dest = dest

        # print("self.filename", self.filename)
        # print("self.mode", self.mode)
        # print("self.width", self.width)
        # print("self.height", self.height)
        # print("self.dest", self.dest)

        if os.path.isdir(dest) != True:
            """
            Creating the Destination directory if it doesn't exists
            """
            os.mkdir(dest)

        if self.filename == "all":
            self.file_list = os.listdir()
            # print(self.file_list)
            print("File is : ")
            for files in self.file_list:
                self.resize_image(files)
        else:
            print("File is : ")
            self.resize_image(self.filename)

    def resize_image(self, files):
        """
        Resizes the image to demanded size
        """
        try:
            image = Image.open(files)
            print(f"\t{files}")
            if(self.mode == 't'):
                image.thumbnail((int(self.width), int(self.height)))
                print(f'{self.dest}/{files}')
                width, height = image.size
                print("File size : ", width, " x ", height, "\n")
                image.save(f'{self.dest}/{files}')
            elif(self.mode == 'r'):
                new_img = image.resize((int(self.width), int(self.height)))
                print(f'{self.dest}/{files}')
                width, height = new_img.size
                print("File size : ", width, " x ", height)
                new_img.save(f'{self.dest}/{files}')
            else:
                print("Error!! Please read Document you idiot :( ")
        except Exception as e:
            print(e)
        # finally:
        #     print(
        #         "Have a nice day and have almonds daily to increase your ability to think :) !!!!")


if __name__ == "__main__":
    Image_resolve(filename=sys.argv[1], mode=sys.argv[2],
                  width=sys.argv[3], height=sys.argv[4], dest=sys.argv[5])
