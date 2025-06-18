from pathlib import Path as áÌî
moon_dir = áÌî('/home/ganer/Projects/Moon_BETA')
__dir__=(__file__:=áÌî(moon_dir / 'Header/base.☾')).parent
import os, sys, inspect, traceback, threading
from threading import get_ident as áÐèþÂÐðþáÐØ
from os import environ as env
from sys import stdin, stdout, stderr, setrecursionlimit, path as syspath, exit, argv as áÑË
from math import *
from site import getsitepackages
from json import dumps as jdumps__, loads as jloads__
from time import time, sleep
from cmath import *
from types import UnionType
from random import shuffle, choice, uniform, randint
from tempfile import gettempdir
from builtins import setattr as setattr_
from operator import setitem as setitem_, __gt__, __lt__, __ge__, __le__, rshift, lshift, getitem, delitem
from itertools import chain, filterfalse, product, accumulate, zip_longest
from functools import partial as MOD, reduce, cache
getattr(syspath, 'extend')(getsitepackages())
setrecursionlimit(100000)
del (getsitepackages, factorial, e, pi, tau, sqrt, cbrt, pow)
(setattr := (lambda x, y, z: setattr_(x, y, z) or z))
(setitem := (lambda x, y, z: setitem_(x, y, z) or z))
(ÄÊSTK := {})
(ÄÊPSH := (lambda x: getattr(getattr(ÄÊSTK, 'setdefault')(áÐèþÂÐðþáÐØ(), []), 'append')(x) or x))
(ÄÊPKE := (lambda x=0: getattr(ÄÊSTK, 'setdefault')(áÐèþÂÐðþáÐØ(), [])[-1 - x]))
(ÄÊPOP := (lambda x=0: getattr(getattr(ÄÊSTK, 'setdefault')(áÐèþÂÐðþáÐØ(), []), 'pop')(-1 - x)))
(ÄÊDEL := (lambda x: getattr(getattr(ÄÊSTK, 'setdefault')(áÐèþÂÐðþáÐØ(), []), '__delitem__')(slice(-x, None))))
(ÂÞÅCAT := (lambda x, y: y(x) if callable(y) else x * y))

