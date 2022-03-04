def main():
    myList = []
    choice = 'a'
    while choice != 'x':
        
        if choice == 'a' or choice == 'A': 
            option1(myList)
        elif choice == 'b' or choice == 'B':
            option2(myList)
        elif choice == 'c' or choice == 'C':
            option3(myList)
        elif choice == 'd' or choice == 'D':
            option4(myList)
        elif choice == 'x' or choice == 'X':
            break
        choice = displayMenu()


    print ("\nProgram Exiting!\n\n")

def displayMenu():
    myChoice = 0
    while myChoice not in ["a","b","c","d","e","x","A","B","C","D","E","X"]:
        print("""\n\nPlease choose
                A. Add a number to the list/array
                B. Print the list/array
                C. Display and Separate the Odd and Even Numbers.
                D. Print the list/array and sort it in reverse order
                X. Quit
                """)
        myChoice = input("Enter option---> ")
        if myChoice not in ["a","b","c","d","e","x","A","B","C","D","E","X"]:
            print("Invalid option. Please select again.")

    return myChoice

# Option A: Add a number to the list/array
def option1(myList):
    num = -1
    while num < 0:
        num = int(input("\n\nEnter a N integer: "))
        if num < 0:
            print("Invalid value. Please re-enter.")
    myList.append(num)


# Option B: Print the list/array
def option2(myList):
    print(sorted(myList))

# Option C: Display and Separate the Odd and Even Numbers.
def option3(myList):
    even = [] 
    odd = [] 
    for i in myList: 
        if (i % 2 == 0): 
            even.append(i) 
        else: 
            odd.append(i) 
    print("Even lists:", even) 
    print("Odd lists:", odd) 
    
# Option D: Print the list/array and sort it in reverse order
def option4(myList):
    print(sorted(myList, reverse=True))

main()