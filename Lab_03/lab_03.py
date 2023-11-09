# echo %ERRORLEVEL% 
import math
import sys

class Pizza:
    __price: float
    __toppings: list[str]
    __diameter: float
    
    def __init__(self, toppings:list[str], diameter:float) -> None:
        try:
            if diameter < 20.0:
                raise ValueError("błędny promień")
            self.__diameter = diameter
            self.__toppings = toppings
            self.__price =  round(0.005 * self.__area() + len(self.__toppings) * 2,2)
        except ValueError as e:
            print(e)
            sys.exit(-10)
    
    def __area(self) -> float:
        return math.pi * (self.diameter/2)**2
    
    def __get_diameter(self) -> float:
        return self.__diameter
    
    def __set_diameter(self, var:float) -> None:
        try:
            if var < 20.0:
                raise ValueError("błędny promień")
            self.__diameter = var
            self.__update_price()
        except ValueError as e:
            print(e)
            sys.exit(-10)
            
    @property
    def toppings(self) -> list[str]:
        return self.__toppings
    
    @property
    def price(self) -> float:
        return self.__price
    
    def __update_price(self) -> None:
        self.__price =  round(0.005 * self.__area() + len(self.toppings) * 2,2)
    
    def add_topping(self, *topp:str) -> None:
        for i_topp in topp:
            self.__toppings.append(i_topp)
            self.__price += 2
            
    def __repr__(self) -> str:
        return f"Pizza:\nśrednica: {self.diameter}{f'*dodatki: {self.__toppings}' if len(self.__toppings) > 0 else ''}\ncena: {self.__price}"\
            .replace("*", "\n").replace("[","").replace("]","")
            
    def __add__(self, pizza_b: 'Pizza') -> 'Pizza':
        return Pizza(self.toppings + pizza_b.toppings, self.diameter if self.diameter > pizza_b.diameter else pizza_b.diameter)
        
    diameter = property(__get_diameter, __set_diameter)      
            

class Slice(Pizza):
    __how_many_slices:int
    __one_slice_price:float
    
    def __init__(self, toppings:list[str], diameter:float, slices: int) -> None:
        super().__init__(toppings, diameter)
        self.how_many_slices = slices
        self.__update_slice_price()

    def __get__slices(self) -> int:
        return self.__how_many_slices
    
    def __set_slices(self, slices:int) -> None:
        try:
            if (slices%2 == 0) and (4 <= slices <= 12) :
                self.__how_many_slices = slices
                self.__update_slice_price()
            else:
                raise ValueError("błędna ilość kawałków")
        except ValueError as e:
            print(e)
            sys.exit(-10)
            
    def __update_slice_price(self) -> None:
        self.__one_slice_price = round(self.price / self.__how_many_slices,2)
            
    def part_price(self, ordered_slices:int) -> float:
        return self.__one_slice_price * ordered_slices
    
    def __repr__(self) -> str:
        return super().__repr__()+f'\nkawałki: {self.how_many_slices}\ncena za kawałek: {self.__one_slice_price}'
            
    how_many_slices = property(__get__slices, __set_slices)
