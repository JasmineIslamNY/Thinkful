class Node(object):
    def __init__(self, name):
        self.name = name
        self.edges = {}
		
    def addEdge(self, distance, toCity):
        self.edges[toCity] = distance
 
class GraphData(object):
    def __init__(self):
        self.list = []
	
    def addCity(self, city, distance = "", toCity = ""):
        if toCity != "":
            try:
                toCityObjIndex = self.list.index(toCity)
            except ValueError:
                newToCity = Node(toCity) 
                self.list.append(self newToCity)
        
    
        try:
           cityObjIndex = self.list.index(city)
        except ValueError:
            newCity = Node(city)  
            if distance != "":
                newCity.addEdge(distance, toCity) 
            self.list.append(newCity)
            
      
