import Faculty_Module
import Student_Module  # import all the dependency filesimport
import Course_Module
import login


def select(cho):
    if cho == 1:
        print("\n" * 3)
        print("\n               ****** Faculty Management ******\n")
        Faculty_Module.main()   # another python scripts or Module can be called using import function

    elif cho == 2:
        print("\n" * 3)
        print("\n               ****** Student Management ******\n")
        Student_Module.main()

    elif cho == 3:
        print("\n" * 3)
        print("\n               ****** Course Management ******\n")
        Course_Module.main()

    elif cho == 4:
        print("\n" * 3)
        print("\n               ****** Login Management ******\n")
        login.main()
    else:
        print("Thank you")
        exit()


def main():
    print("                     \n\n************ University Management System ************\n\n")
    print("***********************************************")
    print("|Enter 1 for Faculty Management")
    print("\n|Enter 2 for Student Management\n")
    print("|Enter 3 for Course Management\n")
    print("|Enter 4 for Login Management\n")
    print("|Enter 5 for Exit!\n")
    print("***********************************************")
    choice = int(input("Enter  choice:  "))
    select(choice)


if __name__ == "__main__":
    main()