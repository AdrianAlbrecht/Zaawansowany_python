from punkt import Punkt

def main():
    punkt = Punkt(3, 4)
    print(repr(punkt))
    print(str(punkt))

    punkt.x = 5
    punkt.y = 6
    print(repr(punkt))
    print(str(punkt))

    del punkt.x
    del punkt.y
    print(repr(punkt))
    print(str(punkt))

if __name__ == "__main__":
    main()
