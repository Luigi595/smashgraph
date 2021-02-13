# SmashGraph
### A single parameter, graph theory approach to ranking Melee players

## Introduction

When ranking competitors, a very common, sensible argument one might hear is this "A is better than C, sure they didn't play, but A beat B who in turn beat C". Clearly, this argument can be extended for chains of longer length. But it doesn't sound fair to value these "indirect wins" the same as straight-up wins, so, every step away from a direct win discounts the indirect win.

Now, what happens when we add up all the players' wins and discounted indirect wins? Is that viable ranking system?

## Prerequisites
Pretty standard data science libraries
* Python 3.6+
* Numpy
* Pandas

## Data
The data for this project comes from [smashdata.gg](https://smashdata.gg/) 



## Graph structure
The graph is directed and weighted. Each player is a vertex, sets played between players are arcs, with the direction following the winner of the set.

The weight on each arc (x,y) is the number of sets x has won against y.

## Methodology

It is a straight implementation of the method descibed in Park, Juyong & Newman, M.. (2005). A network-based ranking system for American college football. [arXiv:physics/0505169 ](arXiv:physics/0505169)

## Results

### Set based

| Rank        | 2018           | 2019  |2020 (see shortcomings)|
| ------------- |-------------| -----|-----|
| 1 | Hungrybox | Hungrybox | Ginger |
| 2 |  Plup  |  Mang0 | iBDW
| 3 |  Leffen|  Zain |Zain
| 4 |   Armada|  Axe | n0ne
| 5 |   Zain|  Leffen | Hungrybox
| 6 | Mang0  |  Wizzrobe | Mang0
| 7 |   Mew2King|  aMSa | SFAT
| 8 |   Wizzrobe| S2J | Plup
| 9 |  aMSa | iBDW | lloD
| 10 |  SFAT |   Plup  | Gahtzu

### Game based

| Rank        | 2018           | 2019  |2020 |
| ------------- |-------------| -----|-----|
| 1 | Hungrybox | Hungrybox | Bobby big ballz |
| 2 |  Plup  |  Leffen | Ginger
| 3 |  Armada|  Zain |Colbol
| 4 |   Leffen|  Mang0 | iBDW
| 5 |   Zain|  Wizzrobe | S2J
| 6 | Mang0  |  Axe | Ben
| 7 |   Mew2King|  Plup | Gahtzu
| 8 |   Wizzrobe| iBDW | LSD
| 9 |  aMSa | aMSa | n0ne
| 10 |  SFAT |   S2J  | Zain

The full results for each season (2018,2019,2020) are in their corresponding csv.

## Comparison to other methods

### Elo 
Unlike Elo this method is order-independent which makes more sense for season rankings. It also handles double elimination tournaments better, because for each win in the loser's bracket, it gives a partial win to the player who knocked them down.  
Furthermore, "farming" a region is less effective, for example, suppose Duck dominates the Michigan area, under Elo, playing a lot of sets in his region would earn him many more points than those he would lose from playing fewer sets at supermajors. Conversely, after a single loss, this system would quickly redistribute Duck's (and Michigan's) points across the network.


### Panel of Experts

The people asked to rate the players are able to discern and evaluate special cases (sandbagging, less serious tournaments, new controllers, etc.) and perform better with poor data quality.


This method is free from the so-called legacy bias and caster bias. It is able to rank the entire dataset and does so at a much faster speed.

Overall, these serve different purposes. While the panelists are asked to rate the quality of play for each of the 120 qualified players during the season on a scale of 1 to 10 based on the quality and quantity of results, this method tries to answer who is the player that beat the most players, who beat the most players, who beat the most players, and so on.


## Shortcomings

### Data Related

Some of the tags in the database are duplicated, while a part of those belong to different people e.g. King, some of them don't e.g. Aniolas. I haven't found a way to scan and solve this problem for 4743 instances of duplicated tags. Considering that most top players have unique tags, I decided to merge records of identical tags.

Incomplete data even in recent years. Stango was ranked 47th on the 2019 MPGR, while ranking 148th here. Upon inspection, we noticed that the database misses his run at Fight Pitt 9, which was described as the "run of his career". Or AbsentPage, whose only 2019 record in the database is his Genesis 6 run.

### Execution related

Not all tournaments are created equal, the original model was used to rank college football so that assumption was fair. On the other hand, it's not the same to defeat Axe at a weekly than to do it at Genesis. As a result of this, without any modifications to the model, we find that Falgoat, an unranked falco main ranks #36 in this model's 2019 Ranking, having defeated Zain at Blast Off! #31, a tournament with 30 entrants.

### Intrinsic

When all eigenvalues are zero, alpha is not limited and the rankings are degenerate. This happens when the graph has no loops of the form A beats B who beats C who beats A or longer. Such seems to be the case of the 2020 season.


## Further Work
* Gather better, more complete data
* Experiment weighting tournament size
* Determine optimal value for alpha scaling (.8 seems low)