# AoC Python Executor

Python executor for the [Advent of Code Solver](https://github.com/tcollier/aoc_solver).

## Template Code

```python
# main.py
import sys

from aoc_executor import AocExecutor


def part1_solution(input):
    # compute part 1 solution
    return solution


def part2_solution(input):
    # compute part 2 solution
    return solution

input = # load input
executor = AocExecutor(input, part1_solution, part2_solution)
executor(sys.argv)
```
