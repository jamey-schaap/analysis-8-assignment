import tkinter as tk
from controllers.login import login

class InvalidLoginPage(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    usernameLabel = tk.Label(self, text="User Name").grid(row=0, column=0)
    username = tk.StringVar()
    usernameEntry = tk.Entry(self, textvariable=username).grid(row=0, column=1)  

    passwordLabel = tk.Label(self, text="Password").grid(row=1, column=0)  
    password = tk.StringVar()
    passwordEntry = tk.Entry(self, textvariable=password, show='*').grid(row=1, column=1)  
    
    loginButton = tk.Button(self, text="Login", 
                        command=lambda: 
                          controller.show_frame("MainMenuPage") if login(username.get(), password.get()) 
                          else None
                        ).grid(row=4, column=0) 
    
    invalidCredentialLabel = tk.Label(self, text="Invalid login credentials", fg="#FF0000").grid(row=3, column=1)
    # if valid login && switch frame
    # else show error message
      