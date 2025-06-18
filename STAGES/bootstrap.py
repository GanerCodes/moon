from pathlib import Path as áÌî
moon_dir = áÌî('/home/ganer/Projects/Moon_BETA')
__dir__=(__file__:=áÌî(moon_dir/'/home/ganer/Projects/Moon_BETA/Header/base.☾')).parent
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
from pickle import dumps as pdump, loads as pload
from zlib import compress as zibe, decompress as zibd
from base64 import b85encode as b85e, b85decode as b85d
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
__dir__=(__file__:=áÌî(moon_dir/'/home/ganer/Projects/Moon_BETA/Header/system.☾')).parent
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

def PL_FORK(Æå, *áÑË, **áÑÕ):
    (f := ÂÞÅCAT('/tmp/%s' % (ÂÞÅCAT(ÄÕØÃ(NULL, NULL), ÁÜÙ)[slice(2, None)],), áÌî))
    (p := ÐÌü(getattr(os, 'fork')))
    if p:
        return (p, lambda: Âåß(ÂåÔ(getattr(os, 'waitpid')(p, 0), ÂÞÅCAT(ÂÞÅCAT(f, getattr(ÐØó, 'b')), pload)), ÂÞÅCAT(f, getattr(os, 'remove'))))
    MOD(ÄÕéý, áØÁ=getattr(ÐØì, 'b'))(f, ÂÞÅCAT(Æå(*áÑË, **áÑÕ), pdump))
    ÂÞÅCAT(0, getattr(os, '_exit'))

def PL_TEXT_COPY(x):
    try:
        from clipboard import copy
        return ÐÌü(copy)
    except Exception:
        Âçß('WARNING: Failed to copy.')

def PL_TEXT_PASTE():
    try:
        from clipboard import paste
        return ÐÌü(paste)
    except Exception:
        Âçß('WARNING: Failed to paste.')

def PL_CHECK_PID(p):
    try:
        return ÂåÔ(getattr(os, 'kill')(p, 0), True)
    except Exception:
        return False
__dir__=(__file__:=áÌî(moon_dir/'/home/ganer/Projects/Moon_BETA/Header/ops_A.☾')).parent
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
    (ÄÊPSH(MOD(ÂÚü, áØÁ=2)()), ((P := ÄÊPKE(0)[0]), (G := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    for Æå in ÁØò(lambda ÂîÓ: lambda: PL_FORK(áØÇ, ÂîÓ))(áØÆ):
        while ãÊú((ÄÊPSH(P), ÄÊPSH(ÄÔÔç(ÄÊPKE(0), PL_CHECK_PID)), (P := ÄÊPKE(0)), ÄÊDEL(2))[2]) >= áØÁ:
            PL_SLEEP(ÄÝôÒ)
        ÁØòþÁÙÇ(lambda ÂîÓ, ÂîÒ: ÂÕÅ(getattr(ÂîÓ, 'append'), ÂîÒ))((P, G), ÐÌü(Æå))
    return Áÿú(G, ÐÌü)

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
__dir__=(__file__:=áÌî(moon_dir/'/home/ganer/Projects/Moon_BETA/Header/ops_B.☾')).parent
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
__dir__=(__file__:=áÌî(moon_dir/'/home/ganer/Projects/Moon_BETA/Header/ops_C.☾')).parent
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
__dir__=(__file__:=áÌî(moon_dir/'/home/ganer/Projects/Moon_BETA/Header/ops_\uea8c.☾')).parent
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
__dir__=(__file__:=áÌî(moon_dir/'/home/ganer/Projects/Moon_BETA/Header/ugex.☾')).parent
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
__dir__=(__file__:=áÌî(moon_dir/'/home/ganer/Projects/Moon_BETA/Header/ℵ.☾')).parent
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
__dir__=(__file__:=áÌî(moon_dir/'/home/ganer/Projects/Moon_BETA/Header/!.☾')).parent
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
__dir__=(__file__:=áÌî(moon_dir/'/home/ganer/Projects/Moon_BETA/Header/𝔍.☾')).parent
(áÐÞ := ÂÞÅCAT({ÁÁ: ÄÊCUR((1,), {'ensure_ascii': False, 'indent': None, 'separators': ',:'}, jdumps__, ÂýÃ), ÿ: jloads__}, ÂÑÖ()))
__dir__=(__file__:=áÌî(moon_dir/'/home/ganer/Projects/Moon_BETA/Header/🌈.☾')).parent
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

def termclr(t, fg=None, bg=None, rst=True, rl=False):
    (rlw := (lambda x: '\x01%s\x02' % (x,) if rl else x))
    (mkc := Âåæ(rlw, lambda x, y, z, w, v: '\x1b[%s;2;%s;%s;%sm' % (x, y, z, w)))
    (R := Âøî([mkc(n, *h2r(c)) for c, n in ÄÕåØ([fg, bg], [38, 48]) if c is not None]))
    return '%s%s%s' % (R, t, ÂÕÅ(rlw, TERM_RESET) if rst else ÁØã)
__dir__=(__file__:=áÌî(moon_dir/'/home/ganer/Projects/Moon_BETA/Header/kots.☾')).parent
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
__dir__=(__file__:=áÌî(moon_dir/'/home/ganer/Projects/Moon_BETA/Header/extra_globals.☾')).parent
(FRAC_CONV := {**dict(ÄÕåØ(ÂÛê('12\u200913\u200914\u200915\u200916\u200917\u200918\u200919\u2009110\u200923\u200925\u200927\u200929\u200934\u200935\u200937\u200938\u2009310\u200945\u200947\u200949\u200956\u200957\u200958\u200959\u200967\u200978\u200979\u2009710\u200989\u2009910\u200903\u20091100'), '½⅓¼⅕⅙⅐⅛⅑⅒⅔⅖\U000f7db2\U000f7db7¾⅗\U000f7db3⅜\U000f7dc6⅘\U000f7db4\U000f7dc2⅚\U000f7db5⅝\U000f7db9\U000f7db6⅞\U000f7dba\U000f7dc7\U000f7dbb\U000f7dc8↉\U000f7dc9'))})
(TOFRAC := (lambda x: getattr(FRAC_CONV, 'get')(x, x)))

class UPSIDEDOWNSYNDROME:
    (NRM := '0123456789abcdefoxABCDEFOXîĵ\U000f7e88ℇτπ\U000f7e8d\U000f7e8f∞')
    (USD := '\U000f7c3d\U000f7c3e\U000f7c3f\U000f7c40\U000f7c41\U000f7c42\U000f7c43\U000f7c44\U000f7c45\U000f7c46\U000f7c47\U000f7c48\U000f7c49\U000f7c4a\U000f7c4b\U000f7c4c\U000f7c4d\U000f7c4e\U000f7c4f\U000f7c50\U000f7c51\U000f7c52\U000f7c53\U000f7c54\U000f7c55\U000f7c56\U000f7c6a\U000f7c7d\U000f7c7e\U000f7c6b\U000f7c6c\U000f7c6d\U000f7c6e\U000f7c70\U000f7c69')
    (MAP := ({**dict(ÄÕåØ(NRM, USD))} | {**dict(ÄÕåØ(USD, NRM))}))
    (flip := (lambda x, m=MAP: Âøî(ÁØò(lambda ÂîÓ: getattr(m, 'get')(ÂîÓ, ÂîÓ))(x), ÁØã)))

class SCRIPT:
    (SCRIPT_FILE_LOC := ð(moon_dir, 'STAGES/.SCRIPT_MAP'))
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
__dir__=(__file__:=áÌî(moon_dir/'/home/ganer/Projects/Moon_BETA/Header/highlighter.☾')).parent
(styf := ð(moon_dir, 'STAGES/style.json'))
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
__dir__=(__file__:=áÌî(moon_dir/'/home/ganer/Projects/Moon_BETA/Header/meta.☾')).parent
(IMPSIMPS := (('ℍ', 'ℍ\U000f7e19\U000f7e18\U000f7e1b\U000f7e1a\U000f7e17\U000f7e16\U000f7e1c\U000f7e3d\U000f7e15ĵ\U000f7e88\U000f7c7d\U000f7c7e'), ('⫚', '⫚'), ('¶', '¶✿')))
(ÄÊPSH((lambda ÂîÓ: ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ, áÍÇ), zibe), b85e), áÍÇ), lambda ÂîÓ: ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ, áÍÇ), b85d), zibd), áÍÇ))), ((stre := ÄÊPKE(0)[0]), (strd := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(__ÄÊIMPORTS__ := ÐÌü(ÂÑÖ()))
(TP_CACHE := {})
(TRANSPILE_REF := ÐÌü(Holder))
(EXEC_NATIVE := exec)
(dump_cached_imports := (lambda: 'TP_CACHE.update({%s})' % ((lambda ÂîÓ: Âøî(ÂîÓ, ','))(ÁØò(lambda ÂîÓ: '%s:strd(%s)' % (ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(moon_dir, getattr(ÂîÓ[0], 'relative_to')), ÁÜÙ), repr), ÂÞÅCAT(ÂÞÅCAT(getattr(ÂîÓ[1], 'native_code'), stre), repr)))(ÄÔÔç(__ÄÊIMPORTS__, lambda ÂîÓ: getattr(ÂîÓ[0], 'is_relative_to')(moon_dir)))),)))

@cache
def moon_to_py_cached(áÖï):
    ÂùÆ(TRANSPILE_REF, 'Cannot transpile without transpiler!')
    return ÂÞÅCAT(áÖï, +TRANSPILE_REF)

def ÄÕôñ(áÖï, ns=None, get_code=False, include_builtins=True, native=False, Æå=EXEC_NATIVE, ret=False):
    if not native:
        (áÖï := moon_to_py_cached(áÖï))
    if get_code:
        return áÖï
    (ns := (ÐÌü(getattr(BOOTSTRAP_GLOBALS, 'copy')) | ({} if ns is None else ns)))
    try:
        (r := Æå(áÖï, ns))
        if ret:
            return r
    except áÍÚ as Ïã:
        Âçß('Failed to exec!')
        raise Ïã
    return ns

class Module(ÁØö(ÐÌü(ÂÑÖ()))):

    def __init__(áÑÞ, name, ns, code=None, native_code=None, hardcoded=False):
        getattr(super(), '__init__')(ns)
        (ÄÊPSH(áÑÞ), ÄÊPSH('name'), ÄÊPSH(áÑÞ), ÄÊPSH('code'), ÄÊPSH(áÑÞ), ÄÊPSH('native_code'), ÄÊPSH(áÑÞ), ÄÊPSH('hardcoded'), ÄÊPSH((name, code, native_code, hardcoded)), (setattr(ÄÊPKE(8), ÄÊPKE(7), ÄÊPKE(0)[0]), setattr(ÄÊPKE(6), ÄÊPKE(5), ÄÊPKE(0)[1]), setattr(ÄÊPKE(4), ÄÊPKE(3), ÄÊPKE(0)[2]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)[3])), ÄÊDEL(9))[9]

    def __repr__(áÑÞ):
        return 'Module[%s,%s]' % (getattr(áÑÞ, 'name'), '✗✓'[getattr(áÑÞ, 'hardcoded')])

