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

[part1.py](part1.py) is the python implementation of this solution. Time complexity is `O(N^2 * K + K^2 * N)` where `N` is a length of the grid (assumed to be square) and `K` is the number of asteroids.

#### Linear Algebra

There should be a smart linear algebra solution. I haven't figured out details yet but the approach will something like this :

 - For each point:
   - Transform matrix according to point
   - Find and count all lineary independent point groups
 - Select max

`TODO: Update if I implement this solution`

#### Hash Angles

A slightly better solution would be hashing `x / y` with `Fraction` class in the standard library and putting in a set. The length of the final set would be equal to the number of asteroid in the enter point's line of sight. The complexity of this approach is `O(N^2 + K^2)` but it takes more time than brute force approach :

Set Method:

```
real	0m1,798s
user	0m1,788s
sys		0m0,008s
```

Brute Force Method:

```
real	0m0,532s
user	0m0,524s
sys		0m0,008s
```

I profiled the code with line profiler, Adding into set takes around 60% of whole script time.

```
    37    120756      60351.0      0.5      1.7              if x < 0:
    38     58788      28992.0      0.5      0.8                  if y == 0:
    39      1494       1394.0      0.9      0.0                      left_set.add(float('inf'))
    40                                                           else:
    41     57294     398996.0      7.0     11.6                      angle = Fraction(x, y)
    42     57294    1028585.0     18.0     29.8                      left_set.add(angle)
    43     61968      32030.0      0.5      0.9              elif x > 0:
    44     58788      29051.0      0.5      0.8                  if y == 0:
    45      1494       1209.0      0.8      0.0                      right_set.add(float('inf'))
    46                                                           else:
    47     57294     398340.0      7.0     11.5                      angle = Fraction(x, y)
    48     57294    1021678.0     17.8     29.6                      right_set.add(angle)
```

My guess is cpython's Fraction [hash function](https://github.com/python/cpython/blob/master/Lib/fractions.py#L556) is more complicated than we need in our case. To get around this problem, I created a custom Fraction class and solution became faster than brute force solution.

```python
class Fraction:

    def __init__(self, a, b):

        if a == 0:
            self.val = (0, 0)
        else:
            gcd = math.gcd(a, b)
            self.val = (a // gcd, b // gcd)

    def __hash__(self):
        return hash(self.val)

    def __eq__(self, other):
        return self.val == other.val
```

Runtime result:

```
real	0m0,202s
user	0m0,198s
sys	0m0,004s
```

### Part 2

For my input, the solution of part 1 was `299` and second part 2 asks about `200`th destroyed asteroid. Since it is less than `299`, I just sorted the points found in part 1 according its angle to station's point. No need for the second turn of laster. This implementation can be found in [part2.py](part2.py).