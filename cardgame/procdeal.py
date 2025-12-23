import random
from cardgame.proc import Proc
from cardgame.table import Table
from cardgame.eventtype import EventType as ev

class ProcDeal(Proc):
    '''ディール処理の実装。'''
    def do(self, table:Table):
        '''山札をシャッフルし、最初のリードを決め、プレイヤーに指定枚数の手札を配る。
        手札枚数はルールに記載がなければデッキ配りきり。'''
        # 手札と山札をリセットする
        del table.playedCards[:]
        for player in table.players:
            player.clear()
        table.newDeck().shuffle()
        # ディーラーを決めて、左隣がオープニングリード
        table.dealer = random.randrange(len(table.players)) if table.dealer is None else (table.dealer + 1) % len(table.players)
        table.turn = (table.dealer + 1) % len(table.players)
        # プレイヤーに手札を配ってソート
        handsize = int(table.deck.size() / len(table.players)) if (table.rules.getHandSize() < 1) else table.rules.getHandSize()
        for player in table.players:
            hand = [table.deck.pick() for _ in range(handsize)]
            hand.sort(reverse=True)
            player.setHand(hand)
        # 初期値設定
        self.setEvent(table)

    def setEvent(self, table:Table):
        '''ゲーム卓の出力用辞書eventに値を設定する。'''
        table.event = {}
        table.event['EVENT_TYPE'] = ev.BEGIN_DEAL
        table.event['DEALER'] = table.dealer
        table.event['OPENING_LEAD'] = table.turn
        table.event['TURN_PLAYER'] = table.turn
        table.event['PLAYER_NAMES'] = table.inputData['player_names']
        table.event['WIN_COUNTS'] = [0] * len(table.players)
        table.event['SCORES'] = table.scores
        table.event['TOTAL_SCORES'] = table.totalScores
        table.event['HANDS'] = [p.getHand() for p in table.players]
        table.event['PLAYED_CARDS'] = table.playedCards
        table.event['IS_PLAYABLE'] = True

# 単体テスト。4人戦で手札を配る
if __name__ == '__main__':
    from cardgame.table import Table
    from cardgame import inputData
    
    table = Table(inputData=inputData.makeTestData())
    ProcDeal().do(table)
    for player in table.players:
        hand = ', '.join([card.string() for card in player.getHand()])
        print(f'{player.pname}: {hand}')