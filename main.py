from bike_rental import BikeRental
from customer import Customer


def safe_choice(prompt, options = None):
    while True:
        choice = input(prompt)
        if options == None:
            options = ['1','2','3','4','5','6']
        for option in options:
            if choice == option:
                return int(choice) 
                
        print(f'Invalid Choice! {','.join(map(str,options))}')


def main():
    """Displays the user interface for interaction"""
    bikeRental = BikeRental(100)
    customer = Customer()

    while True:
        print("""
            ===================== BIKE RENTAL APP ============================
            1. Display available bikes
            2. Request a bike on hourly basis - $5
            3. Request a bike on daily basis - $20
            4. Request a bike on weekly basis - $60
            5. Return a bike(s)
            6. Exit 
            """)
        

        choice = safe_choice('Enter choice: ')

        if choice == 1:
            bikeRental.display_stock()

        elif choice == 2:
            requested_bikes = customer.request_bike()
            rental_time = bikeRental.rent_bike_on_hourly_basis(requested_bikes)
            customer.rental_time = rental_time
            customer.rental_basis = 1


        elif choice == 3:
            requested_bikes = customer.request_bike()
            rental_time = bikeRental.rent_bike_on_daily_basis(requested_bikes)
            customer.rental_time = rental_time
            customer.rental_basis = 2

        elif choice == 4:
            requested_bikes = customer.request_bike()
            rental_time = bikeRental.rent_bike_on_weekly_basis(requested_bikes)
            customer.rental_time = rental_time
            customer.rental_basis = 3

        elif choice == 5:
            request_tuple = customer.return_bike()
            bill = bikeRental.return_bike(request_tuple)
            customer.bill = bill
            customer.rental_time,customer.rental_basis,customer.bikes = 0,0,0
            
        elif choice == 6:
            break

        else: 
            print('Invalid Input! Please enter a number between 1-6')
    
    print('Thank you for using the bike rental app.')
    

if __name__ == '__main__':
    main()
