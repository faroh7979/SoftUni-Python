from library import Library
from user import User


class Registration:

    def add_user(self, user: User, library: Library):

        if user not in library.user_records:
            library.user_records.append(user)

        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):

        if user in library.user_records:
            library.user_records.remove(user)

        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):

        try:
            searched_user = next(filter(lambda u: u.user_id == user_id, library.user_records))
        except StopIteration:
            return f"There is no user with id = {user_id}!"

        if searched_user.username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"

        searched_user.username = new_username
        return f"Username successfully changed to: {new_username} for user id: {user_id}"

