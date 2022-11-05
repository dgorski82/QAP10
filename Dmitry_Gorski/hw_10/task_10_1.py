class Flowers:

    def __init__(self, name: str, freshness: (int, float), color: str, stem_length: (int, float),
                 price: (int, float), life_time: (int, float)):
        """
        Args:
            name: flower name
            freshness: freshness (hour)
            color: flower color
            stem_length: flower stem_length (sm)
            price: price (у.е)
            life_time: flower life time (hour)
        """
        self.name = name
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.life_time = life_time


class Bouquet:

    def __init__(self):
        self.flowers, self.total_price = list(), list()
        self.bouquet_life_time_lst, self.bouquet_freshness_time = list(), list()

    def add_to_bouquet(self, *args):

        for flower in args:
            assert flower.freshness < flower.life_time, f'The flower {flower.name} is not fresh \
            and cannot be added to the bouquet'
            assert flower.stem_length > 0, 'The positive length of the flower stem must be specified'
            assert flower.price >= 0, 'The cost of the flower must be within [0, ...)'
            self.flowers.append(flower)
            self.bouquet_freshness_time.append(flower.freshness)
            self.total_price.append(flower.price)
            self.bouquet_life_time_lst.append(flower.life_time)

    @property
    def bouquet_price(self):
        return f'Cost of the bouquet : {sum(self.total_price)} у.е'

    @property
    def bouquet_life_time(self):
        life_time = []
        for idx, val in enumerate(self.bouquet_life_time_lst):
            life_time.append(val - self.bouquet_freshness_time[idx])
        return f'Bouquet life time : {round(sum(life_time) / len(life_time), 2)} hour'

    def check_if_exist(self, flower_name):
        for flower in self.flowers:
            if flower_name == flower.name:
                return True
            return False

    def find_in_bouquet_by_param(self, **kwargs):
        for flower in self.flowers:
            if all([getattr(flower, k) == v for k, v in kwargs.items()]):
                return f'Found this flower in a bouquet : {getattr(flower, "name")}'
            return 'Flower with installed params not in a bouquet'

    def sort_bouquet_by_param(self, param):
        for flower in self.flowers:
            if hasattr(flower, param):
                return sorted((getattr(flower, param), flower.name) for flower in self.flowers)


flower_1 = Flowers('Rose', 2, 'Red', 120, 10, 7)
flower_2 = Flowers('Tulip', 1, 'Yellow', 35, 2, 5)
flower_3 = Flowers('Chamomile', 3, 'White', 15, .3, 4)

bouquet = Bouquet()
bouquet.add_to_bouquet(flower_1, flower_2, flower_3)

print(bouquet.bouquet_price)
print(bouquet.bouquet_life_time)
print(bouquet.check_if_exist('Buttercup'))
print(bouquet.check_if_exist('Rose'))
print(bouquet.find_in_bouquet_by_param(stem_length=120, color='Red'))
print(bouquet.find_in_bouquet_by_param(stem_length=120, color='Red', name='Buttercup'))
print(bouquet.sort_bouquet_by_param('price'))
