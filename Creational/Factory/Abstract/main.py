from Creational.Factory.Abstract.Factories.Interface.building_factory import BuildingFactory
from Creational.Factory.Abstract.Factories.Concretes.medieval import MedievalBuildingFactory
from Creational.Factory.Abstract.Factories.Concretes.cyberpunk import CyberPunkBuildingFactory


theme = "medieval"

if __name__ == "__main__":
    factory: BuildingFactory = MedievalBuildingFactory() if theme is "medieval" else CyberPunkBuildingFactory()

    first_house = factory.create_family_house()

    print(type(first_house))

    first_house.pet_dog()

