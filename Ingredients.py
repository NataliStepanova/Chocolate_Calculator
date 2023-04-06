class Kakao:
    prot = 14.2
    fat = 53.5
    carb = 27.5
    ves = 100
    ccal = 648

    def set_gramm(self, ves):
        self.ves = ves
        self.fat = round(self.fat * ves / 100, 2)
        self.carb = round(self.carb * ves / 100, 2)
        self.prot = round(self.prot * ves / 100, 2)
        self.ccal = round(self.ccal * ves / 100, 2)


class Maslo(Kakao):
    prot = 0
    fat = 99.9
    carb = 0
    ves = 100
    ccal = 899


class Pudra(Kakao):
    prot = 0
    fat = 0
    carb = 99.8
    ves = 100
    ccal = 399
