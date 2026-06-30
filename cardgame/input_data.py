from cardgame.player_type import PlayerType as T

class InputData:
    def __init__(self, names:list[str]=[], types:list[T]=[], clear:bool=False):
        self.dic = {
            'player_names': names,
            'player_types': types,
            'choice': -1,
            'clear': clear,
        }

    def setNames(self, names):
        self.dic['player_names'] = names

    def setTypes(self, types):
        self.dic['player_types'] = types

    def setChoice(self, choice):
        self.dic['choice'] = choice

    def setClear(self, clear):
        self.dic['clear'] = clear

    def set(self, names:list[str], types:list[T]):
        self.dic['player_names'] = names
        self.dic['player_types'] = types

def makeTestData(self, number=4):
    names = ['You', 'Abigail', 'Benjamin', 'Camille', 'Dennis']
    types = [T.HUMAN, T.AI_RANDOM, T.AI_RANDOM, T.AI_RANDOM, T.AI_RANDOM]
    test_data = InputData(names, types)
    del test_data['player_names'][number:5]
    del test_data['player_types'][number:5]
    return test_data