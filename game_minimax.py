def get_feedback(guess, secret):
    """Calculate feedback for a guess against a secret number"""
    guess_str = str(guess).zfill(3)
    secret_str = str(secret).zfill(3)
    
    correct_position = sum(g == s for g, s in zip(guess_str, secret_str))
    
    guess_counts = {}
    secret_counts = {}
    
    for i in range(3):
        if guess_str[i] != secret_str[i]:
            guess_counts[guess_str[i]] = guess_counts.get(guess_str[i], 0) + 1
            secret_counts[secret_str[i]] = secret_counts.get(secret_str[i], 0) + 1
    
    wrong_position = sum(min(guess_counts.get(d, 0), secret_counts.get(d, 0)) 
                        for d in set(guess_counts.keys()))
    
    return correct_position, wrong_position

def is_consistent(candidate, guesses_feedback):
    """Check if a candidate is consistent with all previous feedback"""
    for guess, (correct_pos, wrong_pos) in guesses_feedback:
        expected_pos, expected_wrong = get_feedback(guess, candidate)
        if expected_pos != correct_pos or expected_wrong != wrong_pos:
            return False
    return True

def find_best_guess_minimax(possible_numbers):
    """Find the guess that minimizes the maximum partition size (minimax strategy)"""
    best_guess = None
    best_score = float('inf')
    
    for guess in possible_numbers:
        partitions = {}
        
        for candidate in possible_numbers:
            feedback = get_feedback(guess, candidate)
            if feedback not in partitions:
                partitions[feedback] = 0
            partitions[feedback] += 1
        
        worst_case = max(partitions.values())
        
        if worst_case < best_score:
            best_score = worst_case
            best_guess = guess
    
    return best_guess

def play_game_minimax():
    print("Think of a 3-digit number (000-999)")
    print("I'll try to guess it using Minimax strategy!\n")
    
    possible = list(range(1000))
    guesses_feedback = []
    
    guess_count = 0
    
    while True:
        guess_count += 1
        
        print("Thinking...", end="", flush=True)
        guess = find_best_guess_minimax(possible)
        print("\r          \r", end="")  # Clear the "Thinking..." message
        
        print(f"\nGuess #{guess_count}: {str(guess).zfill(3)}")
        
        print("\nFeedback:")
        print("  [1] All digits wrong")
        print("  [2] Some correct digits, all in WRONG positions")
        print("  [3] Some correct digits, all in CORRECT positions")
        print("  [4] Some correct digits, some in correct positions, some in wrong positions")
        print("  [5] All digits correct, all in CORRECT positions (I win!)")
        
        choice = int(input("\nYour choice (1-5): "))
        
        if choice == 5:
            print(f"\n🎉 I found it! Your number is {str(guess).zfill(3)}")
            print(f"It took me {guess_count} guesses!")
            break
        elif choice == 1:
            correct_pos = 0
            wrong_pos = 0
        elif choice == 2:
            wrong_pos = int(input("How many digits are correct but in wrong positions? "))
            correct_pos = 0
        elif choice == 3:
            correct_pos = int(input("How many digits are correct and in correct positions? "))
            wrong_pos = 0
        elif choice == 4:
            correct_pos = int(input("How many digits are in CORRECT positions? "))
            wrong_pos = int(input("How many digits are correct but in WRONG positions? "))
        else:
            print("Invalid choice!")
            continue
        
        guesses_feedback.append((guess, (correct_pos, wrong_pos)))
        
        possible = [num for num in possible if is_consistent(num, guesses_feedback)]
        
        print(f"Possibilities remaining: {len(possible)}")
        
        if len(possible) == 0:
            print("\n❌ No valid numbers remain. Please check your feedback!")
            break
        elif len(possible) <= 10:
            print(f"Remaining possibilities: {[str(n).zfill(3) for n in possible]}")

if __name__ == "__main__":
    play_game_minimax()