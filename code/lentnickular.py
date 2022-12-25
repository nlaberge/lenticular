# import image libraries
from PIL import Image

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
    # Image parameters, only change the variables in all caps
    IMAGE_WIDTH_INCHES = 6
    IMAGE_HEIGHT_INCHES = 4
    IMAGE_DPI = 600
    CPI = 49.66

    # take command line arguments for image paths
    parser = argparse.ArgumentParser(description='Weave two images together')
    parser.add_argument('image1', help='Path to first image')
    parser.add_argument('image2', help='Path to second image')

    #add optional arguments
    parser.add_argument('-cpi', help='CPI of the lenticular sheet', type=float, default=CPI)
    parser.add_argument('-dpi', help='DPI of the output image', type=int, default=IMAGE_DPI)
    parser.add_argument('-width', help='Width of the output image in inches', type=float, default=IMAGE_WIDTH_INCHES)
    parser.add_argument('-height', help='Height of the output image in inches', type=float, default=IMAGE_HEIGHT_INCHES)

    args = parser.parse_args()
    # update variables from command line arguments
    IMAGE_WIDTH_INCHES = args.width
    IMAGE_HEIGHT_INCHES = args.height
    IMAGE_DPI = args.dpi
    CPI = args.cpi

    image_width_px = IMAGE_WIDTH_INCHES * IMAGE_DPI
    num_colums = CPI*IMAGE_WIDTH_INCHES
    px_per_column = image_width_px / num_colums

    im_weave = weave_images_together(args.image1,args.image2,px_per_column)
    im_weave.save('figures/lenticular_output.png',dpi=(IMAGE_DPI,IMAGE_DPI))
    print('saved image to lenticular_output.png')