# Python program to create a simple Graphical User Interface (GUI)
# Basic calculator using Tkinter


# import everything from the tkinter module
from tkinter import *

# import everything from the math module
from math import *  

# creating a GUI window
calci = Tk()

# set the height and width for GUI window
calci . geometry("350x435")

# set the background colour for GUI window 
calci . configure(background="sky blue")

# setting the title for GUI window
calci . title("Calculator")

# Holds a string the default value is an empty string
# StringVar() is the variable class we create an instance of this class
string_variable = StringVar()

# creating the text entry box for showing the values
# grid method is used for placing the widgets at respective positions in table like a structure
values_variable = Entry(calci, textvariable=string_variable) .  grid(columnspan=4 , ipadx=70)


string_variable.set("Enter your values")

# it is a global variable
values = ""



# Function to update their values in the text entry box 
def press(number):

    #point out the global expression variable
    #using the keyword global we can change the values for the global variable locally
    global values

    # concatenation of string
    values=values + str(number)

    # updating the values by using set method
    string_variable . set(values)

    
    
# function for power operation
def buttonpower(number = "**"):

    global values

    values=values + str(number)

    string_variable . set(values)
    


# function for floor operation
def buttonfloor(number = "//"):

    global values

    values=values + str(number)

    string_variable . set(values)
    


# function for decimal to binary convertion    
def buttonbin():

    # Try and except statement is used for handling the errors like zero division error , type error etc.
    # Put that code inside the try block which may generate the exception 
    try:

        global values
        
        # here the input values is in string so we are typecasting it to int and bin function is used to convert our input to binary
        answer = str(bin(int(values)))

        string_variable . set(answer)

        values = ""
        
    # if the exception is generated then it is handled by the except block
    except:
        
        string_variable . set("please press the bin after the number (-_-) ")

        values = ""



# function for decimal to octal convertion
def buttonoct():

    try:

        global values
        
        # here the input values is in string so we are typecasting it to int and oct function is used to convert our input to octal
        answer = str(oct(int(values)))

        string_variable . set(answer)

        values = ""
        
    except:

        string_variable . set("please press the oct after the number (-_-) ")

        values = ""    




# function for decimal to hexadecimal convertion
def buttonhex():

    try:

        global values
        
        # here the input values is in string so we are typecasting it to int and hex function is used to convert our input to hexadecimal
        answer = str(hex(int(values)))

        string_variable . set(answer)

        values = ""
        
    except:

        string_variable . set("please press the hex after the number (-_-) ")
 
        values = ""
        



# function for square root operation
def buttonsqroot():

    try:

        global values
        
         # here the input values is in string so we are typecasting it to int and sqrt function is used to convert our input to  sqroot values
        answer = str(sqrt(int(values)))

        string_variable . set(answer)

        values = ""
        
    except:

        string_variable.set("please press the sqroot after the number (-_-) ")

        values = ""

        


# function for factorial operation
def buttonfact():

    try:

        global values
        
        # here the input values is in string so we are typecasting it to int and factorial function is used to convert our input to corresponding factorial values
        answer = str(factorial(int(values)))

        string_variable . set(answer)

        values = ""
        
    except:

        string_variable . set("please press the fact after the number (-_-) ")

        values = ""
        


# function for sin operation
def buttonsin():

    try:

        global values
        
        # here the input values is in string so we are typecasting it to int and sin function is used to convert our input to corresponding sin values
        answer = str(sin(int(values)))

        string_variable . set(answer)

        values = ""
        
    except:

        string_variable . set("please press the sin after the number (-_-) ")

        values = ""




# function for cos operation
def buttoncos():

    try:

        global values
        
        # here the input values is in string so we are typecasting it to int and cos function is used to convert our input to corresponding cos values
        answer = str(cos(int(values)))

        string_variable . set(answer)

        values = ""
        
    except:

        string_variable . set("please press the cos after the number (-_-) ")

        values = ""




# function for tan operation
def buttontan():

    try:

        global values
        
        # here the input values is in string so we are typecasting it to int and tan function is used to convert our input to corresponding tan values
        answer = str(tan(int(values)))

        string_variable . set(answer)

        values = ""
        
    except:

        string_variable . set("please press the tan after the number (-_-) ")

        values = ""

        




# function for comma 
def buttoncomma(number = ","):

    global values

    values=values + str(number)

    string_variable . set(values)


                       


# function for gcd operation
def buttongcd():

    try:

        global values
        
        # spliting our values based on comma using split function
        spliting = values.split(',')

        # here the input values is in string so we are typecasting it to int and gcd function is used to convert our input to corresponding gcd values
        answer = str(gcd(int(spliting[0]),int(spliting[1])))
        
        string_variable . set(answer)

        values = ""
        
    except:

        string_variable . set("please press the gcd after the number (-_-) ")

        values = ""

        




# function for exponential 
def buttonexp(number = "e"):

    global values

    values=values + str(number)

    string_variable . set(values)




# Function to evaluate the final answer
def buttonequal():

    try:

        global values

        # the eval function evaluates the “String” like a python expression and returns the result as an integer
        answer = str(eval(values))

        string_variable . set(answer)

        values = ""

    except:

        string_variable . set(" please check your input (-_-) ")

        values = ""
        



