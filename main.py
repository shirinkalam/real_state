from random import choice
from estate import Apartment, House, Store
from advertisment import ApartmentSell
from user import User
from region import Region

FIRST_NAME = ['Ali', 'Reza', 'Mahdi']
LAST_NAME = ['Alizade', 'Rezazade', 'Mahdizade']
MOBILES = ['09123456789', '09191234567', '09361234567',
           '09381234567', '09969876543']

if __name__ == '__main__':
    for mobile in MOBILES:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    for user in User.object_list:
        print(f"{user.id}\t {user.fullname}")

    reg1 = Region(name='R1')
    apt1 = Apartment(
        user=User.object_list[0],
        area=80,
        rooms_count=2,
        built_year=1393,
        has_elevator=True,
        has_parking=True,
        floor=2,
        region=reg1,
        address='Some text...'
    )

    apt1.show_description()

    house1 = House(
        has_yard=True,
        floors_count=1,
        user=User.object_list[2],
        area=400,
        rooms_count=6,
        built_year=1370,
        region=reg1,
        address='Some text ...'
    )

    house1.show_description()

    store1 = Store(
        user=User.object_list[-1],
        area=30,
        rooms_count=0,
        built_year=1390,
        region=reg1,
        address='Some text ...'
    )

    store1.show_description()

    # Create advertisment
    apartment_sell = ApartmentSell(
        user=User.object_list[0],
        area=80,
        rooms_count=2,
        built_year=1393,
        has_elevator=True,
        has_parking=True,
        floor=2,
        region=reg1,
        address='Some text...',
        price_per_meter=10,
        discountable=True,
        convertable=False
    )

    apartment_sell.show_detail()
