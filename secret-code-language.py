import random 
import string

input1=input("Enter your massage\n")
input2=input1.split(" ")
cryptography=input("Do you want to code it or decode it? write encryption for coding it else decryption for decoding it\n")


if(cryptography=="encryption"):
    count=0
    for i in input2:
       count=count+1
    j=0
    if(count>1):
     for i in input2:
      msg=''.join(i)
      count2=0
      for i in msg:
       count2=count2+1
      if(count2>2):
        print(''.join(random.choices(string.ascii_lowercase, k=3))+msg[1:]+msg[0]+''.join(random.choices(string.ascii_lowercase, k=3)), end=' ' )
       
      else:
        print(msg[::-1], end=' ')
    else:
        k=input2[0]
        msg=''.join(k)
        count1=0
        for i in msg:
          count1=count1+1
        if(count1>2):
          print(list[0]+msg[1:]+msg[0]+list[1], end=' ')   
        else:
            print(msg[::-1], end=' ')
        
elif(cryptography=="decryption"):
    count=0
    for i in input2:
      count=count+1
    if(count>1):
      for i in input2:
       msg=''.join(i)
       count1=0
       for i in msg:
         count1=count1+1
       if(count1>2):
          msg=msg[3:-3]
          print(msg[-1]+msg[:-1], end=' ')
       else:
          print(msg[1]+msg[0], end=' ')
    else:
         k=input2[0]
         msg=''.join(k)
         count1=0
         for i in msg:
          count1=count1+1
         if(count1>2):
          msg=msg[3:-3]
          print(msg[-1]+msg[:-1], end=' ')
         else:
          print(msg[1]+msg[0], end=' ')







        

    

