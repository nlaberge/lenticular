# import image libraries
from PIL import Image

# Image parameters, only change the variables in all caps
IMAGE_WIDTH_INCHES = 6
IMAGE_HEIGHT_INCHES = 4
IMAGE_DPI = 600
image_width_px = IMAGE_WIDTH_INCHES * IMAGE_DPI
CPI = 49.66
num_colums = CPI*IMAGE_WIDTH_INCHES
px_per_column = image_width_px / num_colums

def weave_images_together(im1_path,im2_path,px_per_column):
    # load two images from jpeg files
    im1 = Image.open(im1_path)
    im2 = Image.open(im2_path)
    # weave images together
    im = Image.new('RGB', (im1.width, im1.height), (255, 255, 255))
    for x in range(im.width):
        for y in range(im.height):
            if x % px_per_column < px_per_column/2:
                im.putpixel((x, y), im1.getpixel((x, y)))
            else:
                im.putpixel((x, y), im2.getpixel((x, y)))
    return im

# take command line arguments in main function
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Weave two images together')
    parser.add_argument('image1', help='Path to first image')
    parser.add_argument('image2', help='Path to second image')
    args = parser.parse_args()
    im_weave = weave_images_together(args.image1,args.image2,px_per_column)
    im_weave.save('lenticular_output.png',dpi=(IMAGE_DPI,IMAGE_DPI))
    print('saved image to lenticular_output.png')