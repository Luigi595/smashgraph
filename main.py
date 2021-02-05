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

c. execute("SELECT * FROM players")
#print(c.fetchmany(size=2))

c. execute("SELECT * FROM players WHERE player_id='1004'")
#print(c.fetchall())

#Get 20 sets
#Vertex are players
#Direction goes to winner
c. execute("SELECT * FROM sets")
last20=c.fetchmany(size=20)


c.execute("SELECT tag FROM players")
players=c.fetchall()
print(len(players))

#c.execute("SELECT game_data FROM sets")
#print(c.fetchall()[-2:])

def adjancency():
    count=0
    adjMatrix= pd.DataFrame(np.zeros((len(players), len(players))), index=players, columns=players)
    for player in players:
        count+=1
        if count%100==0: print(count)
        c.execute("SELECT p1_score-p2_score, p1_id, p2_id FROM sets WHERE winner_id=?", (player))
        temp=c.fetchall()
        for game in temp:
            if game[1]==player:
                adjMatrix.loc[player,game[2]]+= game[0]
            elif game[2]== player:
                adjMatrix.loc[player,game[1]]+= game[0]
    adjMatrix.to_csv("out.csv")

#Add new column? Nevermind the first line, can't drop column on sqlite
#c.execute("ALTER TABLE sets DROP COLUMN loser_id")
#c.execute("ALTER TABLE sets ADD loser_id text")
c.execute("UPDATE sets SET loser_id= CASE WHEN winner_id=p1_id THEN p2_id ELSE p1_id END")
#c.execute("ALTER TABLE sets ADD score_diff integer")
c.execute("UPDATE sets SET score_diff= ABS(p1_score-p2_score)")

"""
c.execute("SELECT * FROM sqlite_master")
tables=c.fetchall()

for i in tables:
    print(i)
    print("\n")

"""
#c.execute("SELECT player_id, player. FROM sets")
#tt=c.fetchmany(size=50)
#print(tt)



c.execute("""SELECT p1.tag,p2.tag,COUNT(s.winner_id),SUM(s.score_diff)
    FROM sets s
    JOIN players p1 ON p1.player_id=s.winner_id 
    JOIN players p2 ON p2.player_id=s.loser_id
    WHERE s.winner_id='1004'
    GROUP BY s.winner_id, s.loser_id""") 
players=c.fetchmany(size=20) 
print(players)

#adjancency()

c.close()
conn.close()

#g=ig.Graph.Tree(12,2)
#ig.plot(g)
