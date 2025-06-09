
__file__='/home/ganer/Projects/Moon_BETA/Header/base.☾'
import os, sys, inspect, traceback, threading
from os import environ as env
from sys import stdin, stdout, stderr, setrecursionlimit, path as syspath, exit, argv as áÑË
from math import *
from site import getsitepackages
from json import dumps as jdumps__, loads as jloads__
from time import time, sleep
from cmath import *
from types import UnionType
from random import shuffle, choice, uniform, randint
from pathlib import Path as áÌî
from tempfile import gettempdir
from builtins import setattr as setattr_
from operator import setitem as setitem_, __gt__, __lt__, __ge__, __le__, rshift, lshift, getitem, delitem
from itertools import chain, filterfalse, product, accumulate, zip_longest
from functools import partial as MOD, reduce, cache
getattr(syspath, 'extend')(getsitepackages())
setrecursionlimit(100000)
(moon_dir := áÌî('..'))
del (getsitepackages, factorial, e, pi, tau, sqrt, cbrt, pow)
(setattr := (lambda x, y, z: setattr_(x, y, z) or z))
(setitem := (lambda x, y, z: setitem_(x, y, z) or z))
(ÄÊSTK := [])
(ÄÊPSH := (lambda x: getattr(ÄÊSTK, 'append')(x) or x))
(ÄÊPKE := (lambda x=0: ÄÊSTK[-1 - x]))
(ÄÊPOP := (lambda x=0: getattr(ÄÊSTK, 'pop')(-1 - x)))
(ÄÊDEL := (lambda x: getattr(ÄÊSTK, '__delitem__')(slice(-x, None))))
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
    (__repr__ := (lambda áÑÞ: 'Timer[%s; %ss; %s; %s Remaining loops]=%s' % ('ID'[getattr(getattr(áÑÞ, 'áÓË'), 'y') >= 0], ÂüÌ(getattr(getattr(áÑÞ, 'áÓË'), 'y')), ÂÛê('Running\u2009Completed')[ÂÕÅ(áÍÖ, áÑÞ)], getattr(getattr(áÑÞ, 'áÓË'), 'n'), getattr(getattr(áÑÞ, 'áÓË'), 'r'))))
(tmp := {'ᴍ': 'Áÿú', 'ꟿ': 'ËãÂ', 'ſ': 'ÆÑ', 'Ϝ': 'ÐÌ', '\U000f0233': 'ÄÔÔè', '\U000f0232': 'ÄÔÔç', '\ueb86': 'ÐÌÛ', '\U000f04bc': 'ÄÔàÑ', '\U000f04bd': 'ÄÔàÒ', 'ᙎ': 'Ááæ', 'ᙡ': 'Ááú', 'ᗢ': 'Áßô', 'ᙧ': 'ÁâÁ', '⊚': 'ÂØÍ', '⊜': 'ÂØÏ', '🟕': 'ãéÜ', '🟖': 'ãéÝ', '⊛': 'ÂØÎ', '⍟': 'ÂÛÜ', '○': 'Âåæ', '⍜': 'ÂÛÙ', '\U000f0b2b': 'ÄÔüÑ', '\U000f0b29': 'ÄÔüÏ', '\uf071': 'ÐâÄ', '\U000f0536': 'ÄÔâÑ', '\uea6c': 'ÐÇò', '\U000f147c': 'ÄÕåØ', '\U000f7e45': 'ÄÝöÔ', '⪡': 'Âúù', '⪢': 'Âúú', '\U000f0e35': 'ÄÕÊÂ', '\U000f0e37': 'ÄÕÊÄ', '⤉': 'ÂóÍ', '⤈': 'ÂóÌ', '⟷': 'Âîí', '\U000f7e4c': 'ÄÝöÜ', '\U000f7e4d': 'ÄÝöÝ', '\U000f7e4e': 'ÄÝöÞ', '\U000f7e39': 'ÄÝöÈ', '\U000f7e3a': 'ÄÝöÉ', '\U000f7e38': 'ÄÝöÇ', '\U000f7e3b': 'ÄÝöÊ', '⨝': 'Âøî', '⟕': 'ÂîÊ', '⟖': 'ÂîË', '⟗': 'ÂîÌ', '⫰': 'ÂüÌ', '⫯': 'ÂüË', '\U000f7e52': 'ÄÝöâ', '\U000f7e53': 'ÄÝöã', '\U000f7e54': 'ÄÝöä', '\U000f7e55': 'ÄÝöå', '\U000f7e56': 'ÄÝöæ', '\U000f7e13': 'ÄÝõà', '\U000f7e3c': 'ÄÝöË', '\U000f7e14': 'ÄÝõá'})
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

__file__='/home/ganer/Projects/Moon_BETA/Header/system.☾'
def PL_SLEEP(x):
    from time import sleep
    sleep(x)

def PL_TIME():
    from time import time
    return time()

def PL_CPU_COUNT_():
    import multiprocessing
    return getattr(multiprocessing, 'cpu_count')()

def PL_THREAD(Æå, *áÑË, **áÑÕ):
    from threading import Thread as T
    (atom := [])
    ÐÌü(getattr((t := T(target=lambda: ÂÞÅCAT(getattr(atom, 'append'), Æå(*áÑË, **áÑÕ)))), 'start'))
    return lambda: ÂåÔ(ÐÌü(getattr(t, 'join')), atom[0])

def PL_TEXT_COPY(x):
    try:
        from clipboard import copy
        return copy(x)
    except Exception:
        print('WARNING: Failed to copy.')

def PL_TEXT_PASTE():
    try:
        from clipboard import paste
        return paste()
    except Exception:
        print('WARNING: Failed to paste.')
(áÐè := PL_THREAD)

__file__='/home/ganer/Projects/Moon_BETA/Header/ops_A.☾'
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

__file__='/home/ganer/Projects/Moon_BETA/Header/ops_B.☾'
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

__file__='/home/ganer/Projects/Moon_BETA/Header/ops_C.☾'
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

__file__='/home/ganer/Projects/Moon_BETA/Header/ops_\uea8c.☾'
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

__file__='/home/ganer/Projects/Moon_BETA/Header/ugex.☾'
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

__file__='/home/ganer/Projects/Moon_BETA/Header/ℵ.☾'
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

__file__='/home/ganer/Projects/Moon_BETA/Header/!.☾'
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

__file__='/home/ganer/Projects/Moon_BETA/Header/𝔍.☾'
(áÐÞ := ÂÞÅCAT({ÁÁ: ÄÊCUR((1,), {'ensure_ascii': False, 'indent': None, 'separators': ',:'}, jdumps__, ÂýÃ), ÿ: jloads__}, ÂÑÖ()))

__file__='/home/ganer/Projects/Moon_BETA/Header/🌈.☾'
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

__file__='/home/ganer/Projects/Moon_BETA/Header/kots.☾'
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

__file__='/home/ganer/Projects/Moon_BETA/Header/extra_globals.☾'
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
    (NRM := getattr(ÁÜÙ, 'maketrans')(CHAR_SUP + CHAR_SUB, 2 * CHAR_NRM))
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

__file__='/home/ganer/Projects/Moon_BETA/Header/highlighter.☾'
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

__file__='/home/ganer/Projects/Moon_BETA/Header/meta.☾'
(IMPSIMPS := (('ℍ', 'ℍ\U000f7e19\U000f7e18\U000f7e1b\U000f7e1a\U000f7e17\U000f7e16\U000f7e1c\U000f7e3d\U000f7e15ĵ\U000f7e88\U000f7c7d\U000f7c7e'), ('⫚', '⫚'), ('¶', '¶✿')))

def __ÄÊADDGLOBALS_CLEAN__(M, áÒÿ):
    getattr(áÒÿ, 'update')(M)

