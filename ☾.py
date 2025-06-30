#!/bin/python
BOOTSTRAP_HASH='OjWIk0g1PdZH_P1yt4VpYCZCB3HiSB_Gyr-8ZS2OwHI'
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
(ÁØòþë := (ÁÙÇþë := (lambda Æå: lambda áØÆ, *áÖÒ, **áÖÝ: [áÑÿ for ÄÝõÌ, v in ÂÓÏ(áØÆ) if (áÑÿ := Æå(v, ÄÝõÌ, áØÆ, *áÖÒ, **áÖÝ)) is not ÄÔýò])))
(ÁØÿþÁÙÄ := (lambda Æå: Æå))
(ÁØòþÁÙÄ := (lambda Æå: lambda áØÆ, áØÇ, *áÖÒ, **áÖÝ: [áÑÿ for v in áØÆ if (áÑÿ := Æå(v, áØÇ, *áÖÒ, **áÖÝ)) is not ÄÔýò]))
(ÁØÿþÁÙÇ := (lambda Æå: lambda áØÆ, áØÇ, *áÖÒ, **áÖÝ: [áÑÿ for v in áØÇ if (áÑÿ := Æå(áØÆ, v, *áÖÒ, **áÖÝ)) is not ÄÔýò]))
(ÁØòþÁÙÄþë := (lambda Æå: lambda áØÆ, áØÇ, *áÖÒ, **áÖÝ: [áÑÿ for ÄÝõÌ, v in ÂÓÏ(áØÆ) if (áÑÿ := Æå(v, áØÇ, ÄÝõÌ, áØÆ, *áÖÒ, **áÖÝ)) is not ÄÔýò]))
(ÁØÿþÁÙÇþë := (lambda Æå: lambda áØÆ, áØÇ, *áÖÒ, **áÖÝ: [áÑÿ for ÄÝõÌ, v in ÂÓÏ(áØÇ) if (áÑÿ := Æå(áØÆ, v, ÄÝõÌ, áØÇ, *áÖÒ, **áÖÝ)) is not ÄÔýò]))
(ÁØòþÁÙÇ := (lambda Æå: lambda áØÆ, áØÇ, *áÖÒ, **áÖÝ: [áÑÿ for x, y in ÄÕåØ(áØÆ, áØÇ) if (áÑÿ := Æå(x, y, *áÖÒ, **áÖÝ)) is not ÄÔýò]))
(ÁØòþÁÙÇþë := (lambda Æå: lambda áØÆ, áØÇ, *áÖÒ, **áÖÝ: [áÑÿ for ÄÝõÌ, (x, y) in ÂÓÏ(ÄÕåØ(áØÆ, áØÇ)) if (áÑÿ := Æå(x, y, ÄÝõÌ, áØÆ, áØÇ, *áÖÒ, **áÖÝ)) is not ÄÔýò]))
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
(ÂØÑ := (lambda *áÑË, áØÁ=1: (Æå := (lambda *áÑË, n=1, r=[]: (lambda ÂîÓ: Áÿú(ÂîÓ[0], lambda x: Æå(*ÂîÓ[slice(1, None)], r=r + [x]) if ãÊú(ÂîÓ) > 1 else r + [x]))(áÑË * n)))(*áÑË, n=áØÁ)))
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
(SPE := MOD(lambda ÂîÓ: ÂîÓ in ENC + 'þ'))
(PEV := MOD(lambda ÂîÓ: Âøî(MOD(ÄÔÔç, áØÁ=Âåæ(Âøî, MOD(ÁØò(lambda ÂîÓ: ÄÝöì(ÄÝöí(ÂîÓ), ãÊú(ENC), C=ENC)))))(áÇù(ÂîÓ, RCD), MOD(lambda ÂîÓ: ÂÞÅCAT(ÂîÓ[0], RCD))), 'Þ')))
(VEP := MOD(lambda ÂîÓ: Âøî(MOD(ÄÔÔç, áØÁ=MOD(lambda ÂîÓ: Âøî(ÁØò(lambda ÂîÓ: MOD(Áëý, áØÁ=ÄÊCUR((1,), {}, ÂÖó, ÂýÃ, ENC))(ÂîÓ, ÄÔâÑ(Âåæ(Âåæ(Âøî, ÄÝöí), ÄÊCUR((1,), {'C': ENC}, ÄÝöì, ÂýÃ)), lambda x: '⸮%s?' % (x,))))(ÄÝöÞ(ÂîÓ, 'þ')))))(áÇù(ÂîÓ, SPE), MOD(lambda ÂîÓ: ÂÞÅCAT(ÂîÓ[0], SPE))))))

