
def add(firstNumber,*numbers):
  for i in numbers:
    firstNumber +=i
  print(firstNumber)

add(1,2,3,4)