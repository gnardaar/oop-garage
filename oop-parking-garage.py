class denverParking():

    def __init__(self, arrive, space, ticket):
        self.arrive = ["A1", "B2", "C3", "D4", "E5", "F6", "G7", "H8", "I9", "J10"]
        self.space = ["A1", "B2", "C3", "D4", "E5", "F6", "G7", "H8", "I9", "J10"]
        self.ticket = { "False": "A1", "False": "B2", "False": "C3", "False": "D4", "False": "E5", 
                            "False": "F6", "False": "G7", "False": "H8", "False": "I9", "False": "J10"}

    def enter(self, arrive, space):
        print("Welcome to our parking garage! Please take a ticket and the corresponding space.")
        for arrive in self.arrive:
            self.arrive.remove(arrive)
        for space in self.space:
            self.space.remove(space)
    

    def leave(self):
        if self.ticket:
            print("Thank you, please come back to Denver")
        else:
            time = input(int("How many time were you parked for? "))
            rate = 10
            if time > 0:
                cost = int(time) * rate
                print("You owe: ", cost)
                response = input("To pay enter 'y' ")
                if response.lower() == 'y':
                    print("Thank you for using Denver Parking, please come again")
                    self.ticket["True"] = self.ticket.pop("False")
                else:
                    print("Error, please enter 'y', or 'n'.")
            else:
                print("Error, please enter 'y', or 'n'.")
        for arrive in self.arrive:
            self.arrive.append(arrive)
        for space in self.space:
            self.space.append(space)
    
    def pay(self):
        time = input("How many hours did you parked for? ")
        if int(time) > 0:
            cost = int(time) * 10
            print(f"You owe $", cost)
            response = input("To pay type 'y' " )
            if response.lower() == 'y':
                print("Thank you, please leave the garage in the next 5 mins")
                self.ticket["True"] = self.ticket.pop("False")
            elif response.lower() == 'n':
                noResponse = input("you can stay as long as you want to, but to leave,type 'y' to pay")
                if noResponse.lower() == 'y':
                    print("Thank you, please leave the garage in the next 5 mins")
                    self.ticket["True"] = self.ticket.pop("False")
                elif noResponse == 'n':
                    print("dude you parked here for absolutely too dang long... So we towed your car!")
                    self.ticket["True"] = self.ticket.pop("False")
            else:
                print("Error, please enter 'y', or 'n'.")
        else:
            print("go back to California")


class UI(denverParking):
    def ___int__(self):
        super().__init__()

    def run():
        denverParking = denverParking([], [], {})
        print("Welcome to Denver Parking, only $10 per hour!")
        while True:
            ticketResponse = input("Would you like to park in Denver today? Type 'y' or 'n'. " )
            if ticketResponse.lower() == "y":
                denverParking.enter([], [])
                while True:
                    payResponse = input("Would you like to pay for your parking time and leave? Type 'y' or 'n'. ")
                    if payResponse.lower() == "y":
                        denverParking.pay()
                        while True:
                            leaveResponse = input("Would you like to leave? Type 'y' or 'n'.")
                            if leaveResponse.lower() == "y":
                                denverParking.leave()
                                break
                            elif leaveResponse.lower() == "n":
                                print("dude parking here is only 10 dollars, you can stay as long as you have the monies!")
                                denverParking.pay()
                            else:
                                print("Error, please enter 'y', or 'n'.")
                    elif payResponse.lower() == "n":
                        print("dude parking here is only 10 dollars, you can stay as long as you have the monies!")
                        denverParking.pay
                    else:
                        print("Error, please enter 'y', or 'n'.")
            elif ticketResponse.lower() == "n":
                print("Maybe try your luck in Cambridge!")
                break
            else:
                print("Error, please enter 'y', or 'n'.")

def main():
    UI.run()

if __name__ == "__main__":
    main()