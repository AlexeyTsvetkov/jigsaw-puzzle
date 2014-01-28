Jigsaw puzzle solver
=====================
Description
----------
Implementation of jigsaw puzzle solver, capable of solving small puzzles, that consist of square non-overlapping pieces.

Depends on Pillow (modern PIL fork) and NumPy.

Algorithm
---------
1. Represent puzzle pieces as nodes, dissimilarity measures between pieces as edges (4 for each pair of pieces).
2. Find constrained MST using Kruskal algorithm.
3. Trim resulting image using known puzzle dimensions (maximizing nonempty slots in trimmed image).
4. Fill empty slots in trimmed image using greedy criteria: for each empty slot, a piece, with minimum average dissimilarity among nonempty neighbours, is chosen. Following heuristic used: empty slots with more nonempty neighbours should be filled first.

Usage example
---------
Puzzle generation:

```bash
src/run.py --generate -i examples/boat.jpg  -o examples/puzzle --piece_size 40
Puzzle saved to: examples/puzzle
Puzzle sizes: width=10, height=10
```

Puzzle solving:

```bash
src/run.py --solve -i examples/puzzle  -o examples/boat-solved.png  --puzzle_width 10 --puzzle_height 10
Resulting image saved to: examples/boat-solved.png
```
Arguments
---------
* ```-g/--generate``` --- generate puzzle pieces from image
* ```-s/--solve``` --- generate puzzle pieces from image
* ```-i/--input``` --- path to input image or puzzle directory (required)
* ```-o/--output``` --- path to output image or puzzle directory (required)
* ```-ps/--piece_size``` --- piece size of generated puzzle (required for generation)
* ```-pw/--piece_width``` --- puzzle width in pieces (required for solving)
* ```-ph/--piece_height``` --- puzzle height in pieces (required for solving)

References
--------
[1] A. C. Gallagher. Jigsaw puzzles with pieces of unknown orientation. In CVPR, 2012.

[2] D. Mondal et. al. Robust Solvers for Square Jigsaw Puzzles. In CVPR, 2013.

[3] D. Pomeranz et. al. A fully automated greedy square jigsaw puzzle solver. In CVPR, 2011.
