#Lucia
#Chapter 2 Programming Exercise 14 Compound Interest.

PV = 1000
R = .025
T = 2
M = 12

#Imput

PrincipalInv = float(input("Enter the starting principal: "))
fInterestRate = float(input("Enter the annual interest rate (in %): ")) / 100  # Convert percent
iCompound = int(input("How many times per year is the interest compounded?: "))
fNumberOfPeriods = float(input("For how many years will the account earn interest?: "))

#Formula
#FV: Future Value

future_value = PV * (1 + R / M) ** ( M * T)

#Output

print("\n------ Compound Interest Summary ------")
print(f"{'Starting Principal:':35} ${PrincipalInv:,.2f}")
print(f"{'Annual Interest Rate:':35} {fInterestRate * 100:.2f}%")
print(f"{'Times Compounded Per Year:':35} {iCompound}")
print(f"{'Years:':35} {T}")
print(f"{'Future Value:':35} ${future_value:,.2f}")


print('At the end of', nYears, 'years', 'you will have $', format(nAccount, ',.2f'))