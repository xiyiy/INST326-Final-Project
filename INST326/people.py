"""A template for a python script deliverable for INST326.
Driver: Instructor Daniel Pauw
Navigator: None
Assignment: Template INST326
Date: 1_26_23
Challenges Encountered:
Collaborated with: Xiyi Yang, Kennedy K. Bydume, Kibron Tesfatsion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import re

def parse_name(text):
  """Uses regular expressions to capture first and last name of the person
  
  Args: 
    text (string): represents a single line of the file

  Returns: 
    tuples with first and last names
  """
  firstName = re.search(r"^\w+", text).group()
  lastName = re.search(r"\w{4,8}(?=\s\d)", text).group()
  return firstName, lastName

def parse_address(text):
  """Uses regular expressions to capture street, city and state of the person
  
  Args: 
    text (string): represents a single line of the file

  Returns: 
    an address object with street, city and state
  """
  street = re.search(r"\d+\s.+(?=\s\w+\s+[A-Z]{2})", text).group()
  city = re.search(r"\w+ (?=[A-Z]{2})", text).group(0)
  state = re.search(r"[A-Z]{2}", text).group()
  return Address(street, city, state)

def parse_email(text):
  """Uses regular expressions to capture the email of the person 
  
  Args: 
    text (string): represents a single line of the file

  Returns: 
    email identified
  """
  email = re.search(r"\S+\w+$", text).group()
  return email

class Address:
  """ This class gets the Employee's address (street, city and state)  
  Attributes:
    street: Employee's street
    city: Employee's city
    State: Employee's State """
  
  def __init__(self, street, city, state):
    """Define a __init__() and sets street, city, and state to their
    corresponding parameters
    Args: 
      street(str): employee's street    
      city(str): employee's city
      state(str): employee's state
    Side effects:
      sets attributes street, city and state. """
    self.street = street
    self.city = city
    self.state = state
    
class Employee:
  """ This class uses the functions that we defined before to get the
    full information (name, address, email) of an Employee.
  Attributes:
    first_name: The first name of the employee 
    last_name: The last name of the employee 
    address: The address of the employee
    email: The email of the employee 
  """
  
  def __init__(self, row):
    """Uses functions to parse each row of the file
  Args: 
    row: a row of the file that we are parsing
  Side Effects:
    Sets attributes first_name, last_name, adress and email
    to functions parse_name, parse_address and parse_email. """
    self.first_name = parse_name(row) [0]
    #second elem of name tuple
    self.last_name = parse_name(row) [1]
    self.address = parse_address(row)
    self.email = parse_email(row)

def main(path):
  """This function extracts data from the file
  
  Args: 
    path: path to the file

  Returns: 
    employee_list (list)
  """
  employee_list = []
  with open(path, 'r') as file:
    for line in file:
      worker = Employee(line)
      employee_list.append(worker)
  
  return employee_list
 
if __name__ == "__main__":
  path = "people.txt"
  employee_list = main(path)
  for e in employee_list:
    print(f"\nFirst Name: {e.first_name}")
    print(f"\nLast Name: {e.last_name}")
    print(f"\nStreet: {e.address.street}")
    print(f"\nCity: {e.address.city}")
    print(f"\nState: {e.address.state}")
    print(f"\nEmail: {e.email}")