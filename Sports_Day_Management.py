#Transfer games file to gameslist as 2D Array
def readFile(filename):
    with open(filename) as gamesfile:
        for record in gamesfile:
            eventRec=record.split(',')
            #Removes /n from the last studentID
            last=eventRec[9].strip()
            #Replace the last student ID without
            #the /n
            eventRec[9]=last
            ''' add each line in the file as a record
            to the gameslist to form a 2D array.'''
            gameslist.append(eventRec)
    gamesfile.close()

#Extract the game ID from gameslist and add it to games list
def groupGames():
    for row in range(0,len(gameslist)):
            games.append(gameslist[row][0])
            
#function for displaying menu options
def display_Option(): 
    print("*"*50)
    print("*"*50)
    print("   <<Welcome to Tournament 2022>>")
    print("""This system helps track of Students score""")
    print("Here are the options:")
    print("""
    A.Enter Ranking for Events
    B.Assign Points to Students
    C.Calculate Students' Points
    D.Display Game Board
    Q.Quit program""")
    print("*"*50)
    print("*"*50)
    choice = input("Enter your choice: ")
    return choice
    
#Check whether the user entry of studentID for game ranking is correct
def validStudent(plist,rank):
    for person in plist:
        if rank==person:
            return True
    print("Participant ID entered is not valid")
    print("You need to enter valid Participant ID again")
    return False

#Add a record of the ranking for each game to game rank list
def addGameRank(netID,rank1,rank2,rank3):
    record=[]
    record.append(netID)
    record.append(rank1)
    record.append(rank2)
    record.append(rank3)
    gameRank.append(record)

