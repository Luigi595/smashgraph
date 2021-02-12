# SmashGraph
### A Graph Theory approach to ranking Melee players

## Prerequisites
Pretty standard data science libraries
* Python 3.6+
* Numpy
* Pandas

## Data
The data for this project comes from [smashdata.gg](https://smashdata.gg/) 

## Preprocessing
DQs are removed from the data.  
If a character makes up less than 5% of any player's games, sets played entirely as that character will be removed.
## Graph structure
The graph is directed and weighted. Each player is a vertex, sets played between players are arcs, with the direction following the winner of the set.

The weight on each arc is determined by the following formula

## Methodology

## Results

## Problems (Opportunities if you're feeling positive)

Some of the tags in the database are duplicated, while a part of those belong to different people e.g. King, some of them don't e.g. Aniolas. I haven't found a way to scan and solve this problem for 4743 instances of duplicated tags. Considering that most top players have unique tags, I decided to merge records of identical tags.

`numpy.linalg.eigs(A)` may produce an error related to the LAPACK wrapper. Apparently this is a problem with numpy 1.19.4 on Windows.

Not all tournaments are created equal, the original model was used to rank college football so that assumption was fair. On the other hand, it's not the same to defeat Axe at a weekly than to do it at Genesis. As a result of this, without any modifications to the model, we find that Falgoat, an unranked falco main ranks #36 in this model's 2019 Ranking, having defeated Zain at Blast Off! #31, a tournament with 30 entrants.

Incomplete data even in recent years. Stango was ranked 47th on the 2019 MPGR, while ranking 148th here. Upon inspection, we noticed that the database misses his run at Fight Pitt 9, which was described as the "run of his career". Or AbsentPage, whose only 2019 record in the database is his Genesis 6 run.

When all eigenvalues are zero, alpha is not limited. This happens when the graph has no loops of the form Mang0 beats Zain who beats Leffen who beats Mang0 or longer. Such seems to be the case of the 2020 season.