def __ÄÊIMPORT__(p, áÒÿ):
    MOD(Âçß, áØÁ=ÁØã)('.')
    return
    (p := áÌî('/tmp/compiled_Libraries$$%s.py' % (MOD(ÄÔéÄ, áØÁ=p)('/', 2 * '$'),)))
    (ÄÊPSH((getattr(p, 'name'), ÐØó(p))), ((name := ÄÊPKE(0)[0]), (áÖïþáÖüþáÖðþáÖñ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (ns := getattr(áÒÿ, 'copy')())
    getattr(ns, 'pop')('__EXPORTS__', None)
    (ÄÊPSH(ns), ÄÊPSH('__file__'), ÄÊPSH(ns), ÄÊPSH('__dir__'), ÄÊPSH((p, getattr(p, 'parent'))), (setitem(ÄÊPKE(4), ÄÊPKE(3), ÄÊPKE(0)[0]), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)[1])), ÄÊDEL(5))[5]
    exec(áÖïþáÖüþáÖðþáÖñ, ns, ns)
    getattr(áÒÿ, 'update')(getattr(ns, 'get')('__EXPORTS__', {}))
    return ns

def __ÄÊADD_EXPORTS__(áÒÿ, *áÑË):
    (E := getattr(áÒÿ, 'setdefault')('__EXPORTS__', {}))
    getattr(E, 'update')({**dict(áÑË)})
    return E
from subprocess import Popen

def ÄÕôñ(áÖï, ns=None, get_code=False):
    ÐØì((pi := áÌî('/tmp/%s.☾' % ((fn := sha(__file__, áÖï)),))), áÖï)
    (po := ð(getattr(pi, 'parent'), '%s.py' % (fn,)))
    ÐÌü(getattr(Popen(ÂÛê("bash\u2009-c\u2009%s o '%s' '%s'" % (env['PREVILER'], pi, po))), 'wait'))
    (code := ÐØó(po))
    if get_code:
        return code
    return eval(code, *(ÂÚü() if ns is None else [ns]))

# /home/ganer/Projects/Moon_BETA/Libraries/text_format.☾⟶/tmp/γ/BZnq75qCvzepzQyMhGqhVkJEyoMy4nbdjZ6o1fnGrcI.py
exec('\n__file__=\'/home/ganer/Projects/Moon_BETA/Libraries/text_format.☾\'\nimport re\n(áüícache := (lambda Æå, *áÑË, **áÑÕ: ÂåÔ((Ëðá := cache(Æå)), lambda *áÑË, **áÑÕ: (Ëðá if ÂøÑ(ÁØò(lambda ÂîÓ: ãÊú(ÂîÓ) if ÁØö(ÂîÓ, áÓö) else 1)(áÑË)) < 1024 else Æå)(*áÑË, **áÑÕ))))\n(ÄÊPSH((áüícache(__highlighter__), áüícache(termclr))), ((H := ÄÊPKE(0)[0]), (Åøþáüì := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n(find_esc_seqs := getattr(re, \'compile\')((S := \'\\x1b\\\\[(?:\\\\d+;2;\\\\d+;\\\\d+;\\\\d+|0)m\')))\n(find_next_char := getattr(re, \'compile\')(\'((?:(?:%s)|\\x1b\\\\[0m)*.?)\' % (S,)))\n(rm_esc := áüícache(ÄÊCUR((3,), {}, getattr(re, \'sub\'), find_esc_seqs, ÁØã, ÂýÃ)))\n(dotrim := áüícache(lambda x, y: x[slice(None, y - 1)] + \'…\' if áüíþËðâ((x := ÁÜÙ(x))) > y else x))\n(lines := (lambda ÂîÓ: getattr(ÂîÓ, \'split\')(\'\\n\')))\n(tspl := (lambda x, y: Áÿú(áÇù(getattr(re, \'findall\')(find_next_char, x), y), Âøî)))\n(áüíþËðâ := (lambda x: ãÊú(rm_esc(x)) if ÁØö(x, ÁÜÙ) else x))\n(áüíþáüí := (lambda x: (lambda ÂîÓ: (MOD(ÂóÍ, áØÁ=0)(Áÿú(ÂîÓ, áüíþËðâ)), ãÊú(ÂîÓ)))(lines(x)) if ÁØö(x, ÁÜÙ) else (x, None)))\n\ndef slice_áÖùþáÖï(áÖï, áÖý):\n    (áÖÞ := áØÁ[slice(áÖý[0], áÖý[2] + 1)])\n    if ãÊú(áÖÞ) == 1:\n        (áÖÞ := Âêà(áÖÞ[0][slice(áÖý[1], áÖý[3])]))\n    else:\n        (áÖÞ := [áÖÞ[0][slice(áÖý[1], None)], *áÖÞ[slice(1, -1)], áÖÞ[-1][slice(None, áÖý[3])]])\n    return Âøî(áÖÞ, \'\\n\')\n\n@áüícache\ndef pad(áØÆ, áØÇ, áØÈ=\' \', áÖü=-1):\n    (ÄÊPSH((áüíþËðâ(áØÆ), áüíþËðâ(áØÇ))), ((l := ÄÊPKE(0)[0]), (áØÇ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n    if l >= áØÇ:\n        return áØÆ\n    (ÏÁ := (áØÇ - l))\n    if áÖü == -1:\n        return áØÆ + ÏÁ * áØÈ\n    if áÖü == 0:\n        return ÂîÌ([ÏÁ % 2 * áØÈ + áØÆ], ÏÁ // 2 * áØÈ)\n    if áÖü == 1:\n        return ÏÁ * áØÈ + áØÆ\n    ÂùÆ(False, \'%s∉\\U000f7c3e\\U000f7e3b1\' % (áÖü,))\n(padl := (lambda x, y, *áÑË: Âøî(ÁØòþÁÙÄ(lambda ÂîÓ, ÂîÒ: pad(ÂîÓ, ÂîÒ, áÑË[0] if áÑË else \' \', áÖü=-1))(lines(x), áüíþáüí(y)[0]), \'\\n\')))\n(padc := (lambda x, y, *áÑË: Âøî(ÁØòþÁÙÄ(lambda ÂîÓ, ÂîÒ: pad(ÂîÓ, ÂîÒ, áÑË[0] if áÑË else \' \', áÖü=0))(lines(x), áüíþáüí(y)[0]), \'\\n\')))\n(padr := (lambda x, y, *áÑË: Âøî(ÁØòþÁÙÄ(lambda ÂîÓ, ÂîÒ: pad(ÂîÓ, ÂîÒ, áÑË[0] if áÑË else \' \', áÖü=1))(lines(x), áüíþáüí(y)[0]), \'\\n\')))\n(linewrap := áüícache(lambda áØÆ, d=80, p=4 * \' \': Âøî(ÁØò(lambda ÂîÓ: MOD(Áëý, áØÁ=áüíþËðâ(ÂîÓ) > d)(ÂîÓ, lambda x: CURR(lambda ÂîÓ, ÂîÒ: ÂîÓ + \'\\n\' + linewrap(p + ÂîÒ, d, p), *tspl(x, d))))(lines(áØÆ)), \'\\n\')))\n(linenum := áüícache(lambda áØÆ, m=1, s=ÄÕÍÔ: (lambda ÂîÓ: Âøî(ËãÂ(ÂåÔ((l := (ÂóÍ(ãÊú(ÄÝöì(ãÊú(ÂîÓ) - 1)), m) * Ãù)), ÂÓÏ(ÂîÓ)), CUR(lambda ÂîÓ, ÂîÒ: ÂÞÅCAT(MOD(ÄÝöì, áØÁ=l)(ÂîÓ), s) + \' \' + ÂîÒ)), \'\\n\'))(lines(áØÆ))))\n(linewnum := áüícache(lambda áØÆ, m=1, s=ÄÕÍÔ, d=80, p=6 * \' \': linewrap(linenum(áØÆ, m, s), d, p)))\n\n@áüícache\ndef pads(áØÆ, w=ë, h=ë):\n    if ÁØö(áØÆ, ÁÜÙ):\n        (áØÆ := lines(áØÆ))\n    if w is ë:\n        (w := MOD(ÂóÍ, áØÁ=0)(Áÿú(áØÆ, áüíþËðâ)))\n    if h is ë:\n        (h := ãÊú(áØÆ))\n    if h is not None:\n        getattr(áØÆ, \'extend\')([\' \' * (w or 0)] * (h - ãÊú(áØÆ)))\n    if w is not None:\n        (ÄÊPSH(áØÆ), ÄÊPSH(ÁØò(lambda ÂîÓ: ÂîÓ + \' \' * (w - áüíþËðâ(ÂîÓ)))(ÄÊPKE(0))), (áØÆ := ÄÊPKE(0)), ÄÊDEL(2))[2]\n    return áØÆ\n\n@áüícache\ndef stackr(*áÖê):\n    if not áÖê:\n        return ÁØã\n    (ÄÊPSH(áÖê), ((áØÆ := ÄÊPKE(0)[0]), *(áÖë := ÄÊPKE(0)[slice(1, None, None)])), ÄÊDEL(1))[1]\n    if ãÊú(áÖë) == 0:\n        return áØÆ\n    if ãÊú(áÖë) > 1:\n        return stackr(áØÆ, stackr(*áÖë))\n    (áØÇ := lines(áÖë[0]))\n    if (ãÊú(áØÆ) == ÄÊPSH(1) and ÄÊPOP() == ÄÊPSH(ãÊú(áØÇ))) and (ÄÊDEL(1) or True) or (ÄÊDEL(1) or False):\n        return áØÆ[0] + áØÇ[0]\n    return Âøî(ËãÂ(MOD(ÄÕåØ, áØÁ=ÁØã)(pads(áØÆ, ë, ãÊú(áØÇ)), áØÇ), ì), \'\\n\')\n\n@áüícache\ndef box_(áØÆ, fg=\'05059f\', big=False):\n    (áØÆ := pads(áØÆ))\n    (áØÅ := (áüíþËðâ(áØÆ[0]) if áØÆ else 0))\n    (áÓÕ := ÄÊCUR((1,), {}, Åøþáüì, ÂýÃ, fg))\n    if ãÊú(áØÆ) == 1 and (not big):\n        return áÓÕ(\'[\') + áØÆ[0] + áÓÕ(\']\')\n    (ÄÊPSH(MOD(Áÿú, áØÁ=2)(ÂÛê(\'⎡⎢⎣\\u2009⎤⎥⎦\'), áÓÕ)), ((O := ÄÊPKE(0)[0]), (C := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n    if big:\n        return Âøî([ÂÞÅCAT(\'┌\' + ÂÞÅCAT(\'─\', áØÅ) + \'┐\', áÓÕ), *ÁØò(lambda ÂîÓ: O[1] + ÂîÓ + C[1])(áØÆ), ÂÞÅCAT(\'└\' + ÂÞÅCAT(\'─\', áØÅ) + \'┘\', áÓÕ)], \'\\n\')\n    return Âøî(ËãÂ(Ááú(áØÆ, ÂÞÅCAT(2, [1])), lambda x, y, z: O[(n := (1 - (x is None) + (z is None)))] + y + C[n]), \'\\n\')\n(ÄÊPSH(ÁØò(lambda ÂîÓ: lambda x, *áÑË, **áÑÕ: box_(Âøî(x, \'\\n\') if ÁØö(x, áÍá | áÍé) else x, *áÑË, **áÑÕ, big=ÂîÓ))(ÂÿÇ(2))), ((box := ÄÊPKE(0)[0]), (BOX := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n(fmp := {**dict(ÄÕåØ([ÁØã, ÂÞÅ, ÂýÃ, ÄÔýò, True, False, None, ÃÆë, ÃÆì, ÃÆ, ÂÑõ, ÃÅ, ÂÑø, ÂÑü, ÂÑò, ÂÑÿ, ÂÑó, ÂÑô, ÂÑö, ÂÑù, ÄÝóú, ÄÝôÀ, ÃÇ, ÂÑú, ÄÝóû, ÂÒÀ, ÄÝôÏ, ÂÑû, ÄÝóü, ÄÝôË, ÂÑý, ÄÝóý, ÂÒÁ, ÄÝôÂ, ÄÝóÿ, ÂÒÂ, ÄÝôÃ, ÄÝôÐ, ÄÝôÄ, ÄÝôÑ, ÂÒî, ÄÝôÒ, Ïî, ÂÐæ, ÂÕË, Ãù, Ïò, ÄÝøà, ÄÝøá, ÄÝøâ, ÄÝîá, ÄÝîâ, ÄÝîä, ÄÝîå, ÄÝîæ, ÄÝîç, ÄÝîè, ÄÝîã, áÍÚ, áÍä, áÍÙ, áÍÖ, áÍá, áÍé, áÍè, ÁÜÙ, áÍÞ, áÍÛ, áÍî], \'ᐦ␀⬤\\U000f0b88✓✗□ⴳⴴ½⅓¼⅕⅙⅐⅛⅑⅒⅔⅖\\U000f7db2\\U000f7db7¾⅗\\U000f7db3⅜\\U000f7dc6⅘\\U000f7db4\\U000f7dc2⅚\\U000f7db5⅝\\U000f7db9\\U000f7db6⅞\\U000f7dba\\U000f7dc7\\U000f7dbb\\U000f7dc8↉\\U000f7dc9πℇ∞îτ\\U000f7e8d\\U000f7e8e\\U000f7e8f\\U000f7c69\\U000f7c6a\\U000f7c6c\\U000f7c6d\\U000f7c6e\\U000f7c6f\\U000f7c70\\U000f7c6b𝑒𝑜𝑑𝑏𝑙𝑡𝑠ᔐ𝑖𝑓𝑦\'))})\n(ÄÊPSH(fmp), ÄÊPSH(MOD(ËãÂ, áØÁ=ì)(ÄÊPKE(0), lambda x, y: H(y))), (fmp := ÄÊPKE(0)), ÄÊDEL(2))[2]\n(ÄÊPSH(ÁØò(lambda ÂîÓ: Åøþáüì(ÂîÓ, \'ff3\'))(\',[]{}⟶\')), ((COM := ÄÊPKE(0)[0]), (BL := ÄÊPKE(0)[1]), (BR := ÄÊPKE(0)[2]), (CL := ÄÊPKE(0)[3]), (CR := ÄÊPKE(0)[4]), (ARW := ÄÊPKE(0)[5])), ÄÊDEL(1))[1]\n(ÄÊPSH((ÁØö(ÐÌü(ÂÑÖ())) | ÁØö(ÐÌü(ÂÑØ())) | áÍÙ, áÍá | áÍé)), ((áÌý := ÄÊPKE(0)[0]), (áÍÆ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n\ndef áÓÙþáÓàþáÓç(x):\n    try:\n        if x in fmp:\n            return fmp[x]\n    except:\n        None\n    (T := ÁØö(x))\n    if T is type:\n        return H(getattr(x, \'__name__\'))\n    if T is ÁÜÙ:\n        return Åøþáüì(ÁÜÙ(x), bg=\'202\')\n    if T is áÍÞ:\n        return ÁÜÙ(áÍÞ(x))\n    if T is áÍÛ:\n        return ÁÜÙ(MOD(Âäû, áØÁ=5)(x))\n    if ÁØö(x, áÌý):\n        return (ÁØã if ÁØö(x) is áÍÙ else áÓÙþáÓàþáÓç(ÁØö(x))) + CL + Âøî(ËãÂ(getattr(x, \'items\')(), lambda x, y: \'%s%s%s\' % (áÓÙþáÓàþáÓç(x), ARW, áÓÙþáÓàþáÓç(y))), \' \') + CR\n    if ÁØö(x, áÍè):\n        return (ÁØã if ÁØö(x) is áÍè else áÓÙþáÓàþáÓç(ÁØö(x))) + CL + Âøî(Áÿú(x, áÓÙþáÓàþáÓç), \' \') + CR\n    if ÁØö(x, áÍÆ):\n        return (ÁØã if ÁØö(x) is áÍá else áÓÙþáÓàþáÓç(ÁØö(x))) + BL + Âøî(Áÿú(x, áÓÙþáÓàþáÓç), \' \') + BR\n    if ÁØö(x, áÓó):\n        return \'%s\' % (H(getattr(x, \'__name__\')),)\n    return ÁÜÙ(x)\n(Æø := (lambda *áÑË, **áÑÕ: áÑË[0] if ÂåÔ(Âçß(áÓÙþáÓàþáÓç(k[0] if ãÊú((k := (áÑË or [ÁØã]))) == 1 else k), **áÑÕ), áÑË) else ÁØã))\n__ÄÊADD_EXPORTS__(globals(), (\'rm_esc\', rm_esc), (\'lines\', lines), (\'padl\', padl), (\'padc\', padc), (\'padr\', padr), (\'pads\', pads), (\'stackr\', stackr), (\'box\', box), (\'BOX\', BOX), (\'linenum\', linenum), (\'linewnum\', linewnum), (\'dotrim\', dotrim), (\'slice_áÖùþáÖï\', slice_áÖùþáÖï), (\'áüíþËðâ\', áüíþËðâ), (\'Åøþáüì\', Åøþáüì), (\'áÓÙþáÓàþáÓç\', áÓÙþáÓàþáÓç), (\'Æø\', Æø))\n\ndef test_text_format():\n    Âçß(Âøî(tspl(Åøþáüì(\'egg\', \'f00\') + Åøþáüì(\'weeee\', \'0f0\'), 5), \'│\'))\n    Âçß(linewrap(Âçß(linenum("egg salad number twelve fortnite\\nthe last thing you\'d want on your burg")), 12, 3 * \' \'))\n    (a := Âçß(box(\'jo⭥∈ease\\nasoidasdeeee\')))\n    (b := Âçß(BOX(\'jo⭥∈ease\\nasoidasdeeee\')))\n    (c := Âçß(box(\'5⭥ᐵ²\')))\n    (d := Âçß(BOX(\'5⭥ᐵ²\')))\n    Âçß(stackr(a, \'a\\nb\\nc\\nd\\ne\', b, c, d))\n    Âçß(padl(\'egg\', 11, \'─\'))\n    Âçß(padl(\'egg\', 11, \' \'))\n    Âçß(padc(\'egg\', 11, \' \'))\n    Âçß(padc(\'egg\', 11, \'─\'))\n    Âçß(padc(\'lul\', 10, \'─\'))\n    Âçß(padc(\'lads\\nx\', 10, \'─\'))\n    Âçß(padc(\'lads\\nx\', \'jo\\naaa\', \'─\'))\n    Âçß(padc(\'egg\', 11, \' \'))\n    Âçß(padr(\'egg\', 11, \' \'))\n    Âçß(padr(\'egg\', 11, \'─\'))',__:=globals().copy())
for k,v in __.get("__EXPORTS__",{}).items():globals()[k]=v


# /home/ganer/Projects/Moon_BETA/Libraries/𝐍.☾⟶/tmp/γ/lsp2-R_w4MjEb5v3nCWXF3-FZuX671TvFvcEpFoLwZM.py
exec("\n__file__='/home/ganer/Projects/Moon_BETA/Libraries/𝐍.☾'\n__ÄÊIMPORT__('text_format', globals())\nfrom collections import deque as áÐòþáÑÁ\n\nclass áÌÑ:\n    (__slots__ := ('t', 'c'))\n\n    def __init__(ÄÕÒü, t, *c):\n        (ÄÊPSH(ÄÕÒü), ÄÊPSH('t'), ÄÊPSH(ÄÕÒü), ÄÊPSH('c'), ÄÊPSH((t, c or [])), (setattr(ÄÊPKE(4), ÄÊPKE(3), ÄÊPKE(0)[0]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)[1])), ÄÊDEL(5))[5]\n    (__getitem__ := (lambda ÄÕÒü, i: getattr(ÄÕÒü, 'c')[i]))\n    (__iter__ := (lambda ÄÕÒü: iter(getattr(ÄÕÒü, 'c'))))\n    (__repr__ := (lambda ÄÕÒü: '𝐍⟨%s⟩⟨%s⟩' % (getattr(ÄÕÒü, 't') or '∅', Âøî(ÄÕÒü, ', '))))\n    (__len__ := (lambda ÄÕÒü: ãÊú(getattr(ÄÕÒü, 'c'))))\n    (ft := staticmethod(lambda x: áÌÑ(x[0], *(Áÿú(x[1], getattr(áÌÑ, 'ft')) if ÁØö(x[1], áÍá | áÍé) and ãÊú(x[1]) == 2 else [x[1]]))))\n    (tt := (lambda ÄÕÒü: (getattr(ÄÕÒü, 't'), Áÿú(getattr(ÄÕÒü, 'c'), lambda x: ÐÌü(getattr(x, 'tt')) if ÁØö(x, áÌÑ) else x))))\n    (copy := (lambda ÄÕÒü, t=None, c=None: ÁØö(ÄÕÒü)(getattr(ÄÕÒü, 't') if t is None else t, *(getattr(ÄÕÒü, 'c') if c is None else c))))\n    (rcopy := (lambda ÄÕÒü, t=None: ÁØö(ÄÕÒü)(getattr(ÄÕÒü, 't') if t is None else t, *(Áÿú(getattr(ÄÕÒü, 'c'), getattr(ÁØö(ÄÕÒü), 'rcopy')) if ÁØö(ÄÕÒü, áÌÑ) else ÄÕÒü))))\n    (filter := (lambda ÄÕÒü, Æå, *áÑË, **áÑÕ: getattr(ÄÕÒü, 'extract')(Âåæ(Âó, f), *áÑË, **áÑÕ, Ïà=False, ÏÁ=False)))\n    (ftrp := (lambda ÄÕÒü, fs, *áÑË, **áÑÕ: getattr(ÄÕÒü, 'frp')(lambda x: getattr(x, 't') in fs, *áÑË, **áÑÕ)))\n\n    def frp(ÄÕÒü, Æå, r, pre=False):\n        (áÏï := (lambda x: getattr(x, 'copy')(c=Áÿú(x, lambda x: getattr(x, 'frp')(Æå, r, pre)))))\n        (ÄÕÒü := (áÏï(ÄÕÒü) if pre else ÄÕÒü))\n        if Æå(ÄÕÒü):\n            return r(ÄÕÒü)\n        return ÄÕÒü if pre else áÏï(ÄÕÒü)\n\n    def extract(ÄÕÒü, áÍÛ, E=None, Ïà=True, ÏÁ=False, pre=False):\n        (L := (ÄÊPSH(([], [] if (Ïá := (E is None)) else E)), ((r := ÄÊPKE(0)[0]), (E := ÄÊPKE(0)[1])), ÄÊDEL(1))[1])\n        (áÚì := ÄÊCUR((1,), {'pre': pre}, getattr((ÂÐá := ÁØö(ÄÕÒü)), 'extract'), ÂýÃ, áÍÛ, E))\n        Áÿú(ÄÕÒü, lambda x: getattr(L[ÂÞÅCAT(áÍÖ, ÂÞÅCAT(áÍÛ, (x := MOD(Áëý, áØÁ=pre)(x, áÚì))))], 'append')(x))\n        (n := getattr(ÄÕÒü, 'copy')(c=r if pre else Áÿú(r, áÚì)))\n        return ([n, E] if ÏÁ else E) if Ïà and Ïá else n\n\n    def P(ÄÕÒü, fs=True):\n        (ÄÊPSH(ËãÂ(ÂÛê('∅\\u2009f00\\u205f→\\u200900f\\u205f\\U000f0141\\u2009ff0\\u205f\\U000f0142\\u2009ff0'), Åøþáüì)), ((NA := ÄÊPKE(0)[0]), (AR := ÄÊPKE(0)[1]), (yl := ÄÊPKE(0)[2]), (yr := ÄÊPKE(0)[3])), ÄÊDEL(1))[1]\n        if ÄÝøÇ(ÄÕÒü, áÌÑ):\n            return Åøþáüì(ÁÜÙ(ÄÕÒü), 'f00')\n\n        def format_e(e):\n            if not e:\n                return ÁØã\n            (r := ËãÂ(e, lambda x, y: ÄÔýò if x in {'T', 'p'} else '%s%s%s' % (x, AR, getattr(y, 't')) if ÁØö(y, ÅÒ) else '%s=%s' % (x, y)))\n            return MOD(Áëý, áØÁ=r)(ÁØã if 'p' not in e else Åøþáüì((lambda ÂîÓ: Âøî(ËãÂ(ÄÕåØ(Áÿú(ÂÿÇ(ÂîÓ), ÁÛÛ([ÄÝõà, ÄÝõá])), ÂîÓ), ÂÕÅ)) if ãÊú(ÂîÓ) == 4 else ÄÝõà(Âøî(ÂîÓ, '…')))(getattr(e, 'p')), 'ff0'), lambda ÂîÓ: stackr(ÂîÓ, Âøî(r, '\\n')))\n        (áØÀ := box((ÂÞÅCAT(False, getattr(getattr(ÄÕÒü, 't'), 'P')) if ÁØö(getattr(ÄÕÒü, 't'), áÌÑ) else stackr(Åøþáüì(getattr(ÄÕÒü, 't'), 'f55'), ÂÞÅCAT(getattr(ÄÕÒü, 'e'), format_e)) if ÁØö(ÄÕÒü, ÅÒ) else ÁÜÙ(getattr(ÄÕÒü, 't'))) or NA, fg='0f0' if ÁØö(ÄÕÒü, ÅÒ) and getattr(getattr(ÄÕÒü, 'e'), 'T') else '00007f'))\n        if ãÊú(ÄÕÒü):\n            (ÄÊPSH(Áÿú('─╰├┬│', ÄÊCUR((1,), {'fg': '11a'}, Åøþáüì, ÂýÃ))), ((ÂâÑ := ÄÊPKE(0)[0]), (ÂäÇ := ÄÊPKE(0)[1]), (Ââî := ÄÊPKE(0)[2]), (ÂãÀ := ÄÊPKE(0)[3]), (ÂâÓ := ÄÊPKE(0)[4])), ÄÊDEL(1))[1]\n            (áØÀ := stackr(áØÀ, Âøî(ËãÂ(ÂÓÏ(ÄÕÒü), lambda x, y: Âøî(ËãÂ(ÂÓÏ(ÂÞÅCAT(ÂÞÅCAT(False, getattr(y, 'P')), lines)), CUR(lambda ÂîÓ, ÂîÒ: ÂÁÍ(ì)(ÂîÒ, ÂâÑ if ((ÄÊDEL(1), False)[1] if ÄÊPSH(ÂîÓ) else ÄÊPOP() if ãÊú(ÄÕÒü) != 1 else (ÄÊDEL(1), True)[1]) else ÂîÓ and ' ' or ÂäÇ if x == ãÊú(ÄÕÒü) - 1 else x and Ââî or ÂãÀ if ((ÄÊDEL(1), False)[1] if ÄÊPSH(ÂîÓ) else ÄÊPOP() if ãÊú(ÄÕÒü) == 0 else (ÄÊDEL(1), True)[1]) else ÂâÓ))), '\\n')), '\\n')))\n        return ÂåÔ(Âçß(áØÀ), ÄÕÒü) if fs else áØÀ\n\nclass ÅÒ(áÌÑ):\n    (__slots__ := ('t', 'c', 'e'))\n\n    def __init__(ÄÕÒü, t, *c, e=ÂÞÅ):\n        (ÄÊPSH(ÄÕÒü), ÄÊPSH('t'), ÄÊPSH(ÄÕÒü), ÄÊPSH('c'), ÄÊPSH(ÄÕÒü), ÄÊPSH('e'), ÄÊPSH((t, [*c] if c else [], MOD(ÂÑÖ, áØÁ=None)() if e is ÂÞÅ else e)), (setattr(ÄÊPKE(6), ÄÊPKE(5), ÄÊPKE(0)[0]), setattr(ÄÊPKE(4), ÄÊPKE(3), ÄÊPKE(0)[1]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)[2])), ÄÊDEL(7))[7]\n    (__contains__ := (lambda ÄÕÒü, x: x in getattr(ÄÕÒü, 'e') if ÁØö(x, ÁÜÙ) else x in getattr(ÄÕÒü, 'c')))\n    (__repr__ := (lambda ÄÕÒü: 'Ń(%s│%s)⟨%s⟩' % (getattr(ÄÕÒü, 't') or '∅', getattr(ÄÕÒü, 'e') or '∅', Âøî(ÄÕÒü, ', '))))\n    (__setitem__ := (lambda ÄÕÒü, x, y: (ÄÊPSH(getattr(ÄÕÒü, 'c')), ÄÊPSH(x), ÄÊPSH(y), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]))\n    (__and__ := (lambda ÄÕÒü, x: getattr(ÄÕÒü, 't') == getattr(x, 't')))\n\n    def __getitem__(ÄÕÒü, i):\n        return getattr(ÄÕÒü, 'c')[i]\n\n    def __delitem__(ÄÕÒü, i):\n        del getattr(ÄÕÒü, 'c')[i]\n\n    def set(ÄÕÒü, t=None, c=None, e=None):\n        if t is not None:\n            (ÄÊPSH(ÄÕÒü), ÄÊPSH('t'), ÄÊPSH(t), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n        if c is not None:\n            (ÄÊPSH(ÄÕÒü), ÄÊPSH('c'), ÄÊPSH(c), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n        if e is not None:\n            (ÄÊPSH(ÄÕÒü), ÄÊPSH('e'), ÄÊPSH(e), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n        return ÄÕÒü\n    (cp := (copy := (lambda ÄÕÒü, t=None, c=None, e=ÂÞÅ: ÁØö(ÄÕÒü)(getattr(ÄÕÒü, 't') if t is None else t, *(getattr(ÄÕÒü, 'c') if c is None else c), e=ÐÌü(getattr(getattr(ÄÕÒü, 'e'), 'copy')) if e is ÂÞÅ else e))))\n    (cpr := (rcopy := (lambda ÄÕÒü, t=None: ÁØö(ÄÕÒü)(getattr(ÄÕÒü, 't') if t is None else t, *Áÿú(getattr(ÄÕÒü, 'c'), getattr(ÁØö(ÄÕÒü), 'rcopy')), e=getattr(getattr(ÄÕÒü, 'e'), 'copy')()) if ÁØö(ÄÕÒü, áÌÑ) else ÄÕÒü)))\n\n    def part(ÄÕÒü):\n        (ÄÊPSH(ÄÕÒü), ÄÊPSH('c'), ÄÊPSH(ÂÕÃ(getattr(ÄÕÒü, 'c'), getattr(ÄÕÒü, 'e') ** ì)), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n        return (ÄÕÒü, getattr(ÄÕÒü, 'e'))\n\n    def frp(ÄÕÒü, Æå, r, pre=False, not_T=True):\n        if r is None:\n            return lambda r: getattr(ÄÕÒü, 'frp')(Æå, r, pre, not_T)\n        if not_T:\n            (Æå := (lambda ÄÕÒü, Æå=Æå: not getattr(getattr(ÄÕÒü, 'e'), 'T') and Æå(ÄÕÒü)))\n        if pre:\n            if not ãÊú(ÄÕÒü):\n                return r(ÄÕÒü) if Æå(ÄÕÒü) else ÄÕÒü\n            (ÄÊPSH((áÐòþáÑÁ([ÄÕÒü]), áÐòþáÑÁ())), ((áÖå := ÄÊPKE(0)[0]), (áÖæ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n            (ÄÊPSH((getattr(áÖå, 'popleft'), getattr(áÖå, 'extend'), getattr(áÖæ, 'appendleft'))), ((pl := ÄÊPKE(0)[0]), (ex := ÄÊPKE(0)[1]), (al := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]\n            while áÖå:\n                (C := pl())\n                ex([c for c in C if getattr(c, 'c')])\n                al(C)\n            for C in áÖæ:\n                for i, c in enumerate(C):\n                    if not Æå(c):\n                        continue\n                    (ÄÊPSH(C), ÄÊPSH(i), ÄÊPSH(r(c)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n            return r(ÄÕÒü) if Æå(ÄÕÒü) else ÄÕÒü\n        else:\n\n            def áÏï(ÄÕÒü):\n                if Æå(ÄÕÒü):\n                    return r(ÄÕÒü)\n                for i, y in enumerate(ÄÕÒü):\n                    (ÄÊPSH(ÄÕÒü), ÄÊPSH(i), ÄÊPSH(áÏï(y)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n                return ÄÕÒü\n            return áÏï(ÄÕÒü)\n\n    def ftrp(ÄÕÒü, fs, Æå, pre=False, not_T=True, **áÏè):\n        if Æå is None:\n            return lambda Æå: getattr(ÄÕÒü, 'ftrp')(fs, Æå, pre, not_T, **áÏè)\n        if ÄÝøÇ(fs, ÁÜÙ):\n            (fs := frozenset(fs))\n        return ÄÕÒü if not_T and getattr(getattr(ÄÕÒü, 'e'), 'T') else getattr(ÄÕÒü, 'frp')((lambda x: getattr(x, 't') == fs) if ÁØö(fs, ÁÜÙ) else lambda x: getattr(x, 't') in fs, Æå, pre, not_T, **áÏè)\n\n    def gets(ÄÕÒü, Æå, not_T=True):\n        if not áÓó(Æå):\n            if ÁØö(Æå, ÁÜÙ):\n                (Æå := (lambda ÄÕÒü, t=Æå: getattr(ÄÕÒü, 't') == t))\n            else:\n                (Æå := (lambda ÄÕÒü, t=Æå: getattr(ÄÕÒü, 't') in t))\n        return [c for c in ÄÕÒü if (((ÄÊDEL(1), False)[1] if getattr(getattr(c, 'e'), 'T') else ÄÊPOP()) if ÄÊPSH(not_T) else (ÄÊDEL(1), True)[1]) and Æå(c)]\n\n    def find(ÄÕÒü, Æå, pre=True, not_T=True, R=None):\n        if R is None:\n            (R := [])\n        if not_T and getattr(getattr(ÄÕÒü, 'e'), 'T'):\n            return R\n        if pre:\n            for c in ÄÕÒü:\n                getattr(c, 'find')(Æå, True, not_T, R)\n        if (do := Æå(ÄÕÒü)):\n            getattr(R, 'append')(ÄÕÒü)\n        if do and (not pre):\n            for c in ÄÕÒü:\n                getattr(c, 'find')(Æå, False, not_T, R)\n        return R\n\n    def flat(ÄÕÒü, Æå, áÑÂ=True):\n        (C := [])\n        for c in ÄÕÒü:\n            (getattr(C, 'append') if getattr(getattr(c, 'e'), 'T') or not Æå((c := (getattr(c, 'flat')(Æå) if áÑÂ else c))) else getattr(C, 'extend'))(c)\n        (ÄÊPSH(ÄÕÒü), ÄÊPSH('c'), ÄÊPSH(C), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n        return ÄÕÒü\n\n    def rm(ÄÕÒü, Æå, not_T=True):\n        if ÁØö(Æå, ÁÜÙ):\n            (Æå := (lambda ÄÕÒü, t=Æå: getattr(ÄÕÒü, 't') == t))\n        for i, x in ÂÓÏ(ÄÕÒü)[slice(None, None, -1)]:\n            if not (((ÄÊDEL(1), False)[1] if getattr(getattr(x, 'e'), 'T') else ÄÊPOP()) if ÄÊPSH(not_T) else (ÄÊDEL(1), True)[1]):\n                continue\n            if Æå(x):\n                del ÄÕÒü[i]\n            else:\n                getattr(ÄÕÒü[i], 'rm')(Æå, not_T)\n        return ÄÕÒü\n\n    def __pos__(ÄÕÒü):\n        (áØÀ := '')\n        if getattr(getattr(ÄÕÒü, 'e'), 'T'):\n            return getattr(ÄÕÒü, 't')\n        (áÖã := áÐòþáÑÁ(getattr(ÄÕÒü, 'c')))\n        while áÖã:\n            (v := getattr(áÖã, 'popleft')())\n            if getattr(getattr(v, 'e'), 'T'):\n                (ÄÊPSH(áØÀ), ÄÊPSH(ÄÊPKE(0) + getattr(v, 't')), (áØÀ := ÄÊPKE(0)), ÄÊDEL(2))[2]\n            else:\n                getattr(áÖã, 'extendleft')(reversed(getattr(v, 'c')))\n        return áØÀ\n\n    def lchar(ÄÕÒü):\n        if getattr(getattr(ÄÕÒü, 'e'), 'T') and getattr(ÄÕÒü, 't'):\n            return getattr(ÄÕÒü, 't')[0]\n        for c in getattr(ÄÕÒü, 'c'):\n            if not (x := getattr(c, 'lchar')()):\n                continue\n            return x\n        return ''\n\n    def rchar(ÄÕÒü):\n        if getattr(getattr(ÄÕÒü, 'e'), 'T') and getattr(ÄÕÒü, 't'):\n            return getattr(ÄÕÒü, 't')[-1]\n        for c in getattr(ÄÕÒü, 'c')[slice(None, None, -1)]:\n            if not (x := getattr(c, 'rchar')()):\n                continue\n            return x\n        return ''\n\n    def farnodes(ÄÕÒü, Æå=lambda ÂîÓ: not getattr(getattr(ÂîÓ, 'e'), 'T')):\n        (Ïß := (Ïà := ÄÕÒü))\n        while Æå(Ïß) and ãÊú(Ïß):\n            (Ïß := Ïß[0])\n        while Æå(Ïà) and ãÊú(Ïà):\n            (Ïà := Ïà[-1])\n        return (Ïß, Ïà)\n\n    def first_l(ÄÕÒü, Æå):\n        if Æå(ÄÕÒü):\n            return ÄÕÒü\n        for áÎÚ in ÄÕÒü:\n            if not (l := getattr(áÎÚ, 'first_l')(Æå)) is not None:\n                continue\n            return l\n\n    def first_r(ÄÕÒü, Æå):\n        if Æå(ÄÕÒü):\n            return ÄÕÒü\n        for áÎÚ in ÄÕÒü[slice(None, None, -1)]:\n            if not (r := getattr(áÎÚ, 'first_r')(Æå)) is not None:\n                continue\n            return r\n\n    def first_sides(ÄÕÒü, Æå):\n        return (getattr(ÄÕÒü, 'first_l')(Æå), getattr(ÄÕÒü, 'first_r')(Æå))\n    (filter := (lambda ÄÕÒü, Æå, *áÑË, **áÑÕ: getattr(ÄÕÒü, 'rm')(Âåæ(Âó, Æå), *áÑË, **áÑÕ)))\n    (as_txt := __pos__)\n__ÄÊADD_EXPORTS__(globals(), ('ÅÒ', ÅÒ))\n\ndef test_ÅÒ():\n    ÐÌü(getattr(ÅÒ('the', ÅÒ('joe', e=ÂÞÅCAT({'T': True, 'p': [2, 4], 'swag': 'loog'}, MOD(ÂÑÖ, áØÁ=None)())), ÅÒ('egg', ÅÒ('egg2'), ÅÒ('egg3', e=ÂÞÅCAT({'T': True, 'p': [1, 2, 3, 4]}, MOD(ÂÑÖ, áØÁ=None)())))), 'P'))",__:=globals().copy())
for k,v in __.get("__EXPORTS__",{}).items():globals()[k]=v


# /home/ganer/Projects/Moon_BETA/Libraries/peggle2/main.☾⟶/tmp/γ/7OuHL6frjwX5viTFqUthkbhuRPiT_r5cAfo9bDO5xBw.py
exec('\n__file__=\'/home/ganer/Projects/Moon_BETA/Libraries/peggle2/main.☾\'\n(fcache := (lambda: lambda Æå: Æå))\n__ÄÊIMPORT__(\'𝐍\', globals())\n__ÄÊIMPORT__(\'text_format\', globals())\ntry:\n    import regex as re\nexcept Exception:\n    import re\n(show_cache_table := (lambda áÍÌ, ÂÑÎ: ËãÂ(ÂÓÏ(ÂÑÎ), lambda i, v: ËãÂ(ÄÔàÑ(ÂÑÖ()(v) ** ë), lambda x, y: Âçß(\'%s,%s\\t%s\\t%s\' % (i, x, áÍÌ[x], y))))))\n(áÐè := (lambda x: ÅÒ(x, e=MOD(ÂÑÖ, áØÁ=None)()(T=True))))\n(áÐÍ_ := None)\n\ndef áÏñ(s=ÁØã):\n    global áÐÍ_\n    if áÐÍ_ is None:\n        Âçß(\'Starting timer\')\n        (áÐÍ_ := ÐÌü(time))\n        return\n    Âçß(\'%s took %ss\' % (s, ÐÌü(time) - áÐÍ_))\n    (áÐÍ_ := None)\n\n@ÐÌü(fcache)\ndef gram_convert(ÄÕÒü):\n    (name_remaps := ÂÑÖ()(ÄÕåØ(ÂÛê(\'elm_o\\u2009elm_a\\u2009assign_cln\\u2009group_inner\\u2009group\'), \'∨∧←∧∧\')))\n    (TT := (lambda ÄÕÒü: (getattr(ÄÕÒü, \'t\'), *((getattr(ÄÕÒü[0], \'t\'),) if getattr(ÄÕÒü, \'t\') in \'ᔐ~\' else (getattr(ÄÕÒü[0], \'t\'), *Áÿú(ÄÕÒü[slice(1, None)], TT)) if getattr(ÄÕÒü, \'t\') == \'←\' else Áÿú(ÄÕÒü, TT)))))\n    (escape := (lambda x, t=\'ݺ\': getattr(getattr(getattr(x, \'replace\')(2 * \'␛\', t), \'replace\')(\'␛\', ÁØã), \'replace\')(t, \'␛\')))\n\n    def reduce_j(ÄÕÒü):\n        (ÄÊPSH(ÄÕÒü), ((Ïß := ÄÊPKE(0)[0]), (o := ÄÊPKE(0)[1]), (Ïà := ÄÊPKE(0)[2]), *(C := ÄÊPKE(0)[slice(3, None, None)])), ÄÊDEL(1))[1]\n        if C:\n            ÂùÆ(False)\n        if getattr(o, \'t\') == \'↷\':\n            return ÅÒ(\'∧\', Ïß, Ïà, Ïß)\n        elif getattr(o, \'t\') == \'⯆\':\n            return ÅÒ(\'∨\', ÅÒ(\'∧\', Ïà, ÅÒ(\'+\', ÅÒ(\'∧\', Ïß, Ïà))), Ïà)\n        elif getattr(o, \'t\') == \'△\':\n            return ÅÒ(\'∨\', ÅÒ(\'∧\', ÅÒ(\'*\', ÅÒ(\'∧\', Ïß, Ïà)), Ïß), Ïß)\n        elif getattr(o, \'t\') == \'▽\':\n            return ÅÒ(\'∨\', ÅÒ(\'∧\', ÅÒ(\'∧\', Ïà, ÅÒ(\'*\', ÅÒ(\'∧\', Ïß, Ïà)))), ÅÒ(\'✓\'))\n        elif getattr(o, \'t\') == \'⯅\':\n            return ÅÒ(\'∧\', ÅÒ(\'+\', ÅÒ(\'∧\', Ïß, Ïà)), Ïß)\n        ÂùÆ(False)\n\n    def bad(ÄÕÒü):\n        if getattr(ÄÕÒü, \'t\') in ÂÛê(\'comment\\u2009w\\u2009W\'):\n            return True\n        if ((not getattr(ÄÕÒü, \'t\') and ãÊú(ÄÕÒü) == 1) and getattr(getattr(getattr(ÄÕÒü, \'c\')[0], \'e\'), \'T\')) and getattr(getattr(ÄÕÒü, \'c\')[0], \'t\') in \'()∧∨:=\':\n            return True\n\n    def collapse_ao(ÄÕÒü):\n        if getattr(getattr(ÄÕÒü, \'e\'), \'T\'):\n            return ÄÕÒü\n        (ÄÊPSH(ÄÕÒü), ÄÊPSH(\'c\'), ÄÊPSH(getattr(ÄÊPKE(1), ÄÊPKE(0))), ÄÊPSH(MOD(ÂøÑ, áØÁ=ÂÚü())(Áÿú(ÄÊPKE(0), lambda x: getattr(x, \'c\') if (getattr((x := collapse_ao(x)), \'t\') == ÄÊPSH(getattr(ÄÕÒü, \'t\')) and ÄÊPOP() in ÄÊPSH(\'∧∨\')) and (ÄÊDEL(1) or True) or (ÄÊDEL(1) or False) else [x]))), setattr(ÄÊPKE(3), ÄÊPKE(2), ÄÊPKE(0)), ÄÊDEL(4))[4]\n        return ÄÕÒü\n\n    def parse_elm(N):\n        (ÄÊPSH((+N[0], N[1], +N[2])), ((Ïß := ÄÊPKE(0)[0]), (n := ÄÊPKE(0)[1]), (Ïà := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]\n        (ÄÊPSH(MOD(ÐÌÛ, áØÁ=áÍÖ)(Ïß, ÄÊCUR((1,), {}, ÂÔó, ÂýÃ, \'❗⠶ƨ\'))), ((l1 := ÄÊPKE(0)[0]), (l2 := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n        for o in (*l1, *Ïà, *l2):\n            if o == \'~\':\n                (n := ÅÒ(o, áÐè(getattr(re, \'compile\')(+n))))\n            else:\n                (n := ÅÒ(o, n))\n        return n\n    (rules := getattr(getattr(getattr(getattr(getattr(getattr(ÄÕÒü, \'rm\')(bad), \'ftrp\')(ÂÛê(\'prefix\\u2009suffix\'), lambda x: ÅÒ(getattr(x, \'t\'), áÐè(+x))), \'ftrp\')(\'str\', lambda x: ÅÒ(\'ᔐ\', áÐè(escape((+x)[slice(1, -1)])))), \'ftrp\')(name_remaps ** î, lambda x: ÅÒ(name_remaps[getattr(x, \'t\')], *[y for y in x if not getattr(getattr(y, \'e\'), \'T\')]), True), \'flat\')(lambda x: getattr(x, \'t\') == \'_elm_j\'), \'find\')(lambda x: getattr(x, \'t\') == \'assign_eql\'))\n    (rules := ÂÑÖ()(Áÿú(rules, lambda x: (+x[0], x[2]))))\n    for k, ÄÕÒü in rules:\n        (ÄÕÒü := getattr(getattr(getattr(getattr(collapse_ao(getattr(getattr(ÄÕÒü, \'ftrp\')(ÂÛê(\'assign_eql\'), lambda x: x[0], True), \'flat\')(lambda x: getattr(x, \'t\') in ÂÛê(\'∧\\u2009∨\\u2009elm_j\') and ãÊú(x) == 1)), \'ftrp\')(\'elm_j\', reduce_j, True), \'ftrp\')(\'elm\', parse_elm, True), \'ftrp\')(\'←\', lambda x: ÅÒ(getattr(x, \'t\'), áÐè(getattr(x[0][0], \'t\')), *x[slice(1, None)]), True), \'ftrp\')(\'rname\', lambda x: áÐè(\'_\' * (getattr(x[0], \'t\') not in \'✓✗\') + getattr(x[0], \'t\'))))\n        if getattr(ÄÕÒü, \'t\') in \'∧∨\' and ãÊú(ÄÕÒü) == 1:\n            (ÄÕÒü := ÄÕÒü[0])\n        (ÄÊPSH(rules), ÄÊPSH(k), ÄÊPSH(TT(ÄÕÒü)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n    return rules\n\ndef parse(áÌý, áÍÌ, start_rule=None, debug=False):\n    (ÄÊPSH((Áÿú(ÄÝöÊ(ãÊú(áÌý)), lambda x: {}), 0)), ((ÂÑÎ := ÄÊPKE(0)[0]), (Ïõ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n    (áÏð := [(None, ãÊú(áÍÌ) - 1 if start_rule is None else start_rule)])\n    while áÏð:\n        (ÄÊPSH(getattr(áÏð, \'pop\')(-1)), ((ÏÔ := ÄÊPKE(0)[0]), (Ïç := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n        if ÏÔ is not None:\n            (Ïõ := ÏÔ)\n        (ÄÊPSH(áÍÌ[Ïç]), ((Ïá := ÄÊPKE(0)[0]), *(áÌü := ÄÊPKE(0)[slice(1, None, None)])), ÄÊDEL(1))[1]\n        if debug:\n            (V := Âøî(ÁØò(lambda ÂîÓ: áÍÌ[ÂîÓ[1]][0])(áÏð), \' \'))\n            Âçß(\'%s%s%s%s %s %s %s\' % (áÌý[slice(None, Ïõ)], Åøþáüì(\'│\', fg=\'0f0\'), áÌý[Ïõ] if Ïõ < ãÊú(áÌý) else ÁØã, áÌý[slice(Ïõ + 1, None)], V, Åøþáüì(Ïá, \'f5f\'), dotrim(áÓÙþáÓàþáÓç(áÌü), 75)))\n        (áÐñ := ÂÑÎ[Ïõ])\n        if Ïá == \'ᔐ\':\n            if áÌü[0] == áÌý[slice(Ïõ, (áÚù := (Ïõ + ãÊú(áÌü[0]))))]:\n                (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH((True, áÚù)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n            else:\n                (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH((False, Ïõ)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n        elif Ïá == \'~\':\n            if (m := getattr(áÌü[0], \'match\')(áÌý, Ïõ)):\n                (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH((True, getattr(m, \'span\')()[1], m)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n            else:\n                (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH((False, Ïõ)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n        elif Ïá == \'∧\':\n            (ÄÊPSH(áÐñ[Ïç] if Ïç in áÐñ else (0, Ïõ)), ((n := ÄÊPKE(0)[0]), (áÚù := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n            while True:\n                (ÄÊPSH((áÌü[n], ÂÑÎ[áÚù])), ((áÚê := ÄÊPKE(0)[0]), (áÍØ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n                if áÚê not in áÍØ:\n                    getattr(áÏð, \'extend\')([(Ïõ, Ïç), (áÚù, áÚê)])\n                    (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH((n, áÚù)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n                    break\n                (ÄÊPSH(ÂÑÎ[áÚù][áÚê][slice(None, 2)]), ((áÍÜ := ÄÊPKE(0)[0]), (áÚù := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n                (ÄÊPSH(n), ÄÊPSH(ÄÊPKE(0) + 1), (n := ÄÊPKE(0)), ÄÊDEL(2))[2]\n                if not áÍÜ:\n                    (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH((False, Ïõ)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n                    break\n                if n == ãÊú(áÌü):\n                    (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH((True, áÚù)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n                    break\n        elif Ïá == \'∨\':\n            (n := (áÐñ[Ïç] if Ïç in áÐñ else 0))\n            while True:\n                (ÄÊPSH((áÌü[n], ÂÑÎ[Ïõ])), ((áÚê := ÄÊPKE(0)[0]), (áÍØ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n                if áÚê not in áÍØ:\n                    getattr(áÏð, \'extend\')([(Ïõ, Ïç), (Ïõ, áÚê)])\n                    (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH(n), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n                    break\n                (ÄÊPSH(ÂÑÎ[Ïõ][áÚê][slice(None, 2)]), ((áÍÜ := ÄÊPKE(0)[0]), (áÚù := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n                if áÍÜ:\n                    (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH((True, áÚù, n)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n                    break\n                (ÄÊPSH(n), ÄÊPSH(ÄÊPKE(0) + 1), (n := ÄÊPKE(0)), ÄÊDEL(2))[2]\n                if n == ãÊú(áÌü):\n                    (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH((False, Ïõ)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n                    break\n        elif Ïá == \'*\' or \'+\' == Ïá:\n            if Ïç in áÐñ:\n                (c := áÐñ[Ïç])\n            else:\n                (c := (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH([Ïõ]), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3])\n            (ÄÊPSH((áÌü[0], c[-1])), ((áÚê := ÄÊPKE(0)[0]), (áÚù := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n            while True:\n                (áÍØ := ÂÑÎ[áÚù])\n                if áÚê not in áÍØ:\n                    getattr(áÏð, \'extend\')([(Ïõ, Ïç), (áÚù, áÚê)])\n                    break\n                (ÄÊPSH(áÍØ[áÚê][slice(None, 2)]), ((áÍÜ := ÄÊPKE(0)[0]), (ÏÔ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n                if not áÍÜ:\n                    if Ïá == \'*\' or ãÊú(c) > 1:\n                        (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH((True, áÚù, c[slice(None, -1)])), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n                    else:\n                        (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH((False, Ïõ)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n                    break\n                getattr(c, \'append\')((áÚù := ÏÔ))\n        elif Ïá == \'✓\':\n            (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH((True, Ïõ)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n        elif Ïá == \'←\':\n            if áÌü[1] not in áÐñ:\n                getattr(áÏð, \'extend\')([(Ïõ, Ïç), (Ïõ, áÌü[1])])\n            else:\n                (ÄÊPSH(áÐñ[áÌü[1]][slice(None, 2)]), ((áÍÜ := ÄÊPKE(0)[0]), (áÚù := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n                (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH((áÍÜ, áÚù, áÌü[1])), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n        elif áÌü[0] not in áÐñ:\n            getattr(áÏð, \'extend\')([(Ïõ, Ïç), (Ïõ, áÌü[0])])\n        else:\n            (ÄÊPSH(áÐñ[áÌü[0]][slice(None, 2)]), ((áÍÜ := ÄÊPKE(0)[0]), (áÚù := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n            if Ïá == \'?\':\n                (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH((True, áÚù, áÍÜ)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n            elif Ïá == \'¬\':\n                (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH((not áÍÜ, Ïõ)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n            elif Ïá == \'⮞\':\n                (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH((áÍÜ, Ïõ)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n            elif Ïá == \'❗\':\n                ÂùÆ(áÍÜ)\n                (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH((áÍÜ, áÚù)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n            elif Ïá == \'✗\':\n                ÂùÆ(False, \'Hit an ✗\')\n            else:\n                (ÄÊPSH(áÐñ), ÄÊPSH(Ïç), ÄÊPSH((áÍÜ, áÚù)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n    return ÂÑÎ\n\ndef make_rules(r):\n    (Æå := (lambda ÂîÓ: áÍé(Áÿú(ÂîÓ, Æå)) if ÁØö(ÂîÓ, áÍá | áÍé) else ÂîÓ))\n    (nmp := ÂÞÅCAT(ÄÕåØ(r ** î, ÂÿÇ(r)), ÂÑÖ()))\n    (ÄÊPSH(r), ÄÊPSH(MOD(ËãÂ, áØÁ=ë)(ÄÊPKE(0), CUR(lambda ÂîÓ, ÂîÒ: (\'_\' + ÂîÓ, Æå(ÂîÒ))))), (r := ÄÊPKE(0)), ÄÊDEL(2))[2]\n    (áÌÆ := ÂÑÖ()(ÄÕåØ(r ** î, (áÌÕ := Áÿú(r ** î, MOD(Âêà, áØÁ=áÍé))))))\n\n    def áÑÞ(r):\n        if ãÊú(r) == 1 and r[0][0] == \'_\':\n            return (r[0],)\n        if r in áÌÆ:\n            return áÌÆ[r]\n        if ÁØö(r[0], áÍÞ):\n            (r := (áÌÕ[(áÐø := r[0])][0], *r[slice(1, None)]))\n        else:\n            getattr(áÌÕ, \'append\')((áÐø := ãÊú(áÌÕ)))\n        if r[0] == \'←\':\n            (r := (r[0], r[1], áÑÞ(r[2])))\n        elif r[0] in \'✓✗\':\n            (r := (r[0], áÐø))\n        elif r[0] not in \'ᔐ~\':\n            (r := (r[0], *Áÿú(r[slice(1, None)], áÑÞ)))\n        return ÂåÔ((ÄÊPSH(áÌÕ), ÄÊPSH((ÄÊPSH(áÌÆ), ÄÊPSH(r), ÄÊPSH(áÐø), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]), ÄÊPSH(r), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3], áÐø)\n    áÑÞ((\'T_root\', *Áÿú(ÄÕåØ(nmp ** ì, r ** ì), áÍé)))\n    (ÄÊPSH(áÌÕ), ÄÊPSH(Áÿú(ÄÊPKE(0), lambda x: (x[0], *Áÿú(x[slice(1, None)], lambda ÂîÓ: ÂîÓ if ÄÝøÇ(ÂîÓ, áÍé) else MOD(ÄÔÞÔ, ÁÜñ=ÄÕøü)(r ** î, ÄÊCUR((1,), {}, ÂÖÑ, ÂýÃ, ÂîÓ[0])))))), (áÌÕ := ÄÊPKE(0)), ÄÊDEL(2))[2]\n    return MOD(ÂÑÖ, áØÁ=áÌÕ)() | nmp\n\ndef parse_to_tree(áÍÌ, ÂÑÎ, Ïõ, Ïç, show_table=False, raise_failed=True):\n    (rec := (lambda *áÑË: parse_to_tree(áÍÌ, ÂÑÎ, *áÑË, raise_failed=raise_failed)))\n    (ÄÊPSH(áÍÌ[Ïç]), ((Ïá := ÄÊPKE(0)[0]), *(C := ÄÊPKE(0)[slice(1, None, None)])), ÄÊDEL(1))[1]\n    if Ïç not in (áÐñ := ÂÑÎ[Ïõ]):\n        return (Ïá, \'‼∄‼\')\n    (ÄÊPSH(áÐñ[Ïç]), ((áÍÜ := ÄÊPKE(0)[0]), (áÚù := ÄÊPKE(0)[1]), *(áÌú := ÄÊPKE(0)[slice(2, None, None)])), ÄÊDEL(1))[1]\n    if raise_failed:\n        ÂùÆ(áÍÜ, \'Failed to parse tree!\')\n    if Ïá == \'∧\':\n        (o := [])\n        for r in C:\n            getattr(o, \'append\')(rec(Ïõ, r))\n            if r not in (áÐñ := ÂÑÎ[Ïõ]):\n                break\n            (Ïõ := áÐñ[r][1])\n        return (Ïá, *o)\n    if Ïá == \'ᔐ\':\n        return (Ïá, C[0])\n    if Ïá == \'?\':\n        return (Ïá, *(áÌú and (áÌú[0] and MOD(Âêà, áØÁ=áÍé)(rec(Ïõ, C[0]))) or ()))\n    if not áÌú and Ïá in {*\'∨*+~←\'}:\n        return (Ïá, \'‼∅‼\')\n    if Ïá == \'~\':\n        return (Ïá, getattr(áÌú[0], \'group\')(0))\n    if Ïá == \'∨\':\n        return (Ïá, rec(Ïõ, C[áÌú[0]]))\n    if Ïá == \'←\':\n        return (Ïá, C[0], rec(Ïõ, áÌú[0]))\n    if Ïá in {*\'*+\'}:\n        return (Ïá, *[rec(x, C[0]) for x in áÌú[0]])\n    if Ïá in {*\'✓✗⮞¬\'}:\n        return (Ïá,)\n    return (getattr(Ïá, \'removeprefix\')(\'_\'), rec(Ïõ, C[0]))\n\ndef chop_tree(ÄÕÒü, áÌý, remove_trashes=True, remove_failed_questions=True, remove_lookaheads=True, include_positions=True, track_length=True, DEBUG=False):\n    (ÂÐñ := (áÏñ if DEBUG else ÃÆì))\n    (pops := {*\'∧∨*+❗⠶?\'})\n    (removes := {*\'\\U000f01b4\' * remove_trashes + \'⮞¬\' * remove_lookaheads})\n\n    def reform_str(ÄÕÒü):\n        if getattr(ÄÕÒü, \'t\') in {\'ᔐ\', \'~\'}:\n            (ÄÊPSH(ÄÕÒü), ÄÊPSH(\'t\'), ÄÊPSH(ÄÕÒü), ÄÊPSH(\'c\'), ÄÊPSH(getattr(ÄÕÒü, \'e\')), ÄÊPSH(\'T\'), ÄÊPSH((getattr(getattr(ÄÕÒü, \'c\')[0], \'t\'), [], True)), (setattr(ÄÊPKE(6), ÄÊPKE(5), ÄÊPKE(0)[0]), setattr(ÄÊPKE(4), ÄÊPKE(3), ÄÊPKE(0)[1]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)[2])), ÄÊDEL(7))[7]\n        else:\n            for c in ÄÕÒü:\n                reform_str(c)\n        return ÄÕÒü\n    ÐÌü(ÂÐñ)\n    reform_str(ÄÕÒü)\n    ÂÐñ(\'Reform_str\')\n    if include_positions:\n        ÂÕÅ((Æå := (lambda ÄÕÒü, i=0: (ÄÊPSH(getattr(ÄÕÒü, \'e\')), ÄÊPSH(\'p\'), ÄÊPSH((i, MOD(Áëý, áØÁ=getattr(getattr(ÄÕÒü, \'e\'), \'T\'))(ÄÕÒü, (ÄÊCUR((1,), {\'áØÁ\': i}, ÆÑ, ÂýÃ, ÂÕì(Æå)), lambda ÂîÓ: ãÊú(+ÂîÓ) + i)))), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3][1])), ÄÕÒü)\n    (parsed_len := (ãÊú(+ÄÕÒü) if track_length else None))\n\n    def Æå(ÄÕÒü):\n        if getattr(getattr(ÄÕÒü, \'e\'), \'T\'):\n            return True\n        if getattr(ÄÕÒü, \'t\') in removes:\n            return\n        if remove_failed_questions and getattr(ÄÕÒü, \'t\') == \'?\':\n            if not getattr(ÄÕÒü, \'c\'):\n                return\n            (ÄÊPSH(ÄÕÒü), ÄÊPSH(\'c\'), ÄÊPSH([*filter(Æå, getattr(ÄÕÒü, \'c\'))]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n            if not getattr(ÄÕÒü, \'c\'):\n                return\n            return True\n        (ÄÊPSH(ÄÕÒü), ÄÊPSH(\'c\'), ÄÊPSH([*filter(Æå, getattr(ÄÕÒü, \'c\'))]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n        return True\n    ÐÌü(ÂÐñ)\n    Æå(ÄÕÒü)\n    ÂÐñ(\'Removes\')\n\n    def splat(ÄÕÒü):\n        (C := [])\n        for c in ÄÕÒü:\n            if getattr(getattr(c, \'e\'), \'T\'):\n                getattr(C, \'append\')(c)\n                continue\n            (v := splat(c))\n            if isinstance(v, áÍá):\n                getattr(C, \'extend\')(v)\n            elif getattr(c, \'t\') in pops:\n                if getattr(c, \'t\') == \'⠶\':\n                    for l in c:\n                        getattr(C, \'extend\')(getattr(l, \'c\'))\n                else:\n                    getattr(C, \'extend\')(getattr(c, \'c\'))\n            else:\n                getattr(C, \'append\')(c)\n        (ÄÊPSH(ÄÕÒü), ÄÊPSH(\'c\'), ÄÊPSH(C), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n    ÐÌü(ÂÐñ)\n    splat(ÄÕÒü)\n    ÂÐñ(\'Splats\')\n\n    def get_txt(ÄÕÒü):\n        if getattr(ÄÕÒü, \'t\') == \'ƨ\':\n            (l := \'\')\n\n            def Æå(ÄÕÒü):\n                nonlocal l\n                if getattr(getattr(ÄÕÒü, \'e\'), \'T\'):\n                    return (ÄÊPSH(l), ÄÊPSH(ÄÊPKE(0) + getattr(ÄÕÒü, \'t\')), (l := ÄÊPKE(0)), ÄÊDEL(2))[2]\n                for c in ÄÕÒü:\n                    Æå(c)\n            Æå(ÄÕÒü)\n            (e := ÂÑÖ()(T=True))\n            if include_positions:\n                (ÄÊPSH(ÐÌü(getattr(ÄÕÒü, \'farnodes\'))), ((Ïß := ÄÊPKE(0)[0]), (Ïà := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n                (ÄÊPSH(e), ÄÊPSH(\'p\'), ÄÊPSH((getattr(getattr(Ïß, \'e\'), \'p\')[0], getattr(getattr(Ïà, \'e\'), \'p\')[-1])), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n            (ÄÊPSH(ÄÕÒü), ÄÊPSH(\'t\'), ÄÊPSH(ÄÕÒü), ÄÊPSH(\'c\'), ÄÊPSH(ÄÕÒü), ÄÊPSH(\'e\'), ÄÊPSH((l, [], e)), (setattr(ÄÊPKE(6), ÄÊPKE(5), ÄÊPKE(0)[0]), setattr(ÄÊPKE(4), ÄÊPKE(3), ÄÊPKE(0)[1]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)[2])), ÄÊDEL(7))[7]\n            return\n        for c in ÄÕÒü:\n            get_txt(c)\n    ÐÌü(ÂÐñ)\n    get_txt(ÄÕÒü)\n    ÂÐñ(\'Get_txt\')\n\n    def set_arrows(ÄÕÒü):\n        if getattr(getattr(ÄÕÒü, \'e\'), \'T\'):\n            return\n        for i, c in enumerate(ÄÕÒü):\n            if getattr(getattr(c, \'e\'), \'T\'):\n                continue\n            if getattr(c, \'t\') == \'←\':\n                (ÄÊPSH(getattr(ÄÕÒü, \'e\')), ÄÊPSH(getattr(c[0], \'t\')), ÄÊPSH((ÄÊPSH(ÄÕÒü), ÄÊPSH(i), ÄÊPSH(c[1]), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n            set_arrows(c)\n    ÐÌü(ÂÐñ)\n    set_arrows(ÄÕÒü)\n    ÂÐñ(\'Set arrows\')\n    if parsed_len is not None:\n        (ÄÊPSH(getattr(ÄÕÒü, \'e\')), ÄÊPSH(\'parse_len\'), ÄÊPSH(getattr(ÄÕÒü, \'e\')), ÄÊPSH(\'input_len\'), ÄÊPSH((parsed_len, ãÊú(áÌý))), (setattr(ÄÊPKE(4), ÄÊPKE(3), ÄÊPKE(0)[0]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)[1])), ÄÊDEL(5))[5]\n    return ÄÕÒü\n\ndef parse_to_node(ÄÕÒü):\n\n    def Æå(x, *áÑË):\n        return ÅÒ(x, *[Æå(*(x if isinstance(x, áÍé) else (x,))) for x in áÑË])\n    return Æå(*ÄÕÒü)\n\n@ÐÌü(fcache)\ndef peggle2_call(R, content, rule=\'main\', DEBUG=False, chop=True, **áÏè):\n    (ÄÊPSH((content, rule)), ((c := ÄÊPKE(0)[0]), (r := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n    (ÄÊPSH((getattr(R, \'T_root\'), R[r])), ((root := ÄÊPKE(0)[0]), (rule := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n    (ÂÐñ := (áÏñ if DEBUG else ÃÆì))\n    ÐÌü(ÂÐñ)\n    (ÂÑÎ := parse(c, root, rule, debug=DEBUG))\n    ÂÐñ(\'Parse\')\n    ÐÌü(ÂÐñ)\n    (ÄÕÒü := parse_to_tree(root, ÂÑÎ, 0, rule))\n    ÂÐñ(\'Convert\')\n    ÐÌü(ÂÐñ)\n    (ÄÕÒü := parse_to_node(ÄÕÒü))\n    ÂÐñ(\'Nodeing\')\n    (áÏÅ := (lambda **áÑÕ: chop_tree(ÄÕÒü, c, DEBUG=DEBUG, **áÏè | áÑÕ)))\n    return ÐÌü(áÏÅ) if chop else ÂÑÖ()(table=ÂÑÎ, tree=ÄÕÒü, chop=áÏÅ)\n\nclass peggle2:\n    (__slots__ := ÂÛê(\'rules\\u2009R\'))\n\n    def __init__(áÑÞ, g):\n        if ÁØö(g, ÁÜÙ):\n            (g := FROM_GRAM(g))\n        (ÄÊPSH(áÑÞ), ÄÊPSH(\'rules\'), ÄÊPSH(áÑÞ), ÄÊPSH(\'R\'), ÄÊPSH([getattr(g, \'rules\'), getattr(g, \'R\')] if ÁØö(g, peggle2) else [g, make_rules(g)]), (setattr(ÄÊPKE(4), ÄÊPKE(3), ÄÊPKE(0)[0]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)[1])), ÄÊDEL(5))[5]\n\n    def __repr__(áÑÞ):\n        return \'%s[%s Rules, %s Normalized]\' % (getattr(ÁØö(áÑÞ), \'__name__\'), ãÊú(getattr(áÑÞ, \'rules\')), ãÊú(getattr(getattr(áÑÞ, \'R\'), \'T_root\')))\n\n    def __contains__(áÑÞ, x):\n        return x in getattr(áÑÞ, \'rules\')\n\n    def __or__(áÑÞ, h, allow_conflict=False):\n        if ÁØö(h, áÑÞ):\n            (h := getattr(h, \'rules\'))\n        (conflict := ÂÕÖ(ÐÌü(getattr(getattr(áÑÞ, \'rules\'), \'keys\')), ÐÌü(getattr(h, \'keys\'))))\n        ÂùÆ(not (allow_conflict and conflict), \'Conflicting rules! %s\' % (conflict,))\n        return ÁØö(áÑÞ)(peggle2(getattr(áÑÞ, \'rules\') | h))\n\n    def __call__(áÑÞ, *áÑË, **áÑÕ):\n        return peggle2_call(getattr(áÑÞ, \'R\'), *áÑË, **áÑÕ)\n\n    def print_rules(áÑÞ):\n        ËãÂ(ÐÌü(getattr(getattr(áÑÞ, \'rules\'), \'items\')), lambda x, y: (Âçß(\'%s:\' % (x,)), Âçß(y)))\n\n    def print_normalized(áÑÞ):\n        ËãÂ(ÂÓÏ(getattr(getattr(áÑÞ, \'R\'), \'T_root\')), lambda x, y: Âçß(\'%s\\t%s\' % (x, Âøî(Áÿú(y, ÁÜÙ), \' \'))))\n(áÌÕ := Áÿú([\'[\\ueb26#][^\\n]*\', \'[⯅⯆△▽↷]\', \'"([^"␛]|␛.)*"\', "\'([^\'␛]|␛.)*\'", \'‹([^›␛]|␛.)*›\', \'[^⯅⯆△▽↷\\U000f01b4()?❗⮞.:⠶ƨ✗+*=¬∨∧~#\\ueb26‹\\\'" \\t\\n␛]+|✗\', \'[\\U000f01b4❗⮞⠶ƨ~¬]\', \'[*+?]\', \'([ \\t]|[\\\\\\\\␛]\\n)+\', \'([ \\t\\n]|[\\\\\\\\␛]\\n)+\'], getattr(re, \'compile\')))\n(GRANDMA_RULES := ÂÑÖ()({\'statements\': [\'∧\', (\'?\', [\'_W\']), (\'*\', [\'∧\', (\'∨\', [\'_comment\'], [\'_elm_o\']), (\'?\', [\'_W\'])])], \'comment\': [\'~\', áÌÕ[0]], \'elm_o\': [\'∧\', [\'_elm_a\'], (\'*\', [\'∧\', (\'?\', [\'_W\']), (\'ᔐ\', \'∨\'), (\'?\', [\'_W\']), [\'_elm_a\']])], \'elm_a\': [\'∧\', [\'_elm_j\'], (\'*\', [\'∧\', (\'∨\', [\'∧\', (\'?\', [\'_W\']), (\'ᔐ\', \'∧\'), (\'?\', [\'_W\'])], [\'?\', [\'_w\']]), [\'_elm_j\']])], \'elm_j\': [\'∨\', [\'__elm_j\'], [\'_elm\']], \'_elm_j\': [\'∧\', [\'_elm\'], (\'?\', [\'_W\']), (\'~\', áÌÕ[1]), (\'?\', [\'_W\']), (\'∨\', [\'__elm_j\'], [\'_elm\'])], \'elm\': [\'∧\', [\'_prefix\'], (\'∨\', [\'_assign_eql\'], [\'_assign_cln\'], [\'_group\'], [\'_str\'], [\'_rname\']), [\'_suffix\']], \'assign_eql\': [\'∧\', [\'_rname\'], (\'?\', [\'_W\']), (\'ᔐ\', \'=\'), (\'?\', [\'_W\']), [\'_elm_o\']], \'assign_cln\': [\'∧\', [\'_rname\'], (\'?\', [\'_W\']), (\'ᔐ\', \':\'), (\'?\', [\'_W\']), [\'_elm_j\']], \'group\': [\'∧\', (\'ᔐ\', \'(\'), (\'?\', [\'_W\']), [\'_group_inner\'], (\'ᔐ\', \')\')], \'group_inner\': [\'*\', (\'∧\', [\'_elm_o\'], [\'?\', [\'_W\']])], \'str1\': [\'~\', áÌÕ[2]], \'str2\': [\'~\', áÌÕ[3]], \'str3\': [\'~\', áÌÕ[4]], \'str\': [\'∨\', [\'_str1\'], [\'_str2\'], [\'_str3\']], \'rname\': [\'~\', áÌÕ[5]], \'prefix\': [\'∨\', (\'∧\', [\'?\', [\'_w\']], [\'+\', (\'∧\', [\'~\', áÌÕ[6]], [\'?\', [\'_W\']])]), (\'?\', [\'_w\'])], \'suffix\': [\'∨\', (\'∧\', [\'+\', (\'∧\', [\'?\', [\'_W\']], [\'~\', áÌÕ[7]])], [\'?\', [\'_w\']]), (\'?\', [\'_w\'])], \'w\': [\'~\', áÌÕ[8]], \'W\': [\'~\', áÌÕ[9]]}))\n(BOOTSTRAP := peggle2(GRANDMA_RULES))\n(FROM_GRAM := (lambda x: peggle2(gram_convert(BOOTSTRAP(x, \'statements\')))))\n__ÄÊADD_EXPORTS__(globals(), (\'peggle2\', peggle2))\n\ndef test_peggle2():\n    (GRAM := \'\\n                  main    = \\U000f01b4W? (entry \\U000f01b4W?)*\\n                  entry   = (\\n                      ƨ(section=\\U000f01b4\\\'[\\\' wrd \\U000f01b4\\\']\\\') \\U000f01b4W?\\n                      (pair = (\\n                          (bruh:key = ⠶wrd) \\U000f01b4(w? ↷ \\\'=\\\')\\n                          (value = (wrd ∨ str)+) \\U000f01b4W? ) )* )\\n                  str     = ~‹"[^"]+"›\\n                  wrd     = ~‹[-\\\\w]+›\\n                  w       = ~‹[ \\\\t]+›\\n                  W       = ~‹[ \\\\t\\\\n]+›\\n                  \')\n    (CONTENT := \'\\n                  [section1]\\n                  somekey = somevalue\\n                  someotherkey=someothervalue\\n                  [duawhdiawi]x=y\\n                  somekey =                 somevalue\\n                  someotherkey=✓□awhdapi\\n                  \')\n    (RULE := \'main\')\n    (gram := Âçß(peggle2(GRAM)))\n    (ÄÕÒü := gram(CONTENT, RULE))\n    ÐÌü(getattr(ÄÕÒü, \'P\'))',__:=globals().copy())
for k,v in __.get("__EXPORTS__",{}).items():globals()[k]=v


# /home/ganer/Projects/Moon_BETA/Libraries/peggle2/rgx_golfatron.☾⟶/tmp/γ/_QECnRSQGBfkJDMistBA-QAE5zfpBkKGNvODMaXvHHM.py
exec("\n__file__='/home/ganer/Projects/Moon_BETA/Libraries/peggle2/rgx_golfatron.☾'\n(fcache := (lambda: lambda Æå: Æå))\nfrom functools import cache\n(ÄÊPSH(('\\n\\\\^$.|?*+()[]{}', '\\\\]-')), ((ch1 := ÄÊPKE(0)[0]), (ch2 := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n(ST := 1113936)\n(CF := ((CT := ÂÑÖ()(ËãÂ(ÂÓÏ(ÁãÁ(ch1 + ch2)), ÂÕì(CUR(lambda ÂîÓ, ÂîÒ: [ÂîÓ, ÄÝöí(ST + ÂîÒ)]))))) ** ÂÕì))\n(IF := ((IT := ÂÑÖ()(ËãÂ(ÂÓÏ(ÁãÁ(ch1 + ch2)), ÂÕì(CUR(lambda ÂîÓ, ÂîÒ: [ÂîÓ, ÄÝöí(ãÊú(CF) + ST + ÂîÒ)]))))) ** ÂÕì))\n(OF := ((OT := ÂÑÖ()(ËãÂ(ÂÓÏ(ÁãÁ(ch1)), ÂÕì(CUR(lambda ÂîÓ, ÂîÒ: [ÂîÓ, ÄÝöí(ãÊú(IF) + ãÊú(CF) + ST + ÂîÒ)]))))) ** ÂÕì))\n(ÄÊPSH(ÁØò(lambda ÂîÓ: MOD(ËãÂ, áØÁ=î)(ÂîÓ, lambda x, y: ÄÝöí(x)))([CT, IT, OT])), ((CT := ÄÊPKE(0)[0]), (IT := ÄÊPKE(0)[1]), (OT := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]\n(ÄÊPSH(ÁØò(lambda ÂîÓ: MOD(ËãÂ, áØÁ=î)(ÂîÓ, lambda x, y: ÄÝöí(x)))([CF, IF, OF])), ((CF := ÄÊPKE(0)[0]), (IF := ÄÊPKE(0)[1]), (OF := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]\nÁØò(lambda ÂîÓ: (ÄÊPSH(IF), ÄÊPSH(ÄÝöí(IT[ÄÝöí(ÂîÓ)])), ÄÊPSH('\\\\' + ÂîÓ), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3])(ch2)\n(OF := MOD(ËãÂ, áØÁ=ì)(OF, lambda x, y: '\\\\' + y))\n(DASH := CT[ÄÝöí('-')])\n(ÄÊPSH((CT[ÄÝöí('[')], CT[ÄÝöí(']')])), ((BL := ÄÊPKE(0)[0]), (BR := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n(ÄÊPSH((CT[ÄÝöí('(')], CT[ÄÝöí(')')])), ((PL := ÄÊPKE(0)[0]), (PR := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n(ÄÊPSH((CT[ÄÝöí('?')], CT[ÄÝöí('|')])), ((Q := ÄÊPKE(0)[0]), (BAR := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n\ndef rgx_rans(x):\n    (ÄÊPSH(x), ÄÊPSH(ÄÔàÑ(ÄÊPKE(0), (áÚâ := (lambda x: ord(x[0]))))), (x := ÄÊPKE(0)), ÄÊDEL(2))[2]\n    (r := [])\n    for ÂîÓ in MOD(Ááú, áØÁ='!')(x):\n        (h := Áÿú(ÂîÓ, áÚâ))\n        getattr(r, 'append')(DASH if h[0] + h[1] + h[2] == ÂÞÅCAT(3, h[0]) + 3 else ÂîÓ[1])\n    return getattr(ÆÑ(r, lambda x, y: x + y * (y[-1] != x[-1])), 'translate')(IT)\n\n@ÐÌü(fcache)\ndef rgx_golfatron(áÑã):\n\n    @cache\n    def áüì(x):\n        (ÄÊPSH(MOD(ÐÌÛ, áØÁ=áÍÖ)(x)), ((t := ÄÊPKE(0)[0]), (Ïõ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n        return ËãÂ(ÂÑÖ()(ÐÌÛ(Ïõ, lambda x: x[0])), lambda x, y: (x, áüì((H := áÍé(Áÿú(y, lambda x: x[slice(1, None)])))), 1 if ÁØã in H and ÂØõ(H) else 0))\n\n    def ÐÉ(x):\n        (ÄÊPSH(MOD(ÐÌÛ, áØÁ=áÍÖ)(x, lambda x: len(x) != 1)), ((s := ÄÊPKE(0)[0]), (m := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n        (ÄÊPSH(m), ÄÊPSH(Áÿú(ÄÊPKE(0), lambda x: getattr(ÁØã, 'join')(getattr(x, 'translate')(OT)))), (m := ÄÊPKE(0)), ÄÊDEL(2))[2]\n        if (s := getattr(ÁØã, 'join')(s)):\n            getattr(m, 'append')(getattr(s, 'translate')(OT) if ãÊú(s) == 1 else BL + rgx_rans(s) + BR)\n        return m\n\n    def Åø(x):\n        (ÄÊPSH(x), ((Ïß := ÄÊPKE(0)[0]), (Ïà := ÄÊPKE(0)[1]), (Ïá := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]\n        (r := Ïß)\n        if Ïà and (Ïà := ÐÉ(Áÿú(Ïà, Åø))):\n            (h := getattr(BAR, 'join')(Ïà))\n            if Ïß and ãÊú(Ïà) > 1:\n                (h := (PL + h + PR))\n            (ÄÊPSH(r), ÄÊPSH(ÄÊPKE(0) + h), (r := ÄÊPKE(0)), ÄÊDEL(2))[2]\n        return r + Q if Ïá and Ïß else r\n    (áÑã := áüì(áÍé(sorted(áÑã, key=lambda x: (-ãÊú(x), x)))))\n    return getattr(getattr(getattr(Åø((ÁØã, áÑã, False)), 'translate')(CF), 'translate')(IF), 'translate')(OF)\n__ÄÊADD_EXPORTS__(globals(), ('rgx_golfatron', rgx_golfatron))",__:=globals().copy())
for k,v in __.get("__EXPORTS__",{}).items():globals()[k]=v


# /home/ganer/Projects/Moon_BETA/Libraries/peggle2/gram_tools.☾⟶/tmp/γ/9G2fTxEORVIac9Kv9SPjkVHMCPDjPny3anYUHDhggKw.py
exec('\n__file__=\'/home/ganer/Projects/Moon_BETA/Libraries/peggle2/gram_tools.☾\'\n__ÄÊIMPORT__(\'𝐍\', globals())\n__ÄÊIMPORT__(\'peggle2$$main\', globals())\n__ÄÊIMPORT__(\'peggle2$$rgx_golfatron\', globals())\n__ÄÊIMPORT__(\'text_format\', globals())\n(nrm := (lambda ÄÕÒü: áÐè(ÄÕÒü) if ÁØö(ÄÕÒü, ÁÜÙ | ÂÑÅ) else ÄÕÒü))\n\ndef Âîë(ÄÕÒü, áÎÜ):\n    (ÄÕÒü := nrm(ÄÕÒü))\n    if ÁØö(áÎÜ, ÁÜÙ):\n        return ÄÕÒü\n    if ÄÝøÇ(áÎÜ, ÅÒ):\n        (áÎÜ := áÎÜ[0])\n    if \'p\' not in getattr(áÎÜ, \'e\'):\n        return ÄÕÒü\n    (ÄÊPSH(getattr(ÄÕÒü, \'e\')), ÄÊPSH(\'p\'), ÄÊPSH(getattr(getattr(áÎÜ, \'e\'), \'p\')[slice(None, 2)] * 2), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n    return ÄÕÒü\n\ndef Âîì(ÄÕÒü, áÎÜ):\n    (ÄÕÒü := nrm(ÄÕÒü))\n    if ÁØö(áÎÜ, ÁÜÙ):\n        return ÄÕÒü\n    if ÄÝøÇ(áÎÜ, ÅÒ):\n        (áÎÜ := áÎÜ[-1])\n    if \'p\' not in getattr(áÎÜ, \'e\'):\n        return ÄÕÒü\n    (ÄÊPSH(getattr(ÄÕÒü, \'e\')), ÄÊPSH(\'p\'), ÄÊPSH(getattr(getattr(áÎÜ, \'e\'), \'p\')[slice(2, None)] * 2), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n    return ÄÕÒü\n\ndef ÂØÙ(ÄÕÒü, áÎÜ):\n    (ÄÕÒü := nrm(ÄÕÒü))\n    if ÁØö(áÎÜ, ÁÜÙ) or ÄÝøÇ(áÎÜ, áÓö):\n        return ÄÕÒü\n    if ÄÝøÇ(áÎÜ, ÅÒ):\n        (áÎÜ := ÅÒ(ÁØã, *áÎÜ))\n    (ÄÊPSH(getattr(áÎÜ, \'first_sides\')(lambda ÂîÓ: ÂÔö(getattr(ÂîÓ, \'e\'), \'p\'))), ((l := ÄÊPKE(0)[0]), (r := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n    if l is None:\n        return ÄÕÒü\n    (ÄÊPSH(getattr(ÄÕÒü, \'e\')), ÄÊPSH(\'p\'), ÄÊPSH((*getattr(getattr(l, \'e\'), \'p\')[slice(None, 2)], *getattr(getattr(r, \'e\'), \'p\')[slice(2, None)])), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n    return ÄÕÒü\n\ndef ÂØØ(ÄÕÒü, áÎÜ):\n    (ÄÕÒü := nrm(ÄÕÒü))\n    (ÄÊPSH(getattr(ÄÕÒü, \'e\')), ÄÊPSH(\'p\'), ÄÊPSH((*getattr(getattr(áÎÜ[0], \'e\'), \'p\')[slice(2, None)], *getattr(getattr(áÎÜ[-1], \'e\'), \'p\')[slice(None, 2)])), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n    return ÄÕÒü\n\ndef áÍô(ÄÕÒü, áÎÜ):\n    (ÄÕÒü := nrm(ÄÕÒü))\n    if ÁØö(áÎÜ, ÁÜÙ):\n        return ÄÕÒü\n    (ÄÊPSH(ÄÕÒü), ÄÊPSH(\'e\'), ÄÊPSH(ÐÌü(getattr(getattr(áÎÜ, \'e\'), \'copy\'))), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n    return ÄÕÒü\n(áÎô := (lambda x, *áÑË, **áÑÕ: MOD(ÄÕéý, áØÁ=ÂØÙ)(ÅÒ(x, *áÑË, **áÑÕ), áÑË)))\n(áÐè := (lambda x, **áÑÕ: MOD(ÄÕéý, áØÁ=ÂØÙ)(ÅÒ(+x if ÁØö(x, ÅÒ) else ÁÜÙ(x), e=ÂÑÖ()(T=True, **getattr(áÑÕ, \'get\')(\'e\', {}))), x)))\n\ndef offset_áÖï(ÄÕÒü, áÖý):\n    if \'p\' in getattr(ÄÕÒü, \'e\'):\n        (ÄÊPSH(getattr(ÄÕÒü, \'e\')), ÄÊPSH(\'p\'), ÄÊPSH((getattr(getattr(ÄÕÒü, \'e\'), \'p\')[0] + áÖý, getattr(getattr(ÄÕÒü, \'e\'), \'p\')[1] + áÖý)), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n    for c in ÄÕÒü:\n        offset_áÖï(c, áÖý)\n    return ÄÕÒü\n\ndef offset_áÖùþáÖï(ÄÕÒü, áÖý):\n    if \'p\' in getattr(ÄÕÒü, \'e\'):\n        (áÖî := getattr(getattr(ÄÕÒü, \'e\'), \'p\'))\n        (ÄÊPSH(getattr(ÄÕÒü, \'e\')), ÄÊPSH(\'p\'), ÄÊPSH((áÖî[0] + áÖý[0], áÖî[1] if áÖî[0] else áÖî[1] + áÖý[1], áÖî[2] + áÖý[0], áÖî[3] if áÖî[2] else áÖî[3] + áÖý[1])), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n    for c in ÄÕÒü:\n        offset_áÖùþáÖï(c, áÖý)\n    return ÄÕÒü\n\ndef reform_positions(ÄÕÒü, áÖï):\n    (áÖß := (lambda ÂîÓ: ÄÕåØ(MOD(ÐÌ, áØÁ=0)(ÂîÓ, CUR(lambda ÂîÓ, ÂîÒ: ÂîÓ + 1 + ÂîÒ)), ÂîÓ))(Áÿú(lines(áÖï), ãÊú)))\n    (s := 0)\n\n    def Æå(ÄÕÒü):\n        nonlocal s\n        while áÖß[s][0] + áÖß[s][1] < getattr(getattr(ÄÕÒü, \'e\'), \'p\')[0]:\n            (ÄÊPSH(s), ÄÊPSH(ÄÊPKE(0) + 1), (s := ÄÊPKE(0)), ÄÊDEL(2))[2]\n        for i, x in enumerate(áÖß[slice(s, None)]):\n            if x[0] + x[1] >= getattr(getattr(ÄÕÒü, \'e\'), \'p\')[1]:\n                (ÄÊPSH(getattr(ÄÕÒü, \'e\')), ÄÊPSH(\'p\'), ÄÊPSH((s, getattr(getattr(ÄÕÒü, \'e\'), \'p\')[0] - áÖß[s][0], i + s, getattr(getattr(ÄÕÒü, \'e\'), \'p\')[1] - x[0])), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n                break\n        for z in ÄÕÒü:\n            Æå(z)\n    return ÂåÔ(Æå(ÄÕÒü), ÄÕÒü)\n(is_short := (lambda ÄÕÒü: getattr(getattr(ÄÕÒü, \'e\'), \'parse_len\') != getattr(getattr(ÄÕÒü, \'e\'), \'input_len\')))\n(warn_if_short := (lambda ÄÕÒü: MOD(ÂùÆ, áØÁ=ÂÄ)(not is_short(ÄÕÒü), \'Parse length warning %s<%s\' % (getattr(getattr(ÄÕÒü, \'e\'), \'parse_len\'), getattr(getattr(ÄÕÒü, \'e\'), \'input_len\')))))\n(gram_rp := (lambda áÖó, r, m=True: MOD(Áëý, áØÁ=m)(MOD(ÆÑ, áØÁ=áÖó)(MOD(ËãÂ, áØÁ=ì)(r, Âåæ(rgx_golfatron, ÂåÔ)), lambda x, y: MOD(ÄÔéÄ, áØÁ=x)(ÂîÌ([y[0]], \'%\'), y[1])), peggle2)))\n\ndef fill_ÄÕÒü_holes_basic(ÄÕÒü):\n    if \'p\' not in getattr(ÄÕÒü, \'e\'):\n        (ÄÊPSH(getattr(ÄÕÒü, \'first_sides\')(lambda ÂîÓ: ÂÔö(getattr(ÂîÓ, \'e\'), \'p\'))), ((Ïß := ÄÊPKE(0)[0]), (Ïà := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n        if None is not Ïß and Ïà is not None:\n            (ÄÊPSH(getattr(ÄÕÒü, \'e\')), ÄÊPSH(\'p\'), ÄÊPSH((*getattr(getattr(Ïß, \'e\'), \'p\')[slice(None, 2)], *getattr(getattr(Ïà, \'e\'), \'p\')[slice(2, None)])), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n    for c in ÄÕÒü:\n        fill_ÄÕÒü_holes_basic(c)\n    return ÄÕÒü\n\ndef gram_surgery(ÄÕÒü, holes=None, áÖÇ=0):\n\n    def Æå(ÄÕÒü):\n        nonlocal áÖÇ\n        if \'p\' not in getattr(ÄÕÒü, \'e\'):\n            return\n        if ÄÕÒü and (not getattr(getattr(ÄÕÒü, \'e\'), \'T\')):\n            for c in ÄÕÒü:\n                Æå(c)\n            (ÄÊPSH(ÐÌü(getattr(ÄÕÒü, \'farnodes\'))), ((Ïß := ÄÊPKE(0)[0]), (Ïà := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n            if \'p\' in getattr(Ïß, \'e\') and ÂÔö(getattr(Ïà, \'e\'), \'p\'):\n                (ÄÊPSH(getattr(ÄÕÒü, \'e\')), ÄÊPSH(\'p\'), ÄÊPSH((getattr(getattr(Ïß, \'e\'), \'p\')[0], getattr(getattr(Ïà, \'e\'), \'p\')[1])), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n            return\n        (ÄÊPSH((ÄÊPSH(getattr(ÄÕÒü, \'e\')), ÄÊPSH(\'p\'), ÄÊPSH((getattr(getattr(ÄÕÒü, \'e\'), \'p\')[0] + áÖÇ, getattr(getattr(ÄÕÒü, \'e\'), \'p\')[1] + áÖÇ)), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]), ((l := ÄÊPKE(0)[0]), (r := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n        while holes and holes[0][0] <= l:\n            (ÄÊPSH(áÖÇ), ÄÊPSH(ÄÊPKE(0) + (ÏÁ := getattr(holes, \'pop\')(0)[1])), (áÖÇ := ÄÊPKE(0)), ÄÊDEL(2))[2]\n            (ÄÊPSH(getattr(ÄÕÒü, \'e\')), ÄÊPSH(\'p\'), ÄÊPSH((ÄÊPSH((l + ÏÁ, r + ÏÁ)), ((l := ÄÊPKE(0)[0]), (r := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]\n    Æå(ÄÕÒü)\n    return ÄÕÒü\n\ndef under_gram(ÄÕÒü):\n    (Ïâ := ÂÚü())\n    for r in getattr(ÄÕÒü, \'find\')(lambda ÂîÓ: ÂÔö(getattr(ÂîÓ, \'e\'), \'R\'), True, False):\n        getattr(Ïâ, \'append\')((getattr(getattr(r, \'e\'), \'p\')[0], ãÊú(+r)))\n    for r in getattr(ÄÕÒü, \'find\')(lambda ÂîÓ: ÂÔö(getattr(ÂîÓ, \'e\'), \'I\'), True, False):\n        getattr(Ïâ, \'append\')((getattr(getattr(r, \'e\'), \'p\')[1], ÄÝöâ(ãÊú(+r))))\n    getattr(ÄÕÒü, \'rm\')(lambda ÂîÓ: ÂÕÖ(getattr(ÂîÓ, \'e\') ** î, \'RI\'))\n    return (+ÄÕÒü, ÄÊCUR((1,), {}, gram_surgery, ÂýÃ, Ïâ))\n\ndef gram_subsup(x, áÔë=gram_rp(\'\\n            sup  = ~‹%SUP%+›\\n            sub  = ~‹%SUB%+›\\n            main = ((σscript = sup∨sub)∨~‹.|\\\\n›)*\\n        \', ÂÑÖ()(SUP=ÄÝõá(ë), SUB=ÄÝõà(ë))), r=\'main\'):\n    (Ëðá := (lambda x: getattr(áÔë(x, r, remove_trashes=False), \'ftrp\')(\'σscript\', lambda ÄÕÒü: getattr(ÄÕÒü, \'set\')(t=getattr(ÄÕÒü[0], \'t\'), c=[áÐè(\'\\U000f071e\\U000f071a\'[getattr(ÄÕÒü[0], \'t\')[-1] == \'p\'], e=MOD(ÂÑÖ, áØÁ=None)()(I=True, p=(getattr(getattr(ÄÕÒü, \'e\'), \'p\')[0], getattr(getattr(ÄÕÒü, \'e\'), \'p\')[0]))), *ÁØò(lambda ÂîÓ: offset_áÖï(ÂîÓ, getattr(getattr(ÄÕÒü, \'e\'), \'p\')[0]))(Ëðá(ÄÝöË(+ÄÕÒü))), áÐè(\'\\U000f071b\', e=MOD(ÂÑÖ, áØÁ=None)()(I=True, p=(getattr(getattr(ÄÕÒü, \'e\'), \'p\')[1], getattr(getattr(ÄÕÒü, \'e\'), \'p\')[1])))]))))\n    return under_gram(Ëðá(x))\n\ndef peggrampeg(áÖï, ns={}, áÔë=peggle2(\'\\n           main = (brak∨~‹.|\\\\n›)*\\n           brak = \\U000f01b4‹%⦃› ~‹((?!⦄%).)*› \\U000f01b4‹⦄%›\\n        \'), m=True):\n    return MOD(Áëý, áØÁ=m)(+getattr(áÔë(áÖï), \'ftrp\')(\'brak\', lambda ÂîÓ: getattr(ÂîÓ, \'set\')(c=[áÐè(ÄÕôñ(+ÂîÓ, ns=ns))])), peggle2)\n__ÄÊADD_EXPORTS__(globals(), (\'peggle2\', peggle2), (\'ÅÒ\', ÅÒ), (\'áÎô\', áÎô), (\'áÐè\', áÐè), (\'Âîë\', Âîë), (\'Âîì\', Âîì), (\'ÂØÙ\', ÂØÙ), (\'ÂØØ\', ÂØØ), (\'áÍô\', áÍô), (\'offset_áÖùþáÖï\', offset_áÖùþáÖï), (\'offset_áÖï\', offset_áÖï), (\'reform_positions\', reform_positions), (\'gram_rp\', gram_rp), (\'under_gram\', under_gram), (\'gram_subsup\', gram_subsup), (\'peggrampeg\', peggrampeg), (\'is_short\', is_short), (\'warn_if_short\', warn_if_short), (\'fill_ÄÕÒü_holes_basic\', fill_ÄÕÒü_holes_basic))\n\ndef test_gram_tools():\n    (g := peggrampeg("\\n                        sub = \\U000f01b4\'\\U000f071e\' (sub ∨ sup ∨ ~‹[^\\U000f071b]›)* \\U000f01b4\'\\U000f071b\'\\n                        sup = \\U000f01b4\'\\U000f071a\' (sub ∨ sup ∨ ~‹[^\\U000f071b]›)* \\U000f01b4\'\\U000f071b\'\\n                        main = (sup ∨ sub ∨ (%⦃␛t+‹he›⦄%=~‹.›))*\\n                     "))\n    (ÄÊPSH(gram_subsup(Âçß(\'someᶜᵒᵒˡ\\U0010affe\\U0010aff5\\U0010aff6\\U0010affe\\U0010af7e₂k\'))), ((s := ÄÊPKE(0)[0]), (ÏÆ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]\n    (ÄÕÒü := ÐÌü(getattr(g(Âçß(s)), \'P\')))\n    ÐÌü(getattr(ÏÆ(ÄÕÒü), \'P\'))',__:=globals().copy())
for k,v in __.get("__EXPORTS__",{}).items():globals()[k]=v


__file__='/home/ganer/Projects/Moon_BETA/Libraries/Compiler/generate_operators.☾'
(OP_FILE := ð(getattr(ÂÞÅCAT(__file__, áÌî), 'parent'), 'operators'))
__ÄÊIMPORT__('peggle2', globals())

class áÍáþáÍá(áÍá):
    None
(ÄÊPSH((getattr(SCRIPT, 'sup'), getattr(SCRIPT, 'sub'), getattr(SCRIPT, 'nrm'))), ((sup := ÄÊPKE(0)[0]), (sub := ÄÊPKE(0)[1]), (nrm := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
(ords := '0\U000f7c1c\U000f7c1d\U000f7c1e\U000f7c1f\U000f7c20\U000f7c21\U000f7c22\U000f7c23\U000f7c24\U000f7c25\U000f7c26\U000f7c27\U000f7c28\U000f7c29\U000f7c2a\U000f7c2b\U000f7c2c\U000f7c2d\U000f7c2e\U000f7c2f\U000f7c37\U000f7c30\U000f7c31\U000f7c3e')
(clrs := ÂÛê('0\u2009e3b\u2009f77\u2009c66\u2009b56\u20096cf\u2009b9d\u2009c08\u20090f5\u20091e6\u20092d7\u20093c8\u20094b9\u200985f\u200967f\u2009eae\u2009d8d\u2009c6c\u2009b4d\u2009ff5\u2009ce3\u2009bd2\u2009ad1\u2009fa2\u20090'))
(dummy_ords := {0, ãÊú(ords) - 1})
(minigram := Âåæ((Æå := (lambda ÂîÓ: getattr(ÂîÓ, 't') if getattr(getattr(ÂîÓ, 'e'), 'T') else (lambda ÂîÓ, ÂîÒ: Áÿú(ÂøÚ(ÂîÒ), Âøî) if ÂîÓ == '⨝' else ÄÔÙù(ÂîÒ))(getattr(ÂîÓ, 't'), Áÿú(ÂîÓ, Æå)))), peggle2("main=⨝=((∀=\U000f01b4'⟦'⠶⨝\U000f01b4'⟧') ∨ \U000f01b4'⁅'⨝\U000f01b4'⁆' ∨ ~'[^⟦⟧⁅⁆]')*")))

def parse_operator_file(contents):
    (p := UGX_CREATE(('B', (àìÒ := []), '*', None, ('B', (àìÒ := []), '', None, ('∨', ('∧', (lambda ÂîÓ: ãÊú(ÄÝöå(ÂîÓ, lambda ÂîÓ: ÂîÓ != ' ')) == 0, ''), ('P', (àìÒ := []), '*', MOD(ÁØò(lambda ÂîÓ: ÂîÓ[slice(MOD(ÂÛÒ, áØÁ=ÂÕË)()[0], None)])), ('∨', (Âåæ(Âó, Âüá), ''), (lambda ÂîÓ: ÄÝöç(ãÊú(ÄÝöå(ÂîÓ, lambda ÂîÓ: ÂîÓ != ' '))), '')))), (ÃÆë, ''))))))
    (g_order := (lambda ÂîÒ: MOD(ÄÔÞÔ, ÁÜñ=ÄÕøü)(ords, ÂîÒ)))
    (g_symbs := (lambda ÂîÓ: ÂÞÅCAT(MOD(ÄÕÊÄ, áØÁ=ÁØã)(áÇù(ÂîÓ, lambda ÂîÓ: ÂîÓ in sup('αλςν')), 2), ÐàÒ(CUR(ÁØòþÁÙÄ(lambda ÂîÓ, ÂîÒ: [ÂîÓ, ÂîÒ]))))))
    (g_sig := ÄÕÍÔ)
    (g_combos := minigram)
    (g_desc := (lambda x: Áÿú(ÂøÚ(UGX_CREATE(('B', (àìÒ := []), '*', None, ('∨', ('B', (àìÒ := []), '*', lambda ÂîÓ: ÄÔÔè(ÄÝöÜ(ÂîÓ, ','), ','), ('∧', (lambda ÂîÓ: ÄÔýò if ÂîÓ == '{' else None, ''), (lambda ÂîÓ: ÂîÓ != '}', '*'), (lambda ÂîÓ: ÄÔýò if ÂîÓ == '}' else None, ''))), ('B', (àìÒ := []), '*', Âåæ(Âêà, Âøî), (lambda ÂîÓ: ÂîÓ != '{', '')))))(x)), Âøî)))
    (Æås := [g_order, g_symbs, g_sig, g_combos, g_desc])
    (áÖï := ÄÝöÞ(contents, '\n'))
    (ÄÊPSH(MOD(ÐÌÛ, áØÁ=áÍÖ)(áÖï, lambda ÂîÓ: ÂîÓ[0] == '>')), ((áÖï := ÄÊPKE(0)[0]), (áÖå := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (áÖï := p(áÖï))
    (ops := ÄÔàÑ(ÁØò(lambda ÂîÓ: MOD(ËãÂ, áØÁ=0)(áÇù(ÄÝöÊ(ËãÂ(ÄÕåØ(MOD(ÁÞç, áØÁ=slice(None, 4))(MOD(ÁÞç, áØÁ=slice(None, 1))(Áÿú(MOD(ÄÝöÞ, áØÁ=3)(ÂîÓ[0], '\u2009'), Âüá), lambda ÂîÓ: ÄÝöÞ(ÂîÓ[0])), MOD(ÁØò(lambda ÂîÓ: MOD(ÄÔéÄ, áØÁ=ÂîÓ)(' ', ÁØã)))), Æås), lambda x, y: y(x)), [0, 2, 3, 1, 4]), 2), lambda x, y: ÁØÿþÁÙÇ(lambda ÂîÓ, ÂîÒ: ÄÔÙù(ÂîÓ, ÂîÒ))(ÄÔÙù(x, Âêà(Âøî(ÄÝöÊ(1, ÂîÓ), '\n'))), ÄÕåØ(y))))(áÖï), MOD(ÁÛÛ, áØÁ=(0, 0))))
    (ops := áÍáþáÍá(ops))
    (ÄÊPSH(ops), ÄÊPSH('style'), ÄÊPSH(Áÿú(áÖå, MOD(ÁÝÖ, áØÁ=0))), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    return ops

def get_operator_table(parsed_ops, do_join=False):
    (infer := (lambda ÂîÓ: ('ᴮ' if ÂÔö(ÂîÓ, '∧') else 'ᴾ\U000f0012' if ÂÔö(ÂîÓ, '\U000f7ea4') else 'ᴾᴮʳ' if ÂÔö(ÂîÓ, '\U000f7e0f') else '\U000f0012ᴮˡ' if ÂÔö(ÂîÓ, '\U000f7e10') else 'ᴾ\U000f0012ᴮ' if ÂÕÖ(ÂîÓ, '∨⩚') else ('ᴾ' if ÂîÓ[0] == '.' else '\U000f0012') if ÂÔö(ÂîÓ, '.') else ÁØã) + 'ᴺ' + ('\U000f0037' if ÂÕÖ(ÂîÓ, '\U000f7ea4\U000f7e0f\U000f7e10∨⩚') and ÂîÓ[0] != ÂîÓ[-1] else ÁØã)))
    (áØÀ := ËãÂ(ÂÑÖ()(ÐÌÛ(ÄÔÔè(ÄÔÙù(parsed_ops), lambda ÂîÓ: ÂîÓ[0] in dummy_ords), MOD(ÁÛÛ, áØÁ=0))), CUR(lambda ÂîÓ, ÂîÒ: ÁØò(lambda ÂîÓ: MOD(ÁÞç, áØÁ=-1)(ÂîÓ[4], CURR(lambda ÂîÓ, ÂîÒ: ÂîÓ + ÂîÒ, infer(ÂîÓ[1]))))(ÂîÒ))))
    return Âøî(ÁØò(lambda ÂîÓ: Âøî(ÁØò(lambda ÂîÓ: Âøî(ÂîÓ))(ÂîÓ), ' '))(áØÀ), '\n') if do_join else áØÀ

def generate_fontcompose_conf(parsed_ops):
    (style := getattr(parsed_ops, 'style'))
    return Âøî(ËãÂ(ÂÑÖ()(ÐÌÛ(ÄÔÙù(parsed_ops), MOD(ÁÛÛ, áØÁ=0))), CUR(lambda ÂîÓ, ÂîÒ: '%s⟦⁅BLK%s𝕊⟶"%s"⁆%s⟧' % (ÁØã if ÂîÓ in dummy_ords else '⦑c⦑%s⦒⦒' % (clrs[ÂîÓ],), ÂîÓ, ords[ÂîÓ], Âøî(ÁØò(lambda ÂîÓ: '⁅%s⟶"%s"⁆' % (MOD(ÄÔéÄ, áØÁ=ÂîÓ[3])('"', '␛"')[slice(1, None)] if 'ᴍ' in ÂîÓ[3] else ';;%sᴍ' % (ÂîÓ[3],), MOD(Áëý, áØÁ=lambda ÂîÓ: ÂîÓ == '␛')(ÂîÓ[4][0], lambda ÂîÓ: ÂÞÅCAT(ÂîÓ, 2))))(ÂîÒ))))), '\n') + ÂîÊ(style, '\n')

def to_docs(parsed_ops):
    return ÁØò(lambda ÂîÓ: MOD(ÁÞç, áØÁ=-1)(ÂîÓ, MOD(ÁÛÛ, áØÁ=0)))(Áÿú(MOD(ËãÂ, áØÁ=2)(MOD(ÁÛÛ, áØÁ=(slice(None, None), slice(None, None), slice(1, None)))(parsed_ops), lambda x, y, z, w, v: (w[0], v, 'Sig:%s\n%s' % (x or '□', y))), ÄÕåØ))
(ops := parse_operator_file(ÐØó(OP_FILE)))
__ÄÊADD_EXPORTS__(globals(), ('ops', ops), ('generate_fontcompose_conf', generate_fontcompose_conf), ('get_operator_table', get_operator_table))

__file__='/home/ganer/Projects/Moon_BETA/Libraries/Compiler/op_table.☾'
__ÄÊIMPORT__('text_format', globals())
__ÄÊIMPORT__('generate_operators', globals())
(áÖáþáÖæ := [*get_operator_table(ops), [ÂÛê('.\u2009ᴺ')]])
(add_before := (lambda p, n: getattr(áÖáþáÖæ, 'insert')(MOD(ÄÔÞÔ, ÁÜñ=ÄÕøü)(áÖáþáÖæ, lambda ÂîÓ: ÂÔö(MOD(ÁÛÛ, áØÁ=(slice(None, None), 0))(ÂîÓ), p)), n)))
MOD(ÄÕéý, áØÁ=add_before)('!', [ÂÛê('␀CAT\u2009ᴺᴮ')])
MOD(ÄÕéý, áØÁ=add_before)('ᴍ', [ÂÛê('␀TAC\u2009ᴮ')])
MOD(ÄÕéý, áØÁ=add_before)('⨳', [ÂÛê('␀A3\u2009ᴮ\U000f004c')])
MOD(ÄÕéý, áØÁ=add_before)('␀A3', ÁØò(lambda ÂîÓ: [ÂîÓ, 'ᴮ'])('≔\U000f7e09\U000f7e0a\U000f7e0b≕\U000f7e0e\U000f7e0c\U000f7e0d'))
MOD(ÄÕéý, áØÁ=add_before)('≔', [ÂÛê('␀A2\u2009ᴮ\U000f004c')])
MOD(ÄÕéý, áØÁ=add_before)('␀A2', [ÂÛê('⭜\u2009ᴮ\U000f004c')])
MOD(ÄÕéý, áØÁ=add_before)('⭜', [ÂÛê('⭝\u2009ᴺᴮ\U000f004c')])
MOD(ÄÕéý, áØÁ=add_before)('⭝', [ÂÛê('␀A1\u2009ᴮ\U000f004c')])
(áÖåþáÖæ := Áÿú(ÄÝöÞ(ÂÁÍ(ÂÕÅ)('    \u2009␀T  \u2009ᴺ \U000f0012 \u2009    \n␀TAC\u2009␀T⟞ \u2009ᴺ \U000f0012 \u2009    \n    \u2009␀T⟝ \u2009ᴺᴾ  \u2009␀TAC\n␀TAC\u2009␀T⟞⟝\u2009ᴺᴾ\U000f0012ᴮ\u2009␀TAC\n    \u2009   ⬅\u2009 ᴾ  \u2009␀A1 \n␀A1 \u2009   ➡\u2009  \U000f0012 \u2009    \n    \u2009   ←\u2009 ᴾ  \u2009␀A2 \n␀A2 \u2009   ⥉\u2009   ᴮ\u2009␀A2 \n␀A2 \u2009   →\u2009  \U000f0012 \u2009    \n    \u2009   ⭠\u2009 ᴾ  \u2009␀A3 \n␀A3 \u2009   ⭢\u2009  \U000f0012 \u2009    ', ÄÔéÄ([' '], ÁØã)), '\n'), ÂÛê))
(MT := 'NPSBlrαςνλΔ')

class OP(ÁØö(ÐÌü(ÂÑÖ()))):
    (__repr__ := (lambda áÑÞ: '%s%s' % (getattr(áÑÞ, 't'), ÄÝõá(Âøî(getattr(áÑÞ, 'M'))))))

    def __init__(áÑÞ, *áÑË, **áÑÕ):
        getattr(super(), '__init__')(*áÑË, **áÑÕ)
        getattr(áÑÞ, 'setdef')(ÁØã)

    def __getitem__(áÑÞ, x):
        (x := VEP(x))
        if ÂÖó(x, MT):
            return x if ÂÖó(x, getattr(áÑÞ, 'M')) else None
        return getattr(super(), '__getitem__')(x)

    def __setitem__(áÑÞ, x, y):
        (x := VEP(x))
        if ÂÖó(x, MT):
            return (ÄÊPSH(áÑÞ), ÄÊPSH('M'), ÄÊPSH(getattr(ÄÊPKE(1), ÄÊPKE(0))), ÄÊPSH(MOD(ÄÕéý, áØÁ=ÂÕØ if y else ÂÕÃ)(ÄÊPKE(0), x)), setattr(ÄÊPKE(3), ÄÊPKE(2), ÄÊPKE(0)), ÄÊDEL(4))[4]
        return getattr(super(), '__setitem__')(x, y)
    (__setattr__ := __setitem__)
    (__getattr__ := __getitem__)

def cb(áÎõ):
    for ÂÑÕ in áÎõ ** ì:
        (ÄÊPSH(ÂÑÕ), ÄÊPSH('R'), ÄÊPSH(getattr(ÄÊPKE(1), ÄÊPKE(0))), ÄÊPSH(ÂÕØ(ÄÊPKE(0), '≔\U000f7e09\U000f7e0a\U000f7e0b')), setattr(ÄÊPKE(3), ÄÊPKE(2), ÄÊPKE(0)), ÄÊDEL(4))[4]
    for k in '≔\U000f7e09\U000f7e0a\U000f7e0b':
        (ÄÊPSH(áÎõ[k]), ÄÊPSH('L'), ÄÊPSH(ÂÔð()), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    for k in '≕\U000f7e0e\U000f7e0c\U000f7e0d':
        (ÄÊPSH(áÎõ[k]), ÄÊPSH('R'), ÄÊPSH(ÂÔð()), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    (ÄÊPSH(áÎõ['⬅']), ÄÊPSH('R'), ÄÊPSH(getattr(ÄÊPKE(1), ÄÊPKE(0))), ÄÊPSH(ÂÕØ(ÄÊPKE(0), '→⭢')), setattr(ÄÊPKE(3), ÄÊPKE(2), ÄÊPKE(0)), ÄÊDEL(4))[4]
    (ÄÊPSH(áÎõ['←']), ÄÊPSH('R'), ÄÊPSH(getattr(ÄÊPKE(1), ÄÊPKE(0))), ÄÊPSH(ÂÕØ(ÄÊPKE(0), '⭢')), setattr(ÄÊPKE(3), ÄÊPKE(2), ÄÊPKE(0)), ÄÊDEL(4))[4]
    return áÎõ

def make_op_table(áÖáþáÖæ, áÖåþáÖæ, cb):
    (áÎõ := ÐÌü(ÂÑÖ()))
    for áÖÞ in ÂÀÇ(áÖáþáÖæ):
        (ÄÊPSH(áÖÞ), ÄÊPSH(ÁØò(lambda ÂîÓ: (ÂîÓ[0], ÄÝöË(Âøî(ÂîÓ[slice(1, None)]))))(ÄÊPKE(0))), (áÖÞ := ÄÊPKE(0)), ÄÊDEL(2))[2]
        (ÄÊPSH((áÍè(MOD(ÁÛÛ, áØÁ=(slice(None, None), 0))(áÖÞ)), ÐÌü(ÂÑÖ()))), ((áØÂ := ÄÊPKE(0)[0]), (áÖá := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        for t, m in áÖÞ:
            (food := ÂÕØ(áÍè(áÎõ ** î), ÐÌü(getattr(áØÂ, 'copy')) if 'α' in m else ÂÔð()))
            (ÄÊPSH(áÖá), ÄÊPSH(t), ÄÊPSH(OP(t=t, M=m, L=ÐÌü(getattr(food, 'copy')) if áÍè(ÂÕÖ(m, 'BS')) else ÂÔð(), R=ÐÌü(getattr(food, 'copy')) if áÍè(ÂÕÖ(m, 'BP')) else ÂÔð())), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        (ÄÊPSH(áÎõ), ÄÊPSH(ÄÊPKE(0) | áÖá), (áÎõ := ÄÊPKE(0)), ÄÊDEL(2))[2]
    (áÏì := ÐÌü(ÂÑÖ()))
    for L, t, m, R in áÖåþáÖæ:
        (ÄÊPSH(m), ÄÊPSH(ÄÝöË(ÄÊPKE(0))), (m := ÄÊPKE(0)), ÄÊDEL(2))[2]
        (Lc := (ÂÕØ(getattr(áÎõ[L], 'L'), getattr(áÎõ[L], 'R')) if L else ÂÔð()))
        (Rc := (ÂÕØ(getattr(áÎõ[R], 'L'), getattr(áÎõ[R], 'R')) if R else ÂÔð()))
        for áÏÖ, ÂÑÕ in áÎõ:
            if áÏÖ not in Lc and ÂÕÖ('PB', getattr(ÂÑÕ, 'M')):
                getattr(getattr(ÂÑÕ, 'R'), 'add')(t)
            if áÏÖ not in Rc and ÂÕÖ('SB', getattr(ÂÑÕ, 'M')):
                getattr(getattr(ÂÑÕ, 'L'), 'add')(t)
        (ÄÊPSH(áÏì), ÄÊPSH(t), ÄÊPSH(OP(t=t, M=m, L=ÂÕØ(ÂÕÃ(áÍè(áÎõ ** î), getattr(áÎõ[L], 'L')), áÍè([L])) if L else ÂÔð(), R=ÂÕØ(getattr(áÎõ[R], 'R'), áÍè(ÁØò(lambda ÂîÓ: ÂîÓ[1])(áÖåþáÖæ)) if 'α' in m else ÂÔð()) if R else ÂÔð())), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    (ÄÊPSH(áÎõ), ÄÊPSH(ÄÊPKE(0) | áÏì), (áÎõ := ÄÊPKE(0)), ÄÊDEL(2))[2]
    return cb(áÎõ)
(OP_TABLE := (áÎõ := make_op_table(áÖáþáÖæ, áÖåþáÖæ, cb)))
(IS_OP := (lambda ÄÕÒü: getattr(getattr(ÄÕÒü, 'e'), 'O') if getattr(ÄÕÒü, 't') == '𝗈𝗉' and '´' not in getattr(ÄÕÒü, 'e') else None))
(MODIFIERS := ÂÛê('⟥≺\u2009⦣\u205f≻ᵜ꜠´⟤\u2009ᔨ⦢𐞑'))
(áÕÒ := ÂÑÖ()(OP_LIT=áÎõ ** î, OP_MOD_L_N=MODIFIERS[0][0], OP_MOD_L_Y=MODIFIERS[0][1], OP_MOD_R_N=MODIFIERS[1][0], OP_MOD_R_Y=MODIFIERS[1][1], VAR_SPEC='ⴳⴴ✓✗□ᐦ\U000f0b88\U000f18e9⬤îĵ\U000f7e88ℇτπ\U000f7e8d\U000f7e8f∞\U000f7c6a\U000f7c7d\U000f7c7e\U000f7c6b\U000f7c6c\U000f7c6d\U000f7c6e\U000f7c6f\U000f7c70\U000f7c69' + Âøî(ÐÌü(getattr(FRAC_CONV, 'values'))), BLK_KWDS='\ue00a', STD_KWDS='↪⮂↺⇥\U000f01b4', BLK_CLN_KWDS='\U000f1018¿⸘¡', SUP=ÄÝõá(ë), SUB=ÄÝõà(ë)))

__file__='/home/ganer/Projects/Moon_BETA/Libraries/Compiler/node_types.☾'
from functools import cache
__ÄÊIMPORT__('peggle2/gram_tools', globals())
__ÄÊIMPORT__('text_format', globals())
(fix := ÄÔéÄ('﹕', 'ː'))

def Âçß(*áÑË, s='\n', sep=' ', ÂìÆ=False, **áÑÕ):
    getattr((Æå := (stderr if ÂìÆ else stdout)), 'write')(fix(Âøî(áÑË, ÁÜÙ(sep)) + ÁÜÙ(s)))
    ÐÌü(getattr(Æå, 'flush'))
    if áÑË:
        return áÑË[0]
(áÍñ := (lambda *áÑË: BOX(stackr(*áÑË))))
(áÍñþáÎÚ := Âåæ(box, lambda ÂîÓ: ÂÕÅ(getattr(ÂîÓ, 'P'), False)))
(áÍñþáÍñ := (lambda ÄÕÒü, *áÑË: ÂåÔ(Âçß(BOX(ÂÁÍ(ì)((d := ÂÕÅ(getattr(ÄÕÒü, 'P'), False)), Âøî(ÁØò(lambda ÂîÓ: padc(ÂîÌ([ÂîÓ], ' '), d, '─') + '\n')(áÑË))))), ÄÕÒü)))
(ÄÊPSH((áÐè(ÁØã), áÐè(' '))), ((áÚì := ÄÊPKE(0)[0]), (áÖÊ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda x: áÎô('𝑣', áÐè(x)), lambda x: áÎô('𝑣_spec', áÐè(x)))), ((áÓé := ÄÊPKE(0)[0]), (áÓéþáÓæ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda *áÑË: áÎô('x', *áÑË), lambda *áÑË: áÎô('X', *áÑË))), ((áÓë := ÄÊPKE(0)[0]), (áÓÐ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda *áÑË: áÎô('\U000f7e58', *áÑË), lambda *áÑË: áÎô('⍖', *áÑË), lambda *áÑË: áÎô('\U000f7e57', *áÑË))), ((áÓã := ÄÊPKE(0)[0]), (áÓà := ÄÊPKE(0)[1]), (áÓÖ := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
(áÒÿ := (lambda: áÓÕþáÓÓþáÓßþáÓß('globals')))
(áÓå := (lambda x: áÓÕþáÓÓþáÓßþáÓß('þDEL', áÓá(x))))
(áÓá := (lambda x: áÎô('num', áÐè(x))))
(áÓäþáÓé := (lambda x: áÎô('qvar', áÐè(x))))
(ÄÊPSH(ÁØò(lambda ÂîÓ: lambda *áÑË: áÓÜ(áÓÌ(*áÑË), áÓá(ÂîÓ)))(ÂÿÇ(2))), ((áÓÄ := ÄÊPKE(0)[0]), (áÓÊ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda *áÑË: áÎô('𝑖', *áÑË), lambda *áÑË: áÎô('𝑎', *áÑË), lambda *áÑË: áÎô('𝑇', *áÑË))), ((áÓÜ := ÄÊPKE(0)[0]), (áÓÓ := ÄÊPKE(0)[1]), (áÓÌ := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
(áÓçþáÓàþáÓã := (lambda *áÑË: áÎô('tmp', *áÑË)))
(áÓâþáÓãþáÒú := (lambda x, *áÑË: áÎô('opC', MOD(Áëý, áØÁ=ÄÊCUR((1,), {}, ÁØö, ÂýÃ, ÁÜÙ))(x, áÓÇþáÓÈ), *áÑË)))
(áÓæþáÓçþáÓå := (lambda *áÑË: áÎô('str', *áÑË)))
(áÓØþáÓëþáÓã := (lambda *áÑË: áÎô('exp', *áÑË)))
(áÓÜþáÓçþáÓØþáÓà := (lambda *áÑË: áÎô('item', *áÑË)))
(áÓçþáÓØþáÓåþáÓá := (lambda *áÑË: áÎô('tern', *áÑË)))
(áÓÓþáÓçþáÓçþáÓå := (lambda *áÑË: áÎô('attr', *áÑË)))
(áÓàþáÓÕþáÓÓþáÓß := (lambda *áÑË: áÎô('mcal', *áÑË)))
(áÓÕþáÓÓþáÓßþáÓß := (lambda *áÑË: áÎô('∘', *ÁØò(lambda ÂîÓ: MOD(Áëý, áØÁ=lambda ÂîÓ: ÁØö(ÂîÓ, ÁÜÙ))(ÂîÓ, áÓé))(áÑË))))
(áÓßþáÓÓþáÓàþáÓÔ := (lambda *áÑË: áÎô('lamb', *áÑË)))
(áÓæþáÓçþáÓåþáÓÔ := (lambda *áÑË: áÎô('strb', *áÑË)))
(áÓÙþáÓâþáÓå := (lambda *áÑË: áÎô('∀', *áÑË)))
(áÓæþáÓßþáÓÜþáÓÕþáÓØ := (lambda *áÑË: áÓÕþáÓÓþáÓßþáÓß('slice', *(lambda ÂîÓ: ÁØò(lambda ÂîÓ: áÓéþáÓæ('□') if ÂîÓ is None else áÓá(ÂîÓ))((getattr(ÂîÓ, 'start'), getattr(ÂîÓ, 'stop'), getattr(ÂîÓ, 'step'))))(áÑË[0])) if áÑË and ÁØö(áÑË[0], slice) else áÎô('slice', *Âøî(áÑË, lambda *áÑË: MOD(ÄÕéý, áØÁ=ÂØØ)(áÐè(':'), áÑË)))))
(Æå_dec_áÑË := (lambda x, *áÑË: áÎô('𝔸', áÐè(x))))
(Æå_dec_áÑÕ := (lambda x, **áÑÕ: áÎô('𝕂', áÐè(x))))
(áÓÙþáÓãþáÓÓþáÓåþáÓÓþáÓàþáÓæ := (lambda *áÑË: áÎô('ƒ_dec_params', *áÑË)))
(áÓÚþáÓåþáÓã := (lambda x, *áÑË: áÎô('grp', MOD(ÄÕéý, áØÁ=Âîë)(áÐè(x[0]), áÑË), áÓë(*áÑË), MOD(ÄÕéý, áØÁ=Âîì)(áÐè(x[1]), áÑË))))
(áÓâþáÓã := (lambda x: áÎô('op', MOD(ÄÕéý, áØÁ=Âîë)(ÅÒ('op_⸓_l'), x), áÎô('op_lit', áÐè(x)), MOD(ÄÕéý, áØÁ=Âîì)(ÅÒ('op_⸓_r'), x))))
(áÓÇþáÓÈ := (lambda x: áÎô('𝗈𝗉', MOD(ÄÕéý, áØÁ=Âîë)(ÅÒ('op_⸓_l'), x), MOD(ÄÕéý, áØÁ=ÂØÙ)(áÎô('op_lit', áÐè(x)), x), MOD(ÄÕéý, áØÁ=Âîì)(ÅÒ('op_⸓_r'), x), e=MOD(ÂÑÖ, áØÁ=None)()(O=OP_TABLE[MOD(Áëý, áØÁ=ÄÊCUR((1,), {}, ÄÝøÇ, ÂýÃ, ÁÜÙ))(x, ì)]))))

def áÓÓþáÓèþáÓçþáÓâ(x):
    if ÁØö(x, ÂÑÅ):
        return áÓá(x)
    if ÁØö(x, ÁÜÙ):
        return áÓæþáÓçþáÓå(áÐè(x))
    if ÁØö(x, áÍé):
        return áÓÌ(Áÿú(x, áÓÓþáÓèþáÓçþáÓâ))
    if ÁØö(x, áÍá):
        return áÎô('𝐿', Áÿú(x, áÓÓþáÓèþáÓçþáÓâ))
    if ÁØö(x, slice):
        return áÓæþáÓßþáÓÜþáÓÕþáÓØ(x)
    return x
(áÓÆþáÓÍþáÓÄþáÓÄ := áÓé('NULL'))
(áÓÒ := áÎô('PLACEHOLDER'))

__file__='/home/ganer/Projects/Moon_BETA/Libraries/Compiler/tree.☾'
__ÄÊIMPORT__('node_types', globals())

def ÄÕÒü_is_hot_stuff(ÄÕÒü, Æå, *áÑË):
    if ÁØö(Æå, ÁÜÙ):
        if Æå != getattr(ÄÕÒü, 't'):
            return
    elif ÁØö(Æå, áÓó):
        if not Æå(ÄÕÒü):
            return
    elif getattr(ÄÕÒü, 't') not in Æå:
        return
    return ÂØõ(ÁØò(lambda ÂîÓ: ÄÕÒü_is_hot_stuff(ÂîÓ, *áÑË))(ÄÕÒü)) if áÑË else True
(date_ÄÕÒü := (lambda *áÏÞ: lambda ÄÕÒü: getattr(ÄÕÒü, 'find')(lambda x: ÄÕÒü_is_hot_stuff(x, *áÏÞ))))

def ÄÕÒüþáÒÿ(ÄÕÒü, x, y):
    if getattr(ÄÕÒü, 't') != y[0]:
        return
    for i, t in ÄÕåØ(x, y[slice(1, None)]):
        if ãÊú(ÄÕÒü) <= i or getattr((ÄÕÒü := ÄÕÒü[i]), 't') != t:
            return
    return True

def try_pop_pos(ÄÕÒü, proxy=None, rec=False):
    (Æå := (lambda ÂîÓ: ÂÔö(getattr(ÂîÓ, 'e'), 'p')))
    (ÄÊPSH(getattr(ÄÕÒü if proxy is None else proxy, 'first_sides')(Æå)), ((l := ÄÊPKE(0)[0]), (r := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    if l is None:
        return ÄÕÒü
    (ÄÊPSH(getattr(ÄÕÒü, 'e')), ÄÊPSH('p'), ÄÊPSH((*getattr(getattr(l, 'e'), 'p')[slice(None, 2)], *getattr(getattr(r, 'e'), 'p')[slice(2, None)])), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    if not rec:
        return
    for áÎÚ in ÄÕÒü:
        try_pop_pos(áÎÚ)
    return ÄÕÒü

__file__='/home/ganer/Projects/Moon_BETA/Libraries/Compiler/tree_txt.☾'
__ÄÊIMPORT__('tree', globals())

def rewrite_str_indent(ÄÕÒü):
    if 'p' not in getattr(ÄÕÒü, 'e'):
        return ÄÕÒü
    (ÄÊPSH((getattr(getattr(ÄÕÒü, 'e'), 'p')[0], getattr(getattr(ÄÕÒü, 'e'), 'p')[1] + 1)), ((pl := ÄÊPKE(0)[0]), (áÖð := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    for áÎÚ in getattr(ÄÕÒü, 'gets')('str_tsub_guts'):
        (ÄÊPSH((lines(getattr(áÎÚ[0], 't')), [])), ((áØÁ := ÄÊPKE(0)[0]), (h := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        for i, ÂîÓ in ÂÓÏ(áØÁ):
            (I := (getattr(getattr(áÎÚ, 'e'), 'p')[0] + i))
            getattr(h, 'append')(ÂîÓ if pl == I else ÂîÓ[slice(ÂóÌ(MOD(Áëý, áØÁ=ÄÊCUR((1,), {}, ÂÕó, ÂýÃ, None))(MOD(ÄÔÞÔ, ÁÜñ=ÄÕøü)(ÂîÓ, lambda ÂîÓ: ÂîÓ not in ' \t'), MOD(ÄÕÍÔ, áØÁ=ãÊú(ÂîÓ))), áÖð), None)])
            (pl := I)
        (ÄÊPSH(áÎÚ[0]), ÄÊPSH('t'), ÄÊPSH(Âøî(h, '\n')), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    return ÄÕÒü

def add_blocks(ÄÕÒü):
    (start := (lambda ÄÕÒü: getattr(ÄÕÒü, 't') == 'stmt' and getattr(ÄÕÒü[0], 't') == 'blk_head'))
    (Æå := Âåæ(UGX_CREATE(('B', (àìÒ := []), '*', None, ('∨', ('B', (àìÒ := []), '', lambda C: áÎô('blk', C[0], *Áëý(C[slice(1, None)], Æå)), ('∧', (start, ''), (lambda ÂîÓ: ÄÝöç(getattr(getattr(ÂîÓ, 'e'), 'p')), ''), (lambda ÂîÓ: getattr(getattr(ÂîÓ, 'e'), 'p')[1] >= ÂÛÒ()[1], '*'))), (ÃÆë, '')))), áÍá))
    getattr(ÄÕÒü, 'ftrp')('stmts', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(c=Æå(ÄÕÒü)), True)
(flatten_statments := (lambda ÄÕÒü: getattr(ÄÕÒü, 'flat')(lambda ÂîÓ: getattr(ÂîÓ, 't') in ÂÛê('stmt'))))

__file__='/home/ganer/Projects/Moon_BETA/Libraries/Compiler/expr.☾'
__ÄÊIMPORT__('tree_txt', globals())

def denode_op(ÄÕÒü):
    (ÄÊPSH(ÄÕÒü), ((l := ÄÊPKE(0)[0]), (o := ÄÊPKE(0)[1]), (r := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
    (áÖü := OP_TABLE[getattr(o[0], 't')])
    (ÄÊPSH(ÁØò(lambda ÂîÓ: ÁØò(lambda ÂîÓ: ÂîÓ if getattr(ÂîÓ, 't') == '𝚜' else áÎô(getattr(ÂîÓ[0], 't'), *ÂîÓ[slice(1, None)]))(ÂîÓ))([l, r])), ((áÖù := ÄÊPKE(0)[0]), (áØÀ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (ÄÊPSH(Áÿú(ÁØò(lambda ÂîÓ: ÁØò(lambda ÂîÓ: ÄÔýò if getattr(ÂîÓ, 't') == '𝚜' else getattr(ÂîÓ[0], 't'))(ÂîÓ))([l, r]), áÍè)), ((L := ÄÊPKE(0)[0]), (R := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (áÖü := ÐÌü(getattr(áÖü, 'copy')))
    for t in L:
        if t == '⟥':
            (ÄÊPSH(áÖü), ÄÊPSH('L'), ÄÊPSH(áÖü), ÄÊPSH('P'), ÄÊPSH(áÖü), ÄÊPSH('S'), ÄÊPSH(áÖü), ÄÊPSH('B'), ÄÊPSH((ÂÚü(), False, True, False)), (setattr(ÄÊPKE(8), ÄÊPKE(7), ÄÊPKE(0)[0]), setattr(ÄÊPKE(6), ÄÊPKE(5), ÄÊPKE(0)[1]), setattr(ÄÊPKE(4), ÄÊPKE(3), ÄÊPKE(0)[2]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)[3])), ÄÊDEL(9))[9]
        elif t == '≺':
            (ÄÊPSH(áÖü), ÄÊPSH('L'), ÄÊPSH(áÖü), ÄÊPSH('R'), ÄÊPSH(áÖü), ÄÊPSH('P'), ÄÊPSH(áÖü), ÄÊPSH('S'), ÄÊPSH(áÖü), ÄÊPSH('B'), ÄÊPSH((ÐÌü(getattr(getattr(áÎõ['ᴍ'], 'L'), 'copy')), ÂÚü(), False, True, False)), (setattr(ÄÊPKE(10), ÄÊPKE(9), ÄÊPKE(0)[0]), setattr(ÄÊPKE(8), ÄÊPKE(7), ÄÊPKE(0)[1]), setattr(ÄÊPKE(6), ÄÊPKE(5), ÄÊPKE(0)[2]), setattr(ÄÊPKE(4), ÄÊPKE(3), ÄÊPKE(0)[3]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)[4])), ÄÊDEL(11))[11]
    for t in R:
        if t == '⟤':
            (ÄÊPSH(áÖü), ÄÊPSH('R'), ÄÊPSH(áÖü), ÄÊPSH('P'), ÄÊPSH(áÖü), ÄÊPSH('S'), ÄÊPSH(áÖü), ÄÊPSH('B'), ÄÊPSH((ÂÚü(), True, False, False)), (setattr(ÄÊPKE(8), ÄÊPKE(7), ÄÊPKE(0)[0]), setattr(ÄÊPKE(6), ÄÊPKE(5), ÄÊPKE(0)[1]), setattr(ÄÊPKE(4), ÄÊPKE(3), ÄÊPKE(0)[2]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)[3])), ÄÊDEL(9))[9]
        elif t == '≻':
            (ÄÊPSH(áÖü), ÄÊPSH('L'), ÄÊPSH(áÖü), ÄÊPSH('R'), ÄÊPSH(áÖü), ÄÊPSH('P'), ÄÊPSH(áÖü), ÄÊPSH('S'), ÄÊPSH(áÖü), ÄÊPSH('B'), ÄÊPSH((ÂÚü(), ÐÌü(getattr(getattr(áÎõ['ᴍ'], 'R'), 'copy')), True, False, False)), (setattr(ÄÊPKE(10), ÄÊPKE(9), ÄÊPKE(0)[0]), setattr(ÄÊPKE(8), ÄÊPKE(7), ÄÊPKE(0)[1]), setattr(ÄÊPKE(6), ÄÊPKE(5), ÄÊPKE(0)[2]), setattr(ÄÊPKE(4), ÄÊPKE(3), ÄÊPKE(0)[3]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)[4])), ÄÊDEL(11))[11]
        elif t == 'ᵜ':
            None
        elif t == '꜠':
            if getattr(áÖü, 'B'):
                (ÄÊPSH(áÖü), ÄÊPSH('B'), ÄÊPSH(False), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
                if (ÄÊDEL(1), False)[1] if ÄÊPSH(getattr(áÖü, 'P')) else ÄÊPOP() if getattr(áÖü, 'S') else (ÄÊDEL(1), True)[1]:
                    (ÄÊPSH(áÖü), ÄÊPSH('P'), ÄÊPSH((ÄÊPSH(áÖü), ÄÊPSH('S'), ÄÊPSH(True), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
            elif getattr(áÖü, 'P') or getattr(áÖü, 'S'):
                (ÄÊPSH(áÖü), ÄÊPSH('L'), ÄÊPSH((ÄÊPSH(áÖü), ÄÊPSH('R'), ÄÊPSH(ÂÕØ(getattr(áÖü, 'L'), getattr(áÖü, 'R'))), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
                (ÄÊPSH(áÖü), ÄÊPSH('P'), ÄÊPSH((ÄÊPSH(áÖü), ÄÊPSH('S'), ÄÊPSH(True), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
            else:
                ÂùÆ(False)
    (áÖÉ := ÅÒ('𝗈𝗉', MOD(Áëý, áØÁ=not áÖù)(áÎô('op_⸓_l', *áÖù), lambda ÂîÓ: MOD(ÄÕéý, áØÁ=Âîë)(ÂîÓ, ÄÕÒü[1][0])), áÎô('op_lit', ÄÕÒü[1][0]), MOD(Áëý, áØÁ=not áØÀ)(áÎô('op_⸓_r', *áØÀ), lambda ÂîÓ: MOD(ÄÕéý, áØÁ=Âîì)(ÂîÓ, ÄÕÒü[1][0])), e=MOD(ÂÑÖ, áØÁ=None)()(**getattr(ÄÕÒü, 'e'), O=áÖü)))
    if '´' in R:
        (ÄÊPSH(getattr(áÖÉ, 'e')), ÄÊPSH('´'), ÄÊPSH('´'), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    return áÖÉ

def part(áÖü, áÖÔ, d):
    (ÄÊPSH((getattr(getattr(áÖü, 'e'), 'O'), 0)), ((áÏì := ÄÊPKE(0)[0]), (i := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    if d == -1:
        for i, n in ÂÓÏ(áÖÔ)[slice(None, None, -1)]:
            if not (ÂÑÕ := IS_OP(n)):
                continue
            if ÂÔø(getattr(áÏì, 'L'), getattr(ÂÑÕ, 't')):
                break
    elif d == 1:
        (áØÁþáØÂþáÖø := Âêà(getattr(áÏì, 'R')))
        for i, n in ÂÓÏ(áÖÔ):
            if not (ÂÑÕ := IS_OP(n)):
                continue
            while áØÁþáØÂþáÖø:
                if getattr(ÂÑÕ, 't') in áØÁþáØÂþáÖø[-1] or ((((getattr(áÏì, 'P') or (getattr(áÏì, 'B') and (not getattr(áÏì, 'S')))) and getattr(ÂÑÕ, 't') in getattr(áÎõ['⨳'], 'R')) and getattr(ÂÑÕ, 'P')) and (not i)):
                    getattr(áØÁþáØÂþáÖø, 'append')(getattr(ÂÑÕ, 'R'))
                    break
                getattr(áØÁþáØÂþáÖø, 'pop')()
            else:
                break
        else:
            (ÄÊPSH(i), ÄÊPSH(ÄÊPKE(0) + 1), (i := ÄÊPKE(0)), ÄÊDEL(2))[2]
    return áÇù(áÖÔ, i) or MOD(ÂÚü, áØÁ=2)()

def create_call(áÖü, áÖù, áØÀ):
    (ÂÑÕ := getattr(getattr(áÖü, 'e'), 'O'))
    if getattr(ÂÑÕ, 't') in '⭢→➡':
        return áÓÐ(*áÖù)
    if getattr(ÂÑÕ, 't') in '⭠←⬅':
        return áÓÐ(*áØÀ)
    if getattr(ÂÑÕ, 't') == '⥉':
        return MOD(ÄÕéý, áØÁ=ÂØÙ)(áÓÐ(áÓÐ(*áØÀ), áÓÐ(*áÖù)), (áÖù, áØÀ))
    if not getattr(ÂÑÕ, 'ÏÁ'):
        (ÄÊPSH((áÖù is not áÓÆþáÓÍþáÓÄþáÓÄ, áØÀ is not áÓÆþáÓÍþáÓÄþáÓÄ)), ((Ïß := ÄÊPKE(0)[0]), (Ïà := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        (U := ([áÖù, áØÀ] if Ïß and Ïà else [áÖù] if Ïß else [áØÀ] if Ïà else ÂÚü()))
    else:
        (U := (áÖù, áØÀ))
    return MOD(ÄÕéý, áØÁ=ÂØÙ)(áÓâþáÓãþáÒú(áÖü, *U), (áÖù, áØÀ))

def apply_op(áÖü, áÖÞ, áÖä):
    (ÄÊPSH(part(áÖü, áÖÞ, -1)), ((ll := ÄÊPKE(0)[0]), (lr := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (ÄÊPSH(part(áÖü, áÖä, 1)), ((rl := ÄÊPKE(0)[0]), (rr := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    if rl:
        (rl := parse_expr(rl))
    (ÄÊPSH((getattr(getattr(áÖü, 'e'), 'O'), ÂÚü())), ((áÕÉ := ÄÊPKE(0)[0]), (áÑæ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    if '𝚜' in áÕÉ:
        getattr(áÑæ, 'append')(getattr(áÕÉ, 'pop')('𝚜'))

    def suffix(áÖä):
        if áÖä and (not (áÎÛ := IS_OP(áÖä[0])) or (getattr(áÎÛ, 'P') and ((ÄÊDEL(1), False)[1] if ÄÊPSH(getattr(áÎÛ, 'B')) else ÄÊPOP() if getattr(áÎÛ, 'S') else (ÄÊDEL(1), True)[1]))):
            getattr(áÖä, 'insert')(0, denode_op(áÓâþáÓã(MOD(ÄÕéý, áØÁ=Âîì)('␀CAT', áÖä))))
        return áÖä
    (suf2 := (lambda áÖä: Âêà(getattr(áÖä, 'pop')(0)) if áÖä and getattr(áÖä[0], 't') == 'target_rhs' else ÂÚü()))
    if (getattr(áÕÉ, 'B') and lr) and rl:
        return (ll + [create_call(áÖü, áÓë(*lr), áÓë(*rl)), *áÑæ], rr)
    elif getattr(áÕÉ, 'S') and lr:
        return (ll + [create_call(áÖü, áÓë(*lr), áÓÆþáÓÍþáÓÄþáÓÄ), *áÑæ, *suf2(áÖä)], suffix(áÖä))
    elif getattr(áÕÉ, 'P') and rl:
        return (áÖÞ + [create_call(áÖü, áÓÆþáÓÍþáÓÄþáÓÄ, áÓë(*rl)), *áÑæ], rr)
    elif getattr(áÕÉ, 'N') and (getattr(áÕÉ, 'Ïë') or ((ÄÊDEL(1), False)[1] if ÄÊPSH(lr) else ÄÊPOP() if rl else (ÄÊDEL(1), True)[1])):
        return (áÖÞ + [create_call(áÖü, áÓÆþáÓÍþáÓÄþáÓÄ, áÓÆþáÓÍþáÓÄþáÓÄ) if getattr(áÕÉ, 'Ïë') else áÖü, *áÑæ, *suf2(áÖä)], áÖä)
    if getattr(áÕÉ, 'B'):
        if lr:
            return (ll + [create_call(áÖü, áÓë(*lr), áÓë(áÓéþáÓæ('⬤'))), *áÑæ], áÖä)
        if rl:
            return (áÖÞ + [create_call(áÖü, áÓë(áÓéþáÓæ('⬤')), áÓë(*rl)), *áÑæ], rr)
    áÍñþáÍñ(áÖü)
    ÂùÆ(False, 'Unable to apply operator %s: ll=%s; lr=%s; rl=%s; rr=%s' % (áÖü, ll, lr, rl, rr))

def parse_expr(ÄÕÒü):
    (ÄÊPSH(([], [*ÄÕÒü])), ((áÖÞ := ÄÊPKE(0)[0]), (áÖä := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    while áÖä:
        (c := getattr(áÖä, 'pop')(0))
        if IS_OP(c):
            (ÄÊPSH(apply_op(c, áÖÞ, áÖä)), ((áÖÞ := ÄÊPKE(0)[0]), (áÖä := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        else:
            getattr(áÖÞ, 'append')(c)
    return áÓë(*áÖÞ + áÖä)

def curry_ops(ÄÕÒü):

    @getattr(ÄÕÒü, 'ftrp')('∘', None, True)
    def _(ÄÕÒü):
        (Æå := (lambda ÂîÓ: getattr(ÂîÓ, 't') == '𝑣_spec' and getattr(ÂîÓ[0], 't') == '⬤'))
        (ÓÎ := (lambda ÂîÓ: getattr(ÂîÓ, 't') == 'kw_𝕒'))
        (Ëðá := (lambda ÂîÓ: ÓÎ(ÂîÓ) and Æå(ÂîÓ[1])))
        (C := ÁØò(lambda ÂîÓ: [ÂîÓ, 1] if Æå(ÂîÓ) else [áÓäþáÓé(+ÂîÓ[0]), -1] if Ëðá(ÂîÓ) else [áÓÜþáÓçþáÓØþáÓà(áÓäþáÓé(+ÂîÓ[0]), ÂîÓ[1]), 0] if ÓÎ(ÂîÓ) else [ÂîÓ, 0])(getattr(ÄÕÒü, 'c')))
        if getattr(ÄÕÒü[0], 't') == '𝗈𝗉':
            (ÄÊPSH(C), ÄÊPSH(slice(2, 2)), ÄÊPSH(ÁØò(lambda ÂîÓ: [áÓäþáÓé(getattr(ÂîÓ, 't')), -1] if ãÊú(ÂîÓ) == 1 and Æå(ÂîÓ[0]) else [áÓÜþáÓçþáÓØþáÓà(áÓäþáÓé(getattr(ÂîÓ, 't')), ÂîÓ[0]), 0])(ÄÔÔç(ÄÕÒü[0][2], ãÊú))), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        if not ÂØõ(ÁØò(lambda ÂîÓ: ÂîÓ[1])(C)):
            return ÄÕÒü
        (ÄÊPSH(MOD(ÂÚü, áØÁ=3)()), ((áÑõ := ÄÊPKE(0)[0]), (áÑð := ÄÊPKE(0)[1]), (áÑæ := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
        for c, k in C:
            if getattr(c, 't') == 'item':
                getattr(áÑð, 'append')(c)
            elif k == 0:
                getattr(áÑæ, 'append')(c)
            elif k == 1:
                (getattr(áÑõ, 'append')(áÓá(ãÊú(áÑæ))), getattr(áÑæ, 'append')(áÓéþáÓæ('⬤')))
            elif getattr(c, 't') == 'qvar':
                getattr(áÑõ, 'append')(c)
        if getattr(ÄÕÒü[0], 't') == '𝗈𝗉':
            getattr(ÄÕÒü[0][2], 'set')(c=ÂÚü())
        return áÓÕþáÓÓþáÓßþáÓß('þCUR', áÓÌ(*áÑõ), áÎô('𝐷', *áÑð), *áÑæ)

__file__='/home/ganer/Projects/Moon_BETA/Libraries/Compiler/lambdas.☾'
def Ïé_add_vk(ÄÕÒü, áÑæ='𝔸', áÑð='𝕂'):
    if 'VK' in getattr(ÄÕÒü, 'e'):
        return ÄÕÒü
    (ÄÊPSH((ÄÕÒü[0], MOD(ÄÝöË, áØÁ=2)(+ÄÕÒü[1]))), ((áÖâ := ÄÊPKE(0)[0]), (ÄÔÕý := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (cur := {*ÁØò(lambda ÂîÓ: (lambda ÂîÓ: ÂîÓ[-1] if ÂîÓ in ÂÛê('𝔸\u2009𝕂') else ÄÔýò)(getattr(ÂîÓ, 't')))(áÖâ)})
    if '𝔸' not in cur and áÑæ in ÄÔÕý:
        getattr(getattr(áÖâ, 'c'), 'append')(Æå_dec_áÑË(MOD(ÄÕéý, áØÁ=Âîì)(áÑæ, áÖâ)))
    if '𝕂' not in cur and áÑð in ÄÔÕý:
        getattr(getattr(áÖâ, 'c'), 'append')(Æå_dec_áÑÕ(MOD(ÄÕéý, áØÁ=Âîì)(áÑð, áÖâ)))
    (ÄÊPSH(getattr(ÄÕÒü, 'e')), ÄÊPSH('VK'), ÄÊPSH(True), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    return ÄÕÒü

def preformat_whiskers(ÄÕÒü):
    if getattr(ÄÕÒü[2], 't') == '✓':
        (ÄÊPSH(ÄÕÒü), ÄÊPSH(2), ÄÊPSH(MOD(ÄÕéý, áØÁ=ÂØÙ)(áÎô('𝑋↓↑'), ÄÕÒü[2])), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    (c := (getattr(ÄÕÒü[2], 't') == '𝑋𝐶' and getattr((áÎÎ := ÄÕÒü[2][0]), 't') in ÂÛê('𝑇↑\u2009slice')))
    if getattr(ÄÕÒü[1], 't') in 'ᑀᐵ\U000f7eb9\U000f7eba':
        if c:
            (áÕÃ := (áÕÃ if (getattr(áÎÎ[0], 't') == '𝑋↓↑' and ãÊú(áÎÎ[0])) and getattr((áÕÃ := áÎÎ[0][0]), 't') == 'slice' else áÎÎ))
        if c and getattr(áÕÃ[0], 't') == 'ᗜ':
            (ÄÊPSH(áÕÃ), ÄÊPSH(0), ÄÊPSH(áÎô('𝑋↓↑', áÓé(MOD(ÄÕéý, áØÁ=Âîë)('⟞', ÄÕÒü)))), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        elif c:
            getattr(getattr(áÕÃ[0], 'c'), 'insert')(0, áÓé(MOD(ÄÕéý, áØÁ=Âîë)('⟞', ÄÕÒü)))
        else:
            getattr(getattr(ÄÕÒü[2], 'c'), 'insert')(0, áÓé(MOD(ÄÕéý, áØÁ=Âîë)('⟞', ÄÕÒü)))
    if getattr(ÄÕÒü[3], 't') in 'ᑅᑈ\U000f7ebd\U000f7ebe':
        if c:
            (áÕÃ := (áÕÃ if (getattr(áÎÎ[-1], 't') == '𝑋↓↑' and ãÊú(áÎÎ[-1])) and getattr((áÕÃ := áÎÎ[-1][-1]), 't') == 'slice' else áÎÎ))
        if c and getattr(áÕÃ[-1], 't') == 'ᗜ':
            (ÄÊPSH(áÕÃ), ÄÊPSH(-1), ÄÊPSH(áÎô('𝑋↓↑', áÓé(MOD(ÄÕéý, áØÁ=Âîë)('⟝', ÄÕÒü)))), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        elif c:
            getattr(getattr(áÕÃ[-1], 'c'), 'append')(áÓé(MOD(ÄÕéý, áØÁ=Âîë)('⟝', ÄÕÒü)))
        else:
            getattr(getattr(ÄÕÒü[2], 'c'), 'append')(áÓé(MOD(ÄÕéý, áØÁ=Âîë)('⟝', ÄÕÒü)))
    return ÄÕÒü

def format_whiskers(ÄÕÒü):
    (ÄÊPSH(Áÿú(ÂÛê('ᑀᐵᐒᐖ\u2009\U000f7eb9\U000f7eba\U000f7ebb\U000f7ebc\u205fᑅᑈᐘᐛ\u2009\U000f7ebd\U000f7ebe\U000f7ebf\U000f7ec0'), Âåæ(ÂÑÖ(), ÂÛÅ))), ((tl := ÄÊPKE(0)[0]), (tr := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (ÄÊPSH(ÄÕÒü), ((lb := ÄÊPKE(0)[0]), (áÖù := ÄÊPKE(0)[1]), (áÖÔ := ÄÊPKE(0)[2]), (áØÀ := ÄÊPKE(0)[3]), (rb := ÄÊPKE(0)[4])), ÄÊDEL(1))[1]
    (ÄÊPSH((MOD(Áëý, áØÁ=+lb)(+áÖù, lambda ÂîÓ: tl[ÂîÓ]) or 'ᐳ', MOD(Áëý, áØÁ=+rb)(+áØÀ, lambda ÂîÓ: tr[ÂîÓ]) or 'ᐸ')), ((áÖù := ÄÊPKE(0)[0]), (áØÀ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (áÖü := getattr(áÎõ['␀TAC'], 'copy')())
    (ÄÊPSH(áÖü), ÄÊPSH('t'), ÄÊPSH(áÖù + áØÀ), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    (ÄÊPSH(áÖü), ÄÊPSH('L'), ÄÊPSH(getattr(áÖü, 'L') if áÖù in tl ** î else ÂÚü()), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    (ÄÊPSH(áÖü), ÄÊPSH('R'), ÄÊPSH(getattr(áÖü, 'R') if áØÀ in tr ** î else ÂÚü()), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    (ÄÊPSH(áÖü), ÄÊPSH('N'), ÄÊPSH((ÄÊPSH(áÖü), ÄÊPSH('Ïë'), ÄÊPSH((ÄÊPSH(áÖü), ÄÊPSH('ÏÁ'), ÄÊPSH(True), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    if áÖù != 'ᐳ':
        (ÄÊPSH(áÖü), ÄÊPSH('S'), ÄÊPSH(True), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    if áØÀ != 'ᐸ':
        (ÄÊPSH(áÖü), ÄÊPSH('P'), ÄÊPSH(True), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    if áÖù != 'ᐳ' and áØÀ != 'ᐸ':
        (ÄÊPSH(áÖü), ÄÊPSH('B'), ÄÊPSH(True), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    (ÂÑÕ := áÓâþáÓã(MOD(ÄÕéý, áØÁ=ÂØÙ)(getattr(áÖü, 't'), ÄÕÒü)))
    (ÄÊPSH(ÂÑÕ), ÄÊPSH('t'), ÄÊPSH(getattr(ÂÑÕ, 'e')), ÄÊPSH('O'), ÄÊPSH(('𝗈𝗉', áÖü)), (setattr(ÄÊPKE(4), ÄÊPKE(3), ÄÊPKE(0)[0]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)[1])), ÄÊDEL(5))[5]
    (ÄÊPSH(getattr(ÂÑÕ, 'e')), ÄÊPSH('k'), ÄÊPSH((0 if áÖù == 'ᐳ' else 1 if áÖù in 'ᑀᐒ\U000f7eb9\U000f7ebb' else 2, 0 if áØÀ == 'ᐸ' else 1 if áØÀ in 'ᑅᐘ\U000f7ebd\U000f7ebf' else 2)), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    (ÄÊPSH(áÖü), ÄÊPSH('t'), ÄÊPSH('␀T%s' % ((áÖù in 'ᑀᐵᐒᐖ') * '⟞' + '⟝' * (áØÀ in 'ᑅᑈᐘᐛ'),)), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    (ÄÊPSH((áÖù in 'ᑀᐵ\U000f7eb9\U000f7eba', áØÀ in 'ᑅᑈ\U000f7ebd\U000f7ebe')), ((il := ÄÊPKE(0)[0]), (ir := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (ÄÊPSH(ÂÑÕ), ÄÊPSH(1), ÄÊPSH(Ïé_add_vk(áÓßþáÓÓþáÓàþáÓÔ(MOD(ÄÕéý, áØÁ=Âîë)(áÓÙþáÓãþáÓÓþáÓåþáÓÓþáÓàþáÓæ(*ÁØò(lambda ÂîÓ: áÓé(MOD(ÄÕéý, áØÁ=Âîë)(ÂîÓ, áÖÔ)))((áÖù != 'ᐳ') * '⟞' + '⟝' * ('ᐸ' != áØÀ))), áÖÔ), getattr(áÖÔ, 'set')(t='x')), '𝓐', '𝓚')), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    if not ÂØõ(getattr(getattr(ÂÑÕ, 'e'), 'k')):
        return ÂÑÕ[1]
    return ÂÑÕ

def reformat_whiskers(ÄÕÒü):

    @getattr(ÄÕÒü, 'frp')(lambda ÂîÓ: (getattr(ÂîÓ, 't') == '∘' and getattr(ÂîÓ[0], 't') == '𝗈𝗉') and getattr(getattr(getattr(ÂîÓ[0], 'e'), 'O'), 't') in ÂÛê('␀T\u2009␀T⟞\u2009␀T⟝\u2009␀T⟞⟝'), None, True)
    def _(ÄÕÒü):
        (ÄÊPSH(ÄÕÒü), ((Æå := ÄÊPKE(0)[0]), (áÖí := ÄÊPKE(0)[1]), (áÖî := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
        (ÄÊPSH((áÖí != áÓÆþáÓÍþáÓÄþáÓÄ, áÖî != áÓÆþáÓÍþáÓÄþáÓÄ)), ((Ïß := ÄÊPKE(0)[0]), (Ïà := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        (ÄÊPSH(getattr(getattr(Æå, 'e'), 'k')), ((áÖù := ÄÊPKE(0)[0]), (áØÀ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        ÂùÆ(((ÄÊDEL(1), False)[1] if Ïß else ÄÊPOP()) if ÄÊPSH(not áÖù) else (ÄÊDEL(1), True)[1]) and (((ÄÊDEL(1), False)[1] if Ïà else ÄÊPOP()) if ÄÊPSH(not áØÀ) else (ÄÊDEL(1), True)[1])
        if (ÄÊDEL(1), False)[1] if ÄÊPSH(áÖù) else ÄÊPOP() if áØÀ else (ÄÊDEL(1), True)[1]:
            return Æå
        if not áÖù and 1 == áØÀ:
            return getattr(ÄÕÒü, 'set')(c=[Æå, áÖî]) if Ïà else Æå
        if áÖù == 1 and (not áØÀ):
            return getattr(ÄÕÒü, 'set')(c=[Æå, áÖí]) if Ïß else Æå
        if (((áÖù == ÄÊPSH(1) and ÄÊPOP() == ÄÊPSH(áØÀ)) and (ÄÊDEL(1) or True) or (ÄÊDEL(1) or False)) and Ïß) and Ïà:
            return ÄÕÒü
        if áÖù == 2 or áØÀ == 2:
            (Æå := áÎô('∘', áÓé((ÁØã, 'ᑀ', 'ᐵ')[áÖù] + (ÁØã, 'ᑅ', 'ᑈ')[áØÀ]), Æå))
        if (not áÖù or Ïß) and (not áØÀ or Ïà):
            return getattr(ÄÕÒü, 'set')(c=[Æå, *MOD(Âêà, áØÁ=Ïß)(áÖí), *MOD(Âêà, áØÁ=Ïà)(áÖî)])
        if ((ÄÊDEL(1), False)[1] if ÄÊPSH(áÖù) else ÄÊPOP() if áØÀ else (ÄÊDEL(1), True)[1]) and ((ÄÊDEL(1), False)[1] if ÄÊPSH(Ïß) else ÄÊPOP() if Ïà else (ÄÊDEL(1), True)[1]):
            return áÎô('∘', áÓé('CUR'), Æå)
        if áÖù and áØÀ:
            if (ÄÊDEL(1), False)[1] if ÄÊPSH(Ïß) else ÄÊPOP() if Ïà else (ÄÊDEL(1), True)[1]:
                return áÎô('∘', áÓé('CUR'), Æå)
            if (ÄÊDEL(1), False)[1] if ÄÊPSH(Ïß) else ÄÊPOP() if not Ïà else (ÄÊDEL(1), True)[1]:
                return áÎô('∘', áÓé('CURR'), Æå, áÖî)
            if (ÄÊDEL(1), False)[1] if ÄÊPSH(not Ïß) else ÄÊPOP() if Ïà else (ÄÊDEL(1), True)[1]:
                return áÎô('∘', áÓé('CUR'), Æå, áÖí)
        if ÄÝøø(áÖù, áØÀ) and ((ÄÊDEL(1), False)[1] if ÄÊPSH(Ïß) else ÄÊPOP() if Ïà else (ÄÊDEL(1), True)[1]):
            return áÎô('∘', áÓé('MOD'), Æå)
        ÂùÆ(False)

def rewrite_lambs(ÄÕÒü):
    getattr(ÄÕÒü, 'ftrp')('whiskers', format_whiskers, True)
    getattr(ÄÕÒü, 'ftrp')('lamb_h_preset', lambda ÄÕÒü: MOD(ÄÕéý, áØÁ=Âîì)(áÓÙþáÓãþáÓÓþáÓåþáÓÓþáÓàþáÓæ(*ÁØò(lambda ÂîÓ: áÓé(MOD(ÄÕéý, áØÁ=Âîì)(ÂîÓ, ÄÕÒü[0])))(ÄÝöÈ('xyzwvutsr', ÂóÍ(0, -1 + MOD(ÄÔÞÔ, ÁÜñ=ÄÕøü)('𝚲\U000f0c9f\U000f0ca1\U000f0ca3\U000f0ca5\U000f0ca7\U000f0ca9\U000f0cab\U000f0cad\U000f0caf\U000f0cb1', +ÄÕÒü[0]))))), ÄÕÒü[0]), True)
    getattr(ÄÕÒü, 'ftrp')('lamb_h_implicit', lambda ÄÕÒü: áÓÙþáÓãþáÓÓþáÓåþáÓÓþáÓàþáÓæ(áÓé(ÄÕÒü[0])), True)
    getattr(ÄÕÒü, 'ftrp')('lamb', Ïé_add_vk, True)

__file__='/home/ganer/Projects/Moon_BETA/Libraries/Compiler/rewriters.☾'
def rewrite_for(ÄÕÒü):
    getattr(ÄÕÒü, 'ftrp')('comp_∀', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(c=[MOD(ÄÕéý, áØÁ=ÂØÙ)(áÓÙþáÓâþáÓå(ÄÕÒü[0], ÄÕÒü[1], ÄÕÒü[2], ÄÕÒü[3] or áÓÒ), ÄÕÒü)]), True)
    getattr(ÄÕÒü, 'ftrp')('stmt_∀', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(c=[MOD(ÄÕéý, áØÁ=ÂØÙ)(áÓÙþáÓâþáÓå(áÓÒ, ÄÕÒü[0] or áÓÒ, ÄÕÒü[1] or áÓéþáÓæ('✓'), ÄÕÒü[2] or áÓÒ), ÄÕÒü)]), True)

def grp_blks(ÄÕÒü):
    (áÎÙ := (lambda x: lambda ÄÕÒü: ((getattr(ÄÕÒü, 't') == 'blk' and getattr(ÄÕÒü[0], 't') == 'stmt') and getattr(ÄÕÒü[0][0], 't') == 'blk_head') and (lambda ÂîÓ: getattr(ÂîÓ, 't') == 'stmt_∀' if x == '∀' else getattr(ÂîÓ[0][0], 't') == x)(ÄÕÒü[0][0][0])))

    @getattr(ÄÕÒü, 'ftrp')(ÂÛê('stmts\u2009blk'), None, True)
    def _(ÄÕÒü):
        return getattr(ÄÕÒü, 'set')(c=UGX_CREATE(('B', (àìÒ := []), '*', None, ('∨', ('B', (àìÒ := []), '', lambda ÂîÓ: áÎô('¿⸘¡', *ÂîÓ), ('∧', (áÎÙ('¿'), ''), (áÎÙ('⸘'), '*'), (áÎÙ('¡'), '?'))), ('B', (àìÒ := []), '', lambda ÂîÓ: áÎô('\ue00a¡\ue80d', *ÂîÓ), ('∧', (áÎÙ('\ue00a'), ''), (áÎÙ('¡'), '*'))), ('B', (àìÒ := []), '', lambda ÂîÓ: áÎô('∀¡', *ÂîÓ), ('∧', (áÎÙ('∀'), ''), (áÎÙ('¡'), '?'))), (ÃÆë, ''))))(getattr(ÄÕÒü, 'c')))
(part_cont := (lambda áüì, Æå: lambda x: UGX_CREATE(('B', (àìÒ := []), '*', None, ('∨', ('B', (àìÒ := []), '*', Æå, (áüì, '')), (ÃÆë, ''))))(x) or ÂÚü()))
(T1 := MOD(ÂÑÖ, áØÁ=None)()(ÄÕåØ('𝗮𝗯𝗳𝗻𝗿𝘁𝘃', [7, 8, 12, 10, 13, 9, 11])))

def map_special(x, ÄÕÒü=ÂÚü()):
    (T2 := getattr(ÁÜÙ, 'maketrans')(áÍÙ(ÄÕåØ('𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝗮𝗯𝗰𝗱𝗲𝗳', '0123456789abcdef'))))
    return áÓæþáÓçþáÓå(áÐè(MOD(ÄÕéý, áØÁ=ÂØÙ)(' ' if x else ÁØã, ÄÕÒü)) if x in '𝘀' else áÓæþáÓçþáÓåþáÓÔ(áÐè(MOD(ÄÕéý, áØÁ=ÂØÙ)(ÁÜÙ(T1[x] or MOD(ÄÝöì, áØÁ=16)(getattr(x, 'translate')(T2))), ÄÕÒü))))

def rewrite_strs(ÄÕÒü):
    getattr(ÄÕÒü, 'ftrp')('str_spec_char', lambda ÄÕÒü: map_special(+ÄÕÒü, ÄÕÒü))
    getattr(ÄÕÒü, 'ftrp')(ÂÛê('empty_str\u2009str_t\U000f09a5\u2009str_timp\u2009str_tsub\u2009str_nsub\u2009str_tsys_guts\u2009str_tsub_guts\u2009str_timp_guts\u2009str_nsub1_guts\u2009str_nsub2_guts\u2009str_escape'), lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(t='str'), True)
    getattr(ÄÕÒü, 'ftrp')('str', lambda ÄÕÒü: áÓæþáÓçþáÓå(*ÄÔÙù(ÁØò(lambda ÂîÓ: MOD(Áëý, áØÁ=lambda ÂîÓ: getattr(getattr(ÂîÓ, 'e'), 'T') or getattr(ÂîÓ, 't') != 'str')(ÂîÓ, Âêà))(ÄÕÒü))), True)
    getattr(ÄÕÒü, 'ftrp')('x', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(c=part_cont(lambda ÂîÓ: not getattr(getattr(ÂîÓ, 'e'), 'T') and getattr(ÂîÓ, 't') == 'str', lambda x: áÓæþáÓçþáÓå(*ÄÔÙù(x)))(ÄÕÒü)), True)
    getattr(ÄÕÒü, 'ftrp')('str', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(c=part_cont(lambda ÂîÓ: getattr(getattr(ÂîÓ, 'e'), 'T'), lambda x: áÐè(MOD(ÄÕéý, áØÁ=ÂØÙ)(Âøî(ÁÙÇ(lambda ÂîÒ: +ÂîÒ)(x)), x)))(ÄÕÒü)), True)

def rewrite_numbers(ÄÕÒü):
    getattr(ÄÕÒü, 'ftrp')('neg_num', lambda ÄÕÒü: áÓÚþáÓåþáÓã('()', áÓâþáÓã(MOD(ÄÕéý, áØÁ=Âîë)('¯', ÄÕÒü)), áÓá(MOD(ÄÕéý, áØÁ=ÂØÙ)(getattr(UPSIDEDOWNSYNDROME, 'flip')(+ÄÕÒü), ÄÕÒü))))
    getattr(ÄÕÒü, 'ftrp')('pos_num', áÓá)
    getattr(ÄÕÒü, 'ftrp')('number', MOD(ÁÛÛ, áØÁ=0))
    getattr(ÄÕÒü, 'ftrp')('number_exp', lambda ÄÕÒü: áÓÚþáÓåþáÓã('()', ÄÕÒü[0], áÓâþáÓã(MOD(ÄÕéý, áØÁ=Âîì)('⌃', ÄÕÒü[0])), áÓÚþáÓåþáÓã('()', *ÄÕÒü[1])), True)

def rewrite_ternary(ÄÕÒü):
    (is_xpr_atom := (lambda ÄÕÒü: getattr(ÄÕÒü, 't') == 'x'))

    @getattr(ÄÕÒü, 'ftrp')('opC', None, True)
    def _(ÄÕÒü):
        (ÄÊPSH(ÄÕÒü), ((áÖü := ÄÊPKE(0)[0]), *(Ïß := ÄÊPKE(0)[slice(1, None, None)])), ÄÊDEL(1))[1]
        if getattr(getattr(getattr(áÖü, 'e'), 'O'), 't') != '⭝' or ãÊú(áÖü[2]):
            return ÄÕÒü
        (ÄÊPSH(Ïß), ((Ïß := ÄÊPKE(0)[0]), *(Ïà := ÄÊPKE(0)[slice(1, None, None)])), ÄÊDEL(1))[1]
        (Ïá := Ïß[0])
        if (getattr(Ïá, 't') != 'opC' or getattr(getattr(getattr(Ïá[0], 'e'), 'O'), 't') != '⭜') or ãÊú(Ïá[0][2]):
            return ÄÕÒü
        return áÓçþáÓØþáÓåþáÓá(*Ïá[slice(1, None)], *Ïà)

    @getattr(ÄÕÒü, 'ftrp')('opC', None, True)
    def _(ÄÕÒü):
        (ÄÊPSH(ÄÕÒü), ((áÖü := ÄÊPKE(0)[0]), *(Ïß := ÄÊPKE(0)[slice(1, None, None)])), ÄÊDEL(1))[1]
        if (t := getattr(getattr(getattr(áÖü, 'e'), 'O'), 't')) not in '⭜⭝':
            return ÄÕÒü
        (ÄÊPSH(Ïß), ((Ïß := ÄÊPKE(0)[0]), (Ïà := ÄÊPKE(0)[1]), *(_ := ÄÊPKE(0)[slice(2, None, None)])), ÄÊDEL(1))[1]
        ÂùÆ(is_xpr_atom(Ïà))
        ÂùÆ(not ãÊú(áÖü[2]) or (ãÊú(áÖü[2]) == 1 and getattr(áÖü[2][0], 't') == '𝚜'))
        (áÑæ := (Ïà, áÖü[2][0][0] if ãÊú(áÖü[2]) else MOD(ÄÕéý, áØÁ=Âîì)(áÓë(áÓéþáÓæ('□')), ÄÕÒü)))
        return áÓçþáÓØþáÓåþáÓá(Ïß, *MOD(Áëý, áØÁ=t == '⭝')(áÑæ, ÂÀÇ))

def group_targets(ÄÕÒü):
    (dot := (lambda ÂîÓ: getattr(ÂîÓ, 't') == '𝗈𝗉' and getattr(ÂîÓ[1][0], 't') == '.'))
    (exp := (lambda ÂîÓ: getattr(ÂîÓ, 't') == 'exp'))
    (ÄÊPSH(MOD(ÂÚü, áØÁ=2)()), ((R := ÄÊPKE(0)[0]), (C := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (áÖï := getattr(ÄÕÒü, 'c'))

    def adds(x):
        if C:
            if ãÊú(C) == 1 and getattr(C[0], 't') == 'mcal':
                getattr(R, 'append')(*C[0])
            else:
                getattr(R, 'append')(áÎô('target_rhs', *C))
            getattr(C, 'clear')()
        if x is not None:
            getattr(R, 'append')(x)
    while áÖï:
        (v := getattr(áÖï, 'pop')(0))
        if getattr(v, 't') == '𝐿':
            getattr(C, 'append')(v)
        elif getattr(v, 't') == '𝑇':
            getattr(C, 'append')(áÓàþáÓÕþáÓÓþáÓß(v))
        elif dot(v):
            getattr(C, 'append')(áÓÓþáÓçþáÓçþáÓå((lambda ÂîÓ: áÓæþáÓçþáÓå(ÂîÓ) if getattr(ÂîÓ, 't') == '𝑣' else ÂîÓ)(getattr(áÖï, 'pop')(0))))
        elif exp(v):
            getattr(C, 'append')(áÓØþáÓëþáÓã(getattr(áÖï, 'pop')(0)))
        else:
            adds(v)
    adds(None)
    (ÄÊPSH(ÄÕÒü), ÄÊPSH('c'), ÄÊPSH(R), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    return ÄÕÒü

def regroup_elements(ÄÕÒü):
    (áüì := Âåæ(ÄÔÙù, MOD(ÁØò(lambda ÂîÓ: [áÓàþáÓÕþáÓÓþáÓß(ÂîÓ)] if getattr(ÂîÓ, 't') == '𝑇' else ÂîÓ if getattr(ÂîÓ, 't') == 'target_rhs' else [ÂîÓ]))))
    getattr(ÄÕÒü, 'ftrp')('x', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(c=ÂÕÅ(UGX_CREATE(('B', (àìÒ := []), '*', None, ('∨', ('B', (àìÒ := []), '', lambda x: áÎô('applier', *áüì(x)), ('∧', (lambda ÂîÓ: getattr(ÂîÓ, 't') != 'num', ''), (lambda ÂîÓ: getattr(ÂîÓ, 't') in '𝑇\u2009target_rhs', '+'))), (ÃÆë, '')))), getattr(ÄÕÒü, 'c')) or ÂÚü()), True)
    MOD(ÄÕéý, áØÁ=ÂØÙ)(getattr(ÄÕÒü, 'ftrp')('target_rhs', lambda ÄÕÒü: áÎô('applier', *ÄÕÒü), True), ÄÕÒü)

    def áÕá(áÖý, ÄÕÒü):
        if getattr(ÄÕÒü, 't') == 'mcal':
            return áÎô('∘', áÖý, *ÄÕÒü[0])
        if getattr(ÄÕÒü, 't') == '𝐿':
            return áÓÜ(áÖý, *ÄÕÒü)
        if getattr(ÄÕÒü, 't') == 'attr':
            return áÓÓ(áÖý, ÄÕÒü)
        if getattr(ÄÕÒü, 't') == 'exp':
            return áÎô('opC', áÓÇþáÓÈ('⌃'), áÖý, ÄÕÒü[0])
        ÂùÆ(False)
    getattr(ÄÕÒü, 'ftrp')('applier', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(c=[MOD(ÆÑ, áØÁ=áÓë(ÄÕÒü[0]))(getattr(ÄÕÒü, 'c')[slice(1, None)], áÕá)]), True)

def reduce_Ïð(ÄÕÒü):
    if not getattr((áÖü := getattr(getattr(ÄÕÒü[0], 'e'), 'O')), 'Ïð'):
        return ÄÕÒü
    (áÑæ := [ÄÕÒü[0]])
    for n in ÄÕÒü[slice(1, None)]:
        if (getattr(n, 't') == 'x' and ãÊú(n) == 1) and (lambda ÂîÓ: getattr(ÂîÓ, 't') == 'opC' and getattr(getattr(getattr(ÂîÓ[0], 'e'), 'O'), 't') == getattr(áÖü, 't'))(n[0]):
            getattr(áÑæ, 'extend')(n[0][slice(1, None)])
            continue
        getattr(áÑæ, 'append')(n)
    (ÄÊPSH(ÄÕÒü), ÄÊPSH('c'), ÄÊPSH(áÑæ), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    return ÄÕÒü

def add_cmp_op_chains(ÄÕÒü):
    for L in ÂÀÇ(áÖáþáÖæ):
        if not (áÖå := áÍè(ÁØò(lambda ÂîÓ: ÂîÓ[0] if ÂÔö(ÄÝöË(ÂîÓ[1]), 'λ') else ÄÔýò)(L))):
            continue
        (relv := (lambda ÂîÓ: áÖü if getattr(ÂîÓ, 't') == 'opC' and getattr((áÖü := getattr(getattr(ÂîÓ[0], 'e'), 'O')), 't') in áÖå else None))
        (charg := (lambda ÂîÓ: (ãÊú(ÂîÓ) == 1 and getattr(ÂîÓ, 't') == 'x') and relv(ÂîÓ[0])))

        @getattr(ÄÕÒü, 'ftrp')('opC', None, True)
        def _(ÄÕÒü):
            if not (áÖü := relv(ÄÕÒü)):
                return ÄÕÒü
            (ÄÊPSH(getattr(ÄÕÒü, 'c')), ÄÊPSH(slice(1, None)), ÄÊPSH(ÄÔÙù(ÁØò(lambda ÂîÓ: MOD(Áëý, áØÁ=charg)(ÂîÓ, [Âêà, MOD(ÁÛÛ, áØÁ=0)]))(getattr(ÄÕÒü, 'c')[slice(1, None)]))), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
            return ÄÕÒü
        getattr(ÄÕÒü, 'ftrp')('opC', lambda ÄÕÒü: getattr(ÄÕÒü, 'cp')(t='cmp') if relv(ÄÕÒü) else ÄÕÒü, True)
    return ÄÕÒü

def rewrite_cmp(ÄÕÒü):

    @getattr(ÄÕÒü, 'ftrp')('cmp', None, True)
    def _(ÄÕÒü):
        if ãÊú(ÄÕÒü) <= 3:
            return getattr(ÄÕÒü, 'set')(t='opC')
        (ÄÊPSH(áÇù(getattr(ÄÕÒü, 'c'), lambda ÂîÓ: getattr(ÂîÓ, 't') == '𝗈𝗉')), ((o := ÄÊPKE(0)[0]), (v := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        (ÄÊPSH(o), ÄÊPSH(ÂÀÇ(ÄÊPKE(0))), (o := ÄÊPKE(0)), ÄÊDEL(2))[2]
        (C := ÆÑ([áÓâþáÓãþáÒú(getattr(o, 'pop')(0), getattr(v, 'pop')(0), áÓÖ(getattr(v, 'pop')(0))), *ÁØò(lambda ÂîÓ: áÓâþáÓãþáÒú(getattr(o, 'pop')(0), ÐÌü(áÓã), áÓÖ(ÂîÓ)))(v)], lambda *áÑË: áÓâþáÓãþáÒú('∧', *áÑË)))
        return MOD(ÄÕéý, áØÁ=ÂØÙ)(áÓâþáÓãþáÒú('∨', áÓâþáÓãþáÒú('∧', getattr(ÄÕÒü, 'set')(t='opC', c=C), áÓâþáÓãþáÒú('∨', áÓå(1), áÓéþáÓæ('✓'))), áÓâþáÓãþáÒú('∨', áÓå(1), áÓéþáÓæ('✗'))), ÄÕÒü)

def rewrite_asgns(ÄÕÒü):
    getattr(ÄÕÒü, 'ftrp')('asgn', lambda ÄÕÒü: áÓë(áÓâþáÓãþáÒú(denode_op(áÓâþáÓã(MOD(ÄÕéý, áØÁ=ÂØØ)('≔', ÄÕÒü))), *ÄÕÒü)), True)
    ÁØò(lambda ÂîÓ: getattr(getattr(ÂîÓ, 'flat')(lambda ÂîÓ: getattr(ÂîÓ, 't') == 'x', False), 'flat')(lambda ÂîÓ: getattr(ÂîÓ, 't') == 'applier', False))(date_ÄÕÒü(lambda ÂîÓ: getattr(ÂîÓ, 't') in ÂÛê('asgn_targs\u2009asgn_targ'), 'x')(ÄÕÒü))
    (ÄÔöà := (lambda x, **áÑÕ: ÅÒ('\U000f0a08', e=MOD(ÂÑÖ, áØÁ=None)()(I=x, **áÑÕ))))
    (âÛ := (lambda x, **áÑÕ: ÅÒ('߷', e=MOD(ÂÑÖ, áØÁ=None)()(I=x, **áÑÕ))))

    def p(ÄÕÒü, áÎÄ, *áÖÛ, áÎÜþáÎØ=None):
        if getattr(ÄÕÒü, 't') in ÂÛê('x\u2009applier\u2009target_rhs'):
            return p(ÄÕÒü[0], áÎÄ, *áÖÛ, áÎÜþáÎØ=áÎÜþáÎØ)
        if getattr(ÄÕÒü, 't') == '𝗈𝗉':
            return áÎô('S𝑣', áÓé(ÄÕÒü[1][0]), ÄÔöà(áÖÛ))
        if getattr(ÄÕÒü, 't') == '𝑣':
            return áÎô('S𝑣', ÄÕÒü[0], ÄÔöà(áÖÛ))
        if getattr(ÄÕÒü, 't') == '𝑇':
            (i := MOD(Áëý, áØÁ=lambda ÂîÓ: ÂîÓ is None)(MOD(ÄÔÞÔ, ÁÜñ=ÄÕøü)(ÄÕÒü, lambda ÂîÓ: getattr(ÂîÓ, 't') == '𝔸' or ((getattr(ÂîÓ, 't') == 'x' and ãÊú(ÂîÓ) == 1) and getattr(ÂîÓ[0], 't') == '𝔸')), MOD(ÄÕÍÔ, áØÁ=ÂÕË)))
            return áÓÌ(*ËãÂ(ÂÓÏ(ÄÕÒü), lambda x, y: p(y, áÎÄ, *áÖÛ, x if x <= i else x - ãÊú(ÄÕÒü), áÎÜþáÎØ=ãÊú(ÄÕÒü))))
        if getattr(ÄÕÒü, 't') == '𝔸':
            return áÎô('𝔸', p(ÄÕÒü[0], áÎÄ, *áÖÛ[slice(None, -1)], slice(None) if (not áÖÛ or None is áÎÜþáÎØ) or áÎÜþáÎØ == 1 else slice(áÖÛ[-1], o if (o := (áÖÛ[-1] - áÎÜþáÎØ + 1)) else None)))
        if getattr(ÄÕÒü, 't') in '𝑖𝑎':
            getattr(áÎÄ, 'extend')(getattr(ÄÕÒü, 'c'))
            return áÎô('S' + getattr(ÄÕÒü, 't'), âÛ(ãÊú(áÎÄ) - 2), âÛ(ãÊú(áÎÄ) - 1), ÄÔöà(áÖÛ))
        ÂùÆ(False)

    @getattr(ÄÕÒü, 'frp')(lambda ÂîÓ: getattr(ÂîÓ, 't') == 'opC' and +ÂîÓ[0] in '≔\U000f7e09\U000f7e0a\U000f7e0b≕\U000f7e0e\U000f7e0c\U000f7e0d', None, True)
    def _(ÄÕÒü):
        (áÎÛ := ÄÕÒü[0])
        (áØÂ := getattr(áÎÛ[1][0], 't'))
        (ÄÊPSH((ÄÕÒü[1], ÄÕÒü[2]) if áØÂ in '≔\U000f7e09\U000f7e0a\U000f7e0b' else (ÄÕÒü[2], ÄÕÒü[1])), ((áÎÇ := ÄÊPKE(0)[0]), (áÍô := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        if (áØÂ in '≔≕' and getattr(áÎÇ, 't') == 'x') and ãÊú(áÎÇ) == 1:
            if getattr(áÎÇ[0], 't') == '𝑣':
                return áÓë(áÎô('S𝑣', áÎÇ[0], áÍô))
            if getattr(áÎÇ[0], 't') == '𝗈𝗉':
                return áÓë(áÎô('S𝑣', áÓé(áÎÇ[0][1][0]), áÍô))
        (áÍö := p(áÎÇ, (áÎÄ := ÂÚü())))
        (is_ref_áÍë := CURR(lambda ÂîÓ, ÂîÒ: getattr(ÂîÓ, 't') == '𝑣' and +ÂîÓ == ÂîÒ, getattr(getattr(áÎÛ, 'e'), 'áÖû')))
        (áÔê := (lambda ÄÕÒü, áÖõ: getattr(ÄÕÒü, 'ftrp')('\U000f0a08', lambda ÄÕÒü: MOD(ÆÑ, áØÁ=áÓà(áÐè(áÖõ)))(getattr(getattr(ÄÕÒü, 'e'), 'I'), CUR(lambda ÂîÓ, ÂîÒ: áÓÜ(ÂîÓ, áÓÓþáÓèþáÓçþáÓâ(ÂîÒ)))))))
        (áÔë := (lambda ÄÕÒü, ÏÁ: getattr(ÄÕÒü, 'ftrp')('߷', lambda ÄÕÒü: áÓà(áÐè(ÏÁ + ~getattr(getattr(ÄÕÒü, 'e'), 'I'))))))
        (áÎÞ := áÎô('𝑇'))
        if áØÂ in '\U000f7e09\U000f7e0a\U000f7e0b\U000f7e0e\U000f7e0c\U000f7e0d':
            (áÎÜ := getattr(ÐÌü(getattr(áÍö, 'cpr')), 'ftrp')(ÂÛê('S𝑣\u2009S𝑖\u2009S𝑎'), lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(t=getattr(ÄÕÒü, 't')[slice(1, None)], c=getattr(ÄÕÒü, 'c')[slice(None, -1)])))
            getattr(áÎÄ, 'append')(MOD(ÄÕéý, áØÁ=áÔë)(áÎÜ, ãÊú(áÎÄ)))
        if áØÂ in '\U000f7e0a\U000f7e0b':
            (áÍô := getattr(áÍô, 'frp')(is_ref_áÍë, lambda ÄÕÒü: áÓà(áÐè(0))))
        (áÍù := Áÿú(áÎÄ, áÓÖ))
        (áÍô := áÓÖ(áÍô))
        if áØÂ in '\U000f7e0c\U000f7e0d':
            (áÍô := getattr(áÍô, 'frp')(is_ref_áÍë, lambda ÄÕÒü: áÓÜ(áÓÌ(*áÍù), áÐè(ãÊú(áÍù) - 1))))
            getattr(getattr(áÎÞ, 'c'), 'append')(áÍô)
            getattr(getattr(áÎÞ, 'c'), 'append')(MOD(ÄÕéý, áØÁ=áÔë)(MOD(ÄÕéý, áØÁ=áÔê)(áÍö, 0), ãÊú(áÎÄ) + 1))
            if áØÂ == '\U000f7e0d':
                getattr(getattr(áÎÞ, 'c'), 'append')(áÓã(áÓá(1)))
            (áÍÿ := áÓÜ(áÎÞ, áÓá(ãÊú(áÎÞ) - 1)))
        else:
            if (r2l := ÂÔö('≕\U000f7e0e', áØÂ)):
                getattr(áÍù, 'insert')(0, áÍô)
            else:
                getattr(áÍù, 'append')(áÍô)
            getattr(getattr(áÎÞ, 'c'), 'extend')(áÍù)
            getattr(getattr(áÎÞ, 'c'), 'append')(MOD(ÄÕéý, áØÁ=áÔë)(MOD(ÄÕéý, áØÁ=áÔê)(áÍö, r2l * ãÊú(áÎÄ)), ãÊú(áÍù) - r2l))
            (áÍÿ := áÓÜ(áÎÞ, áÓá(ãÊú(áÎÄ) - 1 if áØÂ == '\U000f7e0b' else ãÊú(áÎÞ) + (áØÂ == '\U000f7e0e') + ~(2 * (áØÂ in '\U000f7e09\U000f7e0e')))))
        getattr(getattr(áÍÿ[0], 'c'), 'append')(áÓå(ãÊú(áÍù) - (áØÂ == '\U000f7e0d')))
        return áÍÿ

def add_short_circuits(ÄÕÒü):

    @getattr(ÄÕÒü, 'frp')(lambda ÂîÓ: (getattr(ÂîÓ, 't') == '∘' and getattr(ÂîÓ[0], 't') == '𝗈𝗉') and getattr(ÂîÓ[0][1][0], 't') in '\U000f7ea5\U000f7e92', None, True)
    def _(ÄÕÒü):
        (ÄÊPSH((ÄÕÒü[1], ÄÕÒü[2])), ((a := ÄÊPKE(0)[0]), (b := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        if getattr(ÄÕÒü[0][1][0], 't') == '\U000f7ea5':
            return áÓçþáÓØþáÓåþáÓá(áÓÖ(a), áÓÊ(áÓå(1), áÓéþáÓæ('✗')), áÓçþáÓØþáÓåþáÓá(b, ÐÌü(áÓã), áÓÊ(áÓå(1), áÓéþáÓæ('✓'))))
        else:
            return áÓçþáÓØþáÓåþáÓá(áÓÖ(a), áÓçþáÓØþáÓåþáÓá(b, áÓÊ(áÓå(1), áÓéþáÓæ('✗')), ÐÌü(áÓã)), áÓÊ(áÓå(1), áÓéþáÓæ('✓')))
        return ÄÕÒü
(part_ats := (lambda ÂîÓ: (getattr(ÂîÓ, 'copy')(c=(h := MOD(ÐÌÛ, áØÁ=áÍÖ)(getattr(ÂîÓ, 'c'), lambda ÂîÓ: getattr(ÂîÓ, 't')[-1] == '@'))[0]), áÍÙ(ÁØò(lambda ÂîÓ: (lambda ÂîÓ: (getattr(ÂîÓ, 't'), ÂîÓ))(getattr(ÂîÓ, 'copy')(t=getattr(ÂîÓ, 't')[slice(None, -1)])))(h[1])))))

def rewrite_ugex(ÄÕÒü):
    getattr(ÄÕÒü, 'flat')(lambda ÂîÓ: getattr(ÂîÓ, 't') in ÂÛê('ugx_and\u2009ugx_or') and ãÊú(ÂîÓ) == 1)
    getattr(ÄÕÒü, 'ftrp')('ugx_☾', lambda ÂîÓ: getattr(ÂîÓ, 'set')(t='𝑇', c=[ÂîÓ[0], áÓÓþáÓèþáÓçþáÓâ(ÁØã if ãÊú(ÂîÓ) <= 1 else +ÂîÓ[1])]), True)

    @getattr(ÄÕÒü, 'ftrp')(ÂÛê('ugx_paren\u2009ugx_brack'), None, True)
    def _(ÄÕÒü):
        (ÄÊPSH(part_ats(ÄÕÒü)), ((n := ÄÊPKE(0)[0]), (e := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        if ãÊú(n) > 1:
            (n := getattr(n, 'copy')(c=[áÎô('ugx_and', *n)]))
        (ÄÊPSH((getattr(e, 'get')('stk', áÎô('𝐿')), getattr(e, 'get')('apply', áÓéþáÓæ('□')))), ((b := ÄÊPKE(0)[0]), (c := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        (r := áÓÌ(áÓÓþáÓèþáÓçþáÓâ('BP'[getattr(n, 't') == 'ugx_paren']), áÎô('S𝑣', áÓé('\U0001cce8'), b), áÓÓþáÓèþáÓçþáÓâ((lambda ÂîÓ: ÂîÓ and +ÂîÓ)(getattr(e, 'get')('mod', ÁØã))), c, n))
        return r
    getattr(ÄÕÒü, 'ftrp')(ÂÛê('ugx_and\u2009ugx_or'), lambda ÄÕÒü: áÓÌ(áÓÓþáÓèþáÓçþáÓâ('∧∨'[getattr(ÄÕÒü, 't') == 'ugx_or']), *ÄÕÒü), True)
    getattr(ÄÕÒü, 'ftrp')('ugx_x', lambda ÄÕÒü: áÓÕþáÓÓþáÓßþáÓß('UGX_CREATE', *ÄÕÒü))

def rewrite_ports(ÄÕÒü):
    getattr(ÄÕÒü, 'ftrp')('str_timp_guts', lambda ÂîÓ: ÂåÔ(getattr(ÂîÓ[0], 'set')(t=getattr(getattr(ÂîÓ[0], 't'), 'rstrip')(' ')), ÂîÓ), True)
    getattr(ÄÕÒü, 'ftrp')('str_timp', lambda ÄÕÒü: áÓÕþáÓÓþáÓßþáÓß('__þIMPORT__', ÄÕÒü[0], ÐÌü(áÒÿ)), True)

    @getattr(ÄÕÒü, 'ftrp')('import', None, True)
    def _(ÄÕÒü):
        if ãÊú(ÄÕÒü) < 2:
            return ÄÕÒü
        ÁØò(lambda ÂîÓ: ÂîÓ if +ÂîÓ[-1] != '@' else ÂåÔ((ÄÊPSH(ÂîÓ), ÄÊPSH(1), ÄÊPSH(áÓÕþáÓÓþáÓßþáÓß(áÓÜ(ÐÌü(áÓà), áÓäþáÓé('__þGET_GLOB_MODNAME__')))), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3], getattr(ÂîÓ, 'set')(t=' ')) if ãÊú(ÂîÓ) == 2 else (ÄÊPSH(ÂîÓ), ÄÊPSH(0), ÄÊPSH(áÓÕþáÓÓþáÓßþáÓß(áÓÜ(ÐÌü(áÓà), áÓäþáÓé('__þSET_GLOB_MODNAME__')))), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3])(getattr(ÄÕÒü[1], 'c'))
        return áÓÜ(áÓÌ(áÓÖ(ÄÕÒü[0]), *ÁØò(lambda ÂîÓ: ÂîÓ if getattr(ÂîÓ[0], 't') == '∘' else áÓÕþáÓÓþáÓßþáÓß(ÐÌü(áÒÿ), '__þADDGLOBALS_CLEAN__', ÐÌü(áÓà)) if ãÊú(ÂîÓ) == 1 and +ÂîÓ == '*' else áÓë(áÓé(ÂîÓ[0][0]), áÓâþáÓã('≔'), ÂîÓ[1] if ãÊú(ÂîÓ) == 2 and getattr(ÂîÓ, 't') == ' ' else áÓÜ(ÐÌü(áÓà), MOD(Áëý, áØÁ=getattr(ÂîÓ[0], 't') == '𝑣')(ÂîÓ[ãÊú(ÂîÓ) - 1][0], áÓäþáÓé))))(getattr(ÄÕÒü[1], 'c')), ÐÌü(áÓã)), áÎô('neg_num', áÐè('\U000f7c3e')))
    getattr(ÄÕÒü, 'ftrp')('export', lambda ÄÕÒü: áÓÕþáÓÓþáÓßþáÓß('__þADD_EXPORTS__', ÐÌü(áÒÿ), *ÁØò(lambda ÂîÓ: áÓÌ(áÓäþáÓé(ÂîÓ[0]), ÂîÓ[ãÊú(ÂîÓ) - 1]))(getattr(ÄÕÒü[0], 'c'))), True)

__file__='/home/ganer/Projects/Moon_BETA/Libraries/Compiler/to_ast.☾'
(GRAM_PATH := '/home/ganer/Projects/Moon_BETA/Libraries/Compiler/gram')
(gram := gram_rp(ÄÔéÄ(ÂÛê('𝗐\u2009𝖶'), ÂÛê('𝘄?\u2009𝗪?'))(ÐØó(GRAM_PATH)), áÕÒ, False))
(gram_comm := gram_rp(gram, ÂÑÖ()(M=['comm'],I=['comment∨σscript∨']),True))
(gram_scrp := gram_rp(gram, ÂÑÖ()(M=['scrp'],I=['σscript∨']),True))
(gram_main := gram_rp(gram, ÂÑÖ()(M=['main'],I=['']),True))

def to_ast(áÖïþáÖüþáÖðþáÖñ, warn_short=True, trim_length_info=True, force_full_match=False, dbg_parser=0, dbg_show_gram_tree=False, **áÏè):
    (áÖïþáÖüþáÖðþáÖñ := (+getattr(gram_comm(áÖïþáÖüþáÖðþáÖñ, remove_trashes=False), 'ftrp')('comment', lambda ÂîÓ: ÂåÔ((ÄÊPSH(ÂîÓ[0]), ÄÊPSH('t'), ÄÊPSH(Âøî(ÁØò(lambda ÂîÓ: MOD(Áëý, áØÁ=ÄÊCUR((1,), {}, ÂÖÐ, ÂýÃ, '\n'))(ÂîÓ, MOD(ÄÕÍÔ, áØÁ=' ')))(getattr(ÂîÓ[0], 't')))), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3], ÂîÓ))))
    (ÄÊPSH(gram_subsup(áÖïþáÖüþáÖðþáÖñ, gram_scrp)), ((áÖï := ÄÊPKE(0)[0]), (ÏÆ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (ÄÕÒü := gram_main(áÖï, DEBUG=dbg_parser, remove_trashes=False))
    if dbg_show_gram_tree:
        áÍñþáÍñ(ÄÕÒü, 'Initial parse')
    if warn_short:
        warn_if_short(ÄÕÒü)
    if force_full_match and is_short(ÄÕÒü):
        return None
    ÏÆ(ÄÕÒü)

    def Æå(ÄÕÒü, ÏÁ=0):
        if getattr(getattr(ÄÕÒü, 'e'), 'T'):
            (ÄÊPSH(getattr(ÄÕÒü, 'e')), ÄÊPSH('p'), ÄÊPSH((ÏÁ, (ÄÊPSH(ÏÁ), ÄÊPSH(ÄÊPKE(0) - ÂÖë(î)(getattr(getattr(ÄÕÒü, 'e'), 'p'))), (ÏÁ := ÄÊPKE(0)), ÄÊDEL(2))[2])), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        elif getattr(ÄÕÒü, 't') in ÂÛê('SB\u2009SP\u2009SE'):
            (ÄÊPSH(getattr(ÄÕÒü, 'e')), ÄÊPSH('p'), ÄÊPSH((ÏÁ, ÏÁ)), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        else:
            (ÄÊPSH(getattr(ÄÕÒü, 'e')), ÄÊPSH('p'), ÄÊPSH((ÏÁ, (ÏÁ := MOD(ÆÑ, áØÁ=ÏÁ)(ÄÕÒü, ÂÕì(Æå))))), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        return ÏÁ
    Æå(ÄÕÒü)
    getattr(ÄÕÒü, 'rm')(lambda ÂîÓ: getattr(ÂîÓ, 't') in ÂÛê('SB\u2009SP\u2009SE'))
    (áÖï := (+ÄÕÒü))
    getattr(ÄÕÒü, 'rm')(lambda ÂîÓ: getattr(ÂîÓ, 't') in '\U000f01b4𝘄𝗪')
    reform_positions(ÄÕÒü, áÖï)
    if trim_length_info:
        del (getattr(ÄÕÒü, 'e')['parse_len'], getattr(ÄÕÒü, 'e')['input_len'])
    add_blocks(ÄÕÒü)
    rewrite_ports(ÄÕÒü)
    getattr(ÄÕÒü, 'ftrp')('𝐷', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(c=ÁØò(lambda ÂîÓ: áÓÜþáÓçþáÓØþáÓà(MOD(Áëý, áØÁ=ÂÔø(getattr(ÂîÓ[0], 't'), 'str'))(ÂîÓ[0], lambda ÂîÓ: getattr(ÂîÓ, 'set')(t='str')), ÂîÓ[1]) if getattr(ÂîÓ, 't') == '𝐷_kv_nam' else áÓÜþáÓçþáÓØþáÓà(*ÂîÓ) if getattr(ÂîÓ, 't') == '𝐷_kv_nrm' else ÂîÓ)(ÄÕÒü)), True)
    getattr(ÄÕÒü, 'ftrp')('str_tsub', rewrite_str_indent, True)
    getattr(ÄÕÒü, 'ftrp')('⊢_dec', lambda ÂîÓ: ÂåÔ(getattr(getattr(ÂîÓ, 'c')[-1], 'set')(t='ƒ_dec_params'), ÂîÓ), True)
    getattr(ÄÕÒü, 'ftrp')('whiskers', preformat_whiskers, True)
    getattr(ÄÕÒü, 'ftrp')(ÂÛê('𝑋𝐶\u2009𝑋↑↑\u2009𝑋↑↓\u2009𝑋↓↑\u2009𝑋↓↓\u2009𝝀𝑎'), lambda ÄÕÒü: MOD(ÄÕéý, áØÁ=ÂØÙ)(áÓë(*ÄÕÒü), ÄÕÒü), True)
    getattr(ÄÕÒü, 'ftrp')(ÂÛê('𝑃\u2009𝑇↑\u2009𝑇↓'), lambda ÄÕÒü: MOD(ÄÕéý, áØÁ=ÂØÙ)(ÅÒ('𝑇', *ÄÕÒü), ÄÕÒü), True)
    getattr(ÄÕÒü, 'ftrp')(ÂÛê('𝝀𝔸\u2009𝝀𝕂'), lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(t=getattr(ÄÕÒü, 't')[-1]), True)
    getattr(ÄÕÒü, 'frp')(lambda ÂîÓ: (getattr(ÂîÓ, 't') == '𝑇' and ãÊú(ÂîÓ) == 1) and getattr(ÂîÓ[0], 't') == 'comp_∀', lambda ÄÕÒü: MOD(ÄÕéý, áØÁ=ÂØÙ)(áÎô('𝐿', *ÄÕÒü), ÄÕÒü), True)
    rewrite_lambs(ÄÕÒü)
    rewrite_numbers(ÄÕÒü)

    @getattr(ÄÕÒü, 'frp')(lambda ÂîÓ: getattr(ÂîÓ, 't') == 'op' and +ÂîÓ[1] in '\U000f7e0a\U000f7e0b\U000f7e0c\U000f7e0d⭠⭢←→⬅➡⥉', None, True)
    def _(ÄÕÒü):
        (ÄÊPSH(ÄÕÒü), ((áÖù := ÄÊPKE(0)[0]), (áÖá := ÄÊPKE(0)[1]), (áØÀ := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
        (áÎÚ := áÓçþáÓàþáÓã(getattr(ÄÕÒü, 'copy')(c=getattr(áÓâþáÓã(áÖá), 'c'))))
        if +áÖá in '\U000f7e0a\U000f7e0b\U000f7e0c\U000f7e0d':
            (áØÄ := áÓé((ÄÊPSH(getattr(áÎÚ[0], 'e')), ÄÊPSH('áÖû'), ÄÊPSH('þ' + Âøî(getattr(getattr(ÄÕÒü, 'e'), 'p'), '_')), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]))
            getattr(getattr(áÎÚ, 'c'), 'append')(MOD(ÄÕéý, áØÁ=Âîì)(áØÄ, áÖá)) if +áÖá in '\U000f7e0a\U000f7e0b' else getattr(getattr(áÎÚ, 'c'), 'insert')(0, MOD(ÄÕéý, áØÁ=Âîë)(áØÄ, áÖá))
        if +áÖù:
            getattr(getattr(áÎÚ, 'c'), 'insert')(0, áÎô('sup', áÖù[0][0]))
        if +áØÀ:
            getattr(getattr(áÎÚ, 'c'), 'append')(áÎô('sup', áØÀ[0][0]))
        return áÎÚ
    getattr(ÄÕÒü, 'ftrp')('sup', lambda ÄÕÒü: áÓçþáÓàþáÓã(áÓâþáÓã(MOD(ÄÕéý, áØÁ=Âîë)('.', ÄÕÒü)), ÄÕÒü[0][0]) if (getattr(ÄÕÒü[0], 't') == 'x' and ãÊú(ÄÕÒü[0]) == 1) and getattr(ÄÕÒü[0][0], 't') == '𝑣' else áÓçþáÓàþáÓã(áÓØþáÓëþáÓã(ÄÕÒü), áÓë(*ÄÕÒü)), True)
    getattr(ÄÕÒü, 'flat')(lambda ÂîÓ: getattr(ÂîÓ, 't') == 'tmp')
    getattr(ÄÕÒü, 'ftrp')('op', denode_op, True)
    getattr(ÄÕÒü, 'ftrp')('x', group_targets, True)
    rewrite_for(ÄÕÒü)
    grp_blks(ÄÕÒü)
    rewrite_strs(ÄÕÒü)
    flatten_statments(ÄÕÒü)
    getattr(ÄÕÒü, 'ftrp')('x', lambda ÄÕÒü: parse_expr(ÄÕÒü), True)
    getattr(ÄÕÒü, 'rm')(lambda ÂîÓ: ((getattr(ÂîÓ, 't') == 'opC' and +ÂîÓ[0][1] == '␀CAT') and ((getattr(ÂîÓ[1], 't') == ÄÊPSH(getattr(ÂîÓ[2], 't')) and ÄÊPOP() == ÄÊPSH('𝑣')) and (ÄÊDEL(1) or True) or (ÄÊDEL(1) or False))) and ((+ÂîÓ[1] == ÄÊPSH(+ÂîÓ[2]) and ÄÊPOP() == ÄÊPSH('NULL')) and (ÄÊDEL(1) or True) or (ÄÊDEL(1) or False)))
    getattr(ÄÕÒü, 'ftrp')('x', lambda ÄÕÒü: getattr(ÄÕÒü, 'copy')(c=ÄÔÙù(ÁØò(lambda ÂîÓ: MOD(Áëý, áØÁ=lambda ÂîÓ: getattr(ÂîÓ, 't') != 'x')(ÂîÓ, Âêà))(ÄÕÒü))), True)
    getattr(ÄÕÒü, 'ftrp')('X', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(t='x'), True)
    getattr(ÄÕÒü, 'ftrp')('opC', reduce_Ïð, True)
    add_cmp_op_chains(ÄÕÒü)
    rewrite_ternary(ÄÕÒü)
    regroup_elements(ÄÕÒü)
    rewrite_asgns(ÄÕÒü)
    rewrite_cmp(ÄÕÒü)
    getattr(ÄÕÒü, 'frp')(lambda ÂîÓ: getattr(ÂîÓ, 't') == 'opC' and +ÂîÓ[0] == '⋄', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(t='𝐿', c=getattr(ÄÕÒü, 'c')[slice(1, None)]), pre=True)
    getattr(ÄÕÒü, 'frp')(lambda ÂîÓ: getattr(ÂîÓ, 't') == 'opC' and +ÂîÓ[0][1][0] == ',', lambda ÄÕÒü: áÎô('𝑇', *ÄÕÒü[slice(1, None)]))
    (squashcat := (lambda ÄÕÒü: ÄÕÒü[0] if ãÊú(ÄÕÒü) == 1 else ÆÑ(getattr(ÄÕÒü, 'c'), lambda x, y: áÓâþáÓãþáÒú(denode_op(áÓâþáÓã(MOD(ÄÕéý, áØÁ=Âîì)('␀CAT', x))), x, y))))
    (squashmul := (lambda ÄÕÒü: ÄÕÒü[0] if ãÊú(ÄÕÒü) == 1 else ÆÑ(getattr(ÄÕÒü, 'c'), lambda x, y: áÓÕþáÓÓþáÓßþáÓß(denode_op(áÓâþáÓã(MOD(ÄÕéý, áØÁ=Âîì)('⋅', x))), x, y))))
    getattr(ÄÕÒü, 'ftrp')('x', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(c=ÂÕÅ(part_cont(lambda ÂîÓ: getattr(ÂîÓ, 't') in ÂÛê('𝐿\u2009𝑇\u2009str\u2009num'), lambda x: áÎô('⋅', *x)), getattr(ÄÕÒü, 'c'))), True)
    getattr(ÄÕÒü, 'ftrp')('x', squashcat, True)
    getattr(ÄÕÒü, 'ftrp')('opC', lambda ÂîÓ: getattr(ÂîÓ, 'set')(t='∘'), True)
    getattr(ÄÕÒü, 'ftrp')('⋅', squashmul, True)
    reformat_whiskers(ÄÕÒü)
    getattr(ÄÕÒü, 'frp')(lambda ÂîÓ: getattr(ÂîÓ, 't') == '𝑇' and ãÊú(ÂîÓ) == 1, lambda ÄÕÒü: MOD(ÄÕéý, áØÁ=ÂØÙ)(áÎô('𝑃', *ÄÕÒü), ÄÕÒü), True)
    getattr(ÄÕÒü, 'frp')(lambda ÂîÓ: getattr(ÂîÓ, 't') == '𝑇', lambda ÂîÓ: getattr(ÂîÓ, 'set')(c=getattr(ÂîÓ, 'c')[slice(None, -1)]) if ÂîÓ and getattr(ÂîÓ[-1], 't') == 'ᗜ' else ÂîÓ, True)
    getattr(ÄÕÒü, 'ftrp')('ᗜ', lambda x: MOD(ÄÕéý, áØÁ=ÂØÙ)(áÓéþáÓæ('□'), x))
    add_short_circuits(ÄÕÒü)
    curry_ops(ÄÕÒü)
    rewrite_ugex(ÄÕÒü)
    getattr(ÄÕÒü, 'ftrp')('∘', lambda ÄÕÒü, *áÑË: getattr(ÄÕÒü, 'set')(c=[ÄÕÒü[0], *ÁØò(lambda ÂîÓ: ÂîÓ[0] if (getattr(ÂîÓ, 't') == '𝑃' and ãÊú(ÂîÓ[0]) == 1) and getattr(ÂîÓ[0], 't') == '𝔸' else ÂîÓ)(ÄÕÒü[slice(1, None)])]), True)
    return ÄÕÒü
(__exports__ := ÂÛê('to_ast'))

__file__='/home/ganer/Projects/Moon_BETA/Libraries/Compiler/ast_to_py.☾'
from unicodedata import is_normalized
from keyword import kwlist
(áÌÐ := ÂÑÖ()(áÍë_spec=ÂÞÅCAT(ÂÛê('✓\u2009True\u205f✗\u2009False\u205f□\u2009None'), ÂÑÖ()), std_kwd=ÂÞÅCAT(ÂÛê('↪\u2009return\u205f⮂\u2009yield\u205f\U000f01b4\u2009del\u205f↺\u2009continue\u205f⇥\u2009break'), ÂÑÖ()), blk_cln_kwd=ÂÞÅCAT(ÂÛê('¿\u2009if\u205f⸘\u2009elif\u205f¡\u2009else\u205f∀\u2009for\u205f\U000f1018\u2009class'), ÂÑÖ()), blk_kwd=ÂÞÅCAT(MOD(ÂÛê, áØÁ='\u205f\u2009')('\ue00a\u2009try'), ÂÑÖ()), op=ÂÞÅCAT(ÐÈÔ('~~%%^^&&||>><<++¯---⋅*÷/', [2]) + ÂÛê('⹏\u2009//\u205f⌃\u2009**\u205f≥\u2009>=\u205f≤\u2009<=\u205f≡\u2009==\u205f≠\u2009!=\u205f∨\u2009or\u205f∧\u2009and\u205f∨\u2009or\u205f¬\u2009not\u205f∈\u2009in\u205f∉\u2009not in\u205f≅\u2009is\u205f≇\u2009is not'), ÂÑÖ())))
(ENC := 'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýÿ')
(RCD := CURR(lambda ÂîÓ, ÂîÒ: ÂÖõ(ÂîÓ, ÂîÒ), abcABC123 + '_'))
(SPE := CURR(lambda ÂîÓ, ÂîÒ: ÂÖó(ÂîÓ, ÂîÒ), ENC + 'þ'))
(enc := (lambda ÂîÓ: Âøî(ÁØò(lambda ÂîÓ: ÄÝöì(ÄÝöí(ÂîÓ), ãÊú(ENC), C=ENC))(ÂîÓ), 'þ')))
(dec := Âåæ(Âøî, lambda ÂîÓ: ÁØò(lambda ÂîÓ: ÄÝöí(ÄÝöì(ÂîÓ, ãÊú(ENC), C=ENC)))(ÄÝöÞ(ÂîÓ, 'þ'))))
(PEV := Âåæ(Âøî, lambda ÂîÓ: MOD(ÄÔÔç, áØÁ=enc)(áÇù(ÂîÓ, RCD), RCD)))
(VEP := Âåæ(Âøî, lambda ÂîÓ: MOD(ÄÔÔç, áØÁ=lambda ÂîÓ: MOD(Áëý, áØÁ=SPE)(ÂîÓ, ÄÔâÑ(dec, lambda x: '⸮%s?' % (x,))))(áÇù(ÂîÓ, SPE), SPE)))
(py_esc_str := Âåæ(Âøî, MOD(ÁØò(lambda ÂîÓ: '\\u%s' % (MOD(ÄÝöì, áØÁ=16 + ÂÞÅCAT(4, Ãù))(ÄÝöí(ÂîÓ)),) if ÂîÓ in áÍè('\n\t\\\'"{}') else ÂîÓ))))
(áÓÄ := (lambda x=ÁØã, y=4 * ' ': Âøî(Áÿú(lines(x), ÄÊCUR((2,), {}, ì, y, ÂýÃ)), '\n')))

def expand_ast_py(ÄÕÒü, PEV=PEV):
    if getattr(getattr(ÄÕÒü, 'e'), 'T'):
        return ÄÕÒü
    if getattr(ÄÕÒü, 't') == '𝗈𝗉':
        if (m := ÄÔÙù(ÄÕÒü[0], ÄÕÒü[2])):
            (t := MOD(ÂÑÖ, áØÁ=[])()(ÐÌÛ(m, lambda ÂîÓ: 1 if getattr(ÂîÓ, 't') in áÍè('≺≻ᵜ꜠') else 2 if getattr(ÂîÓ, 't') in áÍè('ᔨ') else 0 if getattr(ÂîÓ, 't') in '𝚜' else ÄÔýò)))
            (a := (t[0] if ãÊú(t[0]) == 1 else [áÐè('('), *Âøî(t[0], áÐè(',')), áÐè(')')] if ãÊú(t[0]) else ÂÚü()))
            (áÑæ := ÁØò(lambda ÂîÓ: áÓë(áÓé(getattr(ÂîÓ, 't')), áÐè('='), ÂîÓ[0] if ãÊú(ÂîÓ) else áÓé('\U000f18e9')))(([áÎô('𝚜', áÓë(*a))] if a else ÂÚü()) + t[2]))
            (ÄÊPSH(ÄÕÒü), ÄÊPSH(1), ÄÊPSH(MOD(ÆÑ, áØÁ=ÄÕÒü[1])(t[1], CUR(lambda ÂîÓ, ÂîÒ: áÓÕþáÓÓþáÓßþáÓß(getattr(ÂîÒ, 't'), ÂîÓ)))), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
            (ÄÕÒü := (áÓÕþáÓÓþáÓßþáÓß(áÐè('MOD'), ÄÕÒü[1], *áÑæ) if áÑæ else ÄÕÒü[1]))
    if getattr(ÄÕÒü, 't') in ÂÛê('𝑇\u2009ƒ_dec_params'):
        getattr(ÄÕÒü, 'set')(c=[áÐè('('), *MOD(ÄÕéý, áØÁ=ÂîË if getattr(ÄÕÒü, 't') == '𝑇' and ãÊú(ÄÕÒü) == 1 else Âøî)(getattr(ÄÕÒü, 'c'), áÐè(',')), áÐè(')')])
    elif getattr(ÄÕÒü, 't') in '𝑆𝐷':
        if getattr(ÄÕÒü, 't') == '𝐷':
            for c in ÄÕÒü:
                if getattr(c, 't') != '𝔸':
                    continue
                getattr(c, 'set')(t='𝕂', c=[áÓÕþáÓÓþáÓßþáÓß('dict', *c)])
        getattr(ÄÕÒü, 'set')(c=[áÐè('{'), *Âøî(getattr(ÄÕÒü, 'c'), áÐè(',')), áÐè('}')])
    elif getattr(ÄÕÒü, 't') == '𝑃':
        getattr(ÄÕÒü, 'set')(c=[áÐè('('), *Âøî(getattr(ÄÕÒü, 'c'), áÐè(',')), áÐè(')')])
    elif getattr(ÄÕÒü, 't') == '𝐿':
        getattr(ÄÕÒü, 'set')(c=[áÐè('['), *Âøî(getattr(ÄÕÒü, 'c'), áÐè(',')), áÐè(']')])
    elif getattr(ÄÕÒü, 't') == '𝑖':
        getattr(ÄÕÒü, 'set')(c=[ÄÕÒü[0], áÐè('['), *Âøî(ÄÕÒü[slice(1, None)], áÐè(',')), áÐè(']')])
    elif getattr(ÄÕÒü, 't') == '∘':
        (áÖò := ÄÕÒü[0])
        if (getattr(áÖò, 't') == '𝗈𝗉' and +áÖò[1] in getattr(áÌÐ, 'op')) and ((ÄÊDEL(1), False)[1] if ÄÊPSH(ãÊú(áÖò[0])) else ÄÊPOP() if ãÊú(áÖò[2]) else (ÄÊDEL(1), True)[1]):
            (p := (ãÊú(ÄÕÒü) < 3 and getattr((ÂÑÕ := getattr(getattr(áÖò, 'e'), 'O')), 'r') or +áÖò in '¯¬~'))
            getattr(ÄÕÒü, 'set')(c=[áÐè('('), *MOD(Áëý, áØÁ=p)([ÄÕÒü[1], áÖÊ, getattr(áÖò[1][0], 'set')(t=getattr(áÌÐ, 'op')[+áÖò])], ÂÀÇ), áÖÊ, *ÄÕÒü[slice(2, None)], áÐè(')')])
        else:
            getattr(ÄÕÒü, 'set')(c=[áÖò, áÐè('('), *Âøî(getattr(ÄÕÒü, 'c')[slice(1, None)], áÐè(',')), áÐè(')')])
    elif getattr(ÄÕÒü, 't') == '\U000f7e57':
        getattr(ÄÕÒü, 'set')(c=[áÓÕþáÓÓþáÓßþáÓß('þPSH', *ÄÕÒü)])
    elif getattr(ÄÕÒü, 't') == '⍖':
        getattr(ÄÕÒü, 'set')(c=[áÓÕþáÓÓþáÓßþáÓß('þPKE', *ÄÕÒü)])
    elif getattr(ÄÕÒü, 't') == '\U000f7e58':
        getattr(ÄÕÒü, 'set')(c=[áÓÕþáÓÓþáÓßþáÓß('þPOP', *ÄÕÒü)])
    elif getattr(ÄÕÒü, 't') == '𝑎':
        getattr(ÄÕÒü, 'set')(c=[áÓÕþáÓÓþáÓßþáÓß('getattr', *ÄÕÒü)])
    elif getattr(ÄÕÒü, 't') == 'S𝑎':
        getattr(ÄÕÒü, 'set')(c=[áÓÕþáÓÓþáÓßþáÓß('setattr', *ÄÕÒü)])
    elif getattr(ÄÕÒü, 't') == 'S𝑖':
        getattr(ÄÕÒü, 'set')(c=[áÓÕþáÓÓþáÓßþáÓß('setitem', *ÄÕÒü)])
    elif getattr(ÄÕÒü, 't') == 'S𝑣':
        getattr(ÄÕÒü, 'set')(c=[áÓÚþáÓåþáÓã('()', áÓé(ÄÕÒü[0]), áÐè(':='), ÄÕÒü[1])])
    elif getattr(ÄÕÒü, 't') == 'str':
        (sn := (lambda ÂîÓ: not getattr(getattr(ÂîÓ, 'e'), 'T') and getattr(ÂîÓ, 't') == 'str_sub'))
        (ÄÊPSH(MOD(ÐÌÛ, áØÁ=áÍÖ)(getattr(ÄÕÒü, 'c'), sn)), ((Ïß := ÄÊPKE(0)[0]), (Ïà := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        getattr(ÄÕÒü, 'set')(c=[áÐè('("'), *ÁØò(lambda ÂîÓ: getattr(ÂîÓ, 'set')(t=py_esc_str(+ÂîÓ)) if getattr(getattr(ÂîÓ, 'e'), 'T') else áÐè('%s') if sn(ÂîÓ) else ÂîÓ)(ÄÕÒü), áÐè('")'), *([áÐè('%('), *ÂîË(Ïà, áÐè(',')), áÐè(')')] if Ïà else ÂÚü())])
    elif getattr(ÄÕÒü, 't') == 'strb':
        getattr(ÄÕÒü, 'set')(c=[áÐè('\\x%s' % (MOD(ÄÝöì, áØÁ=16 + ÂÞÅCAT(2, Ãù))(ÄÝöì(+ÄÕÒü)),))])
    elif getattr(ÄÕÒü, 't') == '𝑣_spec':
        getattr(ÄÕÒü, 'set')(c=[MOD(ÄÕéý, áØÁ=ÂØÙ)(áÓé(getattr(getattr(áÌÐ, 'áÍë_spec'), 'get')(+ÄÕÒü, +ÄÕÒü)), ÄÕÒü)])
    elif getattr(ÄÕÒü, 't') == '𝔸':
        getattr(ÄÕÒü, 'set')(c=[áÐè('*'), *(Âêà(áÓé(ÄÕÒü[0])) if getattr(getattr(ÄÕÒü[0], 'e'), 'T') else Âêà(ÄÕÒü[0]) if getattr(ÄÕÒü[0], 't') == '𝑣' else [áÐè('('), *ÄÕÒü, áÐè(')')])])
    elif getattr(ÄÕÒü, 't') == '𝕂':
        getattr(ÄÕÒü, 'set')(c=[áÐè('**'), *(Âêà(áÓé(ÄÕÒü[0])) if getattr(getattr(ÄÕÒü[0], 'e'), 'T') else Âêà(ÄÕÒü[0]) if getattr(ÄÕÒü[0], 't') == '𝑣' else [áÐè('('), *ÄÕÒü, áÐè(')')])])
    elif getattr(ÄÕÒü, 't') in ÂÛê('𝑣\u2009op_lit\u2009ƒ_𝑣'):
        getattr(ÄÕÒü, 'set')(c=[MOD(ÄÕéý, áØÁ=ÂØÙ)(áÐè(MOD(Áëý, áØÁ=lambda ÂîÓ: ÂîÓ in ÂÕÃ(kwlist, ÂÛê('False\u2009None\u2009True')))(PEV(+ÄÕÒü), ÄÊCUR((1,), {}, ì, ÂýÃ, '_'))), ÄÕÒü)])
    elif getattr(ÄÕÒü, 't') == 'qvar':
        getattr(ÄÕÒü, 'set')(c=[MOD(ÄÕéý, áØÁ=ÂØÙ)(áÐè('"%s"' % (PEV(+ÄÕÒü),)), ÄÕÒü)])
    elif getattr(ÄÕÒü, 't') == '𝝀𝑃':
        getattr(ÄÕÒü, 'set')(c=Âøî(ÄÕÒü, áÐè(',')))
    elif getattr(ÄÕÒü, 't') in '𝝀eq\u2009kw_𝕒':
        (ÄÊPSH(ÄÕÒü), ÄÊPSH(0), ÄÊPSH(áÓé(ÄÕÒü[0])), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        getattr(ÄÕÒü, 'set')(c=Âøî(getattr(ÄÕÒü, 'c'), áÐè('=')))
    elif getattr(ÄÕÒü, 't') == '⊢_dec':
        getattr(ÄÕÒü, 'set')(c=[*([áÐè('@'), ÄÕÒü[0], áÐè('\n')] if +ÄÕÒü[0] else ÂÚü()), áÐè('def '), ÄÕÒü[1] if +ÄÕÒü[1] else áÓé('_'), ÄÕÒü[2] if +ÄÕÒü[2] else áÐè('()'), áÐè(':')])
    elif getattr(ÄÕÒü, 't') == 'stmt_∀':
        getattr(ÄÕÒü, 'set')(c=(lambda ÂîÓ: [*([áÐè('while(')] if ÂîÓ[1] & áÓÒ else [áÐè('for '), ÂîÓ[1], áÐè(' in(')]), ÂîÓ[2], áÐè('):'), *(ÂÚü() if ÂîÓ[3] & áÓÒ else [áÐè('\n'), áÐè(áÓÄ('if not(')), ÂîÓ[3], áÐè('):continue')])])(ÄÕÒü[0]))
    elif getattr(ÄÕÒü, 't') == 'comp_∀':
        getattr(ÄÕÒü, 'set')(c=(lambda ÂîÓ: [áÐè('('), ÂîÓ[0], áÐè(')for '), ÂîÓ[1], áÐè(' in('), ÂîÓ[2], áÐè(')'), *(ÂÚü() if ÂîÓ[3] & áÓÒ else [áÐè('if('), ÂîÓ[3], áÐè(')')])])(ÄÕÒü[0]))
    elif getattr(ÄÕÒü, 't') == 'tern':
        getattr(ÄÕÒü, 'set')(c=[áÐè('(('), ÄÕÒü[1], áÐè(')if('), ÄÕÒü[0], áÐè(')else('), ÄÕÒü[2], áÐè('))')])
    elif getattr(ÄÕÒü, 't') == 'lamb':
        getattr(ÄÕÒü, 'set')(c=[áÐè('(lambda '), *Âøî(getattr(ÄÕÒü[0], 'c'), áÐè(',')), áÐè(':'), ÄÕÒü[1], áÐè(')')])
    elif getattr(ÄÕÒü, 't') == 'item':
        getattr(ÄÕÒü, 'set')(c=[ÄÕÒü[0], áÐè(':'), ÄÕÒü[1]])
    elif getattr(ÄÕÒü, 't') == 'slice':
        getattr(ÄÕÒü, 'set')(c=[áÓÕþáÓÓþáÓßþáÓß('slice', *(lambda ÂîÓ: Æå(ÄÕÒü[0]) * [áÓéþáÓæ('□')] + ÂîÓ + [áÓéþáÓæ('□')] * Æå(ÄÕÒü[-1]))(ÄÔÙù(ÁØò(lambda ÂîÓ: MOD(Âêà, áØÁ=ãÊú(ÂîÓ) - 1)(áÓéþáÓæ('□')) if Æå(ÂîÓ[0]) else ÂîÓ)(áÇù(getattr(ÄÕÒü, 'c'), (Æå := (lambda ÂîÓ: getattr(ÂîÓ, 't') == ':')))))))])
    elif getattr(ÄÕÒü, 't') == '\ue00a¡\ue80d':
        getattr(getattr(ÄÕÒü[0][0], 'c'), 'append')(áÐè(':'))
        if ãÊú(ÄÕÒü) > 1:
            ÁØò(lambda ÂîÓ: getattr(ÂîÓ[0][0][0][0], 'set')(t='except'))(ÄÕÒü[slice(1, None)])
        else:
            getattr(getattr(ÄÕÒü, 'c'), 'append')(áÐè('except:pass'))
    elif getattr(ÄÕÒü, 't') in ÂÛê('std_kwd\u2009blk_cln_kwd\u2009blk_kwd'):
        getattr(ÄÕÒü[0], 'set')(t=getattr(áÌÐ[getattr(ÄÕÒü, 't')], 'get')(+ÄÕÒü, +ÄÕÒü))
        getattr(getattr(ÄÕÒü, 'c'), 'insert')(1, áÖÊ)
    elif getattr(ÄÕÒü, 't') == 'cln_pfx':
        if getattr(ÄÕÒü[0], 't') != 'std_kwd':
            getattr(getattr(ÄÕÒü, 'c'), 'append')(áÐè(':'))
    elif getattr(ÄÕÒü, 't') == 'stmts':
        getattr(ÄÕÒü, 'set')(c=ÂîË(getattr(ÄÕÒü, 'c'), MOD(ÄÕÍÔ, áØÁ=áÐè('\n'))))
    elif getattr(ÄÕÒü, 't') == 'blk':
        (ÄÊPSH((lambda x: expand_ast_py(x, PEV), '\n' + áÓÄ())), ((P := ÄÊPKE(0)[0]), (d := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        return getattr(ÄÕÒü, 'set')(c=[P(ÄÕÒü[0]), *ÁØò(lambda ÂîÓ: getattr(ÂîÓ, 'frp')(lambda ÂîÓ: getattr(getattr(ÂîÓ, 'e'), 'T'), lambda ÂîÓ: getattr(ÂîÓ, 'cp')(t=MOD(ÄÔéÄ, áØÁ=getattr(ÂîÓ, 't'))('\n', d)), False, False))(Áÿú(ÂîÊ(ÄÕÒü[slice(1, None)], MOD(ÄÕÍÔ, áØÁ=áÐè('\n'))), P)), áÐè('\n')])
    return getattr(ÄÕÒü, 'set')(c=ÁØò(lambda ÂîÓ: expand_ast_py(ÂîÓ, PEV))(getattr(ÄÕÒü, 'c')))
(ast_clean_e := (lambda ÄÕÒü: getattr(ÄÕÒü, 'frp')(ÃÆë, lambda ÂîÓ: getattr(ÂîÓ, 'set')(e=MOD(ÂÑÖ, áØÁ=None)()(ÄÔÔç(getattr(ÂîÓ, 'e'), lambda ÂîÓ: ÂîÓ[0] in 'Tpρ'))), True, False)))
(ast_add_pos := (Æå := (lambda ÄÕÒü, i=0: (ÄÊPSH(getattr(ÄÕÒü, 'e')), ÄÊPSH('p'), ÄÊPSH((i, MOD(Áëý, áØÁ=getattr(getattr(ÄÕÒü, 'e'), 'T'))(ÄÕÒü, (ÄÊCUR((1,), {'áØÁ': i}, ÆÑ, ÂýÃ, ÂÕì(Æå)), lambda ÂîÓ: ãÊú(+ÂîÓ) + i)))), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3][1])))

def get_region(L, p):
    if ÁØö(L, ÁÜÙ):
        (L := lines(L))
    if p[0] == p[2]:
        return [L[p[0]][slice(p[1], p[3])]]
    return [L[p[0]][slice(p[1], None)], *L[slice(p[0] + 1, p[2])], L[p[2]][slice(None, p[3])]]

def map_region(SM, p):
    return ÄÔÒØ(Âîí(ÄÔÙù(ÁØò(lambda ÂîÓ: áÇù(ÂîÓ, 2))(ÄÔÙù(get_region(SM, p))))))

def into_srcmap(ÄÕÒü, áÖï):
    getattr(ÄÕÒü, 'rm')(lambda x: getattr(getattr(x, 'e'), 'p')[slice(None, 2)] == getattr(getattr(x, 'e'), 'p')[slice(2, None)] and getattr(getattr(x, 'e'), 'Ïï')[slice(None, 2)] == getattr(getattr(x, 'e'), 'Ïï')[slice(2, None)])
    (L := ÁØò(lambda ÂîÓ: ãÊú(ÂîÓ) * [None])(lines(áÖï)))

    def R(p, ÏÁ):
        if p[0] == p[2]:
            (ÄÊPSH(L[p[0]]), ÄÊPSH(slice(p[1], p[3])), ÄÊPSH([ÏÁ] * (p[3] - p[1])), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        else:
            (ÄÊPSH(L[p[0]]), ÄÊPSH(slice(p[1], None)), ÄÊPSH([ÏÁ] * (ãÊú(L[p[0]]) - p[1])), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
            for r in ÄÝöÇ(p[0], p[2]):
                (ÄÊPSH(L), ÄÊPSH(r), ÄÊPSH(ãÊú([ÏÁ] * L[r])), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
            (ÄÊPSH(L[p[2]]), ÄÊPSH(slice(None, p[3])), ÄÊPSH([ÏÁ] * (ãÊú(L[p[2]]) - p[3])), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]

    def Æå(ÄÕÒü, n=0):
        R(getattr(getattr(ÄÕÒü, 'e'), 'p'), getattr(getattr(ÄÕÒü, 'e'), 'Ïï'))
        for c in ÄÕÒü:
            Æå(c, n + 1)
    Æå(ÄÕÒü)
    return L

def out_to_in_mapper(ÄÕÒü, Ïß, Ïø):
    (ÄÊPSH((into_srcmap(ÄÕÒü, Ïø), lines(Ïß))), ((SM := ÄÊPKE(0)[0]), (áÖÔ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    return lambda p: Âøî(get_region(áÖÔ, Âçß(map_region(SM, p))), '\n')

def ast_to_py(ÄÕÒü, áÖï, get_tree=False, no_rename_vars=False, reparse=False):
    (ÄÕÒü := fill_ÄÕÒü_holes_basic(ast_clean_e(expand_ast_py(ÄÕÒü, *([ÄÕÍÔ] if no_rename_vars else ÂÚü())))))
    (pyc := (+ÄÕÒü))
    ÂÕÅ((Æå := (lambda ÄÕÒü: Áÿú(ÂåÔ((ÄÊPSH(getattr(ÄÕÒü, 'e')), ÄÊPSH('Ïï'), ÄÊPSH(getattr(getattr(ÄÕÒü, 'e'), 'pop')('p')), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3] if 'p' in getattr(ÄÕÒü, 'e') else None, ÄÕÒü), Æå))), ÄÕÒü)
    ast_add_pos(ÄÕÒü)
    if get_tree:
        return ÄÕÒü
    if not reparse:
        return pyc
    import ast
    try:
        return getattr(ast, 'unparse')(getattr(ast, 'parse')(pyc))
    except Exception as Ïã:
        Âçß('Code:\n%s' % (linewnum(pyc, d=175, s=ÄÊCUR((1,), {'fg': '915'}, Åøþáüì, ÂýÃ)),))
        ÂùÆ(False, 'Error in python reparsing! %s' % (Ïã,))
(__exports__ := ÂÛê('ast_to_py\u2009PEV\u2009VEP'))

__file__='/home/ganer/Projects/Moon_BETA/Libraries/Compiler/main.☾'
from sys import stdin as ÂÐðþáÐâ, argv as áÑË
from time import time as áÏÖ
from subprocess import Popen
__ÄÊIMPORT__('text_format', globals())
__ÄÊIMPORT__('to_ast', globals())
__ÄÊIMPORT__('ast_to_py', globals())
(BASE := áÌî('/home/ganer/Projects/Moon_BETA'))
(COMPILER := ('python3 %s/STAGES/BOOTSTRAP_β.py' % (BASE,)))
(BINARY := 'python3')
(CODE := ÁØã)
(DEST := ÐÌü(getattr(ð(BASE, 'STAGES/BOOTSTRAP_Δ.py'), 'resolve')))
(TMP := mkd('/tmp/γ'))
(áÑð := ÂÑÖ()(show_preast=False, show_ast=False, show_py_ast=False, dbg_parser=0))
(mod_files := ÂÚü())
(áÌë := (lambda x: ÂåÔ(getattr(mod_files, 'append')(x), x)))
(tof := MOD(ÁØò(lambda ÂîÓ: ÐÌü(getattr(ð(BASE, '%s.☾' % (ÂîÓ,)), 'resolve')))))
(code_files := [*ÁØÿþÁÙÇ(lambda ÂîÓ, ÂîÒ: ð(ÂîÓ, ÂîÒ))(áÌî('Header'), ÄÝöÞ(ÐØó(ð(BASE, 'Header/builtins')))), MOD(ÄÕéý, áØÁ=áÌë)('Libraries/text_format'), MOD(ÄÕéý, áØÁ=áÌë)('Libraries/𝐍'), MOD(ÄÕéý, áØÁ=áÌë)('Libraries/peggle2/main'), MOD(ÄÕéý, áØÁ=áÌë)('Libraries/peggle2/rgx_golfatron'), MOD(ÄÕéý, áØÁ=áÌë)('Libraries/peggle2/gram_tools'), 'Libraries/Compiler/generate_operators', 'Libraries/Compiler/op_table', 'Libraries/Compiler/node_types', 'Libraries/Compiler/tree', 'Libraries/Compiler/tree_txt', 'Libraries/Compiler/expr', 'Libraries/Compiler/lambdas', 'Libraries/Compiler/rewriters', 'Libraries/Compiler/to_ast', 'Libraries/Compiler/ast_to_py', 'Libraries/Compiler/main'])
(ÄÊPSH(Áÿú([code_files, mod_files], tof)), ((code_files := ÄÊPKE(0)[0]), (mod_files := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(show := (lambda x, y=True, d=100: MOD(Áëý, áØÁ=y)(BOX(linewnum(x, d=d, s=ÄÊCUR((1,), {'fg': '915'}, Åøþáüì, ÂýÃ))), lambda ÂîÓ: ÂåÔ(Âçß(ÂîÓ), x))))
(to_py := (lambda áÖï, *áÑË, **áÑÕ: lambda *áÑË, **áÑÕ: ast_to_py(*áÑË, áÖï=áÖï, **áÑÕ)))
(moon_to_py := (lambda áÖï, áÖÝ={}, áÏè={}: to_py(áÖï)(to_ast(áÖï, **áÖÝ), **{'reparse': True, **áÏè})))

def moon_to_py_debug(áÖï, show_preast=True, show_ast=True, show_py_ast=False, **áÑÕ):
    (ÄÕÒü := to_ast(áÖï, dbg_show_gram_tree=show_preast, **áÑÕ))
    if show_ast:
        áÍñþáÍñ(ÄÕÒü, 'AST')
    if show_py_ast:
        áÍñþáÍñ(to_py(áÖï)(ÐÌü(getattr(ÄÕÒü, 'cpr')), get_tree=True, no_rename_vars=True), 'PY AST')
    (p := show(to_py(áÖï)(ÐÌü(getattr(ÄÕÒü, 'cpr')), no_rename_vars=True), False))
    Âçß(padc(' CODE ', p, '─') + '\n' + p)
    Âçß(show((pyc := to_py(áÖï)(ÐÌü(getattr(ÄÕÒü, 'cpr')), reparse=True)), False))
    return pyc
(reewrap := (lambda x, y: '\n__file__=%s\n%s' % (repr(ÂÕÅ(ÁÜÙ, x)), y)))

def cached_transpile(áÖý, instant=False):
    (áÖü := ð(TMP, '%s.py' % (sha(TMP, (ÄÊPSH(áÖý), ÄÊPSH(ÐÌü(getattr(ÄÊPKE(0), 'resolve'))), (áÖý := ÄÊPKE(0)), ÄÊDEL(2))[2], ÐØó(áÖý)),)))
    Âçß('%s ⭢ %s' % (padl(getattr(áÖý, 'name'), 25), getattr(áÖü, 'name')))

    def rd():
        (áÖï := reewrap(áÖý, ÐØó(áÖü)))
        if áÖý in mod_files:
            (áÖï := ('\n# %s⟶%s\nexec(%s,__:=globals().copy())\nfor k,v in __.get("__EXPORTS__",{}).items():globals()[k]=v\n' % (áÖý, áÖü, repr(áÖï))))
        return áÖï
    (v := rd)
    if not ÐÌü(getattr(áÖü, 'is_file')):
        (p := Popen(ÂÛê("bash\u2009-c\u2009%s o '%s' '%s'" % (COMPILER, áÖý, áÖü))))
        (v := (lambda: ÂåÔ(ÂùÆ(ÂåÔ(ÐÌü(getattr(p, 'wait')), not getattr(p, 'returncode')), '❗ %s⟶%s failed!' % (áÖý, áÖü)), ÐÌü(rd))))
    if instant:
        (v := MOD(ÄÕÍÔ, áØÁ=ÐÌü(v)))
    return (v, áÖý, áÖü)

def make_header():
    (áØÂ := ÐÌü(áÏÖ))
    (h := Âøî(ÁØò(lambda ÂîÓ: ÐÌü(ÂîÓ[0]))(Áÿú(code_files, cached_transpile)), '\n'))
    Âçß('Head compile took: %s' % (ÐÌü(áÏÖ) - áØÂ,))
    return h
(ÄÊPSH((áÑË[slice(1, None)], ÁØã)), ((áÒø := ÄÊPKE(0)[0]), (pre := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
if ãÊú(áÒø) >= 2:
    if áÒø[0] == 'o':
        ÂåÔ(ÐØì(áÒø[2], ÂÞÅCAT(ÂÞÅCAT(áÒø[1], ÐØó), moon_to_py)), ÐÌü(exit))
    if áÒø[0] == 'e':
        ÂåÔ(ÁØò(lambda ÂîÓ: Âçß('%s ⟶ %s' % (ÂîÓ, PEV(ÂîÓ))))(áÒø[slice(1, None)]), ÐÌü(exit))
    if áÒø[0] == 'd':
        ÂåÔ(ÁØò(lambda ÂîÓ: Âçß('%s ⟶ %s' % (ÂîÓ, VEP(ÂîÓ))))(áÒø[slice(1, None)]), ÐÌü(exit))
    elif áÒø[0] == 'f':
        (code := ÐØó(áÒø[1]))
    elif áÒø[0] == 'F':
        (code := ÐØó(áÒø[1]))
        (pre := ÐÌü(make_header))
    else:
        (code := Âøî(áÒø[slice(1, None)], ' '))
    if áÒø[0] in 'rx':
        (ÄÊPSH(áÑð), ÄÊPSH('show_preast'), ÄÊPSH((ÄÊPSH(áÑð), ÄÊPSH('show_ast'), ÄÊPSH(True), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    if áÒø[0] == 'x':
        (pre := ÐÌü(make_header))
    Âçß('Using code:\n%s' % (linewnum(code, d=175, s=ÄÊCUR((1,), {'fg': '915'}, Åøþáüì, ÂýÃ)),))
else:
    if ãÊú(áÒø) == 1 and áÒø[0] == 'D':
        ÂåÔ(Âçß(VEP(ÐÌü(getattr(ÂÐðþáÐâ, 'read')))), ÐÌü(exit))
    (ÄÊPSH((ÐÌü(make_header), reewrap(áÒø[0], ÂÞÅCAT(áÒø[0], ÐØó)) if áÒø else CODE)), ((pre := ÄÊPKE(0)[0]), (code := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(áØÂ := ÐÌü(áÏÖ))
try:
    (pyc := (pre + '\n' + moon_to_py_debug(code, **áÑð)))
except:
    Âçß('%s: Failed to compile!' % (__file__,))
    moon_to_py_debug(code, show_preast=True)
    ÐÌü(exit)
Âçß('Provided compile took: %s' % (ÐÌü(áÏÖ) - áØÂ,))
ÐØì(DEST, pyc)
Âçß('%s: Wrote code to %s' % (__file__, DEST))
if áÒø:
    Âçß('Executing %s' % (DEST,))
    (áØÂ := ÐÌü(áÏÖ))
    (r := ÂåÔ(ÐÌü(getattr((p := Popen(ÂÛê('%s\u2009-u\u2009%s' % (BINARY, DEST)))), 'wait')), getattr(p, 'returncode')))
    Âçß('Execution took: %s' % (ÐÌü(áÏÖ) - áØÂ,))
    if r:
        Âçß(Åøþáüì('%s: ERROR %s! ' % (__file__, r), 'f33'))
Âçß(1)