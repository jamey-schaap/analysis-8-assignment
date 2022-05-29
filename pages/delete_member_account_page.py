from getpass import getpass
from pages.page import Page
import utils.validation as validation
import utils.database as database
import utils.logger as logger
from utils.encryption import encrypt

class DeleteMemberAccountPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
    
  def display(self) -> None:
    super().display()
    
    print("Please enter the membership id of the member you want to delete.")
    membership_id = validation.get_user_input("> Enter the membership id: ", [validation.is_number(), validation.check_length(10, 10)])
    
    members = database.execute_query("SELECT * FROM members WHERE membership_id=?", membership_id)
    
    if len(members) == 0:
        print(f"\nNo member exists with the specified membership id.")
    else:
        database.execute_query("DELETE FROM members WHERE membership_id=?", membership_id)        
        logger.log("Member deletion", f"The member with membership id {membership_id} has been deleted", self.controller.user, False)

        print(f"The member with the membership id '{membership_id}' has been deleted")
    
    getpass("Press enter to continue to the main menu...")
    self.controller.next_page = "MainMenuPage"
    
   