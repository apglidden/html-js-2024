# Andrew Glidden
# Lab #1B - 10/12/2023 - SE116.21

# PROGRAM PROMPT: You want to develop a program that gathers the user’s hourly pay (use $14.50), hours worked (32/week),
#   and tax rate for a two-week period. Once you have this informa5on, you want to display the user’s Gross
#   Pay, Uncle Sam’s Share (the amount to be removed for taxes), and the User’s Net Pay. All calcula5ons should
#   be limited to run once, rather than numerous 5mes. Include in your flowchart the use of variables and print
#   statements. Use 20% for the tax rate.

#VARIABLE DICTIONARY:
#   wage    hourly pay
#   hours   hours worked that week
#   taxFee  percentage of taxes taken out
#   grossPay    gross earnings
#   taxes       total taxes paid
#   netPay      net earnings
#===================================================

#Variables defing pay rate, hours, tax rate
wage = 14.50
hours = 32
taxFee = 0.20

#Calculations of earnings for 2 weeks
grossPay = wage * hours * 2
taxes = grossPay * taxFee
netPay = grossPay - taxes

#Print statements displaying the output of our calculations
print("Gross Earnings",grossPay)
print("Net Earnings",netPay)
print("Taxes Paid",taxes)

#End of Program
print("\nEnd of Program")