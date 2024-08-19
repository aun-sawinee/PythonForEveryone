Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Pen()
>>> tao.shape('turtle')
>>> tao1 = {'color':'green', 'dis':100}
>>> tao.color(tao1['color'])
>>> def rect(tao_object,tdict):
...     for i in range(4):
...         tao_object.forward(tdict['dis'])
...         tao_object.left(90)
... 
...         
>>> rect(tao,tao1)
>>> tao2 = turtle.Pen()
>>> tao2dict = {'color':'green', 'dis':50}
>>> tao2.shape('turtle')
>>> tao2.color(tao2.dict['color'])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    tao2.color(tao2.dict['color'])
AttributeError: 'Turtle' object has no attribute 'dict'
>>> tao2.color(tao2dict['color'])
>>> rect(tao2,tao2dict)
>>> tao2dict = {'color':'red', 'dis':50}
>>> tao2.color(tao2dict['color'])
>>> rect(tao2,tao2dict)
