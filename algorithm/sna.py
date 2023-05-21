from classtype.People import People
from classtype.Graph import Graph

def socialNetworkAnalysis(graph : Graph, srcPerson : People, destPerson : People):
    # Set adjacency matrix
    checked = [0 for _ in range(len(graph.getPersons()))]

    # Set checked true to the src person
    searchedIndex = graph.getPersonIndexByName(srcPerson.getName())
    checked[searchedIndex] = True

    # Initialize depth level
    depth = 1

    # Initialize name list to be traversed
    nameList = []

    # Add srcPerson friend to the list
    for friendName in srcPerson.getFriends():
        nameList.append(friendName)
        index = graph.getPersonIndexByName(friendName)
        checked[index] = True

    # Set boolean condition
    check = True

    # Traversing through the graph to see relation between srcPerson and destPerson
    while check:

        newNameList = []

        for personName in nameList:

            if (personName == destPerson.getName()):
                    return depth
            
            person = graph.getPersonByName(personName)

            # Get person friends
            for friendName in person.getFriends():
                # Get person friend index
                friendIndex = graph.getPersonIndexByName(friendName)
                if (not checked[friendIndex]):
                    checked[friendIndex] = True
                    newNameList.append(friendName)
    
        nameList = newNameList
        
        depth += 1
        
        check = (len(nameList) != 0)

    return 0

def getNLevelFriend(graph: Graph, person: People, level):
     # Set adjacency matrix
    checked = [0 for _ in range(len(graph.getPersons()))]

    # Set checked true to the src person
    searchedIndex = graph.getPersonIndexByName(person.getName())
    checked[searchedIndex] = True

    # Initialize depth level
    depth = 1

    # Initialize name list to be traversed
    nameList = []

    # Add person's friend
    for friendName in person.getFriends():
        nameList.append(friendName)
        index = graph.getPersonIndexByName(friendName)
        checked[index] = True

    # Set boolean condition
    check = True

    while check:
        if (depth == level):
            return nameList
        
        newNameList = []

        for personName in nameList:
            person = graph.getPersonByName(personName)

            # Get person friends
            for friendName in person.getFriends():
                # Get person friend index
                friendIndex = graph.getPersonIndexByName(friendName)
                if (not checked[friendIndex]):
                    checked[friendIndex] = True
                    newNameList.append(friendName)
        
        nameList = newNameList
        
        depth += 1
        
        check = (len(nameList) != 0)

    return []
        
        