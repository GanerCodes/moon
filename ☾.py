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
syspath.extend(getsitepackages())
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
    (ÄÊPSH((lambda áÑÞ, s: ÂåÔ((ÄÊPSH(s), ÄÊPSH(áÑÞ), ÄÊPSH('s'), setattr(ÄÊPKE(1), ÄÊPKE(0), ÄÊPKE(2)), ÄÊDEL(3))[3], None), lambda áÑÞ: áÑÞ.s)), ((__init__ := ÄÊPKE(0)[0]), (__repr__ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
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
(ÄÊPSH((lambda x, y: {*x}.issubset({*y}), lambda x, y: {*y}.issubset({*x}))), ((ÂÖó := ÄÊPKE(0)[0]), (ÂÖô := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda x, y: not ÂÖó(x, y), lambda x, y: not ÂÖô(x, y))), ((ÂÖõ := ÄÊPKE(0)[0]), (ÂÖö := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda x, y: (Ïß := {*x}).issubset((Ïà := {*y})) and Ïß != Ïà, lambda x, y: (Ïß := {*y}).issubset((Ïà := {*x})) and Ïß != Ïà)), ((ÂÖü := ÄÊPKE(0)[0]), (ÂÖý := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
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
(ÂÀÇ := (lambda áØÆ: ÄÝöì(ÂÀÇ(ÄÝöì(áØÆ))) if ÁØö(áØÆ, áÍÞ) else áØÆ[slice(None, None, -1)] if ÁØö(áØÆ, ÁÜÙ | áÍá | áÍé) else áØÆ.__reversed__() if hasattr(áØÆ, '__reversed__') else [*áØÆ][slice(None, None, -1)]))
(ÄÝöí := (lambda áØÆ=ÂÞÅ, áØÁ=ÂÞÅ: chr(áØÆ) if ÁØö(áØÆ, áÍÞ) else ord(áØÆ) if ÁØö(áØÆ, ÁÜÙ) and (ãÊú(áØÆ) == 1 and áØÁ is not áÍá) else MOD(Áëý, áØÁ=ÁØö(áØÆ[0], áÍÞ))(Áÿú(áØÆ, ÄÝöí), Âøî)))
(ÂÛê := (lambda áØÆ, áØÁ=ÂÞÅ: MOD(ÂÛê, áØÁ=ÂÔö(áØÆ, '\u205f') * '\u205f' + '\u2009')(áØÆ) if áØÁ is ÂÞÅ else MOD(Áëý, áØÁ=ãÊú(áØÁ) > 1)(áØÆ.split(áØÁ[0]), MOD(ÁØò(lambda ÂîÓ: MOD(ÂÛê, áØÁ=áØÁ[slice(1, None)])(ÂîÓ))))))
(Âäû := (lambda áØÆ, áØÁ=ÂÞÅ: ÄÝõé(Áÿú(ÄÝõé(áØÆ), MOD(Âäû, áØÁ=áØÁ))) if MOD(ÁØö, áØÁ=ÂÕó)(áØÆ, ÂÐá) else áÍÞ(round(áØÆ)) if áØÁ is ÂÞÅ else round(áØÆ, áØÁ)))
(ÄÊPSH((floor, ceil)), ((Âüð := ÄÊPKE(0)[0]), (Âüï := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÊPSH((lambda áØÆ: áØÆ.real, lambda áØÆ: áØÆ.imag)), ((ÄÝõè := ÄÊPKE(0)[0]), (ÄÝõç := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ÄÝõé := (lambda áØÆ: ÂÐá(*áØÆ) if ÁØö(áØÆ, áÍá | áÍé) else (ÄÝõè(áØÆ), ÄÝõç(áØÆ))))
(ÂÛÅ := (lambda áØÆ, áØÁ=ÂÞÅ: MOD(ÄÕåØ, áØÁ=áØÁ)(áØÆ)))
(Âüá := ÁÜÙ.strip)
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
    (__bool__ := (lambda áÑÞ: not áÑÞ.i))
    (__repr__ := (lambda áÑÞ: 'Ticker[i=%s]' % (áÑÞ.i,)))

class TimerState:
    (__init__ := (lambda áÑÞ, áÓË: ÂåÔ((ÄÊPSH(áÑÞ), ÄÊPSH('áÓË'), ÄÊPSH(áÓË), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3], None)))
    (__bool__ := (lambda áÑÞ: áÑÞ.áÓË.s))
    (__call__ := (lambda áÑÞ: áÑÞ.áÓË.r if áÑÞ else ÐÌü(áÑÞ.áÓË.r.copy)))
    (__repr__ := (lambda áÑÞ: 'Timer[%s; %ss; %s; %s Remaining loops]=%s' % ('ID'[áÑÞ.áÓË.y >= 0], ÂüÌ(áÑÞ.áÓË.y), 'Running' if áÑÞ else 'Completed', áÑÞ.áÓË.n, áÑÞ.áÓË.r)))
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
(áÍÇ := (lambda x, y='utf-8', *áÑË, **áÑÕ: x.encode(y, *áÑË, **áÑÕ) if ÁØö(x, ÁÜÙ) else x.decode(y, *áÑË, **áÑÕ)))

class ÃÆë(áÍÞ):
    (__new__ := (lambda ÂÑÎ: áÍÞ.__new__(ÂÑÎ, 1)))
    (__call__ := (lambda *áÑË, **áÑÕ: ÃÆë))
    (__repr__ := (lambda áÑÞ: 'ⴳ'))

class ÃÆì(áÍÞ):
    (__new__ := (lambda ÂÑÎ: áÍÞ.__new__(ÂÑÎ, 0)))
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
        pass
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
        return áÌÄ.append(áÌß) or Âáõ(*áÑË[slice(1, None)], Æå, áÌÄ=áÌÄ)

def Âçß(*áÑË, ÂìÆ=False, áÖý=' ', áØÁ='\n'):
    (Æå := (áÐÙþÂÐüþÂÐü if ÂìÆ else áÐãþáÐéþáÐè)).write(Âøî(áÑË, ÁÜÙ(áÖý)) + ÁÜÙ(áØÁ))
    Æå.flush()
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
        return Âåß(áÑÞ.x, ÂùÆ(áÑÞ.x is not ÂÞÅ, 'Holder value unset!'))

    def __call__(áÑÞ, x=ÂÞÅ):
        (ÄÊPSH(áÑÞ), ÄÊPSH('x'), ÄÊPSH(x), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]

    def __bool__(áÑÞ):
        return áÑÞ.x is not ÂÞÅ
__dir__=(__file__:=áÌî(moon_dir/'Builtins/system.☾')).parent
def PL_CPU_COUNT():
    import multiprocessing
    return ÐÌü(multiprocessing.cpu_count)

def PL_THREAD(Æå, *áÑË, **áÑÕ):
    from threading import Thread as T
    (atom := [])
    ÐÌü((t := T(target=lambda: ÂÞÅCAT(Æå(*áÑË, **áÑÕ), atom.append))).start)
    return lambda: ÂåÔ(ÐÌü(t.join), atom[0])

def PL_WAIT_PID(p):
    try:
        os.kill(p, 0)
    except áÍÚ as Ïã:
        return None
    os.waitpid(p, 0)

def PL_CHECK_PID(p):
    return not os.waitpid(p, os.WNOHANG)[0]

def PL_FORK(Æå, *áÑË, **áÑÕ):
    (áÓà := shared_memory.SharedMemory(create=True, size=2 ** 20))
    (áÑÅ := (lambda ÂîÓ: ÂîÓ[slice(4, 4 + struct.unpack('I', ÂîÓ[slice(None, 4)])[0])]))
    (p := ÐÌü(os.fork))
    if p:
        return (p, lambda: Âåß(ÂåÔ(ÂÞÅCAT(p, PL_WAIT_PID), ÂÞÅCAT(áÑÅ(áÓà.buf), pload)), ÂåÔ(ÐÌü(áÓà.close), ÐÌü(áÓà.unlink))))
    (v := ÂÞÅCAT(Æå(*áÑË, **áÑÕ), pdump))
    (ÄÊPSH(áÓà.buf), ÄÊPSH(slice(None, 4)), ÄÊPSH(struct.pack('I', ãÊú(v))), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    (ÄÊPSH(áÓà.buf), ÄÊPSH(slice(4, 4 + ãÊú(v))), ÄÊPSH(v), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    ÂÞÅCAT(0, os._exit)

def PL_SLEEP(x):
    from time import sleep
    ÂÞÅCAT(x, sleep)

def PL_TIME():
    from time import time
    return ÐÌü(time)

def PL_TEXT_COPY(x):
    try:
        from clipboard import copy
        return copy(x)
    except áÍÚ as Ðáü:
        Âçß('WARNING: Failed to copy.')

def PL_TEXT_PASTE():
    try:
        from clipboard import paste
        return paste()
    except áÍÚ as Ðáü:
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
            return ÁØö(áØÆ)(áÖß(áØÆ.items(), Æå, 1))
        elif áØÁ is î:
            return ÁØö(áØÆ)(ÄÕåØ(áÖß(áØÆ.items(), Æå, 1), áØÆ.values()))
        elif áØÁ is ì:
            return ÁØö(áØÆ)(ÄÕåØ(áØÆ.keys(), áÖß(áØÆ.items(), Æå, 1)))
    return _map_d(áØÆ, (lambda x: Æå(*(x if áÓö(x) else [x]))) if áÑã == 'ꟿ' else Æå, áØÁ)

def ÐôÅ(áØÆ=ÂÞÅ, áØÇ=ÐÌü, áØÁ=ÐÌü(PL_CPU_COUNT)):
    (ÄÊPSH(MOD(ÂÚü, áØÁ=2)()), ((P := ÄÊPKE(0)[0]), (G := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    for Æå in ÁØò(lambda ÂîÓ: lambda: PL_FORK(áØÇ, ÂîÓ))(áØÆ):
        while ãÊú((ÄÊPSH(P), ÄÊPSH(ÄÔÔç(ÄÊPKE(0), PL_CHECK_PID)), (P := ÄÊPKE(0)), ÄÊDEL(2))[2]) >= áØÁ:
            PL_SLEEP(ÄÝôÒ)
        ÁØòþÁÙÇ(lambda ÂîÓ, ÂîÒ: ÂÕÅ(ÂîÓ.append, ÂîÒ))((P, G), ÐÌü(Æå))
    return Áÿú(G, ÐÌü)

@OPWRAP_(*'\U000f04bc\U000f04bd')
def _(áÑã, áØÆ=ÂÞÅ, áØÇ=ÄÕÍÔ, ÁÜñ=False):
    (áØÆ := [*áØÆ])
    (áÖê := [(áØÆ, i) for i, v in ÂÓÏ(áØÆ) if (áÑÿ := áØÇ(v)) is not ÄÔýò])
    áÖê.sort(reverse=áÑã == '\U000f04bd')
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
            return ÄÔàÑ(X.items())
        if áØÁ is ì:
            return Áÿú(ÄÔàÑ(X.items()), lambda x: x[1])
        if áØÁ is áÍÖ:
            return [X.get(False, ÂÚü()), X.get(True, ÂÚü())]
        ÂùÆ(False, 'Invalid modifier for \ueb86!')
    (r := {})
    for i, z in ÂÓÏ(áØÆ):
        if (áÑÿ := Æå(z)) is ÄÔýò:
            continue
        if ÁÜñ:
            (z := i)
        if áÑÿ in r:
            r[áÑÿ].append(z)
        else:
            (ÄÊPSH(r), ÄÊPSH(áÑÿ), ÄÊPSH([z]), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    return r

def ÁÞç(áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ):
    if áØÇ is ÂÞÅ:
        (ÄÊPSH((áØÇ, áØÆ)), ((áØÆ := ÄÊPKE(0)[0]), (áØÇ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    ÂùÆ(áØÇ is not ÂÞÅ, 'ᖘ needs right side')

    def Æå(áØÆ):
        (áØÆ := (ÄÔÙù(áØÆ) if (is_str := ÁØö(áØÆ, ÁÜÙ)) else ÐÌü(áØÆ.copy) if ÁØö(áØÆ, áÍÙ) else [*áØÆ]))
        (ÄÊPSH((MOD(Áëý, áØÁ=áÓó)(áØÁ, lambda ÂîÓ: ÂîÓ(áØÆ)), [])), ((ids := ÄÊPKE(0)[0]), (TD := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        if (ÄÝøÆ(ÁÜÙ, ÄÊPSH(ids)) and ÁØö(ÄÊPOP(), ÄÊPSH(áÓö))) and (ÄÊDEL(1) or True) or (ÄÊDEL(1) or False):
            ÁØòþÁÙÇ(lambda ÂîÓ, ÂîÒ: TD.append(ÂîÓ) if ÂîÒ is ÄÔýò else (ÄÊPSH(áØÆ), ÄÊPSH(ÂîÓ), ÄÊPSH(ÂîÒ), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3])(ids, (V := áØÇ(ÄÝöÊ(áØÆ, ids))))
        else:
            ÁØÿþÁÙÇ(lambda ÂîÓ, ÂîÒ: TD.append(ÂîÓ) if ÂîÒ is ÄÔýò else (ÄÊPSH(áØÆ), ÄÊPSH(ÂîÓ), ÄÊPSH(ÂîÒ), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3])(ids, (V := Âêà(áØÇ(áØÆ[ids]))))
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
        s.append(v)
        r.append(i if ÁÜñ else z)
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
(ÄÔéÄ := (lambda áØÆ, áØÇ, áØÁ=ÂÞÅ: ÂåÔ(ÂåÔ((R := (lambda ÂîÓ: Âêà(ÁØã) if ÂîÓ is ÂÞÅ else Âêà(ÂîÓ) if ÁØö(ÂîÓ, ÁÜÙ) else Áÿú(ÁãÁ(ÂîÓ), ÁÜÙ))), (Æå := (lambda ÂîÓ: MOD(ÆÑ, áØÁ=ÂîÓ)((lambda ÂîÓ, ÂîÒ: MOD(ÄÕåØ, áØÁ=ÄÝöÉ(ÂîÒ))(ÂîÓ, ÂîÒ))(R(áØÆ), R(áØÇ)), lambda x, y: x.replace(*y))))), Æå if áØÁ is ÂÞÅ else ÂÞÅCAT(áØÁ, Æå))))

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
        (áØÆ := [*range(áØÆ.start, áØÆ.stop, áØÆ.step)])
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
                áÍÌ.append(R)
                (R := [])
            R.append(áÑü)
        if R:
            áÍÌ.append(R)
        return áÍÌ
    (ÄÊPSH((y((áÝÌ := x[0])), [áÝÌ] * (áÝÌ is not ÄÔýò), [])), ((áÍç := ÄÊPKE(0)[0]), (R := ÄÊPKE(0)[1]), (áÍÌ := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
    for áÑî, áÑü in ÂÓÏ(x)[slice(1, None)]:
        if (r := y(áÑü)) != áÍç:
            áÍÌ.append(R)
            (ÄÊPSH((r, [])), ((áÍç := ÄÊPKE(0)[0]), (R := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
            if not (ÄÊPSH(áØÁ), ÄÊPSH(ÄÊPKE(0) - 1), (áØÁ := ÄÊPKE(0)), ÄÊDEL(2))[2]:
                áÍÌ.append(x[slice(áÑî + (r is ÄÔýò), None)])
                break
        if r is not ÄÔýò:
            R.append(áÑü)
    if R:
        áÍÌ.append(R)
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
        return '\n' * (áÑã in '⟕⟗') + ÁØã.join(Áÿú(áØÆ, ÁÜÙ)) + ÂÔö('⟗⟖', áÑã) * '\n'
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
            R.append(áÑÿ)
        for i in ÄÝöÇ(ãÊú(áØÆ)):
            R.extend([áØÆ[i - 1]] if (áÑÿ := áØÇ(áØÆ[i - 1], áØÆ[i])) is ÄÔýò else [áØÆ[i - 1], áÑÿ])
        if ãÊú(áØÆ):
            R.append(áØÆ[-1])
        if áÑã in '⟖⟗' and ÄÔýò is not (áÑÿ := áØÇ(áØÆ[-1], LR_def)):
            R.append(áÑÿ)
    return ÁØã.join(Áÿú(R, ÁÜÙ)) if ÁØö(Y, ÁÜÙ) else R

@OPWRAP_(*'\U000f7e4c\U000f7e4d\U000f7e4e')
def _(áÑã, áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=-1):
    if ÁØö(áØÁ, áÍé):
        (ÄÊPSH(ÂÀÇ(áØÁ) if áØÁ[0] == áÍá else áØÁ), ((n := ÄÊPKE(0)[0]), (L := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    else:
        (ÄÊPSH([-1, True] if áØÁ == áÍá else [áØÁ, False]), ((n := ÄÊPKE(0)[0]), (L := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    if (not L and ÁØö(áØÆ, ÁÜÙ)) and (áØÇ is ÂÞÅ or ÁØö(áØÇ, ÁÜÙ)):
        (áÏÞ := (() if áØÇ is ÂÞÅ else (áØÇ,)))
        if áÑã == '\U000f7e4e':
            return ÄÔÔç(áØÆ.split(*áÏÞ, maxsplit=n))
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
                    r.append(b)
                elif áÑã == '\U000f7e4c' or (áÑã == '\U000f7e4d' and (not last_v)):
                    r.extend([b] if áÑÿ is ÄÔýò else [b, áÐÏ])
                    (last_v := True)
            (b := [])
            (ÄÊPSH(Ïç), ÄÊPSH(ÄÊPKE(0) + ÏÁ), (Ïç := ÄÊPKE(0)), ÄÊDEL(2))[2]
            (ÄÊPSH(Ïñ), ÄÊPSH(ÄÊPKE(0) + 1), (Ïñ := ÄÊPKE(0)), ÄÊDEL(2))[2]
        elif áÑÿ is not ÄÔýò:
            b.append(áÐÏ)
            (last_v := False)
    if b or áÑã != '\U000f7e4e':
        b.extend(áØÆ[slice(Ïç, None)])
        r.append(b)
    elif áØÆ[slice(Ïç, None)]:
        r.append(áØÆ[slice(Ïç, None)])
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
    (áØÆ := (ÄÔÙù(áØÆ) if (is_str := ÁØö(áØÆ, ÁÜÙ)) else ÐÌü(áØÆ.copy)))
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
                    rf.append(f)
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
                rf.append(f)
                rg.append(g)
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
        return ÂåÔ((áÖÞ.extend if áÍù(áØÆ) else áÖÞ.append)(áØÆ), áÖÞ)
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
        return áØÆ.pop(0) if áØÆ else ÄÔýò
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
    (__bool__ := (lambda áÑÞ: áÑÞ.áÖõ + 1 < ãÊú(áÑÞ.áÖï)))
    (__repr__ := (lambda áÑÞ: '[%s│%s]⟨%s⟩' % (ÂîË(áÑÞ.áÖï[slice(None, áÑÞ.áÖõ + 1)], ' '), ÂîÊ(áÑÞ.áÖï[slice(áÑÞ.áÖõ + 1, None)], ' '), Âøî(áÑÞ.áÖà, ' '))))
    (peek := (lambda áÑÞ: áÑÞ.áÖï[áÑÞ.áÖõ + 1]))
    (next := (lambda áÑÞ: áÑÞ.áÖï[(ÄÊPSH(áÑÞ), ÄÊPSH('áÖõ'), ÄÊPSH(getattr(ÄÊPKE(1), ÄÊPKE(0))), ÄÊPSH(ÄÊPKE(0) + 1), setattr(ÄÊPKE(3), ÄÊPKE(2), ÄÊPKE(0)), ÄÊDEL(4))[4]]))
    (note := (lambda áÑÞ: ÂåÔ(áÑÞ.áÖà.append(áÑÞ.áÖõ), áÑÞ)))
    (eton := (lambda áÑÞ: ÂåÔ(ÐÌü(áÑÞ.áÖà.pop), áÑÞ)))
    (wind := (lambda áÑÞ: ÂåÔ((ÄÊPSH(áÑÞ), ÄÊPSH('áÖõ'), ÄÊPSH(ÐÌü(áÑÞ.áÖà.pop)), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3], áÑÞ)))
(ARROW_TARG := ÂÚü())

def ÄÝöç(áØÆ, áØÁ=ÂÞÅ):
    (áÖí := ARROW_TARG[-1])
    if áØÁ is ÂÞÅ:
        áÖí.append(áØÆ)
        return áØÆ
    if áØÁ == ÂÕË:
        áÖí.extend(áØÆ)
        return áØÆ
    áÖí.extend((h := MOD(Âêà, áØÁ=áØÁ)(áØÆ)))
    return h

def ÄÝöè(áØÁ=ÂÞÅ):
    (áÖí := ARROW_TARG[-1])
    if áØÁ is ÂÞÅ:
        return áÖí.pop(-1)
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
    (áÍí := Æå((p := ÐÌü(áÖÿ.peek))))
    if áÓà == '¬':
        return ÂÞÅ if áÍí else ÂÚü()
    if áÓà == '⮞':
        return ÂÚü() if áÍí else ÂÞÅ
    if not áÍí:
        return ÂÞÅ if áÓà in '+' else ÂÚü()
    (V := (ÂÚü() if ÐÌü(áÖÿ.next) is ÄÔýò or ÄÔýò is áÍí else Âêà(p)))
    if áÓà in '?':
        return V
    while áÖÿ:
        if not (v := Æå((p := ÐÌü(áÖÿ.peek)))):
            break
        if v is ÄÔýò or ÄÔýò is ÐÌü(áÖÿ.next):
            continue
        V.append(p)
    return V

def UGX_RUN(áÖÿ, áØÃ):
    (ÄÊPSH(áØÃ), ((áÓç := ÄÊPKE(0)[0]), *(áÒø := ÄÊPKE(0)[slice(1, None, None)])), ÄÊDEL(1))[1]
    if ÁØö(áÓç, áÓó):
        return UGX_SCAN(áÖÿ, áÓç, áÒø[0])
    elif áÓç in 'BP':
        (ÄÊPSH(áÒø), ((áÓæ := ÄÊPKE(0)[0]), (áÓà := ÄÊPKE(0)[1]), (áÓå := ÄÊPKE(0)[2]), (áÓÕ := ÄÊPKE(0)[3])), ÄÊDEL(1))[1]
        ARROW_TARG.append(áÓæ)
        ÂåÔ(ÐÌü(áÖÿ.note), (V := (r := UGX_RUN(áÖÿ, áÓÕ))))
        if áÓà == '⮞':
            ÂåÔ(ÐÌü(áÖÿ.wind), (V := (ÂÞÅ if r is ÂÞÅ else ÂÚü())))
        elif áÓà == '¬':
            ÂåÔ(ÐÌü(áÖÿ.wind), (V := (ÂÚü() if r is ÂÞÅ else ÂÞÅ)))
        elif áÓà == '?':
            ÂåÔ(ÐÌü(áÖÿ.wind), (V := (ÂÚü() if r is ÂÞÅ else ÂÞÅ)))
        elif r is ÂÞÅ:
            ÂåÔ(ÐÌü(áÖÿ.wind), (V := (ÂÚü() if áÓà == '∗' else ÂÞÅ)))
        elif áÓà not in '?':
            while áÖÿ:
                ÂåÔ(ÐÌü(áÖÿ.note), (r := UGX_RUN(áÖÿ, áÓÕ)))
                if r is ÂÞÅ:
                    ÐÌü(áÖÿ.wind)
                    break
                ÂåÔ(ÐÌü(áÖÿ.eton), V.extend(r))
            ÐÌü(áÖÿ.eton)
        if áÓå is ÄÔýò:
            (V := ÂÚü())
        if V is not ÂÞÅ and áÓó(áÓå):
            (V := áÓå(V))
        ARROW_TARG.pop(-1)
        if V is ÂÞÅ:
            return V
        return MOD(Áëý, áØÁ=áÓç == 'B')(V, Âêà)
    elif áÓç in '∧∨':
        if áÓç == '∧':
            ÂåÔ(ÐÌü(áÖÿ.note), (V := ÂÚü()))
            for U in áÒø:
                if (r := UGX_RUN(áÖÿ, U)) is ÂÞÅ:
                    return ÂåÔ(ÐÌü(áÖÿ.wind), ÂÞÅ)
                V.extend(r)
            return ÂåÔ(ÐÌü(áÖÿ.eton), V)
        elif áÓç == '∨':
            for U in áÒø:
                ÐÌü(áÖÿ.note)
                if (r := UGX_RUN(áÖÿ, U)) is not ÂÞÅ:
                    return ÂåÔ(ÐÌü(áÖÿ.eton), r)
                ÐÌü(áÖÿ.wind)
            return ÂÞÅ
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ℵ.☾')).parent
class aleph_wrapper:
    (__slots__ := ('x',))
    (__init__ := (lambda áÑÞ, y: Âåß(None, (ÄÊPSH(áÑÞ), ÄÊPSH('x'), ÄÊPSH(y), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3])))
    (__repr__ := (lambda áÑÞ: áÑÞ.x))
    (__call__ := (lambda áÑÞ, *áÑË, **áÑÕ: áÑÞ.x(*áÑË, **áÑÕ)))

class ÂÑÖ(áÍÙ):
    (áÌüþáÍã := 'ℵ')

    def __getitem__(áÑÞ, x):
        if x in áÑÞ:
            return áÍÙ.__getitem__(áÑÞ, x)
        if áÑÞ.hasdef():
            return áÑÞ.getdef(x)
        ÐâÄ(KeyError('%s ∉ %s, and I have no default value!' % (x, áÑÞ)))

    def __init__(áÑÞ, *áÑË, áØÁ=ÂÞÅ, **áÑÕ):
        super().__init__(*áÑË, **áÑÕ)
        if áØÁ is not ÂÞÅ:
            áÑÞ.setdef(áØÁ)
    (__repr__ := (lambda áÑÞ: '%s%s(%s)' % (áÑÞ.__class__.áÌüþáÍã, '[%s]' % (h[0] or 'ᐦ',) if 0 in (h := áÑÞ.__dict__) else ÁØã, Âøî(ËãÂ(ÐÌü(áÑÞ.items), lambda x, y: '%s=%s' % (x, y)), ', '))))
    (__json__ := (lambda áÑÞ, cb, *áÏÞ, **áÏè: MOD(ËãÂ, áØÁ=ì)(áÍÙ(áÑÞ), lambda x, y: cb(y, *áÏÞ, **áÏè))))
    (__iter__ := (lambda áÑÞ: iter(áÑÞ.items())))
    (__call__ := (lambda áÑÞ, *áÑË, **áÑÕ: ÂåÔ(áÍÙ.update(áÑÞ, *áÑË, **áÑÕ), áÑÞ)))
    (__bool__ := (lambda áÑÞ: ãÊú(áÑÞ) > 0))
    (__or__ := (lambda áÑÞ, x: áÑÞ.copy()(x)))
    (__setattr__ := áÍÙ.__setitem__)
    (__getattr__ := __getitem__)

    def __getstate__(áÑÞ):
        if áÑÞ.hasdef():
            return (áÍÙ(áÑÞ), áÑÞ.getdef())
        else:
            return (áÍÙ(áÑÞ),)

    def __setstate__(áÑÞ, s):
        áÑÞ.__init__(s[0])
        if ãÊú(s) > 1:
            áÑÞ.setdef(s[1])

    def __pow__(áÑÞ, x):
        if x is î:
            return [*ÐÌü(áÑÞ.keys)]
        if x is ì:
            return [*ÐÌü(áÑÞ.values)]
        if x is ë:
            return [*ÐÌü(áÑÞ.items)]
        if x is ÂÕì:
            return MOD(Áÿú, áØÁ=ë)(áÑÞ, ÂÀÇ)
        if x is Áâ:
            return MOD(Áëý, áØÁ=ÄÝøÇ((v := ÐÌü(áÑÞ.getdef)), (C := aleph_wrapper)))(ÐÌü(áÑÞ.copy), lambda x: x.setdef(C(v)))
        ÂùÆ(False)
    (hasdef := (lambda áÑÞ: 0 in áÑÞ.__dict__))
    (setdef := (lambda áÑÞ, x: ÂåÔ((ÄÊPSH(áÑÞ.__dict__), ÄÊPSH(0), ÄÊPSH(x), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3], áÑÞ)))

    def getdef(áÑÞ, k=ÂÞÅ):
        (d := áÑÞ.__dict__[0])
        if ÁØö(d, aleph_wrapper):
            (ÄÊPSH(d), ÄÊPSH(ÐÌü(ÄÊPKE(0))), (d := ÄÊPKE(0)), ÄÊDEL(2))[2]
            (ÄÊPSH(áÑÞ), ÄÊPSH(k), ÄÊPSH(d), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        return d

    def copy(áÑÞ):
        (r := type(áÑÞ)(super().copy()))
        if áÑÞ.hasdef():
            r.setdef(áÑÞ.getdef())
        return r

class ÂÑØ(ÂÑÖ):
    (áÌüþáÍã := 'ℶ')
    (__iter__ := (lambda áÑÞ: iter(áÑÞ.values())))

class áÍáþáÍá(áÍá):
    None
(ÄÊPSH(sys.modules), ÄÊPSH(ÂÞÅCAT('𝑙𝑙', PEV)), ÄÊPSH(áÍáþáÍá), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
(ÄÊPSH(sys.modules), ÄÊPSH(ÂÞÅCAT('ℵ', PEV)), ÄÊPSH(ÂÑÖ()), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
(ÄÊPSH(sys.modules), ÄÊPSH(ÂÞÅCAT('ℶ', PEV)), ÄÊPSH(ÂÑØ()), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
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
    (c := c.strip().lstrip('#'))
    if c.startswith('0x'):
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
(mkd := (lambda f, e=True, p=True: ÂåÔ((p := ÂÞÅCAT(f, áÌî)).mkdir(exist_ok=e, parents=p), p)))
(mkf := (lambda f, e=True: ÂåÔ(ÂåÔ(mkd((p := ÂÞÅCAT(f, áÌî)).parent), p).touch(exist_ok=e), p)))
(tmpf := (lambda b=ÁØã, f=ÂÞÅ, n=14: mkf(ð((lambda ÂîÓ: MOD(Áëý, áØÁ=b)(ÂîÓ, ÄÊCUR((1,), {}, ð, ÂýÃ, b)))(TMPDIR), Âøî(ÄÔÙù(MOD(ÐâÇ, áØÁ=1)(abcABC123, n))) if f is ÂÞÅ else f))))
(tmpd := (lambda b=ÁØã, f=ÂÞÅ, n=14: mkd(ð((lambda ÂîÓ: MOD(Áëý, áØÁ=b)(ÂîÓ, ÄÊCUR((1,), {}, ð, ÂýÃ, b)))(TMPDIR), Âøî(ÄÔÙù(MOD(ÐâÇ, áØÁ=1)(abcABC123, n))) if f is ÂÞÅ else f))))

class suppar2:
    (__init__ := (lambda áÑÞ, Æå: ÂåÔ((ÄÊPSH(Æå), ÄÊPSH(áÑÞ), ÄÊPSH('Æå'), setattr(ÄÊPKE(1), ÄÊPKE(0), ÄÊPKE(2)), ÄÊDEL(3))[3], None)))
    (__call__ := (lambda áÑÞ, *áÑË, **áÑÕ: áÑÞ.Æå(*áÑË, **áÑÕ)))
    (__getitem__ := (__getattr__ := (lambda áÑÞ, x, *áÑË, **áÑÕ: lambda *áÑË, **áÑÕ: áÑÞ.Æå(*áÑË, x, **áÑÕ))))
(ÐâÒ := (lambda x=ÂÞÅ: ÐÌü(PL_TEXT_PASTE) if x is ÂÞÅ else ÂåÔ(ÂÞÅCAT(ÂÞÅCAT(x, ÁÜÙ), PL_TEXT_COPY), x)))
(ÐÈÃ := suppar2(lambda f, o=ÁØã: áÌî(f).open(o)))
(ÐØó := suppar2(lambda f, o=ÁØã: Âáõ((y := ÐÈÃ['r' + o](f)), lambda x: ÐÌü(x.read))))
(ÐØì := suppar2(lambda f, áÏû, o=ÁØã: Âáõ((y := ÐÈÃ['w' + o](f)), lambda x: ÂåÔ(x.write(áÏû), y))))
(pwd := (lambda: áÌî(ÐÌü(os.getcwd))))

class cd:
    (ÄÊPSH(MOD(ÂÚü, áØÁ=2)()), ((s := ÄÊPKE(0)[0]), (c := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]

    def __init__(áÑÞ, d=None):
        (ÄÊPSH(áÑÞ), ÄÊPSH('d'), ÄÊPSH(d), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]

    def __enter__(áÑÞ):
        (x := áÑÞ.d)
        cd.s.append((ãÊú(cd.c), (x := ÐÌü(pwd))))
        if x is not None:
            os.chdir(áÌî(x))
        return ÐÌü(pwd)

    def __exit__(áÑÞ, *áÑË):
        (ÄÊPSH(cd.s.pop(-1)), ((i := ÄÊPKE(0)[0]), (d := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
        (ÄÊPSH(cd), ÄÊPSH('c'), ÄÊPSH(cd.c[slice(None, i)]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        os.chdir(d)
        return ÐÌü(pwd)

    def __call__(áÑÞ, d=None):
        if d is ÁÃ:
            return cd(áÌî(inspect.stack()[1].filename).parent)
        if d is None:
            os.chdir(cd.c.pop(-1))
            return ÐÌü(pwd)
        cd.c.append(ÐÌü(pwd))
        os.chdir(d)
        return ÐÌü(pwd)

    def __getitem__(áÑÞ, d):
        return áÑÞ.__class__(d)
(cd := ÐÌü(cd))

def sha(*áÑË, **áÑÕ):
    from hashlib import sha256 as _sha256
    from base64 import urlsafe_b64encode, urlsafe_b64decode
    return áÍÇ(urlsafe_b64encode(_sha256(áÍÇ(ÁÜÙ(áÑË) + ÁÜÙ(áÑÕ))).digest())).rstrip('=')
__dir__=(__file__:=áÌî(moon_dir/'Builtins/extra_globals.☾')).parent
(FRAC_CONV := {**dict(ÄÕåØ(ÂÛê('12\u200913\u200914\u200915\u200916\u200917\u200918\u200919\u2009110\u200923\u200925\u200927\u200929\u200934\u200935\u200937\u200938\u2009310\u200945\u200947\u200949\u200956\u200957\u200958\u200959\u200967\u200978\u200979\u2009710\u200989\u2009910\u200903\u20091100'), '½⅓¼⅕⅙⅐⅛⅑⅒⅔⅖\U000f7db2\U000f7db7¾⅗\U000f7db3⅜\U000f7dc6⅘\U000f7db4\U000f7dc2⅚\U000f7db5⅝\U000f7db9\U000f7db6⅞\U000f7dba\U000f7dc7\U000f7dbb\U000f7dc8↉\U000f7dc9'))})
(TOFRAC := (lambda x: FRAC_CONV.get(x, x)))

class UPSIDEDOWNSYNDROME:
    (NRM := '0123456789abcdefoxABCDEFOXîĵ\U000f7e88ℇτπ\U000f7e8d\U000f7e8f∞')
    (USD := '\U000f7c3d\U000f7c3e\U000f7c3f\U000f7c40\U000f7c41\U000f7c42\U000f7c43\U000f7c44\U000f7c45\U000f7c46\U000f7c47\U000f7c48\U000f7c49\U000f7c4a\U000f7c4b\U000f7c4c\U000f7c4d\U000f7c4e\U000f7c4f\U000f7c50\U000f7c51\U000f7c52\U000f7c53\U000f7c54\U000f7c55\U000f7c56\U000f7c6a\U000f7c7d\U000f7c7e\U000f7c6b\U000f7c6c\U000f7c6d\U000f7c6e\U000f7c70\U000f7c69')
    (MAP := ({**dict(ÄÕåØ(NRM, USD))} | {**dict(ÄÕåØ(USD, NRM))}))
    (flip := (lambda x, m=MAP: Âøî(ÁØò(lambda ÂîÓ: m.get(ÂîÓ, ÂîÓ))(x), ÁØã)))

class SCRIPT:
    (SCRIPT_FILE_LOC := ð(moon_dir, 'Builtins/Data/script.map'))
    (ÄÊPSH(ÄÝöÞ(ÐÌü(ÐØó(SCRIPT_FILE_LOC).strip), '\n')), ((CHAR_NRM := ÄÊPKE(0)[0]), (CHAR_SUP := ÄÊPKE(0)[1]), (CHAR_SUB := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
    (SUP := ÁÜÙ.maketrans(CHAR_NRM, CHAR_SUP))
    (SUB := ÁÜÙ.maketrans(CHAR_NRM, CHAR_SUB))
    (NRM := ÁÜÙ.maketrans(CHAR_SUP + CHAR_SUB, ÂÞÅCAT(2, CHAR_NRM)))
    (ÄÊPSH(Áÿú([SUP, SUB, NRM], lambda áÖæ: lambda x: x.translate(áÖæ))), ((sup := ÄÊPKE(0)[0]), (sub := ÄÊPKE(0)[1]), (nrm := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
(ÄÊPSH((SCRIPT.sup, SCRIPT.sub, SCRIPT.nrm)), ((supscript := ÄÊPKE(0)[0]), (subscript := ÄÊPKE(0)[1]), (nrmscript := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
(ÄÊPSH((SCRIPT.CHAR_SUP, SCRIPT.CHAR_SUB)), ((SUPSCRIPT := ÄÊPKE(0)[0]), (SUBSCRIPT := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(ALPHABETS := Áÿú(ÄÝöÞ(Âüá('\n    abcdefghijklmnopqrstuvwxyz\u2009ABCDEFGHIJKLMNOPQRSTUVWXYZ\u20090123456789\n    𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫\u2009𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ\u2009𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡\n    𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳\u2009𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙\u2009𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗\n    𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧\u2009𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍\u2009◌◌◌◌◌◌◌◌◌◌\n    𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇\u2009𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭\u2009𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵\n    𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣\u2009𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉\u2009𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿\n    ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ\u2009ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ\u2009◌\U000f0ca1\U000f0ca3\U000f0ca5\U000f0ca7\U000f0ca9\U000f0cab\U000f0cad\U000f0caf\U000f0cb1\n    ⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵\u2009🄐🄑🄒🄓🄔🄕🄖🄗🄘🄙🄚🄛🄜🄝🄞🄟🄠🄡🄢🄣🄤🄥🄦🄧🄨🄩\u2009◌⑴⑵⑶⑷⑸⑹⑺⑻⑼\n    \U000f0aee\U000f0aef\U000f0af0\U000f0af1\U000f0af2\U000f0af3\U000f0af4\U000f0af5\U000f0af6\U000f0af7\U000f0af8\U000f0af9\U000f0afa\U000f0afb\U000f0afc\U000f0afd\U000f0afe\U000f0aff\U000f0b00\U000f0b01\U000f0b02\U000f0b03\U000f0b04\U000f0b05\U000f0b06\U000f0b07\u2009\U000f0aee\U000f0aef\U000f0af0\U000f0af1\U000f0af2\U000f0af3\U000f0af4\U000f0af5\U000f0af6\U000f0af7\U000f0af8\U000f0af9\U000f0afa\U000f0afb\U000f0afc\U000f0afd\U000f0afe\U000f0aff\U000f0b00\U000f0b01\U000f0b02\U000f0b03\U000f0b04\U000f0b05\U000f0b06\U000f0b07\u2009\U000f0b39\U000f0b3a\U000f0b3b\U000f0b3c\U000f0b3d\U000f0b3e\U000f0b3f\U000f0b40\U000f0b41\U000f0b42\n    \U0001ccd6\U0001ccd7\U0001ccd8\U0001ccd9\U0001ccda\U0001ccdb\U0001ccdc\U0001ccdd\U0001ccde\U0001ccdf\U0001cce0\U0001cce1\U0001cce2\U0001cce3\U0001cce4\U0001cce5\U0001cce6\U0001cce7\U0001cce8\U0001cce9\U0001ccea\U0001cceb\U0001ccec\U0001cced\U0001ccee\U0001ccef\u2009\U0001ccd6\U0001ccd7\U0001ccd8\U0001ccd9\U0001ccda\U0001ccdb\U0001ccdc\U0001ccdd\U0001ccde\U0001ccdf\U0001cce0\U0001cce1\U0001cce2\U0001cce3\U0001cce4\U0001cce5\U0001cce6\U0001cce7\U0001cce8\U0001cce9\U0001ccea\U0001cceb\U0001ccec\U0001cced\U0001ccee\U0001ccef\u2009\U0001ccf0\U0001ccf1\U0001ccf2\U0001ccf3\U0001ccf4\U0001ccf5\U0001ccf6\U0001ccf7\U0001ccf8\U0001ccf9\n    𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓\u2009𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹\u2009𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫\n    ɒც𝼝𝼥⋿ꬵꬶҕї𝼚𝼐ꬷӍꬼϙƿ𝼛Ʀ𝼞ŧꭒѵꭐꭘꭚƶ\u2009ѦƁƇƊᗴҒႺⴼΙɈⴿꝈⱮͶⴲƤꝖⴽႽƬŲѴϢҲⵖΖ\u2009◌◌◌◌◌◌◌◌◌◌\n    𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻\u2009𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡\u2009◌◌◌◌◌◌◌◌◌◌\n    𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏\u2009𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵\u2009◌◌◌◌◌◌◌◌◌◌\n    𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃\u2009𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩\u2009◌◌◌◌◌◌◌◌◌◌\n    𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛\u2009𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁\u2009◌◌◌◌◌◌◌◌◌◌\n    𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷\u2009𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ\u2009◌◌◌◌◌◌◌◌◌◌\n    𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟\u2009𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅\u2009◌◌◌◌◌◌◌◌◌◌\n    𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯\u2009𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕\u2009◌◌◌◌◌◌◌◌◌◌\n'), '\n'), Âåæ(ÂÛê, Âüá)))
(LOWERCASE := Âøî(Áÿú(ALPHABETS, MOD(ÁÛÛ, áØÁ=0))))
(UPPERCASE := Âøî(Áÿú(ALPHABETS, MOD(ÁÛÛ, áØÁ=1))))
(LETTERS := (LOWERCASE + UPPERCASE))
(TERLETS := (UPPERCASE + LOWERCASE))
(ÄÊPSH(ALPHABETS[0][slice(None, 3)]), ((abc := ÄÊPKE(0)[0]), (ABC := ÄÊPKE(0)[1]), (num := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
(ÄÊPSH((abc + ABC, abc + num, ABC + num, abc + ABC + num)), ((abcABC := ÄÊPKE(0)[0]), (abc123 := ÄÊPKE(0)[1]), (ABC123 := ÄÊPKE(0)[2]), (abcABC123 := ÄÊPKE(0)[3])), ÄÊDEL(1))[1]
(TO_LOWERCASE := CUR(lambda ÂîÓ, ÂîÒ: under_script(ÂîÒ, ÂîÓ), (lambda ÂîÓ: lambda x: x.translate(ÂîÓ))(ÁÜÙ.maketrans(UPPERCASE, LOWERCASE))))
(TO_UPPERCASE := CUR(lambda ÂîÓ, ÂîÒ: under_script(ÂîÒ, ÂîÓ), (lambda ÂîÓ: lambda x: x.translate(ÂîÓ))(ÁÜÙ.maketrans(LOWERCASE, UPPERCASE))))
(REVERSE_CASE := CUR(lambda ÂîÓ, ÂîÒ: under_script(ÂîÒ, ÂîÓ), (lambda ÂîÓ: lambda x: x.translate(ÂîÓ))(ÁÜÙ.maketrans(LETTERS, TERLETS))))
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
    while (l := ÐÌü(ÂÐðþáÐâ.readline)):
        Âçß(ÂÞÅCAT(l.rstrip('\n'), __highlighter__))
__dir__=(__file__:=áÌî(moon_dir/'Builtins/meta.☾')).parent
(IMPSIMPS := (('ℍ', 'ℍ\U000f7e19\U000f7e18\U000f7e1b\U000f7e1a\U000f7e17\U000f7e16\U000f7e1c\U000f7e3d\U000f7e15ĵ\U000f7e88\U000f7c7d\U000f7c7e'), ('⫚', '⫚'), ('¶', '¶✿')))
(ÄÊPSH((lambda ÂîÓ: ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ, áÍÇ), zibe), b85e), áÍÇ), lambda ÂîÓ: ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ, áÍÇ), b85d), zibd), áÍÇ))), ((stre := ÄÊPKE(0)[0]), (strd := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(__ÄÊIMPORTS__ := ÐÌü(ÂÑÖ()))
(TP_CACHE := {})
(TRANSPILE_REF := ÐÌü(Holder))
(EXEC_NATIVE := exec)
(dump_cached_imports := (lambda: 'TP_CACHE.update({%s})' % ((lambda ÂîÓ: Âøî(ÂîÓ, ','))(ÁØò(lambda ÂîÓ: '%s:strd(%s)' % (ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(moon_dir, ÂîÓ[0].relative_to), ÁÜÙ), repr), ÂÞÅCAT(ÂÞÅCAT(ÂîÓ[1].native_code, stre), repr)))(ÄÔÔç(__ÄÊIMPORTS__, lambda ÂîÓ: ÂîÓ[0].is_relative_to(moon_dir)))),)))

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
        (ns := (ÐÌü(BOOTSTRAP_GLOBALS.copy) | ({} if ns is None else ns)))
    (r := Æå(áÖï, ns))
    return r if ret else ns

class Module(ÁØö(ÐÌü(ÂÑÖ()))):

    def __init__(áÑÞ, name, ns, code=None, native_code=None, hardcoded=False):
        super().__init__(ns)
        (ÄÊPSH(áÑÞ), ÄÊPSH('name'), ÄÊPSH(áÑÞ), ÄÊPSH('code'), ÄÊPSH(áÑÞ), ÄÊPSH('native_code'), ÄÊPSH(áÑÞ), ÄÊPSH('hardcoded'), ÄÊPSH((name, code, native_code, hardcoded)), (setattr(ÄÊPKE(8), ÄÊPKE(7), ÄÊPKE(0)[0]), setattr(ÄÊPKE(6), ÄÊPKE(5), ÄÊPKE(0)[1]), setattr(ÄÊPKE(4), ÄÊPKE(3), ÄÊPKE(0)[2]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)[3])), ÄÊDEL(9))[9]

    def __repr__(áÑÞ):
        return 'Module[%s,%s]' % (áÑÞ.name, '✗✓'[áÑÞ.hardcoded])

def IMPORT_find_file(p, g_dir=None, w_dir=None, flags=ÁØã):
    (ÄÊPSH(((ÄÊPSH(p), ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0), áÌî)), (p := ÄÊPKE(0)), ÄÊDEL(2))[2].name, None, None, ÂÚü())), ((name := ÄÊPKE(0)[0]), (F := ÄÊPKE(0)[1]), (native := ÄÊPKE(0)[2]), (failed := ÄÊPKE(0)[3])), ÄÊDEL(1))[1]
    (dirs := ÄÔÔè((p.parent if ÐÌü(p.is_absolute) else None, g_dir, ÐÌü(pwd) if w_dir is None else w_dir, ð(moon_dir, 'Libraries')), None))
    (sufs := (p, '%s.☾' % (p,), ð(p, 'main.☾'), ð(p, p.name)))
    for F in ËãÂ(ÂøÚ(dirs, sufs), ð):
        (ÄÊPSH(F), ÄÊPSH(ÐÌü(ÄÊPKE(0).resolve)), (F := ÄÊPKE(0)), ÄÊDEL(2))[2]
        if ('↺' not in flags and ÂÞÅCAT(moon_dir, F.is_relative_to)) and (h := ÂÞÅCAT(ÂÞÅCAT(moon_dir, F.relative_to), ÁÜÙ)) in TP_CACHE:
            (native := h)
            break
        if ÐÌü(F.is_file):
            break
        failed.append(F)
        (F := None)
    return (name, F, native, failed)

def __ÄÊIMPORT__(p, áÒÿ, flags=ÁØã):
    if flags:
        Âçß('FOUND FLAGS: %s' % (flags,))
    (ÄÊPSH(MOD(Áëý, áØÁ=ÄÊCUR((1,), {}, ÄÝøÇ, ÂýÃ, áÍé))(p, ÄÊCUR((1,), {}, IMPORT_find_file, ÂýÃ, áÒÿ.get('__dir__'), ÐÌü(pwd), flags))), ((name := ÄÊPKE(0)[0]), (F := ÄÊPKE(0)[1]), (native := ÄÊPKE(0)[2]), (failed := ÄÊPKE(0)[3])), ÄÊDEL(1))[1]
    ÂùÆ(F is not None, 'Unable to find module "%s"! Paths checked:%s' % (name, ÂîÊ(failed, '\n')))
    if '↺' in flags or F not in __ÄÊIMPORTS__:
        (ÄÊPSH(__ÄÊIMPORTS__), ÄÊPSH(F), ÄÊPSH(None), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        try:
            (ÄÊPSH(({'__name__': name, '__file__': F, '__dir__': F.parent, '__EXPORTS__': {}, '__þIMPORTS__': __ÄÊIMPORTS__, 'TP_CACHE': TP_CACHE, 'TRANSPILE_REF': TRANSPILE_REF}, {})), ((ns := ÄÊPKE(0)[0]), (áÑÕ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
            if native is None:
                (ÄÊPSH(áÑÕ), ÄÊPSH('native_code'), ÄÊPSH(ÄÕôñ((ÄÊPSH(áÑÕ), ÄÊPSH('code'), ÄÊPSH(ÂÞÅCAT(F, ÐØó)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3], get_code=True)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
            else:
                (ÄÊPSH(áÑÕ), ÄÊPSH('native_code'), ÄÊPSH(TP_CACHE[native]), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
            (ns := ÄÕôñ(áÑÕ['native_code'], ns=ns, native=True))
            (ÄÊPSH(__ÄÊIMPORTS__), ÄÊPSH(F), ÄÊPSH(Module(name, ns, hardcoded=native is not None, **áÑÕ)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
            (ÄÊPSH(sys.modules), ÄÊPSH(name), ÄÊPSH(__ÄÊIMPORTS__[F]), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        except áÍÚ as Ïã:
            __ÄÊIMPORTS__.pop(F, None)
            raise Ïã
    (mod := __ÄÊIMPORTS__[F])
    ÂÞÅCAT(mod['__EXPORTS__'], áÒÿ.update)
    return mod

def __ÄÊADD_EXPORTS__(áÒÿ, *áÑË):
    (E := áÒÿ.setdefault('__EXPORTS__', {}))
    E.update({**dict(áÑË)})
    return E

def __ÄÊADDGLOBALS_CLEAN__(M, áÒÿ):
    áÒÿ.update(MOD(ËãÂ, áØÁ=ë)(ÂÞÅCAT(M, áÍÙ), lambda x, y: ÄÔýò if x.startswith('_') else (x, y)))
(__ÄÊGET_GLOB_MODNAME__ := (lambda *áÑË: áÑË))
(__ÄÊSET_GLOB_MODNAME__ := (lambda *áÑË: áÑË))

def show_imports():
    (ÄÊPSH(__ÄÊIMPORT__('text_format', globals(), '')), ÄÊPOP())[-1]
    (show_table := (lambda x, y: Âøî(Áÿú(ÂÛÅ(ÁØò(lambda ÂîÓ: ÂåÔ((m := ÂóÍ(Áÿú(ÂîÓ, áüíþËðâ))), Áÿú(ÂîÓ, ÄÊCUR((1,), {}, padc, ÂýÃ, m))))(ÂÛÅ(MOD(Áÿú, áØÁ=2)([x] + y, ÁÜÙ)))), ÄÊCUR((1,), {}, Âøî, ÂýÃ, '│')), '\n')))
    Âçß(show_table(ÂÛê('Static\u2009Name\u2009Path'), ËãÂ(__ÄÊIMPORTS__, lambda x, y: ('✗✓'[y.hardcoded], y.name, x))))
(BOOTSTRAP_GLOBALS := globals().copy())
TP_CACHE.update({'Libraries/Compiler/main.☾':strd('c$~diZExJh5&o`Uu|{EV*PzaljC|<9=R&WxVA&ERIS3#N1n;<~BYa05NJ^Gq_=BCeEs_>-{gOICoIo{#HfZZ4eKCU8PCxLU_!smibY|bU<nbgqZhMe)OYZE<?Ci`lGb@^Zkbk(gafx~!j+U>it*&o+9(6LlpLyLl8TgswlAV6s_WLPiE^!<Nf5o!ZHOko5<n;Cg9m^*6{Ir&Xq?}z?xVW-9H@mXo&95xZUWGM+)#XK`G>hIqB8c-q>hR$IDKtws|6j_ZgE)@7AWU2`xDn9&Te^8=ZDDyGR@}|M$nVY1Zqj1pdEKzjJr8E@=TGv#0^_vjGyJ%O(z)4<Mbc~$t-}=Cn%c%0;8}S;y{)xcSX`mg4BvoOhxu>vZw2XH7=1z+O?&Z8Z<uhferpMK!%-x>sy+`7>{mg1#~b=d%9GX<V-vK;{eUN4CmsmqcR=}n<v+mpr}-~v-ygICA4NXTAG-4UK@+$5tNbOJM9(;<)5hy3KRDzxk?$V3j5QLT#{E6c7?Pq1fN*X%>}O$=I&zaw^B4ISRNAbD>TKJP<7a{n{jApy+g>;r#z}@MQ>UAN@@j&pi8Xj6eo9WK*CTz9qy>-Wq*w#Yz@tp)yteo*b^iVI{@19M^&n&l*A}9*Jr46v@^4&nMx4q=Fp#6iO`<4jW=xP!Gb#DB3_C?DgbJm{N*3QwTeohD;m7$OVAv#`t=={XyM*>|4fr1|(`#bJNEi{?L8?Md119h1-!a0$QHY6yj*bx+_pGtpixj}91RYx13P@x)yyYZZxSZ1@o5?O$)1b(0boG>HVa5k0K4-KL7*AW{DLXFCL0p{MMnh?Rij7!GI&x2r_3GAbDbvrg<j2UIm<V{+GMg9h_U?|^xd}nJQ}Gz@Rv*16_Q3i40WXK@Xf%hBel+gUoFMRlb5;cM89xwuzt6v<bF1%BuxX!DXZfn57<J-+>*GQXLwel*<NQJX5<Q`Ega{O3;ZEWYJVe`;rK9bwC3RrV(&sS$b^aZ|iTF0sAi!rgHXW_QA-sKGX<)gOMj5rJ(HSOi7|NA|Ju9M1c0I}{tJgNGRsju+RV;pQ!sR5|8}+<B*oE4JmYeWwH;IVUW`YL16DNMg1^2Na@Ty5157Eu@S_a#iEdV+VduLClOoQF^=yW;?cy$S_7!`R?3Itg1`&qch!T)jbo&59sQ+YDDMdM;JP$01kQ76m&G^5tlIO2sj%a<ff1xOT@FEX;Foo1wyt(J<(R*q}at&(wqj9YQdBHm35jp`l68Nof(=&oF>fFWxyMiV(Ze{G%8X&0Ul-b-E}j_OtZzFT4p(vN3+2=4ftjkAHZ{~6f-%r?`cYX3)&*7>eJb#%wn_T8l>ZsGg<IR?nz@_Tg2C8a7u%zp)uW(hC(kbS(ix5^4d`U6w7%0o56$aUr=mjH?Y{CWN7-w_oIS5_Bfpnjdd5~g~R-)RMLmV^UFYlLWzpLqxV9JyFcK7z>)%%p}0=XwMH0#W$ee_|A#`_bIcvue1>;uGJSXiRt)in5;9@jE>ps45ETVCk_6vo_bf`PunPi;Yg7`-wv7gadJ^to|8LsQ`d}h1_t-9##}vXY3+<!}GR_NPs}W@SuBkpb$R_;8mmNCjlOAK!Dp`0|An>T0|dN0vjke;inTvP!;ZSo4wMWc2UW_Mp5U5sTfvR$PG38;gClG?J_f2*+XL(59tj#oqv=+%kOH}l^n+UFV<hO#yZMRF~&tnQV?}q3vO%=-c0-`)jnL*+7DfM(n^ngmmD-nO<kl5yaFrst?|KImSWPuc6h`ET(#pkOS8luLLP&XMz&AjjnE}Dpi$HZYSdg?@s?KCFH<|#v6<6tl}wcg?_NE!|2+Td#JD~@=*ZULC#TM~!|3erAnU~uCP({MSh(D9*vC|KPA)0o9dorW2D^h{CDw{b)Yz^$&`wspfgbWFYV3ovZ-Vkje++QD1nf}weVjHry+Is^r7n4A>Zhf$1Zc+{vDb%cfR6M$WmKt$9u-&8!Sj2N8L(J<2|IVz<pOYaxkR;g=_!P{?o`*YirCs40)rmMU#1+P#H199YAAkH1vb}buWqa@uPl1&i%WJNB4%qMV$@RO6}YID2gIzm<rmFJrypt@S3NM$c6i(G+`!t*5Bgyw@seIz-q`e(K;a5F6;~V>rpVFjg=rQi2bfU?H@eIyI#MMXo~4RVN^Rgkvyxb>;;_3fR4DEE_2*BC+@TL&N#8E@X_P9behd%{9R=Q3JX4c5d%$_5c&w=wK&%V-YPg#*R!vZnzMLvF{$7j&%w9Wj9Gr5BmDn#=bBo&e%>?kYwDZDHth7WIlHZ8LCo->7W~yQ|JxCFv6-k-Ns3x}hfNJ~G?XBrqHMlGR4vjHdS$m-M4j|u7F9VSC7-J)R?ecJBy^Z5FYqhV}bsmDNOWs{vV>Nn=sv%rLG|8irS#mIH5L*G`NlI!22|W_+jcVBurdxc^@1sBKK0b^>=rvQ>n%C%rpOG5HoYH=W53_o;hJKp9!6r_q{XXxE*M5wCvU&duFVXUk^Jhm}QI+(?8Nv#;0HB7v)%GOkFpgy3C_`63Sf)#xL;xA$;)DEqT_lJmJBT}WE73H5eJ%BOc$2*T<-Jh_DR2XP1RuN}saNMkNr8F&f}u)wBLa{|1U4DU$=)bGRE1;^(H2>UoJTiD)CWe$m7>E`<WA1lkip4R$=c*RK)p<?n2IkHQ*+fRLU)G&WQWuwCyNm$=YbT(@dyQ5i~=)-{bgw?Rt5?|Lph3fv!A6|0ACjzR!zEeOP$rWK#@m~M3`yA;dO1X);(#ZCLvvM63qgPALb9mdhr%H!mmKhNoS<r5XJbTqKxX6YpBQhlTraiE4BQV9Bifiu*0D#7hMb67PqWw%E*@YrmF9>VqwZvs$wU>s;s23y2qAkYTu_?WQLqUamRH;$X*?lDvfFN(h_&!_zt#iU8%j@cj&s57U$wBn1$mJ7BEItd)Gyk%4T?I#bvT)A<{W;DAl@HA?h+lO6L8yko_$GF#m`0Kt|4!>67VEIWwry#F-faeam5B*G^i}8Lc}hK-gQ3=ZWh+&k^@@13!#ld|Lr?sbfPdpg4pdX4ybQ)eG8%l8D=<E&%i|RgW!_J$e1*i%Op;{<WcRM)2P<(m=Jcg140g`TL}@7HnB{Wt=*lu_c3aAX(BKT{%=mcWlws4T=kwJNX~2yO_}%IsqepFRtc9Tr*<^!9%EC@KC9b)o(^6Q(-UAkccZ<Y!+RDX=Tht=1b@GrhLKo>e;rBWovo9Y(L$ao~NGq+<%9;=s)Wv#3c#x-UiHnXwbnWTM+C3$1~g36-v{-jw#(>o7ekxu-jL+GsZDQ3-6MB02%Eb0-o@N$rj)kV@|YJ(H&jfR6_Mjc6c@!gh|D$7&iJAU$0Bc{~^I7sl$0W0xt^#QJ2t^HFaQjT~^#)6pFA3^DlRA@jZ2GMy-yUIz?J>N_Si3IhmA76!MjzD_yZTqgO7}8FdV&))kSqTyHvVr2s87ld~o@;rsfV4D40wuQ=Gm_!|N^KAj;%8DUa{Je``d7?RRR4e=jNXt7='),'Libraries/text_format.☾':strd('c$~!=Yi|@s^1FXU>m)Qi&X~-uaRBEwxdd`Ty5t-I(M8&|R{I#+d+fuvyFM=ok-&Iu5?(eo4o-mJ@W=z=I{`tE;2_aIAip8=3+^XeRrO;YJ8N*hgk<UN>gwvM>Z<Ch9xAozMzhVD-T)UH;;HzdR47e(Y&64owNNXT3rsAC+YTFq*=2DSI<j|pl!-ZUTdZ;}&Witv4O~KNIWDkmhpF`mEA^7f1QK~Hmbo}3u88|)%Q>+rR$zyl;xq9RmqVM-5$}<LI1C7`h(|W_sx6PDY%aI5ZT4rDa?^VxocQ5AY}oJzgq|0ly?^8o4@=MU`Kij}R26=0ubI!=w2_$wSgllT+9)IEhfr{$^0#-mYiHeY1dA?+^$V@K7eh#m<3a=+eCJ)BvJo=CCo1)F-fNZeE$?3~T+#G)mm0O{O4Z~12m-8JCsoYlvi!}_T(11e>*?32F@K$K?b?ZKuH&ZQmmarBJR)27I_-REs?dzlwK&j%|97?Q6N<Q7vj=y-X<KX;<3}7K(X1g~Bt%FF$p3*44s$;2fHWU};vnJHOwnNxNgR1%Hyu3FEpeJCmK*J6r52~C&c5TY<Czh6ly$PLYNh1yzc=b0z}OHR@Hl&gS^mj87TE$V1}&p8ea(4?D4r5m#X9f6M(hn(MHbM(U8|M4*NPanwz4^KU33q;bu=(5B4Y1uO;;;zZsqDynQa({2_UPZi2MwVbVDqPCmghZ3Mf>oG2J`B1>oC`H2F<weGw5Nw2k#k{i8%72k00kLlPQl)W)dArRMLA9Yld2i1TFLSH!7|YjZ74;9wyJ$#5e+Y1>k-FJKP=c#bIaK-rsMbhLS(z9ya!!)xL{TsE}nn%J^O2N?X3(Cf-tfJ<c-5((T*<7d-o9bh9itwUxMt3<$NnG8!wnsK^w;(KvJ0f1t3hg7h`@HkMH<Wa0dV%crTkP60SFhv}RkaE~i%GSGF&km)=Bc>nPT*=n-+B40%G9<OP!^lnt2L2LqD$@0Iq0C8j3+kX3ReL65F-y^ZngJfP#-lOOc$g$&$E`xb7gap0CdWfUd6`J4&aTSdPzSyks9DQRd?;Qoic@6iYKI|KwF3hn$?)KZQhlg^$q<P_rIOyIZtqI8{c}7^3wN=!S&YPpDjp_IzWQotHi4}KuENY1dV~erJ`oH2uLUqYIPG06|IDYk4_w!s*jpO*RL>hOrYL&LO&q(AMYN1b%x1)0hfTrX>ik33thO5I%Taqr<$>a*`zzBhBF?f(i;26T6|;!Eeas1LG!k<R(WxGyQ)E%b%_A%jcD>OiuM5^lwA~Pvy?U8v!2>|uz+I!sT)1Bbk?2sIW>l_TqQ+$c7tw&^#D-eD%=Gp{Jx*l;Y~V4raixW*D}~%B4Q`YkkAw+nLcM0tY8Oh!np{Ss?}O7v`6R5@Jn1$ch|7%2(fN~jlM!H0qTP+nnFuIDoeYruqe3{M-?jUAXW%itE8a+OIi&_|ei5zQRYxBRV8-BK7G*QG!J|fl+-Vi1Y*wh3<#6nM9+?ZT!XQeRJdhtP^JsI%qfQJ?vB2)50$@%DkVWVx-5h6O^EsIb%!|vA&R;QpDNowwkywF|BF3-2Q?PT-?tcpv8=btNGclR5+!1$V{{-AW#mZzREJ(<TLYqepqN_uG@AZU7qJk_Eq4dKIEnX3qwGC4Kn$r1eIAz!ADspNk<P-XQQ}VFTVL*z+gMj_Gm9=aW%gwRS4CLuiZ=%DXfM|{)ZDTa}Qhd)X|H6iU;cNfG&D>1db@%%hZuu8(`xow5wkn1$%UgIX@fJR?g9{ksNxJyZY_dVdZ27C_EEFdUIcX`@yEf(Pt4o&Q4wIk6kT?c=OF}X-9zgCw@ie@_>WjC$5^OoHjk2!;07o0)3&>DTJ4`7ll=3_5BV?D?$p}*rx}o%dYk`6n?9M+jBbzFg<0MXf+;|7y{&ooVN~oQsA4&E*ieN1B-Vo=ZxIQ5}-{}e=ftvI^ebXS-XJQd=5V9fIDbb4F9{cd6N?LH<o^r`BF=~#0Q~-{5O00|ds45)UUK*7-Yy?Jf0wHuK>FzL)qQ<h?phOAf7S!_NN+wg{!9JxwoM(5ZEI0pfmUpIQ#GGvwru#erXg@4x_PGw5&g_8{2{wz#689PvIPZ$B;0{YnsUQg`+eXZwLWb+$a6iQa2^+`&jh28<>zD<aDg(0^;P9OQ9kFZ&^|8LhVp^!r^m_-<N~mQZJ8EU<em*Z&dkgtkC{vGe((`1lZBmSRaZNlD_jv4G4PRD(v6_vA$7%7zmhpB)Tr^pzgWB0fIVxVNOoDbXr%=_(1}ZIECB0f}fktAAGIp|K6$OU#nl>DBTuSFA)Yp(Db#l04YpOAuFEz?u%%jSgl<S%&Pl$kqH#+D{SuqgKDXfV}*xK5k8nODM7Zhka@@=WouEsYt@w$|uE3WU^XEAJXsn(8EuwzcCr0(2x2<_qJ(%nnk__?_T<Rj|1Ihbv$w(OufH}e=lEX$=J-MG#eZF!~>HFEop2M5cQQrqO6kW>T@g<wrV1_l_b(7W$Y7VI!p|Ejl<(_(>=Qf%+ZmX<DyA8FK8qsOX!s@nUieWuz6s(q;1N2+~73|s@@e^R}N;v`XCR2V-QjGqZ|iRLBdMTPUT!Fg)t&Z@aBGq<JIpE5XeX6~7qn=^B#O>fEc=1p%|;cptqC3=(CB>0lJL+xea;xtKlk#vH%kHrns+c3SaRd3V4Hbbymrgz))?wH;;ruVJs-Bg*%7plFb+I7{g=}bno->LRn{T`vl*H!zaYB$kve_OiaFP-%7-IC8DZgJl}|LTf=^>cr1!+-d|fB5kEmfu}@{?zYY_PgtTcggR5>35g??j^sw>UY=Fb4t0GHod*ifAPDYo8hqEy{ZSL*Zl4kGqcBl(|-3010M0a*UVtQ>A}+LW>7Fo_ZnEy!1nnIpPIq`Ur+k;i~gDGV)NH|{ra=7Y<lKJXy1f>C3<bY=@m?`WO`-O^GwgI-Rl}y@qgErFTw9B{FdQ&5q|6N+koGV-&U8PS%cpS{Gc$gKM5tg;QgV;5eh7HZv|KOz3_uaB<~(&hai=p+*AdT?H)j0kYk6#vB?FjiHTthc$SkL|M(OCt4Eg1gb$3pmz)W|+nWd@_;3uImep4rdsu?w*n0^4*5QA|;3J7ycJNrM-t3mdIq{TJXj$X<o^XOCOkL4aVV4UP4f;9foY?C3pnJaOr6;itpz5DWv2{}TinyWLZy;HeHD<ecJSa9H&4hZY&ft&(V5oKjc(x<!RIgL=rrQD5bfMLf<@8bYF^FoSpoBk)rCIy<wAWMH9^#$d`Fy=l^YZy9x{Nlx#c;%e^k*k1sU|a4+D%(AA{45U-qUcMob6#$#<hNn)U|wzZWrl2BX*cZq$E6NzNmyKNu#+LMz+ny>+17q^3esl#gq<g`;}NG+Sy%cd$ksiJF&H^h5zYC>SVKU7}&qlZ*Lg|Aj_ex4=2hC7sU?c{r30DD-)qkKXzY&)rB3hy0HUR-~L^!zMahKig?h=s-;dd;zCaJy+!-S0RHoU$Kgab>0cH^N=}(`L-URJs-MLi)5x;2;m7m?Ay%u6CR5qvII4u+?MQ#e?9e|4(3P%wFH!HG_CP+50qw1W2lMZI`2N`8qet?2K3Q!PAq_>_=9c_G3mLcU5R7tS08vX2d<_8rHhNr=<B}dX<+!QGEjgC!<+HS<-=_&yY;^Gbw9%mvR3$KizYPaao+uumXP~nIcvi#ZCwYL%j@(h#Lb$2!(+m|W0Hs#qCVbDuWeH%yk5=YZ=*d8S^dX#3fVH9pl%|nj3f4BZ4Qs&o5Ca<hDZ1^o+W9tqrk`juYlSvf2CfZGdJfg}k&thBlam(a46Z9*cO#Rt9{j;+NIvm#b_89^U!Aj5cvjR+VHz4^QTZnz&RT_Pq0C@d^qQ<a>s9~lG2pRXhrpVvx2HS^tgSX{PgUxZ?093wDzn)_z0DeR95q>SraAd1jFhRg!-i!otY5+l>ccl~3I@cje>VIdZu@7>c!d@aFSHt!a-mfwDfIU*UJNb58u+CamEt>%z?$EdetdpEz$wQG_u{Bo^>wBI+AQSi#az9VtCw?iRCN(*U3zp0<D<Xnqe`Xd3{F}vKw-TIrJW%pZUQLP8H@obcRLht_*}j7@@Q}fp!!0=+6H@j-kUo^kemD;Zu!_l'),'Libraries/Compiler/to_ast.☾':strd('c$~diTW=J}6@K@x=zZ#LJd9?%k)j}tb`5q2T5}OL(n`i^wR_s*7Bk(Q?iv^?iiEN8609Y@fbm{PFo<Nqtg{<M8_3=sO3G_~L*^Io6LL;fb$9h`X1FL8qH5}L&Z%?#s#>G#^!A0>-)M$`y)$PooWD3{7@8W`*8+#wL8w-gR@+-N+o7gc6jjyXf4+EfYU=dN`ID0~v&N~J>B)1jjZyn(8dt`fpwEWSUx5Dn@%qA;R>rgyn4N0VBxVuQED>C+oM<T68iB8!JwJtn@6xAq9abOEeY)B>eR1-vuF)Ix3;Ik`Up=_Lb-6oHtNrTLgT3!mBpT1`uYV9t-GBB0=XgNx(VdF&Ymmd%b<WbTyiSTQwv5m=-P3gKYy-N_=tE7#g~;PfYQ%O)|JGOkSqrVe@v+NT%>~_r15EiNalnOX4g=|SOvfFGE-p;dm5Gft?IneHh8YqKRJ2F`Mt@@M52F1>wBJ^gYi8gY;j$Ny2JWsXByc)L+jd)I*>Kz?PYf@4fn^&@-F6$KB-V0+>Aa#e7h8sJ2B94^YWx=vyJoNxkifR1b;phY$3N1q^b=zW{0)%{m7tBs)*O0@!0vcgZD44I%XY|l>eVFzI*e=z9@{oMi%k>tc|><lVEcsL)naGo<MXwJ$d_SEC93obR=l7`8eIj~{kxVS$J~3B9?~CU=f-`fE?v~LdIhNb?)S`=dvuGnKhiaboXcQGU9hewB1G=dPwCy5imJd8JrS=;bToEo6O)i24(W+VQ0UjCel3d4sp%Q*eF)C?7b-$%prZ?Oh!b-6?k<L1f2h*qP(TKnSdNxUICEucVEB#9M14UPtFGfnED8iQ{UHtnbap|#qD)PnymY#ecwLF@`LRf_!rcx3oTUQyOs4S<n0!jVWhaC-mITan#&w8ewiU)y)n%ed1f_|wac7B7#k5jevq7bpZc}l>?3Og$z$V?mRnB>?9gm}eB^L2GCIY%apGZf6rK^ovh9<}ot*F}7x%6bpL6T*1l=yO#pt)Bo(iZqB2T|+<%5feKhZ;T7CCXLqQMfPdHIm0nfX7TMyk#7uj%l}LEf57#aa4R}Px8t$dqK3*s{T%N#8mT6&k)-0$aq5eEF*2u?Ifq6$g)4(fZlUl^90k$J3NeVbYz$~y6ntJEX4;4I@z?$+u`<1h)J1D8;^OtHZ%3|rCP1FRI4xk0>KNS7AbKAHUxji@VyWci|2;2Mj885qR1BIw2hl~Taj!#ud*zK>(zydB2PH3-z9t^p>H;u#$wyEu7m}e6)+P74M@>^Or00oR}Z%SDOFlAc_LW`&Y@Y2;tC1}-=$x&^t(&{D%yR~KGcc|><xgEFXYk)xjH0)D%Z=R!jD!$QAk59k4hpICYBB(OEww`JC$+es^OX)mBrXFQICoGT23j5De;wwY9kycGz#Jw1S+yxiEV*Hj@txKlU~}t{m5wARw>dEl2{1OqtpL;2e)7`H9Mgit05!AwPh!~!tWYB_gs@0(O_z6g4ee<;jrIDkbQfzzp)MfGQW4_-@BRlU1|Qobr`#Y0_J=x22D@Xp0Q6q(=}$0Loi6B-XtLOGQrnkAwH2Mf*-qYAizz!!>E1&%6lC#@Wgjt$mhRzqmX?nwn!r>VQA-sIuOseg_dzm5RoAe`k3CP|I#8KhRM3lCz3d0TL4=7M*r6JqKF@6l{@qwEM5FOL@l{Ygq#LtD!1EN1g|WDLmwvDDzA-{GCZHFVm!_YQcC}&T{Gj}V%)RhUbFx8!~WNg`WsvQjh+7UoBcl>^q>3z4vL^HdoILiMj6=4mF@&;zbuB@ICYQ*+k9%DUe8QTl;Lo>8s4Fwvu$#+dnnq+N#(ITe+82}4nIn!nM8Wk(xn<I>e{#v_jPou76BYQ+IlSGQ|VI2q(_%cVIIc!do?xmld6m>(G^buqfk-|^(}!-=IE?)GRdk|)%1PaZE9r!b3~u(;(!7h9O(Ke%1cTW=i|6=Um{wqQW~2_^f1q=*k&*DRw!T;#W`FjRYCD3*aCgEkS_S=0J=g^Iij$ukZ1%T+5R%b!l~qwYKgC>eS4rH)v79`GbyzRVe!zKG$v9{FP(&w`BWxOkxDZ7V;P^6h#$d}!(0UOC$)6FObSTbBm;9M>A+1wXw^fd0z&bcw&D3{Fww)u!@%qM1~G${O~SHF4>+SB&$j{};OaoI3IM5S8c#rMxU54M<CD+`c(zyM8ysHSJwK2&$B&r56KGndvYbkn7O)^x7o6&ET|YHBr*aEN+hCIK%sf*~;5$&{3;f+xUd5e37qpW6u6O~L6g!!5@pKaLmujCxcs%Ami2J!qGc#|<eURpJr3RmqKcg>4f08S6;P+VMB`<OOT~(KHc?J`IJoKIe@VcjFcA@zZ$v3-}ZNSy`o2>KWZOj5#<@tuSY&z~BKPPtJn!!rp3Las0+b;9;h=>`s1~LI*2FA%yB$e}b?(CcEqbN`yL@R-{)_mA@EL*E{IHe=DflEoF6y}Z)evwd>l2RbRY8u1m<dB{a!rykyaM>~mdqpTcCGy29VmjCJL@yHg2HlnrRxDnxqO6E26_+E{?f{`U@s3`v0Aob?r=s+jvm*;#&!4K(ZT}xmbx#PrE80It?HiwN^Je+cMoIhGHw=9Ex~V}iAcp0+<+V|IctUSZ?vuO+#fo>};v(JedWqw4$&dA941sVuUshwcD@r;8UqSk}_Oq#qvyE+@uhN-!fVasK123O%e!JXW8+z#;MX*7-vl{WU3eN}pj(5DS%MVHN_4#;I(bfOn|1$Lol-57a%I+}yo#Uwpg};FD_72dVJw07n*p~&vassRC6jlYR8w4v5TZ1Y>w`KQ+Lnrj8oaN9O2Xvcm=E7-S${x6?_=PYoAq+cb47FC^L0R0KdBMOZmXe3KTzX$fJxSO-%k~NXWc0aWhWJkXIJvx(e@dDT0zf;EF|NWT$#Gi>@s!Egx%cG9Vbei@fZ!O{JHN*W8e{R-ePjA#{4zgl7@G7oUQ_wEU(i19==%QveJOT$'),'Libraries/Compiler/rewriters.☾':strd('c%0Q7ZF3XH`8&Vj^67SsqLD<?fTwOtjGHp$ZGcSMaXdF?`D`?iCCy28#FtDUX-r-q0UKfh1Sq8;aS{@mrb+X{4Ew!*p)>q~{DeNwzTNKL-bse=p&o=zce~F%?{B*jVXw2djvV_vi6Xq(fAGlRqsOC&gzb2Fej)CMm0+peosZjnLMuTSQutpC-Meq!^9K$;xA(xYX!^j+-a{~n!}`Mvj?|Ojn%_Qr1g>YFuFvh*v5+hVY4UQ~8YIzTH^pfe*#-7Jo!k+?pZZu`9Hc!GHoMEc=;4`H0TY3f9x#~=?I#1$oSHp&c%OjwG5Z15y~#G&sVR0E-Y!!DAJ^Gs_9K7)t9-w$SD&rTRW!iay7{4De%Lh^bkl%OzCg44bPhfoPgfEu@$L_n2Tv4lj)8$#%|OheMBn~cPX0RyA6{J#sYT)ls)X2<(q1&*eyQ)u46!-KE(eoS0g==WC-Za@J+C?lrlx`rV1+^4Sum-PkC1;MbsuKWVQO?Di5KJ;wJdP$bGAMy-wjw?7C~z<81h^EQ_}7ya-<1+NQu29{G$|DfTaG`)=!vyg?%E#-G6bVQLF7iqJV9Ox}8KZ4<{o3BA0RamnMUiwBstp3(x;4nm#(S_xKDU;d7uxgxz4DvJ1%LSrkh+5voN%o@egh5dT0!1r>KtTwjs!!TpEdY(BUN117{HDu8{&!El-4pitPpaSx`20tfRhK*F290XIP(0h<?Bl3Fc(a1-8l*A~i=5@Yj-Nfag?5d~0-QS3m?DOy%h&R%10ur1**X{JrpCTJ1q#pxhwb~^*pTmaDb>{GD3H`r}$IbcISqZ;5q1TWC$s|knhqC2GA8JuPxu<r>fJ~>`TFx*X@X6M-@?WAyFN+gB1*(M2py7vC(@VX1Hf57WIc-{Z$+U6;Ey#@%(K3fTPSAu#2UNv~_sswxBtu71<ZDcv_Mg3mVY{hLd%v{lw#z(rG;|;`#onlwn<?3?$QZh*6P9I4-3lcFAy8bD=K7$t^b{!DA{sp|ggx5WI0g~6hg4aI{#Nqk-@cjLINCY4q*6NL2zj)@C&+gt6&o=={&Zixw@p8W^{p&}jlYWogA*KF345V8U-slwEy=8b{Djv2v0Z_83otAe!`MxpMx`J~c+Sws@{&Mg&_BGc-F}VIqP=_k#Y&#w#z;sH@_@Jex0(yUt=A#4Lj0PurNuNthddy_GH#mvoh1cX`UVNcet1Z^{#LpNvTgyG;Q-5VX`_!>M4f-eh(b9_Y!)myD3*b4o5KP^3ui@NF`pvkPgi`cQqJjfZZ=>dkIQ2z+Q?Yld+a@msAkC~%iNjzD*9>!chj;M;1)YEq8<1UmOSt0QbHgZCic@UM&>w%GO{&MG(-2|zDIRtKJ0fmX@X;sihT#plCYh)Y$H<km^K>!obO$CbJa4db0D~{XF&HwW7OvxQc}!$8L>-hyTkUD~4f`Bra+$4JU@uGtJH-WhaKP73fNidwmF4*)Z?TSQcakL>S*TYZI1cC*2?-4=ft9k}DkSW4wgqnR!QId_208m?IXhlBa%}&;nSF=<c<9)l5A8d8_~1-+vEAxr_T@M$Nl>rbmjsDL)P2DYxGnYm3cI40tWkSZlni^@=ZIBpjLV)+fjtl3dCi`$SyZ&vgi!+&h<}izoj5(2bJ(qZH0-5OJm@Z4NlISPg>enTg7i4-_NK#a<ibSNqlWwlhO<lTdmcPwiCLq_0icnvciDC4Nx$7{CZw*G<vGfnszmqA93XWlMWGT^i$Z`ED}X^BmcHxZXV*gR&~CA}*uNzPP$n6;dUAIU9e|#oA&+N9!HvhH0AbwZFklsgYtqIaO0rNKoGiG7^^QsK)sUJLixK0KY-U2rpKdy;c@z9A!nNq5bEvDpg#T|9B0Qfr6^Zhogqa&K7ZvK~)*YYf)CEnEm!QVj1cBfAmc3y*0=^if?g$=tT_Zs~BKf=ED(WIKt9w~J|I@V(u7(D9oOho6ox2}gxnfPiZU>reZV8?pmwHmJh+8Dr5xI0TbW+=Gsy0dqSno-h1cj&pRFcKhp;y@&)s2<zN-rA3=~6Pt=g$jWyH@n|IG|KH1FttjBlQ7+W(=+>?h*)GBf(*CQ{$CB%KGmEp0x_f8kD#A2s!H2&*{8!`c+Pd@U9%Lisc>J(&L4NK4dkMrom0y=9H<!w4rI!83UG^aoaIL{5x8Wd%dKyKqjUw&xwDiO(io_*FeZEN>5<FbYhy?K&GqBb`qz=a>`KA^|^aMOSG5J;D=(y%O_gxL}>qA!_BQ~cXPMe>-K=X)&i?qFW$TFP(7^{Sj}c6ZEMc?wW2v(*>6atzbN0=<@<F2>A(ctg_~u-)}16gOU82=T2N(+UJcg(+a%84vYLF9*!*&F1*IQ>tFrnnoohJ|4S=rda2=K`=hxf`+a_kGt^8Kl42@4m;TnpIcrZwHzrCTJ!*$)bu9?QR3yf{ooYk{Xfk&o<!UrYoWI5@0oRH`l$qN29xJ*?k>1^3kKhBO&7b%xHpX}Bw+2uwUMkmJ2ipO(Wu1+2?PI(C+F0#LnC(?W!W^G1LsdkGO8WV!8qGHp%#v;#*iJGWeMEkL5oah#vUlXkh%RPlVy*<i`>36O6pP6)(m!>wmtyO(hQjQau?(-FmSeyj{n0FClEn3|V#t17iIMs>A@n;cTwtY84nPB{27EVqk?ZEZ8Rx?w$N^$_pprJ{ZKwHnzJOVq6;H5;1yqW`FlLmQ4)R{Eng?BODWBroPfp?OpPUeQci@`2I!}fPp<92HykiI3r_ExaiU4i%vnkp0}07ZE!^crraBjfF)y}{0B$|<uwvu-x}@%c(bD44tPl_m=-%_M>p?+e#40_QP~+ZBf1%z{FIR&iS4evkI9GTWUsrc0hLf<1PSRr-;Gwx#`~qpNa}3yQ3$BeJ3~w##^tXk?MPPMp&9&47{)^3ql?K}0nf4lrQi02fg^Gs4zbtFw~qZ~(}N+u3e#6w{wngoKzKHJ5u)w}&m>RwoxCQA`K8n0Rh4G~y;VlS_b>C8SJcZp%FGEW1+>M70=X4BTK}t4{sfL}&UKZ2t3IC`%w7oPS{VC^<l>Bc>eNNt(1*y(NLrX*cw01u>Q0)D<dXkfe_z#N}_4ci1Ig@~x@sMw!)RMWczrQ11I8=0vZpcWLo&ygmZ{74{PR_AS=bbz;6iD5~te+6?hF(_q_NOx50YpPn-~YroHm{(C`dv)n84`~YmKHAt2p*``J@$1AO3hu`es1_;<=$P<5CCfWw%9!n<fg4|cMLjjtp1>SBHuDFeEl+mQn$o*<6*j3sJQrkPo1G6KNxw$pe1kH;4cDA=OAS(5)w^Cmnw^Fw->6#iUonEE}2-jK7fY|_;4Fjg=6+rAJvvy;gzh3|jc4d`SfkIVX@gbMUsxH7V+wyzSQ9#*y>>bE>#q$ib^h01EtC$~1s1rQayj=)ZX7X~Fr<pYR%#Ro7o!qvHyQEKvDnWB<nwHJfaBmA^_MI1^j|buX(B3<?Z7=RG<s+(_2*Q}cEtjn#t}P^;?m_}#+Zj-@v$TmDE^lsF8&cHF<E^TwENWL5+i}tMpNeFafG5gy^w=yD7BeVWh=F$st+IMhZM!26d81M8YwOSa0Lw5mw+waq1sR8EH0#q{zzm_=7h##dunQ!Vd-ri|H=vhHl^hn?KV?kU)j9#mTp6*(fB&_8*xEm5zP%!9px1?cUXqdU9J|U@;~d)*;EHNWgPTLiL?M@4x$WON>6zuoXk6@%<prtq^rdy*G2Rzb7MkJ0o5jLFxx7WjbA^_#2%yGW%_4bwOSsKQ($dF~#yFdRomQb9(%?7Phis!Fjt+e}#h3dA)ZI{z@^HHG4c|i}#Ia+u+A_0O>J(E39CRew4V~p!X*YDyjvF>_*V#K{g1rr^oyN7+*}G<Wlv&WpNl>?w9wi%!E;QsKEs-q^gQs(;N?sS80d$1ufW%Vm;3Fy{EJCKEBIkO#j!`(fLq*ApyHI>EN(S$v)E&!_M_i3tqPXDX3y5;Tr}6x6mqYG~9VmStxn#rG2@<AekyFGH*_FEluXACpat4Z3<!o+&l$lltYiIC*Z{R_VZ8v~O0bQP`d!N)xt^Mci^2GgqYe_YGu+igY*AU>xYD(-h%3<7EeRD%Zo@bNV9(@(-tNDj-Ueq5Febv-g3)|aVM&?~{x;*x-<t95VOL`cow%|Nz{H)=5t)tj;@<ajx8jD2T0MB4pC&1^_7Wg@~=HEv~5r4Iv5`dp8uuud(hiY>d)^X}|Q}@<{Tg-3Y@rR~|%mo+M32x~<I3ubFAQhp&UpX$+yN)+(j<pt#pbB0VLfw@myG*_qyvk5f37+iIb+sa`$z$k-H8?R*sTG-i;izp%6@5TVT2!;!JBi&=ZAlePp*TQRQPHZwbqCA5uG9xYUQXj)krw3@tW=Bgn`9<*9uaNZI?KMshdsHLTJ&|<fszN7jXAA;lqQQ2pSp#kfIFkuW9}Xr9*4I-`ADf{SE@;sd(H2ha|;{n6W_5Z*;W7Nq+8cmsdKKn@%OZEs6)O2rgh9bsqU`?WojU|C)90oPwtMhz4}+B6XMUIbE|;PciE{Nl{|U(*KQdxFcE^<D<&!Vb<eR6wPEli0y0D=>SnH~+;xr!4X%yx$j{f-%>q!#YO|M8`}-i=MTmL;FE3@6=R!LAWN#ML^E(vH>}fNX8o3#xOe|za-Cyx?K~hOvC9u<k(R?)nQJ!BauJ9`!<t>vOsS&lD^v|+y<;nm18co%$$qiMD^G=S(EBgp4SAa((=qk}!J10Rz39j>+-*}s+WnL+MSZx|-5s;G7F{QFDe)tKMN?i$fQ_Rj8d9Le;r^rKenuVMzphBLYz~fVOmuP{<eJ#MN()9JoU=z0w72`@`3kKn|(U!3ScTqwsISeHyPWyWLLOj)0r=O$)QqwVhjPpWr>Nv7f1%S|nCoEs&#e{3_rpTo}!nnr~jVLvW6h$SkjxcxX^wJugg!t$c(g4KG{L|y)lh6(v0%c6KYz4fXH$d;w3!$fri`j}~2F-Q}`zN}1@V}KdS6cQ-n$bm%-BiGX2?gB))zr5i>mz?ASK?>X)t<&99i=s!L{_OHGQ!xK4$g10o-hh3>)>KWMal7ql4F^|`Nyg!{gx7YahJL>3g&#lZovrH>me=oP>)7YIiBOwY*Dlwk_wMDi0?YagT8;G*Q!Ry3Ek8~M6Q@_>nuceJ-o0z$J;ZgF~0?*j6&>k!KP`U>8bLEQVYkylwQe`c99cY!*kz=TUknm#rqm%9e<<Gys|Wmz|KV$i66SDQ&^k*MwxKqxQClRdcN%{R*)M+JblKrGFK0l)CBx%istU7T>n?Pp{DvYz!c*!jpP5!lo`<leMveQmGf!b+}@X|waZePXMF>TkdD_?CEImX`bf>M-9Cm`p_A3vvPh8<#67_d>Wjz8Ce<a7NZ22|r1}`VxOwkBH&6K#I|L^~k16u=>w-wv^9mxH+uGtyb#Q-&j8KN~xg+7MI&`F^7|zj*3a4Wte0sgvOm?Gm=jlj=^Baj-o>RrY<t}nrXeeh0c#KZoNu{10#!_=D%Irt;=i!-;aDP<y=L}W>;5q6!{Aif4|J<tgJgq)g8)he1t)rEWZ|XswQktJ|BwEWj?(x5a1I})#?^R7$!S^*5vKpuEgogNj%Z&H?ExX45#*`o`(pp}^%P3+$s$WI{F2GDPSYCkCZ>0L}<g`<_BdBpx8@l*&9U>Lt>_hsq!z|)gRPgzXxMu<2VuAVNeaWb7&l*=y-Wx;eQ#_>V!`Qdk2FV1hekVcQs2kTK7^_MLBk#DOSot?O>SMwF=Vy*b_;WK6<OhfL9-IL|(8oQMRB_^95Q;C`=Ob#vV7Hg(+7luA*b^X{3Z2SjY*vdxCYaJhN{-YxC-bwMo!2edFBOb1uKaHag?2i6gSr-1AgQ|Buni|nJk-~|vJ-<kO*9XN@UtIT6TCiGq!zhjiGjJ=NGWGFCeAKO;rLT=9!IlpVl&Y^Qq@s&SE4g<$9*S5>AtreM5Jt@nLnZPJLZT*IKHyeR#KC41Ph*P;;Hp}JNP3h(wqGc%WExY'),'Libraries/Compiler/lambdas.☾':strd('c%02z>u(cB5dY3!aeP2~mpGQ~5TQh})IjJ%1QPM+mk?QgoQoBcSmz6mR+W+z(i8;PIDzm82_TSoMHC83tI&Sfzr^_q_!GLbuiM)@JC1SEMgs5M?#}#Xc4l^FY!hF>*G5l$Yo<~#`tJDX$jQ^Gl!@$1B?m=}ABt0%bg^t&5d$HM{Lj`64h?-XJaTw&_*Cl1@X^5&WCta5>?o|1o5+~H9vLO$v7Y$&zI{16Z{S<_MJk=kr7ldswk3QUZ<3XdaTPyLqR%Uf8;C!?g~z2iWDV>y$X_9Epzn_%qcCZReNmfD!JlKh(~dVq-<v`}$!RP$9x;xO48e;P{1IQLyq587GGUqBa#eiX0{mp(V|)icF$R)`5HV&E8Zbv*ERyA)v`N^?Bp*6DY{o5k!@y*x9a#HQ7oH^?-<ieq`AjZt;5odGYXgS<%sxSJAUb=Z!q4Fc_@zlzb#^)ti}f=t8FsO38x++i{LV7jj;L!{Tng)FODdA;*_fPifg%7)Pv-a`a0OG@JoPdX(QGtbD%q1c6VKykshpin(M{J)uG1y_0)LV^r4U|I{)BLZ6CtWqa1iLBINr8{W2prkZ*?5fN<6a?wo6`u%_)zkooSdY+iu!*9clOpv4o7{$~dMPLoYFgUS<rswNlq8Id*=^IiGe@7ta;S6Sh;9kUSrdHkufZx<)c-psj~B<S8g1jRHQQj2kIx8Q-Idx{3b)8>?R5ny+omSGf)ZYm4ci;M(Wg)`6J?cQAtj0oTtfm5+#80|RrDyO~%DP8fCl{!smu0A(&wE*7#jQY=kzZMF^7t26b=hqGs5u~`0)o#~gOw4zP2GwVGu{XQm?eqqqrkSyXL2`WVft~qAYPw_SUm$%Haq;Q;?oZ_MZ6($DvY&y>+64->l5E>ru`rU^}2Q7?(E>+ARri?>Qomxf>zi8rDuPhU7tv*7YeOOi}%me=HV(<VwX|vJ7WZ8CHGuAFlg;Cko*eGV%Ax5eh_IhS`wO(D2#+Q>L`wPslC*GPJ_QV?-BAKJ}?U<s+e<!xs6Yr2QuI#ljg1p|9)E3B=P4UaQgkC<|+&tc?&EkK+fOynpQM6vUU9a3>p*Jj|%27s+vaq@@&&<DGS*}+eX!{jckfXd9Wn=V4n#0fVa{yDtcTD!;0lvzUH@6s?xVcWtDO<>0YMRANcs>Y8#h*daVro&FN{FdtJfltZ(kVyhb8uUn%p7L%E5#VPiy265DY}TEC7Et<j19*vW6B}!T6vFnf~-+-I2D36NX5~qY#=3n)|C=#EP0co07{!OK7ANNTa}s9gGUhYiK)_MGmy;D^=cyLB7b-RVBJi<nGU3MO*jt+IB!OW>2<(Rkb8jGYFC$m*Li@Q!}sx~Y3(kolOeE9a#(OQ0L$5XSSM6iP1cc0@>T0gXFHq4|ChUEGQq58f0FraSPc-+#Hn2<W;}~wP&QhFGP-L}RIP}#WXJFh?*cq_Q!Vi*R>M#5-}Lk8w&fW3rW?G<J^Yk#<8Vi({e|s_&v{6qb$5aM`wj8>c#}qOUE+g^l)XNQSy*pfLt3owBU<XyV?zk)2_Nd1a^gvG;xtyp{qdD0Dz`(DlMLUGh!`=&l#|?6{M2|@q*;4qIV4rd3u?O@Bz>n#ufhXmWE}9WT(87s$r-YYE`t^(<kF*wA$c}6kwhj&h<6l!5L9U09nn?XpfF;&MIk)BE3}c`>CWRTMAU{QIO{5R+8X~{<DZMolX1G{o^W`L#<K=ApPLQ3g{`FjY%O=^MG`XPIf&pGY7@-t_a{YaM776Ah(VNChUq5JC3+Mjbkr({ecnf%D7T2SK~IpzzYj7DL?^6Zzn9L56ZO4hbxqTr8r}4jcoEGzr9f9!v{6~BZDE;TD6BcFw0n5)w6tkEI^u6rfvd7Y2S!Bq>cfg}1`dSi=fu>c9Wm$)MDc=DDZM^xT&_Tev~j`mrg6ct9xPbG{V2rM-*Ee>5$?>AZ}876;*;Cb`t~b%DRB$0hRbmaueIv(el-!zP^;=_r9vzAIs7M{H(5%`<|D?}X>u{ZGJ2PQG@@hAza-%eB8rWgKZV2_`#w_C7ytt6-8AR3)&d{!^JaY1PEQkNzT(Q#_$pUuV^03ghwx`|P$~jXIaK~QxFDk(zFqh?M6GOc49E%V8@DtqX{@~5BF=QJC~T+9-biMv;mk~FhRLLI7qO5c)u_yg2+dn~QlC(TQ;otvd(Tdc6D3gOXsxL{;YvvWMK5DY=&e2xdw4Ss;-~E5ne=9R8lfoxTpuJYK-L%|K2B~Vb-`7-pt`^o5O(01K;GYlRQ!e_lkzF&#wXTxa(-R(qMgGp@tSwd0&yPhtcFY0_>y%?^P*jKBM}(3=Rq|T!a;gOIQ?+lg&i|Ga)vb;;IKlh$g9u%G+T=_?ZNkRYEObM#z-x)(>Nti5#ZVY%z^E#VnvMfn+SYMzkxSQ(Y_Q{)&Ix3iPr~hgWvxQlgL9aIwU7fL4FzNu6r4%OHxoIQdPo6OI|rfz7A-m&ZSC@O@bBj+OnM5fU(`T;d@z-yjBVl@7EYmm0<Q;j0F>2y8PqC3)5~Hetkj~zsEP=E4Q9FxePerMf?aalF3>85dWT}gf@s8p?z`x9V-!I+5Ws3rQ>qcD@T2DbV!c+<tQUZIXRN_GI4^e+mD~;f$~l085Pc#iiK<;^px5>2(ED-m>_S^q*uZ6`F{a_0d|1'),'Libraries/Compiler/expr.☾':strd('c%0=LZEq7t`a8d3zM!26TPsdzujCZzlEC#)U1BBh$%<CS*|Zj0+qd4d@U28N*Ypa6n9v-@OMpO2p(m~-DrqT|ZhlGqv7h(}edcv%cV``&rl=>3!tTz@^UU-9GP{_bqo0;%|Asw}-5q_WJUw&V^RN?zzVAh+BgaMW2F;VzppA)(9EZUFV(rA?!*7+QCnrj?-c;$x#4&*4$lgA}R%#%)=fl%wxUalcoZGi=-d{lTexo_>d(9RDTBmFDDH+>`;D;4OdfY`A2WV^@DfGjnGCaqIo2k(v9}QEZBXf#~!$(TENZ2~L)h&93K4r_N%ii&c$<mQZ6HphTIg+B~EZv~r;Gp{c$@waxOY}dqGlp_T`4!a{<Xs^`<KxJAe*Nk-2l+wUN3iV$`WTC8zMqSR<WoDS*L+-b(XnR3CqTJe1~-+!MIq+}3(9w_LV>9b`cYOgc`}Gu{E2=)7^mmxW%?uirYEm4lUY_=CW`a)OTkmg%FayxoM>&*Rr(oyDhCR+X6p<Q3SDT1C_?oHDhXp_KOkOE-Mx9&iHDQI;h2;u!+=wAjHm2$x%c#J@99Z%nn~>{a05es1&{JwbUa-2<pY;o+mEVI6l(W-Q$fT1pNxAY)Aaf`j5V((*B5Q;4;pJmlj}!p>qm?=#pL?Ygf<U>HV@5d75G7{o0aePOgA$xQFYo7FVO9Z^Yi2L&Rn4+EYd{-E4DanNbgV|n(bi;R?YUX1gmCySi<OlmT)lX*W9tCXKSyWv3l)R|CaGGRj-w6X!Vuz+8_Qey;iHv>c2C}fBRJIE9$i=TljhVTFMq!g=1U!%eBqaN>*QpTt1nc*u|t0Y846^ggb+?QNm=C*&7JMaVesV0JOwOPS8~-6Il_dYS>_FR!k*uG3#QevK;TibvbFw{rLpn?KcT$4@Jw3L5U4P^jBgUNc*Ke<&calOVD*}D4msDwe<}7!${{9P=DLcY8o`NLzkr+8x{WwulPTvYZ&^D&p&~`6=+)DnLf;VnFsVouEGs^cD&Jygf@2wmMxgmY<b-$9WQWL2PWoRlxlN0D%OnNH<0nk2dbsv?C@?C9F_%j;v!><pw9Z})RJB_LIanfF_bj2xdCW=*o#JgoC7Y=OZ18c<DDlacxXrg6d=D%k4qDhtrU2u^S{SVsw_*|+e*PVEe@7vAHitqk^lY+8%^j(i(x}3c14^mw5nkw4PN^1Wf#q-&li-B`-N#24ePf0B7JD>L+kzap&*!fmd9Qz#$sU=Y~4i-CM}S5hh7xBUna8QXEGN(zYBn5E|dS5VF*R7GeVBedXPdIgk=4s)@(%e#-g9epi9uLKani*$i}fjU!KKrGW4sb_UTZ}`6-%O=9WUA@#_-5UZGF8gqG-6bW`mzBaNlE4ECDY58tZ?KC;u8MIl7PCBaFvg0X`umWVJ`Mj{fEdYDAj#yrB(ec8w?I0_$3A?Jl;_seftA(>cECNYk>jaT-wQ&*_AT7F|*iVW~tVPmECfw9$WVbVubP9n{&(e73^ldN_lbO04C-eq{!2w_!h%GLitcd&BoI$?^CaqOyec^1b;Ac%>8Py-?(->X%FAQ=~STor9qaL`5<M+Y76Oieo7uWxsk*Sa@u8MSImV27?^l~8iPH@nNL-G?9d1ZR|Gz<FnNcO?s$mjpKGzj!ubSX0Q|G_k~$X*Cv&rhr?wpaM+%tR?EJbIE!eNmuC5Wo}a)dR|`7sjJ$cztu88U!*tfr=Az-X1@`dlYD}$#+4+mqHbq<aK~ggd0{S>#nXD!0NT_ip1gaMa!a~|+}0}LzO{H;%H$5euCY^FY1Bg}toq|l05Kvs!w=j|54a((Tj}(eO`<n=YT{}L?C0@8`sjW4W9RHPTP~8jg!Wy+zIOq=gn=P^fe^NA`<{Qg6~X{Xo%AQFf>@QZI9Qj}X2$w%fmhrcfGl}LE>Z$ujfoVfbVTQ~JQ@oSrcJhtX|%n#uuwmZ6Z%uZf{(=sMHG|&j<cy)z{^0D$6y|k8VBjCsb%XYbDCN<*Q==|=>#X}DbyQn9}HsHHD3@VY##S4b)D|&M^h8W9c|Ubs6fn8aZ9KjL^#4dQq|LZZp<iS7*$OCkd#t_)gqKJIjV;5`jHpD*LJLtfFBkJeTs4+2t~>_ZB)|8JnR6f<Rq>ReSn7mI(}e=EZPGwo;eqVp^83&X13|9-1N6?mLH(?{&2(OstgmzNm^=_v~sQ-MC9p7Uhf3cw|I^T)0a;W&mV|_Z&z1fYRozT#F}2_|GRLSuNxHe$vIQ+Aw|~6Q=7cg6^Jz6M5Hn8>BSA0U+znC?|~aX+;T`#XC^V0;69)z^S0dGW+;1Q`CkqPS9P!=ri>#B7da;y)sxVOL`{)<QM2WT)d-Age|roC!TA36pFw>55{jpgJvnGU(!>S<{DrW4z$qZQ!&NDa=Da?~6`;AITX^%m@r}G3#v)svIZXFhEL_GJwx&yG9W_mbiQH2oIX!|dQEHj$WN)b#zMt+@1bUTvYl*5%S%o$&Wsai3SPVl(c-vG52mgycLs^JINaEd3HXPOH^Jt*6xtCU@5X~~Zn@CWJuMG72_DgrXcFV6hs-aZx+(om%E!)7^p%-?=dFn&&`Sta+B;Y^kBYMjU3Mkd<eL(}zt-f&J=|09X#kFMpqM)LVs$_(Xk&w9L?$9miwfFG>%`0Kmses~C+TgB9xG&^&LtZy=FSIciE*cg)nA}SIl5l{~dMwnE*00asv}W{yWsXBk8BMb|C>n9m2r)+U<e20~Y1R<Z9r`J293&I$d?%wf;N^v+XY6LmQHtg={QCkMvViv9mGls@2PcA3+Ok{Spxb#LwP?M9oQXA)C@Qm^uI0R8lwcjEF467$M&Xh5vn6W}k^Aiu`>_)>h?J*T8!?qRM5{>~W3qIz2RDL}RIrO<BOo}%z=v}n@9hd%%tA`Z7|l(GIjS^8j+V$2oa}*YwLx}U#qr-isD^nQZ(Had#5I$4TL4?dwQ*hOTaR+qCFvb`y{WF)q0gpH%s8^<_za6;W7~Ln@cjDfcaEw;9>w(t`4waEagP'),'Libraries/Compiler/tree_txt.☾':strd('c$|$?-)j>=5Pr{Jv2VLq&(O1Pfe2|5YA|g|e}IsN<I>wSN3WM~x4{STp=l{ntU`Z?SQU%Zij|^NM8rPLf8t-_?B3p8Q(N>Nl4a)GnQvykSq7W1Jv)Do*|t2@re_;-3%1Ru2sx)FS@C;q$B&p{5=ssHjd7()WvbqoEY;`ja=lub!5b>j{i;N!m+-92jafW5Z(FTg&gC5v@`s@(xE+bm_5zm&Lf$@rUHD}bas)rGLuj9ppeKkIki?niu~&W}7lSZ!DLYGwVcCs*zd7DA$%w&fkz2%)>=^6&q);RY`Edi$(hf)P0=`^vS*@g^O0~`~09sVyPA?>Q;~Bgfp}WFG#Hg%NM1!`yG7u3pvJx`7z8CO_#SxG|USOJLD<+86m#}^<$?pI1OE`My9l{yxDVjsrgXcQ_C0dGFO@`KtbQ7^>o?(o@x_PJH=Yh+Ts2zg+EEY+Pa6jTYSu^szWiB!2@RUtADh$@)6fR5>=PpXd<;6M1EED-ZdaPI;z`6RrfDMz(^a5@e@!d_>hqthg&UJVVUyG{UKTtZFg-Lv8t?fEGdm$-Vi;0pYK{1VvbpSgmmS*xEw&AA^WT<W`AsCuMYqWl?o|^IZOw(Z|JAgK-5~qkEvOZ&7+^nTQ?N-EvBSe_4(wzj2XY0~={PLJ5aLg0&n6K`HS~kaZ?Y7@rUX89U8H<Dy3N`4YV;WG%G%VyeQNwG35+`s|hmxuCwf$AQ%N>_$aWL3|W2MX?9K#2;IQ76T&s9qcRmSKfmCN-GKEtkrG-Z3}7>(PDF8ce)M+vzeNYmMt3-Q8zV=_P5%WBQXVr8+i)|{2h4f}<x)J9>76B%4pubwqCYd|8IO?U&};Y2GzZh&zUG)2gF<*q9G5O$edK2@8N5rYjRa2mg&T30)8q+6DDyCcFrQ{9fTTCbT3Dupc<Wl7mkG3Y`#;6{#he3TIn@O^c}8osX4KV~fPH<TsxOK}LFVqS{=AFH}%P5'),'Libraries/Compiler/tree.☾':strd('c$|e)&5P4O6u<Yc7*Cm5Vrjd#Vh+{T53Jkb?yZEOyP0YrCLxnTb9508yP&wMu!;za?A3#!2N6BIf6O<N%p|Q_9B6s-=6(Kt?}fq(IGOI>r<^P4!K3Nq@d4-5iIYI^yhw#~T=FDJ4(E}i%q5P)@V~Sk42So|liP#wKEE>_4ffDahkH0umevVnt)5I#p55&FtyUlwO7{-V;1>@if12c6=F7!`8ZG*~ge#Zqz$LtaQ`T=0JR!P0hYR>Y%U8U7g!k2>F~Apc!?W?*dHt+TCh}z#Yn6!p33v(T@NGR{oa8#Ft&ROBpiQh@!&rOQJ`MX)Byfx+e5bmSuQZxJI}GMZ`327V+i=paH9oAaj%gIM8Vizw9Arz;qQN{D+!&F*M@%9W;x&Bg6O*{IsZ+NXVH_Cq)wYsWt_j8Ptdk7C@#PHuH26jHqCsm78gf_6I{vkQEs~6cE-6t}E?01&5*ITWg-3#RU9y+Ng83UW@fl9wXAKd#<&ltJEZPLb$g|LAWgXi`r(#Y+t2@oJf~QG}KiOz9&5~8&sghiDIr8q}Mu@65J#tMVEaS)UR!yY7w$al`9ffG=R4r^>IrgX1kWlL8OVYK9A#<5Tg2F&Zolk8erBT(c-qj96w3RyB&~|;ZyTj3#cA3%`z9N%tlO~JedbyTgVLk__RDIPqx)ZfUJFS>3G3zlOrz&gcdzN8zl_H<#d1gO5JrfS)ZbR-g8`;H1c5NeSMUk1U(}r{V3O?9*Q+r`e*ErX9taS|%e*w5_74Q'),'Libraries/Compiler/node_types.☾':strd('c$}?R-A)@v6u##v=5A+GmqMf}l_g&gpiNaLMoEw&5wu$DHL>cyu9wzQRVh#sXbKTwftm=EI4(2@6sc8JrBM<tj?|mJ1uxJ%LeKoI*X!AhMT?Zo?#?;ieCM2RXU@9l)+(g9P|bU_TDd_=m3qzfNZ!uhafT=?!-J_CSEyyNtIw}a<*whfENax9`T4SQ@uPXyu2|gBNRjz+ZO$$?sF@;$VdDSXJ2yp5bLPX**?2V1X?j+%=2mR)zrfV$mS@kE9UX?S9h;c=EStMLmc3z(XD7$5p%(}HVv<<~PMS4~r6x&d*yAlYf@Ny_^XE3MWBk2=@Iyldr$}H4et{?S0<_@~{Fow*jB&e)HVvnqF$i9u!3o^Ye2Qy0DRMy=Zky>Lf`1h5!vR}@;^Ph2g|}$F0k73aN<|4k9P}sLs)Ms^Jd)#c(;WWBEqM;(OVRu#yr7B?EW#e_Qlw*=<b&YWME;Bby05`&PGh)OUTEAAkJ+*uK+t4=uH!AZRrz>kgjJ*s>+maQU$!fA1)In$q{-#nE!yzx{FkoEjLBA%E}Zv6c+7LV1P5?P=W5Lqktq1+1^8(;Zo@q)ZilB*gy%4d6QO{$+J;Sdo$8X|OKeeDDMk%17h#>kiAiZevfxWe=g?xjfIOj#(1PD+gk#+<<ORbuIwKy=qCkj&js?6p+q!G8yfaalw3`YcHolk$NUB@t;JH|>!>q(TLu5|e;4z#?S#lANm{<-rhf_Q7ATl*NtCT%4nWdv9dlFht#?wp_UX$Oc@oxW7#|Rc~GH<<+)u=o99?O8C4@YqfeW_a?4$sB3TUJS>X#}<IQth+46|xG^JdUTi@&C}fJv}lqQoQ7R{K-H(&(?PavI}4@=>zM;2lli-Fg3LknYyTtxsAF#4ZU@omXC54h4tn5M2*ytyR4z!USDo|J<3W%fVW6NsLhAAP@9Bm_e1d<RTnA|c}j<$CG1g*<5yqXZoj9jw0<Md)X9fEvD_N%)>G0KZivgSPGN;!3>R-XzIf+*z5C>Y@9$tbL&JxI8m{Q2xECLdA1}qVL8a*9wl2!~RE{0(nWTt%m3j|P3Gz%i^Klbi^=Kp2k5j9UBhJ;_1XIK@yy3NN!D5DS9G|{U>1YZWfBPLjgj?_jKT6)f_v%o_;y0xrR^;NVriR&}oK#^RB!<`UTwQoA>3lp;j+~}8M|%+_3iN3r7<MKV9a<FSK#uL?@;Po*hvrAP4VEq2)2B;Gsc%C{M62ZOvJNeFTT4VcTWxVL?S7-tU9^4TqLVvKNOQphz5|-!u0+y(5}~V-v6V=dJ=X=_C*Oh4P{vxcUFrR7pz@xr-c6#U0^N&LyA=nTctSPGr9Ar#xe%?DzJk!x3nAB?HnxhQ;YR~fYLIKSsuMK+;bViUt{9ta*GrM$u2v7-u%2I)m+iV{x34F5wGb#o8Q@n73&9MQ6qQh6MZPSe>EViGJ?&9=FI>W*WvaH;NE_k|RBiAO|Maj5PTrEl-m~kz+uwTGe>C@CY)3KVH&+;Bdr99JD0y`vWj=^`B@Pqi_tz$8Rk!hjxuFx{;|P4`ec{i$b#>@yQvCvsgH$)gISW0F$8o3=i3d3efsD@f6fAmJ#xzj1_p`hQoBZSb?4@s&nJSuMA?a_GOJ3wFB$;p+&lPxGzQOq#!}s0(PpkOvhx4(HSN<-~WPC_T-mzh&h?C(?OIVeiz=drVCN*g;lbf<`j$O`9&J5O^EW<v&*efyZ$%#436DfY}2)_f*BOCiOj42)bd?5CgCP#e)_e|X{38InLxCjDzm%j6ab~CDhV!sd^#XzmG?3}`@pbv`;Ef%`1g_fe)I5l`M=UzhW$H{q!J;YRMrBhSB3-{&xx*V6)$Qy2cC{g3ubT(@Qug|8O;$cl?$HphG<gyc!*U{o%9K&HS'),'Libraries/peggle2/gram_tools.☾':strd('c%0Q4ZExJR`MZAwTfh)?Ru6a1wgN_OMb~6#uyrvK2N>YEg6_;a3(-jjNnX!gH#Cmp3{BG}X%aYV+SDnUwQ!K`B{iC$Sw9f_v=93Y^)K1;P^3u7C&!NMy$FVne8}g8&l?|-l&|pjrcb|4T^Cy?-k3glYQ}Y`^^XgdLwZ5f_JV}k4zVm7{)^csr>SkvzSNu>qgB{_&ky&5ANPiCFABO|8b|vgl(J#!cB8oOrMn`t&OhLf$W)8a!0Wf?Ju-Ai4WQTfWoTrrn^WYClgE(dP5u>s3RKql8b9CS%kXpCru-tmPDkO{Vk&@a+ZMd8@-NH0_P}CdNc=A0=K-{d{19jp79<RTcld2O1da@muJK#crZcUXc#&x)^&U&9#XvE?{hf{K7z)8c!S*`;u5SvbfKwzBoGO5ANTFbklz_ZL1ow+dE`?){jm@(z4nE`?CK?*xjy*L-;LG7Chn9*ORB)QXUSKQck_vt?OBdrXXP=|3@K5-+{E|jQ6>2mINA_83wlSx9F7q4wTREi;YPAN|Gg#(ss-ShIoDhJBuX{lLQ-1NaS7&k#^}%cs_#H-n6@|cV(w@VAfReD(OVc=`{)^*uQjvjn(`Yx8%O5-bOL_!+{>a?eC{eX(9{eAf1_Jnhz&4W(LGv8CZ6FOCmTgEBEA_A9*hhS`#NmMKhDl6_@OhRjk%3(@MyB7cA1A4s`135u^AY;zM^l-pH)+;YrbcB_8VD}Af-!gj9G9TrHiqh(HbT^D0^%pao(JbUv=)pG<yt(-jSkm`*7oT`ds}#(Lr2F;O$YKQ4IQ2)*7+6w=)aTcwkgn5A1maXtNeZbolZENXs~o>Dv7#Xpz8v&Tm0*yW^VDPa!s&gurTp8a-Erhz6aOPbHMJ6IWi$RIixVs)FTJ6bf^nS$CO`7UsOORU-|A-_L%>Df2zZ|4`rUpmv29(ZUr$@tI(G6JVcfHU83h?Wm-O#qck<j<Y-DqOiGhQN=FKm{)4vDme`FAV}?fscMv6h>PKNxHs9BIPQc#XLV2vVBgFUu604}+A!hU1y<y8u$|0|vIaS1Svft}dvJcv7qQ(SJXh48%8~4la`4bxWA#8<GC>Z{nzsH~0Dk~=_Sp#Zp?1>b&%D>PlMyo1}!XWB+0ZDSuTMK?5?RIxInKS%GbipT%l2W*8dIjf9%<Pq$6PJeDa8lfc4J$+41pbrLL`(Z{HbG;vaIw!~FJ)9oB=(3T-z|%xfIkki1q@N}pSH^Bq&R)gp_MpgRgjkos&j}B%*)f7I1L3mh(IvEcFeqU1;xERIz;djKJj)j8kWIzZ_uK*XyM^(=qGNn5XEW5$<SD(7bnaOSV&$dXx$G7iz&kKr1_Q?hpyk<iKGalWr*Wd^ANmZ(=bYjlExI)nnun9IP}s5f*ky?N5+$*<B3Ja2^}S)Qz4-`rgr@xaMcudAqrUHw!Osflw(Tfbs^hsx5ekHZTW{;{@GUE!oX*{t#GBt7&}<#qS%727tRwwM*@o#@Sek@hD0lhUSxAvb?**)M72dbJM0g=*z3E=V%%f#lCd`k^j5Yi5&f4S*-z~u`({X{NuJ?FT0#>kuT;@~B0vnco+;(V9h6hZ5FNY1@UkAw-54S*0v|qL_cZi@vI<Aa{8Pq;@SpMl|GC^W_fk>RD8D?Ia;3s(R5RaywS1|vTE4W;B^<<Q8o#Wz5aA+hC|W=W7jd*jf~p*ot)ZftK)ansDFn6pAR1^nB<gNUjlH{!Y6Pfiki#LdZ0+|7;sBhkn0Knv+G04*Vi%KJIZL5#?+Ia-`5z(LWr2ygBQE5ot{=`nd-pnp%FFJcf9}EYz=&96RQCo026Skw!%!5qbRxF*$@;{eSc}sR-ehg^d(@O66C&pw_eXHP$#3PHNv%fsLtHutP%r_VFb)@BJ3JH6reot}yi?d|MD_oaUl2*@9@b4_G#(TxCUo?_f%`e6FRuAz>2#iN81DytJ3E)G@@u-B5}0z}GAwpk4?VDH>||x(eOh>wk<c6HdiwcdDSx-P!N1}wIiaCE`@BzQm%y%|U27Z-vLs!9z<RxaP38rcTz)%Q9Eg{Vb)dJ=lFO#n*|41Giyxp7(jvd#diU}8=`+*g6I<^-c{Wbl!1>v(aPXN6a47xPg`^YvgA_Wzd+QHh0yP_ckXrqnvu8sfX4iHiXE`K)rvZ^$!u!7A>y&SRen21v`3xbbv$&N#v*n?Bng5xu7v7Vmq~=hEV8@vCqu($$jlE<63YIJm>fIDos#aj-<{VMhLqeiyOLg%gFLg+#H7j3)tg~ktjYhZea+BpP&zddF$J;&9YT<r8hmTXTzK4b9&LRpxP{RrNTs3Hwcf4)KE}@W`xPbd>IU-AUS?au9CLr}kW!PWV@hOOJTVmUKPVt*%@i7Fj;4S6{Gbv}14OMhtv;Z7_<PCsB!lZ?1Lk5Zrr&6FOZ*9lkxt)CzXTVIk)@J)h7!+IgFThL@Ae6rH!q)wjal3BU5LTFo1BKYZK+kfLbXB>+(fMgYx~#n0knV{R8Lp|5EoNDCOYMb1w~zQ=fReN|C?`y8yO3$dvX|mlj~#Q5{~BM5PrEKP-iKkQ&t_U02ch_AVaZnw(HAeqmb^56q+lS3rJN>%iI+}G-sEg(*aHQ7pkQnKb_T<z-W;~3U~7uU6~*_8<U8`>3#N>OZ^J0h%x09Y#4KmqEt!}nbF(G4u6Q7z+KFL6cQi(p<1NR`___8oAD0HmI$}&6`(Z>i1-x*b0E30Tm{ED`gV~j1D(q4Q=X4=w8b#<OGV%5>=Nd8jVpX2UEyj#0BVSsC;wXfr*u3x;18w$Aop0tuoQ_0qSMG>NY&1*nuvn@zqlhXdRAi8=AE&UhK3-rz8Z$*pq#@)}u|K|8erhsn0|<ye@w?PYqCWd!^Ue?7T!+7ZuA`LAhS%+~y!GR}^^@(RFSD)X<#Xz4C8;{NuI~1%Q+P9y2j!j;7BW$NS{0J=5d9&(w5sg}M*j_SYwZI'),'Libraries/Ń.☾':strd('c$~c&ZExGg`MZC`?L)w$#|V<`G?)N=Fq{k<wkC$_0s|aDVCa*>jg~Z$PURH^Vx?||bXyw73A&|SoMp+nt;mKJ8-^j-J{<N(^h@?UcSrK>NJ)<E)&?w!_uTXTdS}W%<abx!`2p>8@aczduU=hS?{uh>vSHfk_Tz0obv&{a^{@L;LS2tIjthUqwyUeubvMp8+H>8wzfFRE6tN%;`@MvO+k<|bl1=vW9Y*|w@TdF}{uTcZeBS4Kb8|uDC-8QkA2jC(`~dwV>ZeJkLz*oD<bkLY;2#F`<^;?p>yl0<?1d>X2n;;r2mF;sQjg3B9$_s$;=kwnu0$x1X2NB_8RPH@C}`iR0D@TnOb4LA#>RZmCSjKZghdG>8*Pugef1IrzV7o!9_rvzzSp|a?=hFU2*^kXN)T+zEev%_6PEgE8cX(nbeX=D(Shd++H>9AsJG#}4ZozpESm6*D)<ErreVS_v@>g8y8L5$5zKwDof$0X_fkLXWj2fa?dzL9DGW1gk|7Cu`I{O;nfV@Q;h%Kq;nQdQx2}}jgbcvuib~7|aW#b|asGFko=e7uqjQNne)0u8KKZjl&XL?)wUqQ@;*5W}?|3>N+RG9D7k{a_6Z)L%7W6?`Vam2A3h9yEX4%s~g2Fe3+Vif|KcYN_{x#h%g6<dF1z&z|bBf|M1+-dZSWAnI5$jFTCx6E8@_*|>6x)E~iFUv>YnK+WTbTwmEr(i|#w^{5b>nY@ZGHbHi>B^}^+}sS(|V>5vFDLMeKHw~1txIM6hpGtPYEs+D{q!g(l-jSl96?Of)ny%WUt`t_+cmH$4Hj!jQFuUN4jb-5KbEO2fNkbQFa5Ff}2@x%K6vxNah>3N2V++Jet?%)+!)S?|}Ui{ww~ffMhk~ZDIk)LM|A@g8z7yBq!k;cKp|fbgzV@CJ0LjOxB_5Yni-Y2g|ui=Q$QV6%72i2*=~rX|oKE0N}RCc9GTR=L!GPJzL+>#mgyaGIisD4)PIy?vdCdgP66x4;>S@7X(XZy|o_iSeYiytYSuyqN{8jYpGn2(g-Nju8vf^vBMJfRQnIEwD3<;gtTVnbprK8tW({T8YN)Bq$8=@HN-W6Gzp7}A-&0<WqMI{nxSS>NjEZZ>~X9$S2R|*<B?Q`-9yQx7uHh4Xnz_mzM0Gnpso%2gNSug!2o`THk$P|)z=p_e=vZr2q767M3v02VVMzl?c2}`v-o@OMi?>0OW6{11@R3cs+l(XVMDqR5SRcksrAT;NN=^EU54}{x?;Y?T`QuY6H=E6BS7d$%&fPw&0;@gfTawndlq^~FaZXCupte5JFF5Qx73Q3PeScE2HdA>&Z^@0Bwmhhn{x&>Of{g)d;D+HBCAB8T32P(CK+hgG|&vZ)AG2kX(h<+S*lx;t1@e3YnBeRM4lR%yqjd%yfT$T37r?XzA%%z$hF7F>oVyUsU3+MBo#4@jzQ)_{yEGocjO*9M_F0Fn_z6iVEzl%!#22^XhCjiDz6+e>+5B}@K8~LvND3>og6O!wbl=4EXmy_JUG-WL35kH<dBrA>!f-rQp8jKfPXD2o?EI;S-&E%R4Pq6@x*eOwk)#==~F9t%IG~ET2NA2HkY1{b<<HwixS`w;jCB*WXjg9sLpJZ3yENqJ%ofX&<G7<;VD{yz}04}ZrIx_83%(!#)lp&YZZgmT6LJvHB{0@yWG{3e6upX)~5C-CH0jJ71X3)LL5yLkiy`JZuUhnHd`bU-<qoT6^Rxw00I;VEr6W5r(;!5Q3kKMVhYPeep<4eXp}~FT*(eWH^&UV=!%lLa6Z_Omv0)#;jAWkz&I7oD2Qi6ldIfuMRiXuINk|{g_Un;%FOi`Zy!53&CWfi$~&rD%R{sg<iLA{dNz_M3>cNOuKatx;kGNA_i34Ac=}9I;lfodTh_)5D>mqdJ$TfkuT^JW4Z4OFE9^9}9_pu0gMOl&JQ-6fp6A{|lR1uEou?<M!jJ~GNBo&cDdy->47-}awZ8tD<wrLa4p_;i5xc(!9&eVJlWY_{8VF~efU8I$--X?&nwgXaD&uIu#R=s&CX(FBXcr8}>?Vs7wn=XqVi#Q;&@HSK1vmV-%0`wk%o38$uno*&le1nes16`8xCJ%IkzEh)r_$pU?V&BG<7nCDn-TJSW2%&Ils%O2@!1RC_2XWDliA&1E6bH5{*pgXrx@ZHHDLtnJ^n;wS9my59;<4$9aN&C1Gs8@)OiNJurs#8iJv&QPe62JBRZ-;bfgd+p+QOxFGzV}T_0J(I7vH^rIYeNGHGs`G%ukWK#2W@|88=f&rBYvYy-fxoFC-EoqSL{%M&77#Q0kh@r|54E=eArTJqSIJPFHAU%omiYJ_0|?a0z(P#!RM!zg9(<dZ=>CdLx<v6{{9^M_gwf~9oCpYs>^@wMWtVoQFW?I)ddm?Ak<R5edtH74&;6Pnkck0FRgNboWL3&k6}YdZ_|`uDo^IzC+Jjz2n(Z|e1~d~@yHIy~1KOAQ6uty>EV`GRO3_hGKa()&stB~yB3x$=l^d9Ct@Znxry4qwOC>&0m&clv~{*#wW*tKC~;n#%4{Z;u_&kK+~xO2WOw)qaOjd+t!~UE#PHF>Ga@nF&lvC#?fPlTG~MZWI_f<gfWxqKCw2d*4~dOV)w&f$SBXa|!;6i(A;TyawB#ztGy|UE^*6;9CXwu4^?nicN9zzQ_N{U*|XPu}dZMh#Ke%LGge~b+x({sa09Bdt&8*sNCoLQ<~kQjNs!AmB6m(@E`NX;zas${ttfS5%u&`nmvcZ`;2|nMyvWD*RaE1%DZiWgl0Sl2+-j8)(gC<rmQv)R+b)YF`lG;@UuAIq;SLlf34@}y3@M3>-{06@>*(Td7Y}!vS=D=t5p|3wbU?EM%eI84b<sgxZp?~C^|(K<K_N&jH@Qo-|?y&N6stDfMl!XK#V(6P*fjyIglIb7rTym<uUzgqsUUyC!F!&t?|RZj}Jc^AAUJL9LfJcxV!T18l?>n1b^S@ZaGcjG#bA1fth)PR$lYl*|o)p|AF7HzP1?gKk_@3sYvX4S(%Pt>6zWQV@k?)J+PLRX5WM4&Xd_)yzuP6v4&GSS5yKQ4r06HE_foK2zx9+22r<$`>Rkp5SaJ)uPG#T843qt3AHK?&?Zj3xlvVEn)7d!SCH?tNMq`Gn#3Ux3jcH97yA)uN|7cZ`b&7vXK07gYo&SRMzrRc3j$2kk0l5=jPO*MQp%|%s~p%b93lsQ;!lhTv$!DXCJL(@@#MdyEnm9Sx%?CS*R*$F7T5k6jXD^`jtXWdaah_?2CWXhpejPM3wV6xq&Jv?r_N9N_?+GUqhDcdYN}&Ds1QxEvEY%VHhf9m^F_2q{r(n)>*W9Ja@`C++uCxp=LJV!S)56_;Sr#|hz!gi=(-RH{|6w!jLQ'),'Libraries/peggle2/main.☾':strd('c%0=t{cjt`mA~t+*t#%wmtqJ>j+3i!JYOn1>EY@R$Vz<x#VlxQB{3#<+2zWjFR{^l*bVaOB({?#j%%X`>?TIiG-&Ds&K1bw@?YE!)n9V&V`g?{cSupTY+rF~Bk%6KdGo&J&6}Aw<7KaAuOB=93oi)p>E8|?JG!_O1fKifueeobts9?gbqAhbbzIknzXW~snCJVA$7Y*T-l*DXI81}pIO(<0`$5xgwb#Q55TwbO`6&l}onAjqQYQ)5!lBa|z{6BHY=`~S$!=tCWgp?U>>@nhEx-$4Z?GP32GnejwoZ0KXTI)u-B$19N{dmv35~y;y_>x~?__Uef5=|;;Pw6N9gn{PZ34Pebx!9nuV$CB>)E>ub;a|&)4o%wIN9fUg<;h>Gmpq`X218`y@TrB!E(y~xz1k41B3v=L^Os?fcEJJ;=2Jn-O@=N0;2QTdmdB>>xYjX6zx*=53`r*N8%{-fr_R2QnC?hSl$W{4HZvKt%R#s;hpR&Z&1%(f|`HuS#GQlM^s@^uF6-ZGaw8Mia*KJ@wAnsooLNTJH0S*eFdO54i9f;cRd90bBH8NH<D;d$F_Iiq;Y)8**jnX4XQ?6=P^l;Kx5(XUqyvgQn^nYuO+Qs(2k?iVUnWaE@$s$cLm>G)ar#n682jC0nsYeNpPQLAEKZ?&OY<pu-gmb<&C+SnV;cfiyvEqL1!%r+TDoX*OGXnA9SK9OtcR!+WFRNx3*rpxpm<p{(bGH>q{<{mJFj51kO8()>>M1DxP|6%rxPPPYO~HPQC89f4_9mb;9l-)ar({#0q<^2+3%j3fRTpvhVWGgKnoCdb3p)F_`Jnl5ax@oC%Z#3|vF88xGp7zR?fCsMEUpKi|3Y&ajq*{cZ~yoO3FG^Ww+gEmB{76<>tys?TYaVX+Zv1@)eUD;w=Fc)qA}HXY%iR9V#l3BQy5o~!^1|NW3R<AYGJBrbfNrLO>fy-+ZR1r=|h@R?<}k7Xz&DgEBTL%;N9eMG9r1L-d0#EL%hZFa$X8oXxc>u|9W|6g6R3imMf8!lQLGzSdQ-|PIGV+y-Et}ic)$8`&FnRu_uFVp2R(WXxv<HLw%uYA43X6d;yra{5xcy6zJe=p6JIUh#|k-}wH-*^3yf<Hfj61Np|kzLbxR0lcPTCw#Fvuk%EN4mgv-0Ou=%8qT5|2g6MR)TRD(lL5o6sJ1gR<z>4Q2M&&D14N`tj|RfvW<QztS#9-6LqfVlSjQZU$@JSNKs6;<8Bw6eHgUj?U;vF?aB}UW4(#|<hEVyZ7ob&X_|P_H_Xa1@)N!WDF*pF*}H0xhu4o_Z1Z7sQXW>+%!3Z}p>3A<5WSGj@6h+z(2DfdQYBsv!$|Ft0~RkBEx~xX&vN2~q)QKl?`&*5AV73OybTK6@6))SGbNF`#>c@mKHi)fr30ndek%bkVQlt}*c`n#eFRJfd@uOfssk@`<bcOG{b&bHf3z$2425EJ@^P+EjQy_op6I&(xbW<v2V*Uud*LhvrkAp>>EG|OS8$B`<b$p2-~5QWAlkdLR?53`Wzt7e2w}Ywqr$yPcNPNxa%q+BT%l*9pAw;iSwL*Ew9p~N+r+3zJqc^zOZuH|=uJl|GLSzsne7^gN|B_)v80!5bi;vQpKUwodEn{%+G?8gRXEpA!qv`@eb``Q6`ozA6LGYS0TBn|-ZXR`fx{i7iCY4u=u3ffl;dHwJc4>`7Ds)FMh`u4>hMJgr3TReTEK2AjWeXLGpMg2ss!EY8FW>sdFqU{)ov^Gbbr8u3-*oRc^Aq%(Tb&9#IoV9yK;QegsI|U_B>Re(+iAJ_Zm`f5cQGLQ&pu2q?sz3-IL1-u1aao(3(!7;qs{Mk=$!z82B<)I(W1^ng^-q1JY28L{i@jQdJS9YD$(unQ}j7Ax6bx?Fvb!u?z#pVKLhFO>7BTgo%%_xPc4tG9d$g(I#+YgivGa>IcBvw8JHOS1S$k($9|`n$2Em=uVqO_+{TmTGs}*Q`+;=Qr-%W5uG&bdA4z3cGMWL4?NmF_GrQzP>Vd{CC%Vm@y+b}s+#l<aOxT$Se=9NmGI=oTAhb2F*#IYM?T(ul6{lC?n&toPTw%a7tX@#j2K#I3Bl^3!O8w*QYY=voc&J--td^%oB&`3XU4Or&zvVYW#{oX|LzOzY_5az<+Xr6*=9vlQ0vEi4}6v!CNGWR<mOI>8?-yb1r(y4nhOg|g_I3|S&T`nm|(k2N!kq?X%$w`UF&3Qb|;fDvW)_jzY>1&PWFXI^U*)6Dg4XX7uoysa%qQO0VDQvU&t0$1RS?8^5qL5{69zjpO!<|+64K+3_wyiB?qr^C;Km42Fq@P&$;w6_=wfDx;wKvL(wPKMChiF|6iPcc1$Z)b9b0ot18?W!B0Ed8o;j#ZK4W*qt*SZ*xpK<CY_#;e${z$zwUQ<)#fWTs=Uo~`2_>Hp;k0XQ3&G&VNxhtB(zE`e3X4lOALZ^omKKt@M~Iv49&)XM$Jp1wP~*&dS#LlG_)ITOa4X#KNHhM{!19fE|EnuRHcz(@P{*v9w}4Gw$^K<?e*N@5-ImD>t1cpZ$+L@@q6$8mCSL5Umklk;@BCAo^zAp9qwej#5a=@=ar^4!i%deGpQfP9}gp_pE2^2y)J52Rgb6E<OB>~J{v{VTiJ&@rAnBkz$=0wMpY&ge`2@`hiM3raYMKfp=Kc((b+%qo4yst<mM7R2)`kJCzG&sYK$!#^5=g)YZ_z9oZpmcc`LiRi^gIQ66pd`NN|v`OuaR{b3V?uZR)1=C8F7`<VV_{w^tEzK;xM{Qd!*Q&RBU+!<3zuqSv}r^jZ;*$rJdjnL=oE&z^>2i+>D1!*9FeWuiytTTtQ;-?OkHcA@v{U4|B#9=aeOfN$J=&+<^6r0G~HE-o;;(=KrZU&}KD!=qR{Mq5Oz$`4Jn1leZyHKB-v@3}A8m}He49j<z{F=Jv954Y>_UG6l^sP54RW7~NuYW|*mRCy(2QV+FVj8e98(P`Vh^Do8qw^6L^#J#l*=6QX3_dBz_JMEnIM-rH|Yps4CO;PVdxH9FBa8J0wJ9f6Vy>=elO!C6$^_1DB);+CmbHezAkrn&qM6>LMs{SY@CEKcpo6oyX&g`ygORaB>(Z>#SF=ObWtcMXgn0Z(_&<*r}ZEx`&of{LnyDLRHtv}qpFJkk-VE0{Gq1S(L?Y<~|NK}6EfrUzuyCQVCYkl_tvT=0`8)5`=f6>7V7>9P}c6BXs_qmh_7Zl_1j#{sEDx~eCftRSgvJ2U#MjoTS3Gzp^gGOJW9e@^Dgt+1GO<sWDH=GwmJ-I7ErE*s~>h(p`c`ZA?@YGVCteMD-bSV2<_FJINud2Okl{G44m1uIKbcHuCwYRF0Gd}l?1RG4vFnFu-zwgaEwEa5m=*%%g@A;hh1%yp7Y2&E=f;|savBprB2}*3n%Oa6<@foG0X(=Xu6p6(uR|dYmn_W}N!yl@GW6gv&dubau;oWJ@AF!uac?eTAwr>(KXaO_!1S%?OB<7|d8v<ct?O!WQQdx?E{|5JkJNPM~A&x3mlF}CXxS@}6=@FhlsZW+K7q-n4DUotCB}il@656VevgX7HbEGFs+D`o#WK5bBf!yx@`=yJ;-5CRgOzka+ND}FnvuePcKFuz9x&uOi=pIKexuBKk{Yy}Pe{*3I^?hJc(wq`DfC}>5r67r8Jl|mCKx5}akAr>eHYk-J{Hmk6mg!bX5*nMV=M4?jloCJ`tn#PyugKo`B)bD%&hVYmWs)zzQwrCzOI7S#SF^9`#L%7WuCIB@S1nm*S19XHWSxoqYu+^VebWPN<I;o`S+c=|m^>eRJ&0FJ)d<o!NRu!W8~wt8zs=zXhq$19Jl8=dI_hFfO<EnOyV~k>!xcUSAx5SoZ0iG4h4lT#{5FjVumWEF#isd56BFzS;*;eh$n`DJ?MLmW&lkJ0+@#<7&E2inUWLDInf`n|>>eY1m38r*mBYD7In)JhoIA;bL15)+DtFSDmFb`+e<Ii#y@AT<{0(hRgo$c2Xce;VV>vQ_4T(8bQrMWF;cjA8$X|J>A<ueYEhJ48=Lj8E;xdnBs)Px@pwhBN&9w^nr4Bjam!5H?!Pn72h9;#2b{CWvEc;2m{v|OJB_OvKD!5rxnLdXD>e=yzdp<YZQE3TgHAQ`m&f<78zRf;vjjXRTrEoQENG^<5fR0KbD&S#ZRHjEuq0&GsLm^_a+@T7$m^2GUjxS&y2y@m^sQszpr&<#B;?p7L%3_e~o8lny$#J*W<G%2t>eNpr5<nOUl(q)z;h@fQbn%fpc<}3uaFBN5s8HIC<5R8mu(cw;ccON8V<imw@t~u_1Mc>zpc_VO>ALuI@X*hneWsAk_p<DroP_li3W?yvEaMf3+;2;--jDf67#ZhHvQJLGKH#2}>9Itngj#-fW@ct}X7=Rcn2Tw04YLE6rJon&+?_Q}E#WcCV8Che+n&vML8Ki+2RJ)wRmXBDA=M8h*Z|r#fLf@7EV+d+P(PVb1^+5?S8=!~X8u2+1!((?V2#I@BK+eT%svx-)&@U17%XJ#KMAAGlluBwafW~$tSyd1@WH&2GuKqsE(g&1VG(gUkquGyx3az&mVi8WQ32#`uhb8WA@Xu|-Yd_?Rln@iXXeY+Vd}PT=(Z!KmM>+WixgV&`r0`eU+ec?A*6H}-ko<kXK8Y5#+H{ceUO#|%CRm_!luRaA39OTw;m+fLF}I|M{2V6D12B!55n$2HmuU0LFl@ZVTVCMj6SWViT}MFDk>hBGP}9(G`5<?%+&5x&7)JPb)i*`&Z-;R?A&N?TPI`qkVa*-(@n#KbY0cj@psmL$1la*8y7Ye{9od%NT0=xn5I{7AY?nPW~hTc9+I$FDo;#`q46012Lf-GZ5n?IGInnJrLuM$rJYEVHnn{k+h)?*<tV!|=tP6G6~Qdxv|J~&MAi#(OXPHMVU<Xw-h@MYxuz(mQ11FSmNi@{jxOS`SXPOIZq35`=*>`7uU)KXuVa(&<Yv3D3&v?N#DZxVmUtY?3`1NC(;yvMO|g8!{Kry0Sr;wFl?df;oGX^UD2}>uyVZ5NHai&Yt>sUJ$wHc4GhE7Zc5)st4(jeSd1r#~gCvaX7L3N?5|rRVW06_j8d2(Uqr(h^Nii)<L7m%bB~iQ*4z@XDnU#-I?rhI?OxS{rf(HA%ehLlI%VTP{c2`E62M}iK0HMKAm&59Rte86QE|U%_(klpqws@J6-!S~lGhAwnc<`x}B=P3p9s@Lkb_j@x{4m<+g-I(7N4c8O!=rTw)Q6zb-h$QIjIg~e4-)FLvQehhF)Gg9Z=%}nZKrCg8f^eJeVSuUm^uuQPn)zT-+KCNyGao(7(?yt=f<6=zmXO}wOK~BaQMpFp~rMkYlj}wK~0~!AB4W&+}%~j>5XN0^x(Q_n=_rES|u+pHp|<JDh&dyc*8;rC$Bz|`xWp37Yz0FEI`~e7Nr<fu5asgKmBlRtsBk-Ft~TU#VU2QFiNX*B((1KTAj!>mWQgedL@>PDivB9x>Y&?YM|jkt!*9Al1YcN9QR_4x1OrbVj~f`ocM0XzrnXyP1eLtmb@(8OgqBL$7tIi0HPGhkcVaop>OuTV+ih!L987fHg{qezubqJkrFqsFYt9vJH>C>vx)Kuly#ytwJCz)I&W+ov9VvCx2|@!rA^V_+>khx;oW=_S=zFonVO;X1;nb-9XK%K4K67PY_YDjh*m4=PffMEt-(MVzcAh)7<A)w5CkIHqZ9Cyx4}o>7hQezA_zKBCk+CRH$<z>n%F1(O5aWsu2k&SuZgY2-xas&*RaW_7mpqeo>_eAu(#&hrYOAWthr61&G4=zkVRway;c)95v<h~n<iaC6!HoZ_@bq)tZ^>e!}hqEtdp>xC|Q^Nr@MF1*gJ3*nY+Dsnmg&Wx}E<FSDJhpSme!c{aO&vWf6fsus}ggoxC@`N{3^rA6*=H$AM-7!!l*LcNW-n6mg<eUavafgYo{oI9ly?+NrS|ZyM5i)hUUBjAb1SX<hJ<+mJ*lEc-Ham%K+Q(rTx|GsHa?t@FEPi(*3&LjljEmDbGU3!p%kL(h2K9U=dTJeVz^s+RN#Lrb2pNrOgk5bFg!0416j)lRfAW=U^kN|QiJH;2)o^2LoPLfVfJ4bGgi*-6)(bUlPI7dcma%@<PAOu6=xPQ-T!3`*P@L$5To5(Bz}L<Y1gd~)37jv;Sev}hT_&VgUJc+tyG)6bKdFu<rvahx&op}65lb+OT{i@PBU-Du>UkLt3=VO6^;05d(#D9<Tw0uWa=nyFn4x3Rnto}7E)r_IK5%TW`r7;_t2U!LFk^1{}YueYvzzjfiSP5ijWYdp7S>*B}F7vWFMuk3-3dtCVFY9HM_w2k^LeBS!acUl3w5$5L#sPjE7&p&|MUte6S&C?Y`TUS4ruGD|H&DR>9`zezNxR>2M&T_gOA@=DPF{=p?=ZF{!;W+ohZKAzVnLa=dUIVH&Uu-PH59=>S{<QiI>=#OCOI2Pagz|&2=E%XrPX&w5{_@aqV~OJh7vfGZ6A0l3?!40wx2AdS0r=Z+gA*<d2y};AUdVU9L9w{{3|nmQMLMylpw(|;x{kahjT$-Uifz!#xG@WbTr+Q9AZsDwV&etM#6BP0#8oQJ@h}nmQflXUTRW1;?b^LrYL}!T-Z!yny`h|t=LI1`mN_L1?2=>x9Wp1G2`-SNiFLN51w(J;wj@<%OT5L+jj77oZ9`4{L%SP^4}7~PKjQ`+Kk+R+LK@<7DdJH>XtXXWj23=<w8~=xHIlY7)bpcJKhLO{NxjdAs-C^7b_XgqEWmx&SLj4BBCQA`)XX$?b;~*-Z3!eiTkKYIO;IveEZHYZ_7zJWmnEiM5_+Y}x%_b-%Yj8%z_p)>g!$y?a)z|-fe+J0p@!&*W|?PQyqm&wg+1Atnzl83LNu&3^<>l9bxTcc7McAgV)jJw^Us>iv*>+)e)Q<l@ukJ5j?tV;ggS;xmgyoZ8@+x25au{5qX;ae%ade!w>H*`RfFI0NNxfw>V-y_uvl9QQ)t+i1a#xpiX`B}?6+#RPvB;9xnM+1C@|CxH-n&*{il-yIH3ZzB4+d2t#syee$jf%;L4;|4DRA&O5;F^T4v7c!d|S}(m7Xr&wuo*Sj6Cz*Qezm6d^ARA?KH~^L1%<MD^wD)w(nTv|cq?HPx?OwU#SbJt>pN08bAwfKL71X+NKj!V|An`BQv7`cnrF28aFwuSh=*QNMOIy61{IZeCm1ZyFBLKz1={y^?r$IdTd=T=l|#>rNhsojBllKx=Zw_~uv2wHXR)d*wp>{df!1-o`DWdX8%uqCVHzOjaEITXWg<jRx%)y?(2cjBb!XP9_`c^Dv_WFbF51Asw-|dBA}H)>(Gz(Bc>@r(4~P5L-e@!KFIj@%?F&M#p#jiete7unx=h9E84mAOvqt?}1>t42jrt$i`#K%bU$<JEZtmKsw7165An9lp&WPO11;bg{_67N0ts9SsGy|4WY-`riIzK7qYnViR5MnieXln0AyXgi~w$|Y_vAlS30fDPIFj4Gp<Qn$s{CT=Hrzc*h;J487&nYo=7CLJ}f?B4;J14=X2VSc34mTR_lxiFXdZx5M^OyRqhoW^ZyrWI%7Q'),'Libraries/cache.☾':strd('c$~dfO^ee&7{2FM%q=rZ2+el=D)b<>qNrGQ_aKxI(k9u4P1?|;C5w1aS`j}$!Ij0sLJ!^q*Yzg49_F9;OPr5nGt-8CD40WM=FKzDyziUmeW%^Pj$?4k?)KbaO;G@O9M=Pu<@f!>vLK$}clcBT_&NSWerNa?zsSaEHcn8D?V}IG6a2EZcPHD22qZJ8ltC2?B?!j824=bjX0j6V2A_)<xGY2sJbr=*7{+d5C&`e<d9MkLN=`u*H-vcwwJRoB&u_RcV6Mq{qYQslz+92>+hzD20aKOn)iV6HfH7qJj)^iuqj?`11|lvRrYMrG9Rz|%w%Ftqnef@Mq>LH<fWLxT9dNkLGY#_<$-Zt`eLHk5tBeX=Qu!W$V}YpKJ0zYE1!rd<1pFBE2MNH>@F|`aPS9uQCZl0ra$*9<1-nE|y@Jbp$#AygNG@m+|CI0-TQUd6MIxmDSSC{;a|;d=;pzu&0#hvu5EWFCBb-VDM~iH8g__X{<&X;VBd!}ial<uqBWR|IsOl7@%eu^MKX7@cfqX!J+i^7DMRj}z_aC$xcXu_Q{yw?jVXH`pH6BIeETk9Q%evTFO^klsb9}+ZpJMw64;|=5Xrl@%$<%t1AQg}Te@+uCWKIz6)D$W3Tl^aTfY4)tKNF-N#7GZDx|{lO5~I>1Hj)xK^8|m>JJ3V_D608DStV>x2+Whu#FJ%_YyY)SkV0e>W*?q@6d2fH$FXTGe5`?d!Q@+ydv-42dgP44C>L@)3I?{rTj+bL_bopAQZSG*s4>zNm)-&eB7LmL$W#0ae}`>e%$iW&rUr^Y*u4oaW17Dpp;z|GknbLP^_YrfQNztf!)iWiJ>1>jBPD$h3_5lYL&~J`(^W0|L&I!^SE}eDd&gUb2DqQp;^ii<uoa=Ga$J7^*f*s7'),'Libraries/peggle2/rgx_golfatron.☾':strd('c$~dgTZ`L96n@vQm_R@?yV_;7hC&T)vTLtd)1-2|E);ClIJUfYYfFpdfK1Z|FG-=fkZiXNp`}f>`&3BtP)I2u(1-bBJ!fWgjY_<PRv=rN%Q@eC=R0RKl;7d^ng{!|*TbjA^`_No_j*(x^ao={H^|}CyV;)xlo>?V8T^U~R+BQ;*)VNw<a;wRy5$b$o;MB1WOn5Fb0TJIG%`;0uG{T?etGlum9=%sI`&szgK53nwKs%KN(W<;lq=Hs$9r^(b+&Bm7>u`b?WP@}sO?>&Cc_qu9<*_oX_}=EOCK<eR_pjqX;rlIV}8P)P)7NEe$J06yr1$%lrQ0JDSWRJ@FWZ$^B?#NTK%*|r~TQ@VINyw@>4_pe^(}*xZw`}ng7XuN9XIRn*lnw$l98+!~je~foc37V8F^f{u&5iVCP-PEQQQk4cU8QY6wgh0vIU>Fg)ddWIdM2b*rYZg0nLiv8?cyj7I*|=+GdGasnm<C$v*-8>9iZ)wZPql~VEoY~-6w(QM_Lw+m(Y-@&f~e7LQ81ixMkKi{n2=bH=R7o(0B1>scX09P2{YqUE_+{F|Y+s1*A^?DTZQ)myI`DE_QXar_E8Vk>6>Uk>-umk{0HpB7|tGI~G7YsUcOez2ilvi!%U?1mJQ=oOINp?zlG}GCEP9r<s)|m>z?zO@o?6y{_VZ{#V+YVXmuvzS|`92P>yzTII?C?hM0(Vw&s12PF@ejkE-**ELa#<sA#W2FGoWAGJ`3X&If*%O$kNj6rvZ9cdiRTY#h(PdyL17k33I^0v5V~~g<EReA8Q(^puLMaZt`yP|e7%l^q+ilm3|Pz`3olFlH<Yrt-U)b&#iRVq{?U=+4yDc}BQge@puI7$A^x^)QW16c7k;<8)21au48h7+BF;2$6fERZSoNLxE#D>l8=%I|2|GkplQlvYxHFSW6%yhDW1Dj%eA=Hokey7^uJXtH0e?eBVw+}hSPs4Es6Y2T7l}UM=dfPk^s3y>@ezkY=Ns4oGIT_76WpQopOPdz;}7{0q)#YlUZ^1ch`(AzLNT+7hj^n>8<%h`tR>_CGeRCYx@c%bOQE6&2%x`F71Tx6Kro#Q9BLZm6VG+zR%H+qV=AiTISOZ=^xYvw>?wam_n8bJC{RnNd(6MRIB{ttQ^y4Z7+h2G85Ht4y9k*vh*>%Vm9|s)m!Obq-u%Lw0GgD%thP$R*(ynh7Z9kHkTMyt6h(N=qC^U^&IJGRdm><%N~R<o3h{bUX#&ir-4@HMXO;@gUH(^bU_!w%DC*h23HN#777HC`t8B8dLs5~?4@;9H?4zs_PpF|NI?!ea@GMW6tWZ#yC8anrRhbg&&!lK2iDDG_h?rShi9OtLpm4$6Y~{?wjQQC*u2zrJkQaYdWvC$eF!6@MdM2?VXc1;#Z6KmrsT9V1R+${YQN$UlZi9U3EGmhF>4sV}1~?R(N2bD}Amn%3xyVRiq7FwPCsR=2Gd5jbGjCR%Y4TjPQ>*p%KEt!s0UWMUXDX^^3NM_BGVhH214M)F)&'),'Libraries/Compiler/op_table.☾':strd('c$~FZTW=Fb6n^)wm_DGHrLJWs6hb6F<c1pIB-T1mRl!>MvWX&miR?`kq&`3jfs|4LBms#e5N@IrqEZ4vT%}B(!*9qw_KBa+b9QEDXB~%_n<d+4XU_S~WzLy1vy7kSzoj!jFv~)!e;_?%4qFzZjy>gAqt#kD=g=q_D^>HkQk@x5La712p4d>D8OF$WiEM=J1T$t=>{`yTt?C5+S8Mf_&{p{(eBXHg_ef`wjO-n=9R*@JxqQiH)rmR?kML=Joj+hSc5JdO9zVFX{(>6WtPx?kV$sUm;Dn73tduL~i#ak8C6!JRRuLPo)a{zX28Mdkm3h9x=fSK~e2G6!!oUK5&R-b~c14Lq1OwLil}`Mh=g$PlDX{5!6xCegr;@B*8ZX#vuv)RB1b@NqxB-BkBs@%D7%GNgM5GA|{7?Q`$p@YojDABkr`@@eJzc}f^R4wYaK06kt@R5HIKy2%K2ED3?)@hXAYJVW<JggSJU$wa?<=&5hT_zV`!)U#Yl!ZMARuSZzAW<3&I=s}?D#=N<rI~7XBX6it*C;cinOJGgPuk&+dj|Bwh-Q<rO!Znv=qi#)^p(#;FcR*P3&ZxD2KaxnZnAw<u6djGJnQbFuzan3;4Id&j37ukATB`^J%b^_}GayIq0!g^t43Uy|J>pP*{t5W0`0%d85w(bTbtoqDus7FbE;xKot<~!!wc&tLaJzPw-#yuB`g>u3jMf%v^KmHVLiCx_4(4tsC5wcjod(nepgmb2Hi{bi2-b>x0nL+xO=o7f-VhN@!LV{%za}>9GpM#^B{46e$}R#{8m#=}dR2w)yzo^ycf$mz(p{h(rpdT)j@9eR$%}7@y<6^H-R3m-r&|6vOC@ph9R)HG86FS$a2s+`YtCItkrV-&3b#4`E^?=6L2U^QU|jp`P<Ke`Ww7K`&w!?NMS`<CSp-x}BJhlD!^r9tc4#NCWUwpM)O9jF=MI&a8N)zPjyz8YY9I>xG^;?$~8b^^~THO`)Sl`_gR62tdb2F{+FF37d+NfnkjwKQ-H#tX0TVm`yoO>{8wK8d#)3BJe9PYAR%GeY>$ya^lO_tIi(++CNgj03D#(6WEq>oSI-i+{Y6B9MI5@HO{76rMHh=Lz7O3NO%Lk8Z5xTC4irLgQ9j#QCnE4c<Aj*v3+p<*_YipvOxsB$oWYvb&0&zxD>-!m|-knh~Ux`@))*1_){5MXa&S8o&_>qAz})$lkkVyTB(40jC#P$PYbw+Z77nvH+cFbVvYVDM^{_W*DL~FfJTmI^&q5Z*tL27H*03AZeL<2Tie0b_U*RrcD8BNR`V;_+NhO6f22EW{>)UFxeN{Gi{!(0yJzOUp50%_Xt`MklSN&ZbI0-CB`-^jcbD+tEegAU-zH_n<8iLBlLq?(O09VN!!$q1&o;mt&2w)tv^6(B=F2<LNIWYW@H2j1HDEC%E>j74lgeT@X5olSWu6bs0@ntCYs+r85#=uM`yX|M6K)~+wsQv<!aVWmuqEJ}GIF(HDv{L<O&B<$48_pH!K5rVW>6e%hitT3EqZ`5)r33R9=@g->RA>mR3}at*wg6dV~W6K)!W2QV1!kK)^k-`Pe-HSH0C71(t%_-N>WLw5v>dK`NpBCiwyW^cLr)9tUXH1mZj6%q-AAcyZhvAtjU(3C$W+yzYrA?y@qzlKV-egAAY#pQc-W&AsA}qRp~Y<wQ|@%SwrCpDYsl4se*T44pIs?#Z)$yijv^L^cE$xW9l%o8H%Z+m_CZRBZ}O5F7n0bwj)Zo5=4doBdJs!WCAa8l_HV(Let&Uhk$c!SQbBW%8bGF7&80A*k%|z(;9ZF5nInPNQo9pO9s?CiSAVJ!J3ID<bg+{*`j$B*SJci5^KI|%bgiEuZFh*#s{~SrmOw=CEI$riZFjfxyn8poS7rAAl7hKcdAe1w?g{p_KVlt{){!04&6`j4sw~l>Qq$BjtzM!=s!Co2{+^S%U93Acb0moNH^B0pPhkVaDDTx)I+`fhx+@>jBFU<jn9p{?(7SBvA=g4iSI|<*_T^Sm;PJ2xv}ovxFcVU%-?tK-FiQ_atU9ep?{!6B6-^v#wFE1oYZqM3fFWC^jaxvFsbxIJM`MUn)@j{mk8#}kX#}pXNKewLhfjnX=T!VJxS`WKXKRB-K8t;(p7hHb!+aPd@Ygh=nzz*!#?Ofyu;W2ed-^hJ38FcXWyNEcTx=$6*cOfTagci{r)APaG<CtTg~PbRZx`T+aK_aD%rRiJ4ng5#6JLu4spor>alu;29L&m&Xp$ZI_7G3>acbA$KFhm9-Fk|@f>VHnc-eJ<jy>B*QVW>7w*}+((6Qi9~DwPsX<>-gdv{j*m&zczqYZ8AV<>4;6=z^299+5BR6rxF#ZRf#A4F'),'Libraries/Compiler/generate_operators.☾':strd('c$}SB>uwWA6#k#5SRz?7118$Fb4RWUB(w-<A_x*va96&pU01%zYal72A}Ke8B88AdfslZOasjHeKpRoY<;VPMCHf5Y6Z8>!=DKTVHxxq1o}J5?Gv|Egn=^~)6*@C|>Pu|fOgegEbmZiiZDUk*^7*0@Ls27NtfW&#7n7)g5P`pZ%E%}tWPHDs?7(3vGO5fr&i_#`GHM?=dVJUzOc?YRP?IgxY#Rnws!lCcuhd+a)qyLutjmTV^XzHUG;@6!E2E{XmK-hRloZo5VwRR-T8e9_TT4A!>eW)8mio0cprw?S(pu8?#k74fZC^~=7uTBO+S0hTH0~hSeWqCByQkB1nLfebgmW>|9B|@kA>{h{gpld&6+*g43cZ<}Y#GSPF=oFI%v_HUEJqHGWu=~YMvm!D4+x>ZN9yVAlY*0Sgplo5ntL;Ht!~+pQ%hu=xa`WtgpkTwa!g9Lm^{+ibEVRxt>S&r1jIa|GxQaQ05SF()+HEKDwGTPTB;<yvPRc2rq}2id&k98DV<HR_APp6P(HirMj@wUr)$h`imuZ(HY%QTFlUOsgEisxCB275E8*QQ=@#)c8418-b8`g=bpY;pdYAsLW)Q3vkNQ-KmB3m;SVqWf!=0s6p_~9^35=UJE++&AOe@`unh(}d^Wir1wKQ%Z(!8<hZ<@M_+6GNsLonuhH2yUxfhjNq+LDOu?S$1kIzFef^hf#{=Xl1Fj;xb2s;Qdm*eV0<T%qXTOr>0R%5|3vb{O!3tIXA>zc^zbJ~@1FY#3v72+|$Xhx8{p$NI*TEa&$^<5!ik16{!beEnc263-3xY!9P=0l0XDZqqgG$iQeDdmt_b0Ez|3<lMtFkA|6eVq^$IfR^a<VDyZ;#X`oxd>Bi@IS60_hEFBnb%EX_n2eiAu@#ae#J3#@Pk6lG0D4UuL>bh+me|_{{<OVHj^(S<9{^xaRRaW?2QAMM%c<?i5<ooP8iVgDo#$Y^PoE{AVF3{Tn(*vX>ETo7PL|ScNYbs+tA`JcVX1flc67z_8uRrdNRI}+uF@rRe}%H}%x|=T(feob|M+|Q{TqIm#8^(wLO|#6;nOE&1nFCN-lbQ<a(leBA=&C6w~*(g!YsZ;=XHCgQc73&Ru%W?uB_u`{63gy=Z}v|6O{&`19zfk9{z1AxZKz7L{Ww^@i#QB*z7m-c^ju)l#C{f3P!7kzDtOk77Xbi^_SY!i<Al7vX?|p=tIrJyV`USY4qa>;*qxsH6vgi&vBU*P^<_%bD@xD4-s`Hu^=ba)COIoKTDV}m#=Digf-8WkzPYqM?41@&n|lz&;WQX5~(W$`oJmNU7vBZ<JN^|Mvo0+lkpBuc-FPn)@3DC$u%^599x97v~Qs*Wo2`v>Pjv15Q*C%w8(dK6L@M`@5uDhS$Jheju7d;MwhUp*;TrsX9;2zIOv8@ePD>i&Qy_Hl32L^_1L&NaycC%QCT43W8PrSUG=6hmxZ4PnkOIo>5O+03^dHSlW`k|GzXct=tR_*95f~c9>?Kaibah$YznrXlyufIlB;?r3GI4lvC>j?-0^4{>z)bT2)QFDY0C?dC5PW33c3O@B4Cp|eI!7%Tb6w|#;^<1BT$7NhVBL!&Y!HcJtbI^ybZt`a_f^t2l-kQgK}8wl~?GZ4{yv=*QuxK^%_>Fk0~7>TRz$JXF?n@AuckZ=G4#C$_ALz!E2wqQ}-&LdMXX24=;zZ&<fd|t=QjIpiDagml{XaLWOcJ;7|pyVD!(gTS#)>Jl*z~nUOIO90+6H%8JdjVu7ROb-+n=`zL|!KVR%R-puLo-U=}7ug0#^EHl_P-)0u*qJJ}+&ByoD9JcAV$Rm73VqIv5DToA_(WNxWOfvQ{J6<7pVm&$D7ify-DbEMqwzQ$Ca@J?vo`iaVD{0Hp#AEy=dYL0zQra}V4eJs~>)3w?i<I+F6F@q8X{c?y8&7bC37oU~Cj7DzMpUgty5G|5*q!7m!*z;-bf0X98XV(lwv`mTpvpnwPbI}LVdeCPI|UypTNyF2@>T{x@f3@`%tje9-mS8@%u?8~b8s%hAzrP(g$B;(oIflwdpY&+lTdec@wUKS?GpYSQU8=+qKL~bYExGa9X}Rv|6N&_X+GHQjJTa}Yhzs-$cPxie~)}cRSS+}o;BBRXW&1~TAzboK9PM&kOgouN}_ssHchwh9wm0mWR@taxZYikMPOPu89P}y)|_4LL_}VuEOlLC+kgbWg?Oc}=EzMPI1q7pU&O$=FX}n>DSe~Y3oZuv6@7LY`LNH6gU}m`@=2@><QjQ0D`o_AWUByPy<%r88Fwel6pTJTS3_~sQV6xyVliDvwVc)dN{ag)&d;zW6&_e8h{{-j5;eYy8W*C*c{u4VaG#zBXPheJ2P5v;a>V69n*eM<02UhnfXSBXf`8bnsxMof^Q9!e4DuV^5`DqGl<fR20XoE|$Ad#d_V5|@`SFx(W8Y^-j9?8|TUd`#C^fLJm0^8yW_xMCr?fW`@*kj}nl}'),'Libraries/Compiler/gram.data.☾':strd('c$~c&U2_!2@vm$Yt8Q0^T#}Gb1hsX5At{%^s3aUaxjnY_POC#D-Rit|GEj(=VqqEMpt|!V76p=z7%WIi=)oU=c?eZ<m0$D5`|U5#Pe}Ll%<SyP>BLJ^!tR;r>F@68nU!t-a`Ttlr_P+Q&wey{Vd~<vZR_QQ#iFxN(~TpVp83Pnsq>j5TE_A$Z?S3zFIx73r{RyO{UuoWx&OkXeg483`<(rLf3Wg0M7oxW^rr}tpGIjaM#)d3G^J2ln5%0slymQ1q~-ms=0m$ybxRS9Kc1Shrzg+8LpZoltIyc;S7rpl^u;swdmo;eCWPX`yj@!GRD{##-m~91_r8LJR1h(S6e3vO^l8(|SRV`x4b2XX54!++)066y!=}!vQ$?JzmfYgVF-=EpwBXhgEmR9fWCH_cHyWDGw+<Iatqf42S=jJpu+|FJnnup@D$bk-LY94}V)vi#N7)$6=WF#!y~g=`{fw`b7AqB4(}M@k^jh6#%bru8`^1H%8P{MFh~#>82BQhyUbZX`v^NGgm0HQKA{G6=s{qbb>o@>-scMqpKbY*#;s&6==8IzfG|dwqAwZmm<&o?_6alWo#=jY$8s>zRF|ve>QGt%T>^d_H4?Ji?JTTa)l|5ncFZZ_^&ya_JVIwFEQF?2I;ect#&Q175L`l}vg4^HPGu&SoOV!z{T$33EuGEnj$;HT;ENoTDaXo{6Vd21;MKN|Ba14piBKbC3X;bje(1@Z+X75#3Dn^9gaSTyu2vh4OmK3}zMpE#mmiXx*WK#+WQNfMQGC#uU_O~oEQ0FVYgCR-ITct^<XP9!l(8v|(g4Nhu!ZaeDxHCnmp=?c+TLcKkv8DyP-+-e31cB8;MErY~gqTF8&^zYU6em+n6F)esi6R#jBI%=)pA-h&3?_1d8%$JHDn=|L$)k$x()1()M>3eO4J<}gc_Q@XgTH<jw6_a=thxc-7W`|-0%#D*TF`!6=)>%9yo!ZW9*o*$tBO_tv}hrkKHYoY^jTJMR%1N%!|^oGps>Cc&w%YO4o4u^zD*<=&toL6BLPYmq|$h9&(+;ZG(V4sa8pr?fpjDz*F}aKLIUDIzK7BLC${HQ_$EH~D`74E`-}ape|*XVN8Mp|N$dyD;AH8YH7yZx3RNGehU=}=*zQ7vd5D}~5{fLRvK%RvZmvu8WZ9M$*W<WIrL(a~>KOwD<GQYJ*5|L-V6d+!wH_W|h8Sr>Nw5|>`;^oqTYnycLU$=oiu_?|jG!7>Vx`NYmRoV7fycR0V<gvBglp^YTw4coZN<2@xPsg?sgkw0I4Vwr&bp*iTbL`kN>{;=6)Z-n|J{BKYZ<rys>p>`GAYE;nv8JjyW&X_#(%uElji`=&sD06KJ9j|N^q%s)xIi7EI5^7ji(mTTB;OX-v)eT7@-<Hyl`YtR&1^C(#J%_5rpRfK_5rMrch2`SZ}SkABVa#^6Qe(I%`e$c2EQRvJJX|7oaxm?Sy8ExHm#bF(lJKaV+E7GppkAaDps;X&f)&4<0Es<)I-81=IJ_1oE>8vgMJZSdXD!xja{!cm0~lPIHXV5AAbdlSBP(*y*tKsaT5;Zx@nORI@QMy!|v(N^C0vD4(e#sB@20eYfV;HF1&4?{D4vp6ghem=%ySETN+k8k5ktgeD|Zl+cWXB)#Hr0q++*l;t9Ni+;sf&=MWzcYjO7Xmd3e#aY`1oI~=F!D-6=>Y+vqv^Sw@#GS0}74YZ?Z(WpoBy$>usv4#}LR9P(f!ZTT1v<2ZtQ;Puk{>^~lB38~$1m6HIp!l>#}N!ng&{L1kVw5sSL?8WG~l3~K$gb|-j+GLoPk$w8n`NN)QeF%fT=3moAY)#Z^neWUMn*oy3x$Z(7E035|+nHe=@Y6;N3*m6*o*zQhr_v-!Te!eUG%Yv3rw<$FxAj7YDmuTPlj%zwN1mI*8V7XQJE&PhW@-3j-mVW69f(Bo;IF2_PkRZi=fE8DBXnS&g$ieqtsq`1E;HBo{A1LN9jsA!wJE>NOPN?#;*)^wY@G@<JrGhgl8mWY2k?>qo3b`&c$8Cw=0Mu!@c)Pr@MBz8N&`!!P+VdX?#;r9OI-Nv;cWGPkkV<dUZ$Fu`&)kep<xyI8ZKe*i&$eZmAA((}dBh5XQPA-kMkya3SPID%I{LU6(voIN%8`$E=O)^S+K>X!93g9eP;G67;HYv^u1YgvPZ93SVX?0arG%9KPKFCCrH^8z0Ioq)!M3i%L2LN1CWvE}^On2J3p5k@2Eu0%hUj($u+<KbjULbGymY?Q2#N`%`deT`YH%To7UU{yIP3iEbD6$WP=BCk}!<*aoiPY4XwQkuM>)M`srNE`X82t@-*gc{Ls+m1wEJou*1MzS8CAc1C-#AHtr{B<Gvun;?Aqm?i6yns*Iuvt8#i|eU)498^v7VI+Rc=+6o&HGX{#}WJ(f*(QPwDBsk`;8vH>+^C?6yb15EOFLU=I(9s9(TY9srsTJNmfrieD;^r{1j@~RNUJn@tITU9iN?;k;lIup;AzF+WRrANsy%c`78R0far$6(6Oh7Q?BUD$chE`JpRR?$lh#q`E(p6{m_Inc75!|a{k2eBf-uC6Yl7HuYx<bco@4!M}s@Na3aDf164g}e;2eL1y5o45Qyy#Lhb&1f2+L%K>H`LXJWk5c+qM6&}n|wX|8k{cRP)*I?Y?1#!sEb{Z8X+fmfUm+2WRlprM4$?*G*QhmGJ{eNc(5yk!-1<NA$Y`-@=vHikI{@HWJ7(0&rM|3#;T@~tEM#34HZu&G9e2L7(REXeOD%26!86R4pX3)J{Cj<O@#$%v;{gw<zEF$S3Rw0LR3+*tV;9k}um)>*c)SYwV_K^LKa6z52&C?Q8eCDINqO-g=ndN0uN;B|EQeYs;sLbDQbL;oW^F5;t5MEV4RIp|iZ^=r1c&Qt$%jjrW7wNqh0D=29#7Cj5tW!IxlBD~qg=|meFJ&`t;WK3&a&;2H{V(9EUj$sT$+r(5FN|PoPi?%Lr$y>m$tcV+G$;D}|Q%ZLP#6(w>yb6uG;}i5m&5af7m_XJ{qVOHa4W?4KVX$OE?L<=tC&i_M>Il!J_I4<3A=?*<`^I#5W=a}LgL!BgC#W21mQ@E2OIjY8PxPrc9FD}^h!G+VM+^;S?qgxF_FURlMkj^1+$hCm=R|LT`wH}(aUf(q5@*i*a~SR;Z_3@ugzVwIAamGEjm3#^h_*g%&oH>mM8-<H0uo_|OD2iy)=Ey*O*HKhR+0)7RJ(N9@kI?t$%OWHve}O!JQfiy$%W54+&tW18$T4TkHDEL?H5W#WmQqYJm^lsbw6YPQ~0wC0C|B<EUPS!-aV;LMY!lYrFojJEY8Hrp|}+12C~p~?d=re7h>Azc(f6G$cFXBN|sg@{g4x4rTOXTsQUiTcZnxj*kll?;O>98*xfo=(D=@-mC0#3XmXrugnb@@HTPqUUN966iopCELpJ&}gKZKQ&Z$-xuAMXmb3qsPGP*b@`-@9eDLa?g;GaxF1da_CXV;V1%n@AIa^0C@y)Gzl(&XP!Zavn7PDYMj>~XSIpFe3rI17o0Z1U5ac*zsiP}dDi6<T7vi4qejktI)h(1KnnLCx|y8=K5^_!^O+k7IXlCeL1-7ZuA}&SUv47_3RwSepy2ZO;u@uh|}hec@+++hOtpoc<_f`L{;?5~2<0ITQC;)}IZyU+%ZtO-L{JFRbAI#KP<K{H53HF!_3&ruZMnWDMhfDv=tj'),'Libraries/Compiler/ast_to_py.☾':strd('c%0Q6S#uLd`kh}fP~}XIEEGwEgt!p9#CVU22`(ViR@u&!ER8^gj>*h8*qfucF(ib`c7Q;DcnRU&B^M9~Rdm(9?r(@6_bESNzpt<98I4AA;AK^1X{OKbzPerW+D&7+Rj;(GPPH7Aje65<dx25+?N-}smK*iIJJnS+9JSY(-PiW2a>U+!jk+JKBJ?mlF}C9`#J2J2uUp5qZQp6z#PpnfUOjL;-^?1j8||rb!zWhOFii`-`QXi4w)}Z?+gqDQci6+DBb(oWX>7H(M{uN?1kbE_+Za5LuPsc%rq}3a^t3TlGU!2ihAt8dn@-Z(w(mNX5;T5Aj|^|#N#N;AdW)FLm(ER07xVcycY4zfKCQ1UU;2VK{RwuFZHw1<+dJ)+W8%hQd3f}Ls=aq#HEHpqxA-j238uZ4SnA$E-Z)!#8dcsl@oqk!ujLC<uko&`(-4D?KISczb}Oj26o|*J^X4hfDesNJGu7B@R~oG@Fg<_9XVz<CsfXuzgVT^r&#%cAh5p=r-c)OQI>d#1VS|9LQTF`=K%ziw-L^#l0t2tn^YlQ;6zj27OpCy~lh2p=d*IE+)@-{vPN(S{ohRlep9~DV_ueb7eDu+#O&d234nDuXcJ12bPmg5iPp^WMjTa{^W6)4sd31`e{_3j&yUz~shD=5@92ex>RFVz<;0+s9gP>7KHC*Klt7XI7x4c18Y<cbmZz#8_U4}fr!{1x&K#rIb+>*jGcU%oIRO9g@Vw5i%j>!fC21ZC|S*ys%JHx0VCf!dDK*u4_q9gPuJqFY~PEXKJL5EJ#&*>?k?-_cQo}=@0fi42OF3^iW!%OrsaNr8P3M~AZF42F`>+~CXgMLeI(p&U4y+iNPd-Oj2C;b<FK)<8k(;w)M^dWsjAJd=d6Z(`sGXaY2!&?xF;di%hCyjD*s#-=U@6mHv{(E)^e;4TwB-#wvl&312-x@9y*8y8i+eDmpjE(fQ+IO9+Avs_j`U_jgX;pBc=pt<LLwb(@!OqhM9i4}PBtOzSL_FLTn;_wrfTE9)<nS_F!e1-w<(tB;Ri`4X7SNLL&9X*(o3zdEk`M}sVZz>)9QKtOCV&7a#zuDahJq>aVUUS=dPAu(P>q?|WAu?)7Z_~uZ(MuV$k^{(J88@Tkh7<11TfzUvBvpd(=$j@wZY7gVJ<(sH{k!lGzJVZleHKrq5$JE{2KvwXKlx?*nZ$8z%77CV23#|F+Je3T?96aDGJuY>)aLz8}=G>9HNgxz9`wTvX)V=iFHBQ4d%(d1q<1l2qq>b%rzf=Y+43dX+usyxMA2idRUj?nGyqaDQnD@UNbU=X_&e|KLZ(Q)LV{EW`s)xEh40tg|`nsh86&Rmg&n=dI*g$K)|GSRn@5(&WsBd%`W?a?am?+3t%#yWDSs|68u?1s|@%cBBCqj<aY8#{BYN(Iy(jjMhPs{Z<oKAgTLcuI1vVsCgTk9`vS62%o)#5X4L{{{H<^nen^1Rgf9ZCs8};TX<@){8tmVfq}d^yg^(S&KxfGE@yE-@fByA{OaHxeRdS@*ZSb%2-^wxh_!z+R;w4kC6w!K0A0VM4(3cr&1Hh6^=Q@tB7LuyKXOF{nr*S)i);}Yd9dOc!t}F|=<eOz$oeN6gx=5dp4nSb$8Tt)lL9$^&LA=f7@g|XYYFn0sXM*-9HbR`m_I$o6LXHj2n<#vQAc~*U?+GVbR&JLmTO5&c40=$zfJs9P3lXPEfss)qG!?XGCN4+m86_-AzzQHW0eolC`E>O?2;2hwh5eorzgOfhNBC?m$ZDDlk);zrq})`&Z&AVn&jsx{FGJxiBco&;#KP+)J8)#MGRf%$ieL^PY+9NgA%Ypsa&DJ6_ob{VT387xjN&h%uiq}85y8p7&)Q(2ZMW=|n-DsNI;tiD{-jchiLx-N3lMCC4uDbZ(?r8@=9p=Kfl{I+*{mrG*A7ed<tk}P!V$!9Iff!`cJ#N)r+<oCsSb!D1MmY;wNYV25<{ciVx0;su$nC}|Iq9lfghPAbaYl2ErSwFUN{K4!l{}j24=Nh31DQVA~8;5&4;>`=}pFuyOL4x?2y^7IP|?|ch(86JnLi6@s;g4*$dCbv^^v4EDeBhzfrF^q>wc*J+-=;_;hfV=gw=;pdDDG4}^o2fLIat%ZJ2WG}E?0-UkLj_&!L>b8XjRorFkZg;tEE*%ljFQ|4A`D_;dRwv?se3BT?w_@JWnSCQ2*ugAsXF@Vc$VcaNeG}dttS!l4p(C1h>xouX?GeA`ZZcOE$-+zAR6Eo&h`Y>S8_|>(@c*M}M9ZrZ}q#}?&sIa2txPW7lG5jDTbH}W3W+o;a#ZKV}HG+$T?+o=q1GWq2cTvE8r7>M0xwn7AS^q}5TBh1C`U}XCsSzVp{!gZAWAClr9_e>0h1`Z0+i}}izdM4h`8*ap$7COMg!@G1EyGr^0^~ua74Ji_R2wXrJ>@5qn?&no<zgWR^sZDyQ)#x_3CaN=(kIn+#K^YN?fjK*_aZVV;>DG0x72I9i(>if;&%!7XUS;$rk-<Ysy$SS@i7ey6fDi}_^qV!3)Z_t1_9|K7ekpiiA8LGdP=v%Dzaw=mnC&!yokxzVl?9OTWFoYH=UwagxeF*HAfCRuEshr-VH<Vf`u);1D7@2a3&{B94l_?!x97;l!<|sGa@Bqio{kPfH)fa{Z=f6;xCaLM@(5`F<^*-Za|rJh^QIPJu^n6OElL?XZKVek=De-%nGU~#dsCv4iHQtYh_abLM>p&11V5-OFGWe3zkZ7xntJO8**T7LO8O94wBK2hQ>nuZnVm976LrC=v9)SnU<c1pv?{?N6gU%$H!{+J-N1^@QZl%RJ0%o=>x6*C%mF5?vg0%yLO`<sC1X@m6GW8k}?D$A$m--AOfHTdWi57xvYXuoon&qtnmDc)m6quc4@k!)dLH9J&+dzv%LD=r!>F+LD_o&9pmO|z+c0xLJZ9QHR|&I^!zdw&qj@3TJC>&zw<t)<=%b3>V>nBY^r;eDX%>z$@t5u1EpiBr?922c(N$@#MfB1N#UdBOa9n3(!&Zea~^|Qcg%@|qp{8$izuRV3zJ5qR%k~?7h|J~lTo)xm=9FJOKM)?2hG4<p4;D@0CA756J+0>dcz^oZ}Q3~!2Svc{A|n)VO>Zokrp)ifz07DVP{bfqlc8?WR%o4Ti10n<cL~=jW|q9m<W*<;cj29pl>8APTVp^1-B~=EA6JcLK;SM2U#-KAn8e~WJ>)GLe*>fYU|<&b>CD79Iw?+nTvFkVby*Tl*C*Lp(Zgs(7MypZ=`=ezzIGjR;9qlcCCyJbw?@{E|%Y{ux1wDD^0txbnzk?7@LnG6?e)<>Gfzdk}>#dH^uC4h`GFY4Nb$Kbm4<thh$<4uEj)zpPaIju*B3toOs<55j}IS(eswIMnQ(Nu`Ri3usx;n#d8aBma2IaJTST5<uE-=-G<oVvy~d7^GhLkF~!-CuO=`E;9>HXE4!}KsuGR&k(y;k!EcjM=uwQ1*RwiH@5;NYhl=jg<9TEynnY?oy9hqJ$Pr<w=$@oJG((1C%@F`4m??>A2i!WiX2sOrl%_i~6~_&jq7S3EAu)%eZghkVske1UVj5*%Op2WF4KvEe4)~^P`Pa)Gu9(F?SVnoF_$Q@y)FCt+*CCf(Y3dp7i~C>VLRNVBDr|t4q_96;(;W}jpG-*|JB?E%S8w@_7oZ66`frNw1>oG;O!5&GPm5NwFoz-4t)kam&$`7-erm+cN)4LjP`SWKI<FUPRHTv?q5{d2LT?gY1&Q8Sm|>R{#JvWzzC8G`csXb+u@+QaNg*h9$3Z%iu~_viy&_ce+%7$k^mbkq;$0ONq)T0@xk(R4PfYPRp3yUFR4sWFBTr;3c{hX&J&|(S)CaeK#Jc-u;XmhKGI5eg5xZ+5&e)N8dMOVt!QhZe!zs6HC*pv_prLR-q$@oHp6YftA|gaiDdD~d!=G5{#*)0_;B;AunLx-Dce?*Mz=?ucx1zTIyIif>Zre`+J8RTS`Jv8iGUw<9+|>;@sb`aJOocOZJ1s5QC9!nh<m1gDqmG$BzW^a}e^y?&qr;3S#WCmhUY0LGz3S?6!|yff{F(u~eFSFG_MF||bjWDdaJAb;C_q1ABRpNA7c~1zMv=Ds#?xqcU%^H8fc<d61$W#}8Xq0U{z)PHE(=**fW?}eT-9rw)RWApYR+SrSIDx>unVUZ)imzM<?;;CX4#d9?${b)8fwoxFz`H=z`MO7K^ndHR@7rhjiP)b_TfO(TS43Qy$S#mEs!kI`vM>(SYA^zxHBMUZUnia#fYtUs3S^N-p3w#ir()wOY2h;IWIYXyI>v-cp(VKnUJ$_aS*5=zPJ+Nyq&mNEO8&OA}%voS|Scdh=Qh!9l{fdv|ta6><RWjDDDcU@-nJFozYL9P%^qELMbRIr@v%?@q>}LCn9mI=^tZyBXlMu3Ln+r_4GiTL#$939rs=;yb+QX6G*D5buW?@B}v!4Fo;T$BPnCnXqECB6}M~7B<F_tve2|J>g;h@iERQATnp_RpB33R;`B$kS!quPHW-$A%Wh&=>FKuR6urW}9|~B*aIT9n!l7AV-Ep=E<92LKKGQ>mpYJ!A6JQIQ;;Kuun$6@3GUs@MULhT3Tiu`KsH5`)G$J==xe>}T-xhd|QxaiWs|`!F%1y`qpzQgw)pJ~U6N5A&vBeOvTD{S*WrMw^-Ee$+s_fS*dXPlAUE|G&n<)_5vHUFxMEruN49kf-%Wu)g^A;8}93h>RfiN&rLFaWkPkMwpD4Ke-qswsHWuefEg&K%5tfI?%&f!>dZC3cP=;(U%FodD3#YZtMsMi#adtQjf18~9Wj<G;&K8*hd7Hr5~18=rtDD>r~TWlF*e~v%F0y3ZCX+Ar|yok9wP<Tnp+_+Sm!|kdwG|>_#w5V+RTGLHj2QrCL;f?h`^in*OtnG#{(tNY9-o#My2xt!0n4W~kN$jLn-|G=QN`#o3Bc9i0-oTv=_Ox4q81>ff)rJ5ALB$2sKatrZf5ZPe+hN;8`%g1sDy4(GM?JG1NF_{}4H9$L2;Q%OZ_D~0W`~OU')})
__dir__=(__file__:=áÌî(moon_dir/'Libraries/Compiler/main.☾')).parent
(ÄÊPSH(__ÄÊIMPORT__('text_format', globals(), '')), ÄÊPOP())[-1]
(ÄÊPSH(__ÄÊIMPORT__('to_ast', globals(), '')), __ÄÊADDGLOBALS_CLEAN__(ÄÊPKE(), globals()), ÄÊPOP())[-1]
(ÄÊPSH(__ÄÊIMPORT__('ast_to_py', globals(), '')), __ÄÊADDGLOBALS_CLEAN__(ÄÊPKE(), globals()), ÄÊPOP())[-1]
(ÄÊPSH(__ÄÊIMPORT__('tree', globals(), '')), __ÄÊADDGLOBALS_CLEAN__(ÄÊPKE(), globals()), ÄÊPOP())[-1]
(ÄÊPSH((moon_dir, mkd(ð(TMPDIR, ÂÞÅCAT(ÂÞÅCAT(__file__, ÐØó), sha))))), ((BASE := ÄÊPKE(0)[0]), (TMP := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(áÑð := ÂÑÖ()(show_preast=False, show_ast=False, show_py_ast=False, dbg_parser=0))
(header_com := ÁØÿþÁÙÇ(lambda ÂîÓ, ÂîÒ: ÐÌü(ð(ÂîÓ, '%s.☾' % (ÂîÒ,)).resolve))(ð(BASE, 'Builtins'), ÄÝöÞ(ÐØó(ð(BASE, 'Builtins/builtins')))))
(pathlib_import := ('from pathlib import Path as %s\nmoon_dir = %s(__file__).parent' % (PEV('𝐩'), PEV('𝐩'))))
(to_py := (lambda áÖï, *áÑË, **áÑÕ: lambda *áÑË, **áÑÕ: ast_to_py(*áÑË, áÖï=áÖï, **áÑÕ)))
(moon_to_py := (lambda áÖï, áÖÝ={}, áÏè={}: c[h] if (h := sha(áÖï, áÖÝ, áÏè)) in (c := moon_to_py.áÐñ) else (ÄÊPSH(c), ÄÊPSH(h), ÄÊPSH(to_py(áÖï)(to_ast(áÖï, **áÖÝ), **{'reparse': True, **áÏè})), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]))
(ÄÊPSH(moon_to_py), ÄÊPSH('áÐñ'), ÄÊPSH({}), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]

def moon_to_py_debug(áÖï, show_ast=True, show_out=True, show_out_no_rename=False, show_preast=False, show_in=False, **áÑÕ):
    if show_in:
        Âçß(BOX(title('IN', show_code(áÖï))))
    (ÄÕÒü := to_ast(áÖï, dbg_show_gram_tree=show_preast, **áÑÕ))
    if show_ast:
        áÍñþáÍñ(ÄÕÒü, 'AST')
    (áÕÃ := to_py(áÖï)(ÐÌü(ÄÕÒü.cpr), reparse=True))
    if show_out_no_rename:
        Âçß(BOX(title('OUT', show_code(áÕÃ))))
    if show_out:
        Âçß(BOX(title('OUT', show_code(to_py(áÖï)(ÐÌü(ÄÕÒü.cpr), no_rename_vars=True)))))
    return áÕÃ
(decorate_code := (lambda áÖï, áÖý: '__dir__=(__file__:=%s(moon_dir/%s)).parent\n%s' % (PEV('𝐩'), ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(moon_dir, áÖý.relative_to), ÁÜÙ), repr), áÖï)))

def compile_code(áÖï, áÖý=None):
    if áÖý is True:
        (ÄÊPSH((ÂÞÅCAT(áÖï, ÐØó), áÖï)), ((áÖï := ÄÊPKE(0)[0]), (áÖý := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (áÕÃ := moon_to_py(áÖï))
    if áÖý is not None:
        (ÄÊPSH(áÕÃ), ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0), ÄÊCUR((1,), {}, decorate_code, ÂýÃ, (ÄÊPSH(áÖý), ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0), áÌî)), (áÖý := ÄÊPKE(0)), ÄÊDEL(2))[2]))), (áÕÃ := ÄÊPKE(0)), ÄÊDEL(2))[2]
    return áÕÃ
(compile_files := (lambda F: Âøî(ÐôÅ(F, lambda ÂîÓ: Âåß((áÕÃ := compile_code((áÖï := ÂÞÅCAT(ÂîÓ, ÐØó)), ÂîÓ)), Âçß('Compiled %s %s ⭢ %s' % (MOD(ÄÕéý, áØÁ=dotrim)(ÂÞÅCAT(ÂîÓ, ÁÜÙ), 25), MOD(ÄÕéý, áØÁ=dotrim)(MOD(ÄÔéÄ, áØÁ=áÖï)('\n', '𝗻'), 35), MOD(ÄÕéý, áØÁ=dotrim)(MOD(ÄÔéÄ, áØÁ=áÕÃ)('\n', '𝗻'), 35))))), '\n')))

def refresh_cached_imports():
    ÐÌü(TP_CACHE.clear)
    (reimps := ÂÚü())
    for k, v in [*__ÄÊIMPORTS__]:
        if not (v is not None and (v.hardcoded or v.name == 'Compiler')):
            continue
        if ÐÌü((f := v.__file__).is_file):
            reimps.append(f)
        __ÄÊIMPORTS__.pop(k)
    ËãÂ(ÐôÅ(reimps, lambda ÂîÓ: Âåß((sha((c := ÂÞÅCAT(ÂîÓ, ÐØó)), {}, {}), ÂÞÅCAT(c, moon_to_py)), Âçß('Transpiled %s' % (ÂîÓ,)))), lambda x, y: (ÄÊPSH(moon_to_py.áÐñ), ÄÊPSH(x), ÄÊPSH(y), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3])

def generate_bootstrap(dest=ð(TMP, '☾.py')):
    (ÄÊPSH(PL_FORK(compile_code, __file__, True)), ((_ := ÄÊPKE(0)[0]), (Æå := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    (pyc := ('#!/bin/python\n%s\n%s\n%s\n%s' % (pathlib_import, ÂÞÅCAT(header_com, compile_files), ÐÌü(dump_cached_imports), ÐÌü(Æå))))
    if dest:
        ÐØì((ÄÊPSH(dest), ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0), áÌî)), (dest := ÄÊPKE(0)), ÄÊDEL(2))[2], pyc)
        os.chmod(dest, 509)
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
    ÂÞÅCAT(ÂÞÅCAT(HIST_FILE, ÁÜÙ), readline.read_history_file)
    (pfx := Åøþáüì('✝ ', 'f0a', rl=True))
    (ns := ÄÕôñ(ÁØã))
    while True:
        (áÖï := ÂÞÅCAT(pfx, input))
        if not áÖï:
            Âçß('God is good!')
        else:
            readline.write_history_file(HIST_FILE)
            if áÖï == 'clear':
                os.system('clear')
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
                    Âçß(Âøî(ÂÞÅCAT(Ïã, traceback.format_exception), ÁØã))

def transpiler_cli(*áÒø):
    (show_docs := (lambda: Âçß('Usage: ∅                  (cli mode)\n       <file_path>        (run ☾ file)\n       -h                 (show this)\n       -c <code_to_run>   (eval mode)\n       -C <code_to_run>   (exec mode)\n       -b <boostrap_dest>\n       -B <boostrap_dest> (updates compiler)\n       -e <str_to_encode>\n       -d <str_to_decode>\n       -o <file_in> <file_out?stdout>')))
    (ÄÊPSH(([*áÒø], ÂÔð())), ((áÒø := ÄÊPKE(0)[0]), (f := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    while áÒø and (áÓÓ := áÒø[0])[0] == '-':
        if not ÂåÔ((ÄÊPSH(f), ÄÊPSH(ÂÕØ(ÄÊPKE(0), (lambda ÂîÓ: [ÂîÓ[slice(1, None)]] if ÂîÓ[0] == '-' else ÂîÓ)(ÂÞÅCAT(0, áÒø.pop)[slice(1, None)]))), (f := ÄÊPKE(0)), ÄÊDEL(2))[2], áÓÓ != 2 * '-'):
            continue
        None
    (Æå := (moon_to_py_debug if 'a' in f else moon_to_py))
    if (ÄÊDEL(1), False)[1] if ÄÊPSH(f) else ÄÊPOP() if áÒø else (ÄÊDEL(1), True)[1]:
        ÐÌü(moon_cli)
    elif (ÄÊDEL(1), False)[1] if ÄÊPSH(f) else ÄÊPOP() if ãÊú(áÒø) < 1 else (ÄÊDEL(1), True)[1]:
        ÂÞÅCAT(0, áÑË.pop)
        return ÄÕôñ(ÂÞÅCAT(áÒø[0], ÐØó), ns={'__name__': '__main__'}, Æå=lambda x, y: exec(x, y, y))
    elif ÂÔö(f, 'e'):
        ÁØò(lambda ÂîÓ: Âçß('%s ⟶ %s' % (ÂîÓ, PEV(ÂîÓ))))(áÒø)
    elif ÂÔö(f, 'd'):
        ÁØò(lambda ÂîÓ: Âçß('%s ⟶ %s' % (ÂîÓ, VEP(ÂîÓ))))(áÒø)
    elif ÂÔö(f, 'D'):
        while True:
            Âçß(ÂÞÅCAT(ÂÞÅCAT(ÐÌü(input), VEP), __highlighter__))
    elif ÂÔö(f, 'c'):
        (lambda ÂîÓ: MOD(Áëý, áØÁ=ÄÊCUR((1,), {}, ÂÕõ, ÂýÃ, None))(ÂîÓ, MOD(Âçß, áØÁ=ÁØã)))(ÂÞÅCAT(ÂÞÅCAT(Âøî(áÒø, ' '), Æå), eval))
    elif ÂÔö(f, 'C'):
        ÂÞÅCAT(ÂÞÅCAT(Âøî(áÒø, ' '), Æå), exec)
    elif ÂÔö(f, 'b'):
        ÂÞÅCAT(ÂÞÅCAT(áÒø[0], áÌî), generate_bootstrap)
    elif ÂÔö(f, 'B'):
        ÂÞÅCAT(ÂÞÅCAT(áÒø[0], áÌî), generate_bootstrap_live)
    elif ÂÔö(f, 'o'):
        ÐôÅ(Ááú(áÒø, [0, 1, 2]), lambda x: ÂÞÅCAT(compile_code(ÂÞÅCAT(x[0], ÐØó)), ÄÊCUR((2,), {}, ÐØì, x[1], ÂýÃ) if x[1] else Âçß))
    elif ÂÔö(f, 'h'):
        ÐÌü(show_docs)
    elif ÂÔö(f, 'get-dir'):
        Âçß(moon_dir)
    else:
        ÂåÔ(Âçß('Invalid mode(s): %s' % (f,)), ÐÌü(show_docs))
__ÄÊADD_EXPORTS__(globals(), ('moon_to_py', moon_to_py), ('moon_to_py_debug', moon_to_py_debug), ('compile_files', compile_files), ('generate_bootstrap', generate_bootstrap), ('transpiler_cli', transpiler_cli), ('moon_cli', moon_cli), ('refresh_cached_imports', refresh_cached_imports))
TRANSPILE_REF(moon_to_py)
if __name__ == '__main__':
    transpiler_cli(*áÑË[slice(1, None)])