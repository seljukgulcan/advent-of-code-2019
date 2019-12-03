## Day 3

The goal is to find intersection points of two traveler given two sequence of movements. Let's denote move count of a traveler by `M` and total step count of a traveler with `N`.

### Grid Approach

We can mark and store each tile that traveler 1 moved on then compare them with tiles of traveler 2. The problem with this approach is that the runtime depends on step count. If we multiple each step count with 1 million then the program takes 1 million more time to find the answer.

**Full Matrix** We can allocate a 2D array large enough to hold furthest travelled tile. It has `O(N)` time and `O(N^2)` memory complexity though the given input is small enough that this solution is still feasible.

**Sparse Matrix** For better memory complexity, a sparse matrix can be used. We can store only the tiles of interest instead of every tile in the grid. By hashing tiles with a set, look-up time (intersection time) becomes constant. 

### Line Approach

**Compare Each Pair of Move** Since all movements are straight lines, we only need to store start and end point of each line. By doing so, we can break the dependence of runtime on step count. We have two set of lines after parsing the input file. For each pair of lines in `set1 X set2`, we check if there is a intersection with complexity of `O(M^2)`. [part1.py](part1.py) and [part2](part2.py) show the implementation of this approach.

**Balance Binary Search Tree** I didn't implement this one but I guess we can reduce complexity to `O(M logM)` by using a balanced BST. It is much more complicated and python standard library doesn't include an balanced BST implementation so I'll pass.