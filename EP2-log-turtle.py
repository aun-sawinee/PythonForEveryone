Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
type(tao)
<class 'turtle.Turtle'>
tao.shape('turtle')
tao.color('red')
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.clear()
tao.reset()
for i in range(4):
    tao.forward(100)
    tao.left(90)

    
tao.color('green')
for i in range(8):
    tao.forward(100)
    tao.left(45)

    
for i in range(4):
    print(i)
    tao.forward(100)
    tao.left(90)

    
0
1
2
3
list(range(4))
[0, 1, 2, 3]
list(range(1,4))
[1, 2, 3]
list(range(1,5))
[1, 2, 3, 4]
list(range(0,10,2))
[0, 2, 4, 6, 8]
list(range(0,11,2))
[0, 2, 4, 6, 8, 10]
taolist = []
>>> tao.reset()
>>> for i in range(8):
...     tao.forward(100)
...     tao.left(45)
... 
...     
>>> tao.up()
>>> tao.goto(30,30)
>>> tao.down()
>>> for i in range(4):
...     print(i)
...     tao.forward(50)
...     tao.left(90)
... 
...     
0
1
2
3
>>> taolist = []
>>> tao1 = turtle.Pen()
>>> tao2 = turtle.Pen()
>>> taolist.append(tao)
>>> taolist.append(tao1)
>>> taolist.append(tao2)
>>> print(taolist)
[<turtle.Turtle object at 0x000001F42AFA7260>, <turtle.Turtle object at 0x000001F42B5B64E0>, <turtle.Turtle object at 0x000001F42B5B66F0>]
>>> taolist[0].forward(200)
>>> taolist[1].backward(200)
>>> taolist[2].color('red')
>>> taolist[2].left(90)
>>> taolist[2].forward(100)
>>> for t in taolist:
...     for i in range(4):
...         t.forward(50)
...         t.left(90)
... 
...         