#Display option for taking the game event ranking
def enterRankingGames():
    #Checks whether any ranking entry is required
    if len(gamesLeft)>0:
        #Keeps the option menu running until
        #user gives the correct input
        while True:
            #displays the title for the menu
            print("*"*50)
            print("*"*50)
            print(" <<Welcome to game event Selection>>")
            print("Here are the options left to enter ranking:")
            #displays the games require ranking entry
            count=1
            for game in gamesLeft:
                print("Enter", count, "for", game)
                count +=1
            print("*"*50)
            print("*"*50)
            #Validates the user input
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:#deals with entering letters
                print("Make sure to enter a number")
                continue
            if choice <= 0:#deals with 0 or negative number
                print("You need to enter a positive number ")
            elif choice > len(gamesLeft):#deals with input exceeding
                #maximum value
                print("Enter a number for the game choice given: ")
            else:
                break  
        ''' Following selection statement identifies
            the individual game, the user wants to enter
            the ranking 1 to 3.'''
        if gamesLeft[choice-1] =="Nb7":
            #Initialise the list for keeping the participating students for each game
            partId=[]
            #Go through each row in the gameslist 
            for row in range(0,len(gameslist)):
                #Identify the raceID in the gameslist
                if gameslist[row][0]=="Nb7":
                    #Add the participants ID from the gameslist to partId list
                    for index in range(1,10):
                        partId.append(gameslist[row][index])
            
            #Displays the studentID for the participants of the netball game Nb7
            print("Below is the participant list for the netball game Nb7")
            print("*"*12)
            print(partId[0],partId[1],partId[2])
            print(partId[3],partId[4],partId[5])
            print(partId[6],partId[7],partId[8])
            print("*"*12)
            
            check=False
            while check==False:
                rank1=input("Enter the studentID who came first in Nb7: ")
                 #calls the sub program to validate the studentID for the ranking
                check=validStudent(partId,rank1)
            #removes the studentID entred already to avoid duplicate entry
            partId.remove(rank1)
            check=False
            while check==False:
                    rank2=input("Enter the studentID who came second in Nb7: ")
                    check=validStudent(partId,rank2)
            partId.remove(rank2)
            check=False
            while check==False:
                    rank3=input("Enter the studentID who came third in Nb7: ")
                    check=validStudent(partId,rank3)
            addGameRank("Nb7",rank1,rank2,rank3)
            gamesLeft.remove("Nb7")
        elif gamesLeft[choice-1] =="Nb8":
            #Initialise the list for keeping the participating students for each game
            partId=[]
            #Go through each row in the gameslist 
            for row in range(0,len(gameslist)):
                #Identify the raceID in the gameslist
                if gameslist[row][0]=="Nb8":
                    #Add the participants ID from the gameslist to partId list
                    for index in range(1,10):
                        partId.append(gameslist[row][index])
            
            #Displays the studentID for the participants of netball game Nb8
            print("Below is the participant list for the netball game Nb7")
            print("*"*12)
            print(partId[0],partId[1],partId[2])
            print(partId[3],partId[4],partId[5])
            print(partId[6],partId[7],partId[8])
            print("*"*12)
            
            check=False
            while check==False:
                rank1=input("Enter the studentID who came first in Nb8: ")
                 #calls the sub program to validate the studentID for the ranking
                check=validStudent(partId,rank1)
            #removes the studentID entred already to avoid duplicate entry
            partId.remove(rank1)
            check=False
            while check==False:
                    rank2=input("Enter the studentID who came second in Nb8: ")
                    check=validStudent(partId,rank2)
            partId.remove(rank2)
            check=False
            while check==False:
                    rank3=input("Enter the studentID who came third in Nb8: ")
                    check=validStudent(partId,rank3)
            addGameRank("Nb8",rank1,rank2,rank3)
            gamesLeft.remove("Nb8")
        elif gamesLeft[choice-1] =="Nb9":
            #Initialise the list for keeping the participating students for each game
            partId=[]
            #Go through each row in the gameslist 
            for row in range(0,len(gameslist)):
                #Identify the raceID in the gameslist
                if gameslist[row][0]=="Nb9":
                    #Add the participants ID from the gameslist to partId list
                    for index in range(1,10):
                        partId.append(gameslist[row][index])
            
            #Displays the studentID for the participants of netball game Nb9
            print("Below is the participant list for the netball game Nb9")
            print("*"*12)
            print(partId[0],partId[1],partId[2])
            print(partId[3],partId[4],partId[5])
            print(partId[6],partId[7],partId[8])
            print("*"*12)
            
            check=False
            while check==False:
                rank1=input("Enter the studentID who came first in Nb9: ")
                 #calls the sub program to validate the studentID for the ranking
                check=validStudent(partId,rank1)
            #removes the studentID entred already to avoid duplicate entry
            partId.remove(rank1)
            check=False
            while check==False:
                    rank2=input("Enter the studentID who came second in Nb9: ")
                    check=validStudent(partId,rank2)
            partId.remove(rank2)
            check=False
            while check==False:
                    rank3=input("Enter the studentID who came third in Nb9: ")
                    check=validStudent(partId,rank3)
            addGameRank("Nb9",rank1,rank2,rank3)
            gamesLeft.remove("Nb9")
        elif gamesLeft[choice-1] =="Ra10":
            #Initialise the list for keeping the participating students for each 200M race
            partId=[]
            #Go through each row in the gameslist 
            for row in range(0,len(gameslist)):
                #Identify the raceID in the gameslist
                if gameslist[row][0]=="Ra10":
                    #Add the participants ID from the gameslist to partId list
                    for index in range(1,10):
                        partId.append(gameslist[row][index])
            
            #Displays the studentID for the participants of Ra10 200M race
            print("Below is the participant list for the Ra10 200M race")
            print("*"*12)
            print(partId[0],partId[1],partId[2])
            print(partId[3],partId[4],partId[5])
            print(partId[6],partId[7],partId[8])
            print("*"*12)
            
            check=False
            while check==False:
                rank1=input("Enter the studentID who came first in Ra10: ")
                 #calls the sub program to validate the studentID for the ranking
                check=validStudent(partId,rank1)
            #removes the studentID entred already to avoid duplicate entry
            partId.remove(rank1)
            check=False
            while check==False:
                    rank2=input("Enter the studentID who came second in Ra10: ")
                    check=validStudent(partId,rank2)
            partId.remove(rank2)
            check=False
            while check==False:
                    rank3=input("Enter the studentID who came third in Ra10: ")
                    check=validStudent(partId,rank3)
            addGameRank("Ra10",rank1,rank2,rank3)
            gamesLeft.remove("Ra10")
        elif gamesLeft[choice-1] =="Ra11":
            #Initialise the list for keeping the participating students for each 200M race
            partId=[]
            #Go through each row in the gameslist 
            for row in range(0,len(gameslist)):
                #Identify the raceID in the gameslist
                if gameslist[row][0]=="Ra10":
                    #Add the participants ID from the gameslist to partId list
                    for index in range(1,10):
                        partId.append(gameslist[row][index])
            
            #Displays the studentID for the participants of Ra11 200M race
            print("Below is the participant list for the Ra11 200M race")
            print("*"*12)
            print(partId[0],partId[1],partId[2])
            print(partId[3],partId[4],partId[5])
            print(partId[6],partId[7],partId[8])
            print("*"*12)
            
            check=False
            while check==False:
                rank1=input("Enter the studentID who came first in Ra11: ")
                 #calls the sub program to validate the studentID for the ranking
                check=validStudent(partId,rank1)
            #removes the studentID entred already to avoid duplicate entry
            partId.remove(rank1)
            check=False
            while check==False:
                    rank2=input("Enter the studentID who came second in Ra11: ")
                    check=validStudent(partId,rank2)
            partId.remove(rank2)
            check=False
            while check==False:
                    rank3=input("Enter the studentID who came third in Ra11: ")
                    check=validStudent(partId,rank3)
            addGameRank("Ra11",rank1,rank2,rank3)
            gamesLeft.remove("Ra11")
    else:
        #displays no ranking entry is required for the game.
        print("You have entered the rankings for all the game events")
        print("*"*50)
        print("*"*50)
        
