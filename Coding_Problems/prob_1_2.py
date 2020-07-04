#!/usr/local/bin/python
# encoding: utf-8


def sum_of_squared_digits(number):
	"""
	Returns the sum of squares of the digits of a number
	"""
	sum = 0
	while number > 0:
		digit = number%10
		number = number//10
		sum += digit**2

	return sum


def main():

	# Used to store the input number
	number = 0

	try:
		number = int(input("Enter number: "))
	except ValueError:
		raise ValueError("Not a valid number. Must be an Integer")

	if number < 0 or number > 10**9:
		print("Number out of range")
		return

	# Sum of squares of 999,999,999 is 9**3 = 729.
	# So the instead of calculating a new series for 999,999,999 we could
	# follow the already evaluated series of 729 to find if it converges to 1 or not.
	# Similarly for every number > 729, we can calculate sum of squared digits only once
	# and map it to a number <= 729.

	# convergence_list : list of size 730 with the index 0 not used for convenience.
	# Each element is initialized to None, and set to True if the number corresponding
	# to the index of the list converges to 1, and False otherwise.
	# That is, since 31 converges to 1, convergence_list[31] = True.
	convergence_list = [None] * 730

	# From part 1 of the problem
	common_set = {4, 37, 42, 16, 145, 20, 89, 58}

	# number 1 converges to 1. so set convergence_list[1] = True
	convergence_list[1] = True

	# all numbers in common_set do not converge to 1
	for c in common_set:
		convergence_list[c] = False

	# if the number > 730, set upper limit to 730
	upper_limit = min(730, number+1)

	# To store how many numbers converge to 1
	count = 1

	for i in range(2,upper_limit):

		# s_temp is a list to store the sum of squared digits of a number.
		s_temp = []
		sq = i

		while sq not in s_temp:
			# To handle if the number is already known to not converge to 1
			if convergence_list[sq] == False:
				# All the preceding numbers in the list will also not converge to 1
				for s in s_temp:
					convergence_list[s] = False
				break

			# To handle if the number is already known to converge to 1
			elif convergence_list[sq] == True or sq == 1:
				count += 1
				# All the preceding numbers in the list will also converge to 1
				for s in s_temp:
					convergence_list[s] = True
				break

			# If the number is never encountered before
			else:
				s_temp.append(sq)
				sq = sum_of_squared_digits(sq)

	# As previously mentioned, for numbers > 729 we just need to
	# calculate sum of squares once, whatever this value is, we already know
	# if it'll converge to 1 or not, as it is present in convergence_list
	if number >= 730:
		for i in range(730, number+1):
			sq = sum_of_squared_digits(i)
			if convergence_list[sq] == True:
				count += 1


	print("Numbers that converge to 1 :", count)

if __name__ == "__main__":
    main()