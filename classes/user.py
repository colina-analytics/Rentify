from flask_login import UserMixin

from myutils import get_user_data_by_id

class User(UserMixin):
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']


    @staticmethod
    def get(user_id):
        user_data = get_user_data_by_id(user_id)  # Fetch user data by ID from the database
        if user_data:
            return User(user_data)
        return None
