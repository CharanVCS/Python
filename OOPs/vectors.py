#code for vectors in maths
class Vector2d:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    
    def print2d(self):
        print(f'{self.i}i + {self.j}j')
        
class Vector3d(Vector2d):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
        
    def print3d(self):
        print(f'{self.i}i + {self.j}j + {self.k}k')

v2=Vector2d(2,5)
v3=Vector3d(7,3,2)

v2.print2d()
v3.print3d()
