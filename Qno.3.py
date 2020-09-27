
"""3
Write a Python program for department library which has N books, write functions for following:
a) Delete the duplicate entries
b) Display books in ascending order based on cost of books
c) Count number of books with cost more than 500.
d) Copy books in a new list which has cost less than 500."""
print("____________________________________________")
print("Enter 1 For Data Updates")
print("Enter 2 For Data Analytics")
print("____________________________________________")
Data=[]
price_less_500 = []
while True:
    choice = int(input("Enter Your Choice"))
    if choice == 1:
        List=[]
        Book_Name = input("Enter Name Of Book")
        Book_Price= int(input("Enter Price"))

        if [Book_Price,Book_Name] not in Data:
            List.append(Book_Price)
            List.append(Book_Name)
            Data.append(List)
        else:
            print("Already Exists")
    elif choice==2:
        Sorted_Data = (sorted(Data))
        count = 0
        for x in range(len(Data)):
            if Sorted_Data[x][0] >= 500:
                count = count + 1
            else:
                price_less_500.append(Data[x])
        print("+++++++++++++++++++++++++{Data Anaysis}++++++++++++++++++++++++++++++++++++++++")
        print("List of Books in Ascending Orders",Sorted_Data)
        print("There are", count, "Books whose Price is greater Than 500")
        print("The List of books whose price is less than 500 is", price_less_500)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    else:
        print("Please Enter valid Data")













