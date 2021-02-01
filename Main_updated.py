from tkinter import *
from tkinter import font
from tkinter import messagebox

WIN = Tk()
WIN.configure(bg='black')
WIN.title("TIC TAC TOE")
X_O_SIZE = font.Font(family='Helvetica', size=9, weight='bold')
LABEL_SIZE = font.Font(family='Helvetica', size=30, weight='bold')

flag = 1
x_score, o_score = 0, 0


def winner_display(param):
    global x_score, o_score

    if param == 'X':
        x_score += 1
    else:
        o_score +=1


def checkWin():
    choice = 0
    if B1['text'] == B2['text'] and B1['text'] == B3['text'] and B1['text'] != '':
        messagebox.showinfo('winner!!!', "PLAYER " + B1['text'] + " WINS!!!")
        choice = 1
        winner_display(B1['text'])
    elif B4['text'] == B5['text'] and B4['text'] == B6['text'] and B4['text'] != '':
        messagebox.showinfo('winner!!!', "PLAYER " + B4['text'] + " WINS!!!")
        choice = 1
        winner_display(B4['text'])
    elif B7['text'] == B8['text'] and B9['text'] == B7['text'] and B7['text'] != '':
        messagebox.showinfo('winner!!!', "PLAYER " + B7['text'] + " WINS!!!")
        choice = 1
        winner_display(B7['text'])

    elif B1['text'] == B4['text'] and B1['text'] == B7['text'] and B7['text'] != '':
        messagebox.showinfo('winner!!!', "PLAYER " + B1['text'] + " WINS!!!")
        choice = 1
        winner_display(B1['text'])
    elif B2['text'] == B5['text'] and B2['text'] == B8['text'] and B2['text'] != '':
        messagebox.showinfo('winner!!!', "PLAYER " + B2['text'] + " WINS!!!")
        choice = 1
        winner_display(B2['text'])
    elif B3['text'] == B6['text'] and B9['text'] == B3['text'] and B3['text'] != '':
        messagebox.showinfo('winner!!!', "PLAYER " + B3['text'] + " WINS!!!")
        choice = 1
        winner_display(B3['text'])

    elif B1['text'] == B5['text'] and B1['text'] == B9['text'] and B1['text'] != '':
        messagebox.showinfo('winner!!!', "PLAYER " + B1['text'] + " WINS!!!")
        choice = 1
        winner_display(B1['text'])
    elif B3['text'] == B5['text'] and B3['text'] == B7['text'] and B3['text'] != '':
        messagebox.showinfo('winner!!!', "PLAYER " + B3['text'] + " WINS!!!")
        choice = 1
        winner_display(B3['text'])

    if B1['text'] != "" and B2['text'] != "" and B3['text'] != "" and B4['text'] != "" and B5['text'] != "" \
            and B6['text'] != "" and B7['text'] != "" and B8['text'] != "" and B9['text'] != "" and choice == 0:
        messagebox.showinfo("Match Draw", "Match Draw!!!")
        choice = 1

    if choice == 1:
        Check = messagebox.askyesno("playAgain?", "Wanna Play Again?")
        if Check == 0:
            WIN.destroy()
        else:
            main()


def playTicTacToe(button):
    global flag
    button['font'] = X_O_SIZE
    if flag and button['text'] == '':
        button['text'] = 'X'
        flag = 0
    elif not flag and button['text'] == '':
        button['text'] = 'O'
        flag = 1
    checkWin()


def main():

    global B1, B2, B3, B4, B5, B6, B7, B8, B9
    Label(WIN, text="TIC TAC TOE", fg="white", bg="black", font=LABEL_SIZE).grid(row=0, column=0, padx=5, pady=5,
                                                                                 columnspan=3)

    B1 = Button(WIN, text="", fg="black", width=20, height=6, bd=0, bg="#fff", font=font.Font(family='calibri', size=10)
                , command=lambda: playTicTacToe(B1))
    B1.grid(row=1, column=0, padx=5, pady=5)
    B2 = Button(WIN, text="", fg="black", width=20, height=6, bd=0, bg="#fff", font=font.Font(family='calibri', size=10)
                , command=lambda: playTicTacToe(B2))
    B2.grid(row=1, column=1, padx=5, pady=5)
    B3 = Button(WIN, text="", fg="black", width=20, height=6, bd=0, bg="#fff", font=font.Font(family='calibri', size=10)
                , command=lambda: playTicTacToe(B3))
    B3.grid(row=1, column=2, padx=5, pady=5)
    B4 = Button(WIN, text="", fg="black", width=20, height=6, bd=0, bg="#fff", font=font.Font(family='calibri', size=10)
                , command=lambda: playTicTacToe(B4))
    B4.grid(row=2, column=0, padx=5, pady=5)
    B5 = Button(WIN, text="", fg="black", width=20, height=6, bd=0, bg="#fff", font=font.Font(family='calibri', size=10)
                , command=lambda: playTicTacToe(B5))
    B5.grid(row=2, column=1, padx=5, pady=5)
    B6 = Button(WIN, text="", fg="black", width=20, height=6, bd=0, bg="#fff", font=font.Font(family='calibri', size=10)
                , command=lambda: playTicTacToe(B6))
    B6.grid(row=2, column=2, padx=5, pady=5)
    B7 = Button(WIN, text="", fg="black", width=20, height=6, bd=0, bg="#fff", font=font.Font(family='calibri', size=10)
                , command=lambda: playTicTacToe(B7))
    B7.grid(row=3, column=0, padx=5, pady=5)
    B8 = Button(WIN, text="", fg="black", width=20, height=6, bd=0, bg="#fff", font=font.Font(family='calibri', size=10)
                , command=lambda: playTicTacToe(B8))
    B8.grid(row=3, column=1, padx=5, pady=5)
    B9 = Button(WIN, text="", fg="black", width=20, height=6, bd=0, bg="#fff", font=font.Font(family='calibri', size=10)
                , command=lambda: playTicTacToe(B9))
    B9.grid(row=3, column=2, padx=5, pady=5)

    Label(WIN, text="X = " + str(x_score), fg="white", bg="black", font=LABEL_SIZE).grid(row=0, column=4, padx=5, pady=5,
                                                                                 columnspan=2, rowspan=4)
    Label(WIN, text="|| O = " + str(o_score), fg="white", bg="black", font=LABEL_SIZE).grid(row=0, column=6, padx=5, pady=5,
                                                                                    columnspan=2, rowspan=4)

    WIN.mainloop()


if __name__ == "__main__":
    main()
