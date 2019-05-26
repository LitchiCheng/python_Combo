import random
odd_random_list = [0] * 12      # 12 is the len of list
# the first method
odd_random_list = [random.randint(0, 50) * 2 + 1 for i in range(12)]      #2n+1, the 50 is the range of odd number
print(odd_random_list)
odd_random_list = random.sample([i for i in range(100) if i % 2 == 1], 12)          #list the odd number of a range, then sample the number 
print(odd_random_list)
