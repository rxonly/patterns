from abc import ABC, abstractmethod

class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass

class Table(ABC):
    @abstractmethod
    def use(self):
        pass

class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a modern chair"

class ModernTable(Table):
    def use(self):
        return "Using a modern table"

class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on a Victorian chair"

class VictorianTable(Table):
    def use(self):
        return "Using a Victorian table"

class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_table(self) -> Table:
        return ModernTable()

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_table(self) -> Table:
        return VictorianTable()

def build_room(factory: FurnitureFactory):
    chair = factory.create_chair()
    table = factory.create_table()
    print(chair.sit_on())
    print(table.use())

if __name__ == "__main__":
    print("Modern Style:")
    build_room(ModernFurnitureFactory())
    print("\nVictorian Style:")
    build_room(VictorianFurnitureFactory())
