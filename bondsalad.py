import os
import tkinter
# import tkinter.messagebox
import customtkinter

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
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="powered by bondsalad.org", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_label.grid(row=4, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="1. See Portfolio")
        self.sidebar_button_1.grid(row=0, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="2. Connect Broker")
        self.sidebar_button_2.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="3. Copy Portfolio")
        self.sidebar_button_3.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="4. Donate Now", fg_color="#FFBF00", text_color="#000000")
        self.sidebar_button_4.grid(row=3, column=0, padx=20, pady=10)

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
        self.seg_button_1.configure(values=["User Manual", "Support"])
        self.seg_button_1.set("User Manual")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
        self.textbox.insert("0.0", "function not assigned. \n\n")


if __name__ == "__main__":
    app = App()
    app.mainloop()
