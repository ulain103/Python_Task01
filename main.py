class Train:
    def __init__(self, departure_time, return_time, available_seats):
        self.departure_time = departure_time
        self.return_time = return_time
        self.available_seats = available_seats
        self.passengers = 0
        self.revenue = 0.0


def display_start_of_day(trains):
    print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(
        "Departure Time", "Return Time", "Available Seats", "Passengers", "Revenue"))

    for train in trains:
        if train.available_seats > 0:
            print("{:<20} {:<20} {:<20} {:<20} ${:<20}".format(
                train.departure_time, train.return_time, train.available_seats,
                train.passengers, train.revenue))
        else:
            print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(
                train.departure_time, train.return_time, "Closed", train.passengers, train.revenue))


def purchase_tickets(trains, train_index, num_passengers):
    # Check if the selected train is available
    if trains[train_index].available_seats <= 0:
        print("Train is full. Cannot purchase tickets.")
        return

    # Calculate total price including group discount
    ticket_price = 25.0
    total_price = num_passengers * ticket_price
    free_tickets = num_passengers // 10  # Calculate free tickets for groups

    # Update available seats and passenger count
    trains[train_index].available_seats -= num_passengers - free_tickets
    trains[train_index].passengers += num_passengers
    trains[train_index].revenue += total_price

    # Display information
    display_start_of_day(trains)

    # Display purchase details
    print("Purchase successful!")
    print(f"Number of tickets: {num_passengers}")
    print(f"Total Price: ${total_price}")
    print(f"Free Tickets: {free_tickets}")


def display_end_of_day(trains):
    total_passengers = sum(train.passengers for train in trains)
    total_revenue = sum(train.revenue for train in trains)
    max_passengers_index = max(range(len(trains)), key=lambda i: trains[i].passengers)

    print("End-of-Day Summary:")
    print(f"Total Passengers for the Day: {total_passengers}")
    print(f"Total Revenue for the Day: ${total_revenue}")
    print(
        f"Train Journey with the Most Passengers: {trains[max_passengers_index].departure_time} - {trains[max_passengers_index].return_time}")


def main():
    # Initialize train schedule for the start of the day
    trains = [
        Train("09:00", "10:00", 6 * 80),
        Train("11:00", "12:00", 6 * 80),
        Train("13:00", "14:00", 6 * 80),
        Train("15:00", "16:00", 6 * 80 + 2)  # Last train has 2 extra coaches
    ]

    # Display start-of-day information
    display_start_of_day(trains)

    # Keep booking running until all tickets are sold
    while any(train.available_seats > 0 for train in trains):
        # User input for ticket purchase
        selected_train = int(input("Enter the index of the train you want to book (0-3): "))

        if not (0 <= selected_train < len(trains)):
            print("Invalid train index. Exiting program.")
            return

        num_passengers = int(input("Enter the number of passengers: "))

        # Validate number of passengers
        if num_passengers <= 0:
            print("Invalid number of passengers. Exiting program.")
            return

        # Perform ticket purchase
        purchase_tickets(trains, selected_train, num_passengers)

        # Display end-of-day summary if all tickets are sold
        if all(train.available_seats == 0 for train in trains):
            display_end_of_day(trains)
            print("All tickets are sold. Exiting program.")
            return


if __name__ == "__main__":
    main()
