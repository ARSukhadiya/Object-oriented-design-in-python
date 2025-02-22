# The program title
print("Calculate and Display baker's salary details")

# Define constants
BAKER1_regular_rate = 15
BAKER1_fix_rate_hrs = 35
BAKER1_overtime_rate = 1.5 * BAKER1_regular_rate

BAKER2_regular_rate = 16.25
BAKER2_fix_rate_hrs = 40
BAKER2_overtime_rate = 2 * BAKER2_regular_rate

BAKER3_regular_rate = 17.75
BAKER3_fix_rate_hrs = 40
BAKER3_overtime_41_45_hrs_rate = 1.5 * BAKER3_regular_rate
BAKER3_overtime_45_rate = 2 * BAKER3_regular_rate

TAX = 0.3

# Get the user inputs
baker1_pay = baker2_pay = baker3_pay = 0
baker1_overtime_pay = baker2_overtime_pay = baker3_overtime_pay = 0

baker1_hrs = int(input("Baker_1, please enter the number of hours:"))
baker2_hrs = int(input("Baker_2, please enter the number of hours:"))
baker3_hrs = int(input("Baker_3, please enter the number of hours:"))


# Calculate the pay and overtime_pay
if baker1_hrs <= BAKER1_fix_rate_hrs:
    baker1_pay = BAKER1_regular_rate * baker1_hrs
else:
    baker1_pay = BAKER1_regular_rate * BAKER1_fix_rate_hrs
    baker1_overtime_pay = BAKER1_overtime_rate * (baker1_hrs - BAKER1_fix_rate_hrs)

if baker2_hrs <= BAKER2_fix_rate_hrs:
    baker2_pay = BAKER2_regular_rate * baker2_hrs
else:
    baker2_pay = BAKER2_regular_rate * BAKER2_fix_rate_hrs
    baker2_overtime_pay = BAKER2_overtime_rate * (baker2_hrs - BAKER2_fix_rate_hrs)
    
if baker3_hrs <= BAKER3_fix_rate_hrs:
    baker3_pay = BAKER3_regular_rate * baker3_hrs
else:
    baker3_pay = BAKER3_regular_rate * BAKER3_fix_rate_hrs
    if baker3_hrs <= 45:
        baker3_overtime_pay = BAKER3_overtime_41_45_hrs_rate * (baker3_hrs - BAKER3_fix_rate_hrs)
    else:
        baker3_overtime_pay = BAKER3_overtime_41_45_hrs_rate * (baker3_hrs - 45)
        baker3_overtime_pay += BAKER3_overtime_45_rate * (baker3_hrs - 45)

# print('\nbaker1_pay:', baker1_pay)
# print('baker1_overtime_pay:', baker1_overtime_pay)

# print('\nbaker2_pay:', baker2_pay)
# print('baker2_overtime_pay:', baker2_overtime_pay)

# print('\nbaker3_pay:', baker3_pay)
# print('baker3_overtime_pay:', baker3_overtime_pay)

# Measure Gross pay, Tax, and Net pay
baker1_gross_pay = baker1_pay + baker1_overtime_pay
baker2_gross_pay = baker2_pay + baker2_overtime_pay
baker3_gross_pay = baker3_pay + baker3_overtime_pay

baker1_tax = baker1_gross_pay * TAX
baker2_tax = baker2_gross_pay * TAX
baker3_tax = baker3_gross_pay * TAX

baker1_net_pay = baker1_gross_pay - baker1_tax
baker2_net_pay = baker2_gross_pay - baker2_tax
baker3_net_pay = baker3_gross_pay - baker3_tax

print("\n___Banker_1___")
print("Hours worked:", baker1_hrs)
print("Gross pay:", baker1_gross_pay)
print("Tax(30%):", baker1_tax)
print("Net pay:", baker1_net_pay)

print("\n___Banker_2___")
print("hours worked:", baker2_hrs)
print("Gross pay:", baker2_gross_pay)
print("Tax(30%):", baker2_tax)
print("Net pay:", baker2_net_pay)

print("\n___Banker_3___")
print("hours worked:", baker3_hrs)
print("Gross pay:", baker3_gross_pay)
print("Tax(30%):", baker3_tax)
print("Net pay:", baker3_net_pay)
