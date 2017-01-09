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

# First attempt at getting data from the loans.csv file
loans_file = open("loans.csv", "r+")

text_in_file = loans_file.read()
print(text_in_file)

#Attempt at getting data from the loans.csv file using csv module
with open('loans.csv', 'r') as input, open('output.csv', 'w') as output:
    loans_file = csv.reader(input, delimiter=',', quotechar="'")
    output_file = csv.writer(output, delimiter=',', quotechar="'")

    for row in loans_file:
        #Network 1
        if row[1] == network1 and row[2][3:6] == month1 and row[3] == loan_product1:
            loan_count = 0
            loan_count += 1
            network_month1_product1 = 0
            network_month1_product1 = network_month1_product1 + float(row[4])
            new_row = (row[1]+", "+row[2][3:6]+", "+row[3]+", "+str(network_month1_product1)+", "+"loan count: "+str(loan_count))
            output_file.writerow([new_row])
        elif row[1] == network1 and row[2][3:6] == month1 and row[3] == loan_product2:
            loan_count = 0
            loan_count += 1
            network_month1_product2 = 0
            network_month1_product2 = network_month1_product2 + float(row[4])
            new_row = (row[1] + ", "+row[2][3:6]+", "+row[3]+", "+str(network_month1_product2)+", "+"loan count: "+str(loan_count))
            output_file.writerow([new_row])
        elif row[1] == network1 and row[2][3:6] == month1 and row[3] == loan_product3:
            loan_count = 0
            loan_count += 1
            network_month1_product3 = 0
            network_month1_product3 = network_month1_product3 + float(row[4])
            new_row = (row[1] + ", "+row[2][3:6]+", "+row[3]+", "+str(network_month1_product3)+", "+"loan count: "+str(loan_count))
            output_file.writerow([new_row])

        elif row[1] == network1 and row[2][3:6] == month2 and row[3] == loan_product1:
            loan_count = 0
            loan_count += 1
            network_month1_product1 = 0
            network_month1_product1 = network_month1_product1 + float(row[4])
            new_row = (row[1]+", "+row[2][3:6]+", "+row[3]+", "+str(network_month1_product1)+", "+"loan count: "+str(loan_count))
            output_file.writerow([new_row])
        elif row[1] == network1 and row[2][3:6] == month2 and row[3] == loan_product2:
            loan_count = 0
            loan_count += 1
            network_month1_product2 = 0
            network_month1_product2 = network_month1_product2 + float(row[4])
            new_row = (row[1] + ", "+row[2][3:6]+", "+row[3]+", "+str(network_month1_product2)+", "+"loan count: "+str(loan_count))
            output_file.writerow([new_row])
        elif row[1] == network1 and row[2][3:6] == month2 and row[3] == loan_product3:
            loan_count = 0
            loan_count += 1
            network_month1_product3 = 0
            network_month1_product3 = network_month1_product3 + float(row[4])
            new_row = (row[1] + ", "+row[2][3:6]+", "+row[3]+", "+str(network_month1_product3)+", "+"loan count: "+str(loan_count))
            output_file.writerow([new_row])

        # Network 2
        elif row[1] == network2 and row[2][3:6] == month1 and row[3] == loan_product1:
            loan_count = 0
            loan_count += 1
            network_month1_product1 = 0
            network_month1_product1 = network_month1_product1 + float(row[4])
            new_row = (row[1] + ", " + row[2][3:6] + ", " + row[3] + ", " + str(
                network_month1_product1) + ", " + "loan count: " + str(loan_count))
            output_file.writerow([new_row])
        elif row[1] == network2 and row[2][3:6] == month1 and row[3] == loan_product2:
            loan_count = 0
            loan_count += 1
            network_month1_product2 = 0
            network_month1_product2 = network_month1_product2 + float(row[4])
            new_row = (row[1] + ", " + row[2][3:6] + ", " + row[3] + ", " + str(
                network_month1_product2) + ", " + "loan count: " + str(loan_count))
            output_file.writerow([new_row])
        elif row[1] == network2 and row[2][3:6] == month1 and row[3] == loan_product3:
            loan_count = 0
            loan_count += 1
            network_month1_product3 = 0
            network_month1_product3 = network_month1_product3 + float(row[4])
            new_row = (row[1] + ", " + row[2][3:6] + ", " + row[3] + ", " + str(
                network_month1_product3) + ", " + "loan count: " + str(loan_count))
            output_file.writerow([new_row])

        elif row[1] == network2 and row[2][3:6] == month2 and row[3] == loan_product1:
            loan_count = 0
            loan_count += 1
            network_month1_product1 = 0
            network_month1_product1 = network_month1_product1 + float(row[4])
            new_row = (row[1] + ", " + row[2][3:6] + ", " + row[3] + ", " + str(
                network_month1_product1) + ", " + "loan count: " + str(loan_count))
            output_file.writerow([new_row])
        elif row[1] == network2 and row[2][3:6] == month2 and row[3] == loan_product2:
            loan_count = 0
            loan_count += 1
            network_month1_product2 = 0
            network_month1_product2 = network_month1_product2 + float(row[4])
            new_row = (row[1] + ", " + row[2][3:6] + ", " + row[3] + ", " + str(
                network_month1_product2) + ", " + "loan count: " + str(loan_count))
            output_file.writerow([new_row])
        elif row[1] == network2 and row[2][3:6] == month2 and row[3] == loan_product3:
            loan_count = 0
            loan_count += 1
            network_month1_product3 = 0
            network_month1_product3 = network_month1_product3 + float(row[4])
            new_row = (row[1] + ", " + row[2][3:6] + ", " + row[3] + ", " + str(
                network_month1_product3) + ", " + "loan count: " + str(loan_count))
            output_file.writerow([new_row])

        # Network 3
        elif row[1] == network3 and row[2][3:6] == month1 and row[3] == loan_product1:
            loan_count = 0
            loan_count += 1
            network_month1_product1 = 0
            network_month1_product1 = network_month1_product1 + float(row[4])
            new_row = (row[1] + ", " + row[2][3:6] + ", " + row[3] + ", " + str(
                network_month1_product1) + ", " + "loan count: " + str(loan_count))
            output_file.writerow([new_row])
        elif row[1] == network3 and row[2][3:6] == month1 and row[3] == loan_product2:
            loan_count = 0
            loan_count += 1
            network_month1_product2 = 0
            network_month1_product2 = network_month1_product2 + float(row[4])
            new_row = (row[1] + ", " + row[2][3:6] + ", " + row[3] + ", " + str(
                network_month1_product2) + ", " + "loan count: " + str(loan_count))
            output_file.writerow([new_row])
        elif row[1] == network3 and row[2][3:6] == month1 and row[3] == loan_product3:
            loan_count = 0
            loan_count += 1
            network_month1_product3 = 0
            network_month1_product3 = network_month1_product3 + float(row[4])
            new_row = (row[1] + ", " + row[2][3:6] + ", " + row[3] + ", " + str(
                network_month1_product3) + ", " + "loan count: " + str(loan_count))
            output_file.writerow([new_row])

        elif row[1] == network3 and row[2][3:6] == month2 and row[3] == loan_product1:
            loan_count = 0
            loan_count += 1
            network_month1_product1 = 0
            network_month1_product1 = network_month1_product1 + float(row[4])
            new_row = (row[1] + ", " + row[2][3:6] + ", " + row[3] + ", " + str(
                network_month1_product1) + ", " + "loan count: " + str(loan_count))
            output_file.writerow([new_row])
        elif row[1] == network3 and row[2][3:6] == month2 and row[3] == loan_product2:
            loan_count = 0
            loan_count += 1
            network_month1_product2 = 0
            network_month1_product2 = network_month1_product2 + float(row[4])
            new_row = (row[1] + ", " + row[2][3:6] + ", " + row[3] + ", " + str(
                network_month1_product2) + ", " + "loan count: " + str(loan_count))
            output_file.writerow([new_row])
        elif row[1] == network3 and row[2][3:6] == month2 and row[3] == loan_product3:
            loan_count = 0
            loan_count += 1
            network_month1_product3 = 0
            network_month1_product3 = network_month1_product3 + float(row[4])
            new_row = (row[1] + ", " + row[2][3:6] + ", " + row[3] + ", " + str(
                network_month1_product3) + ", " + "loan count: " + str(loan_count))
            output_file.writerow([new_row])