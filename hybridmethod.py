from functools import wraps

class hybridmethod:
    '''クラス呼出とインスタンス呼出の両方に対応するメソッドのデコレータ。
    
    使いたいメソッドの冒頭に @hybridmethod を記載し、第1引数を obj_or_cls 等とする。
    if isinstance(obj_or_cls, type): がTrueであればクラス呼出として扱える。'''
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            # クラスから呼び出された場合（第一引数はクラス）
            @wraps(self.func)
            def bound_cls_method(*args, **kwargs):
                return self.func(owner, *args, **kwargs)
            return bound_cls_method
        else:
            # インスタンスから呼び出された場合（第一引数はインスタンス）
            @wraps(self.func)
            def bound_self_method(*args, **kwargs):
                return self.func(instance, *args, **kwargs)
            return bound_self_method