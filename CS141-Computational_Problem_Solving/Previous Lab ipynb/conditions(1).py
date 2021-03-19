value = int(input("Enter an integer: "))

if value < 0:
  if value > -1:
    print('A')
  elif value > 0:
    print('B')
  else:
    print('C')
else:
  if value > 100:
    print('D')
  if value > 150:
    print('E')
    if value > 200:
      print('F')
    else:
      print('G')
  elif value < 125:
    print('H')
  print('I')



