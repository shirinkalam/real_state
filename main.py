from sample import create_samples
from advertisment import ApartmentSell, ApartmentRent, HouseRent, HouseSell, \
    StoreRent, StoreSell


class Handler:
    ADVERTISEMENT_TYPES = {
        1: ApartmentSell,
        2: ApartmentRent,
        3: HouseRent,
        4: HouseSell
        # 5: StoreRent,
        # 6: StoreSell
    }

    SWITCHES = {
        'r': 'get_report',
        's': 'show_all'
    }

    def get_report(self):
        for adv in self.ADVERTISEMENT_TYPES.values():
            print(adv, adv.manager.count())

    def show_all(self):
        for adv in self.ADVERTISEMENT_TYPES.values():
            print(adv, adv.manager.count())
            for obj in adv.object_list:
                print(obj.show_detail())

    def run(self):
        print("Hello world !")
        for key in self.SWITCHES:
            print(f"Press {key} for {self.SWITCHES[key]}")
        user_input = input('Inter your choice: ')
        switch = self.SWITCHES.get(user_input, None)

        if switch is None:
            print('Invalid input')
            self.run()
        choice = getattr(self, switch, None)
        choice()
        self.run()


if __name__ == '__main__':
    create_samples()
    Handler().run()

