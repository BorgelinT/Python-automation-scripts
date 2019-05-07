import os
from PIL import Image

def resize_image(input_dir, infile, output_dir='resized',  size = (300, 300)): #default size=300x300, default input folder=input default output folder=resized
    outfile = os.path.splitext(infile)[0] + '_resized' #add "_resized" before file ext
    extension = os.path.splitext(infile)[1] #return file ext

    try:
        img = Image.open(input_dir + '/' + infile) #get image
        width, height = img.size #get dimensions
        #print (width, height)
        
        if width >= height: 
            diff = ((width - height)/2)
            diff2 = (width - diff)
            area = (diff, 0, diff2, height)
            
        else:
            diff = ((height-width)/2)
            diff2 = (height-diff)
            area = (0, diff, width, diff2)
            
        img = img.crop(area)
        img = img.resize((size[0], size[1]), Image.LANCZOS)

        new_file = output_dir + '/' + outfile + extension
        img.save(new_file)

    except OSError:
        print('unable to resize {}'.format(infile))

if __name__ == '__main__':
    output_dir = 'resized'
    dir = os.getcwd()
    input_dir = 'input'
    full_input_dir = dir + '/' + input_dir

    if not os.path.exists(os.path.join(dir, output_dir)): #make an output folder called "resized" if it doesn't exist already
        os.mkdir(output_dir) 

    try:
        for file in os.listdir(full_input_dir): #resize the images in input folder
            #print('file: {}'.format(file))
            resize_image(input_dir, file, output_dir)

    except OSError:
        print('file not found')