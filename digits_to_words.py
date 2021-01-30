ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve','thirten', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['ten','twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

position = input("Enter a number from 01-99 using digits: ")

position_int = int(position)

first_digit = int(position[0])
second_digit = int(position[1])

for item in range(1):
  if position_int > 99:
    print("Too high.")
  elif first_digit == 0 or first_digit == 1:
    print(ones[position_int -1])
  elif second_digit == 0:
    print(tens[first_digit - 1])
  else:
    print((tens[first_digit -1]) + "-" +(ones[second_digit -1]))
