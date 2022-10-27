from random import choice
from user import User


FIRST_NAME = ['Ali', 'Reza', 'Mahdi']
LAST_NAME = ['Alizade', 'Rezazade', 'Mahdizade']
MOBILES = ['09123456789', '09191234567', '09361234567',
           '09381234567', '09969876543']

if __name__ == '__main__':
    for mobile in MOBILES:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    for user in User.object_list:
        print(f"{user.id}\t {user.fullname}")