# generic imports
import os
import tkinter
import customtkinter
import webbrowser
# Interactive Brokers imports
import asyncio
from ib_insync import IB, util
# Degiro imports
from degiro_connector.trading.api import API as TradingAPI
from degiro_connector.trading.models.trading_pb2 import Credentials


util.patchAsyncio()

customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Bondsalad")
        self.geometry(f"{900}x{600}")
        customtkinter.set_widget_scaling(1.1)

        # configure icon
        thisdir = os.path.dirname(__file__)
        rcfile = os.path.join(thisdir, 'icon.png')
        self.iconphoto(False, tkinter.PhotoImage(file=rcfile))

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(
            self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(7, weight=1)

        # SEE PORTFOLIO
        self.sidebar_button_1 = customtkinter.CTkButton(
            self.sidebar_frame, command=self.portfolio_web, text="1. See Portfolio")
        self.sidebar_button_1.grid(row=0, column=0, padx=20, pady=10)

        # SELECT BROKER
        self.optionmenu_1 = customtkinter.CTkOptionMenu(
            self.sidebar_frame, values=["Degiro", "Interactive Brokers"])
        self.optionmenu_1.grid(row=1, column=0, padx=20, pady=10)

        # DEGIRO LOGIN ENTRY
        self.login_label = customtkinter.CTkLabel(self.sidebar_frame, text="Only required if executing with Degiro",
                                                  font=customtkinter.CTkFont(size=12))
        self.login_label.grid(row=2, column=0, padx=20, pady=10)
        self.username_entry = customtkinter.CTkEntry(
            self.sidebar_frame, width=150, placeholder_text="username")
        self.username_entry.grid(row=3, column=0, padx=20, pady=10)
        self.password_entry = customtkinter.CTkEntry(
            self.sidebar_frame, width=150, show="*", placeholder_text="password")
        self.password_entry.grid(row=4, column=0, padx=20, pady=10)
        self.otp_entry = customtkinter.CTkEntry(
            self.sidebar_frame, width=150, placeholder_text="otp (if enabled)")
        self.otp_entry.grid(row=5, column=0, padx=20, pady=10)

        # COPY PORTFOLIO
        self.sidebar_button_3 = customtkinter.CTkButton(
            self.sidebar_frame, command=self.copy_portfolio, text="3. Copy Portfolio")
        self.sidebar_button_3.grid(row=6, column=0, padx=20, pady=10)

        # DONATE
        self.sidebar_button_4 = customtkinter.CTkButton(
            self.sidebar_frame, command=self.sidebar_button_event, text="Donate Now", fg_color="#FFBF00", text_color="#000000")
        self.sidebar_button_4.grid(row=7, column=0, padx=20, pady=10)

        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="powered by bondsalad.org", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_label.grid(row=8, column=0, padx=20, pady=(20, 10))

        # create textbox
        self.textbox = customtkinter.CTkTextbox(
            self, width=200, height=400)  # (self, width=250)
        self.textbox.grid(row=0, column=1, padx=(
            20, 10), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0", "Welcome to the Bondsalad desktop app! \n\n \n\nIn this box you will see the output of your interactions and \n\nthe solution to the issues you may encounter. \n\n \n\nFor further information please visit the User Guide by \n\nclicking the button below.")

        # creating a "below textbox" frame
        self.below_textbox_frame = customtkinter.CTkFrame(
            self, fg_color="transparent")
        self.below_textbox_frame.grid(
            row=1, column=1, columnspan=2, padx=(0, 0), pady=(40, 0), sticky="nsew")
        self.below_textbox_frame.grid_columnconfigure(0, weight=1)
        self.below_textbox_frame.grid_rowconfigure(4, weight=1)

        self.seg_button_1 = customtkinter.CTkSegmentedButton(
            self.below_textbox_frame)
        self.seg_button_1.grid(row=0, column=0, padx=(
            20, 10), pady=(10, 0), sticky="ew")

        # default values
        self.seg_button_1.configure(values=["User Guide", "Support"])
        self.seg_button_1.set("User Guide")
        self.optionmenu_1.set("2. Select Broker")

    ##### FUNCTIONS #####

    def sidebar_button_event(self):
        self.textbox.insert("0.0", "Function not assigned. \n\n \n\n")

    def portfolio_web(self):
        webbrowser.open("bondsalad.org/#portfolio", new=1)
        self.textbox.insert(
            "0.0", "Opening portfolio selection in a browser page. \n\n \n\n")

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
                # print(self.connection)
                # type(self.connection)

                if self.connection == True:
                    self.textbox.insert("0.0", "*** connected! ***\n\n \n\n")

            except:
                self.textbox.insert("0.0", "Either you are already connected (in that case ibgateway shows a client1 connection) or something didn't work. In that case proceed this way:\n\nInstall and/or open IBGateway\n\nGo To Configuration->Settings->API->Settings\n\nUncheck -Read Only API-\n\nCheck that socket port matches 4002 otherwise change it\n\nClick on -Connect Broker- once again and wait for the output. \n\n \n\n")
            # interactive brokers execution
            # TODO: read portfolio.json as list of tuples,
            # close position non contemplated if any,
            # get cash available in account,
            # perform "share to buy" calculation leaving some cash as a fee cushion
            # perform buy orders
            #####################################

        elif self.optionmenu_1.get() == "Degiro":
            # degiro connection test
            try:
                credentials = Credentials(
                    int_account=None,
                    username=self.username_entry.get(),
                    password=self.password_entry.get(),
                    totp_secret_key=None,
                    one_time_password=int(self.otp_entry.get()),
                )

                # SETUP TRADING API
                self.trading_api = TradingAPI(credentials=credentials)

                # CONNECT
                self.trading_api.connect()

                self.textbox.insert("0.0", "*** connected!***\n\n \n\n")
            except:
                self.textbox.insert(
                    "0.0", "Something Went Wrong with Degiro connection \n\n \n\n")

            # degiro execution
            # TODO: same as for ib
            #############################

        else:
            # broker not selected
            self.textbox.insert(
                "0.0", "Broker not selected yet. \n\nPlease select a broker. \n\n \n\n")


if __name__ == "__main__":
    app = App()
    app.mainloop()
