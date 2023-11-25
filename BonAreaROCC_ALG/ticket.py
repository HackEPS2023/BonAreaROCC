class Ticket:
    enter_date_time = 0
    customer_id = 0
    articles_id = []
    quantities = []
    ticket_id = 0

    def __init__(self, enter_date_time, customer_id, articles_id, quantities, ticket_id):
        self.enter_date_time = enter_date_time
        self.customer_id = customer_id
        self.articles_id.append(articles_id)
        self.quantities.append(quantities)
        self.ticket_id = ticket_id
