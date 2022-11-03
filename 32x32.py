from tkinter import *

# ------------------------------------------------------------------------------Definiton------------------------------------------------------------------------------------------- #

def whitebtn(i, j):
  global colour   
  if colour == 0:
    button[i][j].config(bg='grey99')
    value[i][j] = 0
  elif colour == 1: 
    button[i][j].config(bg='grey88')
    value[i][j] = 20
  elif colour == 2:
    button[i][j].config(bg='grey77')
    value[i][j] = 30
  elif colour == 3: 
    button[i][j].config(bg='grey66')
    value[i][j] = 40
  elif colour == 4:
    button[i][j].config(bg='grey44')
    value[i][j] = 50  
  elif colour == 5: 
    button[i][j].config(bg='grey33')
    value[i][j] = 60
  elif colour == 6:
    button[i][j].config(bg='grey11')
    value[i][j] = 70
  else: 
    button[i][j].config(bg='grey1')
    value[i][j] = 90

def change_colour(m): 
  global colour
  colour=m
  if colour == 0:
    print("Choose Button to change color to White!")
  elif colour == 1:
    print("Choose Button to change color to Grey 1!")
  elif colour == 2:
    print("Choose Button to change color to Grey 2!")
  elif colour == 3:
    print("Choose Button to change color to Grey 3!")
  elif colour == 4:
    print("Choose Button to change color to Grey 4!")
  elif colour == 5:
    print("Choose Button to change color to Grey 5!")
  elif colour == 6:
    print("Choose Button to change color to Grey 6!")
  else :
    print("Choose Button to change color to Black!")

def allwhite():
  print("All White!")
  for j in range (32):
    for i in range (32):
      button[i][j].config(bg='grey99')
      value[i][j] = 0

def allblack():
  print("All Black!")
  for j in range (32):
    for i in range (32):
      button[i][j].config(bg='grey1')
      value[i][j] = 90

def pat1():
  print("Pattern 1!")
  for j in range (32):
    for i in range (32):
      if  j == 0: 
        button[i][j].config(bg='grey99')
        value[i][j] = 0 
      elif j == 1: 
        button[i][j].config(bg='grey77')
        value[i][j] = 30 
      elif j == 2:
        button[i][j].config(bg='grey44')
        value[i][j] = 50
      else:
        button[i][j].config(bg='grey1')
        value[i][j] = 90

def pat2():
  print("Pattern 2!")

def sendimg():
  global value
  print("Image Print! Values are...")
  print(value)

main = Tk()

# ----------------------------------------------------------------------------- Frame---------------------------------------------------------------------------------------------- #
colour = 0

frame1 = Frame(main) #32x32 btn
frame1.grid(row=0, column=0)

frame2 = Frame(main) #shades btn
frame2.grid(row=0, column=1)

frame3 = Frame(main)
frame3.grid(row=1, columnspan=2) #colour btns 

frame4 = Frame(main)
frame4.grid(row=2, columnspan=2) #send btn

# ----------------------------------------------------------------------------32x32 Grid-------------------------------------------------------------------------------------------- #
button = [[j for j in range(32)] for i in range(32)]

value = [[0 for j in range(32)] for i in range (32)]


for j in range (32):
  for i in range (32):
    button[i][j] = Button(frame1, font=("Arial, 4"), width=2, height=2, command=lambda r=i, c=j:whitebtn(r, c))
    button[i][j].grid(row=i, column=j)

    print(button)

# --------------------------------------------------------------------------Color button-------------------------------------------------------------------------------------------- #
white = Button(frame2, text="White", font=("Arial, 12"), bg='grey99', width=13, height=2, command=lambda m=0:change_colour(m))
white.grid(row=0, column=0)

grey1 = Button(frame2, text="Grey 1", font=("Arial, 12"), bg='grey88', width=13, height=2, command=lambda m=1:change_colour(m))
grey1.grid(row=1, column=0)

grey2 = Button(frame2, text="Grey 2", font=("Arial, 12"), bg='grey77', width=13, height=2, command=lambda m=2:change_colour(m))
grey2.grid(row=2, column=0)



grey3 = Button(frame2, text="Grey 3", font=("Arial, 12"), bg='grey66', width=13, height=2, command=lambda m=3:change_colour(m))
grey3.grid(row=3, column=0)

grey4 = Button(frame2, text="Grey 4", font=("Arial, 12"), bg='grey44', fg='white', width=13, height=2, command=lambda m=4:change_colour(m))
grey4.grid(row=4, column=0)

grey5 = Button(frame2, text="Grey 5", font=("Arial, 12"), bg='grey33', fg='white', width=13, height=2, command=lambda m=5:change_colour(m))
grey5.grid(row=5, column=0)

grey6 = Button(frame2, text="Grey 6", font=("Arial, 12"), bg='grey11', fg='white', width=13, height=2, command=lambda m=6:change_colour(m))
grey6.grid(row=6, column=0)

black = Button(frame2, text="Black", font=("Arial, 12"), bg='grey1', fg='white', width=13, height=2, command=lambda m=7:change_colour(m))
black.grid(row=7, column=0)

# -------------------------------------------------------------------------Special Color button-------------------------------------------------------------------------------------- #
allwhite = Button(frame3, text="All White",font=("Arial, 12"), bg='grey99', width=13, height=2, command=allwhite)
allwhite.grid(row=0, column=0)

allblack = Button(frame3, text="All Black",font=("Arial, 12"), bg='grey1', fg='white', width=13, height=2, command=allblack)
allblack.grid(row=0, column=1)

pattern1 = Button(frame3, text="Pattern 1",font=("Arial, 12"), bg='gold', width=13, height=2, command=pat1)
pattern1.grid(row=0, column=2)

pattern2 = Button(frame3, text="Pattern 2",font=("Arial, 12"), bg='#ff007f', width=13, height=2, command=pat2)
pattern2.grid(row=0, column=3)

# ------------------------------------------------------------------------------Send button------------------------------------------------------------------------------------------ #
send = Button(frame4, text="Send Imaged!", font=("Arial, 12"), width=13, height=2, command=sendimg)
send.grid(row=0, column=0)

print("Button is {}".format(button))

main.mainloop()

