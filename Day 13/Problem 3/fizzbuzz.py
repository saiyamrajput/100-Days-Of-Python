'''
for num in range(1, 101):
  if num % 3 == 0 or num % 5 == 0:
    print("FizzBuzz")
  if num % 3 == 0:
    print("Fizz")
  if num % 5 == 0:
    print("Buzz")
  else:
    print([num])
'''

#   Fixed Code

for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print(num)
