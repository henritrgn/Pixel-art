The script.py file in the repository henritrgn/Pixel-art contains Python functions to pixelate images and manipulate image colors using the PIL library. Here are the key components:

    pixeliser_image: This function pixelates an image by averaging the colors of neighboring pixels.
    pixeliser_image_amelioree: An enhanced version of the pixelation function that retains the original pixel color if it is within a certain distance from the average color.
    rogner_image: Crops the image to ensure its dimensions are multiples of the pixelation size.
    creer_palette: Generates a color palette using k-means clustering to group colors.
    generer_image: Creates a new image using the generated color palette, replacing each pixel's color with the closest palette color.

The script includes example usage of these functions to pixelate an image, crop it, create a color palette, and generate a final image with reduced colors. 

Keyword : PixelME, Pixel Art, Pixel, Art, Algorithm, Python, DIY, Idontneedpaytogetapps, free, easy.
