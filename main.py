#### Bakery Management System:
### Product Management :
# Add new products (cakes, pastries, bread, etc.) to the inventory.
# Remove products from the inventory.
# View the list of available products.
# Update product details (name, price, quantity, etc).
### Sales Tracking :
# Record sales transactions.
# View sales history, including date, products sold, and total revenue.
# Calculate daily, weekly, or monthly sales reports.
### Employee management :
# Add, update, or remove employee details.
# Track employee shifts and responsibilities.
### Bill (Short) and half me and half my Partner :

print('Welcome to our Bakery Management System'.center(105, " "))
# I am confused what can i do, I have multiple product for my system but i can't decide how many classes to make for this:
# that is if i make one class then it will be more complex to handle all data but if i make classes for every type of product.

class Product:
    main_stock_level = 100  # Set a hardcoded value for the main stock level

    def __init__(self, name, price, quantity, size):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.size = size

    def display_info(self):
        print(f'Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}, Size: {self.size}')

    def update_info(self, new_name, new_price, new_quantity, new_size):
        self.name = new_name
        self.price = new_price
        self.quantity = new_quantity
        self.size = new_size
        print('Product information updated successfully.')

    def calculate_percentage(self, whole):
        """
        Calculate the percentage.

        Parameters:
        - whole: The whole or total amount.

        Returns:
        The percentage value.
        """
        percentage = (self.price / whole) * 100
        return percentage

    def calculate_tax(self):
        """
        Calculate tax based on a percentage.

        Parameters:
        - tax_percentage (17): The tax rate as a percentage.

        Returns:
        The calculated tax amount.
        """
        tax_amount = (self.price * 17) / 100
        return tax_amount

    def display_main_stock_level(self):
        print(f"Main stock level: {Product.main_stock_level}")

    def add_stock(self, quantity):
        """
        Add stock quantity to the product and deduct it from the main stock level.

        Parameters:
        - quantity: The quantity to be added to the existing stock.
        """
        if quantity >= 0:
            self.quantity += quantity
            Product.main_stock_level -= quantity
            print(f'Stock quantity added. New quantity: {self.quantity}')
        else:
            print('Error: Cannot add negative stock quantity.')

    def remove_stock(self, quantity):
        """
        Remove stock quantity from the product and add it back to the main stock level.

        Parameters:
        - quantity: The quantity to be removed from the existing stock.
        """
        if 0 <= quantity <= self.quantity:
            self.quantity -= quantity
            Product.main_stock_level += quantity
            print(f'Stock quantity removed. New quantity: {self.quantity}')
        elif quantity < 0:
            print('Error: Cannot remove negative stock quantity.')
        else:
            print('Error: Insufficient stock quantity to remove.')


# Cake Category Class
class Cakes(Product):
    main_stock_level = 100  # Set a hardcoded value for the main stock level
    id_code = 0

    def __init__(self, name, price=0, quantity=0, flavour="", size=""):
        super().__init__(name, price, quantity, size)
        self.flavour = flavour

    def display_info(self):
        super().display_info()
        print(f"Flavour: {self.flavour},\t Size: {self.size} Pound\n")

    def update_info(self, new_name, new_price, new_quantity, new_size):
        return super().update_info(new_name, new_price, new_quantity, new_size)

    def generate_id(self):
        # Increment the ID counter and assign it to the instance variable 'id'
        Cakes.id_code += 1
        self.id = Cakes.id_code

    def display_main_stock_level(self):
        print(f"Main stock level: {Product.main_stock_level}")

    def calculate_percentage(self, whole):
        return super().calculate_percentage(whole)

    def calculate_tax(self, tax_percentage):
        return super().calculate_tax(tax_percentage)

        
# Create a chocolate cake
# chocolate_cake = Cakes("Chocolate Delight", 29.99, 1, "Chocolate", 3)
# chocolate_cake.display_info()
# Create a vanilla cake with additional attributes
# vanilla_cake = Cakes("Classic Vanilla", 19.99, 2, "Vanilla", 2)
# vanilla_cake.display_info()
# Create a strawberry cake
# strawberry_cake = Cakes("Strawberry Bliss", 34.99, 1, "Strawberry", 4)
# strawberry_cake.display_info()

# Example 1: Testing Cakes class
chocolate_cake = Cakes("Chocolate Delight", 29.99, 1, "Chocolate", 3)
chocolate_cake.display_info()

# Update information for the chocolate cake
chocolate_cake.update_info("Chocolate Extravaganza", 34.99, 2, 4)
chocolate_cake.display_info()

# Generate ID for the chocolate cake
chocolate_cake.generate_id()
print(f"Generated ID for Chocolate Cake: {chocolate_cake.id}\n")



# Bread Category Class: 
class Bread(Product):
    id_code = 0  # give Unique code to every product

    def __init__(self, name, price=0, quantity=0, type="", size=""):
        super().__init__(name, price, quantity, size)
        self.type = type
        self.price += self.calculate_percentage(self.price, 10)  # Example: Increase price by 10%

    def display_info(self):
        # Size:  Small, Medium, Large, Extra Large
        print(f'Name: {self.name},\tPrice: {self.price},\tQuantity: {self.quantity},\tType: {self.type},\tSize: {self.size}')

    def update_info(self, new_name, new_price, new_quantity, new_size):
        return super().update_info(new_name, new_price, new_quantity, new_size)

    def generate_id(self):
        # Increment the ID counter and assign it to the instance variable 'id'
        Bread.id_code += 1
        self.id = Bread.id_code

    def display_main_stock_level(self):
        print(f"Main stock level: {Product.main_stock_level}")

    def calculate_percentage(self, whole):
        return super().calculate_percentage(whole)

    def calculate_tax(self, tax_percentage):
        return super().calculate_tax(tax_percentage)


# Example 2: Testing Bread class
whole_wheat_bread = Bread("Whole Wheat Bread", 4.99, 3, "Whole Wheat", "Medium")
whole_wheat_bread.display_info()

# Update information for the whole wheat bread
whole_wheat_bread.update_info("Whole Grain Bread", 5.99, 5, "Large")
whole_wheat_bread.display_info()

###############################################################################################
print("\nTesting:\n")
# Create an instance of the Product class
cake = Product("Chocolate Cake", 24.99, 5, "Large")

# Display product information
cake.display_info()

# Update product information
cake.update_info("New Chocolate Cake", 29.99, 3, "Medium")
cake.display_info()

# Calculate and display the percentage
part_value = 2
whole_value = 50
percentage_result = cake.calculate_percentage(part_value, whole_value)
print(f"The percentage is: {percentage_result}%")


# Display the main stock level
cake.display_main_stock_level()

# Add stock to the cake
cake.add_stock(2)

# Display the main stock level after adding stock
cake.display_main_stock_level()

# Remove stock from the cake
cake.remove_stock(1)

# Display the main stock level after removing stock
cake.display_main_stock_level()
