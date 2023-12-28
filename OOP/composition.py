# Relationships between classes: association, aggregation, and composition
# Composition is a specialization of aggregation.
# In composition, when the "parent" object is deleted,
# all references to the child objects are also deleted.
class Customer:
    def __init__(self, name) -> None:
        self.name = name
        self.addresses = []

    def insert_address(self, street, number):
        self.addresses.append(Address(street, number))

    def insert_external_address(self, address):
        self.addresses.append(address)

    def list_adresses(self):
        for address in self.addresses:
            print(address.street, address.number)

    def __del__(self):
        print('Erasing:', self.name)

class Address:
    def __init__(self, street, number) -> None:
        self.street = street
        self.number = number

    # Garbage collector
    def __del__(self):
        print('Erasing:', self.street, self.number)

customer_one = Customer('Charles')
customer_one.insert_address('Av Brasil', 62)
customer_one.insert_address('B street', 212)

external_address = Address('Rose street', 1234)
customer_one.insert_external_address(external_address)

customer_one.list_adresses()

del customer_one

print('---> Code ends here. <---')