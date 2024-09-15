def swap1(a,b):
     a = a^b
     b = a^b
     a = a^b
     print("After swaping a =,",a,"and b = ",b)
swap1(45,23)
def swap2(a,b):
     a = (a&b)+(a|b)
     b = a +(~b)+1
     a = a+(~b)+1
     print("After swaping a =,",a,"and b = ",b)
swap2(45,23)