def ÄÊCUR(áÍÊ, áÍÅ, *áÎç):

    def Ëðá(*áÌú):
        if len(áÌú) < len(áÍÊ):
            return lambda *áÑË: Ëðá(*áÌú, *áÑË)
        (ÄÊPSH(([*áÎç], {**áÍÅ})), ((áÖÒ := ÄÊPKE(0)[0]), (áÖÝ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        for k, v in zip(áÍÊ, áÌú):
            (ÄÊPSH(áÖÒ if isinstance(k, int) else áÖÝ), ÄÊPSH(k), ÄÊPSH(v), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        return áÖÒ[0](*áÖÒ[slice(1, None)], *áÌú[slice(len(áÍÊ), None)], **áÖÝ)
    return Ëðá()
(ÄÊPSH((Exception, object, dict, bool, list, tuple, set, str, int, float, bytes)), ((áÍÚ := ÄÊPKE(0)[0]), (áÍä := ÄÊPKE(0)[1]), (áÍÙ := ÄÊPKE(0)[2]), (áÍÖ := ÄÊPKE(0)[3]), (áÍá := ÄÊPKE(0)[4]), (áÍé := ÄÊPKE(0)[5]), (áÍè := ÄÊPKE(0)[6]), (ÁÜÙ := ÄÊPKE(0)[7]), (áÍÞ := ÄÊPKE(0)[8]), (áÍÛ := ÄÊPKE(0)[9]), (áÍî := ÄÊPKE(0)[10])), ÄÊDEL(1))[1]
(ÁØã := '')
(ÄÊPSH((1 / 2, 1 / 3, 1 / 4, 1 / 5, 1 / 6, 1 / 7, 1 / 8, 1 / 9, 1 / 10, 2 / 3, 2 / 5, 2 / 7, 2 / 9, 3 / 4, 3 / 5, 3 / 7, 3 / 8, 3 / 10, 4 / 5, 4 / 7, 4 / 9, 5 / 6, 5 / 7, 5 / 8, 5 / 9, 6 / 7, 7 / 8, 7 / 9, 7 / 10, 8 / 9, 9 / 10, 0, 1 / 100)), ((ÃÆ := ÄÊPKE(0)[0]), (ÂÑõ := ÄÊPKE(0)[1]), (ÃÅ := ÄÊPKE(0)[2]), (ÂÑø := ÄÊPKE(0)[3]), (ÂÑü := ÄÊPKE(0)[4]), (ÂÑò := ÄÊPKE(0)[5]), (ÂÑÿ := ÄÊPKE(0)[6]), (ÂÑó := ÄÊPKE(0)[7]), (ÂÑô := ÄÊPKE(0)[8]), (ÂÑö := ÄÊPKE(0)[9]), (ÂÑù := ÄÊPKE(0)[10]), (ÄÝóú := ÄÊPKE(0)[11]), (ÄÝôÀ := ÄÊPKE(0)[12]), (ÃÇ := ÄÊPKE(0)[13]), (ÂÑú := ÄÊPKE(0)[14]), (ÄÝóû := ÄÊPKE(0)[15]), (ÂÒÀ := ÄÊPKE(0)[16]), (ÄÝôÏ := ÄÊPKE(0)[17]), (ÂÑû := ÄÊPKE(0)[18]), (ÄÝóü := ÄÊPKE(0)[19]), (ÄÝôË := ÄÊPKE(0)[20]), (ÂÑý := ÄÊPKE(0)[21]), (ÄÝóý := ÄÊPKE(0)[22]), (ÂÒÁ := ÄÊPKE(0)[23]), (ÄÝôÂ := ÄÊPKE(0)[24]), (ÄÝóÿ := ÄÊPKE(0)[25]), (ÂÒÂ := ÄÊPKE(0)[26]), (ÄÝôÃ := ÄÊPKE(0)[27]), (ÄÝôÐ := ÄÊPKE(0)[28]), (ÄÝôÄ := ÄÊPKE(0)[29]), (ÄÝôÑ := ÄÊPKE(0)[30]), (ÂÒî := ÄÊPKE(0)[31]), (ÄÝôÒ := ÄÊPKE(0)[32])), ÄÊDEL(1))[1]
(ÄÊPSH((3.141592653589793, 2.718281828459045)), ((Ïî := ÄÊPKE(0)[0]), (ÂÐæ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((inf, complex(0, 1), ÂÞÅCAT(2, Ïî), ÂÞÅCAT(ÃÆ, Ïî), ÂÞÅCAT(ÃÅ, Ïî), ÂÞÅCAT(ÂÑÿ, Ïî))), ((ÂÕË := ÄÊPKE(0)[0]), (Ãù := ÄÊPKE(0)[1]), (Ïò := ÄÊPKE(0)[2]), (ÄÝøà := ÄÊPKE(0)[3]), (ÄÝøá := ÄÊPKE(0)[4]), (ÄÝøâ := ÄÊPKE(0)[5])), ÄÊDEL(1))[1]
(ÄÊPSH((-ÂÕË, -Ãù, -Ïò, -Ïî, -ÄÝøà, -ÄÝøá, -ÄÝøâ, -ÂÐæ)), ((ÄÝîá := ÄÊPKE(0)[0]), (ÄÝîâ := ÄÊPKE(0)[1]), (ÄÝîä := ÄÊPKE(0)[2]), (ÄÝîå := ÄÊPKE(0)[3]), (ÄÝîæ := ÄÊPKE(0)[4]), (ÄÝîç := ÄÊPKE(0)[5]), (ÄÝîè := ÄÊPKE(0)[6]), (ÄÝîã := ÄÊPKE(0)[7])), ÄÊDEL(1))[1]
(ÂÒå := (2 ** 3 ** 4))
(ÄÊPSH((lambda *áÑË: áÑË[0], lambda *áÑË: áÑË[-1])), ((Âåß := ÄÊPKE(0)[0]), (ÂåÔ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]

class Named:
    (ÄÊPSH((lambda áÑÞ, s: ÂåÔ((ÄÊPSH(s), ÄÊPSH(áÑÞ), ÄÊPSH('s'), setattr(ÄÊPKE(1), ÄÊPKE(0), ÄÊPKE(2)), ÄÊDEL(3))[3], None), lambda áÑÞ: getattr(áÑÞ, 's'))), ((__init__ := ÄÊPKE(0)[0]), (__repr__ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÂÞÅ := (NULL := Named('␀')))
(ÄÊPSH((Named('\U000f0b88'), Named('\U000f18e9'), Named('⬤'))), ((ÄÔýò := ÄÊPKE(0)[0]), (ÄÕøü := ÄÊPKE(0)[1]), (ÂýÃ := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]

class ÂÐô:
    None
(ÂÑÅ := áÍÞ)
(ÂÐý := (áÍÛ | ÂÑÅ))
(ÂÐá := complex)
(ÂÁÍ := (lambda Æå, *áÑË, **áÑÕ: lambda *áÑË, **áÑÕ: Æå(áÑË[1], áÑË[0], *áÑË[slice(2, None)], **áÑÕ) if ãÊú(áÑË) >= 2 else Æå(*áÑË, **áÑÕ)))
(ÂÖë := (lambda Æå, *áÑË, **áÑÕ: lambda *áÑË, **áÑÕ: Æå(*áÑË[0], **áÑÕ)))
(ãÊú := len)
(ÄÕÍÔ := (lambda *áÑË, áØÁ=ÂÞÅ: (áÑË[0] if áØÁ is ÂÞÅ else áØÁ) if áÑË else (lambda *áÑË: áÑË[0] if áÑË else ÄÕÍÔ) if áØÁ is ÂÞÅ else lambda *áÑË: áØÁ))
(CUR := (lambda Æå, *áÖÒ, **áÖÝ: Æå(*áÖÒ, **áÖÝ) if ãÊú(áÖÒ) >= 2 else lambda *áÖÓ, **áÖÞ: CUR(Æå, *áÖÒ, *áÖÓ, **áÖÝ | áÖÞ)))
(CURR := (lambda Æå, *áÖÒ, **áÖÝ: Æå(*áÖÒ, **áÖÝ) if ãÊú(áÖÒ) >= 2 else lambda *áÖÓ, **áÖÞ: CUR(Æå, áÖÓ[0], *áÖÒ, *áÖÓ[slice(1, None)], **áÖÝ | áÖÞ)))
(ÁØò := (ÁÙÇ := (lambda Æå: lambda áØÆ, *áÖÒ, **áÖÝ: [áÑÿ for v in áØÆ if (áÑÿ := Æå(v, *áÖÒ, **áÖÝ)) is not ÄÔýò])))
(ÁØÿþÁÙÄ := (lambda Æå: Æå))
(ÁØòþÁÙÄ := (lambda Æå: lambda áØÆ, áØÇ, *áÖÒ, **áÖÝ: [áÑÿ for x in áØÆ if (áÑÿ := Æå(x, áØÇ, *áÖÒ, **áÖÝ)) is not ÄÔýò]))
(ÁØÿþÁÙÇ := (lambda Æå: lambda áØÆ, áØÇ, *áÖÒ, **áÖÝ: [áÑÿ for y in áØÇ if (áÑÿ := Æå(áØÆ, y, *áÖÒ, **áÖÝ)) is not ÄÔýò]))
(ÁØòþÁÙÇ := (lambda Æå: lambda áØÆ, áØÇ, *áÖÒ, **áÖÝ: [áÑÿ for x, y in ÄÕåØ(áØÆ, áØÇ) if (áÑÿ := Æå(x, y, *áÖÒ, **áÖÝ)) is not ÄÔýò]))
(ÄÊPSH((lambda x, y: (False if y else x) if x else y, lambda x, y: (y if y else False) if x else x if y else True)), ((ÄÝøø := ÄÊPKE(0)[0]), (ÄÝøú := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÂÕÕ := (Âùè := (lambda x, y: x or y)))
(ÄÝøù := (ÄÝùÀ := (lambda x, y: not (x or y))))
(ÂÕÔ := (Âùç := (lambda x, y: x and y)))
(ÄÝøå := (ÄÝùÁ := (lambda x, y: (False if y else x) if x else y if y else True)))
(ÄÊPSH((__lt__, __gt__, __le__, __ge__)), ((ÿ := ÄÊPKE(0)[0]), (ÁÁ := ÄÊPKE(0)[1]), (ÂÖÔ := ÄÊPKE(0)[2]), (ÂÖÕ := ÄÊPKE(0)[3])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda x, y: x == y, lambda x, y: x != y)), ((ÂÖÑ := ÄÊPKE(0)[0]), (ÂÖÐ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda x, y: gcd(x, y) == x, lambda x, y: gcd(x, y) != x)), ((ÂÕÐ := ÄÊPKE(0)[0]), (ÂÕÑ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda x, y: x in y, lambda x, y: x not in y)), ((ÂÔó := ÄÊPKE(0)[0]), (ÂÔô := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda x, y: y in x, lambda x, y: y not in x)), ((ÂÔö := ÄÊPKE(0)[0]), (ÂÔø := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda x, y: getattr({*x}, 'issubset')({*y}), lambda x, y: getattr({*y}, 'issubset')({*x}))), ((ÂÖó := ÄÊPKE(0)[0]), (ÂÖô := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda x, y: not ÂÖó(x, y), lambda x, y: not ÂÖô(x, y))), ((ÂÖõ := ÄÊPKE(0)[0]), (ÂÖö := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda x, y: getattr((Ïß := {*x}), 'issubset')((Ïà := {*y})) and Ïß != Ïà, lambda x, y: getattr((Ïß := {*y}), 'issubset')((Ïà := {*x})) and Ïß != Ïà)), ((ÂÖü := ÄÊPKE(0)[0]), (ÂÖý := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda x, y: not ÂÖü(x, y), lambda x, y: not ÂÖý(x, y))), ((ÄÝøÄ := ÄÊPKE(0)[0]), (ÄÝøÅ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÝöú := (lambda x, y: ÂÕÃ(ÂÕØ(x, y), ÂÕÖ(x, y))))
(ÂÕØ := (lambda x, y: {*x} | {*y} if ÁØö(x, áÍè) else [*x, *[z for z in y if z not in x]]))
(ÂÕÖ := (lambda x, y: {*x} & {*y} if ÁØö(x, áÍè) else [z for z in x if z in y]))
(ÂÕÃ := (lambda x, y: x - {*y} if ÁØö(x, áÍè) else [z for z in x if z not in y]))
(ÂøÚ := (lambda áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ: Áÿú(product(*([áØÆ] * áØÁ if áØÇ is ÂÞÅ and áØÁ is not ÂÞÅ else (áØÆ if áØÇ is ÂÞÅ else [áØÆ, áØÇ]) * (1 if áØÁ is ÂÞÅ else áØÁ))), áÍá)))
(ÂØÑ := (lambda *áÑË, áØÁ=1: (Æå := (lambda *áÑË, n=1, r=[]: (lambda ÂîÓ: Áÿú(ÂîÓ[0], lambda x: Æå(*ÂîÓ[slice(1, None)], r=r + [áØÆ]) if ãÊú(ÂîÓ) > 1 else r + [áØÆ]))(áÑË * n)))(*áÑË, n=áØÁ)))
(ÄÊPSH((lambda x, y: x % y, lambda x, y: x // y)), ((æ := ÄÊPKE(0)[0]), (ÃËÕ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda x, y: x is y, lambda x, y: x is not y)), ((ÂÕó := ÄÊPKE(0)[0]), (ÂÕõ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda x: ~x, lambda x, y: x @ y)), ((ÂÄ := ÄÊPKE(0)[0]), (ÁÃ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda x, y: x | y, lambda x, y: x & y, lambda x, y: x ^ y)), ((ÂÂ := ÄÊPKE(0)[0]), (ç := ÄÊPKE(0)[1]), (Áâ := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
(ÄÊPSH((lshift, rshift)), ((Âúù := ÄÊPKE(0)[0]), (Âúú := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda x, y: x ** y, lambda x: not x, lambda áØÆ, áØÁ=ÂÞÅ: lambda x: MOD(î, áØÁ=áØÁ)(áØÆ))), ((ÂÙû := ÄÊPKE(0)[0]), (Âó := ÄÊPKE(0)[1]), (Âö := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
(ÂÀÇ := (lambda áØÆ: ÄÝöì(ÂÀÇ(ÄÝöì(áØÆ))) if ÁØö(áØÆ, áÍÞ) else áØÆ[slice(None, None, -1)] if ÁØö(áØÆ, ÁÜÙ | áÍá | áÍé) else getattr(áØÆ, '__reversed__')() if hasattr(áØÆ, '__reversed__') else [*áØÆ][slice(None, None, -1)]))
(ÄÝöí := (lambda áØÆ=ÂÞÅ, áØÁ=ÂÞÅ: chr(áØÆ) if ÁØö(áØÆ, áÍÞ) else ord(áØÆ) if ÁØö(áØÆ, ÁÜÙ) and (ãÊú(áØÆ) == 1 and áØÁ is not áÍá) else MOD(Áëý, áØÁ=ÁØö(áØÆ[0], áÍÞ))(Áÿú(áØÆ, ÄÝöí), Âøî)))
(ÂÛê := (lambda áØÆ, áØÁ=ÂÞÅ: MOD(ÂÛê, áØÁ=ÂÔö(áØÆ, '\u205f') * '\u205f' + '\u2009')(áØÆ) if áØÁ is ÂÞÅ else MOD(Áëý, áØÁ=ãÊú(áØÁ) > 1)(getattr(áØÆ, 'split')(áØÁ[0]), MOD(ÁØò(lambda ÂîÓ: MOD(ÂÛê, áØÁ=áØÁ[slice(1, None)])(ÂîÓ))))))
(Âäû := (lambda áØÆ, áØÁ=ÂÞÅ: ÄÝõé(Áÿú(ÄÝõé(áØÆ), MOD(Âäû, áØÁ=áØÁ))) if MOD(ÁØö, áØÁ=ÂÕó)(áØÆ, ÂÐá) else áÍÞ(round(áØÆ)) if áØÁ is ÂÞÅ else round(áØÆ, áØÁ)))
(ÄÊPSH((floor, ceil)), ((Âüð := ÄÊPKE(0)[0]), (Âüï := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda áØÆ: getattr(áØÆ, 'real'), lambda áØÆ: getattr(áØÆ, 'imag'))), ((ÄÝõè := ÄÊPKE(0)[0]), (ÄÝõç := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÝõé := (lambda áØÆ: ÂÐá(*áØÆ) if ÁØö(áØÆ, áÍá | áÍé) else (ÄÝõè(áØÆ), ÄÝõç(áØÆ))))
(ÂÛÅ := (lambda áØÆ, áØÁ=ÂÞÅ: MOD(ÄÕåØ, áØÁ=áØÁ)(áØÆ)))
(Âüá := getattr(ÁÜÙ, 'strip'))
(ÂÌú := (lambda áØÆ, áØÇ: [*range(áØÆ, áØÇ)]))
(ÂÕÀ := (lambda áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ: (MOD(î, áØÁ=áØÁ)(áØÆ), MOD(ì, áØÁ=áØÁ)(áØÆ)) if áØÇ is ÂÞÅ else (MOD(î, áØÁ=áØÁ)(áØÆ, áØÇ), MOD(ì, áØÁ=áØÁ)(áØÆ, áØÇ))))
(Âù := (lambda áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ: (MOD(ì, áØÁ=áØÁ)(áØÆ), MOD(î, áØÁ=áØÁ)(áØÆ)) if áØÇ is ÂÞÅ else (MOD(ì, áØÁ=áØÁ)(áØÆ, áØÇ), MOD(î, áØÁ=áØÁ)(áØÆ, áØÇ))))

def ì(áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ):
    (v := (+áØÆ if áØÇ is ÂÞÅ else áØÆ + áØÇ))
    return v if áØÁ is ÂÞÅ else v % MOD(Áëý, áØÁ=áÓö)(áØÁ, ãÊú)

def î(áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ):
    (v := (-áØÆ if áØÇ is ÂÞÅ else áØÆ - áØÇ))
    return v if áØÁ is ÂÞÅ else v % MOD(Áëý, áØÁ=áÓö)(áØÁ, ãÊú)

def ÂØú(áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ):
    return áØÆ * áØÇ if áØÁ is ÂÞÅ else áØÆ * áØÇ % MOD(Áëý, áØÁ=áÓö)(áØÁ, ãÊú)

def ÄÃ(áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ):
    return áØÆ / áØÇ if áØÁ is ÂÞÅ else áØÆ / áØÇ % MOD(Áëý, áØÁ=áÓö)(áØÁ, ãÊú)

def ÃËÕ(áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ):
    return áØÆ // áØÇ if áØÁ is ÂÞÅ else MOD(ÂÙû, áØÁ=-MOD(Áëý, áØÁ=áÓö)(áØÁ, ãÊú))(áØÆ, áØÇ)

def ÂÙû(áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ):
    return áØÆ ** áØÇ if áØÁ is ÂÞÅ else pow(áØÆ, áØÇ, MOD(Áëý, áØÁ=áÓö)(áØÁ, ãÊú))

def ÐÌü(Æå, *áÑË, **áÑÕ):
    if áÓó(Æå):
        return Æå(*áÑË, **áÑÕ)
    if áÓö(Æå):
        for x in Æå:
            None
        return Æå
    ÂùÆ(False, '%s is not iterable or callable.' % (Æå,))

def ÂØô(áÍÒ, áØÁ=True):
    for áØÁ in áÍÒ:
        if not áØÁ:
            break
    return áØÁ

def ÂØõ(áÍÒ, áØÁ=False):
    for áØÁ in áÍÒ:
        if áØÁ:
            break
    return áØÁ

class Ticker:
    (__slots__ := ('i',))
    (__init__ := (lambda áÑÞ, i: ÂåÔ((ÄÊPSH(áÑÞ), ÄÊPSH('i'), ÄÊPSH(i), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3], None)))
    (__call__ := (lambda áÑÞ, *áÑË, **áÑÕ: ÂåÔ((ÄÊPSH(áÑÞ), ÄÊPSH('i'), ÄÊPSH(getattr(ÄÊPKE(1), ÄÊPKE(0))), ÄÊPSH(ÄÊPKE(0) - 1), setattr(ÄÊPKE(3), ÄÊPKE(2), ÄÊPKE(0)), ÄÊDEL(4))[4], áÑÞ)))
    (__bool__ := (lambda áÑÞ: not getattr(áÑÞ, 'i')))
    (__repr__ := (lambda áÑÞ: 'Ticker[i=%s]' % (getattr(áÑÞ, 'i'),)))

class TimerState:
    (__init__ := (lambda áÑÞ, áÓË: ÂåÔ((ÄÊPSH(áÑÞ), ÄÊPSH('áÓË'), ÄÊPSH(áÓË), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3], None)))
    (__bool__ := (lambda áÑÞ: getattr(getattr(áÑÞ, 'áÓË'), 's')))
    (__call__ := (lambda áÑÞ: getattr(getattr(áÑÞ, 'áÓË'), 'r') if áÑÞ else ÐÌü(getattr(getattr(getattr(áÑÞ, 'áÓË'), 'r'), 'copy'))))
    (__repr__ := (lambda áÑÞ: 'Timer[%s; %ss; %s; %s Remaining loops]=%s' % ('ID'[getattr(getattr(áÑÞ, 'áÓË'), 'y') >= 0], ÂüÌ(getattr(getattr(áÑÞ, 'áÓË'), 'y')), 'Running' if áÑÞ else 'Completed', getattr(getattr(áÑÞ, 'áÓË'), 'n'), getattr(getattr(áÑÞ, 'áÓË'), 'r'))))
(tmp := {'ᴍ': 'Áÿú', 'ꟿ': 'ËãÂ', 'ſ': 'ÆÑ', 'Ϝ': 'ÐÌ', '\U000f0233': 'ÄÔÔè', '\U000f0232': 'ÄÔÔç', '\ueb86': 'ÐÌÛ', '\U000f04bc': 'ÄÔàÑ', '\U000f04bd': 'ÄÔàÒ', 'ᙎ': 'Ááæ', 'ᙡ': 'Ááú', 'ᗢ': 'Áßô', 'ᙧ': 'ÁâÁ', '⊚': 'ÂØÍ', '⊜': 'ÂØÏ', '🟕': 'ãéÜ', '🟖': 'ãéÝ', '⊛': 'ÂØÎ', '⍟': 'ÂÛÜ', '○': 'Âåæ', '⍜': 'ÂÛÙ', '\U000f0b2b': 'ÄÔüÑ', '\U000f0b29': 'ÄÔüÏ', '\uf071': 'ÐâÄ', '\U000f0536': 'ÄÔâÑ', '\uea6c': 'ÐÇò', '\U000f147c': 'ÄÕåØ', '\U000f7e45': 'ÄÝöÔ', '⪡': 'Âúù', '⪢': 'Âúú', '\U000f0e35': 'ÄÕÊÂ', '\U000f0e37': 'ÄÕÊÄ', '⤉': 'ÂóÍ', '⤈': 'ÂóÌ', '⟷': 'Âîí', '\U000f7e4c': 'ÄÝöÜ', '\U000f7e4d': 'ÄÝöÝ', '\U000f7e4e': 'ÄÝöÞ', '\U000f7e39': 'ÄÝöÈ', '\U000f7e3a': 'ÄÝöÉ', '\U000f7e38': 'ÄÝöÇ', '\U000f7e3b': 'ÄÝöÊ', '⨝': 'Âøî', '⟕': 'ÂîÊ', '⟖': 'ÂîË', '⟗': 'ÂîÌ', '⫰': 'ÂüÌ', '⫯': 'ÂüË', '\U000f7e52': 'ÄÝöâ', '\U000f7e53': 'ÄÝöã', '\U000f7e54': 'ÄÝöä', '\U000f7e55': 'ÄÝöå', '\U000f7e56': 'ÄÝöæ', '\U000f7e13': 'ÄÝõà', '\U000f7e3c': 'ÄÝöË', '\U000f7e14': 'ÄÝõá', '\ue270': 'ÏäÒ', '\U000f114f': 'ÄÕØÃ', '\uf074': 'ÐâÇ'})
(ENC := 'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýÿ')
(RCD := CURR(lambda ÂîÓ, ÂîÒ: ÂîÓ not in ÂîÒ, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'))
(SPE := (lambda ÂîÓ: ÂîÓ in ENC + 'þ'))
(PEV := (lambda ÂîÓ: Âøî(MOD(ÄÔÔç, áØÁ=Âåæ(Âøî, MOD(ÁØò(lambda ÂîÓ: ÄÝöì(ÄÝöí(ÂîÓ), ãÊú(ENC), C=ENC)))))(áÇù(ÂîÓ, RCD), lambda ÂîÓ: ÂÞÅCAT(ÂîÓ[0], RCD)), 'Þ')))
(VEP := (lambda ÂîÓ: Âøî(MOD(ÄÔÔç, áØÁ=lambda ÂîÓ: Âøî(ÁØò(lambda ÂîÓ: MOD(Áëý, áØÁ=ÄÊCUR((1,), {}, ÂÖó, ÂýÃ, ENC))(ÂîÓ, ÄÔâÑ(Âåæ(Âåæ(Âøî, ÄÝöí), ÄÊCUR((1,), {'C': ENC}, ÄÝöì, ÂýÃ)), lambda x: '⸮%s?' % (x,))))(ÄÝöÞ(ÂîÓ, 'þ'))))(áÇù(ÂîÓ, SPE), lambda ÂîÓ: ÂÞÅCAT(ÂîÓ[0], SPE)))))

def OPWRAP_(*áÖê):

    def R(Æå):
        for x in áÖê:
            (ÄÊPSH(globals()), ÄÊPSH(tmp[x] if x in tmp else PEV(x)), ÄÊPSH(MOD(Æå, x)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    return R
(ÄÊPSH((callable, lambda x: hasattr(x, '__iter__'))), ((áÓó := ÄÊPKE(0)[0]), (áÓö := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]

def áÓõ(x):
    try:
        return hash(x)
    except:
        pass
    return False
(áÍÇ := (lambda x, y='utf-8', *áÑË, **áÑÕ: getattr(x, 'encode')(y, *áÑË, **áÑÕ) if ÁØö(x, ÁÜÙ) else getattr(x, 'decode')(y, *áÑË, **áÑÕ)))

class ÃÆë(áÍÞ):
    (__new__ := (lambda ÂÑÎ: getattr(áÍÞ, '__new__')(ÂÑÎ, 1)))
    (__call__ := (lambda *áÑË, **áÑÕ: ÃÆë))
    (__repr__ := (lambda áÑÞ: 'ⴳ'))

class ÃÆì(áÍÞ):
    (__new__ := (lambda ÂÑÎ: getattr(áÍÞ, '__new__')(ÂÑÎ, 0)))
    (__call__ := (lambda *áÑË, **áÑÕ: ÃÆì))
    (__repr__ := (lambda áÑÞ: 'ⴴ'))
(ÃÆë := ÃÆë())
(ÃÆì := ÃÆì())

def ÂùÆ(áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ):
    if áØÆ:
        return áØÆ
    (áØÅ := ('MOON_WARNING_IS_ERR' in env))
    (áÖð := (áØÅ or 'MOON_DEPRECATION_IS_ERR' in env))
    if áØÁ is ÄÔáô:
        (ÄÊPSH((áÖð, 'Deprecation %s' % ('Error' if áÖð else 'Warning',))), ((áÓÔ := ÄÊPKE(0)[0]), (áÓà := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    elif áØÁ is ÂÄ:
        (ÄÊPSH((áØÅ, 'Warning%s' % (' [as Error]' if áØÅ else ÁØã,))), ((áÓÔ := ÄÊPKE(0)[0]), (áÓà := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    else:
        (ÄÊPSH((True, 'Assertion failed')), ((áÓÔ := ÄÊPKE(0)[0]), (áÓà := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (áÓà := ('%s! ⟨𝓿=%s⟩%s' % (áÓà, ÂÞÅCAT(áØÆ, repr), ' ' + áØÇ if áØÇ is not ÂÞÅ else ÁØã)))
    try:
        (áÓà := termclr(áÓà, 'f22' if áÓÔ else 'ff2'))
    except:
        None
    Âçß(áÓà)
    if áÓÔ:
        raise AssertionError
    return áØÆ

@OPWRAP_(*'\uf071\U000f0536\uea6c')
def _(t, Æå=ÂÞÅ, áÍÜ=ÂÞÅ, áØÁ=áÍÚ):
    (ÄÊPSH((áØÁ, ÂÕÃ([Æå, áÍÜ], [ÂÞÅ]))), ((áÍÎ := ÄÊPKE(0)[0]), (v := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    if ãÊú(v) == 1:
        (Æå := v[0])
        if t == '\uf071':
            raise Æå

    def r(*áÑË, **áÑÕ):
        try:
            return Æå(*áÑË, **áÑÕ)
        except áÍÎ as Ïã:
            if ãÊú(v) == 1:
                if t == '\U000f0536':
                    return áÑË[0] if áÑË else None
                if t == '\uea6c':
                    return Ïã
            if t == '\uf071':
                return áÍÜ
            if t == '\U000f0536':
                return áÍÜ(*áÑË, **áÑÕ)
            if t == '\uea6c':
                return áÍÜ(Ïã)
    return r

def Âáõ(*áÑË, áÌÄ=None):
    (ÄÊPSH(áÑË), (*(áÑË := ÄÊPKE(0)[slice(0, -1, None)]), (Æå := ÄÊPKE(0)[-1])), ÄÊDEL(1))[1]
    if not áÌÄ:
        (áÌÄ := ÂÚü())
    if not áÑË:
        return Æå(*áÌÄ)
    with áÑË[0] as áÌß:
        return getattr(áÌÄ, 'append')(áÌß) or Âáõ(*áÑË[slice(1, None)], Æå, áÌÄ=áÌÄ)

def Âçß(*áÑË, ÂìÆ=False, áÖý=' ', áØÁ='\n'):
    getattr((Æå := (stderr if ÂìÆ else stdout)), 'write')(Âøî(áÑË, ÁÜÙ(áÖý)) + ÁÜÙ(áØÁ))
    getattr(Æå, 'flush')()
    if áÑË:
        return áÑË[0]

def ÁØö(áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ, TYPELIKE={áÓó, áÓõ, áÓö}, TYPEE=type | UnionType):
    if áØÇ is ÂÞÅ:
        return type(áØÆ)
    elif áØÇ in TYPELIKE:
        return áØÇ(áØÆ)
    if áØÁ is ÂÞÅ:
        if áØÇ is ÂÐô:
            return ÁØö(áØÆ, áÍÖ | áÍÞ) and áØÆ >= 0
        elif áØÇ is ÂÑÅ:
            return ÁØö(áØÆ, ÂÐô | áÍÞ)
        elif áØÇ is ÂÐý:
            return ÁØö(áØÆ, ÂÑÅ | ÂÐý)
        elif áØÇ is ÂÐá:
            return ÁØö(áØÆ, ÂÐý | complex)
    return isinstance(áØÆ, áØÇ if isinstance(áØÇ, TYPEE) else type(áØÇ))
(ÄÊPSH((lambda áØÆ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ: MOD(ÁØö, áØÁ=áØÁ)(áØÇ, áØÆ), lambda áØÆ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ: not MOD(ÁØö, áØÁ=áØÁ)(áØÆ, áØÇ), lambda áØÆ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ: not MOD(ÁØö, áØÁ=áØÁ)(áØÇ, áØÆ))), ((ÁØñ := ÄÊPKE(0)[0]), (ÄÝøÇ := ÄÊPKE(0)[1]), (ÄÝøÆ := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
(Âõ := (lambda áØÁ: lambda x: ÁØò(lambda ÂîÓ: ÄóÌÁ(ÂÞÅCAT(Ïò, áØÁ ** (-1)) * (ÂîÓ + ÃÆ * (áØÁ < 0))) + ÂÞÅCAT(Ãù, ÄóÌÀ(ÂÞÅCAT(Ïò, áØÁ ** (-1)) * (ÂîÓ + ÃÆ * (áØÁ < 0)))))(ÂÿÇ(ÂüÌ(áØÁ)))))
(ÂÕÇ := (lambda áØÆ=ÂÞÅ, áØÁ=2: áØÆ ** áØÁ ** (-1)))
(ÚÑ := (lambda áØÆ, áØÁ=2: ÁØò(lambda ÂîÓ: ÂîÓ * áØÆ ** áØÁ ** (-1))(MOD(Âõ, áØÁ=ÂüÌ(áØÁ)))))
(ÐàÒ := (lambda áØÆ, *áÑË, **áÑÕ: lambda *áÑË, **áÑÕ: áØÆ(*ÄÔÙù(áÑË), **áÑÕ)))
(ÂÕì := (lambda áØÆ, *áÑË, **áÑÕ: lambda *áÑË, **áÑÕ: áØÆ(*ÂÀÇ(áÑË), **áÑÕ)))
(ë := (lambda x, y: x * y))
(ð := (lambda x, y: x / y))
(ÄÔáô := áÍä())

class Holder:
    (__slots__ := ('x',))

    def __init__(áÑÞ, x=ÂÞÅ):
        (ÄÊPSH(áÑÞ), ÄÊPSH('x'), ÄÊPSH(x), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]

    def __pos__(áÑÞ):
        return Âåß(getattr(áÑÞ, 'x'), ÂùÆ(getattr(áÑÞ, 'x') is not ÂÞÅ, 'Holder value unset!'))

    def __call__(áÑÞ, x=ÂÞÅ):
        (ÄÊPSH(áÑÞ), ÄÊPSH('x'), ÄÊPSH(x), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]

    def __bool__(áÑÞ):
        return getattr(áÑÞ, 'x') is not ÂÞÅ
__dir__=(__file__:=áÌî(moon_dir / 'Header/system.☾')).parent
def PL_SLEEP(x):
    from time import sleep
    ÂÞÅCAT(x, sleep)

def PL_TIME():
    from time import time
    return ÐÌü(time)

def PL_CPU_COUNT():
    import multiprocessing
    return ÐÌü(getattr(multiprocessing, 'cpu_count'))

def PL_THREAD(Æå, *áÑË, **áÑÕ):
    from threading import Thread as T
    (atom := [])
    ÐÌü(getattr((t := T(target=lambda: ÂÞÅCAT(Æå(*áÑË, **áÑÕ), getattr(atom, 'append')))), 'start'))
    return lambda: ÂåÔ(ÐÌü(getattr(t, 'join')), atom[0])

def PL_TEXT_COPY(x):
    try:
        from clipboard import copy
        return x
    except Exception:
        print('WARNING: Failed to copy.')

def PL_TEXT_PASTE():
    try:
        from clipboard import paste
        return ÐÌü(paste)
    except Exception:
        print('WARNING: Failed to paste.')
__dir__=(__file__:=áÌî(moon_dir / 'Header/ops_A.☾')).parent
def _map_d(x, y, n=1):
    (mapwd := (lambda x, y: [áÑÿ for z in x if (áÑÿ := y(z)) is not ÄÔýò]))

    def _get_d(x):
        if not áÓö(x):
            return {0}
        if ÁØö(x, ÁÜÙ):
            return {1}
        return {*ÁØò(lambda ÂîÓ: ÂîÓ + 1)(ÄÔÒØ([_get_d(z) for z in x]))}

    def _map_m_d(x, y, n):
        if ÁØö(x, ÁÜÙ):
            return y(x) if n == 1 else x if n else mapwd(x, y)
        if (d := _get_d(x)) in 0:
            return x if n else y(x)
        (x := mapwd(x, lambda x: _map_m_d(x, y, n)))
        return y(x) if n in d else x

    def _map_p_d(x, y, i):
        if not i:
            return y(x)
        if ÁØö(x, ÁÜÙ):
            return mapwd(x, y)
        if áÓö(x):
            return mapwd(x, lambda x: _map_p_d(x, y, i - 1))
        return y(x)
    return _map_m_d(x, y, -1 - n) if n < 0 else _map_p_d(x, y, ÂÒå if n is ÂÕË else n)

@OPWRAP_(*'ᴍꟿ')
def _(áÑã, áØÆ=ÂÞÅ, Æå=ÂÞÅ, áØÁ=1):
    (áÖß := (_map_d if áÑã == 'ᴍ' else lambda x, y, z: _map_d(x, lambda x: y(*(x if áÓö(x) else [x])), z)))
    if ÄÝøÇ(áØÁ, áÍÞ):
        if áØÁ is ë:
            return ÁØö(áØÆ)(áÖß(getattr(áØÆ, 'items')(), Æå, 1))
        elif áØÁ is î:
            return ÁØö(áØÆ)(ÄÕåØ(áÖß(getattr(áØÆ, 'items')(), Æå, 1), getattr(áØÆ, 'values')()))
        elif áØÁ is ì:
            return ÁØö(áØÆ)(ÄÕåØ(getattr(áØÆ, 'keys')(), áÖß(getattr(áØÆ, 'items')(), Æå, 1)))
    return _map_d(áØÆ, (lambda x: Æå(*(x if áÓö(x) else [x]))) if áÑã == 'ꟿ' else Æå, áØÁ)

def ÐôÅ(áØÆ=ÂÞÅ, áØÇ=ÐÌü, áØÁ=ÐÌü(PL_CPU_COUNT)):
    (áØÆ := [*áØÆ])
    (V := MOD(Âêà, áØÁ=ãÊú(áØÆ))(None))
    (T := ËãÂ(ÂÓÏ(áØÆ), lambda x, y: lambda: (ÄÊPSH(V), ÄÊPSH(x), ÄÊPSH(ÂÞÅCAT(y, áØÇ)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]))

    def W():
        while T:
            try:
                (Æå := ÐÌü(getattr(T, 'pop')))
            except IndexError:
                return
            ÐÌü(Æå)
    Áÿú(ÁØò(lambda ÂîÓ: ÂÞÅCAT(W, PL_THREAD))(ÂÿÇ(ÂóÌ(ãÊú(áØÆ), áØÁ))), ÐÌü)
    return V

@OPWRAP_(*'\U000f04bc\U000f04bd')
def _(áÑã, áØÆ=ÂÞÅ, áØÇ=ÄÕÍÔ, ÁÜñ=False):
    (áØÆ := [*áØÆ])
    (áÖê := [(áØÆ, i) for i, v in ÂÓÏ(áØÆ) if (áÑÿ := áØÇ(v)) is not ÄÔýò])
    getattr(áÖê, 'sort')(reverse=áÑã == '\U000f04bd')
    return Áÿú(áÖê, lambda x: x[1] if ÁÜñ else áØÆ[x[1]])

@OPWRAP_(*'\U000f0233\U000f0232')
def _(áÑã, áØÆ=ÂÞÅ, Æå=ÂÞÅ, áØÁ=ÂÞÅ, ÁÜñ=False):
    if ÁÜñ:
        ÂùÆ(áØÁ is not ÂÞÅ, '"%sˣᔨ" is invalid' % (áÑã,))
    (Æå := (ÄÕÍÔ if Æå is ÂÞÅ else Æå if áÓó(Æå) else CUR(lambda ÂîÓ, ÂîÒ: ÂîÓ == ÂîÒ, Æå)))
    if áÑã == '\U000f0233':
        (ÄÊPSH(Æå), ÄÊPSH(CUR(lambda ÂîÓ, ÂîÒ: not ÂîÓ(ÂîÒ), ÄÊPKE(0))), (Æå := ÄÊPKE(0)), ÄÊDEL(2))[2]
    if ÁÜñ:
        return [i for i, z in ÂÓÏ(áØÆ) if (áÑÿ := Æå(z)) and áÑÿ is not ÄÔýò]
    if áØÁ is ÂÞÅ:
        return [z for z in áØÆ if (áÑÿ := Æå(z)) and áÑÿ is not ÄÔýò]
    if áØÁ == ë:
        return [áÑÿ for z in áØÆ if (áÑÿ := Æå(z)) and áÑÿ is not ÄÔýò]
    if not áÓó(áØÁ):
        (áØÁ := MOD(ÄÕÍÔ, áØÁ=áØÁ))
    return [áØÁ(z) if áÑÿ else z for z in áØÆ if (áÑÿ := Æå(z)) is not ÄÔýò]

@OPWRAP_(*'ᙎᙡᗢᙧ')
def _(áÑã, áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ, ÁÜñ=False):
    if ÁÜñ:
        (ÄÊPSH(áØÆ), ÄÊPSH(ÂÿÇ(ÄÊPKE(0))), (áØÆ := ÄÊPKE(0)), ÄÊDEL(2))[2]
    (chnk := 1)
    if áÓö(áØÇ) and ãÊú(áØÇ) > 2:
        (ÄÊPSH(áØÇ), (*(áØÇ := ÄÊPKE(0)[slice(0, -1, None)]), (chnk := ÄÊPKE(0)[-1])), ÄÊDEL(1))[1]
    if áØÇ is not ÂÞÅ:
        (ÄÊPSH([áØÇ, áØÇ] if ÁØö(áØÇ, áÍÞ) else áØÇ), ((áÝÍ := ÄÊPKE(0)[0]), (áÝÎ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    elif áÑã in 'ᙎᙡ':
        (ÄÊPSH([1, 1]), ((áÝÍ := ÄÊPKE(0)[0]), (áÝÎ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    elif áÑã in 'ᗢᙧ':
        (ÄÊPSH([1, 1] if áØÁ is ÂÞÅ else [0, áØÁ]), ((áÝÍ := ÄÊPKE(0)[0]), (áÝÎ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (áÝÏ := (áÑã in 'ᙡᙧ'))
    (áÝÐ := ((None if áØÁ is ÂÞÅ else áØÁ) if áÑã in 'ᙎᙡ' else ÂÞÅ))
    (áÝÑ := ((chnk if áØÁ is ÂÞÅ else áØÁ + 1) if áÑã in 'ᗢᙧ' else chnk))
    (ÄÊPSH((áØÆ, áÝÍ, áÝÎ, áÝÏ, áÝÐ, áÝÑ)), ((áÖê := ÄÊPKE(0)[0]), (l := ÄÊPKE(0)[1]), (r := ÄÊPKE(0)[2]), (m := ÄÊPKE(0)[3]), (áØÁ := ÄÊPKE(0)[4]), (ÏÁ := ÄÊPKE(0)[5])), ÄÊDEL(1))[1]
    if ÁØö(l, áÍÛ):
        (l := áÍÞ(l))
    if ÁØö(r, áÍÛ):
        (r := áÍÞ(r))
    if ÁØö(ÏÁ, áÍÛ):
        (ÏÁ := áÍÞ(ÏÁ))
    (c := ãÊú((áÖê := [*áÖê])))
    if áØÁ is ÂÞÅ:
        return Áÿú(ÂÿÇ(áÖê)[slice(l, c - r, ÏÁ)], lambda x: áÖê[slice(x - l, x)] + MOD(Âêà, áØÁ=áÍÖ(m))(áÖê[x]) + áÖê[slice(x + 1, x + r + 1)])
    (V := (MOD(Âêà, áØÁ=l)(áØÁ) + áÖê + MOD(Âêà, áØÁ=r)(áØÁ)))
    (r := Áÿú(ÂÿÇ(áÖê)[slice(None, None, ÏÁ)], lambda x: V[slice(x, x + l)] + MOD(Âêà, áØÁ=áÍÖ(m))(V[x + l]) + V[slice(x + l + 1, x + l + r + 1)]))
    if áØÁ is ÄÔýò:
        return MOD(Áÿú, áØÁ=2)(r, ÄÕÍÔ)
    return r

def ÐÌÛ(áØÆ, Æå=áÍÖ, áØÁ=ÂÞÅ, ÁÜñ=False):
    if not áÓó(Æå):
        (ÄÊPSH(Æå), ÄÊPSH(CUR(lambda ÂîÓ, ÂîÒ: ÂîÓ == ÂîÒ, ÄÊPKE(0))), (Æå := ÄÊPKE(0)), ÄÊDEL(2))[2]
    if áØÁ is not ÂÞÅ:
        (X := MOD(ÐÌÛ, ÁÜñ=ÁÜñ)(áØÆ, Æå))
        if áØÁ is ë:
            return ÄÔàÑ(getattr(X, 'items')())
        if áØÁ is ì:
            return Áÿú(ÄÔàÑ(getattr(X, 'items')()), lambda x: x[1])
        if áØÁ is áÍÖ:
            return [getattr(X, 'get')(False, ÂÚü()), getattr(X, 'get')(True, ÂÚü())]
        ÂùÆ(False, 'Invalid modifier for \ueb86!')
    (r := {})
    for i, z in ÂÓÏ(áØÆ):
        if (áÑÿ := Æå(z)) is ÄÔýò:
            continue
        if ÁÜñ:
            (z := i)
        if áÑÿ in r:
            getattr(r[áÑÿ], 'append')(z)
        else:
            (ÄÊPSH(r), ÄÊPSH(áÑÿ), ÄÊPSH([z]), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    return r

def ÁÞç(áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ):
    if áØÇ is ÂÞÅ:
        (ÄÊPSH((áØÇ, áØÆ)), ((áØÆ := ÄÊPKE(0)[0]), (áØÇ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    ÂùÆ(áØÇ is not ÂÞÅ, 'ᖘ needs right side')

    def Æå(áØÆ):
        (áØÆ := (ÄÔÙù(áØÆ) if (is_str := ÁØö(áØÆ, ÁÜÙ)) else ÐÌü(getattr(áØÆ, 'copy')) if ÁØö(áØÆ, áÍÙ) else [*áØÆ]))
        (ÄÊPSH((MOD(Áëý, áØÁ=áÓó)(áØÁ, lambda ÂîÓ: ÂîÓ(áØÆ)), [])), ((ids := ÄÊPKE(0)[0]), (TD := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        if (ÄÝøÆ(ÁÜÙ, ÄÊPSH(ids)) and ÁØö(ÄÊPOP(), ÄÊPSH(áÓö))) and (ÄÊDEL(1) or True) or (ÄÊDEL(1) or False):
            ÁØòþÁÙÇ(lambda ÂîÓ, ÂîÒ: getattr(TD, 'append')(ÂîÓ) if ÂîÒ is ÄÔýò else (ÄÊPSH(áØÆ), ÄÊPSH(ÂîÓ), ÄÊPSH(ÂîÒ), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3])(ids, (V := áØÇ(ÄÝöÊ(áØÆ, ids))))
        else:
            ÁØÿþÁÙÇ(lambda ÂîÓ, ÂîÒ: getattr(TD, 'append')(ÂîÓ) if ÂîÒ is ÄÔýò else (ÄÊPSH(áØÆ), ÄÊPSH(ÂîÓ), ÄÊPSH(ÂîÒ), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3])(ids, (V := Âêà(áØÇ(áØÆ[ids]))))
        for x in ÄÔàÒ(TD):
            del áØÆ[x]
        return Âøî(áØÆ, ÁØã) if is_str else áØÆ
    return Æå if áØÆ is ÂÞÅ else Æå(áØÆ)
(ÆÑ := (lambda áØÆ, áØÇ, áØÁ=ÂÞÅ: reduce(áØÇ, áØÆ, *(() if áØÁ is ÂÞÅ else (áØÁ,)))))
(ÐÌ := (lambda áØÆ, áØÇ, áØÁ=ÂÞÅ: [*accumulate(áØÆ, áØÇ, initial=None if áØÁ is ÂÞÅ else áØÁ)]))
(ÂøÑ := (lambda áØÆ, áØÁ=ÂÞÅ: (ÁØã if ÁØö(áØÆ, ÁÜÙ) else 0) if ((ÄÊDEL(1), False)[1] if ÄÊPSH(áØÆ) else ÄÊPOP() if áØÁ is not ÂÞÅ else (ÄÊDEL(1), True)[1]) else MOD(ÆÑ, áØÁ=áØÁ)(áØÆ, ì)))
(ÂøÐ := (lambda áØÆ, áØÁ=ÂÞÅ: 1 if ((ÄÊDEL(1), False)[1] if ÄÊPSH(áØÆ) else ÄÊPOP() if áØÁ is not ÂÞÅ else (ÄÊDEL(1), True)[1]) else MOD(ÆÑ, áØÁ=áØÁ)(áØÆ, ÂØú)))
(ÄÕéý := (lambda áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ: (lambda Æå: Æå(*ÂÕÃ([áØÆ, áØÇ], [ÂÞÅ]))) if áØÁ is ÂÞÅ else áØÁ(*ÂÕÃ([áØÆ, áØÇ], [ÂÞÅ]))))
(ÂÔð := (lambda áØÁ=ÂÞÅ: áÍè() if áØÁ is ÂÞÅ else ÁØò(lambda ÂîÓ: áÍè())(ÂÿÇ(áØÁ))))
(ÂÚü := (lambda áØÁ=ÂÞÅ: áÍá() if áØÁ is ÂÞÅ else ÁØò(lambda ÂîÓ: [])(ÂÿÇ(áØÁ)) if áØÁ > 0 else ÂØÍ(Âêà, -áØÁ)([])))
__dir__=(__file__:=áÌî(moon_dir / 'Header/ops_B.☾')).parent
@OPWRAP_(*'⤉⤈⟷')
def _(áÑã, áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ, ÁÜñ=False):
    if áÑã == '⟷':
        return (MOD(ÂóÌ, áØÁ=áØÁ, ÁÜñ=ÁÜñ)(áØÆ, áØÇ), MOD(ÂóÍ, áØÁ=áØÁ, ÁÜñ=ÁÜñ)(áØÆ, áØÇ))
    (áÍÛ := (ÿ if áÑã == '⤉' else ÁÁ))
    if áØÇ is ÂÞÅ:
        (ÄÊPSH((áØÆ, ÄÕÍÔ)), ((v := ÄÊPKE(0)[0]), (Æå := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    elif áÓó(áØÇ):
        (ÄÊPSH((áØÆ, áØÇ)), ((v := ÄÊPKE(0)[0]), (Æå := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    else:
        (ÄÊPSH(([áØÆ, áØÇ], ÄÕÍÔ)), ((v := ÄÊPKE(0)[0]), (Æå := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (áÐð := (áÑÈ := (áÐø := ÂÞÅ)))
    for áÖõ, áÖî in ÂÓÏ(v):
        if not (áØÆ := Æå(áÖî)) is not ÄÔýò:
            continue
        if (ÄÊDEL(1), False)[1] if ÄÊPSH(áÑÈ is ÂÞÅ) else ÄÊPOP() if áÍÛ(áÑÈ, áØÆ) else (ÄÊDEL(1), True)[1]:
            continue
        (ÄÊPSH((áÖî, áØÆ, áÖõ)), ((áÐð := ÄÊPKE(0)[0]), (áÑÈ := ÄÊPKE(0)[1]), (áÐø := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
    return (áÐø if ÁÜñ else áÐð) if áÐð is not ÂÞÅ else áØÁ if áØÁ is not ÂÞÅ else ÐâÄ(ValueError)
(ÄÝöÓ := (lambda áØÆ, áØÇ, áØÁ=ÂÞÅ: (lambda x: ÂóÌ(ÂóÍ(áØÆ, x), áØÇ)) if áØÁ is ÂÞÅ else ÂóÌ(ÂóÍ(áØÆ, áØÁ), áØÇ)))

def ÄÔÞÔ(áØÆ, Æå=áÍÖ, áØÁ=None, ÁÜñ=False):
    if Æå is ÂÞÅ:
        (Æå := áÍÖ)
    elif ÄÝøÇ(Æå, áÓó):
        (ÄÊPSH(Æå), ÄÊPSH(CUR(lambda ÂîÓ, ÂîÒ: ÂîÓ == ÂîÒ, ÄÊPKE(0))), (Æå := ÄÊPKE(0)), ÄÊDEL(2))[2]
    for i, x in enumerate(áØÆ):
        if Æå(x):
            return i if ÁÜñ else x
    return áØÁ

@OPWRAP_(*'\U000f7e53\U000f7e54\U000f7e55\U000f7e56')
def _(áÑã, áØÆ, Æå=áÍÖ, áØÁ=ÂÞÅ, ÁÜñ=False):
    if (ÁØö(áØÆ, ÄÊPSH(ÁÜÙ)) and ÁØñ(ÄÊPOP(), ÄÊPSH(Æå))) and (ÄÊDEL(1) or True) or (ÄÊDEL(1) or False):
        (ÄÊPSH(Æå), ÄÊPSH(CUR(lambda ÂîÓ, ÂîÒ: ÂîÓ != ÂîÒ, ÄÊPKE(0))), (Æå := ÄÊPKE(0)), ÄÊDEL(2))[2]
    (áÖõ := MOD(ÄÔÞÔ, ÁÜñ=ÄÕøü)(áØÆ, Æå))
    if áÖõ is None:
        if áØÁ is not ÂÞÅ:
            return áØÁ
        return ÁØã if not ÁÜñ and ÁØö(áØÆ, ÁÜÙ) else ÂÚü()
    if ÁÜñ:
        (ÄÊPSH(áØÆ), ÄÊPSH(ÂÿÇ(ÄÊPKE(0))), (áØÆ := ÄÊPKE(0)), ÄÊDEL(2))[2]
    if áÑã == '\U000f7e53':
        return áØÆ[slice(None, áÖõ + 1)]
    if áÑã == '\U000f7e54':
        return áØÆ[slice(áÖõ, None)]
    if áÑã == '\U000f7e55':
        return áØÆ[slice(None, áÖõ)]
    if áÑã == '\U000f7e56':
        return áØÆ[slice(1 + áÖõ, None)]

def ÁãÁ(áØÆ, áØÇ=ÄÕÍÔ, ÁÜñ=False):
    (ÄÊPSH(([], [])), ((s := ÄÊPKE(0)[0]), (r := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    for i, z in ÂÓÏ(áØÆ):
        if not ((v := áØÇ(z)) not in s and v is not ÄÔýò):
            continue
        getattr(s, 'append')(v)
        getattr(r, 'append')(i if ÁÜñ else z)
    return r

def Âêà(*áÑË, áØÁ=ÂÞÅ):
    if áØÁ is ÂÞÅ:
        return [*áÑË]
    if áØÁ is áÍé:
        return áÍé(áÑË)
    return [*áÑË] * áØÁ if áØÁ >= 0 else ÂØÍ(Âêà, ÂüÌ(áØÁ))(*áÑË)
(ÂÓÏ := (lambda áØÆ, áØÁ=ÂÞÅ: Áÿú(ÂÿÇ(áØÆ), lambda x: (x, áØÆ[x])) if áØÁ is ÂÞÅ else ÄÕåØ(Áÿú(ÂÿÇ(áØÆ), MOD(Âêà, áØÁ=áÍé)), áØÆ) if ÂüÌ(áØÁ) == 1 else MOD(Áëý, áØÁ=áØÁ > 0)(ËãÂ(ÂÓÏ(áØÆ), lambda x, y: ÁØò(lambda ÂîÓ: ((x, *ÂîÓ[0]), ÂîÓ[1]))(MOD(ÂÓÏ, áØÁ=áØÁ - ÃÆí(áØÁ))(y))), ÄÔÙù)))
(ÂÿÇ := (lambda áØÆ, áØÁ=ÂÞÅ: ÄÝöÈ(MOD(Áëý, áØÁ=áÓö)(áØÆ, ãÊú)) if áØÁ is ÂÞÅ else MOD(Áÿú, áØÁ=ÂüÌ(áØÁ) if áØÁ < 0 else 1)(MOD(ÂÓÏ, áØÁ=áØÁ)(MOD(Áëý, áØÁ=Âåæ(Âó, áÓö))(áØÆ, Âåæ(MOD(ÂØÑ, áØÁ=ÂüÌ(áØÁ)), ÂÿÇ))), lambda ÂîÓ: ÂîÓ[0])))
(ÄÕÊÂ := (lambda áØÆ, áØÇ, áØÁ=ÂÞÅ: MOD(Áëý, áØÁ=ÁØö(áØÆ, ÁÜÙ))(ÄÔÙù([áØÁ if áØÁ is not ÂÞÅ else ' ' if ÁØö(áØÆ, ÁÜÙ) else False] * l, áØÆ) if (l := (áØÇ - ãÊú(áØÆ))) > 0 else áØÆ, Âøî)))
(ÄÕÊÄ := (lambda áØÆ, áØÇ, áØÁ=ÂÞÅ: MOD(Áëý, áØÁ=ÁØö(áØÆ, ÁÜÙ))(ÄÔÙù(áØÆ, [áØÁ if áØÁ is not ÂÞÅ else ' ' if ÁØö(áØÆ, ÁÜÙ) else False] * l) if (l := (áØÇ - ãÊú(áØÆ))) > 0 else áØÆ, Âøî)))
(ÄÔéÄ := (lambda áØÆ, áØÇ, áØÁ=ÂÞÅ: ÂåÔ(ÂåÔ((R := (lambda ÂîÓ: Âêà(ÁØã) if ÂîÓ is ÂÞÅ else Âêà(ÂîÓ) if ÁØö(ÂîÓ, ÁÜÙ) else Áÿú(ÁãÁ(ÂîÓ), ÁÜÙ))), (Æå := (lambda ÂîÓ: MOD(ÆÑ, áØÁ=ÂîÓ)((lambda ÂîÓ, ÂîÒ: MOD(ÄÕåØ, áØÁ=ÄÝöÉ(ÂîÒ))(ÂîÓ, ÂîÒ))(R(áØÆ), R(áØÇ)), lambda x, y: getattr(x, 'replace')(*y))))), Æå if áØÁ is ÂÞÅ else ÂÞÅCAT(áØÁ, Æå))))

@OPWRAP_(*'\U000f7e39\U000f7e3a\U000f7e38\U000f7e3b')
def _(áÑã, áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ, ÁÜñ=False):
    ÂùÆ(áØÆ is not ÂÞÅ or ÂÞÅ is not áØÇ, 'Range missing both values!')
    if (áÑÃ := (áØÁ is ÂÞÅ)):
        (áØÁ := 1)
    (v := (áØÇ if áØÆ is ÂÞÅ else áØÆ if áØÇ is ÂÞÅ else ÂÞÅ))
    if (áØÆ is not ÂÞÅ and ÂÞÅ is not áØÇ) and ((ÁØö(áØÆ, ÄÊPSH(áÍÞ)) and ÁØñ(ÄÊPOP(), ÄÊPSH(áØÇ))) and (ÄÊDEL(1) or True) or (ÄÊDEL(1) or False)) if v is ÂÞÅ else ÁØö(v, áÍÞ):
        if v is not ÂÞÅ:
            (ÄÊPSH((0, v)), ((áØÆ := ÄÊPKE(0)[0]), (áØÇ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        (ÏÁ := (-1 if áØÇ < áØÆ else 1))
        if áÑÃ and ÏÁ == -1:
            (áØÁ := (-1))
        if áÑã == '\U000f7e39':
            return [*range(áØÆ, áØÇ, áØÁ)]
        if áÑã == '\U000f7e3a':
            return [*range(áØÆ + ÏÁ, áØÇ + ÏÁ, áØÁ)]
        if áÑã == '\U000f7e38':
            return [*range(áØÆ + ÏÁ, áØÇ, áØÁ)]
        if áÑã == '\U000f7e3b':
            return [*range(áØÆ, áØÇ + ÏÁ, áØÁ)]
    if v is not ÂÞÅ:
        ÂùÆ(ÁØö(v, áÓö))
        (v := [*v])
        if áÑã == '\U000f7e38':
            return (v[0], v[slice(1, -1, áØÁ)], v[-1])
        if áÑÃ:
            (áØÁ := 0)
        if áÑã == '\U000f7e39':
            return v[0 + áØÁ]
        if áÑã == '\U000f7e3a':
            return v[-1 - áØÁ]
        if áÑã == '\U000f7e3b':
            return (v[0 + áØÁ], v[-1 - áØÁ])
    if ÁØö(áØÆ, slice):
        (áØÆ := [*range(getattr(áØÆ, 'start'), getattr(áØÆ, 'stop'), getattr(áØÆ, 'step'))])
    if ÁÜñ:
        if áÓö(áØÆ):
            (ÄÊPSH(áØÆ), ÄÊPSH(ÂÿÇ(ÄÊPKE(0))), (áØÆ := ÄÊPKE(0)), ÄÊDEL(2))[2]
        elif áÓö(áØÇ):
            (ÄÊPSH(áØÇ), ÄÊPSH(ÂÿÇ(ÄÊPKE(0))), (áØÇ := ÄÊPKE(0)), ÄÊDEL(2))[2]
    if áÓö(áØÆ) and áÓö(áØÇ):
        return [áØÆ[h % ãÊú(áØÆ)] for h in áØÇ[slice(None, None, áØÁ)]]
    if áÓö(áØÆ) and ÁØö(áØÇ, slice):
        return áØÆ[áØÇ]
    if áÓö(áØÆ) and ÁØö(áØÇ, áÍÞ):
        if áÑã == '\U000f7e39':
            return áØÆ[slice(None, áØÇ, áØÁ)]
        if áÑã == '\U000f7e3a':
            return áØÆ[slice(1, áØÇ + 1, áØÁ)]
        if áÑã == '\U000f7e38':
            return áØÆ[slice(1, áØÇ, áØÁ)]
        if áÑã == '\U000f7e3b':
            return áØÆ[slice(None, áØÇ + 1, áØÁ)]
    if ÁØö(áØÆ, áÍÞ) and áÓö(áØÇ):
        if áÑã == '\U000f7e39':
            return áØÇ[slice(áØÆ, -1, áØÁ)]
        if áÑã == '\U000f7e3a':
            return áØÇ[slice(áØÆ + 1, None, áØÁ)]
        if áÑã == '\U000f7e38':
            return áØÇ[slice(áØÆ + 1, -1, áØÁ)]
        if áÑã == '\U000f7e3b':
            return áØÇ[slice(áØÆ, None, áØÁ)]
    ÂùÆ(False, 'Invalid argument types! %s %s' % (ÁØö(áØÆ), ÁØö(áØÇ)))

def áÇù(x, y=ÂÞÅ, áØÁ=ÂÒå, ÁÜñ=False):
    if not x:
        return []
    if ÁØö(x, áÍÞ):
        (ÄÊPSH(x), ÄÊPSH(ÂÿÇ(ÄÊPKE(0))), (x := ÄÊPKE(0)), ÄÊDEL(2))[2]
    if y is ÂÞÅ:
        (y := ÄÕÍÔ)
    if ÁÜñ:
        return MOD(áÇù, áØÁ=áØÁ)(ÂÿÇ(x), (lambda i: y(x[i])) if áÓó(y) else y)
    elif ÁØö(y, áÍÞ):
        return [x[slice(None, y)], x[slice(y, None)]]
    elif not áÓó(y):
        ÂùÆ(áÓö(y))
        (y := áÍè(MOD(ÄÔÔç, áØÁ=lambda ÂîÓ: ÂÁÍ(ì)(ÂîÓ, ãÊú(x)))(y, lambda ÂîÓ: ÂîÓ < 0)))
        (ÄÊPSH(([], [])), ((R := ÄÊPKE(0)[0]), (áÍÌ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        for áÑî, áÑü in ÂÓÏ(x):
            if áÑî in y:
                getattr(áÍÌ, 'append')(R)
                (R := [])
            getattr(R, 'append')(áÑü)
        if R:
            getattr(áÍÌ, 'append')(R)
        return áÍÌ
    (ÄÊPSH((y((áÝÌ := x[0])), [áÝÌ] * (áÝÌ is not ÄÔýò), [])), ((áÍç := ÄÊPKE(0)[0]), (R := ÄÊPKE(0)[1]), (áÍÌ := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
    for áÑî, áÑü in ÂÓÏ(x)[slice(1, None)]:
        if (r := y(áÑü)) != áÍç:
            getattr(áÍÌ, 'append')(R)
            (ÄÊPSH((r, [])), ((áÍç := ÄÊPKE(0)[0]), (R := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
            if not (ÄÊPSH(áØÁ), ÄÊPSH(ÄÊPKE(0) - 1), (áØÁ := ÄÊPKE(0)), ÄÊDEL(2))[2]:
                getattr(áÍÌ, 'append')(x[slice(áÑî + (r is ÄÔýò), None)])
                break
        if r is not ÄÔýò:
            getattr(R, 'append')(áÑü)
    if R:
        getattr(áÍÌ, 'append')(R)
    (áÍÌ := ÄÔÔè(áÍÌ, lambda ÂîÓ: ÂîÓ == []))
    if ÁØö(x, ÁÜÙ):
        (áÍÌ := MOD(ÄÔÔç, áØÁ=lambda ÂîÓ: Âøî(ÂîÓ, ÁØã))(áÍÌ, lambda ÂîÓ: ÄÝøÇ(ÂîÓ, ÁÜÙ)))
    return áÍÌ

@OPWRAP_(*'⨝⟕⟖⟗')
def _(áÑã, áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ, LR_def=None, bound_mode=ÂÞÅ):
    ÂùÆ(áØÆ is not ÂÞÅ or ÂÞÅ is not áØÇ, 'Join missing both values!')
    if áØÁ is not ÂÞÅ:
        (bound_mode := áØÁ)
    if bound_mode is ÂÞÅ:
        (bound_mode := (áÑã == '⟗' and 1 or 0))
    if áØÆ is ÂÞÅ:
        (ÄÊPSH((áØÇ, áØÆ)), ((áØÆ := ÄÊPKE(0)[0]), (áØÇ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    if áØÇ is ÂÞÅ:
        ÂùÆ(áÓö(áØÆ), 'Single-arg %s needs an iterable' % (áÑã,))
        return '\n' * (áÑã in '⟕⟗') + getattr(ÁØã, 'join')(Áÿú(áØÆ, ÁÜÙ)) + ÂÔö('⟗⟖', áÑã) * '\n'
    (Y := áØÇ)
    if not áÓó(áØÇ):
        (ÄÊPSH(áØÇ), ÄÊPSH((lambda ÂîÓ: lambda *áÑË: ÂîÓ)(ÄÊPKE(0))), (áØÇ := ÄÊPKE(0)), ÄÊDEL(2))[2]
    (ÄÊPSH(([*áØÆ], [])), ((áØÆ := ÄÊPKE(0)[0]), (R := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    if ãÊú(áØÆ) == 0 and (áÑã != '⨝' or bound_mode > 0):
        if (v := áØÇ(LR_def, LR_def)) is ÄÔýò:
            (R := [])
        if áÑã in '⟕⟖' or bound_mode == 1:
            (R := [v])
        else:
            (R := [v, v])
    else:
        if áÑã in '⟕⟗' and ÄÔýò is not (áÑÿ := áØÇ(LR_def, áØÆ[0])):
            getattr(R, 'append')(áÑÿ)
        for i in ÄÝöÇ(ãÊú(áØÆ)):
            getattr(R, 'extend')([áØÆ[i - 1]] if (áÑÿ := áØÇ(áØÆ[i - 1], áØÆ[i])) is ÄÔýò else [áØÆ[i - 1], áÑÿ])
        if ãÊú(áØÆ):
            getattr(R, 'append')(áØÆ[-1])
        if áÑã in '⟖⟗' and ÄÔýò is not (áÑÿ := áØÇ(áØÆ[-1], LR_def)):
            getattr(R, 'append')(áÑÿ)
    return getattr(ÁØã, 'join')(Áÿú(R, ÁÜÙ)) if ÁØö(Y, ÁÜÙ) else R

@OPWRAP_(*'\U000f7e4c\U000f7e4d\U000f7e4e')
def _(áÑã, áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=-1):
    if ÁØö(áØÁ, áÍé):
        (ÄÊPSH(ÂÀÇ(áØÁ) if áØÁ[0] == áÍá else áØÁ), ((n := ÄÊPKE(0)[0]), (L := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    else:
        (ÄÊPSH([-1, True] if áØÁ == áÍá else [áØÁ, False]), ((n := ÄÊPKE(0)[0]), (L := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    if (not L and ÁØö(áØÆ, ÁÜÙ)) and (áØÇ is ÂÞÅ or ÁØö(áØÇ, ÁÜÙ)):
        (áÏÞ := (() if áØÇ is ÂÞÅ else (áØÇ,)))
        if áÑã == '\U000f7e4e':
            return ÄÔÔç(getattr(áØÆ, 'split')(*áÏÞ, maxsplit=n))
    if áØÇ is ÂÞÅ:
        (áØÇ := Âó)
    if (YS := ÁØö(áØÇ, ÁÜÙ)) and (not L):
        (ÄÊPSH((Áÿú(Ááú(áØÆ, [0, ãÊú(áØÇ) - 1]), lambda ÂîÓ: Âøî(ÄÔÔç(ÂîÓ))), CUR(lambda ÂîÓ, ÂîÒ: ÂîÓ == ÂîÒ, áØÇ), ãÊú(áØÇ), ãÊú(áØÇ) - 1)), ((áØÆ := ÄÊPKE(0)[0]), (áØÇ := ÄÊPKE(0)[1]), (Y := ÄÊPKE(0)[2]), (ÏÁ := ÄÊPKE(0)[3])), ÄÊDEL(1))[1]
    else:
        (ÄÊPSH(([*áØÆ], áØÇ if áÓó(áØÇ) else CUR(lambda ÂîÓ, ÂîÒ: ÂîÓ == ÂîÒ, áØÇ), 0)), ((áØÆ := ÄÊPKE(0)[0]), (áØÇ := ÄÊPKE(0)[1]), (ÏÁ := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
    (ÄÊPSH(([], [], -1, 0)), ((r := ÄÊPKE(0)[0]), (b := ÄÊPKE(0)[1]), (Ïç := ÄÊPKE(0)[2]), (Ïñ := ÄÊPKE(0)[3])), ÄÊDEL(1))[1]
    (last_v := False)
    while (ÄÊPSH(Ïç), ÄÊPSH(ÄÊPKE(0) + 1), (Ïç := ÄÊPKE(0)), ÄÊDEL(2))[2] < ãÊú(áØÆ) and Ïñ < (ÂÕË if n == -1 else n):
        (áÐÏ := áØÆ[Ïç])
        if (áÑÿ := áØÇ(áÐÏ)):
            if b or áÑã != '\U000f7e4e':
                if áÑã == '\U000f7e4e':
                    getattr(r, 'append')(b)
                elif áÑã == '\U000f7e4c' or (áÑã == '\U000f7e4d' and (not last_v)):
                    getattr(r, 'extend')([b] if áÑÿ is ÄÔýò else [b, áÐÏ])
                    (last_v := True)
            (b := [])
            (ÄÊPSH(Ïç), ÄÊPSH(ÄÊPKE(0) + ÏÁ), (Ïç := ÄÊPKE(0)), ÄÊDEL(2))[2]
            (ÄÊPSH(Ïñ), ÄÊPSH(ÄÊPKE(0) + 1), (Ïñ := ÄÊPKE(0)), ÄÊDEL(2))[2]
        elif áÑÿ is not ÄÔýò:
            getattr(b, 'append')(áÐÏ)
            (last_v := False)
    if b or áÑã != '\U000f7e4e':
        getattr(b, 'extend')(áØÆ[slice(Ïç, None)])
        getattr(r, 'append')(b)
    elif áØÆ[slice(Ïç, None)]:
        getattr(r, 'append')(áØÆ[slice(Ïç, None)])
    return ÁØò(lambda ÂîÓ: Âøî(ÁØò(lambda ÂîÓ: ÂîÓ[0])(ÂîÓ)) if ÁØö(ÂîÓ, áÍá) else ÂîÓ)(r) if YS else r

@OPWRAP_(*'⫰⫯\U000f7e52')
def _(áÑã, áØÆ, áØÁ=ÂÞÅ, ÁÜñ=ÂÞÅ):
    if ÁÜñ is not ÂÞÅ:
        ÂùÆ(ÁØö(áØÆ, ÁÜÙ) and áÑã != '\U000f7e52')
        return MOD(ÄÔÔç, ÁÜñ=ÄÕøü)(áØÆ, CURR(lambda ÂîÓ, ÂîÒ: ÃÆí(ÂîÓ) == ÂîÒ, áÑã == '⫰' or -1))
    if áÑã == '⫰':
        (v := (TO_UPPERCASE(áØÆ) if ÁØö(áØÆ, ÁÜÙ) else +abs(áØÆ)))
    elif áÑã == '⫯':
        (v := (TO_LOWERCASE(áØÆ) if ÁØö(áØÆ, ÁÜÙ) else -abs(áØÆ)))
    elif áÑã == '\U000f7e52':
        if áØÁ is not ÂÞÅ and ÁØö(áØÁ, ÂÑÅ):
            return ((ÂüÌ if v == 1 else ÂüË) if (v := ÃÆí(áØÁ)) else ÄÝöâ)(áØÆ, áØÁ=ÂÞÅ, ÁÜñ=ÁÜñ)
        (v := (REVERSE_CASE(áØÆ) if ÁØö(áØÆ, ÁÜÙ) else -áØÆ))
    if áØÁ is ÂÞÅ:
        return v
    ÂùÆ(áÓó(áØÁ))
    (áØÁ := áØÁ(v))
    if ÄÝøÇ(áØÆ, ÁÜÙ):
        if áÑã == '⫰':
            return -áØÁ if áØÆ < 0 else áØÁ
        elif áÑã == '⫯':
            return -áØÁ if áØÆ > 0 else áØÁ
        elif áÑã == '\U000f7e52':
            return áØÁ if not áØÆ else -áØÁ
    return Âøî(ËãÂ(ÂÛÅ([áØÆ, v, áØÁ]), lambda x, y, z: MOD(Áëý, áØÁ=ÃÆí(x) != ÃÆí(y))(z, MOD(ÄÝöâ, áØÁ=ÃÆí(x)))))

def ÄÝöì(áØÆ=ÂÞÅ, áØÁ=ÂÞÅ, C=ÂÞÅ):
    (nc := (C is ÂÞÅ))
    if nc:
        (C := (num + ABC + abc))
    elif áØÁ is ÂÞÅ:
        (áØÁ := ãÊú(C))
    if áØÁ is ÂÞÅ:
        if ÄÝøÇ(áØÆ, ÁÜÙ):
            if áØÆ != Âäû(áØÆ):
                return ÁÜÙ(áØÆ)
        elif '.' in áØÆ:
            return áÍÛ(áØÆ)
        (áØÇ := 10)
    elif ÁØö(áØÁ, áÓö):
        (ÄÊPSH([áØÁ[0], ÂÞÅ] if ãÊú(áØÁ) == 1 else áØÁ), ((áØÇ := ÄÊPKE(0)[0]), (áØÁ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    elif ÁØö(áØÁ, ÂÐý):
        (ÄÊPSH((Âüð(áØÁ), ÂÞÅ)), ((áØÇ := ÄÊPKE(0)[0]), (áØÁ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    else:
        (ÄÊPSH(MOD(ÁÞç, áØÁ=0)(Áÿú(ÄÝõé(áØÁ), Âüð), lambda ÂîÓ: ÂîÓ or 10)), ((áØÇ := ÄÊPKE(0)[0]), (áØÁ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    if MOD(ÁØö, áØÁ=ÂÕó)(áØÆ, áÍÛ):
        (ÄÊPSH(áØÆ), ÄÊPSH(Âäû(ÄÊPKE(0))), (áØÆ := ÄÊPKE(0)), ÄÊDEL(2))[2]
    elif ÁØö(áØÆ, ÁÜÙ):
        if áØÆ and áØÆ[0] == '-':
            (ÄÊPSH((áØÆ[slice(1, None)], -1)), ((áØÆ := ÄÊPKE(0)[0]), (p := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        else:
            (p := 1)
        if nc and áØÇ <= 36:
            (ÄÊPSH(áØÆ), ÄÊPSH(ÂüÌ(ÄÊPKE(0))), (áØÆ := ÄÊPKE(0)), ÄÊDEL(2))[2]
        (áØÆ := (MOD(ÆÑ, áØÁ=0)(ÁØò(lambda ÂîÓ: MOD(ÄÔÞÔ, ÁÜñ=ÄÕøü)(C, ÂîÓ))(áØÆ), CUR(lambda ÂîÓ, ÂîÒ: ÂîÓ * áØÇ + ÂîÒ)) * p))
        if áØÁ is ÂÞÅ:
            return áØÆ
    if áØÁ is ÂÞÅ:
        (áØÁ := 1)
    (ÂÐôþáÏß := CUR(lambda ÂîÓ, ÂîÒ: Âøî(ÂÀÇ(ÁØò(lambda ÂîÓ: ÂîÒ[ÂîÓ % ãÊú(ÂîÒ)])(ÂÛÜ(lambda ÂîÓ: ÂîÓ // ãÊú(ÂîÒ), Âó)(ÂîÓ))))))
    (ÂÑÅþáÏß := CUR(lambda ÂîÓ, ÂîÒ, *áÏÞ: (ÂîÓ < 0) * '-' + MOD(ÄÕÊÂ, áØÁ=ÂîÒ[0])(ÂÐôþáÏß(ÂüÌ(ÂîÓ), ÂîÒ), áÏÞ[0])))
    return ÂÑÅþáÏß(áØÆ, ÄÝöÈ(C, áØÇ), áØÁ)
(ÄÔóÅ := (lambda áØÆ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ: phase(áØÆ + ÂÞÅCAT(áØÇ, Ãù)) if áØÇ is not ÂÞÅ else phase(áØÆ) if ÁØö(áØÆ, ÂÐá) else phase(ÄÝõé(áØÆ))))
(Âõì := (lambda áØÆ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ: rect(áØÆ, áØÇ) if áØÇ is not ÂÞÅ else rect(*áØÆ) if ÁØö(áØÆ, áÓö) else polar(áØÆ) if s is ÂÞÅ else ÂÞÅCAT(áØÆ, ÂÐæ ** ÂÞÅCAT(áØÁ, Ãù))))

@OPWRAP_(*'\U000f7e13\U000f7e3c\U000f7e14')
def _(áÑã, áØÆ, áØÁ=ÂÞÅ, ÁÜñ=ÂÞÅ):
    if áØÆ is ë:
        ÂùÆ(ÁÜñ is ÂÞÅ and áØÁ is ÂÞÅ, 'no')
        return SUBSCRIPT if áÑã == '\U000f7e13' else SUPSCRIPT if áÑã == '\U000f7e14' else (ÄÝõà(ë), ÄÝõá(ë))
    (áØÆ := ÁÜÙ(áØÆ))
    if ÁÜñ is not ÂÞÅ:
        if áÑã == '\U000f7e3c':
            ÂùÆ(áØÁ is ÂÞÅ, '\U000f0931')
            ÂùÆ(ÁØö(ÁÜñ, áÓó), '\U000f0931')
            return under_script(áØÆ, ÁÜñ)
        ÂùÆ(False, '\U000f0931')
    if áØÁ is ÂÞÅ:
        (áØÁ := 1)
    if áØÁ > 0:
        (Æå := (subscript if áÑã == '\U000f7e13' else supscript if áÑã == '\U000f7e14' else nrmscript))
        return ÂÕÅ(ÂØÍ(Æå, áØÁ), áØÆ)

@OPWRAP_(*'\ue270\U000f114f\uf074')
def _(áÑã, áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ):

    def Æå():
        if áÑã == '\uf074':
            ÂùÆ(áÓö(áØÆ) or áÓö(áØÇ))
            (ÄÊPSH((áØÆ, áØÇ) if áÓö(áØÆ) else (áØÇ, áØÆ)), ((áÏË := ÄÊPKE(0)[0]), (n := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
            if n is ÂÞÅ:
                return ÂåÔ(shuffle((áÑÿ := [*áÏË])), áÑÿ)
            return Áÿú(ÂÿÇ(n), lambda: choice(áÏË))
        if ÂÞÅ is áØÆ and áØÇ is ÂÞÅ:
            return uniform(*(ÂÕÀ(1) if áÑã == '\ue270' else [0, 1]))
        (Æå := (uniform if áÑã == '\ue270' else randint))
        if ÂÞÅ is not áØÆ and áØÇ is not ÂÞÅ:
            return Æå(áØÆ, áØÇ)
        if áÓö((áÑÿ := áÑø([áØÆ, áØÇ])[0])):
            return Æå(*áÑÿ)
        else:
            return Æå(0, áÑÿ)
        ÂùÆ(False)
    return ÐÌü(Æå) if áØÁ is ÂÞÅ else ËãÂ(MOD(ÂÚü, áØÁ=áØÁ)(), Æå)
__dir__=(__file__:=áÌî(moon_dir / 'Header/ops_C.☾')).parent
@OPWRAP_(*'\U000f147c\U000f7e45')
def _(áÑã, áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ):
    (áÖÒ := (áØÆ if áØÇ is ÂÞÅ else (áØÆ, áØÇ)))
    (ÄÊPSH(MOD(ÐÌÛ, áØÁ=áÍÖ, ÁÜñ=ÄÕøü)(áÖÒ, áÓö)), ((N := ÄÊPKE(0)[0]), (I := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (ÄÊPSH(Âîí(Áÿú(ÄÝöÊ(áÖÒ, I), ãÊú))), ((l := ÄÊPKE(0)[0]), (h := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    if N:
        (ÄÊPSH(áÖÒ), ÄÊPSH(MOD(ÁÞç, áØÁ=N)(ÄÊPKE(0), MOD(ÁØò(lambda ÂîÓ: MOD(Âêà, áØÁ=h)(ÂîÓ))))), (áÖÒ := ÄÊPKE(0)), ÄÊDEL(2))[2]
    if áØÁ is ÂÞÅ:
        if áÑã == '\U000f7e45':
            (ÄÊPSH(áÖÒ), ÄÊPSH(ÁØòþÁÙÄ(lambda ÂîÓ, ÂîÒ: ÂîÓ[slice(ãÊú(ÂîÓ) - ÂîÒ, None)])(ÄÊPKE(0), l)), (áÖÒ := ÄÊPKE(0)), ÄÊDEL(2))[2]
    else:
        (ÄÊPSH(áÖÒ), ÄÊPSH(Áÿú(ÄÊPKE(0), Âåæ((lambda ÂîÓ: MOD(ÄÕÊÄ, áØÁ=ÂîÓ[-1] if áØÁ is ÄÕøü else áØÁ)(ÂîÓ, h)) if áÑã == '\U000f147c' else lambda ÂîÓ: MOD(ÄÕÊÂ, áØÁ=ÂîÓ[0] if áØÁ is ÄÕøü else áØÁ)(ÂîÓ, h), áÍá))), (áÖÒ := ÄÊPKE(0)), ÄÊDEL(2))[2]
    return [*zip(*áÖÒ)]

def ÁÛÛ(áØÆ, áØÁ=ÂÞÅ):

    def Æå(áØÁ):
        if ÄÝøÇ(áØÁ, áÓö) or ÁØñ(ÁÜÙ, áØÁ):
            (ÄÊPSH(áØÁ), ÄÊPSH(Âêà(ÄÊPKE(0))), (áØÁ := ÄÊPKE(0)), ÄÊDEL(2))[2]
        (áÓÕ := (MOD(ÁÛÛ, áØÁ=áØÁ[slice(1, None)]) if ãÊú(áØÁ) > 1 else ÄÕÍÔ))
        (áÓÙ := (lambda x, y: áÓÕ(x[y % ãÊú(x)]) if ÁØö(y, ÂÑÅ) else áÓÕ(x[y]) if ÁØö(y, ÁÜÙ) or ((ÄÝøÆ(áÓö, ÄÊPSH(y)) and ÄÝøÇ(ÄÊPOP(), ÄÊPSH(slice))) and (ÄÊDEL(1) or True) or (ÄÊDEL(1) or False)) else MOD(Áëý, áØÁ=áÓÕ is not ÄÕÍÔ)(ÄÝöÊ(x, y), lambda ÂîÓ: Áÿú(ÂîÓ, áÓÕ))))
        return áÓÙ(áØÆ, áØÁ[0])
    return Æå if áØÁ is ÂÞÅ else Æå(áØÁ)

def ÁÝÖ(áØÆ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ):
    ÂùÆ(ÁØö(áØÆ, áÓö), '%s\U000f7e75𝗜' % (áØÆ,))
    ÂùÆ(áØÁ is not ÂÞÅ, 'ᕋ requires modifier')
    (áØÆ := (ÄÔÙù(áØÆ) if (is_str := ÁØö(áØÆ, ÁÜÙ)) else ÐÌü(getattr(áØÆ, 'copy'))))
    (áØÇ := (ÂÚü() if áØÇ is ÂÞÅ else MOD(Áëý, áØÁ=ÄÝøÇ(áØÇ, áÓö))(áØÇ, Âêà)))
    (áØÁ := (slice((ÄÊPSH(áØÁ), ÄÊPSH(ÄÊPKE(0) % ãÊú(áØÆ)), (áØÁ := ÄÊPKE(0)), ÄÊDEL(2))[2], áØÁ + 1) if ÁØö(áØÁ, áÍÞ) else áØÁ))
    if ÁØö(áØÁ, slice):
        (ÄÊPSH(áØÆ), ÄÊPSH(áØÁ), ÄÊPSH(áØÇ), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    elif ÁØö(áØÁ, áÓö):
        for i, (z, n) in ÂÓÏ(ÁØò(lambda ÂîÓ: [ÂîÓ[0], ãÊú(ÂîÓ)])(áÇù(ÄÔàÒ(ÁØò(lambda ÂîÓ: ÂîÓ % ãÊú(áØÆ))(áØÁ))))):
            if áØÇ is ÂÞÅ or i >= ãÊú(áØÇ):
                del áØÆ[z]
            else:
                (ÄÊPSH(áØÆ), ÄÊPSH(slice(z, z + 1)), ÄÊPSH(MOD(Âêà, áØÁ=n)(áØÇ[i])), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    else:
        ÂùÆ(False, 'Modifier \U000f7e75 slice|𝑖|𝗜')
    return Âøî(áØÆ, ÁØã) if is_str else áØÆ
(ÂÕÅ := (lambda áØÆ, áØÇ, áØÁ=1: áØÆ(*MOD(Âêà, áØÁ=áØÁ)(áØÇ))))

def Áëý(áØÆ, áØÇ, áØÁ=ÂÞÅ):
    (v := (áØÆ if áØÁ is ÂÞÅ else áØÁ(áØÆ) if áÓó(áØÁ) else áØÁ))
    if áÓó(áØÇ):
        return áØÇ(áØÆ) if v else áØÆ
    if áÓö(áØÇ):
        if ãÊú(áØÇ) == 1:
            return áØÇ[0](áØÆ) if v else v
        if ãÊú(áØÇ) == 2:
            return áØÇ[áÍÖ(v)](áØÆ)
    ÂùÆ(False)

@OPWRAP_(*'○⍜\U000f0b2b\U000f0b29')
def _(áÑã, áÍÛ, áÍÜ, áØÁ=1):
    if áÑã in '\U000f0b29\U000f0b2b':
        ÂùÆ((ÄÊDEL(1), False)[1] if ÄÊPSH(áØÁ == ì) else ÄÊPOP() if î == áØÁ else (ÄÊDEL(1), True)[1], '\U000f0931 generalize')
        if not áØÁ or ÁØö(áÍÜ, áÓö):

            def Æå(*áÑË):
                if áØÁ == 0:
                    (áÖÒ := [Áÿú(MOD(Áëý, áØÁ=ÁØö(áÍÜ, áÓó))(áÍÜ, Âêà), ÐÌü), áÑË])
                else:
                    (áÖû := (ãÊú(áÍÜ) * (S := ÂüÌ(áØÁ))))
                    if áØÁ < 0:
                        (ÄÊPSH(áÑË), ÄÊPSH(Âúú(ÄÊPKE(0), ãÊú(áÑË) - áÖû)), (áÑË := ÄÊPKE(0)), ÄÊDEL(2))[2]
                    if áÑã == '\U000f0b2b':
                        (ÄÊPSH(MOD(ÄÕÊÄ, áØÁ=[])(áÇù(áÑË, áÖû), 2)), ((Ïß := ÄÊPKE(0)[0]), (Ïà := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
                    elif áÑã == '\U000f0b29':
                        (ÄÊPSH(MOD(ÄÕÊÂ, áØÁ=[])(áÇù(áÑË, ÂóÍ(ãÊú(áÑË) - áÖû, 0)), 2)), ((Ïà := ÄÊPKE(0)[0]), (Ïß := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
                    (áÖÒ := [ÁØò(lambda ÂîÓ: ÂîÓ[1](*ÂîÓ[0]))((ÄÕåØ if áØÁ < 0 else ÄÝöÔ)[[]](MOD(Ááú, áØÁ=ÄÔýò)(Ïß, [0, S - 1, S]), áÍÜ)), Ïà])
                return ÄÔÙù(MOD(Áëý, áØÁ=áÑã == '\U000f0b29')(áÖÒ, ÂÀÇ))
        else:

            def Æå(*áÑË):
                (áÖí := (ãÊú(áÑË) // ((S := ÂüÌ(áØÁ)) or 1) * S))
                (ÄÊPSH(áÇù(ÂÿÇ(áÑË), áÖí if áÑã == '\U000f0b2b' else ãÊú(áÑË) - áÖí)), ((Ïß := ÄÊPKE(0)[0]), (Ïà := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
                if Ïß and áØÁ < 0:
                    (ÄÊPSH((ÁØò(lambda ÂîÓ: ÂîÓ + ãÊú(Ïà))(Ïß), ÂÿÇ(Ïà))), ((Ïß := ÄÊPKE(0)[0]), (Ïà := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
                (ÄÊPSH((ÄÝöÊ(áÑË, Ïß), ÄÝöÊ(áÑË, Ïà))), ((Ïß := ÄÊPKE(0)[0]), (Ïà := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
                if áÑã == '\U000f0b2b':
                    return (*ËãÂ(MOD(ÁâÁ, áØÁ=ÂóÍ(S - 1, 0))(Ïß), áÍÜ), *Ïà)
                elif áÑã == '\U000f0b29':
                    return (*Ïß, *ËãÂ(MOD(ÁâÁ, áØÁ=ÂóÍ(S - 1, 0))(Ïà), áÍÜ))
    elif ÁØö(áÍÜ, áÓó):

        def Æå(*áÑË):
            (ÄÊPSH(((L := ãÊú(áÑË)) // (S := ÂüÌ(áØÁ)), L % S)), ((n := ÄÊPKE(0)[0]), (m := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
            ÂùÆ(n != 0, '\U000f0931 generalize')
            (áÖÒ := (MOD(ÄÕÊÄ, áØÁ=ÂýÃ) if áÑã == '○' else MOD(ÄÕÊÂ, áØÁ=ÂýÃ))(áÑË, L + (n - m) % n))
            (v := MOD(ÁâÁ, áØÁ=n - 1)(áÖÒ))
            if m != 0:
                (ÄÊPSH((-1, 0) if áÑã == '○' else (0, -1)), ((Ïß := ÄÊPKE(0)[0]), (Ïà := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
                if ÄÝøø(áÑã == '⍜', áØÁ < 0):
                    (ÄÊPSH(v), ÄÊPSH(Ïß), ÄÊPSH(ÄÔÙù(ÂÀÇ(áÇù(v[Ïß], lambda ÂîÓ: ÂîÓ is ÂýÃ)))), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
                (ÄÊPSH(v), ÄÊPSH(Ïß), ÄÊPSH(ÁØòþÁÙÇ(lambda ÂîÓ, ÂîÒ: ÂîÓ if ÂîÓ is not ÂýÃ else ÂîÒ)(v[Ïß], v[Ïà])), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
            return ËãÂ(v, áÍÜ)
    elif ÁØö(áÍÜ, áÓö):

        def Æå(*áÑË):
            ÂùÆ(ãÊú(áÑË) >= ãÊú(áÍÜ) * (S := ÂüÌ(áØÁ)), '\U000f0931 generalize')
            ÂùÆ(áØÁ > 0, '\U000f0931 generalize')
            ÂùÆ(áÑã != '⍜', '\U000f0931 generalize')
            (ÄÊPSH(áÇù(áÑË, ãÊú(áÍÜ) * (S := ÂüÌ(áØÁ)))), ((l := ÄÊPKE(0)[0]), (r := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
            (áÖÒ := ÁØòþÁÙÄ(lambda ÂîÓ, ÂîÒ: ÄÔÙù(ÂîÓ, ÂîÒ))(MOD(ÁâÁ, áØÁ=S - 1)(l), r))
            return ËãÂ(ÄÕåØ(áÖÒ, áÍÜ), lambda x, y: y(*x))
    return lambda *áÑË, **áÑÕ: áÍÛ(*Æå(*áÑË), **áÑÕ)

@OPWRAP_(*'⊚⊜🟕🟖⊛⍟')
def _(áÑã, Æå=ÂÞÅ, áÍÜ=ÂÞÅ, áØÁ=ÂÕË):
    if not áÓó(Æå):
        (ÄÊPSH((áÍÜ, Æå)), ((Æå := ÄÊPKE(0)[0]), (áÍÜ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    if áÍÜ is ÂÞÅ:
        (áÍÜ := ÄÕÍÔ)
    elif ÁØö(áÍÜ, áÍÞ) and áÑã in '⊚⊛⍟':
        (áÍÜ := Ticker(áÍÜ + 1))

    def r(*áÑË, **áÑÕ):
        (ÄÊPSH((ÂüÌ(áØÁ), áÑË[0] if áÑË else None, áÍÜ(*áÑË, **áÑÕ))), ((n := ÄÊPKE(0)[0]), (f := ÄÊPKE(0)[1]), (g := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
        if áÑã == '⊚':
            if g:
                return f
            while 0 < (ÄÊPSH(n), ÄÊPSH(ÄÊPKE(0) - 1), (n := ÄÊPKE(0)), ÄÊDEL(2))[2]:
                if áÍÜ((f := Æå(f))):
                    return f
        elif áÑã == '⊜':
            while 0 < (ÄÊPSH(n), ÄÊPSH(ÄÊPKE(0) - 1), (n := ÄÊPKE(0)), ÄÊDEL(2))[2]:
                if g == (g := áÍÜ((nf := Æå(f)))):
                    return f
                (f := nf)
        elif áÑã in '⊛⍟':
            (rf := [f])
            if g:
                return rf if áÑã == '⊛' else []
            while 0 < (ÄÊPSH(n), ÄÊPSH(ÄÊPKE(0) - 1), (n := ÄÊPKE(0)), ÄÊDEL(2))[2]:
                (g := áÍÜ((f := Æå(f))))
                if not g or áÑã == '⊛':
                    getattr(rf, 'append')(f)
                if g:
                    return rf
            if áØÁ < 0:
                return rf
        elif áÑã in '🟕🟖':
            (ÄÊPSH(([f], [g])), ((rf := ÄÊPKE(0)[0]), (rg := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
            while 0 < (ÄÊPSH(n), ÄÊPSH(ÄÊPKE(0) - 1), (n := ÄÊPKE(0)), ÄÊDEL(2))[2]:
                if (g := áÍÜ((f := Æå(f)))) in rg:
                    if áÑã == '🟖':
                        return rf
                    return ÄÝöÊ(MOD(ÄÔÞÔ, ÁÜñ=ÄÕøü)(rg, lambda x: x == g), rf)
                getattr(rf, 'append')(f)
                getattr(rg, 'append')(g)
        return None
    return r
__dir__=(__file__:=áÌî(moon_dir / 'Header/ops_\uea8c.☾')).parent
(áÍù := áÓö)

def adjust_depth(áØÆ, áØÁ, áÍù=áÓö):
    if áØÁ is ÂÞÅ:
        return 1
    if áØÁ >= 0:
        return áØÁ
    (ÄÊPSH((áØÆ, 0)), ((áØÆ := ÄÊPKE(0)[0]), (k := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    while (ÄÊPSH(k), ÄÊPSH(ÄÊPKE(0) + 1), (k := ÄÊPKE(0)), ÄÊDEL(2))[2] if áÍù(áØÆ) else None:
        if ÁØö(áØÆ, ÁÜÙ):
            break
        if ÁØö(áØÆ, ÁÜÙ) or not ãÊú(áØÆ):
            break
        (ÄÊPSH(áØÆ), ÄÊPSH(ÄÊPKE(0)[0]), (áØÆ := ÄÊPKE(0)), ÄÊDEL(2))[2]
    return ÂóÍ(áØÁ + k - 1, 0)

def flatten(áØÆ, áØÁ=ÂÞÅ, áÖÞ=None, áÍù=áÓö):
    (áØÁ := adjust_depth(áØÆ, áØÁ))
    if áÖÞ is None:
        (áÖÞ := ÂÚü())
    if (áØÁ <= 0 or not áÍù(áØÆ)) or ÁØñ(ÁÜÙ, áØÆ):
        return ÂåÔ((getattr(áÖÞ, 'extend') if áÍù(áØÆ) else getattr(áÖÞ, 'append'))(áØÆ), áÖÞ)
    for x in áØÆ:
        flatten(x, áØÁ - 1, áÖÞ, áÍù=áÍù)
    return áÖÞ

def chain_structure(áØÆ, áØÁ=ÂÞÅ, áÍù=áÓö):
    (áØÁ := adjust_depth(áØÆ, áØÁ))
    if (áØÁ <= 0 or not áÍù(áØÆ)) or ÁØö(áØÆ, ÁÜÙ):
        return MOD(Âêà, áØÁ=ãÊú(áØÆ))(None) if áÍù(áØÆ) else None
    return ÁØò(lambda ÂîÓ: chain_structure(ÂîÓ, áØÁ - 1, áÍù=áÍù))(áØÆ)

def deflatten(áØÆ, áÖÛ, áÍù=áÓö):
    if áÖÛ is None:
        return getattr(áØÆ, 'pop')(0) if áØÆ else ÄÔýò
    return ÁØò(lambda ÂîÓ: deflatten(áØÆ, ÂîÓ, áÍù=áÍù))(áÖÛ)

def flatten_under(áØÆ, Æå, áØÁ=ÂÞÅ, ÁÜñ=ÂÞÅ, áÍù=áÓö):
    (áØÁ := adjust_depth(áØÆ, áØÁ))
    if ÁÜñ is ÂÞÅ:
        (ÁÜñ := flatten(áØÆ, áØÁ, áÍù=áÍù))
    return deflatten(Æå(ÁÜñ), chain_structure(áØÆ, áØÁ, áÍù=áÍù))

def ÄÔÙù(áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ, ÁÜñ=ÂÞÅ):
    if ((áØÆ is not ÄÊPSH(ÂÞÅ) and ÄÊPOP() is not ÄÊPSH(áØÇ)) and (ÄÊDEL(1) or True) or (ÄÊDEL(1) or False)) and ((ÁØö(áØÆ, ÄÊPSH(áÍÞ)) and ÁØñ(ÄÊPOP(), ÄÊPSH(áØÇ))) and (ÄÊDEL(1) or True) or (ÄÊDEL(1) or False)):
        ÂùÆ(ÁÜñ is ÂÞÅ, '\U000f0931')
        return ÄÝöì('%s%s' % (ÄÝöì(ÂüÌ(áØÆ)), ÄÝöì(ÂüÌ(áØÇ)))) * (ÃÆí(áØÆ) * ÃÆí(áØÇ) or 1)
    if áØÇ is not ÂÞÅ:
        (áØÆ := [áØÆ, áØÇ])
    if ÁÜñ is not ÂÞÅ:
        if áÍù(ÁÜñ):
            return flatten_under(áØÆ, ÄÕÍÔ, áØÁ, [*ÁÜñ])
        return flatten_under(áØÆ, ÁÜñ, áØÁ)
    return flatten(áØÆ, áØÁ, áÍù=áÓö)
(ÄÝõÞ := (lambda áØÆ, áØÁ=ÂÕË: ÂÚü() if ÄÝøÇ(áØÆ, áÓö) else ÁØò(lambda ÂîÓ: ãÊú(ÂîÓ) if ÁØö(ÂîÓ, áÓö) else ÄÔýò)(ÂÕÅ(MOD(ÂØÎ, áØÁ=-áØÁ)(lambda ÂîÓ: ÂîÓ[0] if ãÊú(ÂîÓ) else 0, lambda ÂîÓ: ÄÝøÇ(ÂîÓ, áÓö) or ÁØö(ÂîÓ, ÁÜÙ)), áØÆ))))
(ÄÝõß := (lambda áØÆ, áØÁ=ÂÕË: ãÊú(MOD(ÄÝõÞ, áØÁ=áØÁ)(áØÆ))))
(ÐÈÔ := (lambda áØÆ, áØÇ, áØÁ=ÂÞÅ: MOD(ÆÑ, áØÁ=áØÆ)(ÂÀÇ(áØÇ), lambda x, y: MOD(ÁâÁ, áØÁ=y - 1)(x))))
(ÄÔÒØ := (lambda áØÆ, áØÁ=ÂÕË: MOD(ÄÔÙù, áØÁ=MOD(ÄÝõß, áØÁ=áØÁ)(áØÆ) - 1)(áØÆ)))

@OPWRAP_(*'⪡⪢')
def _(áÑã, áØÆ=ÂÞÅ, áØÇ=1, áØÁ=ÂÞÅ):
    if ÁØö(áØÆ, ÂÑÅ):
        return (áØÆ > ÄÊPSH(ÂýÃ) and ÄÊPOP() > ÄÊPSH(áØÇ)) and (ÄÊDEL(1) or True) or (ÄÊDEL(1) or False) if áÑã == '⪢' else (áØÆ < ÄÊPSH(ÂýÃ) and ÄÊPOP() < ÄÊPSH(áØÇ)) and (ÄÊDEL(1) or True) or (ÄÊDEL(1) or False)
    if áÑã == '⪡':
        (ÄÊPSH(áØÇ), ÄÊPSH(ÄÝöâ(ÄÊPKE(0))), (áØÇ := ÄÊPKE(0)), ÄÊDEL(2))[2]
    if áØÁ is ÂÞÅ:
        return áØÆ and áØÆ[slice((i := (-áØÇ % ãÊú(áØÆ))), None)] + áØÆ[slice(None, i)]
    return ÐÈÔ(MOD(ÄÔÒØ, áØÁ=áØÁ)(áØÆ), Âúú(MOD(ÄÝõÞ, áØÁ=áØÁ)(áØÆ), áØÇ))
__dir__=(__file__:=áÌî(moon_dir / 'Header/ugex.☾')).parent
class winder:

    def __init__(áÑÞ, áÖï, áÖõ=-1):
        (ÄÊPSH(áÑÞ), ÄÊPSH('áÖï'), ÄÊPSH(áÑÞ), ÄÊPSH('áÖõ'), ÄÊPSH(áÑÞ), ÄÊPSH('áÖà'), ÄÊPSH((áÖï, áÖõ, ÂÚü())), (setattr(ÄÊPKE(6), ÄÊPKE(5), ÄÊPKE(0)[0]), setattr(ÄÊPKE(4), ÄÊPKE(3), ÄÊPKE(0)[1]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)[2])), ÄÊDEL(7))[7]
    (__bool__ := (lambda áÑÞ: getattr(áÑÞ, 'áÖõ') + 1 < ãÊú(getattr(áÑÞ, 'áÖï'))))
    (__repr__ := (lambda áÑÞ: '[%s│%s]⟨%s⟩' % (ÂîË(getattr(áÑÞ, 'áÖï')[slice(None, getattr(áÑÞ, 'áÖõ') + 1)], ' '), ÂîÊ(getattr(áÑÞ, 'áÖï')[slice(getattr(áÑÞ, 'áÖõ') + 1, None)], ' '), Âøî(getattr(áÑÞ, 'áÖà'), ' '))))
    (peek := (lambda áÑÞ: getattr(áÑÞ, 'áÖï')[getattr(áÑÞ, 'áÖõ') + 1]))
    (next := (lambda áÑÞ: getattr(áÑÞ, 'áÖï')[(ÄÊPSH(áÑÞ), ÄÊPSH('áÖõ'), ÄÊPSH(getattr(ÄÊPKE(1), ÄÊPKE(0))), ÄÊPSH(ÄÊPKE(0) + 1), setattr(ÄÊPKE(3), ÄÊPKE(2), ÄÊPKE(0)), ÄÊDEL(4))[4]]))
    (note := (lambda áÑÞ: ÂåÔ(getattr(getattr(áÑÞ, 'áÖà'), 'append')(getattr(áÑÞ, 'áÖõ')), áÑÞ)))
    (eton := (lambda áÑÞ: ÂåÔ(ÐÌü(getattr(getattr(áÑÞ, 'áÖà'), 'pop')), áÑÞ)))
    (wind := (lambda áÑÞ: ÂåÔ((ÄÊPSH(áÑÞ), ÄÊPSH('áÖõ'), ÄÊPSH(ÐÌü(getattr(getattr(áÑÞ, 'áÖà'), 'pop'))), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3], áÑÞ)))
(ARROW_TARG := ÂÚü())

def ÄÝöç(áØÆ, áØÁ=ÂÞÅ):
    (áÖí := ARROW_TARG[-1])
    if áØÁ is ÂÞÅ:
        getattr(áÖí, 'append')(áØÆ)
        return áØÆ
    if áØÁ == ÂÕË:
        getattr(áÖí, 'extend')(áØÆ)
        return áØÆ
    getattr(áÖí, 'extend')((h := MOD(Âêà, áØÁ=áØÁ)(áØÆ)))
    return h

def ÄÝöè(áØÁ=ÂÞÅ):
    (áÖí := ARROW_TARG[-1])
    if áØÁ is ÂÞÅ:
        return getattr(áÖí, 'pop')(-1)
    if áØÁ == ÂÕË:
        (r := áÖí[slice(None, None)])
        del áÖí[slice(None, None)]
        return r
    if (ÄÊPSH(áØÁ), ÄÊPSH(ÄÊPKE(0) * -1 == 0), (áØÁ := ÄÊPKE(0)), ÄÊDEL(2))[2]:
        return ÂÚü()
    (r := áÖí[slice(áØÁ, None)])
    del áÖí[slice(áØÁ, None)]
    return r

def ÂÛÒ(áØÁ=ÂÞÅ):
    (áÖí := ARROW_TARG[-1])
    if áØÁ is ÂÞÅ:
        return áÖí[-1]
    if áØÁ == ÂÕË:
        return áÖí[slice(None, None)]
    if (ÄÊPSH(áØÁ), ÄÊPSH(ÄÊPKE(0) * -1 == 0), (áØÁ := ÄÊPKE(0)), ÄÊDEL(2))[2]:
        return ÂÚü()
    return áÖí[slice(áØÁ, None)]
(UGX_CREATE := (lambda x, d=False: lambda ÂîÓ: d if (y := UGX_RUN(winder([*ÂîÓ]), x)) is ÂÞÅ else y[0]))

def UGX_SCAN(áÖÿ, Æå, áÓà):
    if not áÖÿ:
        return ÂÚü() if '*' == áÓà or áÓà == '?' else ÂÞÅ
    (áÍí := Æå((p := ÐÌü(getattr(áÖÿ, 'peek')))))
    if áÓà == '¬':
        return ÂÞÅ if áÍí else ÂÚü()
    if áÓà == '⮞':
        return ÂÚü() if áÍí else ÂÞÅ
    if not áÍí:
        return ÂÞÅ if áÓà in '+' else ÂÚü()
    (V := (ÂÚü() if ÐÌü(getattr(áÖÿ, 'next')) is ÄÔýò or ÄÔýò is áÍí else Âêà(p)))
    if áÓà in '?':
        return V
    while áÖÿ:
        if not (v := Æå((p := ÐÌü(getattr(áÖÿ, 'peek'))))):
            break
        if v is ÄÔýò or ÄÔýò is ÐÌü(getattr(áÖÿ, 'next')):
            continue
        getattr(V, 'append')(p)
    return V

def UGX_RUN(áÖÿ, áØÃ):
    (ÄÊPSH(áØÃ), ((áÓç := ÄÊPKE(0)[0]), *(áÒø := ÄÊPKE(0)[slice(1, None, None)])), ÄÊDEL(1))[1]
    if ÁØö(áÓç, áÓó):
        return UGX_SCAN(áÖÿ, áÓç, áÒø[0])
    elif áÓç in 'BP':
        (ÄÊPSH(áÒø), ((áÓæ := ÄÊPKE(0)[0]), (áÓà := ÄÊPKE(0)[1]), (áÓå := ÄÊPKE(0)[2]), (áÓÕ := ÄÊPKE(0)[3])), ÄÊDEL(1))[1]
        getattr(ARROW_TARG, 'append')(áÓæ)
        ÂåÔ(ÐÌü(getattr(áÖÿ, 'note')), (V := (r := UGX_RUN(áÖÿ, áÓÕ))))
        if áÓà == '⮞':
            ÂåÔ(ÐÌü(getattr(áÖÿ, 'wind')), (V := (ÂÞÅ if r is ÂÞÅ else ÂÚü())))
        elif áÓà == '¬':
            ÂåÔ(ÐÌü(getattr(áÖÿ, 'wind')), (V := (ÂÚü() if r is ÂÞÅ else ÂÞÅ)))
        elif áÓà == '?':
            ÂåÔ(ÐÌü(getattr(áÖÿ, 'wind')), (V := (ÂÚü() if r is ÂÞÅ else ÂÞÅ)))
        elif r is ÂÞÅ:
            ÂåÔ(ÐÌü(getattr(áÖÿ, 'wind')), (V := (ÂÚü() if áÓà == '∗' else ÂÞÅ)))
        elif áÓà not in '?':
            while áÖÿ:
                ÂåÔ(ÐÌü(getattr(áÖÿ, 'note')), (r := UGX_RUN(áÖÿ, áÓÕ)))
                if r is ÂÞÅ:
                    ÐÌü(getattr(áÖÿ, 'wind'))
                    break
                ÂåÔ(ÐÌü(getattr(áÖÿ, 'eton')), getattr(V, 'extend')(r))
            ÐÌü(getattr(áÖÿ, 'eton'))
        if áÓå is ÄÔýò:
            (V := ÂÚü())
        if V is not ÂÞÅ and áÓó(áÓå):
            (V := áÓå(V))
        getattr(ARROW_TARG, 'pop')(-1)
        if V is ÂÞÅ:
            return V
        return MOD(Áëý, áØÁ=áÓç == 'B')(V, Âêà)
    elif áÓç in '∧∨':
        if áÓç == '∧':
            ÂåÔ(ÐÌü(getattr(áÖÿ, 'note')), (V := ÂÚü()))
            for U in áÒø:
                if (r := UGX_RUN(áÖÿ, U)) is ÂÞÅ:
                    return ÂåÔ(ÐÌü(getattr(áÖÿ, 'wind')), ÂÞÅ)
                getattr(V, 'extend')(r)
            return ÂåÔ(ÐÌü(getattr(áÖÿ, 'eton')), V)
        elif áÓç == '∨':
            for U in áÒø:
                ÐÌü(getattr(áÖÿ, 'note'))
                if (r := UGX_RUN(áÖÿ, U)) is not ÂÞÅ:
                    return ÂåÔ(ÐÌü(getattr(áÖÿ, 'eton')), r)
                ÐÌü(getattr(áÖÿ, 'wind'))
            return ÂÞÅ
__dir__=(__file__:=áÌî(moon_dir / 'Header/ℵ.☾')).parent
class aleph_wrapper:
    (__slots__ := ('x',))
    (__init__ := (lambda áÑÞ, y: Âåß(None, (ÄÊPSH(áÑÞ), ÄÊPSH('x'), ÄÊPSH(y), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3])))
    (__repr__ := (lambda áÑÞ: getattr(áÑÞ, 'x')))
    (__call__ := (lambda áÑÞ, *áÑË, **áÑÕ: getattr(áÑÞ, 'x')(*áÑË, **áÑÕ)))

class ÂÑÖ(áÍÙ):
    (áÌüþáÍã := 'ℵ')

    def __getitem__(áÑÞ, x):
        if x in áÑÞ:
            return getattr(áÍÙ, '__getitem__')(áÑÞ, x)
        if getattr(áÑÞ, 'hasdef')():
            return getattr(áÑÞ, 'getdef')(x)
        ÐâÄ(KeyError('%s ∉ %s, and I have no default value!' % (x, áÑÞ)))

    def __init__(áÑÞ, *áÑË, áØÁ=ÂÞÅ, **áÑÕ):
        getattr(super(), '__init__')(*áÑË, **áÑÕ)
        if áØÁ is not ÂÞÅ:
            getattr(áÑÞ, 'setdef')(áØÁ)
    (__repr__ := (lambda áÑÞ: '%s%s(%s)' % (getattr(getattr(áÑÞ, '__class__'), 'áÌüþáÍã'), '[%s]' % (h[0] or 'ᐦ',) if 0 in (h := getattr(áÑÞ, '__dict__')) else ÁØã, Âøî(ËãÂ(ÐÌü(getattr(áÑÞ, 'items')), lambda x, y: '%s=%s' % (x, y)), ', '))))
    (__json__ := (lambda áÑÞ, cb, *áÏÞ, **áÏè: MOD(ËãÂ, áØÁ=ì)(áÍÙ(áÑÞ), lambda x, y: cb(y, *áÏÞ, **áÏè))))
    (__iter__ := (lambda áÑÞ: iter(getattr(áÑÞ, 'items')())))
    (__call__ := (lambda áÑÞ, *áÑË, **áÑÕ: ÂåÔ(getattr(áÍÙ, 'update')(áÑÞ, *áÑË, **áÑÕ), áÑÞ)))
    (__bool__ := (lambda áÑÞ: ãÊú(áÑÞ) > 0))
    (__or__ := (lambda áÑÞ, x: getattr(áÑÞ, 'copy')()(x)))
    (__setattr__ := getattr(áÍÙ, '__setitem__'))
    (__getattr__ := __getitem__)

    def __getstate__(áÑÞ):
        if getattr(áÑÞ, 'hasdef')():
            return (áÍÙ(áÑÞ), getattr(áÑÞ, 'getdef')())
        else:
            return (áÍÙ(áÑÞ),)

    def __setstate__(áÑÞ, s):
        getattr(áÑÞ, '__init__')(s[0])
        if ãÊú(s) > 1:
            getattr(áÑÞ, 'setdef')(s[1])

    def __pow__(áÑÞ, x):
        if x is î:
            return [*ÐÌü(getattr(áÑÞ, 'keys'))]
        if x is ì:
            return [*ÐÌü(getattr(áÑÞ, 'values'))]
        if x is ë:
            return [*ÐÌü(getattr(áÑÞ, 'items'))]
        if x is ÂÕì:
            return MOD(Áÿú, áØÁ=ë)(áÑÞ, ÂÀÇ)
        if x is Áâ:
            return MOD(Áëý, áØÁ=ÄÝøÇ((v := ÐÌü(getattr(áÑÞ, 'getdef'))), (C := aleph_wrapper)))(ÐÌü(getattr(áÑÞ, 'copy')), lambda x: getattr(x, 'setdef')(C(v)))
        ÂùÆ(False)
    (hasdef := (lambda áÑÞ: 0 in getattr(áÑÞ, '__dict__')))
    (setdef := (lambda áÑÞ, x: ÂåÔ((ÄÊPSH(getattr(áÑÞ, '__dict__')), ÄÊPSH(0), ÄÊPSH(x), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3], áÑÞ)))

    def getdef(áÑÞ, k=ÂÞÅ):
        (d := getattr(áÑÞ, '__dict__')[0])
        if ÁØö(d, aleph_wrapper):
            (ÄÊPSH(d), ÄÊPSH(ÐÌü(ÄÊPKE(0))), (d := ÄÊPKE(0)), ÄÊDEL(2))[2]
            (ÄÊPSH(áÑÞ), ÄÊPSH(k), ÄÊPSH(d), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        return d

    def copy(áÑÞ):
        (r := type(áÑÞ)(getattr(super(), 'copy')()))
        if getattr(áÑÞ, 'hasdef')():
            getattr(r, 'setdef')(getattr(áÑÞ, 'getdef')())
        return r

class ÂÑØ(ÂÑÖ):
    (áÌüþáÍã := 'ℶ')
    (__iter__ := (lambda áÑÞ: iter(getattr(áÑÞ, 'values')())))

class _hwrap(áÍÙ):

    def __init__(áÑÞ, áÍØ):
        (ÄÊPSH(áÑÞ), ÄÊPSH('áÍØ'), ÄÊPSH(áÑÞ), ÄÊPSH('áÍã'), ÄÊPSH((áÍØ, getattr(áÍØ, 'áÌüþáÍã'))), (setattr(ÄÊPKE(4), ÄÊPKE(3), ÄÊPKE(0)[0]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)[1])), ÄÊDEL(5))[5]
    (__getitem__ := (lambda áÑÞ, x: getattr(getattr(áÑÞ, 'áÍØ')(), 'setdef')(x)))
    (__setitem__ := (lambda áÑÞ, x, y: ÂåÔ(getattr((Âàü := getattr(áÑÞ, 'áÍØ')()), '__setitem__')(x, y), Âàü)))
    (__call__ := (lambda áÑÞ, *áÑË, **áÑÕ: getattr(áÑÞ, 'áÍØ')(*áÑË, **áÑÕ)))
    (__or__ := (lambda áÑÞ, x: getattr(áÑÞ, 'áÍØ')() | x))
    (__pow__ := (lambda áÑÞ, x: getattr(áÑÞ, 'áÍØ')() ** x))
    (__repr__ := (lambda áÑÞ: '%s()' % (getattr(áÑÞ, 'áÍã'),)))
    (__bool__ := (lambda: False))
(ÂÑÖ := _hwrap(ÂÑÖ))
(ÂÑØ := _hwrap(ÂÑØ))
__dir__=(__file__:=áÌî(moon_dir / 'Header/!.☾')).parent
def ÏÀ(z):
    if ÄÝõè(z) < ÃÆ:
        return ÂÞÅCAT(Ïò, Ãù) / ((ÂÐæ ** ÂÞÅCAT(ÂÞÅCAT(Ãù, Ïî), z) - ÂÐæ ** ÂÞÅCAT(ÂÞÅCAT(ÄÝîâ, Ïî), z)) * ÏÀ(1 - z))
    (p := [1.000000000190015, 76.18009172947146, -86.50532032941676, 24.01409824083091, -1.2317395724501554, 0.0012086509738661786, -5.395239384953128e-06])
    return MOD(ÂøÑ, áØÁ=p[0])(ÁÙÇ(lambda ÂîÒ: p[ÂîÒ] / (z + ÂîÒ))(ÄÝöÊ(1, 6))) * ÂÐæ ** (-5.5 - z) * (5.5 + z) ** (ÃÆ + z) * ÂÕÇ(Ïò) / z

def â(áØÆ, áØÁ=ÂÞÅ):
    if áØÁ is ÂÞÅ:
        if ÁØö(áØÆ, ÂÑÅ):
            return nan if áØÆ < 0 else MOD(ÂøÐ, áØÁ=1)(ÄÝöÉ(0, áÍÞ(áØÆ)))
        return áØÆ * ÏÀ(áØÆ)
    if ÁØö(áØÁ, áÍÞ):
        return MOD(ÂøÐ, áØÁ=1)(ÁØò(lambda ÂîÓ: ÂîÓ + áØÆ)(ÂÿÇ(áØÁ)))
    if ÁØö(áØÁ, ÂÐá):
        if áØÆ == 0:
            return 1
        if (d := Âüð(ÄÝõç(áØÁ))) >= 0 and áØÆ > 0:
            return ÂÕË
        if d <= 0 and áØÆ < 0:
            return nan
        (ÄÊPSH((1, áØÆ)), ((t := ÄÊPKE(0)[0]), (c := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        while ÃÆí(c) == ÃÆí(áØÆ):
            (ÄÊPSH(t), ÄÊPSH(ÄÊPKE(0) * c), (t := ÄÊPKE(0)), ÄÊDEL(2))[2]
            (ÄÊPSH(c), ÄÊPSH(ÄÊPKE(0) + d), (c := ÄÊPKE(0)), ÄÊDEL(2))[2]
        return t
    if ÁØö(áØÁ, áÓö):
        return MOD(ÂøÐ, áØÁ=1)(ÁØò(lambda ÂîÓ: ÂîÓ * áØÁ[-1] + áØÆ)(ÂÿÇ(áØÁ[0])))
    ÂùÆ(False, 'what do you meeeeaaaaaannnnnn!?!?!?')
__dir__=(__file__:=áÌî(moon_dir / 'Header/𝔍.☾')).parent
(áÐÞ := ÂÞÅCAT({ÁÁ: ÄÊCUR((1,), {'ensure_ascii': False, 'indent': None, 'separators': ',:'}, jdumps__, ÂýÃ), ÿ: jloads__}, ÂÑÖ()))
__dir__=(__file__:=áÌî(moon_dir / 'Header/🌈.☾')).parent
def h2r(c=ÁØã):
    if ÁØö(c, áÍÞ):
        (ÄÊPSH(c), ÄÊPSH(MOD(ÄÝöì, áØÁ=16)(ÄÊPKE(0))), (c := ÄÊPKE(0)), ÄÊDEL(2))[2]
    (c := getattr(getattr(c, 'strip')(), 'lstrip')('#'))
    if getattr(c, 'startswith')('0x'):
        (ÄÊPSH(c), ÄÊPSH(ÄÊPKE(0)[slice(2, None)]), (c := ÄÊPKE(0)), ÄÊDEL(2))[2]
    (ÄÊPSH((ÄÊCUR((1,), {}, áÍÞ, ÂýÃ, 16), ãÊú(c))), ((ÂÐí := ÄÊPKE(0)[0]), (n := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    if n == 0:
        return (0, 0, 0, 255)
    if n == 1:
        return (ÂÕÅ(ÂÐí, c[0] * 2), ÂÕÅ(ÂÐí, c[0] * 2), ÂÕÅ(ÂÐí, c[0] * 2), 255)
    if n == 2:
        return (ÂÕÅ(ÂÐí, c[0] * 2), ÂÕÅ(ÂÐí, c[0] * 2), ÂÕÅ(ÂÐí, c[0] * 2), ÂÕÅ(ÂÐí, c[1] * 2))
    if n == 3:
        return (ÂÕÅ(ÂÐí, c[0] * 2), ÂÕÅ(ÂÐí, c[1] * 2), ÂÕÅ(ÂÐí, c[2] * 2), 255)
    if n == 4:
        return (ÂÕÅ(ÂÐí, c[0] * 2), ÂÕÅ(ÂÐí, c[1] * 2), ÂÕÅ(ÂÐí, c[2] * 2), ÂÕÅ(ÂÐí, c[3] * 2))
    if n == 5:
        return (ÂÕÅ(ÂÐí, c[0] * 2), ÂÕÅ(ÂÐí, c[1] * 2), ÂÕÅ(ÂÐí, c[2] * 2), ÂÕÅ(ÂÐí, c[slice(3, 5)]))
    if n == 6:
        return (ÂÕÅ(ÂÐí, c[slice(0, 2)]), ÂÕÅ(ÂÐí, c[slice(2, 4)]), ÂÕÅ(ÂÐí, c[slice(4, 6)]), 255)
    if n == 7:
        return (ÂÕÅ(ÂÐí, c[slice(0, 2)]), ÂÕÅ(ÂÐí, c[slice(2, 4)]), ÂÕÅ(ÂÐí, c[slice(4, 6)]), ÂÕÅ(ÂÐí, c[6] * 2))
    if n == 8:
        return (ÂÕÅ(ÂÐí, c[slice(0, 2)]), ÂÕÅ(ÂÐí, c[slice(2, 4)]), ÂÕÅ(ÂÐí, c[slice(4, 6)]), ÂÕÅ(ÂÐí, c[slice(6, 8)]))
(r2hl := (lambda x: '#%s' % (Âøî(Áÿú(x, MOD(ÄÝöì, áØÁ=16 + ÂÞÅCAT(2, Ãù)))),)))
(h2hl := Âåæ(r2hl, h2r))
(TERM_RESET := '\x1b[0m')

def termclr(t, fg=None, bg=None, rst=True):
    (mkc := (lambda x, y, z, w, v: '\x1b[%s;2;%s;%s;%sm' % (x, y, z, w)))
    (R := Âøî([mkc(n, *h2r(c)) for c, n in ÄÕåØ([fg, bg], [38, 48]) if c is not None]))
    return '%s%s%s' % (R, t, TERM_RESET if rst else ÁØã)
__dir__=(__file__:=áÌî(moon_dir / 'Header/kots.☾')).parent
(TMPDIR := ÂÞÅCAT(ÐÌü(gettempdir), áÌî))
(mkd := (lambda f, e=True, p=True: ÂåÔ(getattr((p := áÌî(f)), 'mkdir')(exist_ok=e, parents=p), p)))
(mkf := (lambda f, e=True: ÂåÔ(getattr(mkd(getattr((p := áÌî(f)), 'parent')), 'touch')(exist_ok=e), p)))
(tmpf := (lambda b=ÁØã, f=ÂÞÅ, n=14: mkf(ð(ð(TMPDIR, b), Âøî(ÄÔÙù(MOD(ÐâÇ, áØÁ=1)(abcABC123, n))) if f is ÂÞÅ else f))))
(tmpd := (lambda b=ÁØã, f=ÂÞÅ, n=14: mkd(ð(ð(TMPDIR, b), Âøî(ÄÔÙù(MOD(ÐâÇ, áØÁ=1)(abcABC123, n))) if f is ÂÞÅ else f))))

class suppar2:
    (__init__ := (lambda áÑÞ, Æå: ÂåÔ((ÄÊPSH(Æå), ÄÊPSH(áÑÞ), ÄÊPSH('Æå'), setattr(ÄÊPKE(1), ÄÊPKE(0), ÄÊPKE(2)), ÄÊDEL(3))[3], None)))
    (__call__ := (lambda áÑÞ, *áÑË, **áÑÕ: getattr(áÑÞ, 'Æå')(*áÑË, **áÑÕ)))
    (__getitem__ := (__getattr__ := (lambda áÑÞ, x, *áÑË, **áÑÕ: lambda *áÑË, **áÑÕ: getattr(áÑÞ, 'Æå')(*áÑË, x, **áÑÕ))))
(ÐâÒ := (lambda x=ÂÞÅ: ÐÌü(PL_TEXT_PASTE) if x is ÂÞÅ else ÂåÔ(ÂÞÅCAT(ÂÞÅCAT(x, ÁÜÙ), PL_TEXT_COPY), x)))
(ÐÈÃ := suppar2(lambda f, o=ÁØã: getattr(áÌî(f), 'open')(o)))
(ÐØó := suppar2(lambda f, o=ÁØã: Âáõ((y := ÐÈÃ['r' + o](f)), lambda x: ÐÌü(getattr(x, 'read')))))
(ÐØì := suppar2(lambda f, áÏû, o=ÁØã: Âáõ((y := ÐÈÃ['w' + o](f)), lambda x: ÂåÔ(getattr(x, 'write')(áÏû), y))))
(pwd := (lambda: áÌî(ÐÌü(getattr(os, 'getcwd')))))

class cd:
    (ÄÊPSH(MOD(ÂÚü, áØÁ=2)()), ((s := ÄÊPKE(0)[0]), (c := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]

    def __init__(áÑÞ, d=None):
        (ÄÊPSH(áÑÞ), ÄÊPSH('d'), ÄÊPSH(d), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]

    def __enter__(áÑÞ):
        (x := getattr(áÑÞ, 'd'))
        getattr(getattr(cd, 's'), 'append')((ãÊú(getattr(cd, 'c')), (x := ÐÌü(pwd))))
        if x is not None:
            getattr(os, 'chdir')(áÌî(x))
        return ÐÌü(pwd)

    def __exit__(áÑÞ, *áÑË):
        (ÄÊPSH(getattr(getattr(cd, 's'), 'pop')(-1)), ((i := ÄÊPKE(0)[0]), (d := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        (ÄÊPSH(cd), ÄÊPSH('c'), ÄÊPSH(getattr(cd, 'c')[slice(None, i)]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        getattr(os, 'chdir')(d)
        return ÐÌü(pwd)

    def __call__(áÑÞ, d=None):
        if d is ÁÃ:
            return cd(getattr(áÌî(getattr(getattr(inspect, 'stack')()[1], 'filename')), 'parent'))
        if d is None:
            getattr(os, 'chdir')(getattr(getattr(cd, 'c'), 'pop')(-1))
            return ÐÌü(pwd)
        getattr(getattr(cd, 'c'), 'append')(ÐÌü(pwd))
        getattr(os, 'chdir')(d)
        return ÐÌü(pwd)

    def __getitem__(áÑÞ, d):
        return getattr(áÑÞ, '__class__')(d)
(cd := ÐÌü(cd))

def sha(*áÑË, **áÑÕ):
    from hashlib import sha256 as _sha256
    from base64 import urlsafe_b64encode, urlsafe_b64decode
    return getattr(áÍÇ(urlsafe_b64encode(getattr(_sha256(áÍÇ(ÁÜÙ(áÑË) + ÁÜÙ(áÑÕ))), 'digest')())), 'rstrip')('=')
__dir__=(__file__:=áÌî(moon_dir / 'Header/extra_globals.☾')).parent
(FRAC_CONV := {**dict(ÄÕåØ(ÂÛê('12\u200913\u200914\u200915\u200916\u200917\u200918\u200919\u2009110\u200923\u200925\u200927\u200929\u200934\u200935\u200937\u200938\u2009310\u200945\u200947\u200949\u200956\u200957\u200958\u200959\u200967\u200978\u200979\u2009710\u200989\u2009910\u200903\u20091100'), '½⅓¼⅕⅙⅐⅛⅑⅒⅔⅖\U000f7db2\U000f7db7¾⅗\U000f7db3⅜\U000f7dc6⅘\U000f7db4\U000f7dc2⅚\U000f7db5⅝\U000f7db9\U000f7db6⅞\U000f7dba\U000f7dc7\U000f7dbb\U000f7dc8↉\U000f7dc9'))})
(TOFRAC := (lambda x: getattr(FRAC_CONV, 'get')(x, x)))

class UPSIDEDOWNSYNDROME:
    (NRM := '0123456789abcdefoxABCDEFOXîĵ\U000f7e88ℇτπ\U000f7e8d\U000f7e8f∞')
    (USD := '\U000f7c3d\U000f7c3e\U000f7c3f\U000f7c40\U000f7c41\U000f7c42\U000f7c43\U000f7c44\U000f7c45\U000f7c46\U000f7c47\U000f7c48\U000f7c49\U000f7c4a\U000f7c4b\U000f7c4c\U000f7c4d\U000f7c4e\U000f7c4f\U000f7c50\U000f7c51\U000f7c52\U000f7c53\U000f7c54\U000f7c55\U000f7c56\U000f7c6a\U000f7c7d\U000f7c7e\U000f7c6b\U000f7c6c\U000f7c6d\U000f7c6e\U000f7c70\U000f7c69')
    (MAP := ({**dict(ÄÕåØ(NRM, USD))} | {**dict(ÄÕåØ(USD, NRM))}))
    (flip := (lambda x, m=MAP: Âøî(ÁØò(lambda ÂîÓ: getattr(m, 'get')(ÂîÓ, ÂîÓ))(x), ÁØã)))

class SCRIPT:
    (SCRIPT_FILE_LOC := '/home/ganer/Projects/Moon_BETA/STAGES/.SCRIPT_MAP')
    (ÄÊPSH(ÄÝöÞ(ÐÌü(getattr(ÐØó(SCRIPT_FILE_LOC), 'strip')), '\n')), ((CHAR_NRM := ÄÊPKE(0)[0]), (CHAR_SUP := ÄÊPKE(0)[1]), (CHAR_SUB := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
    (SUP := getattr(ÁÜÙ, 'maketrans')(CHAR_NRM, CHAR_SUP))
    (SUB := getattr(ÁÜÙ, 'maketrans')(CHAR_NRM, CHAR_SUB))
    (NRM := getattr(ÁÜÙ, 'maketrans')(CHAR_SUP + CHAR_SUB, ÂÞÅCAT(2, CHAR_NRM)))
    (ÄÊPSH(Áÿú([SUP, SUB, NRM], lambda áÖæ: lambda x: getattr(x, 'translate')(áÖæ))), ((sup := ÄÊPKE(0)[0]), (sub := ÄÊPKE(0)[1]), (nrm := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
(ÄÊPSH((getattr(SCRIPT, 'sup'), getattr(SCRIPT, 'sub'), getattr(SCRIPT, 'nrm'))), ((supscript := ÄÊPKE(0)[0]), (subscript := ÄÊPKE(0)[1]), (nrmscript := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
(ÄÊPSH((getattr(SCRIPT, 'CHAR_SUP'), getattr(SCRIPT, 'CHAR_SUB'))), ((SUPSCRIPT := ÄÊPKE(0)[0]), (SUBSCRIPT := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ALPHABETS := Áÿú(ÄÝöÞ(Âüá('\n    abcdefghijklmnopqrstuvwxyz\u2009ABCDEFGHIJKLMNOPQRSTUVWXYZ\u20090123456789\n    𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫\u2009𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ\u2009𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡\n    𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳\u2009𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙\u2009𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗\n    𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧\u2009𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍\u2009◌◌◌◌◌◌◌◌◌◌\n    𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇\u2009𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭\u2009𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵\n    𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣\u2009𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉\u2009𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿\n    ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ\u2009ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ\u2009◌\U000f0ca1\U000f0ca3\U000f0ca5\U000f0ca7\U000f0ca9\U000f0cab\U000f0cad\U000f0caf\U000f0cb1\n    ⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵\u2009🄐🄑🄒🄓🄔🄕🄖🄗🄘🄙🄚🄛🄜🄝🄞🄟🄠🄡🄢🄣🄤🄥🄦🄧🄨🄩\u2009◌⑴⑵⑶⑷⑸⑹⑺⑻⑼\n    \U000f0aee\U000f0aef\U000f0af0\U000f0af1\U000f0af2\U000f0af3\U000f0af4\U000f0af5\U000f0af6\U000f0af7\U000f0af8\U000f0af9\U000f0afa\U000f0afb\U000f0afc\U000f0afd\U000f0afe\U000f0aff\U000f0b00\U000f0b01\U000f0b02\U000f0b03\U000f0b04\U000f0b05\U000f0b06\U000f0b07\u2009\U000f0aee\U000f0aef\U000f0af0\U000f0af1\U000f0af2\U000f0af3\U000f0af4\U000f0af5\U000f0af6\U000f0af7\U000f0af8\U000f0af9\U000f0afa\U000f0afb\U000f0afc\U000f0afd\U000f0afe\U000f0aff\U000f0b00\U000f0b01\U000f0b02\U000f0b03\U000f0b04\U000f0b05\U000f0b06\U000f0b07\u2009\U000f0b39\U000f0b3a\U000f0b3b\U000f0b3c\U000f0b3d\U000f0b3e\U000f0b3f\U000f0b40\U000f0b41\U000f0b42\n    \U0001ccd6\U0001ccd7\U0001ccd8\U0001ccd9\U0001ccda\U0001ccdb\U0001ccdc\U0001ccdd\U0001ccde\U0001ccdf\U0001cce0\U0001cce1\U0001cce2\U0001cce3\U0001cce4\U0001cce5\U0001cce6\U0001cce7\U0001cce8\U0001cce9\U0001ccea\U0001cceb\U0001ccec\U0001cced\U0001ccee\U0001ccef\u2009\U0001ccd6\U0001ccd7\U0001ccd8\U0001ccd9\U0001ccda\U0001ccdb\U0001ccdc\U0001ccdd\U0001ccde\U0001ccdf\U0001cce0\U0001cce1\U0001cce2\U0001cce3\U0001cce4\U0001cce5\U0001cce6\U0001cce7\U0001cce8\U0001cce9\U0001ccea\U0001cceb\U0001ccec\U0001cced\U0001ccee\U0001ccef\u2009\U0001ccf0\U0001ccf1\U0001ccf2\U0001ccf3\U0001ccf4\U0001ccf5\U0001ccf6\U0001ccf7\U0001ccf8\U0001ccf9\n    𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓\u2009𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹\u2009𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫\n    ɒც𝼝𝼥⋿ꬵꬶҕї𝼚𝼐ꬷӍꬼϙƿ𝼛Ʀ𝼞ŧꭒѵꭐꭘꭚƶ\u2009ѦƁƇƊᗴҒႺⴼΙɈⴿꝈⱮͶⴲƤꝖⴽႽƬŲѴϢҲⵖΖ\u2009◌◌◌◌◌◌◌◌◌◌\n    𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻\u2009𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡\u2009◌◌◌◌◌◌◌◌◌◌\n    𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏\u2009𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵\u2009◌◌◌◌◌◌◌◌◌◌\n    𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃\u2009𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩\u2009◌◌◌◌◌◌◌◌◌◌\n    𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛\u2009𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁\u2009◌◌◌◌◌◌◌◌◌◌\n    𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷\u2009𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ\u2009◌◌◌◌◌◌◌◌◌◌\n    𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟\u2009𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅\u2009◌◌◌◌◌◌◌◌◌◌\n    𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯\u2009𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕\u2009◌◌◌◌◌◌◌◌◌◌\n'), '\n'), Âåæ(ÂÛê, Âüá)))
(LOWERCASE := Âøî(Áÿú(ALPHABETS, MOD(ÁÛÛ, áØÁ=0))))
(UPPERCASE := Âøî(Áÿú(ALPHABETS, MOD(ÁÛÛ, áØÁ=1))))
(LETTERS := (LOWERCASE + UPPERCASE))
(TERLETS := (UPPERCASE + LOWERCASE))
(ÄÊPSH(ALPHABETS[0][slice(None, 3)]), ((abc := ÄÊPKE(0)[0]), (ABC := ÄÊPKE(0)[1]), (num := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
(ÄÊPSH((abc + ABC, abc + num, ABC + num, abc + ABC + num)), ((abcABC := ÄÊPKE(0)[0]), (abc123 := ÄÊPKE(0)[1]), (ABC123 := ÄÊPKE(0)[2]), (abcABC123 := ÄÊPKE(0)[3])), ÄÊDEL(1))[1]
(TO_LOWERCASE := CUR(lambda ÂîÓ, ÂîÒ: under_script(ÂîÒ, ÂîÓ), (lambda ÂîÓ: lambda x: getattr(x, 'translate')(ÂîÓ))(getattr(ÁÜÙ, 'maketrans')(UPPERCASE, LOWERCASE))))
(TO_UPPERCASE := CUR(lambda ÂîÓ, ÂîÒ: under_script(ÂîÒ, ÂîÓ), (lambda ÂîÓ: lambda x: getattr(x, 'translate')(ÂîÓ))(getattr(ÁÜÙ, 'maketrans')(LOWERCASE, UPPERCASE))))
(REVERSE_CASE := CUR(lambda ÂîÓ, ÂîÒ: under_script(ÂîÒ, ÂîÓ), (lambda ÂîÓ: lambda x: getattr(x, 'translate')(ÂîÓ))(getattr(ÁÜÙ, 'maketrans')(LETTERS, TERLETS))))
(GET_CASE := (lambda x: (TO_UPPERCASE(x) == x) - (x == TO_LOWERCASE(x))))

def under_script(áØÆ, Æå, áÕÉ=ÂÞÅ):
    (áÓÕ := (lambda ÂîÓ: supscript if ÂîÓ in SUPSCRIPT else subscript if ÂîÓ in SUBSCRIPT else None))
    return Âøî(ËãÂ(ÄÕåØ(ÁØò(lambda ÂîÓ: MOD(ÆÑ, áØÁ=ÄÕÍÔ)(Áÿú(ÂÕÅ(ÂÛÜ(nrmscript, Âåæ(Âó, áÓÕ)), ÂîÓ), áÓÕ), Âåæ))(áØÆ if áÕÉ is ÂÞÅ else áÕÉ), Æå(ÂÕÅ(ÂØÏ(nrmscript), áØÆ))), ÂÕÅ))
__dir__=(__file__:=áÌî(moon_dir / 'Header/highlighter.☾')).parent
(styf := áÌî('/home/ganer/Projects/Moon_BETA/STAGES/style.json'))
(styd := ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(styf, ÐØó), áÐÞ[ÿ]), ÂÑÖ()))

@cache
def sty(s, bg=0, def_='bec'):
    for k, v in styd:
        if s not in k or 'color' not in v:
            continue
        return termclr(s, v['color'], bg)
    return termclr(s, def_, bg)
(__highlighter__ := (lambda l, b=False, clr='bec': Âøî(Áÿú(ÂÞÅCAT(ÂÞÅCAT(l, ÁÜÙ), VEP), ÄÊCUR((1,), {}, sty, ÂýÃ, b, clr)))))

def highlight_tester():
    while (l := ÐÌü(getattr(stdin, 'readline'))):
        Âçß(ÂÞÅCAT(getattr(l, 'rstrip')('\n'), __highlighter__))
__dir__=(__file__:=áÌî(moon_dir / 'Header/meta.☾')).parent
from zlib import compress as zibe, decompress as zibd
from base64 import b64encode as b64e, b64decode as b64d
(ÄÊPSH((lambda ÂîÓ: ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ, áÍÇ), zibe), b64e), áÍÇ), lambda ÂîÓ: ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ, áÍÇ), b64d), zibd), áÍÇ))), ((stre := ÄÊPKE(0)[0]), (strd := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(IMPSIMPS := (('ℍ', 'ℍ\U000f7e19\U000f7e18\U000f7e1b\U000f7e1a\U000f7e17\U000f7e16\U000f7e1c\U000f7e3d\U000f7e15ĵ\U000f7e88\U000f7c7d\U000f7c7e'), ('⫚', '⫚'), ('¶', '¶✿')))
(__ÄÊIMPORTS__ := ÐÌü(ÂÑÖ()))
(TP_CACHE := {})
(TRANSPILE_REF := ÐÌü(Holder))
(EXEC_NATIVE := exec)
(dump_cached_imports := (lambda: 'TP_CACHE.update({%s})' % ((lambda ÂîÓ: Âøî(ÂîÓ, ','))(ÁØò(lambda ÂîÓ: '%s:strd(%s)' % (ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(moon_dir, getattr(ÂîÓ[0], 'relative_to')), ÁÜÙ), repr), ÂÞÅCAT(ÂÞÅCAT(getattr(ÂîÓ[1], 'native_code'), stre), repr)))(ÄÔÔç(__ÄÊIMPORTS__, lambda ÂîÓ: getattr(ÂîÓ[0], 'is_relative_to')(moon_dir)))),)))

def moon_to_py_cached(áÖï):
    if not TRANSPILE_REF:
        (ÄÊPSH(ÁØò(lambda ÂîÓ: ÂÞÅCAT('/tmp/%s.%s' % (sha(áÖï), ÂîÓ), áÌî))(ÂÛê('☾\u2009py'))), ((i := ÄÊPKE(0)[0]), (o := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        ÐØì(i, áÖï)
        ÐÌü(getattr(Popen(['python', ð(moon_dir, 'STAGES/BOOTSTRAP_ζ.py'), 'o', i, o]), 'wait'))
        return ÐØó(o)
    ÂùÆ(TRANSPILE_REF, 'Cannot transpile without transpiler!')
    return (ÄÊPSH(TP_CACHE), ÄÊPSH(n), ÄÊPSH(áÖï + TRANSPILE_REF), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]

def ÄÕôñ(áÖï, ns=None, get_code=False, include_builtins=True, native=False):
    if not native:
        (áÖï := moon_to_py_cached(áÖï))
    if get_code:
        return áÖï
    (ns := (BOOTSTRAP_GLOBALS | ({} if ns is None else ns)))
    try:
        EXEC_NATIVE(áÖï, ns)
    except:
        Âçß('Failed to exec!')
        raise Ïã
    return ns

class Module(ÁØö(ÐÌü(ÂÑÖ()))):

    def __init__(áÑÞ, name, ns, code=None, native_code=None):
        (ÄÊPSH(áÑÞ), ÄÊPSH('name'), ÄÊPSH(áÑÞ), ÄÊPSH('code'), ÄÊPSH(áÑÞ), ÄÊPSH('native_code'), ÄÊPSH((name, code, native_code)), (setattr(ÄÊPKE(6), ÄÊPKE(5), ÄÊPKE(0)[0]), setattr(ÄÊPKE(4), ÄÊPKE(3), ÄÊPKE(0)[1]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)[2])), ÄÊDEL(7))[7]
        getattr(super(), '__init__')(ns)

    def __repr__(áÑÞ):
        return 'Module[%s]' % (getattr(áÑÞ, 'name'),)

def __ÄÊIMPORT__(p, áÒÿ):
    (ÄÊPSH((getattr((ÄÊPSH(p), ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0), áÌî)), (p := ÄÊPKE(0)), ÄÊDEL(2))[2], 'name'), ÂÚü())), ((name := ÄÊPKE(0)[0]), (failed := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (dirs := (*([getattr(p, 'parent')] if ÐÌü(getattr(p, 'is_absolute')) else ÂÚü()), áÒÿ['__dir__'], ÐÌü(pwd), ð(moon_dir, 'Libraries')))
    (sufs := (p, '%s.☾' % (p,), ð(p, 'main.☾'), ð(p, getattr(p, 'name'))))
    (F := (áÖï := None))
    for F in ËãÂ(ÂøÚ(dirs, sufs), ð):
        (ÄÊPSH(F), ÄÊPSH(ÐÌü(getattr(ÄÊPKE(0), 'resolve'))), (F := ÄÊPKE(0)), ÄÊDEL(2))[2]
        Âçß('%s %s %s' % (F, ÂÞÅCAT(moon_dir, getattr(F, 'is_relative_to')), (h := ÂÞÅCAT(ÂÞÅCAT(moon_dir, getattr(F, 'relative_to')), ÁÜÙ)) in TP_CACHE))
        Âçß(Âøî(ÂÑÖ()(TP_CACHE) ** î, ' '))
        if ÂÞÅCAT(moon_dir, getattr(F, 'is_relative_to')) and (h := ÂÞÅCAT(ÂÞÅCAT(moon_dir, getattr(F, 'relative_to')), ÁÜÙ)) in TP_CACHE:
            (áÖï := TP_CACHE[h])
            break
        if ÐÌü(getattr(F, 'is_file')):
            break
        getattr(failed, 'append')(F)
    else:
        (F := None)
    Âçß('%s %s %s: %s→%s' % ('✗✓'[F in __ÄÊIMPORTS__], '✗✓'[ÂÞÅCAT(áÖï, áÍÖ)], áÒÿ['__file__'], p, F))
    ÂùÆ(F is not None, 'Unable to find module "%s"! Paths checked:%s' % (p, ÂîÊ(failed, '\n')))
    if F not in __ÄÊIMPORTS__:
        (ÄÊPSH(__ÄÊIMPORTS__), ÄÊPSH(F), ÄÊPSH(None), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        (ns := {'__name__': name, '__file__': F, '__dir__': getattr(F, 'parent'), '__EXPORTS__': {}})
        (áÑÕ := {})
        if not (native := (áÖï is not None)):
            (ÄÊPSH(áÑÕ), ÄÊPSH('code'), ÄÊPSH((áÖï := ÂÞÅCAT(F, ÐØó))), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        (ÄÊPSH(áÑÕ), ÄÊPSH('native_code'), ÄÊPSH(ÄÕôñ(áÖï, get_code=True, native=native)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        (ns := ÄÕôñ(áÑÕ['native_code'], ns=ns, native=True))
        (ÄÊPSH(__ÄÊIMPORTS__), ÄÊPSH(F), ÄÊPSH(Module(name, ns, **áÑÕ)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    (mod := __ÄÊIMPORTS__[F])
    ÂÞÅCAT(mod['__EXPORTS__'], getattr(áÒÿ, 'update'))
    return mod

def __ÄÊADD_EXPORTS__(áÒÿ, *áÑË):
    (E := getattr(áÒÿ, 'setdefault')('__EXPORTS__', {}))
    getattr(E, 'update')({**dict(áÑË)})
    return E

def __ÄÊADDGLOBALS_CLEAN__(M, áÒÿ):
    getattr(áÒÿ, 'update')(MOD(ËãÂ, áØÁ=ë)(ÂÞÅCAT(M, áÍÙ), lambda x, y: ÄÔýò if getattr(x, 'startswith')('_') else (x, y)))
(__ÄÊGET_GLOB_MODNAME__ := (lambda *áÑË: áÑË))
(__ÄÊSET_GLOB_MODNAME__ := (lambda *áÑË: áÑË))
(BOOTSTRAP_GLOBALS := getattr(globals(), 'copy')())
TP_CACHE.update({"MJwLGvGhZE7OWolu4ZSlfd9LnZj5w0ag3uVxG8W3Tmk":strd("""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"""),"o4FAyrZAJqjH_l7wgvA90o_16U52IaY0hzG_E__W-rg":strd("""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"""),"UfmWzOqvuqCwPcS7_qziHrRyeBfNo0wA4Ew_hP4twjw":strd("""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"""),"V8Vz5YnYBKkWCgJhUvPBshoZsdXyyxga596ztCfF6DI":strd("""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"""),"xqYfl0kCuZH1j3j-fz0bObguuIzMeXQ_kyQSfTLAZ6Y":strd("""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"""),"cs0gvjzBq43oFFqcorWbG5WxiKV5b6EtLj7EvgnUbFo":strd("""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"""),"m2ewnVHe37lzzb6UvI72fT5z6lH6tDVrzJ2hXXhQgwc":strd("""eJyNVVtrE0EUfs+vmLeZqSs09i0QIU1CDaZN6QWENCyb7qRdutmE3Qk+iA9tg0ixCr2IWBWL1IqVolRExD6df+Iv8czsbJImqTYvmZw5l+985zsTBl3YmV+8x2xbnUqz85WFJdtmVIZCUIus+a2640eMc26R2CdXKMyUK9O58qKdLxdzc+itk9wvMj4YYBFtrszjuXo7XUulXNEgoXgYelLYkQxtL3BFIFX0IezBb55JEfx4DULblAQtSbyArAnpSBn2nCxCBTWe6hMK2QkDklxrO0uaYkn0+CyWKsSrkzWL3MgxXSO3SFp1xljbJ5ksSRqfVFmUHY7hJXwdukrXEjYKxTLDBGjRQButkGDEc3h9TatoiihnVLElo07dXusoQ7/9fqu+F4ioj19n1a1RSVX5ai0GjjevYHMs+PWb4k6we3i7Beewr+DjaR9emPwDEDXMkko9Og6NcmgYyLHH+ZXwxH8dnZx2WwQukpJUbhCcRTZLSkT4kTCAqpHvrQrlcwHP2GylwGATzuDSIjG+rOoqv7zAWNrC0o8e604O4UJ/X8K2ReZageA8ju3CAbyDA7zchDfwLatH9BMla1BYxHeaddcx1TMJLUbElKxI1aHJdQi7OpdB8gF24JdJpPcsFhE3EGpXuTDKK/FRDfSGnuwe2qgu3PPYQtTnmseVQMsi6otOj/1O4o3n9MB5clAKUyiFqVgKw/unl9xxXbvut1Y3ouHlZpF0QqnFkDBmHDLj9I/g1WhR/01JiRO4I049iWu/ur9hrwsH5cHNS/AETrSqt+AEPrLlmQd2fqGYWyoyRqepWtj38AX2lEtV0UYnaEw7XtE/Tz8pl/GOtDfzfCZe4u9M1Ud7XoOaiBXH8kaL6WSeyCOi0tuIJU5Vcs2KSqqMw1Lqwlv4Aaej22Ok198efk2K/0eqt+2upukI9pj6qbnQcmSwjYDPdO5En7twbCgeM7WGDNvxq9XE16q/G/+aNOoQQ1azipq+aLDYUtgRPMUaPkaIAP83HNnEf43oxhpSkZj6Gkp6VCgJxa/YEXyOset2/wJyt7AU"""),"w9fOMVfwKf4f4YlHP58xpTJXVvAW0b30e0RKpTjiw54":strd("""eJyFVM+L00AUvvevGE+ZWSK03Vuxh2rrD6zb4u6thKG7mayBmJRkCs3RRTyssOKuwioiLLJXD4oeRPTw/jHfTDLJNLYaCJm8ee+bb773zVB4DqfT/fuUczV68Gg6eXzAOXXixBdc5guROS45jpLDeZRRxphLiszBcHhvPLk9GO/zO+PRYA9rNNTDEWV2gUt0eDLF8exmx2u1fBGo2Fs4h588zPiTRPJMLoOAmijWvIBrl+zAFbyGl6zXIviEWPYMLuE7LWbx5wO8KydNAs6QG31yLORcytRCdKRjpaonFXKZxjokor/Ar+ACvq6Dx4nUC1So/wHcTELDhLFGquut2mJI4ATpfKOa1RcazZ8e+nMV/AwXvW366dlaN1YzZVodHUZymSAH6VK0qD+Xgpsk0usTs5CCeAUfe8QsXOb0Nu0qCGPfYaZ0tY3eyjWw6CO2bgT4hTPn8NuCxfS8bv0WMbHX+aztbRQySFISuqRQW5Vdw6Uikc+yKDwStOOSvSQWzGt46BOcwo9aOnKrT0KCWIYCtQUz41nosZqT3OqMsrtafq2ATHO+SBb4ZtbmFmmyyvuKnoslR/27eJpEyVNb1G5W5YoTeIMOrqQq7eAIR1FbOEr1AqA89E1R1fb1yiTMtDaFV3RI9znNsJmhj5cC0yzU+aY0KoXQp7/NsB8qnDaiHc/cBsPRmHaYipjuRmbBZiMrff9NvNikuWwwQe22/qM7psB8I1uW0g+F2l3moU+b+emG/G7lH4xnNSO94a5ZHscda9y2RdhFEXYrEdTFgL3e6mU8IWfwvnKzOo1V6pqLdB5rbVDxDyhBQaU="""),"4lRJt7Ng2-ZyG_1NIX-gCz5sBhjkCe8D7ruyK3amh5k":strd("""eJytWFtPG0cUfudXzNvOUleFSFUqS37g1qaqEyMSpEgErRZ7TazaXne9NJaqSoFyawoRYKAGgcBQaBAoUquqolESHo7Ul/4L/kDzE3rmsuv1enaxUJHQrGfO+c53LjtzZvOOXSL5mXLWte1ilRRKFdtxSdbMPrV6DAPm4cWX90czY48Mg2oVa3q6aN35ZNoxSwaX1xJkumhPmcUq1fUOedequUbedkqm2y5Imdzow3s0rGFXDNecKlpt4nqCCLmB4eEv0pnBgfRDYyg9MvAANTjQVyNUDyokCJ/OjOLzxMf9kz00X6iRZIpNb8IZzFPt37+20Ib2z5qGdHpyVp7AHPwKB7QXmrAOPyVINaU9KaNM1aqkNIIPKHABi6nP0YaVIL1CcEtP9hD8m7Zc03UdSmERTpgpWnVzluOQQl4qEgv1CM7aMy6jqD1zCq6l6YwbRZFLeE092zALe7BD0bSuk4/8nxgKbgzWYAXeUs8mM4l4+eJM9akmRZhZDibosT/Hcmecspye6MOo4OMq/MbZFs3SVM4k0vskGcw8Rg/M7NeOFxFd54njKvAex5ewy2M6BydwSqfsWoJIFJx6DfUkG7dgocWTTyPTUQ3953EMY4boYL62YAPeJlrEuLlNKrPFaOLjLKxSuNApzUlGbWZ9kDbDPKE86LPQgN9piHvFzGUF4xU6ISYnEYEwhBw+XG8+11huWJHotBUiUXzcoB6sdCayBq+EtWMmJX4zRKbEBXbhQpYpL+o+HdPE1nBpG16ElvonvUofHknTfp3NBOxJf2pJwnP1B9U+7K8fa77hGtNWCxnVipVtk/QZ1uEsiiEu8RzW4fRWTFspllRqmp/3FtUOqccBqQDN82iaa/8PvSfjfX19+bvWp591xfN6dbsrOR/2rtqx42jHDjsd85a2Q0t31D43sW6vAm8gp1XHchaJrcvxwBupJnddzXuT63L7a6usWAR4jxREtdWhKapNQjU7oXiMyjOlUHlKhV8k7FmE4jffmk6npsy0eiNQ5KkOe8LcCm3lU9IXaojLnq5gid4JJm8+Onm3e707ygff3+7qDAVfdiu4pC7FvWhv6tGluNJtKdZxixfpPJTjsfKs8oi6pUobTwly5CnzcQPetNVGohPHrgwhzv3MMKuIc3jHc9uA2RTjODQ+Rml/Ahl/9z0/qBvwJz9K3sEP3sGNya/JgliSxpd1BbNTuei5eRLrXtV1VO41pPJ5VzGyasoY7YWYeKCHsWDYv5RUaGGUEzk249NnOWUVWj3ErbtosaNfheaVUseGFItWyppFFVrkthaLdr3c4GDK/UZRd+G2ihed3075NedP8B1QD3Ylku5BiK4XjM1Yumxe5XxH+XaFhmWsRNuR2kddpfd6+XkcJc/RvVC2G1GgsSdUtVjIsitJbzhX6gxCWy+EXLeb2CqKiwAKkEKVPLDLlrgQhI4N2tktYxvuuKztVKzYlYgFq8JOZK8E2M6st+4ExCzn/CryBPCmw9zUfVoiW57roRtKOIS8alnfexbcL+dwaOhe66slNXFOeq1yD7+6GDkra0hiN+zMH/Y3LzuP7zaMrTCGvKcFQbbm1N2DV4LHoVI4iXhtTmNL9O8Nzqpi4m25qirW3RD88U3uTzsV72BShPo1nPuhromzGNqak/NAtxINchEA6Z9sS1j4QI1osuybWS7ABr/sX1/WjSKripowJPWNYsEN3VTiCQfxHIHX4uufwRF8P+z/vIz/P96OdXTl7/BIRrsUpx3pVoJYKa40h1nZ9lXYhqJTnWZSmVHj0cBgemSiuwZmHvbxxV6KaGEu9EkeSPGFJPgOvApt/kfoU9L/9CD2lhpHXYcFXfUVQjT7ChVBQK3ScebQVkQVUOyLwlkE1AqLzhW88Xu1SNcioZtKaFlUa1cad+bWJsR+HB+HyIPOC61Uqsl3YVGur8px3ht5U84PLqo9GE+nNf/12ZBL3K3R9MDQyL1MenhkDCX+AykiTUw="""),"YMjSDBJA-1uwVS6rFisSOuVkBH8kW157LSh6l0OXiSI":strd("""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"""),"vHu4hBcHeW969p2Z54gZQFcZ21imbLK7S9USTmJ_GIg":strd("""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"""),"Gx1WAK4u71dm9QxL4dNnk3s5cTToMocAUCIPy4IM5-Q":strd("""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"""),"0T-uZGPq8PjxCidwXmsnKPvViz9WFsWpxVCjvVE48c0":strd("""eJy9V99r21YUfvdfcQsD3ZsoI4phMIPXJnZMzLrZdTwY2J5xbTn2ZktBUkFm3YNDO1i30WbZStnY2izsYdD1YdAxSmEP9x/bOUdXP61Sh7IJFEn3x/m++53vnhvz8XAwnJisVGZ8NpjfHA1KLHgy+aX8rUR/hSiMHXvOxresoWfbM5dN58e24zGaW+DyjrzXPDzgXOta3e4nb719++rGJhed3udfaDrTut3eliaEzjgfTgyEognv7/Nt0dnuYcdwspNpN3o4Axuq+9e5IbClwA/bOMwwjOK7xXdEgVdqxJxXqF2eyFP5kAsuv5YX8oTD95m8z+USvpaEvckAiQKfyB/kU175qMXD5Z7IZ/JMD57flVgnargjf5Z/yT8QfFN1C2AHF9vYUJFAIl5XZOr/BxmIck++AAEExHkds4Zi1liP2RtyqhOnSxEMHQQcHsk/04gl9kGjqrgC2DmMWJblM8FDfDXa19miFJPxAYR3Km2d1eFutHuBA5VTsgasZ5sNam5km3dybfnf0a8BfbgbtZB+LZ9+tlnRzzbn0s9nHS0K0hlMoRWG/OrtTpx3miKi2DgQdr0W5vwM2l3Tm3rmnIdkdsKx8G4k3reTBItAsNgTWB4iF+ep+VRAZ0ZJRWCB9qruHh7g3EqCtAY1qZewHk91dqBTT4/vaUIlYe96bhL2WmvVsHxAvgooIsBmPmDzTQCvrgLejgBv5C9wdy3AwsgcM+fI7zsDywUjlwoMroiGn7bT9/KJPOVxTMCBtP4of02cScwvMdsZcR+J4AWD/DSVBA2oqWD0ANTBUR3IM36NbUcZkk2twEhLwHoRGUm7oomIMM2fEMpS/gOlLKp3RE+IaNSR6Q08z+EOHHaD42PTGkEY8tx0zCbAGXw4AWXosdNjZarBv8i7ld02L+o0BKtkkZkz11QUUVtCcEzvlmNFIHAgnyJSyuw+Op1tML7obAHOlTLz8QVV0TxMw2zgmUCq3haFwjX5QH4jX/Lg6BdRuo7s2XjgObaFCTiVF6ADEbgWHPP4ikOh8yWcDCmZwnySphj9p3hznstv5UOUlZzl5TpL3pfP17FWCKg0iQ8wdaARNEWLBQJ1yDYZybivh0vhVByI6O9cJXuRDuDOpkOTGzr70LbM4AjTmYH5pep5gYY6YANrhNl7JJ/zAxEkE5xZiKV7IL+6vHBJJjPTggCYYCPQ083Vc34ZMSMS8+TOVJ5P7MuYReRFWjt47FN7aoG9wnY/Y7tGW23a+TqbFi8QNljaq6BckZAxuQnnyU0YNrqrhCh3wf8orsAtaQQJg+K+GVcvF/flXktknTdPJPWu/Ds/qT5lCNz4+FWmf5J7bEPH+ToHdwRIVQ5xRFJAio+WjJHQf2FmoU0n8iIrZVD1Qu2g6sey46xE5YuRHgfmDwSlUew9ZqTjxrHxRINiCHezlQkXqeekzwmlBE5DjZx1naQS5sDEG4rrecAVSVPKHXVAUdVTpQDrgqoILvzUMUeqW2efmYtyvBX4llozJtunwymvamefZJrI1GHo2gDorBTtSm2ljK+0NGqi0O+jBLvVan//42aj1T7s9/nRzL4JQTlKpqWKPPwyS30L8S/EOhCI"""),"hxpghYl1vCc_2zz4A-dVRihznBGxbu7xdAJkgWxfP4I":strd("""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"""),"pkGnG2eplJt5eRjmyUKl5K5mDb-n0siD5YQeuPoiGf0":strd("""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"""),"XawvMKRS-9QDcVrB5km4D0SPMJyCryrSC8_RqOSCdmg":strd("""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"""),"SRHMwZ76R0D5i3lIhWWHvsdHuvCNdMb7_yjvw4DGEUU":strd("""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"""),"9418KM1Xo_OoOb7QGALgE93GCl1a3HnwkDNNUXw2X-M":strd("""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""")})
__dir__=(__file__:=áÌî(moon_dir / 'Libraries/Compiler/main.☾')).parent
from sys import stdin as ÂÐðþáÐâ
from time import time as áÏÖ
from subprocess import Popen
__ÄÊIMPORT__('text_format', globals())
(ÄÊPSH(__ÄÊIMPORT__('to_ast', globals())), __ÄÊADDGLOBALS_CLEAN__(ÄÊPKE(), globals()), ÄÊPOP())[-1]
(ÄÊPSH(__ÄÊIMPORT__('ast_to_py', globals())), __ÄÊADDGLOBALS_CLEAN__(ÄÊPKE(), globals()), ÄÊPOP())[-1]
(ÄÊPSH(__ÄÊIMPORT__('tree', globals())), __ÄÊADDGLOBALS_CLEAN__(ÄÊPKE(), globals()), ÄÊPOP())[-1]
(IDENT := 'ι')
(BASE := ÂÞÅCAT('/home/ganer/Projects/Moon_BETA', áÌî))
(COMPILER := ('python3\u2009%s' % (ð(BASE, 'STAGES/BOOTSTRAP_ζ.py'),)))
(DEST := ÂÞÅCAT('/tmp/bootstrap_via_%s.py' % (IDENT,), áÌî))
(TMP := mkd('/tmp/%s' % (IDENT,)))
(áÑð := ÂÑÖ()(show_preast=False, show_ast=False, show_py_ast=False, dbg_parser=0))
(header_com := ÁØÿþÁÙÇ(lambda ÂîÓ, ÂîÒ: ÐÌü(getattr(ð(ÂîÓ, '%s.☾' % (ÂîÒ,)), 'resolve')))(ð(BASE, 'Header'), ÄÝöÞ(ÐØó(ð(BASE, 'Header/builtins')))))
(pathlib_import := ('from pathlib import Path as %s\nmoon_dir = %s(%s)' % (PEV('𝐩'), PEV('𝐩'), ÂÞÅCAT(ÂÞÅCAT(BASE, ÁÜÙ), repr))))
(to_py := (lambda áÖï, *áÑË, **áÑÕ: lambda *áÑË, **áÑÕ: ast_to_py(*áÑË, áÖï=áÖï, **áÑÕ)))
(moon_to_py := (lambda áÖï, áÖÝ={}, áÏè={}: to_py(áÖï)(to_ast(áÖï, **áÖÝ), **{'reparse': True, **áÏè})))

def moon_to_py_debug(áÖï, show_ast=True, show_out=True, show_out_no_rename=False, show_preast=False, show_in=False, **áÑÕ):
    if show_in:
        Âçß(BOX(title('IN', show_code(áÖï))))
    (ÄÕÒü := to_ast(áÖï, dbg_show_gram_tree=show_preast, **áÑÕ))
    if show_ast:
        áÍñþáÍñ(ÄÕÒü, 'AST')
    (áÕÃ := to_py(áÖï)(ÐÌü(getattr(ÄÕÒü, 'cpr')), reparse=True))
    if show_out_no_rename:
        Âçß(BOX(title('OUT', show_code(áÕÃ))))
    if show_out:
        Âçß(BOX(title('OUT', show_code(to_py(áÖï)(ÐÌü(getattr(ÄÕÒü, 'cpr')), no_rename_vars=True)))))
    return áÕÃ

def decorate_code(áÖï, inform=None):
    if ÁØö(inform, ÁÜÙ | áÌî):
        return '__dir__=(__file__:=%s(moon_dir / %s)).parent\n%s' % (PEV('𝐩'), repr(ÂÞÅCAT(inform, ÁÜÙ)), áÖï)
    return áÖï

def compile_file(áÖý, set_fp=True, threaded=False, instant=True, cache=True):
    if ÁØö(áÖý, áÍé | áÍá):
        (ÄÊPSH(Áÿú(áÖý, áÌî)), ((áÖý := ÄÊPKE(0)[0]), (áÖü := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    else:
        (ÄÊPSH(áÖý), ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0), áÌî)), (áÖý := ÄÊPKE(0)), ÄÊDEL(2))[2]
        (áÖü := ð(TMP, '%s---%s.py' % (sha(TMP, (ÄÊPSH(áÖý), ÄÊPSH(ÐÌü(getattr(ÄÊPKE(0), 'resolve'))), (áÖý := ÄÊPKE(0)), ÄÊDEL(2))[2], ÂÞÅCAT(áÖý, ÐØó)), getattr(áÖý, 'stem'))))
    Âçß('%s %s ⭢ %s' % (IDENT, padl(getattr(áÖý, 'name'), 25), getattr(áÖü, 'name')))

    def R():
        if cache and ÐÌü(getattr(áÖü, 'is_file')):
            (áÖï := ÂÞÅCAT(áÖü, ÐØó))
        elif threaded:
            (áÖï := ÂåÔ(ÐÌü(getattr(Popen(ÂÛê('%s\u2009o%s\u2009%s\u2009%s' % (COMPILER, ÁØã if cache else '\U000f7c49', áÖý, áÖü))), 'wait')), ÂÞÅCAT(áÖü, ÐØó)))
        else:
            (áÖï := (lambda ÂîÓ: ÂåÔ(ÐØì(áÖü, ÂîÓ), ÂîÓ))(ÂÞÅCAT(ÂÞÅCAT(áÖý, ÐØó), moon_to_py)))
        return decorate_code(áÖï, getattr(ÐÌü(getattr(áÖý, 'resolve')), 'relative_to')(moon_dir) if set_fp else None)
    return MOD(Áëý, áØÁ=instant)(R, ÐÌü)

def compile_files(F, threaded=True, cache=True):
    (threaded := False)
    (files := ËãÂ(ÂÓÏ(F), lambda x, y: compile_file(y, threaded=threaded, instant=False, cache=cache)))
    return Âøî(MOD(ÄÕéý, áØÁ=ÐôÅ if threaded else Áÿú)(files, ÐÌü), '\n')

def generate_bootstrap(dest=ÂÞÅCAT('/tmp/bootstrap.py', áÌî)):
    (pyc := ('%s\n%s\n%s\n%s\nTRANSPILE_REF(moon_to_py)' % (pathlib_import, ÂÞÅCAT(header_com, compile_files), ÐÌü(dump_cached_imports), compile_file(__file__))))
    if dest:
        ÐØì(dest, pyc)
    return pyc

def transpiler_cli(*áÒø):
    (show_docs := (lambda: Âçß('Usage: e <str_to_encode>\n       d <str_to_decode>\n       b <boostrap_dest>?      - %s default\n       o <file_in> <file_out>? - header ✗, stdout default\n       O <file_in> <file_out>? - header ✓, stdout default\n       r <code_to_run>         - header ✗\n       R <code_to_run>         - header ✓' % (DEST,))))
    if ãÊú(áÒø):
        (ÄÊPSH(áÒø), ((m := ÄÊPKE(0)[0]), *(áÒø := ÄÊPKE(0)[slice(1, None, None)])), ÄÊDEL(1))[1]
        (Æå := (moon_to_py_debug if 'a' in m else moon_to_py))
        if 'e' in m:
            ÁØò(lambda ÂîÓ: Âçß('%s ⟶ %s' % (ÂîÓ, PEV(ÂîÓ))))(áÒø)
        elif 'd' in m:
            ÁØò(lambda ÂîÓ: Âçß('%s ⟶ %s' % (ÂîÓ, VEP(ÂîÓ))))(áÒø)
        elif 'b' in m:
            generate_bootstrap(ÂÞÅCAT(áÒø[0], áÌî) if áÒø else DEST)
        elif 'o' in m:
            compile_file((áÒø[0], áÒø[1] if ãÊú(áÒø) > 1 else '/dev/fd/1'), set_fp=False, threaded=False, instant=True, cache='\U000f7c49' not in m)
        elif 'O' in m:
            ÐØì(áÒø[-1], compile_files(header_com) + ÂîÊ(Áÿú(áÒø[slice(None, -1)], Âåæ(Æå, ÐØó)), '\n'))
        elif 'r' in m:
            ÂÞÅCAT(Æå(Âøî(áÒø, ' ')), exec)
        elif 'R' in m:
            ÂÞÅCAT(pathlib_import + '\n' + compile_files(header_com) + '\n' + Æå(Âøî(áÒø, ' ')), ÄÊCUR((1,), {}, exec, ÂýÃ, {}))
        elif 'D' in m:
            while True:
                Âçß(ÂÞÅCAT(ÂÞÅCAT(ÐÌü(input), VEP), __highlighter__))
        else:
            ÐÌü(show_docs)
    else:
        ÐÌü(show_docs)
__ÄÊADD_EXPORTS__(globals(), ('moon_to_py', moon_to_py), ('moon_to_py_debug', moon_to_py_debug), ('compile_file', compile_file), ('compile_files', compile_files), ('generate_bootstrap', generate_bootstrap), ('transpiler_cli', transpiler_cli))
if __name__ == '__main__':
    transpiler_cli(*áÑË[slice(1, None)])
TRANSPILE_REF(moon_to_py)