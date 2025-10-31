from Address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address        # объект Address (куда отправляем)
        self.from_address = from_address    # объект Address (откуда отправляем)
        self.cost = cost                    # число (стоимость)
        self.track = track                  # строка (трек-номер)
