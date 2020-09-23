all=[]
idv=[0]

mC_B=[]
mC=[]
mB=[]
mF=[]
mC_F=[]
print("_________________________________________________")
print(1,"Type 1 to add new entry")
print(2,"Type 2 to show database")
print("_________________________________________________")


while True:
    choice =int(input("Enter Your choice"))
    if choice == 1:

        g_name= input("Enter your group name")
        id=int(input("Enter your Id"))
        if id not in idv:
            idv.append(id)
            name=input("Enter your name")
            sports=input("Enter sports you play").split()
            GA=[g_name,id,name,sports]
            all.append(GA)
        else:
            print("Id Already exists")
    else:
        for x in range(len(all)):
            if 'cricket' in all[x][3] and 'badminton' in all[x][3]:
                C_B = []
                C_B.append(all[x][0])
                C_B.append(all[x][1])
                C_B.append(all[x][2])
                mC_B.append(C_B)

            elif 'badminton' in all[x][3] and 'cricket'and'football' not in all[x][3]:
                B=[]

                B.append(all[x][0])
                B.append(all[x][1])
                B.append(all[x][2])
                mB.append(B)

            elif 'cricket' in all[x][3] and 'badminton'and'football' not in all[x][3]:
                C=[]
                C.append(all[x][0])
                C.append(all[x][1])
                C.append(all[x][2])
                mC.append(C)


            elif 'football' in all[x][3] and 'cricket'not in all[x][3] and 'badminton' not in all[x][3]:
                F=[]
                F.append(all[x][0])
                F.append(all[x][1])
                F.append(all[x][2])
                mF.append(F)

            elif 'cricket'  in all[x][3] and  'football' in all[x][3]  or 'badminton' not in all[x][3]:
                C_F=[]
                C_F.append(all[x][0])
                C_F.append(all[x][1])
                C_F.append(all[x][2])
                mC_F.append(C_F)


        print("*list of students playing Cricket and badminton both*","\n",mC_B,"\n")
        print("*list of students playing Cricket Only*","\n",mC,"\n")
        print("*list of students playing Football *","\n",mF,"\n")
        print("*list of students playing Cricket and FootBall both*","\n",mC_F,"\n")








