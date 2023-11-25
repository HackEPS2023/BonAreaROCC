import sys
import csv
from BonAreaROCC_ALG.customer import Customer
from BonAreaROCC_ALG.ticket import Ticket
from BonAreaROCC_ALG.product import Product
from BonAreaROCC_ALG.weighted_complete_graph import WeightedCompleteGraph
from BonAreaROCC_ALG.tile import Tile
from BonAreaROCC_ALG.vertex import Vertex

def main(arguments):
    customers = get_customers()
    tickets = get_tickets()
    products = get_products()
    tiles = get_tiles()
    for ticket_id in tickets.keys():
        ticket = tickets[ticket_id]
        customer = customers[ticket.customer_id]
        path = find_path(ticket, customer, products, tiles)
        write_to_csv(path)


def get_customers():
    customers = {}
    with open('C:/Users/xavie/Documents/hackeps23_bonarea_ROCC/data/hackathon_customers_properties.csv', newline='') as csv_file:
        file_reader = csv.reader(csv_file, delimiter=';', quotechar='|')
        for row in file_reader:
            customers[row[0]] = Customer(row[0], row[1], row[2])
    return customers


def get_tickets():
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


def get_products():
    products = {}
    with open('C:/Users/xavie/Documents/hackeps23_bonarea_ROCC/data/hackathon_article_picking_time.csv', newline='') as csv_file:
        file_reader = csv.reader(csv_file, delimiter=';', quotechar='|')
        for row in file_reader:
            products[row[0]] = Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    return products

def get_tiles():
    tiles = {}
    with open('C:/Users/xavie/Documents/hackeps23_bonarea_ROCC/data/planogram_table.csv', newline='') as csv_file:
        file_reader = csv.reader(csv_file, delimiter=';', quotechar='|')
        for row in file_reader:
            tiles[row[0] + ',' + row[1]] = Tile(row[0], row[1], row[2], row[3], row[4])
    return tiles

def find_path(ticket, customer, products, tiles):
    num_vertices = len(ticket.articles_id)
    weighted_complete_graph = WeightedCompleteGraph(num_vertices)
    vertices = {}
    current_vertices = 1
    for tile in tiles:
        if tile.description == 'paso':
            continue
        if tile.description == 'paso-entrada':
            vertices[0] = Vertex(tile.x, tile.y, True)
        elif tile.description == 'paso-salida':
            vertices[current_vertices] = Vertex(tile.x, tile.y, False)
            current_vertices += 1
        else:
            for product in products:
                if tile.description == product.article_id:
                    vertices[current_vertices] = Vertex(tile.picking_x, tile.picking_y, True)
                    current_vertices += 1

    for x in range(len(vertices)):
        for y in range(len(vertices)):
            if x != y:
                weighted_complete_graph.add_edge(vertices[x], vertices[y], minimum_weight(vertices[x], vertices[y]))

    weighted_complete_graph.find_optimal_path(0, 3)


def minimum_weight(start, end):
    return 0

def write_to_csv(path):
    return


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))