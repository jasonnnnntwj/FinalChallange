from tkinter import *

main = Tk()
main.geometry("625x625")

# frame1 = Frame(top, highlightbackground="blue", highlightthickness=2)
# frame1.pack(padx=20, pady=20)

# C1 = Checkbutton(frame1, text = "Music", width=200, anchor="w")
# C1.pack(padx=10, pady=10)

# C2 = Checkbutton(frame1, text = "Video", width=200, anchor="w")
# C2.pack(padx=10, pady=10)

# C3 = Checkbutton(frame1, text = "Songs", width=200, anchor="w")
# C3.pack(padx=10, pady=10)

# C4 = Checkbutton(frame1, text = "Games", width=200, anchor="w")
# C4.pack(padx=10, pady=10)

# Button(frame1, text="Button-1", font=("Calibri",12,"bold")).pack(padx=10, pady=10)
frameA = Frame(main, highlightbackground="blue", highlightthickness=2) 
frameA.grid(row=0, column=0, padx=20, pady=20)
Button(frameA, text="Frame 1", font=("Calibri",12,"bold"),width=43,height=17).pack()
#shades buttons  
frameB = Frame(main, highlightbackground="red", highlightthickness=2) 
frameB.grid(row=0, column=1 , padx=20, pady=20)
Button(frameB, text="Frame 2", font=("Calibri",12,"bold"),width=13,height=17).pack()


#colour buttons
frameC = Frame(main, highlightbackground="green", highlightthickness=2)
frameC.grid(row=1, columnspan=2, padx=20, pady=20) 
Button(frameC, text="Frame 3", font=("Calibri",12,"bold"),width=59,height=2).pack()

#send buttons
frameD = Frame(main, highlightbackground="yellow", highlightthickness=2)
frameD.grid(row=2, columnspan=2, padx=20, pady=5)
Button(frameD, text="Frame 4", font=("Calibri",12,"bold"),width=59,height=2).pack()


main.mainloop()