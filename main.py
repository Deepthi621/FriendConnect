import mysql.connector
from classtype.People import People
from classtype.Graph import Graph
from algorithm.recommender import recommendFriends
from algorithm.sna import socialNetworkAnalysis, getNLevelFriend

try:
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        port = 3307,
        password = 'password',
        database = 'makalah_stima'
    )

    cursor = conn.cursor()

    # Get all person in the database

    cursor.execute("SELECT * FROM Person")

    records = cursor.fetchall()

    # List all person in the database
    listOfPerson = []

    for row in records:
        person = People(row[0])
        listOfPerson.append(person)
    
    # Get all person friend in database
    for person in listOfPerson:
        cursor.execute("SELECT friend_name FROM friends WHERE name = %s", (person.getName(),))

        # Fetch the data
        records = cursor.fetchall()

        # Assign the data to a list
        listOfFriends = []

        for row in records:
            listOfFriends.append(row[0])
        
        # Assign the list to the person
        person.setFriends(listOfFriends)
    
    
    # Set the graph
    graph = Graph(listOfPerson)

    print("Welcome to Social Network Analysis and Friend Recommendation Program!!!")
    print("Please choose what do you want to do with this program :")
    print("1. Social Network Analysis Program")
    print("2. Friend Recommendation Program")
    
    choice = int(input("Input : "))
    
    # Friend Recommendation Program
    if (choice == 2):
        # Print all names to select for the recommender system
        print("List of person in the database: ")
        graph.printNames()

        inputIndex = int(input("Select a person to be searched by number from the above list to search : "))

        person = graph.getPersonByIndex(inputIndex-1)

        # Get recommended Friends
        recommendedFriends = recommendFriends(graph, person)

        # Print all the recommended friend names
        print("The recommended friend for you are : ")
        for i in range(len(recommendedFriends)):
            print(f"{i+1}. {recommendedFriends[i]}")
    
    else:

        print("Select what do you want to analysis : ")
        print("1. Relation between person A or person B")
        print("2. Get all the person that is n-level friend of person A")

        choice = int(input("Input: "))

        # Print all names to select for the recommender system
        print("List of person in the database: ")
        graph.printNames()

        # Social network analysis to analyze relation between 2 person
        if (choice == 1):
            firstPersonIndex = int(input("Select the first person by the number from the above list : "))
            secondPersonIndex = int(input("Select the first person by the number from the above list : "))

            firstPerson = graph.getPersonByIndex(firstPersonIndex-1)
            secondPerson = graph.getPersonByIndex(secondPersonIndex-1)

            depth = socialNetworkAnalysis(graph, firstPerson, secondPerson)

            if depth == 1:
                print(f"{secondPerson.getName()} is the first level friend of {firstPerson.getName()}")
            elif depth == 2:
                print(f"{secondPerson.getName()} is the second level friend of {firstPerson.getName()}")
            elif depth == 3:
                print(f"{secondPerson.getName()} is the third level friend of {firstPerson.getName()}")
            elif depth == 4:
                print(f"{secondPerson.getName()} is the fourth level friend of {firstPerson.getName()}")

        # Social network analysis to get n-level friend of a person
        else:
            personIndex = int(input("Select the person you want to analysis by the number from above list : "))
            level = int(input("Select level : "))

            person = graph.getPersonByIndex(personIndex-1)

            nLevelFriend = getNLevelFriend(graph, person, level)

            print(f"All of your {level}-level friend are : ")
            
            for i in range(len(nLevelFriend)):
                print(f"{i+1}. {nLevelFriend[i]}")

except mysql.connector.Error as e:
    print("Error reading data from MYSQL table")
finally:
    if conn.is_connected():
        conn.close()
        cursor.close()

