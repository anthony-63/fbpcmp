class Item:
    def __init__(self, item_type):
        self.item_type = item_type

class ModularItem(Item):
    def __init__(self, item_type):
        super().__init__(item_type)
        self.item_addons = []
    def add(self, item):
        self.item_addons.append(item)        

class WoodenChest(Item):
    def __init__(self): super().__init__("wooden-chest")
class IronChest(Item):
    def __init__(self): super().__init__("iron-chest")
class SteelChest(Item):
    def __init__(self): super().__init__("steel-chest")
class StorageTank(Item):
    def __init__(self): super().__init__("storage-tank")

class TransportBelt(Item):
    def __init__(self): super().__init__("transport-belt")
class FastTransportBelt(Item):
    def __init__(self): super().__init__("fast-transport-belt")
class ExpressTransportBelt(Item):
    def __init__(self): super().__init__("express-transport-belt")

class UndergroundBelt(Item):
    def __init__(self): super().__init__("underground-belt")
class FastUndergroundBelt(Item):
    def __init__(self): super().__init__("fast-underground-belt")
class ExpressUndergroundBelt(Item):
    def __init__(self): super().__init__("express-underground-belt")

class Splitter(Item):
    def __init__(self): super().__init__("splitter")
class FastSplitter(Item):
    def __init__(self): super().__init__("fast-splitter")
class ExpressSplitter(Item):
    def __init__(self): super().__init__("express-splitter")

class BurnerInserter(Item):
    def __init__(self): super().__init__("burner-inserter")
class Inserter(Item):
    def __init__(self): super().__init__("inserter")
class LongHandedInserter(Item):
    def __init__(self): super().__init__("long-handed-inserter")
class FastInserter(Item):
    def __init__(self): super().__init__("fast-inserter")
class FilterInserter(Item):
    def __init__(self): super().__init__("filter-inserter")
class StackInserter(Item):
    def __init__(self): super().__init__("stack-inserter")
class StackFilterInserter(Item):
    def __init__(self): super().__init__("stack-filter-inserter")

class SmallElectricPole(Item):
    def __init__(self): super().__init__("small-electric-pole")
class MediumElectricPole(Item):
    def __init__(self): super().__init__("medium-electric-pole")
class BigElectricPole(Item):
    def __init__(self): super().__init__("big-electric-pole")
class Substation(Item):
    def __init__(self): super().__init__("substation")
