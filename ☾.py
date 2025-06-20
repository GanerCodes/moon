#!/bin/python
from pathlib import Path as áÌî
moon_dir = áÌî(__file__).parent
__dir__=(__file__:=áÌî(moon_dir/'Builtins/base.☾')).parent
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
__dir__=(__file__:=áÌî(moon_dir/'Builtins/system.☾')).parent
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
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ops_A.☾')).parent
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
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ops_B.☾')).parent
(ÃÆí := (lambda áØÆ, áØÁ=ÂÞÅ: (GET_CASE(áØÆ) if ÁØö(áØÆ, ÁÜÙ) else 1 if áØÆ > 0 else -1 if áØÆ < 0 else None) or (0 if áØÁ is ÂÞÅ else áØÁ)))

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
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ops_C.☾')).parent
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
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ops_\uea8c.☾')).parent
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
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ugex.☾')).parent
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
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ℵ.☾')).parent
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
__dir__=(__file__:=áÌî(moon_dir/'Builtins/!.☾')).parent
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
__dir__=(__file__:=áÌî(moon_dir/'Builtins/𝔍.☾')).parent
(áÐÞ := ÂÞÅCAT({ÁÁ: ÄÊCUR((1,), {'ensure_ascii': False, 'indent': None, 'separators': ',:'}, jdumps__, ÂýÃ), ÿ: jloads__}, ÂÑÖ()))
__dir__=(__file__:=áÌî(moon_dir/'Builtins/🌈.☾')).parent
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
__dir__=(__file__:=áÌî(moon_dir/'Builtins/kots.☾')).parent
(TMPDIR := ð(ÂÞÅCAT(ÐÌü(gettempdir), áÌî), 'tmp_☾'))
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
__dir__=(__file__:=áÌî(moon_dir/'Builtins/extra_globals.☾')).parent
(FRAC_CONV := {**dict(ÄÕåØ(ÂÛê('12\u200913\u200914\u200915\u200916\u200917\u200918\u200919\u2009110\u200923\u200925\u200927\u200929\u200934\u200935\u200937\u200938\u2009310\u200945\u200947\u200949\u200956\u200957\u200958\u200959\u200967\u200978\u200979\u2009710\u200989\u2009910\u200903\u20091100'), '½⅓¼⅕⅙⅐⅛⅑⅒⅔⅖\U000f7db2\U000f7db7¾⅗\U000f7db3⅜\U000f7dc6⅘\U000f7db4\U000f7dc2⅚\U000f7db5⅝\U000f7db9\U000f7db6⅞\U000f7dba\U000f7dc7\U000f7dbb\U000f7dc8↉\U000f7dc9'))})
(TOFRAC := (lambda x: getattr(FRAC_CONV, 'get')(x, x)))

class UPSIDEDOWNSYNDROME:
    (NRM := '0123456789abcdefoxABCDEFOXîĵ\U000f7e88ℇτπ\U000f7e8d\U000f7e8f∞')
    (USD := '\U000f7c3d\U000f7c3e\U000f7c3f\U000f7c40\U000f7c41\U000f7c42\U000f7c43\U000f7c44\U000f7c45\U000f7c46\U000f7c47\U000f7c48\U000f7c49\U000f7c4a\U000f7c4b\U000f7c4c\U000f7c4d\U000f7c4e\U000f7c4f\U000f7c50\U000f7c51\U000f7c52\U000f7c53\U000f7c54\U000f7c55\U000f7c56\U000f7c6a\U000f7c7d\U000f7c7e\U000f7c6b\U000f7c6c\U000f7c6d\U000f7c6e\U000f7c70\U000f7c69')
    (MAP := ({**dict(ÄÕåØ(NRM, USD))} | {**dict(ÄÕåØ(USD, NRM))}))
    (flip := (lambda x, m=MAP: Âøî(ÁØò(lambda ÂîÓ: getattr(m, 'get')(ÂîÓ, ÂîÓ))(x), ÁØã)))

class SCRIPT:
    (SCRIPT_FILE_LOC := ð(moon_dir, 'Builtins/Data/script.map'))
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
__dir__=(__file__:=áÌî(moon_dir/'Builtins/highlighter.☾')).parent
(styf := ð(moon_dir, 'Builtins/Data/style.json'))
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
__dir__=(__file__:=áÌî(moon_dir/'Builtins/meta.☾')).parent
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

def IMPORT_find_file(p, g_dir=None, w_dir=None, flags=ÁØã):
    (ÄÊPSH((getattr((ÄÊPSH(p), ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0), áÌî)), (p := ÄÊPKE(0)), ÄÊDEL(2))[2], 'name'), None, None, ÂÚü())), ((name := ÄÊPKE(0)[0]), (F := ÄÊPKE(0)[1]), (native := ÄÊPKE(0)[2]), (failed := ÄÊPKE(0)[3])), ÄÊDEL(1))[1]
    (dirs := ÄÔÔè((getattr(p, 'parent') if ÐÌü(getattr(p, 'is_absolute')) else None, g_dir, ÐÌü(pwd) if w_dir is None else w_dir, ð(moon_dir, 'Libraries')), None))
    (sufs := (p, '%s.☾' % (p,), ð(p, 'main.☾'), ð(p, getattr(p, 'name'))))
    for F in ËãÂ(ÂøÚ(dirs, sufs), ð):
        (ÄÊPSH(F), ÄÊPSH(ÐÌü(getattr(ÄÊPKE(0), 'resolve'))), (F := ÄÊPKE(0)), ÄÊDEL(2))[2]
        if ('↺' not in flags and ÂÞÅCAT(moon_dir, getattr(F, 'is_relative_to'))) and (h := ÂÞÅCAT(ÂÞÅCAT(moon_dir, getattr(F, 'relative_to')), ÁÜÙ)) in TP_CACHE:
            (native := h)
            break
        if ÐÌü(getattr(F, 'is_file')):
            break
        getattr(failed, 'append')(F)
        (F := None)
    return (name, F, native, failed)

