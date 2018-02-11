#Author: Alankrit Srivastava
#Date:11/02/2018
#Status:Incomplete

from tkinter import *
from sentimentAnalysis import SentimentAnalyzer

# function takes the hashtag as an input and sends it forward for analyzing
def Analyzer(s):
    analyze = SentimentAnalyzer(s)
    analyze.authenticate()
    analyze.calculatePolarity()
    analyze.generateGraph()
# extracting the text from the input box and passing it to the Analyzer function
def getText():
    if(text.get()!=''):
        s=text.get().lower()
        Analyzer(s)

root = Tk() #initializing the tkinter object

root.geometry("320x120+540+240") #setting the size of window
root.title("Twitter Sentimental Analysis") #providing the title of window
root.resizable(0,0) #disabling the resize option

label = Label(root,text="Enter #tag")
text = Entry(root)
button = Button(root,text="Analyze",command=lambda:getText())
#command parameter is handling the event with the button on clicking the button the getText function is called
label.pack(pady=10) #packing the label widget in the window
text.pack(fill=X,pady=2.5) #packing the entry box in the window
button.pack(pady=2.5) #packing the button in the window
root.mainloop() #Starting up the window