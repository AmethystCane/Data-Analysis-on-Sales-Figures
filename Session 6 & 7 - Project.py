import csv
import operator
import pandas
import matplotlib.pyplot as plt


# get data from the csv file
def read_data():
    data = []
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data


def run():
    global profit
    data = read_data()

    # put all sale in a list
    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

    # put all month in a list
    month = []
    for row in data:
        months = row['month']
        month.append(months)

    # put all expenditure in a list
    expenditure = []
    for row in data:
        expenditures = int(row['expenditure'])
        expenditure.append(expenditures)

    # get the sum of each month sale and print them
    total = sum(sales)
    print('\n' + "-----------------------------------------------")  # New line and divider
    print('Total sales: {}'.format(total))
    print("-----------------------------------------------")  # Divider

    # get the average of each month sale
    # print them in two decimal points
    average = round(total / 12, 2)
    print('Average sales: {}'.format(average))
    print("-----------------------------------------------", '\n')  # New line and divider

    # Get the max and min sale, and print them
    max_sale = sales[0]
    max_month = month[0]
    min_sale = sales[0]
    min_month = month[0]
    for i in range(len(month)):
        if max_sale < sales[i]:  # get max here
            max_sale = sales[i]
            max_month = month[i]
        if min_sale > sales[i]:  # get min here
            min_sale = sales[i]
            min_month = month[i]
    print('The maximum sale is {} in {}.'.format(max_sale, max_month))
    print('The minimum sale is {} in {}.'.format(min_sale, min_month), '\n')

    # Create Dictionaries in list for sale and month
    # sort them by sales in ascending order and print them
    month_sales = []
    for i in range(len(month)):
        month_sale = {'month': month[i], 'sale': sales[i]}
        month_sales.append(month_sale)
    month_sales.sort(key=operator.itemgetter('sale'))
    for monthAndSale in month_sales:
        print('In {}, the sales is {}.'.format(monthAndSale['month'], monthAndSale['sale']))
    else:
        print('\n', end='')

    # Get the profit for each month and put them in the list
    profits = []
    for i in range(len(month)):
        profit = sales[i] - expenditure[i]
        profits.append(profit)
        current_month = month[i]
        print('The profit for {} is {}.'.format(current_month, profit))
    else:
        print('\n', end='')

    # Calculate the monthly changes in percentage and print them
    for i in range(len(month) - 1):
        percent = ((sales[i + 1] - sales[i]) / sales[i]) * 100
        decimal = round(percent, 2)
        this_month = month[i + 1]
        last_month = month[i]
        print('Monthly changes for {} and {}: {}%'.format(last_month, this_month, decimal))
    else:
        print('\n', end='')

    # Show the csv file in table
    df = pandas.read_csv('sales.csv')
    print(df, '\n')
    print("------------------------------------------------------------------")  # Divider

    # Get all positive profit months and print them
    gain_month = []

    for i in range(len(month)):
        if int(profits[i]) > 0:
            gain_month.append(month[i])
    print('The months that have gains are', end=': ')
    for i in range(len(gain_month)):  # print them in the same line
        print(gain_month[i], end=' ')
    else:
        print('\n' + "------------------------------------------------------------------")  # New line and divider

    # Plotting a graph with colour, legend and marker shapes; Sales, expenses and profit
    plt.plot(month, sales, c="gold", marker="s", markerfacecolor="white", markersize=7, linewidth=2,
             linestyle="dashdot", label="Sales")
    plt.plot(month, expenditure, c="red", marker="o", markerfacecolor="white", markersize=7, linewidth=2,
             linestyle="dashed", label="Expenses")
    plt.plot(month, profits, c="green", marker="^", markerfacecolor="white", markersize=7, linewidth=2,
             linestyle="dotted", label="Profit")
    plt.title("2021 Company Monetary Data")
    plt.xlabel("Months")
    plt.ylabel("Amount (£)")
    plt.legend()
    plt.show()


run()
