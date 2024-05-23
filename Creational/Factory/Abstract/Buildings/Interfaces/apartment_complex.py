from abc import ABC, abstractmethod


class ApartmentComplex:
    def __init__(self, apartments_number):
        self.apartments_number = apartments_number
        self.tenants_number = 0

    def add_tenant(self):
        self.tenants_number += 1

    def remove_tenant(self):
        self.tenants_number -= 1

    @abstractmethod
    def get_apartments_number(self):
        pass

    @abstractmethod
    def has_tenants(self):
        pass
