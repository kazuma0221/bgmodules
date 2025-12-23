from cardgame.playertype import PlayerType as T

inputData = {
    'player_names': [],
    'player_types': [],
    'choice': -1,
    'clear': False
}

def setNames(names):
    inputData['player_names'] = names

def setTypes(types):
    inputData['player_types'] = types

def setChoice(choice):
    inputData['choice'] = choice

def setClear(clear):
    inputData['clear'] = clear

def set(names:list[str], types:list[T]):
    inputData['player_names'] = names
    inputData['player_types'] = types

def makeTestData(number=4):
    setNames(['You', 'Abigail', 'Benjamin', 'Camille', 'Dennis'])
    setTypes([T.HUMAN, T.AI_RANDOM, T.AI_RANDOM, T.AI_RANDOM, T.AI_RANDOM])
    del inputData['player_names'][number:5]
    del inputData['player_types'][number:5]
    return inputData