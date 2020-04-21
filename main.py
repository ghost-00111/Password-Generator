

#importing module
import CreatePassword as MyPassword

while 1:
	PassLength=int(input("Enter the length for your password:"))
	print(MyPassword.Generate(PassLength))
	response=input("Do you want to generate again? (yes,no) :")
	if response.lower()=="yes":
		continue
	elif response.lower()=="no":
		break
	else:
		break