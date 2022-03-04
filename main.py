import webbrowser

from fpdf import FPDF


class Bill:
    """
    Object that contains data about a bill
    such as total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.period = period
        self.amount = amount


class Flatmate:
    """
    Creates a flatmate person who lives in the
    flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = weight * bill.amount
        return to_pay


class PdfReport():
    """
    Creates a pdf file that contains data about
    the flatmates, their names, their amount owed,
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill=bill, flatmate2=flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill=bill, flatmate2=flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        # add image
        pdf.image('logo.png', w=30, h=30)

        # insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        # insert period and label
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # insert name and bill amount owed
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # insert name and bill amount owed 2
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)


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
