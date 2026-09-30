# Problem 6: Bank Loan Repayment Simulator

def calculate_months(loan, rate, payment):
    balance = loan
    months = 0
    monthly_rate = rate / 100 / 12

    while balance > 0:
        interest = balance * monthly_rate
        balance = balance + interest - payment
        months += 1

    return months


loan = float(input("Enter loan amount: $"))
rate = float(input("Enter annual interest rate (%): "))
payment = float(input("Enter monthly payment: $"))

months = calculate_months(loan, rate, payment)

print(f"Loan will be paid off in {months} months.")