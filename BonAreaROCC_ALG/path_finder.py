import sys
import csv
import os
from BonAreaROCC_ALG.customer import Customer
from BonAreaROCC_ALG.ticket import Ticket
from BonAreaROCC_ALG.product import Product
from BonAreaROCC_ALG.weighted_complete_graph import WeightedCompleteGraph
from BonAreaROCC_ALG.tile import Tile
from BonAreaROCC_ALG.vertex import Vertex

def main(arguments):
    current_directory = os.getcwd()
    data_directory = os.path.dirname(current_directory) + '/Data'

    customers = get_customers(data_directory)
    tickets = get_tickets(data_directory)
    products = get_products(data_directory)
    tiles = get_tiles(data_directory)
    for ticket_id in tickets.keys():
        ticket = tickets[ticket_id]
        customer = customers[ticket.customer_id]
        path = find_path(ticket, customer, products, tiles)
        write_to_csv(path)


def get_customers(data_directory):
    customers = {}
    with open(data_directory + '/hackathon_customers_properties.csv', newline='') as csv_file:
        file_reader = csv.reader(csv_file, delimiter=';', quotechar='|')
        for row in file_reader:
            customers[row[0]] = Customer(row[0], row[1], row[2])
    return customers


def get_tickets(data_directory):
    tickets = {}
    with open(data_directory + '/hackathon_tickets.csv', newline='') as csv_file:
        file_reader = csv.reader(csv_file, delimiter=';', quotechar='|')
        for row in file_reader:
            if row[4] in tickets:
                ticket = tickets[row[4]]
                ticket.articles_id.append(row[2])
                ticket.quantities.append(row[3])
            else:
                tickets[row[4]] = Ticket(row[0], row[1], row[2], row[3], row[4])
    return tickets


def get_products(data_directory):
    products = {}
    with open(data_directory + '/hackathon_article_picking_time.csv', newline='') as csv_file:
        file_reader = csv.reader(csv_file, delimiter=';', quotechar='|')
        for row in file_reader:
            products[row[0]] = Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    return products

def get_tiles(data_directory):
    tiles = {}
    with open(data_directory + '/planogram_table.csv', newline='') as csv_file:
        file_reader = csv.reader(csv_file, delimiter=';', quotechar='|')
        for row in file_reader:
            tiles[row[0] + ',' + row[1]] = Tile(row[0], row[1], row[2], row[3], row[4])
    return tiles

def find_path(ticket, customer, products, tiles):
    num_vertices = len(ticket.articles_id)
    weighted_complete_graph = WeightedCompleteGraph(num_vertices)
    vertices = {}
    current_vertices = 1
    for position in tiles.keys():
        if tiles[position].description == 'paso':
            continue
        if tiles[position].description == 'paso-entrada':
            vertices[0] = Vertex(tiles[position].x, tiles[position].y, True)
        elif tiles[position].description == 'paso-salida':
            vertices[current_vertices] = Vertex(tiles[position].x, tiles[position].y, False)
            current_vertices += 1
        else:
            for article_id in products:
                if tiles[position].description == products[article_id].article_id:
                    vertices[current_vertices] = Vertex(tiles[position].picking_x, tiles[position].picking_y, True)
                    current_vertices += 1

    for x in range(len(vertices)):
        for y in range(len(vertices)):
            if x != y:
                weighted_complete_graph.add_edge(x, y, minimum_weight(vertices[x], vertices[y]))

    weighted_complete_graph.find_optimal_path(0, 3)


def minimum_weight(start, end):
    return 0

def write_to_csv(path):
    return


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))