from cardgame.proc import Proc
from cardgame.table import Table
from cardgame.event_type import EventType as ev

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
    from cardgame import input_data
    from cardgame.player_type import PlayerType as PType
    from cardgame.proc_deal import ProcDeal
    from cardgame.proc_trick_init import ProcTrickInit
    from cardgame.proc_comp_play import ProcCompPlay
    from cardgame.trick_taking_rules import TrickTakingRules

    # 入力データとゲームテーブルを作成
    data = input_data.inputData
    input_data.setNames(['A', 'B', 'C', 'D'])
    input_data.setTypes([PType.AI_RANDOM, PType.AI_RANDOM, PType.AI_RANDOM, PType.AI_RANDOM])
    table = Table(inputData=data, rules=TrickTakingRules())

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