#display the game ID and the rank holders.
def displayRankingList():
    print("*"*50)
    print("*"*50)
    print('{:^33}'.format("Game Ranking List"))
    print('{:<6}'.format("Game")+'{:<7}'.format("Rank1")+'{:<7}'.format("Rank2")+'{:<7}'.format("Rank3"))
    for team in range(0,len(gameRank)):
        print('{:^6}'.format(gameRank[team][0])+'{:^6}'.format(gameRank[team][1])+'{:^10}'.format(gameRank[team][2])+'{:^7}'.format(gameRank[team][3]))

#Create a 2D array of students and their points
def assignPoints():
    for row in range(0,len(gameRank)):
        #assign points for students based on ranking
        #initialise the record list
        record=[]
        #Add the student who came first in the game
        record.append(gameRank[row][1])
        #Add the gameID
        record.append(gameRank[row][0])
        #assign 60 points for rank1 student
        record.append(60)
        '''add the record of one student points detail
        for one game to StudentsPoints list'''
        StudentsPoints.append(record)
        #initialise the record list
        record=[]
        #Add the student who came second in the game
        record.append(gameRank[row][2])
        #Add the gameID
        record.append(gameRank[row][0])
        #assign 30 points for rank2 student
        record.append(30)
        '''add the record of one student points detail
        for one game to StudentsPoints list'''
        StudentsPoints.append(record)
        #initialise the record list
        record=[]
        #Add the student who came third in the game
        record.append(gameRank[row][3])
        #Add the gameID
        record.append(gameRank[row][0])
        #assign 5 points for rank3 student
        record.append(5)
        '''add the record of one student points detail
        for one game to StudentsPoints list'''
        StudentsPoints.append(record)

#displays the points scored by students in each game
def displayPointsList():
    print("*"*50)
    print("*"*50)
    print('{:^40}'.format("Student Points for Games"))
    print('{:<20}'.format("StudentID")+'{:<13}'.format("GameID")+'{:<7}'.format("Points"))
    for team in range(0,len(StudentsPoints)):
        print('{:^20}'.format(StudentsPoints[team][0])+'{:^13}'.format(StudentsPoints[team][1])+'{:^7}'.format(StudentsPoints[team][2]))
    
#Calculate the total for each participant by updating the TotalPoints list
def calculateTotal():
    #access each row in StudentsPoints list created in option B
    for row in range(0, len(StudentsPoints)):
        #Selection statement is used to identify all the 40 students and increment their total
        if StudentsPoints[row][0]=="S1":
            TotalPoints[0]=TotalPoints[0] + int(StudentsPoints[row][2])
        elif StudentsPoints[row][0]=="S2":
            TotalPoints[1]=TotalPoints[1] + int(StudentsPoints[row][2])
        elif StudentsPoints[row][0]=="S3":
            TotalPoints[2]=TotalPoints[2] + int(StudentsPoints[row][2])
        elif StudentsPoints[row][0]=="S4":
            TotalPoints[3]=TotalPoints[3] + int(StudentsPoints[row][2])
        elif StudentsPoints[row][0]=="S5":
            TotalPoints[4]=TotalPoints[4] + int(StudentsPoints[row][2])
        elif StudentsPoints[row][0]=="S6":
            TotalPoints[5]=TotalPoints[5] + int(StudentsPoints[row][2])
        elif StudentsPoints[row][0]=="S7":
            TotalPoints[6]=TotalPoints[6] + int(StudentsPoints[row][2])
        elif StudentsPoints[row][0]=="S8":
            TotalPoints[7]=TotalPoints[7] + int(StudentsPoints[row][2])
        elif StudentsPoints[row][0]=="S9":
            TotalPoints[8]=TotalPoints[8] + int(StudentsPoints[row][2])
        elif StudentsPoints[row][0]=="S10":
            TotalPoints[9]=TotalPoints[9] + int(StudentsPoints[row][2])
        elif StudentsPoints[row][0]=="S11":
            TotalPoints[10]=TotalPoints[10] + int(StudentsPoints[row][2])
        elif StudentsPoints[row][0]=="S12":
            TotalPoints[11]=TotalPoints[11] + int(StudentsPoints[row][2])
        elif StudentsPoints[row][0]=="S13":
            TotalPoints[12]=TotalPoints[12] + int(StudentsPoints[row][2])

