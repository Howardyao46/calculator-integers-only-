operation = input('Type an operation. / = division, * = multiplication, +, or -   ')
number1 = int(input('Type a number: '))
number2 = int(input('Type another number: '))

if operation == '/':
  if number2 == 0:
    print('Error: Division by 0')
  elif number1 % number2 == 0:
    print('The quotient is', int(number1 / number2))
  else:
    print('The quotient is', number1 / number2)
elif operation == '*':
  print('The product is', number1 * number2)
elif operation == '+':
  print('The sum is', number1 + number2)
elif operation == '-':
  print('The difference is', number1 - number2)
else:
  print()
  print('I don\'t understand! Check your operation')
  print('Your operation answer:', operation)
