class Cylinder:
	pi = 3.14
    
    def __init__(self,height=1,radius=1):

        self.height=height
        self.radius=radius

 
    def volume(self):

        return self.pi*self.radius**2*self.height
    
    def surface_area(self):
        return (2*self.pi*self.radius*self.height)+(2*self.pi*self.radius**2)




class Line:
    
    def __init__(self,coor1,coor2):
    	
        self.coor1=coor1
        self.coor2=coor2
       
    
    def distance(self):

    	(x1,y1)=self.coor1
        (x2,y2)=self.coor2
    	return ((y2-y1)**2+(x2-x1)**2)**0.5

        
    
    def slope(self):
    	(x1,y1)=self.coor1
        (x2,y2)=self.coor2
        return (y2-y1)%(x2-x1)