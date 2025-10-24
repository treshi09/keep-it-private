#Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.

class Computer:
    __max_price = 900
    def sell(self):
        print("Selling Price is:", self.__max_price)
    def setMaxPrice(self, price):
        self.__max_price = price

obj = Computer()
obj.sell()
print("Updating the price")
obj.setMaxPrice(1000)
obj.sell()