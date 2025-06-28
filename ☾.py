#!/bin/python
BOOTSTRAP_HASH='kEqPPCPj4zdzaYzwTS0NsxpqDfygJLn48j3j8ReF8ac'
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
(ÄÕÍÔ := (lambda *áÑË, áØÁ=ÂÞÅ, **áÑÕ: (áÑË[0] if áØÁ is ÂÞÅ else áØÁ) if áÑË else (lambda *áÑË: áÑË[0] if áÑË else ÄÕÍÔ) if áØÁ is ÂÞÅ else lambda *áÑË, **áÑÕ: áØÁ))
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
    except Exception:
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
    except Exception:
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
    except áÍÚ as Ðáü:
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
    except Exception:
        pass
    Âçß('WARNING: Failed to copy.')

def PL_TEXT_PASTE():
    try:
        from clipboard import paste
        return paste()
    except Exception:
        pass
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
    (áÖê := [(áÑÿ, i) for i, v in ÂÓÏ(áØÆ) if (áÑÿ := áØÇ(v)) is not ÄÔýò])
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
(CACHEDIR := ð(TMPDIR, 'cache'))
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
    (ÄÊPSH(ÄÝöÞ((ÐØó(SCRIPT_FILE_LOC).strip('\n')), '\n')), ((CHAR_NRM := ÄÊPKE(0)[0]), (CHAR_SUP := ÄÊPKE(0)[1]), (CHAR_SUB := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
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
__dir__=(__file__:=áÌî(moon_dir/'Builtins/subproca.☾')).parent
def ÄÊSUBPROCA(cmd, áÏÃ=ÁØã):
    from subprocess import Popen as áÐä, DEVNULL as NULL, PIPE, STDOUT
    ÂùÆ(not ('M' in áÏÃ and ÂÕÖ(áÏÃ, 'OEoe')), 'Cannot use stdout/err and MERGE at once')
    ÂùÆ(not ((('o' in ÄÊPSH(áÏÃ) and ÂÔö(ÄÊPOP(), ÄÊPSH('O'))) and (ÄÊDEL(1) or True) or (ÄÊDEL(1) or False)) or (('e' in ÄÊPSH(áÏÃ) and ÂÔö(ÄÊPOP(), ÄÊPSH('E'))) and (ÄÊDEL(1) or True) or (ÄÊDEL(1) or False))), 'Cannot suppress and ignore stdout/err')
    (K := ÐÌü(ÂÑÖ()))
    (ÄÊPSH(ÁØò(lambda ÂîÓ: ÂîÓ in áÏÃ)((vs := 'toeBPSD'))), ((áÐÍ := ÄÊPKE(0)[0]), (áÐÈ := ÄÊPKE(0)[1]), (áÏý := ÄÊPKE(0)[2]), (áÏß := ÄÊPKE(0)[3]), (áÏí := ÄÊPKE(0)[4]), (áÏð := ÄÊPKE(0)[5]), (áÏá := ÄÊPKE(0)[6])), ÄÊDEL(1))[1]
    (ÄÊPSH(áÏÃ), ÄÊPSH(ÂÕÃ(ÄÊPKE(0), vs) or {'R'}), (áÏÃ := ÄÊPKE(0)), ÄÊDEL(2))[2]
    if áÏð:
        (ÄÊPSH(K), ÄÊPSH('shell'), ÄÊPSH(True), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    if 'M' in áÏÃ:
        (ÄÊPSH(K), ÄÊPSH('stdout'), ÄÊPSH(K), ÄÊPSH('stderr'), ÄÊPSH((PIPE, STDOUT)), (setattr(ÄÊPKE(4), ÄÊPKE(3), ÄÊPKE(0)[0]), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)[1])), ÄÊDEL(5))[5]
    else:
        if not áÐÈ:
            (ÄÊPSH(K), ÄÊPSH('stdout'), ÄÊPSH(PIPE if 'O' in áÏÃ else NULL), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        if not áÏý:
            (ÄÊPSH(K), ÄÊPSH('stderr'), ÄÊPSH(PIPE if 'E' in áÏÃ else NULL), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    (ÄÊPSH(K), ÄÊPSH('bufsize'), ÄÊPSH(ÂÞÅCAT(2 ** 6, 2 ** 10)), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]

    def p_stream(x):
        (t := ÐÌü(getattr(p, x).read))
        if áÏß:
            return t
        (t := t.decode('UTF8'))
        return t if áÐÍ else t.removesuffix('\n')

    def extract(p):
        (r := ÐÌü(ÂÑØ()))
        if ÂÔö(áÏÃ, (v := 'R')):
            (ÄÊPSH(r), ÄÊPSH(v), ÄÊPSH(p.returncode), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        if ÂÔö(áÏÃ, (v := 'M')):
            (ÄÊPSH(r), ÄÊPSH(v), ÄÊPSH(p_stream('stdout')), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        else:
            if ÂÔö(áÏÃ, (v := 'O')):
                (ÄÊPSH(r), ÄÊPSH(v), ÄÊPSH(p_stream('stdout')), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
            if ÂÔö(áÏÃ, (v := 'E')):
                (ÄÊPSH(r), ÄÊPSH(v), ÄÊPSH(p_stream('stderr')), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
        return r[ÐÌü(áÏÃ.pop)] if ãÊú(áÏÃ) == 1 else r

    class Popen_Proxy:
        (__slots__ := ('p',))
        (__init__ := (lambda áÑÞ, p: ÂåÔ((ÄÊPSH(áÑÞ), ÄÊPSH('p'), ÄÊPSH(p), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3], None)))
        (__call__ := (lambda áÑÞ: ÂåÔ(ÐÌü(áÑÞ.p.wait), extract(p))))
        (__getitem__ := (lambda áÑÞ, *áÑË: ÐÌü(áÑÞ).__getitem__(*áÑË)))
        (__getattr__ := (lambda áÑÞ, *áÑË: ÐÌü(áÑÞ).__getattr__(*áÑË)))
        (__iter__ := (lambda áÑÞ, *áÑË: ÐÌü(áÑÞ).__iter__(*áÑË)))
    if áÏá:
        Âçß('Running: "%s"' % (termclr(cmd, '3d3'),))
    (p := áÐä(ÂÛê(cmd), **K))
    return MOD(Áëý, áØÁ=not áÏí)(ÂÞÅCAT(p, Popen_Proxy), ÐÌü)
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
TP_CACHE.update({'Libraries/Compiler/main.☾':strd('c$~di>u%h}75=ZM7^5&aG^n*DBL%wfy3o}YEL#gnHUh{3L6KZ7;aze;QnFOTKb*vEk+g{GOX>u13fBnQpsiD*Z4k7!^JCsbPmo9GIdkLivXUI9UD(=L&dfPy&h?u^%06HpcGoUa*TvD&<?hPry6aNQ_xyfnIb?f~Y<Yu>+77WS8~*YQD_v^a8<SI;6Vy+F(CtNo(8VoLyiM92vYzgQ_5@wO+{ItR8v$j1$6xbHt3csB_655;H?vNQkt;~JFnf<ZX8!<2S>LnaGeP^I7lf(nCqpF0?!f$a>@|FU%6>%$-f%1Mkmhstz!Bf~+eqa%>?LwlGuFwhb@2GLMNSg&?7m~$tu)M%!ER{VxOA8#u^U7wES}wo26+@`mN@Yf_6_@j3em=_JiVp22(d?A-XBC;ZZsSvX^x^(tCzwd<OGouUHD17jGWA_$BHiLz)!6dyEXFCFwVK`-Gyt^`u@qiuTV7O2j`h5?r5L0QhIsHK4D)w<P;2k$3B9A7(HqexuRjl%W{`fqIy!$>1c9tEi#=5!XDv*^F3}5ZtZMSwKD4`H(emuL6?v}lbz~MH%?qQp*IXWi{Nc)W|W4w)qE7i>Zg{WJwf0T_0$6K8$V#@Ke0d1*_C%`9_53OT1!_fNeKN`O38JH>nWJ}5xdV`q6*<Oz+4|B*xGja#_iM_x_KIg9YaP_B_(lS&XDIR`z?C`zRSNgH}ImFwRKC$@D!fDFC_pQNExYeX}PK8k5ce}Gz8zsLaxsW>ylm%Q_9NK^{Q4t0<9H;-kVT4j`UhQcNb0}525&`VZM{bL`Wmt43kfgU`Rnm(sswEg#)(wUgi$GU+lYs#0v_E1vzc!#;lizd%4?7(xI0hBljInin~t}6|r(=e*VJp%IwVYnmf0=Fmna=a8j2RaHZb#hFo>%{=XSxK>V+HmhG$-!-Q2bxn<07j{>g@b1%<R&2(BVf$@|vKBGjKUs$GRL58!Nh2s^hbyDEpPx$x8?9b983s+aZTJq;|TvW0Q&mut5#^EhXMz_@_B46@p;B*^u{aa{-XVAA)ONFo7<A?#%mKf3Ar~{R9Zf5S{0x$befO!F%U0GRQTVI{&x)*2GE^cIl$Pek2B!=Tn{nXxckQc9eNj%sWDWQ7CTG6Q(q;u=GvIz`}L_zx~9{`JS2DC{O6Y6u&QX~|ZyvJVH)l@?KjsB)-S#1*E&~@J!H>zx$EGTdtT!mn{V|t@7aFmC`A8ufjy4kseQcSM`O~0i}1)-m$ULNuS(gb7p_p3IsTtrE(+tC=Q-2uR);M3`onXN$6^;r5{2{<)j&|*};JHZfO;=s$J-4N7(oA0pC*{7oTVinUULbxRW)e$#YfiM)I4*I!KxcEa7WjwqK|I(^ArBj3yK2}^ELggff$6CJ|XEt$8@+ePDZJO$zvhhh3ebgMRfCGixagq}}Q-kahMHt>+oJC6_X6LT1Qaa_pFAUt07jRR(V(&X8!odA#!cQR$Kexx}z&QUjoPQcLBA3eZAF{Loo=|0VbjQr}-NiN@;am0`G0;ERUApLy(yfKhe+gj9U|#Ye)4Zm)iW`sc2V35K9>@`bGiy#z3E(n;{|^54M<Rpa^2)rxVqdXWTvd<RolcPCX*9HH0~6)()9=8aLpRIGhcNkpo>bM&x*h{afGGU^e=rKq{$Oh8Sq;=|ZbW>pqcIJ8aLMcQ1R4hNHm1>|tkvsXmlvv*KM1{40`WA&+AX#I8LW~40QivHaL6v!ij7ky5L$EH%_0&YP%u2`t{EuAivxHBAT<rpxB&rbyDh}Pq|+hFWGNh=poAYkiQ#s+6Po0u^t6XU?zW2iVwCY=g@iaz%NvctIG{aSPgc&*8YLroLrk-e*faK?a$P}Ttp8$V71i@FKgAg5wW3($JH#ySg$J*vUYsc(F7ECR9ARlG$DTv>+oYjjsnT8Kialez|8^BpI@op?hdf<vB}ty;sW*Z;2Detx@c?f;c>KBrfLs|=i`iXv7gts<Q8U&NFsn|8xD8=?cbhZ&FWHyJ&g-Lnzf@4A<*c8aIK36cr$_sFKZ&o$WpLKPo<yPdri#gJi>;cX8p<?8EwNku=Tyo~5z_^VE{{V>xzu))p9ed`Q6-LxNz{gUWknkp*H!eszf!GxoPCoDg6oec3Jw7s7crG&Ex$iZ0>0HD@0|Hr=@tNM$GML?0Hi@{eVKB`YEEl1W<~I@yHIto*YFZfZmo(95J+N+Y(HfuFopKc^eoi_Q5lH4%ed>FPE$wTlI^n7tBod<tfAZ=`>t|`QYM8OP%TojszM+duB>&JmKWUBg+&t#^Vx>zuUl@s02k!;fav`u|KghC4<g<15Pd^f>xWyOe*+`W3kFdvY6HEvw6^Xpg20tTTy$VDB_Tz(A7y!x?xVhkH+r@fv=-@_W(oZYt}PrWQljq2oYULmB9u;i@c9!WPUyi`Ixss|G|ps@J%V!cg7RMPGdX#)50q;_xd9mgTL)_MXeYPrYB3h;%Vkm3nhQyQm3li#f)iG;6K`DAIw}u-GlkkwI(eZeyR=1t=C65?=P1J}6O}n5+t08Z$t7hXbxBO|A<OPfZEZ}=$iXF%a8VicTZ9WzZ$l>D?&pwnUE8*6bWJE++i%vahP}$yn`#E9>X2&-UAsY!x)|IgL>8z`=IMT2A*KM@lO)#|z)Q@pa<T)BWup`BdIR)l)s~LpD0kybbebDv!cPs4X)Epd;V35y{3}Z0W&uZDmc7Aoj(Lu~&>w$}agy?G^k?`Af_==M9j;G#ktwVRJDegFwM6gK4b|brZCL~{PiDCSbSY11m?7`8ZxuA+-Qytf%?ngpd-&DN+Ya00;MaHS0#cv`nG(G5dMqEE<0S<V$9cUf-H8b#Ki*&}R!;Wo^iUL%Lu?z%d~%N0D#-sp2&qzZoeJN{xrSw6nd-7xat@NdDESBy&KFZ5IS0>?Ko}z_V=B;7cuy`(CGyA-@D!tDC;xet2k>>?GGB6t=E8>5{wB{551~NVx}5-z8$oC9xQJ7vYe|V;dSLv3J>dKKQ=|z0c}ASHYWF67sd!jGwq6;pJz|ebV6BR5H^e~p7pEM4`?5DTc`6oDnz!t#3E*mY_ZdfuiZ>#=N=hiJcO)#7=RVOP)8rJgJL+bK<fW-3#5Z7vp`J(V6KZ)gP)2*UJ_72jp#$w4^1iS3@~*a~{63C5%Qv)#@2xD`1l_c71V`p<@CWsdMp&_EVRDctOCx#-pD2;w*Z?S$fP7<f-I!B&Nlb);w~*@@`;h%xhJ#Jck*VX!SaBdwC3m1||G3ENW_1*iVKn+6f#0&!wa{u4V~y&AT5ZxyL)>6wE0nM2Z`*JKjE7zn!}zu=AEnzgW-N+B_-7lcG>kuIdh(e2AuktPAlN`Su*Zv<!|6AZ^-Z$Xu;vY+JM1q;uc+QZ<gxLuqIJmQ)z;TlPJ`E!f`%+o_PBfQ_;Wx37^9zlNk76lb%kr*vK{7=V9|<VvHGc=wAyDv!NY>0On<(be40>og>$1u1V@3gj|OwqV+K_*npkm_-(lbB2vmH8{*TWs9M7$RM|a_x<T0M&Yy-t6q+5wYXWVUnJg2Q6kJET2NsWnU_km`f8k*UFbOzOLdei8<nTe<T;zK{)Gt-&b@t@Z5%DXcT*@HByqLwFMe4r~En9M%xTBeGhM2kx?L}nCl)I~G9ts00u{)Vv@j`oCpRqZakD?6doXl_uesFPNyUs;|LHMF!sJmTw0tu3qG>Y`TNa8{!=acvn*TTTUD7m|rtT^aFta|a3U<jt)mdt!Vi1WctW3x`y?v<M3|fPScnH9R#@*t8*|{TB&!Qep'),'Libraries/cache.☾':strd('c$~dfO>5gg5WVYH?9IDDh$tWZF!&H+hm;l?k{${{2-%Vn5y>`|Y#d4t33e&{fE1cidI*HlTWQl2dMHVI*gw|U)ymqnh3%$L9irXw)7zQRyr(omCyvp&)7bYqWlckHxt@<~J7@-pZDV>)-_SE1(P#7%{5_|q^treX#eG1^{5f`EI-oDMb~eRx1Rx?%VhklIP=Mg<b6|#ZU<NZWuj!?X!P83A(UYeHz&Q32CrLVKo%d_lT+Aq7b5~j~lHElM_TvxSkubMayjg_5C1F-o{8ABqMZzqr_~jz}l7ul;{E9_Hpjvx?O_M;1rX>$a!wExaNEZ0wB`ng_sWKVo^d0?%$`zEtjkMD^+d=mY+ip6MXWK<oWJDGC2=^qS#{L0h0uwCGAOr<5YPJ$YkLej5=1H)t<0airQ%PcgdpWy8&9cJNauGPkb(Iu!g?|YA`6D8MUfxKh0N%;I)VYa-VQ`H-FTs6X6i9L^C6Sa$M~9PaV?q_Qk{tTd`Y@fFAn~F(=0=*CWx}RT(;D1mHiFPgod%~ja#P3Ak>9S+Bl@0xgeB10t!8*w*>J+xlWL8-Z8(b<IrlUdo6E%5+r6Z}`2A|8#pKv)#cD<=>nJ*KvEODh&FlFA8=lcC`h_5;=^}ap>njKwL2NtqxD|F2k01|9Mf3u%udQ#^s`s{8O9(0Ss413EXi-xv!Bi|^6<+VEHSZiliCmMTfs;DPEA69TY|LjU7ZAIBOFlp}3;SHd7r5xKYnB!<ynYZTF;R~Y;y-~m@!hCnUy|)j#nbyY@$jk&TgE4#H(?Xp5&psuc(I?M*lF$3|EpmT4Mzu&m?ic?aOgyJ*I}OUp^UN(mvJTDcQPqg+HN;$XM(P@!<OTwpOUvs_Y3LjYt8_6Q0AmFKK>IFAT%xS$PxWbf8yQL)O5+`ET-?Q5Ux!;s%cz>*f07?6&(KrTbgaNz*@Cx*B);@+<vqJ*0vY6>R^AEF_qHOOS<^Sj>qz>N^*+)H-0jN(>z(k&q974%S$P#b^QShOBX)'),'Libraries/text_format.☾':strd('c$~!=Yi|@s^1FXUD-xO>XG~_-IDm7TTmqbsE;&a)bdh$g)jr1d9{cd^uFp$CBrsl^gqOj_!3hu?9(h2V6A%Om4ifzX@*6V0;C{kYRX^sjvj*o&NS5xduCA`CuBxu;p;DV}G~2A{4REn8o{Aqzh0>JAMl+083$<doz{G;M?XW?Zy(rE=NA@m{GBGD^ixtkr8S!7Sj!S4Q#|5_SFtt8mrCw5*Kq8ODMJ`T?E8@P{a!zcBW!T}S_)PrF<<KT{#CxP54g-SA;*rg~YRh9Oo6D_ioBf5Q-1II9Cw_Pj8#ep_q36YC?;k$M!_xD7eyTD#RfS*MYv%JdZDeKvRx4GTHp<BPK@^;*{QUrT?W{YFV9^D!ex+6SVhE{mT!?`E2j1l=8zBRHqEavCy;dpT^8Vez6-{qvsZpD*R6WiQBf!daQpH>@%ikK!<;t(Vk$!_3^Vf0Lt{u<jI&KPn>2Zt1BeHd`)6SQs3e6Z@ivunAe@Dwcu86xedvNDlw#9ZZe%K)r%^LDWLWGon{O|kV5a+`VNb~V04iaw76de|k#E~a<)4?;{6sL${xzTP`YH^C{>^lxSmKkwJStr}7R!ScKN2Bfmj19p7kF!^q<)64?kuA_-&@vj+*PM5V;z@B;tnm(P#NLEeWC0!AwOXlrt%zZ3E1MJ7MR(uZM*_1VBKFSKbhXmvR<16U*@khL0J1uY$j{J7*TtfE!a)nDfI_tz)4c;+0KV-=li!fm7ZD*s+gQKUKS~sGfR14@B%z^3ZH!u6YX08XeiZnDI7jAvMV!pIHrLVw4i;jN3^(GFwk`Gg0`?Gq=ZHcNl)VW?N1F%gtKtbUyefX=vY|~^#il(vz~GOBURTxvTq?7WNZ@W7KbuDD02{Gs9WtX>B?30fWLQeljMJSH--{ax02HG;q=FrW$AP*ek76Yf%Wgr2R4^`sDdI?kl*5Knw%+A>b|^I-G5yfyO17rgo@v&VA*sC`Ms_+d@Yj%2k*=o;WlpMFPzSxJ+S3_}S&IJC4Dg^e9*v2{!z2+qZWR)~sN!KYIUW+q%S1wTc2)MKI`G9n&022aL-Be+oFq$EI}EX^9T)&fh6g{C>O%!ghDZ!5mGmxkdsm|EpXFIvxPzt5VkAaX@i1}nwbw$k32Y^B6=ufJBP`hViCEx&D}d?2Y42$Hr$5bo;JWU_?$WTQdfsp`MbTSs;@EvGqGe2CHY4sjYzqEX=O4Oewbe*pj@mma4-_xmUzvsxah6qDOxz8vm__8RV@_bBk(gtMPW2F-B8xI^9$|s7>y0*fU9d)??S!!G)yq5!9sueF?ix+z!u>LcM2F%uqjL2UH7*mlhz2AlHq_!}rnevJaVisF1COzdD=kD_Dda|JaHI5iBuq#X>NSH_yHGmX<T4t4ADlkQCt<zjNw@hxTxML3&Y#4ai~xfY?QU$&L_itpWPt1+6~YnyuHDBw1CQxl@n(X{DK%*Gi)iJpI{HumGX@W{D4Vej9yJ=|POB(ovqHTrhhy*a$Xs|822sM~f&6HhN18Jpbz*Re1$G}50CPHkEJ8o&<~ReJ&&f<+UR;KB{)+KSdD1qI#0rcQF@E)(f}MMI|68co=;RHZiOG!Rj<_RxC*b}mRwgrHK|)p(+B|X)T^;g!uO~bb6=abJr5|o+@v^wAZIJTUl+ItnDZ5TrkyAS%pU~%<l81#315zX&1nkGHtYw>6ZjOa!AWx5a6CDNxL~|5r8>7LO;(KoS=hyx7U;F28=4R5ayVpN|%RhhHKYz!vRWWo~-oj&vxA4AgT)-et(#3~nlMOOv%U?Nbp*Ug42}`lwwJBd;S+WdwnEWJ$#4*@g5|WW|A95Fpr{N7&UcBX%V9RlBlzkllI9d;1K!$SKVM<A%l;2?=A-lXzMwo)o4W$QM3lzLycm9zX*;KI{BXR2E#yj}dw?nX3LhUU5NV4Bi1Y?=^x;O{L^>NwxPFDyC)THm}n+B;q6N`9*kPX33iB|N^*oQAw(t`8$luL$*QF8>O0&u*OVol6PRpH3?(x}W~BQTN^2%$SkcZY!#HI~%|B}yo_pq3v~GMN$&_9^}8JiFUvx%sEFyge-==4`Vt-RB8F`(Zh=$933rW*4MLuvtu&xYww_c~@)(cUWRd1xY~JHev=9GF%6T`Y9$z*gytov;=%w$1KoP8JNWYhwlXFh-EvdkM$)M(?Wfw-#ds_LM;Q?Q7c3D^Et87Tgb;knR=9yo+oo{lVZ$^YvPf($7Anm__6|w)od(0PKhVBjJM0;g2_T1)Xo;lQSnk`610msg{oFIP-)pJ>D5{bG!j#kv6F49C@`GYwc(iKQaU%GzJ@HRlfxZbQ;petsZsV~9#zhyT-Q8#LIgCt(Lra*ih*!WVNFcJ*4EzCh}9>(pg`M^Z%dVSHNL5d*QE?yaedD|i(!jPwRWU}9dk-0b?2@@Xb&%!?q1@?&&@R;A5q86!E9NzWe3%{na2oXSuO?X#&yPM%QKy*k=uVfI9RTf+9vOWq#}4I1ZxU1Fu+)W-hGF%V27#tSG|p#5(|`+VtY@vwDh9*iAG&DdaT-~s=cq;XR3Xm+J~xrq}nIMz%>y5XVrTsP7viqh4Hh&_=O;sXkKDoP&mIBoTp~)jGEgtbDL`YNrN+I=ANm!IWu?4^p;F--t;ai{0#%SL~jxs1YZ(&sJ%>FoFXYNkWLWyvAAJ+>!$a$>TMX<MhJGx^lqEp9n<^9^u9H{n<`WJLbbP4yQbPzoyn;7JJo)x-y_ucx@x~v?FJg|?@M?5r4#<WTk=`NE$-RlUtRXEe(tZX`wt)Z4<A0?^t;Q?pZeX)es|69F8SRr{q9A-d&%#v_}x|YoKh~PO>g(}U;XaqW;pD3uj)bRb-#PX%<MAYwBP;0fJgl9H8a?2da(4m85GRY-3C@Pus#05r)IGCw-f&SqJR3j*!XQ;zy9ngo1S?Q+B2bFiC*7pdIi%fnO@oSJkv94ce@5w{NJ^Um*965eiz|)0e)-nTZi9`-&dBPS%u#+{Gc$gKM5tg;QgV;5eh7HZv|KOz3_uaB<~(&2O*W9+*AdTtsX#LkYk6#vB?FjiHTthc$SkL|M(OCt4Eg1g!hfTmz)W|+nWd@_)rX-mep4rdsu?w*t-b)_Mv~q;3J7ycJNrM-t3mdS@D!pXj$d>o^YHcOkL4aVV4UP4f;9ftk~@LpnI<8r6;itpz5DWu{BcovbdqzZy;HeHD<ecEGRZ1&4hZY&ft&(V5oKjc(x<!RIgL=rrYcQHI+s^z@IL(TC%V{qCN{zbrclyN3ck1ADi}is@#LTvooKs7iwNUA4QjOr?)JQ*pmJL1;y25#!9<sD@KHZR?^EFu9LGpjLHbtZ;`s7Z_zy?{b<Av(})y@XU(^j5G83oH^a!b*?3KTNKHP(K)0COft9}+%Sk&sD{ZgV;&FGjcC_$6{al@FAPxghaQf{n;{oJ5wDqAxdEv^~ro7+&QF&!b)al3WOR&1IO;*>p!RkAIh}CzJSzQ(ndRev9X+~VgiN3sO{}{l3DDXI(@+SQogGliyvu|j=5nuJQn4=n5);RpAek#Pewb5iM&m2dU&<h^v@2DO6hXK0gRWB#%CDb0s=P|Usy?=lHz=!XT9XfJ2pXZa+MiCNHv~6z5PqmPH%MQUPI|dN71i^O^0AQoXB{?qXaZ`?)dfbv@xn4d{Tl%G%V8uoUUs4+#8bN&mBlz2J0ELR;0eS{H8-QmuTz;GfsO-ocbyb9$>ORd-*#b~%C2qo(U0jv`Cj4lPZiOBX<mVs42?bayT1sge38r9eVcW0<j1MuO(I2JTUaOsN;|KeRMzdCEb7kP#;H2kJbsq`&mNz+RVfNs<@|`y_IqSh6oQ5<MpJ_+XwfvPiOND1e-IS=IF_xFF0CCnTR10MW!=l$@?OCt-ACCc#?K%Y3T)jQzL11mQS$nEdpJc}xGgg_+7V2%*sN<-~iZjj0S1?kh(heJzRk3~(FQ`x8xG5MAxBk`ef4J?RKJ67+K)lduRLX@`nWWHP!gw*X2&>_jT2zYfGy-dWU;63!{Q##NC)|spX4Q9^0%)_4s~2<iQm$Uk)lt<&sCw!7C5(^$rjII>qBA&Qy#R&vB9yj=khlq;RA(>-q};7gz~OWC&da00A%N-&1#1iJt$A;54?%A7e?(B+5&'),'Libraries/Compiler/to_ast.☾':strd('c$~djZEw`b9e<xs;d^D9EYWVR(y2(RYe-UhY9NRt(n%q*9IumD?AosFg^j98goGR=I+_Ovx$DsqP_96@^scI|(B8v~k@~iuq5BE=2>t(O#^dqR?p{ER5T5nS{GT6wGrJnuAa^g%{7N$n9DQ{0^7NHi!_d^gz7aT)9fWE{S#ElZW;4|EilVAI{LdDTO-x*vnm#`^HDioVO^#iHZIs%tCvm0N1Y`Po`ZA2?&(;=(v@)j4f!P{qn2}k;G)n{*E9dG8K8?WFE>2G%;rrw{*?`rD<bbTzFI*YBsB7dF`6GFusc#-V+`if#tyX{j=F$GQDiRel2OA&8Qx9K!$T%L72V}RR{1W7_b)B&^EU%T~i%&{uhwN**cCik_7v!;~;zH!{QR<EDM%_El{<9uhf#c(lvYHLr2?v<+2jYMW(;RxzZJCZc5M5lDrYjR0YS>Fk<QZldX<(v#@>lW$eSXKEU-RcT73GE*xJJ0*1yLP$SClAlT1L}$m!lQKahE*)ddUkc+gNHhn;>Omt<<T_D@tQ=+3?LEw1aw;eF9=P45~pC*mk_`%o*VL2l7lmH>AK{AGy#7+OY6uUo8T=<z2Udp&72&A>*l!EJa|$*ryP&O|!MwFwveTWbYh4kH~#Z1Uq{_UtNe}8Q!UpDt&?#ugHl;)*y8Mre(;{@LnUw<a-g^xNm&!il)^nK;^f;qrTiH+w}Q8S%=KI3Vzf%>x#lt<N^7V+!s_-1(xWEcq5UH&JOL!jG{oK^k^(7jBC=k8t3N3<dpV4B<K4J6)rT;(YZUghAh0>i(%XEYjlwc$Ux)E(Q^rBW=stnznPh+Ey!ZkbbKR3futtiiA2C)=hQ38#N_$83-u)GN_@}Ma+V4rk_90C0nJazH&h{b3dZ1-*}$}}IqtH;k~LHry(m~sb_4Mwd6L)oN8dY3Y)a78<*nI#QcSm@IAL~6nr>i6?Z8zod9Ix(0k)M`i1%0n$R;_G)PkjJ^=gJD$P%v@u}5apld0H9mdOd?%L#&>UaLr3;G>*B!vD%ymI}ujIngD`BP^J3Upio<U>SvA8C`hG6iBIQH)ShC3RGeB>Rh#2U8;Uiv&Cppj7;^N*om6wo$3+V@5q7N0kj}(lAWZap~!Mf-Gb3eTyuog<Q*!*gB=+r!7c}Ml21ahpp~u4>^YcEQwiFua8RD5#bd%|Rl`|w?1n^Cs*u{SP~y~D)E0k+pa{{B#3Znxva}4}3!TXE+)#EEWuH<q+w9XSHteP%1<kxlOD?Wg7b=Q8;kbS~ViO5{v(YdXo1S$oEN~fzuOMg;70nCktckyQwEYjMgY(IA$ufvK&8io7W>9>Od_i5cNB+W}2mJY1D{9=g0H(f@TQ2xDi~?2e!$p7sy@aAfb-p}qwb<}zt&KfduPan5<Jxt@HCrl8-hQH<;eETDQXnX?m5FI%e8?>d;u#TidbJ{afv+650bnV;w0rl7(Xg#j1jQw>5cbE~|9cm=V3Rgmp(@Of5#q**6JBFy7@tM185!}*)Y9Y}u(Jiqej6VJcDA~kJMb^_c~Ablmzm#_<{#aJclS`hTx<z2_B<UK2jnwdqYgO+hs5Sh5<)K%d|e3fi7XL(*gJ&)x5+N0`Ux2Cr-*?X-+v|R|KL_3`&4d4^`t+dpA+gpJQEgLCNx1r3UA0$a+my5i(?ojYdV`q@{Dc)$nG26J2#6mzMog_k-yV&@nave<SG$z>Q$-Sc54x$vIuMaBB@q+Yov_f`OFl<qAExw{R6vdiqWDNSz^@ae)YKf)syb#c6W2P`|@`8Plw&3--Duv2(x-205r;wWDXM~5dL*BgvY7FJcwsg2jpgEYP1aB%iZuE`J8T(i``@Xe42C~%kx*UxZ~?5$uyNnAF*_)hw{EQ%*FjFwk?EosM>~*@ws$Zq|#%^roa^C`!6;1>IYRBR^p?hgmj^$80uRhri|*eb5hAhtP#`qZMUJ7CCmwVsdEK6HaOJvL5!EQD#pig;T#re)k<k@o{-}_t74zM&U>MNQJm*+OjS9>*We3`)k3-upFQYuL*<CVu0o<QGNt>=5DTM{FRCT6o{sIFhEzvXshmlrjSGuPYtlPjdOGPMoXn>xaf(z@!Jo?bq(uA}rX1%om|fMS`(@HVnr76qW=1VIqHwEvXjDKbUc)v#KMf{2cqtipZQqE@VA+nsvPus)qoB?&2R^{no?sOKQqeSO5ZNwFn-N|$4S;7mMX|x)wcYUp*>X(9{Fy-0GM!~S-CDqd&|Pq<yM1$fY*u9+j<>-i+nKrk8pZpiI2PD_uDpr`gU)Fs^<D7-CMgaw@A;KX%wOt#65(ONzZdsQb5m2N<lf8jxmJVM)Sr>pgJ1QP1@L<`^O74rc3-Q@xIBZ2Kkj?Z0eIa}GrQ3Jh~yh>%QoQ5{B<_?@ib-utnz%rS}`5BSDZ(7;F`f|;R=>vcGE74^q7blF85>t!t~6OzDOz;?=0B2HU=>uM~GGeYpwaP=~%W_V{l4GYy*dqdMV5uApK&YDkZIegVi*K&&eTOA%wqao8gLOM)Ve;R7>QGN5pikXN8^@@=dZMAuJ(Yr=qO#E+yI#eeMDwQFsUMSAa3%`cqLlG}w`auIIICwVVG3tsZcp_xSVA@$=N$ZQU+cZIH5`y~Ds8wc8prgUGNvx4bt3K1)t@+dn4fNj8FJ#RhP2k<NFWB=DHzXF4*5KscRmt0L@*icZg4knWv>Y^h>wh0pU{I&%;3HdUhM;q&yT%boSUhwecH>t#EuF0NHrJz!_Nvo&45NRp4wXXB2p{`cV*sav45{c%<fhyM2*&v`0*3C`O;M1OWfKMhwy!!n!A0U~?8PXh8Y7Mz%7=FVTfGCe+~%ILPXz+vQ<nftLL+__DjCAX>+v+E1FvpzOK`VEU=If2!73LBW!4uVxE1HGD8d)e;vM|l|hIkRBk9FiTfRbZb)d|Xw0nJKy*h54D7S}zFpEX2=Tw%~10$(>=Y6QwO`cP!hF*iHE7iW%Zv{nJ6dUYiU80A^6!uETi_zh;X(Wo%~lJ^3EnbWk85IK=GEj$E9^kobXvG5In6IAO*xH0cKkn##WZ2J5qduKy36b?nX'),'Libraries/Compiler/rewriters.☾':strd('c%0Q7TXPgu`ki0VKJ__aoSGR{g_PM9L)N7hfdZ^`E2g?SlTMg&GBedPiNlK}cnMxWfq+3kKo&)#qO7{QUa0cC?_by|et|z>zwg}ooYSX!CLj-+qM4r4=l0!ir-!iD*jon=|Aj;m-tB$%;DJL&qKJg;czJ#y?uV6NsokBA+kHYSK^Ri_Uv%BQXU{YH4m`bk-{EL_-^}j)Fo@6f*BR`o2f;mWK5!83XCJN4Z6m!n9YoD;XAn$I1w<?qu<Pt6_BnKZgWa4AWaDr$c<!0!qv=C4yN}Ee5<U&vA?zCaoSnt7vvato325Bk?IiFhym#^zb}8<N)8iw#ngEEfSD}4Ve5I5OY0ymrc7lDteu7=oZQB--#UM>yN?U^@TI{9>>3MdR{X{3X1@Nc7Ru>0pkA%(caxc1f@)cN5K_@#*W?lQqfHbFOpFOZg%=Rh!xq?{OV8^Fm=?!*~;x^B*i|iNv`H}p*saKz^%~kY-vvu=J!~C*ij>Ch4&(f@&B36#1D+!hR?hlp+4|U&s2gb%~#>Om2bn~Zj@W(*g%jZIBfj9yxLAIr|7tOa{?7K9>-JE6@O&%Oh=HVuKTy+pkO$8y$6$Wu<!GuCSLi~l)eV9Fmq0!MKUXXn>>z`m>vU8L2)0m6XB4{lJL*B%{CGCD9dzy0(DY2J?f1Gm>)TeCzgwdDSXM)`Q7gidz+Aai&Dlrns!-0su$VD9frO99=?YK<wJIboTf(koGu5U>A>)m_bZ~S^4I!uU1R800sSWz^^PN7g&MjH$Z#U9L7m<b#Igpz+ByLn+Hsnz0Nufylg+CurJMBn_z<Q69Ga|^&0qtJnzQ?#st+|hxWv`wY|mg8R3?<LJv+$O_J-lnvklyY^Xj=Sdi;RHLwE@<t5gr`JKeUojF@V6`Pe+k!Zxc&*(k8s`n?aIb+xL$?*&puHJc2<IV1FjleJ1W60_^5Nv7Hc(dEq0t;W*4i=@r%hIjXQk=@f3h)E_C&CxW0f37Q6}zUi}KLui?4_7c74D8@RqTHU!V#hv)C#!Og*D!dktt;}4HL{>08*@q7~y!tu1tlm@P-q{8~d)Ozo+TclKBhJloGA>PNK^@gF+sCd}w1OUl~)&k!3<mdWW>k7;P$!3RKo662t*mv9(i_Z1O!6a5WX4~-~0i;uED%_lf><`ksx`oDQaIBZ~ImM(3N|t+rW7uD)A>QYO=W4auVr^Ian9<l;?it_uEA!d6j`eNOKi0RuMN2D#zCGA&g4vxWoV4y~YdCF5zZv(EP%?t!2Ve)3n5cO)PJKqz6shg1*~F}vNTY6)T^>x~nqkhYdlxTY*9qvc4#xWj!rAbSYo$1g9A}#bH~H;YQavKwC}Gte;Z_ZHM?_NvAAQEI8Onz9mAUod7_NwRC*7TPx&w1B+$`HB*1*ef41^4+wb${mJmzMzjXGNzEyE|+_v}lg$wjtiO?!4S*e-6+r-l9c0kDO)v$8y&<mK04?M||UJq!8j14kX*AR(b)C9pig8-;*<$u>bL{(3t!g+Y$KUXG6E4j$gSXJ*fVzwJN#_x*bg9e8%8y4Y^@GWl{;mjtNS?Mr~fBC1`W1DYk@Ut*W^k~M1gijrY(>lm?|`Ek+nIiTm>JFnW~HHwPXnlN1K0`d=%v=gVta_YO)kA}T8iU-|gD{RX%x)82mSm1qz-QIM#1y_@(2-Tn;LF0CT{lra)3_5ERF#s?U_Aa~XJn6Sv&4kp|vfLAyQ?counSG=V!70S1YEdw^Vg(S$15$V0`{GK-71|B<7W=o{0Yo9jUOld{2M*YtfFZxn41#M92m#J<ozDTQ;JhYm{GkL3$-%*bCJZM`fG>yCgjn<#A7s-nQu=hmVa@BHUvXXwK01fI3P||>W+B2e93~@CZj{iE1LPt@{ocIeW1YHyDe?l;7#kqaJ3p{DOhv#Kqtxxe?XD{%$VVjK3aX+mEVF9M!sXwtd~i85rpIw-*vDM`;K~(i5GE5)Y;#L+U%6D1az@-FxrD=o>!IW5ZjrT-N`QKg%OoH~4xkb&?hd`e)~L=~bXR)OAWoN(LEf8Q=-SycUkU*Nmy>Y485*t+5Hv$@RbiKa;Tky|8aLHn@uQ6LKHy%ffUH4z(vOfsUjCfUGpC>B1PO1;?kX1DrX@XISm=XSGieIkv@K2<J4_p#Hk~10xf!<|5yZbk)wtJ7ItyfC+R~i(hul;$LIvf5Zc%y^GpG~O)ShIz+H5CrN-U)e@m-&*2b4s62|fK#jCkp2tDOk$zip_wRjqDrS9{$apx0VpRrAGrcO9sw)dH*8h@@?eIkQ$YhBNy$$@J&t=Q;U#6{d9N1m1<lvdPXlPI%^w=Qy+=<`$_C&H=VaoVj7;&?vF-<?a=je#Bmt)Ng8E%bC%b&}ALY!xH8Eo-1Kn#B8^fH-*j6_;v{HA-ISKgH&hW8|pdS*Nyv{DQr7H*mlfW84P83q)RAtP|{A8la5CTi7dK|=Wl|_RFRVQmOb&~><D&|beZ$fZq1@yu7@FXqTj4|Jg4dE_z~lTmoUY7_Bweexy@mg#RHaVw|Jm2A<!x!Hl4~V(#+_niMT~%_lo+7+|ijek-D(dQ@Gum0<4&N*D8pZPFHzoYNOj))fXk@Fp=>-U(v9|nIV92=h4=p)ctJquq=ZUop=;~X3=F<bt9Ax#?NNp<apA~ydKqRdJ30GZo;zJP^3#{JC}ob#O~07mjW&PYCidz6v&ez&ZHSGyo>RS>(_h?e3CqL(l`8b3~~t^wzsnyw_6K=)GYy~w}Qp)3fO1hRKX|#Fv=sLS8y{P8Lv?F20N26r}XyBxY<Z|=OYopU~XM0O%_&~Ndzw5SFU0N%%dH*BMe<Df<S;)aadtFMQc~-?ams*CC(Q?9y^FC{m9w2#r>qCqjKR33a_XmyrMCxQ9MXAyht4<PU-k&KuHI2X)~ArqM8f`XfUyZyHVRS!qix+vyyCcCXg1lvsL3LhCeI|2{t=wF888t4^zCYPR>Lknf7rqao=8W#C0wv7hqc!kusLKDgC%p>{fvh)nt%1aGiap^7d~N?dhYj`OlA`41u_D{+ZpOWFMstnQ~|+Y0_Txh6IAAUDK->#AJGtSE#T-5<b2mPJbi3!z}rdZ%rLHO0O;p8qF;XWmy$>PW0Nk2#SB><q`0&Fqhz$Z?UG16Y~K=QDpDsX0W#z2ixLevi6qq^c=xi`h8a9-wRTk<yw*Z2Ov|eL9%?`GBpZ0UTPI9{ALdeARvz+cl>RdXc>?-mW<p5zOP7!!fYlNc(YNs;uf+|Mv_8r?#ZcOM`<cZm3I&aW=14ab8E;68Ws6!u{SdyBK58}QePc6Qnz-}H91r&y^IZTUS~C9&IZicFy<7w0<hg=)=rG`&$EERu8guO5U8p<-sJ*W)d3iKTYfD%YEt$ddj~vT@jRPa>LC!2RrC+!tP|YUyj?i0^yFnXPcmurks9x$w{m3_cS#=;Rf6W!G%Xvc=e;R}*>@a=KG+QJhjt}7v#R~0T`ZKf(&kFbjyzov1PRQU3zOH;k#}4dR|xFKIz@&dlPE?%k;IRwyIqa@N<C-(rgKh9h+ym$!TGI-pyBVEP#~xo6eZzANg7kIeXMBs78yy^%BVT#3#4nr+~-1Co>I9#h|2dlKFk(GTLGys6tJvO++WK3m~LnUeF}?^n?-tLA?b7%5^!Xl4kfkL4J<*vxo(wcsTtW?d4e)Owz}Akiwfe(x2ps^bflyEX0f3dLCHc4xKrCI%aEvJDTqU!dY30X^ml$@Y8aYDbRCd@4=zeC`ZysVLumW+u*~c1ERlj(i)%Y!d&yMEA*sDn#&FH^1SoT9#2Wwo*VgCON-XnsDk3ZJny^?Gq;GhdUFNKDnr(>bin1&QHir_4f-boPl)spmZA2BuOZQ@bEl<%%wO^VEIm|P~N?c9lEmX6jw}=5Q(ef2xs_|B{K;GICZhD@y^fA0KPU~RpL9mAu_;vOnTd#<tbze{M<-P}YH`t@x!Ce2ISCt8I<k-wVnDHDfu+cCNDiW=RPVrr7HFVzgq+AQ|4w+zY!)hmRt#j;MGhvWP(6LEiw__eA8;ZINc;_t<KMaFMbIyC77o84t1nB_8QtseADkCI9257=Dd9;pxY1TqT5(w+Eyfab;+mY&y<j6DCMw1A)Irw5mx!|Md$aMM4T~U+O?T96Nj_p8UYKHwqD3N*U3vitdbGamdSmlz8V7XMZLRdSSAMgem)F?#5j1;!ZLs##Uda1Ot-!<<U_xr6SmHx!k=V)iwpM}|OB#7{^!JF&K1+4ATcd@>kzxU>O{Uy<NO?|hpHJ=xecge|n+I9R5c0wk(pr`UxJ%R14p?NL0c}||u!HLEKQI~|WIjmO>=G38((`?OuvI0r`%@#d!Vs8=f9IE3Eu#S_tGI?)JsKtCin?E!)WX`y_N^nzGr46elCaDMp{>D+E-gUfYbF8(v1y%E9Ce&S7qRYgKfvapQ%E6O)>#k;`HTm9yAq|dA)X~`VbBAn6s^}w=QlgsO-Z88nXi2JQ2*r`gin3M>&O4a+=t_Pd<fSz36>(9X!AiL(ALE#_bBk!p)+zQKKJ3Z0)S|D+oUDAQ$r#h>M`^Mc@u8d83$QZ^J!U=K&^Wvxz<WwAyHri8Tx<U5oa9+&pZN|F$~x1xlWtsNxz4%h#$V;RrVhc2Ij#2^lIq?{P{szbV5geRD)lYrz`;j~C&Zrv=Vk$%@3P}LD7o|QkKHn0U?3Q^mrYRe>z-yGYQf-61bB#!)y-5>x#}EY8eAFUmY=V!!(m{_YO|M8`voMfB1AlZw->V8(;*#w);+W8`I=obd)myoMy|&w9Sd1w@<+U!kW>O!32ZlEG+s?Zl*gB{EBuaIc}pZmazrgh{Zs4*`DV;ry-k(B%ym_Z^W3IKEBgQ{XMp<z=rYk>I|o5n3C{Bx-`LFEGA|WBtTv6)IS5H<pHf;EKm3eJrmh4$O>Fy&+}HKkQ^cW}jmu%K01A1g2(wXj7ih7MyPANPrReLk^5)(?RER6FEog+(MqAnntSg3=a~MiYobXk-1bM2hPCrQpq^51W)zN=~P7WQ1b}9f6yzr3ei@2C@#oZ*i<VWcDAfyqYMiHYZ=hY$RcI{qTy^|0hy-XUgant|wDETC`4Tsn=x>_~^-pmW2cj*ORE)%^Ki45mugO#OZm^)R*Uy+FieSam`a?Z$6o#Q}LbIGLQDNuB}dttVMN2>_JQ?PTxFTGe$RV}PFC~uHbYmb8|y^_ZYk)z!8%b!jw%W)c+wUwn|1kRVRoA{-hI-!J_VUaEd_Pe+7i|2(>v4SiTafbm7Y0d*K@q+k^i)MvWuK%P?A*jd{;5H7_AoNaI)r1jPBI#sM&Zlv6Yws&-$6qm*^%fK%9j~vRY_<HNkJbFqjoicvoh+)5ZkePY)&)Dr5}v|QQe6Uyg#E#bDstoQ+<SL<VoW~8nCO^}w%jx90!X)-B!Fygsmz;db@mP!!3^Qk2g6x)@JLfJoTC{OPK+q@NWIxib|Q7>=}3n23yB$!P=&wcE@D}5C`Sk=g-%{srJkBfskjySGNbWx@8l;~Bc09sSdA)}c#e7wKpG<KKfCHZQ>)L`hS@1r>v*N3mV4c_yynU`(OSlS5B?qwD7&S;mo;Gp->WQSHBQ|D4e^f4jQ1Uv9pk?>C4h=FmzUr&ir6pe_fh~0Fw!glo&{q!l6|*x*r}TX(R))REc`_bktXHnL-?};E#kLT@cE2rvnJqVf$`(LXjE3E!xfbFMyvS<x0?Du_D!}<G6JigB2W!=<9-BUm9u2jQm-jg{zLZqRG|NvnIjSY2u%bo!2aFO&Hy3kgPu&PICd}y#q0NZi`p>I?FG8_P=G%C5P+tFr*c(jD=3o@q7;#mV>Qm{{48_F&thc1T`)qp^1m<?+9mdD)RnjbO4Z#IRXAbpL%sTyof_1hpjis%)$T0qSD!0li`>z~z+7!4l`|O==NBb${KpHp9nIdxmf^DU$eTNoFz;P*^_>i*`rfh;k+g|so=4?(*ddEhd}SxDBq!wn7C6_yQ|l*f@OMb0Hv1oR9y5;'),'Libraries/Compiler/lambdas.☾':strd('c%02z>u(cB5dY3!aeP2~mpGQ~5TQh})IjJ%1QPM+mk?QgoQoBcSmz6mR+W+z(i8;PIDzm82_TSoMHC83tI&Sfzr^_q_!GLbuiM)@JC1SEMgs5M?#}#Xc4l^FY!hF>*G5l$Yo<~#`tJDX$jQ^Gl!@$1B?m=}ABt0%bg^t&5d$HM{Lj`64h?-XJaTw&_*Cl1@X^5&WCta5>?o|1o5+~H9vLO$v7Y$&zI{16Z{S<_MJk=kr7ldswk3QUZ<3XdaTPyLqR%Uf8;C!?g~z2iWDV>y$X_9Epzn_%qcCZReNmfD!JlKh(~dVq-<v`}$!RP$9x;xO48e;P{1IQLyq587GGUqBa#eiX0{mp(V|)icF$R)`5HV&E8Zbv*ERyA)v`N^?Bp*6DY{o5k!@y*x9a#HQ7oH^?-<ieq`AjZt;5odGYXgS<%sxSJAUb=Z!q4Fc_@zlzb#^)ti}f=t8FsO38x++i{LV7jj;L!{Tng)FODdA;*_fPifg%7)Pv-a`a0OG@JoPdX(QGtbD%q1c6VKykshpin(M{J)uG1y_0)LV^r4U|I{)BLZ6CtWqa1iLBINr8{W2prkZ*?5fN<6a?wo6`u%_)zkooSdY+iu!*9clOpv4o7{$~dMPLoYFgUS<rswNlq8Id*=^IiGe@7ta;S6Sh;9kUSrdHkufZx<)c-psj~B<S8g1jRHQQj2kIx8Q-Idx{3b)8>?R5ny+omSGf)ZYm4ci;M(Wg)`6J?cQAtj0oTtfm5+#80|RrDyO~%DP8fCl{!smu0A(&wE*7#jQY=kzZMF^7t26b=hqGs5u~`0)o#~gOw4zP2GwVGu{XQm?eqqqrkSyXL2`WVft~qAYPw_SUm$%Haq;Q;?oZ_MZ6($DvY&y>+64->l5E>ru`rU^}2Q7?(E>+ARri?>Qomxf>zi8rDuPhU7tv*7YeOOi}%me=HV(<VwX|vJ7WZ8CHGuAFlg;Cko*eGV%Ax5eh_IhS`wO(D2#+Q>L`wPslC*GPJ_QV?-BAKJ}?U<s+e<!xs6Yr2QuI#ljg1p|9)E3B=P4UaQgkC<|+&tc?&EkK+fOynpQM6vUU9a3>p*Jj|%27s+vaq@@&&<DGS*}+eX!{jckfXd9Wn=V4n#0fVa{yDtcTD!;0lvzUH@6s?xVcWtDO<>0YMRANcs>Y8#h*daVro&FN{FdtJfltZ(kVyhb8uUn%p7L%E5#VPiy265DY}TEC7Et<j19*vW6B}!T6vFnf~-+-I2D36NX5~qY#=3n)|C=#EP0co07{!OK7ANNTa}s9gGUhYiK)_MGmy;D^=cyLB7b-RVBJi<nGU3MO*jt+IB!OW>2<(Rkb8jGYFC$m*Li@Q!}sx~Y3(kolOeE9a#(OQ0L$5XSSM6iP1cc0@>T0gXFHq4|ChUEGQq58f0FraSPc-+#Hn2<W;}~wP&QhFGP-L}RIP}#WXJFh?*cq_Q!Vi*R>M#5-}Lk8w&fW3rW?G<J^Yk#<8Vi({e|s_&v{6qb$5aM`wj8>c#}qOUE+g^l)XNQSy*pfLt3owBU<XyV?zk)2_Nd1a^gvG;xtyp{qdD0Dz`(DlMLUGh!`=&l#|?6{M2|@q*;4qIV4rd3u?O@Bz>n#ufhXmWE}9WT(87s$r-YYE`t^(<kF*wA$c}6kwhj&h<6l!5L9U09nn?XpfF;&MIk)BE3}c`>CWRTMAU{QIO{5R+8X~{<DZMolX1G{o^W`L#<K=ApPLQ3g{`FjY%O=^MG`XPIf&pGY7@-t_a{YaM776Ah(VNChUq5JC3+Mjbkr({ecnf%D7T2SK~IpzzYj7DL?^6Zzn9L56ZO4hbxqTr8r}4jcoEGzr9f9!v{6~BZDE;TD6BcFw0n5)w6tkEI^u6rfvd7Y2S!Bq>cfg}1`dSi=fu>c9Wm$)MDc=DDZM^xT&_Tev~j`mrg6ct9xPbG{V2rM-*Ee>5$?>AZ}876;*;Cb`t~b%DRB$0hRbmaueIv(el-!zP^;=_r9vzAIs7M{H(5%`<|D?}X>u{ZGJ2PQG@@hAza-%eB8rWgKZV2_`#w_C7ytt6-8AR3)&d{!^JaY1PEQkNzT(Q#_$pUuV^03ghwx`|P$~jXIaK~QxFDk(zFqh?M6GOc49E%V8@DtqX{@~5BF=QJC~T+9-biMv;mk~FhRLLI7qO5c)u_yg2+dn~QlC(TQ;otvd(Tdc6D3gOXsxL{;YvvWMK5DY=&e2xdw4Ss;-~E5ne=9R8lfoxTpuJYK-L%|K2B~Vb-`7-pt`^o5O(01K;GYlRQ!e_lkzF&#wXTxa(-R(qMgGp@tSwd0&yPhtcFY0_>y%?^P*jKBM}(3=Rq|T!a;gOIQ?+lg&i|Ga)vb;;IKlh$g9u%G+T=_?ZNkRYEObM#z-x)(>Nti5#ZVY%z^E#VnvMfn+SYMzkxSQ(Y_Q{)&Ix3iPr~hgWvxQlgL9aIwU7fL4FzNu6r4%OHxoIQdPo6OI|rfz7A-m&ZSC@O@bBj+OnM5fU(`T;d@z-yjBVl@7EYmm0<Q;j0F>2y8PqC3)5~Hetkj~zsEP=E4Q9FxePerMf?aalF3>85dWT}gf@s8p?z`x9V-!I+5Ws3rQ>qcD@T2DbV!c+<tQUZIXRN_GI4^e+mD~;f$~l085Pc#iiK<;^px5>2(ED-m>_S^q*uZ6`F{a_0d|1'),'Libraries/Compiler/expr.☾':strd('c%0=LZEq7t`a8d3zM!26TPsdzujCZzlEC#)U1BBh$%<CS*|Zj0+qd4d@U28N*Ypa6n9v-@OMpO2p(m~-DrqT|ZhlGqv7h(}edcv%cV``&rl=>3!tTz@^UU-9GP{_bqo0;%|Asw}-5q_WJUw&V^RN?zzVAh+BgaMW2F;VzppA)(9EZUFV(rA?!*7+QCnrj?-c;$x#4&*4$lgA}R%#%)=fl%wxUalcoZGi=-d{lTexo_>d(9RDTBmFDDH+>`;D;4OdfY`A2WV^@DfGjnGCaqIo2k(v9}QEZBXf#~!$(TENZ2~L)h&93K4r_N%ii&c$<mQZ6HphTIg+B~EZv~r;Gp{c$@waxOY}dqGlp_T`4!a{<Xs^`<KxJAe*Nk-2l+wUN3iV$`WTC8zMqSR<WoDS*L+-b(XnR3CqTJe1~-+!MIq+}3(9w_LV>9b`cYOgc`}Gu{E2=)7^mmxW%?uirYEm4lUY_=CW`a)OTkmg%FayxoM>&*Rr(oyDhCR+X6p<Q3SDT1C_?oHDhXp_KOkOE-Mx9&iHDQI;h2;u!+=wAjHm2$x%c#J@99Z%nn~>{a05es1&{JwbUa-2<pY;o+mEVI6l(W-Q$fT1pNxAY)Aaf`j5V((*B5Q;4;pJmlj}!p>qm?=#pL?Ygf<U>HV@5d75G7{o0aePOgA$xQFYo7FVO9Z^Yi2L&Rn4+EYd{-E4DanNbgV|n(bi;R?YUX1gmCySi<OlmT)lX*W9tCXKSyWv3l)R|CaGGRj-w6X!Vuz+8_Qey;iHv>c2C}fBRJIE9$i=TljhVTFMq!g=1U!%eBqaN>*QpTt1nc*u|t0Y846^ggb+?QNm=C*&7JMaVesV0JOwOPS8~-6Il_dYS>_FR!k*uG3#QevK;TibvbFw{rLpn?KcT$4@Jw3L5U4P^jBgUNc*Ke<&calOVD*}D4msDwe<}7!${{9P=DLcY8o`NLzkr+8x{WwulPTvYZ&^D&p&~`6=+)DnLf;VnFsVouEGs^cD&Jygf@2wmMxgmY<b-$9WQWL2PWoRlxlN0D%OnNH<0nk2dbsv?C@?C9F_%j;v!><pw9Z})RJB_LIanfF_bj2xdCW=*o#JgoC7Y=OZ18c<DDlacxXrg6d=D%k4qDhtrU2u^S{SVsw_*|+e*PVEe@7vAHitqk^lY+8%^j(i(x}3c14^mw5nkw4PN^1Wf#q-&li-B`-N#24ePf0B7JD>L+kzap&*!fmd9Qz#$sU=Y~4i-CM}S5hh7xBUna8QXEGN(zYBn5E|dS5VF*R7GeVBedXPdIgk=4s)@(%e#-g9epi9uLKani*$i}fjU!KKrGW4sb_UTZ}`6-%O=9WUA@#_-5UZGF8gqG-6bW`mzBaNlE4ECDY58tZ?KC;u8MIl7PCBaFvg0X`umWVJ`Mj{fEdYDAj#yrB(ec8w?I0_$3A?Jl;_seftA(>cECNYk>jaT-wQ&*_AT7F|*iVW~tVPmECfw9$WVbVubP9n{&(e73^ldN_lbO04C-eq{!2w_!h%GLitcd&BoI$?^CaqOyec^1b;Ac%>8Py-?(->X%FAQ=~STor9qaL`5<M+Y76Oieo7uWxsk*Sa@u8MSImV27?^l~8iPH@nNL-G?9d1ZR|Gz<FnNcO?s$mjpKGzj!ubSX0Q|G_k~$X*Cv&rhr?wpaM+%tR?EJbIE!eNmuC5Wo}a)dR|`7sjJ$cztu88U!*tfr=Az-X1@`dlYD}$#+4+mqHbq<aK~ggd0{S>#nXD!0NT_ip1gaMa!a~|+}0}LzO{H;%H$5euCY^FY1Bg}toq|l05Kvs!w=j|54a((Tj}(eO`<n=YT{}L?C0@8`sjW4W9RHPTP~8jg!Wy+zIOq=gn=P^fe^NA`<{Qg6~X{Xo%AQFf>@QZI9Qj}X2$w%fmhrcfGl}LE>Z$ujfoVfbVTQ~JQ@oSrcJhtX|%n#uuwmZ6Z%uZf{(=sMHG|&j<cy)z{^0D$6y|k8VBjCsb%XYbDCN<*Q==|=>#X}DbyQn9}HsHHD3@VY##S4b)D|&M^h8W9c|Ubs6fn8aZ9KjL^#4dQq|LZZp<iS7*$OCkd#t_)gqKJIjV;5`jHpD*LJLtfFBkJeTs4+2t~>_ZB)|8JnR6f<Rq>ReSn7mI(}e=EZPGwo;eqVp^83&X13|9-1N6?mLH(?{&2(OstgmzNm^=_v~sQ-MC9p7Uhf3cw|I^T)0a;W&mV|_Z&z1fYRozT#F}2_|GRLSuNxHe$vIQ+Aw|~6Q=7cg6^Jz6M5Hn8>BSA0U+znC?|~aX+;T`#XC^V0;69)z^S0dGW+;1Q`CkqPS9P!=ri>#B7da;y)sxVOL`{)<QM2WT)d-Age|roC!TA36pFw>55{jpgJvnGU(!>S<{DrW4z$qZQ!&NDa=Da?~6`;AITX^%m@r}G3#v)svIZXFhEL_GJwx&yG9W_mbiQH2oIX!|dQEHj$WN)b#zMt+@1bUTvYl*5%S%o$&Wsai3SPVl(c-vG52mgycLs^JINaEd3HXPOH^Jt*6xtCU@5X~~Zn@CWJuMG72_DgrXcFV6hs-aZx+(om%E!)7^p%-?=dFn&&`Sta+B;Y^kBYMjU3Mkd<eL(}zt-f&J=|09X#kFMpqM)LVs$_(Xk&w9L?$9miwfFG>%`0Kmses~C+TgB9xG&^&LtZy=FSIciE*cg)nA}SIl5l{~dMwnE*00asv}W{yWsXBk8BMb|C>n9m2r)+U<e20~Y1R<Z9r`J293&I$d?%wf;N^v+XY6LmQHtg={QCkMvViv9mGls@2PcA3+Ok{Spxb#LwP?M9oQXA)C@Qm^uI0R8lwcjEF467$M&Xh5vn6W}k^Aiu`>_)>h?J*T8!?qRM5{>~W3qIz2RDL}RIrO<BOo}%z=v}n@9hd%%tA`Z7|l(GIjS^8j+V$2oa}*YwLx}U#qr-isD^nQZ(Had#5I$4TL4?dwQ*hOTaR+qCFvb`y{WF)q0gpH%s8^<_za6;W7~Ln@cjDfcaEw;9>w(t`4waEagP'),'Libraries/Compiler/tree_txt.☾':strd('c$|$?-)j>=5Pr{Jv2VLq&(O1Pfe2|5YA|g|e}IsN<I>wSN3WM~x4{STp=l{ntU`Z?SQU%Zij|^NM8rPLf8t-_?B3p8Q(N>Nl4a)GnQvykSq7W1Jv)Do*|t2@re_;-3%1Ru2sx)FS@C;q$B&p{5=ssHjd7()WvbqoEY;`ja=lub!5b>j{i;N!m+-92jafW5Z(FTg&gC5v@`s@(xE+bm_5zm&Lf$@rUHD}bas)rGLuj9ppeKkIki?niu~&W}7lSZ!DLYGwVcCs*zd7DA$%w&fkz2%)>=^6&q);RY`Edi$(hf)P0=`^vS*@g^O0~`~09sVyPA?>Q;~Bgfp}WFG#Hg%NM1!`yG7u3pvJx`7z8CO_#SxG|USOJLD<+86m#}^<$?pI1OE`My9l{yxDVjsrgXcQ_C0dGFO@`KtbQ7^>o?(o@x_PJH=Yh+Ts2zg+EEY+Pa6jTYSu^szWiB!2@RUtADh$@)6fR5>=PpXd<;6M1EED-ZdaPI;z`6RrfDMz(^a5@e@!d_>hqthg&UJVVUyG{UKTtZFg-Lv8t?fEGdm$-Vi;0pYK{1VvbpSgmmS*xEw&AA^WT<W`AsCuMYqWl?o|^IZOw(Z|JAgK-5~qkEvOZ&7+^nTQ?N-EvBSe_4(wzj2XY0~={PLJ5aLg0&n6K`HS~kaZ?Y7@rUX89U8H<Dy3N`4YV;WG%G%VyeQNwG35+`s|hmxuCwf$AQ%N>_$aWL3|W2MX?9K#2;IQ76T&s9qcRmSKfmCN-GKEtkrG-Z3}7>(PDF8ce)M+vzeNYmMt3-Q8zV=_P5%WBQXVr8+i)|{2h4f}<x)J9>76B%4pubwqCYd|8IO?U&};Y2GzZh&zUG)2gF<*q9G5O$edK2@8N5rYjRa2mg&T30)8q+6DDyCcFrQ{9fTTCbT3Dupc<Wl7mkG3Y`#;6{#he3TIn@O^c}8osX4KV~fPH<TsxOK}LFVqS{=AFH}%P5'),'Libraries/Compiler/tree.☾':strd('c$|e)&5P4O6u<Yc7*Cm5Vrjd#Vh+{T53Jkb?yZEOyP0YrCLxnTb9508yP&wMu!;za?A3#!2N6BIf6O<N%p|Q_9B6s-=6(Kt?}fq(IGOI>r<^P4!K3Nq@d4-5iIYI^yhw#~T=FDJ4(E}i%q5P)@V~Sk42So|liP#wKEE>_4ffDahkH0umevVnt)5I#p55&FtyUlwO7{-V;1>@if12c6=F7!`8ZG*~ge#Zqz$LtaQ`T=0JR!P0hYR>Y%U8U7g!k2>F~Apc!?W?*dHt+TCh}z#Yn6!p33v(T@NGR{oa8#Ft&ROBpiQh@!&rOQJ`MX)Byfx+e5bmSuQZxJI}GMZ`327V+i=paH9oAaj%gIM8Vizw9Arz;qQN{D+!&F*M@%9W;x&Bg6O*{IsZ+NXVH_Cq)wYsWt_j8Ptdk7C@#PHuH26jHqCsm78gf_6I{vkQEs~6cE-6t}E?01&5*ITWg-3#RU9y+Ng83UW@fl9wXAKd#<&ltJEZPLb$g|LAWgXi`r(#Y+t2@oJf~QG}KiOz9&5~8&sghiDIr8q}Mu@65J#tMVEaS)UR!yY7w$al`9ffG=R4r^>IrgX1kWlL8OVYK9A#<5Tg2F&Zolk8erBT(c-qj96w3RyB&~|;ZyTj3#cA3%`z9N%tlO~JedbyTgVLk__RDIPqx)ZfUJFS>3G3zlOrz&gcdzN8zl_H<#d1gO5JrfS)ZbR-g8`;H1c5NeSMUk1U(}r{V3O?9*Q+r`e*ErX9taS|%e*w5_74Q'),'Libraries/Compiler/node_types.☾':strd('c$}?R-A)@v6u##v=5A+GmqMf}l_g&gpiNaLMoEw&5wu$DHL>cyu9wzQRVh#sXbKTwftm=EI4(2@6sc8JrBM<tj?|mJ1uxJ%LeKoI*X!AhMT?Zo?#?;ieCM2RXU@9l)+(g9P|bU_TDd_=m3qzfNZ!uhafT=?!-J_CSEyyNtIw}a<*whfENax9`T4SQ@uPXyu2|gBNRjz+ZO$$?sF@;$VdDSXJ2yp5bLPX**?2V1X?j+%=2mR)zrfV$mS@kE9UX?S9h;c=EStMLmc3z(XD7$5p%(}HVv<<~PMS4~r6x&d*yAlYf@Ny_^XE3MWBk2=@Iyldr$}H4et{?S0<_@~{Fow*jB&e)HVvnqF$i9u!3o^Ye2Qy0DRMy=Zky>Lf`1h5!vR}@;^Ph2g|}$F0k73aN<|4k9P}sLs)Ms^Jd)#c(;WWBEqM;(OVRu#yr7B?EW#e_Qlw*=<b&YWME;Bby05`&PGh)OUTEAAkJ+*uK+t4=uH!AZRrz>kgjJ*s>+maQU$!fA1)In$q{-#nE!yzx{FkoEjLBA%E}Zv6c+7LV1P5?P=W5Lqktq1+1^8(;Zo@q)ZilB*gy%4d6QO{$+J;Sdo$8X|OKeeDDMk%17h#>kiAiZevfxWe=g?xjfIOj#(1PD+gk#+<<ORbuIwKy=qCkj&js?6p+q!G8yfaalw3`YcHolk$NUB@t;JH|>!>q(TLu5|e;4z#?S#lANm{<-rhf_Q7ATl*NtCT%4nWdv9dlFht#?wp_UX$Oc@oxW7#|Rc~GH<<+)u=o99?O8C4@YqfeW_a?4$sB3TUJS>X#}<IQth+46|xG^JdUTi@&C}fJv}lqQoQ7R{K-H(&(?PavI}4@=>zM;2lli-Fg3LknYyTtxsAF#4ZU@omXC54h4tn5M2*ytyR4z!USDo|J<3W%fVW6NsLhAAP@9Bm_e1d<RTnA|c}j<$CG1g*<5yqXZoj9jw0<Md)X9fEvD_N%)>G0KZivgSPGN;!3>R-XzIf+*z5C>Y@9$tbL&JxI8m{Q2xECLdA1}qVL8a*9wl2!~RE{0(nWTt%m3j|P3Gz%i^Klbi^=Kp2k5j9UBhJ;_1XIK@yy3NN!D5DS9G|{U>1YZWfBPLjgj?_jKT6)f_v%o_;y0xrR^;NVriR&}oK#^RB!<`UTwQoA>3lp;j+~}8M|%+_3iN3r7<MKV9a<FSK#uL?@;Po*hvrAP4VEq2)2B;Gsc%C{M62ZOvJNeFTT4VcTWxVL?S7-tU9^4TqLVvKNOQphz5|-!u0+y(5}~V-v6V=dJ=X=_C*Oh4P{vxcUFrR7pz@xr-c6#U0^N&LyA=nTctSPGr9Ar#xe%?DzJk!x3nAB?HnxhQ;YR~fYLIKSsuMK+;bViUt{9ta*GrM$u2v7-u%2I)m+iV{x34F5wGb#o8Q@n73&9MQ6qQh6MZPSe>EViGJ?&9=FI>W*WvaH;NE_k|RBiAO|Maj5PTrEl-m~kz+uwTGe>C@CY)3KVH&+;Bdr99JD0y`vWj=^`B@Pqi_tz$8Rk!hjxuFx{;|P4`ec{i$b#>@yQvCvsgH$)gISW0F$8o3=i3d3efsD@f6fAmJ#xzj1_p`hQoBZSb?4@s&nJSuMA?a_GOJ3wFB$;p+&lPxGzQOq#!}s0(PpkOvhx4(HSN<-~WPC_T-mzh&h?C(?OIVeiz=drVCN*g;lbf<`j$O`9&J5O^EW<v&*efyZ$%#436DfY}2)_f*BOCiOj42)bd?5CgCP#e)_e|X{38InLxCjDzm%j6ab~CDhV!sd^#XzmG?3}`@pbv`;Ef%`1g_fe)I5l`M=UzhW$H{q!J;YRMrBhSB3-{&xx*V6)$Qy2cC{g3ubT(@Qug|8O;$cl?$HphG<gyc!*U{o%9K&HS'),'Libraries/peggle2/gram_tools.☾':strd('c%0Q4ZExJR`MZAwTfh)?Ru6a1wgN_OMb~6#uyrvK2N>YEg6_;a3(-jjNnX!gH#Cmp3{BG}X%aYV+SDnUwQ!K`B{iC$Sw9f_v=93Y^)K1;P^3u7C&!NMy$FVne8}g8&l?|-l&|pjrcb|4T^Cy?-k3glYQ}Y`^^XgdLwZ5f_JV}k4zVm7{)^csr>SkvzSNu>qgB{_&ky&5ANPiCFABO|8b|vgl(J#!cB8oOrMn`t&OhLf$W)8a!0Wf?Ju-Ai4WQTfWoTrrn^WYClgE(dP5u>s3RKql8b9CS%kXpCru-tmPDkO{Vk&@a+ZMd8@-NH0_P}CdNc=A0=K-{d{19jp79<RTcld2O1da@muJK#crZcUXc#&x)^&U&9#XvE?{hf{K7z)8c!S*`;u5SvbfKwzBoGO5ANTFbklz_ZL1ow+dE`?){jm@(z4nE`?CK?*xjy*L-;LG7Chn9*ORB)QXUSKQck_vt?OBdrXXP=|3@K5-+{E|jQ6>2mINA_83wlSx9F7q4wTREi;YPAN|Gg#(ss-ShIoDhJBuX{lLQ-1NaS7&k#^}%cs_#H-n6@|cV(w@VAfReD(OVc=`{)^*uQjvjn(`Yx8%O5-bOL_!+{>a?eC{eX(9{eAf1_Jnhz&4W(LGv8CZ6FOCmTgEBEA_A9*hhS`#NmMKhDl6_@OhRjk%3(@MyB7cA1A4s`135u^AY;zM^l-pH)+;YrbcB_8VD}Af-!gj9G9TrHiqh(HbT^D0^%pao(JbUv=)pG<yt(-jSkm`*7oT`ds}#(Lr2F;O$YKQ4IQ2)*7+6w=)aTcwkgn5A1maXtNeZbolZENXs~o>Dv7#Xpz8v&Tm0*yW^VDPa!s&gurTp8a-Erhz6aOPbHMJ6IWi$RIixVs)FTJ6bf^nS$CO`7UsOORU-|A-_L%>Df2zZ|4`rUpmv29(ZUr$@tI(G6JVcfHU83h?Wm-O#qck<j<Y-DqOiGhQN=FKm{)4vDme`FAV}?fscMv6h>PKNxHs9BIPQc#XLV2vVBgFUu604}+A!hU1y<y8u$|0|vIaS1Svft}dvJcv7qQ(SJXh48%8~4la`4bxWA#8<GC>Z{nzsH~0Dk~=_Sp#Zp?1>b&%D>PlMyo1}!XWB+0ZDSuTMK?5?RIxInKS%GbipT%l2W*8dIjf9%<Pq$6PJeDa8lfc4J$+41pbrLL`(Z{HbG;vaIw!~FJ)9oB=(3T-z|%xfIkki1q@N}pSH^Bq&R)gp_MpgRgjkos&j}B%*)f7I1L3mh(IvEcFeqU1;xERIz;djKJj)j8kWIzZ_uK*XyM^(=qGNn5XEW5$<SD(7bnaOSV&$dXx$G7iz&kKr1_Q?hpyk<iKGalWr*Wd^ANmZ(=bYjlExI)nnun9IP}s5f*ky?N5+$*<B3Ja2^}S)Qz4-`rgr@xaMcudAqrUHw!Osflw(Tfbs^hsx5ekHZTW{;{@GUE!oX*{t#GBt7&}<#qS%727tRwwM*@o#@Sek@hD0lhUSxAvb?**)M72dbJM0g=*z3E=V%%f#lCd`k^j5Yi5&f4S*-z~u`({X{NuJ?FT0#>kuT;@~B0vnco+;(V9h6hZ5FNY1@UkAw-54S*0v|qL_cZi@vI<Aa{8Pq;@SpMl|GC^W_fk>RD8D?Ia;3s(R5RaywS1|vTE4W;B^<<Q8o#Wz5aA+hC|W=W7jd*jf~p*ot)ZftK)ansDFn6pAR1^nB<gNUjlH{!Y6Pfiki#LdZ0+|7;sBhkn0Knv+G04*Vi%KJIZL5#?+Ia-`5z(LWr2ygBQE5ot{=`nd-pnp%FFJcf9}EYz=&96RQCo026Skw!%!5qbRxF*$@;{eSc}sR-ehg^d(@O66C&pw_eXHP$#3PHNv%fsLtHutP%r_VFb)@BJ3JH6reot}yi?d|MD_oaUl2*@9@b4_G#(TxCUo?_f%`e6FRuAz>2#iN81DytJ3E)G@@u-B5}0z}GAwpk4?VDH>||x(eOh>wk<c6HdiwcdDSx-P!N1}wIiaCE`@BzQm%y%|U27Z-vLs!9z<RxaP38rcTz)%Q9Eg{Vb)dJ=lFO#n*|41Giyxp7(jvd#diU}8=`+*g6I<^-c{Wbl!1>v(aPXN6a47xPg`^YvgA_Wzd+QHh0yP_ckXrqnvu8sfX4iHiXE`K)rvZ^$!u!7A>y&SRen21v`3xbbv$&N#v*n?Bng5xu7v7Vmq~=hEV8@vCqu($$jlE<63YIJm>fIDos#aj-<{VMhLqeiyOLg%gFLg+#H7j3)tg~ktjYhZea+BpP&zddF$J;&9YT<r8hmTXTzK4b9&LRpxP{RrNTs3Hwcf4)KE}@W`xPbd>IU-AUS?au9CLr}kW!PWV@hOOJTVmUKPVt*%@i7Fj;4S6{Gbv}14OMhtv;Z7_<PCsB!lZ?1Lk5Zrr&6FOZ*9lkxt)CzXTVIk)@J)h7!+IgFThL@Ae6rH!q)wjal3BU5LTFo1BKYZK+kfLbXB>+(fMgYx~#n0knV{R8Lp|5EoNDCOYMb1w~zQ=fReN|C?`y8yO3$dvX|mlj~#Q5{~BM5PrEKP-iKkQ&t_U02ch_AVaZnw(HAeqmb^56q+lS3rJN>%iI+}G-sEg(*aHQ7pkQnKb_T<z-W;~3U~7uU6~*_8<U8`>3#N>OZ^J0h%x09Y#4KmqEt!}nbF(G4u6Q7z+KFL6cQi(p<1NR`___8oAD0HmI$}&6`(Z>i1-x*b0E30Tm{ED`gV~j1D(q4Q=X4=w8b#<OGV%5>=Nd8jVpX2UEyj#0BVSsC;wXfr*u3x;18w$Aop0tuoQ_0qSMG>NY&1*nuvn@zqlhXdRAi8=AE&UhK3-rz8Z$*pq#@)}u|K|8erhsn0|<ye@w?PYqCWd!^Ue?7T!+7ZuA`LAhS%+~y!GR}^^@(RFSD)X<#Xz4C8;{NuI~1%Q+P9y2j!j;7BW$NS{0J=5d9&(w5sg}M*j_SYwZI'),'Libraries/Ń.☾':strd('c$~c&ZExGg`MZC`?L)w$%LtO~G?)MZGn@<?wkC$_0s|aDQ0SAxjTSYMPURH^Vx?||bXyw73A&|ioO#K*t;mKJ8-^k2J{<N({7d#ccSrK>NJ)<E)&^{f_uTXTdMC<1;CGkb{t@kT@ae~IEni((?R2P<vSHfkMe$}gbv&{WM%TMxLS2tIjthUqwyVq3b=S@}+B3a4+9ZAyhRjccsGpEva}dQTS!ci8Vx*f8{*-^rzvAD(|NDGrX2uV@3B29qd(9aFKR`bTqcrJsNV7$NJP>t!{KJ6WjDT5ZJ<{m}{U8Mffq{p7kH7Rt>XBLBBdo<o{ByqRN`wMwCR_%bF%GYQg7&Ejz@G-dbN~u$tj+pu67+~qSeP)f*7nF-S1(cE>pp+vp$<ObJFP2GpSjdUKt=*kf?!*2VW?Z0u(X?|v1I=zm+6}s9eBQ=J=fi}dK*65@CzEuyb0f^f}hi18YcW)JG1ts%Ri+T!Q2<ynZf+1pLT<OX0x!nd40W03d0PWWJrR3{-(xIX1)Vj_!k{|`1C3Ny(=X*A$_p9q7t(~Tuq@#od4aX=aQrS(YeGudh!K4KKYA7&XL?)wUk6LagKhy>v%dJ+RG9DH-DkI6Z)L%7W6?`LCQAA3h9yUX4%s~g2Fe3+Vi&5KcYN_{x#jtgYM_s1z+9%`UJ&m3TU;+u$C4ZL)IUsPkzYn^8e^U6x)E~v39^UYnK+W8<_?*EeBed#w^{6b>puEZGHbb3n%V}^>Ld)(|V>5vF8zA{bw>33rygiDTZV}N(n9%E3cPM($@;Il96?O{1ftHWH0~h_+cmH$4Hj!jQFuUN4ly%5KihxgYD|@D7%47!Obi;<^1b;B=Zg2BU2U@9?k1>YZVZvcfkHJ{|$dxK(ZS0Hnsp{A?FWb!GAnWl9TWaJN|1#x>rI{6NIG%ChJi3wM<^HgXLVM^Bjww3I^S{2*=~rX|oKE0N}RCc9GR*X9@q(JzL+>#mgyaGWFtt4)P&?=8@PVgP65`2pto+7X(XZwY3^=S(zrztYSuyqN{8jYpGn2(g-Nju8vf^vBMJfRQnIEwD3<;gtTVnRRZ-ztW({T8YN)Bq$8=@HN-W6Gzp7}A-&0<WqMI{nxSS>N!K!P>~X9$S2R|*<B?Q`-9yQx=hjlgXnz_mz8TL9pso#~LCAWkU;sZu8_oLb>f`fTcQAmD2q767gq6&&VVMzl-L;|Trt$agjUZ%-m$D`365<<#R5NY%!-jOtColnEQtOi?k=|;4yA0V4>5};tcP)vAPDouQi~xZrF|+>GCX2f%11x1o-Lud`{4p^2gAHlW-(r;jxuur0d=hBSG2lL3b5<3{C-HK8+nh15VX6UT-s69t6j>z#)w(LPHqJoXrh%s5os`FQO)EjR&r;o*T$NcPTeEbiCGynB<h>-z=9Q@&O6aV>^@W+#MXo(YUYAL?NbN}6AgPFHbPO^d@Xugwxg+<;Im*iVy#!+$2J>IBKDNQVL<@3DQ+ef(Szj*$hKGt0l$8-2@8oy^sI`7TV@d8d;lZJ%37XpkCWoX{UB}f^ks_Y*2mEVM@!V2%%K8<7rBZ3qiN}`9v}Ku1NS|8CQ%3LU(1McEvbpqptecKfT9g2f2xrAgAXBz(MRjJQTu20?>>(tCfktQ;3s2Ds_^viv^@9F-$v7A+GCuTJS*aMbR;t5<uAq|E+U2gM<eQc8wKB0sDXFh)D8D8J6XIy1fD{H#bUhNq*ldwZd@HKnS0q}%00>Ydv;cDIo{m*LMH#&2iYY7?cGHsOM58pa<4Sf2x;dusMVFM!h4aCNynIt%4revV1IDRvMnOCqnq1|MOR9Tv!SPNoEG&IXQ)aHmc=OoFX?pHCRo+qMS{|Z}AP3$n)U%d^fzPO%b>-jl4Yys{yidv`!_#My3Ky<w*|IifSg}Dr?7^cReXTn4YS1;bSYfBJ^-w>38bpb9@?=b{c%FL;P3Aaub)KB03PT#$9`QqwQq0k%7<M&-YkmEp<wrLa4p_;i5xc(!9&eVJlWY_{8VF~efU8I$Z@}(U%}h!Im2ouZ;)HS>6G?7mv<rq~c9X>kTc<Y-v5PJa=oVHA{Tto5%0`wk%o37Lu?@^(<Fj7PuMQwFxcN27kzEh)r_$pU?V&BG<7nCD+Y$17W1^I=l|7X3@!1RC>&E?Po!Q-BE6bH5{(?VHrx@ZHHDLtnJ^n;wS9my39;<4$9aN&C1Gs8@)OiNJurs#8iT`nMAA{(?Ms!et=s+PlK!cPVUXb#{x<0Z5agugIODE-lWZc{~ZeBt+fDro~|HJq?pP4*V*#>}XIX}pSJN}?}nkR&|i1BwM;%hm3T#`IKwdAoac@mVJzI=63)Cj`_+L5Knpgdsi1!2nK@h5|LOpGPyBQ=}d=MS|W1WW0NKjY8w-`9$>iY@sG@DB!YG+=SMor?&#_5s@~Dj+{E%k_p_D3r2nOz5R%HLq14L9mUGvB&(c6mR;jZOzr|-|yAy_;8_j^x>X-Q?K{rn``gX;kn*eXeiKL-CCH-7ete}3-dRY=$G=ynbIqZl}CAtE0sri+Z9K7_&T;;&rdqx(@z34+u<>Mbr@(&Q`v>;ZL|aWaopnINw}f-3P6WZdp=QNP~qSiF>HAc%|s`qlh%RY%1#Ev9jfq#SNto{YhqNs=d9vo?7(?n_LR=K1b@W^FKk&{fo;%-Xzlg3aR&kLtpa@8wVEKsrnsTs;eX?=@*DctrIL9>4fKVeco3$#UtNpTszBL&vhqMw?lb-g&F))9@b3<lz^<4C9`ncI<oYxIPk!JL_4HJlJ%_`4k6qPnt2!dra1vO^yK;eqW;_T8(BRRn=Xj+}S#2P!EIrs_JW0F$FXDWY!Vv@fwZ5b4PV4%vM?*^G_0`hiDpezB(OlG)t1gOasbQv!u;H5;sMEV}!I3&pbc$}r%l-2hS5l_G<CQp$rdJjL$wte87<VS1s6H5TAUD)6_8jwSWbzeAk)@<hI7j=pjvoHwX#dlr{V$L9NAjBrcbDE-p|s(F;O{xT4W~(*Mx*PzZ)P5$l~??BcD*s;f8_V8uQx{gPy9}0DiXV1RHh?XI<y;nOi9_U2iDTU^!t+Bc{00;7oHtB)(~swib~+ZL2Q@Y22TVOL7yeaAnMj|e-&zb0`m_4Erp~mLt#%Wp;pB~+t}$iH>wItb55@E3i7=cX-qtKlQ;xI;eQVNV&5W7DbgfFe+lpT4DC>Qtu(LPh}JxFL4b++u>=8!5uPejN;$P;l>_^VedOTJ{E0D%78fbKL}8Vqp#1vU;-yQS%Rj@fu)Pg4yY{6u>R=Q*Dwv_fVQEVlv_$xVstC<4>hYD6-e3xzIzNx_Is2Xf`W4ouraB&k3ehBMa~@e}!-wSEu87t!iZ(D@$A1INbu;{IW5dy&=Nx@yek$pPM}Yb~GBAap>p~#>A0d98G5'),'Libraries/peggle2/main.☾':strd('c%0=t{cjt`mA~t+*t#%wmtqJ>j+3i!JYOn1>EY@R$Vz<x#VlxQB{3#<+2zWjFR{^l*bVaOB({?#j%%X`>?TIiG-&Ds&K1bw@?YE!)n9V&V`g?{cSupTY+rF~Bk%6KdGo&J&6}Aw<7KaAuOB=93oi)p>E8|?JG!_O1fKifueeobts9?gbqAhbbzIknzXW~snCJVA$7Y*T-l*DXI81}pIO(<0`$5xgwb#Q55TwbO`6&l}onAjqQYQ)5!lBa|z{6BHY=`~S$!=tCWgp?U>>@nhEx-$4Z?GP32GnejwoZ0KXTI)u-B$19N{dmv35~y;y_>x~?__Uef5=|;;Pw6N9gn{PZ34Pebx!9nuV$CB>)E>ub;a|&)4o%wIN9fUg<;h>Gmpq`X218`y@TrB!E(y~xz1k41B3v=L^Os?fcEJJ;=2Jn-O@=N0;2QTdmdB>>xYjX6zx*=53`r*N8%{-fr_R2QnC?hSl$W{4HZvKt%R#s;hpR&Z&1%(f|`HuS#GQlM^s@^uF6-ZGaw8Mia*KJ@wAnsooLNTJH0S*eFdO54i9f;cRd90bBH8NH<D;d$F_Iiq;Y)8**jnX4XQ?6=P^l;Kx5(XUqyvgQn^nYuO+Qs(2k?iVUnWaE@$s$cLm>G)ar#n682jC0nsYeNpPQLAEKZ?&OY<pu-gmb<&C+SnV;cfiyvEqL1!%r+TDoX*OGXnA9SK9OtcR!+WFRNx3*rpxpm<p{(bGH>q{<{mJFj51kO8()>>M1DxP|6%rxPPPYO~HPQC89f4_9mb;9l-)ar({#0q<^2+3%j3fRTpvhVWGgKnoCdb3p)F_`Jnl5ax@oC%Z#3|vF88xGp7zR?fCsMEUpKi|3Y&ajq*{cZ~yoO3FG^Ww+gEmB{76<>tys?TYaVX+Zv1@)eUD;w=Fc)qA}HXY%iR9V#l3BQy5o~!^1|NW3R<AYGJBrbfNrLO>fy-+ZR1r=|h@R?<}k7Xz&DgEBTL%;N9eMG9r1L-d0#EL%hZFa$X8oXxc>u|9W|6g6R3imMf8!lQLGzSdQ-|PIGV+y-Et}ic)$8`&FnRu_uFVp2R(WXxv<HLw%uYA43X6d;yra{5xcy6zJe=p6JIUh#|k-}wH-*^3yf<Hfj61Np|kzLbxR0lcPTCw#Fvuk%EN4mgv-0Ou=%8qT5|2g6MR)TRD(lL5o6sJ1gR<z>4Q2M&&D14N`tj|RfvW<QztS#9-6LqfVlSjQZU$@JSNKs6;<8Bw6eHgUj?U;vF?aB}UW4(#|<hEVyZ7ob&X_|P_H_Xa1@)N!WDF*pF*}H0xhu4o_Z1Z7sQXW>+%!3Z}p>3A<5WSGj@6h+z(2DfdQYBsv!$|Ft0~RkBEx~xX&vN2~q)QKl?`&*5AV73OybTK6@6))SGbNF`#>c@mKHi)fr30ndek%bkVQlt}*c`n#eFRJfd@uOfssk@`<bcOG{b&bHf3z$2425EJ@^P+EjQy_op6I&(xbW<v2V*Uud*LhvrkAp>>EG|OS8$B`<b$p2-~5QWAlkdLR?53`Wzt7e2w}Ywqr$yPcNPNxa%q+BT%l*9pAw;iSwL*Ew9p~N+r+3zJqc^zOZuH|=uJl|GLSzsne7^gN|B_)v80!5bi;vQpKUwodEn{%+G?8gRXEpA!qv`@eb``Q6`ozA6LGYS0TBn|-ZXR`fx{i7iCY4u=u3ffl;dHwJc4>`7Ds)FMh`u4>hMJgr3TReTEK2AjWeXLGpMg2ss!EY8FW>sdFqU{)ov^Gbbr8u3-*oRc^Aq%(Tb&9#IoV9yK;QegsI|U_B>Re(+iAJ_Zm`f5cQGLQ&pu2q?sz3-IL1-u1aao(3(!7;qs{Mk=$!z82B<)I(W1^ng^-q1JY28L{i@jQdJS9YD$(unQ}j7Ax6bx?Fvb!u?z#pVKLhFO>7BTgo%%_xPc4tG9d$g(I#+YgivGa>IcBvw8JHOS1S$k($9|`n$2Em=uVqO_+{TmTGs}*Q`+;=Qr-%W5uG&bdA4z3cGMWL4?NmF_GrQzP>Vd{CC%Vm@y+b}s+#l<aOxT$Se=9NmGI=oTAhb2F*#IYM?T(ul6{lC?n&toPTw%a7tX@#j2K#I3Bl^3!O8w*QYY=voc&J--td^%oB&`3XU4Or&zvVYW#{oX|LzOzY_5az<+Xr6*=9vlQ0vEi4}6v!CNGWR<mOI>8?-yb1r(y4nhOg|g_I3|S&T`nm|(k2N!kq?X%$w`UF&3Qb|;fDvW)_jzY>1&PWFXI^U*)6Dg4XX7uoysa%qQO0VDQvU&t0$1RS?8^5qL5{69zjpO!<|+64K+3_wyiB?qr^C;Km42Fq@P&$;w6_=wfDx;wKvL(wPKMChiF|6iPcc1$Z)b9b0ot18?W!B0Ed8o;j#ZK4W*qt*SZ*xpK<CY_#;e${z$zwUQ<)#fWTs=Uo~`2_>Hp;k0XQ3&G&VNxhtB(zE`e3X4lOALZ^omKKt@M~Iv49&)XM$Jp1wP~*&dS#LlG_)ITOa4X#KNHhM{!19fE|EnuRHcz(@P{*v9w}4Gw$^K<?e*N@5-ImD>t1cpZ$+L@@q6$8mCSL5Umklk;@BCAo^zAp9qwej#5a=@=ar^4!i%deGpQfP9}gp_pE2^2y)J52Rgb6E<OB>~J{v{VTiJ&@rAnBkz$=0wMpY&ge`2@`hiM3raYMKfp=Kc((b+%qo4yst<mM7R2)`kJCzG&sYK$!#^5=g)YZ_z9oZpmcc`LiRi^gIQ66pd`NN|v`OuaR{b3V?uZR)1=C8F7`<VV_{w^tEzK;xM{Qd!*Q&RBU+!<3zuqSv}r^jZ;*$rJdjnL=oE&z^>2i+>D1!*9FeWuiytTTtQ;-?OkHcA@v{U4|B#9=aeOfN$J=&+<^6r0G~HE-o;;(=KrZU&}KD!=qR{Mq5Oz$`4Jn1leZyHKB-v@3}A8m}He49j<z{F=Jv954Y>_UG6l^sP54RW7~NuYW|*mRCy(2QV+FVj8e98(P`Vh^Do8qw^6L^#J#l*=6QX3_dBz_JMEnIM-rH|Yps4CO;PVdxH9FBa8J0wJ9f6Vy>=elO!C6$^_1DB);+CmbHezAkrn&qM6>LMs{SY@CEKcpo6oyX&g`ygORaB>(Z>#SF=ObWtcMXgn0Z(_&<*r}ZEx`&of{LnyDLRHtv}qpFJkk-VE0{Gq1S(L?Y<~|NK}6EfrUzuyCQVCYkl_tvT=0`8)5`=f6>7V7>9P}c6BXs_qmh_7Zl_1j#{sEDx~eCftRSgvJ2U#MjoTS3Gzp^gGOJW9e@^Dgt+1GO<sWDH=GwmJ-I7ErE*s~>h(p`c`ZA?@YGVCteMD-bSV2<_FJINud2Okl{G44m1uIKbcHuCwYRF0Gd}l?1RG4vFnFu-zwgaEwEa5m=*%%g@A;hh1%yp7Y2&E=f;|savBprB2}*3n%Oa6<@foG0X(=Xu6p6(uR|dYmn_W}N!yl@GW6gv&dubau;oWJ@AF!uac?eTAwr>(KXaO_!1S%?OB<7|d8v<ct?O!WQQdx?E{|5JkJNPM~A&x3mlF}CXxS@}6=@FhlsZW+K7q-n4DUotCB}il@656VevgX7HbEGFs+D`o#WK5bBf!yx@`=yJ;-5CRgOzka+ND}FnvuePcKFuz9x&uOi=pIKexuBKk{Yy}Pe{*3I^?hJc(wq`DfC}>5r67r8Jl|mCKx5}akAr>eHYk-J{Hmk6mg!bX5*nMV=M4?jloCJ`tn#PyugKo`B)bD%&hVYmWs)zzQwrCzOI7S#SF^9`#L%7WuCIB@S1nm*S19XHWSxoqYu+^VebWPN<I;o`S+c=|m^>eRJ&0FJ)d<o!NRu!W8~wt8zs=zXhq$19Jl8=dI_hFfO<EnOyV~k>!xcUSAx5SoZ0iG4h4lT#{5FjVumWEF#isd56BFzS;*;eh$n`DJ?MLmW&lkJ0+@#<7&E2inUWLDInf`n|>>eY1m38r*mBYD7In)JhoIA;bL15)+DtFSDmFb`+e<Ii#y@AT<{0(hRgo$c2Xce;VV>vQ_4T(8bQrMWF;cjA8$X|J>A<ueYEhJ48=Lj8E;xdnBs)Px@pwhBN&9w^nr4Bjam!5H?!Pn72h9;#2b{CWvEc;2m{v|OJB_OvKD!5rxnLdXD>e=yzdp<YZQE3TgHAQ`m&f<78zRf;vjjXRTrEoQENG^<5fR0KbD&S#ZRHjEuq0&GsLm^_a+@T7$m^2GUjxS&y2y@m^sQszpr&<#B;?p7L%3_e~o8lny$#J*W<G%2t>eNpr5<nOUl(q)z;h@fQbn%fpc<}3uaFBN5s8HIC<5R8mu(cw;ccON8V<imw@t~u_1Mc>zpc_VO>ALuI@X*hneWsAk_p<DroP_li3W?yvEaMf3+;2;--jDf67#ZhHvQJLGKH#2}>9Itngj#-fW@ct}X7=Rcn2Tw04YLE6rJon&+?_Q}E#WcCV8Che+n&vML8Ki+2RJ)wRmXBDA=M8h*Z|r#fLf@7EV+d+P(PVb1^+5?S8=!~X8u2+1!((?V2#I@BK+eT%svx-)&@U17%XJ#KMAAGlluBwafW~$tSyd1@WH&2GuKqsE(g&1VG(gUkquGyx3az&mVi8WQ32#`uhb8WA@Xu|-Yd_?Rln@iXXeY+Vd}PT=(Z!KmM>+WixgV&`r0`eU+ec?A*6H}-ko<kXK8Y5#+H{ceUO#|%CRm_!luRaA39OTw;m+fLF}I|M{2V6D12B!55n$2HmuU0LFl@ZVTVCMj6SWViT}MFDk>hBGP}9(G`5<?%+&5x&7)JPb)i*`&Z-;R?A&N?TPI`qkVa*-(@n#KbY0cj@psmL$1la*8y7Ye{9od%NT0=xn5I{7AY?nPW~hTc9+I$FDo;#`q46012Lf-GZ5n?IGInnJrLuM$rJYEVHnn{k+h)?*<tV!|=tP6G6~Qdxv|J~&MAi#(OXPHMVU<Xw-h@MYxuz(mQ11FSmNi@{jxOS`SXPOIZq35`=*>`7uU)KXuVa(&<Yv3D3&v?N#DZxVmUtY?3`1NC(;yvMO|g8!{Kry0Sr;wFl?df;oGX^UD2}>uyVZ5NHai&Yt>sUJ$wHc4GhE7Zc5)st4(jeSd1r#~gCvaX7L3N?5|rRVW06_j8d2(Uqr(h^Nii)<L7m%bB~iQ*4z@XDnU#-I?rhI?OxS{rf(HA%ehLlI%VTP{c2`E62M}iK0HMKAm&59Rte86QE|U%_(klpqws@J6-!S~lGhAwnc<`x}B=P3p9s@Lkb_j@x{4m<+g-I(7N4c8O!=rTw)Q6zb-h$QIjIg~e4-)FLvQehhF)Gg9Z=%}nZKrCg8f^eJeVSuUm^uuQPn)zT-+KCNyGao(7(?yt=f<6=zmXO}wOK~BaQMpFp~rMkYlj}wK~0~!AB4W&+}%~j>5XN0^x(Q_n=_rES|u+pHp|<JDh&dyc*8;rC$Bz|`xWp37Yz0FEI`~e7Nr<fu5asgKmBlRtsBk-Ft~TU#VU2QFiNX*B((1KTAj!>mWQgedL@>PDivB9x>Y&?YM|jkt!*9Al1YcN9QR_4x1OrbVj~f`ocM0XzrnXyP1eLtmb@(8OgqBL$7tIi0HPGhkcVaop>OuTV+ih!L987fHg{qezubqJkrFqsFYt9vJH>C>vx)Kuly#ytwJCz)I&W+ov9VvCx2|@!rA^V_+>khx;oW=_S=zFonVO;X1;nb-9XK%K4K67PY_YDjh*m4=PffMEt-(MVzcAh)7<A)w5CkIHqZ9Cyx4}o>7hQezA_zKBCk+CRH$<z>n%F1(O5aWsu2k&SuZgY2-xas&*RaW_7mpqeo>_eAu(#&hrYOAWthr61&G4=zkVRway;c)95v<h~n<iaC6!HoZ_@bq)tZ^>e!}hqEtdp>xC|Q^Nr@MF1*gJ3*nY+Dsnmg&Wx}E<FSDJhpSme!c{aO&vWf6fsus}ggoxC@`N{3^rA6*=H$AM-7!!l*LcNW-n6mg<eUavafgYo{oI9ly?+NrS|ZyM5i)hUUBjAb1SX<hJ<+mJ*lEc-Ham%K+Q(rTx|GsHa?t@FEPi(*3&LjljEmDbGU3!p%kL(h2K9U=dTJeVz^s+RN#Lrb2pNrOgk5bFg!0416j)lRfAW=U^kN|QiJH;2)o^2LoPLfVfJ4bGgi*-6)(bUlPI7dcma%@<PAOu6=xPQ-T!3`*P@L$5To5(Bz}L<Y1gd~)37jv;Sev}hT_&VgUJc+tyG)6bKdFu<rvahx&op}65lb+OT{i@PBU-Du>UkLt3=VO6^;05d(#D9<Tw0uWa=nyFn4x3Rnto}7E)r_IK5%TW`r7;_t2U!LFk^1{}YueYvzzjfiSP5ijWYdp7S>*B}F7vWFMuk3-3dtCVFY9HM_w2k^LeBS!acUl3w5$5L#sPjE7&p&|MUte6S&C?Y`TUS4ruGD|H&DR>9`zezNxR>2M&T_gOA@=DPF{=p?=ZF{!;W+ohZKAzVnLa=dUIVH&Uu-PH59=>S{<QiI>=#OCOI2Pagz|&2=E%XrPX&w5{_@aqV~OJh7vfGZ6A0l3?!40wx2AdS0r=Z+gA*<d2y};AUdVU9L9w{{3|nmQMLMylpw(|;x{kahjT$-Uifz!#xG@WbTr+Q9AZsDwV&etM#6BP0#8oQJ@h}nmQflXUTRW1;?b^LrYL}!T-Z!yny`h|t=LI1`mN_L1?2=>x9Wp1G2`-SNiFLN51w(J;wj@<%OT5L+jj77oZ9`4{L%SP^4}7~PKjQ`+Kk+R+LK@<7DdJH>XtXXWj23=<w8~=xHIlY7)bpcJKhLO{NxjdAs-C^7b_XgqEWmx&SLj4BBCQA`)XX$?b;~*-Z3!eiTkKYIO;IveEZHYZ_7zJWmnEiM5_+Y}x%_b-%Yj8%z_p)>g!$y?a)z|-fe+J0p@!&*W|?PQyqm&wg+1Atnzl83LNu&3^<>l9bxTcc7McAgV)jJw^Us>iv*>+)e)Q<l@ukJ5j?tV;ggS;xmgyoZ8@+x25au{5qX;ae%ade!w>H*`RfFI0NNxfw>V-y_uvl9QQ)t+i1a#xpiX`B}?6+#RPvB;9xnM+1C@|CxH-n&*{il-yIH3ZzB4+d2t#syee$jf%;L4;|4DRA&O5;F^T4v7c!d|S}(m7Xr&wuo*Sj6Cz*Qezm6d^ARA?KH~^L1%<MD^wD)w(nTv|cq?HPx?OwU#SbJt>pN08bAwfKL71X+NKj!V|An`BQv7`cnrF28aFwuSh=*QNMOIy61{IZeCm1ZyFBLKz1={y^?r$IdTd=T=l|#>rNhsojBllKx=Zw_~uv2wHXR)d*wp>{df!1-o`DWdX8%uqCVHzOjaEITXWg<jRx%)y?(2cjBb!XP9_`c^Dv_WFbF51Asw-|dBA}H)>(Gz(Bc>@r(4~P5L-e@!KFIj@%?F&M#p#jiete7unx=h9E84mAOvqt?}1>t42jrt$i`#K%bU$<JEZtmKsw7165An9lp&WPO11;bg{_67N0ts9SsGy|4WY-`riIzK7qYnViR5MnieXln0AyXgi~w$|Y_vAlS30fDPIFj4Gp<Qn$s{CT=Hrzc*h;J487&nYo=7CLJ}f?B4;J14=X2VSc34mTR_lxiFXdZx5M^OyRqhoW^ZyrWI%7Q'),'Libraries/peggle2/rgx_golfatron.☾':strd('c$~dgTZ`L96n@vQm_R@?yV_;7hC&T)vTLtd)1-2|E);ClIJUfYYfFpdfK1Z|FG-=fkZiXNp`}f>`&3BtP)I2u(1-bBJ!fWgjY_<PRv=rN%Q@eC=R0RKl;7d^ng{!|*TbjA^`_No_j*(x^ao={H^|}CyV;)xlo>?V8T^U~R+BQ;*)VNw<a;wRy5$b$o;MB1WOn5Fb0TJIG%`;0uG{T?etGlum9=%sI`&szgK53nwKs%KN(W<;lq=Hs$9r^(b+&Bm7>u`b?WP@}sO?>&Cc_qu9<*_oX_}=EOCK<eR_pjqX;rlIV}8P)P)7NEe$J06yr1$%lrQ0JDSWRJ@FWZ$^B?#NTK%*|r~TQ@VINyw@>4_pe^(}*xZw`}ng7XuN9XIRn*lnw$l98+!~je~foc37V8F^f{u&5iVCP-PEQQQk4cU8QY6wgh0vIU>Fg)ddWIdM2b*rYZg0nLiv8?cyj7I*|=+GdGasnm<C$v*-8>9iZ)wZPql~VEoY~-6w(QM_Lw+m(Y-@&f~e7LQ81ixMkKi{n2=bH=R7o(0B1>scX09P2{YqUE_+{F|Y+s1*A^?DTZQ)myI`DE_QXar_E8Vk>6>Uk>-umk{0HpB7|tGI~G7YsUcOez2ilvi!%U?1mJQ=oOINp?zlG}GCEP9r<s)|m>z?zO@o?6y{_VZ{#V+YVXmuvzS|`92P>yzTII?C?hM0(Vw&s12PF@ejkE-**ELa#<sA#W2FGoWAGJ`3X&If*%O$kNj6rvZ9cdiRTY#h(PdyL17k33I^0v5V~~g<EReA8Q(^puLMaZt`yP|e7%l^q+ilm3|Pz`3olFlH<Yrt-U)b&#iRVq{?U=+4yDc}BQge@puI7$A^x^)QW16c7k;<8)21au48h7+BF;2$6fERZSoNLxE#D>l8=%I|2|GkplQlvYxHFSW6%yhDW1Dj%eA=Hokey7^uJXtH0e?eBVw+}hSPs4Es6Y2T7l}UM=dfPk^s3y>@ezkY=Ns4oGIT_76WpQopOPdz;}7{0q)#YlUZ^1ch`(AzLNT+7hj^n>8<%h`tR>_CGeRCYx@c%bOQE6&2%x`F71Tx6Kro#Q9BLZm6VG+zR%H+qV=AiTISOZ=^xYvw>?wam_n8bJC{RnNd(6MRIB{ttQ^y4Z7+h2G85Ht4y9k*vh*>%Vm9|s)m!Obq-u%Lw0GgD%thP$R*(ynh7Z9kHkTMyt6h(N=qC^U^&IJGRdm><%N~R<o3h{bUX#&ir-4@HMXO;@gUH(^bU_!w%DC*h23HN#777HC`t8B8dLs5~?4@;9H?4zs_PpF|NI?!ea@GMW6tWZ#yC8anrRhbg&&!lK2iDDG_h?rShi9OtLpm4$6Y~{?wjQQC*u2zrJkQaYdWvC$eF!6@MdM2?VXc1;#Z6KmrsT9V1R+${YQN$UlZi9U3EGmhF>4sV}1~?R(N2bD}Amn%3xyVRiq7FwPCsR=2Gd5jbGjCR%Y4TjPQ>*p%KEt!s0UWMUXDX^^3NM_BGVhH214M)F)&'),'Libraries/Compiler/op_table.☾':strd('c$~FZTW=Fb6n^)wm_DGHrLJWs6hb6F<c1pIB-T1mRl!>MvWX&miR?`kq&`3jfs|4LBms#e5N@IrqEZ4vT%}B(!*9qw_KBa+b9QEDXB~%_n<d+4XU_S~WzLy1vy7kSzoj!jFv~)!e;_?%4qFzZjy>gAqt#kD=g=q_D^>HkQk@x5La712p4d>D8OF$WiEM=J1T$t=>{`yTt?C5+S8Mf_&{p{(eBXHg_ef`wjO-n=9R*@JxqQiH)rmR?kML=Joj+hSc5JdO9zVFX{(>6WtPx?kV$sUm;Dn73tduL~i#ak8C6!JRRuLPo)a{zX28Mdkm3h9x=fSK~e2G6!!oUK5&R-b~c14Lq1OwLil}`Mh=g$PlDX{5!6xCegr;@B*8ZX#vuv)RB1b@NqxB-BkBs@%D7%GNgM5GA|{7?Q`$p@YojDABkr`@@eJzc}f^R4wYaK06kt@R5HIKy2%K2ED3?)@hXAYJVW<JggSJU$wa?<=&5hT_zV`!)U#Yl!ZMARuSZzAW<3&I=s}?D#=N<rI~7XBX6it*C;cinOJGgPuk&+dj|Bwh-Q<rO!Znv=qi#)^p(#;FcR*P3&ZxD2KaxnZnAw<u6djGJnQbFuzan3;4Id&j37ukATB`^J%b^_}GayIq0!g^t43Uy|J>pP*{t5W0`0%d85w(bTbtoqDus7FbE;xKot<~!!wc&tLaJzPw-#yuB`g>u3jMf%v^KmHVLiCx_4(4tsC5wcjod(nepgmb2Hi{bi2-b>x0nL+xO=o7f-VhN@!LV{%za}>9GpM#^B{46e$}R#{8m#=}dR2w)yzo^ycf$mz(p{h(rpdT)j@9eR$%}7@y<6^H-R3m-r&|6vOC@ph9R)HG86FS$a2s+`YtCItkrV-&3b#4`E^?=6L2U^QU|jp`P<Ke`Ww7K`&w!?NMS`<CSp-x}BJhlD!^r9tc4#NCWUwpM)O9jF=MI&a8N)zPjyz8YY9I>xG^;?$~8b^^~THO`)Sl`_gR62tdb2F{+FF37d+NfnkjwKQ-H#tX0TVm`yoO>{8wK8d#)3BJe9PYAR%GeY>$ya^lO_tIi(++CNgj03D#(6WEq>oSI-i+{Y6B9MI5@HO{76rMHh=Lz7O3NO%Lk8Z5xTC4irLgQ9j#QCnE4c<Aj*v3+p<*_YipvOxsB$oWYvb&0&zxD>-!m|-knh~Ux`@))*1_){5MXa&S8o&_>qAz})$lkkVyTB(40jC#P$PYbw+Z77nvH+cFbVvYVDM^{_W*DL~FfJTmI^&q5Z*tL27H*03AZeL<2Tie0b_U*RrcD8BNR`V;_+NhO6f22EW{>)UFxeN{Gi{!(0yJzOUp50%_Xt`MklSN&ZbI0-CB`-^jcbD+tEegAU-zH_n<8iLBlLq?(O09VN!!$q1&o;mt&2w)tv^6(B=F2<LNIWYW@H2j1HDEC%E>j74lgeT@X5olSWu6bs0@ntCYs+r85#=uM`yX|M6K)~+wsQv<!aVWmuqEJ}GIF(HDv{L<O&B<$48_pH!K5rVW>6e%hitT3EqZ`5)r33R9=@g->RA>mR3}at*wg6dV~W6K)!W2QV1!kK)^k-`Pe-HSH0C71(t%_-N>WLw5v>dK`NpBCiwyW^cLr)9tUXH1mZj6%q-AAcyZhvAtjU(3C$W+yzYrA?y@qzlKV-egAAY#pQc-W&AsA}qRp~Y<wQ|@%SwrCpDYsl4se*T44pIs?#Z)$yijv^L^cE$xW9l%o8H%Z+m_CZRBZ}O5F7n0bwj)Zo5=4doBdJs!WCAa8l_HV(Let&Uhk$c!SQbBW%8bGF7&80A*k%|z(;9ZF5nInPNQo9pO9s?CiSAVJ!J3ID<bg+{*`j$B*SJci5^KI|%bgiEuZFh*#s{~SrmOw=CEI$riZFjfxyn8poS7rAAl7hKcdAe1w?g{p_KVlt{){!04&6`j4sw~l>Qq$BjtzM!=s!Co2{+^S%U93Acb0moNH^B0pPhkVaDDTx)I+`fhx+@>jBFU<jn9p{?(7SBvA=g4iSI|<*_T^Sm;PJ2xv}ovxFcVU%-?tK-FiQ_atU9ep?{!6B6-^v#wFE1oYZqM3fFWC^jaxvFsbxIJM`MUn)@j{mk8#}kX#}pXNKewLhfjnX=T!VJxS`WKXKRB-K8t;(p7hHb!+aPd@Ygh=nzz*!#?Ofyu;W2ed-^hJ38FcXWyNEcTx=$6*cOfTagci{r)APaG<CtTg~PbRZx`T+aK_aD%rRiJ4ng5#6JLu4spor>alu;29L&m&Xp$ZI_7G3>acbA$KFhm9-Fk|@f>VHnc-eJ<jy>B*QVW>7w*}+((6Qi9~DwPsX<>-gdv{j*m&zczqYZ8AV<>4;6=z^299+5BR6rxF#ZRf#A4F'),'Libraries/Compiler/generate_operators.☾':strd('c$}SBTW=Fb6n@XISdh@nfQfeP+@(~dB($i|L?K8>j=QqGYuA-;@)}5rsFIYMLMw%kM1eqpg+c;UX@NF^l*_}swG#ae^)Km}>#m*M(2_{rvu9?`oSE~TZ_X^HSLod6nJ=(yGwI~%(UGxn+s3Hs=JQ22j$%f>SjnV|9wspZAp*aA$jB%rBze?Ib>Juy*>v_B_rDkz8MRNGJT+_#3>x%TFyj<zwhf&tRkxO|S85)N>cEwn<FPJi;;d<!x!!ETQIeI_lCN{Mlv7gN)RLv8xRw%H>e5oTmU^_*tEE0I^=m1urHq!ee{t<!T>BT-{w1{Kg!VL{Jx#a>wjo=r@ok{9bd^5A$ecJIH_d)Gkr6_!w^s<+o*p4&x~0&Q%}GtaBm0<rLNIgPLa<!fIqpb1iLC6?mFX8kU$?Z=(<=ox?Fzx^Q<i(Oa;`3^$*C!_ZbCLWaUrA~OZG`ijmbmqoG+E8Y!&!RCP3#Qouj)P3&c2TSeKz!sZcKDYw42Ql@0m`V|tBluy<TcmoiS8>9^_a0r~8#8-<*b-Oh2tEqZQS-<WtVz?d2O4(5c{m-H?cTEd%O(rw~fG6n&h&8_=Lm;;nA(mV8(8bPp{JQgr1W&&>sVW}b04j(L~3*|vDHi&Wa#`K`TfN5pAP;>neYChP3wie|kBF!6HLDkGv)YfU{8iGFGqvY3M1cpEt(4`PLd=O^u==hY*(;w+;oa3oWIvh7=RMR!jwN)zGxkAy!*-E+Ymg^oF=rG_9SJ_sd{rsGLd~EpG_%O!kGst^PAJCua0&7dASn?kR<yV!m3r*o20`1@@63<QcY!9P=0c`Pox<fbgMutY)H~?`m08lJICMO|gc{Iw!(<4I|0<=P(hodLy6$@Dx^KL8&7a)KQ=sq(DuS@hM!6a#>#8OC#kic>zJmK+z1L!qv5am$&Tw-mT_~X_p$(GMfe*l0zRSF0+4_cljmRsACC4hLoGzQ-_y2!zLk3Jg&#S$R?HR0K((j#Ebn<{0zh@@MiSC1bX$I|c;tmulrYizF{LV7glb(JoW>noJS&iqar7`=b?{*S+B-@oCfN}T27JOp$BA3r-LBS_!E^A5cdmD|ZyMXGg!yh5In3iJ3Ux~TQpN-0y}OI6&Xn;h562KQjHoj?9xny560?6?;-i}1gt;BrrICyFtYiQmYyVx!;C=WU#JNiv#nDjcmo`Yt2xS~#S`%wKLdFH$CQ$$k<&p${|<@9Wbgq|uKjiBH}t)Qo_6Jd-jjplT6#=0YLQ9wO>YVnI%+p$)oBe~~a@TfV005$2pIBRz*KlXwm=o?Z1bpaJk&Cel^}^np|Oc74Lpj$0?58~t(^n~ZmO!n3B0wk9j3YOkT;Q`jO*)4qhNl$Fnwswb^1LL_dnJ>R735$wnpb`$7oRxix-vs!G<oa`Z3V1uq;$+l~BQ;!n-D&Wus5&J+Fiyf^Z$0Wb-FzCJsb@FmnMxww#BtXF7)Vt;nV>=gpENHrX9Aq`#NHDN5r%*<59N8Re{-l#JV`{*d60l6d@f43430M>?JtbMKr6)J_PV(CI$eN|4__*z}HP$VYTnQ;8m}%P&ktMs|CJMm<I3i$EJc|@g^uDYH@Qh&@rca~_MGWN)@SH!HwmmhNN?s4(4SDscqKg6=#iShGdgl9dIRH53lIPab^?D5}^v9JAkgb4h1~Vc78IcefQFH6(Yh?r6>EJa`-mUu;P(7W25{Q>Y4rn3Eor?W!1<JJ(aLaL3O;jl7LJn6z3r7F^wv8kQF47&Jp&2O?!G+N0t*qQkD<0ZgUJKlGS8x#6{`1AY{mq>2@6Q0k{%Y(y%re7$3oK@dE(aI0)qH$cjbV#^i+ti&WY&rHxPnNS8=cCMOeNz8^J5pm6YIf=-cVQko$~j<UzT<>U3LQA9T-$Ea7S&Kn)uAWLZ>;hC8y2OTQDz?^p1mvvB)_eH6g5{r-mBGzxjk`n7}!!bD}RTQB2j!q(?1Hk6kHlGTNp%P>)DO%-|STqpg%622~c4U@9q!i7Kl<+$ac1`O27ymANtqil|uhWj4x?@n)69WtPIOorCik4)baSE;evh=YnC8*~_VipNP7tlj~&cWtFE`9}24JT~=c>=U15&zW9AmvIiU=6LWOPWB0n5t0QAWOx$TszXGwjzBT}_)4OojW9m(095TdiKMa&&EvS=O*<9aZBOdb+?8}3!ms2qk)6=v5TEBlV*`-u@rd$%<=qrLmQvyuECW~o;w}%<}l)lk>5?=E0i}?I13Lu-G{gL+)wUjv9VK!|GkTtp_^5+CRq*j2dUa_4@*4qmug@ON{kC7l~sdicmuDGt2TF&EOxx}xfa7IR{Ecp)egwYkNLSn{uG2>#)xB#cwMZU8aU^C7X@_@66@*$6hbP|98VOVZJUQD%=5d3RiRei<sLm(yjIgsDxR_F`%Rb=ls2(Tf(Hy#@rvWL&HZ;oed8wb8MVgz%*+`@Z|BGaFJqKs;jBioOEKBQeq$iMmCnVb'),'Libraries/Compiler/gram.data.☾':strd('c$~c&U2hcE^{-6bSUcmzk!@^TgGLL4w2A@&8PcTPSw^$FW3%$^c(c0>AWY@P#38h?*4Z{7uvr=tLo35WlK|nNNRHIkzVW{E3;Yv$&OP^QKGrr;RR_qq_nv#sx##Pid&aK&^NpWxoj7&MefQ&YXQwZmcU^O~I$!jvP18DLn3>;9pE#2_WMrJc3Fhl=_@d)h0|S3-;}7A|PlIRAxo6Iva!<P-42DZD71GsIq~Ar58flcKW0V?cl%_RG)k@2Vp`3p20xj=utZll@x?hT5{Px7Od;Z+J?+^|yG+SkN?s8cmoWF3&egC6V=Lw-$opVdoKu0)v`hEAE(;sL^NCgpNND9FTYF;IPwb_POa|h21;uM4Ve6v++HI4A*V`F#Yn`eBjG+(R1ni)QLW;R<5wj6k^%BMaom3@m%Ad(-n7>u0XUUZxQm|8=eO0(3cBNg*M%K%pDEgS&6P`By4AD$b`;s&6==8IzfB+V0_=GCTK@~Tz0*;=Sq$}Z7zFL|XoTIT}BWpDyI8!$zHpYirT7~p(3GBPqVGFlvWGRK^Zl_hL67V7ho@0A%IC>Hn<>@{ZtPG#*+yBqCi$V0%e5flQ>b90H|fa-85Tv>xZh$zY0MtJL6w+!CFv<N1y&s^arDQj@8g~UiMM%HHDq)U$L8MK>WDrQlP?FSq~B6LW;^-kIp{Iv|CsFT@w)t8DD;dj)5pp}ZSjecTD!TVw)1z$4~Kl=!|CWQpA;7Vr!8R2y6TPMTMe7WJF%aZYyX;PjOb-c-jJpSd1G{JIgE}<IXPb~5%`oSmL5&J2bg>#?}8%Fr_J{<CIAgrDnh_{kWB_AbeiZr%3bIhVC2BtJ4esI<hc_%7F(mp9aDGd54OT+{Be39rVQL$(wYihbnJ0~eP61{|NVWO(bBt4K1|M+>>-6{;Q%m;WI@V70KqeUnyVfRsC03*NsD&|UgP->s8I$8nHVo8Xg$x;6R`vq>1WuN7k4CcXPuu#FUz7mgytuGHoAl$k|B-+noB(5O=3LT`<e(qLUek~fShlKm-DArIql9lTt!*wA6aUfrS(cGtQ;MMphK5o=hUjECA-HpF~#vMuDVfP902hZS^**}Up!UZ*|4Wz2pJE^|jhX}I}8NntLnObFP(loucD$$cETx#5m<06&b?R7eyHDocas~Tr>?y?IC`<g;+a}PDdNLyOKb=W<qg(~U#3k8a^OL<b{SE(|BYGsL)DX(3w#oKMX+O?b`xppF4I|t|5*_&%8#<jx_$W@anS%-_G<3#AJN;=JIrQ~ZB21nMg7^T7Y1`W(@T>r}=7GBAq5KAl4!>LA#2Z{3kNHrF(3FRe$^OahCzCon?D-v9oz2aUG^r~L1NOfnhP%HWk7Z9}}kH84k=*@;Bi$Y{$iRVEkH;%wp_lSTv8di&P0)2dA$^S$tf{|a9j8<7qyR(faa4)%VRxk-9ik)qxvxu!Dgfy+P6KGauT=xyJxICO7b7mUHGx~#vT7ucMMAl&E{Vaj}EQ0I=WGGgEn3peAnsa`mX|t;y-Ss2)w5oon5LP7+Tc3{A5Aj+eNkvy1Bg5-bOQ*!PB7pMQCW0onNWI}V{gxpfUisaPyZ_{8EKSV_$QzZ=VF^u0Xi`E`5-LilEFnp+I9kAm$3BPUA_nt~npaJhqTl^F;iGHIxhT%c7T_F^k91C37GIkNF)-eQsuee~zE{BGW4x|WMzomG&{cIe-N!}6Ug4<wIH^E~dXeSEgQWGNd#802x$ZS)n{I{K$TV>T16yOr)CnY#Q3{jw7HpssaL`O3%ew`i*_>U@vT}mAuk*%pF-m(d)n$8g-ahBem{3XVWQIhknmMkF+y9~A1U&U8UHdUUTuf6pgD7M@iqng#vMu2IKegtKJ+R0-)7%yt7jCP$P!vr9H_!(y5VYUUMDh)vybunj+#(ur$%m387E}E(ASHLMi&qz!Lc2Iw#&ZIGe<t<$<atyiAKy#jT<j`D(4AdqHBpE=HzHF|Y9mi4P)KYK(;Dc>tpowTg#}gG$6`af_Y=>DWi&I{69(bdjj(+W{*XnZubu%~8lcuqa$S&<k&dY+m%JN+2_~<h<RlB^`KAj+1qk}@$4syhGhaMe$d8N`vWxlovj7cGB6#Iv1gE^=nG?gmE@Z7m6NiPY={RpQXvoSf5+G)>mg(oSjx$`y@o|nWfxw@QG9}R_ONYy5UclqO641m*A+Inb<fB*;Th32R=-9&&VLXEFOY|e@=tm?psU}Mjnvs(e<D`vLB3wV|YfNK(miq4kt;$hRsJ9=gP&k#16ez;vtezxG2n<$d+M>#AE<lN?nv;+;AVt_|iN}w6VZsSzf{J7T>}&#$bduhIN%BTTv_}!Uk)wGr(y73PHEb45a`Cbit!`Wfpz6+24p7Z>tos-0IgZeXAv7WgoHo8<p58ZA*PdSvL=mo{#1dysY4GkkuZV{%MYSQymt=M|Ra0M5Yot)a66EeWiO-BqU3zxEMtX=pKqjH=wey3@SrEj$lNN12Ai5<mOnd>romlkBGNZv0k$(>;vevIDJJ2dAj7)hG*Cwtn=8qjc6mCDT;d#IFD*WmucXR*nc=***xIf_*f~+5QzYDt$!zVD@1Y%EzA-8|AyV2bSp!=iPGd0<3zv#8U@2!2_TU+Y2@ATSV_ttLq+CTQ%_j>Jb1YU7UM3Y|{f$|gT!2egdtjfl>1|U;AdB-W3*0t;5)|cVdEp&5q;4Sdsu=_ad{+(_U6_6^9RHT4T4Z2kD&(h0+{7Rx-)$((M?wT=2jdy^w9nrc+ba4^ZJECF?Fsp#^iG#7R^b;Cz=_RbQXl1^}47G$NLi=dOkx)@Wo`gztI(TAf@xkf6K*NL8(d75!j<SSiB;+gmBRwwSLnR{nlCsA)7%UUtlI7&n`|JykQZk#STI_05QHs?KlEDA6K8!MMVH)vk_10BaG&4*p5>*(gf+w|bq&|o{>jzXHsn>g)PPAMz6TyzDft|`UbH9kJSSI_3Wm!YfBc{^ON>6c8-bd<F$D#Up{g-^gP5P5l)OY6!h}Cw$Ka)to#-8k8Duo^TZAOVK>QA_|F7B1mcvyG0l(>cLfRgu(>F^{WX=t_ZfoUA0%xpML3(O{I1*AVwQsZzm;!tCjLL7}~8uUECY`gMY>Q=fO`K{b2#bp7qzrX_p`m#Etn2*JoGy5Eb``DXucQT4SJZ)qw+NsVsH3{xE!1bw|%T9!$)GHtnwpy}DT)$cJ>VD#V5n&~%KyG(Sm%N4u?37UGZYAF(QG`dr!zDS@kK*d#3cLM%;o2Bn|5ATSD$4NM0qnh=PyFl$bYOCS76BkH(1}Hr6HvpJN@|3Q4aoO2U7Ih*pQN#Dog2!+Ww5hd=$EO9kQWdkuqhk1=4)A6nQti0h?Qoy!{ho_4ZchCnqiYgq{2J@;>YM)Y-gaxaxyu?gp(cRC&UsI!KVL-L9G~#gC;Qla*~bqn6QH5!g=+2_3Ck3Fc)-jFQbct*~a`rUCPcSw)lr2g}|}l&F=>in;C|mb++YISQ!onIBxT=LpL88;!IYK_atz#*_u0UgL?~!h-~tMqG(A9ZRqP3h7K(;-b9Isl!%(g`_O_iFF_6dQ;#q#Hnb8jqb(Mri^a&I7hUvlv3Gl&c?9-nGV~?!&W+@~ZSvgZ1dDmh@&$_(9|kMzp_t!y16~VkkHvm9g8kBr%`bmv!7q*-S^T91)eWExnK>KxInM7bcyaG`yK4}|@Gq?3|HQ)U)%?ZRt1$U`m8SSF`(!NZzm}s|00'),'Libraries/Compiler/ast_to_py.☾':strd('c%0Q6S#uLd`kh}fP~}XIEEGwEgt!p9#CVU22`(ViR@u&!ER8^gEKO#{!Cpd&8$&|4YzGJgh(ov`OD-S~s_3eH-QN&D?o)okeqUeHGa8NLz{{%2(oA39(cj(en%9~%rkeFitLjwCLD{HJx-Bm->b~7<d6VTv{hv;CMGZ&oc4qdpys8|rdrzb82P+6YOizq#`x~)seER$5ku6)d+cq&hXOCA89M3ni#?D4-qTKL_l{HM$f^R-}<EBl29p3WJ#^G)D;PBAK_h1@Z?cE_9sV2cQYu+*f&!ejg;{fy;{fwSA21*7!NYBs(Vqw!sddK!%r&5B(ujrA%joS%4eMxT<bLrB#v8iG{|Mqro%E70#wWUj6@TR{26xp_LjkmqmYC0wY7R$q<A5`t#d#Xu`AHB_Ic}_6pHN{f*5Aw#Dy3?rgwz2o~`Ft&3n0SMCRh@<yeDn!#skE9wy{S+<cAYm*cuskD44;X{ZoATGcEIVyb3U_P6H7fh&l{YEY<h7`wkYyv_w%M&%hNF~<O}NrevPv4Cm<3<V)K?w0udN^jh?3mN~TzktzudP-kp5D%-;iVCbnkF)oD6SXXzX<Kl!Au?}HCsd+p<oH*8qHzQ6y)gVn27FMWC>Lw|l9q-?Y}ZW;ZC+Lgzr`0B5}E~xwL5O2t2M8k2x-VG($@C|QRuNnl8N~+;1Z&)cCW^eKa$+4x`8@!?1tacdk;x2!0wgNd~R_vA(p4sDSh@l#f9}%N`*>FrY7%(uxLd#k~hTa=Q6*1|4dH^~OffgO1N9i%(=5cz0ehNBtl73E40e{cXv-BLDqw{nDw(A1D2t2$*FT)O8p;uuGzov`y8+x67OK;Gd^cKBM@6fyS9=%T=(C_HK=tKHF{ek{Sf1;1*WBP>tLZ8xS^tlOGY#rQ$SPZ_ubt`F<Cnu_9#PU8pm*u}_2k>`+{z#(DKuvj~vhkh4LU9djt7)4^)3%YJo>u$5eKlkUtV4fg3pvdSE)-paO@2i06JXeR`mn9@FtFq&dY6cYdjbeDei1nO1X&I*gC+d6!d?y(pjMrVuv)-N!hvOtIG8lx_eh9^q%Z-tC5L^bh6yA9i;<xn-LYUwd>CY6j^0pe3|wQT_85Jv)`bnW_&2V-V`$_LuAMaI0La-hH3Bx@3aQ5VU(++lQw3mpz%Z8{-S6}NWEy=2na)~_6;Xt78UBq3yEC@qS8PA<67UvCBy5K{Ha6AgGbn-@wkZnN!kgR{2^;nXbR43O!+lY*V`VL)UK8trvKxCd=2&wq7#kZiSMA+r?laIp8*((F3?R<Y!@BrRml&3dS!1U3hLJH$!_;N@IfzH2-gJC2Exaix5Fy1ZyzSiwEr9n7Q<Z1*5ZYhBfC=o1s#7zZX%~!{UG@Xpok9HP!CE}c8X!g`__GF981O+FL|4wqZRd^n;a*X7wha!95*Vr9FMlx$f5**mA`BvvY*TQnFW?S}IivaUtXcr=z7@{G4+(IZa6@1a)vk<=TNo>x2GjQ?nQW8GLbww-G`t3jDsF-^IsRnn_%FZxc<H~Fu9_C#kz%L8zs=p0WAgDaK<C9vrr1&>>luBBjE-PmW?LHom25g!Z+x|oRRunK6u_NEa0Cs1Mr?M#StGi#EZUN9mT9#wD23}HeM;I8fthFMw`>cNZ4wIN9WIZzh@?{kSrSeO+N0D6aTehDd{aal>zuby_y|D~Kc_zs&a|uqmnmDEka7%r(71p}LyQU$qDq000VOmQv}YzRN9h?QEK0x%AT<GeXVLF;bUTRLJpGmZo)f=U<S!@qY%a)ZnhZgu6F`tWsp8(E#0Q=W+H+n;!JCGL$r=cQ*NnH($Z%zn(+w4|IY6*!X?lbNX84wKlf-vl%Btdpm7u~X{vz=D{qh+Rm;C#z4aV7a%U*dBqQ+21)kL75R7x>X7WQ-=;*8MtGp>D_XgJOsGYv3MO0?uQYs$j4!%}^@N}7^z0x?pKk%+*K{(kxN&rvJYhEZeyejuPWDvU{DXtZ0bQ-K9mvIXWIne8L+BNK$S&I;pYP=d+x2SHajSJTA6tkx?5jLcLd#c5l!SGO|V*|@JG8^xX-GJ6$=o?&+0I<YIydw@B*JecF%=v+vH8F6Q62#orTdc`4ytbv)S)zQSKqq8)7Uc(0Mzyf_J9IQmdinw1sB<`Y_w)OKqFbKl;K}McyxfbgrL>eo!Vl2b9*vOhPw^CdADgfA0mWJp0y0_qiiqc<2R>zbc7mvpPF1Lkoqp;ps!%<|R!8{|MQ|aWkSUJxCRTZ=`m4ETz#obTLm`~}!fJH-B*CL}4L(3qX5WmPpV1ZC!#miBF$2i;YgOJA^v%;B~m~a%^g(K7mE)u>o(2WcL7tZgXfW1m%x<Ybq|CY1%t#q|awPEyEkR?-NMymXuOx4Ejpxzzo6_g@w-OEATGSVwVur;5@g6Ej*qmFQ&$h>9PDpr6L$h6{pD3%JqqS;k`Lb*w_ZdNW9azO8LMKqOXJDs2$03khcZCi|O%LV5zAKc5xpokZj18%V!xQk->>*9A2_Ro^h_ANc<(o}n(6x+u%G*GZKzvDNPDlb^-5*Y-fk6a98;v^Qa{izAv6069b8C;gsh4CULV++xU&u^l20^f9sUJ-6jMAw`+?6?~1z<4(dy$cq$bPrrsal@IMG;yl9txs?jh=iq;B}ji*Wx|Z{7ClVNKG>ilCi;DtDrs3J@=hjI43|ELys_VJ#*!}n63L3hlvNf(pD23zlp}x`oN=jZj)|O%W@qUFGSNe9Ha0fBjFL++UUIn$oRq{`*;Is3Z`fHv3Ra!cl=Jk0rBY(<%C*CZ92lq&kF24iWb~rbvE-l=uQGfK0iWCSDoM~~OV3=;%7>C8=4gZCV>OSET#ZolMPh+evLJ2gfvo>0x}r((qBsR`?M6LN2{MC~k{WlDGDIT5h$Pw^fzUiXMELPtR^g`(!T8x%cv!|NF(X4eG~LlEhy}fZ$jgUWUaId=nm_!g?7f7JadXw@uVPjqhGy>?b$Ne!MjDHNqsA|-T5x&4^C9Qu?me*8^JgRZSLeD^UVBcG@mEthN~cm!dP^PYWO4P0ud&dRvX7cC`E$qE5NpoNdGu@DF((p^#>#Xo28qrsj2n^aq8%AsjEydiN8Ki2K2U`_shNx)Oa}JS?EcOSh{pgrL-y>dHyk4UCa;wO?yqsg&&KQ!R+6-$YC+>4$Q&*cb{6%(dq5dZ#z_s>nvTG5N7NE*1cV+i5n?sM-M(Bw2PA7$+%iT5w<8ZLtx0#8Jd9==vdFAq(v?@qocaTds@L?@*2Girp1BY>UbC0N7-=iqDtHo=#Ow>PCNVwGy3-SO<bN;7iG50}V}XzDSW6q|OjIgfEF)TGl`Re{O}nw!@iI9Zn~x$DcgjcU^=LGbG5Bh?#O!a0xwLQ%O+&wQ;r$(lWMT`h#?*x$v$C_Z#AHOAk=+&%J#(+o6PndVL58z2kX$twOsRbF+(I0@Y90lTSgv<Cc@LAl0d`VtrN-#|1_|C`an|Ll2^$3XFnP<BUDs(=iMIEVDrZ}XaD!3kQofH@z}k!T%DbzFitf|nnP(-Mc4|Jm2tK>W31P|WuB6O0Lk45b5d<ZgDXDB5-a5Kw#nj%EraRLW#|@aG52CmsGY47bJ{Wp#;e8>%I;(qBqwI@`k#oU8#{Jl_;8ZRDX1UEBvls}AFE14XrBs~S1V_+2#D40n=77s?Lv;=Q#nmx!mn*!t6*j<2QW6la36F;BkEbM(?WU@dt2cee3s4|<{W!%F19EO{I{Ao;CrK+=(8Gx8R1xf~b)6z8KQ;blg$K=!sLbFbozsgxDsD*&Sb^n9fj9|okwou2OtZ@l;$8&WVjc=vyqq+WSWBudr;rr8BOzVONUZvnUQw!fZigO7f!l8x@ve$1t5Bl06g_dp<9x=?tWmY(QI0&(vE<znHuOZwX;lxq1uWKs0hSE#9ZY6UGAm+tRm2%RZk}EW#7i_dq|$K8P1}jMBQa<ogok{khrn;$>BL0D$SEb<H(~S>OI>!7cO;w+D=}jTnd5f%KL<EdFb7xs7HF5NRoiX(NoZ${dMQ89o?GS|-JH9+IVbgO(q*e~W^TKsrM@JV{F{8dIbhVW4!|!^h)Mt}Hr&;5Mv~%`bIUKQoS<HHbvfdXns<Ipf!$sLGiiIyPB7PGIBU4tZ6y?-pRf_0F3}5`{UyW5TYh6|IK1!R;`V_3aKRzB-ESHl9>xA~A^a{2U|qn)8XsTLZJgAT%&=<CW6)Q~GGN$+(~4>u_v&(aM(AYOm4t5F98wx;&m3&vc`kwXy2XVwdS$MtN0J&xIUx4oNYtA_%l5qrAQLT@EYJr6AthMeq-JoZLC)L=aYc(UTklXuoGi$|9(syC=rl{~Qxo}K^8M{Vc{KcmkQ`@12FJxgkb?B$N=Wlo;%2eneZY#i%w%baI2<7gnliQtPbBUF7#Qah?18}C6;9<<)PmaMpdPVgd`-ksa8gcx#R%gE<8n{L<yhfA#`H$$OiD~Xtl{hFVL8WGkuW^!y;6K5EG;ImR8#A2EG<fwu6bz`l_W<J$gI&U<uxvD)tpJr4YOyVX<^ja<+2k40ufvj?HivJfg5r9!`!U2rUDxbOTB4NVp!?vw&fJP!oD8~T*Gj#gE7LPSz+CAwg}_4ZB9NDM1`O0HJB4<3!CDqOSqcN<O?$Ac!ORcZDw2DzvZN(^8_*?H*dKS$}-;;c#cyNVOg^UOEt@rj{Q;D^JS~&xbP+hX-r~^Az`(8qhZSidsnOB`1VBEuUGUSiFCRKoDnx$AhctdToj4;1ydQ86L*GRz>nuGEM_=D+Uo>iV5Wl3>vWEE33X63^=L<z;g-unp_dCakYrdzm-n2*spi_O=ws2*_2|(EBUy`&Vp>qIsXgv`p&Ad+#a6eC1!nVM{GYb~AbSnGnYN+Omz!#`WpMj*{0SD2`4mrr*^%Z&%;JH=i(2N!rP>^9Rh@ycrZ}%fW!ux7n#6S=lPDG5S_@1s#Y4&3P6#8-w+m}c3?+|%=3vF?X?VEA&TVyAkLgh&#M~V6ycY8Y?o6<&)fCLAH+QZy1R97cE};JZ%pUp&{=?cf+a}sSsS#5t9ppXgne{*_VajZfm^+5>ehz$F*8c#=1fkC')})
__dir__=(__file__:=áÌî(moon_dir/'Libraries/Compiler/main.☾')).parent
(ÄÊPSH(__ÄÊIMPORT__('cache', globals(), '')), ÄÊPOP())[-1]
(code_file_caching := True)
(TMP := mkd(ð(TMPDIR, ÂÞÅCAT(ÂÞÅCAT(__file__, ÐØó), sha))))
(header_com := ÁØÿþÁÙÇ(lambda ÂîÓ, ÂîÒ: ÐÌü(ð(ÂîÓ, '%s.☾' % (ÂîÒ,)).resolve))(ð(moon_dir, 'Builtins'), ÄÝöÞ(ÐØó(ð(moon_dir, 'Builtins/builtins')))))
(pathlib_import := ('from pathlib import Path as %s\nmoon_dir = %s(__file__).parent' % (PEV('𝐩'), PEV('𝐩'))))
(to_py := (lambda áÖï, *áÑË, **áÑÕ: lambda *áÑË, **áÑÕ: ast_to_py(*áÑË, áÖï=áÖï, **áÑÕ)))

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

def ÄÊdo_imps():
    if ÄÊmoon_to_py.has_lazy_load:
        return
    (ÄÊPSH(__ÄÊIMPORT__('text_format', globals(), '')), ÄÊPOP())[-1]
    (ÄÊPSH(__ÄÊIMPORT__('to_ast', globals(), '')), __ÄÊADDGLOBALS_CLEAN__(ÄÊPKE(), globals()), ÄÊPOP())[-1]
    (ÄÊPSH(__ÄÊIMPORT__('ast_to_py', globals(), '')), __ÄÊADDGLOBALS_CLEAN__(ÄÊPKE(), globals()), ÄÊPOP())[-1]
    (ÄÊPSH(__ÄÊIMPORT__('tree', globals(), '')), __ÄÊADDGLOBALS_CLEAN__(ÄÊPKE(), globals()), ÄÊPOP())[-1]
    (ÄÊPSH(ÄÊmoon_to_py), ÄÊPSH('has_lazy_load'), ÄÊPSH(True), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]

def ÄÊmoon_to_py(áÖï, áÖÝ, áÏè):
    ÐÌü(ÄÊdo_imps)
    return to_py(áÖï)(to_ast(áÖï, **áÖÝ), **{'reparse': True, **áÏè})
(ÄÊPSH(ÄÊmoon_to_py), ÄÊPSH('has_lazy_load'), ÄÊPSH(False), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
(ÄÊmoon_to_py_fcache := fcache(fp=ð(CACHEDIR, '%s' % (BOOTSTRAP_HASH[slice(None, 16)],)), file_only=True)(ÄÊmoon_to_py))

def moon_to_py(áÖï, áÖÝ={}, áÏè={}):
    if (h := sha(áÖï, áÖÝ, áÏè)) in (c := moon_to_py.áÐñ):
        return c[h]
    return (ÄÊPSH(c), ÄÊPSH(h), ÄÊPSH(ÄÊmoon_to_py_fcache(áÖï, áÖÝ, áÏè) if code_file_caching else ÄÊmoon_to_py(áÖï, áÖÝ, áÏè)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
(ÄÊPSH(moon_to_py), ÄÊPSH('áÐñ'), ÄÊPSH({}), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
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
    (pyc := (lambda ÂîÓ: '#!/bin/python\nBOOTSTRAP_HASH=%s\n%s' % (ÂÞÅCAT(ÂÞÅCAT(ÂîÓ, sha), repr), ÂîÓ))('%s\n%s\n%s\n%s' % (pathlib_import, ÂÞÅCAT(header_com, compile_files), ÐÌü(dump_cached_imports), ÐÌü(Æå))))
    if dest:
        ÐØì((ÄÊPSH(dest), ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0), áÌî)), (dest := ÄÊPKE(0)), ÄÊDEL(2))[2], pyc)
        os.chmod(dest, 509)
    return pyc

def generate_bootstrap_live(*áÑË, **áÑÕ):
    ÐÌü(refresh_cached_imports)
    Âçß(Åøþáüì('Refreshed cached imports!', 'f0f'))
    (Compiler := (ÄÊPSH(__ÄÊIMPORT__('Compiler', globals(), '')), ÄÊPOP())[-1])
    (ÄÊPSH(Compiler), ÄÊPSH('code_file_caching'), ÄÊPSH(False), setattr(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
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
                except Exception:
                    pass
                try:
                    ÄÕôñ(áÕÃ, ns, native=True, Æå=exec, ret=True, init_ns=False)
                except áÍÚ as Ïã:
                    Âçß(Âøî(ÂÞÅCAT(Ïã, traceback.format_exception), ÁØã))

def transpiler_cli(*áÒø):
    (show_docs := (lambda: Âçß('Usage: ∅                  (cli mode)\n       <file_path>        (run ☾ file)\n       -h                 (show this)\n       -c <code_to_run>   (eval mode)\n       -C <code_to_run>   (exec mode)\n       -B <boostrap_dest>\n       -e <str_to_encode>\n       -d <str_to_decode>\n       -o <file_in> <file_out?stdout>')))
    (ÄÊPSH(([*áÒø], ÂÔð())), ((áÒø := ÄÊPKE(0)[0]), (f := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
    while áÒø and (áÓÓ := áÒø[0])[0] == '-':
        if not ÂåÔ((ÄÊPSH(f), ÄÊPSH(ÂÕØ(ÄÊPKE(0), (lambda ÂîÓ: [ÂîÓ[slice(1, None)]] if ÂîÓ[0] == '-' else ÂîÓ)(ÂÞÅCAT(0, áÒø.pop)[slice(1, None)]))), (f := ÄÊPKE(0)), ÄÊDEL(2))[2], áÓÓ != 2 * '-'):
            continue
        None
    (Æå := (moon_to_py if not ÂÕÖ('aA', f) else ÂåÔ(ÐÌü(ÄÊdo_imps), lambda *áÑË, **áÑÕ: moon_to_py_debug(*áÑË, **áÑÕ, show_preast=ÂÔö(f, 'A')))))
    if (ÄÊDEL(1), False)[1] if ÄÊPSH(f) else ÄÊPOP() if áÒø else (ÄÊDEL(1), True)[1]:
        ÐÌü(ÄÊdo_imps)
        ÐÌü(moon_cli)
    elif (ÄÊDEL(1), False)[1] if ÄÊPSH(f) else ÄÊPOP() if ãÊú(áÒø) < 1 else (ÄÊDEL(1), True)[1]:
        ÂÞÅCAT(0, áÑË.pop)
        return ÄÕôñ(ÂÞÅCAT(áÒø[0], ÐØó), ns={'__file__': áÒø[0], '__dir__': ÂÞÅCAT(áÒø[0], áÌî).parent, '__name__': '__main__'}, Æå=lambda x, y: exec(x, y, y))
    elif ÂÔö(f, 'C'):
        ÂÞÅCAT(ÂÞÅCAT(Âøî(áÒø, ' '), Æå), exec)
    elif ÂÔö(f, 'c'):
        (lambda ÂîÓ: MOD(Áëý, áØÁ=ÄÊCUR((1,), {}, ÂÕõ, ÂýÃ, None))(ÂîÓ, MOD(Âçß, áØÁ=ÁØã)))(ÂÞÅCAT(ÂÞÅCAT(Âøî(áÒø, ' '), Æå), eval))
    elif ÂÔö(f, 'h'):
        ÐÌü(show_docs)
    elif ÂÔö(f, 'get-dir'):
        Âçß(moon_dir)
    else:
        ÐÌü(ÄÊdo_imps)
        if ÂÔö(f, 'D'):
            while True:
                Âçß(ÂÞÅCAT(ÂÞÅCAT(ÐÌü(input), VEP), __highlighter__))
        elif ÂÔö(f, 'd'):
            Âçß(ÂÞÅCAT(Âøî(Áÿú(áÒø, VEP), ' '), __highlighter__))
        elif ÂÔö(f, 'e'):
            Âçß(Âøî(Áÿú(áÒø, PEV), ' '))
        elif ÂÔö(f, 'B'):
            ÂÞÅCAT(ÂÞÅCAT(áÒø[0], áÌî), generate_bootstrap_live)
        elif ÂÔö(f, 'b'):
            ÂÞÅCAT(ÂÞÅCAT(áÒø[0], áÌî), generate_bootstrap)
        elif ÂÔö(f, 'o'):
            ÐôÅ(Ááú(áÒø, [0, 1, 2]), lambda x: ÂÞÅCAT(compile_code(ÂÞÅCAT(x[0], ÐØó)), ÄÊCUR((2,), {}, ÐØì, x[1], ÂýÃ) if x[1] else Âçß))
        else:
            ÂåÔ(Âçß('Invalid mode(s): %s' % (f,)), ÐÌü(show_docs))
__ÄÊADD_EXPORTS__(globals(), ('moon_to_py', moon_to_py), ('moon_to_py_debug', moon_to_py_debug), ('compile_files', compile_files), ('generate_bootstrap', generate_bootstrap), ('transpiler_cli', transpiler_cli), ('moon_cli', moon_cli), ('refresh_cached_imports', refresh_cached_imports))
TRANSPILE_REF(moon_to_py)
if __name__ == '__main__':
    transpiler_cli(*áÑË[slice(1, None)])
else:
    ÐÌü(ÄÊdo_imps)