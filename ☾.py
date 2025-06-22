#!/bin/python
from pathlib import Path as áÌî
moon_dir = áÌî(__file__).parent
__dir__=(__file__:=áÌî(moon_dir/'Builtins/base.☾')).parent
import os, sys, inspect, traceback, threading, errno, struct
from threading import get_ident as áÐèþÂÐðþáÐØ
from os import environ as env
from sys import stdin as ÂÐðþáÐâ, stdout as áÐãþáÐéþáÐè, stderr as áÐÙþÂÐüþÂÐü, argv as áÑË
from sys import exit, setrecursionlimit, path as syspath
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
from multiprocessing import shared_memory
getattr(syspath, 'extend')(getsitepackages())
setrecursionlimit(100000)
del (getsitepackages, factorial, e, pi, tau, sqrt, cbrt, pow)
(setattr := (lambda x, y, z: setattr_(x, y, z) or z))
(setitem := (lambda x, y, z: setitem_(x, y, z) or z))
(ÄÊSTK := {})

def ÄÊPSH(x):
    if (t := áÐèþÂÐðþáÐØ()) in ÄÊSTK:
        ÄÊSTK[t].append(x)
    else:
        ÄÊSTK[t] = [x]
    return x

def ÄÊPKE(x=0):
    return ÄÊSTK[áÐèþÂÐðþáÐØ()][~x]

def ÄÊPOP(x=0):
    return ÄÊSTK[áÐèþÂÐðþáÐØ()].pop(~x)

def ÄÊDEL(x):
    del ÄÊSTK[áÐèþÂÐðþáÐØ()][-x:]
(ÂÞÅCAT := (lambda x, y: y(x) if callable(y) else ÁÜÙ(x) + y if isinstance(y, ÁÜÙ) and (not isinstance(x, int)) else x * y))

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
    getattr((Æå := (áÐÙþÂÐüþÂÐü if ÂìÆ else áÐãþáÐéþáÐè)), 'write')(Âøî(áÑË, ÁÜÙ(áÖý)) + ÁÜÙ(áØÁ))
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
def PL_CPU_COUNT():
    import multiprocessing
    return ÐÌü(getattr(multiprocessing, 'cpu_count'))

def PL_THREAD(Æå, *áÑË, **áÑÕ):
    from threading import Thread as T
    (atom := [])
    ÐÌü(getattr((t := T(target=lambda: ÂÞÅCAT(Æå(*áÑË, **áÑÕ), getattr(atom, 'append')))), 'start'))
    return lambda: ÂåÔ(ÐÌü(getattr(t, 'join')), atom[0])

def PL_WAIT_PID(p):
    try:
        getattr(os, 'kill')(p, 0)
    except áÍÚ as Ïã:
        return None
    getattr(os, 'waitpid')(p, 0)

def PL_CHECK_PID(p):
    return not getattr(os, 'waitpid')(p, getattr(os, 'WNOHANG'))[0]

