from cmath import pi
import re
import math

class MyMath():
  """This is the class to calculate standard deviation."""
  def __init__(self):
    """This function to initialize the class."""
    try:
      self.num_list = []
    except Exception as e:
      print("There is error when creating the number list.")

  def calc_average(self, num_list) -> float:
    """This function calculates the average of a list of numbers."""
    sum = 0
    try:
      if (len(num_list) == 0):
        raise ZeroDivisionError("The list is empty. Cannot divide by 0.")
      for number in num_list:
        sum = sum + number
        avg = sum / len(num_list)
    except ZeroDivisionError as e:
      print("Error: ", e)

    return float("{:.3f}".format(avg))

  def std_dev(self, num_list) -> float:
    """This function calculate the standard deviation of a list of numbers."""
    total_square = 0

    try:
      if (len(num_list) == 1):
        raise Exception("A list with a single element cannot have standard deviation.")

      for number in num_list:
        total_square += (number - self.calc_average(num_list)) ** 2

        standard_deviation = math.sqrt(total_square / (len(num_list) - 1))

    except Exception as e:
      print("Error: ", e)

    return float("{:.3f}".format(standard_deviation))

  def format_input(self, inputlist: str) -> list:
    """This function will format the input list and convert it to a list of numbers."""
    try:
      self.num_list = inputlist.split()
      if ',' in inputlist:
        raise Exception("Please use space as your divider between numbers.")
    except Exception as e:
      print("Error: ", e)

    try:
      if bool(re.search(r'\d', inputlist)) :
        for i in range(len(self.num_list)):
          self.num_list[i] = int(self.num_list[i])
      else:
        raise Exception("Please enter numbers only.")
    except Exception as e:
      print ("Error: ", e)

    return self.num_list

  def find_max(self, inputlist) -> float:
    """This function will find the max value element in the list."""
    try:
      max_value = max(inputlist)
    except Exception as e:
      print("There is no max value.")

    return max_value

# input a list of numbers
input_value = input("Please enter your list of numbers separated by space: \n")

# set up the instance of the class and add input value to the number list
instance = MyMath()

# print out the average and standard deviation
format_list = instance.format_input(input_value)

try:
  print('Average: ' + str(instance.calc_average(format_list))  + ' + standard deviation: ' + str(instance.std_dev(format_list)) + ' + max value: ' + str(max(format_list)) + '.')
except Exception as e:
  print("Please check the above errors.")