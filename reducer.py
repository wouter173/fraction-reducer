import deco
import math

def Reduce(inp):
  inp = inp.split("/")
  if len(inp) != 2:
    return print("invalid input")
  
  numerator = int(inp[0])
  denominator = int(inp[1])

  common_Divisor = Differance(Primes(numerator), Primes(denominator))
  try:
    numerator = numerator / common_Divisor
    denominator = denominator / common_Divisor
    denominator, numerator = int(denominator), int(numerator)
  except:
    pass

  if denominator == 1:
    print(deco.color("{} => {}".format("/".join(inp), numerator), "green"))
  else:
    print(deco.color("{} => {}/{}".format("/".join(inp), numerator, denominator), "green"))

def Primes(number): 
  out_list = []
  i = 2
  
  while number > 1:
    if number % i == 0:
      out_list.append(i)
      number = number / i
      i -= 1

    i += 1

  return out_list

def Differance(list_one, list_two):

  finish = []

  for index_one, number_one in enumerate(list_one):
    for index_two, number_two in enumerate(list_two):
      if number_one == number_two:
        finish.append(number_one)
        del list_two[index_two]

  multiplied = 0
  for number in finish:
    if multiplied == 0:
      multiplied = number
    else:
      multiplied = multiplied * number

  return(multiplied)

