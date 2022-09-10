class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []
        self.first_letter_list = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        self.first_letter_list = [product for product in self.products if product[0] == first_letter]
        return self.first_letter_list

    def __repr__(self):
        self.products.sort()
        var = '\n'.join(self.products)
        return f'Items in the {self.name} catalogue:\n'\
            f'{var}'
