# Recusion Introduction

# fibonacci numbers
#
#  positions
#  0    1     2     3      4      5      6   ....
#
#  values
#  0    1     1     2      3      5      8   ....


def fibonnaci(position):
  if position == 0:
    return 0
  if position == 1:
    return 1
  else:
    return fibonnaci(position - 1) + fibonnaci(position - 2)

# fib(2) = fib(1) + fib(0)
#        = 1      + 0
#
# fib(3) = fib(2) + fib(1)
#        = (fib(1) + fib(0)) + fib(1)
#        = (1 + 0) + 1
#        = 2


# Recursion Structure
'''
def recursive_function():
  # base cases
  if (case_1):
    return primitive
  if (case_2):
    return primitive:
    ...
  
  # recursive case
     - call our recursive function again
     - normally we are going to call it with smaller numbers

'''

#  never stops becaause no basse cases
def no_base_cases(num):
  return no_base_cases(num + 1)

# never stops becausse we don't make the problem smaller
def numbers_dont_get_smaller(num):
  if num == 0:
    return 0
  if num == 1:
    return 1
  else:
    return numbers_dont_get_smaller(num)