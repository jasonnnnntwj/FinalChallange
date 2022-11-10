from tkinter import*
from turtle import color


#function section

#function to assign colour integer value so can switch ltr, also it prints out value of colour when selected, the bottom is just the hard code method that doesnt use the .format call back 
#argument which is way lesser lines18
def ColourSwitch(a):
 global colour
 colour= a
#  print("currently selected colour is {}".format(colour))
 if colour == 0:
    print("Click button to make it white.")
 elif colour ==1:
    print("Click button to make it gray 1")
 elif colour ==2:
    print("Click button to make it gray 2")
 elif colour ==3:
    print("Click button to make it gray 3")    
 elif colour ==4:
    print("Click button to make it gray 4")    
 elif colour ==5:
    print("Click button to make it gray 5")
 elif colour ==6:
    print("Click button to make it gray 6")
 else:
    print("Click button to make it black")

#function to assign button to colour 
def ColourButton(i, j):
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


#nested for loops, basically i is the amt of 'patterns' and j is the amt of times the pattern is repeated 

#function to make everything white
def allwhite():
  print("all 1024 squares are white")
  for j in range (32):
    for i in range (32):
      button[i][j].config(bg='grey99')
      value[i][j] = 0

def allblack():
  print("all 1024 squares are black")
  for j in range (32):
    for i in range (32):
      button[i][j].config(bg='grey1')
      value[i][j] = 90

def pattern1():
    print("This is pattern 1")
    for j in range (32): 
        for i in range(32): 
            if j <= 5: 
                button[i][j].config(bg='grey99') 
                value[i][j] = 0 
            elif 6 <= j <= 10: 
                button[i][j].config(bg='grey77') 
                value[i][j] = 30 
            elif 11 <= j <= 15: 
                button[i][j].config(bg='grey44') 
                value[i][j] = 50 
            elif 16 <= j <= 20: 
                button[i][j].config(bg='grey33') 
                value[i][j] = 60 
            elif 21 <= j <= 25: 
                button[i][j].config(bg='grey11') 
                value[i][j] = 70 
            else: 
                button[i][j].config(bg='grey1') 
                value[i][j] = 90 



def pattern2():
  print("Pattern 2!")
  for i in range (32): 
     for j in range (32): 
      button[i][j].config(bg ='white') 
      value[i][j] = 0 
      if i == j:  
        button[i][j].config(bg='grey1') 
        value[i][j] = 90 
      elif i + j == 1:  
        button[i][j].config(bg='grey99') 
        value[i][j] = 0 
      elif i + j == 31:  
        button[i][j].config(bg='grey1') 
        value[i][j] = 90 




def sendImage():
    global value
    print("Image has been printed, the values are...")
    print(value)

main=Tk()
colour = 0

#INDIVIDUAL FRAMES FOR GUI WIDGET PLACEMENTS
#32x32 buttons
frameA = Frame(main, highlightbackground="blue", highlightthickness=4) 
frameA.grid(row=0, column=0,padx=20, pady=20)

#shades buttons  
frameB = Frame(main, highlightbackground="red", highlightthickness=4) 
frameB.grid(row=0, column=1,padx=20, pady=20)

#colour buttons
frameC = Frame(main, highlightbackground="green", highlightthickness=4)
frameC.grid(row=1, columnspan=2) 

#send buttons
frameD = Frame(main, highlightbackground="yellow", highlightthickness=4)
frameD.grid(row=2, columnspan=2)

#FRAME A's GRID'S BUTTON NESTED LOOP TO MAKE THE 32X32 

button = [[j for j in range(32)] for i in range(32)]

value = [[0 for j in range(32)] for i in range (32)]


for j in range (32):
  for i in range (32):
    button[i][j] = Button(frameA, font=("Arial, 5"), width=2, height=2, command=lambda c=i, d=j:ColourButton(c, d))
    button[i][j].grid(row=i, column=j)

#FRAME B's Buttons to control colour selection
#lambda is a 'small function like the 'def' functions on top. In this instance it sets the value of colour/a as the number then it calls the colour switch function with the variable set as a
#in the parameter so it'll print out the value in the terminal accourding to the button pressed.

white= Button(frameB, text="White", font=("Arial,12"),bg='grey99',width=13,height=2, command=lambda a=0:ColourSwitch(a))
white.grid(row=0,column=0)

grey1= Button(frameB, text="Grey 1", font=("Arial,12"),bg='grey88',width=13,height=2, command=lambda a=1:ColourSwitch(a))
grey1.grid(row=1,column=0)

grey2= Button(frameB, text="Grey 2", font=("Arial,12"),bg='grey77',width=13,height=2, command=lambda a=2:ColourSwitch(a))
grey2.grid(row=2,column=0)

grey3= Button(frameB, text="Grey 3", font=("Arial,12"),bg='grey66',width=13,height=2, command=lambda a=3:ColourSwitch(a))
grey3.grid(row=3,column=0)

grey4= Button(frameB, text="Grey 4", font=("Arial,12"),bg='grey44',fg='white', width=13,height=2, command=lambda a=4:ColourSwitch(a))
grey4.grid(row=4,column=0)

grey5= Button(frameB, text="Grey 5", font=("Arial,12"),bg='grey33',fg='white',width=13,height=2, command=lambda a=5:ColourSwitch(a))
grey5.grid(row=5,column=0)

grey6= Button(frameB, text="Grey 6", font=("Arial,12"),bg='grey11',fg='white',width=13,height=2, command=lambda a=6:ColourSwitch(a))
grey6.grid(row=6,column=0)
    
grey7= Button(frameB, text="Black", font=("Arial,12"),bg='grey1',fg='white',width=13,height=2, command=lambda a=7:ColourSwitch(a))
grey7.grid(row=7,column=0)    

#FRAME C's Button Presets to make patterns

allwhite = Button(frameC, text="All White",font=("Arial, 12"), bg='grey99', width=13, height=2, command=allwhite)
allwhite.grid(row=0, column=0)

allblack = Button(frameC, text="All Black",font=("Arial, 12"), bg='grey1', fg='white', width=13, height=2, command=allblack)
allblack.grid(row=0, column=1)

pattern1 = Button(frameC, text="Pattern 1",font=("Arial, 12"), bg='red', width=13, height=2, command=pattern1)
pattern1.grid(row=0, column=2)

pattern2 = Button(frameC, text="Pattern 2",font=("Arial, 12"), bg='yellow', width=13, height=2, command=pattern2)
pattern2.grid(row=0, column=3)

#FRAME D's Button to send image value in a sets of 32 , 32 times onto the terminal
send = Button(frameD, text="Send Imaged!", font=("Arial, 12"), width=13, height=2, command=sendImage)
send.grid(row=0, column=0)

print("Button is {}".format(button))


main.mainloop()
