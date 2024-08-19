cars = ['toyota','honda','benz']
cars.append('byd')
print(cars)
cars.remove('honda')
print(cars)

cars.insert(0,'tesla')
print(cars)
print(cars[0])
print(cars[1])

for c in cars:
    print(c)

print(*cars)

for i,c in enumerate(cars):
    print(i,c)

for i,c in enumerate(cars, start=0):
    print('ลำดับที่่ {} {}'.format(i,c))
    print('--------------------------------')


for i,c in enumerate(cars, start=1):
    print('ลำดับที่่ {} {}'.format(i,c))

i = 0
for c in cars:
    print(i+1, c)
    i = i + 1

print(cars)
cars[1] = 'isuzu'
print(cars)

del cars[2]
print(cars)

len(cars)
print(len(cars))

print(ord('ก'))
print(ord('ข'))
print(ord('ฃ'))

print(chr(ord('ฃ')))

for i in range(10):
    print(chr(3585+i))
    print('---------------')
    
for i in range(3585,3595):
    print(chr(i))

number = {'1001':'สมชาย', '1002':'สมศรี','1003':'สมศักดิ์'}
print(number['1001'])

for n in number:
    print(n)

for n in number.items():
    print(n)

for n in number.items():
    print(n[1])

for n in number.keys():
    print(n)

for n in number.values():
    print(n)

def hello():
    print('hello world')
    print('hello world')
    print('hello world')
    print('hello world')
    print('hello world')

hello()

def hello(q):
    for i in range(q):
        print('hello world')

hello(10)
        
