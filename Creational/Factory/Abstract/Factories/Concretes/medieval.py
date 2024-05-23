from Creational.Factory.Abstract.Buildings.Concretes.medieval import MedievalApartmentComplex, MedievalFamilyHouse
from Creational.Factory.Abstract.Factories.Interface.building_factory import BuildingFactory


class MedievalBuildingFactory(BuildingFactory):
    def create_apartment_complex(self, n_tenants) -> MedievalApartmentComplex:
        return MedievalApartmentComplex(n_tenants)

    def create_family_house(self) -> MedievalFamilyHouse:
        return MedievalFamilyHouse()
