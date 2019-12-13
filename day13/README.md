## Day 13

We play [Breakout](https://en.wikipedia.org/wiki/Breakout_(video_game)) in this puzzle although the puzzle description doesn't mention it explicitly. It gives us an intcode program and expects us to figure out the game. The output of the program gives location of the objects, i.e. game screen. Paddle can be controlled with encoded left, right inputs.

### Part 1

In part 1, the answer is the number of block objects in the screen. Parsing the output of intcode program is sufficent to solve it. It's in [part1.py](part1.py)

### Part 2

The answer asks the final score we can get after hitting the last block on the screen. 

#### Simulate the Game with Tracking Paddle

We write a stupid simple bot to play the game. We can send left, right signals according to position of ball. Go left if the ball is on the left side of the paddle or vice versa. [part2.py](part2.py)

![Game](game.gif)

#### Reverse Engineer the Score System (*TODO*)

The score is not as simply as destroyed block multiplied by some constant. However, I think I can figure it out by inspecting intcode program a while. I'll update if I can find something intelligent.