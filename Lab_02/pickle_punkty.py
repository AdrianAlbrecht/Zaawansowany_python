import pickle
from punkt import Punkt
from nazwany_punkt import NazwanyPunkt

punkty = [Punkt(1, 2), Punkt(3, 4), NazwanyPunkt(5, 6, "Punkt A"), NazwanyPunkt(7, 8, "Punkt B")]
with open('./Lab_02/punkty.pkl', 'wb') as file:
    pickle.dump(punkty, file)
    
with open('./Lab_02/punkty.pkl', 'rb') as file:
    punkty = pickle.load(file)

for punkt in punkty:
    print(repr(punkt))
