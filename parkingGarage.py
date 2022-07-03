import random
import time

class OOPParking:

    
    def __init__(self, clientEntered = False, tickets = random.sample(range(50), 10), oopparkingSpaces = random.sample(range(50), 10), currentTicket = {}):
        self.clientEntered = clientEntered
        self.tickets = tickets
        self.oopparkingSpaces = oopparkingSpaces
        self.currentTicket = currentTicket
    
    
    def takeATicket(self):
        self.clientEntered = True;
        if (len(self.tickets) > 0):
            newTicket = self.tickets.pop()
            newParking = self.oopparkingSpaces.pop()
            print(f'your number is  #{newTicket}, here is your parking space: #{newParking}!')
            self.currentTicket[newTicket] = 'false'
        else:
            print("Garage is full!!")
    

    def pay4parking(self):
        ticketNum = int(input('ticket number? '))

        if (ticketNum in self.currentTicket):
            paidTicket = input("'pay' to confirm payment ")

            if (paidTicket.lower() == 'pay'):
                self.tickets.append(ticketNum)
                self.oopparkingSpaces.append(ticketNum)
                self.currentTicket[ticketNum] = 'true'
            else:
                print('your payment was declined!!')
                self.pay4parking()
        else:
            print('check your ticket number !')
            self.pay4parking()
    

    def leaveOOPParking(self):
        if (self.clientEntered):
            print('checking payment status')
            time.sleep(2)
            for value in self.currentTicket.values():
                if (value == 'false'):
                    print("you didnt pay yet!!")
                else:
                    print('thank you!!! ')
        else:
            print('enter the garage please!! ')




christianGarage = OOPParking()

christianGarage.takeATicket()
christianGarage.pay4parking()
christianGarage.leaveOOPParking()

