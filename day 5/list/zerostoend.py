numbers = [0, 1, 0, 3, 12, 0, 5]
result =[]
count =0
for num in numbers:
    if num ==0:
        count+=1
    else:
        result.append(num)
# print(result)  

for i in range(count):
    result.append(0)
print(result)  
   