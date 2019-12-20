## Day 20

Much easier than Day 18. I've solved it under 1 hour, almost got in top 100.

I've converted input file manually into more machine readable format. I thought it's easier to change them by hand so my code works on converted input files for now, I'll probably change that in the future.

Original Example Input:
```
         A           
         A           
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###.#  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #########.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z       
             Z       
```

Converted Example:
```
#######@#########
#######.........#
#######.#######.#
#######.#######.#
#######a#######.#
#####       ###.#
a..##       ###.#
##.##       ###.#
##..b       ###.#
#####       ###.#
#########c#####.#
b.#######...###.#
#.#########.###.#
c.#########.....#
###########>#####
```

### Part 1 & Part 2

I solved both [part1](part1.py) and [part2](part2.py) with breadth first search (BFS). In part1, teleportation points just add extra edge to those nodes. In part2, we consider waypoints as staircase, inner waypoints let you go to next level and outer ones for previous level. We start at level 0 so we need to exit at level 0. Considering this way, it is as simple as part 1.
