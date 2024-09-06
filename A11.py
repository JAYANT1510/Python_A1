'''
Created on 6 Sept 2024

@author: ABHISHEK
'''
file=open("F:/Projects/A6/C1/Scripts/File_S1_A.sql","r+")
data=file.read()
print(data)
data_len=len(data)
print("\nData in file = ",data_len)
list1=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
j=-1 # this variable is for whole data string length
j1=0 # this variable is for address, public key  and private key length calculation
j2=0 # this variable is for space calculation
key='ad' # ad for address
file.write("\n")
for i in data:
    if i in list1:
        if(j==-1):
            file.write("(\"")
            file.write(i)
            j=j+1
            j1=j1+1
        else:
            file.write(i)
            j=j+1
            j1=j1+1
    elif(i=='\n'):
        file.write("\"),\n(\"")
        j=j+1
        j1=0
        j2=0
        key='ad'
    elif(i==" "):
        if(j<data_len):
            if(j2==0):
                if(key=='ad' and j1==42):
                    file.write("\",\"")
                    file.write(i)
                    j=j+1
                    j2=j2+1
                    key='pu' # pu for public key
                    j1=0 # setting j1=0 for public key length calculation
                elif(key=='pu' and j1==68):
                    file.write("\",\"")
                    file.write(i)
                    j=j+1
                    j1=0
                    j2=j2+1
                    key='pk' # pk for private key 
            else:
                if(j2>0):
                    if data[j+1] in list1: # this condition checks that this is the final white space and again characters will start
                        file.write(i)
                        j=j+1
                        j2=0 
                    else:
                        file.write(i)
                        j=j+1
                        j2=j2+1
        else:
            if(j==data_len):
                file.write("\"),")
                file.write(i)
                    
file.close()                        
              
              
              
              
              
              
              
              
                
              