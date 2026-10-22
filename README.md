

A small menu-driven program that applies basic image processing operations to a grayscale image. The image is stored as a 2D list (5x5) of pixel values from `0` (black) to `255` (white). No external libraries are required.




## The Image

`A` is the sample grayscale image: a 5x5 grid where each number is the brightness of one pixel.

## Functions

### `show(img)`
Prints the image row by row so it is easy to read in the terminal.

### `invert(img)`
Creates the negative of the image. Each pixel becomes `255 - pixel`, so dark areas turn bright and bright areas turn dark.

### `brightness(img)`
Asks for a brightness factor and adds it to every pixel. A positive value makes the image brighter, a negative value makes it darker. Results are clamped to stay between `0` and `255`.

### `threshold(img)`
Asks for a threshold value and converts the image to pure black and white. Pixels below the threshold become `0`; pixels at or above it become `255`.

### `h_flip(img)`
Flips the image horizontally (mirror image). The order of pixels in each row is reversed, so left becomes right.

### `v_flip(img)`
Flips the image vertically (upside down). The order of the rows is reversed, so top becomes bottom.

### `rotate(img)`
Rotates the image 90 degrees clockwise. Columns of the original become rows of the new image, read from bottom to top.

### `edge(img)`
A simple edge detector. It compares each pixel with the pixel to its right. If the difference is greater than `50`, the pixel is marked as an edge (`255`), otherwise `0`. The last column is always set to `0` since it has no right neighbour.

### `load_ppm()`
Reads a PPM image file named `test.ppm` (plain-text P3 format). It prints the width, height, and then the RGB values of each pixel, grouped by row. The file must be in the same folder as the script.

### `main()`
The main loop. It shows the menu, takes the user's choice, prints the original image and the processed result, and repeats until the user enters `-1`.

## Notes

- The original image `A` is never changed; each operation returns a new image.
- The menu text says `1-exit`, but the actual exit option is `-1` (`1` is Invert).
