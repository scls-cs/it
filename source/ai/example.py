from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def threshold(imageArray):
    newArr = imageArray
    numOfPixel = 0    #像素点个数
    sum = 0           #像素点RGB平均值的和
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = (eachPix[0]+eachPix[1]+eachPix[2])/3
            numOfPixel = numOfPixel+1
            sum = sum+avgNum

    avg = sum/numOfPixel

    for eachRow in imageArray:
        for eachPix in eachRow:
            if (eachPix[0]+eachPix[1]+eachPix[2])/3 > avg:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0

    return newArr

def createExamples():
    numbersWeHave = range(0,10)
    versionsWeHave = range(1,10)

    for eachNum in numbersWeHave:
        for eachVer in versionsWeHave:
            imgFilePath = 'images/numbers/' + str(eachNum) + '.' + str(eachVer) + '.png'
            print(imgFilePath)

i1 = Image.open('images/numbers/y0.4.png')

iar1 = np.array(i1)

iar2 = np.array(i1)

threshold(iar1)

ax1 = plt.subplot2grid((8,6), (0,0), rowspan=4, colspan=3)

ax2= plt.subplot2grid((8,6), (0,3), rowspan=4, colspan=3)


ax1.imshow(iar1)
ax2.imshow(iar2)


plt.show()

#createExamples()





