 #open("employees.txt","r")
#read
 #open("employees.txt","w")
#write
 #open("employees.txt","a")
#apen a aduauga la sfarsit
 #open("employees.txt","r+")
#read and write 
employee_file=open("employees.txt","r")
print(employee_file.readable()) #if there was a w we could have not read the file
print(employee_file.read())#spit out the file
print(employee_file.readline())#read a specific line
print(employee_file.readlines()[1])
for employee in employee_file.readlines():
    print(employee)

employee_file.close()
