import random 
numbers=[chr(i) for i in range(ord('0'),ord('9')+1)]
#print(numbers)

sample4 = random.sample(numbers,k=4)
num4=''.join(sample4)
print(num4)

while True:
    val = input()
    if val == num4:
        print('OK')
        break
    else:
        print('NG')