def __ÄÊIMPORT__(p, áÒÿ):
    (ÄÊPSH((getattr((ÄÊPSH(p), ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0), áÌî)), (p := ÄÊPKE(0)), ÄÊDEL(2))[2], 'name'), ÂÚü())), ((name := ÄÊPKE(0)[0]), (failed := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (dirs := (*([getattr(p, 'parent')] if ÐÌü(getattr(p, 'is_absolute')) else ÂÚü()), áÒÿ['__dir__'], ÐÌü(pwd), ð(moon_dir, 'Libraries')))
    (sufs := (p, '%s.☾' % (p,), ð(p, 'main.☾'), ð(p, getattr(p, 'name'))))
    (F := (áÖï := None))
    for F in ËãÂ(ÂøÚ(dirs, sufs), ð):
        (ÄÊPSH(F), ÄÊPSH(ÐÌü(getattr(ÄÊPKE(0), 'resolve'))), (F := ÄÊPKE(0)), ÄÊDEL(2))[2]
        if ÂÞÅCAT(moon_dir, getattr(F, 'is_relative_to')) and (h := ÂÞÅCAT(ÂÞÅCAT(moon_dir, getattr(F, 'relative_to')), ÁÜÙ)) in TP_CACHE:
            (áÖï := TP_CACHE[h])
            break
        if ÐÌü(getattr(F, 'is_file')):
            break
        getattr(failed, 'append')(F)
    else:
        (F := None)
    ÂùÆ(F is not None, 'Unable to find module "%s"! Paths checked:%s' % (p, ÂîÊ(failed, '\n')))
    if F not in __ÄÊIMPORTS__:
        (ÄÊPSH(__ÄÊIMPORTS__), ÄÊPSH(F), ÄÊPSH(None), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        try:
            (ns := {'__name__': name, '__file__': F, '__dir__': getattr(F, 'parent'), '__EXPORTS__': {}, '__þIMPORTS__': __ÄÊIMPORTS__, 'TP_CACHE': TP_CACHE, 'TRANSPILE_REF': TRANSPILE_REF})
            (áÑÕ := {})
            if not (native := (áÖï is not None)):
                (ÄÊPSH(áÑÕ), ÄÊPSH('code'), ÄÊPSH((áÖï := ÂÞÅCAT(F, ÐØó))), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
            (ÄÊPSH(áÑÕ), ÄÊPSH('native_code'), ÄÊPSH(ÄÕôñ(áÖï, get_code=True, native=native)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
            (ns := ÄÕôñ(áÑÕ['native_code'], ns=ns, native=True))
            (ÄÊPSH(__ÄÊIMPORTS__), ÄÊPSH(F), ÄÊPSH(Module(name, ns, hardcoded=native, **áÑÕ)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        except áÍÚ as Ïã:
            getattr(__ÄÊIMPORTS__, 'pop')(F, None)
            raise Ïã
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

def show_imports():
    __ÄÊIMPORT__('text_format', globals())
    (show_table := (lambda x, y: Âøî(Áÿú(ÂÛÅ(ÁØò(lambda ÂîÓ: ÂåÔ((m := ÂóÍ(Áÿú(ÂîÓ, áüíþËðâ))), Áÿú(ÂîÓ, ÄÊCUR((1,), {}, padc, ÂýÃ, m))))(ÂÛÅ(MOD(Áÿú, áØÁ=2)([x] + y, ÁÜÙ)))), ÄÊCUR((1,), {}, Âøî, ÂýÃ, '│')), '\n')))
    Âçß(show_table(ÂÛê('Static\u2009Name\u2009Path'), ËãÂ(__ÄÊIMPORTS__, lambda x, y: ('✗✓'[getattr(y, 'hardcoded')], getattr(y, 'name'), x))))
(BOOTSTRAP_GLOBALS := getattr(globals(), 'copy')())
TP_CACHE.update({'Libraries/text_format.☾':strd('c$~!=Yi|@s^1FY<C=!|;XMCAm;{eWWashHey5t-I(M8%_t@bgt_t=MTcYIz4kid9t5?(eo4o-mJ@W=z=I{`tE;2_aIAip8=3+^XeRrO;YJ8N*hgk<UN>h5}VRdrPl)%sMk<ryt^fbk9fjQ>zBmM2|fG-I$@v0kba4Zgtd*v25tF7tEH5xpy;2A|`1_$p)k9RDxhz%8_w;RegH4Y@yIr`l2-M<h@9GUKQDRsKMeoa38(1t{F&pYflV7+SO(*FBaH+W>?s{IO-YwYF=dEG9@<mhopJ<)n8DIPt@J*s$Oa2tCg~`|!vi7M7kB3X|1|$r}7Tw^b-uL`cs9tX{6QER>P4Lnt_5`P+NUv9eAc!MqD%{X)C$#}=gWxDf#d-+P~>EQAcO@oJ+|aNFfV+x=G?cTBim(eqlY<=Tc>Zq}!&HP^HlJA#vDu9GU|a#{AyXf9WI{jKy{)abuXI9B~cHrH`d@Jr`S5|v0a+>Tc$PZnF-&@dU`h5vW8trL=vQ?~~H^p0g3y9{>3CUmVj@=L;nl!I~|_~<ZW!!}5H{G=Tv(w;7v0FOv(i&MR2<GF9~Glad;^jg(=9J{oSj&00lMx0TjlWo_kWtaWE*#PXb#t;}m-gw<G{Zn^MvKQJ6CxHg{HDevZc$#11>#PHWjJIJISxE<})~XG+9Wj1siAo3<-{9Q??;Z_IkdRp@+f=RUq55(Sp>Pi%VPwemC~kO;M!mro`BN6r4yvVCs{xMaS=qoH?6qv+E}Oz~Bces<XwMO6gp!7wr=yt;Nv^R`8^adY2K!*_AS&P?zd){Wm7mTy7E_W1&KY8mj6UMemL>H467~>)=ZiuQRNQfcj=TWa*Z5Onc#Z#uiH3--@hxj~z<@sjdP7<fa4F42ECN?m>$7RJ8n7LU_8~KpRYG7HnT(MVIOBNd`1ky#1OUb;g;YRcI1ktbdK4=WS#}#Vq=LK%#JEN*NZH0v%2HHrWQS7uh)aZsOW9hkH{EJTLz1+?^w4Gp2L2LqHq!M}vBF4o3-X{BWqUSb8m7emECW0!jYs3D_B?^aid%(%FUnY2OOB<q<W-`mJiD6lwmk5~K+Q^S;zRO!iJvA*mlTGKniUuTNrneMl<I>8OomVlN|p3(b$WNA?Vo2^+PKR|>&=Lau;O9j<Qs2<W)s*-;3~|F#z(7w>{GtL{#pdngVWyC_RoHr`^a&e@jc~XSN7cDQi>wHAYxm6ETXMVVkX1y*~TRNEzdu6MJuZjz8tl8R30c^xW6<FE#iz(Z5#YvXvYjL-ah68HX4aJ8tG&Y(n+!??dA~{Xmz9Mk=F%#^erH%nGm4eMg`(^7Q6ve51ckzh68udAQBjg<B!VNOF+9%;4TV~oFGw)7oH+N)Z<_}*aqHXX}4O4x>d-f(%@3*d?aKDbLusTwpT14YcUa-z7H$`<rA=8Q>7b!ATBd*$3T$8n}`O3V%fdeoQ{Sf?1^C6KSG3~`#r0Vrv~2ByW{Ny_mgT+#u3rVJ$dw@V5W^9W>Ge68!T!x$emJA$})<LiWrW4$Rcy$T^LYlB@5(7%RJhecBvDCQ(Un6r~sH#!DJEoNw>&3AU-Fuf_Z)g%7UxfN5x57ED|>`YQ*?e_X~FJTm5gOQnORgc*Z9(rZeJ<>>G!>s8pTEgarv%QHXftAi662_g+<aBr@P45=up!(B>6>McE+byD63LhEso)(juo;LT;hXHzf`W9R{RGJP4r2%&ckYxUP?dW+2CpdJ`Q61xI}pX$zylm;8HX`WH9+i(mT}Z{?=bj<e6dc-y~t$G>>jv}93rMcl|^i8u0r9bCpBPtqlbW|IxFY13alZ=yJ1$SG5@-nA&FUtKaacbEtzhQu+TEf9&wcmTNz#nUi>)t8gJ8j#E@qwMPdz|ltdGSZmSwjq@iDg|ug6J(b)$Ouyqx}iLQYk`6nP-ma$kwsO_EQ!;|Ywuv&-wpw-gc@A<kzl_g5yrCc4SoTN^b?}<ovIcRunFH&Hw|Ka&KL0pAsYfpiB`0K?BiD|jlp?)$|%jms6GNx0XW`izRu^Ps<1_Sc~s=H5g5q{h|rycyTd?;8q08lawU{!P|IeeOuF;~I^{o{XJ@A@xBhUJccx`rInydm^?4>xept!ub!=lQvl~(*AQqD)?lm%S-s4-r9hR6<K@w20w3tD)4A;Toeu@baHjn`tB>|gKF$*+R0cJ74;rjtPV#Nw-Wp#<gw9uID_g12mP|rYi)XvcTe1Wg_7WJ`ECLi~N=ZU;qrx^46I)BXXv)KC_zP<osbqkA-GyJI~;_V8*q_a>PwX=<KWW1D_1X0naP*chVENx3By-I6=Mq-N6cCup?1%~scG8}zeQs+9<*O4W8a!9c~*_<hqn-w?aQI$-}arDzEL_p0O9dxE583^YT=J*7VHut4Q%s%M_1=@~ybE<l^I8hz1%Ne@j`ks9j!xj^2?Fa?i`jpD@&RvJl9^Nk8z09<q>uW$f#^&|GY+J!)2j#ixhY4a?Yz67^Dr2<7nU2@V?T-%*R;p!B=beyL1doYeO+f|*D^{WRz@{wNHe@X<-$~B!1xiY>y)RnYy3Bv1QCE(h$o83RAISE(Y#++@k!&B!_9-!N9fbc$_8#$5gn3b}_(`w$nIM;GUaY(%*Zi#4JkxXM<lL5?+micF>os$F?zx<s({pEZZ%Oy&b#Ga&-_(%H^ggjk@Fjki+AGAx8Itl6=>*q4;Wu?}L-)Rxy-f|<48d;e-W}b$t9#$*-nY7UOJ*ux$o95u*JZn=G8x%^C);n;+k_n7knNYU-9*FvZRxJRbjrVfTRf3CrM-LoYb*Y>&;7Lx|ItJL(W4hzes|@?GrxPq@2>mZCBOTn-(B{*m;LUl-(8bWE0t1O_x8N_#qWNuhr@pNni`bf^t)H}%x(=%``s@zc*O5s*Moh!2U~CGK~ZnrqhTct+v_iUst5aiJ>}0Y`e$$O&0pu$OVHkm?&;T|z2oY|=*@k)SJb_-?p1Wp)jhp;kE3Cw|6O0c48LpeTZZ2y_^rcl1AaGuTU~-?4Sp-|gTll*8A^D;`$LZ-6j<oq3a;$?;RlaM-aTp@f>eTXQyE0IdjNS!jvWriIu|g<$A>ZCnRYgR{G|WYV^d_p2gW`~&V=9ZO@tAAI0jCO>MOo_Sb*cJcN6&C!~clEM-sE_;Ne!j-!1X;{28Orvc~W|;e?SebyZD;T`p8KsOOyXe5>E%?uDM0p2RwUs(&iQ)=A+j{HAQbfn-tCm|kl(C^jL@gnFuBz##{~Q0)frY)90oZl~-{dBG~Y6ht|FRDLj`nkXpYk78-&%}%*Jwe2DONe8Q{LZMNtyM=-o+bSYYZ($s<CiR&L%BzWtnRe1<3<-s;q_;KPCuVz?7BQ~hCV55Qrkh51(uftt5h)MP>n|-KOu~R}g%?|z@VfjYn|zFco-w@xJAXZvm4;PY_1t>fv{>A^&0TH$Pd#KOn~QCLU)cTl5YYj$A7bNhqU>;i>`?Y^f3NH!LF)8l_Z3)O*dePMJ79JH?_za-GOH{6VK1wuJk7qYWk=s+l-~^CKSg*FPKJ~I6+@&f6?r){-|(;cS<f-GSX4jkn0iFSiniG@WCof?_0ZcM>GGHr`lkn~8kTP=@{QCQC=@X0y?gLr;k}PP96NmUNTI+cYRwX)s%YoT6d!aUD;FJtQQiz7Y6*fbCIG-jjmu(OR^yf!x74^T#$vyCx;E7tHo;2G4!*HAJ2ZmI1xE0<<^W0<$piE>bS41LD7g5v4^Yt&6ji;1L{*<=sGtETwPJ0;_g~zW0H*cP>fH=ID~OLov?dgI&1jLOa3q+5xs9E}9xy&!0gd`}?YV8Q;NfTe@n)-D^q4euWpKiasP2zk1*SVOVPan4IN}93GCAYIADo5+6(4X%(9QhSId$ns?7Dajjj`~24Uik{Vy##)U|4cnhBxEZ{_PsTqt}2in`?NJE(F=OXLys<#)L83oHi@QOtIk^%?6HIMrpb=@ft?WRN6L%MZK(E%Zu_uIT8f}V&*@a{ttKjvuE968;}><&1$9Cu8<V!8yPEwHesFoN}I}YN+Yo6x1}FnJP6iQ;)r|K$XWRXrwH0C<{G73qnvA0at%~<3F={bm<g{(e^W=5O3@jdGGDU9=v`3W*@8qOu%tGPF(Bn^w*(wM*XX?ZGB^ZKeX(e6vwC~pTRU4Ii2NT{EBTZ'),'Libraries/Compiler/to_ast.☾':strd('c$~c&+iu*(^<7`VJdu>v%}Oay)W9N@B{elFUl7Sa09ha?E+rA(CD|d@UZE&pS(msL;^<<_N*bq@4Y#r7s7_m?cABIQ1N61u(ES2`LeH5QlEd3xWV;JNGs~Gd_v>&qx=wFhocWbz7&tq7?&5_HXAMJBiG7VYp-lp{qAWGM1+x)ox~^9gzHxkV@`LFMXU3;zjEU)~@$+zmLHhNSrppH^3VVFvBFyJbjm{5gOT=s{r)vtmLBFIM6XUZQeXcb<&o$}}sVM5Svp`JZ*ulFKUek9PHhCA1s0eDC9?-w(dIAJTgZSFH3zLZd4t+w`Vc#L_Tdm=ut^uAu(5IUE>i)g$%dN3$_2;kd?|;j{#VZHv??+4bp1!X#vJdH9x?53x34GWQO2hJ+DZDr`Ks$6_)3tLom_DTsG!-`@j<cyJwi|YCe)XTVz#@*1Q-*4mv=R)k<oAUEH>NRkh1)b8w=cN3F%4G+HdMD4mC!THAk;ua`}8mLM>c*h#^+-ErlMRkiE9MQ9tmrBx}t={X&MdNT?&^C$6fTq<3*2Hwz1f1G=R#`TCOpfSCsm~lHr>qut}}TzX7mo2IC+kwjJ#o9tMn`(y#Q>LkfI)(1k+KMwaZ*3`3G=wI?^kZhBX3Kx_ufcEE9iT-3!7^$_b9+@)bQ7wRU;_L%OS#_=(|qiK<+@#k~Z`N%oonHs9nH`wul9&2<J%=oWb1{^c>ReD5!hz%XjO<ej=(?%-*<+s0MdflhnZ2W<)0hO0Qr@BC0QG~nPrJv9{F%(sSExHy-CMFY3hqwZugJ?~-`dCCX%txhpHFEsPscG#!@cj4YD}n(8B-A9h<!0Yn2wHwmCB!a*2sE*sMUxma7pw*bv6)#IotMcP)$vJ83OGCcK6Vgv0s+0EOirD-^g%7L#u8iLY=vZnn<0Lj#R9WUmhl5fKB3<*4q=Qb0imCDozO8G3PY;uGSI}c(!khrXOS<(uu?~}&Zd}dU2%f!ku+Rlhb`hN=RMbspQC^!6!CKm5OkA1mRNzUtF>wdCeRW)VPaMh^EUc}I;&<5r46U>nCw-)>{VzItCi$9ewCdrHWcL)_n#w;9w+`#N~Etc-(c|47AINT7+Blb{A>D9N)&cOlAuHs_^JY-K1yygXLx3txhTe|w;)p{$~VeeV7~>$3k9+0w@G)B_=)7p_Id+m&v4IU{j~#Mks~3(#F1oYNqn_{NdhHBHXWqHb$|L#kVp|!8;NOnV??NzFIB76#p>w7PqE0t>PiY^#D-whG<+|BK<BxEtN}(=DsW|shqQgv?S@if7jr6$pm<h=G*q_9as5`vHzjz@dfixPc-EDmKtrNL1_nr2w4RL|gN_n~QIYZL{`Nnl3PWr-UBncaES#`v#Z?3dc#nR;(#{_JvltJ=_&_TvGHyV5{i3WqK!hPlY7Dl}%St$jVND#3N(4;Qa(YNvRjsBlDHvC-8ZNX2ELQYlXIRu8{Xr!$RDLQ^ZBz$K8UfOc5ULlo659hla@;x;gZb^9TMv!8ZIxDuIU9(mv{cqV$x{3GE`q|M#B2s?EWQFFuPr;l72eDF-0RHHh#uy)Cw<Y*76|3rs5RQz>TK@7U*`Ls{CzL8z9+5UzYfoCBcVC_jSJEzX^T6cpXnM?;t?n@QbR?Nrsc%1#e{q;Qw3l4PC&#4-DOZe1|beg3UYqug)E1=HwsB8_2aNsoa)ggWXue4#<cRrl$boQ!zw`fh~A>#X_246;;7CRO8lK2hnB}TIybKuMWkLDy-okl!r8xih%*;$5mUEl?6#T<VAVyX=`V^RYmvlC1?Kr&TqAL$lG5DI?5Y{h7UG!|&+478A9TKc*xB6fZ0>fRZFIgo>^%NG2mlM~EWcPs8)XG~Qp6_W67A5-;&up^4)YBWUpk=IGfQJ-y^>rx+@_ziV{*`aAjU^UY0UEc6_%9ZHQf3zKEkQgdAQT1Iz-d}BZ7@VWUdw!lF0IUO#2fpUs^KmxVdL)OGd*#)zqUORb@mGZF@fr1N=AC*DNeE;wh>)I2T-;@Za=(+pU8F%AE6<KGTJ8L=ASR>-`8`B+MT89T&Q1jAqqJX?!@QM|l#8?cilzvjY$i#h{?&s{+$Y&^P)^AwKYtf$_xx&mjY7g~*}?fx+okhR5{>gP04yB|e$)x2{T1f1*m^SPIR8a1>0=$kPd;olY*vp27^10-w%OkK{V9gsrIDJ4zl)X(d}j<nl|Aj2mV+KynD1zS<q0(3yuSgZj{`+lJ@&Lx?!o#>;r(wR|Hq3G55Xk|dOPMGXn@p_}R2%Ruc~w2YDnZ5Ni!5N|oVwL2wr=S-A$Wp>*qvZ8v*qNxAW%1a#2pGc={urA2jxYXIcJ~2M4ax2V&m>ZQ$Fqa+pma*t=lv{c9qC-BxjaTf@l6<OogtLm1%yV&_7||uw8WP}<n1*iH&tICJJ|XrK>$O|nr}&QMGy1asyX}6Q?;RFulIv~$;zE}jx4zt6aP`qZ9X2##ZFLavXpz_~)?1cs&`;^}>{+~Yu%NQ`e8XBc9k-jmhBk3cvQoH%M+&=Pmw9Xi#0-|YA^~Fh^!EXa>6~kFzua0MR0E=su!_1Q?3{y!W7*m$ue5b6d!Y}m^;X&I@&isAaaAcv)1nbd_mw$<r7OGOH!U+*w#<;-+T}qeX%sVbCin8hE0XCZ-6^cnrPj1vQC37X5tj{Y+y$U<3hTeFc!qZ%JnmMMHuFnFkt+5Dhs{>w|IFcC!N8sv{}_!Y=5%YLoXs~7SK~WAys+NTAftwc<+<UYm&E8k$^8hQK_$Q^&``_bN{p6sH{3?<iiJE-*hQve+a5Tc_I=mbxp^>9xaM5OCYi6eGS_KuBT{y~r#boM%g$QAmoIOIgMPIng>m`%lgC7US8{4p=N$;&QFK*xO0MA4|K9r|b*npo1>jNH{(E0mJ`wTZPhdX#hiGnXJ)Pg#>sG^Zh}CimbF<YVWCa3Fx4hh1vfG0d;%NLidqEpGq&sx0YmAvowRpoNuNC4%o@x#YtYNLdp354;f~!ZoPc6Bn&*jeflsVgN%l1S5-u-jM4De;#qolJhe;+?Z2$aVVUa#6DblfE+^px?L*>~hOTBd^p0l*=yC*I5p7(?+-r;MqO@OM@-hM~njm8vM3%70h`8sZaO{~wy-Gco'),'Libraries/Compiler/rewriters.☾':strd('c%0oFTXPfF`Q5)_^R&B0bR^Lv;ECH1<EBixjWN@79FJx#FGdqt(yU}6UOK@^FeE?#8)Lv+97;kkfrOG28VEC-_x^>>_!s0S^!v_j&)GeDGohWS2cgyKT)zADtQ_(Q`Ru^KKRUG<UhUp{VE@>7t>)NGZ+2?h>)Iu2rrDnInq9|r-IB$I?cBBN-97u?*}3OnZDh~r&V4X}uJfl+$5khkEP8wY0l1#nTA3UenD!4_f&XF9==rt7?Et4;Bp1k2cWA(ZzZt*h^?Kp$l4T$61s&UU?0S2)Q`<QC5kSOXv&5hw)3mPNgIV?AiM{)GvHRbUX8_L{Ss}-V$vnJWb{+V*NG_9~>HC-b{kB|ZqC8oW+e}o{4^{QUwn?iUSak9QH@xpo!iVu-&Udqr>-J`Q|25<&m<se|1$qr#dHWka`76iXSY5PTjSg9;Q=ZQRo!V6MgKm`J2+dh?*%}(Q9FBQ^C{6>%F;D?$U=0sjHmqw~UTZo=Dat-M3~3CP2?O=9uw?Cs?@jaZ0yLoPeX^*qgno|fLHTGk4qJVCi+=K(T|Y7_x@X^wfCK+P<pwC3-cFVsSnVpg%S5RA{#><O-hl)G^6zW6d{zFC549)*@GtOtb3rRj&<?%(UTtJ-bm#b}<Jj+jlse=lxkoM_-zJdN_Mj~`1Q|Jb2ZxvkDk9FQNk!n1W50O5@p$FM8Vnd@U%70tujw*WPH>P-S8<hlFwJH#sCQu{y!m^Z8m_|7yg%oc%ifDMc;8;0P6vvOjRVF(7~CWXAUav(K<P@_R$xv(CMU=`9Rz<SO{(KJ15U>adbN7H)l=0G7JW+Yfo7i|x20x+j{b@wfdg@Qh63FUVU2^{cd4<NCs)W*hk`s_!DXl!oG0hWvNVFYvFmW1x=mIb`<H8%?!)T=y#5ZapWyZUmuoA>;q@^9F!5%|+Fr6MRd|)*wXJ0BfVT=$Le!mEuT$%G{CdM{I{nbp4NG{qNgJ;sOp?sU$tt-FD9m~v_`Seub!}>z&j6=X;BMT5*SGKjAa4MWH@<_{_wafMF97()BY6FwAOYWBg6}UqM1%kVyIiSm`|ay*yt#dcH&q9KDa{5H1!p##+w!kfhj5PEaZ-JWZE=%EEg9gnLT)M6-eq4lS{7ikA`G5+KmNXyYhOk^VDm(uIvPIs8u^jRBpY0LBb4esT2!QR)9d*_>G7)Ts(wjwQ$!)%UJ&z2sh&EZLQtz8@dA^(R;6T1xIhR%#ty=s`?H<iF@%oUblkW1{-JWYe7L;BdtJHNnC&Q^x^q+Er<V4q*FDy)&CCfeA%;h9!FrKfxJ<=xuNt}Mck5oqN86J>i0KU@N$vcBl9A{Ml066`mLLRr;!ufw81>^+nvRooMeq_leaz!iH0^PlS|npU@EVN=0>)B$8{Y4dn{Mdnsc7cHyI(Lel%_n2a;x3TgOnB}#iJaB3H=<@@4Fh(FURZ6V4aO|1fOifG*2Fr`zSq^$%3}sg&}JTyFiBp3nyT&S)tb4?37=~5VianoRz2zS0eWImSa1vU9z-n;8r4%_sKeJ^5TK5nl3(jEuAz1=tBn%?%p-JYyY439sJ9_U1R(Ajw1NY27)gwW7IZhVBKkVIo1r4%n6LJFrMrBRdQ7VT+ZH)O|SX=PH{qONn~EC--AszPJgV=my}Q1Yf#DB5+tnW2Q4o+7E8by-CDmB)VyAMRtx*m^i3FozMUgMvD=*yyFfPLh?0aNA`S)%%j79SC@KwQ7byd{JLC&;Bl1nR*{J(YMQlr>!AVh&*fqMxskkoCN^T0_OVmb4jOfnNR_v$$3j@FL?KPXmq_@at<ez*jB*h9oY5>MDGT;g*Fg)Y9gjn8uNi1=VHM$1ug6pdIhX}(U1w~|^>f~bdf#EEZH4|u+`A9(_Hab6v)Yw({mX(Matbwn=bv1gplc*O!wErIwb$V)MkylV%>hv)-2WFta{@Su>63q(3yJkeXnj2}biBHH0)kx9JTsJxbQH&`e%AFIx3#O~0M>yg;y$bZpwJWQ(vK5XyPrjmN5}}|*Sx&?{8t^E-9nFPOEj|_EbthJ9TVAsx$xA`CK#l<$3~_Fc6{kQNT#govPd_3Ht}NNL=Q_2X7XX#wb-U@dUM0w?j6srm5?-flLud&M*9rd{L3IZlZ=r3_QH!}ketC7^3QfZp_EncwryXa^D9<BtVK$2>WAg(o-`C431JaUs)6-oD2!~XK9??}X6rT};l#b{`nyq`yh$`cs7(E6<y-vq(O#_DqM>K1Xe<+nXXN!6ilZ9Gv1lt0GBd)%n1QRiD`W|LJnuF<EjV?7ssP#j}x!SgUHv7XPji%2u?SW!~k7`7x-@@ch8|``7bxofAs3wo+p4(<1MpPh<hAa8a#I?>Z<XMX<<xQ@f7y0`lf4>1+MfL(6gPVC5UW_DQVImgQo}@Yut1_w-GpO<TTcWzdhC9hTh~fjvSpXkl&DLeCo3fL#QB<s{-f=e4YwC1#6QO4#^cHGw_-PETyP<|t!%!99!*xZuF00038yJgilUfx{I9eW_Gdt@y{aL?dFtn^9N)6IHSoW_RkyXo-#!%Rp$PhKoyU8qGFKE0@9jzD#HfMqjnaq>c6)kVT(ih36&MRq4^uq!?2xPNCv&TWk2A0svDtsQVgh4RNSXq%i&m2}qJ-@(8Yns`$w-~GXr6m8O70lJ(HdhL7V3h`qDI<<iF4Qf$yAscY&JpHa#CQcY`<XIg$YjS2nW(`Th7l5PrmWaJV0)$}%#kc8We<bPP@}L_C$@OrmGOSc%8PNj<XjlTp;W4{#E0&(z^%hcR)BCrVi{@0<L*CrpzE3X9g0Ko_Vx*KK9o-$D66HBgoai;8DugR?Mw&$^jzJqL8Sa$)b;{x)pDtl;Kfoet>Y~7FMPv=?Rc|QOShE7VnSJpQ~NNea0_jM{3?Q)rX&)kmR6{tkt7c;TP(ON*xROc05u*p7gf!rfZ<52#)Z^%TF66lNFdS@km4ST3vh50c|8cl;%}oh=MN+<CWDMt(HMX&@u~s=2u*7B*-ow9!PZiv6^jH=4E9hlplKST;~G`kWdKVP0u);|;5LmMu-$kkAy$xVqv^*y1Q$Pw7Tf1xf`*Lz*H1RjW@!xaj68ImJ+2#JUyKD#;5Uz&vN*0!X;DQ?=+czXB!6z`QaL>+0#tUC%pSXWGbR{i`G5z<@!CNY<UVhoAl4yF@+b%X6)#2MUt&2b#&k*^w!bVL#B;r*!jGmE31LO36}mdA>QcD(Mwt+{%O+UAETMFt-}2M&2z0j5^Jh1$vspyT<Y*qpSMRWnDA)m;=3zPyrS9?Zp?D;u7Oe6QtEp0xSq#P93lu|@nwJFhtzm1MG44p~10$W(Vq0i-7eI>4ypEln$u2;#!cW^+_&J)l@S{Q4R;8XB=TMw*-N<grnpIe{s;tRMPZ0As6MD~xzFz<;3k=&z0vv|_N42|j>at_{5`h>@@CZdVCg;d$NG{mea7%74U96x?N-hmjANqOX7Cf=y!wmJ#>;sR+MeoEKpV2L|1hZt-hezDBRpcJGnL#lfoOEAqg-f=6m_^rfuR9Zu8q$Jt7@yeHTu-9rwBKq^`w*r?2Bh?aSFopfYDsG)yK0)GC8lPXOzhwvZhFY3yk-C^4J>CVJ~zx_*b1&Q?E&2d8hKNDal!}bPwVUa2#x$qW0$_I9vYCLDnw_j*CLP00wI~cTm;sAN-j7yKPKdrw*#pDaLVbp-NVXsS*US<t5-Aj`1e1GuPyyZM-fMwiGIR#ewlmtvt*Tu)mgH_mdjHHP$=8y1ZDh+RZ+~H#}Fvdu}_6d|Cqmqz`amvR(_C{S%n1%;i7#KW&o%huxRh9x!P^q9hS|vvqp-|Zx^kLI}LeWGxgk+C^&Xm3@41s61h&6N)|m8`28^5@-e7~vU&b+VCgY!Yddk1V$Pb?48U|iD%v}Q_0h0Nvv`I=F3sXa-M{I)SR|*NLGn55Jddj{k}uTsG}OvtLm;-t48q!H4Ht;R8Z2t;TU%pcT3n_h1Ka|v26R&;i;gH|Xc-UPS?syBf{{abhepJ#(Mty-_wYVSNkkj@GYQHqmbg(;uod}+Tk)xmHeI>R8oTm7QcPcC3vk|56UaQ|;l<o#c%4n?5(z4Vm5!utVw&pO0G}BKpfgx>r4tUjxqx0Z@taDjmC<W|$q5CGGYZ$2wkQ<|JhX6Xi8-`4{qhcZ<;kn5jZ+up2VY**<<)etqa8?tt2|zhmpvV-!Sj*kBg{~n*oG`dHR9UiGgPYiqPfuJ?G;B^Lwjn+6^BvIk_Gc=4Xg$|Dw64-cIY4i&F$zB3fRw322n+8fmzR3<w9R1YDi-~D{3p(WrtdEoMIt{ZA5i4_cVIxT>DaoE!GS@b`%Q6g&&a%9Z5W{fV|nqA97IUG`h9GKU||z*KyRyp|LSt!AkNFYDN!N(KNivW|iV`HWhAJQKP2dC)<r+vPABh4iEAc!Vkt`he$)TXf>9Mm|Flh#lr(^ef6;x!%htJ-S|HcEQwx(H*v&mwPSiG(k%bd;U|3AUxXIx3AFfv98aYLjj7G)Scotz0(SnddC-l+c9vY{^<eIkAwbien4;$CW+=ntM#4VkNHwd;>IRCOfjZC{Siq{bk>??(im^~0FPFp1vqhgcFgwY3!>Dc=85S7BC?y)m#r(Q#I+&AWDm46@&1%Wgy>T{wROb+<JGb>3p&v=_teKQd=_|)1>I`{8CF(eNE<qMWpxDqyT=-~#C~6TCkV_Y;UjeyQM+V#!9cHbmu1P-NZ5kCNaa!Z}by1ttPP8Dlo0^*{Gs$1xb){0#I-MTk(NH#a_>9pXokSwl3u29xA;JzLR-(jX@I9A8u__nhGgO$b3kIYd^}#qLs5ZI(#735_1&21L(7dS~qRG$`K%>#>`T<&uvh?2tPSD9^UPcCFKEP%0e<VLh)4`}&QbmgE2aJ0e7PHJFNf1Tg8xe{vGBnjjgA+tI=~Mx5HFh;PHQ&}9rGc)10*eq$0)9JgD2yOYYhhCuNW$V_3%Glvjn6POg8E!TKMhta%}TCn;6a!i<qOd*F%Q*_?5cG2UKdw8s+&4epPVSsyv8%8G*bn$8N<1a*dgQ)qm-jLDMzoFoAX2=|1%*h$)){L)|yiZ?UszS7i~A)Zf*{vbU5?ltYK6HrNlEe>`8X7*EM$ZW13NKcaG5mN6ryhokXCnss`~4#50DeIa`plo`h2MHUO@qgqIV#<GIwiB+lTP0An~Q!LAC8A%Jy`P_2nQA3ZnY_wzKB^0!iyLjBxKzXtY&#q#)}9Yo3oYSA^Tp@j=<to$7RL4_C?vb9GuAdK`U6f2mO`q8J~)xI|e@-10n6eTR6sB+va(SYlj4x#}9?6*R)Oa)%O*l&7Bdn!~xdji#QT1GqS7qp|{fwJF4%Q|ca^)Q-Lvk8%Za`t1#w}nDz@CIT5z}lXnT(i5q4@8NF=CJ3U+v)*WWh6F$j@btLK_9GPgowHhMu>W$g8+eyZ%#WI!ehU4z@9K2(UV-aC*2UcNMVUNrAoc-Z%1jEax;b1eA-K`{<tO@&$f{(OwuW#>Lsfcx41!uN~Y?0QbLwZ!;O<)W4C<5u(3)`*ksZ*oIuWFM~o-ZiSabOJXLRp=h3x;&k>8-fe5eYPfo~RWib3&3_cdHWIP2IEqEkEeDHq&o6rZdZHqZ&@ryHgpVX%iZiZ&H8u?lL>{zVvC_{q_<hh&MklFwW(D<bfF<I4oPfDhptHhOsH^3O+H5voRrz((h;YlY!baA7iTxZZxWLHWsbyHY}zwuGuFlxU$I$pz{Z>vF|vv23#QJ}l~vS;K<DLxh@%HS<QORHfk!%TqkD<QzaS3rPx%Z}zRde<)YxPUZv%i5Xt<dazm&*A8q3(fGtU*O45zW9&%*?LfZ(~W7OnVpqrQ^6io;SdkFYCnJ$I}pW=3P}@$KSP%wJE^B|Ep_Kiu?Q8E9o0?ara5Dw-a7nE4#FykB8jYT^JT)4Vz>N0w_BUCqQJ=7=zC~M4@P*1JWD_A$Hg#45yl`%9TQ<hT}0aF{{XOCmZ1'),'Libraries/Compiler/lambdas.☾':strd('c%02z>u(cB5dY3!aeS!uE^#E=DMBDwDz837AQ8}h36bT;87xc^ogJX9Dv=auT2ydILQ^0RKp^poC=`@d(0<szB>4;Y6FRf6+g-08F%HyHa(j2PGryUgnVnhNrx)liBS*jVvsoN{b!cSx$gynJC*irth$Ordm5F?=QuTu%NO+uP&;I>i3=QwyGjue&Z|K0D!$8fL96aC$`h<kX9uJSecyu5&wryK6EP3=QeU!}=i`g@$aM~ihM&AJCT{=e}X2`qcg*75>pX2S~3<-8`^Wal1dE}de#4C?`C&F5;R*SUxB$Q<MiNe}cH15gQ?71%$RkKEuV+rrj@P2%-OkdN>Ozsk$&ZGmsUs0vTnC>v|F1=3gdAl>7R5uv_4}1p?7J&S%^%AFYE9^fo<fj6B!od`#BBcGkk4}Tc7k(voI$z9rbcU|d`Q4s<&#!1iGy}gwL%`@Jee5%{9iK`kle@UZys%OYJ%;KneG&M|U~DFst42U6p;7QdpbX6H?~PB?kUN6RjTgn@FnL1H*wm7<lE7GkgaQH8Np5m794`_Ob%{R67Q;f8F}v&wyD!p5^sTZxgZGr-0)gx?;tO<qpq>-o^Iqax>;T_$8=vwpw|mNX00Q)5?e<tS6~b*bp2i#~ElFUU(#A>MsRqHR2Dww&UeCg9G73u*(dk?*d-i0xdMb>n3RWCfHsI0p821q`lkv#Lt$7j~RB5T$#EPV~aWexh(chT?uh2iyZ|5#=T$<mwG$-sK#RuFT<yv^UYkT+w46%mQFqK0D@0RPY3G*aL%K=^y;Vh@|U}sZ}*qi$a6yV`kt&|J6)<IL#rp96xWPR@Zdi~Y$uan7SX=j+<rA9f;;=rX4-|;oL3*3HW>WLu`={^qNS$Z?{6qe>ObD#b~|Bgw6puqq_f+Eq>M~+-ok!cu>&{|?P7;=6lruE-$5nD0oT#Q_Er=&J^cn|ZidHSeD+&&3>vT^4&iTx}Hdf{gH2`i0@<j6eA0zCPY$E#rk#_*Hf!q)&)!#3g#_wOkHmzxioZhmonZdN&WQH{bLxcNY;b3Y$QwRd!&VRY~7>L#wu`1(MqN6x<dv7MdUz}{-R0{@<_-V5o@4Ytkh8n5y+{TCfk>>51tuh*}w*RS)f!?g>jQC^J-NWG)PLu$Rgv|hhy&DX+9jY@J<NV1)FhCZMV5zHLD?(+vX=|xfK)+){-w-$9=-a2Xo->>A|wKEn`e>Jj}uNJIVY58i2p0{2NvR9EU=hL=0xjRhLCz><#SMt~fFmwseD#&Y<Q9c|Cyom_HyZ(}hX2RkU2`+%PkxOKAStDAnVH+jcT=N!7ft=nTxsf+tjgpP}`D1(b5f&p8lixyY*o7>gs~4^{Vx}ep+0S)7--8mih2$Y!vQf=reLaLbP0168V9x;`?(6gDsz};1^ag$72U`pANK1%E6hvG;gcyBzh=+BEE$E<2f6_VWbZ@(vk2zZwG{Td%XLxM8`kw|%9NmJZF7_A>Wvw$PBU=VVw~Fk(Hw|y^7Qo}X*`lcA=IK5954+xP-HJBEX-#iM8+v;#q-jdj4qAY$vGE@^f(nYd-)7<OXClrL-mvU%TjEnq`$5AJd`sxua@Ibv1FW~h${Fo6IAv&%)Vv}iy@KVll$not!E?<~<mAPKbizw&?w%3;WO5U!lXVpJB}d6qlH9g9ks7Pcw$e|k#QP-Py5shq7kQBV`#jb_!G_5SOt|+gm1IQ+%zKKz5tQ@HAz_=iNz=w_l(M@_EO${R+CgPBK>C3(2J{^f*z@ALBCZRqi+V=$yG#lej|WY7KJ=TM(00;B$kSF{#^QmiZzWKtPjI*2o{?o0vmR%W@Qie|0O1Kf0+m}WL(Z{ffs`^|C;WPY^rGd1z{B%amM>rV4ZW6@Cg4A02gf-)qmip_Jmfu8%QH$g=`+WfYAKoo&FzzO*HJe=#++R;5BbEQx^+w@60&(p;Luu4<%+Y!ZXXR|THwtYj$objn`Pq-E<SKLJTV?7Jhme;z0o>ZyQgg4V&N%v^Cs(A^CoMxvB`4BtRt;F6TUhR(s|VUDy|pgRXFf!drHy%T%~v1dR(O|ou(J(wx(7PEM<6YPrEMsfD`;hFZsN5=I;~U=Q-G%kc{nTsHOa-Mto7mo(s$@>=-2Rg^t0BISE2wp4vvvN(XW<*R+zOpLn$pW;BO^C0E<Vn@ciJcVxbR1=A74#$o!WFnl>@=X6K@;F+_K8RfpfJ#;LvEM|#~Yn>FgyJo!i5&TREzT+0`EBDM~w0)A7;L5z(JGpysn6aJlq=8u)2i9}Gl7cBfQKJ?2n&@A!HW(<49OG&(Z6ANiTqO=TF+Z!5O`q+$_Y<sK!R-u677~nd=3}s1>I4@V!Q3n-0C5<x$lg4q)#8aEQ~GIZC|;~|yOw>dAef<#=}KG<pdgVdgQg@af@C$YB5g}UO(u`_GMKd-5>%wP`Mdqbwd7>q*Zcql7tY~Paj$9e>?|8~2j7&`od)lXk$GpYaVnrP@pS=M0Q<0pmHE<i5&Q+m8eQ|{ajo3W{y*LgQQznrqDJ7DWG#F)f_goRb#24939c%*#>!wKOJ@*i71Me>*@6KI%%03nMj__3_^et`?)KXKB;rGMS5LL>D*ibS`%Me~G0&_|&VBpc*)vnMD*lWKh+ooQ@q5mJ6zm>?@dCY#JrrQLMgPb!Mr&YeJeRrgg7>@0!mg4W<x*-is75=~Xr~(OQlq>Y71c=b%clTYzllExOpP|Tc;(ZRm2#o%T)r+>NGyecaucA?_HhF*CjJMKaY5Y'),'Libraries/Compiler/expr.☾':strd('c%0=L-ES1f{hhyJUeL~(jpRG0AGoqqV`v-of-M`KPS)x;ugQtc-F0u>khfqFH%<c>pG{o~#sot`p%qQB3MomX&R>#y>=S=NfAhIByR&<HhDNP8$=<u2ncw&KE+&`Br*jLx!oE+xz4Pwe?ED$u$4(ptfgfLt9S@xkJLei<54*1GA--?=<jG&wW=~Al7W|posp->jf&u#VDeUS8Jj8C#&cXNkTb0ElN0x$Rv=p>EOM&0%(nH&1le};zk0AJ9NsYSiA&f&bIfW$nakoCcNN;yicPs2}l)778lti37Rl^mR?h~l)k{jd&-99_#pP4>UJ5@g)#Em$Pa0gI$$cY_y(M{2HiR_TCaM*bN+)@LPRq|KTpF}x#*%h^xk%Y_daL8zC3OO%t-@N6ZAnXMQ$hk_MVsopa!$V`@PA_aV16=XY=}tQU`dqOUzSKhxMT}p}xqEIE94zgSkFwIslT*U_cjW8QBygE*k#ERXWo3}Ve3nIzit7sblJi=#vN>O#LuCnMgM3C_BuZclKt!|C{SfHj#<1LpP>fn_RO3cVKfqwjxEb8J?<BWP0WxUPCE$irbF^RC<+<YJh2rHC`ZAT^P2db}{Q^8Q@X(oPB@jQD6nm0qA+evz)A0Q#+IK16^!^`fdwyi@uh{m#t?ijG_g8KEtJ<E5xqrgY>~YZS@kOPAAWU?#{`G6q&HN9jI@2gM<Ge}^>dyC1uQ=3E7{Ss~Jv6eyE906}kC)JRfrVH#USJ_sjTczR#E2I1w(0xK`Gxl@Z=Sb$^L}}Y`5{e0DOc0#8|Tgc{J->OrMi-SJ#YGTNrk_m-kh?L?+<RJY=l-#ww?dJwU^qd*DSIQ09BfshM1k9dakTdIMukEaH*U!xPeHVlr+*HKx1@8BF?Y@_UwwPQ&#6zcEPauHUkH>K#C$Oi6PRMGaaFvKQU~tB(&Eka%M0#aU#efHt~&QEwz&JF{9NgbV@r}9W!8=yYmif;{G?J`39IvFUVQ|XzV#z6X8JXK-O6Y@-f-O&=dXP6Zl()=KI~*leFi0M8087&kngX)$YWI_jfK9ZKKoa`h#bEKXhoP$k#lSYR4ET+E_o-fU(6#uIkH(=)A$fX`*mFq@f5~bRLk}QbZ#(ni(1+K_guofyT#0GzL@b;3~OJZm46dL&h#18#|vUlpO?52&mP}P6=}otsQu`^RK5)svK0dXSmZk2clad9L@d&V`|00`-e8BD2P|0HdpvMpPzIaQLKELUAH{6l%Ap3DvKKl@6Ig!Kd#0F*T`dQAKfb3M}zQ|XfA!Ll8BC0*DVjVsYF3LeR7RcvE_<E2GtRtWq5GVUCiWQYDiqM+mw)Z7JNuoZPyZ6o1J#tYOe%o2yl3dJkzBBtY#u4!yx7jS=i^IpmE`dN&$?|if$py;>fq`y2`FM$TKFnRq|)Dm&HD><_X1edffu~;JsEDAUnNT5a!@UNr;hY1wn^=G#O%yvpkDLnO%T72{qbF2vg=Vs|!?Ad_x{F>Ee0t<=<uToO5tat}vV}oBZfU18m_I;5543puOa{ID>)Ww!%z|X(UYDP8ZO)B{GbOAiGC}h?ZVRC>KY^P{rc;n%7rdTIHw0)9=W0EQ3*tDO$wjn<7lnm|UeCuprh1BICesHp0-1WzRjCIb=Xn#y&ivsW_fzDbC<8pAXhH2fKH*dOu;JPd2bjpd~=<4c0aWk3TL1ML8)1#k$%1>scUq$#94Kk!4kiA%)0GGvRuoyhy~Vs4=`vQUp$SNiSTJd?IGbtsWBDy-(JdefG%}alI_B5?Q(3A_-k1ckC1EYh<r%7GflyrMq$6<eT?I6bE&C29q^6Vq3DT?rMj`UfI118Jeyo&|0NkTBDx}ncQR7O*(NGMm~1ds!Qff5QV}I*#i~blXk^*KV2GR3y58oewi9V`}3AC{b*(QBZDlOeGdsNksV7^8Vl$p3N_(#fPk_W_`$_)1UKB&)0<KiQKDi|7;THnJY$u2!DAkbK(2Vy!E+}-O^Da%0g%?L!cM3xz(G;%)8o_vdMnGzt&7;ux4_HqCCQFw$v-941K+?(>2!XEeIjwQ<0B0l_}LRfhYfsR@vy;7Cul>3U{+46-3uZJr+D1cA21p|g$vsYXRz_n%=8&Yd5vD7>1FsnH!Bc%m3h4EVc6QFrR3uja@9d1O)16Ps2+Q<ybw1cSoWj$dX6;$(E(7#Mr1h^M*OP#iQt2J`7u<_Ny2^d2#>+(<Og*o-nM~(0)bH^BcQ2EPQZd9;MEZ4Ck#ake4%=fh7Y8fo=`-lG;5oDcvLJTwK(}5LTsm{n`KrY13ePO^KciWYR@_x#K$7{`mabJUw_EPzu;0n59e7gPtD?6rn1tUz=(pnEgs$x*yW*M;{k+>$NPMwmgra~%#x@^6mcHP;WkF-Bl5qob8wY|Grpvapg>e-+l_P36viE1N1#qOh#D~%+tJ=63d5<Ry`O>j*d^k>BKpfgN0A~n4B;;V>>;DTRg(&tj!Dj|9=HxP*T>|t{{F&lUf!jVvt-^?{Vom7Nwv__+lg$1)|JO|WYf**p;YPB%v4>kmlGa0(!HF)!>(RBG>ytrT8lC{X{NjxTZtmdL{C=}JN|Ra>})xXSP?S#WXF-i8x~1aHR7k$%|*6G?i&eH4E+k;4Y_{L?{$NwlWyYm_d|FC#k@kp)hAa+!gb*T|K;uNO%urP$rEzd28M!{uch#Q0(g^zv2rDWGQ%`%eM6=$$q*4d0pccYNT2Kr?|+DoDc)ULvGY@mO53?x;@lVFx+AW8xCm^*g@?vD2Ax|0Ul0x_u*F20#&}DQ&vJHaXip8ibDV5O8&vSYVbw!befXLuUz1Op_BBD?BcIZSOE5}jd>P#WzlV}=4rX2MRFs6iGPOm%(B)LG(yYR0lTUA6X`(DN!rF4$dLHDx)TQhI<nLNDn4~g0EwIdfCS0sS;&pP6-&8%ZzS?K)w{qX_qaQj|g{XXiwp=s0Pj{P|9a6bE*@2qTpFObz*(5##;0qMg_z)-$N<pb)p<n~dfewb58UzAi#taR!n0(AR^-TU#PhDES`E4T_Car@UJ`WobEQgqXIN%i&!<1@}tRuN?!D?Sz@5n25$hR|R=N(a3eTI2Kb)Y=}dwF}~AC9cFo+LGw`yWg$i=+'),'Libraries/Compiler/tree_txt.☾':strd('c$|$@TWb?R6n@XIn75g!D>U{k5Ft%M4W>=$1%xy#o9?7ty4i%?2|kDqZG%X$3cZL}6^qo0m7-Kc#6F#W;xF;c>}--IsWvZ}oH>{8eCIn823^>hU%ba`Tb)X?^Oc1q+h$aTLQspW`K`L+M~riBk=Q3!D9n^A)4B4Zoi7)2bLg#;+%Gad7+?`?uFT`PdOKZ9rCiY<p?Da2QrM9UZ7*;|AXW4s?7?rINfG>b4MN+L1T9ItfUF7WNE!B=EJ6h}p6U|{*$D%ZTx&Z^nqo=x_$-zx#H*7vi`>XDT_d+hT6M-)+b5YUNgAJ2S(F`);U#<>x=Pm)HVVZu!vtv2KpU-)V8nBHeNC%qiYRAPu_dEU-CpY`L%;ogtG*YAsE=P~)vZxURrzWy297tcU~??^^_${OuzPsB1?RA@;Nxi@UYPs?5H-w_N<BIbjdExh$g#)ymGH!W9i5zZTLdnWl2mRGoJBTEN<{dPFo3F&@2v{ua{<rTY^A_p6VBk$A~C+K>MFmyz*ySC(vKeNP7dKhe_z73Mdn(8;5?4)!U4R41H9aXH}Ea1NAwdVYfxCkcbawAG1W5(Ek?wYtVq?N$#n?3I+sE60e0Y*Nu>8I77;fPYFD{1$}90v4fKYd>>k>vF5L6jLe%G)$CW_KBI=7ykNr;Kjpy{hd2&z+Qz(V0SPH}Yr<dGuUAykLRyU&I<z|s|LaD`&FlHPw<MfZ<)o4-wO-YFpxFb$IiEF>QzhSQn2j#)dOYj6vw5qq@1U|CmnFn@$p_p4LGDfGVTG;pS1@@FnRnbN#XiPg^(LYZ=DVOn%v^Vp7CSKz2Ow~twUW1y5702>Mi|J&Z$RncC+lVDjRdUUWN~(;*QtHB6_yMP*+he5H-yVKVivLHdx9zT`=?M0i`l-3la%8ZLfX{U9M4!8GY$zTxwT2Aa@vGIu*Q&o8|C%)F5JOh8ikiM?u-H=A5j@2jK1PTD|2G`j#D9(G#u`$QnEDz@dQ>P0#jn^Ae2%f}cK-r$x3Cl'),'Libraries/Compiler/tree.☾':strd('c$|e)&x_MQ6u$Sb7*Cm5BDCFGv4?8w53Jkb?yZEOyP2$kn3QA+&Cx|Xtgzy)!YU#xvR4m^9z^u;{xRQ7GRZWy8VH%ZdGDKVzW2>gcn+u2{ri-2HG1%9I(dA+Id$U17hL8GkvT3oj*`Q9lu^c*ONz|FaCmP#xjh)~^E>0wU=M3F)WZ>Fc7aQDcrwND>}JPnwR{n%*jqS<pFGU?lSJ}NE`xxYDAv4yYnSZ66}*O*tk)v=gjn_rF5x>ZX7T3(yelV70?v>deR3@1T*}l!bfjaYswWk4nZ`OKqQAhe-~zs`gU5-~3sk880o+VN!-TO$s_U)VVo2Zw>3pM_)fXDgpC0;i75oery>0sG*;+SNGi6#G9Y%7QAP4DEw5UIqf}14L>l3q(f_McVd&DeU=JYo0DhOlWVWxDojo!*Nu;?SUZUp#+Gw1Nzg2nW_Zv7T9vDf*m?QIk?NKz8Iq)=OxUBjg!k<YRyJQB3ylD#Ar%xie)6P&`2S~_y8PeOuNh61$(Gvit4v6_?I>Ws3xT7Ip7Omn_S7Wih?<`!wP%KM6*izP?>yLg&J$x~a@ZdT=r6L^CTuB0mM;0Q-iTR2Mf0-!wfO;OeM^~xm7v^IrTbV&C(&9IrFkCy_|EY$g?G%AJAr@zgxA1a(Sq8-oN2E);qc9@Eo?nY+8W+N+o|4qEuq`7P`LG8BwqdTU+d?Q<y(hr5&UFM-roB8R6{BGqRjAu0?z2UA|9>*PP+_pv7MG<x@5!A(iz253&JRxWBzH+lVjaBNJi*z1qZBX$KC_zD`'),'Libraries/Compiler/node_types.☾':strd('c$}?RTTdHD6n^Jd%-haVSA|GbDocLg)~2cxBNC)Y1g#c(O|05pcfB;0s!D-!YYGuypay}!P-qY+Qmd+>Q4$`G)R+DX{y_5+dgik0^?G)(P?6BAXU_S~cP=|~X7i3+BKete*0t?ol@v-9+i^+O%s#bx3<Kuj#h3R-Gh>eogK8CPdb()c`DEHLO9q$M5@fn)PnpFk)%6Z}*Q&Wj-gZi++b&3%+~~u5G^}A)4A-10T5aNbf(W^R;o&dRnZbedLt`jCGVlO3IM7!kR1Yd72%pZ3;`7AE{gXX3U#O8}icN3A8O&4d-@mrdhW5{zhID#zR-V8d{0axO7n-mRKP5;tr9CO5Ox3ESG=dK(Z~=>{&(VgJAiY9xOHcL?{F}C1({&w6VG&N4DOz=NmgA5@UMdm`^$5<|GcKd3J#z}KrRj_tMUhK*O+DK%3wy9b(X_6UkNlq)3T_P6U<KY%&n7d8c=_T?^{FOBm{|@c=&?V?a%Y^foSx{zsNmx&{KnZ9&C*oPB+~mN8O%IJ56tY>ju#PK=ZWJg@E*sPu*+jQ2Pbe!r|epSNEDoU4fP}&w_u^glTRblQ4Rg)aSUUI=wQCKU<2MJTEw`yO)9g+XyW56tWvnpDa}bnZDxItHp4ujJm|B~fZu6|d&SIU1>+SuAtomgfiQ#|K3s1;*H~^?k?6D)B2j$YpdPGrCb9;vgtcQPC4MtRro;ty;X;-vFX}!W)5O+rX&YXImii~XN*^9c(|(=J1nfzFYDvO#^#|2H?5`hdzTq0vRtp)`ij{4X^cmLSEQ%p6@f_CS^j1t;DV9`fnxFR;)efo00jU7Z^JtoD{|~(<<9&U7`McJqpLNCadUd-iIUn|}+Ogwk#|}Fk^Om+lOLx>hH?eN70&gIvRmXA`iLJ}=z#FM1cU{eUlk0N(YpbkS1bB}WM77nSDXL9EH9MhrjLI{mP<cv)UnJ~VgyJ{fnog&t%(QwVP~@o&d&1lbZRJza7ix&ho~~et-U%jeK00}~d%Zi#2jAcB>I?;6b}P7~F2%iQZ|c#dxYBJY)^Up$={%I<vGT0)h`Oap8&3&x<SFxU1KzaNMxqnPt_&g0{md|{h;w+ybK8K~6yrEFK1OMO0vUhzJwK=$@Fzb?-oX#v!HvnU$%0st#+P*kvs1a~xp@-nUe$F}?lq+Hc~>#AYRVYxg_wAthp}MTzm!yHVU!a&HsjN0Ib{`EJ;bfMXtASTh31t~$A%P(R?3=16<XxB7K?Vh+~8o!{YFuD;kJqwo!?IRHRn(89Z(N;C6ewzh^`lm%~-l@Ugdm8`F4edWvoQok=jRHrT2RIc^oCr(Y;W%8&ROKCsegq$g(R*Z#Y-#3_@Ekgj~0q*eZ&P01A*ol{~P^mbegvjt$z`En^$*xUB6|tk{)^1*^hNWUmC+&aAiY1jH=o{3`MU@TSAu)O}haTb}Eo8%j8YylPqBdluX;=WuA~UhAtRHE~XQt#S{)x)?btYe-@@?93nbH!nMn?>3CBFowLR1wppv)ZK$ug2$m!IEi>|PGd{-?+wnXV&ZMNsw&pq5d85??oT@v?_g4d`Zb*Up{|Lu7}}bX^FX%}4RR3x>7Q&%SolDVXtL~^SuVf^zwBRM){P>oikdJa^^Ib|4c%1Y2?y~Uf!E^epTQA)KkWa!jQ>C0j&*e9@9;=QyA-D#=~jYRDXuh!S=shg*oLB0on}&*QRC6TV0vVty9Q<+_VLADifCaj^hq8_@r5M#4!jC&{zvFj(*N`z_Ldq)U55o-^%X)i`wA67K&{eo=FnC|6;SMp!dV2=3X9GayzzUrNY^5vn@VU|RBKlncjne6#C{wfhscA@3$0YD$#-E<uCK~*-Wz#S&JQlCJs3}?HUIV5kW1XH(e%L3$h}N@cw`JE{sSo@O-u'),'Libraries/peggle2/gram_tools.☾':strd('c%0Q5+iu*(^<7^v2_SGNF~P3fHh|!5k;X1+v}pue1`5b3!Ci4zgt_E`Lp7^3En-=g3p;LX$2R2Fts@6<6WDNiafH~2+lN7)`p|EPzNF_2XNE)WMO3v)k%gco&&;{Zxz3qc*X5i1%BeRO-a5VLy43pDMav<bFm8GwqqaTemd3kY5RIRaboy>54%=Ru#QRK5{eJ4U<D~1Q#fg;f@Za&LWWGUY=yjVb9_c$|2B0_iRd~prZqJi9-#S5o=578Nf8h{-Zu1Kbz5!o%ZOSk4n{*hSEv5p<mb|X>Ps_Xxz+$#ff;Qn70JMwz5NH!WWIh7#@w>DS9DPK(!S7I;E;bgEH6NLD{M1X+gl5bfVgbOispW${e)Ve*&mnywWF$nm$-nBFf-2xV$reEsz&0dOFh@#5-X%hkOG-wCV^2-3_-!0~!XKGvXpDRI{1kzYhNB$0RMen?(+u_kTQQeZ@RRuIS`umY8f}yRk$=fA=ZL7z98JQJefG3eTh4iI@LT*#YN%C^0DXcct)8_HdtAkpg)=|S31}rC3G^E|0cquL!1ho4(i^WYYQ)hJEU_?X`SfRT1RgMFFXKNLVmZev3qLtY=M;H(t{cxaCB=!8Kc&ZPd+FHn)Uf5`rhNP@GUY4vZ=)^e9D?RNa$7>mIVxL{I8o->!m$teZi&N$?2HLhi12Zin2~`!!eC0@?I2;P%Yqf3L2^{N4}JT?`OHmrb0h&ajf6_3G!)#m;xTCeI4MEF{S1@TZG@;*h9qFZ&PU^Sbf)ZY;rO&MFh3dRnn&xG+lTba$tg|Ogz<4Y3J(&{IISO@7I*kH{`CKoskQPoIYZrkAva#<@AI$rON_0!x1NRFk*F$ew}Gw;Oz-f|iyFJbU&ytBD!_guh{$k{GLzH)=z0TMDBwx|sV$RPDVakmVbpVsNvIIE*QAAd(0fI_@}eSJT7%V8|BU}*awb5$C+OT&RAe9Cb{Rv{IwE68Fqj}{lYCCLP1a)?rJkeA4X1R>q%>EgbgV$>8?<$9xhghKeC*KNUd)0th$B`u_vboC;oJQ}d!kA-VtfKcLiAFQLv$Zivvt9K<Lv1oo|ApwoR{yQtvYH<0EGqw*tT&$@lXDohC$>rDusgKkNFk;+*TEap=34aaqvx~+%5h|p7L^4MR63yEiWWYgWg^ZLTR`AOKjQj8}SN0alBe^*OqfW1qWtkmepp)CF3@Q6}Ksd^<lpWex+%m2L#YFq7(ShTGvm!)Tc^PQOlU#5fnuMKka7=>*IpHUo944YLU#L!je_Yks#(P1#>tg0Ku!G*AX2TJBgq(Kh4DV&KHdF&hT)=kMO^DijlVgVRDNWJ=4iM^eGxJm#xN0I{Xx1|J8d5^WD&oEStPk!NNh*TT8R~cna~hmqc#R9w&kb@eRl^TjpWOrcI+bB}#g8an=ILM1V&pT_wmNh&p7N9iL_vnI;v=Y`&%n_AjhR9eK2aFm%;acQp=u<~BVRw95HG)-<t}!)+}l(bMn`vV1$x*1*6=RXZEGEX)bm;Na2(T`yW8f{p|hJD)>^`QYXo7#^_MLD7!7-x*U+M|(_bOfBssUe{%7Nykst4Q&bZMz&g!)h<I}oIgON%8*QR9>7a;X-xvU<3K+U!Mks0ErQL9WXCA5kOf=zaK|e38)o=Go`^;4OgIz_{h7Mc4w}V9DLzZSIKhgzZ=_)D+c!2Qv%MVQEP8F<R3~-$z@60PLoR<3CrJ3o_K_mog&&D0AcTuM-XP(K{3_QlVuy(4zF_uFf-34D1})?=NitQpl816z{ScxFKt6{g^69Y0aT9RlVm=+6uGgX!KXEZ>m$NVG{DBa5gZ~~flx#9E-z6h*Zaaup4qE9?<Nxfg=tmy3jz(rNV*LTk^m;vC&>sk<WFTE+jS-zq>?0EU)WpRWoi?5_@A3!Kls{X*5V@1?P^oY8J42-=Gc$xgL6x6U2Mp3B=&aH3f-hm8O6!h|7j#acqKl671;6N^pFhC;vKUQzg`F}6;ol(~9MTonfO5-xfj=_t7rS=WD{t`|`8HZ$%7Lq(gpGXYv5g87?ZZP_xPg_>TNn!Y_2#<1*Sy6)<C~gLU-skg)1`Ir6+8=_MkB1tQ0)1gPUz3+jk8>Sldbi{&F2o#d(@E2rq;QrTnLLFKqI6<ezW)9v*|Nu7p7<T-g~}3PSe2oVI>^AwFVqY|8tSGlAxEu3-I3i?WaJ^hA*V{>bvL8ML^7+8Ar}?h`z@KksHD*zu-HRKLY)LKnn5^LQrQ(BfB-%spBgD3*RZ+H|L#Ora{yt*fa6F@h^QhO+2;=8^kP@FecLkGrOf$V`<Y4wt_}TFmbn>Hp)ZUVR?#nZZ($VO|o_FY^_#n*Iujp`pL7FM&jbhIcYR7T$k~(TlRsVDD7NgV-9LNC9l7GjjENu^09zW_>4FN|64iwOXtQi_$w2ZcB3*4UCr}?U^<|-rZr(T)T^oiLlqmKVjeS#S+<hCieijvfWwzOJ#$FJ8kpW>K+CW%1+<E)X5yV6A450;W=h@Eo8Q6U-FtWuW{N<j^an5PJ=~nOU$titR+xwbg&4<$X1P;_lw9HPJUUwnEqy+y!w97_LP)yHK$XbCCyx-J`=|V`;0SUGC@o^PUC5O3M=!6RIN_fBIsWkFjO$YUQy19tSaPP7;~*3-N-cSlD&EB}Vk~(v^i;t>5KB2<1{1&Du;l6Jqa5~F!5%BvHou#}@TV*qwyj{>ipMp@_nPE8^e`Ew422J1lxJo$%E!!>GjQ@O=E>S($<mwj1T=SU7|368jI2gkj#;s^_A}p?2FPB-m^!Y45%nnGg<~)nEWC>uBaa7Q_Q)|6j;YU5A-<c&F?xwC9389~My$R(x=vw{G~><4<`$ti3IQw1FMeYPF8w0UT+1SYhoU#f)N~{_oT+zoOjQz6WEC4K^2_x<q_97Dw(0|M%p(nvq>$6dD*y7pm9(+Pfx!4PzfUa|cm1z-?|uEnP5Arw4oX_DdF{5ZpT4V~zBf4fn!mTPabBHWuu%sWTUC3@!u@dhl2!@LY;oFZsk%@;T=@Wh`C*>R!p#2yJu*;@'),'Libraries/Ń.☾':strd('c%01|ZEqCE`8&U2`T^}MJ)}F^6!oP0U>T}bZ2&n$s${IyvYs>7uJ5k9YjSQB2~0?;q%8pqN=s5qU1-`yv`W+}s-XEW${+DB>GRCX?#%4$-I+L54Z_RL%=7*}8%6vb{{D|%yL55&aum^^V3Q*1kFu?}2wG$_9bJvnoQC0vem2@7$tX=(QVd4JoD8<cqpTns>=)aN#5v(l_=o&+{vY^#m)|^bB1z*M-rnZ-x+e(y&?w5&QISUx>GlX<0{B6K|F8hyi#;2xPoiir927tc5cYuI<1bpIXpvJ%i?ANw<$vI}LkUm-Md~lT{=;%}*dqEBU@-pY+mOuKz|0L4$XGj-tdl{XB!s0oBWvp|^4i676zICkAGS~iAMu;L3!@<mX^0yc8GsN3+42Yr0VK^?5f?=!$^Y?r`aO*Yp3fN1?QpHV4*z%eFBy9l?fo6!{sm)C$KJoN9;z4T&i{m-4a2pw>sn#SXjsI9q1IU%Z(ZGpNu`)cmrTfDNH!~UY6V4y{PUY2k$=%i3!gsbzYC=lnofa6z!nttjEyrt<}L}ozC};whkLsx^YHNTr||grF9A78s0S$60U2c^IQ-RZv}r%B)dtYkm;AZ84u3;~E)edZU|WqsX_1|7Wtk0JR(3Tpo_D0~5d0jvGxW9ydRtttXpDy&Q<T;qq+YLFnaEcaz?2P}bioh!`~2Tcj8-6kt44j|+7t*zblB9=H?|FokdU!rJ8LqowZXaxYlEdzVZr)5fIwqrv=aW`B8mFVWIU*#f?E_A7KWpO;8L}6w2)RD$<b@ZV$zemB0W|FO^%Nq_KNga0h=8YJ<6gqK55R$SQv6L8t?estZoJ}4Rm!(Ea`8GS=vtUybPO|2phbl)MB+8^#NEv<iF-G%2WREhcJK>aJHtTrQJ9gXM*2s7U$oTPdNQmV^lH1xPt`NGsOyWKPTHXG_zH;3CkCivPukQI2y-U<@)p1C3e}d3mb0DX4B4Ar%n<6S$MqmZQ$@@HTdplV^d1+@~175wa7SQy&piq2<8sX8(r>Q&bFP%muXGgUae?Qwv>5O6d(mnnaC8H&_p2KxFG}1_-z$ediYOQgqxY>av6jVxmBE_rb!qS0AV(MNtMo%9&>S|P~nwUY2mW1(H|PAU5wK;y&Y>qXDt*3DV}&Jh2++ra_O0~)UnFOPKa+Bh$)3BP=FA}qjAdmg=OD*4f+o@+^8)*gQa*ph9!AY5<O161hYw<Sa=<~yBB8h@aDBa%7~<`t}VKP@Wv@M)USWogsvq78Yv9QL$ZQ;)C?ukx!3Eb;*_q~ZxO-@LXc9Z6M-8BEs2E<x3^dp7Yv}(cbb-n7L_#Y!5=LA2g7aV-B4<F#fW1A;~7{CzgZ#ciw&>h75KJ$!h(k33xs)x|9zS#))4q*RVS@UK|8jBX26}6KTJt0Ms|)<+y-CXD5KXL85+r<u(Crx*BQc_9w61960knC6NQM`bL0vcynX4S5c$GFuMitJEtK!@PoVdEPo9zes*_3jIr@A*8~u_EvFz{XhVwg8E3=Wv7;~i-Va1K9Pp2=VgPT;X8<1kuFa`?}YV%nz%vnMzbqi<nTIO%c^&-?f;rIC$A_IrDtf=cP0mUnD=?snOyXZBlUrD8Kg0qYW$A<!hSJX|wjQyrLP)e(G(;~tdFzcA<!Auj5We69(cu7~QDhS9LNbaz}3yom%t4fw6H2T*5V7O6JCOWC~OVdYJJx%PY-#zIn3UY0|UX{)52VQ?)omykn#9ddiDOhB^EG7+hfm4fax-k+(gI(^~ur=J(vPMD3wS)lB02qn@HHI97$H#&hRxKV%;Z<5s<D#Z@Q4H?7J}fI7Q<XDlEVa5~$YQo}1JJT8p^5NAi&LOjaVia85UZQq&<UF>Mim)?!M{RNw(>1a4oV$lTXP4|*)j6i;-e~6#Bdh+();{QC91VN9VCp(S%&=gbSGT*HabU%a+BkWa&>p{ma)3Dn|Kc3z)!P`BR+G@pE+E~!YLd<Y?Yqrbf}Fc5k=!sZcHMrX#(CW+&~ovffZ0*Ihgtl!ov8FABfOrw~JGU_V{D;Ob3pgUPpLVTX$e~gKi(?;qQ7gW0LHuE(U?ww>!#P$#;nftq_AEL&9FaUI?*UJc>DJ?qnoV3});)%W}41@negxs;+^a$~w~ITAcZ8V@@NmQm?J_BiIM@*Y!-`w+Me=n3xuTp<VDLR6nQpD*7g_z=FVtuKypxI^CIDT1SemH6do-h7kL4HXLm*x7zRN9J9-x^ZN}`GqGk$)Cy*I_+yc+;9*~RoT{tbAR?+R*scm#H9x}_ZU$5^@iz{E8UXFPfc8Cr_7$LgRA9|91*(=<H(TC8mKRa#$g1AZHue2Y{Wh8ngo5Al-#6D>+ALBhy22q*B?`)P`4l!^tjw~O)MYpOAF+ER=g6i=Av*>sWUdtQLETB}*O9(><EX|vc6SMvmoWW7TCl8nqK(%ln65uiJ^Wq%z*_^#GG&)P<<Icf7m9k%@$&vB&ZA;dAZk^x7+!G6n)=k5i82>|01mi|2p{pkQoMD)vc1r5f4|>u<HMQ$;k)<bn|8Y|-&}d44bSb)Qb%p=x1EKBazPaGxA~W%WO*U4NhrOr>>U*^uX;ztJDyQ7zRsN2i_<2^=0wTR4_+zx-N7K5%1Yn5*8=$jVKvMYCMdqti5PWzN#zb6<JQQqtvIlQpX5$z2b@e#jKud0K*%0{$v;QPqCt2I;yPAu!P~MX4^HOzM|^|<N0wJBd)`rXmeJ1aSa)l1wpSh937tYvku1Knxyk>=UzT6mWTCtOJV4Mui(ncDt*VnSB}$#lrN8q~)`)_B%0Hs&-Vs*6LcNL2q3FCG@kin&<rDr-zTYD1>4`Lfav$F3-B!G+JR{ez+gd6+907!C8g#-uyzvaH!7^GfA>mMHUs|@qL|(+n&#R29;AOD?%FwDSjSBbbXhNyH-d$O~Ox5UMN?{~!YJy9)2AlR7YSqM<T4)5{KXWFK@>6s*RcPAg=eV+!KIBIkim}6mWdOL@3m}FBQ@|Z<fEz$eYM<=~_O;;j>%S^GO8W~A_ih|M_{ZVi$A^2L9q#Q0GR&;Ju}W#D1?b)i`kO(Q1f5PCylqE3A;p*cmcH8C<$vUN{a1Ut{7?KnZwM5po_oU}EFHMb5{5#3>b|qIH2bcwG)`?Z;zi4KQfDaP#whRR(x4hmen(k1fEx^1jt?kj%hi;N-xFAF^50NMEYj`ni6xY<81ObuK1v0vaA40md=^5!(<7a!b6p8T02DSFz#pukq*_I&hNx46ds>5?$a+|+S{_8r9y=pIM0+kqz<7k!%J5YWV>)|b&9a9S{Fy(ty8Y^cu%9cavXzd+m#)j_&PC^cieJ0F9!0eLz7;GtKu-^p!$X?I^ja_|zVHQA-s*fzBbI{V8dK+J@Usy<>u-I~)-X?Y)rc8ld6%p$w8#<;iSjpN;lb%>w23a<{3U4^YWQq(GccYP0&`_?ChAU$0QN;BU<Sfahy4En`zPcv'),'Libraries/peggle2/main.☾':strd('c%0=uYi}IKk>B+zCJKa^S*`+-vg`|Sdpd`bo#3JeC^|Y|xgLy`Lvp3rna%7_T%9c;eu!uI71@?#Uo0y!3`2@7$nhC*WJA6H9-RNheF%R^>d`&ZJ=3#XO0=BdHZga0y1Kf$s=BJWySnA9bp7sHV9m8GC-nQLm;E`5zpZRD`*@E2y6zs&%U;f2{l(D}#}^ho&$0jaCA(>@hVf}X96E;bG#I7cN}TllR0m9x^K*MF`1JaNI7zJ}SPe#&KZJ)p!KfPyQtJqP_2Q@mD4?9-TD;*A*<R|O4pri<?8EGh?DeLVy_mg~y$R&MmVK1H=)li+vfn!V)@{lz_L|nY0_NrHN_I1Qi=nPLu5-?{8VxJ^w5Tv@TIc5w`K|2tj=gW#+&5fG`9Is*XE}fnK$wX3r~}Y0efBu;?s9fpC3OUdE@f{!P$6g?J$_iUOV!`YUT7VQqre3!7F&zSdZ1u=!$UMwyl2mHu!0qSn|<yKTiFXx^COq}#!R<F6=vm%{Au-ugn>cvBRh36^^>$0ty*cXA0)P$1E`I|!|U072SMBdA_>y<B-*25+c&h*I6iCb8#052O|7oAUlJtH7<%}xq5^BGOFdpq{Jz(XqjN!$qTsG(Z)f*Kzn#eM2VN5N{lSoEmEt70kF)oX(eG!UICc>By?AMTc6$1!_~`SaKOFW}Bd;4q{ChQt*9TrNih@LWVS`fGTd&;Sdga#E=4Jf*$}QWKy;xk-lu{5lXF01u>ZfUv(+o&bMAdLAMeXU1D0NYA=9*TkW!Znda@n?ma2OQ$4bTCRoJ@f4Vi{YNB&z|s_LuDIqG%ZQx`8v(WU&F<;-b4<L%=!FR0$i`&e<6ZyZ%5M=P+o}mi>QU+jCaA%kq1Ky$uGT--Vt#vsMGzyZk;_qtw+(#9J|Tw4$`hb&wFE1a&V7me;$1cc!d&tiE6cPn`UDQP#8^2S(@bNfWW~-;OxbE-(^H;?mn0dJEt;O9itX(vkVnYv%a@=DFm&3!n&d_{cAv85fb}<bgEi3u47M{VLmZo&xI}xGJ3FVyubl&$eEjM?Bjx8%F>%4V|UGH~G218iaLtKieFS_cr3y+qfy;OjXN7`z~<;A0{B-+7~+{fu0*<8W-K4oD0{!c@Pq+92rLxk;P@#-?80^gmY;Ep>HdSG8=To%LmtKf7vvy>di<mvZOih#{GT}rEH`(`0JGI8i_}js$zGXC{F9z@S|l5LWEZp14X=<;i5VNq+sdVF56Bv!i&IpV^vcX(M#KL$;;fHYnkOiUCJ5Rjl&QeVBq=jHVmzG6^k{zlYnEbo_vM<D1Iqzkqw)XWn|A>1yTe=_p-P0fCzs64&ne8JbCUdM9m^VEBwKTnMl%=@0<}@P?a|$Y*Z?{flNgYgd!l!@e>ZKp6n%yM#4CS{k7tRBts9S_pJQv03lkW{trtWI-qc9R_9h><{twy|5#^Fot$!|82AbF8e$#in8|55Q^!c<j)Bi;TJU3*oXHpm7VW@+)w?A}6FNqF?-xSHSo)gl2wMVx^Uo|e5N80o=Ppp7e<k~ZzQ4&{LVx|iyIVKE{0?P7w1+cB%EQ?z>Gc%COvZ{);7%i)!Qh9?Z6lm5jS$eaScFh|0d<qPg$6R-Cgx9CQU#L$)i~}CdLc$6Q&Aoj$q%Z}c8x`qDBa>X-AUHNfWqWDD>i|3OZq?=SZ*9iD`^6;aUNn1l3=AbVp}|1Ux8;^8>~d2I$|lf<jImVH6j^Goc1tH>`G;de)B3EDLPoSh)DO(U{s`{Ql|(w#k*TUt3b3%^ugF@w9k`HoJXA)q1aXTA-~V7rWCb~3;|LR!nD|R%r;9pUL2?18LGb0i<Y;A7xR|j*P-<5g>Z{G5L-?vQ2PuFqoF^dkt*tA56?DpJA!?sin{6GvI#UuHM?W9siZ+_w^WLm-ibM?#0g-lSs}q<7qh=Jx}zTn53lMUgEjLRfYN*c0p+=wtpebTXJY-&-$PgPSO6yiqw;Lat+te)2J3AxR@<{-E~FtBJVG7DNCQH{t?Tc?iz%xLrJA3yVVU%a_2H9lwKQE)W}I%-PmmTW!NOVPd2z95h5czS4f>ABhtAab(*t1r53uzY){<J})fSR2u2a08ebdYroQAk;;vrazCu7UO>GjnXyLhoMk^9*qe)%B#GJDmL+##H<rsmIGfS=RC4b$?K(Vc-q`qQKi&7t+8KO%VBVPXpcpfk8CGlQ}%`XrZ&I94g%yFxk}Yv7)E9qNyUz#>-?0ss{m#HgeDXY%mkN?osR?Zi#v`WE5>YEhT<1umvY@(I8UiX~R=u-%R%?L!l34HnjY<Ai)>ClhkglM<D`5;pr@cGsbGiT}=*l3vX2X79|&B}V=U7|}ksg1=}5EV~pX6bo|vKTH0fmgQLU1o=WGfK%w|z(U>2{s#c=XLrDUU3n2~%F1fXo?e+2rV48!bVu<2Pu4$Mx<=<~Jnv;6<yE*bf}gUKb)#RE+C&kcT|2mf?JdV?((4QEH?1cQs`iLi4?oX6-kVI9TT+k@^HsA-^u~CBnKT_J6WXK}ewTekOHqP!wX0;W;L|Y#WQvXfjf%xWZBu?aXvv97(9mv}F!`wo6ep&OY?)AuT_THC9de13gJzt$_0`BC=P~F*-%q=1wp$otBJ1J#F53d<Z4U>21WmX!AL{?Vk_E2dRQ<C;92-e7qHa-q#e<KRj;9OaoXRv&SoeG=O={oq!>$HpHHLpuQ=(2Yw*=IhoY3NrPwJ?8BYSVBR0(wzcts$^sH$Y*r{WTWQ5sN`-xj7uh+MEq7=%yUj%&m>x#~pUhi#Fc(@Ef;9i!KpEcpAAj^=k}-HsH|8`<?;R2+?vNM%rt1RarKSwq1)>*895N%Salrr9j;A9QSQFCy##`8?H|8O-U<y7GOwGIL+b7VLJ}f<^4NC$L}BrSR#2tq#Q>|9Ccsf9;ONiGDacgWP}gR)&SL3zk3~KD3DU$Qk)P*vZ|uGLO_?>PDtv<3heYWmB)<ZFNSWSr>!#=n@kZn>5k#ZkJ8jge($v=%IL{lT|T#7?gM0`)4MycDo+;6$Vs~_Wr(twC$`Gk@CRys=A6YskPcJcByK-7{FcE`j_%LUR~FAV(PkD=Xw2p_XoClXziT#A0%MQSJgo+{lS3MQXN~k!sXVOE!_McJG<LnQs3XqbF+S3W~QSITcbIBfEb4nm&fcxGxT;|{fC&uY%3~mz8F?TXLnU{`I^}n**u_JrZu@#Wl|%L=|?3GRdElQ_Iw}E05YMwyW*tM`t6;EBDQcCyKnYN*5K}qhobZmQTf5U1}a64laS@EjpOgJ8`sBlLwGs+=e^YOBa3zjcXds3_j@T5VJIf#-MhYjHlVGmp_AnMa+}%5TE4Ej$?}JMw~pR6MMgZ0eB99ZvM50C53T1#J-O>arE*6;>JLPedLz3u|Kwtkl$^*!1StDU_MbqV+syav^XzEBt3=@&rIEabDeTQWY35T`OOC>n8Le+k{(gJTqV3=*OYIzY=xvu%CV;RBCV4yy*fi%`=Uro{s{|zy5oD1_hWUij7?sqYKZpeSJckM1zLnj`g@+#$1;?WaZ!FW6bHcmkoJ(O&nR5`PscjD>!hu0&%*k(5)K2tGM^*&F#?rr0n$$8EMgQA87VhDzgj^g|Y$TO!{c)~O+Z4H4jsgXGb)tQ>v~{0I?o=Z#K`wVFq3sXJcTNz|BLKprWDbl$#-te$$n=B1Ub$S}3DQu=)bk3vB#~}4+X+<b<Lru~8Y5(gYJJp_O{GK~Yl8ZRn@8)Y9|BX(P3o->kYg`;NgU&`8!bm42O?S@9B+3(sQlnIt$dj2CZ@unu}POAK}5D#Nl?jQbK6SaG<Yxz;vQH$&5la*Np=BG=G@4xG;yF^&pvNahwf$fUBzm?Y{(3}M%kkxGf?c6^9HT!>egr*^Cq;&kg+G&<hWq>fxSwKh?mA*ngoGJDiFr}O%6pk+y&|5StdHg)Dr$R@q18r#qWi|GN1erUMdN?s*`GvykDE!rZE9l!mIu;Nq*8K2=jr2$?_lM+L##jb$j=7<)JJS0=9m0f9sW(;jdk#zgSCqz^FgZ@c7!;!`VrDs4`kRYgGh>(3PjC+)85>riGIHk?2<arYs*HX)E(1OxPm_Hg9$nvFas2pTt}%DQ$L;8=P1y@>5-=D6(x>B1s2XTO-d#T<x!(qM^gj=c!?JbFdPADNjz&rf2jz__IFvP`EVDri1dh<(Mhf&Ln1{1o-w`12>==Qy0;>UKp>$mkK4WONY>_X|Dfk&W8}E(wu46q&K%~aj6~5@pVi{HpdG?MU^8e;bF!!rs_G;Xd{-9U^i*>C=bb)Gy_JCJ7BH|^V&Mpu4>7Plr)w@67=J90cR^?_N0foMrGNvaqq6h17U0PoX1Qgp)eXK^@nT0u*GwF@sf>z_v`gwh=*HCrC}VO_16M_S-$T@-Ee(5@CNa)r@{m7?pZGkqSbUwygGd3XU{xcN;P~@j#^%E`5YNWaAH>S5=8oUq~#yPd{mN@_7>?ar_mp>FUVA4B2z*wJu^K$y)r#>`Z3HU)q4%I37aKR6cxR@pq-?{6T;q5Ngti`%+GTo?HdNkg}N0X!(o(EJ&a-ks5`BqoQzSy7gg|y4ge7aZJD`@E~tFs<8dYEJE#SK?6b=7k0~$*bodz)e0_jfI;HUhc(NzdwZ8HU1P5nV9E0Hlt`(=Ch`3t~%GHBJ;*>8dt{kgX{a{!Ea_og1pfI16aih82tJx)|I^WOb)N4)88PZm3<v-Bm-xJf=7qU-9YA|||NzPfh%3G%t%G!*_p0j!vXo9ZCv{x}jl9nW@F*Z;Bro<8i49uQuJY=+kIY+T1s>s8kuw@yo5}O>^aGvfBf>8|@8zBmw)Tuo!KJ4ycwemr~dXpk7oC%9IYc^YR?KocvxoL5@bYw&~6{c~d(Xp+e)9hHgvC<3EAR#?z*0kyF%vOwFR($y0nZ)<^+T${<22-Z1cFBm5-r34P7!E?ea<2h#VBQq+kFmjqq0_A&Gx(8U^Xgoo>sH{pag_EVMLI;^Ii!!t?^b6Oy<smJrhWu7sB?0?bQ==#ZK8AK#b%{z-C`7DC{x8~fTfW3=9h-`ZpqdV@pbDrh>c{*m!Z(HO6~eh=dt*@CVXaG+evWpVKl!B1H>>GO6skRhLc#P4F>3rmyV3XVf^h9-&OMeLex%MBA1_Wu19{NI11ygA6nr!-J0Ax$xl8*5gZTo__WBksyUL}6rI{`0ZaW%5Vny-kR_#oZ!lvya|3PhU*1|%F#+}AS&k`Z0IQDajG&)H@iH3CZ4M}B)uYHe+hY&v!@Y{s>4>tB_&@~w2B4c7(EfZkepfv2E>3?;0D;DVkf$>LSo4@-*iGt0r3Dg$!C=uUHcGQ;Pjji};o+5^B=N>@mjhm{PcR{&ZUxbLKS=yEs55ap4-<^;zs}88_LnqG-FBLl<5Um9=1Mq5U3<!NH`k(v*tprPZFfcd^-5*Z5#3h?sl@=r^jDdQ8Bam(WO7Rz3xH{7Ya+d9u%4EyDKo@o>2RRYc#JUyM&mKY80hx?APD22o*j^1lc8<hpnp+^i#|&o<vT0Y4GMXyTcb^&4QEt}edQH#a*qpM;KH)H)(MC^+JYscD)hj3E!rShT@8a-4+53YS!mKA4WhJ3$Cq1n-|t1Xwp`ex)l9LB*l5sF;qA(CWep8G+^*5vCX>3_0=Lws1vE6gaS2rx+KI>`#y94+*7@eY$(q~Aa;RY_Do3yR_&1n0q>Nc24|@|rS0AG%5ZoSvSUL2r@8mIlxsNw3xvycL=PU4bieJ}l9py17>qV>irW&&AlD6^4ihp&^xDwu#`bB>WrQ)=hw~8bLsn>#LYKGQ{5Nn<~!@(qPkV;lyi!G%^)L>D6&z^4R4~KFf2u1e1VHl@F&l3?U-2y>5Kz#kff~~GXd0sE-rJm>ThB}0BrBoA6_E;6W(f?J>^jO7Ko?1A5)O&j2$)nDyYnpj+o`PaEi5xBZs(>tLD;&AM#@!29S$zrM9i3jm6?x+jyiu~DRyjrTQ5#}~?MX05a<*5^s=aU6-Z!)s`0A2<cp*X3_ru<Q1j`*d#Gbn*k(MPHXnP*r=0bZq!uKdUXe49F!YV`sa)E;)VXJh_K}!incBp92sM-@U@^uub=;A~{wAQr1tmD<EakLWlx~aC~qbuiHo(fY^&NcNo^_tS}LPsTfF<7p`2rNy+>PUyDv%z`6MZL;eQKqyd_Q5eqarC~?a;p4+i08#K-b_l({Yc(jAfcLutRGDi9HIZU^n;CBE6Ee6Qbdp^Q)n(!8bn<Z1X8(dk?vqvSdSv?#|fgxnzc51>6(?U1rP!t7xF&Nl`<^L6JkmKAn8SXA%`YP!38ZUFspN^W2)`Ojwv^Y6)jZ<s=P>dVr{`#n$<<SU)L!vtC%AZV|>(<>^rZGIVLE|O+h_Xd<F2N!@Bm$-~6uMQB%311CyT4=N>^^z#(qz)iWO3c6(_(I6eFLk2~#Wm!b~d)@Zl4KD)H_+2+=@FSf3Iv$gr>4!+#$w4dF(b@~0y^YG^<ZeuUJ+-t*2TX|{kr7VK4;PuvTzE%q07h!(3gu2+eb=*U^%X|06Pv+>xw5{v!PBmKJ-r-wqFaDUx1l&vZUTY~`iV*wM^O)d=hzmrFg>YQ__72hBZcH7b2d52HJI}Y5;Dhy-B6li(58W@7C@UuV&1c9<@TbQPAAQnWc;=T!PHL-7&)E=KgEB#sI<)7kwzz=Ou@AxDw(Xs=$+^+hm_;F9sR_m6=16S4&G&A_qJmPtgIR3yl1XahqAhm*uVP*T&V;CD(Y`?DBjR%7CCbEhHeDiEDK79Z5&Wal&KXlXvXk4jd#lneaYOvxz^2uP3PR2ZLIf`hN*LHC&Uh+hK{69uB1vKEOhpQs+^TI!s`QpbUPni(tXwSCQD1b!NW9>b8h*w-W`5#}wFEcBop#hm1)<ius8G-RR=vn$4K<RsGt_hSsLwEJ?xZ?qL{-OJRk;qE8y4U$U5sa|#fY>alu%LA*j6>`l+-2Q@JxAF&2~h|Y`NrsEICjvc}$k*dP(SWS<V)Z2bd4c$`Y=FR3y}=Kv#4~86NmBr4=fO9`989tg?4QsIJf_Q&Ur>hEIuxm8PEP7>919sf}`H|A{(#s{Hz=oz4ZczCSyDeDUPs!jmUxDk(xK%_JjKKJh7Cb)Uyx>doyrO1k<^G2xu^&;O{vlZOv`NB$lEVS$qnisk>50QN{AwTr2Z$k9rJVd}{y<$8vs%3g}B$_Lj*@VjLde(lsD%K>td^V&PNVXDt?Sl=-f<LA5EFuUsFrbny5w*-#Vwl<PwOMTZ_f@oB2v<{~;@O#O)MhWP2vc5J4;Wq$+mxjhv<j%$+3*rK6$!<ZbWAU8x!}S1LLwZ3!Ef_xTluoJTT5iKK;sI!jd3+I~ioFosbf)$~oMM8-77Ez*{-vdj&Qu+&_!h9%5=0zzu&1i9OAv<Cfy-r(`QyhHj~rX9RiCzy>`cel@wgu_`|*jmSO*rvG#~-kR{o<FyuG~cZ>%l%{Ec2`)H*-DVN=OugkWyvwGXi+f6yDpBeVg;AX;Y>FLAt!Pz?iU#cmu`6VHoFL;+rMyJ;axeO1n|{(J(=#oqvGSrfG'),'Libraries/peggle2/rgx_golfatron.☾':strd('c$~dg-)q}e6n^(#aSH?8n<yiSVK9T&CU#8By4iI+7}%b1Z8`R4OF>dWX5E8BJ6N~TX4y*F*xD@YVbJwq&@oD35BDG2IY(DNtx|`w2^2~9$N9edo$sC-^YL&noS3XsW_&i7-y97}EO;{crTnc#e}yQF9ed8kx2&OO+cTF<=f}3=F`8T8@{YXMJUrlB>ssCJCvUxd`|8Ff7oFbcUuZhhy4~KECWOv7A5IK}q6zQs^KH@D?qSDpvXf~ydN>0cs{7ZuA+V*u58F7*FpT26#dk!3S8BwZSEyZ{$W!@{3ogHw7xIL|_nExU<r2P@guTfCi2|R<ALLVB`KZOi<(|lA@=On&-<4P=YPchRmVe1V5PVa03t$Hq+t^T%Kq6jOWa|G18HjREz5oFP#CaXFhGN!OkJ%e?suQP65eyv!93II((}*SZL8Gd;0@yi>SeE58!9#pC+Sl2l6qE4*gm)@!oz>xPw0nUAl~b|?tY@1IYHnnkcXDm{-_frDeYhL7kbW(nezsZB&o<}M&u1Mi3ep)&p%sSw>g`UPcbX!i*f<b&y%y&D4BB1On|kJ)hh%obvG8sr-nWwki$Jj06IdQ17w4(@R6u7&Nkw3R_Nwk49^l+cg0u!Tsh6-GPjz;nQ%{fYX+kAo?|N<$_F8MzuzWzi3MeALW<Fr^O#rX10^W`QZ{#m<cP+re$Q(20$nQG?%LOBs3Jk7@hM%_6_wtE6<#9~FfwcZ8e@&c8%r7z98F3$p;01&HG?fGmsHtG|0Mx-z9mq3&jcrF6l1;6^NK3$a5gAFlqKSww&7Tm;QvL&_EUI@zPl#yLk?9RQ&*2Unc7x+%(;7h-^4xUHCcqhdI00qovD0H^s=>d=yOrHGFX}V|t7MUxGuKoUQCmWAOz)OsMIdk>pCVGq>^?f3Z7{y*Yyr-dGV}2TRna_5!))N0K&svrg~B!YKz<`%^5EzfQM!)o*?8bNwuK2el^37`5x5o{^Z1HGq4Oo23@Mqye3GUZ{ik?yp386LLzI=A<>fj{-j~nUu~rDEG>H!|b)XS6MT-Rjb;vdu$+)kFOW{-;i0JQJC3}$$;LfH)lN&nw(6-Fr2-BH?`K9W4frdI@18aoYdnBLp0}&(>oLPvadmz8Myl_b-Gt+_qm|!E&)6La$ei<<%67%HFRGv@l%a}#vMOr&}>{EMcfxW_ZKV!Q_TW#9;I-3?R5H?uatDszwkTJOl=gCbNHoB{XD0jjCD6YUQX#@#_;=UPIFBkXaUQ1-1H%}z>uKYVcsXk>0-1zuarhk%qY(vNSItO<INL3DTL{dPCkCu#)(0^fOp-m_9A}eK3^+N5S>c_I<tVHFDksb%;4+N!A>^)|r<HoV^M1x`oce9lV7pdo@&k3ajPD72Hb)BRV=D@@oitBm66-iUd9d$ra)l;Pa>w>BXF8tInN2*(ApP7qtycPJCS~Diwr^6|)YG<Ehn#j~)=-L42tQ74^ZKaH_v@~j>(C?!JyVYuc|Knz()jsU^`O(b22|+nZrlpEJ{4z^@3-K?+IuM8'),'Libraries/Compiler/op_table.☾':strd('c$~FZTTdHD6n^)wm_9_an_87^XaY!n;1(6dfMq+WDzH|*tPzSY$X+TU^&wC~LeexO0fH1TaS~9H64W$+qFg1W&*V3-kA2Ed=$YBs@vOZDbBQI`*_m_s&Y5$WSxqC;<W^sQcrX&vGzA;_grQ{$#azO`UNn*|Boo<^qN*OPhHymB>&1kjYlSiTEEG#ldWBTTBK&<~&vn!hL_=psbVJZ<Mk1NjmBLs_^`ap%MIMot3jSeuJmB-S?{B@sYCH~N66v&-)B%xBMJU-sE}2fCF)zw@AP|=@jAD%{FT$hwl3p~hs`L-`D1dvOl*zmokx8;lUI$@ffxIOj)H+5k9l&go2Oab|Pj)OJlYs9Lh^UYyG8t4#+0m4)3>5OZ7t#M<gHHv4j1ykQRQQ)y!4Vw70(n6`3jV59s)E16k^{`SYu%kO;f4LJO>jgrQuep*)X0f-cH45A6=FVrQzN9aMaUSw<n#G5K3{99S!t9VGrup9f0P>U4p{@(E{ZQs>1XFH9p`mlyBH<JC~3|vh!<UqQeu?GO*tI&)LI!hnUw*DyjRO7koIcXDQiWJg=2_YsWsK#2%MD;YjVoM&V45DsE!q~L&`M1C&?Z9SRmIyJc6Gkj>elk2CT@I?GNxtMw*wyl8(*Q^5INQE#~S9l6>+>UIWo?Du6}isH&k(a4=U@!NA<O&c{wQoqo#_`V_R~iakEm3Q9gR=Po+HMN7Qq+N>DMfL&>4?jH%ptH<szTDa&InfA$nqG_VjQu~5TD?=FJI8Xeiv=rjuJcfrAhqOKP$7p=vfpD}dTikp7Woqx^-uu0Ita?1DY@$>`gJFfS?<i!B{6Rj@pu0yFp|_}NhleUuG_9zQ6*W!n3=q5bNVx;yGo>>njLslM>JqR5Pz;8IhV(Y6P_b{xW<6CuR@u+PbfxtS(zMb1r~%E-ra8+7w_#w77C12av*ne>q2DRg12#LfrFzCXK7pg88=xGRxHDxuKs;*bISJB)1VNdgj=9_$RwmS{g3%1!g+=m4ned|im_$#1Mco)L=Fx<c%+)za&z5x7{5&<>Zng`kV9A8Th*G@~UUc<z?4XtFRyg_-7j5l3o1i9C--Lnm{bH};x7T0{eO;n-ExD{7E>TEVEw8YN-&Lh5gKiD{E7d4!krV}-O0Ack-jLF&sza^uX1rXIy-dAmCkoeV<%&cn2u7R)BUJ(q-KJEMy6{i3&HW7R1+j!&K%;qNEkQIRvLWr8a6TiHogX=#^DRF+yn6Vd0iTB7sl8XIsZHo}^8j<u(3QCCgb;R`Hc$Rm+_1{{{Ee`-0M?dztcRVKn#CIVMp$dLV(7WJvE~zo%FKOeVy6-h^|)u|z8&sU0?iAD1=-5$T;dA7!tu*k?S063AoM~Nuv;(BczQ&v?atNuK)K4SK1`8o<VKBn)jjqW9c9}6>cH<=L%uj~<U8cH-N^ZpbwTs<+gY4;a>eO!u8i5>=C}YjE)cKBNcrxN=SR90T4qt<b!Qm>qA>O;ClWADfUMLk`QtKBze;BWQ0jWai*md$gJNfER5FD^nhE5gW|<?^@Xabvsq+Iuh{aT4>?&>k(ChHtYfP2oM9;ITg6dS~*xQP<w}v!^)1DCo)cwJn7lnc~+9_hEZW}Z;VNn4d+!YmP5*vvZMUEvYTqlWVA8m=pE_E(tLk@JojebMIRdSvk5~Gy#F4;IZB|}~o8sHca9U{G5(lO@*$n(sZMY*OED3oFcbslz7WYGc|f>gFTqT51*Z&s*bs40<yq(>S_kI2#^4W;vPc9$%A>yACn?6M*X2vNRZP$IB8kxwHYUpU-_B@j#$KTkX5(4S3KN6vZ+hKoKN^9=Q1{Sl}B=xOK=x$Bps8$z+kROeNQotPUGqXw~}dhP6mDc1mD6`*lMSUsAnbnP^}n?S*>`8slN33QF7lb4X@%ZKIuBa{z*HmIKSJ+M()tg|cBYvq-YbmSugz3%r#wZX9Co=)#j_sNHj`Y7Wous=GBvq8-K>9P(tc@zvH{B`BwP57I|EY$Jt7Ph0`U1;^{%05L5_Viuo>y1QtQ?$O6t*)7~@AwCi^`~_3W5%3)zrVfw-}2+#Epzo5|D-hk++2V1b*_95^UvO(h)ZJSm-;c(7YoWU?L{yNdbN-?5ES~M<+CG=So_7f=C7_r9DIHUU&O)ZxA-o1Mzm<Sw>yZ<tvBY@mbv`ETz+USR`%!C`RANuTbniVx9RQX#xt_{@3wtaXlpa4Z+w~la!pL6#VBLmEc2JtIr}1%I-eFJU92X>C?!UM?p&2FBY1sct{tQAk$uQ>cJ&L9&Tg%HaNsg*@2`pMxL(36-?~B<wTnOZM1y#ET=)4BQ2L^=9zJExyfinb%$axQjWzB8f3g)@T-~7oo6~ZM&)>HD*?haSTcJWOg@e@(NPnqxrpumrOlMT}fB7@F5d'),'Libraries/Compiler/generate_operators.☾':strd('c$}SB>2B0k6#k#5Fp)<0UNFd>$&OM9NN5pIA_x*vm|C8(XEfC;(RhHQh>E0a3PlPbiBduW5y}EoX@NGPl;y|$*GlvmI#19?=((#si-RDL`1r18`ObIGH9j@s96feo*cccz=&#suyh7D+OaoQM{i<85R0BjvhvU#|bmrK}kyEEf9S5UvKc6r9Nn{%NVkP4i0}O*YvPCxt47x_|!0$Wp#Nt5)It=*vx>EK#aHZ-6Y(He3KWkZ5t~YCEwd85Z*HTVNNj)QJYbmLvl$N@*)UBl+E%j=tPfPt;a<!DvlGZP&^-F5~l3Kr%UOA;TO=(S2J|Z1BTdZ>H=`>xYPcb;*LejGO{ZvK>x!ztOWP5sqkm;5}Pc|o8`aL<u>Jx&M>lT9T%fU%cu9M2jF<qH{A@p_2b$WWG;JdyMygs#ZPgd^LC0lZ8i>#lLU0zZMu4l_Ju57UwY_NBsRGM^Dyf0g(K_Al@`kF(482b(T3XCch%7uK@ElIDe(+!O24Z6<WanUVhJeRd^(|ZF(-mkf}S`~|Tz-bK;qma|>E&bqg_&W-t{9@oYt!Iko+<-x+=zGu$USHAsV)h*2-LL32-$BeU1_8JAtraAegS42ZKhZzb4AQDVjVTZ=FLnj%2>h6a%p}}datq}_Sa=ZQ`mL*j0yCDK=|c5~8>s$h2l^TsHxa4d+KM(!T}MrWrfwh@^F12-1{Q%SFa+Ati0thoEMq-CXN<emz;{%-JGny9$Jt7`=9g=MOj|t8LUH!XbIy^|!-qzPF-C_W_c47$f2MP+Z!FEcycZf-ibGfX0g-;t3yJ3@dp3nx!UWvALU-u8c3kr?5tBU-69WLpf@8652wQn1PQ{a_hA;$ViN0vrmOsaWVj=5eK8z*loXJRSiB1i|>jJ$^Fd4Jb!W5DwBw~()FFamy@Vo))QwlZjC2ZTopJ%IBmOnB50RZ((H9%l_(DE$t{Ax=U0ou7~47#gyo`drNeLe^c3xM`FglDHpjmUDrWGNH0OG<dI((6YKjbgd*0$6k{^cwT^W5SMtn<`ae?JJapXMTsX1ATb@;m?1jKfFcE%p}XBSqSJHK63W7j3AsdQ;>ky;_`Z|u_4{)prDZFq{B46L+5pSwo=MexT%VpbeHD`*{BaDnz`fC(nO^}?7&vk%)`Ge1(ydQ(U_d+Ohk4`D>nNrebK~cmnEACrP`x4MBf#}RcjCFcFSLBUS6b3tjS>#J*AH{2k)xWWu(!MCrC)#D%6Z{c|6BtRzT$<@XUomo;^g=nZ$yeR#VsLBK<|egt>fG(<AJ8zKrx9P$G?-`AX!#Ed7x#hZ(?%phY6rih(|G3U}8R9PPMq<C&4;!`NcH!xNr$tv7YqoQhb((C`Ut6V}pf!nl-`&Xw^%t}+jixEn)@+@jmSQ`6caD@<qMl^Hogr2jfy!jfiJ>873~h*jXA3qtjgAz%ZR$t8(}`(KYu5v*OuV!<m9L?X=Fo^w~jY0PEu=Yi(QCs8`%odg37bM9o^#v#o?7H&FW8j}OYq`>1CoJ&d5NP$scdRo$1!$`i=dr4?FV+)mrisN2L(^&UR@J7fTK}p+Th-^9h9#PO0h!Fvs<mn>;qTR9_!7&CatdKwzdKxQ!Xl+gj)+C_G-cV4REb_WcwI~MVu+}@T(8UPen5uy)t|aP{Y7LO>h-^hOAqAO`5}8o-YZt0z1Jn_<4-{)*<x_JrQ2Ow4$b(kMZm;5eTY<9dDBN&-RSOl$xi*I?fCZy}f7?cq`{wCR$jpq4W&H_b-pLBhvXgB`%j<&gc10(_+JC*=b-b0+<HH?b+TUxtPP47{x<!mxpo>vsw(3vr>w20^LLuQR5<7reR6(Sj8VA%$GLwvbOpn(Ho>)&#^|n<d^i=4B&@8Q}TlON_?HN=r`|WhY)+A*7C3=-3TT<FIy$kyiN$WUz2#b^pQPYNW^wv<@gg2u0876Sf>YMnBN*qx&66t<hvtw79FB!k4I7s)&2GigeSF`Q3;009<l4vR^hKVbuKi(<$Na@OmiIul92#Tjz^kp{6knwJn#buVlzLSG<84mIB3S4O5jLt>FBD0rM4-2ijr$zH!5mQ?WcY#6+0zN0OC=swr+SK*KCypnA|5g@e>JN816G123*jU#lG7^UH<>N?!)qp9PbM=k8S@?xn8*}iVPh_7RWHFpJiK(||({%gp5o0$@ris#uue-|;39JjJWG5@l>a)w8h{%hTt*%bY3`q7nh*$k;jx^%n!9>9O5(d_NX6W2!^sU~nePPJ2>a)uzk_Ws{h`qfipCp?AuTdy7WJbV9wh9o|Dvnpl2Ca}&F#7bojm1$zQPfzMC3R8NaBfGdD(-tYOXHeUcwnD)w8n}R)A-IbE}6zfIQ1@ZpI!uKoGIi762bX$BH%%r0Bk`37S{j(lMR&y`!u9#hp6+VBtJ>=+ujm=$-a`bexuM|B@Yb^Im74Jm&r4ZgZ1}FcEf-@U~i#4MzJ)(K4Zr9$(hY%0-w^{NXY*%7MO+'),'Libraries/Compiler/ast_to_py.☾':strd('c%0o^>vI!F693L$u~6mgtSu^%2p6J4+!5n@R7`LIp{~kywq$8dROqqUT?hN}DBc(n!pk^7AV3Hqyzj^h2!tx8>b~CJ5P!T+`4g^tUOW4cv@-s5s<I``&h-4IyQinSr#0=ho5oD5UTxQ$S|z9$^`_hQ0;BHRt+v;!H0u9wYOAKP*B)nXZ`-TM9((pS>VB|_&_ne2*p9yv+s03S+d8&w`%c>?rswSS>Vf0=X3p5%XirrdKCvt-XYh`jw`}>#=(aaEkM6LCM@Kfl4MP~Ew?>Gi56Bs;dD|F#9$#CSgbA<F&*&+mR5s`VdYUd03!6^RJGSpS)iN}GMGp^e-bvuom-IF<moA;1m?`G-Z|wAD9Q?F?dg;;^yy?#{i)>rG#@pU*w;U5E7UbchAJptUduwULkKE>?JSUj(T7uO51H5sr?lfw=ZQ`ALK0lo=Oufb*)trXteB=plskU1|y`>-?y}_HOJg2fJhG(j=$F4S79WcFk&PUd#1*u2pd4toCO)sv=7Pb8OeY|P9?dgaM`N9T)uTk;+6d+L$TeocyK%nC_dY<ktn}QyrVp;^gJNbNte-FI57|ph;ujv$>rwhdV<dcDcci(;Gm5)B!v}xnUp`jNK)~;Q<^y%S2`tz%xVdKR~%NR10R34w?)L(s7tnRaeykT%qG#nG`-Bgwh-|&WwszLCmtQxNJhSjoR{yW|vIkq%^lQ&dawGLfg+~wa}?LhXJ7t)f-Gk;8VF;wHR!=jfj8;;5b13E@nXj!Ys$lJrXMNGPn?uQ2lVHX{yN9a-D<}rGlehPc&1pS<z1pc0;XXshFK+n-d5Z48I5qNlsUIqzVp;tkKU(@UK8+wC&OK;Ne=q-Ai-l2EtJ$j!$p#P-*q7Ui!^auJQ{fR!JkLeTo3w=tT(dQ<h*gm`kQ4GJceLHDXnp3q3qP$Pf=J@-W6233eA4#+sR#Ta(ZhmvPP+SLMHEk2uv}0@}6SeP?)Q}xOhyKb4Ijt%ZiV|UiAJO{+7<QgMOguaUEcuDvCE~+9F$psMI&ky}vK+n)m+{>SpYlmz)|yilRttDZ_+&XFK25jD?~xFNTw%)GmhASG>Lx${im{Phy-~1Dd<b-6f!<Wx7`Vnv?NRzz(FFlp{6Es(H8QqL+G&0EgPuK8JwW(YxN02#H9d_yRTIpX40Gwx{Q>`vrZHfU*__2#5e1B7_<scK&e@J%wf(?L!7V_fh{K$im>KZdEMhfGC<<%g58M_B8}=GJI7lCda#6Zt<t(E<E$G5#H`qz`9azZLL@+TiVXpb`W79IwN*i(r;)ZT#=^<T*XUh!g^_($Re$5y(OvBU_`Z?%Gquz3SGAoW$*hPdCbMWoMkD&#?&$0dTj2=WI3<#LkuBtiHhBNDeMYAh@V7qg;h;v{vp5_eDr84|krBw#JU?IDmpb`Wgk?&zwlO3t%PE&No7e6u$*(pv$8w~c%D1$Zo{qh&{@OR7%iNFBTWYR;OxPYP-<HqxoIYk@~2yJS7kpPE@^9n4d65sfwg-*pOu#sPqW<r4r5s-3&Aw*4pOUIrp9sA|CA20p)(p4$JVwQowEqo{Y=ezX>UR=Cn3e~`+Kcf#(V38G8n2H3z38rS;R^V60&H^7j4pX1PsR@c`P$*5n*(V<5Oy-J-Z<c8#2}&isNS~4f5Eyxye#^v^Zs1U%?{K}oMbg%+O<xwL9XyM!Ol%PWh0`*H8?(WA0~MMOT<+)e2f`VclT!~?EWW5pY$dRj1ExK(6$!srDwy<Cp{byKX6ki>o>t1G6tVzX7Qp`;9%voUGX!^z{>t9ZiuWt>J<6yvoKZQ=Qh?{`1mJ}?m2+K`*x++P`<$1q_Lh-RvJQOhb(4wpGTcm~dccx`g2kJbwg+*sgIpE3-Q!vzby)Gm>R}3Sy9iJ3_sge+BlPbxHk<~wTk$GQUpF%;M1U*chgQom)fdM695^}Q!Na)uX-~s+`lxAukyNTE)k527d}mo{*0E|@-8LI%2)gfGSb`vq{C@e=&r$2x6?LRDzQFr8s*J&+d-QRPW>pYd&4?{LGLyaWB_o@}L!AznNl*qt=MKQW<kIP;W@fEk4WQ>>RdOh+xIfe_U4P>EIFmSpP8>9sqlU}El}$~A)Svf>Ykc{*Ci~&nVpd#{BR&nJ>ftx)RfiOE28Q)k$0IE}%%%DB8cMWvi}ayzKqM$D;+`mCtZSM(!z{-Te+~u^_n$WCGkOXJwOs(rIuarcHCk|%!m!w=X?5&KE5s=RAWK<Uo=nkCP2Q;}&+rI!%$XqZxbNihb0BW)HX7>~M2VieR_CyD!Z(!M;GW?&CJxgB)_@5TykKVS#e)}jKQUwHZ=Xgz8cVnq8IK%FY_{V$BZ>_kF$GhmDOD!p0_!AGt^*KoAGJb?gE2)cCKWN<xm^8xr_|3<858?3AX#@rc7wt_tk<3OuV*(aUF|yk6?E9tn3s8Pp2%!LdP8_?WH}HNGd8Rol5JzlK?3&l^A*A%#x4iNjunLAzZ{H}(hcELFBiu3eqdY_)7}v8*I|!aGHSV{$GY0qEtO+#cUE{lFjqU<{8n0;4D*r+V=f~#73N2dfk^NwCbIpRDc!28h>96(7JP?3I0nayojqs2g_a9Wo0Ig4IEqD7!x@7QuEri<oDqgR1q)mHbJo^yW1AY#CRQ%bkTB&$hGd|YnmS2xRED)|_5t5y<NQ`E?B!n~aj6)x#$tepTET!iE+E2TJn9+oBOjyjady?3>eK6-n3(M&%T|nM+3o^^B@?V%W}vu3*;P_Tw4H*+^YnrhPiQ0@2<_&IiFr4pIuy>MFTv>l1c-!WS$ICkRRr+grdLUdl}T4t-5*bAte~Y4NsCMQSX~NcdVWfwk9aDXSpvajpDg)*=1DY_a$Q_jxpt!-sI&^3H)BGj*KR;?DIR(9CPpU24*;!$gx@yj6jpU_%dcz0`(2jf8ynfB?R_oZUC{I0JlUP&w@b^|UGINT@m9!2aPvIiuVL0M27h@w|MI@<`G;7{96bcG=AJI^bKd82*s~W@=G>V`l-xO6n%6$3?X8u`VfJ2que3%v6E9d4a{OydMP}3u?L7Wd#BI}a8+aST4&Wi}aqJ)td*hu=%ma*$Ele7b9Jw9oU5xcEPDWi1V(EM-WsVd5pc&Xp^ZT+fChk$`jN1ENz2Ok)lkl4WSko(fL1$t%5_6i`l|ez{E9fqg2_F{qz`UdkKjW}A*}9ICp`;WE*5eQ{VIX+Tgu7Idf<BSVkaDXX-2j<*TWvSpm*8#WI8j$C8p57DOy}S-7+9aysjZ7AN|wc)!0}rBreaCr>O$d=5Yu+5g{vX4{iHq4o>oB_^$S|awOba5`xIR=wx!Ms&y1bL$1jn~jbq4aVKB9|Qc*smh3Xr3PL9wUQO|AA;M8u3(ccntY4IAGry=Re40Y@>7$dkA15;ih!EUot!%J~%eOp9q%$<ndfvz<QGW>{5$+sb!Q*QKl?8s{-I-Q7kp?M=MGte>IFR|hiD{~CS3&gNU&DoHzr3f@dsWrVeE3WIbYG&wLmGn%5miktS>rF->nsv<**7I4_-0B9)nXNi5-dT6NhRBld?Zp1%>iB#mm(}O><@1ZeMp0=PRuzT~@THsY-z`Bto<9F%k2trduoWZfE#L8wP(dc#Gai<(NOyX+`#otGd#z@^3uBb|vZ5+w5s-A2{LJn<=5IQIP{GFux}ay&l)IAEuLX5T^XW-ge-$khnq?J2qL>IxA@_zXo~s*6P1M!;$<m1eqHb1xES4h8ny#DnTp-Y)SLYmEqF5-=wd%5+qN?C-(L+iosdX<*MmeKq$-6#z<!8ylF4p~cmn+W<8UUiweE=43aINUg<aCzCipIo}P$4?yaj~)uyH^`drDZ#j6Gn6_rQzVRq6gtvy3<<#9JNzUDg0vmBI58}pf@`RIyG6rDv=-%-s%2lKW8YWBb2Pf(kiu@?Y8~2rR9uzIbRC5RmwsgQx(KR2h%mRZ={|}E1T?Mp_I~ES}Td=N=#12EE#o7oA62|kvL(wnY;SBtQ79>lUC-s!3@+@Ws*eHZ&c4~gji`JtjqSC-Su{hjOGkCEJb8W`4cw6r%UvLc7~Br<UcQm91V+&TofVLITsxEM3Lh7=r}%~6r0Osez6N!tjWn$z52<0I5?`B^XMBEa%?hugu{wz7!C-@vxPP*u3YGjt>H?;8p;I_;CZg8_j<XHG+Go})E!QZqkJOv;vnj+pl$nJ6~IKZMT_)-0F<I=UNbbMvq>vDt8~#-x6_;fMT-d}%K&w+9=Uf)j-V&$gMMd;j44K4IIc?_xE%G!AxglJ5WsTP6Kq4?A|>SScH-vnj%B|UaZS=SGja$EwbKkjLQ%D6<2VO~9t592tl)}+b|q46Nsl%oO2*ezl!B9T_zDBY7v?uSQTK+IM@QKn75g(;)fTQu!|UmpOpaJBVRYPEQM?hB7E@TNnUG#AElQTIdufPDlOr*0&S;hM8W*=GFT~=<5<A;^_ToD;j2L=UFEUV7K!diIkBZ=oI6R}=<h5r48;oAPWjE28*FoTIGyDHYtSxkjI~YprniD4vjux))j;-mJ)@UFWvO2^9wy;62s{YsPIVZ>t?wj-qNgOGv@SiUo4|Z5aq~xC)EhZW}@EoTsT+&t>NVO_W$Nr$=`Lfk>T=*tBX-s0oaADK+M#Gj3_IvGy<J(gezh2cHLDK2>2ZN%F3*1_k366q@SES1@hq!b6=Rfh7lle1;Niw~moX^nVzCjmAAFdi#)Uctq{$ptwbMaozRYJA^l}JTlWG>DnZY>l)n5TCmdMn0Qr1^TWUBg31rV~AX;eiz-LNyY7K{&h{|CuRF$i4>NT%xO7Pz7%W&6yS>Xok@RZ<nn=SjM?5U1E%|H_(2V1h?k(a00PG%;9#;DNVFQ6$0+ty{(xhl7fJ&TzGvw$fg|kn5TDxw`{&qSZ|`od>A$%=HH%%SB|V2L7(d}Jwn8eF-JVF%?=`WE_e^HaX!^syH^_m20}#w>W8%U$lvi-w>xZ`s2|RP`7qV~h44{*W=|jrGi7j2%v~c`Uk3jz>wkwd1j_')})
__dir__=(__file__:=áÌî(moon_dir/'/home/ganer/Projects/Moon_BETA/Libraries/Compiler/main.☾')).parent
from sys import stdin as ÂÐðþáÐâ
from time import time as áÏÖ
from subprocess import Popen
__ÄÊIMPORT__('text_format', globals())
(ÄÊPSH(__ÄÊIMPORT__('to_ast', globals())), __ÄÊADDGLOBALS_CLEAN__(ÄÊPKE(), globals()), ÄÊPOP())[-1]
(ÄÊPSH(__ÄÊIMPORT__('ast_to_py', globals())), __ÄÊADDGLOBALS_CLEAN__(ÄÊPKE(), globals()), ÄÊPOP())[-1]
(ÄÊPSH(__ÄÊIMPORT__('tree', globals())), __ÄÊADDGLOBALS_CLEAN__(ÄÊPKE(), globals()), ÄÊPOP())[-1]
(IDENT := 'ι')
(BASE := ÂÞÅCAT('/home/ganer/Projects/Moon_BETA', áÌî))
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
(decorate_code := (lambda áÖï, áÖý: '__dir__=(__file__:=%s(moon_dir/%s)).parent\n%s' % (PEV('𝐩'), repr(ÂÞÅCAT(áÖý, ÁÜÙ)), áÖï)))

def compile_code(áÖï, áÖý=None):
    if áÖý is True:
        (ÄÊPSH((ÂÞÅCAT(áÖï, ÐØó), áÖï)), ((áÖï := ÄÊPKE(0)[0]), (áÖý := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (áÕÃ := moon_to_py(áÖï))
    if áÖý is not None:
        (ÄÊPSH(áÕÃ), ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0), ÄÊCUR((1,), {}, decorate_code, ÂýÃ, (ÄÊPSH(áÖý), ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0), áÌî)), (áÖý := ÄÊPKE(0)), ÄÊDEL(2))[2]))), (áÕÃ := ÄÊPKE(0)), ÄÊDEL(2))[2]
    return áÕÃ
(compile_files := (lambda F: Âøî(ÐôÅ(F, lambda ÂîÓ: Âåß((áÕÃ := compile_code((áÖï := ÂÞÅCAT(ÂîÓ, ÐØó)), ÂîÓ)), Âçß('Compiled %s %s ⭢ %s' % (MOD(ÄÕéý, áØÁ=dotrim)(ÂÞÅCAT(ÂîÓ, ÁÜÙ), 25), MOD(ÄÕéý, áØÁ=dotrim)(MOD(ÄÔéÄ, áØÁ=áÖï)('\n', '𝗻'), 35), MOD(ÄÕéý, áØÁ=dotrim)(MOD(ÄÔéÄ, áØÁ=áÕÃ)('\n', '𝗻'), 35))))), '\n')))

def generate_bootstrap(dest=ÂÞÅCAT('/tmp/bootstrap.py', áÌî)):
    (ÄÊPSH(PL_FORK(compile_code, __file__, True)), ((_ := ÄÊPKE(0)[0]), (Æå := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (pyc := ('%s\n%s\n%s\n%s' % (pathlib_import, ÂÞÅCAT(header_com, compile_files), ÐÌü(dump_cached_imports), ÐÌü(Æå))))
    if dest:
        ÐØì(dest, pyc)
    return pyc

def update_importer():
    ÐÌü(getattr(TP_CACHE, 'clear'))
    for k, v in [*__ÄÊIMPORTS__]:
        if not (getattr(v, 'hardcoded') or getattr(v, 'name') == 'Compiler'):
            continue
        getattr(__ÄÊIMPORTS__, 'pop')(k)
    __ÄÊIMPORT__('Compiler', globals())
    TRANSPILE_REF(moon_to_py)

def moon_cli():
    import traceback, readline
    (ns := globals())
    (ÄÊPSH(ns), ÄÊPSH('globals'), ÄÊPSH(lambda: ns), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    (pfx := Åøþáüì('✝ ', 'f0a', rl=True))
    while True:
        (áÖï := ÂÞÅCAT(pfx, input))
        if not áÖï:
            Âçß('God is good!')
        elif áÖï == 'clear':
            getattr(os, 'system')('clear')
        else:
            Âçß('%s\x1b[1A%s\x1b[K' % (pfx, ÂÞÅCAT(áÖï, __highlighter__)))
            (áÕÃ := compile_code(áÖï))
            Âçß(ÂÞÅCAT(ÂÞÅCAT(áÕÃ, VEP), __highlighter__))
            try:
                Âçß(ÄÕôñ(áÕÃ, ns=ns, native=True, Æå=eval, ret=True))
            except:
                try:
                    ÄÕôñ(áÕÃ, ns=ns, native=True, Æå=exec, ret=True)
                except áÍÚ as Ïã:
                    Âçß(Âøî(ÂÞÅCAT(Ïã, getattr(traceback, 'format_exception')), ÁØã))

def transpiler_cli(*áÒø):
    (show_docs := (lambda: Âçß('Usage: e <str_to_encode>\n       d <str_to_decode>\n       b <boostrap_dest>\n       B <boostrap_dest> (updates compiler)\n       o <file_in> <file_out?stdout> (header ✗)\n       O <file_in> <file_out?stdout> (header ✓)\n       r <code_to_run>               (header ✗)\n       R <code_to_run>               (header ✓)')))
    if ãÊú(áÒø):
        (ÄÊPSH(áÒø), ((m := ÄÊPKE(0)[0]), *(áÒø := ÄÊPKE(0)[slice(1, None, None)])), ÄÊDEL(1))[1]
        (Æå := (moon_to_py_debug if 'a' in m else moon_to_py))
        if 'e' in m:
            ÁØò(lambda ÂîÓ: Âçß('%s ⟶ %s' % (ÂîÓ, PEV(ÂîÓ))))(áÒø)
        elif 'd' in m:
            ÁØò(lambda ÂîÓ: Âçß('%s ⟶ %s' % (ÂîÓ, VEP(ÂîÓ))))(áÒø)
        elif 'b' in m:
            generate_bootstrap(ÂÞÅCAT(áÒø[0], áÌî))
        elif 'B' in m:
            ÐÌü(update_importer)
            generate_bootstrap(ÂÞÅCAT(áÒø[0], áÌî))
        elif 'o' in m:
            ÐôÅ(Ááú(áÒø, [0, 1, 2]), lambda x: ÂÞÅCAT(compile_code(ÂÞÅCAT(x[0], ÐØó)), ÄÊCUR((2,), {}, ÐØì, x[1], ÂýÃ) if x[1] else Âçß))
        elif 'O' in m:
            ÐØì(áÒø[-1], compile_files(header_com) + ÂîÊ(Áÿú(áÒø[slice(None, -1)], Âåæ(Æå, ÐØó)), '\n'))
        elif 'r' in m:
            ÂÞÅCAT(Æå(Âøî(áÒø, ' ')), exec)
        elif 'R' in m:
            ÂÞÅCAT(pathlib_import + '\n' + compile_files(header_com) + '\n' + Æå(Âøî(áÒø, ' ')), ÄÊCUR((1,), {}, exec, ÂýÃ, {}))
        elif 'D' in m:
            while True:
                Âçß(ÂÞÅCAT(ÂÞÅCAT(ÐÌü(input), VEP), __highlighter__))
        elif 'h' in m:
            ÐÌü(show_docs)
        else:
            ÂåÔ(Âçß('Invalid mode(s): %s' % (m,)), ÐÌü(show_docs))
    else:
        ÐÌü(moon_cli)
__ÄÊADD_EXPORTS__(globals(), ('moon_to_py', moon_to_py), ('moon_to_py_debug', moon_to_py_debug), ('compile_files', compile_files), ('generate_bootstrap', generate_bootstrap), ('transpiler_cli', transpiler_cli), ('moon_cli', moon_cli), ('update_importer', update_importer))
TRANSPILE_REF(moon_to_py)
if __name__ == '__main__':
    transpiler_cli(*áÑË[slice(1, None)])