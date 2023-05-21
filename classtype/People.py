class People:

    # Constructor
    def __init__(self, name):
        '''
        name : name of the person
        friends : all friends of the person
        '''
        self.name = name
        self.friends = []
    
    # Getter
    def getName(self):
        return self.name
    
    def getFriends(self):
        return self.friends
    
    # Setter
    def setName(self, name):
        self.name = name
    
    def setFriends(self, friends):
        self.friends = friends
    
    def addFriend(self, friend):
        self.friends.append(friend)