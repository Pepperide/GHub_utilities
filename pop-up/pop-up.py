#
# copyright © 2022 Giuseppe Fanuli3
#
# See README.txt for more information
#

import tkinter as tk
from PIL import ImageTk, Image
from buffer import BufferRead


transparency = 1
class PopUp(tk.Tk):
    def __init__(self,msg):
        super().__init__()

        #configure the root window
        #self.update_idletasks()
        self.overrideredirect(True)
        self.resizable(False, False)
        self.wm_attributes("-topmost", 1)
        self.geometry(self.setPosition())
        self.configure(bg="#1C1C1C")
        
        

        #Image
        image=Image.open("..\\data\\Ghub_logo_black1.png")
        resized_image= image.resize((30,30), Image.ANTIALIAS)
        display = ImageTk.PhotoImage(resized_image)
        im = tk.Label(self, image=display,highlightthickness=0, borderwidth=0)
        im.image = display
        im.pack(padx=10, side=tk.LEFT)

        #Label  
        self.label = tk.Label(self, text = msg, justify=tk.CENTER, font=("Helvetica",12,"bold"),bg="#1C1C1C", fg="white")
        self.label.pack(padx=10, side=tk.LEFT)
        
        #Button
        self.button = tk.Button(self, text="Quit", command=lambda root=self:quit(root))
        #self.button.pack(padx=10, side=tk.LEFT)

        self.start()
        
    def setPosition(self, height=100,width=250, right=25, top=25):
        h_screen = self.winfo_screenheight()
        w_screen = self.winfo_screenwidth()
        x = w_screen-width-right
        y = top
        geo=f"{width}x{height}+{x}+{y}"
        return geo

    def start(self):
        self.transparency_gradient()
        pass

    def transparency_gradient(self):
        global transparency
        self.attributes('-alpha',transparency)
        
        if( transparency <= 0):
            self.destroy()
        
        self.after(20,self.transparency_gradient)
        transparency -= 0.01

            

if __name__ == "__main__":
    last =""
    while(1):
        buff = BufferRead()
        msg = buff.readBuffer()
        if(msg!=last and msg!=""):
            last=msg
            transparency=1
            app = PopUp(msg)
            app.mainloop()
