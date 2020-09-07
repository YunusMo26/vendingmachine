#Author: Yunus Maltiti Mohammed
#Project Name: Vending Machine
#Project Code: py0120
#Language: Python
#Work in progess...
#last editted: 03/03/2020
#Can currently support only one vending machine
#Will have to create a new vending machine system each time you login, author yet to create permanent storage (database)
#Inspiration: Kitkat abuse
from sys import exit

class Vending_Machine():
    """Creates vending machine objects.

    Attributtes:
    id:  string representing id of machine
    snacks: dictionary with key,value (snack name, Snacks object)
    people: dictionary with key,value (int, Person object)
    balance: a float of the amount(money) vending machine has made from
                sales
    """

    def __init__(self,id, snacks = {}, people = {}, balance=0):
        """A vending machine with identification id containg snacks and
        a dictionary of people allowed access.
        """
        self.id = id
        self.snacks = snacks
        self.people = people
        self.account = balance

    def create_snack(self):
        """Creates a snack object and puts it in Vending_Machine object.

        PRECONDITIONS:
        vending_machine: An existing Vending_Machine object
        quantity of snack to be stocked greater than 0

        returns: None
        """
        name = input('> What is the name of the snack you are putting in me?\n')
        price = float(input('> How much does %s cost?\n' % name))
        quantity = int(input('> How many %s are you putting in?\n' % name))
        assert quantity > 0, "Come back when you have enough snacks."

        self.snacks[name] = Snacks(name, price, quantity)

    def create_person(self):
        """Creates a Person object and puts it in Vending_Machine access
        list/dictionary

        PRECONDITIONS:
        Vending_Machine: An existing Vending_Machine object
        balance is non-negative

        returns: None
        """
        name = input('> What is your prefered name?\n').strip()
        assert name not in self.people, "%s used already. Use another name.\nQuiting..." % name
        id = input('> What is your prefered id?\n').strip()
        password = input('> What is your password?\n')
        balance = float(input('> What is your initial deposit in USD?\n'))
        assert balance >= 0, "Negative funds not allowed"

        if verification():
            self.people[name] = Person(id, password, balance)
            print(f"Account created for {name}.")
        else:
            print("Failed to verify admin....\nQuiting...")

    def transaction(self):
        """Allows a Person object in an existing Vending_Machine's people list to
        buy an existing Snack object from the Vending_Machine object.

        PRECONDITIONS:
        customer has enough money in account to buy snacks
        number of snacks to be bought present greater than 0
        number of snacks to be bought non negative

        returns: None
        """
        customer = input(">What is your name?\n")
        snack = input(">Which snack are you buying?\n")
        if self.login(customer):
            quant = int(input('> How many %s are you buying?\n' % snack))
            cost = quant * vending_machine.snacks[snack].price
            assert quant <= self.snacks[snack].number_present, "Not enough %s in machine. Ask admin to refill" % snack
            assert self.people[customer].account >= cost, "Not enough funds"
            try:
                print("Processing transaction")
                self.snacks[snack].number_present -= quant
                self.people[customer].account -= cost
                self.account += vending_machine.snacks[snack].price
                print(f"Your new balance is {self.people[customer].account}")
                print("Transcation complete.")
                print("Enjoy your %d %s" % (quant, snack))

            except:
                #Yet to code a better exception
                print("Something went wrong")
        else:
            print("You failed to login.\nQuiting...")

    def add_money(self):
        """Adds money to balance of an existing Person object.

        PRECONDITIONS:
        self: A Vending_Machine object.
        amount added should be non negative.
        returns: None"""
        if verification():
            customer = input('> What is your name?\n')
            assert customer in self.people, "You are not registered.\nQuiting..."
            print("Logging in...")
            assert self.login(customer), "Failed to login.\nQuiting..."
            amount = float(input('> How much are you recharging?\n'))
            print(f"Adding {amount} to your account. Wait a second...")
            self.people[customer].account += amount
            print(f"Your new balance is {self.people[customer].account}")
            print("Transaction Complete!!!")
        else:
            print("Failed to verify admin.\nQuiting...")

    def login(self, customer):
        """Allows customer to login to carry out a transaction.

        PRECONDITIONS:
        self: an existing Vending_Machine object.
        customer: an existing Person object registered on self.

        returns: boolean. True if login is successsful, False otherwise.
        """
        print(f"Logging into a registered user's account in {vending_machine.id}")
        if True:
            username = input(">Input your username\n")
            assert username == self.people[customer].id, "Wrong username.\nQuiting..."
            password = input('What is your password?\n')
            assert password == self.people[customer].password, "Wrong password.\nQuiting..."
            return True
        else:
            return False

class Snacks():
    """Creates Snack objects to put in vending machine
    ...
    """

    def __init__(self, name, price, number_present):
        """A snack object of identification name.

        name: Name of the snack, a string
        price: price of the snack, a float
        number_present: number of {name} snacks, an int
        """
        self.name = name
        self.price = price
        self.number_present = number_present

class Person():
    """Creates a person object who can access the vending machine
    ...
    """

    def __init__(self, id, password, balance = 0.0):
        """A person with identification {id} holding an amount of {balance}

        id: identification of person, a string
        password: password of the person, a string
        balance: amount the person hold, a float
        """
        self.id = id
        self.password = password
        self.account = balance


def create_vending_machine():
    """Creates a Vending_Machine object.

    returns: Vending_Machine Object
    """
    print("Creating new vending machine....")
    id = input("What is the id of the machine?\n")
    if verification():
        print("Creating Vending Machine %s...Done!!!" % id)
        return Vending_Machine(id)
    else:
        print("Wrong admin passsword....\nQuiting...")

def verification():
    """ Verifies if admin is '0000'

    admin: A string
    return: boolean. True if admin is '0000', False otherwise"""
    admin = input('> What is the admin password (type 0000)?\n')
    return admin == '0000'

def engine():
    global vending_machine
    print("Hello. Welcome to this under-construction vending machine projects.")
    print("Make sure you read specifications to prevent unhandled errors.")
    print("\nSelect (type in) the number of the operation you want to perform")
    print("1. Create a new vending machine system.")
    print("2. Create a new customer account.")
    print("3. Add money to an existing customer's account.")
    print("4. Create and stock a new snack to an existing vending machine.")
    print("5. Buy a snack in stock in an existing vending machine.")
    print("6. Exit the system.")

    task = input("> Select and type in number from 1 through 6:\n").strip()

    if task == '1':
        vending_machine = create_vending_machine()
        engine()
    elif task == '2':
        vending_machine.create_person()
        engine()
    elif task == '3':
        vending_machine.add_money()
        engine()
    elif task == '4':
        vending_machine.create_snack()
        engine()
    elif task == '5':
        vending_machine.transaction()
        engine()
    elif task == '6':
        exit(0)
    else:
        print("Invalid input.")
        engine()


if __name__ == '__main__':
    engine()
