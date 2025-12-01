

from game import Game

# starting output to determine the game conditions 
# Timecomplexity: AI- O(1) / PvP- O(n^4)
def main():
    print("TicTacToe")
    print("1. Player vs AI (board 3x3)")
    print("2. Player vs Player (board 3-7)")
    choice = ""

    while choice not in ("1", "2"):
        choice = input("Choose mode (1 or 2): ").strip()

    vs_ai = (choice == "1")
    game = Game(vs_ai)
    game.play()

if __name__ == "__main__":
    main()
