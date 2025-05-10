import index


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.ctr = 0

    def insert_end(self, new_data):
        new_node = Node(new_data)
        # new_node = Node(n)
        self.ctr += 1
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def insert_front(self, new_data):
        new_node = Node(new_data)
        self.ctr += 1
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def delete_front(self, delete):
        self.ctr -= 1
        if self.head is None or delete is None:
            return
        if self.head == delete:
            self.head = delete.next
        if delete.next is not None:
            delete.next.prev = delete.prev
        if delete.prev is not None:
            delete.prev.next = delete.next
        print("student deleted")

    def delete_end(self):
        self.ctr -= 1
        if self.head is not None:
            if self.head.next is None:
                self.head = None
                print("student deleted")
            else:
                temp = self.head
                while temp.next.next is not None:
                    temp = temp.next
                lastNode = temp.next
                temp.next = None
                lastNode = None
                print("student deleted")

    def printDLList(self, node):

        print("__________________________________________")
        while node:
            for i in range(self.ctr):
                print("\n***Student {} Data***".format(i + 1))
                print("__________________________________________")
                print("{}".format(node.data))
                last = node
                node = node.next
        print("__________________________________________")

    def search(self, rollno):
        temp = self.head
        while temp.data.read_regno() != rollno and temp.next:
            temp = temp.next
        if temp.data.read_regno() != rollno and temp.next is None:
            return "No Record Found!"
        else:
            return temp.data

    def modify(self, rollno):
        temp = self.head
        while temp.data.read_regno() != rollno and temp.next:
            temp = temp.next
        if temp.data.read_regno() != rollno and temp.next is None:
            print("No Record Found!")
        else:
            ch = str(input("""What you want to change?
1. Name
2. Gender
3. Department\n"""))
            if ch == '1':
                temp.data.set_name(input("Enter your new Name: "))
            elif ch == '2':
                temp.data.set_gender(input("Enter your new gender: "))
            elif ch == '3':
                temp.data.set_dept(input("Enter your new Department: "))
            else:
                print("Invalid Option Chosen!")
                return self.modify(rollno)


class Student:
    def __init__(self):
        self.name = None
        self.gender = None
        self.regno = None
        self.dept = None

    def set_name(self, name):
        self.name = name

    def set_gender(self, gender):
        self.gender = gender

    def set_regno(self, regno):
        self.regno = regno

    def set_dept(self, dept):
        self.dept = dept

    def read_regno(self):
        return self.regno

    def __str__(self):
        return f"""Name of Student: {self.name}
Gender of Student: {self.gender}
Reg_No of Student is: {self.regno}
Department of Student is: {self.dept}
"""


def main():
    dl = DoublyLinkedList()  # object of class which will use to access the function in classes

    while True:
        print("***********************************************")  # main menu
        print('1. Student induction AT END')
        print('2. Student induction AT front')
        print('3. Total number of student')
        print('4. Student detail/ Status')
        print('5. Delete from front student')
        print('6. Delete from end student')
        print('7. Search Data of Students by Registration No')
        print('8. Modify your data')
        print("9. Return to Main Menu")
        print('10. To Exit!')
        print("***********************************************")
        ch = int(input("Enter your choice:"))
        print("\n" * 3)
        if ch == 1:
            n = int(input("Enter the number of Students to add :"))
            for i in range(n):
                print("Student {} details".format(i + 1))
                student = Student()
                data = input("Enter name: \n")
                student.set_name(data)
                data = input("Enter Registration No:\n")
                student.set_regno(data)
                data = input("Enter Gender:\n")
                student.set_gender(data)
                data = input("Enter Department:\n")
                student.set_dept(data)
                dl.insert_end(student)
                print("\n"*3)
                print("Details Are Entered Successful")

        elif ch == 2:
            n = int(input("Enter the number of Students to add:"))
            for i in range(n):
                student = Student()
                data = input("Enter name:\n")
                student.set_name(data)
                data = input("Enter Reg No:\n")
                student.set_regno(data)
                data = input("Enter Gender :\n")
                student.set_gender(data)
                data = input("Enter Department:\n")
                student.set_dept(data)
                dl.insert_front(student)
                print("\n" * 3)
                print("Details Are Entered Successful")

        elif ch == 3:
            if dl.ctr == 0:
                print("No students detail has been found")
            else:
                print("Total number of students:\n", dl.ctr)
        elif ch == 4:
            if dl.ctr == 0:
                print("No students detail has been found")
            else:
                print("Details of Student")
                dl.printDLList(dl.head)

        elif ch == 5:
            if dl.ctr == 0:
                print("No Students details has been found")
            else:
                dl.delete_front(dl.head)

        elif ch == 6:
            if dl.ctr == 0:
                print("No students Details has been found")
            else:
                dl.delete_end()

        elif ch == 7:
            regNo = input("Enter rollno: ")
            print(dl.search(regNo))

        elif ch == 8:

            regNo = input("Enter rollno: ")
            dl.modify(regNo)
        elif ch == 9:
            index.main()
        else:
            print("Thank You")
            exit()

#Driver's code
if __name__ == "__main__":  # main body
    main()