import sys

try:
  from Sort import insertion_sort, selection_sort
except ImportError:
  print("THIS SUBMISSION WILL RECEIVE ZERO CREDIT. The grading environment is unable to locate your Sort.py or the expected functions contained within it.")
  sys.exit(1)
  
if __name__ == '__main__':
  iarr1 = [3]

  sarr1 = [3]
  
  try:
    insertion_sort(iarr1)
    selection_sort(sarr1)
  except NameError:
    print("THIS SUBMISSION WILL RECEIVE ZERO CREDIT. The grading environment is unable to call your sorting functions because they are not named as specified.")
    sys.exit(2)
  except TypeError:
    print("THIS SUBMISSION WILL RECEIVE ZERO CREDIT. The grading environment is unable to call your sorting functions because they take an incorrect number of parameters.")
    sys.exit(3)
  print("If this is the only output you see, then our grading program should be able to access your functions.")
