from random import choice
from estate import Apartment, House, Store
from advertisment import ApartmentSell
from real_state.advertisment import HouseSell, ApartmentRent, HouseRent
from user import User
from region import Region

FIRST_NAME = ['Ali', 'Reza', 'Mahdi']
LAST_NAME = ['Alizade', 'Rezazade', 'Mahdizade']
MOBILES = ['09123456789', '09191234567', '09361234567',
           '09381234567', '09969876543']


def create_samples():
    for mobile in MOBILES:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

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

    store1 = Store(
        user=User.object_list[-1],
        area=30,
        rooms_count=0,
        built_year=1390,
        region=reg1,
        address='Some text ...'
    )

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

    apartment_rent = ApartmentRent(
        user=User.object_list[0],
        area=80,
        rooms_count=2,
        built_year=1393,
        has_elevator=True,
        has_parking=True,
        floor=2,
        region=reg1,
        convertable=False,
        initial_price=100,
        monthly_price=3.5,
        address='Some text ...',
    )

    house_rent = HouseRent(
        has_yard=True,
        floors_count=1,
        user=User.object_list[2],
        area=400,
        rooms_count=6,
        built_year=1370,
        region=reg1,
        address='Some text ...',
        convertable=False,
        initial_price=130,
        monthly_price=5.5,
    )

    house_sell = HouseSell(
        has_yard=True,
        floors_count=1,
        user=User.object_list[2],
        area=400,
        rooms_count=6,
        built_year=1370,
        region=reg1,
        address='Some text ...',
        price_per_meter=10,
        discountable=True,
        convertable=False
    )

    print("#" * 20, "\t Samples created\t", "#" * 20)
