import sqlite3
import igraph as ig
import cairo

#I don't understand Cairo, but run this with python 3.6

conn = sqlite3.connect('melee_player_database.db')

c = conn.cursor()

c.execute("SELECT * FROM sqlite_master")
tables=c.fetchall()

for i in tables:
    print(i)
    print("\n")

c. execute("SELECT * FROM players")
#print(c.fetchmany(size=2))

c. execute("SELECT * FROM players WHERE player_id='1004'")
#print(c.fetchall())

#Get 20 sets
#Vertex are players
#Direction goes to winner
c. execute("SELECT * FROM sets")
last20=c.fetchmany(size=20)

players=[]
for match in last20:
    players.append(match[4])
    players.append(match[5])

print(players)
c.close()
conn.close()

#g=ig.Graph.Tree(12,2)
#ig.plot(g)
