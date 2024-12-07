class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if isinstance(item, MenuItem):
            self.items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)


class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class Beverage(MenuItem):    
    def __init__(self, name, price, size: str = 'Normal'):
        if size.upper() == 'GRANDE': 
            price += 1000
        elif size.upper() == 'PEQUEÑO': 
            price -= 1000
        super().__init__(name, price)
        self.size = size.upper()


class MainDish(MenuItem):
    def __init__(self, name: str, price: float, protein_choice: str = 'chicken'):
        if protein_choice.upper() == 'BEEF': 
            price += 3000
        elif protein_choice.upper() == 'SEAFOOD': 
            price += 2500
        super().__init__(name, price)
        self.protein_choice = protein_choice.upper()


class Starters(MenuItem):
    def __init__(self, name: str, price: float, extra_portion: bool = False):
        if extra_portion: 
            price += 2000
        super().__init__(name, price)
        self.extra_portion = extra_portion


class Desserts(MenuItem):
    def __init__(self, name: str, price: float, topping: str = 'none'):
        if topping.upper() == 'CHOCOLATE': 
            price += 500
        elif topping.upper() == 'CARAMEL': 
            price += 1000
        elif topping.upper() == 'NUTS': 
            price += 1200
        super().__init__(name, price)
        self.topping = topping.upper()



# Crear ítems del menú
beverage1 = Beverage(name="Coca Cola", price=2000, size="Grande")
beverage2 = Beverage(name="Agua Mineral", price=1500, size="Pequeño")

main_dish1 = MainDish(name="Pollo Asado", price=10000, protein_choice="chicken")
main_dish2 = MainDish(name="Filete de Res", price=15000, protein_choice="beef")
main_dish3 = MainDish(name="Cazuela de Mariscos", price=20000, protein_choice="seafood")

starter1 = Starters(name="Ensalada César", price=5000, extra_portion=True)
starter2 = Starters(name="Sopa de Tomate", price=4000, extra_portion=False)

dessert1 = Desserts(name="Brownie", price=3000, topping="chocolate")
dessert2 = Desserts(name="Helado", price=3500, topping="caramel")
dessert3 = Desserts(name="Tarta de Frutas", price=4000, topping="none")

# Crear el pedido
pedido = Order()

# Agregar ítems al pedido
pedido.add_item(beverage1)
pedido.add_item(beverage2)
pedido.add_item(main_dish1)
pedido.add_item(main_dish2)
pedido.add_item(main_dish3)
pedido.add_item(starter1)
pedido.add_item(starter2)
pedido.add_item(dessert1)
pedido.add_item(dessert2)
pedido.add_item(dessert3)

# Mostrar el pedido
print(pedido.calculate_total())

        
        
    
        