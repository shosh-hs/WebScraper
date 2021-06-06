class Gpu:
    def __init__(self, limit, name, offer1, offer2):
        print("gpu const")
        self.limit = limit
        self.name = name
        self.offer1 = offer1
        self.offer2 = offer2


class Offer():
    def __init__(self, zustand, price):
        print("offer const")
        self.zustand = zustand
        self.price= price


offer1 = Offer("neu", 1300)
offer2 = Offer("neu", 1300)
rtx = Gpu(700, "rtx3070", offer1, offer2)

print(rtx.offer.price)




