from pages.page import Page
from controllers.login import logout
from utils.user import User

class MainMenuPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
  
  def display(self) -> None:
    super().display()
    print(
      f"Welcome {User().first_name}.\n" +
      "\n" + 
      "1: Something \n" + 
      "2: Something \n" + 
      "\n"
      "To:\n" +
      " > logout type: /lo\n" + 
      " > quit type:   /q\n" 
      )
    
    user_input = input()
    
    if user_input == "/lo":
      logout()
      self.controller.next_page = "LoginPage"
    