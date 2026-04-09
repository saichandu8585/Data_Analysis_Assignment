str=input("enter the string:")
result=""
for letter in str:
    if letter not in result:
       result+=letter
print(result)