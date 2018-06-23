# these should be the only imports you need
import sys
import sqlite3

data = sqlite3.connect('Northwind_small.sqlite')
d = data.cursor()


def customers():
    d.execute('SELECT Id, CompanyName FROM Customer')
    customer_list=d.fetchall()
    print ('ID      Customer Name')
    for pair in customer_list:
        print(pair[0]+'    '+pair[1])
    return None

def employees():
    d.execute('SELECT ID, FirstName, LastName FROM [Employee]')
    employee_list=d.fetchall()
    print('ID    Employee Name')
    for tup in employee_list:
        print(tup[0],'   ', tup[1], tup[2])
    return None

def orders(cust='o.CustomerId', emp='e.LastName'):
    d.execute('SELECT o.OrderDate FROM [Order] as o, [Employee] as e WHERE o.EmployeeId=e.Id AND o.CustomerId = ? OR e.LastName = ?;', (cust,emp))
    order_dates=d.fetchall()
    print('Order Dates')
    for date in order_dates:
        print(date[0])
    return None



try:
    if __name__== "__main__" and sys.argv[1]=='customers':
        customers()
    elif __name__=="__main__" and sys.argv[1]=='orders' and sys.argv[2][:4]=='cust':
        orders(cust=sys.argv[2][5:])
    elif __name__=="__main__" and sys.argv[1]=='orders' and sys.argv[2][:3]=='emp':
        orders(emp=str(sys.argv[2][4:]))
    elif __name__=="__main__" and sys.argv[1]=='employees':
        employees()
except IndexError:
    print('No function called')
except NameError:
    print('No function called')


# write your code here
# usage should be
#  python3 part2.py customers
#  python3 part2.py employees
#  python3 part2.py orders cust=<customer id>
#  python3 part2.py orders emp=<employee last name>
