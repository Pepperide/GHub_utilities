#
# copyright © 2022 Giuseppe Fanuli
#
# Software v1.0.0
# See README.txt for more information
#

import tkinter as tk
from PIL import ImageTk, Image
from buffer import BufferRead


transparency = 1
class PopUp(tk.Tk):
    def __init__(self, msg:str):
        """
        Args:
        - msg: the message that will be displayed on the popup
        """
        super().__init__()

        # configure the root window
        self.overrideredirect(True) # permits to override default system settings for the window appearence
        self.resizable(False, False) # deny window resize
        self.wm_attributes("-topmost", 1) # permits to show the window over all other windows
        self.geometry(self.setPosition())
        self.configure(bg="#1C1C1C") # background window color

        #Image widget
        image=Image.open("..\\data\\Ghub_logo_black1.png")
        resized_image= image.resize((30,30), Image.ANTIALIAS)
        display = ImageTk.PhotoImage(resized_image)
        im = tk.Label(self, image=display,highlightthickness=0, borderwidth=0)
        im.image = display
        im.pack(padx=10, side=tk.LEFT)

        #Label widget
        self.label = tk.Label(self, text = msg, justify=tk.CENTER, font=("Helvetica",12,"bold"),bg="#1C1C1C", fg="white")
        self.label.pack(padx=10, side=tk.LEFT)
        
        #Button
        #self.button = tk.Button(self, text="Quit", command=lambda root=self:quit(root))

        self.start()
        
    def setPosition(self, height:int=100,width:int=250, right:int=25, top:int=25):
        """
        It permits to set window position.\n
        Return the string with "widthxheigth+left_marign+top_margin" format.\n
        Args:
        - height: window's height (default 100)
        - width: window's width (default 250)
        - right: padding from right margin (default 25)
        - top: padding from the top margin (default 25)
        """
        h_screen = self.winfo_screenheight()
        w_screen = self.winfo_screenwidth()
        x = w_screen-width-right
        y = top
        geo=f"{width}x{height}+{x}+{y}"
        return geo

    def start(self):
        """
        Shows popup message window
        """
        self.transparency_gradient() # The window will gradually disappear after few seconds
        pass

    def transparency_gradient(self):
        """
        Menage the trasparency of the window.
        """
        global transparency # global transparency value
        self.attributes('-alpha',transparency) # windw's transparency color 
        
        if( transparency <= 0):
            # if the window disappear from the screen, it will be destroyed
            self.destroy()
        
        self.after(20,self.transparency_gradient) # transaction time
        transparency -= 0.01 # updating trasparency value

            

if __name__ == "__main__":
    last =""
    while(1):
        buff = BufferRead()
        msg = buff.readBuffer()
        if(msg!=last and msg!=""):
            # if statement permits to avaiod that multiple message will be displayed
            last=msg
            transparency=1 # Set again teh trasparency value
            app = PopUp(msg)
            app.mainloop() # Permits to show up the popup