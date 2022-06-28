def addnumbers(number1, number2):
	return number1 + number2

add_numbers = addnumbers(3,9)
print(f"Added numbers are eaqual to a total of {add_numbers}:  Fund you")


add_numbers2 = add_numbers + 24
print(add_numbers2)

#dictionaries
squares = {1:1, 2:4, 3:"Error", 4:16}
squares[8] = 64
squares[3] = 9

squares[9] = 81

print(squares)



#tuples


words = "Spam" "Eggs" "Sausages"
print(words[0])



#lists


my_num = [1,2,3,4,5]

my_num[0] = 9
print(my_num)



for i in range(len(my_num)):
	if my_num[i] > 0:
	   my_num[i] = 0
else:
	print(f"My lists are here {my_num}")


print(my_num)		




		
