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
    if len(val) !=4:
        print("input 4 numbers")
        continue
    answer=''
    for i in range(4):
        if num4[i]== val[i]:
            answer += num4[i]
        else:                                                                               
            answer+='X'
    print('->'+ answer)
