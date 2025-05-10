import index


class Node:

    # Constructor to create a new node
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.next = None
        self.prev = None


# Class to create a Doubly Linked List

class login:

    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None
        self.ctr = 0

    def push_beg(self, name, password):  # This function will push a node in list with multiple parameters(name,pass)
        self.ctr += 1
        new_node = Node(name, password)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def modify(self, name):  # This function will use to update detail in  node.
        node = self.head
        if self.ctr != 0:

            if node.name == name:
                while node:
                    if node.name == name:
                        print("________________________________________________")
                        print("User found")
                        print("Name:  ", node.name)
                        print("________________________________________________\n")

                        node.password = input("Enter Your New Password: ")
                        print("\n" * 3)
                        print("Password Is Modified Successfully ")
                    node = node.next
            elif node.name != name:
                print("No Person With This Name Exist")
        elif self.ctr == 0:
            print("User Not Found")

    def search_password_name(self, name, password):  # This function will take user to University management side.
        if self.ctr != 0:
            node = self.head
            if str(node.name) == name and int(node.password) == password:
                while node:
                    if node.name == name and int(node.password) == password:
                        print("\n" * 3)
                        print("Login Successful")
                        index.main()
                        node = node.next

            elif node.name != name or int(node.password) != password:
                print("\n\nNo Person Match With Your Entered Details"
                      "\nPlease Try Again\n\n")
        else:
            print("\n" * 3)
            print("No Details Has Been Found...\n")
            print("Please Try Again\n\n")


def main():  # main body function
    dll = login()

    print("      \n                         *****************************************"
          "      \n                               UNIVERSITY MANAGEMENT SYSTEM"
          "      \n                         *****************************************"
          "\n         ****Group Members****"
          " \n |Abdul Rahim                       210201097|"
          " \n |Syed Muhammad Dawood Shah         210201004|"
          " \n |Mujeeb Ahmed                      210201039|"
          " \n |Ali Bajwa                         210201087|"
          " \n |Rehman Munawar                    210201060|"
          " \n |Saad Ashraf                       210201064|")
    
    print("\n" * 3)
    while 1:
        # Menu

        print("\n       ******Login System*******")
        print("***********************************************")
        print("1. Sign Up.")
        print("2. Log In.")
        print("3. Forget Password.")

        print("***********************************************")

        choice = int(input(" Enter Your Choice: "))
        print("\n" * 3)
        if choice == 1:
            print("Enter your signup details\n")
            name = input("\nEnter Username: ")
            password = int(input("Create your password: "))
            dll.push_beg(name, password)
            print("\n" * 3)
            print("\n\nUser Details Are Successfully Entered \n\n")
        if choice == 2:
            print("Enter Your Login Details\n")
            name = input("\nEnter Username: ")
            password = int(input("Enter Password No.: "))
            dll.search_password_name(name, password)

        if choice == 3:
            print("Enter Your Previous Details\n")
            name = input("\nEnter Username: ")
            dll.modify(name)


if __name__ == '__main__':
    main()
