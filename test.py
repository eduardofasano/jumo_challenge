import random
import sys
import os
import csv

#Manually inputed depending on the months received by accounting department
month1 = 'Mar'
month2 = 'Apr'

#Manually inputed depending on the networks received by accounting department
network1 = 'Network 1'
network2 = 'Network 2'
network3 = 'Network 3'

#Manually inputed depending on the networks received by accounting department
loan_product1 = 'Loan Product 1'
loan_product2 = 'Loan Product 2'
loan_product3 = 'Loan Product 3'

#Initialise Variables
n1m1p1_loan_count = 0
n1m1p1_loan_amount = 0.0
n1m1p2_loan_count = 0
n1m1p2_loan_amount = 0.0
n1m1p3_loan_count = 0
n1m1p3_loan_amount = 0.0
n1m2p1_loan_count = 0
n1m2p1_loan_amount = 0.0
n1m2p2_loan_count = 0
n1m2p2_loan_amount = 0.0
n1m2p3_loan_count = 0
n1m2p3_loan_amount = 0.0

n2m1p1_loan_count = 0
n2m1p1_loan_amount = 0.0
n2m1p2_loan_count = 0
n2m1p2_loan_amount = 0.0
n2m1p3_loan_count = 0
n2m1p3_loan_amount = 0.0
n2m2p1_loan_count = 0
n2m2p1_loan_amount = 0.0
n2m2p2_loan_count = 0
n2m2p2_loan_amount = 0.0
n2m2p3_loan_count = 0
n2m2p3_loan_amount = 0.0

n3m1p1_loan_count = 0
n3m1p1_loan_amount = 0.0
n3m1p2_loan_count = 0
n3m1p2_loan_amount = 0.0
n3m1p3_loan_count = 0
n3m1p3_loan_amount = 0.0
n3m2p1_loan_count = 0
n3m2p1_loan_amount = 0.0
n3m2p2_loan_count = 0
n3m2p2_loan_amount = 0.0
n3m2p3_loan_count = 0
n3m2p3_loan_amount = 0.0

# First attempt at getting data from the loans.csv file
loans_file = open("loans.csv", "r+")

text_in_file = loans_file.read()
print(text_in_file)