def PL_FORK(Æå, *áÑË, **áÑÕ):
    (áÓà := getattr(shared_memory, 'SharedMemory')(create=True, size=2 ** 20))
    (áÑÅ := (lambda ÂîÓ: ÂîÓ[slice(4, 4 + getattr(struct, 'unpack')('I', ÂîÓ[slice(None, 4)])[0])]))
    (p := ÐÌü(getattr(os, 'fork')))
    if p:
        return (p, lambda: Âåß(ÂåÔ(ÂÞÅCAT(p, PL_WAIT_PID), ÂÞÅCAT(áÑÅ(getattr(áÓà, 'buf')), pload)), ÂåÔ(ÐÌü(getattr(áÓà, 'close')), ÐÌü(getattr(áÓà, 'unlink')))))
    (v := ÂÞÅCAT(Æå(*áÑË, **áÑÕ), pdump))
    (ÄÊPSH(getattr(áÓà, 'buf')), ÄÊPSH(slice(None, 4)), ÄÊPSH(getattr(struct, 'pack')('I', ãÊú(v))), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    (ÄÊPSH(getattr(áÓà, 'buf')), ÄÊPSH(slice(4, 4 + ãÊú(v))), ÄÊPSH(v), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    ÂÞÅCAT(0, getattr(os, '_exit'))

def PL_SLEEP(x):
    from time import sleep
    ÂÞÅCAT(x, sleep)

def PL_TIME():
    from time import time
    return ÐÌü(time)

def PL_TEXT_COPY(x):
    try:
        from clipboard import copy
        return ÐÌü(copy)
    except áÍÚ:
        Âçß('WARNING: Failed to copy.')

def PL_TEXT_PASTE():
    try:
        from clipboard import paste
        return ÐÌü(paste)
    except áÍÚ:
        Âçß('WARNING: Failed to paste.')
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
        ÂùÆ(áØÁ is ÂÞÅ, '"%sˣᔨ" is invalid' % (áÑã,))
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
            return ÁØò(lambda ÂîÓ: choice(áÏË))(ÂÿÇ(n))
        if ÂÞÅ is áØÆ and áØÇ is ÂÞÅ:
            return uniform(*(ÂÕÀ(1) if áÑã == '\ue270' else [0, 1]))
        (Æå := (uniform if áÑã == '\ue270' else randint))
        if ÂÞÅ is not áØÆ and áØÇ is not ÂÞÅ:
            return Æå(áØÆ, áØÇ)
        if (ÄÊPSH(áØÇ if áØÆ is ÂÞÅ else áØÆ), (áÑÿ := ÄÊPKE(0)), ÄÊDEL(1))[1]:
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

class áÍáþáÍá(áÍá):
    None
(ÄÊPSH(getattr(sys, 'modules')), ÄÊPSH(ÂÞÅCAT('𝑙𝑙', PEV)), ÄÊPSH(áÍáþáÍá), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
(ÄÊPSH(getattr(sys, 'modules')), ÄÊPSH(ÂÞÅCAT('ℵ', PEV)), ÄÊPSH(ÂÑÖ()), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
(ÄÊPSH(getattr(sys, 'modules')), ÄÊPSH(ÂÞÅCAT('ℶ', PEV)), ÄÊPSH(ÂÑØ()), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
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
(TMPDIR := ð(ÂÞÅCAT('/dev/shm', áÌî), '☾_tmp'))
(mkd := (lambda f, e=True, p=True: ÂåÔ(getattr((p := ÂÞÅCAT(f, áÌî)), 'mkdir')(exist_ok=e, parents=p), p)))
(mkf := (lambda f, e=True: ÂåÔ(getattr(ÂåÔ(mkd(getattr((p := ÂÞÅCAT(f, áÌî)), 'parent')), p), 'touch')(exist_ok=e), p)))
(tmpf := (lambda b=ÁØã, f=ÂÞÅ, n=14: mkf(ð((lambda ÂîÓ: MOD(Áëý, áØÁ=b)(ÂîÓ, ÄÊCUR((1,), {}, ð, ÂýÃ, b)))(TMPDIR), Âøî(ÄÔÙù(MOD(ÐâÇ, áØÁ=1)(abcABC123, n))) if f is ÂÞÅ else f))))
(tmpd := (lambda b=ÁØã, f=ÂÞÅ, n=14: mkd(ð((lambda ÂîÓ: MOD(Áëý, áØÁ=b)(ÂîÓ, ÄÊCUR((1,), {}, ð, ÂýÃ, b)))(TMPDIR), Âøî(ÄÔÙù(MOD(ÐâÇ, áØÁ=1)(abcABC123, n))) if f is ÂÞÅ else f))))

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
    while (l := ÐÌü(getattr(ÂÐðþáÐâ, 'readline'))):
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

def ÄÕôñ(áÖï, ns=None, get_code=False, include_builtins=True, native=False, Æå=EXEC_NATIVE, ret=False, init_ns=True):
    if not native:
        (áÖï := moon_to_py_cached(áÖï))
    if get_code:
        return áÖï
    if init_ns:
        (ns := (ÐÌü(getattr(BOOTSTRAP_GLOBALS, 'copy')) | ({} if ns is None else ns)))
    (r := Æå(áÖï, ns))
    return r if ret else ns

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
            (ÄÊPSH(getattr(sys, 'modules')), ÄÊPSH(name), ÄÊPSH(__ÄÊIMPORTS__[F]), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
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
TP_CACHE.update({'Libraries/Compiler/main.☾':strd('c$~c%+iu*(^<7^vMqzNqplwM;9=h<l(A5?!TY@A90c3&TlCxUEyX1nTWC?~JoWyOBw213V>I88D)d<?4t&{W;1g(=k@K5{&{e+$~Hx4h7r6%pd)($ym&TY<pY4L9H-s<`l>Up?Yy0*Hqw&8iy$@yOH^^<hu=Z;IZhe^*LW|X<aaTxp+$5vJ;W1DBEwkGJIXcEuQS}{n-nfdw4%PX@p%j@3U^1{q@I3rM9T|h{4=mZpjoCj3L`~Od(dCK|!k{%r;N$iDD>XOl|kQQIjjccp(OKWiA?c&qo{@lz4Emxk`kA~dyVD~}swD>C^&IUfik4q?>ompQXoi5QlOtQ_%E!+W|wf9q7nydMRWje+14RCc({HFLyfW8f@4=JPBAi3?0Qx4kiE`l^1Ny4l8^LXEW7528hv7cr<?M^Z_K?mFqdFlnpNFcul%>S$S9=<;+enE%+s2BQ3@<s8;mER9LDB`b*mvo!wex9eO8V%u`&d$Ah`n^L=6Z!6;i_$nL&ywLThYMl|j_QE7vpdl+kK)Xc0zWIhDL$oAe=Shwdj=do6Ljq7gJIP3qR}`>b7Y@7{S*XI8$@la!XxoBayq*i>q{kFcr>@h&VfpJoD05J7v7}Kzn?w$0@<=21WjS)f|S<HLGfYnrAy9;8+soWa`mJ`6hzC8aTsbgC7!N9r(gw9!Stb&#rL!Box5WBLGcGzc1W-}*dkG%&;gzSTclNZ4a^vcVnPFi(id9N1N8&ggW_utpKvfBV*De}z60xlwU%;8VvNdQL@Qzeb%x73U>3p@oetSZcevUHrtYHAWIT^@J~Dngt%<;T%34p_{&E5Q<-!&!P4iO<V=-x@Dqr2XD``rTJ~_>aiIDe6NzDs+Z)e*`Zd_AJDjt)a`lA;o9vGrO;#C)JdU+J<M`J3T2?8Iua|Ixu@dK{-`{FY?yYdzVoenv5maaPrQILdOUl&>%!lV38iigEZw2ImlVgL~bw^M)QVHECKJld99VF&gseh!LX7hgk|5#NRySli6{hNF2nfVb}`4lI+ZN1yU=Fiu4ZP-Z1`TVtc5<D(R`a$}>eA>hVn$ijCLEGL!3u<GrCL`opdL(21=G$xX>2^#VsN&TD)N{0rD?>fZsFammB*Tlb07lNS<jpt8iOb5i9@#(A?6x$MDxhnIf5lj#kX<+E*(JluMktNN&;*;Vdd1EQlK@jB=&ICzmjQm+9s-@^&PhwtLynIQbOazkhM#^k%ajFsNM6Ib}qL%B{RIO+nBU{(Zw~PtK&zgM4Nls9v7T%TVm7&U##c(2b=WeV~I_1I>rh|$_h->?<c*m_E2I{Xzd;n(pf*qy<Oa5t)e|n2)P$mBnplx=nZyilDv+a1XgCcxeyg<kKTXCN*x};K}i2cvO11;he8?vw0wp>}=NPA$a&UvI(=+Vxc#1cZ$fd5|o`FBJ)#<i7s>9}8@g#-Sl#l3Er<Y_cww1tSa_~|#`&yk1K=404=*KF$0;oOWNuz*MY_MhmH7yfH(Xjv`TWZ{bMjW?#e4`tlI3;bZfLsfM_4J|FU7RxqPy}6mWD_Fk;L+)cVlWvi6IGCv$_!v&84d{EwEtl+KHL`ieF80?wZ>#hQa2j+Kx@$WP@#Byf+Pgq>;HM#8dFU_#nC&eLr|`DhCHh*CyOIKaf+U7YbBEhxYZB7FT{0nJ9Zf}ObD~T<Hc;ymQV{^?kH<U)K53s#)PZVx0O)Zt2GCm)w0OUGUc9Z{L1R3`C$I*Tb>307k8wkkLM2e(S|QB#ijCBdGwl~;&Hu=i)}#2?bIE?E3_3>_nPn{6v)21RupE>Iyv<`S!eK8-@+?pNG2~1rt7K~jTtMe?4w_hfV}|9`Wp8n1?JBin2{xL#<&$X{(}&ldIeuPze(bz4-VbCe^OIBOdr^FTyq^z}7!$GmUue790NGboc6BbP#8c*KI}Ue7<C-s*o5-<U>!6;jItQ)gPt@oKcTbW<5dJlZ!6l%FravU;Fu`DypuZp*m%K6g(@Hr6=MKAWZwR#qZS-T+2-Y6vl)p*CFYZGY!s7KMXu(;N2fzvB5!H5Pr!b`UC;N_7RJTqtOcZ+k(B}vy&PuY#hQe28U}J6O`ugh9@`AUvuxR&16H>(u?`Uf3a0V``;~_EUZTe+%6bvJsGgN;LumSJ+!7Z!<{csq?GVanVOY0lnA~0MFTIDDPT^2EVgDA_BbRV<V=vJQ@MjO?s!D;2<G9*jtqEhukja0{R<)8gM!A?c`SD!p1Qd%Fr(xKgY&^S}Z{sh7_bUQd>d9F5Z4*++gXl<!dfUFC-alDf=R!@c!zM5uqjJ}+Nm?^iDBs}GmC$X15EH4=)+)g3l*0fM6kX4TBV)jdsSY^(y5@`5wwx2;j2b8)*sDL*)w8erbxHr|?oSIRKt1=*>lA4vi2Qq9!q}(3l5EMPeSOc$Jt~SowalhrP_J_8vNMLozn+vO~g^wm1!c;_K-`vd8{iZ@}28@L%sxfFe77dpgGhkTn@?C$3o~CCHQ5-=}oXK%Q3s3lI)I;W$_5wc6+u0iXS#|;;j>-KV4-V)45dP%A;bR;E79SMPkJh4UG0HoH6J?CBf|Vm@^`4{=C9&>lrF)Bzm+KNK6@d@q=)>Y$U0{g8K$rw}o6|8iek1d@d566E<^3kJ6tF=&1$(?1t5+9AIf6C8B?Fc2!~{Yl!L1VV?4XGcSs^+2x&;=Hi)iwgB>)j(rD!}gx@YHFz~GkZU_EjXQiDvyn7S{OTeI~oLU+a?WRuJ!GYb(X7XcK>@fZnPh(fc4y>DeJQ3{HHL%B+J@}FgS2w#^RR!`D&Q{B~;h$xRC=`b@QfY+^sUjMjNo(%g6lW1OG{it{(&WpE*5&ny4de&+5Kcc9AT$W({YW?-3cv>yKj5SYI#xg)i_Y`b18%6=AQ?6*Km|(pwQA?es7(dk|)8q{D`npyMu`6Axx|r6drYNQ3JJ<{M<=EM7Ky*<`OU1e>W`cf2CNf%)r%e^5(iCdFoMvkjB4-1JN}-D-p{`pbWj_1?w4WF675`A0XQ;HPV=<yfBqm1M8Ae)*HPC`^cn7*sF*o!aG4LDtQ4H(5DvDNGGjvvpOZdku867Tfz|sfCw!hG3gQ;>ddG*;hwN_C4f}#g1`0I}p-J%ly7*rs^9!+JwPNl8#64Z~#=F%Kw6?Sw|mqdd)(YjD#Ds!*+qcyN;j`4&)|Gk{w3HM}1bb&)KUE)wVh_#EMGMsjQB4)bS@wo)!dqsq~#_gOGBUqP>uy-tkmQ~BX(QRo^Y_zjK9$L{R+PISjZaHuPH6IvncF88hR*0U{Th{EOW6x14<81SK&vssWjyr7(K=j)#*@Kv%%|L_`e4(O@Fo4R<4O+NH^EE|>2F|KKgkWCL&bAbTJw%~M<uqd*?RI_fvu*<+n=rq=dkb%=p%t~7TI!U6+^LL}s(UgGR3PLl0aux5IL!$Mb()vzv>Fh?R!cO1tG*~Xle;Dv;QRJr0k(kcQv^0~coPnHren6q`X*@0+i9sJp*L?N?f(EjahaR'),'Libraries/text_format.☾':strd('c$~!=Yi|@s^1FY<C=!|;XMCAm;{eWWashHey5t-I(M8%_t@bgt_t=MTcYIz4kid9t5?(eo4o-mJ@W=z=I{`tE;2_aIAip8=3+^XeRrO;YJ8N*hgk<UN>h5}VRdrPl)%sMk<ryt^fbk9fjQ>zBmM2|fG-I$@v0kba4Zgtd*v25tF7tEH5xpy;2A|`1_$p)k9RDxhz%8_w;RegH4Y@yIr`l2-M<h@9GUKQDRsKMeoa38(1t{F&pYflV7+SO(*FBaH+W>?s{IO-YwYF=dEG9@<mhopJ<)n8DIPt@J*s$Oa2tCg~`|!vi7M7kB3X|1|$r}7Tw^b-uL`cs9tX{6QER>P4Lnt_5`P+NUv9eAc!MqD%{X)C$#}=gWxDf#d-+P~>EQAcO@oJ+|aNFfV+x=G?cTBim(eqlY<=Tc>Zq}!&HP^HlJA#vDu9GU|a#{AyXf9WI{jKy{)abuXI9B~cHrH`d@Jr`S5|v0a+>Tc$PZnF-&@dU`h5vW8trL=vQ?~~H^p0g3y9{>3CUmVj@=L;nl!I~|_~<ZW!!}5H{G=Tv(w;7v0FOv(i&MR2<GF9~Glad;^jg(=9J{oSj&00lMx0TjlWo_kWtaWE*#PXb#t;}m-gw<G{Zn^MvKQJ6CxHg{HDevZc$#11>#PHWjJIJISxE<})~XG+9Wj1siAo3<-{9Q??;Z_IkdRp@+f=RUq55(Sp>Pi%VPwemC~kO;M!mro`BN6r4yvVCs{xMaS=qoH?6qv+E}Oz~Bces<XwMO6gp!7wr=yt;Nv^R`8^adY2K!*_AS&P?zd){Wm7mTy7E_W1&KY8mj6UMemL>H467~>)=ZiuQRNQfcj=TWa*Z5Onc#Z#uiH3--@hxj~z<@sjdP7<fa4F42ECN?m>$7RJ8n7LU_8~KpRYG7HnT(MVIOBNd`1ky#1OUb;g;YRcI1ktbdK4=WS#}#Vq=LK%#JEN*NZH0v%2HHrWQS7uh)aZsOW9hkH{EJTLz1+?^w4Gp2L2LqHq!M}vBF4o3-X{BWqUSb8m7emECW0!jYs3D_B?^aid%(%FUnY2OOB<q<W-`mJiD6lwmk5~K+Q^S;zRO!iJvA*mlTGKniUuTNrneMl<I>8OomVlN|p3(b$WNA?Vo2^+PKR|>&=Lau;O9j<Qs2<W)s*-;3~|F#z(7w>{GtL{#pdngVWyC_RoHr`^a&e@jc~XSN7cDQi>wHAYxm6ETXMVVkX1y*~TRNEzdu6MJuZjz8tl8R30c^xW6<FE#iz(Z5#YvXvYjL-ah68HX4aJ8tG&Y(n+!??dA~{Xmz9Mk=F%#^erH%nGm4eMg`(^7Q6ve51ckzh68udAQBjg<B!VNOF+9%;4TV~oFGw)7oH+N)Z<_}*aqHXX}4O4x>d-f(%@3*d?aKDbLusTwpT14YcUa-z7H$`<rA=8Q>7b!ATBd*$3T$8n}`O3V%fdeoQ{Sf?1^C6KSG3~`#r0Vrv~2ByW{Ny_mgT+#u3rVJ$dw@V5W^9W>Ge68!T!x$emJA$})<LiWrW4$Rcy$T^LYlB@5(7%RJhecBvDCQ(Un6r~sH#!DJEoNw>&3AU-Fuf_Z)g%7UxfN5x57ED|>`YQ*?e_X~FJTm5gOQnORgc*Z9(rZeJ<>>G!>s8pTEgarv%QHXftAi662_g+<aBr@P45=up!(B>6>McE+byD63LhEso)(juo;LT;hXHzf`W9R{RGJP4r2%&ckYxUP?dW+2CpdJ`Q61xI}pX$zylm;8HX`WH9+i(mT}Z{?=bj<e6dc-y~t$G>>jv}93rMcl|^i8u0r9bCpBPtqlbW|IxFY13alZ=yJ1$SG5@-nA&FUtKaacbEtzhQu+TEf9&wcmTNz#nUi>)t8gJ8j#E@qwMPdz|ltdGSZmSwjq@iDg|ug6J(b)$Ouyqx}iLQYk`6nP-ma$kwsO_EQ!;|Ywuv&-wpw-gc@A<kzl_g5yrCc4SoTN^b?}<ovIcRunFH&Hw|Ka&KL0pAsYfpiB`0K?BiD|jlp?)$|%jms6GNx0XW`izRu^Ps<1_Sc~s=H5g5q{h|rycyTd?;8q08lawU{!P|IeeOuF;~I^{o{XJ@A@xBhUJccx`rInydm^?4>xept!ub!=lQvl~(*AQqD)?lm%S-s4-r9hR6<K@w20w3tD)4A;Toeu@baHjn`tB>|gKF$*+R0cJ74;rjtPV#Nw-Wp#<gw9uID_g12mP|rYi)XvcTe1Wg_7WJ`ECLi~N=ZU;qrx^46I)BXXv)KC_zP<osbqkA-GyJI~;_V8*q_a>PwX=<KWW1D_1X0naP*chVENx3By-I6=Mq-N6cCup?1%~scG8}zeQs+9<*O4W8a!9c~*_<hqn-w?aQI$-}arDzEL_p0O9dxE583^YT=J*7VHut4Q%s%M_1=@~ybE<l^I8hz1%Ne@j`ks9j!xj^2?Fa?i`jpD@&RvJl9^Nk8z09<q>uW$f#^&|GY+J!)2j#ixhY4a?Yz67^Dr2<7nU2@V?T-%*R;p!B=beyL1doYeO+f|*D^{WRz@{wNHe@X<-$~B!1xiY>y)RnYy3Bv1QCE(h$o83RAISE(Y#++@k!&B!_9-!N9fbc$_8#$5gn3b}_(`w$nIM;GUaY(%*Zi#4JkxXM<lL5?+micF>os$F?zx<s({pEZZ%Oy&b#Ga&-_(%H^ggjk@Fjki+AGAx8Itl6=>*q4;Wu?}L-)Rxy-f|<48d;e-W}b$t9#$*-nY7UOJ*ux$o95u*JZn=G8x%^C);n;+k_n7knNYU-9*FvZRxJRbjrVfTRf3CrM-LoYb*Y>&;7Lx|ItJL(W4hzes|@?GrxPq@2>mZCBOTn-(B{*m;LUl-(8bWE0t1O_x8N_#qWNuhr@pNni`bf^t)H}%x(=%``s@zc*O5s*Moh!2U~CGK~ZnrqhTct+v_iUst5aiJ>}0Y`e$$O&0pu$OVHkm?&;T|z2oY|=*@k)SJb_-?p1Wp)jhp;kE3Cw|6O0c48LpeTZZ2y_^rcl1AaGuTU~-?4Sp-|gTll*8A^D;`$LZ-6j<oq3a;$?;RlaM-aTp@f>eTXQyE0IdjNS!jvWriIu|g<$A>ZCnRYgR{G|WYV^d_p2gW`~&V=9ZO@tAAI0jCO>MOo_Sb*cJcN6&C!~clEM-sE_;Ne!j-!1X;{28Orvc~W|;e?SebyZD;T`p8KsOOyXe5>E%?uDM0p2RwUs(&iQ)=A+j{HAQbfn-tCm|kl(C^jL@gnFuBz##{~Q0)frY)90oZl~-{dBG~Y6ht|FRDLj`nkXpYk78-&%}%*Jwe2DONe8Q{LZMNtyM=-o+bSYYZ($s<CiR&L%BzWtnRe1<3<-s;q_;KPCuVz?7BQ~hCV55Qrkh51(uftt5h)MP>n|-KOu~R}g%?|z@VfjYn|zFco-w@xJAXZvm4;PY_1t>fv{>A^&0TH$Pd#KOn~QCLU)cTl5YYj$A7bNhqU>;i>`?Y^f3NH!LF)8l_Z3)O*dePMJ79JH?_za-GOH{6VK1wuJk7qYWk=s+l-~^CKSg*FPKJ~I6+@&f6?r){-|(;cS<f-GSX4jkn0iFSiniG@WCof?_0ZcM>GGHr`lkn~8kTP=@{QCQC=@X0y?gLr;k}PP96NmUNTI+cYRwX)s%YoT6d!aUD;FJtQQiz7Y6*fbCIG-jjmu(OR^yf!x74^T#$vyCx;E7tHo;2G4!*HAJ2ZmI1xE0<<^W0<$piE>bS41LD7g5v4^Yt&6ji;1L{*<=sGtETwPJ0;_g~zW0H*cP>fH=ID~OLov?dgI&1jLOa3q+5xs9E}9xy&!0gd`}?YV8Q;NfTe@n)-D^q4euWpKiasP2zk1*SVOVPan4IN}93GCAYIADo5+6(4X%(9QhSId$ns?7Dajjj`~24Uik{Vy##)U|4cnhBxEZ{_PsTqt}2in`?NJE(F=OXLys<#)L83oHi@QOtIk^%?6HIMrpb=@ft?WRN6L%MZK(E%Zu_uIT8f}V&*@a{ttKjvuE968;}><&1$9Cu8<V!8yPEwHesFoN}I}YN+Yo6x1}FnJP6iQ;)r|K$XWRXrwH0C<{G73qnvA0at%~<3F={bm<g{(e^W=5O3@jdGGDU9=v`3W*@8qOu%tGPF(Bn^w*(wM*XX?ZGB^ZKeX(e6vwC~pTRU4Ii2NT{EBTZ'),'Libraries/Compiler/to_ast.☾':strd('c$~c&+iu*(^<7`VJdu>v!LCxEsDVW)TdHeRzQB@!0J1<(TuLImOR^-_UZE&pS+e3<h@*=wD{0(XHr&RRqb5a>+HI0P4A9qpL-z~(2|Z_KNDj&2UL>arK{LylIrr;uHL_0bU7q=+W*9g-f8p|_E3<~7seyena3VVh)rzvz^cKu!sOc3&Rdx8!Hcw1Wo}0dOW@38AI6FNxaS@JDXuq1moyj4X)5n)C!+h>kZGJ>6L%I~0t@j&dWXh1{f#7E4bX~#G2z>3rrAY+*fV?2<u={}QlhyjUD-#!Vjoc=`CoeVi?c+yV*V^ON>d)Rj-uqTXpvlVq`iJq-qn95tj0fZ)*{LYM06J`4XDAKJYi01_NC9n=Jx$jx)M5IPJkeC#h&aw?p4e{Gz5C^V)<P?Ae4J8Lvq3w>089Qr7;s}2Lr=IZ({TraiyO0WMPMThdr^rz!we%0M6^f#LVlp*cYOSskKa_3n`Yn|;j$M*bv#{BqQGexP1{|HmJP>U^!VdNFR*N5vE6I}m65evr!uc7jfEw{H-pd)>Q(j)fZa4G2T@?#@xIYf!1yWoQa?SSz^4ygC<JY6$&Sn@3R121<tDIO-VGZNo8ht@GTdmNixKJ}(JxqU(`+p?OqA^r**%TpbMin-44*xptIo%E4bRj_6~4ia*W^eet6;`|)pFpdsjrel@_l0Hc<$`gE1FiT0F>YSmg;qnY|-(1vIbOM1D)y|bw%Os@{oK&9wbmy1-9r~ESZE%I33{%fDYp|?&{+)(J-$G^J?s~lT*{$2jH|H%vU%A2#BkRbIZ)Wy%4tjzDh`31QBR_J8Cq=%mk}}L2Tp}YV#slH65QMq=2)N?-B<=C*aU4%H-6UtLN&eHI~={V=D?)m>J^7S(KP<x{Mz{@(KBdatLEW2?+hX>qL&(R47ta7lEdpl?6thJBw^7ft5L$cQ(az8;TR=k7VHncGM1B<)Y`>$#WF2fFgO00fKCh=K?FRb+um2!30_oCrr&MX5L1BP-oTLp{(IZkBMI8i(Z8$v06!w<5$t?5<^i=G5<N#$WiJKr9}EF^$iLyYjJ|Ljf1s~&!5nTGNQ1Xf&>Mkz*iLr^>K2WIm0sB%w;}K{RlFpqI{>kh4zo2c&;EC{Wi#U8b6VI(Oz%E>=o{LuAeyY$s7q0rj8^!OX{l<CIcub^64NOt_Rb9ibRN@+E_xvJ0n89cC}iqE>>#`Kfxjkt1BUp1vUhumf?FL1Uk<RMGa80GJz{!JY?;oVK<c$yO>jH1jVx|q@l7+j_bE0wkgGHHX6o4)3dIJ5)JV(85js6*?K;53_A)G#zn^4$6J3FDh$5iw2Ub*SvX<U<y8a-c$a)Z)6OpWGavW)_(YQx8MmRleqB}`Ai^j}YYe*3&q^4HQJo)+O9V{RVtU9}RlTlIDHzvp7_Qk;X{_kS&M2=v27?+TP}!+ewQ(IRXaq<%BB)-}N@5TA$Z;D`3>LR{?>#jdwpCgs7HlA<(o$*bBTDVxI|vGk60;SmiTET$-duLV>#U#inb(<-5kD+!Py3?nO%Teraci`_+1=QNzufm-@%wIWeOFk2d<&l4M?wqsn-rukvKF^bKGQX-#6wVGtcHprOv{O1O9=T`qzb<59)pNGWQRii7=$=1DaiSQ*P<LA-j<S3>c>%Cp6byiM9dU%&a{fgl$t!SLn}b?jNBvt&|*J<#hOkRO8lK3hnB}Tx_58MB2qt%-Y0*f;p|_1#94^8h^bdJcH6B5uxeRp`g2)il}W5rV4ly!HI_swA<g~NuA0egA(>gptkM1IN%yO#-Hom8#!mOuo$enFy3c<H0>HvL&o9=|Mp;3g7O|<gcsuk)-VWi?L9roXOZ((jZfU%%R}w3S`{Z+aObohD`1nkg#w^cYp-CxO!>vz~BaBL&g*#oSLwF4^#@QG~=BliaM3&bR+FxkJ(vot=%sp3IQX2lLW*+^ZDq{+7+XrbF;J=}su&~UDM^<q#E|@sszv=t7+W-ZWIp-01rE}r%8tg#V2N66^n0@d&E_BZr&8n5s_;5rHizLYH;7w7pLl6+hps?+$9Mc=nH~NbdANa`7_!5B^kO4F)vbaH@a0ad<C6yw>R0zu@zMAvHp2|_*SA{Swglx_b3amg`HgR;aNhjSS%{&?K+3fX9tp7^bip#*m^s$g`^0kGSOq*sjL~e*$%&}t)c&GrV0=<T9cz&@c>)=Iq;I(}tG6R4bmSsGs*JRyA;6rQDvoV1}RJM$KMYapeW`tLkC+S@zme-Nl9c#htjvt89k3}NuDYf#l#q-Z*(=b>DWMW+EZrwUNF{?5Q%7d7z3FcFX_-xB~eBa3|G=A?Oo?wQ@cW7yjRJ?$3gp=HJenlA5CDacB;IV{;Uf3^Qot{1>_I_IGm9h!GUipl?8T?v$5XX6sMuYTbn!R(-#hy#j&wMmg4-BnRN0mT9Gs3Q|(Y9=Zd`iB~J0N!d7L>T2Z&=Hw<M#5k$PQdHSds2vUT!z-GH;84nBh`SBtXmnzIuY{w%}LHsW#V#6*#Z#Em_-wt!&tIEL*Fw(pSei6dKcd&o*Yra1aw;DM^F80m=4r1-gW*vhde!GhDXJh~AbJL8fU6Ghi;avBbuc)dty?R>wk1*r_NhJX<GenT|UEG)XFh=j~T`_rPLfMd?tdLKK-In{(J|H~-HZKI9DS^6`)Hcx+BL@07Fou2NdBJ2$*QzN10Xiww(iqhT*?(R<SS3O0je&L+^{iegNSnQ=YZL9XS(m&H=#Eivt~AUW_&Uia?4EYvd668kDvI=MTkAu5t%N4uVvAIHDZ*j^jpf@pX`2i1WPamA}c7T4H4!>O9is&uwPcFl82td!LMKKdeaBU;oi?hs9~|9##I?#h1x<Jdbuo9XD;%uC-$8kQ4SZAY3lt#%NsKy2uhG22UaXRwzmiK&7G7qpKWJs{g;v!~n7WxAcwlAHG=wPyMxiPG03)>+mgNp9!x%CY1kyO8FRJ47lWyJOjY#9mE*u9zXduX>g?zvZv2r-A^gO^A3mpv`vNB_;BdiJ95=#Fsv%g9HJ<5vC{B?{XL;$*+rysgLlNK{JM-3BLx?RQB5w&=8yG`u_lH9ovT'),'Libraries/Compiler/rewriters.☾':strd('c%0olYjYD<mf!gmolo7@C|i=4B;XqF4l$lAH3TRiwX@~8y4rHvs3J?MmQ2K#se#PI<N*oT5ED#*up}hTB$F)3CYuLUx!?CMY!$yCKVi<fufDHtwM;ToH7<mt?t9NY@7KMpi2jMbe*EOWM{$gw4nKeV*ojkd9EF`^b#W;fgtcI$(_2hBgNW3EFeLClAA0c6q34bqd-mXwlkx14xr0Yx5`*=-IUK1b!Dn{)*m3wg|72rf&z_}pImptNv-U8JmwOpbyGpOn@5uC?0RC3eVKN+Mk$ji8Vfp1@)(=S(wtB1m_|b(w0(KnFKn|J?Jktj05N5Sz=AS=yh+qGReh+xvp<DFa3_TBT*GU9lH|TZx1ABj8yx&uB=IaYJwak1&|I*aI>{|$WS->V=A^CN(0AEgJYbnv_7z|g3e>XZ9MjE1Z4N-$Kb@?MP`GY8Yw7n4$gXA$(axt%D{dlqS(!iE6VsnXJ52j~=NKihSc6ku_lmK`T%*+HKzzu_>yX0_+NlFbv9>d3if#z5M8J|v*B{5#22AutrZfGK5->o&69E0|9Fk+Y3x3n`zty%V(BVwTg{|Ev0A)9_vYy$x82K|_;(BQ?jX1#s@83OD-+UurL2nYn_5ZeO4zbqZDW!*AGd*Qj?$FnEq4xXBeqVQSJ(um%spU^8Pw|NwGI2FnTK}Rm!$07cKnu-f<G8K3bg+D%g^!3({cVNI2zePB(4;dJyCpakN{ztn8(?X7eeib0$#eV}=MRtMBi)(4Up8R+R-uKs+%8}w@UBm<mQ@ca~RA(GJP`iqjm6X$0=&N*xJ8eRImej&Kd!l}l4dYg?JJih)fPP0m0n2`s-cyzdHu^KF1P(;-oCLNS4=^_BBf^}`dHOE>E@CL3Y9JWq2G7&W^qO*lxG;%?P2HngQTWr%cRq#JXYl%Oczp}6hd<riItQ;;0D<{uYQg?m&}hP|4zGQ+-~hZexDlf5tS0?<&`(?Kq!W#DS2v^Z5iadi6LC^(K1a9dbs%9ic_|%cNp}!3*L)Eqr6YIi6L|dvUV!8+K=RgK;q^JZzJM1XeCq+czSM|-`|rU0cfLS^fPk>xXzu&fQ%^s$|3I?X0)!dQ_GkvqeYo)DAL;?&ZF)Z{jU{0qTpIIaK+_hzt9g6EZ??MuP_iW*o_{^@zFBEq&OH$G{D=h_G599^is>XD+;}?I>JfTW<Z>q&roib_O+xgzq@*bmkHIi=qY_+<hiCig03|6sY`WSXp2hLp%d#;qzEH2%m+J?Tr?iXh)xP#^u(p_g>l)vNgR_HpWlj2RIo!Sk@T^M+rs28Pw63LtR?-JH5N|?N^zKQt5E$xy+&Z0PzAQyIj=ed6obNd>#oS4fo#71P5PEYbFG2;%J_RE-AuIYOVoLml9om_KoufONE*1oTCkaTI*F6<7C*@5Mo?t0L#-ld74DTP)+a!<uOj~UdM-%3S%8}dDb$i1q_!~Kro8xHw9#vrUh#2%$mf&s(98a8u`gjj?o_<X~MV+`#*Nx?_Ob2`U2aHSr*iWeGZn|r$i>d2zc43m;bOoUm>i)Zy!@V1Y5eaL7Q4ZWKB>q#n1B?9lS!fzDn{}t0WfJKZj-NbyXztLl|2TT`KaU<daqRgyM8DHU^p%gWoU=w?zc&yB@<sJ~oQ-fx*y{~?L!nV8?#MVD^(W_)QSnt}+b6K-qc>kM=PT9~tu>|9T?MK$OtWs1oppj$dk~NMS)2@et488hW=PVQM`48$Bkc8O!wKq%NcIvm8AllIuhH*VKo#wQIzi3=?Gb&8-m>ltI_*{(HRQ4^pIeY!ghO*jq6Q(rE43&jAce-mR#r~n82exP<41qF8M3VME`6Q;uNVtutwxWYLJ5jIv;qm7PM4OP%G-}gCBnGFV8AK}SEoNG7zSx1qWJWf<nRZE^IFu;plu$~B!~Fu>MYW;PZ=M!EHk(R@dDu*{2&Wx7r?ZC9u<v-dTmfuQ3(s&m|cS~P+@;=-SnwugVP;*iEdUV8hqk6^i|zSvBe0nM<9ug5u)Bj?p1JI4KquT_sl-dPdDG)4z;Cl+-3R!bCZY#bINKWcEUhL?sBY}DfReFiFYEWTXyYEXq6umngvP>#NbIwhrGQ6+CT(ZES>x#T_>vP)?4ex!z2SPxi!vG&#d#u^|qkQya2D)LQi@K0yi1|FOusK1m203!9XqNO8ph}{kyE9;M6w>Ybi(339mlSy2|WVQ7-1sjEdcCjO<aKBw1P-K&CgX8}zJcin;pCdbD)bWYTIY=~$+We{%E*7@G9^X?F=EJT+^0d;CMKtT<bCl(;U$*=g+OPt6h&ph6QV@1zM9Dn@{T3V*;{5nBDUcdoJQh|hlcbi0#sOZ!Z7!DkGnv%4_4-$Q?1C&U-o&lvjn_QTMR#H^0QnH*BuDTH--y$UR5l(&U(UKQ^f;{6sZWvvA^1{bRW-mr?OyqL1Br>K*|`-D2jJZ60PuI$h7;Zd;+Y<j>rC!j}qvmKS|maL>LWUDo^J0V8)nFSrwMVRFTyM)%8e>(x62f2ka$Iz7b;d4X#T-Tk&K5!QM7K}cc474IW=YBTrq^oJy<7jzLQ*@H<L0FKLv8rA?eTexnswQN&FizI%hOA3RYtDhsndd_mlpd7iUz4^d0Q6P*=ja#NSQzCkbWq4nn-z*vTnxNYSAFy<Q3;b^UWf8FdzCr76MA`_x8e-98}9Y?<!eRp$7p%$$!(<?+#@Oj8(&52a4xqk(YjGr^56*bu42A|mi@gpV%q1&J(Z{@80Hz0*bdnWMZ)&IUNBo#P{|sekfCQ`+mQpjDrCG~0(rybOGUt#4wZ6+7d~v2b>ST@@CF3QndRjb+l2U>&4KsG#Y`mTzfHgy07{3uXOd2PDG-h>z#eX}+*^YL2h^QwRRCJ`L^#%4<jOVqcK56Fa<1(n?baJD1shy$X~{L#-l@*grL|TXL*D&Y+mnN&^aiR{E*7=xtg0H{5OC;jz8b}wR;J8rpoHv}!69^!<?5D2nqhJZr>@cVVR@-YRl7V@op7(4brtmN*57;eHx_2B%ulF1iMl95e}W;49I%NY&oXeZO}v@XVvo4pT}$^A0#hkVchZc4gZQP=3P^O~)@ncQ^>NRo-F5N`RD&Z-4Or2~`FMw!^EE)rPy$q2KHwh9L(t;y7i1nvY^<0$52?yma?9<Fyxc=U{@=HusEt`h^F957L`Mj*#OH`0%F@mmUri|NsVqlvl&;JOefmf804?~z2w=LS^$BpBYsH77YDS1u+wDZyD38R33R0cpq>gsr-{g%g{3~p3IYMXb;p?kLgj+clwUG>~C`eLrt1!(`H<yVw-k1>by|Q_}Sys^VukQI-vIREV9;U0iw%Kt^8!OQ&fv?r)JD=bOLRQt8GE}xF#^>r$P^j>I1c0V%&Dho|u0BC)RqLQBM1MUK?DJ+ZW&6FzC%tu-yWMrrBEPJivozz|S-g$Z^R|)BRBa;}81{6n7tT3XCxmOQron6i%%%pDH?kn-iRR56DE58@xGX8`Y2|cYOq?;UvZ>c1-%UhfsvsgvvM_y{z6qrYADb^J{3XGD%z~2A6pNv66fPmkG%?K6Jsp1l(hKyyvkz)7IZiQaL2G7~ltEEz+~W?#caV}i9)x#7^Kgr4=gDBj%^J#*au{E@N4itQ&84*4TS_5Ku?CcE5pUrR>1&(D&N9)9E~Cu#>tx|Z|8gfmF;#T~*tcK>4w-yzUd3<-Bw9*<?~;tFjRJYT2>H*t_2K}J`p$BfQK+9SP^l_pXME>I9iIh8a(lT7qWd$w5{2TBQc~X!sHQU|r{xaMXwy~OCjzP77_-Lz|Ig&GRUGMS>d5NaKXIGCCL;VLy3N$;65Zn9sx%ce&W;2_xxAd7jDH_9M@sJhm*Qo9t=^FkQK+=WKgpW5(gWmpv0WGL0GJ-|Z10A@ckW#sz*bw?V8!m2v%Bn3Tb<u5J#;18mjj-|N$0Xj-=mwgfSnTje1<LgHJFFCc=dE(^J}(A9=R^XUp4C$fbYnZy%P!W(XlDFc#&bQ+~QR;zL~Pvpl?P~^bJ_~JVM`~Z|UV}Zk1=JL2b`^ly$_nZy*nA^Q>_cJn5uqu1;G6$ONJWa!WOfji`;WGLgFT-1Er>W)ArkmJ#!9V>TG2hu2X{ENc|cC}@{>;l^0OA&Lc`#0NTh404Ze6RYdUF%!mKkUY@~$SUj+t>J6%x>T^|B)O1xI*Rrt%S<-}{QNiopTVPR`|7Y70rHxKcN(Q$=I8AsCWAqHMK%<%nOIz*u*7BJhSgrJ#erukUfbjm@|m=LKz&Nor^QFFT~%LF^{J&kElqav1etn66aa2lHexQ}ytOw9GxR-nPgyjtMFr#e9Nx#_Kr4}}c7Jjh#$!PX@~q4yy6!(rf@<(!lF|vy%|sD+9@-~7U_DP?Mc37J?v9;ShzZ2@%uW!ro$rp?K-VI%1jMPeY;o+G-mqV3U6uhzn0X3dV_}>Jb9v|Ct%;&cZq3jpDp$2UTidWOE51whjAmarVOnZUouYLtw$<yO<sE-5luC~96Sp<lr))BP#FD!wbS#Qq&XRtSX1YpSs+sO?v<{s`anp7$(y#DlUol;HQL+Cko?Ox9v<GpPF2`)@4vqp&RcDpCt*?1Eyvk?Q++vA26x9}G{`}jJSO=vx>BqkFq+(a;OK-<Y){;ia;Z&6VeVp6!i4YE7e^$w}5=Z?o{$HY6RP5`?%lanzee3+h`%<^~pT&!v0$#jD&y{k56-NG=Iwu%_K(PKp6>?qNF46atQL@AevTV~4Xs)%~^^Xa2wr#U)$cR+D`J?F>m;-BMW}$v6TNY-_t?_ycKVHi}UebGc<2MI~GyY7+-SunvM&@1OJk_+baVI%bJ4gOb2U8kx^lG~nm?_nG`RD=J<-3Tl2BROSjL2{)W3{jDXw*ge4b!M|^r1pocJiE|4}|iuE}tg~`G_l5s-J<l?MPKkj2s>znXM@~;ANKD7D?KW_<OR!Y#eezYIilaRA-8BeoT~6v1Y58r?Yy*IgiNsk3pi4>l0Fq?LErRr#5Wnar_=CrPx-0#0(wh_oM(y;w>gJS+gVJC+<duMnWD64xRVyX&E~74Up094$=%gMqTAh6CA2kU>-*YR8c2%@E@c<$kQp?E$J#H>;uL<j)-~rSfq%u*szphuPO(O(GUbNOh!#WT(1{AK`jl<K<VKtkib)3pMu|W9fcRAB_nMT$vb9<Vg-`#<_}Ky@Ts+S)>><u#{?%UaElvMctWZ|CrWO7`G*>3xpnR)PsvXQn!9?|LT_9eB`VL_6K~4CIAI;>IfCPyPR}VSIkQ!ACZ7kpMDEGFE>)&@m!>uj=3>Fl*%;UxAu0EsyQ8Qa&+0TA6iq@>;qfT`BL&HD;60pCTuDZ!Rihb^x}m$pi;&fLrdHfdX01Wgs^0+OS}}gT;Gjb#bC%^T@gc@((o$X>8&4V=on}_!Jo>)2l8(kbh^jlI>bqmw-pks`C<Z^nGkg5f%dEzY-bdF8Cmj1|>j(GeF`O0E#w;s+FvWNJ1|>Bg`z-_g)Plh0*Q!A*`-Q+n?XX~>&o)aOBm;Cd?dBX<%#zk*ztEywsMLPrG2<xedR=Eaq3g_#1OBVsL*pyxM+vnajVL^Yq;bE#i+bk?01^N;fmfK+!olz**-vA|>)Q`Q{V=pP5<607LyyZ~4_R?W*wKPBqBYSmj!Y#sZ$@L3Cw%sJIPW`PsiYn*keoWJi^t<oqt#0Hqc$v(vC8T{tEabph>ypsJ(LR9bjGMwE$F&VHXG{!T-A0=yQm@?&&x*_KEyK*^PYuuw!$I{#Cs~;a2?(U5~%lK3iVJ$m_LqSoO`$YW*_pnius#BsJ)7F9{&MVaKS4BuZqJ8zUMciGf8GoXz~X;=e!Sg?yLSNGAAll)>6XPIHo_ypOgbGz)U?kxB_YNSk>RlXtx?CQI4BDgn_?XhQ3U&59!Yj%JH9{!~1jmngM``1?E?Ky0+}}EUqA<2Brs3u=GGZiF1!`M!A6Hk2}c=4ej$7#>(<b%d>7vR{ob5^$}<Pb91L+{GGlSa-gFJpPvIkkjFg<Su2UfLCAj<$c^$%jrCpz)PE5MocskCK)8N6*{ack63MkNmy%<41&?T%wF|59@}E~4V|4D1Glphbew)~qSRl2Ay}1xh>3GOzpN(I)b56JMb6@%9O=F=*MM{rU2l~omrJvg&KX)yJ<}XiJoX&q*h4QAMtQcGSQdOOlxchV@-2KD>NXRUn`#n0#la{!+qbxh6DYVTYp36cp!gE$ywL;YCyT1WV3me@'),'Libraries/Compiler/lambdas.☾':strd('c%02z>u(cB5dY3!aeP2~mpGE`5LF;qDz837Ac#l5gvj#aTr5lyogE&nDv`9%6a+XVf$#`~B9MR*QCd)1LHl9<lH@PoPw33PZg;(Y)NyDnCAW7sJM){_nc11Oefk5va^%<-em0AvFAp6VIeI*s^+|YsG9n4@>&iqvSE>3z!XqSr|D0~m{{5d1kL=wud@Q?f_`sgSFoQ8VcmOHYBp9>DBS&C7I*=OMwyhYJJbHsZ%jSy3?Ag;eZIRxj?|||Vouf}P<iqm98WFdz@OE*A1iQC+@F|x(^3_4&mB+oW!&<IZi?sP9lw|mc!rD|c?#b8exi6JfvqqC+3GdLzetfV@-_om0?h>8OqyxWSQKiNL)CJ}}qPOVJ-tLSi)lCM#1K+`e1t5QKy~L^93i}TX`>6n*a4?0b2x-6VqthVqwO`4d$rp1TouR9Aez#}e^D7z=&A{)_5HPw&pZm;gC#TZM<SuS8FRWBUkD+=`UkAQ27@G;^s=;~&LZjfjKpB|X-y5H(A$J6s8!w8*Ve*8Yv8g3zC4sR72?c^~lbf6j$BP6+U8Ya6#jucN%&z*v?u+ypeXs1!;QhjIfk5^c@dY|QP|u0)RWI=^c7X4djZb-)+dXAG00H{3c6&UU3gNaIPh$?0mLxDvY2&2sRD<ADgWRcXuV>*l8HJ^Z=uEDbJ$I^HJsn0>1uKp#8}Mj)jQfa}$#`Vr{yd2ds<c#WVnx#0xS0W$=pAOj>-2Z@+qtV7m*+Pw&k1`-@d39-xfY)3+8%xZL#$ynOyv;4hvoWP!aPaRa)8%GILm1~*x6Jg_U3*B1$g*XE9C;Nb<otbsj-*^S)aSOUVn4)L^7EyeG=w(sZma|IB+S%cYF;V0k`j&dSVDfx{m{Rmfj3Kg{67SJf>IZpD}3=G#EfgP$ZiA$dRimG7X~<T1(6ZL(b2{w0`?Ou@#ff#mF^xN@`<=_b?Ber_Wl%?Tf%C8xJ3l*w2EX7jA~1u+q3lj?AMhz>`mTyc$Me3_sZ|d<{S~Y$M)q|DFPHx%r^!=9kvzW|ean)hO(Nn-8Qq_w#{Ndq)QvMz>j4H*x(NUmr;I$k~_wYiH*+u(#T-z;Dvkdm-Jq!M535<5ixff1@LcU4v)-_4>{A`Ypb7xOM?G%BxWUsfS8Dq}J<8>-Brqd@a1xs3b>)B-?3c=o9)B!OYQHK7VkJUJ`|Ft>P?lYf;DLt)oWp{Yu_lJ7W>`M<Z+bYQcJymamrRMeEfddllJocDBXI-C>%((43*alE*fHp-XsHL0+qj^5IzEO+*mh_1}nSCM+(I-~wnHxkNUXHKO$zwo#JJHE*#L$mt!D8+r51DA}lAJicciVKFi>c>!X>E@b&!y>P7&Gc_T|ey;1q9+a>xBoFJ7jcOk2>tWn!N}fOjdk*+;U!O-;Mbe(3cj-Gn*jk83TS7dlAmZ{N#OUKgJgh@(K?hy>i_S@>d)v+Ym$PL-BRpw)hR3$6|7ozqu`OuoVvpfa);fc7WXquFR*~KJzlOJW3*hnHY*AEl^Ymx>7rQ=g-HJBEX-#iM8+v;#q-jdj4qAY$vGE@<f(nYd+q3ZZ6A@<#?^yP?EwNM6e$cQ4-x4~voV8C3f%S&0oY78$(}o5~%_}m}D_A~DnfaI(JU1OhPF_q%C%mNQ?it}vCO45fSw~S{a+EwJ$!&`hsj=#8E8S5g-i~<dj@x@)<U#iD^H>7~8zw6-;oi4Yk`)~=?<xL9P|h=lgl*y`O&hOK%I-3;+(nsa2bIwP=?BIb&<{mm&x`AdxGuCV>KV-)nG`G@Pnz(2>Nh!|?WB#6r>(q<#RFI0N}x`k;BLP?Bg-mgJ<cNG8R=>P!V`Q1Dz{pOoM+1dDP_J+`1LO7Mau_)hv%&<U%v4hdMzzYz<<aNj&pcMBUjyc$a|=kXOwKxr;an#QZxyg+b8F)qi%kTIlE*Y@`*!r>zGU=Wb>53p|zUI6=#XvJ{rWdz?(B1!8+?V%f=gAeBf|+VmwTEY)52zqjj=&PuaZ1!c*+#P1eiiP1b5-ljV+CM_PF)e03hA^QgHdu0P1DaNyPUl%oB)K_9yHxItGsO)t)EO|2kU%JABrc3t=ZC-{S2_Ic^d-zU7!a<Dle8QafLOZiQW_@azG7noVtF-YPI9fK8f5`@4!wT+yW4&-32X(dNL@oFK=XbuBQuC|Rgmt>yq$b10{rXz@r!}L#K_;Sw9>5lxtGiM<)%6)-*=vZJ`%n}>dIw@{<&3Ky;{89;i=oaiN_snFpeUg{p%Dmb;xqEP!v7Paxfms>{)^om+f+;{zqZRj>=wGll7$}V#<7zH#AAibRB@Q?-KdX~XpY6Jj6Rcdp?F>p55{z=@W3XH51eX}W+$<*maTu}4-aMt%;)x+s`e|z@UaWMxmVK-sn4!<<N?Z=0AdxDArX(wZWHqoNZA(K<CXe<qn6(@dRHV51yZy$s<YeCoet?1t=kTbw*ED%{mW{fDZ%XP;gH2;(-q~xM3aCtcT>uuqKCWS9zBF9~f5EXv*L-<gE4Q=%k9R}VH~NOC5jZAU3!jUiUe97(+wg5dvwGB39oJZSOk_z7P^=<b=%LY~%<QS`WE5gri;t@X*WF&bUqyV(2J08C!HR#;!+zGnf6p`Plk*q8Id^udR>fa40r7A28h+I|kb(_FFkYY!u#Ex?_vx=0#%K-9jYl(gU-OnXS=d#Qqg+aj2GwXtjXqJMU22q9qoNuqe)$w2>o@TSfvHi`bt<2ktdt97=Sp?C7{clXAh&$9Xxy0#ntuQ|H!y$'),'Libraries/Compiler/expr.☾':strd('c%0=LTW=KC`JG>JUeKH|6Ul3*7hGAYF|>`k!IlkAD{Hl^$7IE1cRM?7$Xl?88>az`*QPE7V}c=}(2Ay5g_I;x&o9Y7_KBa+?>o0SXXea$*U+dHE7`L<=bZ0;pP}qB`*e2xSF~EiZ|}T2J2Q8tTBTkRhha6jn0Ns>AGOZaq7L-~;(0#&7kj5pp8REb=EPKazB*k#HFX+JabUkbg*){j_|9+7%)<A|Tcw2~M;5~+vKTg7i($3Z#zR|dgT3%4ju7}zMUlQA5K1F5F-a8oQNJ>}fVW$jyCr@%&fFbaP(++ORi-5$_eoTD*$wsrx6jO0&rF>tpQ@Y>lUkC*v;`=D-^BA5{0v=}*f#r$Mz#0PE!GHIVSi=a2~u#EUrA$$D7fN|fJ`PQiTCpM&08J`qfSVGoU809wYO?I0x}}+bfQK*q@{qIZZ$)o&zD=_OC<_O%=x8)yXQ{9!O}MSC@;MtIi;+B$G#p;0+-n)`-Xirs0<32&$AeyxUR4-1+Qf%n{$J6s4ao5v(MOzR0(_mh^V*P9|9f17?xTwNl2qf%ED;z0}Ljdo8F!KUV7UWAcv-00&aL^&-j&Jp6$Op-+%dpxr`FL37o;LUw~(Z0XY*dhw=xPVn^{TCH7Nw8ovL;_^#xe-Tz}_&yVc=CD;D9jXmS`{xR47F=J23-al?>_Bd$v_<~kJ7^S*d`}(!%X6^@6oo$qcab9Kn74Q3}S3GnSPO!4nfDEnh(x@TT;{#~CkA*lj-p4|m8t-Ev<3n1=+qUm>=a=5Ey?M^*&3l7e%nxZ2TDgW+-#Bmn=l`WQYt;?t*K@XC52)}r)SELl^8Nm;jE!K`<l6b~Tf3Q^X3e7N08pj9=>W5{R4<e@45tQ{<37qMhZ~5bX-T6D0yKsz3UQ7NuxDRZovJ!_vI~YSwplpP0ue=C5(h|Q)^>!!{E1_GC851Wk#mD_iIYGUafxpzYbg&XA3IvDK&P~w*D(i{yE}(f?Ei{1-vD#zgn0`9jXh_pG8`Bk$QtiJK4u#fdZIsk0)K1JfWJF)5__&k>>J+nY_m&~%~nE0f9F%#HhQggwfC%BjXdlW#aciz?HC7zjrBtV7+-wk>%NT1&Kn#Y6NMiT14Y!pnLuVsKN_LY%+VN28gXq18XxzgF`VQFSJ-uSLm%TEGWF@m$oW*E{2+Kjh*mQ*Da}c?cHrIKzn*%Ta!}iz<xXn?h-ry%H2)KfsgZ>5AKIAWFj<b9Lg8y-e$uYRiS}uJ-3-WLc821rEN-N{do%cdRF4a;vB%Cnx-n=U4Z>T*T>4fi6&+UBjes;!qM)5FyC$gE^yMG}btGmP0UY!fayb|cNho#;33+F}3hAopJ0fen)l3@A<uD5Y4sWt&rWAnHT!iEp<h&sd`&=B>E*#M*fb&^0EreSf`<7o<`1J;R#wEAH{>*ms*yr>-p}(A7w?IC4uMvgBO>Z8AJ-E>l;$%8O;E)fKA*D3WvrLrv1*nrqt+_}jGM8JOM^T9lMZ{!_=iZlpSH*L|!CAG!aW-7?!;b;j!7ae4wcBBH(er5z1LAhVOpR$MOzl=1(D(yn7#l%;j}8$Hvyjj(PL7e1!}ATVAM>%w&xEJnvFB6;qXt*BjLA1;n8KJmh8*x9RtF-Juv)K0ksZsP2P$)@fToT8;E1N<c#)-ey}x|kTixjG+%@X`l!-1|rz(LC0BX0ly54*IabHl#NncRBo4vo52U3&_x7i<gRz(aML_wAbKak}`DppO6<!y>0aJoxo;hN?XIa6+Qh|KO?w#x0Z%dW`lWp!1^2HP!@&^30)J+Z#Vb_dNuoaD2(n^tVTMNfn{(Cs-)-rUG->9W3S9Flug_bz2<yOu=jl=i?H{aniA9=~qj#9bQs$XTZ@xidi&iaz8IR7_9Wk=MO!X^<}<c6j>bYKYv=TcYfvm4hD{<k9Q}L}H2ESmJ@PfL`Lr5WWBiC_7;_yx5N6hM#$QGf+j8s#q3ATe33GS>;{um<L0UD<5@;+zC)q;thHLq%*7V6FLhBP^f)8juy~aURr8gq?W!VUU4r?b|OpuDXkvF23|^M^E2#|iJKoEYS<voo;YyWAoleiHu%{DZK)8<%4;+`VGQAvjt1rfM$4yY-}b`mt$#E<b;i?PV^(Np8NMgX3Pe7}Jzn)Nd~L!}@(Bus>L8J3lwxnxkG*(aNNO=GSL63Oo-+dB04Qf8s+@{qaW(x!@_}A{j8qDeaF;!zBXBzXfzBk_HZV{iFpgCOv~?*6nAZfn8sg%Fp=p6Hs0U^EK$`6d{m4{i?UIj(ihW7#pZpFXw$sYZax0L59?9bQU>8KS=N%5>V?X!$uSlR+f5gSV<WfBk7g?`J&GK8WvND{&ih`ys9^Mi7<)LKb0fdaldt#)P>ewXAk*J0gaS_UcZH(a~^1tzOa8-jdv1E*(KvZX&wR6xECM{7%kXAd4YY7<J(ar>kqRFG3pMm)JB^JM8{N<6OL=ziD@D~I2h*RL}Nrg(stl(7-S^=6XBWl@ve_^L6?_%T}Fz@Pq7ejMeE!53+A|Ihm<%t|w_X~O`U3%4XRoCm~M8u73FK6+vW0nqetMXLVqD@Yjsc6QQ;~1Ifm}=t3f9{x_EhRB8LVBNUdun*YBZ;m?s#$dlk*%`(R>G7+zdrAVT)$WCw8OfWZQ{-MLqr3`y~4oNWmkv7b>V~R%iCKUHjv-5C+w~Z41!m$rHFn4cvFP&awUZ_%{A<NL#Cq0kP$ou;-_s$m+eXKe@KsM-hHgt#VJmu>)b7Q?hAR{me*a{4{XXsKt=@ylUoU25)LP*!$j)Vc*~5>YIbXBPY=8coNU?{REWXhSU|?i;cJn6Z9ZMvHw1Z)eTog2WE5w7Io$%khmvpsW>fAcN`|jYZL%*+IaS6mt8m)X)0<bCC`*m-wj5i}{i2t;v>kx_eP;$!ROY7zj@i$+PjyJV&i0F&swd7@`<(q&;ro5~!Ko@l<qOzyO&31hts8cTa`o~9HLE{+;s~;7d<MW55Y*@aP#z2frId$4Ein5g7;b712&5TvG~8l}F&ES`#ZNs=Y5nH6wfG=u?HBNQ*pT2j#QnnquRsiwx<PV|<hCTMU3tBuuGC}SPM@9gWL@<c6$RD4@c``Q?e%|ns?vIr)?EI70DvuwJ^'),'Libraries/Compiler/tree_txt.☾':strd('c$|$@TWb?R6n@XIn75g&D>U{k5Ft%M4W>=$1%xy#n`Y83-E6|{1RunQUJxl(p%)RWVv$<0Qk05_*r)SP{3V__JDapgs@;cVcII5Z^PTU^3fO|}+4+0IarCM*JzJSua2&x^C?&Vqir=ogek3fLac<#nY?mt(rplGcTzTHfmy5X>^q@fZi`ug1glpQa%;LIwJ6%hq8nVek`7rd9bRrcxUeJ(%(%uKK3%{*Qis9om8Siiwv=#FLwj!0QRM;~@ERq{b{e)6=!+<5nv@epvMB+U<imek_)$y9mZe*CQv0E&yD-)vQvrLvHg^%kfdLNG9C43z?O4kxL3dOR(0JuXyo9&RH$8&gnO{usQaZ7N`mWsM{XQit*`sMda^}Rqwef$)aO5=)}SFOds@#Gb(j|9JZQ``x54^KDX4E8j9T<yUN6aNxKf?3j`huc9Y2bzH#dzN*@J+WU!Be&C$K?6xiGB+9aBAaC;CjCenK-I|imZi2ihi78CQV_5Xr*L7j7++Rbm0z3_B5h;pM~|tJ130Ju3)r;TOgoU475i?%KD>i{JY0u2@GVO%`iYV?C~W4tt$M>X*)s_(M#P*gDP5t7bpSgQ%OLpx+wjW-vWRgKk!2v%u5w|NSF(mR&}(`!d$`9banE7{QJ)cyO99Cu>WhxrekZZUb^6kJ{IV1#Pzn>V6b9#yhTLs5oVwp$UW*2YTSUqY6^S8X%ot=w=^w%C)}sDfiZeH83>oz#PIh&F%~_Q$%EK}@!4o(pRd2vCd=!gQ51jm5F}F|@f=_Ziu<zju>}r#$rj3vBn07qkf1ZBQCZi2`ujlzpJjCCH&X4<f0yP#ZPUMXi(@8&(M?^)_h$&8VaAJk7S-Ve6BBd>O3qRmwczTTV`qN`w6XO4#`fj^RG#$dO(67V=$x*;20zQqu0!E)ZaAYVR(Y2-uJMpd6!rQ7p8~^Gw>JVL)vznT|XfWAA*p*gFG=21t0e&}J)xxhvbYl%^PYitxB|R#%gyLK55I)D)socNg%CN2'),'Libraries/Compiler/tree.☾':strd('c$|e)O>fgc5WVMDEGO?)MoQ9KL=J(34-uM(_7+*IwB8g;#*XZb6d$P&hawfxf>aPfs!*>SKyW|^4)e#D9eZsjBw#7=cy?y??VC5t;W?a+_wREljrHKsc=Y%{O729lucXfADs^0T9L9&!Fy+E!jwA3tkM8yR_lBd}z2UyRGaU5xFptVT9GJ*532kzZ#%ND&w!B8eS2N>#3+M1t2B~}!YnkfBY{sn@b6&u;%XZ)jUc*b#X)t^OOnU~G@SW$Y`0)YW6^k|iSJ;g%J63wCbyBP7Xr~rxo<!+I5|K-Ve-*!i3;4QPJc>1KP*(j<!ObA3Ob}6}D!-PSn+#46&Noh|zVLAR^w6Ig=V!R+Y~znsE8awfR1iDlMsTTO2gyP;xIfiO+91~HGP{u}@d`e6nBBOD>1;aHEQowZ*wp1VcuUuo75J<Q0e<1iIsC4b#qg|Z{T4E@*V&}$Z6tCQCoFJT&bCRrhD!q?o1|fIq<G6^dvT<Mx2B;_a0)*v>e#I=3mDe25O|$1Yfl1CRG9QuWfa{d`iTLZWO5$Q@t4*PH&5ba)-~{4OgZY_#c5InPLgQ7S*0pY;0-Fcq^gjEqZ|Wm?ikkd0>$93lWLAnJF_4qZgQ=Vi~5|T*v!Dki$M?yGvAzt1rap;O@aL|?qto|^6YKU9}Ia*7?164Xg6GMWXbQpf#-*`mkkD((^g-6$0pc!Sf{1XL(X<vc&O9$_+&$TyVMW*(+UwCxNWybyH&HBbrN=wgx!(^b1`7Aw`v(D<P6@IYBtkYhOVfH;zVNui+=#;BSJp'),'Libraries/Compiler/node_types.☾':strd('c$}?RTTdHD6n^Jd?Ay+!t_nz1DocLg)~2e15eZTxf>w*YCRTmxdTA|Hl>&u8Q-}x))I^}fxKI!XsZ~{_5eW}R>P!Cxf1vz?p1G~p>)DM(iv+Xmob%0hE;HxM=ABAO%g>jyZlzMJX@yd?;<#GY%09CD2rR+ViF<d5Y0{_9?@nYU@0%vktM=Sn(H{J0&ap}+Q`8gMT(L516>G#uXu59TU#6XzAcish;lNBZnrqixGhcB^miu2|Dpk|9W{b88gUb$$j((QT3=gI6nIq}3p>fn=U|)<;Nnc5^X1-9@k}3Ln3r=8(=>Pn=jqB)tZy<bMU(U{Jun51vOL7aE@Em?jXtk97u#7S_yPDE9d_aLSc#`@Q*RT`XEiSliB>Ob{nX_HXbsa+B2^`X;2u^RnF1$mv4Y-h_R>%t=%|;xJNwsj6jwfO~rY7j$I0e_%4a%LM%4;|$k{c|*9_$jNW*FKB{=Wv=LdhV+8e9;`iBdwmd~v?^NEafM1_R^t>5pT(^G;d3p6;iSYQj4F%B(3`rP-XN3GXDe;miY4bFJ)`j`Wy8R~IVGj%V<K`Fs%$;fTyu>IqGt;Hz`+l62gL<u*_D8ktV$Xg~9F7&Al%<GBr+aFJ*eW6Nz35lu=H9~WSqz?nfvPB7|N)(7cWm<60UeE}Nq8wqi*TDdG|yhf(^%Naz_C_)Y&uC^ZQG&VGe4AOQHPfoTVH%{yZo-fCIwHB4)|5HS&!~|ZznMh-n^!)~giO%8F4m=G_4a~@$Fglhd0|tE)SWnnfPiibyzZ3m>|9MOI7p_xnwUAk>+Sv|CpP>gQQ4Bqi-yR&@h-o{-f=XTY<KCv)CG{X66`*+<O>^V_q4#jAzrR0!+y3~Io_JoZ@AM?+!`@aK)`~XlRkvYsY9}-`sJ6L@d3zbyfsB@i>C6M`iSeZzi7rlMUG8L09FHBD6^j7xkOI#(51KsN1XQydiutHKUkatCQ21HEo<t~q^|j@6Yl=v#4+2G;JlNyQt&w&-1%0lDxb*1~R>)v5cuUd2yV>^cN*~<6z2zASKI>I*MV*R!(bjm;skqi_DtdUt^KiZrV@p}9BvH3i?cgau4x}<0H{nf3ZX~*KD%BChxtkfK8F314S!^4ykfIz%rX~p)NFd{Hzhi~E0e`Sk@)o|Ag&Tuk7YVT<7GE_K%#OsQH1jalyqfE%%xehc)1G`}*Ofln3o((PuVTTle<`WZ!YGGgY{rMrcFHO=FT|}kZ_(1PLX)Y~bs)u}m9kb*g%)|N#iCuUHW--lyiw#`xUFJI=eJXS&iOCc31|en5<&N6h^}<TRxDlmUS)h&`u2o|X{<!s71{?qh4*UpaU3OS=w2w=jVRFA3RNo>vh><=D;z6z1fioBLasYaY!&&%00p!{O&hP2ZU2H0EE}Y|TgEoracSGBn5k4FChRJ$$T9`!$!xUm1e#UO`B@|d@FqmfG<;e-TGI5;4JGVCmbJ9+Jqezdi#Rk4+4|~9o!3d(D)+Igi<z^trXcp7llgjo>vebe?!ed%V~BfP5M+B%-95+@Y=u(cFk;&r#ir<An~YV}!b^Bfm8>s9@U8cmKj&0sVN$sI98P^#*Lf|5j^^Yv(5*y+oCQDzW;y~EE~pVrR^|OHmtm8A5V(5nnMIlvb-s|$H;V-~bW@2Z9K>@tUYoC9gCqD}@Bg%lzdziJb#&(MGEYXE6sH|&RzkB=Olc9Lvg51J1H~W)$)qw9=KZ1J^w@N74a^ek<HlZzXkpHb8Rkg-1tqu#jzfq40os)GKRxiXrOr^F!?L0J3c;Iwg$gI2R_Urar0r1!6#b%b5&^YFy>kg~{9Y~6v`FZt5?UnH#-+}Tx$zSGJdXE6WTBI;6-srn7oLdubuli<ku~M4a1nicDxKE-?XxMSm{}9)p^>pWne^z`Bue}XH^6&1'),'Libraries/peggle2/gram_tools.☾':strd('c%0Q5+iu*(^<7^v2_SGr+623D+W>;MMH;)P(WVw`87LsD1b4+<5$2K$l1f%-TEwy}7k1p(j%~=TTSpG!CXnIu;s~)3w-19p^&#I7eM!$5&J2g#i>U4@MHYgVJTvDq=Q?L*Dc|H*7ta2a+BQC&dUN6QnMK>C*1s=V71H*@hU3SSRfuIV_%CLkUZ9LEy;57AqQkH|ju(uBAGLdSJM>#l5`|+CO59#zx5B97B&Epg@Za;NWWG+Q?{pd~4(V0M3_x%4Yw(ah-I*tEo<4yr@9@v~3!t*YxB107-+-@sjPlF;79E7g#8dz=#sse${L><@L$H|b5wAt~MF8y~KLj%3`mu|^`}`j50Y?{+Zt}a7(Z%{=wB{m{wwpLf648_yXafKiqm~Ow`t@%Zs-`D|41@@`_*WfMPz9VP=_05CFhe2*t4L|cyF^HGS;?qy*woaD+rq&oeAh%nW87!+Qv^O5j&fvDQG*IjGuR7k#avRsPvj<RQJ~ptv`zje{w2SXA)-1nGzmxc>C;kmIpev(Z}Tsyp;kcx^og$4wGLpf-B%OPN<b3IQDFko%HDwOpZVoCUSHIR!zEaXeXr@#UxWd8z#Ln~e=rnh9Ir0?>?EC2<l(tyJXe(zCr<vH9)ox}wmdaxIhiRRe}_y7!T%k!<y?iJIgi|ykaCX7mL!anxwdfZL%vtwFd;i*!W1HWoF-;uz=jx1>AU4cabm~biW@_6RJjj*`@{LvP4+S*0XB_<N~Y8o+_mB{X#hAXK*9YClhhbO)GB@A#lp@<<9BqX=x_e$w9z*|8s(Zt>zCVO`sL)5rfb6JI30!u322nok4}p_{5pU7|H;%^`I?-eZa0@3Z}9i|R|h4=X4qX%!|q5_6}DPH*9N9{`R93!-Q_RjT0s?HKjH;sut%B6>3?*+J}u<%r2kZx$*h#DLP}xOGK@*65cb@piF(j`MZNO8BAZ%+<y8NS|8sICK)fgD++|e6#<yL{(6o-o7!nL7@LD9BlWvpsm`15(D071;9WyD-<tZJ@QTi5bomsAo%_A4vHoF_fUgCv8Tr~IRI!EE#gIs%}N;G180!2dfQjkM*A5~?#V83zhOdhY2e&3px@1U(3YD@ry1_YQf+)w<AKc~JIxG|MN!SKiYDu2#Yg^5wJD)cz`CQ|Me|0GL!nW};?@WZC#lURe^UiExww+Bn{vf(%46@21&x!|rYXMA!F9Gh8In;Dmk+mtxJO);zw`%UmGO%px9gPswczzx<qZsa5`Rg#KY7V8~BUKH@tUb?UzF6f8lViBh1$&3}2amgGBV!o0yM}>GGcv<usqT^yG5p?FK5xLHVoH5=R9FF)A{`XEk@-`q$ZqvMHR<aI#ih8jfuZB@F_!Qva)jLt_+P)iDjJ#CB!d}o_OVasx3h}lR1-923C4va?4ahND=3&Vuqd}MuCB3;gYXM~<z@we466D|oZ89AnpN=guO-hv6Y)vKXpIebS@@RR!Z>y>HYUsPM-Ed;BS<DZzrirzTx3!o=Ps2Y*^KD;S0|OtG?QG<-FehMxgG&>1onVCsIue-ge8vj%{>?WqJY=(jq8)X=Goqdj_n790TH21BjvcQ>Z8ussv?b8%>1st*y8?xA{t%TaMKaBK2rtc~H3{gB1N}e*?}4GU2sY1?9ihNn7HqP?j#cP4%<zFc5sKKEa3~o1Gj*pOG>wZwd=`9hf)(+=NWt27U~EigdpX2e^xD3yPU^~`JE<#UE`JgyNcc(jks{oMABiU*go`^~C;pK9D%UV%hlu9BX!cHmD(WBvEo3rDGG(`tW4Wz<@X-VyUxh^SY24$u2{>{-pAJvgYr%>e*_gD8*%x*GPzbxh{{R_EHW`@jq9HlA<pnE;t@LN`e|lH+69-yHBeNK>{t#w5-L5O>_XShbmoC!Ah|Wgrh{QfMaj`|Gji=0e{2?{vPZuyi?x-_R>O1`IK&i>h4B<~u<)_pEgLDZxYc#yzOW3E<T7}^ST_so1MMwIAU#g&=Kg9jA7>&BQoiYaDKOh_`q$92Y<(By(-!<+RJ1p&$xA@I$8!a&9z%@|9MmF@Ap~6J_@QCIvZ6)+JhC+6|xvuXuZ}ZRirY6*r{rLNIX&rn8&qAls2<tKwyKcMfyK{QuESKMi*Sg~7a|h_{*5$IPbv`H-!u$u&2&t3b?!WhJ`s}%d>Dm4Fo*#_UFmQfc3J0&j0f*ABFU8Hs>n895y!U_iDNtkZh16bs_x$+)h_RVb<g5zO_qZT(U3ldee24N~&<_ZtARi$Fbr#jrYj~YHuJOO}o!otM*14q`L|uYCBexU2<=RQ)#H+ADOk)XSGKny=TWU3yHf?_^XoN&8?v|5!aVR}3PteZI`jWg!w$7icR;#V*Yc*FtIo8rpTs%1^^*V;@GG2DeJ`fb8ol9)YL2akx^>?>kw(^%g77z-b5r^P^FGhdi+*k&GX~NQORHmV8SzZuK`_$I3Cai{9Sv6p&Vgr=VV`ec+SJG2aj8P46_>!k*6%xdCOm8xvW!M)2T18bOaxRRHA)Em-rEY4C?_u!nKe_}nMIcl9qnGv{ZBDaS*$l#R6LBCH<G9c?cgm2GD;%6hXA7aF&j)oFp>#$FNq6b15^4Bk5h8T|l>ZGJK~4ds1u<i}OgWYQ66W<2C+w5I#9zalwQXwr{sneU=}arbK`367TJk1Uyo+DNSn^`%se*wZmU6xnCVstP$<xu@4E9*T9xK>3zn8-Brz{$_tzg@V$92W`y5u|XFd3!{g!f?-XQnfX$IMox@8ns`leNW?r8nvdXy)87kiBFWX^pZfX2sIlPkmn+Abk;I>bMF<)T4msj=^9s_bz4(JsyDBL&sD&CT^Sv@$DoG(Mx3EXk*PVV)f-=bqY(Q8Er-`w+O{i2v<>j@f!nh=~r3aS{Cs;5WO+9q9d`vES;lbsnU-ks+drbS#JC>ft|s#RToHO2C0kmgnWk7_m}&wqK&-`1jJwX18T)#$NgsS{x@ITg1`Ulpp><$(`vc;>HGTW2mPb3x%(R%7u1<WJnX<?t87o1yB98A&MKi}CQex`RS$}XDj(o4KFsr2nE78(?{`r'),'Libraries/Ń.☾':strd('c%01|ZEqY$`MZC`@FCjSaFOopgou;wgXIK)ph@JW5|VQ|ZPs(n!TRplU8iTNN{Q37s0GqEPE<%s985xiDxg-N3MKTzsDH%2gy)%;-I>|hyR+*eoXXzr%slV!vy{KX-@o$u4{5K5Pd|F?%H`Foy&es6HpzSaQMwuBL4#~0qw7(U(Xc^+AcWuI*ySrU4A;)Ix(oeuv`OMolCU@*jD{H*Y>r21PS)8kwit;r!k_XF`RDvU@b^Byy|54`Q3h}C^4<0Vfgix1C8Ip+^+>xz06icLV*JGb--6h)&ibU+8w>|I5C{Z3<h%T3gX9fzI&Kiw;XC{f{B9@#3ZR-fy;&0uuK<Jbf4&XztPRZEK!J?4({Yy!`XnYS$rxGdHppw2FHoTCK7Z6e8GOWVcP@>FETkcBWMlwB5M;|E3}s6*mPdJ>O7eevk$z9(f#-9^b2D6PcH#fs{b!9mOZNVjZ~vmPr)BS7>}qXaxcC!#9@Krls}&ZHhIup?YMmv~=JoZ6l!}?O$%G7sWTQl<R#0@vKfetU`4^ou@abdzyHHA@?i6SQY(Zg9**NuMZj<2aJM>g`xVLjE3lE=s3Xf0z5|C4bdVqo*kWos4!(ZJ+L-*5KZUAk4$zPc3@Ly=q1;QQVY_nD<4YJ)XEwhHp(yk`P^S0C-f}cZohTfJyZ%f^h#%Q=cMQJrc>U4^giF{Q8OxUna7yN*~&;MP=XbA$is?{g1O@UxUhYc-#W81(82`S6B(mLZ>8+1)r>nxcH3)bfW1R67=mGJ)tiPc{w<3R}(+#<)YFdXFsm&%o+g|z%gj$Sbqlb-mP^jHxzJ~?{WG3l`aHaj7DltpQL(wyV5FyweN-uAm$)eK}BXzQ3*&|ep`w4LC288$Hy)_6&w#d0_51F(L`f6ZSOr~Kg$VE`xKY;{RXyKy{D1;6Pm&c7+2aQds-sA7b12MMgFiWTI3PPS=iW~*`&mM<!06&TELG>+2J_2;ci?6PAAHr$!brk$-$pC<gX@MP`Vz~RSg@ZC?xrj*|0&l)6cka5a7KY%I{%pIJ!ceQgh-Etydsx@tUwW2}UQtC}nfD|-kB2#EW6M=Z+h7364w^dx};IFm_H#5!UDhMBPt2jqZlQ1X%!fgDKDxD`i=Hf`9#4D}R!ev{dKQvOi7^iD`JJyEIS||!qJn={h$*n!*(sO62WtEMs5Z}}gQwUR_03nV?<An8d%f9s*G$m}fURin$OVM}?OY)>7dYpI(W|Jzh@H%pLFV5oO%^QP+5lLHBTXY5CjT369U;nTPU5g2HR~VFsWCiu88H%NIcdMtOgs#|c5yA>WkW#1;fg1)5iG>ZfHdz|w44_nZnwE$b71!*+A1wR_!!73BP-u3=h+_le8CVRzSt09-4ae~ceA`~Ipkep|Vcz3^pXP}b1b$gnNvl)PwymHUaHr)DQ__l&?UNL@!IwA6=ru=%Msmol?9k72hVZ5bNcE=$tWWJkA!7C%xk3hSU%JRezOc|M#0E|a<vaWn=>6W4XJo(XWRiY{KHpDAzhpx!`}>*U{EpO$Y$P(qT&YD^ac%0;>C5QgCS~geq!=}f!GeTZe-;dLmXHeF!r82n`Rj7M2sKan1OA1`z+ojT>Uv8+@d{izLv8xbJGJUpQpug*EF;3np#b6KRTD5{ziAGX(lXsNh;RnXI%aw>(}ZIgyqL);a}_~A)<ANH1zu<blV4e~#G%o*_6NiDiZanjrC*vpy6S0SSN-luS5c5_-D*`fw;y=@eRXP$RS|bp$);eD^`e+G*ac24y6O5z6b*K{XT#QTSBn}2Ay*OtKm%YX0@N6C5S|<hW>~d&D1=vPJ&E#))<rS6<NC0ya7<Osps~>EiXn^H#tlG=vV_LM4=qlCV#TR6d_k;kaziI<t{7Eh2nK(QrflU~nj925NH^yWqO)V<iN!}%s)*q%^ra8@y;4+bSu%(jm9q@_`%EkBdK;aiM7hbyMY*cGc*|H_+D$wMaNws|#u1;n=Fc3iWZ@K!AT|rnbUM^plj!xvqs*8@TGIr)SGa{L4gxEn96Ol$4Z_0sh#!d1XSa(}hxYhm^h^hio!&%vR$F&qc7tvo<>BvUJ!6vWvMvUJ*|$5&Tgi8c2`v|cB16Jnzg`TnTRe(6XzpYrQVgc-CQCE6Zt-J_udJ?tp3*v!_(qiaY-3I%uu`wB^dr~@^w-r);I{~WV3?Q|fT3ORB~(AB_bU1(uE2u8h_3%1!aCEMTUtkot`#As--ZzTQ92y0Gq>9B=p3`dU+@PtQ!}w<O4JHw_xKZ$t>9r_d7P@N+#n*VF4(RLST#Sx7j6brF!3)AfocHlyMXpRfc6!jeN<q@F$JoIST|eVL7L^g#F16Cp{?ut>-udp8wdrz<-f15xwKg%PIQGsqDmB$>GCP8zgU@NEs4u+`afd#NY0T?kwSU`Qb=7XWP_@cRIej_@y1b&ckJ#GE-zvFgCu8Z{X`qDPcU77pnCZG{Gqo7lx4~ef5xBVpDz^kp5w*+Pn7lYNsg#h!D4v96>I8KX(ozX`~f)N4kCQa|4Q-J{o2-Iv-$mgvxyJq`iJlC$~VnsU%t8aMiZW!t+Oq)wcm6W7K;T@$lv8(ijw7}ye6Ua(z16{yu9ii6>ob+#rQgPUN23XAe$2<LqB+><aY;yXeujx>s|}w6NKe3Q<$Lme5c2#+e<2U@EEs7hHb@x9sDGBQaj*edSWELX8=O>_$&T7LKY3eTM*Z=dJEo`HF<C<!++u<3^=m9TH5ors<VuCX4|@3gR`CT=yvE7f{JAErOj>rH~y;l(k2b%1>gaK23iEuIA~R!geg(#WG?-khq6W#^fUeuRrijt`W5O;Yz{@|^_V{vHz}X+fAakXQBO~$2^9PAKJTvLRplAEhTYcLqQenDsHQ<D%)?vHu^KF*1rrhuh4!UoJ4|GG6#u-;xC&kh`>zeHy3(j{ua72_%In>g<*QVU4yF`F;-)6JVr#H&pP^PwoT-Ic@cnb=0x3U5S6zjsZGMg`Tj@i7l%W_qTv`Tz8=U}RNH7K5(FV8y#H8l=eqdh<PQU&uqocIH;BfEO;lqC%?tOf?_u1jzP9Vd~${VYcwi<x$t)RaVv`NrvMZw#4#1m3{#qa2=y&e8Xe&2t!x5NL$-}8n*aq5LP48qcZ+bm%y)TbUeOJ`@_6&A*+ZAQFkxK8Q}CEOV0-CP({t;ugI>jrRxA<OUq<!rf{a`9b(<u?Bfg~TG=ZdWX!gvEfjcJfguScL<7*5R`d@|_N8O`YpX7y_WM(E$Eo4JFkoLN!F43fwaq>_pbXQq}SxYWBn#0V0}nF#^UTtX77vY8cbm3u~4=q~Oo|iPi0w7li#xL6xnv{QPzK!iC<&pW-L5ulIV?_~?}e=;?uScu2FDUULS;7rvm%Tb++-#8QyoVCozVem25q{jCq$8s^Ei8ZkpGZ<Dpf204pEqU_B`cyKZrZJ-O+e@PmK8a~_D2#n{&z+73HiMrJwfPD!Gn1L|VA^*R*mF^+'),'Libraries/peggle2/main.☾':strd('c%0=uYi}IKk>B+zCJKa^S*`+-vg`|Sdpd`box?>BP;_*_ay=L=hvZ7LGn?6=xH?-x{E%Y!71<VL$Cecdh9Sif?D&j0vLRmp56=JMK7_yI>d`&ZJ=3#XO0=BdHZga0y1Kf$s=BJWySn9MFK4fwIQetO^YH24j-EKau;_V?{XZ|+O=~rbPy6A}ahsNHyYQEwkDqW{x4nO+v&X5cod%=STZxmtpFRwluHRh?CP0uT=jZlV@agpjagtg|uo{dke+UnIf>AdZq*it-dn0?l1SLS6;aa@mQDa`}pAG|Su4Or)-#@+VbH&%8$rrP?vNz|f?6vHp>_rEDzLWjd;kQ7MfbKP|a|O)H+12c3_7+23b6n?~Yc(2H_Q#^asA-*_L*%!!-#hlcVRPSbDdqocYoFx+LI7bR+M^CYyYvC3-O8?HcT`eGfap^8wgVM{*3sjKMY~k}z3he7u{a7`pklGLn5+j1mNz^^L&bacEC(xC;kVi6&ajoe05v~ynQtrxOH^T2uE?KOZ%7yz6hE?4CsRL3d(o<u_WD6$yE%Z`I6S<b-FFbgEg+I0T~DGtDz<$?D~;o`*1jP#XxP;1TKgqI0*#@E|0*i1kjP!?@oM7ty>1+x3z8HCx0$`2-533KBEKJaNznHPL!woRli)ti-a|%zkbUCVLD=`=rS;kA>7U}G&yW6a*jtUfZW!_J)g)dYc)chJ66J-B+P(G4ovl}HZ(Y8Ee_y$6yRsLHi<(jj0_QAeHAww5O>&w6Ns6c%PNk?l-4UfO3eH^9YPBr;Z&$C_RuB$@0>1$|Ad-^_@LeoptCD0jK-d17eO(j{!(KOVW|}NEfLmO2w`&MECz>i@<JvhpgJIVnXyY6PP1>^m_iKC3DtB3akFdAFAoRP?b7$6SKzmm{0Q;1>T8Vfo#*S8$Hn|QGLX@EHCBgD~H}KAs^^Vn7*v7o9X*mvz&fk+JV&T6Zai(2hB$mXbw=?t>z;BicW;>)K^QG6!^8?It$$4pU4<Gr3GvgxCoIH@md_k-jr(b24ou|NF2d)YyxfpBW`ires=Mm3#%*GJ_O+#nt?@fL#um)ir-p?+N$9o6y>TTSVZ>FkcqJ5V*fe#aqaP5m7l0eUmF^!AvPtJvF-#iEjRgR1!ipb)!>+jg^M8df=fzY=VMVSq{;^l+uw7+Z`SM_G37g^GrcjJCPh*CDv8~k<3c8$cNOI5KuP86qgZTQi$1tG$#ih&~D%y3bi0aCDZZI^8)8{tLZys@gOis+^7xa4K-%(cw&pf2T%?8adT4lwZicpHY+x{Adb-bui*R!_ddeiXlyw#bIf$TG5Lt^z3nqI=m}c|Zg|--kHB1y7!P3sJKO&<cMrVkVMw<vVAD7F6ZU2pg5kZXi?91EB~qm?hPdy=2iy7^kqmR-BMz=%MtUm7g6TM2pn_VTnTr6b{Ym+$zlcV_@bV>+GqMQ?3*PKY?CDtm7OrIW1@E7^&Pb@EJ`De$0|H8RNjB9XPOhx8!I-$7t_^Lg*MvUvnK{O8{{GnFR;p3_$nX1q$@9W?#_vH`z<*uRnZu>*kl=p)82@aK=b^I9nyXo<f)$SuqOSX@oNv{E)eAgtMg)0=gE95K1qgZZfyfK*rm|{7FlyU=pAj$NfPs#E4`n%A+FrLG{_Lv8WQITO6l5$$A)2m|SPYCa`WvA1DLMjU#C#O&~VTL+n8ktn@}~i-+qg@N8>?l?YTvECrW5S#qXEBtwbQ9;S(1sZ7ytUWFq?2dfql>HZmvid0nU6alArpH|Q+5bY9uFg6<P^Q05!Q71+ycGZ2z@AIlDMXe)4fK-Gq({>%R&6186$EkOQs;~5-<!#}`ye0TmDE)dN++q&ImXiw9J_EyO=#OZmiu%~Yv(4O&U|*@CZaTPZ0u55l?ig(<X^`42m13rMVvZ_t0@!L+NU+$&?C*^3=tsiCtNO=a&3p!+G+#hKd2VK_0662BSpW0)(A7K^z=^=9Jlk@sEhVVIdRvUu_H397X~+eSP=_(nfY5O3`n&LA%Bn)C=4WhJCVgUk_@rAcO_!7zr(5+Cq=ibba8`L<Tr65)f7(lfzGL#CGj;y-09gM6Z2g6`q!xL#g`|t?6t8FBH1h?gAugME2-f1s*m7`seYM3dUMx)Hezu5TKFq$%UUejQ2&b#5`EwWG=d^Icw0vcBXW)?jJgGx-Xuar92;O#>*n$A)46e$|plpji$>k!BRf_knkj};$xF=qR`ja8B$d!ZuKt%>I>gfKNJiNGC*Q?t*anrcIg}8uP)Mb5viz$+P0x*MOiIqESw<AfrWg@M?!n$vqkk9O7LQZ;8qVku*X5Y&`b!c7Uzw)J|7qd^Zcjn|0BmV@9Xdhg`U$g?2U5XNl1v&noCI3&$a;$lRe4!G+DRgyUq3&h>4FLDEyI{Yrz6dsDWwm8buS^S5g*6enBl!Pk>z^%Mqw_VM_p*=jD%=>sPg%;k(JxDFq6pBg9bCcomg6+(^#%8v))NO+d&H}UpXVO$O{U8&DafsS)vOY|F<xLMO$W+^HmQa8v#)3=N|3I0mFyLKI);Eu(J`P=u~?{W%1;L^IdKUZ+6@yXKQ)2k#B`A@6N<4*WYMZaE|GH3j5D{s8d>B#27T!JX?M+b3qwp~Jv`rKTj0Fy;lPie376(W{r^|8z!jXTe^!WNBPmAIZHljW@bS{|bU~a`nI;PBo)4u-?K^(h)u61#@K0(=)M@6HfLfCiTKw@z9aV2+@9mT-p{@e22&5QQl}!9pTw*Xv1B&w7!qf<n3pNRZ@QK@Tjrb;4o#^|pE%I|Z3H-BT^jebze}B@^{LZY~ks^8{yS|HxqY)CR49bz9BQh*&D0pXGT+1+t9%arnn+5)Zj_vJ5ggqdir+PDkIo(-TzAsm1?n~K%-6>nJi2e2i_G`KnK0UD2q4?t;&*t#2-LW{)4`*kP`;Xqruuyiv5~#z67V#cABfkebx%*b;ks3_h$TVzR$hW6#>J_}L&L}kNVz3@vVxnS`CR*O@vMHO8MZyj}6mN90Dn<{3@-F80Ok(YJJ?<+Es2=V8eFbUTSuG;vf$ddw6=hOuwO#B|)p#+0yRP*w<#oKeuI<Fsb+yj(`u*+?Z1d3CIqg44z?QG7gIfB70js4tws3{Ztub4;`9F4cx4opkznSOd`gNI^jxubG=JWw#97bFovlGqG+j;dLViL2hsJQuJSQVY!RmtURW@BXYfO47E<WiMMjXb6wl{{3%J!IPReLw@qgzoN&lS=EicOQz_!eQ*b*(+ItPj5UFrH_cp58pLVDRP{IEO%`je~;a`KBgPO%h^BgrIsIAv_rV7Ynr>?OPL5mF(L2X_5HH}ZCwqWB;S|2oPDh2>#Cb9f5><1=q<DZ(45&y8ya601qgo2dS29%yB<_3cjTk~Kt!oGvP<(%E*442iA+R*vcG1(0qWdlzHgsrM+;sh3g0M=<TXrTZ{|ree{{9vC`_5r`qt#{x92R{4xX~q&T)s{b~$AN2%BJ%$FqRT=6vhCYYeqXP$CgQ7Kvn-PbiI1N&WeQNTAPinBeVO*^OLy_(4%{Jeu&vGHp30ylc+66y}sU2Vt7p_D~`m7<9&*{6<CXMBj8|MIdY}{Tro8Ept)yzs+Oe9==M*#ZkpZQrXrY=lZlwk<D@xDA21D?ak8GeImJ2jkpB4+@XZFKP2BdK}3%L2$PaIFa{ZuW<(&<5B_%bN_i(pLm^YoE9{a)y47qaP_2)%tBz`nkRht|QA;i>CF)oc)IZ!jT1Wj5m~w7XZ-syyd(lhc7*FzOIr=yd(fZ(cy9+|)2e)bE!%R0Z6%LI}x)cc_vc*b*N)DUbR{EyFgIN&wz~X6kRGLq+3wSc;Ms~G{1MPbDd5b!9FT3w5R`X>;X5cl-9u=8^Vy~PxXkAygM%$P-p+$y_J;5f&1-lRIRZ>K}H1^UY2t-nWFy?P^D8k_`NFUEK(J7{u@UMyAgSsnzFASFX<d5)DNzhfDRD<OG+T1pc39u4g^@mCFlO{o!4<t;M{~*`K#IUd1yPqo$WtkAL_3Qgvue=O@?JE7nTG|6f{dtDR*Tx>sPTE72(b`$7A~1xmJVoVJ8nZAhl;n>@x9T@#`S?g%nIB=o9yzdiv#W?zF9G@_=2}T<vxD5=#A1=3>M})<ZNm~tI>_1@c{bu|fAtg%9ezGf4Xc}jmGDb>a)LHJqu0To^}&b2rFk|Tl*cW{OtE$*F%u=gx91wT0o9ngh|cxGcqP76C~;jngkDW^{a<rFggBMvOuHt%xl@Zv?O=|tV?uIyyf9Q$IieCCW=vzMo+FJmVi^f`lSYs7kc>$)VC1+1=87<{twZgqmb^$wV>u*2KRy?5wlZc<dYEfemOUHy?piz$wl>ds%tR6jqk&R?xE2gsJf{~g*$8;QS`UV4FOEv3VH}_J*8+c8zVAidaD6%O2Jx_`!UOK^SuYHt)pSj~I(+13&pcg9HGENyT3&Ja92rJ%Vpj4JMEZB7<sZa+RFahTHt8*=(I2ue$W&q?Q$j60Gd(@MGCgzpG0Y{^dkwP*n<Y^c6}`KloutD<$KFs$AD#5f&vPQ}8wSaRx)mYAVU$!ojA8<)JFTLej8VZCRq%-p01*XknYoNEsC?q%aV6+Gs0D!Rv&!&~DKH0g_!$#?eSldyrSSxKvM1EFzVZwN2WM9tgW&_N6{nzxxLXa%)q_OhlrJl;9II9RU|0fj?1dblFrSriqq*J9?2=QR@8@#rwWj9`X{)vJA87LLiD~Q$*&jt}FnW?n&RMz2Tc;Gt+Kk7Zvw9b3g09E3o0uX=OA^%>n<sx$VhI8UX3sSqGTOnMqgWDE<l#`*vW!-VO^$3hPxl7FsD_J;5Cu=_)Sea}cK5Ja`Ji9DNf8##ghiV*o2|KaoUer3v^ZQkGNPLb(>T)T*w)Z#cC6i4>4j;Kke)Pa+H`kjE5<J?K78*?;`@8;ahX<wDbrQEWW-4CY-Jz}2cciN*MK-MZwmRx*kHrZ>DG@K{7A5Qb*|8LD{$R7N_&wa9is0X(#Pa?tFwyUuon$eKY|(5Ik{fC4GH-+(Yf+sv(mM0F^VyisbVz1Qb>FAOT&7%WNV1{y7e2xMl$8gQ0Q2tcKxRFSbSX*J~OWEBslpnn%{*1Vi*i1_0~qiNi5R_19ZnrN5<hW{&tD)D*1mQYNsuc%g;F1BR^3bg>lypt#F)fP41oKC!e7Rj)!`DTI5^R97%49PHne<rG6#|+ejkFlG4C8n6aF>fwuTBZ>_1Afco$($CNXGRmXHj&`+Xx8I9&P2b8nwQRJQNu?O|xUPbD3L|I6DAOd~^&`k|!f4&>PE1q{3r#~iuK;uBjQ<;CPc}y|vCUv6H0*S$3uxJ$<rP;Knxm5G;@XAk;cw@NB0k764n2=Dnf@r-TBz_vynYf*Y2}bu{=VmMWOPZ!`JI%^*s)t~6B^;x!J>|KZYtch&-0ar2yCVL2r84P=?kj`TVt``$tIWiVryzGSxuuN-z_hb9kzO=dPs`Pm8Dg_^IM8T3#ux*m@fc$abbEgggmF;M4#=;`(6(;Szo^4SpQVoSot5eag}l|R(I(J_Gb+Wt@`^aQ#|1BNVOd@41jHR}!IDuGdSJX3Z4j)khQX`{flBBsG-;3qQQD;A%PqU__aa+cE^N|jrdUR7G-#>tPUX0=hK3z(*XV7NNnLG$Tk6vS8XDfXgenW|MC1|U8*^LheDmLA&Fy44)G!p4qt|@=8_XM0#w?MCy$PYKkI@qdZjV8%9D3Jx@)*C|$D5Yi*Rap?6?i+vuj{ss@)(r$qSbs;4cT=`+jwNf-<&h9gm<NW(ceO;I4$O_A_+n2wV;`rp>-m}ny1ciFv%OFk`>ruOKA}`Sk&LMryKgip&ST8kv(r1#_7=WM1)GWKu``4U;nURtE*6+*Nb|o=Q+Hg4k4V_Xa8K?juqxsWPYrQt?A#D(>_+Q$)^^MAN8JIc=D*T>YAouoV1{rP@+u>#VQ~R+Hyzkym2c-R#smEct@vKut;7%1aFkos8!CFeAHH1kwFp+l3WH=8*A?yw)YLK1-{2*AKp%o^!>2+pTTm6PPFHKO5|us2HKuSSG&*#k8niFb{Yv>vakwKfn4ASNf<6&jnHg@#T_cDG^+N5EPfpYD!MpP5Un*Wu<>{gY8<VEy>6;)|LDrOmgmKklyglzTfL_AyU<aIUW}Yg7>=b`Ssm%{bT&9IxTsfIE6S9%#HKigERNncT3eMr5b?Zt#%oHcxgW`k3?x+3kOHJ>f+O_5mVPi;YbALCRf-7m%nHq)O6#agf<P)aFVck!3+qvY{WwANShLnfFI}_JwE*G)<U-!Zxl+1id3G%6A0)kqZ|BfNDY&482xfIIbxbwn*fHfgv7)8wK$W-ZPOL2$ShKolm+d;m%@uPbVhom=l6~j3F~<Z&xhbfpithuSbXeEk|C?X@J8CNTbzlb6`P?Ij+c?Day?Xj%+iowd2d8Hr|8b}N>{8Uhs~he1)@PTtKD)ei?Tf8z-)vp}O9x->b=uGF-MaEY=Xv<^6SuJ!UhcKwrLDZQ_fks1SMYl4*Iz3I@QW}%TS8sz<2vpk-17bO#!u$x`n0X<?@l#Z-`?dbZZH0r$pqX>_Fii#U5XI<)bp6_hlmSAjD>Jq{Pr%<-fm1Cq6eo9RXfkOm*9i-mm+s6e-GU+l_<+6`ZZ|COYo=14j+BeTX^OdM^0)>PtVy9XM-|9$U3y=thTs~(y<T0-?r_YvdOv8J()!z->(V9;u=Y8z0H?!#iD{zzk?}l^2SMO<f1Lo05&m60jEV&vuIx+^AT~m@e*ZXZ<}rutP~e`m<aw+Y3Gco9ofn4+Pz(Am$)H*Z(!4ELj@sc1R;W#1tkn@6K6aXvLKlWE|H|Lb*3T(O>Wh;BvpD#BFUqpRaR~p>!>ffVI*E~ehok4hBH6$En9*c;(|Nsqk>RtT~w%Neyd*Ov4$E++ZpP)demnaHFr`SGoq?vuBzOP%?%51mu|_k)nY{25K5@1X>6;SbxP_IaCoLXtY$l+WVT##K$aXRmpmp*biE|>xh!Xk#{<j<W@QQ2K`IjJQ=lt4qzn&yn9>RrM2~l>eOB4KAyilBlc}jGQ^Ti3!%9<6bc{o{($q$|v;Rb$Jym}F(@y6CTHl`?KfZW!apB1mG_Mq)lxC7;y43P|f8YUx?u%tKf~9n^nK%wnA0N<)$?w?n*8wl+fZK!~?BwA!kjW032o7U^SrYtS_M3b)gsSO>H$=w^H<iD@X-2Stvy4i1ZE^I2@WV_DTNJAu`Gt+;<&Fj8O{>e3UbDK3lTD=u;u^{Pl!_{xg{CQ8df9c{AAZG;I=IIf(9#*QkQdRg=bPE3mQ-1ydNX^uB~=17KcCF&s-Rr6SO_?O%7+Wx@u-9+I89gnEd#fhm%|gU?74gRAKG~G@L})Bf8am1aS~=B%0IH<*rJYI)E2s&2E){o!&7RqB;H<%tkMTp2=TjR6#?C;LzV-yCg-(xZlhY8p|G}7EyT}vcR=i2-1ch~xRxM#w5^R~*;3zimS75|HfYA^4E$bF-yngUPS)4vV7>`p5SBtiDq?5jkOhITwPd%T#W7gU`QdtiEg_{~jxF#O?vzfW<yvmTGGGB%i}`vHLg>8^%6F#rLQr0XMC=7*d;ikXMrX<lDZT}ywFIHH8S+#WatWesGq7Cvn?HVR@yM~o8bxUfInHzposIhevm2j?Z)TtvX1NJKw(=h}!0qLAe`9UA=Wp~nqt^LxO`1w3AptXpuie5{{6VjtE9lyYCA5|<Ug8KA)&S>)iaR{2n*ZXWT!5GSZCZ#@UwJm{v77)$@_&vNSJ4'),'Libraries/cache.☾':strd('c$~#nO^ee&7{2FM%q=rZ4$XG`D)b<>qNrGQ_aKxK(k9u4P1@3=C5w1)X+`{i6<k?7EcD<_P}iI2dYFIWFLAz-OwzQQRly#b$>f=NpLgEpd6S-J1_8Kb_WJg?rYL~?EZYHw;SSu;Fd$ywH~3To_!<5{{ulTdKNr`zxXw_Gt)oAPXZS^H=Z;v12t-V%bO%+MC_u2?OJL?DFtZCWuko3Tf$LJ#z~d)~fMH;VW*Clnp7)wiuf$uBn;X)&g4&f1xz8`SE@7@^@p=*ds)V_c#cvkjw<Jt8i?0^pHzkao#cy?xm}oTbLtRINqTZ23(lb3z63GS|yd(oYI?gC#f#2aTpjHQaF$J+KDLjmyEF*+?RKpmUzHJ!vW;q;6!nqEB)52iA{yyPN^iJY&P6z=v0E1x&@F70M^OQ9GjqPwU9;_fuR0gMM)D<B)d$^A8(i+pUax}FS9OjHex|JY2O$(KzoUDwb%H$F(3L>ncl4m4Xq=|z<X^4bw8bSjH%TbaBu`-Ng$w(R>aP7LG?U&H5q}wW@%2$*g>vXqW&*t3@@(cRYuBQQKRL7s;?t@n2?lwu_*U5QYF)8mj&tNhlF}Z|!6k6DIUA0tGrOG(N=j{4JZfE|!1)UMPl;aCdt(=62+all=n}ij$w51rj9d+cb@ezK7zbA@;4mBA$`J(l?(}-wJsvWsO7-Y)wFC>}ZkMIfpO7LA$QV0E|P;>0K(=K7O46BcVRoT<h{+mIOLL}=8k<kJ}&-A;NNj><!2I3oLm3q)OW4qKx*2Evhrm2s-p=t3~!&~aD4L<sm?m#S8W1C*^!e80~ksg~`@hSd^zri+dBAV1!IvPk5Vc!fe$tnMF0G*;odiK3bU%MT}FzCe1M#E@6YCYWE-63si&l`44FQ8oosyw=?iH|upm$Fi2itHJ0RT|(t>5LOkIq6)Qiki*qH^!gy6a'),'Libraries/peggle2/rgx_golfatron.☾':strd('c$~dg-)q}e6n@uVaSH?8n<yiSVK9T&CU#8B+R1f17}%OoZ8`R4OF>dWX5E8BJ6N~TX4y*F*xD>lgRT#Qj!_DGxc}JBxw`skl{%D7;7B_6-g7>E=ey_RQht};Zyz4e!2q9HH`+$0I~Y)PXbmT}s*$6ad&`>nlxaj&8T=Isj5cMgx22oP*mLJ(eA^iYt~>L|bbjo50THVe8at<I-|6>1edpafS2s2(>zQAC39i+C-`o;DDIHF9QmsYKKisF=tha6Az;Lotu<K@wqOpIS>I^LkJ?!E%UDqq`SKea^tvB(V(z>wo6Mo7cQAYVU{DPlQct7J0C||<cQpDaQ5J@;b;Xm?cwEl62&aC;Zk%gA${7j4P-&aX5G2G?9@W1#U7<^L>Ge8Fy+1QYt7=UR>Fs=Us40yTEUjhLP{JaU7A(0vDA$v<qErID$0AmFKhR6KRe8eibVKgLG2zCxLmNovI(Kx=G9cpAzO~Hf^g!bxPjkMrrbj?VCQYl3Nwu)w5n2n-&r&N~z9sDN1ho8}m;Wx|S7tIoW(Oe3@9Ch+hkWN_+@C##nt!^*PyI8^!-#8I=y&C8I4D7xgOapsPV=z1MTzJ+q&)Zpm6#!T<8J34c#bs<hV=!1?QUX|@yc)ZQ2e`JL0j)w!GBeVnxxpR`YWex5%48Duu9qfZud`MSD-TFl1F|GwyF6g~Z313h4R|LBc(eQich?H2jO;P-j>3UwIX(!vst~vm7-3#cKk%pgl%_r*4y5%b{+lRSaZ0Pi^+q&AAb7!~Fb^dI18OP=JqqgKtRCbU-^Q*d1xcn(B%~$8dYK4Gy`r)NuvkA4QI`B4C}l~#6Yv;IW*ymq6$BpjpxIf+$F?&9H$rpMF_{2n(BTA_5w{(a)I<&bmEWuHc4<WuQ?N=_h&}Ud2@$y!5j;D%?Kw#h{uR*W6~rE*(#Zy)3+&e9N{xj0fUKwireS6UHh^k%nW9|d5BazJ6&;KA&60E-xwEkqc&>v9IOP|>g8*<XYV-JrQ(^EGbcP&FaXtm7=>6w(bDs0>_#>oMC@Uyc7JtBBtRt;BpyVWNV6vf!(860v5U?X;Q=p87TKp+g6bAwHcPf*;$UE?7)1ggujeO)fcGSW&qGNtV^}Ikq9T3YIVfG&L7xaKd$pmF8DRmF|*Ow<Qi)3ay-~bb>M|}FFe9kXJW&&cK-I-GJnSGg}NVF)v9W?ftJ9R)_u{|uv&gjZbJ6~th;swM;pZ2;?KFiRU-GuY(CX9{#Dj<=&=zkQS;g-~+gh6rNOskiV`*N?tipra3l6sH-U7plXWC+yw<aMHdTH3Z@;C!9NodgtB4&$&afx<sZGL3}#i!%#0O@L=bDx<0wa|cyFr5#sgDqkAuNhJP=P%(>qK=i!d)HilCD2DKBcM9$j_Pl(bkWAn*<j7lBNity`EW9bPo<~>_v`D!p8<ePevJ_xlkQKp)qmDh2!y5VAUewa9K)2*KW3ofhoXV<p@h(J@h&p!Ngd>=}Qnc&Ml`_6!F`7(?&UU+v#$f*wJl`F{0WWi|qiU|m!^tf7&e*@q&KJ!'),'Libraries/Compiler/op_table.☾':strd('c$~FZTTdHD6n^)wm_9_ao4S>4XaY!n;1(6dfMt_Z6<8}@7KGvp@-7vT`Vc4~p=lbD06_|uI0-0C32GXHB9bN&(`WJ<*vCHQC-lth?0D8*gSo_#?XxrIeCIM}&Y4+-Op{-u@$VH)qf}3Cv_CeWX$m&=2~!&`6mv-v`_V|YkV<9^MfD?$RrqCM{ZU0#2fqm>d`dl-5k0RLlcuf}#^`^cXf%XYB8%|-!2UN-TNn+VAJI(#qM6B5R#ysR1_%$5De{=SRPeV$<Do#H^`N|q)kH$|DalMmOX=W*P9c<RGMCCE(U>3Q+YrDdO|w{~3Je;}8+y^is?yuvMctYwt7INboFvQSbr=Q~$XoJWtr6ttV9XYI*hc^7$&L*&3HCh(h!R;MlVQckj;3{`uaMXMi2i~P0Tlq5Bs`4KkmOZW^>Gsx$RFe%Az$%IRq$6>3V=0tqqBWLMB$*k1%YS;<)D1G3TL3b)4^#J#Cq|j3Z%VBU<_Re1Omf>Ky$iLG%Ai++?UATN>y|RZ332y+LxgGv-7r&i+Z3{P)R|htl0(epbIK3s0?l>;Gn14%h2h(47u=LEuRAI)v_CFMb3p2z^zof8mwoWy&cx&Eek96k?c|(D`bbP()^wzcj?~(xe4$HJ~kZ9H-`pWk%Ju!@j=F#m(!Bc*4paPLT)YA+6t0l@<E;hXfG8YB1=@%&>*;kE2@C7Hg9s;t)@L_dqV#O?`p}RkMx4F&&+v4hd8t(Ypu@;S~l2|cjm#d%y{+0+l(d--6ZoqJro+V9xxBNIIRp~gcE$@Kcl4(59Kj!5-bm4lPbLfG{10PG~SUd?!W#twg1olyZw2r`h4kZ(l8LT5+=T*kU8=jc~6t>K3RnRqN;5^st_7gQ6DR6n%o&6ckh$cHiXX^=M0R_Aw}vEFaxHT*lt%VWSf*I>|3%`%hiij_VF=Y8GRUO+Gu{%gpTO&oM*%xAZ%)Z8%944o-q#nj&(^#9NJQ?V2zxx!_ZAo4njPbvOT~&YU(-3qzTCcWr7CgYIjtbP%8>Xhv_OTk~hkPAN3AM{Pa`Q&GBL$O}N=SgM;*}p|j@atCIHeU6=}<Ot_pdYMt<->u2MKIMdkB&M^fBs0)=R;UIm!+^qziIiR7hOPro1m({~1YSMK(Ds12vRjFXmrGX!#N>P)fDCAaZKXi3Rlx8?nH76R0vLQ#AM$y?QT(7-XBtF3~;$|4BF!<;)rBgJ7zmshqXJ{{oZO8>Qnn(5&WHTb0(z=P@Ge$Z1v6BVgj<YMOM;{vSS;U?CdyTr<fIhDXumBBSOUOZpV7F`Y<S)g`R@uH_JzJZ=)}~rpk2)_kYHREZ*;=g?L(j$aHJ>t7W*$HjJCl5<wR>jn%h`QKM)Sg9n{4mvT=E*d*YV3(^?k^FAoN2Oa9S_l@$`sT-JL7-fl95i`Y=UqkXu#os(0=!y2`Zo)q&r$1_KG+$alycr;+n1`+^qax3dK8<cd4uTp9DhD{vtQTqsd%BbB>LUL5OMXuCzhYtAxYh{D9D+?IfI!pKt9R4^eM8dT|sFqDSg^rIXv%%Ira8kONfA;SQ9s@d*HHGHdLsMPtvLdeB*VeC3>{?P02{%cH?<V4T2tAgrQ=UUs6w6>;1!)eb9gVnv^oF7HPRobb=ZrzU2)P+R_WN=4ZoJkx@{3v!Jq-YHi-+i<tp19O`lnpu2g*5sZiBQS=?1&tttoO*~;af7|XQ=^!5!oTOx5swOxees|%)N_p4R4@GnjO@6+DVy33upwkvfUBACSrWCB6U+ui5-R>tA`$w(PMSdc{#gB7X3BH9{29DGYS|{zF<-&@H&~#Af8`1+JPk_7!*HGyK(5pVXI+hy#>QXAC7sZdbs|WTYvm4^hdn)%h?U7*x**@RfwIK>lC9pxuW`=-3vpW3BoEs{fw}CG*{`_X?Qn*f?M@=<nR*cnN6oJA&r+0JN(BeAN*`kIp_Oep|pYaj!3t?uLRPuj|}v>-xJsRqpo{8y+b`9@7rp#jL*RO=q%6rF^i|iJly0_IE?V;l}ESXJBwMW<GnI=vfmrDa&={|BKo^}F7<TB;=C!^Z_3uzt=V1vLS*9^CB7TBX5SrbFaNjvWUp+kJ?F2K=3iJFPe0GC-ls1gX*@s?M`God#xc?}5SDY=k6;k=Y7wn3Ec8RmXGa<__oI6*Sec8t<bp1_m`g5b%Ux}cY4K=xXBb=MH&(f9EkCrDA6bi~gSid<Iw#fAVpG8uz17-$PPYEtcCHF7E!Om{Pt%`nh=GithOOJH{2_h8xd^2%W(1{+*_5Etf)aceDtyC2HXz1YG5Q)ghdg&zzZ7fl)H?h7uEO&El+2Fn24?%MBXU{0{6kkfjEBbcKp+XFFFw%4hpd^G*4C6YvuoX2=Me~|nz1d_8R>H*?T`e5EqfoWw@Z5^3UVbHuDn3{Q>7yv&d3uwqN@J`QZmZ('),'Libraries/Compiler/generate_operators.☾':strd('c$}SB>uwWA6#k#5SRz?70|xEdxg%Ev5?TZ_5d;azxGP`Qt}EZ<HINihk(8T4kwQqKKu91$xd0U{&_<MU`7!@mi9SR91bu{_x$fHD4TTW0XXkR}%sJor=FDPxna+%z{1V$Xla3r88$B^@+ZffHLZRfuP}C@ts+n}j#UyGVMBp!<GCGC{N$#~$T{uidHl6*(`9BIq$LzyLj*S>Y34{IuYI4Q8ZNuPd&8epw)w&C_x^T6gbJ-ANo;hWjX1+gbWwn&klB1=(l45#B%+gX!OK~mrXsK6AeOl_*(twr*wUpLUMoZehn6@vb?Tcyq;#zZDTN>Av#vKH^&z9<Z_jH;r)5jQ`a5iR|gHAjngnWO$5VC!JLdf(=p)Z@4ErU5Z#vBlWneP>X<;cOYoYWJ~$}v5eK_LwEN<Dr3QgG6a5OM=bb6-}j)gxQ-YKg29mtDD-5YjnIj!DZFlSevtwp^aHRlF~lfS8ALhQ8tuAjV$9x(K7n#Y(YIPnV@v*69Yu^eSCv@3@pMXL4!Q{*>MxG73&3-DuRYcn4@T5HX5*-QLj;K8L^KFv=;pPMf}{c+L$Obc((MyWsUDy(?zV5#IfhKIJQj8Abwd+uT|~LLDT)JiSAIS2IYb0S#t=r(UcIyCZ~UkjzfpT}~G(2~eECxOx3jLSV+UGCinye*-liY(rm5<0c}_>s$V&sVk^$(9~4~W4=epuR#e+fg#YALS%P0tlri2Ii00H($_f8Gn{ngoV-y>*Ima}8EfZ@B?o7#m4;JkxMZlyfFE3Ap*i)%Y5UNLkptr+7^8zg512lnKhZhXmrOCQ?}o;&suc&if(Q8e!A>Neo9x*Zb_pAB_X^#n>)Mg+!$gdBL5vIlAPbhsxr%8X3p4Tf=rD!=Ez##4%kpQ^Efup4=EGRh&OrdzVE9x5UKi*Mf=SX$iLH<nA-?TMIK$%w2h(f1MwCJAYl*#W;!oSF<Yc}&{Q&^>L^VL5dC&?h5uJKRRss6?))<sm={yJPJ^CyG4GVz&*Mw)QN)?|vce0#ugOU`UtMtmD1LIgKUVt54_PoY?{g7aIy{1wpbbrN)@XT*?4WswZ-v9CU^!qpb@QJa!nuUPQ;X|iR$OzK6@VrAWhvj*)wIS8&Ah%fHB*ZMfN#}KYwpz|q`BoKI>8_mPX8k^xXy=lTOB0m_p#wWnGY|i^6kP6k#1rMr7e!=;v|_X0(C2OZc0sb6Fe(_W9{MgKZdx#;gVbMaS1(c~bjw~6J*E#dC+}#}1*FlBCx}PnD%6aCc|4OcE1<X$c;-T}z#by%OkzP!si|vpk^U@U!d$+p=@HgEQ$czSSxxaAU_86*WxyK1YmrD@A<zd-;qLm3qaC*{JTrE51e=U^c*3);^|mf6rAoBnkz?2*tfhSmH7P5bt2I|@nTJT+3ZX^5qZ`0e(|Sjym(Ic~GjfDT|8=^ACC#qVO+8BxtH41Igz5uBU=LU(mn0VMe?2x%uy!4b1+PR9@iA{O=dOCwn9IV?1I?3<{B*`U2?iSG+{w6&Lz;ukTXZ67Ob!{70*^^Jmts*P4x56lrzD-VjO41`NkY38TDY`SAh$i5#=2*MH$v_RN_y&r$dbcv69rv?7!j~Zo<0&F+AYgI9Ansp=@F<x4@37F7|x%pwLK+Rle|5^8*&?yC0?hg7R8_()_Ua?y6D3jGu2hamPCC_=>XaC$)-OO;*be(kqLFDakgGDz??2#`#|yLRX&Y$21*}Z4&|T~vO8C`zpX-<b{H-}j;e)<m3+XV3ShzLpI@IM$$j&5+hb-%#<CuTF>htXW?Hep(enD>q<j36K=+?7b{uc!^>}XunD*D&j?*kN*f!s07U-gXGh59^cXfTuCLxdT6^ZRb9i|`>WX3+FNoJC<huQH8!4vDr@%}(lJWqK(@V2E5O;>V0>vkp73tVAamL?wKFVRaJ*^<(x=`C27NLt7KLs+DohnfJ=(Mv;Z<K2*gGfd!|)i>c6moTDgCDOf?X2+fsR~fET9He_>L)73HSF^2@;009<5`QWwh6yXDKinz!NZHDWiIul92#Tjz^kp{6knwJn#TAyqj-7{d84mGU6)rSzM(6!uk=e_shlN(%+x+>ih$(P~J3yfW0iP0B6mi+5ZR*OwV@D(Izbgwf&HLNk5w{y|aI9++84*MH@}aN5YQdDux#q^LEc}OA8*}i>C$i5FvKUT9NmMV-rs?*bBgSr=%o1f4*So_J39JjJWH&3#nzPH@h{%hTrLInF8<6Zb5wH5y9Jz`8`y(#zix^n<MLp*}p>Onh!G$5ey3Z~nUmoy6A@ug5d=hH|yhfqSkQo6Z*(yNTsM@(|*6oCxg3-t4Z77afilWxKET)U9mUG)*RdL_LSsK=)!UO9B(HbjOqQ-Yo<9yUO2dCb7?$dMNjFZK}P{ch`iMTvy6M!uUz~UMJV6vss;2#BR>Z_RNd@0GViu|^>L|?G4CY|3XK!^Bjd0=?h9y!fEU7oaU?E7Si5v&1g3+pior3v<>GptX}Y%de|l=enK{sTAStj_'),'Libraries/Compiler/gram.data.☾':strd('c$~c&U2_!2@vmGIt8Pb!T#}Gb1hsX5At{%^s3aUaxjnY_PAj3(-Rit|GEj(=VqqDRpt|!Vh5{)^EG(0h;K3h&c?eZ<m0$D5`|U5#Pe}Ll%<SyPN#Z3c0X;K4-97y^J-yiW&o_U*ed^2^`|L-P7p5*w+qN-RSu8n~y1|ZQjO_2GPMyyl$z(0h@)m1$@S<&3ybS)BnLh<9KlNXjw9j8SW1q9%?+;d9hDg^^k^T@t^3y0y#VGk{l%_OFmH9>{hH~!Ri?qDA+1j$}HMbnW`2DFVdwTNhJA{J^^~Q|7aAig!OkX@>zxUypX+kJf7VL7x(-BUed(VF7-1{05QbEKRQix!A)2B@<Yke>@G&DOjKI{VQO;74m4xc)!Pn9gL`l>VU0ogg<soMSL`*DiHV!qy}HtLz+*5l0H=2y?eT6wWrg*791_{^v`e7@{CjrmVpSekJepFkwnYj7BaetX%nJdl?S2rBimUqdR!e^&vVuQhN0@KVhrRednopTiA6fzOxZ{ArpeK2m@<56dIjfhYpv40r#{0ilKA(x{a^VP#p4u+fgF>dUS(!|_1pHdv6uPJPZ3R9b)8+iX5V9ukI)aA5GOTPqv~RD(;wS_^&=QIRz>!R@c@8E_n~C9r;N_Nq9^j0RU5NQ~s-WKHg9y5zW?MZ08-kXaOC=b^w*2yK#Yqn$Pde^`bn>ST6b^`ycg{EnkjDMgr>UScW1dtxL7Z)Flc2MF0xLV{NarSn*gaJv1ql@({c;ydV)WV}_HROdt;Z}Fi>4QfT1U^O<EP>u8_VN97Ez%QE-8-{XA2N9krvqjA6?SmLg-x7>vKB1uIo=uw3WJnM)QNJi?BoYXlVNlmpF6=7=fBr1!Y!~}@mH@m>_|sI0gb~VG(D}C5hf&mg6*Ef#jM8JPj#dP;Xh2V&K6u~sSsuBoF`mZZcrsKdtgppAY5R-A5eT+#6N%>Y7>VmhfZPtLG@sk^4YwNg^CQw-brd#`j>PgkWVj(EAP!`E7%hBadrnns5@Wv_=Cr@P*xUU3r^0dc9cGUJdH4)6bc$P=@)+bqZRv6vRUfH_>+MwE?m>iGh>Tzoib_i=tTj!y))jg({V9zbaa^R*y}LojV*`wHUDr4p3s-DV*q0PqTl=UXMw)2>*5-GJ7Mi5%&qGk2UCEOof0$w-s4PdU40UA*E#7V7wWy^S#kC#b+CDtj_WoSkF|KWKK%tsc$=X639VbF(UD2sm=F6^jI}2nDi&N@<w?BiqOz3}A#=<KV6mn@zc{tTC@gNEPKVBkHRR=#fKVPja`n21<s=%eWtM*k%qT*CbbrD)bYpGgteH-w#VT5W}pvn=WsMuT)sgH|_BXG}soIZ|*#g&>sx87WFKMv2%$*(I$>%7F<-N6&smu)yJSOIdw?oOzth<PJ~G)3|gXolrn4~(j~Jc1ziUmC}g_`^q9PT68IQSkGAnm~RQLAE?H6p)AF<jUpw`hx4%O@r4efc&9-PP@5z-56fne0_>3BPM=iyhN$!YU5-?8OL-=d@BMdpJ^ay2#eHwx9&F76Q;1YdH*|c#`46hgq&do9aYeng2ojzp`en2W)!68m4=I0ryp=wA)>eFSDi|-a{K152_J2(=A$@k+kkUOKFT?%NFv`N2AMaZ%Hl@W_eywlM3gR}5g9icx~lG`2e_!*D;@O!Cza?>67qC-m`r|r|4fb|*BpPYZqIWY83vAEU}_AxI)OwoN@23rfDLp40U8Npb)Dd=Q?Sc3mY2L;oj0C~Q`(2AF58>)b_H+FgsNUEJ0Ppk?8(r$TPf+73M9)DsXyu3kN=64prM&zdXnPvQuu-|;xjl>*2bOz(jU_t6<_Xl176kg6>WR^paG)w+L=hV!IKx##X?7j#u&Y3Qi;Ws4e#-A=SEvT+`00#tCHt9%M&+dQiD&PM@4e+5hTyWFFyqBxur%Og}8S!G6nTC^0d4ViSOZB13lUEp6B`zZP7j+4cbkgcq6Q$Vabv(2)1tq%?I#Hwv0Yy`e><-dK<}gNlwK!CYyZnHUuV^t_G5mJaiZ9Hq;Lw=r51CU_(Zsbh=m=8ZPFR3yT*38XQOP>PHApID@mN27g=3v1J2?#hhVTZ*ypX<(CPNGdX6sg`8y#7V~19r?l_6b5W)w+Iacsj8TyA=x-!6HdHKx7z%PxEQPJ+$HsK*L4`0HL3b7Uv2^rf3K|b5%L<xRlVhW#jZ`8+Kj~{+V?CC7?*gr=QAw(|7phb^uMkD1k|yV+BUwUX@RHIL1!bnbRD-Zl-8o1akRo)ChSzq)`{K?weKr#H*vbQ%Q4*5}k`Ud6Xk#IE$3`<>q`iR6T-Yod$ntqA+rYRCK*gS;7!MoGSiCRQ@&dt+A@~slK^vbUPyb<r9c_{Bi6UGsi6z0B(%k(GQR5D<kg6{Wl4SNY!iKk^=BH4@qT>DriO-En9c+GMMw)0pK&GJVwEIJtlORY*X)M}BKy)TC46NzlmMb|kDr3PrPxQ)5y!UCS7Hk;wLle%}^|2evg%ih*1UnB+c%$#W3hvwzZtNZ%4emUJ8xd|9$m&7oo1pV3cml&MAog?+a`)$Zo1Gm1IzP%i6XV_Hi*ED#ZtJsdYo*(~*KK~;ZQbfNf9y6NbemsEywZe>7PmYE1tnB=|E~f#ECk=`gG_7{EURd+>o<b!FM{pc=;r9a+u*}N=W)>a7u^<Gmp^RotBL@0nxRVre^*`>)fWWqDpvh=-8Ey58gJuhJEE10Y+)j-Hz?&8U|!SWqXlDQ<tH@Y%1c=1(aL>|8)^kjg!a*lqo9(490ir>bns}>;zQ7TfrbaGqsbqr9Wx4=RgfFnAL$7ZAB7^)rv!{aw_0mlv*mN1>Zfb;EH|i}3LRQQNh`6aEnv^N9#s<I%Qj9YTG$wgu)!eXr#6iIuOchV;NL?S8;F*PsWh}AO&u&+y1b=c0l)Ah&h(Uv)8b4i)e#VrRaNpSH13X1P>Wh9D^@Xqtl323+m{<mrEo)M$%dzsMIGD}m-fpeB9=Pap|r(ZUnuSy(-D!WXlMoIp=q3;beOTM23T0p@<@HMPQ~GH#P>#6h&UWkG^n|cyTRIXrCa5l<l<_h5|`f-2MgR+r0;bDA@h+qb8er*a36V7?p8Kr5AOvP!)B^4PK<-M^$C53&SfSdR_PUx2s>OdNnE#Hc4}^-XpgW`R3M?+<;#vQb3jTYbheYleiY$b>EVi8*wzv15emEeeewDT+__4Bp;VMswF8*@y-CE`59z?<{yYLeUZ4|;D$Aq3C)KG4mwczZK-1O5nOHiMkK+754yvx*onrh!OdB1KHi8ZLu(4Rp(aNG9azd;$I~^U>`~PB>Y|+9dMx=s!{}E#Ms$}8Bcb;0=e8zy292Y0TIuF6R`*DUk7#asnVDXJ17j4a8nIwdBYPHI>lcr=Y>Ed2a7YB3x;!;h?E+l5+lSzmmu;JnCdJ3BxLY#H3;mq?|7Y=aJ6yH&9eVdVIVtMhf$H{tQ;iL)fEF~hc$xm;xlP9&IuQLo4TH?Hk5*H~EC65oF1+`Ryn&oxxZgA6KHzG?P$L`%s-o1uMDwelg!1P;WyhzUQG8anQ12<s4=6e|bQqKR6gefj?YsoE*99#Z1D_laf0V8kXKFj(egZJfLr_+M)g1=z}|B(x?*9(_kufyc)b(#|YEhNj>{{YKuw2c'),'Libraries/Compiler/ast_to_py.☾':strd('c%0o^>vI!F693L$u~6mgtSu^%2p6J4+!5n@R7`LIp{~kywq$8dROqqUT?hN}DBc(n!pk^7AV3Hqyzj^h2!tx8>b~CJ5P!T+`4g^tUOW4cv@-s5s<I``&h-4IyQinSr#0=ho5oD5UTxQ$S|z9$^`_hQ0;BHRt+v;!H0u9wYOAKP*B)nXZ`-TM9((pS>VB|_&_ne2*p9yv+s03S+d8&w`%c>?rswSS>Vf0=X3p5%XirrdKCyC!X<G1~ciy~Z%U?#fy}5aGhdn$xviWTo#;CnDf<4tB_{^HOjlt*fwS`HT^cww)o-#^hgC3x#=_0YP=>)xF`>s<hL*rNU@bKoH1U`L9ZxeIr(%FfbVm|-IPH)D+PwS_bE`7n9{tUCow#93_?d^8UF>zu+9zOa(&EB)OmPY)@Z9d9#f*G$RNZmic8|UgyqsH4N-pS|l)A_>GYy45oX^758p754xyA{-13gXclym`uVDtlshrW$+fYNOQw(~IYPWPMtYdUT#QI1SnK;+kwx%b(xJo2J{Ij<}F7Y!LVw72i(*5(Tk!+ZF)?I$opa>He}Q=rJm$Mc})W&sX^Oz?+NFY`glJPSJU~K+I1*85nr?-B(`u=%Y=WHf|gmdhuZG+O<oc9v-AWzY1D5UYxXyAwx;!@kvho)mO#pK0C-81_wpMF~QzVW!dlzZ`i0B1dqz9;VN%fEgR;);|-EyOY=8*L#0*g(B;Kl{=L->WRH0vEvY>7$5a<XH6A-Gdik>9sBAExV}ym4wTg_qJ&aq#r2FW8cyJJQ(P4Uo9tCb5qsQr|u!m02&*@3v?`e95o}~-)99;x)U7#0%hnMJOkiZps6-4+oy-vTOH|V$YCjE}yqPOWCdY9g#_vr)rPx>$VkbX~ppg+=|=p*`=KB2$Rr}P<pZUTz!!&?x=@H^YLlSZXERjVM%`}Ay%zn>}L`y&03M4MqXm8t6HH-`(wbs$#LHgQcm#zrzx`#wnx*#UIuuZ)n>sv@B%5jOY{y-$E)=jp@5!$ZK5pXgm8KHL+NAmgtCN1q_e;mdFt->vW|pA=@TIaOh`fR}_%mNVkhbesGh2~o%urp#^0ZeOWx0tBEK8`;$x1>3}jKqnUHO|^}IYs}OhrH>U|5U|DnBkf%yW6PwS)@MKH*)!Dxgl~nb#_?a%)5udb!EDJemmb|8@c(EU0|uGRS&S7?z(|JwN5Jl!?f6yO54;rI0z`^9%!!Ga0iVqxR>Op%uonKnZIQ5Hufc<Z^l>N`r8`#6GV0TUE^Ky#on+sEg=|d(6B85Wnh!rVEd#BzA%`Gt=ysMK(sg*Y%%EP+8FS^=j6uUROkJU$gN`)nEypLb;z)&EL`X3Q-#+{pS^)eU+b_@PK{UdEfNAZjnlo)Uvo2UPyW$77JBN!n2PWfb&H!C1!=F`JWxxv-vfBwNLEsVj9(Fa^k!tQVMQ42RBh!$b;zYE;VBd@~ShL?Re=!e#$IOrj3?NM=J=BQ{C~7foJU^LJ#PNX8rp6ZuaF{r+z;Y__jZa$WRGb1E`6X#46u1xpDK{8G)C9P6?8(xxUw-@X(tj^ql@csw8Ti}6cd~!JTYuoi#Y?784P5#&`Va*cSz(2#NC2E*YQ}8^er4<|@X_Ni^(ma1poj*A(gd7+;!%#dZt|ODT1kRZNiWi;Bmo3Qo~GY2F{K+gROmZguWymGHEYwC#c2o6qAL?yL_p!ROyS0CaNa<LCIpxJIsJif2Il0{gB6P}suEiXY~_GyPi#fP_mv7JJymEbXrGyS9igX{aw&x@fR+XDKZgfe$MX!qouj|9_p{>tihPeU>I`R8PO}u?xjF%O;!WjT7bQ0MT+lw}rK`PVWR$D}UwhqTV!aGE)2JS>q@ZB&rlsvcT<joM1#b7aR!ALIe6f0%0^Bab)BFAMY2gU{`-}~zf$dhjO4HZPObQX;3izSba!mDwF+T@RPI&MzZhqR+Fr7YX8ek-qDoVA`HX7eqR+@FJnpU^X#u<X{dl!}<h$FvWKJ|0dI(9`J>5MP%{*5YQu;?Cr9HUtk#8xw63y;iXZ+ywfCh<_G!(|ebfzY`FurIlEx~Z92t5*Z)Iark($|~*;bxYTuI6lrK4xtkV&E=@!vT$Wn6Cw5Iec~ElKCa1r__df7SLBFK1F3rWje6A~g`9z5z18tZ%MNpC{=9|~ZQUY$C>#(8%8IxriWuvf=FTw7F~pyP0mS{M4f>3pf<bK;0JDySNJEVloTV@<HfmZOJJJeqiU7z`R+cAI^iz{}D#|lFLLGA^NIdR4x%?c68@r9hItEdq=dRT`?40loB{#TdxQ&U!^nf*Bf&?#^S$px|#obTL*!kP1QIEzFu0_TphZ39Zc+QAogGWrklxa$p$+*Be$&~8=1l&ihkm6uW5sOJh40kS9Ki?_!vsA{!J`70K9g*Fja1ZNsXZ`Eh%}Q6hPJaa*HZ|sD-kT>fTaexm-WpjB1jURED~Dv;*m977J^g%zFo?0sL9t^6VfZfxW2JOM_|(gValIcH7sa$U#QSyF<CctCZt1bEwslM8nA@Edo)65`&Njc5mL|izWWt!sNKJ+Lkz*hdyo!lze`ZRz>MEjQ2Ac)np%0G1@nUDs*>9ocg45<Cy&{fc5!G<U;Df8N2N-9BAy2`=mj0ZzHQd;y2DFKl%QGZQIgue5sHLV(k{p#`Et`G7H`zG96$^X$mq=VHhODs|V4_wqppFZOa2StzM*PUfXndSqwWj*?IwvM(`^d5t<5{-5z+lM)E0-B4?of7>lo4&Gpz%DtV8s&}2?s*Exng48&8QBA^XN-3`ac08Az2ol4{{X&{I}^<l451jl~wo06B;XMX++ZEQa)Cff|;J5Qs^U|N@kWoaM>qI{-1dgO{H8HmsPIas0S*o!sgAGQ0cWB5L}8!p1g^X3Go9!>mcDb&N+ou-P`i(+VFmt<@m-%c4>QG%Xb&_d^b;a=lJc?GIrPdA5^>*vJu=o5BO`CwTr=D-p;?gFMIwW7Bfc=fvmZw%ln-7xg7TF1(i8>CK4rg&X(r2&uM#WWpbFkSKlkGQO?8*7KI%D8dH%ObwfLk{}gfC^xOvC#;^l;NP8SRh{N7^XA|=Pqhkw`MkGgWM|u}yy^E7k*MnF(UrL$dL_cT-_R{>mY>bI}R63*fzE^KJMEWHBCIHs-3SZEfn2p4orgmje(D(|vi)6xwMLjStDZ|e=tWCDA<76l)MS}G>L`)b6UNhk?m876gBr~MkYDYIfCf-)tP4^{u8#zwY)ry9&ClAv(xC{o?r*&%U;)#-FaVK!RR==rOlDN81I3&chooeA~NNhi8kF%#$P)7ZN7IN*D1>!zMmyB(x^TIP@XYuh%<Z|N}vRW8SZLL(4&uF3g#+{QR^hVTk8#FkzTVnLL#9UguhURHVx-vr@y9~w%uEoHVS4gni?9}j5+*;oj5gT(SqIaNcje-n6VpH;M$mWzAJsvyqnu$&)B3@|TNXra#4EIZ{_{7Q_gYg0}EK+ke<ZCGcO;Ku1ug!|<I<1-+`c@@9)1alkRpNS+QHW+;vxN10RyDV}!E$D+j*EBJ9j_s><a;}@Ke;+SU&&?ld42i(qOeg^8irMcVFP^W=KFU`kdLR&KiMPB?I~=<h<eL+JS0?*3HOYLB`ngNp6z~58pd9$neW0FWxlMaN?8OXoh3iB`;PgWP9Rk9ae^-B88zjuWc6!79nySy64qZu3x#G`g^(yFLQ}}SA&ckg#!?e?wSKa6qJXHIl^=_xNVBHvrac!3bm-MNN0%rTN_4HdY^SIyxLfp)5=v^_3zJdKs9Ex^PhR<1vapMFKi=iaGlK?zsB|BI#T#5JdNVnlrLm$hu_RQ8PI+9cY{Tx=hEr+TPUM6U9ZP9AxUA?wIF|18763=>lv4`77{7=(d>81=4uVciR<KGW2!waK|JlzOis=X?E3vdnt!BGzKW%9_qh8LJ!flnZP{&jS@zB9^P3;@0=hDh1yI3ftw3gONV!0BN(=kg%9n&Vfl1U^^SZ?O7zAh_;JN%@Txo$86byb-p5%n9@^BN&mnh5K%J!f~l-6Eqo!wpLjnNt3QjqvFby`Y_8WEA<&%OOX@Vj~wt2zJf|hdoiGI6gX#&nLy^a+zQ30v2m>a#gQ>avu(ks^&cUhJ_rP3?JdJq8f$+Lh@{(&5A1*x?^j&(y)ed0R(uSYwEpT?jwyB#TIpkQ{yO~h`l(7dMjw#zE=e>(QMHoeINj(D4N#{P3dgXiq0xsbk*%NXF$<n0?9H!-K$6LosuKyN&2AQSt4VKQ5TNuQU@+aJ#vT=a3ln<T=fLokhe$)`MaICIlN=pZ$(^_bj^$$!b0sdgOE^E?b$fafuRS%ClD*R;-FoLR9n)c&4`lmH5H}cq#VA&fboU-4Nug);pNd$wnxSOOjfmpE7I_KdM1-2R!bNi_f`~dgr&t4mTD%X7fXwhrR!cAqSE9@Oq(-W<-Eql?a2$V__4&!ww}HC&I}`l9@UEsR29&m?d78)I3o_vC^vcSnZO34S8v%(bmnysc-zeWKN4#TUE&Ug61(Qa$%CVXE4*WC`lU4*h=r^Uv4AaXkgKZyHG9qpvV;33y+RU4iYol)OUHv9mJuoW=SGW(#tuBkDGQgh)do_nO4G4FsCd3?^&A(ziB1}m7%^PfbiL8AWrO`*yW#luRK>4Xbw`kN`u)M6DB}XRmSuvYAmSD2GRz_F9RK-GJmzHn%wdvDZz$(8bhvNO1=5GB#uYVe=&k=)TE<+wmvfbnEkGqwQ5czvbBS9E#SiA`-H6_bF&1gQUToL!(2?mx&tG_81&L6NL|+gN@5X;>3KO!gfj5`vDi>72n?ZA?#R!^VbivzYD-f1(E=!jfBkT>dA11-Ac|Dv!Y!Gv}U2{qkEm4Jl`*v?@rir8=AS)MMUk|b=$35oh-QX>oZxq&>=rJFLO^Eror{R?&t47f0dQ6WHv17~;&ug=T$ejz`18kg6_15myhJb-kk%0Oktv&L0{N?Qq+a}ttZHcM&FNBZkGkXG2m??vEV(uEj`ZD-$S^onRIt66')})
__dir__=(__file__:=áÌî(moon_dir/'Libraries/Compiler/main.☾')).parent
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
        if not (v is not None and (getattr(v, 'hardcoded') or getattr(v, 'name') == 'Compiler')):
            continue
        if ÐÌü(getattr((f := getattr(v, '__file__')), 'is_file')):
            getattr(reimps, 'append')(f)
        getattr(__ÄÊIMPORTS__, 'pop')(k)
    ËãÂ(ÐôÅ(reimps, lambda ÂîÓ: Âåß((sha((c := ÂÞÅCAT(ÂîÓ, ÐØó)), {}, {}), ÂÞÅCAT(c, moon_to_py)), Âçß('Transpiled %s' % (ÂîÓ,)))), lambda x, y: (ÄÊPSH(getattr(moon_to_py, 'áÐñ')), ÄÊPSH(x), ÄÊPSH(y), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3])

def generate_bootstrap(dest=ð(TMP, '☾.py')):
    (ÄÊPSH(PL_FORK(compile_code, __file__, True)), ((_ := ÄÊPKE(0)[0]), (Æå := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (pyc := ('#!/bin/python\n%s\n%s\n%s\n%s' % (pathlib_import, ÂÞÅCAT(header_com, compile_files), ÐÌü(dump_cached_imports), ÐÌü(Æå))))
    if dest:
        ÐØì((ÄÊPSH(dest), ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0), áÌî)), (dest := ÄÊPKE(0)), ÄÊDEL(2))[2], pyc)
        getattr(os, 'chmod')(dest, 509)
    return pyc

def generate_bootstrap_live(*áÑË, **áÑÕ):
    ÐÌü(refresh_cached_imports)
    Âçß(Åøþáüì('Refreshed cached imports!', 'f0f'))
    (ÄÊPSH(__ÄÊIMPORT__('Compiler', globals(), '')), ÄÊPOP())[-1]
    Âçß(Åøþáüì('Re-imported compiler!', 'f0f'))
    TRANSPILE_REF(moon_to_py)
    generate_bootstrap(*áÑË, **áÑÕ)
    Âçß(Åøþáüì('Generated bootstrap!', 'f0f'))

def moon_cli():
    import traceback, readline
    (HIST_FILE := ÂÞÅCAT(ð(TMPDIR, '☾_cli_history'), mkf))
    ÂÞÅCAT(ÂÞÅCAT(HIST_FILE, ÁÜÙ), getattr(readline, 'read_history_file'))
    (pfx := Åøþáüì('✝ ', 'f0a', rl=True))
    (ns := ÄÕôñ(ÁØã))
    while True:
        (áÖï := ÂÞÅCAT(pfx, input))
        if not áÖï:
            Âçß('God is good!')
        else:
            getattr(readline, 'write_history_file')(HIST_FILE)
            if áÖï == 'clear':
                getattr(os, 'system')('clear')
            else:
                Âçß('%s\x1b[1A%s\x1b[K' % (pfx, ÂÞÅCAT(áÖï, __highlighter__)))
                (áÕÃ := ÂÞÅCAT(áÖï, compile_code))
                Âçß(ÂÞÅCAT(ÂÞÅCAT(áÕÃ, VEP), __highlighter__))
                (s := False)
                try:
                    Âçß(ÄÕôñ(áÕÃ, ns, native=True, Æå=eval, ret=True, init_ns=False))
                    continue
                except:
                    pass
                try:
                    ÄÕôñ(áÕÃ, ns, native=True, Æå=exec, ret=True, init_ns=False)
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