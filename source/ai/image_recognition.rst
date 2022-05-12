图像识别实验（上）
**********

这次实验课的任务是识别手写的数字。

1.人工智能介绍
------
人工智能的第一步是训练。我们可以把它类比成在学校学习。人工智能和我们同学一样，为了完成一项工作，需要接受教育。

具体来说，经过训练（training)的人工智能可以将其所学应用于数字世界的任务，例如识别图像、推荐商品等，这个过程被称为"推理"(inference)。

没有训练，就不可能有推理。这很容易讲通。我们如果不默写古诗词（训练），就不可能培养对诗歌的鉴赏能力（推理）。我们如果不大量的做托福真题（训练），我们就不会在实际托福考试中取得好成绩（推理）。

所以人工智能分为训练和推理两个步骤。我们这次需要识别手写的0-9十个数字。为了可以识别（推理），我们需要先进行训练，也就是让人工智能先看大量手写数字的图片。


2. 下载训练所用图片
------------

我们所使用的数据集是由0到9的数字图像构成的。每个数字都由9张图片组成，总共包含了90张训练图像。

每一张图片的命名规则是数字.序号.png，命名规则很重要。为了让人工智能做出正确的决定，我们需要提供带标签的数据，例如人工需要知道7.1.png对应数字7。所以这里每一张图片文件名的第一个数字，就是图片的标签。


下载图片: :download:`手写数字图片 <images.zip>`

3. 安装PIL和MatplotLib
--------------------

与numpy和opencv-python一样，PIL和MatplotLib也是Python的模块，提供了很多有用的库函数。为了完成这项实验，我们需要安装这两个模块：

打开terminal，运行如下命令：

.. code-block:: text

        python3 -m pip install --upgrade pip (windows用户将python3替换成python)

        python3 -m pip install --upgrade Pillow（同上）

        python3 -m pip install -U matplotlib（同上）


4. 准备编程
----------------

将训练图片解压缩后，放入project中。新建一个python文件，取名为imagerec.py。前三行输入

.. code-block:: text

        from PIL import Image
        import numpy as np
        import matplotlib.pyplot as plt


现在project的窗口类似下图(images文件夹和imagerec.py平行放置）：

.. image:: pil.png
   :scale: 30%

将script path设置为imagerec.py（这一步相信大家已经都会了）。试运行一下，如果没有出现任何的error（会有红色字体出现），就说明模块都安装成功了。

5. 感受图像矩阵
--------------

点击images文件夹，打开dot.png这幅图片。如果图片过小可以放大。这幅图片的分辨率是8x8，左上角的像素点是黑色，其余的像素点均为白色。

接下来输入下面三行指令。

.. code-block:: text

        i = Image.open('images/dot.png') #加载dot.png图片

        iar = np.asarray(i)  #将图片转化为像素值数组

        print(iar)           #打印数组

运行程序，你会看到如下结果：

.. image:: matrix.png
   :scale: 30%

打印结果总共有8部分，分别代表图片每行的像素信息。每行有8个像素，每个像素都有4个值。其中前三个值代表像素的三通道，也就是B、G、R值；

第四个值是alpha值，是表征图片透明度的值，我们这次的实验不需要用到。

例如下图中绿色方框的部分，就是第一行第一个像素的RGB值。是不是可以和图片对应起来？

.. image:: dot.jpeg
   :scale: 30%

6. 将所有图像变为二值图像
--------------------

识别物体最关键的信息是边缘特征，而不是颜色。例如下面两幅图像，右边图像是彩色图，左边图像只有黑白两色。两个图像都能够显示出数字0的边缘特征，而由于存储和处理左边图像的数据量要远远小于右图，从而可以大大缩短训练所用的时间。所以我们第一步，就是要将所有的彩色图像变为二值图像。

（注：二值图像就是图像中只有2种颜色的图像，一般就是黑白图像，2个灰度值分别为0（表示黑色）和255（表示白色））

.. image:: binary.png
   :scale: 40%

我们首先构造一个threshold函数，来将彩色图像变为黑白图像。这个函数的原理非常简单，通过对图像编码的学习，大家已经具备了理解这段函数的能力。我们将图像数组作为函数参数，函数会返回一个只有0和1组成的数组，也就是我们想要的二值图像的数组。

.. code-block:: text

      def threshold(imageArray):
            newArr = imageArray
            numOfPixel = 0    #像素点个数
            sum = 0
            for eachRow in imageArray:
                for eachPix in eachRow:
                    avgNum = (eachPix[0]+eachPix[1]+eachPix[2])/3   #将像素点的RGB求平均值
                    numOfPixel = numOfPixel+1
                    sum = sum+avgNum     #对平均值求和

            avg = sum/numOfPixel        #图像的RGB均值，作为变黑或者变白的分界点

            for eachRow in imageArray:
                for eachPix in eachRow:
                    if (eachPix[0]+eachPix[1]+eachPix[2])/3 > avg:
                        eachPix[0] = 255    #如果像素点RGB平均值高于分界点，就变为白色
                        eachPix[1] = 255
                        eachPix[2] = 255
                    else:
                        eachPix[0] = 0      #否则变为黑色
                        eachPix[1] = 0
                        eachPix[2] = 0

            return newArr


得到二值图像数组后，我们就可以显示新的图像了。

.. code-block:: text

        i1 = Image.open('images/numbers/y0.4.png')

        iar1 = np.array(i1)    #将图片转化为数组1

        iar2 = np.array(i1)    #将图片转化为数组2

        threshold(iar1)        #对iar1数组进行二值化处理

        ax1 = plt.subplot2grid((8,6), (0,0), rowspan=4, colspan=3)    #在画布上开辟一块区域

        ax2= plt.subplot2grid((8,6), (0,3), rowspan=4, colspan=3)     #在画布上开辟另一块对比区域


        ax1.imshow(iar1)    #显示图1（也就是处理后的图片）
        ax2.imshow(iar2)    #显示图2（也就是原图）


        plt.show()

7. 将文件名输出
------------

.. code-block:: text

        def createExamples():
            numbersWeHave = range(0,10)    #create array from 0-9
            versionsWeHave = range(1,10)   #create array from 1-9

            for eachNum in numbersWeHave:
                for eachVer in versionsWeHave:
                    imgFilePath = 'images/numbers/' + str(eachNum) + '.' + str(eachVer) + '.png'
                    print(imgFilePath)



8. 作业
---------

作业要求：:download:`图像识别作业I <Image Recognition I.pdf>`

课堂PPT: :download:`深度学习 <deep learning.pptx>`