This module used to convert image to appropriate size given by user. You can also do bulk resizing.
    Usages:
        $ python imageResize.py [filename, "all" for allfiles "<FILENAME>" for specific file] [mode , t for thumbnail or r for resize] [width] [height] [destination]
    Note : t here refers to the img.thumbnail() function 
    and r refers to the img.resize() 
    Thumbnail maintains the aspect raio of the image while resize function doesn't maintain the aspect ratio
    
    Advantages:
        if the destination doesn't exist, it will automatically make the folder

