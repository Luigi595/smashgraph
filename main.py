import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect('melee_player_database.db')
c = conn.cursor()

c.execute("SELECT * FROM sqlite_master")
for i in c:
    print(i)
    print("\n")


#Helper columns
#c.execute("ALTER TABLE sets ADD loser_id text")
c.execute("UPDATE sets SET loser_id= CASE WHEN winner_id=p1_id THEN p2_id ELSE p1_id END")
c.execute("ALTER TABLE sets ADD score_diff integer")
c.execute("UPDATE sets SET score_diff= ABS(p1_score-p2_score)")

#TODO refactor more efficiently
c.execute("""SELECT p1.tag,p2.tag
    FROM sets s
    JOIN players p1 ON p1.player_id=s.winner_id 
    JOIN players p2 ON p2.player_id=s.loser_id
    JOIN tournament_info t ON s.tournament_key=t.key
    WHERE t.season=20""")
temp=[x for y in c for x in y]
players=np.unique(temp)
print("There are %i unique players" %len(players))


#How many times has player x beaten player y and game diff without dqs in season
c.execute("""SELECT p1.tag,p2.tag,COUNT(s.winner_id),SUM(s.score_diff)
    FROM sets s
    JOIN players p1 ON p1.player_id=s.winner_id 
    JOIN players p2 ON p2.player_id=s.loser_id
    JOIN tournament_info t ON s.tournament_key=t.key
    WHERE p1_score <> -1 AND p2_score <> -1 AND t.season=20
    GROUP BY s.winner_id, s.loser_id""") 
head2Head=c.fetchall()
print("There are %i h2h records" %len(head2Head))

#Adjacency Matrix
def adjancency():
    adjMatrix= pd.DataFrame(np.zeros((len(players), len(players))), index=players, columns=players)
    for record in head2Head:
        adjMatrix.at[record[0],record[1]]+=record[2]
    return adjMatrix

A=adjancency()
kIn=A.sum(axis=1)
kOut=A.sum(axis=0)


#alpha must be less than the inverse of the max eigenvalue
#For Season 19, the max eigenvalue is 16.075
#For season 20, it was 0, is it acyclic?
print("Waiting on eigenvalues")
#alpha=.8/max(np.linalg.eigvals(A))
#print(alpha)
alpha=.8/16.075

print("No more eigenvalues")

w= np.dot(np.linalg.inv(np.identity(len(players))-alpha*A),kIn)
l= np.dot(np.linalg.inv(np.identity(len(players))-alpha*np.transpose(A)),kOut)

s=w-l
scores=pd.DataFrame(s, index=players,columns=["Score"])

scores.sort_values(by="Score", ascending=False).to_csv("2020ranking.csv")

c.close()
conn.close()
