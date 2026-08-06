class Nigiri:
    category = 'にぎり'
    top = 'ねた'
    base = 'しゃり'
    price = 100

    def show_attributes(self):
        print("top:{},base:{},category:{}".format(self.top,self.base,self.category))
        print("price:{}円".format(self.price))

n1 = Nigiri()
n1.show_attributes()

class Katsuo(Nigiri):
    top = 'かつお'
    topping = '生姜とネギ'
    price = 100

    def show_attributes(self):
        super().show_attributes()
        print('topping:{}'.format(self.topping))

k1 = Katsuo()
k1.show_attributes()
