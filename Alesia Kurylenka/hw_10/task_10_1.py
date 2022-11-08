class Flowers:

    def __init__(self, name: str, freshness_days: (int, float), color: str, stem_length: (int, float),
                 price: (int, float)):

        self.name = name
        self.freshness_days = freshness_days
        self.color = color
        self.stem_length = stem_length
        self.price = price


class Rose(Flowers):
    pass


class Tulip(Flowers):
    pass


class Camomile(Flowers):
    pass


class Bouquet:

    def __init__(self, bouquet_name):
        self.bouquet_name = bouquet_name
        self.flowers_in_bouquet = list()
        self.bouquet_price = list()
        self.bouquet_freshness = list()
        self.filtered_flowers = list()

    def add_flower_to_bouquet(self, *flowers):
        for flower in flowers:
            self.flowers_in_bouquet.append(flower)
            self.bouquet_price.append(flower.price)
            self.bouquet_freshness.append(flower.freshness_days)

    def count_freshness(self):
        self.bouquet_freshness = sum(self.bouquet_freshness) / len(self.bouquet_freshness)
        print(f"Your bouquet will be alive {self.bouquet_freshness} days")

    def count_price(self):
        self.bouquet_price = sum(self.bouquet_price)
        print(f"Your bouquet will cost: {self.bouquet_price}")

    def find_flower(self, flower):
        if flower in self.flowers_in_bouquet:
            print(f"Yes, your flower {flower.name} in bouquet")
        else:
            print("There is no flower in bouquet")

    def sort_flowers(self, param):
        assert param in ['name', 'freshness_days', 'color', 'stem_length', 'price'], "There is no such param"
        sorted_bouquet = sorted(self.flowers_in_bouquet, key=lambda flower: getattr(flower, param))
        sorted_bouquet_result = []
        [sorted_bouquet_result.append(flower.name) for flower in sorted_bouquet]
        print(f"Your sorted bouquet: {sorted_bouquet_result}")

    def search_for_flowers_in_bouquet(self, param, value):
        assert param in ['name', 'freshness_days', 'color', 'stem_length', 'price'], "There is no such param"
        searched_params = list()
        for flower in self.flowers_in_bouquet:
            if param == 'name' and value == getattr(flower, 'name'):
                searched_params.append(flower.name)
            elif param == 'freshness_days' and value == getattr(flower, 'freshness_days'):
                searched_params.append(flower.freshness_days)
            elif param == 'color' and value == getattr(flower, 'color'):
                searched_params.append(flower.color)
            elif param == 'stem_length' and value == getattr(flower, 'stem_length'):
                searched_params.append(flower.stem_length)
            elif param == 'price' and value == getattr(flower, 'price'):
                searched_params.append(flower.price)
        if len(searched_params) > 0:
            print(f"Flowers with this param {param} and value {searched_params} in your bouquet")
        else:
            print("Nothing found by your search")


rose = Rose('Rose', 1, 'Red', 10, 20)
tulip = Tulip('Tulip', 2, 'Yellow', 8, 10)
camomile = Camomile('Camomile', 3, 'White', 5, 10)

bouquet_for_mother = Bouquet("Bouquet for mothers day")
bouquet_for_mother.add_flower_to_bouquet(rose, camomile, rose, tulip)
bouquet_for_mother.count_freshness()
bouquet_for_mother.count_price()

bouquet_for_mother.find_flower(rose)
bouquet_for_mother.find_flower(tulip)

bouquet_for_mother.sort_flowers("freshness_days")

bouquet_for_mother.search_for_flowers_in_bouquet("price", 10)
