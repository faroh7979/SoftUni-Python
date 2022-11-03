from product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def product_search(self, product_name):

        try:
            searched_product = next(filter(lambda p: p.name == product_name, self.products))
            return searched_product

        except StopIteration:
            return 'No such a product available!'

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):

        return self.product_search(product_name)

    def remove(self, product_name):
        if self.product_search(product_name) in self.products:
            self.products.remove(self.product_search(product_name))

    def __repr__(self):
        final_return = []

        for product in self.products:
            final_return.append(f'{product.name}: {product.quantity}')

        return "\n".join(final_return)

