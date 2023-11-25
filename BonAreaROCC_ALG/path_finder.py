import sys
import csv
from BonAreaROCC_ALG.customer import Customer
from BonAreaROCC_ALG.ticket import Ticket
from BonAreaROCC_ALG.product import Product

def main(arguments):
    customers = get_customers_info()
    tickets = get_tickets_info()
    products = get_products_info()
    for ticket_id in tickets.keys():
        ticket = tickets[ticket_id]
        customer = customers[ticket.customer_id]
        path = find_path(ticket, customer, products)
        write_to_csv(path)

def get_customers_info():
    customers = {}
    with open('C:/Users/xavie/Documents/hackeps23_bonarea_ROCC/data/hackathon_customers_properties.csv', newline='') as csv_file:
        file_reader = csv.reader(csv_file, delimiter=';', quotechar='|')
        for row in file_reader:
            customers[row[0]] = Customer(row[0], row[1], row[2])
    return customers

def get_tickets_info():
    tickets = {}
    with open('C:/Users/xavie/Documents/hackeps23_bonarea_ROCC/data/hackathon_tickets.csv', newline='') as csv_file:
        file_reader = csv.reader(csv_file, delimiter=';', quotechar='|')
        for row in file_reader:
            if row[4] in tickets:
                ticket = tickets[row[4]]
                ticket.articles_id.append(row[2])
                ticket.quantities.append(row[3])
            else:
                tickets[row[4]] = Ticket(row[0], row[1], row[2], row[3], row[4])
    return tickets

def get_products_info():
    products = {}
    with open('C:/Users/xavie/Documents/hackeps23_bonarea_ROCC/data/hackathon_article_picking_time.csv', newline='') as csv_file:
        file_reader = csv.reader(csv_file, delimiter=';', quotechar='|')
        for row in file_reader:
            products[row[0]] = Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    return products

def find_path(ticket, customer, products):
    return

def write_to_csv(path):
    return

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))