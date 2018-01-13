
print("welcome to my third program")

print("------------------------------------------------")

#here i am going to implement a program with a nested if else statements

name= input("please enter the name of the position of the person in mind")
person_name= input("please ente the name of the person to be identified")

if (name=="senior-executive"):
   if (person_name=="surya" or "hanuhitha"):
       print("Welcome", person_name," you may proceed with the signing in")
   print("The name entered is of the directory and may be proceeded in")

elif (name== "project manager"):
     if (person_name== "dad"):
        print("Welcome", person_name,"You are our valuable project manager please go on with your work")
     print("The name enterd is in the directory 2.2.3 and is part of our directory")

elif ( name=="teacher"):
     if (person_name=="mom"):
        print("Welcome",person_name," Ma'am you are our valuable employee please proceed")
     print("The name enterd is part of our 3.3.4 teaching program unit")

elif (name=="imp position"):
     if (person_name=="brother"):
        print("Welcome", person_name,"Please proceed on with your work kindly good sir")
     print("The employee is part of the 3.4.5 unit of the development unit")


else:
           print("please get away fromt the server")
