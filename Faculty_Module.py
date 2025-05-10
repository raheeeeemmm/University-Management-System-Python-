import index


# A linked list node
class Node:

    # Constructor to create a new node
    def __init__(self, name, gender, pin, contact, address, designation, salary):
        self.name = name
        self.gender = gender
        self.pin = pin
        self.contact = contact
        self.address = address
        self.designation = designation
        self.salary = salary
        self.next = None
        self.prev = None


# Class to create a Doubly Linked List
class faculty:

    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None
        self.ctr = 0

    # Given a reference to the head of a list and an
    # integer, inserts a new node on the front of list
    def push_beg(self, name, gender, pin, contact, address, designation, salary):

        self.ctr += 1
        new_node = Node(name, gender, pin, contact, address, designation, salary)

        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def delete_beg(self):
        if self.head is not None:
            self.head = self.head.next
            self.ctr -= 1
            print("Recent Faculty Details Has Been Deleted Successfully")
        else:
            print("No Details found")

    def push_end(self, name, gender, pin, contact, address, designation, salary):

        self.ctr += 1
        new_node = Node(name, gender, pin, contact, address, designation, salary)

        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while last.next:
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

        # 7. Make last node as previous of new node
        new_node.prev = last
        return

    def delete_end(self):
        if self.ctr == 0:
            print("No Details found")
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.prev.next = None
        self.ctr -= 1
        print("Faculty Details Has Been Deleted Successfully")

    # This function prints contents of linked list
    # starting from the given node
    def printList(self):
        if self.ctr != 0:
            node = self.head
            while node:
                for i in range(self.ctr):
                    print("________________________________________________")
                    print("****Faculty {} Details****\n".format(i + 1))
                    print("|Name:   ", node.name)
                    print("|Gender: ", node.gender)
                    print("|Pin no: ", node.pin)
                    print("|Contact:", node.contact)
                    print("|Address:", node.address)
                    print("|Designation: ", node.designation)
                    print("|Salary: ", node.salary)
                    print("________________________________________________\n")
                    node = node.next
        else:
            print("No Faculty Details Has Been Entered Yet\n\n")

    # Function to search name and print details
    def search_name(self, name):
        if self.ctr != 0:
            node = self.head
            if node.name == name:
                while node:
                    if node.name == name:
                        print("User Found")
                        print("________________________________________________")
                        print("|Name:   ", node.name)
                        print("|Gender: ", node.gender)
                        print("|Pin no: ", node.pin)
                        print("|Contact:", node.contact)
                        print("|Address:", node.address)
                        print("|Designation: ", node.designation)
                        print("|Salary: ", node.salary)
                        print("________________________________________________\n")
                        node = node.next

            elif node.name != name:
                print("No Faculty Person Match With Your Entered Name \n\n")
        else:
            print("No Faculty Has Been Entered Yet\n\n")

            # Function to search pin and print details

    def search_pin(self, pin):
        if self.ctr != 0:
            node = self.head
            if int(node.pin) == pin:
                while node:
                    if int(node.pin) == pin:
                        print("User Found")
                        print("________________________________________________")
                        print("|Name:   ", node.name)
                        print("|Gender: ", node.gender)
                        print("|Pin no: ", node.pin)
                        print("|Contact:", node.contact)
                        print("|Address:", node.address)
                        print("|Designation: ", node.designation)
                        print("|Salary: ", node.salary)
                        print("________________________________________________\n")
                        node = node.next

            elif int(node.pin) != pin:
                print("No Faculty Person Match With Your Entered Pin No\n\n")
        else:
            print("No Faculty Has Been Entered Yet\n\n")
            # Function to modify details by name

    def modify(self, name):
        node = self.head
        if self.ctr != 0:
            if node.name == name:
                while node:
                    if node.name == name:
                        print("User Found")
                        print("________________________________________________")
                        print("|Name:  ", node.name)
                        print("|Gender:", node.gender)
                        print("|Pin no:", node.pin)
                        print("|Contact:", node.contact)
                        print("|Address:", node.address)
                        print("|Designation: ", node.designation)
                        print("|Salary: ", node.salary)
                        print("________________________________________________\n")

                        # Input modified data
                        node.name = input("Enter Modified Name: ")
                        node.gender = input("Enter Modified Gender: ")
                        node.pin = input("Enter Modified Pin: ")
                        node.contact = input("Enter Modified Contact: ")
                        node.address = input("Enter Modified Address: ")
                        node.designation = input("Enter Modified Designation: ")
                        node.salary = input("Enter Modified Salary: ")
                    # Next node

                    node = node.next
            else:
                print("No Faculty Person Match with your Entered Details:")

            print("\n" * 3)
            print("Details are Modified Successfully ")
        elif self.ctr == 0:
            print("No Details Has Been Entered Yet\n")


def main():
    fac = faculty()
    # Iterate continuously till break is called
    while 1:
        # Menu
        print("***********************************************")
        print("1. Input Multiple Faculty Details.            *")
        print("2. Total Faculty Count.                       *")
        print("3. Perform Insertion, Deletion at End.        *")
        print("4. Delete Recently Added Faculty person.      *")
        print("5. Update Faculty Information.                *")
        print("6. Search And Display Faculty By Name And Pin.*")
        print("7. Display All Faculty With Their Details.    *")
        print("8. Exit.                                      *")
        print("9. Return To Main menu.                       *")
        print("***********************************************")

        choice = int(input("Enter your Choice: "))
        print("\n" * 3)
        if choice == 1:

            n = int(input("Enter Number Of Faculty Person´s To Add: "))
            for i in range(n):
                print("\nEnter Faculty {} details:".format(i + 1))
                name = input("\nEnter Name: ")
                gender = input("Enter Gender: ")
                pin = int(input("Enter Pin No.(6 digits): "))
                contact = input("Enter Contact No.: ")
                address = input("Enter Address: ")
                designation = input("Enter Designation: ")
                salary = input("Enter Salary(Rs): ")
                fac.push_beg(name, gender, pin, contact, address, designation, salary)
            print("\n\nDetails Are Successfully Entered \n\n")
        elif choice == 2:
            print("Total Faculty Person´s Details Entered: ", fac.ctr, "\n")

        elif choice == 3:
            print("1. For insertion at end")
            print("2. For deletion from end")
            ch = int(input())
            if ch == 1:
                name = input("Enter Name: ")
                gender = input("Enter Gender: ")
                pin = int(input("Enter Pin No.(6 digits): "))
                contact = input("Enter Contact No.: ")
                address = input("Enter Address: ")
                designation = input("Enter  Designation: ")
                salary = input("Enter Salary(Rs): ")
                fac.push_end(name, gender, pin, contact, address, designation, salary)
                print("\n\nDetails Are Successfully Entered At The End \n\n")
            else:
                fac.delete_end()

        elif choice == 4:
            fac.delete_beg()

        elif choice == 5:
            print("Enter Faculty Person Name, That You want To Update his Details: ")
            name = input()
            fac.modify(name)

        elif choice == 6:
            print("1. Search By Name")
            print("2. Search By pin")
            ch = int(input())
            if ch == 1:
                name = input("Enter Name: ")
                fac.search_name(name)
            elif ch == 2:
                pin = int(input("Enter Pin: "))
                fac.search_pin(pin)

        elif choice == 7:
            fac.printList()

        elif choice == 8:
            print("Thank You")
            break
        elif choice == 9:
            index.main()
        else:
            print("Invalid Choice")


# Driver Method
if __name__ == '__main__':
    main()
