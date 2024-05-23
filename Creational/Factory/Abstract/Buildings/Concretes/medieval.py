from Creational.Factory.Abstract.Buildings.Interfaces.family_house import FamilyHouse
from Creational.Factory.Abstract.Buildings.Interfaces.apartment_complex import ApartmentComplex


class MedievalFamilyHouse(FamilyHouse):
    def pet_dog(self):
        print("The dog barks happily")

    def has_garden(self):
        return True


class MedievalApartmentComplex(ApartmentComplex):

    def add_tenant(self):
        if self.tenants_number < 5:
            super(self).add_tenant()

    def get_apartments_number(self):
        return self.apartments_number

    def has_tenants(self):
        return True if self.tenants_number > 0 else False