def __ÄÊIMPORT__(p, áÒÿ, flags=ÁØã):
    if flags:
        Âçß('FOUND FLAGS: %s' % (flags,))
    (ÄÊPSH(MOD(Áëý, áØÁ=ÄÊCUR((1,), {}, ÄÝøÇ, ÂýÃ, áÍé))(p, ÄÊCUR((1,), {}, IMPORT_find_file, ÂýÃ, getattr(áÒÿ, 'get')('__dir__'), ÐÌü(pwd), flags))), ((name := ÄÊPKE(0)[0]), (F := ÄÊPKE(0)[1]), (native := ÄÊPKE(0)[2]), (failed := ÄÊPKE(0)[3])), ÄÊDEL(1))[1]
    ÂùÆ(F is not None, 'Unable to find module "%s"! Paths checked:%s' % (name, ÂîÊ(failed, '\n')))
    if '↺' in flags or F not in __ÄÊIMPORTS__:
        (ÄÊPSH(__ÄÊIMPORTS__), ÄÊPSH(F), ÄÊPSH(None), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        try:
            (ÄÊPSH(({'__name__': name, '__file__': F, '__dir__': getattr(F, 'parent'), '__EXPORTS__': {}, '__þIMPORTS__': __ÄÊIMPORTS__, 'TP_CACHE': TP_CACHE, 'TRANSPILE_REF': TRANSPILE_REF}, {})), ((ns := ÄÊPKE(0)[0]), (áÑÕ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
            if native is None:
                (ÄÊPSH(áÑÕ), ÄÊPSH('native_code'), ÄÊPSH(ÄÕôñ((ÄÊPSH(áÑÕ), ÄÊPSH('code'), ÄÊPSH(ÂÞÅCAT(F, ÐØó)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3], get_code=True)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
            else:
                (ÄÊPSH(áÑÕ), ÄÊPSH('native_code'), ÄÊPSH(TP_CACHE[native]), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
            (ns := ÄÕôñ(áÑÕ['native_code'], ns=ns, native=True))
            (ÄÊPSH(__ÄÊIMPORTS__), ÄÊPSH(F), ÄÊPSH(Module(name, ns, hardcoded=native is not None, **áÑÕ)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
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
    (ÄÊPSH(__ÄÊIMPORT__('text_format', globals(), '')), ÄÊPOP())[-1]
    (show_table := (lambda x, y: Âøî(Áÿú(ÂÛÅ(ÁØò(lambda ÂîÓ: ÂåÔ((m := ÂóÍ(Áÿú(ÂîÓ, áüíþËðâ))), Áÿú(ÂîÓ, ÄÊCUR((1,), {}, padc, ÂýÃ, m))))(ÂÛÅ(MOD(Áÿú, áØÁ=2)([x] + y, ÁÜÙ)))), ÄÊCUR((1,), {}, Âøî, ÂýÃ, '│')), '\n')))
    Âçß(show_table(ÂÛê('Static\u2009Name\u2009Path'), ËãÂ(__ÄÊIMPORTS__, lambda x, y: ('✗✓'[getattr(y, 'hardcoded')], getattr(y, 'name'), x))))
(BOOTSTRAP_GLOBALS := getattr(globals(), 'copy')())
TP_CACHE.update({'Libraries/Compiler/main.☾':strd('c$~diTW{RP6@K4eF-Bl;XwcTh$U_!h7rHqSEL(yk2LWV(;F7ai!n@>x<SG&jKgfyOB54uVw<<xLKrw<gXzMs_8U(GAJj_4QFX&I`IWwH$@FLlA(k>+JaOUt_X3qJ}Iip?@4@tV4l5jYRlZ>QU5JtpH3BS$n@@M=<egNNJw0cOFg+rzY#Te-h_(%Lvi}LsR2P<oDQP;)M;+2)<)pggUR>pQRw-+ZvFS8u7HHf?3Af>iLEX#(!;<e=!YTFxUr#6pa6T4p8$U#!h%+J5Mv^+brwC2t&EzDencLb};3rMM7I)OwG=YrJH?*CJ0mN53elt+hg9JxW5IAnMup!^wKzp^sFxa#0}f5z|3&8*X6<hs3Zz+4wr@A7^A4`7`3JsUp`p>%d;ZGp5qMCmYTZ%l6D3h=DVPi-o#<`<Uel#Mf>)dBwle<nz8!{`yUY1)t9bw>$<-S1oiYZ!`zsp|7+*PIHvTkgn9QkHZkZM#ML%nMlJ`rxz3d=HfW30!%Pf6RYF2i~w7cqsBIzwgNJdu=rFcl<fsVwsm^32u#|uuiAv4)=ew$Y~<y?m1|Um9R7(Y%@3@8_97yV0LyK4ze&xEoty${vH2}%KdAgn&@hB{IuxE%ld<`>*iqw>QhSuU%sH?Zv`GP{!XXYBXy{x1CRRD>~pXsEXsu5D+_N^>pze0euZio4??DJb0JFY%>jSJzjnwOaY7%$K#m@^NlwwQq63ENMaie5+2yoCs8ISy$>RHQ=jJU(BFvv**e3o)f0KkgLi_j*_#!RSD`MLwfMV1~Ds`ZRJlKALYTtnQgn<JQ9Us1m9T@kGv9wDHv#A6lS~3fy+c>-lZXsOJYLoS3%<^SW>J~ap%CazHLmju%N(hXnjPaxyFXtg%&TrzTDSZlK3?;Qy#njDPQl@n2lgn(i0@fpiG&f+~@s_q+ho-btJjUbdqZ`F8IHEUX<q)n%c^Iij?JDgSfe)N{P9UH01EKgQ{yCjpeuu)I4j8o-uUa`HKMt5WF7!5}NBbZ0d;B?iMdb()K*Wn%i8pi+g*%3hrstN_fi**)1O9vdjmVhrt)+pt&8)3kN{0iOeJ|I*aH%T#6fgUuM5KV+t;F6|)F|!oaT~OJZN0ifppD)kgWpNGoYWGns=Eyq<pwDo5|)jVh)B&^G+=(5co`Ftjs%Jy+Qf1Z0bRGF@vq$hFjUYuaXPgXAYPA7r*%+lN`S?v$eY?QAy}k=ftQ8b3?f99G<*D0{;@o<#8x1P_K9GEq%=bP3>Q^abgsq`D?DCKk}wrOQk+PU%?(WzBbBI?R7})z+?c9!884BoEACrhf{wGg-cg(pw5dV&-1Q2mGHlVB$kn-PtCUVT@Pz50<PqZ7e&FvpCB`8A#f%TYO`qCF?SWzcG}u4AX)Ds){$og+{8*hjx@Kzn@ufDJ@I8Nuf%7fDLoYd`RH2CVFChXA;Uyn3kJt2ES=~r~u=6_Sem=s8w&o<40E!0uIsDrfBoB-$%kwgDzd{cO{`-8d6U12(4sF^XM0x!5>+t8;m-EF3u=u`SRM25vj{sO8BLDbrjL7q^%nd!OftxH`ab8Db!g^4~^<Cfd`z*+-E~ufU$5yaxeZ`%dnR^TCH-Er9L^Bx{34<5Y`~*IMH}VDOd&mukY-2UDamFn6*IakAhzbZA3>7VC8zl6-B*60xESmrua|y8%W;-3C&Ja{7xZ%f-Bd99J%oI_vhW5<z2>B}H6fkCmsd$8kGHdmQG#UuK(TGK$Chgg+DpAE|pdQ5|AiW_;`G@=ozpY$faXiBRvEGw4-En@77$M4@g2;CaxH2PPJ@KMc#XwQt-*=>^<a+ElWVc-a%<%<ffjc|Kc=u<Pe$rXDSi}VMb>lcov&0)geuNULu+*B!hNB5+R?dmORe@Yv7eGRrl_mGm^6F)3!U*=5s@szp88e65oHTyTzkKPGG1~QI7xUVwiEbE8jCQkr9AOSNf5qmPdmr-zi-yi2B`CEW<<`M?II4tkv4|R*We#qeQR1NU{FUnc!PS!_5Tt)WPH+h9Lp?lVj32*0j4^zWjYD3ae4|te!FxxYzB_=jgVtKHGI%v3oL%;a>OF*pl^0*xAfNTsnX79ni%Sdc>cS<nIcZ5_Yi?WD+2}O<L8t&&T{b12&$^y}1B)sz7=)1oHW~@gEp9%_Rz<1V9pzMJdn5zAO$6c3h|k>9dpp7l?m#-nF5o%%ly&&&V}fa@H|fDwGBE4+cl)r%wc@TJn*(PDa>!_$*>*K)Ncu8FD|~x14zLW{isRsvRlLats!ID>BoUd+no(YOXu6xi&VY-myl1dVS+i`2>z%3Y#?(wcxGX~)Evc8SuG<f{AojQV8HBlO8)m9aQFT}CT@%GB@8!BQmiB_9L*8Cku^Z%<*ks9W*+!E$)+XO#zn3$N(oO_>7Kxr9?}QP4I;CvFw!HzxA^eC|Au}CA@9vJzMp<2Uqe4QdSJY;Q`Ayo?WJrZ%tNV$#{{4tQIYJe^_oBEhHXhz6x+o*EEqP1qN*Q4sscveYKT+jcrV@4{Py)f@9{*nDH_?&?v2PaGZS9cPQg4g3$>DGB)Rm>c4ZsH+=z5e-T@cw2Q_@9Em5d_-$(7(zL3y@c=ZC70tRJQZnNKdDk0LYzBjifa4JvZa&NYz1`Bcfe<O1NS%mbJ?E*49()g?m5qW};%Rl$-Nj2O89q$rL>DA-^W=q2pBN=tFRK_O@;NAWoORhk9xb<wh`P)s-Sv)UBl|A0TEwr);gy0Omay=;*ofi&mjMS%c}`~1FmU(6y$_!V$>)~Z$BqQrbqQ~<ql`hUpx%eh~B^JM8l00gND*WO46q0gXi6&<iGRIggpP$uMxpX!ilat3vMQDKkV^S#c?GFrW_Ln|%M!Y-sIFFeh1Sk*+d*jR^%YdG9r(KzT`k#Fk?An*2Z*Nb~p#X=wma46MTSdpkCFC~j)^s2I-@DKRE@}0MF)23cZ5!IY)v^3L#^cLeP1u*m`^hV;w%C*E*)6fee7~gs!m>M=(OrC(TABb&#r}cIxPoU)R^Y1E+iMYF0tvvqUL7Hwz34RGFkQI-YGGCR_RLcnI$E0BC4zjK}J`+o!epP7IC~+UK$Nyqn71S?~L_GhqxH%HxX=~F35219yBhNv0vl)4YQ{hiUg^3M^Bhq}ygt^-3oRlMYm&vgEQVb2RmTimEP?ei(XMZ`iqDwJ($2H!v{fBKn(9!IW4Zv1F&*@F06K|Vced!`qPw$w)Yu+GEYX=bRo<nv36O<bWIKhb=WrPEiPOjgeHM*}ZIuvnQzJkZRqJnKP0)Getk;-Xmw^i8n#6J{k4DFWwzpuOSPJV?#jfRX`1&~{%OOEoIOamnfIVI>y4YgHou%UIT9jevnKuB9I(SWWzQD`Ptbuz&D=3W*1rsgKrZXMlu!kH<|7Fl0|wmhANN)j5<TGIY6m$*92'),'Libraries/text_format.☾':strd('c$~!=Yi|@s^1FY<C=!|;XMCAm;{eWWashHey5t-I(M8%_t@bgt_t=MTcYIz4kid9t5?(eo4o-mJ@W=z=I{`tE;2_aIAip8=3+^XeRrO;YJ8N*hgk<UN>h5}VRdrPl)%sMk<ryt^fbk9fjQ>zBmM2|fG-I$@v0kba4Zgtd*v25tF7tEH5xpy;2A|`1_$p)k9RDxhz%8_w;RegH4Y@yIr`l2-M<h@9GUKQDRsKMeoa38(1t{F&pYflV7+SO(*FBaH+W>?s{IO-YwYF=dEG9@<mhopJ<)n8DIPt@J*s$Oa2tCg~`|!vi7M7kB3X|1|$r}7Tw^b-uL`cs9tX{6QER>P4Lnt_5`P+NUv9eAc!MqD%{X)C$#}=gWxDf#d-+P~>EQAcO@oJ+|aNFfV+x=G?cTBim(eqlY<=Tc>Zq}!&HP^HlJA#vDu9GU|a#{AyXf9WI{jKy{)abuXI9B~cHrH`d@Jr`S5|v0a+>Tc$PZnF-&@dU`h5vW8trL=vQ?~~H^p0g3y9{>3CUmVj@=L;nl!I~|_~<ZW!!}5H{G=Tv(w;7v0FOv(i&MR2<GF9~Glad;^jg(=9J{oSj&00lMx0TjlWo_kWtaWE*#PXb#t;}m-gw<G{Zn^MvKQJ6CxHg{HDevZc$#11>#PHWjJIJISxE<})~XG+9Wj1siAo3<-{9Q??;Z_IkdRp@+f=RUq55(Sp>Pi%VPwemC~kO;M!mro`BN6r4yvVCs{xMaS=qoH?6qv+E}Oz~Bces<XwMO6gp!7wr=yt;Nv^R`8^adY2K!*_AS&P?zd){Wm7mTy7E_W1&KY8mj6UMemL>H467~>)=ZiuQRNQfcj=TWa*Z5Onc#Z#uiH3--@hxj~z<@sjdP7<fa4F42ECN?m>$7RJ8n7LU_8~KpRYG7HnT(MVIOBNd`1ky#1OUb;g;YRcI1ktbdK4=WS#}#Vq=LK%#JEN*NZH0v%2HHrWQS7uh)aZsOW9hkH{EJTLz1+?^w4Gp2L2LqHq!M}vBF4o3-X{BWqUSb8m7emECW0!jYs3D_B?^aid%(%FUnY2OOB<q<W-`mJiD6lwmk5~K+Q^S;zRO!iJvA*mlTGKniUuTNrneMl<I>8OomVlN|p3(b$WNA?Vo2^+PKR|>&=Lau;O9j<Qs2<W)s*-;3~|F#z(7w>{GtL{#pdngVWyC_RoHr`^a&e@jc~XSN7cDQi>wHAYxm6ETXMVVkX1y*~TRNEzdu6MJuZjz8tl8R30c^xW6<FE#iz(Z5#YvXvYjL-ah68HX4aJ8tG&Y(n+!??dA~{Xmz9Mk=F%#^erH%nGm4eMg`(^7Q6ve51ckzh68udAQBjg<B!VNOF+9%;4TV~oFGw)7oH+N)Z<_}*aqHXX}4O4x>d-f(%@3*d?aKDbLusTwpT14YcUa-z7H$`<rA=8Q>7b!ATBd*$3T$8n}`O3V%fdeoQ{Sf?1^C6KSG3~`#r0Vrv~2ByW{Ny_mgT+#u3rVJ$dw@V5W^9W>Ge68!T!x$emJA$})<LiWrW4$Rcy$T^LYlB@5(7%RJhecBvDCQ(Un6r~sH#!DJEoNw>&3AU-Fuf_Z)g%7UxfN5x57ED|>`YQ*?e_X~FJTm5gOQnORgc*Z9(rZeJ<>>G!>s8pTEgarv%QHXftAi662_g+<aBr@P45=up!(B>6>McE+byD63LhEso)(juo;LT;hXHzf`W9R{RGJP4r2%&ckYxUP?dW+2CpdJ`Q61xI}pX$zylm;8HX`WH9+i(mT}Z{?=bj<e6dc-y~t$G>>jv}93rMcl|^i8u0r9bCpBPtqlbW|IxFY13alZ=yJ1$SG5@-nA&FUtKaacbEtzhQu+TEf9&wcmTNz#nUi>)t8gJ8j#E@qwMPdz|ltdGSZmSwjq@iDg|ug6J(b)$Ouyqx}iLQYk`6nP-ma$kwsO_EQ!;|Ywuv&-wpw-gc@A<kzl_g5yrCc4SoTN^b?}<ovIcRunFH&Hw|Ka&KL0pAsYfpiB`0K?BiD|jlp?)$|%jms6GNx0XW`izRu^Ps<1_Sc~s=H5g5q{h|rycyTd?;8q08lawU{!P|IeeOuF;~I^{o{XJ@A@xBhUJccx`rInydm^?4>xept!ub!=lQvl~(*AQqD)?lm%S-s4-r9hR6<K@w20w3tD)4A;Toeu@baHjn`tB>|gKF$*+R0cJ74;rjtPV#Nw-Wp#<gw9uID_g12mP|rYi)XvcTe1Wg_7WJ`ECLi~N=ZU;qrx^46I)BXXv)KC_zP<osbqkA-GyJI~;_V8*q_a>PwX=<KWW1D_1X0naP*chVENx3By-I6=Mq-N6cCup?1%~scG8}zeQs+9<*O4W8a!9c~*_<hqn-w?aQI$-}arDzEL_p0O9dxE583^YT=J*7VHut4Q%s%M_1=@~ybE<l^I8hz1%Ne@j`ks9j!xj^2?Fa?i`jpD@&RvJl9^Nk8z09<q>uW$f#^&|GY+J!)2j#ixhY4a?Yz67^Dr2<7nU2@V?T-%*R;p!B=beyL1doYeO+f|*D^{WRz@{wNHe@X<-$~B!1xiY>y)RnYy3Bv1QCE(h$o83RAISE(Y#++@k!&B!_9-!N9fbc$_8#$5gn3b}_(`w$nIM;GUaY(%*Zi#4JkxXM<lL5?+micF>os$F?zx<s({pEZZ%Oy&b#Ga&-_(%H^ggjk@Fjki+AGAx8Itl6=>*q4;Wu?}L-)Rxy-f|<48d;e-W}b$t9#$*-nY7UOJ*ux$o95u*JZn=G8x%^C);n;+k_n7knNYU-9*FvZRxJRbjrVfTRf3CrM-LoYb*Y>&;7Lx|ItJL(W4hzes|@?GrxPq@2>mZCBOTn-(B{*m;LUl-(8bWE0t1O_x8N_#qWNuhr@pNni`bf^t)H}%x(=%``s@zc*O5s*Moh!2U~CGK~ZnrqhTct+v_iUst5aiJ>}0Y`e$$O&0pu$OVHkm?&;T|z2oY|=*@k)SJb_-?p1Wp)jhp;kE3Cw|6O0c48LpeTZZ2y_^rcl1AaGuTU~-?4Sp-|gTll*8A^D;`$LZ-6j<oq3a;$?;RlaM-aTp@f>eTXQyE0IdjNS!jvWriIu|g<$A>ZCnRYgR{G|WYV^d_p2gW`~&V=9ZO@tAAI0jCO>MOo_Sb*cJcN6&C!~clEM-sE_;Ne!j-!1X;{28Orvc~W|;e?SebyZD;T`p8KsOOyXe5>E%?uDM0p2RwUs(&iQ)=A+j{HAQbfn-tCm|kl(C^jL@gnFuBz##{~Q0)frY)90oZl~-{dBG~Y6ht|FRDLj`nkXpYk78-&%}%*Jwe2DONe8Q{LZMNtyM=-o+bSYYZ($s<CiR&L%BzWtnRe1<3<-s;q_;KPCuVz?7BQ~hCV55Qrkh51(uftt5h)MP>n|-KOu~R}g%?|z@VfjYn|zFco-w@xJAXZvm4;PY_1t>fv{>A^&0TH$Pd#KOn~QCLU)cTl5YYj$A7bNhqU>;i>`?Y^f3NH!LF)8l_Z3)O*dePMJ79JH?_za-GOH{6VK1wuJk7qYWk=s+l-~^CKSg*FPKJ~I6+@&f6?r){-|(;cS<f-GSX4jkn0iFSiniG@WCof?_0ZcM>GGHr`lkn~8kTP=@{QCQC=@X0y?gLr;k}PP96NmUNTI+cYRwX)s%YoT6d!aUD;FJtQQiz7Y6*fbCIG-jjmu(OR^yf!x74^T#$vyCx;E7tHo;2G4!*HAJ2ZmI1xE0<<^W0<$piE>bS41LD7g5v4^Yt&6ji;1L{*<=sGtETwPJ0;_g~zW0H*cP>fH=ID~OLov?dgI&1jLOa3q+5xs9E}9xy&!0gd`}?YV8Q;NfTe@n)-D^q4euWpKiasP2zk1*SVOVPan4IN}93GCAYIADo5+6(4X%(9QhSId$ns?7Dajjj`~24Uik{Vy##)U|4cnhBxEZ{_PsTqt}2in`?NJE(F=OXLys<#)L83oHi@QOtIk^%?6HIMrpb=@ft?WRN6L%MZK(E%Zu_uIT8f}V&*@a{ttKjvuE968;}><&1$9Cu8<V!8yPEwHesFoN}I}YN+Yo6x1}FnJP6iQ;)r|K$XWRXrwH0C<{G73qnvA0at%~<3F={bm<g{(e^W=5O3@jdGGDU9=v`3W*@8qOu%tGPF(Bn^w*(wM*XX?ZGB^ZKeX(e6vwC~pTRU4Ii2NT{EBTZ'),'Libraries/Compiler/to_ast.☾':strd('c$~c&+iu*(^<7`VJdu>v!LCxEsDVW)TdHeRzQB@!0J1<(TuLImOR^-_UZE&pS+e3<h@*=wD{0(XHr&RRqb5a>+HI0P4A9qpL-z~(2|Z_KNDj&2UL>arK{LylIrr;uHL_0bU7q=+W*9g-f8p|_E3<~7seyena3VVh)rzvz^cKu!sOc3&Rdx8!Hcw1Wo}0dOW@38AI6FNxaS@JDXuq1moyj4X)5n)C!+h>kZGJ>6L%I~0t@j&dWXh1{f#7E4bX~#G2z>3rrAY+*fV?2<u={}QlhyjUD-#!Vjoc=`CoeVi?c+yV*V^ON>d)Rj-uqTXpvlVq`iJq-qn95tj0fZ)*{LYM06J`4XDAKJYi01_NC9n=Jx$jx)M5IPJkeC#h&aw?p4e{Gz5C^V)<P?Ae4J8Lvq3w>089Qr7;s}2Lr=IZ({TraiyO0WMPMThdr^rz!we%0M6^f#LVlp*cYOSskKa_3n`Yn|;j$M*bv#{BqQGexP1{|HmJP>U^!VdNFR*N5vE6I}m65evr!uc7jfEw{H-pd)>Q(j)fZa4G2T@?#@xIYf!1yWoQa?SSz^4ygC<JY6$&Sn@3R121<tDIO-VGZNo8ht@GTdmNixKJ}(JxqU(`+p?OqA^r**%TpbMin-44*xptIo%E4bRj_6~4ia*W^eet6;`|)pFpdsjrel@_l0Hc<$`gE1FiT0F>YSmg;qnY|-(1vIbOM1D)y|bw%Os@{oK&9wbmy1-9r~ESZE%I33{%fDYp|?&{+)(J-$G^J?s~lT*{$2jH|H%vU%A2#BkRbIZ)Wy%4tjzDh`31QBR_J8Cq=%mk}}L2Tp}YV#slH65QMq=2)N?-B<=C*aU4%H-6UtLN&eHI~={V=D?)m>J^7S(KP<x{Mz{@(KBdatLEW2?+hX>qL&(R47ta7lEdpl?6thJBw^7ft5L$cQ(az8;TR=k7VHncGM1B<)Y`>$#WF2fFgO00fKCh=K?FRb+um2!30_oCrr&MX5L1BP-oTLp{(IZkBMI8i(Z8$v06!w<5$t?5<^i=G5<N#$WiJKr9}EF^$iLyYjJ|Ljf1s~&!5nTGNQ1Xf&>Mkz*iLr^>K2WIm0sB%w;}K{RlFpqI{>kh4zo2c&;EC{Wi#U8b6VI(Oz%E>=o{LuAeyY$s7q0rj8^!OX{l<CIcub^64NOt_Rb9ibRN@+E_xvJ0n89cC}iqE>>#`Kfxjkt1BUp1vUhumf?FL1Uk<RMGa80GJz{!JY?;oVK<c$yO>jH1jVx|q@l7+j_bE0wkgGHHX6o4)3dIJ5)JV(85js6*?K;53_A)G#zn^4$6J3FDh$5iw2Ub*SvX<U<y8a-c$a)Z)6OpWGavW)_(YQx8MmRleqB}`Ai^j}YYe*3&q^4HQJo)+O9V{RVtU9}RlTlIDHzvp7_Qk;X{_kS&M2=v27?+TP}!+ewQ(IRXaq<%BB)-}N@5TA$Z;D`3>LR{?>#jdwpCgs7HlA<(o$*bBTDVxI|vGk60;SmiTET$-duLV>#U#inb(<-5kD+!Py3?nO%Teraci`_+1=QNzufm-@%wIWeOFk2d<&l4M?wqsn-rukvKF^bKGQX-#6wVGtcHprOv{O1O9=T`qzb<59)pNGWQRii7=$=1DaiSQ*P<LA-j<S3>c>%Cp6byiM9dU%&a{fgl$t!SLn}b?jNBvt&|*J<#hOkRO8lK3hnB}Tx_58MB2qt%-Y0*f;p|_1#94^8h^bdJcH6B5uxeRp`g2)il}W5rV4ly!HI_swA<g~NuA0egA(>gptkM1IN%yO#-Hom8#!mOuo$enFy3c<H0>HvL&o9=|Mp;3g7O|<gcsuk)-VWi?L9roXOZ((jZfU%%R}w3S`{Z+aObohD`1nkg#w^cYp-CxO!>vz~BaBL&g*#oSLwF4^#@QG~=BliaM3&bR+FxkJ(vot=%sp3IQX2lLW*+^ZDq{+7+XrbF;J=}su&~UDM^<q#E|@sszv=t7+W-ZWIp-01rE}r%8tg#V2N66^n0@d&E_BZr&8n5s_;5rHizLYH;7w7pLl6+hps?+$9Mc=nH~NbdANa`7_!5B^kO4F)vbaH@a0ad<C6yw>R0zu@zMAvHp2|_*SA{Swglx_b3amg`HgR;aNhjSS%{&?K+3fX9tp7^bip#*m^s$g`^0kGSOq*sjL~e*$%&}t)c&GrV0=<T9cz&@c>)=Iq;I(}tG6R4bmSsGs*JRyA;6rQDvoV1}RJM$KMYapeW`tLkC+S@zme-Nl9c#htjvt89k3}NuDYf#l#q-Z*(=b>DWMW+EZrwUNF{?5Q%7d7z3FcFX_-xB~eBa3|G=A?Oo?wQ@cW7yjRJ?$3gp=HJenlA5CDacB;IV{;Uf3^Qot{1>_I_IGm9h!GUipl?8T?v$5XX6sMuYTbn!R(-#hy#j&wMmg4-BnRN0mT9Gs3Q|(Y9=Zd`iB~J0N!d7L>T2Z&=Hw<M#5k$PQdHSds2vUT!z-GH;84nBh`SBtXmnzIuY{w%}LHsW#V#6*#Z#Em_-wt!&tIEL*Fw(pSei6dKcd&o*Yra1aw;DM^F80m=4r1-gW*vhde!GhDXJh~AbJL8fU6Ghi;avBbuc)dty?R>wk1*r_NhJX<GenT|UEG)XFh=j~T`_rPLfMd?tdLKK-In{(J|H~-HZKI9DS^6`)Hcx+BL@07Fou2NdBJ2$*QzN10Xiww(iqhT*?(R<SS3O0je&L+^{iegNSnQ=YZL9XS(m&H=#Eivt~AUW_&Uia?4EYvd668kDvI=MTkAu5t%N4uVvAIHDZ*j^jpf@pX`2i1WPamA}c7T4H4!>O9is&uwPcFl82td!LMKKdeaBU;oi?hs9~|9##I?#h1x<Jdbuo9XD;%uC-$8kQ4SZAY3lt#%NsKy2uhG22UaXRwzmiK&7G7qpKWJs{g;v!~n7WxAcwlAHG=wPyMxiPG03)>+mgNp9!x%CY1kyO8FRJ47lWyJOjY#9mE*u9zXduX>g?zvZv2r-A^gO^A3mpv`vNB_;BdiJ95=#Fsv%g9HJ<5vC{B?{XL;$*+rysgLlNK{JM-3BLx?RQB5w&=8yG`u_lH9ovT'),'Libraries/Compiler/rewriters.☾':strd('c%0oFZF3XH`8&Tt`E++ibR^Lv;ECH1<EBh`8)K&FIG&rcd^VcMl17q={G}6|1VaJ@umJ<+Ez}9Y1QJS8Xduk6-}@Ij<6n@U(C68=+uhrHkqPZgJqSs6yU#xFZ@VX#d_q1uc<7I=@8hRE`wku$9rJzHsRy%@Q$fcm7G~<r$)MhGy<)*}Joujt-L-r7yL%73vup1me|Yc6uKh5H!urz)j+B$&GrfG^AbcL*R-V|hWh$I5w8IbEwQlH7H`_Sv0y$5fdV^aE@HZ27gKoF&ig$4vmY?pnTaM>C)#hx=-#GCRV8`$*h(Ut|%d}3|g;~|1@qGt&v+LiGXMoo&vO<mxkp+0W?78rDiCiW>)Auj=`<jF^UYaP%WyZ_umx}sj`$VDHF3`#6z393(0bj=2bD^iu(do{1|7&zmj1)vm3Zfci^71!)@>j02vAX1V8p#<{GBMAzTmEGIgN`X<#O4gSTo@cGxSaCdV4Mf8O$mSpg`uH>18|)}(3pyGib_fjLmtD&gn{~40O=nIgDE~<paz`1PnHys(C@|?RE~w(bfHHt(QjeB6B@J3HG7_c4*c^xU>~yS?PMDOXjjQyrb3<f=PISrPGktMe}A(P3Lzj6l!I>y0RP%ycdp$?Q?$eHzUL2*j_ev6ab4#f&{CJ&B=^X9l-oFp+8J=ff}kTO?%)vnKt;tlH>nCda-A2?Hy*FNxCH|S*e#C%`<jBGdV+%-=6{rHFwJ2&s8<0JUi>|{DsL0mygwI~O2La;@V=uom5vk}8%K<zFtAA!Ky|X%f!dX{te~8HOpcRv=CnP}W=U1Nv&C%%?XF*KHoB@g0??=A9$5BqvL-DPZ1h)D2^@&v83}YX7GO-&dmeQ*3*-uU>Qa=)$_R$K!3A=TT$D}_7xr9kQ)^_!b$+>a={~$3!0Yeu`Uzgof4R1D3|=1t0^@HM3p<L1as^%`cx^8hcEVek86n!vY|!#Mt*}}P>TWM`bwd&#?$X98h?8XVF|tZ70|~Ri2Vu7zG&&A-&8I<9DsngO!RuRi0g^WW$s6Cn>w9=Tgcl%u;}N`mP>6v0m*D=The!|*;FQXh?Z18fjW>7f3?{39Fy+}6#lV>l=f3=FH6WZNcihxi;uN?`qn-?CS|PU;Z|||2wMGFbSrHD;z8-&H&b2P%9*B9oM*|HXe2x4_b&?G(zY%G54?QY!xgK;w;PhC<^VGN`r704RPPZM8N^sHd&bPu2N>X^(aJJQ*$MMX|(lPHJE|p5trJcd+%Ej7jOZnEBn~c6Sv~S(ce8-=e6MkC^H!lG^;}U`?Tdq}%YhkAvw15qsHK9s+w<KB!40YeH9tqmEEJZbrtr38T?-4M`+<uas?hxYOSaT;ULJ7(~03((mD|+HmC4OjzcB){<$hxA73Bf;>1ccP<jycpxSyP19Xo}EgQJY?d_q*h#7sY<6ttN@RKJ!B9$W7`R&2Aq2wHzs)<0$;@<zRHr)9A}B!OakuO`L&xwg*}ukI8-1iOXbBTkiZ|VJrK9kqH3X3Dw<AV{UdbjC-6-m}DcIL1>A(f5mXPw_V5eoMJ&M2W}@4f1j+wA}<~|x)IY^x6)ZAkUo6y(4O5RyAS+%|DnI^-#vO@-w2{#uOa%<M;OjoA+Xi#a01z)>OICrxW(=DD!D4rD0%Ube%NdE&nd0q%geTVu;|9AkM;SIbxCUtD0NqY>U6_)BWTaZf>o{K_gZZ~=r(7y#4XK`gfaJ=93_U+Yz;eo)Dy1gB`7j>G2CAyPia8q?SYbqoB`Th@&&nJ-09S7)zB@AWobS)A-V{=NA|j9&jVh`MIix6G#<LLbOHzH|H2<{e0$BIS><i=8Tlt43uUcBkD5YpiY&AO35?D-EfJMBUy@3Maf`x$RS>R9e?%}0Qb<JcsWB<W9~jPRQ9FZHSx6HcVx#l3NX<S)d{{Be;1<LSgsbtxn?Sn&rv3k@sM}R*gS?9B(ZG$_H3$P0_Se=;n`)LB-M*FRN^YXTCq5y^RVPIk^E`6|k{B~W)H^qR6<k+Y&r-xay^r(DwJWQRvJ{RxN4}zN60x98Sx&@G7|1BT9Ia+jJw8?9bvM>6yLihn%8x$H0wo4wu%xA3)?NZ_@HkmCo&1O_da~)(oNM{rpbcD#*Emy6z0S|-Z9$oN0$wK_OL_<b*BSpC!F3k`Z(qw`pcZq5{_^_%3auy@^%ak{lwEh!s?Wo5Wwxs*6Y~SDV%HlZTcjrmrlvZO=?$s|J*=Bzq&~wIEgjaGG+PbohAHEp7(EI@gH|hSOo4<4hBa@Gf2fr?XN!&!(*?hM1pD~|!=4UMqKTB(!vG5vEx<s9-=VGut$xrtS6jBnW`B63Ru7q_Jy2ZmQH|;JE=+DU(Vv$*&lcH_YWjHgxnoCSSViJ!1Sza1!aBE@2NpHTo7^}r@b@MDegl>=)&d)Yi+KSr8AVi7Oqte`)X8CeLX~3{Gd_1)^k>*`H(3TIJz$)D&?CIry3BP`R#Fx+)tcHJ7bE>lgO2VZ^m2k;LhFsbjl$<nWZ~2?RK$JwTvk4pRA;droW=GDt&b)GEl<yxpAGBbY}l|kTGrF#ouoAg3!*ZX)r+MMF`l7nTy_&#vR>3=ojO`^4s6ai8!{pFASM6mw?zS<FOW~&SF*9ti(2TQko6iZ6bG0XSfwue=y{?NCc&%@Wo`C6b66+z+#+kmX>QlqYVFGxlj4uo@>Y}ETs62wR2nw6ia5r($hLUvMqY`6Bh0&i`3hS0GiAh}&5v6uQA;q4G9<novf}WB?U`CI8&y!s8kUfuW?`#t40vA1cs&L3Qk*Y20b@Fp$`w}l&{Y<>cR0Zs5MIPAE3bIo{f7W-J=4A;b?ASC`Zzfk=_gN=)z(PDmQ=hLWIAT<Ew{s|xoYS`ru?1hdx5uV%Tp=vk{WDA9gJ@X*okkKYUP$vSd1&6IJc+4gd6A+<Sm0V%}69p4Xsf_GfAFYHdu1m=k7G^1E~3^y<2K;1q>Ov8dp-!ZJ-S8DS;?UK#RL9FTlYj@p=-9UENw^F5Hp`OePtPescf@;#DOAkec|_*_PjI;Vwz75z7Qn4fawspk*54<1K2m7Xd9z2~cg>fHj&q;D+Iygj_+2jg}t^kX-yIHpxDZ3N#etzkYIfHA{1lXXK&h?)5xFd@&KY?XZ5-R>g69O3Nx@N|$DYHvRLWkjnW%381>8RQ9+rHDkk3whwr69Pb^NDEIgl2vQy4BoAZYU;nKr{7Y;{#e`1T!`7FrgLti%)cDb?A|b7atU@<O)m-}CDx*S(cDKga_EtidKELOu=@Hm$tsBm6+GewumMPIZfv?(PdzIh^99oCzGL*K*$4BasP+G9gKR{EpCbJoetM}0iReD|$(YJ;Q+pT#=+72!9No}@8Zg&y1$S&*H>6h#V6l?r6t&N|fc^f|(hD}xLxpR)x3E>*6DKIMlv!cLcttZHN+;M%+h`yf(E(;2qN&y_D|3|f}bm~Rdb`y~pNQemiEKJUlQ&3#6vC)#;UwYU<nUGQ%pfU9G#3guP#fMq?o!Lhgtw8U@b}r2&vlO#fs16N#X;9=EYs{h8jy`%X2jP;VA4k#cJm}2Cvxc;!9L6W^YOW`7b1G~!r$R_mi~%W|x+}P+d2(6X3-;79Nh?h4I+?gNKV1({OnKb^b{bgC(*NA3ieV5ucPaqB3o`PS_Toek@}KtC`H>s>o#rk*M?DQ7Q&q^$*j|e~@CuA%_HqG4_bEB=I{a8sP}%{ghC?am+x848(`BQ^1*u-mSmWRS=pVL>BP~T8X(jpzv-yiW!k;0lRISdC6$UO(8$jV~k293XE7nD^?>t6Gi5>e?y!5a6dk8!VrB>yKXq#1dfCw+TPr@7k)dQC8UA1?+t*Zmrd@F0L*!*&4U)-(96PKySq(sB9!*V#`T$agovRo|CbA8_r(Ip>)c_@qLPY0GC(`{`x?o#YkvswYz4mp{7hX5ZPn{<n(Ddy5GUeM#4E{i2{${iq|!^#T?eTjUbmZy<b&JTjx&RdkV$2MFb538}Pu~*m@OVi>yZ4B`G5H*mSs#$bIF~iDu>dtb{ZDq_HqAN5bW*fb9FiH=vqm~%f$e$`uF0sOmvVuY63vR<lFq#x{lWpwE>&P)3##WHLrxuWT*u$H-7vXg#VV6j7A?kD_?Ixy~t^@elaR5GpM^|>jVKooPt0dkjr+OK^_m^By&^)8>{?b;ZBY}q&PA;>6_GVbxDL)1B)8xj<3-U`SKUL+Yss4_3AP=tcd_CUwbg2a|7@LnUL*2x-R57X(*B*eOTFrsxBA0KkxC#vIxf@R$Mma+k?WZ-c8}z83N(Ze&M-h1Lm`5mJJxd!zRjozlJ!72<9f;{jV=>G0mFsecS_zy25Tn*Goy;|@Q99SUG++yuQN%W}U{d%IrO=Yh;|9n#`}kuD%A8uqZ->)9ow|;rh7XU9>IPPnr%N;Ta1~3#t87*=o@Z0#mK`<f3Vw1tgOX)(*LHZ2Zz23(ZFYz<M9WrV#fW_i;HEhK&)};MrdU>DsPDo5fniDfB774^Tvm5X?--lqU%LG0F8echv7W$-FUYY}PSBj%UXDcs0}$}@f6YT~9Je#%I`0Sbm<$P;9>f$gPj^EZF4su=SRmEBChHq0dIsh|dthxxJ%TH8dTL@UmB)`4qmO6QHc<AyQg_H6B;y-KRolp@!5C#JW+E4h>vGe<UL;ec;pc2tiv>LzXUj(o4spJ7U#~Ixk&MooOUcx}QcR;xlP6T8j*;gQWzhtR4SmFwk2Z)*kC;GQx>EfL#I3qA;ilv;Z%u7Y$^kFatSCv+n#8Y*-lTS-1*zTC+*F-OzIoS^Mn(H{dWuI=+1TMT#(xYFiCpiKYU~UVb{Mg2GLPZ+Tq?z?1jJ{kIA0e6NIB|*c}lxd=kXIavK%crbU23=Y}+B44m|-fYK>0VMvqaF@w<-`bP~+V=zy#TxDNi0^apu5V7et$rMP{-xR((zt2~kvQ6#>GQf!r}sWuvdAcje|0*I@*t0ky~jvgp2d<7C%hG<jpwYa0OqBNzYO;I8Vz@shT&XFcQoK$O9=W6<Cu>Q)d<gNxDgvrsq5W6Mzq1usMm9N3;;?vH`rjFDn7fQ6Q39Kc}WS`ZH<=jT>5OPFO%F&#Zqt`6V1)`DvnNXJG)_ySy=48TlO9t#E$4mE{o1-Wl&-^rN6!k+=;+Y!uEPBxGSa<YemQiiC=IMbW_lWFHB2rgXhj<$D8Ozk1TadJ$gj)4BAg+{zmlJl!bD48doWZpr#%NNKT@@Qk0_z^3Rug-|d2S}`Wj$}GI-~qsDoVqCZl>phpJ6#YerdLi_JP`bRZ1otyRq_f{8tcSE6UwGTJ&IYKdv~wtZI)wvaW7*b9~;CT}9Eg0wyXa%o2UJUfduVptE5k;=p7(sP^|m9MXjf?bn_rb=`*5b%uSq&gcx;@61jPTR}a4CM|1Rl$>1BxXIf<y|V-W0RX6WW~kJhPWJ=R)uCnU+2@XW=2aPqdp`4y#bwZEX&58SXu%j!?Q8G9EmN9PZiezW?;Lc-ZKv|2)SU@0qR!|gu{cz&R>K{r4U=A`vf2-LsSO{`#^c#0N`+}UWmL6TXvCdtJJSQiRXb+dNwruuFE>tnjT`0TmW5Te!Xgu%_3*LgI;`i;iS^99JUj11r_QzG&4%A>K^~Vgf8z+%W^vBTKZgh|c&1}jaah6jn4WtyXqyu%?D@SB>+^ft^FMLQi1MYir0~`E$<N}K!+;AgQ%w%eljqs0zm?K%v`pLxH?eb%KTn0ejI$5vk4{&yUm3&uBT=he0-$1n`S~8AOgnOkD~PCp>A`C>J&+GvtdV6m60rCUA910qe9mC3D7=(B>!x7k-}tC+82jHH8T0Yy*nG%=_V3y^0)p^f_V`>eB^DPP_Tw+{C|^-nZ)HH~l`!DYD`0@f^vhEDDa|LITyt|tIh&R6B#vIY&>AoL6`c&Di~k0nqo?IJJ<}2sq*gY!6`TPT5Aler_9JGoBT?+Ikj!p{ty)wh^&D<NT{%<wksY$bx?E`X@`T3e=od5yYZr=&vAR8!)k%uG4}09*_Z@(^%>0q}&{-Zb#KjzC+R;9)Z874REF>c=2W({%L>}4t52lY*mH'),'Libraries/Compiler/lambdas.☾':strd('c%02z>u(cB5dY3!aeP2~mpGE`5LF;qDz837Ac#l5gvj#aTr5lyogE&nDv`9%6a+XVf$#`~B9MR*QCd)1LHl9<lH@PoPw33PZg;(Y)NyDnCAW7sJM){_nc11Oefk5va^%<-em0AvFAp6VIeI*s^+|YsG9n4@>&iqvSE>3z!XqSr|D0~m{{5d1kL=wud@Q?f_`sgSFoQ8VcmOHYBp9>DBS&C7I*=OMwyhYJJbHsZ%jSy3?Ag;eZIRxj?|||Vouf}P<iqm98WFdz@OE*A1iQC+@F|x(^3_4&mB+oW!&<IZi?sP9lw|mc!rD|c?#b8exi6JfvqqC+3GdLzetfV@-_om0?h>8OqyxWSQKiNL)CJ}}qPOVJ-tLSi)lCM#1K+`e1t5QKy~L^93i}TX`>6n*a4?0b2x-6VqthVqwO`4d$rp1TouR9Aez#}e^D7z=&A{)_5HPw&pZm;gC#TZM<SuS8FRWBUkD+=`UkAQ27@G;^s=;~&LZjfjKpB|X-y5H(A$J6s8!w8*Ve*8Yv8g3zC4sR72?c^~lbf6j$BP6+U8Ya6#jucN%&z*v?u+ypeXs1!;QhjIfk5^c@dY|QP|u0)RWI=^c7X4djZb-)+dXAG00H{3c6&UU3gNaIPh$?0mLxDvY2&2sRD<ADgWRcXuV>*l8HJ^Z=uEDbJ$I^HJsn0>1uKp#8}Mj)jQfa}$#`Vr{yd2ds<c#WVnx#0xS0W$=pAOj>-2Z@+qtV7m*+Pw&k1`-@d39-xfY)3+8%xZL#$ynOyv;4hvoWP!aPaRa)8%GILm1~*x6Jg_U3*B1$g*XE9C;Nb<otbsj-*^S)aSOUVn4)L^7EyeG=w(sZma|IB+S%cYF;V0k`j&dSVDfx{m{Rmfj3Kg{67SJf>IZpD}3=G#EfgP$ZiA$dRimG7X~<T1(6ZL(b2{w0`?Ou@#ff#mF^xN@`<=_b?Ber_Wl%?Tf%C8xJ3l*w2EX7jA~1u+q3lj?AMhz>`mTyc$Me3_sZ|d<{S~Y$M)q|DFPHx%r^!=9kvzW|ean)hO(Nn-8Qq_w#{Ndq)QvMz>j4H*x(NUmr;I$k~_wYiH*+u(#T-z;Dvkdm-Jq!M535<5ixff1@LcU4v)-_4>{A`Ypb7xOM?G%BxWUsfS8Dq}J<8>-Brqd@a1xs3b>)B-?3c=o9)B!OYQHK7VkJUJ`|Ft>P?lYf;DLt)oWp{Yu_lJ7W>`M<Z+bYQcJymamrRMeEfddllJocDBXI-C>%((43*alE*fHp-XsHL0+qj^5IzEO+*mh_1}nSCM+(I-~wnHxkNUXHKO$zwo#JJHE*#L$mt!D8+r51DA}lAJicciVKFi>c>!X>E@b&!y>P7&Gc_T|ey;1q9+a>xBoFJ7jcOk2>tWn!N}fOjdk*+;U!O-;Mbe(3cj-Gn*jk83TS7dlAmZ{N#OUKgJgh@(K?hy>i_S@>d)v+Ym$PL-BRpw)hR3$6|7ozqu`OuoVvpfa);fc7WXquFR*~KJzlOJW3*hnHY*AEl^Ymx>7rQ=g-HJBEX-#iM8+v;#q-jdj4qAY$vGE@<f(nYd+q3ZZ6A@<#?^yP?EwNM6e$cQ4-x4~voV8C3f%S&0oY78$(}o5~%_}m}D_A~DnfaI(JU1OhPF_q%C%mNQ?it}vCO45fSw~S{a+EwJ$!&`hsj=#8E8S5g-i~<dj@x@)<U#iD^H>7~8zw6-;oi4Yk`)~=?<xL9P|h=lgl*y`O&hOK%I-3;+(nsa2bIwP=?BIb&<{mm&x`AdxGuCV>KV-)nG`G@Pnz(2>Nh!|?WB#6r>(q<#RFI0N}x`k;BLP?Bg-mgJ<cNG8R=>P!V`Q1Dz{pOoM+1dDP_J+`1LO7Mau_)hv%&<U%v4hdMzzYz<<aNj&pcMBUjyc$a|=kXOwKxr;an#QZxyg+b8F)qi%kTIlE*Y@`*!r>zGU=Wb>53p|zUI6=#XvJ{rWdz?(B1!8+?V%f=gAeBf|+VmwTEY)52zqjj=&PuaZ1!c*+#P1eiiP1b5-ljV+CM_PF)e03hA^QgHdu0P1DaNyPUl%oB)K_9yHxItGsO)t)EO|2kU%JABrc3t=ZC-{S2_Ic^d-zU7!a<Dle8QafLOZiQW_@azG7noVtF-YPI9fK8f5`@4!wT+yW4&-32X(dNL@oFK=XbuBQuC|Rgmt>yq$b10{rXz@r!}L#K_;Sw9>5lxtGiM<)%6)-*=vZJ`%n}>dIw@{<&3Ky;{89;i=oaiN_snFpeUg{p%Dmb;xqEP!v7Paxfms>{)^om+f+;{zqZRj>=wGll7$}V#<7zH#AAibRB@Q?-KdX~XpY6Jj6Rcdp?F>p55{z=@W3XH51eX}W+$<*maTu}4-aMt%;)x+s`e|z@UaWMxmVK-sn4!<<N?Z=0AdxDArX(wZWHqoNZA(K<CXe<qn6(@dRHV51yZy$s<YeCoet?1t=kTbw*ED%{mW{fDZ%XP;gH2;(-q~xM3aCtcT>uuqKCWS9zBF9~f5EXv*L-<gE4Q=%k9R}VH~NOC5jZAU3!jUiUe97(+wg5dvwGB39oJZSOk_z7P^=<b=%LY~%<QS`WE5gri;t@X*WF&bUqyV(2J08C!HR#;!+zGnf6p`Plk*q8Id^udR>fa40r7A28h+I|kb(_FFkYY!u#Ex?_vx=0#%K-9jYl(gU-OnXS=d#Qqg+aj2GwXtjXqJMU22q9qoNuqe)$w2>o@TSfvHi`bt<2ktdt97=Sp?C7{clXAh&$9Xxy0#ntuQ|H!y$'),'Libraries/Compiler/expr.☾':strd('c%0=LTW=KC`JG>JUeKH|6Ul3*7hGAYF|>`k!IlkAD{Hl^$7IE1cRM?7$Xl?88>az`*QPE7V}c=}(2Ay5g_I;x&o9Y7_KBa+?>o0SXXea$*U+dHE7`L<=bZ0;pP}qB`*e2xSF~EiZ|}T2J2Q8tTBTkRhha6jn0Ns>AGOZaq7L-~;(0#&7kj5pp8REb=EPKazB*k#HFX+JabUkbg*){j_|9+7%)<A|Tcw2~M;5~+vKTg7i($3Z#zR|dgT3%4ju7}zMUlQA5K1F5F-a8oQNJ>}fVW$jyCr@%&fFbaP(++ORi-5$_eoTD*$wsrx6jO0&rF>tpQ@Y>lUkC*v;`=D-^BA5{0v=}*f#r$Mz#0PE!GHIVSi=a2~u#EUrA$$D7fN|fJ`PQiTCpM&08J`qfSVGoU809wYO?I0x}}+bfQK*q@{qIZZ$)o&zD=_OC<_O%=x8)yXQ{9!O}MSC@;MtIi;+B$G#p;0+-n)`-Xirs0<32&$AeyxUR4-1+Qf%n{$J6s4ao5v(MOzR0(_mh^V*P9|9f17?xTwNl2qf%ED;z0}Ljdo8F!KUV7UWAcv-00&aL^&-j&Jp6$Op-+%dpxr`FL37o;LUw~(Z0XY*dhw=xPVn^{TCH7Nw8ovL;_^#xe-Tz}_&yVc=CD;D9jXmS`{xR47F=J23-al?>_Bd$v_<~kJ7^S*d`}(!%X6^@6oo$qcab9Kn74Q3}S3GnSPO!4nfDEnh(x@TT;{#~CkA*lj-p4|m8t-Ev<3n1=+qUm>=a=5Ey?M^*&3l7e%nxZ2TDgW+-#Bmn=l`WQYt;?t*K@XC52)}r)SELl^8Nm;jE!K`<l6b~Tf3Q^X3e7N08pj9=>W5{R4<e@45tQ{<37qMhZ~5bX-T6D0yKsz3UQ7NuxDRZovJ!_vI~YSwplpP0ue=C5(h|Q)^>!!{E1_GC851Wk#mD_iIYGUafxpzYbg&XA3IvDK&P~w*D(i{yE}(f?Ei{1-vD#zgn0`9jXh_pG8`Bk$QtiJK4u#fdZIsk0)K1JfWJF)5__&k>>J+nY_m&~%~nE0f9F%#HhQggwfC%BjXdlW#aciz?HC7zjrBtV7+-wk>%NT1&Kn#Y6NMiT14Y!pnLuVsKN_LY%+VN28gXq18XxzgF`VQFSJ-uSLm%TEGWF@m$oW*E{2+Kjh*mQ*Da}c?cHrIKzn*%Ta!}iz<xXn?h-ry%H2)KfsgZ>5AKIAWFj<b9Lg8y-e$uYRiS}uJ-3-WLc821rEN-N{do%cdRF4a;vB%Cnx-n=U4Z>T*T>4fi6&+UBjes;!qM)5FyC$gE^yMG}btGmP0UY!fayb|cNho#;33+F}3hAopJ0fen)l3@A<uD5Y4sWt&rWAnHT!iEp<h&sd`&=B>E*#M*fb&^0EreSf`<7o<`1J;R#wEAH{>*ms*yr>-p}(A7w?IC4uMvgBO>Z8AJ-E>l;$%8O;E)fKA*D3WvrLrv1*nrqt+_}jGM8JOM^T9lMZ{!_=iZlpSH*L|!CAG!aW-7?!;b;j!7ae4wcBBH(er5z1LAhVOpR$MOzl=1(D(yn7#l%;j}8$Hvyjj(PL7e1!}ATVAM>%w&xEJnvFB6;qXt*BjLA1;n8KJmh8*x9RtF-Juv)K0ksZsP2P$)@fToT8;E1N<c#)-ey}x|kTixjG+%@X`l!-1|rz(LC0BX0ly54*IabHl#NncRBo4vo52U3&_x7i<gRz(aML_wAbKak}`DppO6<!y>0aJoxo;hN?XIa6+Qh|KO?w#x0Z%dW`lWp!1^2HP!@&^30)J+Z#Vb_dNuoaD2(n^tVTMNfn{(Cs-)-rUG->9W3S9Flug_bz2<yOu=jl=i?H{aniA9=~qj#9bQs$XTZ@xidi&iaz8IR7_9Wk=MO!X^<}<c6j>bYKYv=TcYfvm4hD{<k9Q}L}H2ESmJ@PfL`Lr5WWBiC_7;_yx5N6hM#$QGf+j8s#q3ATe33GS>;{um<L0UD<5@;+zC)q;thHLq%*7V6FLhBP^f)8juy~aURr8gq?W!VUU4r?b|OpuDXkvF23|^M^E2#|iJKoEYS<voo;YyWAoleiHu%{DZK)8<%4;+`VGQAvjt1rfM$4yY-}b`mt$#E<b;i?PV^(Np8NMgX3Pe7}Jzn)Nd~L!}@(Bus>L8J3lwxnxkG*(aNNO=GSL63Oo-+dB04Qf8s+@{qaW(x!@_}A{j8qDeaF;!zBXBzXfzBk_HZV{iFpgCOv~?*6nAZfn8sg%Fp=p6Hs0U^EK$`6d{m4{i?UIj(ihW7#pZpFXw$sYZax0L59?9bQU>8KS=N%5>V?X!$uSlR+f5gSV<WfBk7g?`J&GK8WvND{&ih`ys9^Mi7<)LKb0fdaldt#)P>ewXAk*J0gaS_UcZH(a~^1tzOa8-jdv1E*(KvZX&wR6xECM{7%kXAd4YY7<J(ar>kqRFG3pMm)JB^JM8{N<6OL=ziD@D~I2h*RL}Nrg(stl(7-S^=6XBWl@ve_^L6?_%T}Fz@Pq7ejMeE!53+A|Ihm<%t|w_X~O`U3%4XRoCm~M8u73FK6+vW0nqetMXLVqD@Yjsc6QQ;~1Ifm}=t3f9{x_EhRB8LVBNUdun*YBZ;m?s#$dlk*%`(R>G7+zdrAVT)$WCw8OfWZQ{-MLqr3`y~4oNWmkv7b>V~R%iCKUHjv-5C+w~Z41!m$rHFn4cvFP&awUZ_%{A<NL#Cq0kP$ou;-_s$m+eXKe@KsM-hHgt#VJmu>)b7Q?hAR{me*a{4{XXsKt=@ylUoU25)LP*!$j)Vc*~5>YIbXBPY=8coNU?{REWXhSU|?i;cJn6Z9ZMvHw1Z)eTog2WE5w7Io$%khmvpsW>fAcN`|jYZL%*+IaS6mt8m)X)0<bCC`*m-wj5i}{i2t;v>kx_eP;$!ROY7zj@i$+PjyJV&i0F&swd7@`<(q&;ro5~!Ko@l<qOzyO&31hts8cTa`o~9HLE{+;s~;7d<MW55Y*@aP#z2frId$4Ein5g7;b712&5TvG~8l}F&ES`#ZNs=Y5nH6wfG=u?HBNQ*pT2j#QnnquRsiwx<PV|<hCTMU3tBuuGC}SPM@9gWL@<c6$RD4@c``Q?e%|ns?vIr)?EI70DvuwJ^'),'Libraries/Compiler/tree_txt.☾':strd('c$|$@TWb?R6n@XIn75g&D>U{k5Ft%M4W>=$1%xy#n`Y83-E6|{1RunQUJxl(p%)RWVv$<0Qk05_*r)SP{3V__JDapgs@;cVcII5Z^PTU^3fO|}+4+0IarCM*JzJSua2&x^C?&Vqir=ogek3fLac<#nY?mt(rplGcTzTHfmy5X>^q@fZi`ug1glpQa%;LIwJ6%hq8nVek`7rd9bRrcxUeJ(%(%uKK3%{*Qis9om8Siiwv=#FLwj!0QRM;~@ERq{b{e)6=!+<5nv@epvMB+U<imek_)$y9mZe*CQv0E&yD-)vQvrLvHg^%kfdLNG9C43z?O4kxL3dOR(0JuXyo9&RH$8&gnO{usQaZ7N`mWsM{XQit*`sMda^}Rqwef$)aO5=)}SFOds@#Gb(j|9JZQ``x54^KDX4E8j9T<yUN6aNxKf?3j`huc9Y2bzH#dzN*@J+WU!Be&C$K?6xiGB+9aBAaC;CjCenK-I|imZi2ihi78CQV_5Xr*L7j7++Rbm0z3_B5h;pM~|tJ130Ju3)r;TOgoU475i?%KD>i{JY0u2@GVO%`iYV?C~W4tt$M>X*)s_(M#P*gDP5t7bpSgQ%OLpx+wjW-vWRgKk!2v%u5w|NSF(mR&}(`!d$`9banE7{QJ)cyO99Cu>WhxrekZZUb^6kJ{IV1#Pzn>V6b9#yhTLs5oVwp$UW*2YTSUqY6^S8X%ot=w=^w%C)}sDfiZeH83>oz#PIh&F%~_Q$%EK}@!4o(pRd2vCd=!gQ51jm5F}F|@f=_Ziu<zju>}r#$rj3vBn07qkf1ZBQCZi2`ujlzpJjCCH&X4<f0yP#ZPUMXi(@8&(M?^)_h$&8VaAJk7S-Ve6BBd>O3qRmwczTTV`qN`w6XO4#`fj^RG#$dO(67V=$x*;20zQqu0!E)ZaAYVR(Y2-uJMpd6!rQ7p8~^Gw>JVL)vznT|XfWAA*p*gFG=21t0e&}J)xxhvbYl%^PYitxB|R#%gyLK55I)D)socNg%CN2'),'Libraries/Compiler/tree.☾':strd('c$|e)O>fgc5WVMDEGO?)MoQ9KL=J(34-uM(_7+*IwB8g;#*XZb6d$P&hawfxf>aPfs!*>SKyW|^4)e#D9eZsjBw#7=cy?y??VC5t;W?a+_wREljrHKsc=Y%{O729lucXfADs^0T9L9&!Fy+E!jwA3tkM8yR_lBd}z2UyRGaU5xFptVT9GJ*532kzZ#%ND&w!B8eS2N>#3+M1t2B~}!YnkfBY{sn@b6&u;%XZ)jUc*b#X)t^OOnU~G@SW$Y`0)YW6^k|iSJ;g%J63wCbyBP7Xr~rxo<!+I5|K-Ve-*!i3;4QPJc>1KP*(j<!ObA3Ob}6}D!-PSn+#46&Noh|zVLAR^w6Ig=V!R+Y~znsE8awfR1iDlMsTTO2gyP;xIfiO+91~HGP{u}@d`e6nBBOD>1;aHEQowZ*wp1VcuUuo75J<Q0e<1iIsC4b#qg|Z{T4E@*V&}$Z6tCQCoFJT&bCRrhD!q?o1|fIq<G6^dvT<Mx2B;_a0)*v>e#I=3mDe25O|$1Yfl1CRG9QuWfa{d`iTLZWO5$Q@t4*PH&5ba)-~{4OgZY_#c5InPLgQ7S*0pY;0-Fcq^gjEqZ|Wm?ikkd0>$93lWLAnJF_4qZgQ=Vi~5|T*v!Dki$M?yGvAzt1rap;O@aL|?qto|^6YKU9}Ia*7?164Xg6GMWXbQpf#-*`mkkD((^g-6$0pc!Sf{1XL(X<vc&O9$_+&$TyVMW*(+UwCxNWybyH&HBbrN=wgx!(^b1`7Aw`v(D<P6@IYBtkYhOVfH;zVNui+=#;BSJp'),'Libraries/Compiler/node_types.☾':strd('c$}?RZA&9p6#nk7m~V5(rc{NpC6Eukq}|f23GNCDt_))`$%ZDGbTYPqQdq5T-Rh#o*eHrdt6foqmQw7pyM8#(FZ~z(f%+4A?#oP)$(=FS2J}wmp7WgNyxe=wP1d%GN_MuCb}Xw<QS!yIWjjjRNIy6G2rR(M)Z>Rl*Xh&ek5b8rC%R75vYE>j%%P8Rwo%lXq8d?h1#8AAREQQ)R8_<OOgot(nl|;};B+vWV^$qKYuQD^`7bb5S$B+?f+@q`vcqFzpCytb!->cGXd*s5j#>=ti#V0^lq5E@`Kl6)(brpW1`9;}=g&IYQU6{?_`bf3nN?sOet`qh4^7yBA0tX7ramj7OvNn6R0SVU-~yInpP~&jqV#jYx)$wI@RKtg!*OgvU<ppBDN=DVrfn<vtWZ=;)Kl=SHS17{>Nj@YF;$InBPenOm&COVbFc?H1Wjw2@`3kNL$1^qtivk2C9X|s67jNy*~)WOh)}Z(jMJkZ+jM5_l6XBeKr_*VHTadWEf~d_jG+kcqsmC~DSBX}zqH+mXw<q;f%iDRf?XEVc{qVnGGkREia^0vmr#q+u?~wZp6oR;O{wTVi=!XYM+fs&hfR1JX%S=Qwus0UrHPMoutwlQBP1gjb(r-)It;UfvY^jF1AZeu?qwsB=8RX#6n{C52nt2W;KR+<3zg=E7Kuh$A>zfy407j0wNsIGc+IUHQz`zPB2pzLunQNWOj%J6XqYBChf~||(l<3Y?N<6&JV6FE`lijE@TVG8Sgw92>h1o<vFaJFQf;}AUMZXD4oQz;4bFlX;uOna4NmXHw3T8(rK);)Z&B@%dfFz{M)N$F=KB9b@7d(Qz(Dqa`SB+`@w{2v?n%yreIR%2IM}hnZpYlIZQs<8+~+3N?RDD<WVC8n&OEU-F&?-hQN^ySx+}RRw!e<b3PphTNP$;d4Vt{#1XQydip8ijTlAHuQ21HEo&_j=^|fJlYl=+EHv&nXYOu%6t&&zg1%0lDxb*27mdQ|i@)m-VcfaM`RX(_Wd#f`PeATPqvb+@cg1xB)m*Q%#rC7r)o~QFrjK|Wm$|dR)%N;xg$dRke#!YzBQ5%tN9IHHvIFFKJv?9*o9m{P4=3<oN=;Q<;gAru>?RV^;ZonVxD0v6py9YNWzbXo1Sr}i@B+O35r0eEMsCyO1mbupu%I7`B$gE0ZwC7{uf*yu~VgFK;q4`lx#Mlf^pJ|t5Xf+?V-l9d1ei@ouN?jXLC|WUX6l7?D+gd2v%}RrTN%tE`-TB)pR&-uF<<*?`g6)7>dsiap9{A|G!Pp9=OW(_!?<(J((6Ef9XgfmtsHgPath@-L<T|?N%XT9OH1ve36!K|$E$R2?N}fUJ=!KB$b`x7gei1+cC0|j-t&+(v1ioW~ba%_xhT9HpJ0&w#Ibgyp(-YY(0lG75tvi8YlrmlwxdM38p>Ap(EuJmcb>9ueA3|2OwC_D@-!JEJXlQQht439RPP(mfAG^Bf88fX5Vt4G!xBFXH-N$zaM%|Ag?rH5H^?7;s;FjRAuM|!Kmd$BsiT<_8Sd|UDWLIRxy6b~KzRUfbU3L#9NvJR3+zWM;pT*G8oSe6HE5RTaZ6Jfw9SQRvr~yrubvMgJ*kl*}o2!~$pjA=jhJ?Oe$UDB9N;u(mJe%XS_<Cn>0N>mFpH}eihx@S(uKXPq$zYelv;*CWC}xZ)&0|)!Jr%m4Xhb8)STdzQ86HW*r+RB(7GNJ2_HsZAbD>SMK=NNm+SkBq-{yaWK1IEs9{Ao;WvCmlsL6hX;LW~7g%gmgbe%b*6;TNk{YBv{0BV&+=NjI4y;`7afzVAUv?!|eYn3^3Zxeh!4v$0NLFa~6C{@K;SQ7JVVq9=X)|9h@i>Tw1iG=DcpG`5v+)5>eN8=BZiLv+uO8g5S8DYo'),'Libraries/peggle2/gram_tools.☾':strd('c%0Q5+iu*(^<7^v2_SGr+623D+W>;MMH;)P(WVw`87LsD1b4+<5$2K$l1f%-TEwy}7k1p(j%~=TTSpG!CXnIu;s~)3w-19p^&#I7eM!$5&J2g#i>U4@MHYgVJTvDq=Q?L*Dc|H*7ta2a+BQC&dUN6QnMK>C*1s=V71H*@hU3SSRfuIV_%CLkUZ9LEy;57AqQkH|ju(uBAGLdSJM>#l5`|+CO59#zx5B97B&Epg@Za;NWWG+Q?{pd~4(V0M3_x%4Yw(ah-I*tEo<4yr@9@v~3!t*YxB107-+-@sjPlF;79E7g#8dz=#sse${L><@L$H|b5wAt~MF8y~KLj%3`mu|^`}`j50Y?{+Zt}a7(Z%{=wB{m{wwpLf648_yXafKiqm~Ow`t@%Zs-`D|41@@`_*WfMPz9VP=_05CFhe2*t4L|cyF^HGS;?qy*woaD+rq&oeAh%nW87!+Qv^O5j&fvDQG*IjGuR7k#avRsPvj<RQJ~ptv`zje{w2SXA)-1nGzmxc>C;kmIpev(Z}Tsyp;kcx^og$4wGLpf-B%OPN<b3IQDFko%HDwOpZVoCUSHIR!zEaXeXr@#UxWd8z#Ln~e=rnh9Ir0?>?EC2<l(tyJXe(zCr<vH9)ox}wmdaxIhiRRe}_y7!T%k!<y?iJIgi|ykaCX7mL!anxwdfZL%vtwFd;i*!W1HWoF-;uz=jx1>AU4cabm~biW@_6RJjj*`@{LvP4+S*0XB_<N~Y8o+_mB{X#hAXK*9YClhhbO)GB@A#lp@<<9BqX=x_e$w9z*|8s(Zt>zCVO`sL)5rfb6JI30!u322nok4}p_{5pU7|H;%^`I?-eZa0@3Z}9i|R|h4=X4qX%!|q5_6}DPH*9N9{`R93!-Q_RjT0s?HKjH;sut%B6>3?*+J}u<%r2kZx$*h#DLP}xOGK@*65cb@piF(j`MZNO8BAZ%+<y8NS|8sICK)fgD++|e6#<yL{(6o-o7!nL7@LD9BlWvpsm`15(D071;9WyD-<tZJ@QTi5bomsAo%_A4vHoF_fUgCv8Tr~IRI!EE#gIs%}N;G180!2dfQjkM*A5~?#V83zhOdhY2e&3px@1U(3YD@ry1_YQf+)w<AKc~JIxG|MN!SKiYDu2#Yg^5wJD)cz`CQ|Me|0GL!nW};?@WZC#lURe^UiExww+Bn{vf(%46@21&x!|rYXMA!F9Gh8In;Dmk+mtxJO);zw`%UmGO%px9gPswczzx<qZsa5`Rg#KY7V8~BUKH@tUb?UzF6f8lViBh1$&3}2amgGBV!o0yM}>GGcv<usqT^yG5p?FK5xLHVoH5=R9FF)A{`XEk@-`q$ZqvMHR<aI#ih8jfuZB@F_!Qva)jLt_+P)iDjJ#CB!d}o_OVasx3h}lR1-923C4va?4ahND=3&Vuqd}MuCB3;gYXM~<z@we466D|oZ89AnpN=guO-hv6Y)vKXpIebS@@RR!Z>y>HYUsPM-Ed;BS<DZzrirzTx3!o=Ps2Y*^KD;S0|OtG?QG<-FehMxgG&>1onVCsIue-ge8vj%{>?WqJY=(jq8)X=Goqdj_n790TH21BjvcQ>Z8ussv?b8%>1st*y8?xA{t%TaMKaBK2rtc~H3{gB1N}e*?}4GU2sY1?9ihNn7HqP?j#cP4%<zFc5sKKEa3~o1Gj*pOG>wZwd=`9hf)(+=NWt27U~EigdpX2e^xD3yPU^~`JE<#UE`JgyNcc(jks{oMABiU*go`^~C;pK9D%UV%hlu9BX!cHmD(WBvEo3rDGG(`tW4Wz<@X-VyUxh^SY24$u2{>{-pAJvgYr%>e*_gD8*%x*GPzbxh{{R_EHW`@jq9HlA<pnE;t@LN`e|lH+69-yHBeNK>{t#w5-L5O>_XShbmoC!Ah|Wgrh{QfMaj`|Gji=0e{2?{vPZuyi?x-_R>O1`IK&i>h4B<~u<)_pEgLDZxYc#yzOW3E<T7}^ST_so1MMwIAU#g&=Kg9jA7>&BQoiYaDKOh_`q$92Y<(By(-!<+RJ1p&$xA@I$8!a&9z%@|9MmF@Ap~6J_@QCIvZ6)+JhC+6|xvuXuZ}ZRirY6*r{rLNIX&rn8&qAls2<tKwyKcMfyK{QuESKMi*Sg~7a|h_{*5$IPbv`H-!u$u&2&t3b?!WhJ`s}%d>Dm4Fo*#_UFmQfc3J0&j0f*ABFU8Hs>n895y!U_iDNtkZh16bs_x$+)h_RVb<g5zO_qZT(U3ldee24N~&<_ZtARi$Fbr#jrYj~YHuJOO}o!otM*14q`L|uYCBexU2<=RQ)#H+ADOk)XSGKny=TWU3yHf?_^XoN&8?v|5!aVR}3PteZI`jWg!w$7icR;#V*Yc*FtIo8rpTs%1^^*V;@GG2DeJ`fb8ol9)YL2akx^>?>kw(^%g77z-b5r^P^FGhdi+*k&GX~NQORHmV8SzZuK`_$I3Cai{9Sv6p&Vgr=VV`ec+SJG2aj8P46_>!k*6%xdCOm8xvW!M)2T18bOaxRRHA)Em-rEY4C?_u!nKe_}nMIcl9qnGv{ZBDaS*$l#R6LBCH<G9c?cgm2GD;%6hXA7aF&j)oFp>#$FNq6b15^4Bk5h8T|l>ZGJK~4ds1u<i}OgWYQ66W<2C+w5I#9zalwQXwr{sneU=}arbK`367TJk1Uyo+DNSn^`%se*wZmU6xnCVstP$<xu@4E9*T9xK>3zn8-Brz{$_tzg@V$92W`y5u|XFd3!{g!f?-XQnfX$IMox@8ns`leNW?r8nvdXy)87kiBFWX^pZfX2sIlPkmn+Abk;I>bMF<)T4msj=^9s_bz4(JsyDBL&sD&CT^Sv@$DoG(Mx3EXk*PVV)f<Wbqb558E-~5w+O{i2v|{m@f$;M=~r3iS{4yJ5WO*?rX#t*Or4`+s*;c*tJqMHUvB&{f&Ia=RTqe39;u5Yg`9>~`Iq~yq>Vie1jb+Z18T)#$NgsS{x@ITg1`Ulpro~`(`vc;>HGTW2mPb3x%(R%7u4BBJnZ0Nt88zXyB{uI(kh{2CQe%|RTqkfD<9x5Kg@GknE77|YIso'),'Libraries/Ń.☾':strd('c%01|ZEqY$`MZC`@FCjSaFOopgou;wgXIK)ph@JW5|VQ|ZPs(n!TRplU8iTNN{Q37s0GqEPE<%s985xiDxg-N3MKTzsDH%2gy)%;-I>|hyR+*eoXXzr%slV!vy{KX-@o$u4{5K5Pd|F?%H`Foy&es6HpzSaQMwuBL4#~0qw7(U(Xc^+AcWuI*ySrU4A;)Ix(oeuv`OMolCU@*jD{H*Y>r21PS)8kwit;r!k_XF`RDvU@b^Byy|54`Q3h}C^4<0Vfgix1C8Ip+^+>xz06icLV*JGb--6h)&ibU+8w>|I5C{Z3<h%T3gX9fzI&Kiw;XC{f{B9@#3ZR-fy;&0uuK<Jbf4&XztPRZEK!J?4({Yy!`XnYS$rxGdHppw2FHoTCK7Z6e8GOWVcP@>FETkcBWMlwB5M;|E3}s6*mPdJ>O7eevk$z9(f#-9^b2D6PcH#fs{b!9mOZNVjZ~vmPr)BS7>}qXaxcC!#9@Krls}&ZHhIup?YMmv~=JoZ6l!}?O$%G7sWTQl<R#0@vKfetU`4^ou@abdzyHHA@?i6SQY(Zg9**NuMZj<2aJM>g`xVLjE3lE=s3Xf0z5|C4bdVqo*kWos4!(ZJ+L-*5KZUAk4$zPc3@Ly=q1;QQVY_nD<4YJ)XEwhHp(yk`P^S0C-f}cZohTfJyZ%f^h#%Q=cMQJrc>U4^giF{Q8OxUna7yN*~&;MP=XbA$is?{g1O@UxUhYc-#W81(82`S6B(mLZ>8+1)r>nxcH3)bfW1R67=mGJ)tiPc{w<3R}(+#<)YFdXFsm&%o+g|z%gj$Sbqlb-mP^jHxzJ~?{WG3l`aHaj7DltpQL(wyV5FyweN-uAm$)eK}BXzQ3*&|ep`w4LC288$Hy)_6&w#d0_51F(L`f6ZSOr~Kg$VE`xKY;{RXyKy{D1;6Pm&c7+2aQds-sA7b12MMgFiWTI3PPS=iW~*`&mM<!06&TELG>+2J_2;ci?6PAAHr$!brk$-$pC<gX@MP`Vz~RSg@ZC?xrj*|0&l)6cka5a7KY%I{%pIJ!ceQgh-Etydsx@tUwW2}UQtC}nfD|-kB2#EW6M=Z+h7364w^dx};IFm_H#5!UDhMBPt2jqZlQ1X%!fgDKDxD`i=Hf`9#4D}R!ev{dKQvOi7^iD`JJyEIS||!qJn={h$*n!*(sO62WtEMs5Z}}gQwUR_03nV?<An8d%f9s*G$m}fURin$OVM}?OY)>7dYpI(W|Jzh@H%pLFV5oO%^QP+5lLHBTXY5CjT369U;nTPU5g2HR~VFsWCiu88H%NIcdMtOgs#|c5yA>WkW#1;fg1)5iG>ZfHdz|w44_nZnwE$b71!*+A1wR_!!73BP-u3=h+_le8CVRzSt09-4ae~ceA`~Ipkep|Vcz3^pXP}b1b$gnNvl)PwymHUaHr)DQ__l&?UNL@!IwA6=ru=%Msmol?9k72hVZ5bNcE=$tWWJkA!7C%xk3hSU%JRezOc|M#0E|a<vaWn=>6W4XJo(XWRiY{KHpDAzhpx!`}>*U{EpO$Y$P(qT&YD^ac%0;>C5QgCS~geq!=}f!GeTZe-;dLmXHeF!r82n`Rj7M2sKan1OA1`z+ojT>Uv8+@d{izLv8xbJGJUpQpug*EF;3np#b6KRTD5{ziAGX(lXsNh;RnXI%aw>(}ZIgyqL);a}_~A)<ANH1zu<blV4e~#G%o*_6NiDiZanjrC*vpy6S0SSN-luS5c5_-D*`fw;y=@eRXP$RS|bp$);eD^`e+G*ac24y6O5z6b*K{XT#QTSBn}2Ay*OtKm%YX0@N6C5S|<hW>~d&D1=vPJ&E#))<rS6<NC0ya7<Osps~>EiXn^H#tlG=vV_LM4=qlCV#TR6d_k;kaziI<t{7Eh2nK(QrflU~nj925NH^yWqO)V<iN!}%s)*q%^ra8@y;4+bSu%(jm9q@_`%EkBdK;aiM7hbyMY*cGc*|H_+D$wMaNws|#u1;n=Fc3iWZ@K!AT|rnbUM^plj!xvqs*8@TGIr)SGa{L4gxEn96Ol$4Z_0sh#!d1XSa(}hxYhm^h^hio!&%vR$F&qc7tvo<>BvUJ!6vWvMvUJ*|$5&Tgi8c2`v|cB16Jnzg`TnTRe(6XzpYrQVgc-CQCE6Zt-J_udJ?tp3*v!_(qiaY-3I%uu`wB^dr~@^w-r);I{~WV3?Q|fT3ORB~(AB_bU1(uE2u8h_3%1!aCEMTUtkot`#As--ZzTQ92y0Gq>9B=p3`dU+@PtQ!}w<O4JHw_xKZ$t>9r_d7P@N+#n*VF4(RLST#Sx7j6brF!3)AfocHlyMXpRfc6!jeN<q@F$JoIST|eVL7L^g#F16Cp{?ut>-udp8wdrz<-f15xwKg%PIQGsqDmB$>GCP8zgU@NEs4u+`afd#NY0T?kwSU`Qb=7XWP_@cRIej_@y1b&ckJ#GE-zvFgCu8Z{X`qDPcU77pnCZG{Gqo7lx4~ef5xBVpDz^kp5w*+Pn7lYNsg#h!D4v96>I8KX(ozX`~f)N4kCQa|4Q-J{o2-Iv-$mgvxyJq`iJlC$~VnsU%t8aMiZW!t+Oq)wcm6W7K;T@$lv8(ijw7}ye6Ua(z16{yu9ii6>ob+#rQgPUN23XAe$2<LqB+><aY;yXeujx>s|}w6NKe3Q<$Lme5c2#+e<2U@EEs7hHb@x9sDGBQaj*edSWELX8=O>_$&T7LKY3eTM*Z=dJEo`HF<C<!++u<3^=m9TH5ors<VuCX4|@3gR`CT=yvE7f{JAErOj>rH~y;l(k2b%1>gaK23iEuIA~R!geg(#WG?-khq6W#^fUeuRrijt`W5O;Yz{@|^_V{vHz}X+fAakXQBO~$2^9PAKJTvLRplAEhTYcLqQenDsHQ<D%)?vHu^KF*1rrhuh4!UoJ4|GG6#u-;xC&kh`>zeHy3(j{ua72_%In>g<*QVU4yF`F;-)6JVr#H&pP^PwoT-Ic@cnb=0x3U5S6zjsZGMg`Tj@i7l%W_qTv`Tz8=U}RNH7K5(FV8y#H8l=eqdh<PQU&uqocIH;BfEO;lqC%?tOf?_u1jzP9Vd~${VYcwi<x$t)RaVv`NrvMZw#4#1m3{#qa2=y&e8Xe&2t!x5NL$-}8n*aq5LP48qcZ+bm%y)TbUeOJ`@_6&A*+ZAQFkxK8Q}CEOV0-CP({t;ugI>jrRxA<OUq<!rf{a`9b(<u?Bfg~TG=ZdWX!gvEfjcJfguScL<7*5R`d@|_N8O`YpX7y_WM(E$Eo4JFkoLN!F43fwaq>_pbXQq}SxYWBn#0V0}nF#^UTtX77vY8cbm3u~4=q~Oo|iPi0w7li#xL6xnv{QPzK!iC<&pW-L5ulIV?_~?}e=;?uScu2FDUULS;7rvm%Tb++-#8QyoVCozVem25q{jCq$8s^Ei8ZkpGZ<Dpf204pEqU_B`cyKZrZJ-O+e@PmK8a~_D2#n{&z+73HiMrJwfPD!Gn1L|VA^*R*mF^+'),'Libraries/peggle2/main.☾':strd('c%0=uYi}IKk>B+zCJKa^S*`+-vg`|Sdpd`box?>BP;_*_ay=L=hvZ1RGn?6=xH?-x{1DIZE3z%gK3i5K7={#Eu;Vl0$cB6YJUIW0`w;$;t4H@t_e{@nDbaF*+r-@2>FVn0s_Lrh?&_A4y_~&z;^Z$K&%>vGIeOyw!lLIn_W!(OH?7rPeA@2~9k*%OwhMm=`uGXQb=&)AI(wYD+G#LKy_GoW`{^WTR=R$7EwJWVmece5r<eUXi@&XGGy8as{<`j-G&w)F$AVATAH+#&CBbSiviu=D><LEQV31nbt?Z5L{SuS_afWO0hDS|#seihsHpmrU2hv{5-pbyDCSS`w%3gHf=R4W&9DWOw3+S+Eohx8o&aPxPv$q)Pn&Ud>T&vNrvQLW&qo#F!4w2u^e(%`(hRuD$rIi1(t$mgQ2myqNXpcGo?a~KWd@H-0-BC#$0isLU+YVF+T1Sr`7VT2?_p%pS$Koh(fr`b}VzM46Sl;ju4HfU%vmC5oh2LdgIKx)<0@VD-WxlbvEK!A7xgvjB;gB#eD1Kz8PNsg6hS92(hW#M1-5fw|93EcJ?mGzL77$60t|!qR72Cd{mB#T|Yu}I=G;C^ht^JZ9fyU6oe-;&3yIkt=YU203ZXBHpk`x7ZHG4a|FZ%67en0S%pzjZcM5`1h!F`;)hm8Ip`^2$>Uf+wC)@P@ue~ynnKl;OAxEgugUc|pwlX!jLg;5kF$_pDu!PYBxwqCitwRsu;zH-}kWiJ*NHKh~;&RNcCkosww<TL}46j3#tN>O{dBT8KqoVljeYFYMQuUxjRpf?N({08WNNKPiecd?AEN|Mz8UHeP+O;I%Lh26lJX|mV=ZgJ7wt|8!@XsU#bYv=3?hFyQ4jdK_@Y0LiKZ|pg%+-3Pa!rlghp5KL@JF`{;+PnM#*s;{rO2k_+cC@0j$#swrq6Bp>36|Hpfp?~?cdWj`lICSi%W+_I{+=`u3;*?qGwlK+u_P|NouRh?ezR0C+aVp9FTG}-A7GwK&P&UD_{guE85fb}<bgEi3u47M{W{xpo&vibxGJ3FVyubl&$eEjM?Bjx8%F>%4V|UGH~G218uaS$e!e*#?;XUew{cUxnW~nF_FduxK1@KuwJ&!_0zEgzG%mV7ITx;d`yeD#IWmqYB8$tezhk=-3Fp!TLf=*tWj5%Fmk+Mf{<3LY)tiwpvZOih#{GT}rEH`(`0JGI8i_}js$zGXC{F9z@S|l5LWEZp14X=<;i5VNq+sdVF56Bv!i&IpV^vcX(M#KL$;;fCYnkOiUCJ5Rje9+CfPv@7+c31&RV>!<P6Cd#dh!+aqxhw?MK)|kmXSSk6-W^f-OJv}10wkOKEweoc=Fs^h?+%!R``PvGm)e#-#H_+pek=h*r-%?1DT2*2t|-VFR7mFC5uMFIEDSS;)Ena52g34{OkZBTBQCDOB_0&aA;QNR$=BJ12g|vXHT7+a-|sf3G^Cb9p{+IX*pBJNac=!&uCikW0suB7zY;Zz=74fB}WrFMtdI=LdRJ8n(GK#0)X?+EI1Hn0J`TcP@sP$`;xxD&0a!({o%V?H^2HGWkIy}W{i~gW~-#vQwVb)D@K7kjou6fKV)tjz1h+T0bPql2&ETLH<?>#AmeRf{-h;UFbPnN<NhG*VMH<&<x!FRp!#grSX7D9EsoQjWW5(qm|SPYCa`WvA1DLMjU#C#O&~VTL+n8ktb`-B#l!U#c(%2{N(8DSmV!&3EICsnlA*+D57Wf1RHo=Rufma{gH?-&bpH%SMJg(FihxtR&njpYh<1rS7#ofDdD4mVs1qX;yXrpV_j%QnqSlciKq`7Lp>`d!&6186$EkOQs;`96^0x3|-V*$#C;fUM++q&ImXiw9J_EyO=#OZmiu%~Yv(4O&U|*@CZaTPZ0u55l?ig(<X^`42m13rMVvZ_t0@!L+NU+$&?C*^3=tsiCtNO=a&3p!+G+#hKd2VK_0662BSpW0)(A7K^z=^=9Jlk@sEhVVIdRvUu_H397X~+eSP=_(nfY5O3`n&LA%Bn)C=4WhJCVgUk_@rAcO_!7zr(5+Cq=ibba8`L<Tr65)e;TGi-!b{nnL2-Z0IdH3w*JCeQj5IWLej-`ir2GmoB4v%5SL9n1Z(kRY&kf+zS?3JFBT?pKU>5vA7)==uR4-Dgwxg3{J9J8b6U7zTD~&6GjK?Mn$)2=v|jW_1aCV`Y(W5Y23KWfP_{*%<Z=<mD#d$ONM~aW+!L=u{m~Fu<Vr#Spdy19b#(ts9$s9j>(%X@xM^J9LR>&C>axDT#S}?C0hmFt#L6AE+mWQ*GLhC`Vcj=Q$Y*vkAtya4QTc0Ov+re}IkYbEU-?qfi`i${J9Bc0k$(b4v=6S}FIoZ1E=38&f*k+PlK-b=Io3QuzEBC^6uLUFQ1`O`27vq7U9ewQUId%6vf8qzSEhxj!kP%(5&Zv?^^caW(fJzBd)Y^M6>f~+rz~aN=+~t-Q3Pn$4z6H(%W;~7eZl>v^~6Ed9`Wko7rDoKlj(9x3UVu7HLFB#j2D<m(}6OfO={u&>}y(z5~QnLC3^**jv*jZbPQ-zEEZ~;^3y>}PF#Y9cEg0pPfegWF<oTKgktOxS+weqOQak$<IJtEMix1bK_B{l+Fi5V!VnW#56^em7C3KvIPfEA!ln68|NoUNa0RF8pB3WRNQx14o8l`Te7tl#T@dF~risG3=R;{y`;H%WH7Khw{F9mzb(*;)pw{Gs7JqzFN7WnIdpo5{sH?y$0x3pSB@;gtml%xFfTH}iFf~Htf=$98eByRoBfiO1C;B05i~O8U0{`q7z1C#G-=B0ezccH0q=??guJ5AaXoN&6gK{M3hz!db3f@^4*D_3^N0~FtW`X~xV|#lMVGqdXsou<BPIuOoAIg=P`%<=GcghwlV!u6s{hBU?PY-N$DE|2SvpM{0cPviy<JlSH{-d`tER<ca1nTgiMZ8DO$REH??!J|Iqy|$rG7TFS^6e>`dIfK*GYZYR7_3K^n5fvKiI#V}Y|18Nk+4G##T%WhiqXTMyo-52lUTc5kNXM(sz-Z&TS3}(R*Oh^V0%?vMVZuEZ5O*#HC_zhu50~Mc^$8=YdbM@U9I!He!u$z+dQ;(PWz7%u;r`jpqBn%z-p<EEnMMpYs?mI{*RsAZ7-=GZsxgJzb-S=QHHJ2oIXH|!-&gccA^=2JFos@Ok%bb6*pfDtD>{JD!F{kY>aFkP%hJ&T&gmuk;n9-l836ehfI6E4`=|H(A`~eQfd9}?n4n<IE>vldnIe|*^P&y^bt|{;kyPZMUIn@<*tq6AFvzO$8<w@Is2DkYWa~xJA}Ksrn&pQl!-7D6Y}m|-#;7B*45BS@_o6@>|-roSKVa!L%v%_Z<`{Eokl)xXna)^Aowloc~MX9dQhp{k&pTV5vAV9F3mr=SR^GUG7$mF{*wI%Q0F%DefvB+TJS1S_(o|YuVD&%Gf$fN)YX!sFl9#TTa&-vp0j8>c*;^c#~pgx<&+5^Y=TK1&jL2h`PO;Y80soPi9`fhB$8o1p)^J%_2&;Ffj-Y+g12vFH*(?O2Svg0Xu=!IwB?-et~uvYm{aB)glTHqLy2%;&>3^`8x^$^ebbQ@fv~akZ<Hpr%tg`vHjjmS_$nb6M->}MWm|uo>(e$xu9l-ffnJ?xUoCCjCz3nWh)a;m9ZG2XL-L&yMDz%NFe#Y>V~{avMg%hb;ICIMmv@3R6f*U^!Y)aqTg`R?)%rNQ;;6<58KPPrwPaH%QOBB~{^91)I_ihOlyj4MD+J`&i(V4Pcwk4%(Z_*^)(6MiT@WfixJ@e`X1a-~aA<7OrAQEwEmjg#a@gFq(l-qr%!0TF7EiOI(tMI#z>_&QvMWs-XxFnZTGXL?*?m{BnlBqN1Fuo`sK^Wyd*!@A>$<u%+Qz&IEiz>62{t({*nMEHk|N@zv6m)6Ad(7%F@KXo5e|1j`goR!PBFEFe@*-l>aO@<FIeW2Kf+5TL05HB4U+e3bK5i~z)E=4A1299ngn4!kT6;PgIpUE!@h3sey%)}WkSH#Z|`rt@-qCjtMnIZX%86n=NTT~7<)K7X%AIKYiF&Bz!19f6qQ?P%)+!#l0OmMs^665<0EZleuN2o<iO_5t|C^w1n85PYbB-44swGNi$#8_%M?Yn4ND~HAZu&n*@&zC)l)Qd`1w3FtZoig!Y}2?3EK3GUI%~H2OkQT=Gk;m9=9Ab#oC#~Oq2lMo@?L+RAcHQI@b&1mH1Mj#C7QqdNs}Uf5Z6@;#8V5?V9xFPAx9AgE_vA3CZSoVW_BbL?t}Tn8s8+M;dL!G7{`2jUMG88Ixwf$Z-eE6=7amhuT#wd6AOFa!7)Hd@kT@Wz3%RFxRLodp7RfwRj+GZJzU(i6j(81Ev0OEf}_VPA^`v5%7Mq9t_hkj!LDyI6mvI1^%*pA4c8Y`f}h6;$f)51McowuNOqC>6&<T_{cAwdAgKp_@W%OyyEf&GK}EFtmGw#^zTZ`KZyCLBq{A}(pyfWKV)B!sl-I4gj#xLdU|?gdgk<Fm`ken8fFtVOQI+$dUruPNrz{Py`hpmI_a68=S12!43Z0VD?*0DD5-iF#RO1yT17b-qk=E0;1eAHA`03va~WMw`NYTLO3-&u3jo<?mEj*#U=HZ;GbZ@@0JC&T;|cI&PpE5s<rxSL&aOBH!v|a|PC*fIw;GhI2Z_WfUshZ>R;&8Kumt4T3pqexJ}cu!bGuiwOHOsZpUWw1P0tz9R%_)y(BvPAY3vKxry?~NJ;@~JtX$=-Qwn8m#$(S};RTwY>oM(BOp&A|iE50^lfNmk1OWpxbd86Mb};8CmP8eKI25)lqg7&)BOA`sy+JUl;bJ31!IL_*r^SceJ*-wf=vQx2goQI<(PqtNYpxyVD<L;64wsIM=%&Injx;*9HFTOCYd2QHUK%8%C(W8R-JRKr@ym)2-#e4|{#JWjrqy7|bk!~yG15C*83@Bc&#&BTKpdDih5Tb|uwm$Q>&Fa!B-p$<SLnJGxNaP!VWdch=sSn>G5Ou<tRftS(J=KRm_ePB>!sU}kZ%*6D=#)HUF#O37(<yVMguH`v^T#ptanSc_7GpUeuLOZrhM5GI##J&zv(;{U)O}sjB7gyPCkt0cVU1S217}`wb5`A%e27&-SN_qaX5^>UE=#n{$CHZ)0W8PXPoPipD2!cao6uzy>YrVxp$JEe1;-8-qYjLBHya!NODtjYP$t2^)o@(MiN1mlm@=RjOEM?w8ejUYfZ%j)Q4v|rknw+I;Jy%eiFsYXf(Gupqy2YBJXUEJ*W@&DpIE-%0l7;5%3#;ZfZdL^WFGe@w~e@{V@Rq8V7njmHGRc#}vbEQYR`ckQfXGi&n8wnoWC}OEnJ<ulyv5H-@_$@M?X62?=#8h}Qc-;-^8KiQ9RYV08a=Znm<&q-pB5)2tk)dI&aG!ZGR^D$m_qiymU*X1BK874g?Al}Sf*Um2tp0~FI=WhQ1k1-X;SEp03Srk$;cgwbF<Emu=!h|SXBK%?;(V+@SOV~jD-?fpRz#z8$hAipL<+qyyjq7D~*mO9FJR;n8m@>aJ-n?M`Rs1*CkE8^rH7relQWp%9+5O=f%OGZ`bf$>_jL9n{o3uZkCRC>-rlLl!JrA<1%+_L+A7}?r#VUt!f#WG@}K}&^qD#w*IH0*G@MsJ%;>S_zzQlA#k(D243R9R>zB99o~nA=+CoBt+jZYRs3hM}k&z2@WJVBU~2W{EuPO$c3mjGjPndkkXb(7V2q$N1$w-n8VthJBu|z}qQ)UAJ|V$Dk~XR`X3YWY;Ba<B=8r>YQ;UyesvK{uWBbX)$jVNeEJ}1<lk9trH>EJavYHN!}optiTpqN{gt$qW+#e-JU-j%7Gvh+4F|II30SPh*0Sk2+9HC>mL?ubrs6<!YE8V&*2Sq2;oYpCY<cCDt4p)vz+O%img1gaQvwE^um)zomJN~^Wr=O#cC2cTJ%)`S<qHEa(|7x7qYVY62Ln;y@D(9#vyp4WJ9fTisYj<#0uM!V36c&ubNeR->|)JXf5#7CHwF~f~4>F!ha8zJ9LOWcTFNKOES>*Ji5(=_H=~rQFhQs#*&3qhzjHa2SvhG>6(L<5{&Fn(VkJYCuHR7C{WSGiGpaYX@ObCt54%-r5AQnZO2Df&b2%hrlg!}>T&8drQd~)O7vo|T!j%>nuyhr4o_!;^MZ?dm9?TwX-n*bW0d0PeWT@6`2!Kpi)Xx<l$!gAyt_a`H4RxmnkG0x|7+<78?{!FCs3t`AWx>yT&OgNx+Dmsa@iu?!LYC%Mc9uMM2|IVZG`EXm97O40w5RiKF*agEXxyON&g@TBfgMB6Q$sS78RJ)xzsV$c4Nns8^ns1ssmMCq&u;;U@Xn*qTR3S6qi-Zk%%!qYD)H<*Tx(Z6y>I%o+`cqc+z2Ad*yF_*YBvQT+x9^Pv>)wATHn#H}>iok8QiXv>u$Eef+1L_OnY-2XAY%+gqPs+WLHR>)MxF*S_7_{Bs9i?seMF?%lflLFak+^E0=x7hdkQ;iav-wD(dL!PoG5>$l%11@Mb7KU+dwY~4EUA>8Ht?8eXL=*G0I>+eoATHoE}TWv4?l*t6#OZHxCDP4*X`_%K8;D?9{M2v-ST>S1X(cW%M9ij)P4OKhOx0m39^_L=dDt`~%FO?`OCi=~1$V>32#||HT(pz}uS4U22t4+_@5L$yWL6kbQ=d8B4fYPxK!QZy+owCWf(bbqmAz!Hp#p32jY`x9*ZpEU4Qon;)Z1R#xYUH9VcK)woUINa9sAkc=K;|Rja^oe+#CA4aB3LOd@Guelqteb9Q#-Pg+qHYU(k^jB{NBK()rJZ}&Im#TFAGW-*e1?+Dr7-26I>!mVe3pq3Yy%iZAq&1mPB4hN2{z{EY?w9bbFC_!6`NTjC;)d#20G`ZiqYWsE-Olt#whMp82hMk;fWpByDG?=ju_PVbt77b<BvWj=8FG9X2;Cz+Ji+&sK{OX+tQXqNcH}YSt;KOTgio^01oih?3cI$pKk%pj`5pEYbCn(C4z8EglarADERTTnDL0s84~e=#Vlz@L@_TR1iJhsrFfA?}kuap--l!rc4c=5)CU&J<%}^-AYp%<<9;Cb@o*G_0Kz<3ut|Ras2q=$;E{yPta6Sgi@MGMyPz^Q@ZLtkG<5J+jEq3^_^nEIp?4MIf5q-ANG#?8~&37Cm|G5{t*Jl7D(-4Y9n&A(qNc+vPrp~A*r&LBCGPjwGsSoS%qIab;xpnoaDUr&TW|LGaS};OvU*5{tnEpy141lD)23VBekuKWZ6>Rb(SC+RU56t=?wfZ8P_NQole%*<{<nAK=9Jgn2OxlIAlRwU@h4#Xmu=}bAE3<z}Apn&`%47k2|GPYPpu%u#9*B+F~AGgs5UKL^qwOy%49EV6lY)w!MF8X`?e$2P?h>thEFYM;+{`D(n)3A$8z#8D#$WvBe|D7Hid~EhIbBF?Kxe2h4taA}-c}#V`#>0JfF?s0D8?ulpNo%b~v!c1Er9;~O@WOhyRiR$jY>E%}3R9FNcj5QAu)QM|<QE<!a7pcT7uR82fDE)fNI$?c|vDD_o2!}{|HFc<#^5PK*2'),'Libraries/peggle2/rgx_golfatron.☾':strd('c$~dg-)q}e6n^(#aSH?8n<yiSVK9T&CU#8By4iI+7}%b1Z8`R4OF>dWX5E8BJ6N~TX4y*F*xD@YVbJwq&@oD35BDG2IY(DNtx|`w2^2~9$N9edo$sC-^YL&noS3XsW_&i7-y97}EO;{crTnc#e}yQF9ed8kx2&OO+cTF<=f}3=F`8T8@{YXMJUrlB>ssCJCvUxd`|8Ff7oFbcUuZhhy4~KECWOv7A5IK}q6zQs^KH@D?qSDpvXf~ydN>0cs{7ZuA+V*u58F7*FpT26#dk!3S8BwZSEyZ{$W!@{3ogHw7xIL|_nExU<r2P@guTfCi2|R<ALLVB`KZOi<(|lA@=On&-<4P=YPchRmVe1V5PVa03t$Hq+t^T%Kq6jOWa|G18HjREz5oFP#CaXFhGN!OkJ%e?suQP65eyv!93II((}*SZL8Gd;0@yi>SeE58!9#pC+Sl2l6qE4*gm)@!oz>xPw0nUAl~b|?tY@1IYHnnkcXDm{-_frDeYhL7kbW(nezsZB&o<}M&u1Mi3ep)&p%sSw>g`UPcbX!i*f<b&y%y&D4BB1On|kJ)hh%obvG8sr-nWwki$Jj06IdQ17w4(@R6u7&Nkw3R_Nwk49^l+cg0u!Tsh6-GPjz;nQ%{fYX+kAo?|N<$_F8MzuzWzi3MeALW<Fr^O#rX10^W`QZ{#m<cP+re$Q(20$nQG?%LOBs3Jk7@hM%_6_wtE6<#9~FfwcZ8e@&c8%r7z98F3$p;01&HG?fGmsHtG|0Mx-z9mq3&jcrF6l1;6^NK3$a5gAFlqKSww&7Tm;QvL&_EUI@zPl#yLk?9RQ&*2Unc7x+%(;7h-^4xUHCcqhdI00qovD0H^s=>d=yOrHGFX}V|t7MUxGuKoUQCmWAOz)OsMIdk>pCVGq>^?f3Z7{y*Yyr-dGV}2TRna_5!))N0K&svrg~B!YKz<`%^5EzfQM!)o*?8bNwuK2el^37`5x5o{^Z1HGq4Oo23@Mqye3GUZ{ik?yp386LLzI=A<>fj{-j~nUu~rDEG>H!|b)XS6MT-Rjb;vdu$+)kFOW{-;i0JQJC3}$$;LfH)lN&nw(6-Fr2-BH?`K9W4frdI@18aoYdnBLp0}&(>oLPvadmz8Myl_b-Gt+_qm|!E&)6La$ei<<%67%HFRGv@l%a}#vMOr&}>{EMcfxW_ZKV!Q_TW#9;I-3?R5H?uatDszwkTJOl=gCbNHoB{XD0jjCD6YUQX#@#_;=UPIFBkXaUQ1-1H%}z>uKYVcsXk>0-1zuarhk%qY(vNSItO<INL3DTL{dPCkCu#)(0^fOp-m_9A}eK3^+N5S>c_I<tVHFDksb%;4+N!A>^)|r<HoV^M1x`oce9lV7pdo@&k3ajPD72Hb)BRV=D@@oitBm66-iUd9d$ra)l;Pa>w>BXF8tInN2*(ApP7qtycPJCS~Diwr^6|)YG<Ehn#j~)=-L42tQ74^ZKaH_v@~j>(C?!JyVYuc|Knz()jsU^`O(b22|+nZrlpEJ{4z^@3-K?+IuM8'),'Libraries/Compiler/op_table.☾':strd('c$~FZTTdHD6n^)wm_9_ao4S>4XaY!n;1(6dfMt_Z6<8}@7KGvp@-7vT`Vc4~p=lbD06_|uI0-0C32GXHB9bN&(`WJ<*vCHQC-lth?0D8*gSo_#?XxrIeCIM}&Y4+-Op{-u@$VH)qf}3Cv_CeWX$m&=2~!&`6mv-v`_V|YkV<9^MfD?$RrqCM{ZU0#2fqm>d`dl-5k0RLlcuf}#^`^cXf%XYB8%|-!2UN-TNn+VAJI(#qM6B5R#ysR1_%$5De{=SRPeV$<Do#H^`N|q)kH$|DalMmOX=W*P9c<RGMCCE(U>3Q+YrDdO|w{~3Je;}8+y^is?yuvMctYwt7INboFvQSbr=Q~$XoJWtr6ttV9XYI*hc^7$&L*&3HCh(h!R;MlVQckj;3{`uaMXMi2i~P0Tlq5Bs`4KkmOZW^>Gsx$RFe%Az$%IRq$6>3V=0tqqBWLMB$*k1%YS;<)D1G3TL3b)4^#J#Cq|j3Z%VBU<_Re1Omf>Ky$iLG%Ai++?UATN>y|RZ332y+LxgGv-7r&i+Z3{P)R|htl0(epbIK3s0?l>;Gn14%h2h(47u=LEuRAI)v_CFMb3p2z^zof8mwoWy&cx&Eek96k?c|(D`bbP()^wzcj?~(xe4$HJ~kZ9H-`pWk%Ju!@j=F#m(!Bc*4paPLT)YA+6t0l@<E;hXfG8YB1=@%&>*;kE2@C7Hg9s;t)@L_dqV#O?`p}RkMx4F&&+v4hd8t(Ypu@;S~l2|cjm#d%y{+0+l(d--6ZoqJro+V9xxBNIIRp~gcE$@Kcl4(59Kj!5-bm4lPbLfG{10PG~SUd?!W#twg1olyZw2r`h4kZ(l8LT5+=T*kU8=jc~6t>K3RnRqN;5^st_7gQ6DR6n%o&6ckh$cHiXX^=M0R_Aw}vEFaxHT*lt%VWSf*I>|3%`%hiij_VF=Y8GRUO+Gu{%gpTO&oM*%xAZ%)Z8%944o-q#nj&(^#9NJQ?V2zxx!_ZAo4njPbvOT~&YU(-3qzTCcWr7CgYIjtbP%8>Xhv_OTk~hkPAN3AM{Pa`Q&GBL$O}N=SgM;*}p|j@atCIHeU6=}<Ot_pdYMt<->u2MKIMdkB&M^fBs0)=R;UIm!+^qziIiR7hOPro1m({~1YSMK(Ds12vRjFXmrGX!#N>P)fDCAaZKXi3Rlx8?nH76R0vLQ#AM$y?QT(7-XBtF3~;$|4BF!<;)rBgJ7zmshqXJ{{oZO8>Qnn(5&WHTb0(z=P@Ge$Z1v6BVgj<YMOM;{vSS;U?CdyTr<fIhDXumBBSOUOZpV7F`Y<S)g`R@uH_JzJZ=)}~rpk2)_kYHREZ*;=g?L(j$aHJ>t7W*$HjJCl5<wR>jn%h`QKM)Sg9n{4mvT=E*d*YV3(^?k^FAoN2Oa9S_l@$`sT-JL7-fl95i`Y=UqkXu#os(0=!y2`Zo)q&r$1_KG+$alycr;+n1`+^qax3dK8<cd4uTp9DhD{vtQTqsd%BbB>LUL5OMXuCzhYtAxYh{D9D+?IfI!pKt9R4^eM8dT|sFqDSg^rIXv%%Ira8kONfA;SQ9s@d*HHGHdLsMPtvLdeB*VeC3>{?P02{%cH?<V4T2tAgrQ=UUs6w6>;1!)eb9gVnv^oF7HPRobb=ZrzU2)P+R_WN=4ZoJkx@{3v!Jq-YHi-+i<tp19O`lnpu2g*5sZiBQS=?1&tttoO*~;af7|XQ=^!5!oTOx5swOxees|%)N_p4R4@GnjO@6+DVy33upwkvfUBACSrWCB6U+ui5-R>tA`$w(PMSdc{#gB7X3BH9{29DGYS|{zF<-&@H&~#Af8`1+JPk_7!*HGyK(5pVXI+hy#>QXAC7sZdbs|WTYvm4^hdn)%h?U7*x**@RfwIK>lC9pxuW`=-3vpW3BoEs{fw}CG*{`_X?Qn*f?M@=<nR*cnN6oJA&r+0JN(BeAN*`kIp_Oep|pYaj!3t?uLRPuj|}v>-xJsRqpo{8y+b`9@7rp#jL*RO=q%6rF^i|iJly0_IE?V;l}ESXJBwMW<GnI=vfmrDa&={|BKo^}F7<TB;=C!^Z_3uzt=V1vLS*9^CB7TBX5SrbFaNjvWUp+kJ?F2K=3iJFPe0GC-ls1gX*@s?M`God#xc?}5SDY=k6;k=Y7wn3Ec8RmXGa<__oI6*Sec8t<bp1_m`g5b%Ux}cY4K=xXBb=MH&(f9EkCrDA6bi~gSid<Iw#fAVpG8uz17-$PPYEtcCHF7E!Om{Pt%`nh=GithOOJH{2_h8xd^2%W(1{+*_5Etf)aceDtyC2HXz1YG5Q)ghdg&zzZ7fl)H?h7uEO&El+2Fn24?%MBXU{0{6kkfjEBbcKp+XFFFw%4hpd^G*4C6YvuoX2=Me~|nz1d_8R>H*?T`e5EqfoWw@Z5^3UVbHuDn3{Q>7yv&d3uwqN@J`QZmZ('),'Libraries/Compiler/generate_operators.☾':strd('c$}SB>24EO6#k#57$RBsUNC4p&W>CONN5qzL=Yq-<BrCjvE|B3<S~#GQIV8Qp-3SlQA$W4LRo++EzlxLS$^Dqtwf)peu6$i&s}G{Ob~>GIdj*ueCNC84jvt|j~+WQVhp7W`YX0=w^+07xPht@Ud^djYd#{R3)8D~cI@<5(9fh}C&xxljoUUx6JDWE@+=fL3Z-h+DfyVdT$mC!_>|ExOh|fvBGc8CD>=Sz&~<tn{@#fv77sGiWx&tZ)r!}Jt2NhW+931X8PhcL{kcR=ORknYE#;MD=^0i+OO}?BTI$hKua^3>)UTxhEe&eP(Nb1RT0cwcXKDQ`tzS~FoYa~owWdiAfunP!8n>R#&=vXwgA>kMra9;(vqH%C_X{D{*C&K*uN3-ndD$}P$}#4E5X^k95E7moY`JosWKNFh$qou(pjWQb*DnRn@r2+GsFnM2a<3lQl2=>gyrk@MEg?8=LXL4{i^)Odo-dcDY!&ZICSc|fou#ii1c<TUNL+?d<zl5+s5xcnl?}RyF}+SV*gGyc<*e(l_8oe6$S8Pqr(UmN@eW9=BVrWuy1lI*d=CGQ!zi!hdoAn5#dChhpwsj{=moE@=shuep78EhbcgRCW*8~JZDV^CiRB;#7U)m(4>g0dD^O<&1j~zE!8$@%4$1Vw-DRg(Nx{M?j2kzvqy%QnM79St9&Dn<!<W$4)VPI6<K}j_Y5E#!88m$z!I<w+`WsjTroa$r%OJA18+PyNa=pAU;naN3R%Br3izN@|s+GD|srxc*@dOLSnJ>@UM^23#8Xv(J9R@<c^dbG3&a=LBhIx4}G_n+juFeBO{h${T&n@<B3A2O=xObJlq#N3Ct;0l2_CQPw02~XB$=QjmJQk(m$<bj90a>Qc+qUJ;v|lRbJj{o&B%O~lQd_3eDR^C^w+JR_Gb2nP8A3wlNch6z1qaU?pgyHg>t4dPE&O@5N*3n3(;om(PgMg1mItlC63?r(Wf7pAo5rBKMi)3Z@6%@~XjlZazacz3RceHm^QX#Lzf)4ebB$g*a%ddOg%`o1tAW>;uOAV16x>j$5@}ztB0TduoE_-Hvk!m%GxOmsKW;3RM{^L+d3@x|DH%aHXQm+muSVr{y160K>>$5b;H1MezD*Z&d#+l}R=KH)n{=1!`MIzUCR@4V)6ztxLFB-8)GWZiZ3UP60nx-c)5Q_lC9T-(xAb`npIwq{CY0)o)&PB%5m&7<q&qEtxpjGwGLa?+N%Vw1)EvC4PM45IKb|B3ajQ@>!sYQy%dCKMM&OwX#R7YXs56NLIiseo(<S<ggb8!`nx;qC^IQe#J!A#Nb6}4CNLPXkU`5apk!wXjA2@}(>kE!{+`RGZ*zpl;GTz|{&$>2Rx)K>xlnsxZzzM=yT1}XcveLOa;mcJPAQE>XXpviV3wUZqTVw|5EW9!+M~L*_pvzd&>>AzDvjnjU9P~h_J~9Msz%sccv2g$Eu}Olp>sTy!<$*|uc{_9NS}={dEc!gqJoz|GXS|bOpkdCPjN3S*Imm)dC*#J{kTE6jn1*x7iW^BV3QW&PI%^uqmwGP=?M7sw(o}KW4QLwco=M&axg#iPCkRnO4!=tjbOmBWz@~WmNPuX!tb}lk!3r}VP=%i6iXU2AQ-U?g`vSZnzdlvsb(v~W49a1xcV4ASA-pkFeN|jZ)LUu|kP{)<3}-?TG9f84q2|@k*D406BWfQg)`H5X?qs3#;pLDEt&rVr)&8~$W!X`<_IRomDpv9x4pjgPM*se{gCzGY(3b%-GcuO-CyaR~D>O4<bsR0P3!c*xo&;<E^<vlYW?qjEc7SPrukSi7VRqInWXvL63LCTCczjRS(`*t72w#!d0o0}nBAwJYpjMKZWb9*lyhiZEdUCSAqbh-?0v`lsX+@oi8`5r1O1;3PwP|Y-F#a;V!jUa0ZHC@~eTk%X96p3a$_1$DKstJBsBMB9QRfU3IA`@u^hG6#sG5m%e?qfkPlhiUy{0%w_sNF1!7;98Co+N;R5?h(siYVts+|6Kr{E){D<dXW-pU{-o?_9L*(gKCyHyrfSPFY~9?oSr#3!n7p@B0x9}bJmUQRtMwCbJ~&UZyj9WC4i3T+7ZoWP=(&n{`x*AAaJ9`pZOU7T$^c-bBEyWz&hy0(xJGlVZ6g$k@DOv#*UY~IPiAI#dEhhILCeRhz=a3)UTdV4lax9=V?cEe<vD6ROqyBv|gx^PN%v(l_Fx6+M>yjUgF)rpw_$$lI0s$b2KMjSjC^Lby)z`8FUIQJ=itM}_%81k$7+zJZi0WTCHZ!gLxRtw-Y3T1}O3K+>&0m6FKcB?tR9dZgrpPsjoIBF`2n(H!47gbH?cDSnIzK63ks!4?h_US}xtXPQ~-^GoKapMA<dKbA*FMu;n7Yjo%|6C>J^Po)vwjcmY>i~eMrb>f-8d9}G*!fbDA1wK8Z<)SeUrE}(QNSAFQ{|!IVSD5(`&@b2wsGhqB}T9Z>@Bp%D3T`Fx6P<NIkUA);8R)~3Hcw;bE0<'),'Libraries/Compiler/gram.data.☾':strd('c$~c&U2_!2@vmGIt8Pb!T#}Gb1hsX5At{%^s3aUaxjnY_PAj3(-Rit|GEj(=VqqDRpt|!Vh5{)^EG(0h;K3h&c?eZ<m0$D5`|U5#Pe}Ll%<SyPN#Z3c0X;K4-97y^J-yiW&o_U*ed^2^`|L-P7p5*w+qN-RSu8n~y1|ZQjO_2GPMyyl$z(0h@)m1$@S<&3ybS)BnLh<9KlNXjw9j8SW1q9%?+;d9hDg^^k^T@t^3y0y#VGk{l%_OFmH9>{hH~!Ri?qDA+1j$}HMbnW`2DFVdwTNhJA{J^^~Q|7aAig!OkX@>zxUypX+kJf7VL7x(-BUed(VF7-1{05QbEKRQix!A)2B@<Yke>@G&DOjKI{VQO;74m4xc)!Pn9gL`l>VU0ogg<soMSL`*DiHV!qy}HtLz+*5l0H=2y?eT6wWrg*791_{^v`e7@{CjrmVpSekJepFkwnYj7BaetX%nJdl?S2rBimUqdR!e^&vVuQhN0@KVhrRednopTiA6fzOxZ{ArpeK2m@<56dIjfhYpv40r#{0ilKA(x{a^VP#p4u+fgF>dUS(!|_1pHdv6uPJPZ3R9b)8+iX5V9ukI)aA5GOTPqv~RD(;wS_^&=QIRz>!R@c@8E_n~C9r;N_Nq9^j0RU5NQ~s-WKHg9y5zW?MZ08-kXaOC=b^w*2yK#Yqn$Pde^`bn>ST6b^`ycg{EnkjDMgr>UScW1dtxL7Z)Flc2MF0xLV{NarSn*gaJv1ql@({c;ydV)WV}_HROdt;Z}Fi>4QfT1U^O<EP>u8_VN97Ez%QE-8-{XA2N9krvqjA6?SmLg-x7>vKB1uIo=uw3WJnM)QNJi?BoYXlVNlmpF6=7=fBr1!Y!~}@mH@m>_|sI0gb~VG(D}C5hf&mg6*Ef#jM8JPj#dP;Xh2V&K6u~sSsuBoF`mZZcrsKdtgppAY5R-A5eT+#6N%>Y7>VmhfZPtLG@sk^4YwNg^CQw-brd#`j>PgkWVj(EAP!`E7%hBadrnns5@Wv_=Cr@P*xUU3r^0dc9cGUJdH4)6bc$P=@)+bqZRv6vRUfH_>+MwE?m>iGh>Tzoib_i=tTj!y))jg({V9zbaa^R*y}LojV*`wHUDr4p3s-DV*q0PqTl=UXMw)2>*5-GJ7Mi5%&qGk2UCEOof0$w-s4PdU40UA*E#7V7wWy^S#kC#b+CDtj_WoSkF|KWKK%tsc$=X639VbF(UD2sm=F6^jI}2nDi&N@<w?BiqOz3}A#=<KV6mn@zc{tTC@gNEPKVBkHRR=#fKVPja`n21<s=%eWtM*k%qT*CbbrD)bYpGgteH-w#VT5W}pvn=WsMuT)sgH|_BXG}soIZ|*#g&>sx87WFKMv2%$*(I$>%7F<-N6&smu)yJSOIdw?oOzth<PJ~G)3|gXolrn4~(j~Jc1ziUmC}g_`^q9PT68IQSkGAnm~RQLAE?H6p)AF<jUpw`hx4%O@r4efc&9-PP@5z-56fne0_>3BPM=iyhN$!YU5-?8OL-=d@BMdpJ^ay2#eHwx9&F76Q;1YdH*|c#`46hgq&do9aYeng2ojzp`en2W)!68m4=I0ryp=wA)>eFSDi|-a{K152_J2(=A$@k+kkUOKFT?%NFv`N2AMaZ%Hl@W_eywlM3gR}5g9icx~lG`2e_!*D;@O!Cza?>67qC-m`r|r|4fb|*BpPYZqIWY83vAEU}_AxI)OwoN@23rfDLp40U8Npb)Dd=Q?Sc3mY2L;oj0C~Q`(2AF58>)b_H+FgsNUEJ0Ppk?8(r$TPf+73M9)DsXyu3kN=64prM&zdXnPvQuu-|;xjl>*2bOz(jU_t6<_Xl176kg6>WR^paG)w+L=hV!IKx##X?7j#u&Y3Qi;Ws4e#-A=SEvT+`00#tCHt9%M&+dQiD&PM@4e+5hTyWFFyqBxur%Og}8S!G6nTC^0d4ViSOZB13lUEp6B`zZP7j+4cbkgcq6Q$Vabv(2)1tq%?I#Hwv0Yy`e><-dK<}gNlwK!CYyZnHUuV^t_G5mJaiZ9Hq;Lw=r51CU_(Zsbh=m=8ZPFR3yT*38XQOP>PHApID@mN27g=3v1J2?#hhVTZ*ypX<(CPNGdX6sg`8y#7V~19r?l_6b5W)w+Iacsj8TyA=x-!6HdHKx7z%PxEQPJ+$HsK*L4`0HL3b7Uv2^rf3K|b5%L<xRlVhW#jZ`8+Kj~{+V?CC7?*gr=QAw(|7phb^uMkD1k|yV+BUwUX@RHIL1!bnbRD-Zl-8o1akRo)ChSzq)`{K?weKr#H*vbQ%Q4*5}k`Ud6Xk#IE$3`<>q`iR6T-Yod$ntqA+rYRCK*gS;7!MoGSiCRQ@&dt+A@~slK^vbUPyb<r9c_{Bi6UGsi6z0B(%k(GQR5D<kg6{Wl4SNY!iKk^=BH4@qT>DriO-En9c+GMMw)0pK&GJVwEIJtlORY*X)M}BKy)TC46NzlmMb|kDr3PrPxQ)5y!UCS7Hk;wLle%}^|2evg%ih*1UnB+c%$#W3hvwzZtNZ%4emUJ8xd|9$m&7oo1pV3cml&MAog?+a`)$Zo1Gm1IzP%i6XV_Hi*ED#ZtJsdYo*(~*KK~;ZQbfNf9y6NbemsEywZe>7PmYE1tnB=|E~f#ECk=`gG_7{EURd+>o<b!FM{pc=;r9a+u*}N=W)>a7u^<Gmp^RotBL@0nxRVre^*`>)fWWqDpvh=-8Ey58gJuhJEE10Y+)j-Hz?&8U|!SWqXlDQ<tH@Y%1c=1(aL>|8)^kjg!a*lqo9(490ir>bns}>;zQ7TfrbaGqsbqr9Wx4=RgfFnAL$7ZAB7^)rv!{aw_0mlv*mN1>Zfb;EH|i}3LRQQNh`6aEnv^N9#s<I%Qj9YTG$wgu)!eXr#6iIuOchV;NL?S8;F*PsWh}AO&u&+y1b=c0l)Ah&h(Uv)8b4i)e#VrRaNpSH13X1P>Wh9D^@Xqtl323+m{<mrEo)M$%dzsMIGD}m-fpeB9=Pap|r(ZUnuSy(-D!WXlMoIp=q3;beOTM23T0p@<@HMPQ~GH#P>#6h&UWkG^n|cyTRIXrCa5l<l<_h5|`f-2MgR+r0;bDA@h+qb8er*a36V7?p8Kr5AOvP!)B^4PK<-M^$C53&SfSdR_PUx2s>OdNnE#Hc4}^-XpgW`R3M?+<;#vQb3jTYbheYleiY$b>EVi8*wzv15emEeeewDT+__4Bp;VMswF8*@y-CE`59z?<{yYLeUZ4|;D$Aq3C)KG4mwczZK-1O5nOHiMkK+754yvx*onrh!OdB1KHi8ZLu(4Rp(aNG9azd;$I~^U>`~PB>Y|+9dMx=s!{}E#Ms$}8Bcb;0=e8zy292Y0TIuF6R`*DUk7#asnVDXJ17j4a8nIwdBYPHI>lcr=Y>Ed2a7YB3x;!;h?E+l5+lSzmmu;JnCdJ3BxLY#H3;mq?|7Y=aJ6yH&9eVdVIVtMhf$H{tQ;iL)fEF~hc$xm;xlP9&IuQLo4TH?Hk5*H~EC65oF1+`Ryn&oxxZgA6KHzG?P$L`%s-o1uMDwelg!1P;WyhzUQG8anQ12<s4=6e|bQqKR6gefj?YsoE*99#Z1D_laf0V8kXKFj(egZJfLr_+M)g1=z}|B(x?*9(_kufyc)b(#|YEhNj>{{YKuw2c'),'Libraries/Compiler/ast_to_py.☾':strd('c%0o^>vI!F693L$u~6mgtSu^%2p6J4+!5n@R7`LIp{~kywq$8dROqqUT?hN}DBc(n!pk^7AV3Hqyzj^h2!tx8>b~CJ5P!T+`4g^tUOW4cv@-s5s<I``&h-4IyQinSr#0=ho5oD5UTxQ$S|z9$^`_hQ0;BHRt+v;!H0u9wYOAKP*B)nXZ`-TM9((pS>VB|_&_ne2*p9yv+s03S+d8&w`%c>?rswSS>Vf0=X3p5%XirrdKCyC!X<G1~ciy~Z%U?#fy}5aGhdn$xviWTo#;CnDf<4tB_{^HOjlt*fwS`HT^cww)o-#^hgC3x#=_0YP=>)xF`>s<hL*rNU@bKoH1U`L9ZxeIr(%FfbVm|-IPH)D+PwS_bE`7n9{tUCow#93_?d^8UF>zu+9zOa(&EB)OmPY)@Z9d9#f*G$RNZmic8|UgyqsH4N-pS|l)A_>GYy45oX^758p754xyA{-13gXclym`uVDtlshrW$+fYNOQw(~IYPWPMtYdUT#QI1SnK;+kwx%b(xJo2J{Ij<}F7Y!LVw72i(*5(Tk!+ZF)?I$opa>He}Q=rJm$Mc})W&sX^Oz?+NFY`glJPSJU~K+I1*85nr?-B(`u=%Y=WHf|gmdhuZG+O<oc9v-AWzY1D5UYxXyAwx;!@kvho)mO#pK0C-81_wpMF~QzVW!dlzZ`i0B1dqz9;VN%fEgR;);|-EyOY=8*L#0*g(B;Kl{=L->WRH0vEvY>7$5a<XH6A-Gdik>9sBAExV}ym4wTg_qJ&aq#r2FW8cyJJQ(P4Uo9tCb5qsQr|u!m02&*@3v?`e95o}~-)99;x)U7#0%hnMJOkiZps6-4+oy-vTOH|V$YCjE}yqPOWCdY9g#_vr)rPx>$VkbX~ppg+=|=p*`=KB2$Rr}P<pZUTz!!&?x=@H^YLlSZXERjVM%`}Ay%zn>}L`y&03M4MqXm8t6HH-`(wbs$#LHgQcm#zrzx`#wnx*#UIuuZ)n>sv@B%5jOY{y-$E)=jp@5!$ZK5pXgm8KHL+NAmgtCN1q_e;mdFt->vW|pA=@TIaOh`fR}_%mNVkhbesGh2~o%urp#^0ZeOWx0tBEK8`;$x1>3}jKqnUHO|^}IYs}OhrH>U|5U|DnBkf%yW6PwS)@MKH*)!Dxgl~nb#_?a%)5udb!EDJemmb|8@c(EU0|uGRS&S7?z(|JwN5Jl!?f6yO54;rI0z`^9%!!Ga0iVqxR>Op%uonKnZIQ5Hufc<Z^l>N`r8`#6GV0TUE^Ky#on+sEg=|d(6B85Wnh!rVEd#BzA%`Gt=ysMK(sg*Y%%EP+8FS^=j6uUROkJU$gN`)nEypLb;z)&EL`X3Q-#+{pS^)eU+b_@PK{UdEfNAZjnlo)Uvo2UPyW$77JBN!n2PWfb&H!C1!=F`JWxxv-vfBwNLEsVj9(Fa^k!tQVMQ42RBh!$b;zYE;VBd@~ShL?Re=!e#$IOrj3?NM=J=BQ{C~7foJU^LJ#PNX8rp6ZuaF{r+z;Y__jZa$WRGb1E`6X#46u1xpDK{8G)C9P6?8(xxUw-@X(tj^ql@csw8Ti}6cd~!JTYuoi#Y?784P5#&`Va*cSz(2#NC2E*YQ}8^er4<|@X_Ni^(ma1poj*A(gd7+;!%#dZt|ODT1kRZNiWi;Bmo3Qo~GY2F{K+gROmZguWymGHEYwC#c2o6qAL?yL_p!ROyS0CaNa<LCIpxJIsJif2Il0{gB6P}suEiXY~_GyPi#fP_mv7JJymEbXrGyS9igX{aw&x@fR+XDKZgfe$MX!qouj|9_p{>tihPeU>I`R8PO}u?xjF%O;!WjT7bQ0MT+lw}rK`PVWR$D}UwhqTV!aGE)2JS>q@ZB&rlsvcT<joM1#b7aR!ALIe6f0%0^Bab)BFAMY2gU{`-}~zf$dhjO4HZPObQX;3izSba!mDwF+T@RPI&MzZhqR+Fr7YX8ek-qDoVA`HX7eqR+@FJnpU^X#u<X{dl!}<h$FvWKJ|0dI(9`J>5MP%{*5YQu;?Cr9HUtk#8xw63y;iXZ+ywfCh<_G!(|ebfzY`FurIlEx~Z92t5*Z)Iark($|~*;bxYTuI6lrK4xtkV&E=@!vT$Wn6Cw5Iec~ElKCa1r__df7SLBFK1F3rWje6A~g`9z5z18tZ%MNpC{=9|~ZQUY$C>#(8%8IxriWuvf=FTw7F~pyP0mS{M4f>3pf<bK;0JDySNJEVloTV@<HfmZOJJJeqiU7z`R+cAI^iz{}D#|lFLLGA^NIdR4x%?c68@r9hItEdq=dRT`?40loB{#TdxQ&U!^nf*Bf&?#^S$px|#obTL*!kP1QIEzFu0_TphZ39Zc+QAogGWrklxa$p$+*Be$&~8=1l&ihkm6uW5sOJh40kS9Ki?_!vsA{!J`70K9g*Fja1ZNsXZ`Eh%}Q6hPJaa*HZ|sD-kT>fTaexm-WpjB1jURED~Dv;*m977J^g%zFo?0sL9t^6VfZfxW2JOM_|(gValIcH7sa$U#QSyF<CctCZt1bEwslM8nA@Edo)65`&Njc5mL|izWWt!sNKJ+Lkz*hdyo!lze`ZRz>MEjQ2Ac)np%0G1@nUDs*>9ocg45<Cy&{fc5!G<U;Df8N2N-9BAy2`=mj0ZzHQd;y2DFKl%QGZQIgue5sHLV(k{p#`Et`G7H`zG96$^X$mq=VHhODs|V4_wqppFZOa2StzM*PUfXndSqwWj*?IwvM(`^d5t<5{-5z+lM)E0-B4?of7>lo4&Gpz%DtV8s&}2?s*Exng48&8QBA^XN-3`ac08Az2ol4{{X&{I}^<l451jl~wo06B;XMX++ZEQa)Cff|;J5Qs^U|N@kWoaM>qI{-1dgO{H8HmsPIas0S*o!sgAGQ0cWB5L}8!p1g^X3Go9!>mcDb&N+ou-P`i(+VFmt<@m-%c4>QG%Xb&_d^b;a=lJc?GIrPdA5^>*vJu=o5BO`CwTr=D-p;?gFMIwW7Bfc=fvmZw%ln-7xg7TF1(i8>CK4rg&X(r2&uM#WWpbFkSKlkGQO?8*7KI%D8dH%ObwfLk{}gfC^xOvC#;^l;NP8SRh{N7^XA|=Pqhkw`MkGgWM|u}yy^E7k*MnF(UrL$dL_cT-_R{>mY>bI}R63*fzE^KJMEWHBCIHs-3SZEfn2p4orgmje(D(|vi)6xwMLjStDZ|e=tWCDA<76l)MS}G>L`)b6UNhk?m876gBr~MkYDYIfCf-)tP4^{u8#zwY)ry9&ClAv(xC{o?r*&%U;)#-FaVK!RR==rOlDN81I3&chooeA~NNhi8kF%#$P)7ZN7IN*D1>!zMmyB(x^TIP@XYuh%<Z|N}vRW8SZLL(4&uF3g#+{QR^hVTk8#FkzTVnLL#9UguhURHVx-vr@y9~w%uEoHVS4gni?9}j5+*;oj5gT(SqIaNcje-n6VpH;M$mWzAJsvyqnu$&)B3@|TNXra#4EIZ{_{7Q_gYg0}EK+ke<ZCGcO;Ku1ug!|<I<1-+`c@@9)1alkRpNS+QHW+;vxN10RyDV}!E$D+j*EBJ9j_s><a;}@Ke;+SU&&?ld42i(qOeg^8irMcVFP^W=KFU`kdLR&KiMPB?I~=<h<eL+JS0?*3HOYLB`ngNp6z~58pd9$neW0FWxlMaN?8OXoh3iB`;PgWP9Rk9ae^-B88zjuWc6!79nySy64qZu3x#G`g^(yFLQ}}SA&ckg#!?e?wSKa6qJXHIl^=_xNVBHvrac!3bm-MNN0%rTN_4HdY^SIyxLfp)5=v^_3zJdKs9Ex^PhR<1vapMFKi=iaGlK?zsB|BI#T#5JdNVnlrLm$hu_RQ8PI+9cY{Tx=hEr+TPUM6U9ZP9AxUA?wIF|18763=>lv4`77{7=(d>81=4uVciR<KGW2!waK|JlzOis=X?E3vdnt!BGzKW%9_qh8LJ!flnZP{&jS@zB9^P3;@0=hDh1yI3ftw3gONV!0BN(=kg%9n&Vfl1U^^SZ?O7zAh_;JN%@Txo$86byb-p5%n9@^BN&mnh5K%J!f~l-6Eqo!wpLjnNt3QjqvFby`Y_8WEA<&%OOX@Vj~wt2zJf|hdoiGI6gX#&nLy^a+zQ30v2m>a#gQ>avu(ks^&cUhJ_rP3?JdJq8f$+Lh@{(&5A1*x?^j&(y)ed0R(uSYwEpT?jwyB#TIpkQ{yO~h`l(7dMjw#zE=e>(QMHoeINj(D4N#{P3dgXiq0xsbk*%NXF$<n0?9H!-K$6LosuKyN&2AQSt4VKQ5TNuQU@+aJ#vT=a3ln<T=fLokhe$)`MaICIlN=pZ$(^_bj^$$!b0sdgOE^E?b$fafuRS%ClD*R;-FoLR9n)c&4`lmH5H}cq#VA&fboU-4Nug);pNd$wnxSOOjfmpE7I_KdM1-2R!bNi_f`~dgr&t4mTD%X7fXwhrR!cAqSE9@Oq(-W<-Eql?a2$V__4&!ww}HC&I}`l9@UEsR29&m?d78)I3o_vC^vcSnZO34S8v%(bmnysc-zeWKN4#TUE&Ug61(Qa$%CVXE4*WC`lU4*h=r^Uv4AaXkgKZyHG9qpvV;33y+RU4iYol)OUHv9mJuoW=SGW(#tuBkDGQgh)do_nO4G4FsCd3?^&A(ziB1}m7%^PfbiL8AWrO`*yW#luRK>4Xbw`kN`u)M6DB}XRmSuvYAmSD2GRz_F9RK-GJmzHn%wdvDZz$(8bhvNO1=5GB#uYVe=&k=)TE<+wmvfbnEkGqwQ5czvbBS9E#SiA`-H6_bF&1gQUToL!(2?mx&tG_81&L6NL|+gN@5X;>3KO!gfj5`vDi>72n?ZA?#R!^VbivzYD-f1(E=!jfBkT>dA11-Ac|Dv!Y!Gv}U2{qkEm4Jl`*v?@rir8=AS)MMUk|b=$35oh-QX>oZxq&>=rJFLO^Eror{R?&t47f0dQ6WHv17~;&ug=T$ejz`18kg6_15myhJb-kk%0Oktv&L0{N?Qq+a}ttZHcM&FNBZkGkXG2m??vEV(uEj`ZD-$S^onRIt66')})
__dir__=(__file__:=áÌî(moon_dir/'Libraries/Compiler/main.☾')).parent
from sys import stdin as ÂÐðþáÐâ
from time import time as áÏÖ
(ÄÊPSH(__ÄÊIMPORT__('text_format', globals(), '')), ÄÊPOP())[-1]
(ÄÊPSH(__ÄÊIMPORT__('to_ast', globals(), '')), __ÄÊADDGLOBALS_CLEAN__(ÄÊPKE(), globals()), ÄÊPOP())[-1]
(ÄÊPSH(__ÄÊIMPORT__('ast_to_py', globals(), '')), __ÄÊADDGLOBALS_CLEAN__(ÄÊPKE(), globals()), ÄÊPOP())[-1]
(ÄÊPSH(__ÄÊIMPORT__('tree', globals(), '')), __ÄÊADDGLOBALS_CLEAN__(ÄÊPKE(), globals()), ÄÊPOP())[-1]
(ÄÊPSH((moon_dir, mkd(ð(TMPDIR, ÂÞÅCAT(ÂÞÅCAT(__file__, ÐØó), sha))))), ((BASE := ÄÊPKE(0)[0]), (TMP := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(áÑð := ÂÑÖ()(show_preast=False, show_ast=False, show_py_ast=False, dbg_parser=0))
(header_com := ÁØÿþÁÙÇ(lambda ÂîÓ, ÂîÒ: ÐÌü(getattr(ð(ÂîÓ, '%s.☾' % (ÂîÒ,)), 'resolve')))(ð(BASE, 'Builtins'), ÄÝöÞ(ÐØó(ð(BASE, 'Builtins/builtins')))))
(pathlib_import := ('from pathlib import Path as %s\nmoon_dir = %s(__file__).parent' % (PEV('𝐩'), PEV('𝐩'))))
(to_py := (lambda áÖï, *áÑË, **áÑÕ: lambda *áÑË, **áÑÕ: ast_to_py(*áÑË, áÖï=áÖï, **áÑÕ)))
(moon_to_py := (lambda áÖï, áÖÝ={}, áÏè={}: c[h] if (h := sha(áÖï, áÖÝ, áÏè)) in (c := getattr(moon_to_py, 'áÐñ')) else (ÄÊPSH(c), ÄÊPSH(h), ÄÊPSH(to_py(áÖï)(to_ast(áÖï, **áÖÝ), **{'reparse': True, **áÏè})), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]))
(ÄÊPSH(moon_to_py), ÄÊPSH('áÐñ'), ÄÊPSH({}), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]

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
(decorate_code := (lambda áÖï, áÖý: '__dir__=(__file__:=%s(moon_dir/%s)).parent\n%s' % (PEV('𝐩'), ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(moon_dir, getattr(áÖý, 'relative_to')), ÁÜÙ), repr), áÖï)))

def compile_code(áÖï, áÖý=None):
    if áÖý is True:
        (ÄÊPSH((ÂÞÅCAT(áÖï, ÐØó), áÖï)), ((áÖï := ÄÊPKE(0)[0]), (áÖý := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (áÕÃ := moon_to_py(áÖï))
    if áÖý is not None:
        (ÄÊPSH(áÕÃ), ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0), ÄÊCUR((1,), {}, decorate_code, ÂýÃ, (ÄÊPSH(áÖý), ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0), áÌî)), (áÖý := ÄÊPKE(0)), ÄÊDEL(2))[2]))), (áÕÃ := ÄÊPKE(0)), ÄÊDEL(2))[2]
    return áÕÃ
(compile_files := (lambda F: Âøî(ÐôÅ(F, lambda ÂîÓ: Âåß((áÕÃ := compile_code((áÖï := ÂÞÅCAT(ÂîÓ, ÐØó)), ÂîÓ)), Âçß('Compiled %s %s ⭢ %s' % (MOD(ÄÕéý, áØÁ=dotrim)(ÂÞÅCAT(ÂîÓ, ÁÜÙ), 25), MOD(ÄÕéý, áØÁ=dotrim)(MOD(ÄÔéÄ, áØÁ=áÖï)('\n', '𝗻'), 35), MOD(ÄÕéý, áØÁ=dotrim)(MOD(ÄÔéÄ, áØÁ=áÕÃ)('\n', '𝗻'), 35))))), '\n')))

def refresh_cached_imports():
    ÐÌü(getattr(TP_CACHE, 'clear'))
    (reimps := ÂÚü())
    for k, v in [*__ÄÊIMPORTS__]:
        if not (getattr(v, 'hardcoded') or getattr(v, 'name') == 'Compiler'):
            continue
        if ÐÌü(getattr((f := getattr(v, '__file__')), 'is_file')):
            getattr(reimps, 'append')(f)
        getattr(__ÄÊIMPORTS__, 'pop')(k)
    ËãÂ(ÐôÅ(reimps, lambda ÂîÓ: Âåß((sha((c := ÂÞÅCAT(ÂîÓ, ÐØó)), {}, {}), ÂÞÅCAT(c, moon_to_py)), Âçß('Transpiled %s' % (ÂîÓ,)))), lambda x, y: (ÄÊPSH(getattr(moon_to_py, 'áÐñ')), ÄÊPSH(x), ÄÊPSH(y), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3])

def generate_bootstrap(dest=ÂÞÅCAT('/tmp/☾.py', áÌî)):
    (ÄÊPSH(PL_FORK(compile_code, __file__, True)), ((_ := ÄÊPKE(0)[0]), (Æå := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (pyc := ('#!/bin/python\n%s\n%s\n%s\n%s' % (pathlib_import, ÂÞÅCAT(header_com, compile_files), ÐÌü(dump_cached_imports), ÐÌü(Æå))))
    if dest:
        ÐØì((ÄÊPSH(dest), ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0), áÌî)), (dest := ÄÊPKE(0)), ÄÊDEL(2))[2], pyc)
        getattr(os, 'chmod')(dest, 509)
    return pyc

def generate_bootstrap_live(*áÑË, **áÑÕ):
    ÐÌü(refresh_cached_imports)
    (ÄÊPSH(__ÄÊIMPORT__('Compiler', globals(), '')), ÄÊPOP())[-1]
    TRANSPILE_REF(moon_to_py)
    generate_bootstrap(*áÑË, **áÑÕ)

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
            (áÕÃ := ÂÞÅCAT(áÖï, compile_code))
            Âçß(ÂÞÅCAT(ÂÞÅCAT(áÕÃ, VEP), __highlighter__))
            try:
                Âçß(ÄÕôñ(áÕÃ, ns=ns, native=True, Æå=lambda x, y: eval(x, y, y), ret=True))
            except:
                try:
                    ÄÕôñ(áÕÃ, ns=ns, native=True, Æå=lambda x, y: exec(x, y, y), ret=True)
                except áÍÚ as Ïã:
                    Âçß(Âøî(ÂÞÅCAT(Ïã, getattr(traceback, 'format_exception')), ÁØã))

def transpiler_cli(*áÒø):
    (show_docs := (lambda: Âçß('Usage: ∅                  (cli mode)\n       <file_path>        (run ☾ file)\n       -h                 (show this)\n       -c <code_to_run>   (eval mode)\n       -C <code_to_run>   (exec mode)\n       -b <boostrap_dest>\n       -B <boostrap_dest> (updates compiler)\n       -e <str_to_encode>\n       -d <str_to_decode>\n       -o <file_in> <file_out?stdout>')))
    (ÄÊPSH(([*áÒø], ÂÔð())), ((áÒø := ÄÊPKE(0)[0]), (f := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    while áÒø and (áÓÓ := áÒø[0])[0] == '-':
        if not ÂåÔ((ÄÊPSH(f), ÄÊPSH(ÂÕØ(ÄÊPKE(0), ÂÞÅCAT(0, getattr(áÒø, 'pop'))[slice(1, None)])), (f := ÄÊPKE(0)), ÄÊDEL(2))[2], áÓÓ != 2 * '-'):
            continue
        None
    (Æå := (moon_to_py_debug if 'a' in f else moon_to_py))
    if (ÄÊDEL(1), False)[1] if ÄÊPSH(f) else ÄÊPOP() if áÒø else (ÄÊDEL(1), True)[1]:
        ÐÌü(moon_cli)
    elif (ÄÊDEL(1), False)[1] if ÄÊPSH(f) else ÄÊPOP() if ãÊú(áÒø) != 1 else (ÄÊDEL(1), True)[1]:
        return ÄÕôñ(ÂÞÅCAT(áÒø[0], ÐØó), ns={'__name__': '__main__'}, Æå=lambda x, y: exec(x, y, y))
    elif 'e' in f:
        ÁØò(lambda ÂîÓ: Âçß('%s ⟶ %s' % (ÂîÓ, PEV(ÂîÓ))))(áÒø)
    elif 'd' in f:
        ÁØò(lambda ÂîÓ: Âçß('%s ⟶ %s' % (ÂîÓ, VEP(ÂîÓ))))(áÒø)
    elif 'D' in f:
        while True:
            Âçß(ÂÞÅCAT(ÂÞÅCAT(ÐÌü(input), VEP), __highlighter__))
    elif 'c' in f:
        (lambda ÂîÓ: MOD(Áëý, áØÁ=ÄÊCUR((1,), {}, ÂÕõ, ÂýÃ, None))(ÂîÓ, MOD(Âçß, áØÁ=ÁØã)))(ÂÞÅCAT(ÂÞÅCAT(Âøî(áÒø, ' '), Æå), eval))
    elif 'C' in f:
        ÂÞÅCAT(ÂÞÅCAT(Âøî(áÒø, ' '), Æå), exec)
    elif 'b' in f:
        ÂÞÅCAT(ÂÞÅCAT(áÒø[0], áÌî), generate_bootstrap)
    elif 'B' in f:
        ÂÞÅCAT(ÂÞÅCAT(áÒø[0], áÌî), generate_bootstrap_live)
    elif 'o' in f:
        ÐôÅ(Ááú(áÒø, [0, 1, 2]), lambda x: ÂÞÅCAT(compile_code(ÂÞÅCAT(x[0], ÐØó)), ÄÊCUR((2,), {}, ÐØì, x[1], ÂýÃ) if x[1] else Âçß))
    elif 'h' in f:
        ÐÌü(show_docs)
    else:
        ÂåÔ(Âçß('Invalid mode(s): %s' % (f,)), ÐÌü(show_docs))
__ÄÊADD_EXPORTS__(globals(), ('moon_to_py', moon_to_py), ('moon_to_py_debug', moon_to_py_debug), ('compile_files', compile_files), ('generate_bootstrap', generate_bootstrap), ('transpiler_cli', transpiler_cli), ('moon_cli', moon_cli), ('refresh_cached_imports', refresh_cached_imports))
TRANSPILE_REF(moon_to_py)
if __name__ == '__main__':
    transpiler_cli(*áÑË[slice(1, None)])