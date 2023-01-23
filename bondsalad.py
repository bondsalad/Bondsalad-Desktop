import os
import tkinter
import customtkinter

import asyncio
from ib_insync import IB, util


util.patchAsyncio()

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Bondsalad")
        self.geometry(f"{700}x{430}")
        customtkinter.set_widget_scaling(1.1)
        
        # configure icon
        thisdir = os.path.dirname(__file__)
        rcfile = os.path.join(thisdir,'icon.png')
        self.iconphoto(False, tkinter.PhotoImage(file=rcfile))
            
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(3, weight=1)
        
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="See Portfolio")
        self.sidebar_button_1.grid(row=0, column=0, padx=20, pady=10)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Degiro", "Interactive Brokers"])
        self.optionmenu_1.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.copy_portfolio, text="Copy Portfolio")
        self.sidebar_button_3.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Donate Now", fg_color="#FFBF00", text_color="#000000")
        self.sidebar_button_4.grid(row=3, column=0, padx=20, pady=10)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="powered by bondsalad.org", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_label.grid(row=4, column=0, padx=20, pady=(20, 10))

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self)  # (self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 10), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0", "Welcome to the Bondsalad desktop app! \n\n \n\nIn this box you will see the output of your interactions and \n\nthe solution to the issues you may encounter. \n\n \n\nFor further information please visit the User Guide by \n\nclicking the button below.")
        
        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, columnspan=2, padx=(0, 0), pady=(40, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        
        self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 0), sticky="ew")
        
        # default values 
        self.seg_button_1.configure(values=["User Guide", "Support"])
        self.seg_button_1.set("User Guide")
        self.optionmenu_1.set("Select Broker")



    def sidebar_button_event(self):
        # print("sidebar_button click")
        self.textbox.insert("0.0", "function not assigned. \n\n")

    
    def copy_portfolio(self):
        """ given selected broker, performs connection test and
            executes portfolio orders"""
        # broker selection condition
        if self.optionmenu_1.get() == "Interactive Brokers":
            # interactive brokers connection test
            try:
                self.ib = IB().connect('127.0.0.1', 4002, 1)
                IB().sleep(1.5)

                self.connection = self.ib.isConnected()
                print(self.connection)
                type(self.connection)

                if self.connection == True:
                    self.textbox.insert("0.0", "*** connected! ***\n\n \n\n")

            except:
                self.textbox.insert("0.0", "Either you are already connected (in that case ibgateway shows a client1 connection) or something didn't work. In that case proceed this way:\n\nInstall and/or open IBGateway\n\nGo To Configuration->Settings->API->Settings\n\nUncheck -Read Only API-\n\nCheck that socket port matches 4002 otherwise change it\n\nClick on -Connect Broker- once again and wait for the output. \n\n \n\n")
            # interactive brokers execution
            #############################
        
        elif self.optionmenu_1.get() == "Degiro":
            # degiro connection test
            # degiro execution
            self.textbox.insert("0.0", "Degiro functions not coded yet. \n\n \n\n")
            #############################
        
        else:
            # broker not selected
            self.textbox.insert("0.0", "Broker not selected yet. \n\nPlease select a broker. \n\n \n\n")


if __name__ == "__main__":
    app = App()
    app.mainloop()
