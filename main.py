from flat import Bill, Flatmate
from reports import PdfReport

bill_amount = float(input('Hey Buddy, enter the bill amount: '))
period = input('What\'s the billing period? eg December 2020: ')

name1 = input('What is your name? ')
days_in_house1 = int(input(f'How many days did {name1} stay in the house? '))

name2 = input('What is the name of the other flatmate? ')
days_in_house2 = int(input(f'How many days did {name2} stay in the house? '))

the_bill = Bill(amount=bill_amount, period=period)
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)

print(f"{flatmate1.name} pays {flatmate1.pays(bill=the_bill, flatmate2=flatmate2):.2f}")
print(f"{flatmate2.name} pays {flatmate2.pays(bill=the_bill, flatmate2=flatmate1):.2f}")

pdf_report = PdfReport(filename=f'{the_bill.period}.pdf')
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)
