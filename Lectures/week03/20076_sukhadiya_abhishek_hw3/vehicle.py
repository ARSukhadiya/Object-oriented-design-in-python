from abc import ABC, abstractmethod
from enum import Enum

class FeatureType(Enum):
    ENHANCED_SAFETY = 3000
    SECURITY = 1000
    ENTERTAINMENT_SYSTEM = 2000 
    SUNROOF = 2500

class Feature:
    def __init__(self, feature_type: FeatureType) -> None:
        self.__feature_type: FeatureType = feature_type
        self.__price: float = feature_type.value
    
    def __str__(self) -> str:
        return f"Feature_type: {self.__feature_type}, Price: {self.__price}"

    def display(self) -> None:
        print(self)


class Vehicle(ABC):
    def __init__(self, model, base_price, color, model_yr) -> None:
        self._model: str = model
        self._base_price: int = base_price
        self._color: str = color
        self._model_yr: int = model_yr
        self._features: list[FeatureType] = []
    
    def __str__(self) -> str:
        output = f"Model: {self._model}, Base_price: {self._base_price}, Color: {self._color}, Model_yr: {self._model_yr}, \n"
        return output

    def display(self) -> None:
        pass

    def convert_to_list(self) -> list[str]:
        lst = []
        lst.append(self._model)
        lst.append(self._base_price)
        lst.append(self._color)
        lst.append(self._model_yr)
        lst.append(self._features)
        return lst


class Sedan(Vehicle):
    def __init__(self, model, color, model_yr, base_price=30000) -> None:
        super().__init__(model=model, base_price=base_price, color=color, model_yr=model_yr)

    def __str__(self) -> str:
        output = f"Model: {self._model}, Base_price: {self._base_price}, Color: {self._color}, Model_yr: {self._model_yr}, \n"
        return output

    def display(self) -> None:
        print(self)


class Truck(Vehicle):
    def __init__(self, model, color, model_yr, cargo_bed_size, base_price=35000) -> None:
        super().__init__(model=model, base_price=base_price, color=color, model_yr=model_yr)
        self.__cargo_bed_size: str = cargo_bed_size

    def __str__(self) -> str:
        output = f"Model: {self._model}, Base_price: {self._base_price}, Color: {self._color}, Model_yr: {self._model_yr}"
        output += f"Cargo Bed Size: {self.__cargo_bed_size}"
        return output

    def display(self) -> None:
        print(self)


class SUV(Vehicle):
    def __init__(self, model, color, model_yr, roof_rack_type, base_price=40000) -> None:
        super().__init__(model=model, base_price=base_price, color=color, model_yr=model_yr)
        self.__roof_rack_type: str = roof_rack_type

    def __str__(self) -> str:
        output = f"Model: {self._model}, Base_price: {self._base_price}, Color: {self._color}, Model_yr: {self._model_yr}\n"
        output += f"Roof Rack Type: {self.__roof_rack_type}"
        return output

    def display(self) -> None:
        print(self)


    
class Minivan(Vehicle):
    def __init__(self, model, color, model_yr, base_price=45000) -> None:
        super().__init__(model=model, base_price=base_price, color=color, model_yr=model_yr, )

    def __str__(self) -> str:
        output = f"Model: {self._model}, Base_price: {self._base_price}, Color: {self._color}, Model_yr: {self._model_yr}\n"
        for feature in self._features:
            output += '\t' + feature
        return output

    def display(self) -> None:
        print(self)

