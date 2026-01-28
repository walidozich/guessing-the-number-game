# Numbers Game

A guessing game where the AI tries to find your secret 3-digit number (000-999) using feedback on digit matches.

## Game Mechanics

Think of a 3-digit number and the AI makes guesses. After each guess, you provide feedback:

1. **All digits wrong** - None of the digits in the guess are in your number
2. **Correct digits, wrong positions** - Some digits are right but in wrong positions
3. **Correct digits, correct positions** - Some digits are right and in correct positions
4. **Mixed** - Some digits in correct positions, some in wrong positions
5. **Found it!** - All digits correct and in correct positions

## Files

### `game.py`
The original linear search implementation. Picks guesses sequentially from the remaining possibilities.

**Run:**
```bash
python game.py
```

**Performance:** May require many guesses; worst case ~1000 guesses

---

### `game_minimax.py`
Optimized implementation using the **Minimax strategy**. Selects each guess to minimize the worst-case number of remaining possibilities.

**Run:**
```bash
python game_minimax.py
```

**Performance:** ~5-6 guesses on average; much faster convergence

---

## Strategy Comparison

| Strategy | Approach | Avg Guesses | Worst Case |
|----------|----------|-------------|-----------|
| Linear | Pick first remaining number | ~500 | 1000 |
| Minimax | Minimize worst-case partition | ~5-6 | ~9-10 |

## How Minimax Works

For each potential guess, the algorithm:
1. Simulates all possible feedback outcomes
2. Counts how many candidates fall into each partition
3. Selects the guess with the smallest maximum partition

This ensures rapid elimination of possibilities with each guess.

## Algorithm Complexity

- **Linear:** O(n) per guess where n = remaining candidates
- **Minimax:** O(n²) per guess (evaluates all candidates × partitions) but dramatically fewer total guesses

The Minimax approach trades off computation per guess for exponentially fewer guesses needed.
