import json
from flask import Flask, render_template, request, jsonify   
from tkinter import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")

@app.route("/help")
def xyz():
    return render_template("InputOutput2.html")

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)


    def orent(source, side):
        storeObj = Frame(source, borderwidth = 6, bd=4, bg="orange")
        storeObj.pack(side=side, expand =YES, fill =BOTH)
        return storeObj
 
    def button(source, side, text, command=None):
        storeObj = Button(source, text=text, command=command)
        storeObj.pack(side=side, expand = YES, fill=BOTH)
        return storeObj
    
    class app(Frame):
        def __init__(self):
            Frame.__init__(self)
            self.option_add('*Font', 'arial 30 bold')
            self.pack(expand = YES, fill = BOTH)
            self.master.title('CALCULATOR')
    
            display = StringVar()
            Entry(self, relief=RIDGE, textvariable=display,justify='left', bd=30, bg="green").pack(side=TOP,expand=YES, fill=BOTH)
    
            clearButton = "Clear"
            erase = orent(self, BOTTOM)
            button(erase, LEFT, clearButton, lambda storeObj=display, q=clearButton: storeObj.set(''))
    
            for numButton in ("><!(","[]=)","789/", "456*", "123-", ".0+"):
                FunctionNum = orent(self, TOP)
                for equls in numButton:
                    button(FunctionNum, LEFT, equls, lambda storeObj=display, q=equls: storeObj.set(storeObj.get() + q))
    
            EqualButton = orent(self, TOP)

            equls = "Calculate"
            if equls == 'Calculate':
                btnequls = button(EqualButton, LEFT, equls)
                btnequls.bind('<ButtonRelease-1>', lambda e,s=self,storeObj=display: s.calc(storeObj), '+')
    
            else:
                btnequls = button(EqualButton, LEFT, equls,lambda storeObj=display, s=' %s ' % equls: storeObj.set(storeObj.get() + s))
    
        def calc(self, display):
                try:
                    display.set(eval(display.get()))
                except:
                    display.set("SYNTAX ERROR")
    
    
    if __name__=='__main__':
        app().mainloop()

    response = "<b> YOU CLOSED THE APPLICATION </b>"
    return response


if __name__ == "__main__":
	app.run()