#Attempt at getting data from the loans.csv file using csv module
with open('loans.csv', 'r') as input, open('output.csv', 'w') as output:
    loans_file = csv.reader(input, delimiter=',', quotechar="'")
    output_file = csv.writer(output, delimiter=',', quotechar="'")

    for row in loans_file:
        # Network 1
        # Month 1
        if row[1] == network1 and row[2][3:6] == month1 and row[3] == loan_product1:
            n1m1p1_loan_count += 1
            n1m1p1_loan_amount = n1m1p1_loan_amount + float(row[4])
        elif row[1] == network1 and row[2][3:6] == month1 and row[3] == loan_product2:
            n1m1p2_loan_count += 1
            n1m1p2_loan_amount = n1m1p2_loan_amount + float(row[4])
        elif row[1] == network1 and row[2][3:6] == month1 and row[3] == loan_product3:
            n1m1p3_loan_count += 1
            n1m1p3_loan_amount = n1m1p3_loan_amount + float(row[4])

        # Month 2
        elif row[1] == network1 and row[2][3:6] == month2 and row[3] == loan_product1:
            n1m2p1_loan_count += 1
            n1m2p1_loan_amount = n1m2p1_loan_amount + float(row[4])
        elif row[1] == network1 and row[2][3:6] == month2 and row[3] == loan_product2:
            n1m2p2_loan_count += 1
            n1m2p2_loan_amount = n1m2p2_loan_amount + float(row[4])
        elif row[1] == network1 and row[2][3:6] == month2 and row[3] == loan_product3:
            n1m2p3_loan_count += 1
            n1m2p3_loan_amount = n1m2p3_loan_amount + float(row[4])

        # Network 2
        # Month 1
        elif row[1] == network2 and row[2][3:6] == month1 and row[3] == loan_product1:
            n2m1p1_loan_count += 1
            n2m1p1_loan_amount = n2m1p1_loan_amount + float(row[4])
        elif row[1] == network2 and row[2][3:6] == month1 and row[3] == loan_product2:
            n2m1p2_loan_count += 1
            n2m1p2_loan_amount = n2m1p2_loan_amount + float(row[4])
        elif row[1] == network2 and row[2][3:6] == month1 and row[3] == loan_product3:
            n2m1p3_loan_count += 1
            n2m1p3_loan_amount = n2m1p3_loan_amount + float(row[4])

        # Month 2
        elif row[1] == network2 and row[2][3:6] == month2 and row[3] == loan_product1:
            n2m2p1_loan_count += 1
            n2m2p1_loan_amount = n2m2p1_loan_amount + float(row[4])
        elif row[1] == network2 and row[2][3:6] == month2 and row[3] == loan_product2:
            n2m2p2_loan_count += 1
            n2m2p2_loan_amount = n2m2p2_loan_amount + float(row[4])
        elif row[1] == network2 and row[2][3:6] == month2 and row[3] == loan_product3:
            n2m2p3_loan_count += 1
            n2m2p3_loan_amount = n2m2p3_loan_amount + float(row[4])

        # Network 3
        # Month 1
        elif row[1] == network3 and row[2][3:6] == month1 and row[3] == loan_product1:
            n3m1p1_loan_count += 1
            n3m1p1_loan_amount = n3m1p1_loan_amount + float(row[4])
        elif row[1] == network3 and row[2][3:6] == month1 and row[3] == loan_product2:
            n3m1p2_loan_count += 1
            n3m1p2_loan_amount = n3m1p2_loan_amount + float(row[4])
        elif row[1] == network3 and row[2][3:6] == month1 and row[3] == loan_product3:
            n3m1p3_loan_count += 1
            n3m1p3_loan_amount = n3m1p3_loan_amount + float(row[4])

        # Month 2
        elif row[1] == network3 and row[2][3:6] == month2 and row[3] == loan_product1:
            n3m2p1_loan_count += 1
            n3m2p1_loan_amount = n3m2p1_loan_amount + float(row[4])
        elif row[1] == network3 and row[2][3:6] == month2 and row[3] == loan_product2:
            n3m2p2_loan_count += 1
            n3m2p2_loan_amount = n3m2p2_loan_amount + float(row[4])
        elif row[1] == network3 and row[2][3:6] == month2 and row[3] == loan_product3:
            n3m2p3_loan_count += 1
            n3m2p3_loan_amount = n3m2p3_loan_amount + float(row[4])

    #Define Rows
    n1m1p1_row = (network1 + ", " + month1 + ", " + loan_product1 + ", " + "Loan Count: " + str(n1m1p1_loan_count) + ", " + "Total Amount: " + str(n1m1p1_loan_amount))
    n1m1p2_row = (network1 + ", " + month1 + ", " + loan_product2 + ", " + "Loan Count: " + str(n1m1p2_loan_count) + ", " + "Total Amount: " + str(n1m1p2_loan_amount))
    n1m1p3_row = (network1 + ", " + month1 + ", " + loan_product3 + ", " + "Loan Count: " + str(n1m1p3_loan_count) + ", " + "Total Amount: " + str(n1m1p3_loan_amount))
    n1m2p1_row = (network1 + ", " + month2 + ", " + loan_product1 + ", " + "Loan Count: " + str(n1m2p1_loan_count) + ", " + "Total Amount: " + str(n1m2p1_loan_amount))
    n1m2p2_row = (network1 + ", " + month2 + ", " + loan_product2 + ", " + "Loan Count: " + str(n1m2p2_loan_count) + ", " + "Total Amount: " + str(n1m2p2_loan_amount))
    n1m2p3_row = (network1 + ", " + month2 + ", " + loan_product3 + ", " + "Loan Count: " + str(n1m2p3_loan_count) + ", " + "Total Amount: " + str(n1m2p3_loan_amount))

    n2m1p1_row = (network2 + ", " + month1 + ", " + loan_product1 + ", " + "Loan Count: " + str(n2m1p1_loan_count) + ", " + "Total Amount: " + str(n2m1p1_loan_amount))
    n2m1p2_row = (network2 + ", " + month1 + ", " + loan_product2 + ", " + "Loan Count: " + str(n2m1p2_loan_count) + ", " + "Total Amount: " + str(n2m1p2_loan_amount))
    n2m1p3_row = (network2 + ", " + month1 + ", " + loan_product3 + ", " + "Loan Count: " + str(n2m1p3_loan_count) + ", " + "Total Amount: " + str(n2m1p3_loan_amount))
    n2m2p1_row = (network2 + ", " + month2 + ", " + loan_product1 + ", " + "Loan Count: " + str(n2m2p1_loan_count) + ", " + "Total Amount: " + str(n2m2p1_loan_amount))
    n2m2p2_row = (network2 + ", " + month2 + ", " + loan_product2 + ", " + "Loan Count: " + str(n2m2p2_loan_count) + ", " + "Total Amount: " + str(n2m2p2_loan_amount))
    n2m2p3_row = (network2 + ", " + month2 + ", " + loan_product3 + ", " + "Loan Count: " + str(n2m2p3_loan_count) + ", " + "Total Amount: " + str(n2m2p3_loan_amount))

    n3m1p1_row = (network3 + ", " + month1 + ", " + loan_product1 + ", " + "Loan Count: " + str(n3m1p1_loan_count) + ", " + "Total Amount: " + str(n3m1p1_loan_amount))
    n3m1p2_row = (network3 + ", " + month1 + ", " + loan_product2 + ", " + "Loan Count: " + str(n3m1p2_loan_count) + ", " + "Total Amount: " + str(n3m1p2_loan_amount))
    n3m1p3_row = (network3 + ", " + month1 + ", " + loan_product3 + ", " + "Loan Count: " + str(n3m1p3_loan_count) + ", " + "Total Amount: " + str(n3m1p3_loan_amount))
    n3m2p1_row = (network3 + ", " + month2 + ", " + loan_product1 + ", " + "Loan Count: " + str(n3m2p1_loan_count) + ", " + "Total Amount: " + str(n3m2p1_loan_amount))
    n3m2p2_row = (network3 + ", " + month2 + ", " + loan_product2 + ", " + "Loan Count: " + str(n3m2p2_loan_count) + ", " + "Total Amount: " + str(n3m2p2_loan_amount))
    n3m2p3_row = (network3 + ", " + month2 + ", " + loan_product3 + ", " + "Loan Count: " + str(n3m2p3_loan_count) + ", " + "Total Amount: " + str(n3m2p3_loan_amount))

    #Print Rows in Output File
    output_file.writerow([n1m1p1_row])
    output_file.writerow([n1m1p2_row])
    output_file.writerow([n1m1p3_row])
    output_file.writerow([n1m2p1_row])
    output_file.writerow([n1m2p2_row])
    output_file.writerow([n1m2p3_row])

    output_file.writerow([n2m1p1_row])
    output_file.writerow([n2m1p2_row])
    output_file.writerow([n2m1p3_row])
    output_file.writerow([n2m2p1_row])
    output_file.writerow([n2m2p2_row])
    output_file.writerow([n2m2p3_row])

    output_file.writerow([n3m1p1_row])
    output_file.writerow([n3m1p2_row])
    output_file.writerow([n3m1p3_row])
    output_file.writerow([n3m2p1_row])
    output_file.writerow([n3m2p2_row])
    output_file.writerow([n3m2p3_row])
