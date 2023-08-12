user = int(input("enter the value"))
even_num = 0
odd_num = 0
for i in range(1,user+1):
    if i %2==0:
        even_num+=1
    else:
        odd_num+=1
print("number of even_numbers: ",even_num)
print("number of odd_numbers: ",odd_num)