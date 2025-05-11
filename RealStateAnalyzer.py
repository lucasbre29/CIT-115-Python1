#Lucia Castillo-Breton
#Real State Analyzer



def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Value must be greater than 0. Please try again.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


def getMedian(sales_list):
    n = len(sales_list)
    if n % 2 == 1:
        return sales_list[n // 2]
    else:
        mid1 = sales_list[(n // 2) - 1]
        mid2 = sales_list[n // 2]
        return (mid1 + mid2) / 2


def main():
    sales = []

    while True:
        value = getFloatInput("Enter property sales value: ")
        sales.append(value)

        while True:
            more = input("Enter another value Y or N: ").strip().lower()
            if more in ('y', 'n'):
                break
            else:
                print("Please enter 'Y' or 'N'.")

        if more == 'n':
            break

    sales.sort()

    print("\nWith", len(sales), "entries:")
    for i, price in enumerate(sales, start=1):
        print(f"Property {i} $ {price:,.2f}")

    minimum = sales[0]
    maximum = sales[-1]
    total = sum(sales)
    average = total / len(sales)
    median = getMedian(sales)
    commission = total * 0.03

    print(f"Minimum:    $ {minimum:,.2f}")
    print(f"Maximum:    $ {maximum:,.2f}")
    print(f"Total:      $ {total:,.2f}")
    print(f"Average:    $ {average:,.2f}")
    print(f"Median:     $ {median:,.2f}")
    print(f"Commission: $ {commission:,.2f}")


# Run the program
main()
