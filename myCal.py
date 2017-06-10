from Tkinter import *

def frame(root, side):
    w=Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

def button(root, side, text, command=None):
    w=Button(root, bd=8,text=text, command=command)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

class  Calculator(Frame):

       def __init__(self):
           Frame.__init__(self)
           self.pack(expand=YES, fill=BOTH)
           self.master.title('Maiagogo')
   
           display=StringVar()
           Entry(self, bd=20, font=30, relief=SUNKEN, textvariable=display).pack(side=TOP, expand=YES, fill=BOTH)
           for key in ('123', '456', '789', '-0.'):
               keyF=frame(self, TOP)
               for char in key:
                  button(keyF, LEFT, char, lambda w=display, s='%s'%char: w.set(w.get()+s))
              
           opsF=frame(self, TOP)
           for char in '+-*/=':
               if char =='=':
                  btn=button(opsF,LEFT, char)
                  btn.bind('<ButtonRelease-1>', lambda e, s=self, w=display: s.calc(w), '+')
               else:
                   btn=button(opsF,LEFT, char, lambda w=display, c=char: w.set(w.get()+''+c))
           clearF=frame(self, BOTTOM)
           button(clearF, LEFT, 'Clear', lambda w=display: w.set(''))
       def calc(self, display):
         try:
            display.set(eval(display.get()))
         except ValueError:
            display.set("ERROR")
if __name__ == '__main__':
      Calculator().mainloop()

