def cube(num):
   return num*num*num



result =cube(4)
print(cube(3))    
print (result)
is_male=True 
is_tall = False 

if is_male or is_tall :
   print("you are a male or tall ")
elif is_male and not(is_tall):
   print("u are a short male")
elif not(is_male)and is_tall:
   print("u are a tall woman ")
else: print("u female and small ")
if is_male and is_tall :
   print("you are a male and tall ")
else: print("u female and maybe even  small ")
def maxnum(num1,num2,num3):
    if num1 >= num2 and num1 >=num3:
      return num1
    elif num2 >= num1 and num2 >= num3:
      return num2
    else:
      return num3
print(maxnum(3,455,5))