import image

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        red = p.getRed()
        green = p.getGreen()
        blue = p.getBlue()
        
        avg = (red + green + blue) / 3.0
        newpixel = image.Pixel(avg, avg, avg)
        
        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()
