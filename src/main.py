from game import TicTacToe

def main():
    game = TicTacToe()

    print("=== Tic-Tac-Toe ===")
    print(game)

    while True:
        print(f"\n{game.current.name}'s turn ({game.current.symbol})")

        try:
            row = int(input("Row (1-3): ")) - 1
            col = int(input("Col (1-3): ")) - 1
        except ValueError:
            print("Invalid input. Use numbers 1–3.")
            continue

        if not (0 <= row < 3 and 0 <= col < 3):
            print("Out of range (1–3).")
            continue

        if not game.play_turn(row, col):
            print("That position is already taken.")
            continue

        print("\n" + str(game))

        state = game.check_state()

        if state == "X" or state == "O":
            print(f"\nWinner: {state}!")
            break

        if state == "draw":
            print("\nDraw!")
            break

        game.switch()

if __name__ == "__main__":
    main()
