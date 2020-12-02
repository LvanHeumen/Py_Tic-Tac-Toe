# Brainstorm

Important things to note that could help implementation:
- It's a two player game, no AI implementation necessary.
- The first possible "win" takes place at turn 5. Therefor, win conditions don't need to be checked before that
- When checking win conditions, an initial check of three surrounding cells should narrow down the possible win. For example:
1|2|3
4|5|6
7|8|9
 If the current player places their mark in cell 3, and only cell 5 has that player's mark, the only cell that needs to be checked for a possible win is cell 7
