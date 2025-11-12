import datetime as dt

class BikeRental:
    def __init__(self, stock):
        """Initializer for Bike Rental Class"""
        self.stock = stock

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

    def display_stock(self):
        """Displays Bikes currently available in stock"""
        print(f'There are currently {self.stock} bikes available for rent.')
        return self.stock
    
    def rent_bike_on_hourly_basis(self, n):
        """Rents a bike(s) on hourly basis"""
        now = dt.datetime.now()
        print(f'You have rented {n} bike(s) on hourly basis at {now.hour}:{now.minute}:{now.second}.')
        print('You\'ll be charge $5 on each bike per hour.' )
        print('We hope that You enjoy Our service.' )
        self.stock -= n
        return now
    
    def rent_bike_on_daily_basis(self, n):
        """Rents a bike(s) on daily basis"""
        day = dt.datetime.today()
        print(f'You have rented {n} bike(s) on daily basis at {day.date()} {day.hour}:{day.minute}.')
        print('You\'ll be charge $20 on each bike per day.')
        print('YWe hope that You enjoy Our service.')
        self.stock -= n
        return day
    
    def rent_bike_on_weekly_basis(self, n):
        """Rents a bike(s) on weekly basis"""
        week = dt.datetime.today()
        print(f'You have rented {n} bike(s) on weekly basis at {week.date()}.')
        print('You\'ll be charge $60 on each bike per week.')
        print('YWe hope that You enjoy Our service.')
        self.stock -= n
        return week
    
    def return_bike(self, request, bill = 0):
        """Returns bikes from user""" 
        rental_time, rental_basis, num_of_bikes = request
        if rental_basis and rental_time and num_of_bikes:
        
            self.stock += num_of_bikes
            now = dt.datetime.now()
            rental_period = now - rental_time

            if rental_basis == 1:
                bill = round(rental_period.seconds/3600)*5*num_of_bikes

            elif rental_basis == 2:
                bill = round(rental_period.days)*20*num_of_bikes

            elif rental_basis == 3:
                bill = round(rental_period.days/7)*60*num_of_bikes
            
            if 3<=num_of_bikes<=6:
                print('You are eligible for family rental discount of 30%')
                bill = bill*0.7

            print('Thanks for returning the bike. Hope you enjoyed the service!')
            print(f'The total bill: is {bill}')
            return bill
        else:
            print('Are You sure you rented a bike with Us? ')
            return None

