class Graph:
    
    # Constructor
    def __init__(self, persons):
        '''
        persons : all the person in the social network
        '''
        self.persons = persons
    
    def getPersons(self):
        return self.persons
    
    # Print names of all persons
    def printNames(self):
        for i in range(len(self.persons)):
            print(f"{i+1}. {self.persons[i].getName()}")
    
    # Get person in the list by its name
    def getPersonByName(self, name):
        for person in self.persons:
            if person.getName() == name:
                return person
    
    # Get person index by name
    def getPersonIndexByName(self, name):
        for i in range(len(self.persons)):
            if (self.persons[i].getName() == name):
                return i

    # Get person by index
    def getPersonByIndex(self, index):
        return self.persons[index]

