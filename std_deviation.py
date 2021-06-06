import csv
import math
with open ('data.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)


data=file_data[0]
print(data)

#finding mean
def mean(data):
    n=len(data)
    total=0
    for x in data :
        total+=int(x)
    mean=total/n
    print(mean)
    return mean

# substracting and squaring the values
square_list=[]     
for number in data:
    a=int(number)-mean(data)
    a=a**2
    square_list.append(a)
print(square_list)

#getting sum
sum=0
for i in square_list:
    sum=sum+i
print(sum)
#dividing the sum/n-1
result=sum/(len(data)-1)        
print(result)
#sqrt of sum
std_deviation=math.sqrt(result)

print(std_deviation)
    
