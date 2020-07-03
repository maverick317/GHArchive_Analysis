import copy

number = 10
series_dict = {}

def square_of_digits(number):
	number = int(number)
	sum = 0
	while number>0:
		digit = number%10
		number = int(number/10)
		sum += digit**2

	return sum


for i in range(2,number+1):
	s_temp=[]
	sq = i
	end_at_1 = False
	while(sq not in s_temp):
		s_temp.append(sq)
		if sq == 1:
			end_at_1 = True
			break
		sq = square_of_digits(sq)
		# print(sq, end=" ")

	if not(end_at_1):
		series_dict[i]=set(s_temp)
		
	# print("")

common_set = set()
cs_initialized = False
for num,series in series_dict.items():
	# print(num,series)
	if not(cs_initialized):
		common_set = copy.deepcopy(series)
		cs_initialized = True
	else:
		common_set = common_set.intersection(series)

	# print("CS: ",common_set)
print("S:",common_set)