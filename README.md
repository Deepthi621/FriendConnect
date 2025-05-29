FriendConnect: A BFS-Based Social Network Analyzer
Leveraging Discrete Mathematics to Map and Recommend Connections

Project Description
This Python project analyzes social networks using Breadth-First Search (BFS) to:

🔍 Discover multi-level connections (up to 4 degrees deep)

🤝 Recommend friends based on mutual connections

📊 Visualize networks with color-coded nodes (Matplotlib)

📝 Justify suggestions transparently (e.g., "3 mutual friends with Juliet")

Key Features:
✔ Shakespearean social network dataset pre-loaded
✔ MySQL integration for scalable data storage
✔ Interactive graph visualization
✔ Educational demonstration of graph theory

Guidelines to Run the Project
Prerequisites
Python 3.8+

MySQL Server 8.0+

Libraries: mysql-connector-python, networkx, matplotlib

Setup
Clone the repository:

bash
git clone https://github.com/yourusername/FriendConnect.git
cd FriendGraph
Install dependencies:

bash
pip install -r requirements.txt
Database Setup:

Import the sample dataset:

bash
mysql -u root -p makalah_stima < data.sql
Configure MySQL credentials in config.py:

python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'yourpassword',
    'database': 'makalah_stima'
}
Execution
Run the main program:

bash
python main.py
Follow the menu prompts to:

Analyze connections between users

Get friend recommendations

Visualize the social graph