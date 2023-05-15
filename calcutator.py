def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

while True:
  print("Select operation.")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")

  operation = input("Select operation(1/2/3/4): ")

  if operation in ('1', '2', '3', '4'):
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    if operation == '1':
      print(first_number, "+", second_number, "=", add(first_number, second_number))
    elif operation == '2':
      print(first_number, "-", second_number, "=", subtract(first_number, second_number))
    elif operation == '3':
      print(first_number, "*", second_number, "=", multiply(first_number, second_number))
    elif operation == '4':
      print(first_number, "/", second_number, "=", divide(first_number, second_number))

    next_calculation = input("Continue calculation? (Y/N): ")
    if next_calculation == "N":
      break
  else:
    print("Invalid input!")