# Function to clear the contents from the text entry box 
def buttonclear():

    global values

    values = ""

    string_variable . set("")
    





if __name__  ==  "__main__":
    

    # creates a Buttons and place at a particular location inside the root window . 
    # when user press the button, the corresponding function initiated to that button will be executed . 

    button_1 = Button(calci, text=' 1 ', fg='white', bg='blue', command=lambda: press(1), height=2, width=8) . grid(row=2, column=0)

    button_2 = Button(calci, text=' 2 ', fg='white', bg='blue', command=lambda: press(2), height=2, width=8) . grid(row=2, column=1)

    button_3 = Button(calci, text=' 3 ', fg='white', bg='blue', command=lambda: press(3), height=2, width=8) . grid(row=2, column=2)

    button_4 = Button(calci, text=' 4 ', fg='white', bg='blue', command=lambda: press(4), height=2, width=8) . grid(row=3, column=0)

    button_5 = Button(calci, text=' 5 ', fg='white', bg='blue', command=lambda: press(5), height=2, width=8) . grid(row=3, column=1)

    button_6 = Button(calci, text=' 6 ', fg='white', bg='blue', command=lambda: press(6), height=2, width=8) . grid(row=3, column=2)

    button_7 = Button(calci, text=' 7 ', fg='white', bg='blue', command=lambda: press(7), height=2, width=8) . grid(row=4, column=0)

    button_8 = Button(calci, text=' 8 ', fg='white', bg='blue', command=lambda: press(8), height=2, width=8) . grid(row=4, column=1)

    button_9 = Button(calci, text=' 9 ', fg='white', bg='blue', command=lambda: press(9), height=2, width=8) . grid(row=4, column=2)

    button_0 = Button(calci, text=' 0 ', fg='white', bg='blue', command=lambda: press(0), height=2, width=8) . grid(row=5, column=1)

    button_dot = Button(calci, text=' . ', fg='white', bg='darkblue', command=lambda: press('.'), height=2, width=8) . grid(row=5, column=0)

    button_add = Button(calci, text=' + ', fg='white', bg='grey', command=lambda: press('+'), height=2, width=8) . grid(row=6, column=0)

    button_sub = Button(calci, text=' - ', fg='white', bg='grey', command=lambda: press('-'), height=2, width=8) . grid(row=6, column=1)

    button_multiply = Button(calci, text=' * ', fg='white', bg='grey', command=lambda: press('*'), height=2, width=8) . grid(row=6, column=2)

    button_divide = Button(calci, text=' / ', fg='white', bg='grey', command=lambda: press('/'), height=2, width=8) . grid(row=7, column=0)

    button_modulo = Button(calci, text=' % ', fg='white', bg='grey', command=lambda: press('%'), height=2, width=8) . grid(row=7, column=1)

    button_power = Button(calci, text=' power ', fg='white', bg='grey', command=buttonpower, height=2, width=8) . grid(row=7, column=2)

    button_modulo = Button(calci, text='floor \n division', fg='white', bg='grey', command=buttonfloor, height=2, width=8) . grid(row=8, column=0)

    button_binary = Button(calci, text=' bin ', fg='white', bg='grey', command=buttonbin, height=2, width=8) . grid(row=8, column=1)

    button_octal = Button(calci, text=' oct ', fg='white', bg='grey', command=buttonoct, height=2, width=8) . grid(row=8, column=2)

    button_hexa = Button(calci, text=' hex ', fg='white', bg='grey', command=buttonhex, height=2, width=8) . grid(row=9, column=0)

    button_sqroot = Button(calci, text=' sq \n root ', fg='white', bg='grey', command=buttonsqroot, height=2, width=8) . grid(row=9, column=1)

    button_factorial = Button(calci, text=' fact ', fg='white', bg='grey', command=buttonfact, height=2, width=8) . grid(row=9, column=2)

    button_sin = Button(calci, text=' sin ', fg='white', bg='grey', command=buttonsin, height=2, width=8) . grid(row=10, column=0)

    button_cos = Button(calci, text=' cos ', fg='white', bg='grey', command=buttoncos, height=2, width=8) . grid(row=10, column=1)

    button_tan = Button(calci, text=' tan ', fg='white', bg='grey', command=buttontan, height=2, width=8) . grid(row=10, column=2)

    button_gcd = Button(calci, text=' gcd ', fg='white', bg='grey', command=buttongcd, height=2, width=8) . grid(row=11, column=0)

    button_comma = Button(calci, text=' , ', fg='white', bg='darkblue', command=buttoncomma, height=2, width=8) . grid(row=11, column=1)

    button_exponential = Button(calci, text=' exp ', fg='white', bg='grey', command=buttonexp, height=2, width=8) . grid(row=11, column=2)

    button_clear = Button(calci, text=' clear ', fg='white', bg='darkblue', command=buttonclear, height=2, width=8) . grid(row=5, column=2)

    button_equals = Button(calci, text=' = ', fg='white', bg='green', command=buttonequal, height=2, width=8) . grid(row=6, column=4)



    # start the GUI
    calci.mainloop()
