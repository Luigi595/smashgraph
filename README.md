# SmashGraph
### A Graph Theory approach to ranking Melee players

## Prerequisites
* Python 3.6
* Igraph
* Cairo or cairocffi (If you want to render the graph)

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

Some of the tags in the database are duplicated, while a part of those belong to different people e.g. King, some of them don't e.g. Aniolas. I haven't found a way to scan and solve this problem for 4743 instances of duplicated tags.