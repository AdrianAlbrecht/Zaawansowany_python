from nazwany_punkt import NazwanyPunkt

def main():
    nazwany_punkt = NazwanyPunkt(3, 4, "Punkt A")
    print(repr(nazwany_punkt)) 
    print(str(nazwany_punkt))   
    
    nazwany_punkt.x = 5
    nazwany_punkt.y = 6
    nazwany_punkt.name = "Punkt B"
    print(repr(nazwany_punkt))  
    print(str(nazwany_punkt))   
    
if __name__ == "__main__":
    main()
