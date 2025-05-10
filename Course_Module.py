import index


# A doubly linked list node
class Node:

    # Constructor to create a new node
    def __init__(self, course_name, instructor, course_code, credit_hours, Quiz_weightage, Assignment_weightage,
                 Final_exam_weightage):
        self.course_name = course_name
        self.instructor = instructor
        self.course_code = course_code
        self.credit_hours = credit_hours
        self.Quiz_weightage = Quiz_weightage
        self.Assignment_weightage = Assignment_weightage
        self.Final_exam_weightage = Final_exam_weightage
        self.next = None
        self.prev = None


# Class to create a Doubly Linked List
class Course:

    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None
        self.ctr = 0

    # This function will remove one node from the beginning
    def delete_beg(self):
        if self.ctr == 0:
            print("Course details not found")
        elif self.head is not None:
            self.head = self.head.next
            self.ctr -= 1
            print("Course Deleted")

    def push_end(self, course_name, instructor, course_code, credit_hours, Quiz_weightage, Assignment_weightage,
                 Final_exam_weightage):

        self.ctr += 1

        new_node = Node(course_name, instructor, course_code, credit_hours, Quiz_weightage, Assignment_weightage,
                        Final_exam_weightage)

        # 4. If the Linked List is empty, then make the
        # new node as head
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

    # This function prints contents of linked list
    def printList(self):
        if self.ctr != 0:
            node = self.head
            while node:
                for i in range(self.ctr):
                    print("****  Course {} Details****".format(i + 1))
                    print("________________________________________________")
                    print("\nCourse name:   ", node.course_name)
                    print("|Instructor name: ", node.instructor)
                    print("|Course code no:  ", node.course_code)
                    print("|Credit hours(hr):    ", node.credit_hours)
                    print("|Quiz weightage(%): ", node.Quiz_weightage)
                    print("|Assignment weightage(%): ", node.Assignment_weightage)
                    print("|Final_exam weightage(%): ", node.Final_exam_weightage)
                    print("________________________________________________\n")
                    node = node.next
        else:
            print("No courses details has been entered yet\n\n")

    # Function to search course_name and print details
    def search_course_name(self, course_name):
        if self.ctr != 0:
            node = self.head
            if node.course_name == course_name:
                while node:
                    if node.course_name == course_name:
                        print("Course Found")
                        print("________________________________________________")
                        print("|Course_name:    ", node.course_name)
                        print("|Instructor name:", node.instructor)
                        print("|Course code no: ", node.course_code)
                        print("|Credit hours:   ", node.credit_hours)
                        print("|Quiz weightage: ", node.Quiz_weightage)
                        print("|Assignment weightage: ", node.Assignment_weightage)
                        print("|Final_exam weightage: ", node.Final_exam_weightage)
                        print("________________________________________________\n")
                        node = node.next
            elif node.course_name != course_name:
                print("No course match with your entered course_name\n\n")

        else:
            print("No course has been entered yet\n\n")

            # Function to search course_code and print details

    def search_course_code(self, course_code):
        if self.ctr != 0:
            node = self.head
            if int(node.course_code) == course_code:
                while node:
                    if int(node.course_code) == course_code:
                        print("Course Found")
                        print("________________________________________________")
                        print("|Course name:  ", node.course_name)
                        print("|Instructor name:", node.instructor)
                        print("|Course code no:", node.course_code)
                        print("|Credit hours:", node.credit_hours)
                        print("|Quiz weightage:", node.Quiz_weightage)
                        print("|Assignment weightage: ", node.Assignment_weightage)
                        print("|Final exam weightage: ", node.Final_exam_weightage)
                        print("________________________________________________\n")
                        node = node.next
            elif int(node.course_code) != course_code:
                print("No courses match with your entered course code no\n\n")
        else:
            print("No courses details has been entered yet\n\n")
            # Function to modify details by course_name

    def modify(self, course_name):
        if self.ctr != 0:

            node = self.head

            while node:
                if node.course_name == course_name:
                    print("Course Found")
                    print("________________________________________________")
                    print("|Course name:  ", node.course_name)
                    print("|Instructor name:", node.instructor)
                    print("|Course code no:", node.course_code)
                    print("|Credit hours:", node.credit_hours)
                    print("|Quiz weightage:", node.Quiz_weightage)
                    print("|Assignment weightage: ", node.Assignment_weightage)
                    print("|Final exam weightage: ", node.Final_exam_weightage)
                    print("________________________________________________\n")

                    # Input modified data
                    print("________________________________________________")
                    node.course_name = input("Enter Modified Course name: ")
                    node.instructor = input("Enter Modified Instructor name: ")
                    node.course_code = input("Enter Modified Course code: ")
                    node.credit_hours = input("Enter Modified Credit hours: ")
                    node.Quiz_weightage = input("Enter Modified Quiz weightage: ")
                    node.Assignment_weightage = input("Enter Modified Assignment weightage: ")
                    node.Final_exam_weightage = input("Enter Modified Final exam weightage: ")
                    print("________________________________________________\n")
                    # Next node
                    node = node.next
                    print("Details are modified successfully ")
                elif node.course_name != course_name:
                    print("No courses details found with your entered name")
        else:
            print("no course details has been entered yet")


def main():
    co = Course()
    # Iterate continuously till break is called
    while 1:
        # Menu
        print("***********************************************")
        print("1. Input multiple courses details.            *")
        print("2. Total courses details entered.             *")
        print("3. Delete Course details.                     *")
        print("4. Update Courses information.                *")
        print("5. Search and display courses by name and code*")
        print("6. Display all courses with their details.    *")
        print("7. Exit.                                      *")
        print("8. return to main menu.                       *")
        print("***********************************************")
        choice = int(input("Enter Your Choice: "))
        print("\n" * 3)
        if choice == 1:

            n = int(input("Enter Number Of Courses To Add: "))
            for i in range(n):
                print("Enter Courses {} Details:".format(i + 1))
                print("________________________________________________\n")
                course_name = input("Enter Course name: ")
                instructor = input("Enter Instructor name: ")
                course_code = int(input("Enter Course code No.(6-digits): "))
                credit_hours = input("Enter Credit hours No(hr).: ")
                Quiz_weightage = input("Enter Quiz weightage(%): ")
                Assignment_weightage = input("Enter Assignment weightage(%): ")
                Final_exam_weightage = input("Enter Final_exam weightage(%): ")
                print("________________________________________________\n")
                co.push_end(course_name, instructor, course_code, credit_hours, Quiz_weightage, Assignment_weightage,
                            Final_exam_weightage)
            print("\n" * 3)
            print("\n\nDetails are successfully entered \n\n")
        elif choice == 2:
            print("Total courses details entered: ", co.ctr, "\n\n")

        elif choice == 3:
            co.delete_beg()

        elif choice == 4:
            print("Enter Course Name ,That You Want To Update: ")
            course_name = input()
            co.modify(course_name)

        elif choice == 5:
            print("1. Search by course name")
            print("2. Search by course code")
            ch = int(input())
            if ch == 1:
                course_name = input("Enter course name: ")
                co.search_course_name(course_name)
            elif ch == 2:
                course_code = int(input("Enter course code: "))
                co.search_course_code(course_code)

        elif choice == 6:
            co.printList()

        elif choice == 7:
            print("Thank You")
            break
        elif choice == 8:
            index.main()
        else:
            print("Invalid Choice")


# Driver Method
if __name__ == '__main__':
    main()
