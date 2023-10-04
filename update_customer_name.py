import csv

def update_customer_csv_row(file_name, row_number, column_name, new_value):

    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        rows[row_number][rows[0].index(column_name)] = new_value

    with open(file_name, 'w') as f: 
        writer = csv.writer(f)
        writer.writerows(rows)

update_customer_csv_row('customers.csv', 1000, 'name', 'JANE RAMBO')

    
