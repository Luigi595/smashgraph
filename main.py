import sqlite3
import igraph as ig
import cairo
import pandas as pd
import numpy as np

#I don't understand Cairo, but run this with python 3.6

conn = sqlite3.connect('melee_player_database.db')

c = conn.cursor()

c.execute("SELECT * FROM sqlite_master")
tables=c.fetchall()

for i in tables:
    print(i)
    print("\n")

#Get 20 sets
#Vertex are players
#Direction goes to winner


#Add new column? Nevermind the first line, can't drop column on sqlite
#c.execute("ALTER TABLE sets DROP COLUMN loser_id")
#c.execute("ALTER TABLE sets ADD loser_id text")
c.execute("UPDATE sets SET loser_id= CASE WHEN winner_id=p1_id THEN p2_id ELSE p1_id END")
c.execute("ALTER TABLE sets ADD score_diff integer")
c.execute("UPDATE sets SET score_diff= ABS(p1_score-p2_score)")

"""
c.execute("SELECT player_id FROM players WHERE tag='Chillindude'")
print(c.fetchone())

c.execute("SELECT * FROM sets WHERE winner_id='1493' AND loser_id='1000'")
players=c.fetchall()
print(players)
"""
c.execute("SELECT tag FROM players")
players=np.unique(c.fetchall())
print("There are %i unique players" %len(players))

#How many times has player x beaten player y and game diff without dqs
c.execute("""SELECT p1.tag,p2.tag,COUNT(s.winner_id),SUM(s.score_diff)
    FROM sets s
    JOIN players p1 ON p1.player_id=s.winner_id 
    JOIN players p2 ON p2.player_id=s.loser_id
    WHERE p1_score <> -1 AND p2_score <> -1
    GROUP BY s.winner_id, s.loser_id""") 
head2Head=c.fetchall()
print("There are %i h2h records" %len(head2Head))


#Adjacency Matrix
def adjancency():
    adjMatrix= pd.DataFrame(np.zeros((len(players), len(players))), index=players, columns=players)
    for record in head2Head:
        adjMatrix.at[record[0],record[1]]=record[2]
    #Saving the matrix to disk is a ~2 GB endeavor
    #adjMatrix.to_csv("out.csv")
    return adjMatrix

A=adjancency()


c.close()
conn.close()

#g=ig.Graph.Tree(12,2)
#ig.plot(g)
