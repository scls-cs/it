PyCharm入门
******

实验
=======

上学期我们主要通过网站来编写和运行Python程序。通过网站编程的好处是无需安装额外软件，可以随时随地进行程序编写。但也有不好的地方。由于网站提供的函数和工具有限，我们只能进行简单的操作。所以网站编程只适合初学者入门学习。

如果我们要编写更复杂的程序，例如读取和处理图像，我们就需要更为专业的编程工具。目前世界最流行的Python编程工具是PyCharm，它是由JetBrains打造的编译工具。作为高中生，我们可以免费使用这款工具。下面是基于Mac的PyCharm安装步骤。基于Windows的安装步骤非常类似，有一些不同的地方我会指出。

1. 下载PyCharm
----
PyCharm是由JetBrains打造的编译工具。

下载地址：`PyCharm <https://www.jetbrains.com/pycharm/download>`_

选择Community版本并下载。


2. 安装PyCharm
-------------
双击下载后的文件，将PyCharm拖到Applications中。


.. image:: drag.png
   :scale: 50%

选择Do not import settings

.. image:: import.png
   :scale: 50%

3. 下载并安装Python
------------
到了这一步我们已经成功一半了！Python是一门编程语言，下一步我们需要安装它的**解释器**（巧了，它也叫Python)。

下载地址：`Python Download <https://www.python.org/downloads/>`_

点击有Download的黄色按钮下载最新版本的Python。

.. image:: python.png
  :scale: 20%

下载完毕之后安装Python。在点击若干continue和agree之后，Python解释器就成功安装在我们的电脑里了。从现在开始，我们的计算机也可以读懂Python程序了（哦还差一点）。



4. 在PyCharm中配置Python
-----------------------
打开PyCharm，点击New Project。

.. image:: new.png
  :scale: 30%

接下来关注两个红框的地方：

1. Location这一栏是给你的项目进行命名的位置，你可以将最后的文件名改为你想要的任意文件名，例如hw1。

2. 选择Previously configured interpreter, 在下拉栏中选择Python 3.10（希望它已经出现在那里了）。

.. image:: config.png
  :scale: 30%

点击Create，到这里我们成功了90%了。


5. 编写程序
----------

右键hw1 -> New -> Python File，取一个名字（比如loop)，按下回车。你会发现hw1项目下出现了一个文件：loop.py。

.. image:: file.png
  :scale: 50%

.. image:: loop.png
  :scale: 50%

