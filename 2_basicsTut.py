friends = ["Paul","Mihai","Octav","Andrei"]
number =[4,8,15,16,23,42]
print(friends[2])
print(friends[-1])
print(friends[1:])
friends[1] = "Sose"
print(friends[1])
friends.extend(number)
friends.append(123)
friends.insert(1,"creed")
friends.remove(4)
friends.clear()
friends.pop()
print(friends.index("Octav"))
print.count("Sose")
friends.sort()
friends.reverse()
friends2=friends.copy()
print(friends)
coordinates =(4,5)
coordinates[1] = 10
print(coordinates[0])