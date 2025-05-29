import mysql.connector
import networkx as nx
import matplotlib.pyplot as plt
from classtype.People import People
from classtype.Graph import Graph
from algorithm.recommender import recommendFriends
from algorithm.sna import socialNetworkAnalysis, getNLevelFriend

def count_mutual_friends(graph, person1, person2):
    """Count mutual friends between two people"""
    friends1 = set(person1.getFriends())
    friends2 = set(person2.getFriends())
    return friends1 & friends2

def draw_social_graph(graph, target_user=None):
    """Visualize the social network with highlighted recommendations"""
    G = nx.Graph()
    
    # Add all nodes and edges using Graph class methods
    for person in graph.getPersons():
        G.add_node(person.getName())
        for friend in person.getFriends():
            G.add_edge(person.getName(), friend)
    
    # Set node colors
    node_colors = []
    recommended = []
    if target_user:
        recommended = [friend[0] for friend in recommendFriends(graph, target_user)]
    
    for node in G.nodes():
        if target_user and node == target_user.getName():
            node_colors.append('red')  # Target user
        elif node in recommended:
            node_colors.append('orange')  # Recommended
        else:
            node_colors.append('skyblue')  # Others
    
    # Draw graph
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=800)
    plt.title(f"Social Network - {target_user.getName()}" if target_user else "Full Network")
    plt.show()

# Database connection and main program
conn = None
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        port=3306,
        password='Flydeepthi@1',
        database='makalah_stima'
    )
    
    if conn.is_connected():
        print("✅ Connected to MySQL Database!")
        cursor = conn.cursor()

        # Load all people
        cursor.execute("SELECT * FROM Person")
        listOfPerson = [People(row[0]) for row in cursor.fetchall()]

        # Load friendships
        for person in listOfPerson:
            cursor.execute("SELECT friend_name FROM friends WHERE name = %s", (person.getName(),))
            person.setFriends([row[0] for row in cursor.fetchall()])

        graph = Graph(listOfPerson)

        # Main menu
        print("\nWelcome to Social Network Analysis and Friend Recommendation Program!!!")
        choice = int(input("1. Social Network Analysis\n2. Friend Recommendation\nInput: "))

        if choice == 2:
            # Print all names with numbers
            print("List of people in the database:")
            for i, person in enumerate(graph.getPersons(), 1):
                print(f"{i}. {person.getName()}")
            
            # Get user selection
            inputIndex = int(input("Select person by number: "))
            person = graph.getPersons()[inputIndex - 1]
            
            # Get recommendations with mutual friend info
            recommendations = []
            for potential_friend in graph.getPersons():
                if (potential_friend.getName() != person.getName() and 
                    potential_friend.getName() not in person.getFriends()):
                    
                    mutuals = count_mutual_friends(graph, person, potential_friend)
                    if mutuals:
                        recommendations.append({
                            'name': potential_friend.getName(),
                            'mutual_count': len(mutuals),
                            'mutual_names': sorted(list(mutuals))
                        })
            
            # Sort by mutual friend count (descending)
            recommendations.sort(key=lambda x: -x['mutual_count'])
            
            # Display results with justification
            print("\nRecommended friends (sorted by mutual connections):")
            for i, rec in enumerate(recommendations, 1):
                mutual_names = ", ".join(rec['mutual_names'])
                print(f"{i}. {rec['name']} (Mutual friends: {rec['mutual_count']} - {mutual_names})")
            
            # Show visualization
            draw_social_graph(graph, person)

        else:
            analysis_choice = int(input("1. Relation between 2 people\n2. N-level friends\nInput: "))
            
            # Print all names with numbers
            print("List of people in the database:")
            for i, person in enumerate(graph.getPersons(), 1):
                print(f"{i}. {person.getName()}")
            
            if analysis_choice == 1:
                p1_index = int(input("First person number: ")) - 1
                p2_index = int(input("Second person number: ")) - 1
                p1 = graph.getPersons()[p1_index]
                p2 = graph.getPersons()[p2_index]
                
                depth = socialNetworkAnalysis(graph, p1, p2)
                level_names = ["not connected", "1st", "2nd", "3rd", "4th"]
                print(f"\n{p2.getName()} is {level_names[depth]} level friend of {p1.getName()}")
                
                # Show mutual friends if connected
                if 1 <= depth <= 4:
                    mutuals = count_mutual_friends(graph, p1, p2)
                    if mutuals:
                        print(f"Mutual friends: {', '.join(mutuals)}")
                    else:
                        print("No mutual friends")
            else:
                person_index = int(input("Person number: ")) - 1
                person = graph.getPersons()[person_index]
                level = int(input("Friend level (1-4): "))
                
                friends = getNLevelFriend(graph, person, level)
                print(f"\n{level}-level friends:")
                for i, friend in enumerate(friends, 1):
                    print(f"{i}. {friend}")

except mysql.connector.Error as e:
    print("❌ Database error:", e)
except Exception as e:
    print("❌ An error occurred:", e)
finally:
    if conn and conn.is_connected():
        conn.close()
        print("🔌 Connection closed")