from models.user_model import user_data 
from views.user_view import render_user 
 
def show_user(): 
    render_user(user_data) 
