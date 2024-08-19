Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
help(print)
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

def hello(friend):
    print(f'Hi, {friend}')

    
hello(aun)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    hello(aun)
NameError: name 'aun' is not defined
hello('aun')
Hi, aun

def land(width,long):
    cal = width * long
    cal_wa = cal/4
    print(f'ที่ดินผืนนี้กว้าง: {width} เมตร   ยาว: {long})
          
SyntaxError: unterminated f-string literal (detected at line 4)
def land(width,long):
    cal = width * long
    cal_wa = cal/4
    print(f'ที่ดินผืนนี้กว้าง: {width} เมตร   ยาว: {long}')
    print(f'ที่ดินผืนนี้มีพื้นที่: {cal} ตารางเมตร')
    print(f'ที่ดินผืนนี้มีพื้นที่: {cal_wa} ตารางวา')

    
land(5,15)
ที่ดินผืนนี้กว้าง: 5 เมตร   ยาว: 15
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางวา
land(10,80)
ที่ดินผืนนี้กว้าง: 10 เมตร   ยาว: 80
ที่ดินผืนนี้มีพื้นที่: 800 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 200.0 ตารางวา
def land(width,long):
    cal = width * long
    cal_wa = cal/4
    print(f'ที่ดินผืนนี้กว้าง: {width} เมตร   ยาว: {long} เมตร')
    print(f'ที่ดินผืนนี้มีพื้นที่: {cal} ตารางเมตร')
    print(f'ที่ดินผืนนี้มีพื้นที่: {cal_wa} ตารางวา')

    
res = land(5,15)
ที่ดินผืนนี้กว้าง: 5 เมตร   ยาว: 15 เมตร
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางวา
print(res)
None
def land(width,long):
    cal = width * long
    cal_wa = cal/4
    print(f'ที่ดินผืนนี้กว้าง: {width} เมตร   ยาว: {long} เมตร')
    print(f'ที่ดินผืนนี้มีพื้นที่: {cal} ตารางเมตร')
    print(f'ที่ดินผืนนี้มีพื้นที่: {cal_wa} ตารางวา')
    return cal_wa
res = land(5,15)
SyntaxError: invalid syntax
>>> res = land(5,15)
ที่ดินผืนนี้กว้าง: 5 เมตร   ยาว: 15 เมตร
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางวา
>>> print(res)
None
>>> def land(width,long):
...     cal = width * long
...     cal_wa = cal/4
...     print(f'ที่ดินผืนนี้กว้าง: {width} เมตร   ยาว: {long} เมตร')
...     print(f'ที่ดินผืนนี้มีพื้นที่: {cal} ตารางเมตร')
...     print(f'ที่ดินผืนนี้มีพื้นที่: {cal_wa} ตารางวา')
...     return cal_wa
... 
>>> res = land(5,15)
ที่ดินผืนนี้กว้าง: 5 เมตร   ยาว: 15 เมตร
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางวา
>>> print(res)
18.75
>>> def land(width,long,price=999888):
...     cal = width * long
...     cal_wa = cal/4
...     print(f'ที่ดินผืนนี้กว้าง: {width} เมตร   ยาว: {long} เมตร')
...     print(f'ที่ดินผืนนี้มีพื้นที่: {cal} ตารางเมตร')
...     print(f'ที่ดินผืนนี้มีพื้นที่: {cal_wa} ตารางวา')
...     return cal_wa * price
... 
>>> res = land(5,15)
ที่ดินผืนนี้กว้าง: 5 เมตร   ยาว: 15 เมตร
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางวา
>>> print(res)
18747900.0
>>> def land(width,long,price=999888):
...     cal = width * long
...     cal_wa = cal/4
...     print(f'ที่ดินผืนนี้กว้าง: {width} เมตร   ยาว: {long} เมตร')
...     print(f'ที่ดินผืนนี้มีพื้นที่: {cal} ตารางเมตร')
...     print(f'ที่ดินผืนนี้มีพื้นที่: {cal_wa} ตารางวา')
...     calprice = cal_wa * price
...     return 'ที่ดินผืนนี้ราคา: {:,.2f} บาท'.format(calprice)
... 
>>> res = land(5,15)
ที่ดินผืนนี้กว้าง: 5 เมตร   ยาว: 15 เมตร
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางวา
>>> print(res)
ที่ดินผืนนี้ราคา: 18,747,900.00 บาท
>>> land(5,15)
ที่ดินผืนนี้กว้าง: 5 เมตร   ยาว: 15 เมตร
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางวา
'ที่ดินผืนนี้ราคา: 18,747,900.00 บาท'
