from game2dboard import Board as GUIBoard        # gui board thing
from src.board import Board as LogicBoard        # our board logic
from src.ai import AI                            # ai logic
import tkinter as tk

# little window to pick options
def ask_settings():
    win=tk.Tk()
    win.title("TicTacToe setup")

    m=tk.StringVar(value="ai")
    sz=tk.IntVar(value=3)
    fst=tk.StringVar(value="human")

    tk.Label(win,text="Mode:").pack(anchor="w",padx=10,pady=(10,0))
    tk.Radiobutton(win,text="Player vs AI (3x3)",variable=m,value="ai").pack(anchor="w",padx=20)
    tk.Radiobutton(win,text="Player vs Player (3-7)",variable=m,value="pvp").pack(anchor="w",padx=20)

    tk.Label(win,text="Board size (PvP):").pack(anchor="w",padx=10,pady=(10,0))
    tk.Scale(win,from_=3,to=7,orient=tk.HORIZONTAL,variable=sz).pack(fill="x",padx=20)

    tk.Label(win,text="First move (AI mode):").pack(anchor="w",padx=10,pady=(10,0))
    tk.Radiobutton(win,text="Human",variable=fst,value="human").pack(anchor="w",padx=20)
    tk.Radiobutton(win,text="AI",variable=fst,value="ai").pack(anchor="w",padx=20)

    out={"ai":True,"size":3,"first":True}

    def go():
        out["ai"]=(m.get()=="ai")
        out["size"]=sz.get()
        out["first"]=(fst.get()=="human")
        win.destroy()

    tk.Button(win,text="Start",command=go).pack(pady=15)
    win.mainloop()
    return out["ai"],out["size"],out["first"]


# main gui game func
def run_gui():
    vs_ai,bd_size,h_first = ask_settings()

    if vs_ai:
        bd_size=3
        b=LogicBoard(bd_size)
        if h_first:
            p_sym="X"; a_sym="O"
        else:
            p_sym="O"; a_sym="X"
        ai=AI(a_sym)
        turn="X"
    else:
        if bd_size<3 or bd_size>7: bd_size=3      # safety check
        b=LogicBoard(bd_size)
        ai=None
        p_sym=None
        turn="X"

    g=GUIBoard(bd_size,bd_size)
    maxpx=600
    g.cell_size=maxpx//bd_size                    # scale cells
    g.cell_border=2
    g.cell_color="white"
    g.title=f"TicTacToe GUI {bd_size}x{bd_size}"

    win_cells=[]
    blink=True
    ended=False

    # refresh gui from logic board
    def sync():
        for r in range(bd_size):
            for c in range(bd_size):
                v=b.grid[r][c]
                g[r][c]=v if v!=" " else " "       # draw X/O or blank

    # find winning line
    def find_line(board,s):
        g2=board.grid
        n=board.size
        for r in range(n):
            if all(g2[r][cc]==s for cc in range(n)): return[(r,cc)for cc in range(n)]
        for c in range(n):
            if all(g2[rr][c]==s for rr in range(n)): return[(rr,c)for rr in range(n)]
        if all(g2[i][i]==s for i in range(n)): return[(i,i)for i in range(n)]
        if all(g2[i][n-1-i]==s for i in range(n)): return[(i,n-1-i)for i in range(n)]
        return[]

    # click handler
    def clicked(btn,r,c):
        nonlocal turn,ended,win_cells
        if ended: return

        if vs_ai:
            if turn!=p_sym: return                # wait for human turn
            ok=b.make_move(r,c,p_sym)
            if not ok: return                    # cell already used
            sync()
            w=b.check_winner()
            if w:
                print("Winner:",w)
                win_cells=find_line(b,w); ended=True; return
            if b.is_full():
                print("Draw"); ended=True; return

            turn=a_sym
            ai.make_move(b)                      # AI turn
            sync()
            w=b.check_winner()
            if w:
                print("Winner:",w)
                win_cells=find_line(b,w); ended=True; return
            if b.is_full():
                print("Draw"); ended=True; return

            turn=p_sym
            return

        # pvp
        ok=b.make_move(r,c,turn)
        if not ok: return
        sync()
        w=b.check_winner()
        if w:
            print("Winner:",w)
            win_cells=find_line(b,w); ended=True; return
        if b.is_full():
            print("Draw"); ended=True; return
        turn="O" if turn=="X" else "X"            # switch turn

    # animation
    def tick():
        nonlocal blink
        if not ended or not win_cells: return
        for (rr,cc) in win_cells:
            g[rr][cc] = b.grid[rr][cc] if blink else " "
        blink=not blink

    # AI goes first?
    if vs_ai and p_sym=="O":
        ai.make_move(b)
        sync()
        turn=p_sym

    g.on_mouse_click=clicked
    g.on_timer=tick
    g.start_timer(300)
    sync()
    g.show()


if __name__=="__main__":
    run_gui()
