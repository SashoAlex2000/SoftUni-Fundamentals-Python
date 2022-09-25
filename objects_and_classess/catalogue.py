class Catalogue:

    def __init__(self, name):
        self.name = name

    products = []


    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str) :
        new_list = [item for item in self.products if item[0] == first_letter]
        return(new_list)


    def __repr__(self):
        return (f"Items in the {self.name} catalogue:\n" +
                ("\n".join(sorted(self.products))))




