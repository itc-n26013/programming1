class cylinder:

    pi=3.14

    def __init__(self,radius=1,height=1):
        self.radius = float(radius)
        self.height = float(height)

    def clac_base_area(self):
        pi = cylinder.pi
        r = self.radius
        return pi * r * r

    def clac_side_area(self):
        pi = cylinder.pi
        r = self.radius
        h = self.height
        return 2 * pi * r *h

    def clac_surface_area(self):
        c = self.clac_base_area()
        s = self.clac_side_area()
        return 2 * c + s

    def clac_volume(self):
        c = self.clac_base_area()
        h = self.height
        return c * h

    def show_results(self):
        r = self.radius
        h = self.height
        S = self.clac_surface_area()
        V = self.clac_volume()
        print('半径:{},高さ:{},表面積:{},体積:{}'.format(r,h,S,V))

c1 = cylinder()
c1.show_results()

c2 = cylinder(1., 3.)
c2.show_results()

c3 = cylinder(2., 1.)
c3.show_results()

c4 = cylinder(2., 3.)
c4.show_results()
