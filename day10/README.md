## Day 10

### Part 1

It is a line of sight problem in cartesian grid. Given a grid of points where some asteroids are placed on. The puzzle is asking the asteroid that can see maximum number of asteroids. Asteroids have no volume, they are all points.

#### Brute-force

It seems this problem requires more thinking than previous puzzles. Even coding brute-force way was not super easy.

**Observation :** All x, y coordinates are integer. We can use this fact to find a method to detect occlusions. 

**Finding** 

Points `(0, 0)`, `(a, b)` and `(c, d)` are linear if and only if `a / gcd(a, b)` equals `c / gcd(c, d)` and `b / gcd(a, b)` equals `d / gcd(c, d)`. (a, b, c, d are not zero)

**Method**

 - For every asteroid A:
   - Transform asteroid matrix so that A's point becomes `(0, 0)`
   - For every asteroid B:
     - Find its integer unit vector
     - Mark every B + k `*` u point in the grid as undetectable (k > 1)
   - Count every deteable asteroids.

[part1.py](part1.py) is the python implementation of this solution. Time complexity is `O(N^2 + K^2 * N)` where `N` is a length of the grid (assumed to be square) and `K` is the number of asteroids.

#### Linear Algebra

There should be a smart linear algebra solution. I haven't figured out details yet but the approach will something like this :

 - For each point:
   - Transform matrix according to point
   - Find and count all lineary independent point groups
 - Select max

`TODO: Update if I implement this solution`

### Part 2

For my input, the solution of part 1 was `299` and second part 2 asks about `200`th destroyed asteroid. Since it is less than `299`, I just sorted the points found in part 1 according its angle to station's point. No need for the second turn of laster. This implementation can be found in [part2.py](part2.py).