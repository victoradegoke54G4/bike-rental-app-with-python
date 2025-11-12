
class Customer:
    def __init__(self):
        """initializer for Customer Class"""
        self.bikes = 0
        self.rental_basis = 0
        self.rental_time = 0
        self.bill = 0

    @staticmethod
    def get_int(prompt):
        """Returns positive integers and checks users input"""
        while True:
            try:
                choice = int(input(prompt))
                if not choice or choice < 1:
                    print('You can only input positive integers')
                    continue
                return choice
            except ValueError:
                print('Invalid Input')

    def request_bike(self):
        """Take a request from the customer for the number of bikes"""
        bikes = Customer.get_int('How many bikes would you like to rent?: ')
        self.bikes = bikes
        return self.bikes
    
    def return_bike(self):
        """Allows ths custoomers to return their bikes to the rental shop"""
        if self.rental_time and self.rental_basis and self.bikes:
            return self.rental_time, self.rental_basis, self.bikes
        else:
            return 0,0,0

