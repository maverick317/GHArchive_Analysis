
def square_of_digits(number):
	number = int(number)
	sum = 0
	while number>0:
		digit = number%10
		number = int(number/10)
		sum += digit**2

	return sum

def get_number(num_str):
	if len(num_str) == 0:
		print("Invalid input string")
		return -1
	num_str = " ".join(num_str.split())
	if " " in num_str:
		print("Invalid input string")
		return -1
	if "." in num_str:
		print("Please input integer")
		return -1

	number = int(num_str)
	if number < 1 or number > 10**9:
		print("Number not in valid range [1,10^9]")
		return -1

	return number

def main():
	convergence_list = [None] * 730
	# 730 because largest sum = 9*(9**2)

	common_set = {4, 37, 42, 16, 145, 20, 89, 58}
	# From part 1 of the problem

	convergence_list[1] = True
	for c in common_set:
		convergence_list[c] = False

	input_string = str(input("Enter number: "))
	number = get_number(input_string)

	if number == -1:
		return()

	upper_limit = min(730,number+1)
	for i in range(2,upper_limit):
		s_temp=[]
		sq = i
		while(sq not in s_temp):
			# print (sq)
			if convergence_list[sq] == False:
				for s in s_temp:
					convergence_list[s] = False
				break
			elif convergence_list[sq] == True or sq == 1:
				for s in s_temp:
					convergence_list[s] = True
				break
			else:
				s_temp.append(sq)
				sq = square_of_digits(sq)

	relevant_list = convergence_list[1:number+1]
	total = relevant_list.count(True)
	if number >= 730:
		for i in range(730,number+1):
			sq = square_of_digits(i)
			if convergence_list[sq] == True:
				total += 1


	print("Total numbers whose sum of squares of digits converge to 1 :", total)

if __name__ == "__main__":
    main()