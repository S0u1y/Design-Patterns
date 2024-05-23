from Creational.Factory.Abstract.Buildings.Interfaces.family_house import FamilyHouse
from Creational.Factory.Abstract.Buildings.Interfaces.apartment_complex import ApartmentComplex


class BuildingFactory:
    def create_apartment_complex(self, n_tenants) -> ApartmentComplex:
        pass

    def create_family_house(self) -> FamilyHouse:
        pass
