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

	"""
	It is observed that series of repeated sum of squared digits
	of any number always converge to a single digit number.
	So it is not necessary to find this series for all numbers.
	As an optimal approach, we calculate this series for numbers
	from 1 to 9 and find the set of numbers S where the series
	gets stuck in.
	"""
	number = 9

	# series_dict stores the numbers whose sum of squared digits do not converge to 1.
	# key: number, value: list of sum of squared digits.
	# Example: series_dict = { 3: [3, 9, 81, 65, 61, 37, 58, 89, 145, 42, 20, 4, 16, 37] }

	series_dict = {}

	for i in range(1, number+1):

		# s_temp is a list to store the sum of squared digits of a number.
		# It is initialized with the number itself. squares will be appended to it.
		s_temp = [i]
		sq = sum_of_squared_digits(i)

		while sq not in s_temp:
			s_temp.append(sq)
			sq = sum_of_squared_digits(sq)

		# if a number's series converges to 1, we do not add that to series_dict
		if s_temp[-1] != 1:
			series_dict[i] = s_temp

	# convergence_set: set of 8 numbers that the sum of squared digits converge to.
	# we do set intersection on the series_dict values to identify the set.
	convergence_set = set()

	for series in series_dict.values():

		if len(convergence_set) == 0:
			convergence_set = set(series)
		else:
			convergence_set = convergence_set.intersection(set(series))

	# The convergent set has 8 numbers {4, 37, 42, 16, 145, 20, 89, 58}.
	# But as per the question, the set S doesn't include 89. Hence removing 89.
	# Because of the set operation, ordering of these numbers isn't preserved.
	print("Set S: ", convergence_set - {89})


if __name__ == "__main__":
	main()