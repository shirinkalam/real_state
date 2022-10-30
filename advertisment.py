from abc import ABC, abstractmethod

from estate import Apartment, House, Store
from deal import Rent, Sell
from real_state.base import BaseClass


class ApartmentSell(BaseClass, Apartment, Sell):
    def show_detail(self):
        self.show_description()
        self.show_price()

    def __str__(self):
        pass


class ApartmentRent(BaseClass, Apartment, Rent):
    pass


class HouseSell(BaseClass, House, Sell):
    def show_detail(self):
        self.show_description()
        self.show_price()


class HouseRent(BaseClass, House, Rent):
    pass


class StoreSell(BaseClass, Store, Sell):
    pass


class StoreRent(BaseClass, Store, Rent):
    pass
