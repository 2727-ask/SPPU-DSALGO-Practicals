from colorama import Fore, Style
print(Fore.MAGENTA+"=======================================================")
print(Fore.LIGHTBLUE_EX+"Press 1 for Adding Data")
print(Fore.LIGHTBLUE_EX+"Press 2 for Attendance")
print(Fore.LIGHTBLUE_EX+"Press 3 to Display Result Analytics")
print(Fore.MAGENTA+"=======================================================")

freq={}
DataBase=[]
Attendance = []
while True:
    choice = input("Enter Choice")
    if choice=='1':
        pairs = []
        name = input("Enter Name of Student")
        marks = int(input("Enter marks of Student"))
        pairs.append(marks)
        pairs.append(name)
        DataBase.append(pairs)

    elif choice=='2':
        name = input("Enter Name of Absent Student")
        Attendance.append(name)


    elif choice == '3':
        sum=0
        SortedArray = sorted(DataBase)
        for x in range(len(SortedArray)):
            sum=sum+SortedArray[x][0]
        avg = sum/len(SortedArray)
        print(Fore.YELLOW+"=========================[STUDENTS DATA-STRUCTURE'S MARKS ANALYTICS]==============================")
        print(Fore.LIGHTBLUE_EX+"++++++++++++++++*** [Average of Marks] ***++++++++++++++++++")
        print(Fore.LIGHTCYAN_EX+"Average marks obtained By Students in DataStructures is",avg)
        print(Fore.LIGHTBLUE_EX+"=======================================================")
        lowMarks = SortedArray[0][0]
        lowName = SortedArray[0][1]
        highMarks = SortedArray[len(SortedArray)-1][0]
        HighName = SortedArray[len(SortedArray)-1][1]
        print(Fore.YELLOW+"++++++++++++++++*** [Ranking] ***++++++++++++++++++")
        print(Fore.LIGHTCYAN_EX+"Highest Marks Are Scored By",HighName,"and He Scored",highMarks)
        print(Fore.LIGHTCYAN_EX+"Lowest Marks Are Scored By",lowName,"and He Scored",lowMarks)
        print("=======================================================")
        AbsentStudents = len(Attendance)
        PresentStudent = len(SortedArray)
        print("++++++++++++++++*** [Students Attendance Record] ***++++++++++++++++++")
        print(Fore.LIGHTCYAN_EX+"List of Students Absent For The Test:",AbsentStudents)

        print(Fore.LIGHTCYAN_EX+"List of Students Present For The Test:", PresentStudent)
        print(Fore.LIGHTYELLOW_EX+"=======================================================")

        for x in range(len(DataBase)):
            if DataBase[x][0] in freq:
                freq[DataBase[x][0]] = freq[DataBase[x][0]]+1
            else:
                freq[DataBase[x][0]] = 1


        print(Fore.LIGHTCYAN_EX+"Marks Frequency ",freq)
        print(Fore.MAGENTA+"=================================================================")
    else:
        print(Fore.RED+"Warning!!!!!!! Please Enter Valid Data!!!!!")
        print(Style.RESET_ALL)





