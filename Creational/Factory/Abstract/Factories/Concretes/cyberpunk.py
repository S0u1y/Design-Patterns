from Creational.Factory.Abstract.Buildings.Concretes.cyberpunk import CyberPunkApartmentComplex, CyberPunkFamilyHouse
from Creational.Factory.Abstract.Factories.Interface.building_factory import BuildingFactory


class CyberPunkBuildingFactory(BuildingFactory):
    def create_apartment_complex(self, n_tenants) -> CyberPunkApartmentComplex:
        return CyberPunkApartmentComplex(n_tenants)

    def create_family_house(self) -> CyberPunkFamilyHouse:
        return CyberPunkFamilyHouse()
