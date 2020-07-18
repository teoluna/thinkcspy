import image

img = image.Image("luther.jpg")
win = image.ImageWin()

newimg = image.EmptyImage(img.getWidth(), img.getHeight())

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)

        newred = p.getRed() * 0.393 + p.getGreen() * 0.769 + p.getBlue() * 0.189
        newgreen = p.getRed() * 0.349 + p.getGreen() * 0.686 + p.getBlue() * 0.168
        newblue = p.getRed() * 0.272 + p.getGreen() * 0.534 + p.getBlue() * 0.131

        newpixel = image.Pixel(newred, newgreen, newblue)

        newimg.setPixel(col, row, newpixel)

newimg.draw(win)
win.exitonclick()