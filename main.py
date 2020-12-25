"""
Arbolito lindo de navidad...
"""

__author__ = "FelipedelosH"

from tkinter import *
import random

class Software:
    def __init__(self):
        self.screem = Tk()
        self.canvas = Canvas(self.screem, bg="blue", width=640, height=480)
        self.arbolTXT = Text(self.canvas, bg="black", fg="green", width=76, height=28)

        self.configureView()

    def configureView(self):
        """
        Show and configure elements in screem
        show three paint line to line
        """
        self.screem.title("Feliz navidad los AMO a todos!!!!")
        self.screem.geometry("640x480")
        self.canvas.place(x=0, y=0)
        self.arbolTXT.place(x=10, y=10)

        limit = 40 # to paint NOTHING 
        character = 1 # to paint a character  

        arbol = "\n\n" # The three
        line = " " # Create a layer to three

        # Create a leaves
        for i in range(0, 16):
            line = " "*limit

            for j in range(0, character):
                line = line + self.getRamdomCharater()

            line = line + "\n"
                
            arbol = arbol + line

            # Rules
            limit = limit - 1
            character = character + 2


        line = " "*37
        aux = ""

        for k in range(0, 8):
            aux = aux+self.getRamdomCharater()

        line = line + aux + "\n"
        line = line*8

        arbol = arbol + line

    
        self.drawThreeInScreem(arbol)

        self.screem.mainloop()


    def getRamdomCharater(self):
        chars = ".*@#&!¡/%"
    
        return chars[random.randint(0, len(chars)-1)]

    def drawThreeInScreem(self, three):
        self.arbolTXT.insert(END, three)





s = Software()