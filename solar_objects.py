class Star:
        """Описание звезды. Её физические свойства (радиус, цвет, масса и.т.д)"""
        
        def __init__(self):
                self.type = "star"   
                self.R = 5           
                self.color = "yellow"   
                self.m = 1.0         
                self.x = 0.0         
                self.y = 0.0         
                self.Vx = 0.0        
                self.Vy = 0.0        

                self.Fx = 0.0        
                self.Fy = 0.0        

class Planet (Star):
        """Описание планет. Её физические свойства (радиус, цвет, масса и.т.д)"""
       
        def __init__(self):
                super().__init__()
                self.type = "planet"    
                self.R = 3
                self.color = "green"    
                self.m = 0.5         
                self.x = 0.0         
                self.y = 0.0         
                self.Vx = 0.0        
                self.Vy = 0.0        

                self.Fx = 0.0        
                self.Fy = 0.0 
