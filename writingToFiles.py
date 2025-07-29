employee_file=open("employees.txt","a")

employee_file.write("Toby-Human resources")
employee_file.write("\n Kelly-customer service")

print(employee_file.read())
employee_file.close()