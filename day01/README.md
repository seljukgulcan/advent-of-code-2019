## Day 1

### Part 1

An easy one. We apply a couple of operations on input and then sum them up. 

```python
total = 0
for line in sys.stdin:
	total += int(line) // 3 - 2
print(total)
```

### Part 2

Here we apply the same operations again and again until the number becomes nonpositive.

```python
total = 0
for line in sys.stdin:
	fuel = int(line) // 3 - 2

	while fuel > 0 :
		total += fuel
		fuel = fuel // 3 - 2
		
print(total)
```

At each step, we divide by 3 so the complexity is `O(log n)`. 

I wonder if we can find a form for the summation which can be calculated in constant time. 

![](tex/1.png)

![](tex/2.png)

`A_0` is the given number, `n`.

It looks possible at first but the floor operation makes it difficult. I think, it is not possible to calculate floor of the terms before knowing them so we need to find 3 modulus of each term explicitly, which costs `logn` operations. Let me know if you found a `O(1)` solution.