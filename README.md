# FantasyOrder
Randomizer for FF Draft

This contains the code I used to randomly create our draft order (posted here for transparency). I didn't want to just shuffle the 10 teams to avoid one person getting picks 1 and 2 (or 9 and 10) or similar. So I used the following process:

1. Each person is assigned a random number from 1-5 with no overlap. These correspond to the first 5 positions in the draft.
2. Each person is assigned a random number from 6-10 with no overlap. These correspond to positions 6-10 in the draft.
3. Each player flips a coin. If the coin is heads, their team 1 gets their chosen pick from spots 1-5 and their team 2 gets their chosen pick from spots 6-10. If the coin is tails, the opposite happens.

If you want, you can run the code yourself with the command `python3 FantasyOrder.py` in a terminal. If you run it multiple times, you will see that it is randomized.

After testing the code, I ran it once to generate a single permutation, and posted the results in the chat.

Hopefully this is clear. Let me know if you have any questions!