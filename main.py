p1 = input("Please enter the name of one person:")
p1_age = int(input("Please enter the name of {}'s age:".format(p1)))

p2 = input("Please enter the name of one person:")
p2_age = int(input("Please enter the name of {}'s age:".format(p2)))

if p1_age < p2_age:
  print (p1, "is younger")
elif p1_age > p2_age:
  print (p1, "is older")
elif p1_age == p2_age:
  print(p1, "and", p2, "are the same age")


'''
Please enter the name of one person: Craig
Please enter Craig's age: 45
Please enter the name of another person: Mark
Please enter Mark's age: 49
Craig is younger

Please enter the name of one person: Judith
Please enter Judith's age: 74
Please enter the name of another person: Bo
Please enter Bo's age: 74
Judith and Bo are the same age
'''