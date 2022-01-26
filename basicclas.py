class Restaurant:

    def __init__(self, name, cuisine, price, rating):
        self.name = name
        self.cuisine = cuisine
        self.price = price
        self.rating = rating

    def __str__(self):
        return self.name
