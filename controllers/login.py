from typing import Tuple
import utils.database as database
from utils.encryption import decrypt, encrypt
from utils.user import User

login_attempts = 0

def login(app, username: str, password: str ) -> bool:
  global login_attempts
  
  (is_valid, user) = __validate_login(username, password)
  if (is_valid):
    app.user = User(user[0], user[1], decrypt(user[2]), user[4], user[5])
    login_attempts = 0
    return True
  
  login_attempts += 1
  return False

def __validate_login(username: str, password: str):
  users = database.execute_query("SELECT * FROM users WHERE username=? AND password=?", encrypt(username), encrypt(password))
  
  if len(users) == 0:
    return (False, ())
  if len(users) > 1:
    raise ("")
  
  user = users[0]
  return (True, user)

def logout(app):
  app.user = None