# travidux

class Shape:
    def area(self,*args):
        if len(args)==1:
            r=args[0]
            print("areaa of circle=",3.14*(r**2))
        elif len(args)==2:
            l=args[0]
            b=args[1]
            print("area of rectancgle=",l*b)
        elif len(args)==3:
            l=args[0]
            b=args[1]
            h=args[2]
            print("area of cuboid=",l*b*h)
shp=Shape()
shp.area(5,4)