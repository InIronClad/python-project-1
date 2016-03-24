#Assignment: (Homework #1) 
# 
#Description: (Programming Task - Loan Calculator) 
# 
#Author: (Robert Crismon) 
# 
#Completion Time: (3 hours) 
# 
#In completing this program, I obtained help or worked with the following: 
#
#(for the Loan Calculator Programming Task, I did use a few websites,
#https://www.daniweb.com/software-development/python/code/216739/mortgage-calculator-python,
#https://www.daniweb.com/software-development/python/code/448171/a-simple-mortgage-calculator,
#and http://stackoverflow.com/questions/4520739/am-i-doing-it-right-question-regarding-piece-of-code-i-wrote.)

#pseudocode task #1:
"""

list_of_numbers = (u, v, x, y, z)
u = float(input("enter first number"))
v = float(input("enter second number"))
x = float(input("enter third number"))
y = float(input("enter fourth number"))
z = float(input("enter fifth number"))

def add(u, v, x, y, z):
	if type(u) == type(v) == type(x) == type(y) == type(z):
		return u+v+x+y+z
	else:
		return x
total = (u+v+x+y+z)
average_of_numbers = float(total / 5)
print("the average is average_of_numbers")		
"""
#end of pseudocode task #1
#
#pseudocode task #2:
"""

user_input = ("type am integer or decimal number")
if user_input = int(user_input) {
	print("user_input is an integer")
} else {
	print("user_input is a decimal number")
}
"""
#end of pseudocode task #2

amount_borrowed = float(input("Please input amount borrowed [in dollars]: "))
yr_rate = float(input("Please input interest rate [in percent form]: "))
loan_period = float(input("please input term of the loan: "))
#these are the three inputs needed from the user: loan amount, interest rate, and period.
monthly_rate = yr_rate / (100 * 12)
#monthly rate
payment_number = (loan_period * 12)
#number of monthly payments to be made
monthly_payment = amount_borrowed * ( monthly_rate / (1 - (1 + monthly_rate) ** (- payment_number)))
#monthly loan payment amount

print ("Monthly payment:    $%0.2f" % monthly_payment)
print ("Total cost:         $%0.2f" % (payment_number * monthly_payment))
print ("Total interest:     $%0.2f" % (payment_number * monthly_payment - amount_borrowed))










