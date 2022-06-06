HTML
******


HTML介绍
=======

什么是 HTML？

HTML 是用来描述网页的一种语言。

* HTML 指的是超文本标记语言 (Hyper Text Markup Language)
* HTML 不是一种编程语言，而是一种标记语言 (markup language)

HTML标签
=======

HTML 标记标签通常被称为 HTML 标签 (HTML tag)。

* HTML 标签是由尖括号包围的关键词，比如 <html>
* HTML 标签通常是成对出现的，比如 <b> 和 </b>
* 标签对中的第一个标签是开始标签，第二个标签是结束标签

HTML文档
========
* HTML 文档 = 网页
* HTML 文档描述网页
* HTML 文档包含HTML标签和纯文本
* Web 浏览器的作用是读取 HTML 文档，并以网页的形式显示出它们。浏览器不会显示 HTML 标签，而是使用标签来解释页面的内容：

.. code-block:: text

    <!DOCTYPE html>
    <html lang="en">
       <head>
         <title>This is Title</title>
       </head>
       <body>
          This is Body!
       </body>
    </html>

作业与资料
=======

课堂PPT：  :download:`HTML <HTML.pptx>`

课堂示例程序(可以粘贴到html文件里直接打开）：

* 网页标题和内容：

.. code-block:: text

    <!DOCTYPE html>
    <html lang="en">
       <head>
         <title>This is Title</title>
       </head>
       <body>
          This is Body!
       </body>
    </html>

* 段落：

.. code-block:: text

    <!DOCTYPE html>


        <html lang="en">
            <head>
                <title>paragraphs</title>
            </head>
            <body>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis scelerisque quam, vel hendrerit lectus viverra eu. Praesent posuere eget lectus ut faucibus. Etiam eu velit laoreet, gravida lorem in, viverra est. Cras ut purus neque. In porttitor non lorem id lobortis. Mauris gravida metus libero, quis maximus dui porta at. Donec lacinia felis consectetur venenatis scelerisque. Nulla eu nisl sollicitudin, varius velit sit amet, vehicula erat. Curabitur sollicitudin felis sit amet orci mattis, a tempus nulla pulvinar. Aliquam erat volutpat.
                </p>
                <p>
                    Mauris ut dui in eros semper hendrerit. Morbi vel elit mi. Sed sit amet ex non quam dignissim dignissim et vel arcu. Pellentesque eget elementum orci. Morbi ac cursus ex. Pellentesque quis turpis blandit orci dapibus semper sed non nunc. Nulla et dolor nec lacus finibus volutpat. Sed non lorem diam. Donec feugiat interdum interdum. Vivamus et justo in enim blandit fermentum vel at elit. Phasellus eu ante vitae ligula varius aliquet. Etiam id posuere nibh.
                </p>
                <p>
                    Aenean venenatis convallis ante a rhoncus. Nullam in metus vel diam vehicula tincidunt. Donec lacinia metus sem, sit amet egestas elit blandit sit amet. Nunc egestas sem quis nisl mattis semper. Pellentesque ut magna congue lorem eleifend sodales. Donec tortor tortor, aliquam vitae mollis sed, interdum ut lectus. Mauris non purus quis ipsum lacinia tincidunt.
                </p>
                <p>
                    Integer at justo lacinia libero blandit aliquam ut ut dui. Quisque tincidunt facilisis venenatis. Nullam dictum odio quis lorem luctus, vel malesuada dolor luctus. Aenean placerat faucibus enim a facilisis. Maecenas eleifend quis massa sed eleifend. Ut ultricies, dui ac vulputate hendrerit, ex metus iaculis diam, vitae fermentum libero dui et ante. Phasellus suscipit, arcu ut consequat sagittis, massa urna accumsan massa, eu aliquet nulla lorem vitae arcu. Pellentesque rutrum felis et metus porta semper. Nam ac consectetur mauris.
                </p>
                <p>
                    Suspendisse rutrum vestibulum odio, sed venenatis purus condimentum sed. Morbi ornare tincidunt augue eu auctor. Vivamus sagittis ac lectus at aliquet. Nulla urna mauris, interdum non nibh in, vehicula porta enim. Donec et posuere sapien. Pellentesque ultrices scelerisque ipsum, vel fermentum nibh tincidunt et. Proin gravida porta ipsum nec scelerisque. Vestibulum fringilla erat at turpis laoreet, nec hendrerit nisi scelerisque.
                </p>
                <p>
                    Sed quis malesuada mi. Nam id purus quis augue sagittis pharetra. Nulla facilisi. Maecenas vel fringilla ante. Cras tristique, arcu sit amet blandit auctor, urna elit ultricies lacus, a malesuada eros dui id massa. Aliquam sem odio, pretium vel cursus eget, scelerisque at urna. Vestibulum posuere a turpis consectetur consectetur. Cras consequat, risus quis tempor egestas, nulla ipsum ornare erat, nec accumsan nibh lorem nec risus. Integer at iaculis lacus. Integer congue nunc massa, quis molestie felis pellentesque vestibulum. Nulla odio tortor, aliquam nec quam in, ornare aliquet sapien.
                </p>
            </body>
        </html>

* 不同级别标题

.. code-block:: text

    <!DOCTYPE html>
    <html lang="en">
       <head>
         <title>This is Title</title>
       </head>
       <body>
          <h1>A Large Heading</h1>
          <h2>A Smaller Heading</h2>
          <h6>The Smallest Heading</h6>
       </body>
    </html>

* 表格

.. code-block:: text


    <!DOCTYPE html>
    <html lang="en">
       
    <head>
             <title>This is Title</title>
           
    </head>
       
    <body>
    <table>
        <thead>
        <th>Ocean</th>
        <th>Average Depth</th>
        <th>Maximum Depth</th>
        </thead>
        <tbody>
        <tr>
            <td>Pacific</td>
            <td>4280 m</td>
            <td>10911 m</td>
        </tr>
        <tr>
            <td>Atlantic</td>
            <td>3646 m</td>
            <td>8486 m</td>
        </tr>
        </tbody>
    </table>
       
    </body>
    </html>


作业：:download:`HTML作业 <HTML作业.pdf>`
