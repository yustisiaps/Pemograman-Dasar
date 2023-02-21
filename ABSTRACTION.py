class orang:

    def __init__(self, nama, asal):
        self.nama= nama
        self.asal = asal

    def perkenalan (self):
        print(f'perkenalkan nama saya {self.nama} dari {self.asal}')

dhandy = orang('dhandy', 'bandung')
dhandy.perkenalan()



