from Creational.Factory.Abstract.Buildings.Interfaces.family_house import FamilyHouse
from Creational.Factory.Abstract.Buildings.Interfaces.apartment_complex import ApartmentComplex


class CyberPunkFamilyHouse(FamilyHouse):
    def pet_dog(self):
        print("The dog plays music")

    def has_garden(self):
        return False


class CyberPunkApartmentComplex(ApartmentComplex):
    def get_apartments_number(self):
        return self.apartments_number

    def has_tenants(self):
        return True if self.tenants_number > 0 else False
