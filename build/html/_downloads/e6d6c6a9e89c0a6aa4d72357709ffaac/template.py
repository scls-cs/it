import cv2

img = cv2.imread('paris.jpeg') #read the beautiful image of golden gate bridge

img_width= img.shape[1]  #image width
img_height= img.shape[0] #image height

print(img_width, img_height) #print image width and height

blue = img[100, 200, 0] #get the value of blue channel of pixel at row 100, column 200
green = img[100, 200, 1] # get the value of green channel of the same pixel
red = img[100, 200, 2]  #get the value of red channel of the same pixel

print(blue, green, red) #print the pixel's RGB value

img[100, 200] = [255, 255, 255]

for row in range(img_height):
    for col in range(img_width):
        blue = img[row, col, 0]
        green = img[row, col, 1]
        red = img[row, col, 2]

        r = 0.393*red+0.769*green+0.189*blue
        g = 0.349*red+0.686*green+0.168*blue
        b = 0.272*red+0.534*green+0.131*blue
        #print(blue, green, red)
        #color = (blue+green+red)/3
        img[row, col] = [r, g, b]

cv2.imshow("Demo", img)
cv2.imwrite('1.png', img)


k=cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()




