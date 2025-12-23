from cardgame.proc import Proc
from cardgame.table import Table
from cardgame.eventtype import EventType as ev

class ProcHumanPlay(Proc):
    '''人間プレイ処理の実装。'''
    def do(self, table:Table):
        '''入力値を判定し、選べるならそれを選ぶ。'''
        # 手番をセット
        table.event['TURN_PLAYER'] = table.turn

        # カード未選択なら入力待ちとして終了
        if table.inputData['choice'] is None:
            table.event['EVENT_TYPE'] = ev.USER_TURN
            return

        # プレイ可否を判定し、不可なら入力待ちとして終了
        human = table.players[table.turn]
        playOK = table.rules.isPlayable(table.playedCards, human.getHand(), table.inputData['choice'])
        table.event['IS_PLAYABLE'] = playOK
        if not playOK:
            table.event['EVENT_TYPE'] = ev.USER_TURN
            return

        # カードが選択済み、かつプレイ可能であれば実際にプレイ
        table.playedCards.append(human.playCard(table.inputData['choice'])[1])
        table.event['MY_CHOICE'] = table.inputData['choice']
        table.event['PLAYED_CARDS'] = table.playedCards
        table.event['EVENT_TYPE'] = ev.USER_APPROVED

# 簡単な結合テスト
if __name__ == '__main__':
    from cardgame import inputData
    from cardgame.playertype import PlayerType as PType
    from cardgame.procdeal import ProcDeal
    from cardgame.proctrickinit import ProcTrickInit
    from cardgame.proccompplay import ProcCompPlay
    from cardgame.ttrules import TTRules

    # 入力データとゲームテーブルを作成
    data = inputData.inputData
    inputData.setNames(['A', 'B', 'C', 'D'])
    inputData.setTypes([PType.AI_RANDOM, PType.AI_RANDOM, PType.AI_RANDOM, PType.AI_RANDOM])
    table = Table(inputData=data, rules=TTRules())

    # ディール、トリック開始
    ProcDeal().do(table)
    ProcTrickInit().do(table)

    # コンピュータに適当にプレイしてもらう
    proc = ProcCompPlay()
    print('---')
    for i in range(3):
        proc.do(table)
        table.turn = (table.turn + 1) % len(table.players)
    print(f'【場札】{", ".join([card.string() for card in table.playedCards])}')

    # 人間の手札を表示し、手札入力を受け取ってプレイ
    player = table.players[table.turn]
    print_hand = [f'{i}:{card.string()}' for i, card in enumerate(player.getHand())]
    print(f'【手札】{", ".join(print_hand)}')
    proc = ProcHumanPlay()
    while True:
        table.inputData['choice'] = int(input('プレイするカードを番号で選んでください > '))
        proc.do(table)
        if table.event['EVENT_TYPE'] == ev.USER_TURN:
            print('そのカードは選べません')
        if table.event['EVENT_TYPE'] == ev.USER_APPROVED:
            break
    print('選んだカードは: ' + table.playedCards[-1].string())