#displays total points each student scored in a table.
def displayTotalPoints():
    print("*"*50)
    print("*"*50)
    print('{:<40}'.format("Total Points Earned by Students"))
    print('{:<20}'.format("StudentID")+'{:<15}'.format("Total Points"))
    for index in range(0,len(TotalPoints)):
        if TotalPoints[index] != 0:
            name="S"+str(index+1)
            print('{:^20}'.format(name)+'{:^15}'.format(TotalPoints[index]))

#Workout the top 3 places
def ranking():
    #To keep the total points for each ranking
    global first,second,third
    #Create a copy of the totalPoints list
    tempPoints=TotalPoints.copy()
    #Remove duplicate points from the list
    #This helps to find the first three ranking points
    tempPoints=list(dict.fromkeys(tempPoints))
    #Using max function work out the first place total points.
    first=max(tempPoints)
    #Remove the first place total point from the list
    tempPoints.remove(first)
    '''work out the second place total point using the list without
    first place total point.'''
    second=max(tempPoints)
    #Remove the second place total point from the list
    tempPoints.remove(second)
    '''work out the second place total points using the list without
    first and second place total points.'''
    third=max(tempPoints)
    #Initialise the list to keep all the first ranking position
    #In the total point list.
    rankPosition=[]
    #Used to generate the index for rankPosition list
    cou=0
    #Access each row at a time in the TotalPoints list
    for index in range(0,len(TotalPoints)):
    #Select the points in TotalPoints list Whichmatch the first place
        if TotalPoints[index]==first:
    #Add the index of totalPoints list with 1st place value to rankPosition
            rankPosition.append(index+1)
    #Workout the StudentID for first place
            firstStudent="S"+str(rankPosition[cou])
            cou +=1
    #calls the subprogram to add the details for rank 1 students to scoreboard
            addtoscoreboard(firstStudent,first)
    #Initialise the list to keep all the second ranking position
    #in the Total point. list.
    rankPosition=[]
    #Used to generate the index for rankPosition list.
    cou=0
    #do the game process like first place for second and third places.
    for index in range(0,len(TotalPoints)):
        if TotalPoints[index]==second:
            rankPosition.append(index+1)
            secondStudent="S"+str(rankPosition[cou])
            cou +=1
            addtoscoreboard(secondStudent,second)
    rankPosition=[]
    cou=0
    for index in range(0,len(TotalPoints)):
        if TotalPoints[index]==third:
            rankPosition.append(index+1)
            thirdStudent="S"+str(rankPosition[cou])
            cou +=1
            addtoscoreboard(thirdStudent,third)

#Create the 2D array of score board with data required
def addtoscoreboard(student, total):
    #initialise the record list add one student details for scoreboard
    record=[]
    #Add the studentID to record
    record.append(student)
    #Access each row in the StudentsPoints list
    #find all the games the students took part in.
    for row in range(0,len(StudentsPoints)):
    #Select the student detail given from the StudentsPoints list
        if StudentsPoints[row][0]==student:
    #Add the gameID and points for the given studentID to record list.
            record.append(StudentsPoints[row][1])
            record.append(StudentsPoints[row][2])
    #Add the total points for the studentID
    record.append(total)
    #Add one student detail to the scoreboard.
    scoreboard.append(record)

