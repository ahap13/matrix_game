"""Numpy Matrix Game for SDEV300 Lab 4
User enters and validates phone number and ZIP+4
Then user enters 2 3x3 matrices and select whether to
add, subtract, matrix multiplication, and element by
element multiplication. Program computes and returns
results and the transpose of results, the mean of the
rows for the results and the mean of the columns for
the results"""
import sys

import numpy as np

def yes_no_validation(y_n):
    """Validates user entered y or n"""
    if y_n.upper() == "Y" or y_n.upper() == "N":
        return True
    return False

def phone_num_validation(num):
    """Ensures Number is 10 digits, plus dashes in appropriate spots"""
    if len(num) == 12 \
        and num[:3].isdigit() \
        and num[3] == "-" \
        and num[4:7].isdigit() \
        and num[7] == "-" \
        and num[8:].isdigit():
        return True

    return False

def zip_validation(zip_code):
    """Ensures ZIP is 5 digits, then dash, then additional 4"""
    if len(zip_code) == 10 \
        and zip_code[:5].isdigit() \
        and zip_code[5] == "-" \
        and zip_code[7:].isdigit():
        return True

    return False

def mtrx():
    """Gets input from user to get 3x3 matrix"""

    #Strings to hold user input
    a = input("Enter 3 x 3 matrix:\n")
    b = input()
    c = input()

    ra = []
    rb = []
    rc = []

    #For looping to get rid of spaces in input
    for i in range(0, len(a), 2):
        ra.append((int(a[i])))

    for i in range(0, len(b), 2):
        rb.append((int(b[i])))

    for i in range(0, len(c), 2):
        rc.append((int(c[i])))

    matr = np.array([ra, rb, rc])

    return matr

#============== Initial Coninutation Validation =================
user_input1 = input(("******** Welcome to the Python Matrix Application ********\n"
      "Do you want to play the Matrix Game? Y or N:\n"))

while not yes_no_validation(user_input1):
    user_input1 = input("Please enter Y or N:\n")

if user_input1.upper() == "N":
    sys.exit()

#================ Phone number validation ======================
phone_num_input = input("Please enter phone number (XXX-XXX-XXXX):\n")

while not phone_num_validation(phone_num_input):
    phone_num_input = input("Please use XXX-XXX-XXXX format:\n")

#================= ZIP Validation ==========================
zip_input = input("Please enter ZIP + 4 (XXXXX-XXXX):\n")

while not zip_validation(zip_input):
    zip_input = input("Please use XXXXX-XXXX format:\n")

#================= Matrices =======================

m1 = mtrx()
m2 = mtrx()

print("First 3 x 3 matrix:")
print(m1)
print("Second 3 x 3 matrix:")
print(m2)

#=============== Matrix Operations ====================
op_input = int(input("Select from the following matrix operations:\n"
                 "1. Addition\n"
                 "2. Subtraction\n"
                 "3. Multiplication\n"
                 "4. Element by element multiplication\n"))

while op_input > 4 or op_input < 1:
    op_input = int(input("Please enter between 1-4:\n"))

if op_input == 1:
    result = np.add(m1, m2)
if op_input == 2:
    result = np.subtract(m1, m2)
if op_input == 3:
    result = np.matmul(m1, m2)
if op_input == 4:
    result = np.multiply(m1, m2)

print(result)
print("Transpose of result is:\n",
      result.transpose())

#============== Row and Column Means for Matrix ==================
row_a_mean = (result[0,0] + result[0,1] + result[0,2]) / 3
row_b_mean = (result[1,0] + result[1,1] + result[1,2]) / 3
row_c_mean = (result[2,0] + result[2,1] + result[2,2]) / 3
column_a_mean = (result[0,0] + result[1,0] + result[2,0]) / 3
column_b_mean = (result[0,1] + result[1,1] + result[2,1]) / 3
column_c_mean = (result[0,2] + result[1,2] + result[2,2]) / 3

print("The row means are:\n",
      row_a_mean, row_b_mean, row_c_mean)
print("The column means are:\n",
      column_a_mean, column_b_mean, column_c_mean)

print("************ Thank you for playing the Matrix Game *************")
