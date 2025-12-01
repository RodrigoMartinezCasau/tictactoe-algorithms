from game2dboard import Board as GUIBoard        # GUI board from the library
from src.board import Board as LogicBoard        # our group's board logic
from src.ai import AI                            # AI class (minimax for 3x3)

print("TicTacToe GUI")
print("1. vs AI (3x3)")
print("2. PvP (3-7)")
choice=""
while choice not in("1","2"):
    choice=input("Choose(1 or 2): ").strip()     # simple mode selection

vs_ai=(choice=="1")

if vs_ai:
    size=3                                       # AI only works properly on 3x3
    logic_board=LogicBoard(size)
    first=input("Go first?(y/n): ").strip().lower()
    if first=="y":
        human_symbol="X"
        ai_symbol="O"
    else:
        human_symbol="O"
        ai_symbol="X"
    ai_player=AI(ai_symbol)                      # init AI object
    current_symbol="X"                           # X always starts in TicTacToe
else:
    size=0
    while size<3 or size>7:
        try:size=int(input("Board size(3-7): ")) # ask for size until valid
        except:print("numbers pls")
    logic_board=LogicBoard(size)
    ai_player=None                                # PvP mode
    human_symbol=None
    current_symbol="X"

# make the GUI board (separate from our logic board)
gui=GUIBoard(size,size)
max_pixels=600
gui.cell_size=max_pixels//size                   # scale cells so big boards fit
gui.cell_border=2                              
gui.cell_color="white"                           # white so X/O are visible
gui.title=f"TicTacToe GUI {size}x{size}"         # window title

winning_cells=[]                                 
blink_on=True                                    
game_over=False                                  # stops after win

def sync_gui():
    for r in range(size):
        for c in range(size):
            v=logic_board.grid[r][c]
            gui[r][c]=v if v!=" " else " "       # write X/O/space into GUI cell

def get_winning_cells(board,sym):
    g=board.grid
    n=board.size
    for r in range(n):
        if all(g[r][cc]==sym for cc in range(n)):
            return[(r,cc)for cc in range(n)]
    for c in range(n):
        if all(g[rr][c]==sym for rr in range(n)):
            return[(rr,c)for rr in range(n)]
    if all(g[i][i]==sym for i in range(n)):
        return[(i,i)for i in range(n)]
    if all(g[i][n-1-i]==sym for i in range(n)):
        return[(i,n-1-i)for i in range(n)]
    return[]                                      # no win found

def on_click(button,r,c):
    global current_symbol,game_over,winning_cells
    if game_over:return                            # ignore clicks after game ends

    if vs_ai:
        if current_symbol!=human_symbol:return     # only human moves on their turn
        ok=logic_board.make_move(r,c,human_symbol)
        if not ok:return                           # clicked occupied cell
        sync_gui()
        w=logic_board.check_winner()
        if w:
            print("Winner:",w)
            winning_cells=get_winning_cells(logic_board,w)
            game_over=True
            return
        if logic_board.is_full():
            print("Draw")
            game_over=True
            return
        current_symbol=ai_player.symbol            # switch to AI move
        ai_player.make_move(logic_board)           # AI plays its turn
        sync_gui()
        w=logic_board.check_winner()
        if w:
            print("Winner:",w)
            winning_cells=get_winning_cells(logic_board,w)
            game_over=True
            return
        if logic_board.is_full():
            print("Draw")
            game_over=True
            return
        current_symbol=human_symbol                # back to human turn
        return

    ok=logic_board.make_move(r,c,current_symbol)   # PvP mode: just alternate turns
    if not ok:return
    sync_gui()
    w=logic_board.check_winner()
    if w:
        print("Winner:",w)
        winning_cells=get_winning_cells(logic_board,w)
        game_over=True
        return
    if logic_board.is_full():
        print("Draw")
        game_over=True
        return
    current_symbol="O" if current_symbol=="X" else "X"   # swap symbols

def on_timer():
    global blink_on
    if not game_over or not winning_cells:return

    for(rr,cc)in winning_cells:
        gui[rr][cc]=logic_board.grid[rr][cc] if blink_on else " "  
    blink_on=not blink_on

if vs_ai and human_symbol=="O":
    ai_player.make_move(logic_board)               # if human goes second
    sync_gui()
    current_symbol=human_symbol

gui.on_mouse_click=on_click
gui.on_timer=on_timer
gui.start_timer(300)                               
sync_gui()
gui.show()