#Display the score board
def displayScoreboard():
    #displays the border
    print("*"*79)
    print("*"*79)
    #displays the title
    print('{:^79}'.format('Scoreboard for Games'))
    print("_"*79)
    #displays the headings for the columns in the scoreboard
    print('{:<4}'.format('SID'),'{:<6}'.format('GID1'),'{:<4}'.format('P1'),'{:<6}'.format('GID2'),'{:<4}'.format('P2'),'{:<6}'.format('GID3'),'{:<4}'.format('P2'),'{:<6}'.format('GID3'),'{:<4}'.format('P3'),'{:<6}'.format('GID4'),'{:<4}'.format('P4'),'{:<8}'.format('Total'),'{:<7}'.format('Rank'))
    print("_"*79)
    #Access each row in scoreboard list
    for row in scoreboard:
        #initialise the gameID and points for the 5 different games
        gid1=""
        p1=""
        gid2=""
        p2=""
        gid3=""
        p3=""
        gid4=""
        p4=""
        gid5=""
        p5=""
        #store the studentID to be printed
        name=row[0]
        #store the total points for the student to be printed
        total=row[len(row)-1]
        #store the total number of games the student took part in
        gtotal=len(row)-2
        '''use the selection statement to identify the number of games the student took part in
        store the gameID and points for each game.'''
        if gtotal==2 :
            gid1=row[1]
            p1=row[2]
        elif gtotal==4 :
            gid1=row[1]
            p1=row[2]
            gid2=row[3]
            p2=row[4]
        elif gtotal==6:
            gid1=row[1]
            p1=row[2]
            gid2=row[3]
            p2=row[4]
            gid3=row[5]
            p3=row[6]
        elif gtotal==8:
            gid1=row[1]
            p1=row[2]
            gid2=row[3]
            p2=row[4]
            gid3=row[5]
            p3=row[6]
            gid4=row[7]
            p4=row[8]
        elif gtotal==10:
            gid1=row[1]
            p1=row[2]
            gid2=row[3]
            p2=row[4]
            gid3=row[5]
            p3=row[6]
            gid4=row[7]
            p4=row[8]
            gid5=row[9]
        #Store the rank for each student to be printed
        if total==first:
            rank=1
        elif total==second:
            rank=2
        else:
            rank=3
        #display the scoreboard details for one studentID at a time.
        print('{:<6}'.format(name)+'{:<6}'.format(gid1)+'{:^5}'.format(p1)+'{:<6}'.format(gid2)+'{:^5}'.format(p2)+'{:<6}'.format(gid3)+'{:^5}'.format(p3)+'{:<6}'.format(gid4)+'{:^5}'.format(p4)+'{:^13}'.format(total)+'{:^4}'.format(rank))
        #display border
        print("_"*79)
    print("_"*79)
    #starts new line
    print("\n")
              
#Main program starts 
#2DArray for Game Participants Entry
gameslist=[]
''' Calls the subprogram readFile
with "games20.txt" as argument
to transfer the file content to
gameslist array'''
readFile("games22.txt")
#display the gameslist 2D array.
print(gameslist)
#games list is initialised to have all the game eventIDs
games=[]
#This extracts the gameID for each event from the games list.
groupGames()
print(games)
#You make a copy of the games list so that
#you can moniter what games ranking are not entered yet.
gamesLeft=games.copy()
#This list will contain the ranking for the games
gameRank=[]
checkoption = "A" #calls the respective procedure depending on user input
while checkoption != "Q":
    option_choice = display_Option()
    if option_choice.upper() == "A":
        print("\n\nRecord the ranking for each event\n")
        #Calls the subprogram to enter ranking
        enterRankingGames()
        #Calls the subprogram to display the ranking list.
        displayRankingList()
    elif option_choice.upper() == "B":
        print("\n\nAssign Points to Students\n")
        #Keeps a list of students and the points scored in each game
        #initialise the list at the beggining
        StudentsPoints=[]
        #Calls the sub program to add points for students based on ranking achieved
        assignPoints()
        #Calls the subprogram to display the list of students and points achieved in each game.
        displayPointsList()
    elif option_choice.upper() == "C":
        print("\n\nCalculate Points\n")
        #Initialise the totalPoints list for each student. 13 students took part in the games.
        TotalPoints=[0,0,0,0,0,0,0,0,0,0,0,0,0]
        #Calls the subprogram to calculate the total points scored by each student.
        calculateTotal()
        #Calls the subprogram to display the studentID and total points
        displayTotalPoints()
    elif option_choice.upper() == "D":
        print("\n\nGame Board\n")
        #Global variables to keep the top 3 ranking scores
        first=0
        second=0
        third=0
        #Initialise the scoreboard list
        scoreboard=[]
        #Calls the sub program ranking to workout the top three total points
        ranking()
        #Calls the sub program to display the scoreboard.
        displayScoreboard()
    elif option_choice.upper() == "Q":
        print("Thanks for using the system.")
        print("Good Bye")
        checkoption = "Q"       
    else:
        print("\n\nInvalid entry. Please enter a valid option. Menu will be displayed again\n\n")
        

