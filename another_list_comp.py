# For all the numbers between 1 and 100(including 100), create a variable called answer, which contains a list with all the numbers that are divisible by 12.  (12, 24, etc)

answer = [num for num in range(1,101) if num % 12 == 0]

print(answer)