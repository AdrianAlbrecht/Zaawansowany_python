import math
import sys
from typing import Optional
sys.path.append('Lab_01/punkt')
from punkt_alfa import Point

#Zad 1
class Point(Point):
    @staticmethod
    def distance(point1: Point, point2: Point) -> float:
        return math.sqrt((point2.x - point1.x)**2+(point2.y - point1.y)**2)
    
# p1 = Point(2,2)
# p2 = Point(5,6)
# print(Point.distance(p1, p2))

#Zad 2
class Adres():
    house_number:int
    street: str
    room_number: Optional[int]
    city: str
    postal_code: str
    
    def __init__(self, house_number, street, room_number, city, postal_code):
        self.house_number = house_number
        self.street = street
        self.room_number = room_number
        self.city = city
        self.postal_code = postal_code
        
    def __init__(self, house_number, street, city, postal_code):
        self.house_number = house_number
        self.street = street
        self.room_number = Optional(None)
        self.city = city
        self.postal_code = postal_code
        
    def show(self) -> None:
        print(self.street + " "+ self.house_number, end='')  
        if(self.room_number != None):
            print("/"+self.room_number,end='\n')
        print("\n"+self.postal_code + " " + self.city)
        
  
    
        