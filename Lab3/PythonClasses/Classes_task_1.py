#Task 1
class Text:
    def __init__(self, text):
        self.text = text
    
    def getstring(self):
        self.text = input("input the text:")
    
    def printstring(self):
        print(self.text.upper())

txt = Text("") 
txt.getstring()
txt.printstring()