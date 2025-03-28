@lambda fliky : setattr(__import__('builtins'), 'FLIK', fliky())
class FLIKY:
    __slots__ = ('__x', )

    def __init__(self):
        self.__x = 0

    def __getitem__(self, x):
        print(f"#define LINE_{self.__x}(x) x {'^&'[x.start]} 0b%0{x.step}d" % x.stop)
        self.__x += 1
        return self
