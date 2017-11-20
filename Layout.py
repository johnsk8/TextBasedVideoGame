# The layout scheme of Space Sauce
# Author: John L Garcia

# Worlds are represented as NxN matrices

world1_Size = [0, 4] # World 1 is 5x5 -> 0-4

world1 = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-']
]

# Legend for World 1:
#   S = Starting point
#   - = Empty
#   I = Item
#   M = Monster
#   G = Gate to move onto the next world
#   * = Key for unlocking gate

world1_Legend = [
    ['M', '-', '-', 'I', 'G'],
    ['-', 'I', '-', '-', 'I'],
    ['-', '-', 'S', '-', '-'],
    ['*', '-', '-', 'I', '-'],
    ['M', 'I', '-', '-', 'M']
]