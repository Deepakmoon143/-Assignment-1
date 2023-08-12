user = int(input("enter the value"))
even_number = 0
odd_number = 0
for i in range(1,user+1):
    if i %2==0:
        even_number+=1
    else:
        odd_number+=1
print("number of even_numbers: ",even_number)
print("number of odd_numbers: ",odd_number)
