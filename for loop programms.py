# For Loop using basic Program
for i in range(1,10):
    print(i)

# For Loop using get the input from user Program
name= input("what is your name? ")
for i in name:
    print(i)


# For Loop using get the input from user only want alphabets
mail= input("what is your mail id? ")
for i in mail:
    if i>='a' and i<='z':
        print(i)


# For Loop using get the input from user only want numbers
mail= input("what is your mail id? ")
for i in mail:
    if i>='0' and i<='9':
        print(i ,end = ",")

# For Loop using get the input from user to find count of alphabets
name= input("enter any statement")
count=0
for i in name:
    if i>='a' and i<='z':
        count += 1
else:
    print("no of alphabets present is", count)


# For Loop using get the input from user to find count of words:
name = input("enter any statement")
count=0
for i in name:
    if i==" ":
        count += 1
else:
    print("no of words in sentence is", count+1)


# For Loop using get the input from user to find count of sentence:
name = input("enter any statement")
count=0
for i in name:
    if i==".":
        count += 1
else:
    print("no of sentence is", count+1)


# For Loop using get the input from user to find count of UPPER case and Lower case:
name = input("enter any statment ")
upper=0
lower=0
for i in name:
    if (i.islower()) :
        lower+= 1
    else:
        upper+=1
print("no of upper is", upper )
print("no of lower is", lower)


# For Loop using get the input from user to find count of UPPER case and Lower case: (another method)
name= input("enter any statement")
upper=0
lower=0
for i in name:
    if i>='a' and i<='z':
        upper += 1
    if i>='a' and i<='z':
        lower += 1
else:
    print("no of caps alphabets present is", upper)
    print("no of small alphabets present is", lower)
