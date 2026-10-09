people = int(input("How many people are coming for cookout ?"))
perpeoplehotdogs = int(input("How many hotdogs per person ?"))
hotdogs = int((perpeoplehotdogs*people/10)+1)
hotdogbuns = int((perpeoplehotdogs*people/8)+1)
print("min no. of hotdogs required = ", hotdogs)
print("min no. of hotgo buns required = ", hotdogbuns)
lefthotdog = (hotdogs*10)-perpeoplehotdogs*people
lefthotdogbuns = (hotdogbuns*8)-perpeoplehotdogs*people
print(lefthotdog)
print(lefthotdogbuns)