def OPWRAP_(*áÖê):

    def R(Æå):
        for x in áÖê:
            (ÄÊPSH(globals()), ÄÊPSH(tmp[x] if x in tmp else PEV(x)), ÄÊPSH(MOD(Æå, x)), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
    return R
(ÄÊPSH((callable, lambda x: hasattr(x, '__iter__'))), ((áÓó := ÄÊPKE(0)[0]), (áÓö := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]

def áÓõ(x):
    try:
        return hash(x)
    except áÍÚ:
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
    except áÍÚ:
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
    (áÑÅ := MOD(lambda ÂîÓ: ÂîÓ[slice(4, 4 + struct.unpack('I', ÂîÓ[slice(None, 4)])[0])]))
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
    except áÍÚ:
        pass
    Âçß('WARNING: Failed to copy.')

def PL_TEXT_PASTE():
    try:
        from clipboard import paste
        return paste()
    except áÍÚ:
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
        (ÄÊPSH((MOD(Áëý, áØÁ=áÓó)(áØÁ, MOD(lambda ÂîÓ: ÂîÓ(áØÆ))), [])), ((ids := ÄÊPKE(0)[0]), (TD := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
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
(ÂÿÇ := (lambda áØÆ, áØÁ=ÂÞÅ: ÄÝöÈ(MOD(Áëý, áØÁ=áÓö)(áØÆ, ãÊú)) if áØÁ is ÂÞÅ else MOD(Áÿú, áØÁ=ÂüÌ(áØÁ) if áØÁ < 0 else 1)(MOD(ÂÓÏ, áØÁ=áØÁ)(MOD(Áëý, áØÁ=Âåæ(Âó, áÓö))(áØÆ, Âåæ(MOD(ÂØÑ, áØÁ=ÂüÌ(áØÁ)), ÂÿÇ))), MOD(lambda ÂîÓ: ÂîÓ[0]))))
(ÄÕÊÂ := (lambda áØÆ, áØÇ, áØÁ=ÂÞÅ: MOD(Áëý, áØÁ=ÁØö(áØÆ, ÁÜÙ))(ÄÔÙù([áØÁ if áØÁ is not ÂÞÅ else ' ' if ÁØö(áØÆ, ÁÜÙ) else False] * l, áØÆ) if (l := (áØÇ - ãÊú(áØÆ))) > 0 else áØÆ, Âøî)))
(ÄÕÊÄ := (lambda áØÆ, áØÇ, áØÁ=ÂÞÅ: MOD(Áëý, áØÁ=ÁØö(áØÆ, ÁÜÙ))(ÄÔÙù(áØÆ, [áØÁ if áØÁ is not ÂÞÅ else ' ' if ÁØö(áØÆ, ÁÜÙ) else False] * l) if (l := (áØÇ - ãÊú(áØÆ))) > 0 else áØÆ, Âøî)))
(ÄÔéÄ := (lambda áØÆ, áØÇ, áØÁ=ÂÞÅ: ÂåÔ(ÂåÔ((R := MOD(lambda ÂîÓ: Âêà(ÁØã) if ÂîÓ is ÂÞÅ else Âêà(ÂîÓ) if ÁØö(ÂîÓ, ÁÜÙ) else Áÿú(ÁãÁ(ÂîÓ), ÁÜÙ))), (Æå := MOD(lambda ÂîÓ: MOD(ÆÑ, áØÁ=ÂîÓ)((lambda ÂîÓ, ÂîÒ: MOD(ÄÕåØ, áØÁ=ÄÝöÉ(ÂîÒ))(ÂîÓ, ÂîÒ))(R(áØÆ), R(áØÇ)), lambda x, y: x.replace(*y))))), Æå if áØÁ is ÂÞÅ else ÂÞÅCAT(áØÁ, Æå))))

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
        (y := áÍè(MOD(ÄÔÔç, áØÁ=MOD(lambda ÂîÓ: ÂÁÍ(ì)(ÂîÓ, ãÊú(x))))(y, MOD(lambda ÂîÓ: ÂîÓ < 0))))
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
    (áÍÌ := ÄÔÔè(áÍÌ, MOD(lambda ÂîÓ: ÂîÓ == [])))
    if ÁØö(x, ÁÜÙ):
        (áÍÌ := MOD(ÄÔÔç, áØÁ=MOD(lambda ÂîÓ: Âøî(ÂîÓ, ÁØã)))(áÍÌ, MOD(lambda ÂîÓ: ÄÝøÇ(ÂîÓ, ÁÜÙ))))
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
        (ÄÊPSH((Áÿú(Ááú(áØÆ, [0, ãÊú(áØÇ) - 1]), MOD(lambda ÂîÓ: Âøî(ÄÔÔç(ÂîÓ)))), CUR(lambda ÂîÓ, ÂîÒ: ÂîÓ == ÂîÒ, áØÇ), ãÊú(áØÇ), ãÊú(áØÇ) - 1)), ((áØÆ := ÄÊPKE(0)[0]), (áØÇ := ÄÊPKE(0)[1]), (Y := ÄÊPKE(0)[2]), (ÏÁ := ÄÊPKE(0)[3])), ÄÊDEL(1))[1]
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
        (ÄÊPSH(MOD(ÁÞç, áØÁ=0)(Áÿú(ÄÝõé(áØÁ), Âüð), MOD(lambda ÂîÓ: ÂîÓ or 10))), ((áØÇ := ÄÊPKE(0)[0]), (áØÁ := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
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
    (ÂÐôþáÏß := CUR(lambda ÂîÓ, ÂîÒ: Âøî(ÂÀÇ(ÁØò(lambda ÂîÓ: ÂîÒ[ÂîÓ % ãÊú(ÂîÒ)])(ÂÛÜ(MOD(lambda ÂîÓ: ÂîÓ // ãÊú(ÂîÒ)), Âó)(ÂîÓ))))))
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
        (ÄÊPSH(áÖÒ), ÄÊPSH(Áÿú(ÄÊPKE(0), Âåæ(MOD(lambda ÂîÓ: MOD(ÄÕÊÄ, áØÁ=ÂîÓ[-1] if áØÁ is ÄÕøü else áØÁ)(ÂîÓ, h)) if áÑã == '\U000f147c' else MOD(lambda ÂîÓ: MOD(ÄÕÊÂ, áØÁ=ÂîÓ[0] if áØÁ is ÄÕøü else áØÁ)(ÂîÓ, h)), áÍá))), (áÖÒ := ÄÊPKE(0)), ÄÊDEL(2))[2]
    return [*zip(*áÖÒ)]

def ÁÛÛ(áØÆ, áØÁ=ÂÞÅ):

    def Æå(áØÁ):
        if ÄÝøÇ(áØÁ, áÓö) or ÁØñ(ÁÜÙ, áØÁ):
            (ÄÊPSH(áØÁ), ÄÊPSH(Âêà(ÄÊPKE(0))), (áØÁ := ÄÊPKE(0)), ÄÊDEL(2))[2]
        (áÓÕ := (MOD(ÁÛÛ, áØÁ=áØÁ[slice(1, None)]) if ãÊú(áØÁ) > 1 else ÄÕÍÔ))
        (áÓÙ := (lambda x, y: áÓÕ(x[y % ãÊú(x)]) if ÁØö(y, ÂÑÅ) else áÓÕ(x[y]) if ÁØö(y, ÁÜÙ) or ((ÄÝøÆ(áÓö, ÄÊPSH(y)) and ÄÝøÇ(ÄÊPOP(), ÄÊPSH(slice))) and (ÄÊDEL(1) or True) or (ÄÊDEL(1) or False)) else MOD(Áëý, áØÁ=áÓÕ is not ÄÕÍÔ)(ÄÝöÊ(x, y), MOD(lambda ÂîÓ: Áÿú(ÂîÓ, áÓÕ)))))
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
                    (ÄÊPSH(v), ÄÊPSH(Ïß), ÄÊPSH(ÄÔÙù(ÂÀÇ(áÇù(v[Ïß], MOD(lambda ÂîÓ: ÂîÓ is ÂýÃ))))), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3]
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
(ÄÝõÞ := (lambda áØÆ, áØÁ=ÂÕË: ÂÚü() if ÄÝøÇ(áØÆ, áÓö) else ÁØò(lambda ÂîÓ: ãÊú(ÂîÓ) if ÁØö(ÂîÓ, áÓö) else ÄÔýò)(ÂÕÅ(MOD(ÂØÎ, áØÁ=-áØÁ)(MOD(lambda ÂîÓ: ÂîÓ[0] if ãÊú(ÂîÓ) else 0), MOD(lambda ÂîÓ: ÄÝøÇ(ÂîÓ, áÓö) or ÁØö(ÂîÓ, ÁÜÙ))), áØÆ))))
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
(UGX_CREATE := (lambda x, d=False: MOD(lambda ÂîÓ: d if (y := UGX_RUN(winder([*ÂîÓ]), x)) is ÂÞÅ else y[0])))

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
        return (ÂÐí(ÂÞÅCAT(c[0], 2)), ÂÐí(ÂÞÅCAT(c[0], 2)), ÂÐí(ÂÞÅCAT(c[0], 2)), 255)
    if n == 2:
        return (ÂÐí(ÂÞÅCAT(c[0], 2)), ÂÐí(ÂÞÅCAT(c[0], 2)), ÂÐí(ÂÞÅCAT(c[0], 2)), ÂÐí(ÂÞÅCAT(c[1], 2)))
    if n == 3:
        return (ÂÐí(ÂÞÅCAT(c[0], 2)), ÂÐí(ÂÞÅCAT(c[1], 2)), ÂÐí(ÂÞÅCAT(c[2], 2)), 255)
    if n == 4:
        return (ÂÐí(ÂÞÅCAT(c[0], 2)), ÂÐí(ÂÞÅCAT(c[1], 2)), ÂÐí(ÂÞÅCAT(c[2], 2)), ÂÐí(ÂÞÅCAT(c[3], 2)))
    if n == 5:
        return (ÂÐí(ÂÞÅCAT(c[0], 2)), ÂÐí(ÂÞÅCAT(c[1], 2)), ÂÐí(ÂÞÅCAT(c[2], 2)), ÂÐí(c[slice(3, 5)]))
    if n == 6:
        return (ÂÐí(c[slice(0, 2)]), ÂÐí(c[slice(2, 4)]), ÂÐí(c[slice(4, 6)]), 255)
    if n == 7:
        return (ÂÐí(c[slice(0, 2)]), ÂÐí(c[slice(2, 4)]), ÂÐí(c[slice(4, 6)]), ÂÐí(ÂÞÅCAT(c[6], 2)))
    if n == 8:
        return (ÂÐí(c[slice(0, 2)]), ÂÐí(c[slice(2, 4)]), ÂÐí(c[slice(4, 6)]), ÂÐí(c[slice(6, 8)]))
(r2hl := (lambda x: '#%s' % (Âøî(Áÿú(x, MOD(ÄÝöì, áØÁ=16 + ÂÞÅCAT(2, Ãù)))),)))
(h2hl := Âåæ(r2hl, h2r))
(TERM_RESET_B := '\x1b[49m')
(TERM_RESET_F := '\x1b[39m')
(TERM_RESET := '\x1b[0m')

def termclr(t, fg=None, bg=None, rst=True, rl=False):
    (rlw := (lambda x: '\x01%s\x02' % (x,) if rl else x))
    (mkc := (lambda x, y, z, w, v: ÂÞÅCAT('\x1b[%s;2;%s;%s;%sm' % (x, y, z, w), rlw)))
    (R := Âøî([mkc(n, *h2r(c)) for c, n in ÄÕåØ([fg, bg], [38, 48]) if c is not None]))
    return '%s%s%s' % (R, t, rlw(ÁØã if fg is None and bg is None else TERM_RESET_B if fg is None else TERM_RESET_F if bg is None else TERM_RESET) if rst else ÁØã)
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
    (ÄÊPSH(ÄÝöÞ(ÐØó(SCRIPT_FILE_LOC).strip('\n'), '\n')), ((CHAR_NRM := ÄÊPKE(0)[0]), (CHAR_SUP := ÄÊPKE(0)[1]), (CHAR_SUB := ÄÊPKE(0)[2])), ÄÊDEL(1))[1]
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
    (áÓÕ := MOD(lambda ÂîÓ: supscript if ÂîÓ in SUPSCRIPT else subscript if ÂîÓ in SUBSCRIPT else None))
    return Âøî(ËãÂ(ÄÕåØ(ÁØò(lambda ÂîÓ: MOD(ÆÑ, áØÁ=ÄÕÍÔ)(Áÿú(ÂÕÅ(ÂÛÜ(nrmscript, Âåæ(Âó, áÓÕ)), ÂîÓ), áÓÕ), Âåæ))(áØÆ if áÕÉ is ÂÞÅ else áÕÉ), Æå(ÂÕÅ(ÂØÏ(nrmscript), áØÆ))), ÂÕÅ))
__dir__=(__file__:=áÌî(moon_dir/'Builtins/highlighter.☾')).parent
(styf := ð(moon_dir, 'Builtins/Data/style.json'))
(styd := ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(styf, ÐØó), áÐÞ[ÿ]), ÂÑÖ()))

@cache
def sty(s, bg=0, def_='bec'):
    for k, v in styd:
        if not (s in k and ÂÔö(v, 'color')):
            continue
        return termclr(s, v['color'], bg)
    return termclr(s, def_, bg)
(__highlighter__ := (lambda l, b=None, clr='bec': Âøî(Áÿú(ÂÞÅCAT(ÂÞÅCAT(l, ÁÜÙ), VEP), ÄÊCUR((1,), {}, sty, ÂýÃ, b, clr)))))

def highlight_tester():
    while (l := ÐÌü(ÂÐðþáÐâ.readline)):
        Âçß(ÂÞÅCAT(ÂÞÅCAT('\n', l.rstrip), __highlighter__))
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
(ÄÊPSH((MOD(lambda ÂîÓ: ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ, áÍÇ), zibe), b85e), áÍÇ)), MOD(lambda ÂîÓ: ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ, áÍÇ), b85d), zibd), áÍÇ)))), ((stre := ÄÊPKE(0)[0]), (strd := ÄÊPKE(0)[1])), ÄÊDEL(1))[1]
(__ÄÊIMPORTS__ := ÐÌü(ÂÑÖ()))
(TP_CACHE := {})
(TRANSPILE_REF := ÐÌü(Holder))
(EXEC_NATIVE := exec)
(dump_cached_imports := (lambda: 'TP_CACHE.update({%s})' % ((lambda ÂîÓ: Âøî(ÂîÓ, ','))(ÁØò(lambda ÂîÓ: '%s:strd(%s)' % (ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(moon_dir, ÂîÓ[0].relative_to), ÁÜÙ), repr), ÂÞÅCAT(ÂÞÅCAT(ÂîÓ[1].native_code, stre), repr)))(ÄÔÔç(__ÄÊIMPORTS__, MOD(lambda ÂîÓ: ÂîÓ[0].is_relative_to(moon_dir))))),)))

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
TP_CACHE.update({'Libraries/Compiler/main.☾':strd('c$~didvDyv5&vJGVvWM!(xA?kj1=g>=R!|guxuS9*$5yD1V!?6gzv}$Ny$<T|KTKVi=;(dKT;=%Q@BRZ25p@hZG)h-oj>-Q=o924bY@>%K2DP3v<KO@$K9Qoot?*ThLnB4KJ2btq^^sjrOVxw)pggUmhbuf&~nK3AldQ;8MPf^SvLI7H>`B2ZEs9YZB9@>2|~9Q4MG>UMDaFhcgT9W6WSAW{c;z74Q~XL{T+YJFRcQF_t+Qg?%d2eEk>>&;lk`a_L%(x7-fCWhR+1;hh7k-uAdB%7`p@W-?7*5{VDqu9eBg7z(bnP*#k#>-)|$8->{d+Rn1r@v(~}m*A_WR#IyU3ZMV`eO9s24ZR65mlEiKhrLcH*CmQ5YoLS<;PuMr?3o1k#v-0$o-Xg>vd3k>jZMo5Kl%zR|POV-FhmaFQPITcX@iKBUyB;gLqys;-QtZ~qOT#$lvUeA*QS19B_r5~Wj31n5p17lZ&PwU!Df@(d?T}M2_#OKQ24eK6P2`G(886FSPKoMCL8qh1$+gIIA_#kg3(ohrLAbTEP1VY*pWJkTU<XY?{!DhNKixQS;e_5W>@0${shLq4;#Tuf6sw<FhV}%3Pt;Qj#Bcn-J^zXQfzGbHOY<lngw$HPVo5@1w^B;3J6uoUsvoiY>?NuYP6N#KL4vJqmv7uoy`h_@Vc0QbG*wa(2j&cUp0eMv7ht>mTXO>|nps=7lnhVd>HAUwxC1F8RVFPrwfs>E7LbNu8(GNpSz%q$>tRY+xw>A}3P_-}V$gdND#wvti|6jbDdZs(-!#m3(wGQogqdOR2@-TEh)DY0@o8azt-hDJ1Me66?jZ4kLSjKq-*aQs%fr3g?Ir2Z%a0NJ4kyLUr-_PKIWs?hVR>bCW_it>TV9yC0(&^AOAEMCZ+b(n+I9cmjL{+f*F4MjtQNzBRl0J^nBf)$RvG4Ao~N4Wv|0k=DPw#_i7>ygOwWQ0XEzJOD_HBGz`vjH?~mD^r9~E|u57hr&t<=;L>V4MfTWGXTbA^0t4&0_<kP_EHpKe3&<c;BZ>g3FU$@5*1BNXzqP<ZEGUeRN+{Fc+_8|fD1U9>}vc9&yI@5J8&a7SB$Oe%g(kn>}$D8`8z3Ct?p7)Y?urESF^^CQoQ@N1Nt=sBOU|0kS+DG{SSd6<sn?y08J_jvDK!M47?1fzoCB)z8Z<;r&uf#WW-8aUKDjO#Y3S0+QA>7<Ctx;TXl!wC~e!(bpvvCQfm{tXveoK=ILO)5pJmd+a3C8g6S8Zash>~2lqcKvu1As}vr_(1hTY;wQv9!AqaB9M!#i)RHf+4`fftN?SA*ca2-(jD#Pet;@ET&O}FiQZcBYtHC!cc@dXy-=a;txrbarZ9lORL_LP7zZ0SaEd-m6IGEYyEDV*~B@?qdYaWX{vw9#wS(uQ8Tat4is|7Nlx%g4YErVVOW207A=XGox8e9>68P%&~Zyvz_02Rd*3M$2JS}_ehOjuxjjw?#`&k={L`Qjxm2G2kfjaqgsNLdbIeTJU2NkKzGcr51O1cTrHc-^yfR;|T=<$V0Z<tNl<dg7V$)(p)gx@emi5mAIYNMD%?T<26cqS(@V7q_=@2Lc$75fyS6p3>*_}?1<Y_dtX#*2w_0#Xz;sj$i%gKi@`GKBP8PB>N15f}@{QZB>6VLu&YG_>z)c6M;!Gw0nH0(j8*XL0*3}i{BA*4*$>s^;;tCl|qy;P#{G{gih)&3c*l3oBHk=$^|E+&kPQzjZ(bKT9t9l%@AN9eBUEyRlhcmzl_4e)jY0@QX}2!u(eL)4w6aDajme*7ec5_2as$xG>J4~5)q6-8r|@nMC8I8e(QjlwvfJzGy!&d?eqBYHzjvya#__MWm|LE%s%#uO{k=wZf+&d!rYvB-Cbndb{LUQfL^Q-)j=@edq%-BOS}hwQgWL+VmVyoefm#(4kja;3Dg?Jy2`;Mz)(Jj+vW1Q`wLSJC?blRS9*x&_c&-KrL|yX-EmtX`s~$0KxBJrPkCVW4-LWBf1Km&cCqqkX@WTIJPQKRI!FD~eB#_Va!cUysW$t%Kc(Lh((xlV2`2ZHl}ogAujFZuO5-DYr*V8z}lc4k<-d+fl|I><mX0XD%jD8)or}cVHB*XnudCTK72nCb<OHACVp$0y-`nE6G}Zf0zV(t3%#7^RrSt0BgsYk2?U&L2DhFa@cB)ZPIat_prN=f3WND5>9TdiVfgNVvB4<WhXF@_RjPy)eTW$h?~o}!cWJlBkN_mZ1ifQ2`X!N_s6bU4pGXaPy?z(N>)_}c*B*o?$YvtySlJw!eTz#;QjTR8!x~Gxji6yzsbKSc>F=6dmo~M2y6Xt%kyub=Xt>(ibaB;7nj!7-9-?%5{ZjmEQTbc==P&5PttwV_wYu~)`HeNUDGV#V8OM814T+C9~pCcdt8Lli4Q)1Lc|F@_(}(64~xc`bh1Z~b6!y1^?fEMZ}x$54Kg?2BVg-5f*$SUwq4E0VtqL`s$_E^2{2u6CrNO^Dt2P+RZXVy;5Spq9i@{Oin2>v6ny@gXL=4btTIs<GqU{*(~(?KCQ_Hg6d$7O-qhB{)QlWl5&;*LQLiUlka`;;@peClpzGSUU88G);@W;QXEp3qw%(L8I8}#STj<&ia@57(CLy9gZ8A^y>k2Ui(3T{*#(-dAUew86G^UMCxa$qjo>hZ7ilf|(GtqNykO@CEP^NEb&kskr==y%vEZxY<vNt%(F%Pj9`r{9AxS04Rf_==M9j;7S&lFb)JDeg8wL}Zm6_leS7Dco0U>?bG1?N&8&oDgRXWuGZ#GA-L;+u6;TbuXQ%-asz<lxtL>jF}s24NCR@p>#Do#Xig;l_ErD&2_*L_XeUDppSR>-10*l7nL#%Y1T<Cn^a3KnST)w3`aw$+?DQa5L3qv*a8^e39=FA)GI!LUInCBY`kRQpQxEr?6ZuO(pWk5%3hFWGDZ5mIv^4-ZI~Hh#td+)cz(94-X+b*t)9#j~fwZ@3?SN#A->2mpw3kz#j1Z{3%j|e>@ycTD8iFmlO{Ryw)p&wMXo638__K?S>f0Hsh4T>o0qAlgD8(rFqNdnn10Fb)Rvhs8|!(RZ>D(y(2N9JokwXnI@-@-BGn2l9yK{@x6gL4D~!>pHR!2fgIYi^$}2K4UK5$kk@{-cX+im<=1lDSiYe>e0^ovCgP@rAviK%gFUEMHR2YFP9{f)GB2W)@QD%$4h(=o3B@<|*o`>_mc&Fjcni6nu@Bk5r90T<9GN<vj1>a{RdNHWwvmgdZl*@z8AiVk0{AUU)r3}?7;98J)M}Gv8lrrW9Z|lXzjVV5FdlkQ4CC7}eUwURj93(h@MjyUG%kP6wB#|xAx{@vAlN`Ss>dqL;q;ry`X<?`Tl1dK9rhQaT~u!*a^Lt@(Lv<?YU^5+)8IL!pdpi#J+8<de-20hWAxK6=|>o+&T!3Jw!?f9ZnUCU%zmmht@fEX@Gz$+)1R*fpC(9M;oPVZ!BIf$qmf+om_b#HCRSYKci4B@0~H^k|KoED$8&4o(OtMEd5otx+d#1i=2raB8CU9$=d|_XaT?DgsWA}^KhVrmLo*u?&LI0uZyIekGw_t(f9S`1W;in&|I^xEd27ZYdk{vI*YW_24|HaOE3*%)$yD-_XmKe9&x`_&x@cy%Rr|2VUo_U-(Voz6tlfooWiON(oegRgdD1F%E6Z~thn7}|M|@qWuVvNyT-2&xoYi=nxVDU@EvEvn3(3T+&W!lHxqXBMd2?UMo*3T-fvZxPg+nTxTEq=CfPTn{H9R#@+-XBZ`!7}iRVD'),'Libraries/cache.☾':strd('c$~dfO>5gg5WVYH?9IDDh$tWZF!&H+hm;l?k{${{2-%Vn5y>`|Y#d4t33e&{fE1cidI*HlTWQl2dMHVI*gw|U)ymqnh3%$L9irXw)7zQRyr(omCyvp&)7bYqWlckHxt@<~J7@-pZDV>)-_SE1(P#7%{5_|q^treX#eG1^{5f`EI-oDMb~eRx1Rx?%VhklIP=Mg<b6|#ZU<NZWuj!?X!P83A(UYeHz&Q32CrLVKo%d_lT+Aq7b5~j~lHElM_TvxSkubMayjg_5C1F-o{8ABqMZzqr_~jz}l7ul;{E9_Hpjvx?O_M;1rX>$a!wExaNEZ0wB`ng_sWKVo^d0?%$`zEtjkMD^+d=mY+ip6MXWK<oWJDGC2=^qS#{L0h0uwCGAOr<5YPJ$YkLej5=1H)t<0airQ%PcgdpWy8&9cJNauGPkb(Iu!g?|YA`6D8MUfxKh0N%;I)VYa-VQ`H-FTs6X6i9L^C6Sa$M~9PaV?q_Qk{tTd`Y@fFAn~F(=0=*CWx}RT(;D1mHiFPgod%~ja#P3Ak>9S+Bl@0xgeB10t!8*w*>J+xlWL8-Z8(b<IrlUdo6E%5+r6Z}`2A|8#pKv)#cD<=>nJ*KvEODh&FlFA8=lcC`h_5;=^}ap>njKwL2NtqxD|F2k01|9Mf3u%udQ#^s`s{8O9(0Ss413EXi-xv!Bi|^6<+VEHSZiliCmMTfs;DPEA69TY|LjU7ZAIBOFlp}3;SHd7r5xKYnB!<ynYZTF;R~Y;y-~m@!hCnUy|)j#nbyY@$jk&TgE4#H(?Xp5&psuc(I?M*lF$3|EpmT4Mzu&m?ic?aOgyJ*I}OUp^UN(mvJTDcQPqg+HN;$XM(P@!<OTwpOUvs_Y3LjYt8_6Q0AmFKK>IFAT%xS$PxWbf8yQL)O5+`ET-?Q5Ux!;s%cz>*f07?6&(KrTbgaNz*@Cx*B);@+<vqJ*0vY6>R^AEF_qHOOS<^Sj>qz>N^*+)H-0jN(>z(k&q974%S$P#b^QShOBX)'),'Libraries/text_format.☾':strd('c$~!=Yi|=*_IrNC)k<jYgb5uxq>yyoZVO!@ZM&&}YAe~6<;NuP;@DZ+*_f6}5aNWES3*KcT1uPp=mVNv0Y#-HMdJQ|{)Wyk*q^ZHocoxE$AR=qLFT^CJ@0$Y8LHDWjb@uQy#X#Z#S`&;xmcd^*jR?~T5-BmDKfDrZaZucR#(J%=*ZsHF(&54ZL!9=I4}MyHt`6Z<#@oh9j4AFoYY6E6A0u-vBJd}aZTJeSI&zqu?jcb6d#M9xE$KF9rry_GY$iQtKyN(yjsg+DVxiyY@7X=rQGy>IZycT9yDzD14J)~kKZ|Vgoml;g~C*Ia;gTuw%05aY`Vy-!rXMZ*0hmE&W|AB1m$mUa@Wqfd7KtqAnO-8buYFdmB)iParn)*c*@3^0X|W!R|;OMTxfa!YT=2dx3Aooo~hP6&X3`QmFuKRxm=dNHkQj(_P&ySg&OnEDfd)%cz=G>o<5b$b=(yE(s_%BB;a+g(=L>!ip>~wivz?xEqid^YqrJqFn-LTL(OT#hma2uk9Z$?_bBJX4p8yIhYo^j&6XS%p}>)ny6K=Sx5Zh4SZTDI)#*4yCG(EMPG&~jG1kepYSpsG|K6y3Fvo^Kuz9wZS^nue7U=*T2JWH~eZ_f)Af6G|#Rl)dMeJ2LMUwB}t+i_1BaXg3ez-@$=EV)sJ@oqVK%)qby{|P>tG2n7t6Ng<7R2Wu(WS8FT?7q2B|G0L6;zrEx3&R5*ou(6F@*jU6?#)FiN_o`hfFKhYB32pfH~~99cdn0Qd1*jM_?OEkupOrgp8$Qs0wk#K%+JWEzTy6tb@S=agiv$CeCDBn`>$UmV^)_C6CyzZA)1^2R)oX*(1>d6>ox(Iuro<x_C?ouZ#b1+0doyV%r`YVDLxI-cT9_SSnSLo4_>n{%jgG3iQgRbBK&Wl>pc*lVK?dGX^&+y8tT+I~Bkl&f9qf7zx@n7$QC|T`umC8&VD%O4<6B8`+^$K4K`nmp8rkY_qOZNZsu)Qt5$#zl2PXxI9y=aAMk`67iC1&t)uTDfmw^fP?0B)N>kpltApbKFIkc<uz-`UX!-Gh`&@)tFc#=sFwmZYq|*!h3jQ;hICxrFvMzhAbO$<MLv}30|k_YKnyCD^d5D4Pomae;8{Ajho#M71V&I%n7H`TOQF>Sv=XoiBV*vvF1YrwSmb{#g6e^^_q6<TALZV4U3cO@dDv4uZ@82qUoS6l>^>UNGAc2b5qBLn1^+7fhaO|CHPVWs`i{&4#!JIjs$oc+W7QTDcS9%Uw4?6tZ2}#QcpC$Bst4#4X_PVW2nw{j-e{B61!v^8ec+J2dWC1f0)X9sU8Bidc#Q@T=ujMHl&)T&#$*B$(G$tx54HI8>FbAjjLNvyz+!A;N{dlb3Yk$F%qX3YxCyC3y=u^E7t1G_TzaGL0_h`ta;{fB>Fpng(~QT__>*vx9$-*zyBk|G9#FbE=^*=ig|IKbYxl9vz+!q&yqaKgiVa%*B3!wvL?3csM&V%<X*0UPqe_F=X%?kyR;*X#aQqz}Sqq;+CrUecKtF2c@#d^Yo!C720=o|j06FbImY|>Xa-4_D=Vc7AAg)5tf6dsXl(fwwz5+c(3}5}GVCSCQ{}n1VIt2q~Vlrd7BksuP1iU|`>SQKNNJxu9mq!HA)h@sHc|wsWCyPKR@Nh$iSH)GWgB0zibhH}|>~(O9nA!=EgqCkg3JVPes7Mq9+{djf#F~5KVxbj?<D=F@!XSreM3J`98+<0d<CcGE)4%kUf9Ym!Hto8j{-s;~rQ80cJC?0drmON59#4FQ5AEUs26~bnK2)1*5L{dS+64>A3D2Ci6zW}@qWiUF%V3AWPohg4hr1;p=@}0pb|HTnzF_V7S6&OQ%xk6WYXE@JX7~XzkkbxRObP}24tpQb<#kfR6u53kRNz@4=LNU(_sz(r{N^N)Q_mag;5)w#!CeU%wzMOOen$a}#oUPrOcFF{d-|n8s81mgN~=f?Zc5amH^$$4p~M%Aw<l3DNQ@Z~5DUQY&WH`M5M_lU+bd%-hK<Y-od5{UNt!zhB&o5eHb_oFu?4mKq@szqh{+S&Q~twoc6W<%^AAUPcU;DubIsyRpMrt5!%F6$>#&*3eh87^vKTFKt5J^guGkLVu*8rGf`E!`$P990cn*&CV@wdR0S(Y-3iyonS-`0ZAd3zTD+FkW6+6g`^&=MJLVdPh)kHI4Is?&BD?{(|MX@Fmi;UZw%Ew%qD&a{BlrgsnHL&FINZjMGDx6A%uq*?3PTQD=oE494>3&zmWfPP-$gCZBrQD|qEa);Ll$z$fx(|T0Y!wP?UIu)MvCnAF?_iu(r<b)l86hf3m<M1QQBv~68(UM2xk9;7@nUvX$)sG@luN-c8r(?ynTkRn9BEh+lW?^)ni{eC1RdmlJ9Kfo+OEYfHD0`&p@*-pCS=i>amm(>WUym|RaP(Y1~~liap?rg+*rSP9Ap7DZv?YrE|(otax*0gLRlUK>hd~{w53cZrpXz6FgRGLmfI#8g-|0XHiA+GaT)AbgWi3IVq=G?tXNe{&Wc3}Rk6J%TROTTexOlTjeb<^6V={V?Nil0Q0+t2K2q&tN7fA=P?UzfhvGCrUQ#=LGCO{znJcs|cV1R|el~lan6>k2ZQHDEtMg~fo_VwORISaMwX>$TY<df(x1#oMnVBo(P_}4(S=^!aDq(S!sJu)(ku}mUO>fimzEZs{Gq)9*yJdQ}P4ABBeQkQ*nBGklzkI6NTdLhq?YfR{RQs)JztL3+HNK(R&s4jGiu>F09e??>fA5wombj&Z2mR}-{`F7%^-cfb1OMT}XWM>v_1P1@d)4o5_}yi{`<dTe@w-?2?wa3SS4EaeDQ$WOp8eu?KQY5$zk6K|$}jufYi4D?nNIuNPtEj*-~HSSMokZn-Y|orIeNg%mCW2hfAJ$T82$CMzp&(=yCJrIUC=e5gB8;=b)th4x_0#PsOc3=uWWi1)ALNvoIT*0xzhhWU%3Lm>+oBF-(~o1z;6?NU;ehX49z<HR^bQfiv3|I3<m2Dl}yO7&?^=^<oCj5kVrH>#*RRMK@qERB0H5uo)dY8-LZ)ftci(Xba<AN&42Kr|HUIq#>a=o-%gH?-|7vIar$U%IxTau`0imj9pAm5re8n$kJ$W3V(cB1a8)I5SzHiLIJuT}j#Y+JEMe)IUJ9FBD3#Dfo(p2TUzzt}PyHt`JD{2XC1@MO@Ky1pYQKgMQf8j*=E)!hh2RsitU3cB2a}<U4(78RnZ0_QvNzLKek9mDQ*5<lu6<m6SE7U|$nTG1-qt=j<MkxIM|fvnp-?YQdxb)DyL39enQ}yt^cO71w<a@I+D%(AAmp)<ifwpKuJ#}*-CMsy>UF+FkBl^;5jzYck}qB`A6i0?r0(1dZ??_F8|t%IvIGO(Vq^y@zBd-0cJ@`<-gJw{ZQ0t>!oRwLova-W12b^?-7TE~1Uq!~(L{RTz1Sta-~3*BWjxgBhwclYy0}YJH+O;R8@~(HH<D3Z6%Tq*wUjg?CgenmG1@)`@P8Qm7>;+7{&PYkAC;juG+&D^`f1Dwy;-I^{DiI^Vk+BcG8JUzktI~rBmSMRL;s^dr@{Jbuq=++1BC+mwbu_HF1-2PJL5->A1f62WUWzxXcTpuTk^Xt1m3bka}*lG6ty&i86!+!Lt`wRz!)1nF3WLQkDGGb)Z>;MOL($|ZRuh*&6OG*EVec}G=gLWM)0q}2(lK16ZFjNTrfSS=jGRan3WxQqfU|VQr(xdVGe`DVJr70eD=j-3DdMcn#Nn9`hxsIM0-LG*NWy<8b*R@SUc!CoB?IT9nk16)@`rVF0}D${zRiWU2Jou@LB<-B~bw&@&s7k<fMh6gzL&uaAa}LgFm<oF)3DZN6^&#wRuaqYX#lptD!OGntuY|tW~TPD-4DuugThTUhUr=1036RaJ0F4d&&bx+iJ7+RJA_IPBvz(3Y#m|+pJN?QInNso0ES+&zVX)Y*?nqx@=yg_flR83dF5{HvI2z`{&Mi#TEcBwi?w+u~i`|^v5z@3LV1K_=OIY<2Q}KnctRwcy>S7Q;7ra-J@33r<@{ivzV)wa`keqUdh#w)g?%QsX`OpkM^cTl}eEePFv5}!g@E9cef$&64+9kMIVrIciI95pR0FXd>aS>SYIq!JM7*W_vY?4$V>hY;;sKU'),'Libraries/Compiler/to_ast.☾':strd('c$~djZEw`b9e<xs;d^D9EYWVR(y2(RYe-UhY9NRt(n%q*9PcEt*tK2T3ma9H2njh#bTkhTa@V6Jpj?4)>0MP_p}mI}BlT@RL-!N#5&HknjK^cI_u&HS3gKDL%>Vh}H?uM52EBWE=2wPg;pn4_m#44HT9%=Q<VNVmB#iWuwp{lY?RsRGB~8~&_@6Hxo0zyTHGO_;YQ`F$njE_X+ZeT9PvT0s3C8U8^ko>&pRFtm8QqvJhjwG6X2*6B(>xJetevZB__V^nxHvt5gzwYmbOTl&(gV6yy>MmhqG`}u^pEs~p}%?baQkX=v|RrAn@9WK>PS@19Bh1;Og((@A?J8VAJE;B_Dhh1m?mdwIesI<7oUvK4&66Q<6;$tFX&@K$A!q_qs$xP#qB%K{<9uAp&Q_kv6>B=DF>Je2I7DVvmAQTZP>0i5M5lDrK=Jfs*xov_ANV#4KUF@{VV-}J--vruf_A5l6J!mJu6!A!?=pOOIjSd4XaMP<#@$%y(M3~Uh+eSSWC@%9i)t%l`6A&Nvka`TY()$B&?SCHz0PyVj9FDA<4QkXMp1$=ri-&kOrSVa-k87Vd>4jT7;zGUnjuOj#fy-d72|jG1xHiDMTy=VBKyk)@-!t3Eew~&m(%@kO9x%&zBdHc!qa+tSjGO#VdMZ&@~9(zvaoX5MQIm^m`fLxNm&!ieXerK;^f;WB%Ny+wA#0U5D(s3cfT2Yc3^hdO$y=_azlwgC%Av-bies!y^*gaU9CD9!&&=aYY%Ill+{RoHE{r1bu&@B!o8cBYYxM<T2h{jG94T%gcN~4u)8c?n_y7YZ~DF&D=y~L6xgw;u|RnWH$XyW&=jNpkC4@CeP1ZsHUOUB>=cu?ovTm@+ia)(EOBs!xVz2WDIVZ4Q=O|>n&?MV<Vl@i^J7)HxN%VD1D6|_TF9MQ<AQ!Zp|l^W_vZwjq+QvbVCw1Lr=Tpdn8o?Y^$)4@39cjO?srL1xwee<s40rC0Q{-MrN~<nb=5|sTmTe8G@c(D=AyxtC~R4|Jqre3&#dMF%`-qJeY7_Hei%s8HHdOU3kkJ$f!x`suf}lO0j-*u3RoJl|QHuIa-t>TYo2ZV&-|LdPL+MIZ!x&RisV2lh!m8S&gY%FnWn=j#xQ)cgl!hM}}#zs{x(nlT<8h7{!$yo`d<-%w%b=>cJRytsoPGmkxKyB{e-Is+37%SZeZCs#F$#h7bv{kt%*jpvE+;z>nP6^}R@S8j~TTX}<So^{kP)ri9PD&WbOt*B45fI^lXjGv*U1eY;k(7VExqEh=!HK(iod7#Gb;>b$4Fd9?ixXy}Pu#N@ej8N{FAREwK5D85I(VE)>pe-Y0E@qBC)_3&GOT3@N%7n~c#p{};%ZukOSh2q3jvBgYUFZMrHdJ}(Es~S_yx^~_2?1s*Axu3jeL?7=?DU_7>%GACIW)x-x`K%Zkzh06K!B?(V0|1p>+P?e5su8CrsuI#TcpOMf@b6vRhJD*^M7o)xkSzHdD{gd+A8rC3!**;XFEdNi1H#T0X#8z*M%dYEZ|=aq-1j~8`(AE-Pnmyo6W-lJ2|J=pBDCk(7&)MynFjO9F?c1hahe)tH^JAX5TB?L!I!;L2ymP3GOC||@qUUJsPX+*s{Rjd6|&D{SzJwfCOSH$E{=S;*f4T23Su(YL!Z*S^q)o&%rIFo`9zv^YzyG|z-r&Qc`Dc3qkm`B<HtU>=_pLdsaN6hnvF#W%_0!?i?nzZn<QfqKj8KlmNh~t^B<71Ek}!T<j7I2{ng|4S5MlT+wINW_RHJtKOMG@evhU?yqH%G;i1(HXLcZl6yU!u2KYF2*a`9Z)B(Mjn;Pwg{?#^lkABX!skQI1cs@<Lk>dxeSn%=nlXRL%WR5td(h^0l8y4dJ6yp{GK2&W(%J^J4OET#(a5GSg@%@*cdG&*?4Qt8CQo+H{W-R?J@l;NA)=imYBhH8&1jMTu-LmF{zBGk`0xukz<{-vPI~V8UdT>gMjdH1Lf}YUhPFBS}d)?`U0!B%)!y#4|6kmfcFjfocLVWh1D-6{^6m}I7O>isQ-wnlZDxKxEORQ&OyQd-b5nZWiN_`W;qSA))PSl=OwiKuHnR=WdmDcg6DqQIzeu7$#J2IHx=4Cr)+Dhtn+_!MX4LHOk_`yfZ0&4MV#PWkIwrJtyW#~5pE4IUB5=Y%?KERHGioYBNfMa{2SO85$)2K#FJeam)ypkFK=(dUigyU|~3PRO<T*cxOgJI-)%y_oRfGeTT;8c72=J?pG&Rv~sgGs(KcTF~m_fSbt@Vj4i6^{y2&`Jxv=7(Hb9OT}Mo128c(ghX5!;*h5?w97KrcTM->}CFrrh|9dpV8NY-wE~#<@Z<~D))i>hSyY4dk!pr-1jI1z`LdAc3}`8&aX8cV!;9X>wFsEfz1J|<p-9tV!K|ih>uC=+2Ly83Z84EPP)Z>Ld1@idolrGdS=W(=&B>~dDw4l3<7l%=;)-N*O`y%u0xCphgc@!9XPU7dxGErvN4gYR4kW-vRRnlA&heA5dEfUM=OpUvwMfGsv=`NN@kk??*O90Z_*tFdP(tGC2du-FWINqa~BB7Vmx>w1Mrd5qmtHQVUH|Kvs0@^v;Ke3>VXh?PdxveJWs9N*6r@94blqo7an*KciVsl5nGP$^=_H~-qOS0_K)eYlaHW@@c|rd7zR!3kwzaE|4d6o7znmI`>l+<q8ilq-lTo!K+jX<yruU$dwA~B;B6~M@0053kD@#4eUIsbN@w;nrBjtxGQ3XkL*dzqsa`~>r|z>!=hy%H@Qds%Qq~<ft%gYdJCf%jN4^AK?jNG?E!lUY)yQ(}dVPS9pYM~I;#3A_teLs<m#<8ZkLfBNt}F=P`DN~c?Fe^n(`V@gEkpUHyx_?6N%o74<+!2KbPIc&(+tB^s1LpRTXUJT`a?oYh7Pk}2p!TLx>aDGRD4`jd?hNIAv+l4B5S=M?(>I&+$9a(Bz3uT>}XM0i;|W@f|y^bf3DdP-u*uv<mbA{Fa!h#Rqr~S0P$zL*w@BpX5Ulp-9y_&fq>u;w>v+i2^vH4uO_U?kMS=aW-QB4{>s77`ETlAeLgVF{{gA80Ui'),'Libraries/Compiler/rewriters.☾':strd('c%0QdTay#Vx$pdn@zZoKvPu%iF>GZ|f|orGbudtX>*UmWYid?IyQr*{RHIoeUQz)&UVH%?Sny)NKnOARIwp1;$Br*lx!>~_QpGRuPdMM#x9RTb8A--GoGk{8diwU=Z#^RHHTLGw<G&$Mgm(vDIC|vRi6|mrH(p;}iHBh=SnKwe<L;2qS`da5{uf>MA2{&*p(D@jKXg2rKeVv_Fbv{z{r3X))PvxjHy=3)_lr+Amv)gsoMutG-^+s8xqyg;0(OUe%RYh5ud{ozfovSj1}{GU+i3pS!u}HrgoMw*b_l!8K4F(|?BWvcX$Be(_j?IE3Ll-jk6p?;;`I1Pt|kB?>{V#r5nm}KBO3J6fSqOUvu|P7bl0wxWHm^WSJF<FM63N2A-%#bv2W?@t^oej*ZOLf4oKMUuMeU}=Y9|CDd=Q}*}Us8$w+%{@r5G?#B3k2?`nvJZFXi3mfmL9C~osIyT-ofpMR8}_w?$Ejis8NaItBAX_;U4EOB^n@FkkJQ^d-NbR(g1-@|M@d!qa1J1{oZFg9jEqMJXGgZ~V)y>U6D7Kme@5@cIT2hno(<)KS6+|31c&E&z+Y!Pmv$JMi7ZY~I6t}uvuD<%~35#leT?!){!42@1E@rvxDS^q5ilwF>cpT=CA7C~n<81W|lE$I#u+0&eRM2Wp5{NtR9p#IwCPZ)ijeJsd5d}*WAXzW9vs1hTAJRFGli(JIvUz%haY0qVfpHWt!4LQuk5R&W*68`Y;(O26)+<{Ir;t`i(nDN7~rU;9@LZP#aHW(L*jhL-46*m3~#s4R6>7|XN(TIPz1D|^vD`R#hIu~~*_c8Mr`v4{xix_02vb7Zs9F?dk-B#*wJsw2ELDKHTT{6nWZ%(UCDP|{{xOJ{B&a#W_s#X@r2b9RE@3CzX{&@4fPvLq1*Wcj!2Cj!c-rPO|*Q>Dq#b;~5-dfOX!PS6kPc7I7A5G5aVyzag#m=xB>{@+2emTj~xHm))&jX0&LbpDF>o0J@g12D7TYrV?Gq^s73l_ii1zdkOHU!V#gXiykj+=wcgpFov&wo7gi)Z)li<jGg5RRu^rf_h*CH2>brV@OY-6xg$GYq8I3u!+Ct#=I#N5#WVF91lkwNmh|CqK6)T328WNVYiQ%2js0$-d;KS#)mx0xV>mW40S-2_T(PQ~wqW<}gc(+7}w5?DQZRa*9cfl&lZ3)7W2VCEn+y7aNVnYGYsgjM3Ox9~j?;8_W5(p7kvoo*vrYqP2}|Xb*OqV0NboCvAG#T25OsY{!Enl#JlG1=s;4CTgFIQ=g4BMQXQdHZdzE(x@9}rn5O*Gb~tn@8TuwIs-knz?OeaI2(TM>K)D^XV{LxO+M`;Oj}YvAw4T$=$_(+4t7Y1Xsh9~kJ)WQ<8bCO_dlAzJ<%>E@oc8o&&&;Rb8VYmj<eh;7>k+_wKhB%zNgr6zFT)+<3;)``-**vB)Y~nt$8oa2D`-#db}{P9|~KRdmHP^Nl}~~PVXga*t3+)-gmUqT@n%+)&k34yju#`r)&pw<PQ%*Q#R!2JJslT@#yh`2Nn(-`Jcnb|M&2LV@F<CsIPWAgIwGkO(p>v^oJ54v50CH=#Ul}aD1Iz*Go32-788)gXuA1x%!i$=MzBBqqkqR$7>Xotu<pf;3eeGlC&46rwiJ=GmJ)qG>WtSx)szFxm}3ZC@k?!!~S4CoWc<$Dt<NSN6^+?W#4kkB16&!MGOFpguTOVIZuY&PCFq@wJdi`mQ>_=VBrvHLg)&St6CJSuUG*j@`zMpkN$Eq<ht!Hdz1ZB?f_yGW3L{^*#ie`Pry*zXAZ&b$AkdqxWngwRd8MtHvUk8h2-F1K@$cWCcrmBYC<e}Ob)W?CMl)5?Xcz@P_j6$1s`2PUIirl|7Ib=^B*Q7QEr;htpnsDL;c*m<71tsfGP3<)S4I|&^uqV*G)yh7o*he!L6?=B*;gk*b1tmDeSXq%Y*43Z@zycG^WRK7ulb=`oWcJ)*wtZpx73c;I4C}CgqH{Lkj7Lt9L@j@12shkxGDij|U|nL=K=5EbbWno^4W{)#z^wqAX6=lC0=luk<q&bXDaTAe1==*BhbX0|8BQ9M=_s3D~YlW<(RGhA6I-q2K%5l@;){C{GL$a?H!6^F<c*GoB#i1KC{#sJpbh$15vC@NH&Iv75JrDrbs$gWu+J9IUtFt|N%}cdQ-{21##)%*<Q*6aSE>Dn_VKT~IGdPhysJW}e!U%-7r9Bu<H?njz>LawUQCXfL6sABhpKoa}THAp;K#Wp_#|od@+ne*oyU7C5C@<K2f2)bnbAQ~8LbYmK?MSvH2V{B6nlSLEkq`FRVbbmjyOhQ_MNE<65s?w5N~Bi=w<BuF?1*iv!vu9at_#KxDqS77=vdsVW(qdhKXMq@&kbvO@8l=FM8ifs|IombuzwnO9FF}Q~~BhIo^XX#t&Iovmm`-UlOdqCLsELmv{Wqzb%C^S*hP1cj1M-_=oyA1O0f#Os_llGZCLFM8Yc9C>h^3iV7qFtefA#|eOqIkTd>FRhBlZ2Zv#TE7k^7H0DtvHV>3}C5lhld+80<9u$)A_wB?TjuPMld?>SJhc$mM(6J#D;+~9KG9{A*`7i*eaixPFQuQY9roKkG`m>fRkJb_=<*Y&P@W0yMneC<?lPAhh-z2XvJd!atklBuG^t>IKDFjDaW&R=JhC9({s2%3KLe%hQeJj+vNhxV|ItOyb@^PXY<K7rD&cLaVO1j;a!X;WIy9$;FA=glfL4A#UP=;VF!Ds;%;XpkXk0d>{qbb-vCPutST5K07iK#^onrKBa@Z2US}6`=9J!_8Alu0@M2^l7|g9grOC=hJBh&M`>U%W0rP0l?TABHmLM>obsSb&e9?MVdcTXtaEbF(kjEaPN<VV8ZE-*8=_p+|hQdGU3IAw<+7%BP4VO~KjdMEQ$tdX|E^P)AK-7~_hNcrcxEr;7B+Qp}dK<|uX98(^d()apG5kr{O0eEhdwme~2bclw^a{oj$#jU5iTnD3Bkpi9xeD8|h?KL;J?YV%XZK6YsV0N8hFk1QmDYcYXty7A`@g;kWk|%$^mpuYN)A!#kg0%nk|y0#W$}SvYu65I9x?geWEU#zkOYzMiL-za@nIf)tz=mpO-e5>4<*fAjASVm_fPclx^RkrlVun1uQbEpmvXVDjvk8vLs`7<<!P|GIUn0XV>0;E$$XCEJUzcC^7ADL&uZPsy#$b~PL{0yWXT$b951!X)qZ<`RT7ZOkOu-bO|&G)LQGEX5?@#(NntjV3%ofhTycsVm65v8oBQQlu%|LXq-sEj12a#OE4xkP1dR%RUD=y35FQ}ud&BorlZNlscKRlpO8uAf0?zBKX3W`wIa|h@B7p#AoGjWobN+b=(AbxuR}G?9b;rA0C8u;$hK`qCp^lrBz02MP=T|(>r&cw23IW}cX3H6FcHSzTR=W4Hn<vjS{w$7n())#qi@T(clWIYGZk|?+)brjG674(3LmzL3_d>hooEzBT$vzg+I%#{OV~3-z9D*2n?S{$l=+`@*j4KKDW1T+35K5G;pH1Rt)ZM<;RL5+zaOD1{bIMD|VeFN|<!R*5@c&IP5Y`-witwT$%_(?4R)l<$j3sSt+?>lLA~t63%OR~!w)`}Rs`oiL%oaq`fK(b9SavBMt`&VwH&lW?rA5k}GG(%o^!h6aIJQoQidyV8mMGuYvP!trjC8HML6u)yU+u<KRdem>)dC(*(#Zy>pivK_WF-bHstt}ypr|t~h*6%Xm&Zi(cTRKMm*E8Jcm-T^QK`{q69G5E0$hQ0{=hB~DVL47u@|tI%vBt*Iyh$x*CIfGP}j$-@$Y|3KeyItxf@gyNrTsf6}u{(#tZBQ=adU<TTEA$gfY-Ll2{bfDJH1A@|<r()zK^WVt=j9;7Bu2nJ78VQ_4zuO<gWDwW7BO4zAPc6=AB$R<l5!ZV5M!PdfS#--Ks<uuvhQ52XaQ*avK@CQj#lHpkce3V7b&k@4>5)>ph5O^74gW}d=~_-KjohIzQU(fa8;-<sA>S8PAaH4Sf*8TJ+|cNQ1B%-%6G3%M+vo(0A`?P0f(DCK|y-w`3kD0sTy-xs;k=|IO25n!z36W*gXMmA&&Cp?y?o9MOXEmUNSu%OF3BWbW5Y46C8JgRLpiHMwoFJ_brK8+qupU>PE#a!KvShDBX4J4*!a-a+)GNXMJt_xuy=>!m~q>~X(R|;7OYv=O=-awZc6>ON1!ghId>wVI!lzaBGCP?Gqu(PJ}q?jX}%oX<MYjzviBs{6`#+LFA8~gNKtnZc|y>Uf<N%UP?->ppP5hDh#J6Tfu6u>q+D^p_7Q+cwU0C>?*#FkUNBv1I@L=(ZNOG)`0*6R#Q>PX22w&_2Yfpq?2N`IZ$TLeUh>aYZ?<7Bu@2HX_Nu~-P_4^2H;ur;nG+|ku+!^nwAYJ!WuaP+8m9j_IgXf19~)qJ@{byt??GVx;ID&LCs`b2KBuNi4mzEfd{gJU9ftTzARF<X>s`oN_Wsdj&G8mkRjlxiA6aUip%Y*vf&4(3Msk{<|pC5;DVTvTMRN-io!K<4b+EZVYlo_&cA2XZa7=xZ{4D_@v0#&m{Jnyf~A=nnP*?2JQ?S%)`N4lf_@o|4P1*ONL|o!>a;fVSAjzGH~8D)skSH|nuG=|b$|uL<2&C+fwV)=Lse{a`JqVgp&;Q_W^|`@VBf;g5<Z#GeD_P6?dvurmcHxi9aJ>~dgWAXv8FnV=Ncy}&-ug26ora2Orao2#a3)j7sCxH87gKVMr1%fOQL_8_J9%S~KGi0}Y!ujaQGjKkd}g}`hsH|@m=Ups%=F8D{T+bF#YS&{O`!<>**0#^%cUtv66O+!?~m$EDTj+=T*B*$_@qd@)h>}&a&%|pFSmEtUPRg3fVr$;OM0IFtyp9s(mqFr|mg0K>t=QX~unfqp5Dt=IJ8>e~@lFB}nv@U=6F_lbR3wS2kb{x6G>#?VZLo-)bz+4Fw@+=bOs+um)VjmAR0dGjr*C*}Gy?vk%S7BSw2&b*Cv=vx|3@z_4l$bc{tA+{k)H}Ull4hi#ZM@adfAUTaorHEO3J|>Tgz1a8m~qA3B)Q~A==V6J5%ESDqbTRqA?9xFURu4A5Fh=Hv|!_=|LIZkNoX4mv1N3%YzDkn6hQCNE51x8dMgqc&Z`O=Yssi^8jZhY6KBKHqOs+lk&`;>f!5}_Nyzh{>vZ?Z)CG@R5t3gc0ET~ht)vQDT9Qy+A*I$vvpKz##~P87+yyM2ZX1^bHIi-{YoiDpF=0dTOFwnO3Nz=TUVFigkG8)rd0$m5BMVF1gFwq#aEUA2BK}&WSsIm__@z!Ps8|&cV7}3UcyJ1`CZxb5NiT<WIgQ)Xy&bJX0mW|CTUCVgyxw~<ZMjAt%lS_?mJ=)V@;E~}YLbpvOza^>JcXvDz6K--huO<2mg5fIyAOG~T0X@n>9mf&+%xe4NVobVfNW1y8&0)?dz*~mhVZ$g;i5XYq^TG#(HsgVY80BK*={F$k-E!tEXS2(I*ky8D*UbY5zB%_IYK~3^or^$_0(W0g|5uI8IPYw=RU;3>SFHMYE;3*OVo3K(vV~SDOm66TzyJ6%+JGG$1@#8J?N*^g<8Ie&N}vc{P%i5?X3;HtO+alUX3BA;?y0`67S3`c;A`XGx=Ls0;ouHc?B+`h<&eqodvJ}Bh7;0B`|+u*>^XGow`{Oy*E|p!r$Kz*;9@_gg-wDBYw#RpD&0uYXVLd7(dyIOI1}pTtTUCG@ws$1FDa9-(y=OC$Nyc{QOAMxF3U9<vtm;*V_t}f0DgE66k+^;Y5T#c@u#-JG}pe1t0`{+%ruz#}Edgc)P!7S6c?Uy+Ajf2++r$0MJzMRH15Zg=sQolp<1b7RNc~pXc)U;f?&K5yl8t@%M~EyCi>`x)N7HsivE>3TMoHs8`AI^M=|dG)w2aI-Vy2n@eSEQ8?5Xn5&JYaxP=y<f9~x|2P7-qxsw2GJsY-dV5b27X3`FzLSwu-%}eANt<Zlx2XJ%J7f`xuj-hV<fH<?0_PfdYW;u?{>+KgX8#AzxlWP'),'Libraries/Compiler/lambdas.☾':strd('c%02zS#J|b5Ps)Z3=gPhf@6&x5DJo|<=R685^?NHh%6uD#lj@kc*3y=Daitxg#{dvKsW*c1QJ)o!h*so>^}4_Nqzx8VY{l2>A4(Z5_Thjd#0<azOMedx~grHUZ9r;4u5av^U(U?z(D_@Bl)~ZoHKQoq>P_xBgI0kVOlAJ5R3iK<#z4e`(0oE?p=L{^LzUC?K;RtprZZzKvE52ZG7E7z}kb|nW0Ua%1*_g*Xgr-p<K?NIswCG=?%KfBp=c#`ZPyA&Ce_m@%S1ZXD5iYbCbdTsuhF$xStr+VMC5fJG=}2T*n)A{VsfO$_Xk<gZ5C$IMBZrUd+??^a|RVqvN@(Wo}hcnIQ}CvvCjUP5Q{#nKR@RZHwuEKK5dUiGK`r!cac*z5Dvij0JBvn9`^Vvgf+!IJ5Z1tQAfc%LRi@&_z1E(+EHFPjDPeoj>8^C+J=J+(cI$8_n8wFZYt+)EbU~s6Ns+mdQt?J<Afau+Ce`k?3b*c*FyZ0IV=v7K<PpjC1qd%T=UH=|a8k43|xMi9X4fol+hLT``4EXX!KgQTY@hyhQs<aY`s*uGMfb=&?9ncY<TK4IHn-I222KT1oD*m%usg@rXMLy$#1Jc%G|>pOqr4ozdF1PKF*vh8|9aFk5kJ)Lo}C;+`yc`P0X%jT4UBP>}pRpg5WxN_$2wXOPu<)5LdBWHuW3tkzC))EvEyj=Dzw1ddHzS-mv9dTC1dK$^C=52~JXvSS~ZCD;yTbV6YD(|q$iK{jwO*TgoHqOb|mUT{B5{mOvyEzzh|OAgVPrfqFLjI2zJtu)^qJ8Ii@WrtJjRjq>NO*XRRKXLy)WSV~A(0P*y36KnxHV5H3&gsYWGX2XJvn(|^p-pv(seu+g4Y9MaU(85illz6~@NKW$x<|sGB`Hu;qk*lpV^$rRF-@Pf*jFzsldL|tPkeq@)_Twb{+wEL0sPsP($(RH<9epuDNM~!!wH$uXt_>?bQ<>fG`zSnHL1u~RxRfXXxN=;kB8lvWFoRY?C*q%zWvYPVs~bp$T<JC$q4iHkED)3woSz^w-S5!ta0-At2R#m0RoAr%cJN@^TtZ^CJ()F5mmK{s#OB%?G;Y{mFC<^^KNLowiQ&XB3mUJPoxR@ggyl@Q}m|EU)-e^Me^p=ViPydZ98R)IZI8mR*cUFA*uKfRV}+_LS0$eHAlxnT|L<4hV5)y6DOy`IDMg!VQZ}jsV$=8xo;@Z^lF2=39(?rWqY>ymWV7lq{<bl802_WZba1*(K6|<d+cN%v{)3-w5%f4yFs$r96PdW4`I7wq<+?nq;)8-r*s|(1{wgil}~bP9g@2imir=>m(zWCFmM#?L}0A#>N4n}2(=UR4qY~_jfHh62G$_~3zi08xnCdFK^;~LIaX7?XkT=Eee?PMa<ob-ID0nd_~wnP1|ps~ya8p6&lnD6sXZtI8wN%9icC;G8{X~>fXC0QSrNsi=_C3#em-8aFoV76MGti!KPpZRci0^)ar*<ChoxM%CfUE=h^Um8F@lF@yiJ>BPhiG8theu>P^{n1ytF+W8)8tO2%xsL70<~P$5@pK##f%Q+=xk2ief-EW!M^(bAl^DZ6YjU{@$F6Nm?pW+Xe^8!0O^rxTQgiE&h?~7rQ)7BbL!+V2Q#GJxmeVvl*I_%*mMYb;TbA6<dL)!Y)oIk$7%VjZgHd?I(K98P6@`>sU?!+1}EtigW1`7H}YoZj-ic8@#8<Fq;vna;1VkR*w#MwLd5$2k|SuS(e3~>(b<XbDGNYDTC*8GxE|8E)*ZH83+R9m3|Eif#-n;K-1!LL43}%E-_H%whUe&9ZwQ;J~b2WK-(#5xU2|GGc5cmPRT$Y%WuAgH|J!U$NI#gBPX~r*+?_Kn_iBbL4vV>INc=t^A1^$a+0mKFdlaR#l*UO8+1g%%`2WQ?{vCHZ`H9+?v}tyUOl$Fxx_)=$QS8~TQ_5B2X$f1FEuCU#DUGP!L^GuaX49_ZYSLzyby#?$V*CSF+S)I^MM{92{`HC$gq<#(7gy6rj`$v!pW5(Tt+9?hOd%q!^LQA7$2x&V(BYE>S<=3Z?CK3^Md>ov|e0WQq*eK>4W%rT&D}|#?+vjm}ih$>skup<;Vp6Krfj*=jZ(?<J$rYiy($^6=oy991-6~iMu$&hI;@ZiEtWFg=7E-{F<z_orN~+VDM>SN552SVJuL+S|Phyj*@ICdZG9`eT}YXi>2R3$vDB64cw4{t;h`|YVp5LfnZw74T4(9#33u>F)$gj=_hj;?t9IF9a(*)tUgG#YASx_a@xtsgN^d9)+Z3jYgFZExc@*`LnHK_FQrh*;HcI@@}kH<qw~W@ngz9f!kP{1k&#K<szP{G*QqAYA5xf+!8ymWGGYyK<wKa}_yQMEU}};JFmosX2NcF$+~;@zcj1W@^f35WqY^+?v)7habSxw<bNniIVd5}BpVI|DZ2$uzQd)^33qoYk8j2EPBR8Q8D{I?8N5xoBdnjIivJ2y=K=vFx6tiyne)Oy8pz8L*RcEsZTKa;C_^aA6RHW%fz*Tr<kn9Y%!1wjtETe3MH}F%7CAwtFJ7{?b{=b;d0z)kGBj3jGgo8tkB+6(+=ESF6Rwd*i&y9Sa;%CDiONWU}n;D)^A}uB)<Um*cc)spBEbuX5nL`V0JB_t||L`@7wU=74=KuZ%DmKc0eKTp2GiQH3eQMNe!0(Mj-EF6g?hHFrgyI=`pU$M9#=S@X$f2So=0>=ty7Put#dfK;B3p%wYW1krcGcRUTD_`ORIRdVDSgEZfpR;5U!<ezP3#&~Pu6SIQZ;s!I$Q|h@c@{pZSbUD-HZNz0rU7FOa'),'Libraries/Compiler/expr.☾':strd('c%0=LZEqaK`FnoFe2I3(Sx!D1C~;+}wv$rSBR<*5r<1k1oY!#5a(CTZm+*~P!Nrs$jxP>wniq#Sfsjz85Q`WBNS$B8ee9?Fgg*1Sv%9nBy<iYkjKb{B%=66i{xW-*o~IvG=l_H~k3GHdW_5P%q~~EL3Vq*;&PI-l-U`~M>p>S27dZ}r|BJm-$Bw;TnVp`h%zHDH<5MR9iX;2;akf(f!84zpt-^EdrSig|LyP_rTJ&4(Mc-?87|<r&pijxfAq0O|QKaWxgmHi-CXqrvN@}AEY`UGAE%VthH9NMTh&Xn<g3E;MlSkdASLsu>eYWbIoSLp2ueAYnDOw;YTF%ie`V|i9@0?z&Bf3KWMSBw{XO@qsxg?)T5t^Jt&a)fWt~<yNx;}zqFVe?YEc5eRG$P-+L9^lGvWrf%TRs8G<u-Vz1uhCXFIZ5%XB7%8ZPE9$lF5@n%;Jyq+u=ApPp{DL=~n}JjhW1{;xbWOpq~q#Dpq#pigTj1N!RJe^r@UEHQJr`h*0QKJ46v`wopYF8~X#|1=amqcb#}TDIAVTnKDc`6~}nXE>{OH&ktUnHkX;yt^qeN^+)h1-$f_GWnaE<$#wmx9z~&czt<ErJpaykRx(ZRf7RIYN^*bMw*O^g&v<hGm~H=<v8SBeKc3L$QPAem1+4-<h;_5}?SbiL?pIWuHpGi`x90rx_=2-gstAj8(a?%5j~dcDT0pY{EWxVT0hVCZ>;Ov`AJP(DPWm->Z0XtBYv-(9yHngUeofVD<r-Rj;k@>{|4Xmcs<Zm<obum-ihV)7Hf0Mx?OspW0;_OrJO6uqJGGP57b2HWCl~fHsf1dEf`;MF;B1^Q*<{WJ!f;%QC?fzZagq~sm8wKmM5-D#*qRqh30%y&7^*DC`*2-N8gnt9;HUj8;T)i7xiKiQA&CA;OhakEQcw=b$g%=m$ClDr#Z^bok>8ATUI6uX{j8=zGkbJZy0KC5uknii1G<5s@A%|H__qd4>zlL3STFN{e$Q37MbAyP+L6%a9>KB&bJ`uR|D@*y4(q_gnt)BUIvgEqNbeg6`QiiB)^L`1#|lo%0z2n2J|}3hW;(TJ5TVe;We5!=p=@nPLLUw!)Su*#EA%qGs^NGKiU}SWQ4l4_bhDGvm}FB0zUutvv6Cv$l9snt@=e==?b%l_pJwF0^W5eW`q6UO5-MI3w+x+n7)jHYo_xhci|LyN<?ViH)<vVb!M;QvT07Ea(T)@Zv&b^qOXXNBtd?!MsKulO((chq;`A#-w*E}!qWgCNkSt^}A+rvls7*%58}l9{lNKRak7=}9QM0w|XL9KZ^zBb1i#*10Y|x=+ahwkQ`k6yID06<wrk1&-&>#4?!pE!h3760c{eo_*Q|6?x43@z`GyCq_&A>-?8nY;bXt*ReX;v_Hg~d`5#>z-Uic&ArsNPycSo$!VnFmMVlPTo9r0jqGH7h9-8>%G6(X{c({_ND1>Ya|?T9hIKyjIv)sRb~0+8s;^#OEZ^>>llIO*7qUH$q2H+2UP>XN?h7&!$}cZ*&hU$8Hj)2pPw&Ntb7FYz%^!2nY=zGV;AfJqVI<Vb4_|R|N-cba8ah@y^tw)Bp0*{^~~m=53>DjS1}0b*xfL4)}I|b-n-agMr|TvJ5!yvF@&A0rRrJ7X1fLDGX~0xtk`IxH7@UqR|v^>lRdiiJ!AXeRV_G>>}w3J-W(msz)!#@w^(<0mXL90DXzxvfqDRqT59yG$;8K+l^~UUPT4Z&ft#8aPkseZi|=otO2yG?>>1SDdm=Q33;ql!iBZ?sg%hbK5nr4TWQoIr>y$pP5?0?c#mJbn;vjejyvh}m`$QLd1~Tn2<$iWLHZJY{|o5sF*`1jr-b%X!osJ3Uc$f-zCZ{^c74x3+X-QUr0)C^RY9yuSsZN2x-(;ax4|p!4MCQ?EEg#Ou*O6RR63&bRUVB62-7Cp#x&YpURr9N#R>hXV8Q3&gd!@+f5zEVY~XdE%44t&NsWUPYH!*8>74eKtqp2#Njkv^dP>b!*9U_bb<Iyj37f|QYh9<m{{GC=Nk>~XF)9$VRNN722N8~Ok5mOUUz;$>7)BKnKP07;V6_NkOpfZ|TYlt)Z+9JQB;eNuLZ6~s2ttwaO&gUoG7md~YB`CkM<3u3fR107A&VXXjAy|`VW^^ypqU*yFAx2Bhvf%oeLg%exhlg1a*~#sC9Rq(2N8J&k~cWP6c*13Vfyk7;`swn@a^jgOpRG5fLJrg{C^Qn^L2w_J~?OVi=@aJd1{kSx&o2Ln}{@~Jw3kx^WnZE_a3<M!yShtb!HM{3GPFRGVjR!ZHBUsm;dH)FsdsSv1D9UxX3xxs-K2NBx;M?i`pGOtVdu}hr1If2qq7Ae-Gm0Lnz)t_U53&ND~_b@GpeZ15N?a9j;1YH0MJ)t^v(8-NKt+kZ<PYFc#Sg<}lr3v2Yn@*oH2hb<{K!CUQ@M<n#!-L}_HIlY^yR_<p)q5$ILwZ6vBPWfj`AlsSq9V>t{N;ayW59Q+UZ4rM6{A&K`t+;UW-&!d6P=3ZKrLNu%NF5}8_>67~Se)*2q?f4Bx^_1!ZyyzFWaT{oR^kNaTXWsRm-Pqhn!v38;qPO#)0kQhxFDL;9)Q=u`-j5N@aCKRKWKdI=Rx;GaNJw0J_vnsv-~0H8=9sWDRX}k<ZE)8m+-Gv!lH)cWgf`~FMWf;blUs>j5)Kerp`}LB4fIW%){nl!%<+sFqk9%NMq@4-BgSl=9FzPg<r+e|LqB32gk*wU^knn~ygZlmjMGdxO3_?_|31TpETGSKB|U^3z}29XwrpFs=x*NcT(n+6&cvEh6qVVQ*K+YNPOy$wm+5YP$MDGdOD1bGk^6Hd_Q$T)AY`6l{lrY>HmxCTjLFi;-rxvIQc*7sl7Qe010T(Sytgl8ISVNzV{|z^=BUyXIa+m*o@|C}MMCyi#qnSMS`YI$-nGy@jB6(Cwgk3{8<V=?x8CV&O456Byro9$&>v<_%{j98_!x_-W7qhU@a)F=H;yVt9>s+T`5$}Oc98'),'Libraries/Compiler/tree_txt.☾':strd('c$|$?-D?v;5P#2Kv2VLu&(PSnK!h|2HJCP~A0VXRxb!y7(d#ALZSX;S=m#RjD)d9ds#v5}tQ4gpMeNi3C;lbQ?(OB88mf6nHZ#AS`OVC4mcbTm&(7atwyjRp>Dl_+f^9P@Lm{X|R{U<u@gv49LMg}Z7*{Npr)u@dVr||o)hfjqyrBc#uPEf;5}viWK8xqZ?OZdHaYdVi;$i4XVMj8wy}%WLRJRXc7k=@4hTz9*6WXIB=t|-RByna%>{Xvo$bOi*w4Eizu=GZ@*BEbFWXO<fl3OIF*fG}gNxnc5^5Y!Q$__{H624w@<(f%F<w}iV0JP}D?QTf$#&dW*M0Z8Vh*4FgjQTBmr7t7O(-Km;z88py#SxG|R$`h)GbV`ESFk>kWaoeRB^*8UZonDrX__0b2QN(gE3`DVstRownI>Y-JkEz;ovhRAiNIw^)HcC>77C<FgdYi$tP%O%vQU_Fc*dsdWd`eT3YQj%a~Blj(&8LrISctedaPL<z`6dtgiVXgbOXV8e0K}>;T`Owa~<Bmw}Ni>1xm-Tu!w^B&RWZL41;`9wh<I1OH!-Z1U!Hp9njGE0Ne1>MB}=pS`FOrXbv~QNT|yH9_(PE$s(YQV&?Q8Cb@t!*1`2!3N)oiNJq+WuupdqG@f%;&f`~SJ%O{Hh-ZC$G4#ecu4}ja?(%AMebZPZolxp&CoMC8d@5wAW{N^ylax4tJ8)>NYG2D=wL8LbsZj`nCvdFgxdF%Uku6R=uuF55;zETnI!V=ry@xNbs~`>49y&(j_M(gae)>s4Mg!4in3nSK)_rFxKiW%r*T-Ucv62y9E}0wl3t8#4!W1VexUOEmZTM%DZnoep{D2dq2DJ*D--I8))GKpW*MA7ROfRRdQVWW~CQ><#A628U9XK-08}z*`!yeOpkJ73~%m+2YmJ6!5bi5dJA?ypDVQn7;B?5eI9l3^&ZS;?6EBp<$N%MFd!snQqE`k369rJ4v'),'Libraries/Compiler/tree.☾':strd('c$|e)&1(}u6u;-M7*9J>){vyP&>W(PADA}5_7;{Q?M`%I-CcGjkUd(&Lko&+g(@Nx>D7ax2N6BIf6O<tJG+~-!GVM~Z{Fwc_uf)?1t*jJN0f6dJ>H#+pB`{dohbGNS6L#Y<C14#d^igwWiD|XhX1*Be=vAB8sF=W_WAwMu)l|XCft*uwk(}cHtO*N<>}qF*J$`+u66I>41V)K^5?PQQZ43lYPIO|8m?Wk1y}G6PFc4>@C4}g5-#B<&0q2I2|g5$)&O6~on9Hgsj6pvQlS=UWK<%&5%3Dm;rnX9C{`wDSsVLLz%sFM4I<-R`PA%lk-#yQ@PnF4zR_^@;?SRI<yScGZo<jDR`{^0I%ZHXYAi?!a*!@WgZeWixHTf(9<hmZh_~>$OKjr8rb^wM2a#{hmzzpjx;7NUvr01j!Iv}mTjLkavl^`xXvkeQZF#o>Hjh&hxFknayIjMiPMl3;7#s=OcFA5G3FfWM#1}Y$Ull}Tr$+*Uv1lC-D^CND<#lWxoq{<7t?5*y8BgK_f3ntOlE%xdr%Q6t<*4@nH$oJ(nUT|ZcgKSpq#whD9!hg<qO+4Y8r0mc*x9OhY|&&Qfi(T+yc-om@=}Q$1-_6brCvx%!=huet}TXuYjwJ&ZF_co2g4C<Gp(_dg*MwdQzekA<(3o+`$a&d?yI`dt*|MYNkL`~TZef#SZPh)DM?0GDb!4<wEXgPY&ewLHMv!9WE&gVE*sHXisWn@I2_$K@Ua{@y&9$I3hl;@HEu!TAC~tP&;'),'Libraries/Compiler/node_types.☾':strd('c$}?R-A)@v6u##v=5A+FHwC0Bl_f3+(59+`Q4*v`1g#c(O|1H_>!r0+RSJ{<O(6mns6ikwE;I-fsZ~{_5eXMZ>P_E*7buU=`CYHqvx`NGl+5nVIp2KeoNs5&I_H#&C^u8exaD%8it@!u*>O?E$~?7uFwDb?v4{7tX|k)&?~kP)JTgseRP5>Lg5Ceov||-b?r0>?bfG+D6{?sdkYNz|Kle_LVL~Q8?3;{6bM2aI=E_dda{miVxnjE3RKeC^2;0Ho;m=a(yMw8R=1^*6aFlv+urEfKrSGI!GncQS<N$lT0Vgnzjeq{!r0W=euTuD)o~)fiFbBWDKE4GFSc4xEs5)RgDN&oMT^TSCy`TnXurTl`UBgbGTf%UYBzqA3!>|BHYza&sufjIGr{=40u11v4NdRP1f5fetbe4@La(qR|?QfjCYcsx>n!kb9Sn+{b*oAFO=@5cG@NWs_&j?WWWjN<FZs!U!)u-YyTb2U|n(WW9-5IAOA5ZkMiZoyae&y^7R&gq8A(@3Fx|@ECtFD##(ovZqY(?q9dB21mp4&M%f@3^Yt|id@^sqvrk6(kAWaB10$Kv+(SOW1pc7TO=(1LBkI-Dn3jQBbmSeA?NqnER=g5iu{oRw7gTGBbN8m}VH>MYdZw=l_ymCXo>%XmUOoTMs226fERi_48?21`Cu2Ena-2*vTmL_kvFLJY6OYE5P(?inI;;s!f#Cbh|x+)HRp*c_eOf)}BwzDXtT;gJ;XBkW0FJsD3eiFjdt$Hvv(TGQ|st}$=Dky)+SnKnzGp$8{X3_U4c4~}odv{hC~rDpiGZc**9dK|C{&^(Q%x%&UmdoteJ+nc*%fBZ>TJTF(ay0Y_O@8|<-MhAA#8JL>d3QhIvV{TC0UIgAcPRpZm7KQcXxUWWR$gS2;Z?7l!zBXmWBEWk}L8#4xhESV?YIH*J9F=B@A$dxNpC#-`gyUCVTTZ8^th9b3(A3F;U9sFUZq-xL7j6`nU0uK;?hh7kKDu}}d%Zj4L*L)-bVdzdc5Aq(m*Q@8G+wk6m%EjsN4IrR&I36%wFi?T>J}?)JSE7Xa^~YYylvA)q7$cF88XDdMHO)h?|5zNFgw6F4vjy+xGzB&fBPLjiR<tOKT6)g_v&P(#ji<0EXu`~h=$p*oK#^R#fDdP9bI^J>3rH%j_jH?N4p^=3iKcrjJ7959a<RWNREy8^4U&FhvtR2b(by6)u&5IsbfQmMJr~kf(|WmTZ=`zT&i<0?S7-tovw%C!jrpAOLwI8gl~f+*qTVr`ytLMBO9@t*>hb6IyBrB8r8BEZCiRDc2(ocrDt)JRG_<|lGmd^V~?q7A)jF%B)7Ds=qMw!HAIx_R)hA7qV=Z+C|^aR<&y1x0tC+vta@YGZaZ!Q`FG_?;D&Yos=RFLC9Mu0S*5Hm5oJKXUswplUs6;;g%$e72&ae3k~Ov`!3}Ya4t1h>TO(<RgHZLtJ^UlY%-R`K61!&Wz1rJ&(|JC(VQhvm<kwdaWOGj69w>P=LuEdScqNWw<@eV*XH~K2r*l;&#GMd)^Sbb-or*enG^u_Kr+%ty;;@Cb?&CDjjzoi;1wi^H+X@ywF(bOD^7SmA!#e+rzkK7F1*VFcSV;Ptg}fX36p1Gs#B&5*i?4skM)1Ab`)P^(`{8D+qm{qSGZ`IHoOfhc31ssPpW3X!mhZwg3xWww52VM;M}v1$BNN?qDD$vKU+l$*9_5To@<fW?J%aDRtI)=NNMlO+KO~5~rN&X$;5pI#rXad`jf)_lcj-7!a4Vx4DE2eKNd(j~%gzP7^_#KC&?2E5T4*V%)eD0MbK@n%ejJ~N$U{t}Ryx(>yRabVSL8UaM&5PvLkSzB<EfP4zdq}7iib6p8XOwAmrf0jJfIf;0{FgTk^'),'Libraries/peggle2/gram_tools.☾':strd('c%0Q4ZExJR`MZAwTfh)?Ru6a1wgN_OL)T<juyrvK2N>XZg6_;a3(-jjNnX!gH#Cmp3{A5pX%aYFw$v$_wQ!K`B{iC$***~av=93Y^)K1;P^3u7C&!M@dl3vD`H;^GpEo`vDPQC7&z}7ubzN+odTaLdnK{>`);}&;4(SC^+Y1tEJH)bV_%CLko~5=u|5|flf>vSoJwH4Qe%u?ny(s8<X&fDjP|Aj>+l}JBm+p(qCjSk8LS|Zo2426t=#imAY5={#uR<eh-JT(Doj!pqZ}ZRjbD*-xH~7UCUxlB$HszQ3O*#tC7E=La+qU3!oqty5bpRGqL*jP{zX+gh<cC0;upnUwyvOg-A#h}fbc5faHl1tD#mh`HsrOh)Ee4AD#V>7C$503s3br@-*L_ns1)L$7;8X!@Lkb0Rqy*$$BDh~xaw!~pVq%eXaquzUGSScg_w1Po0$&bCIkZ&Npn}s3_5xcmmsIeJS-KpDIr|)KjsKp1#jj{YRG~(baAcpg<{Jx|=PJL&zmikxpjK;Oy?|xzrV3hT$_W98___z=|G+Q5`Nmw%p+1;T0>8uPPofamP1_6j4^R@8dTAPG)PHo6PAf9dZW`@|a`_V{e@u^o&mUWu7$vGU&7=P#(?9_K57=hfA!wc>w+*C$qp}T&Vx|6d9Q%lGmpF{cZkWV`2%luh5*gSfV`Td6`f-xFiNDAaiiuI>B=pgbW-@bc)2yq^EixLVfnb$u86z0LaR~~(W9YwWBSbAJAbui@Iz9)YwP18S*WyvWbhM7NaY#ox*uwKfIyz`-I+{mm=;$=D$*=Jz|DANVOM#~PSRwIT=O6H|b=K)bgOwvwN!0BET^E?$;a?OrbB8~dYl0<%g^90`>&%Sy1Gt8s19opLkSWQ@A%&5q9vR2dp*SQRQ+_RdQ30KN<@;0FQ~tNZsSf8pmU${)zWtKA6~s)fLR-r77**<biJp_yYWY}>($px^qbVITDNPqC9V<}!586&!Vm~&F8J-v1L6rEZAB9QTd|%`_0eklgHL}`|5aUxwtfGjAn9U3LhAnp~hrD_2OcBq?es9jmK4`0n8WTXF0Rgsc+%*5rpV7b%VLy~Y!SE;ieg4c=Svf(;8c=9sPo%hY{;5teT2)~b22sZgNRorzUh)HJxBK(Sg5fu!3qEn2l)_chD>!FjX0P0wxHQ~`lj1gPSQ&~Z@SmI}TH1#L3L2Y*%Y7DmDWggvu}38NZdnus{Bf8qV2FZ$w^dFj#pwqQt;8v-g1lBxokM(JUY^#(X(-q@0>S*+G4n1I6!*^P5W!FQ#5=`kSOwR;MT_2|g@*&8pSa0V6sHx(Lt~X*oG>?FA$g^sbw3;|rwGU6=G$Hzx_);rk|K;&A&%G0lkl2N!zd+68dF$n7C95(&`XyHa`3|*nM{sPCKj0_bd-!vg@o#?+Vz9LRa4xhC}4@(_7cBSjwzYfg>3uX77tP2@(;5lw5!I2fsglF=1RFSfUw#{*#%uMTqJ^y1QyHS1IJ1YiB?p;$mXbu-#s>pYO{9s*d%(f*LRcUxX0oZV}lUrt!z~y1zdrQKXZT-oFSPed4Vfw2~DKDTt)kdC^39{u9P76P);FDbnFVl%c3;*WeB$j9C^&{Y3KuG6^@korwk6^KjowTOSx(8rJ}M?emS0+rNU@bGe3OEe5JBvzH-PVjN?d+Ushm<a1k~XEg*!8INl;bRgTHlP*GB#-7caOf?9nL4YV8*b-(q-!Cgi*0#r4~;gDFi4tozV2B$0Lo$9o<94@lh#pG7bQmESpLfBRQTZnd9Wn%7#3%RN5hl~5$!p?{*`0Psh2Ob<0jIc#+b#E|WK#ayZ7Db6mr($~y{7)T>zc~Eh?bbGbKutk1Npb<=eg*s6{7%lE)M|u3MkSyW1&h!r<G=x?#B%~|IyT<YJB5u$oCu!tOCm=-z*<U-#)Co?g?|56@J5I9#r?l5r!Mj><6)t1XJ?glenXd70#goLg%z*rp+`22ovc)RNDHqu5_$`DtKT(N@&}Du{BypR6B^3%&<AvW1uP6Iwk9#IR%9d$Sg#kb>AVP&%Wo&k1M%ds3G}vFa@o{6AC~ie@dGqMTI5$d?>(J7dv11eYUjOYFUDybIN#qF4!(Z@4yFIPlyqW$kU|G|@BI2Rpk~7lQmemv{(K0;?Al)BEQjO|I3RLMxZsz3lkzRl4+x|nA0q^H7PqqZw>)yM@;~v-!b8)H)Ew#%>=?6t^mFE>v6n1C{gMSky_=#+)e5ZKoFhto$WJtFsV-jbr4H$|=H*k7b^ctV(daf_Z?e4QS@VVYc;iP}E!@5r@YPDz{IKxcSwuYuYB(j|u?DU32Ds}eCKOT=mvVn8hh*t~OP#^X1f>3`jQy)RJ_YezOKe*&DSopoK866+zs3Au=IBhap^6TS7J$Q#ycKXrn6xl$$Uu?dR0<U3t?k&mu(xmG445g`+H8LdgJS35C73A!gwpT5vh#3l(yrSzgcT;@Kp}Q8(6gK*T~)4dbbgwWE-UXlq<f-7pzzTd7gH^|ruIak-zWUfKuy{k6ci?znsvIF$lj6PIB~)~`BQvLKI^*Fcs+*QKbvW39E9SNh9%!TL|?ooTk<yfiGqP7mhzkoCf-3UdBwA(VUHB-k%DdTyBQ20f^*o0f^8@s*A(AtlJCeHF_<zEz6+x~Gn-MqE3=$k*Jom$Owg9xzv6*_YEOm%-O(6XqPH9~?dRIh99<e9>xeOR9{?k&Dd2^B1{f^##f-|MAk3~DQ?ZvaIKT@z(<nkOk=eJ0iPs3sSF4ge?lWd+8A;P36h|R8#SVtQ7;W=E(@AGR1nWrjcICE+#7499j*6wqHHxTWLPZ+6{<{>m*QZMiNMpKaiClzyDmKYi%WqI-fdB#VM}D7LNz`ZGY~TCl%bW1`&rOuF+3>numbbp0x4yG`^mVqgx_ZHq*DXoaVRn7L=byr3k~}>3l(3MB>a(h(ln3h%@f}v}IWYQf>Cf~j'),'Libraries/Ń.☾':strd('c$~c&ZExGg`MZC`?L)w$%LtO~G?)MZGn@<?wkC$_0s|aDQ0SAxjTSYMPURH^Vx?||bXyw73A&|ioO#K*t;mKJ8-^k2J{<N({7d#ccSrJ$JV}o2)&^{f_uTXTdMC<1;CGkb{t@kT@ae~IEni((?R2P<vSHfkMe$}gbv&{WM%TMxLS2tIjthUqwyVq3b=S@}+B3a4+9ZAyhRjccsGpEva}dQTS!ci8Vx*f8{*-^rzvAD(|NDGrX2uV@3B29qd(9aFKR`bTqcrJsNV7$NJP>t!{KJ6WjDT5ZJ<{m}{U8Mffq{p7kH7Rt>XBLBBdo<o{ByqRN`wMwCR_%bF%GYQg7(P<;7<c!IsgSW)@J=S33|jQEKC?#YkTCatCuM7b)P@-PzRszoz|78&s^#vAR_@NL9i{iFw`wgSlUg~ShD|<%k<5R4m@Abp6l*fy$zqs@CzEuyb0g1!Ov+h4HJH@omu<R<)6}vVD5|U%wT@hPrE@svsu{PyuRKgg<*zGG9*Die^X;9Gv5I%{EH4feEO9C-j$M@kUrR4QHj|gwo_;l=YO~9x#VbnbS`m^o_qn1PyXVNb0jxcEhSM*oTFdwI-bsl_HxAk&0lElgg)oG1$|Ifkh0COLV9GoS@krKpzw{M_Pj0ik0_6!e@*xEp!@lD!B@AxK0)!C0$MFHtfj@qkoCvulOOWC{6D%7#Wvu0tQ~Nzv`dTFjZA}@mIEzJW0r2ky7AY7w!VLzg%kI~`nb)YX+2Yj*z<_5{xcbi1txIM6hpEfr39CXmDfur>1zd9#mG88{t5XpvX_5${IC=9V<by<M*NgKN4ly%5KihxgKc|wRNX+P;AWPaa{l!^lKBSiktquckLLBcwF(H-J7E8q|AxOTAXyE08(RRfkn;zz;6I)w$w~Nz9se~V-K!v}3BpnWlXa;2S|%^p!E&zBd5%R-1%qx}gyV7Rv{{Bn0C3x6yU6OZvxI-?o~>``;^mYynR@X+2l<dc^GNKGLCjh|gpLW^3xcJy+FFgbN|`3ktYSuyqN{8jYpGn2(g-Nju8vf^DTgKOvHK6MwD3<;gtTVnRRZ-ztW({T8YN)Bq$8=9Ylv$CX%ZF{Lwb`z%k(09nxSS>N!K!P>~TtKu4t@q$0MnXat|e!o|l#yM*Gun@y&Q<0CjB;4MNsS1q1jQ+Gy5aS0A6(x`P3HL<q^yAha^WhE+!3b+-&XH;un{Zv-Jzyi_egmk{3|q?&27A2y_GK7k1UlUkoFiS$<U+f~SJNSDmFxNAu?bVBMXVFU;~iJA4cHd)+F8DObG>Yjxj;*WvBA8bg2{uZ+W<d#~}@=2gQ$AJ5E&6zEZPvYhHwmD;9!&C#xyvP4ODY7aA?7FJ5HqJoXrh%s5os`FQO)EjR&r;o*T-L0St(A1BCGynB<h>-z=GIgWC3IHc`oc`=BG(=xugj!cq;@23kW|DpItG~!_-8P;+>v|a997Ety#!+$2J>IBKDNQVL<{ngrt-=mv%X#i3=b70C@Uj4-pTO-P;32w#**A^!h=Ii6EwF8Ob$t<x{j--B1Jsq5BS%j;<=UTl=UkDi&bgTiN}`9v{f>jkUlLXPZ_<ZLkmhutLD=4v2Hp_X;A_^BAgW~flS%D71f!Iav>3nvWJim1{$GZEIdUk;Jeyv)eHLT72{yA$oSA>WyLaRt=PkauAq|E+SRV6;+xj^TAA3RRMb~BlwXsA32`)0KnjB=x*myQY_>=yz7<vPEr}K|00I;VEr6W5r(;!5Q3kKMVhYQJ-Lzsk(I}0|aV0wh-5gW+qDxBV!ueoBUcRX>hqIdG0pnCSqadCQO|EjsCDlE-;CLq(7M8xHDKpn&ym{>8G(Gp6D(|RrEf3K~kOS`(>RC&|z-Ls>y7KS&hTFC_?~^jg@bsC);=;C;Eo)<jmJRx04<7aCYxc~mLD$e?g`LLML;dt=5GC5llQFg8dG0MVnd6kJ^W-E|7}CJ@h#!iSVva7wu&Wtd>+26oesojefR$_-Dfjol<IO5_l8vHA1L4dQa1|-!4cMKknMrBD8b@<3PAJDQk>plJyI?qGH(8vpb$ZhfyXfM8ZegX+ztN3tHYypzEFtL>+rTU~KI_$ddjN^S&96z0%Jl$$tRAmu56gl&j+Sk{9U;#*CQA8Q*+U5*pS|$CZrqR7S-Bf*;r&XMFGu_Zf1pk>#4~EcH6r#Ne<D&WJRB&uRfW48S)!~1xaxk?p$5Jvr)`B3|Ks#N2GKzo(SZfgfkJeER;hTsAmxd5eQpWjB<+MH#Z;$~al_lVp$UBf;_P?)595n{X7^B~900E6{2&+Z_|xKP?huwmjK3ohU(4g;isbRBC6CLJCqdQotM?~Gp)gFKom-j=%2VcE5T-01e>{k1#aM?vQUlt3{!nW~u%3?iGyWX^eXTgNY{`#-e=vxn0gKb^TtvXN57=H&0r`1Vt~caDp_FA~Os{mTdBOS!f^CG1J?4L<c-?nxYp!1Zey?7~hYP)<5BKDodc7y#TzjVu&-KPaLxJ|{rG>eCL3EnCFoa{BeksqLDZR32J<nTQv7YB`Th8<FbzFKqKk1lHKMv4rhiCEjFwmH$vK7^PX$SP<xW(y{a6|DufDWVOAw`9O#lbUT*!LcqiB3u<tpmZ89S?|$RN)P;_*bIg#Hf7FS;ZUKf%Cp>ES+-+{)$^(*s{0++n^cIdhBiEA_CxB1^BjG>Vy=V;+lSk|Bb)Oujyl#O6CzY&=-Q@X_#t(buE@lP<E-TJP?)pjDJG2OP3M+yF(?gE5?Dx{INK`{*3>VA9zGPJ(Xt9;qdZfSM}Vgj>t6}2Nv?yTp*zt4*~)-cy#MI-fL4<8we{)54P0LB<=dYi1UpKPYipm^^2Qv8ESd|cRd<XDlf8@7FVenMvFG1wrsmHs-=dlGRlU7YM@T<!UabvLeVMu9xr#&V_Z&|PLG%4IHX=#1SA_R2Lj!hfWm%6=0Jj|U+g*NCCTK=kRnw{$8e7JZyi1S$I<?$NBdtM?T_Sl7Va*+vqEXZ1Hs>OdK*rYIE_ZvdEZPwLMyNM?d+ms#Q(_e+b=ps{7?LjH6MvxFRVEUmJZ9UKIWxt*Mrj1!t|Sy+<7v)ix*xwdP?JLIbm3V3kNB?<TiLBpa}XbK?YH`hX1R0+Y^{~_-`p>b{PwMVhOb>j@-u1$+=NgY?>3Z%`3?FTBI@Y1Ww`*2!;PS@QclhG^NOukOC@r&u3_d(rcx8<wmsTnF|6;)Q=?yIE?UAnN#xIQW^BHx!6Yz{>+~kGih<9(n}OpITXq-vMpY^)VcgK{4(3yFuiMEU!x92v7>?+>KxX$ltEvFFQ|&p?8+WrIq40i;HmTT2%ocW44_|OfoiIQLMRhWvNq?Dg*JRh-tCHL4WnoS!*%?3!CW`P&o(w3?Rn18SLUaZZg>Q!&m#j<2)Zr=!v6t4G@z6'),'Libraries/peggle2/main.☾':strd('c%0=t{cqgHmA~t+U|kp_SDS?-$H`T=Jzpw2>EY@R$Vz>{YD3T~O4@jr+>(^FzQjiJVK>O9lh{t0IIfK%u$vf3)1avnI9DLV<-fQes=wsk#|$|`&aPIrY+rHPMkYBkZ{F9u_h#nJIN7V&>&K4&!tp$O`nSW!jxH{Fo@4*_D|X#l>qRI1UgEfQ%eGzkOSO+4b6mIe*lc^s8Pz%shN-t2#eF}$A21!ivmQ(UAdSz=Pg(Hm_6Jd%T5+%z3@tx_hpAxL2?nW^-N@d`KEiL=MR>kjsxK-#$$GTuQMX>|pX>$JeA9Aze*ff(&mi7}&R@>n&EB53vNy6nWG_4L`hNC~!(Rb6QM+5WP8W4v%`Rovvv;}H6~}c>yH>4cWuF%fhIQ-AJOaO&{ob+nCiT6^a?1bN)?Uj2fKY{zXbsy?+od0{?*`CxOGR}EfX-*{InW?z9zJ?d^h?b@%wB39iNe4IES8!}@kXFPdCNmER6I4c60Bl_ce1aXq?x@0E&t#$-&i1)Xu_;qm9JJeAqZR*f0C%<sUN4^aLr1){UEm8yn@;}JiM9Rb+C$C)QE$0BMzrjXnPYYjiOW5-h>&H)U~$OV-g_&#z5h}iUzABa+fGxi~YXWiNe!CoTA_^XYXZq1>H{Q_X95u`u-pxT%|av-ly4z$mox=&m24G^}T3$V{T^VXZYyzqn{+*wb1MILVjP1qm6;r4Z|Q-KG>+|Td&>PdhO=cg^T$2wVSppsaRUllu{r#Z{@f)(z;c1^4Hc(8@{+CpuC3FY+Cl;FI}{)pqB(n+n^B}>z*suWUy8Z^x|*Xcg5$V*X;z(Y@JyQYPz)Kng9Z20%QpSx5&v2l8!&n#vv$m+O+@YJA2+5HsWB=^P$5zs|GMHehk(kb@Q*{i_qQtb6V%R*a`K5a*u<RjZWY_UzRzmj<8U9S=|B-zmxr*v;YhL{g5-`0#mRgDt(=$uTcGZsbCHZYR*FGGxKmC^H6e9+P#B^e(B7*2sB3zxVumwE5^vT*#+lmu$qCZ){AoX|JBx;@CakOVWY-DcR(Qhz0S`Cq@bt5`trhfSho<C4)?nJGF>ebeY!+3K8)!0%GW#WmY!>4IuvA%r}oPC_tI^Z@^Od|DqME;ecK($`12D8aa%T*$<>u7A0Q|F71P+zhjur#qzUXq{eBRpY}hvWpA)ugL>S$W3ej=GC{^M5;fe*W^mWBhxX6Q9my2Z04%(%lv1Iy8*x8Ot7WLMA)66?UB`3NQ^?G3J1J94PBOZD+3qw>GYfa=QyJIVFYeDL#Y3xYbFe}T*PPj@<;pFdR@8(V(UOxig=7M+1Ev#r+1RZEYJIwJRS|OF*q3g1umGNz)IeR$_Be6>gn7yF1RL3c7mKDXsU3w^eXJuoD0MQN6mXxU9r%*qqbD}VfkArD^ygfBa2DxAdehgHCZ+4ED481db1XKoWFWA|-1ut`CfX5j9a0f<zv?+Hqfns#>aUoEQ{jRu<7`sq$;n_t8d@X=`;VcEFm$I+v-|w?m(8qo9!PfO}eneRi?!8$f=DoQp>Z37)u-=ML;7+YKiva+cv|4YjG_ui7iO@kWATpU-Xpo|9V$`@92Mw?#gKjTyro%ikkUvzJ?K%i6k)*}3q!VxSf<%zdx*hi&uyk%?HH`;(I5&uc)$WjOShBGS&$c#*INHX5h=Xxw8U~MmVJB&9S1MEVl~?B|$H8Vr1ohY~dVL8-4Lxz{@I?irQlka9fZo<xXGmUWP+mh637XY2XsS^1G#DGJJwJ6+d%(^G$A<U34dvZ%#ZWF{+2Geb>7Nv4=5aAw9x71r1wv_f4QVup_K4}JdM*jXnHuWDlgmn`Dwm!nH5En8<Wb)vsaJd$*fJJ6ShOOV2d=0NX(&9Als8wY=MiPzl`Ms_-2CW;7!{AzD@2`q83vBSa<uL0&|=gG9UeomJsaX>0tWP=PM~LmP-E-r2SD4j#U<)ctGIb-=SRC{eN<|)Q)Urv)%KCp73X$Jd0tv7dSM^YO@qE;@(Z)0e8fJmX#3cr32Q(-@{E@xgLB0<v+wKqq(8x_tB2K^9F(sFCpXrb?6$<@F!vpWzx^cpCVSnH+##5*riw3|h1VJ3T4)KuXrjT${$)}l?a-Y4PguR>FtP;#Kn%`|XHlL7O>)Z4{<rw<3h8XFgYo6HfIpdLMO4rjL<0wGmUNSsMp1HeC+-II4q*X?sHghE0%IY01Jw-5BvwqY-?l{Uh6%MA3+S$KGB&%D$r$NI3CmvzyLc!2!lC)-pYtjF%h?y%`}1;XhhG6Aj&oP=7FPr;yX5(bg%JLqCI3&$A*^izeW3=xDV&mnRk@S>7cPTkx54IIdKqlQ>RQvDS)HNilUri#w&4F?tbew2EzaleFtg5^aA#D1+EUg4epTudMF147?q9|JR-!cS_67Ir)|2~HyThwCU*%rqZN|$jDaeg{MWYghFkE0Jg|cNt>(s+X*|)UBAW&CHB^w35wjsz+bPRA*tQ2aS^6H>fCN4ooyJ5EEZ$$7jF<xZ9gktOxS~Nq=B~lLlaHi2GVM^XM`hMD3FAOfBa{s*UH<E!LIxfZU{r^`y#~FUr_bSM-F%%=`CdE5E$aslwra;cAOlyP{&xg#Ub{v1~Mo>Ou_$NnQ*skXzo_doLFnsxJ6jpC#AMO+@p_T%!2!<F`6;1pJcNYxP03zd-Fe5_Df;D2Wf9AGbBaF$_C43NeL;g<2fq!a@E^GYfe?Mz$K4s2rOR>C_UEM`x(GUq$2IWA|$rz^I3fwst=i4T6)A|zOY!>n(9naf~2q_?crg|!a+1wc^56VrMX(?N+TV<;ivQM7CX3dmBqkFbA6kGgb*cpD?9V-()I@^LAfB2S#1+fdGUmY^E(Dcw5`2cL=?pv0JY9w{TQnPV^*`BtED)?HRA!ruGU@<x(V$JQ)L`#qzHeVC6NZ6kH;*E}0#n9oZR|hjDCb4k49^Vy4Q;+H%eK5A2rK0Zd*+x}YLMF9P+r=nVEf<5f<68exUVj@!+D^<{M<brsr+0ran}^fRaepL%S*PI-2B?ba7{Zk)cZ7Mu4c@V{we6+z;AWB+Mz5#Lww2*&G@BE~FAS_aHYb{8xANwXVp6iLc)0sw_!PwMs<iU;tugZ0fh=Y;SybgPLIyJrO9rZf9x&}K-lK72M0a<kNX7Ms+xLZR;S6@)q?Jbf7uW6!(}#rRCm$HF6uB!xmb*4~A0Qc5$B-dBnEi_`X24jqJGZNAk-JZ&Ot_#Jk9XAi{;7brlM*M+_sTA0pW?vBjepZV$RG1fH2Ml%K?9LUh<gs-6a`rQhV`OoCpRXjRBlX%{ecKPuVv>Ko?0sMHDkG#4rPDKehUb?^?ds}PaGBOiWSyT#=;wz-CNJ|Gd_2<92?Be&}ggkzwgakv;#YBsl+is@41}(1&B>BZ{xuJf;km6Cyi@erdnb@UKWYGi_a)4P02F(qsT4J(`Df6yV<o|e)vOCaJU)selP6=$Gkz!DFo&WD+lY;wH=&T_$?sDoI^!Ltytd|WJMroEd6Vxc`9>J(BI<Wa0frd<mISgEw1dMkMn*EOAYb_NOit^xwLa0OO8|nDuE&s5z}sk<Td9;=+2%XDVz0UfH7)D0CLCw@0Tu?H)u2vGP}3JB8jA1O{@WR`ZT-bs5S^0q8c5w<bqP7jxT}z{Y{5;(Dwl;=jN2q0Ths9FL`kk;SmQd4H^d@S{xi>w?U}<;MT2tXz6C9!lAMGdd^T2O(h4UZnUZNuSnwfB)bEaPP3oVY?3{|!wT23OLZJzSF^90MAV(^uB%wfR}IN$S19>VB%g_GY~DL%lct!VZS0y*B|}!2;FaTo!3Q2IDH~oId1)L3V#8lp@wYh);ZPS;0MB>O$&RM*t+C&QwyS=(7p(AU2;rgPprdA;*GTAZ%x}|~s8)ijzL>;6X@Y_|QGBx81i8*7#{Q^%_4)F6mYelkzqz~h+N<!_uHs*;i``?ypJ!iuXQXg$QVLZ@Yv)gjpb$uTn#!#-Vqsb+$)5<aMsK8YT7OHK8)3p4d9G6SeI(rj=#ZFO#ib1j@_7@BLjI~t4n_70OCfF}J4eW{7FB7~QzrEK3we6hs5w^&zLX&+{?aqL8+;udX((J;V0%IN!E&4w>tGTxVFG-6p@y4Awdr%{RnLxB-1CLvj!I9^o8{Oy=uD0?<C^s2*2wlMQ8}!(3CM-<0#HHafJ$(f8MW!rT&T4W%22SFG<TTCT#T9lA_o~TAB4H<DA4Xy`BNhf`qAltb7nEpb#-<S`ee8}>(M~i(fssJCK5py2$cHCdXO}Et}Z_E0QY{q5hQ6h3QMKEC_3e@2mXru-VHmwjg`O~L`hez53oC@yj~ElrR(C;!9zcP_L)*z-^+4zax&Ie$Rw&KrW&t6_<mbj^+Ci(!$>)Al74a;_5u5>Op_%vWv%6BXJ%$rXJ$`6jyah+)i6b{nfpaiLETyH^b#Jo^b$^&-}a2g3nKj(2Ef@-t2>6n38{KG!BnARs?Z43Dob`L7F17Y)WN=r99DD}<r4r;C{fyeEn;K;Qm+5FQfHrDf7VogbVOLn+J6$f&XejoTzQ&+1FR#CMeqT=iZNG2)~QC(>Y)*FN|6;&j<>43xh_?5?8Ur7VfHHHKy#6ov-3_qFE5`jghAAtnXhVxF57`7+pd^jzLb3~QfbNRE9YfgW!yWZn9}C@_Po_SOEY9WxV(&MgtR7L4tRMsHZ9fxU?6ox7&^JkE3<%NZBk*lLovh(nh~}UvgbS(8aS_78nzk~$*2=-S^~JY6Gr9JQ~FpJ=El@go1>adtA36uHLki!7oCq~ld^05ZEI;XL(;0Pc6(_MlfdgrKkm*3@%VMQd!xc6g8xgDmGLv!5?%F5R)loNRunZE;E4%?rt<8h93PJ{g23=jRj2W{AOq-*TPf>AVcHE9Zd2c<v2RALQw_DdNjFSVKZL2oX}Mx(2(K69{>bU_Dl4H%qY3?cwWTPhc<%Z)h6P>8jvm4=XjTP<Uc*59=$+BLU8mg6+{VP=$<=mY7nIYWh$Yq1H1Rl=X^OZOq+U8Ss$%uH`Hz+4vL0%TEdk2kI8!WtVHEbFj^DF-COsH!t>rI|l?69@ddyTL@Dwy)Fx1;=CeH*h2yqz6Eh&w`B;<?>wB=@bg+yh@jgB>PNIB6$74kz|ejG+CL9)$>%dC2~a%UU3V`3NV6eKv{l~m}6ULMQ0Zg<7wJb+kRtq^Dw^*FZv#|o^A;WDXHkyb${w86?$?1pA%p5ao><H09Cj-$=w9s@KDcZiA!{UF@v2eF?9qfE_c_h@v1stc;@G8nZ@i`_f&RG~UG8>L!Zt>NtbX07es-l`(1(F$Oar|xTl)Zz-o+)0V@jYrY8n;FrnF|^)(g4_)U8)><!GRvr!PGT7c^q2u^9MEG1sBTmD1Jn2GTfO<&dTlKpEx4-M`b=k-FO^qUoaNO;wH8&aIm1#6C+|U$yB6>PR}IxgEdbosR;CzKA#dZ|KZ9UxtryIB;M{x8Vx0zB5T<oHAKJA0emAtWHKIB#VTrY)T8-9+ZdJ~MYGBx@b&MV@p46QcuooM=301ciTd_#&#CJ3N4ZhN9vMzSA?qwKe%6V2kQ`-Rs5T=NRJV8qUU48r=!|L`Jz{*KteLIHX%gvY>$#D((0^jYlQ~0_*>mZLnSvOqEcSew1=e6A<R`$#D#wE{=)G7K~C=w?%yjyH1OI;Q?Q#Z7}fKc<q2M)}5mrJq&du%E_qSlJ`Q&XLupCnTGh4Ok{(u>l>^F*{q$Kff7gU`V)+Un|s=XJww>Uj=tjn=I-v19s`x~C>gso1w)6B~@bD{tDbVV6%Y9zE<mv-s3uXU#QDQF!}VF`I;&W?d^)7PYDOT0>k*u+~^?>v#!P$ooj(i;}~##))kY+u|y`j)Os*^SWw3?Y&8BZ(=Pnb$jt>cii`T-Tw?$+I%!vWYBQ?hUd}E5uWN;prDZ-!`Hq_gQJTdO&nOqL{WiZ6|=%R3+O6{C{`M;*DbKYco|<5uJ*c}R9lnR6=}V0RaimFvW|+hF6bz9NP-laeHn&JF`{zR8mEFYL_HU+^Sh#pVpkDE0Y}G`*39G!fIyQ&&v^G80so0Sr7dgK4T%(*lpLXx8jfHf)=P2#OcXZe+tHfOlGaG)CRM3iBSt687dOHXaX&^lSaa59H(j^V^#FV>Ql8T_U&>F@`8tTZAzv(zRH)TluT-@P0jhyS0+joF3fR?wA+KRHNEyS<#4X*z=oClm=SfT$VALf$&S;rY+;Nx>vC+MYiy}+IXygTu`OS~Rx^i&<=6syVEvL8^K-}M`CwaB(*78Pha_)(rwp-6Fhi$xX%x-Ocd4B853tLyd-n#Pr)`h>e@#7w+_1vDViyyaNgg*_pwg*1$vEiewe6;t_Uh22-dFwadDFyIGke@4oE;hCt_W<sJeQ~WZPxldRUHxFX*8Jf%-*I^Er;H}RUbgpG%jt56(5GL-{3Zlk0AeTv<J=Fo3HMfQ`T#vREoj<)v9%08Y`+}3)A@HGzf?l|s`6eT<RAE&BL@#Z<t;w@%R|StC5{(th&w?|AcRZod8;L^P;=}9@V8}qCv0*EbfH^O$QQvuvA72fdu;KoI+19gv~OeLj=VCBIyq;Hz0k|JI}3%}vgls`^AT{l^AcuavyZOjsuUM+7zuu<^z*!_A4%kP{obtfOWY9eo7lD5QGv+w0ujN>0u!!m6K6cNW`QyzTtZ1<>uf~|n%t^=Nv!mqc%Pd)%Nr|K54F_~on9zD@KvAujJtIF#8>tRZit(vh(-mV*1Kphn)%JqB9AoCh}zCT&yNQEJcDK;)iEQQI_9Rzg{a)IsP5Ws4o(y!(3(&}MNK1H)vOazmw>~w<zY3~7A14#l6|sdU%BLQS)%JDfzM?*S3K@xJ}@gwu=Z1tP@e)^L69;$@L^gjQ~*8EuF|ZscT=dY&?i$@)25D3h>n%6o@^V3Zl$ZuGO_<e#GWXB{#m<y7On5kj~-n*zO?w%F`9FUP)9S#GG}CEqd)MVhVEx&6oI95lafsIR(!o!HTWHSa=pT$TBwByi;cA)g^pc`KrixFBmy61zs+a+R9#Oq7lh;!3JkS_P0y>O0IKK!OlW|;h}pbyMV&sKUo>7hxH9Q|gS$AHQYetDmO1n)vlr{8oX!>3aUcCE77;k*3}`tBS;z}RNcrXLd{e3&VSPD!wJFsAwKt!v>f%@KT`L5fKjkWq0iGIS0G{e4)NU~!g(qIEa;NyN^rsFU^bY+8-j{wHqJHI`bjKEL?4q^M-!w>4PYyAuy%KqQIkZYYT=l|#n^qBsoj71QfNOk4`{vfFt+^JqcB+N=`|%cty@Ojs%>vdkM18ik8LwFCxAwB_Y8{#(Is?BOkM5AFoQyZt=V3+%)gYXNj#R+T<^c-=SZmpCLXTshoc4Pg0rrHLf=RW&;=9v2j+Se=HOl}6>RQa#a}fIOfe^esy$6EnYE6V*)NDPryu8_-HrEvYikj9kgv92WC#p4<Axbt^mJ3@8M~^HWI<hoEQCdQdvuy*hQ9odI;}h}CTq%NCWehc&`OApPt(6UbbA6@jZ+6?m=9zI_no1@?0n;C^+`wM^L3cD)&^-}LXnk0G#1Sm40nX<Xmv&gq0MFMMvA*PQ-9nJ1l~uV{aLoN*yfJ2f'),'Libraries/peggle2/rgx_golfatron.☾':strd('c$~dgTZ`L96n@vQm_R@?yV_;7hC&T)vTLtd)1-2|E);ClIJUfYYfFpdfK1Z|FG-=fkZiXNp`}f>`&3BtP)I2u(1-bBJ!fWgjY_<PRv=rN%Q@eC=R0RKl;7d^ng{!|*TbjA^`_No_j*(x^ao={H^|}CyV;)xlo>?V8T^U~R+BQ;*)VNw<a;wRy5$b$o;MB1WOn5Fb0TJIG%`;0uG{T?etGlum9=%sI`&szgK53nwKs%KN(W<;lq=Hs$9r^(b+&Bm7>u`b?WP@}sO?>&Cc_qu9<*_oX_}=EOCK<eR_pjqX;rlIV}8P)P)7NEe$J06yr1$%lrQ0JDSWRJ@FWZ$^B?#NTK%*|r~TQ@VINyw@>4_pe^(}*xZw`}ng7XuN9XIRn*lnw$l98+!~je~foc37V8F^f{u&5iVCP-PEQQQk4cU8QY6wgh0vIU>Fg)ddWIdM2b*rYZg0nLiv8?cyj7I*|=+GdGasnm<C$v*-8>9iZ)wZPql~VEoY~-6w(QM_Lw+m(Y-@&f~e7LQ81ixMkKi{n2=bH=R7o(0B1>scX09P2{YqUE_+{F|Y+s1*A^?DTZQ)myI`DE_QXar_E8Vk>6>Uk>-umk{0HpB7|tGI~G7YsUcOez2ilvi!%U?1mJQ=oOINp?zlG}GCEP9r<s)|m>z?zO@o?6y{_VZ{#V+YVXmuvzS|`92P>yzTII?C?hM0(Vw&s12PF@ejkE-**ELa#<sA#W2FGoWAGJ`3X&If*%O$kNj6rvZ9cdiRTY#h(PdyL17k33I^0v5V~~g<EReA8Q(^puLMaZt`yP|e7%l^q+ilm3|Pz`3olFlH<Yrt-U)b&#iRVq{?U=+4yDc}BQge@puI7$A^x^)QW16c7k;<8)21au48h7+BF;2$6fERZSoNLxE#D>l8=%I|2|GkplQlvYxHFSW6%yhDW1Dj%eA=Hokey7^uJXtH0e?eBVw+}hSPs4Es6Y2T7l}UM=dfPk^s3y>@ezkY=Ns4oGIT_76WpQopOPdz;}7{0q)#YlUZ^1ch`(AzLNT+7hj^n>8<%h`tR>_CGeRCYx@c%bOQE6&2%x`F71Tx6Kro#Q9BLZm6VG+zR%H+qV=AiTISOZ=^xYvw>?wam_n8bJC{RnNd(6MRIB{ttQ^y4Z7+h2G85Ht4y9k*vh*>%Vm9|s)m!Obq-u%Lw0GgD%thP$R*(ynh7Z9kHkTMyt6h(N=qC^U^&IJGRdm><%N~R<o3h{bUX#&ir-4@HMXO;@gUH(^bU_!w%DC*h23HN#777HC`t8B8dLs5~?4@;9H?4zs_PpF|NI?!ea@GMW6tWZ#yC8anrRhbg&&!lK2iDDG_h?rShi9OtLpm4$6Y~{?wjQQC*u2zrJkQaYdWvC$eF!6@MdM2?VXc1;#Z6KmrsT9V1R+${YQN$UlZi9U3EGmhF>4sV}1~?R(N2bD}Amn%3xyVRiq7FwPCsR=2Gd5jbGjCR%Y4TjPQ>*p%KEt!s0UWMUXDX^^3NM_BGVhH214M)F)&'),'Libraries/Compiler/op_table.☾':strd('c$~FZTTdHD6n^)wm_9_ao4S?_Gyx<(aEpp!z*>`36|q*nEC|IHWG@ww`VeSBLen%P0TL-dLM|vx32GWZQLYlxXYw1^$3EpJ^qig9*;!+P$;FcGvoq&>=Q8KanOTipV810(KWL_jRBvB$z!)@5joQ|PZ4Q?!#f(kEWTa5eW(rkJ4--mt_;tkwlA5j$eHTlIwEbX4tddp9*p^uy!~b%n+7Q|bTY&Fd_kWeN$H~yq5zCe!rk%+aEUi3N1>qq!#qO{t8jYM8Z;D3Sb~j#9J)PD=S|*=2vlcjEA%s@Q6tnpZ84HtAI|-_YjFzfa#n$=;y3v(6w#??htVy=Wp2cBcp1okN^%}dv1la{D7_rW7w&VXC+u}fzVAq{6s=Cc4<65;anzOY2a>)u4`~};iI)J*8@Gz!hEK2Yj5_Zh9KiL}z;Jc%1^c$*p?#!O=>KK&n?{2I^1R6ov-MCtVGuYAP;WP^3JbqpS($Oq2&YX%yqr=f?ORiBg6sK<RZ?k`D!#l(YNF1~;jr=onT*q-M+9s)tq_WP;ynL`Em6KGSHWYBsQ|o2Z=Xu!_z<av*8E8)zgIG&yE_?#qQmw18{fy%^@kp&zSh;uXCF)pWTWlE<e3D(ozj<~M;0b&<9Oj!xgRR8Fjx~uvm$js(CDP8_<%5NSTAaH}M2X2;bq=8GsQ?jG!dHVq2nhSCfN<6>3OcB!BgQ?!f62SN;?W0sf$Y<>^`V;tv?A*~nvt|>a9!T%8;3IE>Am`9Gz;ivmG}Nfp{cw1&p|F;(1s|XX;JtOa4V!|N))?;n}<-OTHhe%7wu1`It!JZXYZ$W-t4^EnWK6rlq+PaRRTT472nd>Ec>0k#-zK>7ND`{dV2^JLWinYV-?d>TLR?nb++72=#lD?DkVpV#z!KyYu*yuWGe{uf~|WqeFzD95i@TM6Vn_mjoQ%i_<Wcgb%`rLaB5x{fS>9(G%`((NTI#Vl2_=fS~jTBL~vBS&=^N;tEi}+P*iCX=;-O5q&A`ZprgYW)dlukn}9AhsPN;bV%g)B5}63HNymv*s9J6Z3)M*Ye)&dC1dOfjH8xDneHnY@A%sJF=L#60eN=e@+cLIY;p``Sw3s&sbX3<B&bnKryN}&Qlg{x-xC6iHnva1?06*0lMa_z$rl3;((A|^JTHp}WlHNbEegxgfc}XpF@w`^JB*RFMVZ>($;nL)?7`8vyrid-H0^%0WJQ*z!J_XrH*qX9dGT<(w8gS#&0?uO_h~&Wyo_>i~qrYd-)duv{i+~%Tp|fc<2niZ=ZI1n|)w5N#FSehp&0uTuURw`3+cavc@s(_?)k>j1()~4mW~xlzfQIu$@?o#t)3aaC?k{At*etloysnFxvv~OuH>TPPOz`j)hF!pGlcM7BI9J<A{rv%@mfihfik)YdYT)(yxwjD5n(H6)#ieK{nidUsi(Qcom{0NBR7_l@(%6l)V8n$o*N1w6Yl6TvrT5y1a#z{oL*3!HTL`}A+yRDYuJ}~Y5^zo$xl%I~ORI*)bR3a}V(8&uQWP6AC=RwmZMa;{yMQ9qxI4-ozOESRS{BKb$Ij{4)9B7KioiwL+xSkP2UP^tb46KCTcP1JX2-$OzIZWA5^<pst@HJH#-XVT8t~E16x2dcdzcsvODFe8i^{@w_sQE>oh?C4Vku32Au=Rt4IPkw$a;;feZ1TfVRzXf7;@!h>DDQ=V$eWQL%|9uHe4KuoO@vQQwlf5L^_fP6aT?*7bUT8>S#ti6hlQZJQQPJ6tVSOV+-LuN0eYC@C*S)QYzcX1YTrHc_Q+KCOfGI0q5GFEPlk45rOM5WcJ6gjUaZaG3-Pwwwh&-5)GD?2&j7!-LK&NHRDgn1CM&WMRO~zc9je%R)5zPJ2PxvHE#v<k8Uk>SNrozw()Z1VLn8;iazU~nM1H3=3qx>qKD_VL^^c)#cOVF${a`r?x%PMxxrqyODbYT2HX_%o^29`oAHOGTbJQGL)}!Q+Z)u&PG8W!zPVTGf$rWDy*)-sGz|X6=k6nC=B2pUuRcKH`(bD1)$Zove~b6FH=Mf<#jBCI$Ij~g53|eH@g*Ai2TBBzyM19?61{_QH5bEhO*cWWnK1j~Qa`jqx82LRpMrBSf6fTV#R76hKrY7RPInk)D%sN&r_RQ6XJf-zyy-07au!y0XII5*iEL{tr(&&Eo3r+it^d2}9iv-YoeP)VUwD6B4&)^@>|9<J54mIBB_Ve_FDXmTW+j!Al;k_+^9@Vcs2ppf<Xhq$fOv;EVRUqvT?756BR^*f<5m@OwKH+jJo#gHDo)RgThV9+wxHBtw-|D!pE&DN&h$&?(j(z@EZai4R9B+kljLED##*=EIWKN+uOP^&WZZud@|TVyo!-bj9MSdv0lJT51O'),'Libraries/Compiler/generate_operators.☾':strd('c$}qJ>u(cB5dWUP;y^;X3nsd=^OjtdlF*_;6NMllIqu1iv+K$)`3xjQR7uK9p_M{NqCg;Ep^yMoTA+;}<?&&^wG#as>c6D3&%1McPEkS1jc0dfXJ>x%yV=9^3Y{N2^98nTCY?MzHab3G+Za`ye7@*JQN+j>E9q3x#Ux@NMBp!9GCGC{NgTD3T{z4{CYAZd`7Z`W$Ltd)PmLHuafAK}X0nBvZNubB)v2ZGm6{8yx^ShIb=ed&dDb+|Tz@8(Rg#s_lBaXDlv7gF)RLv8sFq?{>d{iKmin~RucZMk4QeT+rL>l`e^KpURQngz{>8NAnD#WLJ&idC!jLJ}co^s$U87GiGAGYRO>@wRrG=2|?-xR*uTKc+UMcita#Ayxm2=DiA(**dAy|%_9L-8Qv5cJ4lO7bpK(DmZ*DnPp<p?1=pe*-g<X$~elT%w{oR}QSMum{dT5?WGYD}K;?D<k@+E$6bWCC;^(RsSdu|SNYhIJWcl?vrTzLqM<sBF;37}INXgZ(}|I*f~{QaYPrL)-NBkbHL6jY3YzPWOc26kW#%&W(uYBCMIE?_pc``HJ4fLQDAYE4ocQOGX^<+1$F1ggF5E61_uTs}%&R%_BaOVkdBz5LO+s^6<e@s!)!Du{g%f8#8eM1Jg?Ppyq?esQGXQ#sbPsM4C6Y{HocjsAbaZH3W0MM~Sb&2rPjqpi3fh_#o`w)%7V|pg+<#ILE7(bY-2KQBBoc$5z#7=L$s!XDa2oQ?9#YsLOzVxXPk^_VaW0@$r#k6C)U-&!F@%eMo<%i)<{BWc7a-lwVcK4h*%Q;2Q@&k$7&hXS-AiG(ec|(;d2@gBhB2;{fEx0BjMKDN`^K+hZ)uS!N1SwMt*Kx0rB?g^a_U;}y9GscgXX**N@MrZ)*D2{S1UMUsU04kob*kCz-uZ)ih1)b0f0l$-c}oSH}u=6=v00Cdlk0+P=YnP>Ip)Y=sf6aqgdL-jgc;uyY1pT|M542AH9@VZo0<Fn{am(p%{Ij+;I$B#{5X?qz?cg2e$i~S=goCdwF3aR5+3uO_h-)RG*56?gR@%P+^w}_uO%1U+tvb>0opB<NJrSIT*hh7OQ{X|fa493bW<T>pyw|}BbTA!(u(iMJW#ZG!C>$n*<pf;RprI(MZB2^`!6Wc>+3I1;>4BgXlMG*!+_LuBadd$RI`l5yVE=lI&aPI_W515yc@H8Cu?KZl+XCvWpXc)X|drBW_>fYD8OGuXt!BfN|eT4x=+&s|<Svk<~2*7ipkY^782PU!XC)LshU7^27{IEQ%Yg&apC(B6hAv-KyA&j5by!vPW?pBDj)uAweg?QjTk&z1SK0o&52sRm2ab{pc8!batQuS`bBd4%Mn5Oj{RVgdSD^*uoS%RG03Sm-yteZe<bNX1OSMee=^Kyn@hz+`mB{Q$nO}$ERv8aq5$k#qoEcQYcr6;+ECqd7RsrNN!a3netM0{i&PSfk&QXcQ{_lTy{Cw|)Fg9HO@bDCuw$n9{r!Bde(#F!p3rUfz+&>%%4Mhs2{=TAz;3(VxE-b>EA9@_2%`j*=sqhmcX#g$M>g0;52JXv!3ZK6OdU?Z|N%?nAQM2BU~hiD9^Fg=b{5MnrQfaCnhw5`R#RPt^CzmQv>E;`7kQ6$T;t#`gpSA3vjuDVV=Rj=2uf__xl0NL`%roS9wP!2Is4mGEKzE(ECoi5%z<(<0MJJnNZXr6dOl?5%-dA4GITY*OJ1YD6E)lC)3x%RJMzzatI{I-oG9WK!wkGmOL6G4kG=bdc(Oe@-Uw!Bt2sUH6#u>I%Dj`Pi&p6~4d%l>L~TxOZ=ee)e=nXdQ`v(<cZSFK@(euunwfMT<5w8s@h+PTrKEXiUrjxaxV5j?S89P4lEiWey_2Hvr>qp5P%=iPz0`T=*`z}Cd0|5ZA}!7Zt6j^2WOiR5_fe@%<3^MDgVK6-m-gS^`lX<umq@2nLHzxIR?R*+SXTAC_*lH6ptP4R9$A{7yXV_mJbl7b&p2TA-TrI;qH9p8UY@RIVC5fp2SWhN9~F$l=2lzHRBs+!BJlpQ+<Z)$k0S1WKeg12_gpBq`loPzjkQ4e)<odkev1Qq#1yEU_m81xs`nAHC89iY+{As?G_bjW2l!`Z8&<HJncY0kU`vH4(q2!77&!flbMH<5A35Yc|*Ys~_%lcm{wu*Ft9;VanZ3)xa9BP61?XY;kbb28brR(Yme65i;mghW#eOhJ&vHvU`2EPY1b>X?Lgfc!eYu!e{a-n<#;c#%<Oit<=92Lh1RIFmInFMuMo0%rA!ovmcty`WNP`1r~Ug+rhR3btWU-9rW5(EcV$HsGNuOa6v^0@(DmB@yGhh;cDuT!5F`MIPP@5R5a0JRokee8}a=odSqJGFBQ;A=81Lf`1&Ws*hq`4x}W%F7m72Dt*bmu<ZSw0XD?v%VWdC_Q*N*3G<9?W8bGsj9?GgTX>IAC=swPo?&BhWotvgm$WJg`4@#8s+j'),'Libraries/Compiler/gram.data.☾':strd('c$~c&U2hcE^{-6bSUcmzk!@^TgGLL4w2A@&8PcTPSw^$FW3%$^c(c0>AWY@P#38h?*4Z{7uvr=tLo35WlK|nNNRHIkzVW{E3;Yv$&OP^QKGrr;RR_qq_nv#sx##Pid&aK&^NpWxoj7&MefQ&YXQwZmcU^O~I$!jvP18DLn3>;9pE#2_WMrJc3Fhl=_@d)h0|S3-;}7A|PlIRAxo6Iva!<P-42DZD71GsIq~Ar58flcKW0V?cl%_RG)k@2Vp`3p20xj=utZll@x?hT5{Px7Od;Z+J?+^|yG+SkN?s8cmoWF3&egC6V=Lw-$opVdoKu0)v`hEAE(;sL^NCgpNND9FTYF;IPwb_POa|h21;uM4Ve6v++HI4A*V`F#Yn`eBjG+(R1ni)QLW;R<5wj6k^%BMaom3@m%Ad(-n7>u0XUUZxQm|8=eO0(3cBNg*M%K%pDEgS&6P`By4AD$b`;s&6==8IzfB+V0_=GCTK@~Tz0*;=Sq$}Z7zFL|XoTIT}BWpDyI8!$zHpYirT7~p(3GBPqVGFlvWGRK^Zl_hL67V7ho@0A%IC>Hn<>@{ZtPG#*+yBqCi$V0%e5flQ>b90H|fa-85Tv>xZh$zY0MtJL6w+!CFv<N1y&s^arDQj@8g~UiMM%HHDq)U$L8MK>WDrQlP?FSq~B6LW;^-kIp{Iv|CsFT@w)t8DD;dj)5pp}ZSjecTD!TVw)1z$4~Kl=!|CWQpA;7Vr!8R2y6TPMTMe7WJF%aZYyX;PjOb-c-jJpSd1G{JIgE}<IXPb~5%`oSmL5&J2bg>#?}8%Fr_J{<CIAgrDnh_{kWB_AbeiZr%3bIhVC2BtJ4esI<hc_%7F(mp9aDGd54OT+{Be39rVQL$(wYihbnJ0~eP61{|NVWO(bBt4K1|M+>>-6{;Q%m;WI@V70KqeUnyVfRsC03*NsD&|UgP->s8I$8nHVo8Xg$x;6R`vq>1WuN7k4CcXPuu#FUz7mgytuGHoAl$k|B-+noB(5O=3LT`<e(qLUek~fShlKm-DArIql9lTt!*wA6aUfrS(cGtQ;MMphK5o=hUjECA-HpF~#vMuDVfP902hZS^**}Up!UZ*|4Wz2pJE^|jhX}I}8NntLnObFP(loucD$$cETx#5m<06&b?R7eyHDocas~Tr>?y?IC`<g;+a}PDdNLyOKb=W<qg(~U#3k8a^OL<b{SE(|BYGsL)DX(3w#oKMX+O?b`xppF4I|t|5*_&%8#<jx_$W@anS%-_G<3#AJN;=JIrQ~ZB21nMg7^T7Y1`W(@T>r}=7GBAq5KAl4!>LA#2Z{3kNHrF(3FRe$^OahCzCon?D-v9oz2aUG^r~L1NOfnhP%HWk7Z9}}kH84k=*@;Bi$Y{$iRVEkH;%wp_lSTv8di&P0)2dA$^S$tf{|a9j8<7qyR(faa4)%VRxk-9ik)qxvxu!Dgfy+P6KGauT=xyJxICO7b7mUHGx~#vT7ucMMAl&E{Vaj}EQ0I=WGGgEn3peAnsa`mX|t;y-Ss2)w5oon5LP7+Tc3{A5Aj+eNkvy1Bg5-bOQ*!PB7pMQCW0onNWI}V{gxpfUisaPyZ_{8EKSV_$QzZ=VF^u0Xi`E`5-LilEFnp+I9kAm$3BPUA_nt~npaJhqTl^F;iGHIxhT%c7T_F^k91C37GIkNF)-eQsuee~zE{BGW4x|WMzomG&{cIe-N!}6Ug4<wIH^E~dXeSEgQWGNd#802x$ZS)n{I{K$TV>T16yOr)CnY#Q3{jw7HpssaL`O3%ew`i*_>U@vT}mAuk*%pF-m(d)n$8g-ahBem{3XVWQIhknmMkF+y9~A1U&U8UHdUUTuf6pgD7M@iqng#vMu2IKegtKJ+R0-)7%yt7jCP$P!vr9H_!(y5VYUUMDh)vybunj+#(ur$%m387E}E(ASHLMi&qz!Lc2Iw#&ZIGe<t<$<atyiAKy#jT<j`D(4AdqHBpE=HzHF|Y9mi4P)KYK(;Dc>tpowTg#}gG$6`af_Y=>DWi&I{69(bdjj(+W{*XnZubu%~8lcuqa$S&<k&dY+m%JN+2_~<h<RlB^`KAj+1qk}@$4syhGhaMe$d8N`vWxlovj7cGB6#Iv1gE^=nG?gmE@Z7m6NiPY={RpQXvoSf5+G)>mg(oSjx$`y@o|nWfxw@QG9}R_ONYy5UclqO641m*A+Inb<fB*;Th32R=-9&&VLXEFOY|e@=tm?psU}Mjnvs(e<D`vLB3wV|YfNK(miq4kt;$hRsJ9=gP&k#16ez;vtezxG2n<$d+M>#AE<lN?nv;+;AVt_|iN}w6VZsSzf{J7T>}&#$bduhIN%BTTv_}!Uk)wGr(y73PHEb45a`Cbit!`Wfpz6+24p7Z>tos-0IgZeXAv7WgoHo8<p58ZA*PdSvL=mo{#1dysY4GkkuZV{%MYSQymt=M|Ra0M5Yot)a66EeWiO-BqU3zxEMtX=pKqjH=wey3@SrEj$lNN12Ai5<mOnd>romlkBGNZv0k$(>;vevIDJJ2dAj7)hG*Cwtn=8qjc6mCDT;d#IFD*WmucXR*nc=***xIf_*f~+5QzYDt$!zVD@1Y%EzA-8|AyV2bSp!=iPGd0<3zv#8U@2!2_TU+Y2@ATSV_ttLq+CTQ%_j>Jb1YU7UM3Y|{f$|gT!2egdtjfl>1|U;AdB-W3*0t;5)|cVdEp&5q;4Sdsu=_ad{+(_U6_6^9RHT4T4Z2kD&(h0+{7Rx-)$((M?wT=2jdy^w9nrc+ba4^ZJECF?Fsp#^iG#7R^b;Cz=_RbQXl1^}47G$NLi=dOkx)@Wo`gztI(TAf@xkf6K*NL8(d75!j<SSiB;+gmBRwwSLnR{nlCsA)7%UUtlI7&n`|JykQZk#STI_05QHs?KlEDA6K8!MMVH)vk_10BaG&4*p5>*(gf+w|bq&|o{>jzXHsn>g)PPAMz6TyzDft|`UbH9kJSSI_3Wm!YfBc{^ON>6c8-bd<F$D#Up{g-^gP5P5l)OY6!h}Cw$Ka)to#-8k8Duo^TZAOVK>QA_|F7B1mcvyG0l(>cLfRgu(>F^{WX=t_ZfoUA0%xpML3(O{I1*AVwQsZzm;!tCjLL7}~8uUECY`gMY>Q=fO`K{b2#bp7qzrX_p`m#Etn2*JoGy5Eb``DXucQT4SJZ)qw+NsVsH3{xE!1bw|%T9!$)GHtnwpy}DT)$cJ>VD#V5n&~%KyG(Sm%N4u?37UGZYAF(QG`dr!zDS@kK*d#3cLM%;o2Bn|5ATSD$4NM0qnh=PyFl$bYOCS76BkH(1}Hr6HvpJN@|3Q4aoO2U7Ih*pQN#Dog2!+Ww5hd=$EO9kQWdkuqhk1=4)A6nQti0h?Qoy!{ho_4ZchCnqiYgq{2J@;>YM)Y-gaxaxyu?gp(cRC&UsI!KVL-L9G~#gC;Qla*~bqn6QH5!g=+2_3Ck3Fc)-jFQbct*~a`rUCPcSw)lr2g}|}l&F=>in;C|mb++YISQ!onIBxT=LpL88;!IYK_atz#*_u0UgL?~!h-~tMqG(A9ZRqP3h7K(;-b9Isl!%(g`_O_iFF_6dQ;#q#Hnb8jqb(Mri^a&I7hUvlv3Gl&c?9-nGV~?!&W+@~ZSvgZ1dDmh@&$_(9|kMzp_t!y16~VkkHvm9g8kBr%`bmv!7q*-S^T91)eWExnK>KxInM7bcyaG`yK4}|@Gq?3|HQ)U)%?ZRt1$U`m8SSF`(!NZzm}s|00'),'Libraries/Compiler/ast_to_py.☾':strd('c%02!TXPdf7JlbfOsI0E#}<ktLPA`KU1GeKiU}?tsjae|DOnnU3VAe{83%g_Def2&!p(LFfdKIm?yyU4Kp<4nRr|WXA%5Ja{DeKHZ__gxjYQ1Dy2{q5r!VK$=X~dMyY9E9jA^$~ZPlDwC9D{YDX-;+MkBD@mOoW#HvaC^R@JfBZfAB+%dg2EyZ1C3LAZ+0!}P@H_P-F@#;3n-8Qr>VhiwznclP*=(D4H^XY6dYCM(T=SUJNqE%?hjZ`!>1&m&vk-ZZk^9vT_m^ezlzv%NEnJ=Gw1X3bki;dyLLaRL^-N<X8gjlr@(57IMqkyzMtlHRrh&#9K7@oRcyXwwb?PhZhn#9Y33ZhX2_D7>}9pLXzRU48lD7rg0Du!?M3yvp0&ZMlw#3ybODF$in+?me}%$&cRRqkJcv_FXa6y@R}Qw&65uylwowLZMJE6enNjuWC+HbUyl+w^Unh*l-nz$FA|_N#CjLPS7*i+-+BzZU>s4KjR}Cburb$^Sr@n%BJU6Ws72eZa;6Tw|t%AVxhQR(ATU4K?)&pBDQSZEC_*)SLu0rplpiy*es?+;JZ^ORQUJMpH0l!@^qd~(>Xd%%uhb)>-*q?S6}`3<Bc0PY#11Let*rHHOrqK>8C%v239s!ny`!kLuuvFDL(sauL<rxJH#9M`$fZXA>NH;+3*kEut7Bl8I@JT72fcQY?!;j8>GaR=dSaHid*Z@<@p`{-ED=k$DGiXG@iNRs*9l-j~@}e0@-j(HW<(`CPK?vMTXxU!YyLb{qz95I0U=s2t7)Vfi#cP6ZBKqLnrCy^c2YV3_VNF(RsQ+7eQTL(hDHNi}Vs`;4-}eD*T2n(SOiu^jmtJ-k>+>Eqa^Yp?B#$dY}H2{);}K-_h^s5A;X+kUpZ1>Cf~DeM+C1K*hG9%}B-2d)u~=W@T!!RzWK7(Q`Ted3F##7wHcq-VEGSCaas?9x9gBf?7@6M4q;f4)-+MckQ#GIA9+73!BJst2hywYHS`h{vo|bKxXIZgSMB4K`KAeJ48I(73-kvmq4hGQR?tzsEnUh^p>v+3)h^ga9kix!WYY>(vd~LT@q0u8BJN=lHI;m-2@>>%INU>y^+E;^kJ}%d3s%KX^<duyT|AwH908T;(yr!?+=fzV1Z8k4uJ7JRlUF>tVjkp$2as0N;zkU!83z~x%}{6U+@Rh=rhPnj<KI49p~YH8R_1v?F3aj2>lKmq^rjqAD`|E*gAqIrX)pe@eS^xgll^pUL2y2B0VX4vT~NusEc{Q2N-+%&2e`;93LMySMS|t?laJD8?rZ&3`?A&hml-K)l8XDxs)?z%dZ>#hH03(eLn+pX*OIZATuJ!!oDJ;l!I@3_dyHLJ<E2`Q+f#9GEl&bcva1*8_tXeKF+QLq3z8g{R`kkp5zR$sxtgqgR2bqK_0}byp!L-8}Ww+OZBp?b7+*ocl~zhi#hl`Zbk#46PaR4L1ll5DimYJ3KKas0fqxB8ihY3lv|$rNu`ys2@4^_Y4C_&k*QP*Ek@eNqfa&%;J5*C=J?~~<3IoU!^Qtzykc5hE2U1If1SS}`xKIWfY%EbO`%p~?J0f06dPlq!t@&gt86^q^Z3<5c@_EaF<9?3u17E^^b3uLTt4Dejv+Dm%`&a_38jTypif8}Au#d`{g&w=-BF=6-sVPmlSoFjCCegUL3^AVVbfxHKHd~aWWDniS|B0F;^*{x!ljmz%k@_*&PXLeJ#4#>nM8sM0bixnNU#Y_MeUi{%u#wqS&Xu>BA8AHe{&d<I))@9Zh`*7KF^8I%kq;md^R8EwCxOl(+L4UPbo}XlJvlHQF|^(guHopgscUKymq3EM@B2NoNlBD<p9H`rEMl;u%D}(`z5Y@X{<^XR?0p``xl_>w@YUPX8HG78+^3wRs6~nAj)W?s)4{isg@I_ES%~BV2~&TFsXf->OIaJGY#-k%Cw}KwavnJho#=-t67_bGl(cU!6Ghp^tVf=e~P=RHi}{$@CU%QQDs6BUE{CCJctCVYLfYfW_vIEkqJcG%PNy+Scbt12VuW($!3{?S!+~7=-FSDTxY3gukLBOi*jE_Q3|~sGJ7?Np4aTGKB1XsJ*+wQVrx!x<8v`<%~)K^B48|NHmVLO<_yeSt&VO!n;h<A-*nc!nJtJ+tD(Pu!$h-Ddo5$d<&&BGcVFtA;a-<g%&lM9id#o}T@keVd9PNSs%k5r@WJqw1vip#XXtskM`OM&Y88|KiUrt_cn6b3gf5v8a>$gxPA9B{FkO!_*xp?Tnac$)zT8SIO2ph3S#GJ@au>w(*Tm-%sN9l><)#i^wT(JhPN+U}7tNj5h`<=WNFNA<tmcm4XWk`=v6+Po@OQAJ0Ir|W)A^Ri&4&;PG!TKX%9+J_))iEerpaf4g)M~=cnwcSdc0FfV$Im>SgOOxlOW#XI3^j;HyCR<i45B>F!ni@PJXME_YDZMf;SefpWlCe=Myu52YUb?@$A#H$e5<39AEQ<_<SI?84tZmmScjB3FfE|(*5+96^&GuC!Bhz-Kj^BjGIK@40dA!mW#%B2%Nn}k?cT<&PKDw!0k|HK|~|c0!R$GcarIln8yyLCv_DmxXv`e(zOT#Vv4mGhjD?6WP{P3qL;;f5RjSgHhgg<@d80?gr|!ZwsiO5tGPteGa=3uH-Z!!LLw}!;6MhVniA%LH|b$w_JPMJVG7@e`Hz-6qU>a*#AxXQIF0WEH<3y4FR@fd3|Vb4@`>W7Pgw{6YbK?xi6crfo^oZ|$Yc+paeRE{1&S%9WHIFqNK!Iu<uVCEN6ropGN|g5dz`0VS}M=wdt5t>$V0@8=*Ss5Not8~(qd@8ldSq96(+;Vgr10?KT<ZML(H~bso+5OABv}#W5{F$a*rNZ`G4mnp3yFe^1f#`8==Z>*;*NSZ8vK|B2t`1dcj)M2;pgg9wPi~E~jWzCtUnsD>?~dg<vcLYa2x?1Qzu|Ag==Ecp<(=)BW(Hiob#l#eGv>u$sAm1ev{WpG*6*^T|XUjC;DQeE-sZ=R+>c-Fraa3uj{}taD|lpgpIU_)Dt&WOJ#ftmTe;GIV+38!Xji=urzCf9#mdVCk4`%K`0mB4R|nvA~=_!11xg2_se?v}3(XiQc7&c#I@0;3=@(1<y={_VV2R&H_koNL?U%b~Ty~kwKDIJAw9BIpJp$&IoHkT3NKH$q#G}r-@#cbU--BJ*JeTw%FQ^i=jr;6s!l}3|?v?JjTlz^o3-FiMz+R;dYc^wKe6vpbX>bu`Cm7lysF<x}<)Gpc-|3wzWwh-m?@!$9H=v2#~hYt6EQzl3Ff6s!3uWXs@$jJIcQo;)I@3t56VVJ66I5J2RC@7t6<Autt_#D{FUS%CnM+0UM7dm5j<q>9v?$0C*RGMvVTJn9GY-(KQUn7(URkOMha*HJGRHGgEd1mYR8pqpn*5zO(QeKVw;A6eV^|EXlV9TT^bnWFjFBP_>AHha}fJpQ}g7-5@`M&cx*WiU?j)an=`VDLMj@n91cUp69qVqNzVt?r5tOY&42pYVgTaxV_r00=#;t>R~;ZX;$NDrWUqK5VlL45tgj(O3PIH$xxy>MxZ1!BXw<~TPN47n%XzD*`1lH<ArRm523}OFo#&CJ`@FS5r6?>oz;V?Q3=Gr*x}v~lYZiCZ@ON1qtX_U84SYe--=*RMs=jka0I`7!JvotoFwX$yk($43AM#7F>!4xx}p^|z?ZbNAXz3Fi{_umNFm$(RyE&n1IG{1G<ZoVBP;`PUVSG0#EPd)uP_9}m@<16quPI+;8c(a##zZhb1EuLI7#RAa*qNrS?Co+o`%XvbT=e^k70&gU=Vj5&@ppdWbs1MXlfOy_97*u#JvX@XGRl+;Otsb-S<dm7Yiw|m42m&zpr|-5GBe>@sm_Mre}i988yZ?%O7RA*OE6!Sl<&FM^HWJ4TP;@1ePOkU8ajET_}m0DB|!P)u@*P@rn#~snlw=*9!D|GSSv*lnaCHxm(`ReWj=SO47)s-Aal^f-bbwk|dIAllM0VjRxk~{EC6dv{^QPN2l59pjPf$W!Vs{wqdC|1i#mT^3!~F(+Av-?K?XgEtibs3{Sh+gX;JZ8{z39WbN8c8$ki{+eIVMwEz#J0qjc;LSEZlps|rLd_N&f$zv$d16r(!iB;YDNvrE0QOyNJR>d4!3}4}}k{ZV2rktKJI#ux`quaMcoJO`d4_Z9WE$nVL@I~YI%St+2(<I6l;y3ab5e+wN*@0gLV&XN4MS5Qlq^!%I(j3_g7@HSku4FM`>o3%40t@5#hMuDLJB`xbsexRVT)!PSk7G>0y*LumByJ9Z733FZLY}t~FNY=M16C{)rCUqPkqcAMc4V9J#E=cFfnb{88$iFFaMmxQ;L?sXdZd!cHI+&sNjdx_6O2EIe0_m@v1WdZ?HjRYGEnb`Mz5~}Urw=NVPwpIsr1G~T1pYAwynE~v?N8kcEuzrOO9n}Im0a%G%0S=B1+ziQdF_iA~e_KP7qrJkdcf2jgN}08w;T$JnU7QPQ|sIw6HfA5rV*i9)ihkX8{Nd#!flqA|<nAVyU~l^4_15F&oPdT*KVq{pWxw;uaRC72ptlu{9mq;29gPJ%xDF*PY`jdYS!wD1;s1ybj(JyXHiA!qEcXZQqi9Oo$$9zE_kd<Sv-?)Qwxs>GKI$h`&xRleV~{F57a}QGdWj?3yk2qB$0vL*H@A0;Rbvn98k8Irc{tKaj1y<H0x4NfQ#A3>m98noV0a*t=RyC$J|gL8Gc059xI0w_lus1Jaw|x7Bnak{3xOUMJoxON&V|p<&492vOC96oXY5^ctNfT>u;IEgiGzo3Q0EK({iige=1>`i9LroNMlm6n_lkU5g)}FqSoxm)ORQy3%pi+tYZaE>zvt7lh5b@qgfg1=-iopKa?3@AA_wn+DaN=T9(!Otg5O%uYEkV4@EaUeZ!JZq?>ctL6-jyW$8JH`^X}dJ5-(%%WU;a~%l1oCL)6odAZ-w~Fgb1jI*R=U`pxNpu9oj&k+29?_#jn7KLZ`z;pEyxDM9%N4?CxI14l1Q|#wPN4n=%^v<6{?poa+a}sSsu5FdI>>|6GkXJ>g(=fSV!l6&H^ShrW&ID#8k$r')})
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
(compile_files := (lambda F: Âøî(ÐôÅ(F, MOD(lambda ÂîÓ: Âåß((áÕÃ := compile_code((áÖï := ÂÞÅCAT(ÂîÓ, ÐØó)), ÂîÓ)), Âçß('Compiled %s %s ⭢ %s' % (MOD(ÄÕéý, áØÁ=dotrim)(ÂÞÅCAT(ÂîÓ, ÁÜÙ), 25), MOD(ÄÕéý, áØÁ=dotrim)(MOD(ÄÔéÄ, áØÁ=áÖï)('\n', '𝗻'), 35), MOD(ÄÕéý, áØÁ=dotrim)(MOD(ÄÔéÄ, áØÁ=áÕÃ)('\n', '𝗻'), 35)))))), '\n')))

def refresh_cached_imports():
    ÐÌü(TP_CACHE.clear)
    (reimps := ÂÚü())
    for k, v in [*__ÄÊIMPORTS__]:
        if not (v is not None and (v.hardcoded or v.name == 'Compiler')):
            continue
        if ÐÌü((f := v.__file__).is_file):
            reimps.append(f)
        __ÄÊIMPORTS__.pop(k)
    ËãÂ(ÐôÅ(reimps, MOD(lambda ÂîÓ: Âåß((sha((c := ÂÞÅCAT(ÂîÓ, ÐØó)), {}, {}), ÂÞÅCAT(c, moon_to_py)), Âçß('Transpiled %s' % (ÂîÓ,))))), lambda x, y: (ÄÊPSH(moon_to_py.áÐñ), ÄÊPSH(x), ÄÊPSH(y), setitem(ÄÊPKE(2), ÄÊPKE(1), ÄÊPKE(0)), ÄÊDEL(3))[3])

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
                except áÍÚ:
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