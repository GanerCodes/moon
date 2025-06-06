
__file__='/home/ganer/Projects/Moon_BETA/NewMoon/base.☾'
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
(ÄÊÞSTK := [])
(ÄÊÞPSH := (lambda x: getattr(ÄÊÞSTK, 'append')(x) or x))
(ÄÊÞPKE := (lambda x=0: ÄÊÞSTK[-1 - x]))
(ÄÊÞPOP := (lambda x=0: getattr(ÄÊÞSTK, 'pop')(-1 - x)))
(ÄÊÞDEL := (lambda x: getattr(ÄÊÞSTK, '__delitem__')(slice(-x, None))))
(ÂÞÅÞCAT := (lambda x, y: y(x) if callable(y) else x * y))

def ÄÊÞCUR(áÍÊ, áÍÅ, *áÎç):

    def Ëðá(*áÌú):
        if len(áÌú) < len(áÍÊ):
            return lambda *áÑË: Ëðá(*áÌú, *áÑË)
        (ÄÊÞPSH(([*áÎç], {**áÍÅ})), ((áÖÒ := ÄÊÞPKE(0)[0]), (áÖÝ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
        for k, v in zip(áÍÊ, áÌú):
            (ÄÊÞPSH(áÖÒ if isinstance(k, int) else áÖÝ), ÄÊÞPSH(k), ÄÊÞPSH(v), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
        return áÖÒ[0](*áÖÒ[slice(1, None)], *áÌú[slice(len(áÍÊ), None)], **áÖÝ)
    return Ëðá()
(ÄÊÞPSH((Exception, object, dict, bool, list, tuple, set, str, int, float, bytes)), ((áÍÚ := ÄÊÞPKE(0)[0]), (áÍä := ÄÊÞPKE(0)[1]), (áÍÙ := ÄÊÞPKE(0)[2]), (áÍÖ := ÄÊÞPKE(0)[3]), (áÍá := ÄÊÞPKE(0)[4]), (áÍé := ÄÊÞPKE(0)[5]), (áÍè := ÄÊÞPKE(0)[6]), (ÁÜÙ := ÄÊÞPKE(0)[7]), (áÍÞ := ÄÊÞPKE(0)[8]), (áÍÛ := ÄÊÞPKE(0)[9]), (áÍî := ÄÊÞPKE(0)[10])), ÄÊÞDEL(1))[1]
(ÁØã := '')
(ÄÊÞPSH((1 / 2, 1 / 3, 1 / 4, 1 / 5, 1 / 6, 1 / 7, 1 / 8, 1 / 9, 1 / 10, 2 / 3, 2 / 5, 2 / 7, 2 / 9, 3 / 4, 3 / 5, 3 / 7, 3 / 8, 3 / 10, 4 / 5, 4 / 7, 4 / 9, 5 / 6, 5 / 7, 5 / 8, 5 / 9, 6 / 7, 7 / 8, 7 / 9, 7 / 10, 8 / 9, 9 / 10, 0, 1 / 100)), ((ÃÆ := ÄÊÞPKE(0)[0]), (ÂÑõ := ÄÊÞPKE(0)[1]), (ÃÅ := ÄÊÞPKE(0)[2]), (ÂÑø := ÄÊÞPKE(0)[3]), (ÂÑü := ÄÊÞPKE(0)[4]), (ÂÑò := ÄÊÞPKE(0)[5]), (ÂÑÿ := ÄÊÞPKE(0)[6]), (ÂÑó := ÄÊÞPKE(0)[7]), (ÂÑô := ÄÊÞPKE(0)[8]), (ÂÑö := ÄÊÞPKE(0)[9]), (ÂÑù := ÄÊÞPKE(0)[10]), (ÄÝóú := ÄÊÞPKE(0)[11]), (ÄÝôÀ := ÄÊÞPKE(0)[12]), (ÃÇ := ÄÊÞPKE(0)[13]), (ÂÑú := ÄÊÞPKE(0)[14]), (ÄÝóû := ÄÊÞPKE(0)[15]), (ÂÒÀ := ÄÊÞPKE(0)[16]), (ÄÝôÏ := ÄÊÞPKE(0)[17]), (ÂÑû := ÄÊÞPKE(0)[18]), (ÄÝóü := ÄÊÞPKE(0)[19]), (ÄÝôË := ÄÊÞPKE(0)[20]), (ÂÑý := ÄÊÞPKE(0)[21]), (ÄÝóý := ÄÊÞPKE(0)[22]), (ÂÒÁ := ÄÊÞPKE(0)[23]), (ÄÝôÂ := ÄÊÞPKE(0)[24]), (ÄÝóÿ := ÄÊÞPKE(0)[25]), (ÂÒÂ := ÄÊÞPKE(0)[26]), (ÄÝôÃ := ÄÊÞPKE(0)[27]), (ÄÝôÐ := ÄÊÞPKE(0)[28]), (ÄÝôÄ := ÄÊÞPKE(0)[29]), (ÄÝôÑ := ÄÊÞPKE(0)[30]), (ÂÒî := ÄÊÞPKE(0)[31]), (ÄÝôÒ := ÄÊÞPKE(0)[32])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((3.141592653589793, 2.718281828459045)), ((Ïî := ÄÊÞPKE(0)[0]), (ÂÐæ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((inf, complex(0, 1), ÂÞÅÞCAT(2, Ïî), ÂÞÅÞCAT(ÃÆ, Ïî), ÂÞÅÞCAT(ÃÅ, Ïî), ÂÞÅÞCAT(ÂÑÿ, Ïî))), ((ÂÕË := ÄÊÞPKE(0)[0]), (Ãù := ÄÊÞPKE(0)[1]), (Ïò := ÄÊÞPKE(0)[2]), (ÄÝøà := ÄÊÞPKE(0)[3]), (ÄÝøá := ÄÊÞPKE(0)[4]), (ÄÝøâ := ÄÊÞPKE(0)[5])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((-ÂÕË, -Ãù, -Ïò, -Ïî, -ÄÝøà, -ÄÝøá, -ÄÝøâ, -ÂÐæ)), ((ÄÝîá := ÄÊÞPKE(0)[0]), (ÄÝîâ := ÄÊÞPKE(0)[1]), (ÄÝîä := ÄÊÞPKE(0)[2]), (ÄÝîå := ÄÊÞPKE(0)[3]), (ÄÝîæ := ÄÊÞPKE(0)[4]), (ÄÝîç := ÄÊÞPKE(0)[5]), (ÄÝîè := ÄÊÞPKE(0)[6]), (ÄÝîã := ÄÊÞPKE(0)[7])), ÄÊÞDEL(1))[1]
(ÂÒå := (2 ** 3 ** 4))
(ÄÊÞPSH((lambda *áÑË: áÑË[0], lambda *áÑË: áÑË[-1])), ((Âåß := ÄÊÞPKE(0)[0]), (ÂåÔ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]

class Named:
    (ÄÊÞPSH((lambda áÑÞ, s: ÂåÔ((ÄÊÞPSH(s), ÄÊÞPSH(áÑÞ), ÄÊÞPSH('s'), setattr(ÄÊÞPKE(1), ÄÊÞPKE(0), ÄÊÞPKE(2)), ÄÊÞDEL(3))[3], None), lambda áÑÞ: getattr(áÑÞ, 's'))), ((__init__ := ÄÊÞPKE(0)[0]), (__repr__ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÂÞÅ := (NULL := Named('␀')))
(ÄÊÞPSH((Named('\U000f0b88'), Named('\U000f18e9'), Named('⬤'))), ((ÄÔýò := ÄÊÞPKE(0)[0]), (ÄÕøü := ÄÊÞPKE(0)[1]), (ÂýÃ := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]

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
(ÁØÿÁÙÄ := (lambda Æå: Æå))
(ÁØòÁÙÄ := (lambda Æå: lambda áØÆ, áØÇ, *áÖÒ, **áÖÝ: [áÑÿ for x in áØÆ if (áÑÿ := Æå(x, áØÇ, *áÖÒ, **áÖÝ)) is not ÄÔýò]))
(ÁØÿÁÙÇ := (lambda Æå: lambda áØÆ, áØÇ, *áÖÒ, **áÖÝ: [áÑÿ for y in áØÇ if (áÑÿ := Æå(áØÆ, y, *áÖÒ, **áÖÝ)) is not ÄÔýò]))
(ÁØòÁÙÇ := (lambda Æå: lambda áØÆ, áØÇ, *áÖÒ, **áÖÝ: [áÑÿ for x, y in ÄÕåØ(áØÆ, áØÇ) if (áÑÿ := Æå(x, y, *áÖÒ, **áÖÝ)) is not ÄÔýò]))
(ÄÊÞPSH((lambda x, y: (False if y else x) if x else y, lambda x, y: (y if y else False) if x else x if y else True)), ((ÄÝøø := ÄÊÞPKE(0)[0]), (ÄÝøú := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÂÕÕ := (Âùè := (lambda x, y: x or y)))
(ÄÝøù := (ÄÝùÀ := (lambda x, y: not (x or y))))
(ÂÕÔ := (Âùç := (lambda x, y: x and y)))
(ÄÝøå := (ÄÝùÁ := (lambda x, y: (False if y else x) if x else y if y else True)))
(ÄÊÞPSH((__lt__, __gt__, __le__, __ge__)), ((ÿ := ÄÊÞPKE(0)[0]), (ÁÁ := ÄÊÞPKE(0)[1]), (ÂÖÔ := ÄÊÞPKE(0)[2]), (ÂÖÕ := ÄÊÞPKE(0)[3])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((lambda x, y: x == y, lambda x, y: x != y)), ((ÂÖÑ := ÄÊÞPKE(0)[0]), (ÂÖÐ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((lambda x, y: gcd(x, y) == x, lambda x, y: gcd(x, y) != x)), ((ÂÕÐ := ÄÊÞPKE(0)[0]), (ÂÕÑ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((lambda x, y: x in y, lambda x, y: x not in y)), ((ÂÔó := ÄÊÞPKE(0)[0]), (ÂÔô := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((lambda x, y: y in x, lambda x, y: y not in x)), ((ÂÔö := ÄÊÞPKE(0)[0]), (ÂÔø := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((lambda x, y: getattr({*x}, 'issubset')({*y}), lambda x, y: getattr({*y}, 'issubset')({*x}))), ((ÂÖó := ÄÊÞPKE(0)[0]), (ÂÖô := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((lambda x, y: not ÂÖó(x, y), lambda x, y: not ÂÖô(x, y))), ((ÂÖõ := ÄÊÞPKE(0)[0]), (ÂÖö := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((lambda x, y: getattr((Ïß := {*x}), 'issubset')((Ïà := {*y})) and Ïß != Ïà, lambda x, y: getattr((Ïß := {*y}), 'issubset')((Ïà := {*x})) and Ïß != Ïà)), ((ÂÖü := ÄÊÞPKE(0)[0]), (ÂÖý := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((lambda x, y: not ÂÖü(x, y), lambda x, y: not ÂÖý(x, y))), ((ÄÝøÄ := ÄÊÞPKE(0)[0]), (ÄÝøÅ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÄÝöú := (lambda x, y: ÂÕÃ(ÂÕØ(x, y), ÂÕÖ(x, y))))
(ÂÕØ := (lambda x, y: {*x} | {*y} if ÁØö(x, áÍè) else [*x, *[z for z in y if z not in x]]))
(ÂÕÖ := (lambda x, y: {*x} & {*y} if ÁØö(x, áÍè) else [z for z in x if z in y]))
(ÂÕÃ := (lambda x, y: x - {*y} if ÁØö(x, áÍè) else [z for z in x if z not in y]))
(ÂøÚ := (lambda áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ: Áÿú(product(*([áØÆ] * áØÁ if áØÇ is ÂÞÅ and áØÁ is not ÂÞÅ else (áØÆ if áØÇ is ÂÞÅ else [áØÆ, áØÇ]) * (1 if áØÁ is ÂÞÅ else áØÁ))), áÍá)))
(ÂØÑ := (lambda *áÑË, áØÁ=1: (Æå := (lambda *áÑË, n=1, r=[]: (lambda ÂîÓ: Áÿú(ÂîÓ[0], lambda x: Æå(*ÂîÓ[slice(1, None)], r=r + [áØÆ]) if ãÊú(ÂîÓ) > 1 else r + [áØÆ]))(áÑË * n)))(*áÑË, n=áØÁ)))
(ÄÊÞPSH((lambda x, y: x % y, lambda x, y: x // y)), ((æ := ÄÊÞPKE(0)[0]), (ÃËÕ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((lambda x, y: x is y, lambda x, y: x is not y)), ((ÂÕó := ÄÊÞPKE(0)[0]), (ÂÕõ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((lambda x: ~x, lambda x, y: x @ y)), ((ÂÄ := ÄÊÞPKE(0)[0]), (ÁÃ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((lambda x, y: x | y, lambda x, y: x & y, lambda x, y: x ^ y)), ((ÂÂ := ÄÊÞPKE(0)[0]), (ç := ÄÊÞPKE(0)[1]), (Áâ := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((lshift, rshift)), ((Âúù := ÄÊÞPKE(0)[0]), (Âúú := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((lambda x, y: x ** y, lambda x: not x, lambda áØÆ, áØÁ=ÂÞÅ: lambda x: MOD(î, áØÁ=áØÁ)(áØÆ))), ((ÂÙû := ÄÊÞPKE(0)[0]), (Âó := ÄÊÞPKE(0)[1]), (Âö := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]
(ÂÀÇ := (lambda áØÆ: ÄÝöì(ÂÀÇ(ÄÝöì(áØÆ))) if ÁØö(áØÆ, áÍÞ) else áØÆ[slice(None, None, -1)] if ÁØö(áØÆ, ÁÜÙ | áÍá | áÍé) else getattr(áØÆ, '__reversed__')() if hasattr(áØÆ, '__reversed__') else [*áØÆ][slice(None, None, -1)]))
(ÄÝöí := (lambda áØÆ=ÂÞÅ, áØÁ=ÂÞÅ: chr(áØÆ) if ÁØö(áØÆ, áÍÞ) else ord(áØÆ) if ÁØö(áØÆ, ÁÜÙ) and (ãÊú(áØÆ) == 1 and áØÁ is not áÍá) else MOD(Áëý, áØÁ=ÁØö(áØÆ[0], áÍÞ))(Áÿú(áØÆ, ÄÝöí), Âøî)))
(ÂÛê := (lambda áØÆ, áØÁ=ÂÞÅ: MOD(ÂÛê, áØÁ=ÂÔö(áØÆ, '\u205f') * '\u205f' + '\u2009')(áØÆ) if áØÁ is ÂÞÅ else MOD(Áëý, áØÁ=ãÊú(áØÁ) > 1)(getattr(áØÆ, 'split')(áØÁ[0]), MOD(ÁØò(lambda ÂîÓ: MOD(ÂÛê, áØÁ=áØÁ[slice(1, None)])(ÂîÓ))))))
(Âäû := (lambda áØÆ, áØÁ=ÂÞÅ: ÄÝõé(Áÿú(ÄÝõé(áØÆ), MOD(Âäû, áØÁ=áØÁ))) if MOD(ÁØö, áØÁ=ÂÕó)(áØÆ, ÂÐá) else áÍÞ(round(áØÆ)) if áØÁ is ÂÞÅ else round(áØÆ, áØÁ)))
(ÄÊÞPSH((floor, ceil)), ((Âüð := ÄÊÞPKE(0)[0]), (Âüï := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((lambda áØÆ: getattr(áØÆ, 'real'), lambda áØÆ: getattr(áØÆ, 'imag'))), ((ÄÝõè := ÄÊÞPKE(0)[0]), (ÄÝõç := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
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
    (__init__ := (lambda áÑÞ, i: ÂåÔ((ÄÊÞPSH(áÑÞ), ÄÊÞPSH('i'), ÄÊÞPSH(i), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3], None)))
    (__call__ := (lambda áÑÞ, *áÑË, **áÑÕ: ÂåÔ((ÄÊÞPSH(áÑÞ), ÄÊÞPSH('i'), ÄÊÞPSH(getattr(ÄÊÞPKE(1), ÄÊÞPKE(0))), ÄÊÞPSH(ÄÊÞPKE(0) - 1), setattr(ÄÊÞPKE(3), ÄÊÞPKE(2), ÄÊÞPKE(0)), ÄÊÞDEL(4))[4], áÑÞ)))
    (__bool__ := (lambda áÑÞ: not getattr(áÑÞ, 'i')))
    (__repr__ := (lambda áÑÞ: 'Ticker[i=%s]' % (getattr(áÑÞ, 'i'),)))

class TimerState:
    (__init__ := (lambda áÑÞ, áÓË: ÂåÔ((ÄÊÞPSH(áÑÞ), ÄÊÞPSH('áÓË'), ÄÊÞPSH(áÓË), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3], None)))
    (__bool__ := (lambda áÑÞ: getattr(getattr(áÑÞ, 'áÓË'), 's')))
    (__call__ := (lambda áÑÞ: getattr(getattr(áÑÞ, 'áÓË'), 'r') if áÑÞ else ÐÌü(getattr(getattr(getattr(áÑÞ, 'áÓË'), 'r'), 'copy'))))
    (__repr__ := (lambda áÑÞ: 'Timer[%s; %ss; %s; %s Remaining loops]=%s' % ('ID'[getattr(getattr(áÑÞ, 'áÓË'), 'y') >= 0], ÂüÌ(getattr(getattr(áÑÞ, 'áÓË'), 'y')), ÂÛê('Running\u2009Completed')[ÂÕÅ(áÍÖ, áÑÞ)], getattr(getattr(áÑÞ, 'áÓË'), 'n'), getattr(getattr(áÑÞ, 'áÓË'), 'r'))))
(tmp := {'ᴍ': 'Áÿú', 'ꟿ': 'ËãÂ', 'ſ': 'ÆÑ', 'Ϝ': 'ÐÌ', '\U000f0233': 'ÄÔÔè', '\U000f0232': 'ÄÔÔç', '\ueb86': 'ÐÌÛ', '\U000f04bc': 'ÄÔàÑ', '\U000f04bd': 'ÄÔàÒ', 'ᙎ': 'Ááæ', 'ᙡ': 'Ááú', 'ᗢ': 'Áßô', 'ᙧ': 'ÁâÁ', '⊚': 'ÂØÍ', '⊜': 'ÂØÏ', '🟕': 'ãéÜ', '🟖': 'ãéÝ', '⊛': 'ÂØÎ', '⍟': 'ÂÛÜ', '○': 'Âåæ', '⍜': 'ÂÛÙ', '\U000f0b2b': 'ÄÔüÑ', '\U000f0b29': 'ÄÔüÏ', '\uf071': 'ÐâÄ', '\U000f0536': 'ÄÔâÑ', '\uea6c': 'ÐÇò', '\U000f147c': 'ÄÕåØ', '\U000f7e45': 'ÄÝöÔ', '⪡': 'Âúù', '⪢': 'Âúú', '\U000f0e35': 'ÄÕÊÂ', '\U000f0e37': 'ÄÕÊÄ', '⤉': 'ÂóÍ', '⤈': 'ÂóÌ', '⟷': 'Âîí', '\U000f7e4c': 'ÄÝöÜ', '\U000f7e4d': 'ÄÝöÝ', '\U000f7e4e': 'ÄÝöÞ', '\U000f7e39': 'ÄÝöÈ', '\U000f7e3a': 'ÄÝöÉ', '\U000f7e38': 'ÄÝöÇ', '\U000f7e3b': 'ÄÝöÊ', '⨝': 'Âøî', '⟕': 'ÂîÊ', '⟖': 'ÂîË', '⟗': 'ÂîÌ', '⫰': 'ÂüÌ', '⫯': 'ÂüË', '\U000f7e52': 'ÄÝöâ', '\U000f7e53': 'ÄÝöã', '\U000f7e54': 'ÄÝöä', '\U000f7e55': 'ÄÝöå', '\U000f7e56': 'ÄÝöæ', '\U000f7e13': 'ÄÝõà', '\U000f7e3c': 'ÄÝöË', '\U000f7e14': 'ÄÝõá'})
(ENC := 'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýÿ')
(RCD := CURR(lambda ÂîÓ, ÂîÒ: ÂîÓ not in ÂîÒ, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'))
(SPE := (lambda ÂîÓ: ÂîÓ in ENC + 'þ'))
(PEV := (lambda ÂîÓ: Âøî(MOD(ÄÔÔç, áØÁ=Âåæ(Âøî, MOD(ÁØò(lambda ÂîÓ: ÄÝöì(ÄÝöí(ÂîÓ), ãÊú(ENC), C=ENC)))))(áÇù(ÂîÓ, RCD), lambda ÂîÓ: ÂÞÅÞCAT(ÂîÓ[0], RCD)), 'Þ')))
(VEP := (lambda ÂîÓ: Âøî(MOD(ÄÔÔç, áØÁ=lambda ÂîÓ: Âøî(ÁØò(lambda ÂîÓ: MOD(Áëý, áØÁ=ÄÊÞCUR((1,), {}, ÂÖó, ÂýÃ, ENC))(ÂîÓ, ÄÔâÑ(Âåæ(Âåæ(Âøî, ÄÝöí), ÄÊÞCUR((1,), {'C': ENC}, ÄÝöì, ÂýÃ)), lambda x: '⸮%s?' % (x,))))(ÄÝöÞ(ÂîÓ, 'þ'))))(áÇù(ÂîÓ, SPE), lambda ÂîÓ: ÂÞÅÞCAT(ÂîÓ[0], SPE)))))

def OPWRAP_(*áÖê):

    def R(Æå):
        for x in áÖê:
            (ÄÊÞPSH(globals()), ÄÊÞPSH(tmp[x] if x in tmp else PEV(x)), ÄÊÞPSH(MOD(Æå, x)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    return R
(ÄÊÞPSH((callable, lambda x: hasattr(x, '__iter__'))), ((áÓó := ÄÊÞPKE(0)[0]), (áÓö := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]

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
        (ÄÊÞPSH((áÖð, 'Deprecation %s' % ('Error' if áÖð else 'Warning',))), ((áÓÔ := ÄÊÞPKE(0)[0]), (áÓà := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    elif áØÁ is ÂÄ:
        (ÄÊÞPSH((áØÅ, 'Warning%s' % (' [as Error]' if áØÅ else ÁØã,))), ((áÓÔ := ÄÊÞPKE(0)[0]), (áÓà := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    else:
        (ÄÊÞPSH((True, 'Assertion failed')), ((áÓÔ := ÄÊÞPKE(0)[0]), (áÓà := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    (áÓà := ('%s! ⟨𝓿=%s⟩%s' % (áÓà, ÂÞÅÞCAT(áØÆ, repr), ' ' + áØÇ if áØÇ is not ÂÞÅ else ÁØã)))
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
    (ÄÊÞPSH((áØÁ, ÂÕÃ([Æå, áÍÜ], [ÂÞÅ]))), ((áÍÎ := ÄÊÞPKE(0)[0]), (v := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
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
    (ÄÊÞPSH(áÑË), (*(áÑË := ÄÊÞPKE(0)[slice(0, -1, None)]), (Æå := ÄÊÞPKE(0)[-1])), ÄÊÞDEL(1))[1]
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
(ÄÊÞPSH((lambda áØÆ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ: MOD(ÁØö, áØÁ=áØÁ)(áØÇ, áØÆ), lambda áØÆ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ: not MOD(ÁØö, áØÁ=áØÁ)(áØÆ, áØÇ), lambda áØÆ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ: not MOD(ÁØö, áØÁ=áØÁ)(áØÇ, áØÆ))), ((ÁØñ := ÄÊÞPKE(0)[0]), (ÄÝøÇ := ÄÊÞPKE(0)[1]), (ÄÝøÆ := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]
(Âõ := (lambda áØÁ: lambda x: ÁØò(lambda ÂîÓ: ÄóÌÁ(ÂÞÅÞCAT(Ïò, áØÁ ** (-1)) * (ÂîÓ + ÃÆ * (áØÁ < 0))) + ÂÞÅÞCAT(Ãù, ÄóÌÀ(ÂÞÅÞCAT(Ïò, áØÁ ** (-1)) * (ÂîÓ + ÃÆ * (áØÁ < 0)))))(ÂÿÇ(ÂüÌ(áØÁ)))))
(ÂÕÇ := (lambda áØÆ=ÂÞÅ, áØÁ=2: áØÆ ** áØÁ ** (-1)))
(ÚÑ := (lambda áØÆ, áØÁ=2: ÁØò(lambda ÂîÓ: ÂîÓ * áØÆ ** áØÁ ** (-1))(MOD(Âõ, áØÁ=ÂüÌ(áØÁ)))))
(ÐàÒ := (lambda áØÆ, *áÑË, **áÑÕ: lambda *áÑË, **áÑÕ: áØÆ(*ÄÔÙù(áÑË), **áÑÕ)))
(ÂÕì := (lambda áØÆ, *áÑË, **áÑÕ: lambda *áÑË, **áÑÕ: áØÆ(*ÂÀÇ(áÑË), **áÑÕ)))
(ë := (lambda x, y: x * y))
(ð := (lambda x, y: x / y))
(ÄÔáô := áÍä())

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/system.☾'
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
    ÐÌü(getattr((t := T(target=lambda: ÂÞÅÞCAT(getattr(atom, 'append'), Æå(*áÑË, **áÑÕ)))), 'start'))
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

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/ops_A.☾'
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
        (ÄÊÞPSH(Æå), ÄÊÞPSH(CUR(lambda ÂîÓ, ÂîÒ: not ÂîÓ(ÂîÒ), ÄÊÞPKE(0))), (Æå := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
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
        (ÄÊÞPSH(áØÆ), ÄÊÞPSH(ÂÿÇ(ÄÊÞPKE(0))), (áØÆ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
    (chnk := 1)
    if áÓö(áØÇ) and ãÊú(áØÇ) > 2:
        (ÄÊÞPSH(áØÇ), (*(áØÇ := ÄÊÞPKE(0)[slice(0, -1, None)]), (chnk := ÄÊÞPKE(0)[-1])), ÄÊÞDEL(1))[1]
    if áØÇ is not ÂÞÅ:
        (ÄÊÞPSH([áØÇ, áØÇ] if ÁØö(áØÇ, áÍÞ) else áØÇ), ((áÝÍ := ÄÊÞPKE(0)[0]), (áÝÎ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    elif áÑã in 'ᙎᙡ':
        (ÄÊÞPSH([1, 1]), ((áÝÍ := ÄÊÞPKE(0)[0]), (áÝÎ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    elif áÑã in 'ᗢᙧ':
        (ÄÊÞPSH([1, 1] if áØÁ is ÂÞÅ else [0, áØÁ]), ((áÝÍ := ÄÊÞPKE(0)[0]), (áÝÎ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    (áÝÏ := (áÑã in 'ᙡᙧ'))
    (áÝÐ := ((None if áØÁ is ÂÞÅ else áØÁ) if áÑã in 'ᙎᙡ' else ÂÞÅ))
    (áÝÑ := ((chnk if áØÁ is ÂÞÅ else áØÁ + 1) if áÑã in 'ᗢᙧ' else chnk))
    (ÄÊÞPSH((áØÆ, áÝÍ, áÝÎ, áÝÏ, áÝÐ, áÝÑ)), ((áÖê := ÄÊÞPKE(0)[0]), (l := ÄÊÞPKE(0)[1]), (r := ÄÊÞPKE(0)[2]), (m := ÄÊÞPKE(0)[3]), (áØÁ := ÄÊÞPKE(0)[4]), (ÏÁ := ÄÊÞPKE(0)[5])), ÄÊÞDEL(1))[1]
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
        (ÄÊÞPSH(Æå), ÄÊÞPSH(CUR(lambda ÂîÓ, ÂîÒ: ÂîÓ == ÂîÒ, ÄÊÞPKE(0))), (Æå := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
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
            (ÄÊÞPSH(r), ÄÊÞPSH(áÑÿ), ÄÊÞPSH([z]), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    return r

def ÁÞç(áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ):
    if áØÇ is ÂÞÅ:
        (ÄÊÞPSH((áØÇ, áØÆ)), ((áØÆ := ÄÊÞPKE(0)[0]), (áØÇ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    ÂùÆ(áØÇ is not ÂÞÅ, 'ᖘ needs right side')

    def Æå(áØÆ):
        (áØÆ := (ÄÔÙù(áØÆ) if (is_str := ÁØö(áØÆ, ÁÜÙ)) else ÐÌü(getattr(áØÆ, 'copy')) if ÁØö(áØÆ, áÍÙ) else [*áØÆ]))
        (ÄÊÞPSH((MOD(Áëý, áØÁ=áÓó)(áØÁ, lambda ÂîÓ: ÂîÓ(áØÆ)), [])), ((ids := ÄÊÞPKE(0)[0]), (TD := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
        if (ÄÝøÆ(ÁÜÙ, ÄÊÞPSH(ids)) and ÁØö(ÄÊÞPOP(), ÄÊÞPSH(áÓö))) and (ÄÊÞDEL(1) or True) or (ÄÊÞDEL(1) or False):
            ÁØòÁÙÇ(lambda ÂîÓ, ÂîÒ: getattr(TD, 'append')(ÂîÓ) if ÂîÒ is ÄÔýò else (ÄÊÞPSH(áØÆ), ÄÊÞPSH(ÂîÓ), ÄÊÞPSH(ÂîÒ), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3])(ids, (V := áØÇ(ÄÝöÊ(áØÆ, ids))))
        else:
            ÁØÿÁÙÇ(lambda ÂîÓ, ÂîÒ: getattr(TD, 'append')(ÂîÓ) if ÂîÒ is ÄÔýò else (ÄÊÞPSH(áØÆ), ÄÊÞPSH(ÂîÓ), ÄÊÞPSH(ÂîÒ), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3])(ids, (V := Âêà(áØÇ(áØÆ[ids]))))
        for x in ÄÔàÒ(TD):
            del áØÆ[x]
        return Âøî(áØÆ, ÁØã) if is_str else áØÆ
    return Æå if áØÆ is ÂÞÅ else Æå(áØÆ)
(ÆÑ := (lambda áØÆ, áØÇ, áØÁ=ÂÞÅ: reduce(áØÇ, áØÆ, *(() if áØÁ is ÂÞÅ else (áØÁ,)))))
(ÐÌ := (lambda áØÆ, áØÇ, áØÁ=ÂÞÅ: [*accumulate(áØÆ, áØÇ, initial=None if áØÁ is ÂÞÅ else áØÁ)]))
(ÂøÑ := (lambda áØÆ, áØÁ=ÂÞÅ: (ÁØã if ÁØö(áØÆ, ÁÜÙ) else 0) if ((ÄÊÞDEL(1), False)[1] if ÄÊÞPSH(áØÆ) else ÄÊÞPOP() if áØÁ is not ÂÞÅ else (ÄÊÞDEL(1), True)[1]) else MOD(ÆÑ, áØÁ=áØÁ)(áØÆ, ì)))
(ÂøÐ := (lambda áØÆ, áØÁ=ÂÞÅ: 1 if ((ÄÊÞDEL(1), False)[1] if ÄÊÞPSH(áØÆ) else ÄÊÞPOP() if áØÁ is not ÂÞÅ else (ÄÊÞDEL(1), True)[1]) else MOD(ÆÑ, áØÁ=áØÁ)(áØÆ, ÂØú)))
(ÄÕéý := (lambda áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ: (lambda Æå: Æå(*ÂÕÃ([áØÆ, áØÇ], [ÂÞÅ]))) if áØÁ is ÂÞÅ else áØÁ(*ÂÕÃ([áØÆ, áØÇ], [ÂÞÅ]))))
(ÂÔð := (lambda áØÁ=ÂÞÅ: áÍè() if áØÁ is ÂÞÅ else ÁØò(lambda ÂîÓ: áÍè())(ÂÿÇ(áØÁ))))
(ÂÚü := (lambda áØÁ=ÂÞÅ: áÍá() if áØÁ is ÂÞÅ else ÁØò(lambda ÂîÓ: [])(ÂÿÇ(áØÁ)) if áØÁ > 0 else ÂØÍ(Âêà, -áØÁ)([])))

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/ops_B.☾'
@OPWRAP_(*'⤉⤈⟷')
def _(áÑã, áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ, ÁÜñ=False):
    if áÑã == '⟷':
        return (MOD(ÂóÌ, áØÁ=áØÁ, ÁÜñ=ÁÜñ)(áØÆ, áØÇ), MOD(ÂóÍ, áØÁ=áØÁ, ÁÜñ=ÁÜñ)(áØÆ, áØÇ))
    (áÍÛ := (ÿ if áÑã == '⤉' else ÁÁ))
    if áØÇ is ÂÞÅ:
        (ÄÊÞPSH((áØÆ, ÄÕÍÔ)), ((v := ÄÊÞPKE(0)[0]), (Æå := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    elif áÓó(áØÇ):
        (ÄÊÞPSH((áØÆ, áØÇ)), ((v := ÄÊÞPKE(0)[0]), (Æå := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    else:
        (ÄÊÞPSH(([áØÆ, áØÇ], ÄÕÍÔ)), ((v := ÄÊÞPKE(0)[0]), (Æå := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    (áÐð := (áÑÈ := (áÐø := ÂÞÅ)))
    for áÖõ, áÖî in ÂÓÏ(v):
        if not (áØÆ := Æå(áÖî)) is not ÄÔýò:
            continue
        if (ÄÊÞDEL(1), False)[1] if ÄÊÞPSH(áÑÈ is ÂÞÅ) else ÄÊÞPOP() if áÍÛ(áÑÈ, áØÆ) else (ÄÊÞDEL(1), True)[1]:
            continue
        (ÄÊÞPSH((áÖî, áØÆ, áÖõ)), ((áÐð := ÄÊÞPKE(0)[0]), (áÑÈ := ÄÊÞPKE(0)[1]), (áÐø := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]
    return (áÐø if ÁÜñ else áÐð) if áÐð is not ÂÞÅ else áØÁ if áØÁ is not ÂÞÅ else ÐâÄ(ValueError)
(ÄÝöÓ := (lambda áØÆ, áØÇ, áØÁ=ÂÞÅ: (lambda x: ÂóÌ(ÂóÍ(áØÆ, x), áØÇ)) if áØÁ is ÂÞÅ else ÂóÌ(ÂóÍ(áØÆ, áØÁ), áØÇ)))

def ÄÔÞÔ(áØÆ, Æå=áÍÖ, áØÁ=None, ÁÜñ=False):
    if Æå is ÂÞÅ:
        (Æå := áÍÖ)
    elif ÄÝøÇ(Æå, áÓó):
        (ÄÊÞPSH(Æå), ÄÊÞPSH(CUR(lambda ÂîÓ, ÂîÒ: ÂîÓ == ÂîÒ, ÄÊÞPKE(0))), (Æå := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
    for i, x in enumerate(áØÆ):
        if Æå(x):
            return i if ÁÜñ else x
    return áØÁ

@OPWRAP_(*'\U000f7e53\U000f7e54\U000f7e55\U000f7e56')
def _(áÑã, áØÆ, Æå=áÍÖ, áØÁ=ÂÞÅ, ÁÜñ=False):
    if (ÁØö(áØÆ, ÄÊÞPSH(ÁÜÙ)) and ÁØñ(ÄÊÞPOP(), ÄÊÞPSH(Æå))) and (ÄÊÞDEL(1) or True) or (ÄÊÞDEL(1) or False):
        (ÄÊÞPSH(Æå), ÄÊÞPSH(CUR(lambda ÂîÓ, ÂîÒ: ÂîÓ != ÂîÒ, ÄÊÞPKE(0))), (Æå := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
    (áÖõ := MOD(ÄÔÞÔ, ÁÜñ=ÄÕøü)(áØÆ, Æå))
    if áÖõ is None:
        if áØÁ is not ÂÞÅ:
            return áØÁ
        return ÁØã if not ÁÜñ and ÁØö(áØÆ, ÁÜÙ) else ÂÚü()
    if ÁÜñ:
        (ÄÊÞPSH(áØÆ), ÄÊÞPSH(ÂÿÇ(ÄÊÞPKE(0))), (áØÆ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
    if áÑã == '\U000f7e53':
        return áØÆ[slice(None, áÖõ + 1)]
    if áÑã == '\U000f7e54':
        return áØÆ[slice(áÖõ, None)]
    if áÑã == '\U000f7e55':
        return áØÆ[slice(None, áÖõ)]
    if áÑã == '\U000f7e56':
        return áØÆ[slice(1 + áÖõ, None)]

def ÁãÁ(áØÆ, áØÇ=ÄÕÍÔ, ÁÜñ=False):
    (ÄÊÞPSH(([], [])), ((s := ÄÊÞPKE(0)[0]), (r := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
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
(ÄÔéÄ := (lambda áØÆ, áØÇ, áØÁ=ÂÞÅ: ÂåÔ(ÂåÔ((R := (lambda ÂîÓ: Âêà(ÁØã) if ÂîÓ is ÂÞÅ else Âêà(ÂîÓ) if ÁØö(ÂîÓ, ÁÜÙ) else Áÿú(ÁãÁ(ÂîÓ), ÁÜÙ))), (Æå := (lambda ÂîÓ: MOD(ÆÑ, áØÁ=ÂîÓ)((lambda ÂîÓ, ÂîÒ: MOD(ÄÕåØ, áØÁ=ÄÝöÉ(ÂîÒ))(ÂîÓ, ÂîÒ))(R(áØÆ), R(áØÇ)), lambda x, y: getattr(x, 'replace')(*y))))), Æå if áØÁ is ÂÞÅ else ÂÞÅÞCAT(áØÁ, Æå))))

@OPWRAP_(*'\U000f7e39\U000f7e3a\U000f7e38\U000f7e3b')
def _(áÑã, áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ, ÁÜñ=False):
    ÂùÆ(áØÆ is not ÂÞÅ or ÂÞÅ is not áØÇ, 'Range missing both values!')
    if (áÑÃ := (áØÁ is ÂÞÅ)):
        (áØÁ := 1)
    (v := (áØÇ if áØÆ is ÂÞÅ else áØÆ if áØÇ is ÂÞÅ else ÂÞÅ))
    if (áØÆ is not ÂÞÅ and ÂÞÅ is not áØÇ) and ((ÁØö(áØÆ, ÄÊÞPSH(áÍÞ)) and ÁØñ(ÄÊÞPOP(), ÄÊÞPSH(áØÇ))) and (ÄÊÞDEL(1) or True) or (ÄÊÞDEL(1) or False)) if v is ÂÞÅ else ÁØö(v, áÍÞ):
        if v is not ÂÞÅ:
            (ÄÊÞPSH((0, v)), ((áØÆ := ÄÊÞPKE(0)[0]), (áØÇ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
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
            (ÄÊÞPSH(áØÆ), ÄÊÞPSH(ÂÿÇ(ÄÊÞPKE(0))), (áØÆ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
        elif áÓö(áØÇ):
            (ÄÊÞPSH(áØÇ), ÄÊÞPSH(ÂÿÇ(ÄÊÞPKE(0))), (áØÇ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
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
        (ÄÊÞPSH(x), ÄÊÞPSH(ÂÿÇ(ÄÊÞPKE(0))), (x := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
    if y is ÂÞÅ:
        (y := ÄÕÍÔ)
    if ÁÜñ:
        return MOD(áÇù, áØÁ=áØÁ)(ÂÿÇ(x), (lambda i: y(x[i])) if áÓó(y) else y)
    elif ÁØö(y, áÍÞ):
        return [x[slice(None, y)], x[slice(y, None)]]
    elif not áÓó(y):
        ÂùÆ(áÓö(y))
        (y := áÍè(MOD(ÄÔÔç, áØÁ=lambda ÂîÓ: ÂÁÍ(ì)(ÂîÓ, ãÊú(x)))(y, lambda ÂîÓ: ÂîÓ < 0)))
        (ÄÊÞPSH(([], [])), ((R := ÄÊÞPKE(0)[0]), (áÍÌ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
        for áÑî, áÑü in ÂÓÏ(x):
            if áÑî in y:
                getattr(áÍÌ, 'append')(R)
                (R := [])
            getattr(R, 'append')(áÑü)
        if R:
            getattr(áÍÌ, 'append')(R)
        return áÍÌ
    (ÄÊÞPSH((y((áÝÌ := x[0])), [áÝÌ] * (áÝÌ is not ÄÔýò), [])), ((áÍç := ÄÊÞPKE(0)[0]), (R := ÄÊÞPKE(0)[1]), (áÍÌ := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]
    for áÑî, áÑü in ÂÓÏ(x)[slice(1, None)]:
        if (r := y(áÑü)) != áÍç:
            getattr(áÍÌ, 'append')(R)
            (ÄÊÞPSH((r, [])), ((áÍç := ÄÊÞPKE(0)[0]), (R := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
            if not (ÄÊÞPSH(áØÁ), ÄÊÞPSH(ÄÊÞPKE(0) - 1), (áØÁ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]:
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
        (ÄÊÞPSH((áØÇ, áØÆ)), ((áØÆ := ÄÊÞPKE(0)[0]), (áØÇ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    if áØÇ is ÂÞÅ:
        ÂùÆ(áÓö(áØÆ), 'Single-arg %s needs an iterable' % (áÑã,))
        return '\n' * (áÑã in '⟕⟗') + getattr(ÁØã, 'join')(Áÿú(áØÆ, ÁÜÙ)) + ÂÔö('⟗⟖', áÑã) * '\n'
    (Y := áØÇ)
    if not áÓó(áØÇ):
        (ÄÊÞPSH(áØÇ), ÄÊÞPSH((lambda ÂîÓ: lambda *áÑË: ÂîÓ)(ÄÊÞPKE(0))), (áØÇ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
    (ÄÊÞPSH(([*áØÆ], [])), ((áØÆ := ÄÊÞPKE(0)[0]), (R := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
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
        (ÄÊÞPSH(ÂÀÇ(áØÁ) if áØÁ[0] == áÍá else áØÁ), ((n := ÄÊÞPKE(0)[0]), (L := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    else:
        (ÄÊÞPSH([-1, True] if áØÁ == áÍá else [áØÁ, False]), ((n := ÄÊÞPKE(0)[0]), (L := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    if (not L and ÁØö(áØÆ, ÁÜÙ)) and (áØÇ is ÂÞÅ or ÁØö(áØÇ, ÁÜÙ)):
        (áÏÞ := (() if áØÇ is ÂÞÅ else (áØÇ,)))
        if áÑã == '\U000f7e4e':
            return ÄÔÔç(getattr(áØÆ, 'split')(*áÏÞ, maxsplit=n))
    if áØÇ is ÂÞÅ:
        (áØÇ := Âó)
    if (YS := ÁØö(áØÇ, ÁÜÙ)) and (not L):
        (ÄÊÞPSH((Áÿú(Ááú(áØÆ, [0, ãÊú(áØÇ) - 1]), lambda ÂîÓ: Âøî(ÄÔÔç(ÂîÓ))), CUR(lambda ÂîÓ, ÂîÒ: ÂîÓ == ÂîÒ, áØÇ), ãÊú(áØÇ), ãÊú(áØÇ) - 1)), ((áØÆ := ÄÊÞPKE(0)[0]), (áØÇ := ÄÊÞPKE(0)[1]), (Y := ÄÊÞPKE(0)[2]), (ÏÁ := ÄÊÞPKE(0)[3])), ÄÊÞDEL(1))[1]
    else:
        (ÄÊÞPSH(([*áØÆ], áØÇ if áÓó(áØÇ) else CUR(lambda ÂîÓ, ÂîÒ: ÂîÓ == ÂîÒ, áØÇ), 0)), ((áØÆ := ÄÊÞPKE(0)[0]), (áØÇ := ÄÊÞPKE(0)[1]), (ÏÁ := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]
    (ÄÊÞPSH(([], [], -1, 0)), ((r := ÄÊÞPKE(0)[0]), (b := ÄÊÞPKE(0)[1]), (Ïç := ÄÊÞPKE(0)[2]), (Ïñ := ÄÊÞPKE(0)[3])), ÄÊÞDEL(1))[1]
    (last_v := False)
    while (ÄÊÞPSH(Ïç), ÄÊÞPSH(ÄÊÞPKE(0) + 1), (Ïç := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2] < ãÊú(áØÆ) and Ïñ < (ÂÕË if n == -1 else n):
        (áÐÏ := áØÆ[Ïç])
        if (áÑÿ := áØÇ(áÐÏ)):
            if b or áÑã != '\U000f7e4e':
                if áÑã == '\U000f7e4e':
                    getattr(r, 'append')(b)
                elif áÑã == '\U000f7e4c' or (áÑã == '\U000f7e4d' and (not last_v)):
                    getattr(r, 'extend')([b] if áÑÿ is ÄÔýò else [b, áÐÏ])
                    (last_v := True)
            (b := [])
            (ÄÊÞPSH(Ïç), ÄÊÞPSH(ÄÊÞPKE(0) + ÏÁ), (Ïç := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
            (ÄÊÞPSH(Ïñ), ÄÊÞPSH(ÄÊÞPKE(0) + 1), (Ïñ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
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
        (ÄÊÞPSH([áØÁ[0], ÂÞÅ] if ãÊú(áØÁ) == 1 else áØÁ), ((áØÇ := ÄÊÞPKE(0)[0]), (áØÁ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    elif ÁØö(áØÁ, ÂÐý):
        (ÄÊÞPSH((Âüð(áØÁ), ÂÞÅ)), ((áØÇ := ÄÊÞPKE(0)[0]), (áØÁ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    else:
        (ÄÊÞPSH(MOD(ÁÞç, áØÁ=0)(Áÿú(ÄÝõé(áØÁ), Âüð), lambda ÂîÓ: ÂîÓ or 10)), ((áØÇ := ÄÊÞPKE(0)[0]), (áØÁ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    if MOD(ÁØö, áØÁ=ÂÕó)(áØÆ, áÍÛ):
        (ÄÊÞPSH(áØÆ), ÄÊÞPSH(Âäû(ÄÊÞPKE(0))), (áØÆ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
    elif ÁØö(áØÆ, ÁÜÙ):
        if áØÆ and áØÆ[0] == '-':
            (ÄÊÞPSH((áØÆ[slice(1, None)], -1)), ((áØÆ := ÄÊÞPKE(0)[0]), (p := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
        else:
            (p := 1)
        if nc and áØÇ <= 36:
            (ÄÊÞPSH(áØÆ), ÄÊÞPSH(ÂüÌ(ÄÊÞPKE(0))), (áØÆ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
        (áØÆ := (MOD(ÆÑ, áØÁ=0)(ÁØò(lambda ÂîÓ: MOD(ÄÔÞÔ, ÁÜñ=ÄÕøü)(C, ÂîÓ))(áØÆ), CUR(lambda ÂîÓ, ÂîÒ: ÂîÓ * áØÇ + ÂîÒ)) * p))
        if áØÁ is ÂÞÅ:
            return áØÆ
    if áØÁ is ÂÞÅ:
        (áØÁ := 1)
    (ÂÐôáÏß := CUR(lambda ÂîÓ, ÂîÒ: Âøî(ÂÀÇ(ÁØò(lambda ÂîÓ: ÂîÒ[ÂîÓ % ãÊú(ÂîÒ)])(ÂÛÜ(lambda ÂîÓ: ÂîÓ // ãÊú(ÂîÒ), Âó)(ÂîÓ))))))
    (ÂÑÅáÏß := CUR(lambda ÂîÓ, ÂîÒ, *áÏÞ: (ÂîÓ < 0) * '-' + MOD(ÄÕÊÂ, áØÁ=ÂîÒ[0])(ÂÐôáÏß(ÂüÌ(ÂîÓ), ÂîÒ), áÏÞ[0])))
    return ÂÑÅáÏß(áØÆ, ÄÝöÈ(C, áØÇ), áØÁ)
(ÄÔóÅ := (lambda áØÆ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ: phase(áØÆ + ÂÞÅÞCAT(áØÇ, Ãù)) if áØÇ is not ÂÞÅ else phase(áØÆ) if ÁØö(áØÆ, ÂÐá) else phase(ÄÝõé(áØÆ))))
(Âõì := (lambda áØÆ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ: rect(áØÆ, áØÇ) if áØÇ is not ÂÞÅ else rect(*áØÆ) if ÁØö(áØÆ, áÓö) else polar(áØÆ) if s is ÂÞÅ else ÂÞÅÞCAT(áØÆ, ÂÐæ ** ÂÞÅÞCAT(áØÁ, Ãù))))

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

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/ops_C.☾'
@OPWRAP_(*'\U000f147c\U000f7e45')
def _(áÑã, áØÆ=ÂÞÅ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ):
    (áÖÒ := (áØÆ if áØÇ is ÂÞÅ else (áØÆ, áØÇ)))
    (ÄÊÞPSH(MOD(ÐÌÛ, áØÁ=áÍÖ, ÁÜñ=ÄÕøü)(áÖÒ, áÓö)), ((N := ÄÊÞPKE(0)[0]), (I := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    (ÄÊÞPSH(Âîí(Áÿú(ÄÝöÊ(áÖÒ, I), ãÊú))), ((l := ÄÊÞPKE(0)[0]), (h := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    if N:
        (ÄÊÞPSH(áÖÒ), ÄÊÞPSH(MOD(ÁÞç, áØÁ=N)(ÄÊÞPKE(0), MOD(ÁØò(lambda ÂîÓ: MOD(Âêà, áØÁ=h)(ÂîÓ))))), (áÖÒ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
    if áØÁ is ÂÞÅ:
        if áÑã == '\U000f7e45':
            (ÄÊÞPSH(áÖÒ), ÄÊÞPSH(ÁØòÁÙÄ(lambda ÂîÓ, ÂîÒ: ÂîÓ[slice(ãÊú(ÂîÓ) - ÂîÒ, None)])(ÄÊÞPKE(0), l)), (áÖÒ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
    else:
        (ÄÊÞPSH(áÖÒ), ÄÊÞPSH(Áÿú(ÄÊÞPKE(0), Âåæ((lambda ÂîÓ: MOD(ÄÕÊÄ, áØÁ=ÂîÓ[-1] if áØÁ is ÄÕøü else áØÁ)(ÂîÓ, h)) if áÑã == '\U000f147c' else lambda ÂîÓ: MOD(ÄÕÊÂ, áØÁ=ÂîÓ[0] if áØÁ is ÄÕøü else áØÁ)(ÂîÓ, h), áÍá))), (áÖÒ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
    return [*zip(*áÖÒ)]

def ÁÛÛ(áØÆ, áØÁ=ÂÞÅ):

    def Æå(áØÁ):
        if ÄÝøÇ(áØÁ, áÓö) or ÁØñ(ÁÜÙ, áØÁ):
            (ÄÊÞPSH(áØÁ), ÄÊÞPSH(Âêà(ÄÊÞPKE(0))), (áØÁ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
        (áÓÕ := (MOD(ÁÛÛ, áØÁ=áØÁ[slice(1, None)]) if ãÊú(áØÁ) > 1 else ÄÕÍÔ))
        (áÓÙ := (lambda x, y: áÓÕ(x[y % ãÊú(x)]) if ÁØö(y, ÂÑÅ) else áÓÕ(x[y]) if ÁØö(y, ÁÜÙ) or ((ÄÝøÆ(áÓö, ÄÊÞPSH(y)) and ÄÝøÇ(ÄÊÞPOP(), ÄÊÞPSH(slice))) and (ÄÊÞDEL(1) or True) or (ÄÊÞDEL(1) or False)) else MOD(Áëý, áØÁ=áÓÕ is not ÄÕÍÔ)(ÄÝöÊ(x, y), lambda ÂîÓ: Áÿú(ÂîÓ, áÓÕ))))
        return áÓÙ(áØÆ, áØÁ[0])
    return Æå if áØÁ is ÂÞÅ else Æå(áØÁ)

def ÁÝÖ(áØÆ, áØÇ=ÂÞÅ, áØÁ=ÂÞÅ):
    ÂùÆ(ÁØö(áØÆ, áÓö), '%s\U000f7e75𝗜' % (áØÆ,))
    ÂùÆ(áØÁ is not ÂÞÅ, 'ᕋ requires modifier')
    (áØÆ := (ÄÔÙù(áØÆ) if (is_str := ÁØö(áØÆ, ÁÜÙ)) else ÐÌü(getattr(áØÆ, 'copy'))))
    (áØÇ := (ÂÚü() if áØÇ is ÂÞÅ else MOD(Áëý, áØÁ=ÄÝøÇ(áØÇ, áÓö))(áØÇ, Âêà)))
    (áØÁ := (slice((ÄÊÞPSH(áØÁ), ÄÊÞPSH(ÄÊÞPKE(0) % ãÊú(áØÆ)), (áØÁ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2], áØÁ + 1) if ÁØö(áØÁ, áÍÞ) else áØÁ))
    if ÁØö(áØÁ, slice):
        (ÄÊÞPSH(áØÆ), ÄÊÞPSH(áØÁ), ÄÊÞPSH(áØÇ), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    elif ÁØö(áØÁ, áÓö):
        for i, (z, n) in ÂÓÏ(ÁØò(lambda ÂîÓ: [ÂîÓ[0], ãÊú(ÂîÓ)])(áÇù(ÄÔàÒ(ÁØò(lambda ÂîÓ: ÂîÓ % ãÊú(áØÆ))(áØÁ))))):
            if áØÇ is ÂÞÅ or i >= ãÊú(áØÇ):
                del áØÆ[z]
            else:
                (ÄÊÞPSH(áØÆ), ÄÊÞPSH(slice(z, z + 1)), ÄÊÞPSH(MOD(Âêà, áØÁ=n)(áØÇ[i])), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
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
        ÂùÆ((ÄÊÞDEL(1), False)[1] if ÄÊÞPSH(áØÁ == ì) else ÄÊÞPOP() if î == áØÁ else (ÄÊÞDEL(1), True)[1], '\U000f0931 generalize')
        if not áØÁ or ÁØö(áÍÜ, áÓö):

            def Æå(*áÑË):
                if áØÁ == 0:
                    (áÖÒ := [Áÿú(MOD(Áëý, áØÁ=ÁØö(áÍÜ, áÓó))(áÍÜ, Âêà), ÐÌü), áÑË])
                else:
                    (áÖû := (ãÊú(áÍÜ) * (S := ÂüÌ(áØÁ))))
                    if áØÁ < 0:
                        (ÄÊÞPSH(áÑË), ÄÊÞPSH(Âúú(ÄÊÞPKE(0), ãÊú(áÑË) - áÖû)), (áÑË := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
                    if áÑã == '\U000f0b2b':
                        (ÄÊÞPSH(MOD(ÄÕÊÄ, áØÁ=[])(áÇù(áÑË, áÖû), 2)), ((Ïß := ÄÊÞPKE(0)[0]), (Ïà := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
                    elif áÑã == '\U000f0b29':
                        (ÄÊÞPSH(MOD(ÄÕÊÂ, áØÁ=[])(áÇù(áÑË, ÂóÍ(ãÊú(áÑË) - áÖû, 0)), 2)), ((Ïà := ÄÊÞPKE(0)[0]), (Ïß := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
                    (áÖÒ := [ÁØò(lambda ÂîÓ: ÂîÓ[1](*ÂîÓ[0]))((ÄÕåØ if áØÁ < 0 else ÄÝöÔ)[[]](MOD(Ááú, áØÁ=ÄÔýò)(Ïß, [0, S - 1, S]), áÍÜ)), Ïà])
                return ÄÔÙù(MOD(Áëý, áØÁ=áÑã == '\U000f0b29')(áÖÒ, ÂÀÇ))
        else:

            def Æå(*áÑË):
                (áÖí := (ãÊú(áÑË) // ((S := ÂüÌ(áØÁ)) or 1) * S))
                (ÄÊÞPSH(áÇù(ÂÿÇ(áÑË), áÖí if áÑã == '\U000f0b2b' else ãÊú(áÑË) - áÖí)), ((Ïß := ÄÊÞPKE(0)[0]), (Ïà := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
                if Ïß and áØÁ < 0:
                    (ÄÊÞPSH((ÁØò(lambda ÂîÓ: ÂîÓ + ãÊú(Ïà))(Ïß), ÂÿÇ(Ïà))), ((Ïß := ÄÊÞPKE(0)[0]), (Ïà := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
                (ÄÊÞPSH((ÄÝöÊ(áÑË, Ïß), ÄÝöÊ(áÑË, Ïà))), ((Ïß := ÄÊÞPKE(0)[0]), (Ïà := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
                if áÑã == '\U000f0b2b':
                    return (*ËãÂ(MOD(ÁâÁ, áØÁ=ÂóÍ(S - 1, 0))(Ïß), áÍÜ), *Ïà)
                elif áÑã == '\U000f0b29':
                    return (*Ïß, *ËãÂ(MOD(ÁâÁ, áØÁ=ÂóÍ(S - 1, 0))(Ïà), áÍÜ))
    elif ÁØö(áÍÜ, áÓó):

        def Æå(*áÑË):
            (ÄÊÞPSH(((L := ãÊú(áÑË)) // (S := ÂüÌ(áØÁ)), L % S)), ((n := ÄÊÞPKE(0)[0]), (m := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
            ÂùÆ(n != 0, '\U000f0931 generalize')
            (áÖÒ := (MOD(ÄÕÊÄ, áØÁ=ÂýÃ) if áÑã == '○' else MOD(ÄÕÊÂ, áØÁ=ÂýÃ))(áÑË, L + (n - m) % n))
            (v := MOD(ÁâÁ, áØÁ=n - 1)(áÖÒ))
            if m != 0:
                (ÄÊÞPSH((-1, 0) if áÑã == '○' else (0, -1)), ((Ïß := ÄÊÞPKE(0)[0]), (Ïà := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
                if ÄÝøø(áÑã == '⍜', áØÁ < 0):
                    (ÄÊÞPSH(v), ÄÊÞPSH(Ïß), ÄÊÞPSH(ÄÔÙù(ÂÀÇ(áÇù(v[Ïß], lambda ÂîÓ: ÂîÓ is ÂýÃ)))), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
                (ÄÊÞPSH(v), ÄÊÞPSH(Ïß), ÄÊÞPSH(ÁØòÁÙÇ(lambda ÂîÓ, ÂîÒ: ÂîÓ if ÂîÓ is not ÂýÃ else ÂîÒ)(v[Ïß], v[Ïà])), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
            return ËãÂ(v, áÍÜ)
    elif ÁØö(áÍÜ, áÓö):

        def Æå(*áÑË):
            ÂùÆ(ãÊú(áÑË) >= ãÊú(áÍÜ) * (S := ÂüÌ(áØÁ)), '\U000f0931 generalize')
            ÂùÆ(áØÁ > 0, '\U000f0931 generalize')
            ÂùÆ(áÑã != '⍜', '\U000f0931 generalize')
            (ÄÊÞPSH(áÇù(áÑË, ãÊú(áÍÜ) * (S := ÂüÌ(áØÁ)))), ((l := ÄÊÞPKE(0)[0]), (r := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
            (áÖÒ := ÁØòÁÙÄ(lambda ÂîÓ, ÂîÒ: ÄÔÙù(ÂîÓ, ÂîÒ))(MOD(ÁâÁ, áØÁ=S - 1)(l), r))
            return ËãÂ(ÄÕåØ(áÖÒ, áÍÜ), lambda x, y: y(*x))
    return lambda *áÑË, **áÑÕ: áÍÛ(*Æå(*áÑË), **áÑÕ)

@OPWRAP_(*'⊚⊜🟕🟖⊛⍟')
def _(áÑã, Æå=ÂÞÅ, áÍÜ=ÂÞÅ, áØÁ=ÂÕË):
    if not áÓó(Æå):
        (ÄÊÞPSH((áÍÜ, Æå)), ((Æå := ÄÊÞPKE(0)[0]), (áÍÜ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    if áÍÜ is ÂÞÅ:
        (áÍÜ := ÄÕÍÔ)
    elif ÁØö(áÍÜ, áÍÞ) and áÑã in '⊚⊛⍟':
        (áÍÜ := Ticker(áÍÜ + 1))

    def r(*áÑË, **áÑÕ):
        (ÄÊÞPSH((ÂüÌ(áØÁ), áÑË[0] if áÑË else None, áÍÜ(*áÑË, **áÑÕ))), ((n := ÄÊÞPKE(0)[0]), (f := ÄÊÞPKE(0)[1]), (g := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]
        if áÑã == '⊚':
            if g:
                return f
            while 0 < (ÄÊÞPSH(n), ÄÊÞPSH(ÄÊÞPKE(0) - 1), (n := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]:
                if áÍÜ((f := Æå(f))):
                    return f
        elif áÑã == '⊜':
            while 0 < (ÄÊÞPSH(n), ÄÊÞPSH(ÄÊÞPKE(0) - 1), (n := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]:
                if g == (g := áÍÜ((nf := Æå(f)))):
                    return f
                (f := nf)
        elif áÑã in '⊛⍟':
            (rf := [f])
            if g:
                return rf if áÑã == '⊛' else []
            while 0 < (ÄÊÞPSH(n), ÄÊÞPSH(ÄÊÞPKE(0) - 1), (n := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]:
                (g := áÍÜ((f := Æå(f))))
                if not g or áÑã == '⊛':
                    getattr(rf, 'append')(f)
                if g:
                    return rf
            if áØÁ < 0:
                return rf
        elif áÑã in '🟕🟖':
            (ÄÊÞPSH(([f], [g])), ((rf := ÄÊÞPKE(0)[0]), (rg := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
            while 0 < (ÄÊÞPSH(n), ÄÊÞPSH(ÄÊÞPKE(0) - 1), (n := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]:
                if (g := áÍÜ((f := Æå(f)))) in rg:
                    if áÑã == '🟖':
                        return rf
                    return ÄÝöÊ(MOD(ÄÔÞÔ, ÁÜñ=ÄÕøü)(rg, lambda x: x == g), rf)
                getattr(rf, 'append')(f)
                getattr(rg, 'append')(g)
        return None
    return r

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/ops_\uea8c.☾'
(áÍù := áÓö)

def adjust_depth(áØÆ, áØÁ, áÍù=áÓö):
    if áØÁ is ÂÞÅ:
        return 1
    if áØÁ >= 0:
        return áØÁ
    (ÄÊÞPSH((áØÆ, 0)), ((áØÆ := ÄÊÞPKE(0)[0]), (k := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    while (ÄÊÞPSH(k), ÄÊÞPSH(ÄÊÞPKE(0) + 1), (k := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2] if áÍù(áØÆ) else None:
        if ÁØö(áØÆ, ÁÜÙ):
            break
        if ÁØö(áØÆ, ÁÜÙ) or not ãÊú(áØÆ):
            break
        (ÄÊÞPSH(áØÆ), ÄÊÞPSH(ÄÊÞPKE(0)[0]), (áØÆ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
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
    if ((áØÆ is not ÄÊÞPSH(ÂÞÅ) and ÄÊÞPOP() is not ÄÊÞPSH(áØÇ)) and (ÄÊÞDEL(1) or True) or (ÄÊÞDEL(1) or False)) and ((ÁØö(áØÆ, ÄÊÞPSH(áÍÞ)) and ÁØñ(ÄÊÞPOP(), ÄÊÞPSH(áØÇ))) and (ÄÊÞDEL(1) or True) or (ÄÊÞDEL(1) or False)):
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
        return (áØÆ > ÄÊÞPSH(ÂýÃ) and ÄÊÞPOP() > ÄÊÞPSH(áØÇ)) and (ÄÊÞDEL(1) or True) or (ÄÊÞDEL(1) or False) if áÑã == '⪢' else (áØÆ < ÄÊÞPSH(ÂýÃ) and ÄÊÞPOP() < ÄÊÞPSH(áØÇ)) and (ÄÊÞDEL(1) or True) or (ÄÊÞDEL(1) or False)
    if áÑã == '⪡':
        (ÄÊÞPSH(áØÇ), ÄÊÞPSH(ÄÝöâ(ÄÊÞPKE(0))), (áØÇ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
    if áØÁ is ÂÞÅ:
        return áØÆ and áØÆ[slice((i := (-áØÇ % ãÊú(áØÆ))), None)] + áØÆ[slice(None, i)]
    return ÐÈÔ(MOD(ÄÔÒØ, áØÁ=áØÁ)(áØÆ), Âúú(MOD(ÄÝõÞ, áØÁ=áØÁ)(áØÆ), áØÇ))

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/ugex.☾'
class winder:

    def __init__(áÑÞ, áÖï, áÖõ=-1):
        (ÄÊÞPSH(áÑÞ), ÄÊÞPSH('áÖï'), ÄÊÞPSH(áÑÞ), ÄÊÞPSH('áÖõ'), ÄÊÞPSH(áÑÞ), ÄÊÞPSH('áÖà'), ÄÊÞPSH((áÖï, áÖõ, ÂÚü())), (setattr(ÄÊÞPKE(6), ÄÊÞPKE(5), ÄÊÞPKE(0)[0]), setattr(ÄÊÞPKE(4), ÄÊÞPKE(3), ÄÊÞPKE(0)[1]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)[2])), ÄÊÞDEL(7))[7]
    (__bool__ := (lambda áÑÞ: getattr(áÑÞ, 'áÖõ') + 1 < ãÊú(getattr(áÑÞ, 'áÖï'))))
    (__repr__ := (lambda áÑÞ: '[%s│%s]⟨%s⟩' % (ÂîË(getattr(áÑÞ, 'áÖï')[slice(None, getattr(áÑÞ, 'áÖõ') + 1)], ' '), ÂîÊ(getattr(áÑÞ, 'áÖï')[slice(getattr(áÑÞ, 'áÖõ') + 1, None)], ' '), Âøî(getattr(áÑÞ, 'áÖà'), ' '))))
    (peek := (lambda áÑÞ: getattr(áÑÞ, 'áÖï')[getattr(áÑÞ, 'áÖõ') + 1]))
    (next := (lambda áÑÞ: getattr(áÑÞ, 'áÖï')[(ÄÊÞPSH(áÑÞ), ÄÊÞPSH('áÖõ'), ÄÊÞPSH(getattr(ÄÊÞPKE(1), ÄÊÞPKE(0))), ÄÊÞPSH(ÄÊÞPKE(0) + 1), setattr(ÄÊÞPKE(3), ÄÊÞPKE(2), ÄÊÞPKE(0)), ÄÊÞDEL(4))[4]]))
    (note := (lambda áÑÞ: ÂåÔ(getattr(getattr(áÑÞ, 'áÖà'), 'append')(getattr(áÑÞ, 'áÖõ')), áÑÞ)))
    (eton := (lambda áÑÞ: ÂåÔ(ÐÌü(getattr(getattr(áÑÞ, 'áÖà'), 'pop')), áÑÞ)))
    (wind := (lambda áÑÞ: ÂåÔ((ÄÊÞPSH(áÑÞ), ÄÊÞPSH('áÖõ'), ÄÊÞPSH(ÐÌü(getattr(getattr(áÑÞ, 'áÖà'), 'pop'))), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3], áÑÞ)))
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
    if (ÄÊÞPSH(áØÁ), ÄÊÞPSH(ÄÊÞPKE(0) * -1 == 0), (áØÁ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]:
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
    if (ÄÊÞPSH(áØÁ), ÄÊÞPSH(ÄÊÞPKE(0) * -1 == 0), (áØÁ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]:
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
    (ÄÊÞPSH(áØÃ), ((áÓç := ÄÊÞPKE(0)[0]), *(áÒø := ÄÊÞPKE(0)[slice(1, None, None)])), ÄÊÞDEL(1))[1]
    if ÁØö(áÓç, áÓó):
        return UGX_SCAN(áÖÿ, áÓç, áÒø[0])
    elif áÓç in 'BP':
        (ÄÊÞPSH(áÒø), ((áÓæ := ÄÊÞPKE(0)[0]), (áÓà := ÄÊÞPKE(0)[1]), (áÓå := ÄÊÞPKE(0)[2]), (áÓÕ := ÄÊÞPKE(0)[3])), ÄÊÞDEL(1))[1]
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

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/ℵ.☾'
class aleph_wrapper:
    (__slots__ := ('x',))
    (__init__ := (lambda áÑÞ, y: Âåß(None, (ÄÊÞPSH(áÑÞ), ÄÊÞPSH('x'), ÄÊÞPSH(y), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3])))
    (__repr__ := (lambda áÑÞ: getattr(áÑÞ, 'x')))
    (__call__ := (lambda áÑÞ, *áÑË, **áÑÕ: getattr(áÑÞ, 'x')(*áÑË, **áÑÕ)))

class ÂÑÖ(áÍÙ):
    (áÌüáÍã := 'ℵ')

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
    (__repr__ := (lambda áÑÞ: '%s%s(%s)' % (getattr(getattr(áÑÞ, '__class__'), 'áÌüáÍã'), '[%s]' % (h[0] or 'ᐦ',) if 0 in (h := getattr(áÑÞ, '__dict__')) else ÁØã, Âøî(ËãÂ(ÐÌü(getattr(áÑÞ, 'items')), lambda x, y: '%s=%s' % (x, y)), ', '))))
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
    (setdef := (lambda áÑÞ, x: ÂåÔ((ÄÊÞPSH(getattr(áÑÞ, '__dict__')), ÄÊÞPSH(0), ÄÊÞPSH(x), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3], áÑÞ)))

    def getdef(áÑÞ, k=ÂÞÅ):
        (d := getattr(áÑÞ, '__dict__')[0])
        if ÁØö(d, aleph_wrapper):
            (ÄÊÞPSH(d), ÄÊÞPSH(ÐÌü(ÄÊÞPKE(0))), (d := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
            (ÄÊÞPSH(áÑÞ), ÄÊÞPSH(k), ÄÊÞPSH(d), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
        return d

    def copy(áÑÞ):
        (r := type(áÑÞ)(getattr(super(), 'copy')()))
        if getattr(áÑÞ, 'hasdef')():
            getattr(r, 'setdef')(getattr(áÑÞ, 'getdef')())
        return r

class ÂÑØ(ÂÑÖ):
    (áÌüáÍã := 'ℶ')
    (__iter__ := (lambda áÑÞ: iter(getattr(áÑÞ, 'values')())))

class _hwrap(áÍÙ):

    def __init__(áÑÞ, áÍØ):
        (ÄÊÞPSH(áÑÞ), ÄÊÞPSH('áÍØ'), ÄÊÞPSH(áÑÞ), ÄÊÞPSH('áÍã'), ÄÊÞPSH((áÍØ, getattr(áÍØ, 'áÌüáÍã'))), (setattr(ÄÊÞPKE(4), ÄÊÞPKE(3), ÄÊÞPKE(0)[0]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)[1])), ÄÊÞDEL(5))[5]
    (__getitem__ := (lambda áÑÞ, x: getattr(getattr(áÑÞ, 'áÍØ')(), 'setdef')(x)))
    (__setitem__ := (lambda áÑÞ, x, y: ÂåÔ(getattr((Âàü := getattr(áÑÞ, 'áÍØ')()), '__setitem__')(x, y), Âàü)))
    (__call__ := (lambda áÑÞ, *áÑË, **áÑÕ: getattr(áÑÞ, 'áÍØ')(*áÑË, **áÑÕ)))
    (__or__ := (lambda áÑÞ, x: getattr(áÑÞ, 'áÍØ')() | x))
    (__pow__ := (lambda áÑÞ, x: getattr(áÑÞ, 'áÍØ')() ** x))
    (__repr__ := (lambda áÑÞ: '%s()' % (getattr(áÑÞ, 'áÍã'),)))
    (__bool__ := (lambda: False))
(ÂÑÖ := _hwrap(ÂÑÖ))
(ÂÑØ := _hwrap(ÂÑØ))

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/!.☾'
def ÏÀ(z):
    if ÄÝõè(z) < ÃÆ:
        return ÂÞÅÞCAT(Ïò, Ãù) / ((ÂÐæ ** ÂÞÅÞCAT(ÂÞÅÞCAT(Ãù, Ïî), z) - ÂÐæ ** ÂÞÅÞCAT(ÂÞÅÞCAT(ÄÝîâ, Ïî), z)) * ÏÀ(1 - z))
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
        (ÄÊÞPSH((1, áØÆ)), ((t := ÄÊÞPKE(0)[0]), (c := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
        while ÃÆí(c) == ÃÆí(áØÆ):
            (ÄÊÞPSH(t), ÄÊÞPSH(ÄÊÞPKE(0) * c), (t := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
            (ÄÊÞPSH(c), ÄÊÞPSH(ÄÊÞPKE(0) + d), (c := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
        return t
    if ÁØö(áØÁ, áÓö):
        return MOD(ÂøÐ, áØÁ=1)(ÁØò(lambda ÂîÓ: ÂîÓ * áØÁ[-1] + áØÆ)(ÂÿÇ(áØÁ[0])))
    ÂùÆ(False, 'what do you meeeeaaaaaannnnnn!?!?!?')

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/𝔍.☾'
(áÐÞ := ÂÞÅÞCAT({ÁÁ: ÄÊÞCUR((1,), {'ensure_ascii': False, 'indent': None, 'separators': ',:'}, jdumps__, ÂýÃ), ÿ: jloads__}, ÂÑÖ()))

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/🌈.☾'
def h2r(c=ÁØã):
    if ÁØö(c, áÍÞ):
        (ÄÊÞPSH(c), ÄÊÞPSH(MOD(ÄÝöì, áØÁ=16)(ÄÊÞPKE(0))), (c := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
    (c := getattr(getattr(c, 'strip')(), 'lstrip')('#'))
    if getattr(c, 'startswith')('0x'):
        (ÄÊÞPSH(c), ÄÊÞPSH(ÄÊÞPKE(0)[slice(2, None)]), (c := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
    (ÄÊÞPSH((ÄÊÞCUR((1,), {}, áÍÞ, ÂýÃ, 16), ãÊú(c))), ((ÂÐí := ÄÊÞPKE(0)[0]), (n := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
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
(r2hl := (lambda x: '#%s' % (Âøî(Áÿú(x, MOD(ÄÝöì, áØÁ=16 + ÂÞÅÞCAT(2, Ãù)))),)))
(h2hl := Âåæ(r2hl, h2r))
(TERM_RESET := '\x1b[0m')

def termclr(t, fg=None, bg=None, rst=True):
    (mkc := (lambda x, y, z, w, v: '\x1b[%s;2;%s;%s;%sm' % (x, y, z, w)))
    (R := Âøî([mkc(n, *h2r(c)) for c, n in ÄÕåØ([fg, bg], [38, 48]) if c is not None]))
    return '%s%s%s' % (R, t, TERM_RESET if rst else ÁØã)

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/kots.☾'
(TMPDIR := ÂÞÅÞCAT(ÐÌü(gettempdir), áÌî))
(mkd := (lambda f, e=True, p=True: ÂåÔ(getattr((p := áÌî(f)), 'mkdir')(exist_ok=e, parents=p), p)))
(mkf := (lambda f, e=True: ÂåÔ(getattr(mkd(getattr((p := áÌî(f)), 'parent')), 'touch')(exist_ok=e), p)))
(tmpf := (lambda b=ÁØã, f=ÂÞÅ, n=14: mkf(ð(ð(TMPDIR, b), Âøî(ÄÔÙù(MOD(ÐâÇ, áØÁ=1)(abcABC123, n))) if f is ÂÞÅ else f))))
(tmpd := (lambda b=ÁØã, f=ÂÞÅ, n=14: mkd(ð(ð(TMPDIR, b), Âøî(ÄÔÙù(MOD(ÐâÇ, áØÁ=1)(abcABC123, n))) if f is ÂÞÅ else f))))

class suppar2:
    (__init__ := (lambda áÑÞ, Æå: ÂåÔ((ÄÊÞPSH(Æå), ÄÊÞPSH(áÑÞ), ÄÊÞPSH('Æå'), setattr(ÄÊÞPKE(1), ÄÊÞPKE(0), ÄÊÞPKE(2)), ÄÊÞDEL(3))[3], None)))
    (__call__ := (lambda áÑÞ, *áÑË, **áÑÕ: getattr(áÑÞ, 'Æå')(*áÑË, **áÑÕ)))
    (__getitem__ := (__getattr__ := (lambda áÑÞ, x, *áÑË, **áÑÕ: lambda *áÑË, **áÑÕ: getattr(áÑÞ, 'Æå')(*áÑË, x, **áÑÕ))))
(ÐâÒ := (lambda x=ÂÞÅ: ÐÌü(PL_TEXT_PASTE) if x is ÂÞÅ else ÂåÔ(ÂÞÅÞCAT(ÂÞÅÞCAT(x, ÁÜÙ), PL_TEXT_COPY), x)))
(ÐÈÃ := suppar2(lambda f, o=ÁØã: getattr(áÌî(f), 'open')(o)))
(ÐØó := suppar2(lambda f, o=ÁØã: Âáõ((y := ÐÈÃ['r' + o](f)), lambda x: ÐÌü(getattr(x, 'read')))))
(ÐØì := suppar2(lambda f, áÏû, o=ÁØã: Âáõ((y := ÐÈÃ['w' + o](f)), lambda x: ÂåÔ(getattr(x, 'write')(áÏû), y))))
(pwd := (lambda: áÌî(ÐÌü(getattr(os, 'getcwd')))))

class cd:
    (ÄÊÞPSH(MOD(ÂÚü, áØÁ=2)()), ((s := ÄÊÞPKE(0)[0]), (c := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]

    def __init__(áÑÞ, d=None):
        (ÄÊÞPSH(áÑÞ), ÄÊÞPSH('d'), ÄÊÞPSH(d), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]

    def __enter__(áÑÞ):
        (x := getattr(áÑÞ, 'd'))
        getattr(getattr(cd, 's'), 'append')((ãÊú(getattr(cd, 'c')), (x := ÐÌü(pwd))))
        if x is not None:
            getattr(os, 'chdir')(áÌî(x))
        return ÐÌü(pwd)

    def __exit__(áÑÞ, *áÑË):
        (ÄÊÞPSH(getattr(getattr(cd, 's'), 'pop')(-1)), ((i := ÄÊÞPKE(0)[0]), (d := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
        (ÄÊÞPSH(cd), ÄÊÞPSH('c'), ÄÊÞPSH(getattr(cd, 'c')[slice(None, i)]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
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

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/extra_globals.☾'
(FRAC_CONV := {**dict(ÄÕåØ(ÂÛê('12\u200913\u200914\u200915\u200916\u200917\u200918\u200919\u2009110\u200923\u200925\u200927\u200929\u200934\u200935\u200937\u200938\u2009310\u200945\u200947\u200949\u200956\u200957\u200958\u200959\u200967\u200978\u200979\u2009710\u200989\u2009910\u200903\u20091100'), '½⅓¼⅕⅙⅐⅛⅑⅒⅔⅖\U000f7db2\U000f7db7¾⅗\U000f7db3⅜\U000f7dc6⅘\U000f7db4\U000f7dc2⅚\U000f7db5⅝\U000f7db9\U000f7db6⅞\U000f7dba\U000f7dc7\U000f7dbb\U000f7dc8↉\U000f7dc9'))})
(TOFRAC := (lambda x: getattr(FRAC_CONV, 'get')(x, x)))

class UPSIDEDOWNSYNDROME:
    (NRM := '0123456789abcdefoxABCDEFOXîĵ\U000f7e88ℇτπ\U000f7e8d\U000f7e8f∞')
    (USD := '\U000f7c3d\U000f7c3e\U000f7c3f\U000f7c40\U000f7c41\U000f7c42\U000f7c43\U000f7c44\U000f7c45\U000f7c46\U000f7c47\U000f7c48\U000f7c49\U000f7c4a\U000f7c4b\U000f7c4c\U000f7c4d\U000f7c4e\U000f7c4f\U000f7c50\U000f7c51\U000f7c52\U000f7c53\U000f7c54\U000f7c55\U000f7c56\U000f7c6a\U000f7c7d\U000f7c7e\U000f7c6b\U000f7c6c\U000f7c6d\U000f7c6e\U000f7c70\U000f7c69')
    (MAP := ({**dict(ÄÕåØ(NRM, USD))} | {**dict(ÄÕåØ(USD, NRM))}))
    (flip := (lambda x, m=MAP: Âøî(ÁØò(lambda ÂîÓ: getattr(m, 'get')(ÂîÓ, ÂîÓ))(x), ÁØã)))

class SCRIPT:
    (SCRIPT_FILE_LOC := '/home/ganer/Projects/Moon_BETA/STAGES/.SCRIPT_MAP')
    (ÄÊÞPSH(ÄÝöÞ(ÐÌü(getattr(ÐØó(SCRIPT_FILE_LOC), 'strip')), '\n')), ((CHAR_NRM := ÄÊÞPKE(0)[0]), (CHAR_SUP := ÄÊÞPKE(0)[1]), (CHAR_SUB := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]
    (SUP := getattr(ÁÜÙ, 'maketrans')(CHAR_NRM, CHAR_SUP))
    (SUB := getattr(ÁÜÙ, 'maketrans')(CHAR_NRM, CHAR_SUB))
    (NRM := getattr(ÁÜÙ, 'maketrans')(CHAR_SUP + CHAR_SUB, 2 * CHAR_NRM))
    (ÄÊÞPSH(Áÿú([SUP, SUB, NRM], lambda áÖæ: lambda x: getattr(x, 'translate')(áÖæ))), ((sup := ÄÊÞPKE(0)[0]), (sub := ÄÊÞPKE(0)[1]), (nrm := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((getattr(SCRIPT, 'sup'), getattr(SCRIPT, 'sub'), getattr(SCRIPT, 'nrm'))), ((supscript := ÄÊÞPKE(0)[0]), (subscript := ÄÊÞPKE(0)[1]), (nrmscript := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((getattr(SCRIPT, 'CHAR_SUP'), getattr(SCRIPT, 'CHAR_SUB'))), ((SUPSCRIPT := ÄÊÞPKE(0)[0]), (SUBSCRIPT := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ALPHABETS := Áÿú(ÄÝöÞ(Âüá('\n    abcdefghijklmnopqrstuvwxyz\u2009ABCDEFGHIJKLMNOPQRSTUVWXYZ\u20090123456789\n    𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫\u2009𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ\u2009𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡\n    𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳\u2009𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙\u2009𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗\n    𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧\u2009𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍\u2009◌◌◌◌◌◌◌◌◌◌\n    𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇\u2009𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭\u2009𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵\n    𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣\u2009𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉\u2009𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿\n    ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ\u2009ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ\u2009◌\U000f0ca1\U000f0ca3\U000f0ca5\U000f0ca7\U000f0ca9\U000f0cab\U000f0cad\U000f0caf\U000f0cb1\n    ⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵\u2009🄐🄑🄒🄓🄔🄕🄖🄗🄘🄙🄚🄛🄜🄝🄞🄟🄠🄡🄢🄣🄤🄥🄦🄧🄨🄩\u2009◌⑴⑵⑶⑷⑸⑹⑺⑻⑼\n    \U000f0aee\U000f0aef\U000f0af0\U000f0af1\U000f0af2\U000f0af3\U000f0af4\U000f0af5\U000f0af6\U000f0af7\U000f0af8\U000f0af9\U000f0afa\U000f0afb\U000f0afc\U000f0afd\U000f0afe\U000f0aff\U000f0b00\U000f0b01\U000f0b02\U000f0b03\U000f0b04\U000f0b05\U000f0b06\U000f0b07\u2009\U000f0aee\U000f0aef\U000f0af0\U000f0af1\U000f0af2\U000f0af3\U000f0af4\U000f0af5\U000f0af6\U000f0af7\U000f0af8\U000f0af9\U000f0afa\U000f0afb\U000f0afc\U000f0afd\U000f0afe\U000f0aff\U000f0b00\U000f0b01\U000f0b02\U000f0b03\U000f0b04\U000f0b05\U000f0b06\U000f0b07\u2009\U000f0b39\U000f0b3a\U000f0b3b\U000f0b3c\U000f0b3d\U000f0b3e\U000f0b3f\U000f0b40\U000f0b41\U000f0b42\n    \U0001ccd6\U0001ccd7\U0001ccd8\U0001ccd9\U0001ccda\U0001ccdb\U0001ccdc\U0001ccdd\U0001ccde\U0001ccdf\U0001cce0\U0001cce1\U0001cce2\U0001cce3\U0001cce4\U0001cce5\U0001cce6\U0001cce7\U0001cce8\U0001cce9\U0001ccea\U0001cceb\U0001ccec\U0001cced\U0001ccee\U0001ccef\u2009\U0001ccd6\U0001ccd7\U0001ccd8\U0001ccd9\U0001ccda\U0001ccdb\U0001ccdc\U0001ccdd\U0001ccde\U0001ccdf\U0001cce0\U0001cce1\U0001cce2\U0001cce3\U0001cce4\U0001cce5\U0001cce6\U0001cce7\U0001cce8\U0001cce9\U0001ccea\U0001cceb\U0001ccec\U0001cced\U0001ccee\U0001ccef\u2009\U0001ccf0\U0001ccf1\U0001ccf2\U0001ccf3\U0001ccf4\U0001ccf5\U0001ccf6\U0001ccf7\U0001ccf8\U0001ccf9\n    𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓\u2009𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹\u2009𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫\n    ɒც𝼝𝼥⋿ꬵꬶҕї𝼚𝼐ꬷӍꬼϙƿ𝼛Ʀ𝼞ŧꭒѵꭐꭘꭚƶ\u2009ѦƁƇƊᗴҒႺⴼΙɈⴿꝈⱮͶⴲƤꝖⴽႽƬŲѴϢҲⵖΖ\u2009◌◌◌◌◌◌◌◌◌◌\n    𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻\u2009𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡\u2009◌◌◌◌◌◌◌◌◌◌\n    𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏\u2009𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵\u2009◌◌◌◌◌◌◌◌◌◌\n    𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃\u2009𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩\u2009◌◌◌◌◌◌◌◌◌◌\n    𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛\u2009𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁\u2009◌◌◌◌◌◌◌◌◌◌\n    𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷\u2009𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ\u2009◌◌◌◌◌◌◌◌◌◌\n    𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟\u2009𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅\u2009◌◌◌◌◌◌◌◌◌◌\n    𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯\u2009𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕\u2009◌◌◌◌◌◌◌◌◌◌\n'), '\n'), Âåæ(ÂÛê, Âüá)))
(LOWERCASE := Âøî(Áÿú(ALPHABETS, MOD(ÁÛÛ, áØÁ=0))))
(UPPERCASE := Âøî(Áÿú(ALPHABETS, MOD(ÁÛÛ, áØÁ=1))))
(LETTERS := (LOWERCASE + UPPERCASE))
(TERLETS := (UPPERCASE + LOWERCASE))
(ÄÊÞPSH(ALPHABETS[0][slice(None, 3)]), ((abc := ÄÊÞPKE(0)[0]), (ABC := ÄÊÞPKE(0)[1]), (num := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((abc + ABC, abc + num, ABC + num, abc + ABC + num)), ((abcABC := ÄÊÞPKE(0)[0]), (abc123 := ÄÊÞPKE(0)[1]), (ABC123 := ÄÊÞPKE(0)[2]), (abcABC123 := ÄÊÞPKE(0)[3])), ÄÊÞDEL(1))[1]
(TO_LOWERCASE := CUR(lambda ÂîÓ, ÂîÒ: under_script(ÂîÒ, ÂîÓ), (lambda ÂîÓ: lambda x: getattr(x, 'translate')(ÂîÓ))(getattr(ÁÜÙ, 'maketrans')(UPPERCASE, LOWERCASE))))
(TO_UPPERCASE := CUR(lambda ÂîÓ, ÂîÒ: under_script(ÂîÒ, ÂîÓ), (lambda ÂîÓ: lambda x: getattr(x, 'translate')(ÂîÓ))(getattr(ÁÜÙ, 'maketrans')(LOWERCASE, UPPERCASE))))
(REVERSE_CASE := CUR(lambda ÂîÓ, ÂîÒ: under_script(ÂîÒ, ÂîÓ), (lambda ÂîÓ: lambda x: getattr(x, 'translate')(ÂîÓ))(getattr(ÁÜÙ, 'maketrans')(LETTERS, TERLETS))))
(GET_CASE := (lambda x: (TO_UPPERCASE(x) == x) - (x == TO_LOWERCASE(x))))

def under_script(áØÆ, Æå, áÕÉ=ÂÞÅ):
    (áÓÕ := (lambda ÂîÓ: supscript if ÂîÓ in SUPSCRIPT else subscript if ÂîÓ in SUBSCRIPT else None))
    return Âøî(ËãÂ(ÄÕåØ(ÁØò(lambda ÂîÓ: MOD(ÆÑ, áØÁ=ÄÕÍÔ)(Áÿú(ÂÕÅ(ÂÛÜ(nrmscript, Âåæ(Âó, áÓÕ)), ÂîÓ), áÓÕ), Âåæ))(áØÆ if áÕÉ is ÂÞÅ else áÕÉ), Æå(ÂÕÅ(ÂØÏ(nrmscript), áØÆ))), ÂÕÅ))

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/highlighter.☾'
(styf := áÌî('/home/ganer/Projects/Moon_BETA/STAGES/style.json'))
(styd := ÂÞÅÞCAT(ÂÞÅÞCAT(ÂÞÅÞCAT(styf, ÐØó), áÐÞ[ÿ]), ÂÑÖ()))

@cache
def sty(s, bg=0, def_='bec'):
    for k, v in styd:
        if s not in k or 'color' not in v:
            continue
        return termclr(s, v['color'], bg)
    return termclr(s, def_, bg)
(__highlighter__ := (lambda l, b=False, clr='bec': Âøî(Áÿú(ÂÞÅÞCAT(ÂÞÅÞCAT(l, ÁÜÙ), VEP), ÄÊÞCUR((1,), {}, sty, ÂýÃ, b, clr)))))

def highlight_tester():
    while (l := ÐÌü(getattr(stdin, 'readline'))):
        Âçß(ÂÞÅÞCAT(getattr(l, 'rstrip')('\n'), __highlighter__))

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/meta.☾'
(IMPSIMPS := (('ℍ', 'ℍ\U000f7e19\U000f7e18\U000f7e1b\U000f7e1a\U000f7e17\U000f7e16\U000f7e1c\U000f7e3d\U000f7e15ĵ\U000f7e88\U000f7c7d\U000f7c7e'), ('⫚', '⫚'), ('¶', '¶✿')))

def __ÞÄÊÞADDGLOBALS_CLEAN__(M, áÒÿ):
    getattr(áÒÿ, 'update')(M)

def __ÞÄÊÞIMPORT__(p, áÒÿ):
    Âçß('\U000f0931 __þIMPORT__ "%s"' % (p,))
    return
    (p := áÌî('/tmp/compiled_Libraries$$%s.py' % (MOD(ÄÔéÄ, áØÁ=p)('/', 2 * '$'),)))
    (ÄÊÞPSH((getattr(p, 'name'), ÐØó(p))), ((name := ÄÊÞPKE(0)[0]), (áÖïáÖüáÖðáÖñ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    (ns := getattr(áÒÿ, 'copy')())
    getattr(ns, 'pop')('__EXPORTS__', None)
    (ÄÊÞPSH(ns), ÄÊÞPSH('__file__'), ÄÊÞPSH(ns), ÄÊÞPSH('__dir__'), ÄÊÞPSH((p, getattr(p, 'parent'))), (setitem(ÄÊÞPKE(4), ÄÊÞPKE(3), ÄÊÞPKE(0)[0]), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)[1])), ÄÊÞDEL(5))[5]
    exec(áÖïáÖüáÖðáÖñ, ns, ns)
    getattr(áÒÿ, 'update')(getattr(ns, 'get')('__EXPORTS__', {}))
    return ns

def __ÞÄÊÞADD_EXPORTS__(áÒÿ, *áÑË):
    (E := getattr(áÒÿ, 'setdefault')('__EXPORTS__', {}))
    getattr(E, 'update')({**dict(áÑË)})
    return E
import subprocess

def ÄÕôñ(áÖï, ns=None, get_code=False):
    (fn := sha(áÖï))
    (po := ð(getattr((pi := áÌî('/tmp/%s.☾' % (fn,))), 'parent'), '%s.py' % (fn,)))
    ÐØì(pi, áÖï)
    getattr(getattr(subprocess, 'Popen')(ÂÛê("bash\u2009-c\u2009☾ '/home/ganer/Projects/Moon_BETA/Compiler/main.☾' o '%s' '%s'" % (pi, po))), 'wait')()
    (code := ÐØó(po))
    if get_code:
        return code
    return eval(code, *(ÂÚü() if ns is None else [ns]))

# /home/ganer/Projects/Moon_BETA/NewMoon/Libraries/text_format.☾⟶/tmp/α/compiled_$$home$$ganer$$Projects$$Moon_BETA$$NewMoon$$Libraries$$text_format.☾.py
exec('\n__file__=\'/home/ganer/Projects/Moon_BETA/NewMoon/Libraries/text_format.☾\'\nimport re\n(áüíÞcache := (lambda Æå, *áÑË, **áÑÕ: ÂåÔ((Ëðá := cache(Æå)), lambda *áÑË, **áÑÕ: (Ëðá if ÂøÑ(ÁØò(lambda ÂîÓ: ãÊú(ÂîÓ) if ÁØö(ÂîÓ, áÓö) else 1)(áÑË)) < 1024 else Æå)(*áÑË, **áÑÕ))))\n(ÄÊÞPSH((áüíÞcache(__highlighter__), áüíÞcache(termclr))), ((H := ÄÊÞPKE(0)[0]), (Åøáüì := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n(find_esc_seqs := getattr(re, \'compile\')((S := \'\\x1b\\\\[(?:\\\\d+;2;\\\\d+;\\\\d+;\\\\d+|0)m\')))\n(find_next_char := getattr(re, \'compile\')(\'((?:(?:%s)|\\x1b\\\\[0m)*.?)\' % (S,)))\n(rm_esc := áüíÞcache(ÄÊÞCUR((3,), {}, getattr(re, \'sub\'), find_esc_seqs, ÁØã, ÂýÃ)))\n(dotrim := áüíÞcache(lambda x, y: x[slice(None, y - 1)] + \'…\' if áüíËðâ((x := ÁÜÙ(x))) > y else x))\n(lines := (lambda ÂîÓ: getattr(ÂîÓ, \'split\')(\'\\n\')))\n(tspl := (lambda x, y: Áÿú(áÇù(getattr(re, \'findall\')(find_next_char, x), y), Âøî)))\n(áüíËðâ := (lambda x: ãÊú(rm_esc(x)) if ÁØö(x, ÁÜÙ) else x))\n(áüíáüí := (lambda x: (lambda ÂîÓ: (MOD(ÂóÍ, áØÁ=0)(Áÿú(ÂîÓ, áüíËðâ)), ãÊú(ÂîÓ)))(lines(x)) if ÁØö(x, ÁÜÙ) else (x, None)))\n\ndef slice_ÞáÖùáÖï(áÖï, áÖý):\n    (áÖÞ := áØÁ[slice(áÖý[0], áÖý[2] + 1)])\n    if ãÊú(áÖÞ) == 1:\n        (áÖÞ := Âêà(áÖÞ[0][slice(áÖý[1], áÖý[3])]))\n    else:\n        (áÖÞ := [áÖÞ[0][slice(áÖý[1], None)], *áÖÞ[slice(1, -1)], áÖÞ[-1][slice(None, áÖý[3])]])\n    return Âøî(áÖÞ, \'\\n\')\n\n@áüíÞcache\ndef pad(áØÆ, áØÇ, áØÈ=\' \', áÖü=-1):\n    (ÄÊÞPSH((áüíËðâ(áØÆ), áüíËðâ(áØÇ))), ((l := ÄÊÞPKE(0)[0]), (áØÇ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n    if l >= áØÇ:\n        return áØÆ\n    (ÏÁ := (áØÇ - l))\n    if áÖü == -1:\n        return áØÆ + ÏÁ * áØÈ\n    if áÖü == 0:\n        return ÂîÌ([ÏÁ % 2 * áØÈ + áØÆ], ÏÁ // 2 * áØÈ)\n    if áÖü == 1:\n        return ÏÁ * áØÈ + áØÆ\n    ÂùÆ(False, \'%s∉\\U000f7c3e\\U000f7e3b1\' % (áÖü,))\n(padl := (lambda x, y, *áÑË: Âøî(ÁØòÁÙÄ(lambda ÂîÓ, ÂîÒ: pad(ÂîÓ, ÂîÒ, áÑË[0] if áÑË else \' \', áÖü=-1))(lines(x), áüíáüí(y)[0]), \'\\n\')))\n(padc := (lambda x, y, *áÑË: Âøî(ÁØòÁÙÄ(lambda ÂîÓ, ÂîÒ: pad(ÂîÓ, ÂîÒ, áÑË[0] if áÑË else \' \', áÖü=0))(lines(x), áüíáüí(y)[0]), \'\\n\')))\n(padr := (lambda x, y, *áÑË: Âøî(ÁØòÁÙÄ(lambda ÂîÓ, ÂîÒ: pad(ÂîÓ, ÂîÒ, áÑË[0] if áÑË else \' \', áÖü=1))(lines(x), áüíáüí(y)[0]), \'\\n\')))\n(linewrap := áüíÞcache(lambda áØÆ, d=80, p=4 * \' \': Âøî(ÁØò(lambda ÂîÓ: MOD(Áëý, áØÁ=áüíËðâ(ÂîÓ) > d)(ÂîÓ, lambda x: CURR(lambda ÂîÓ, ÂîÒ: ÂîÓ + \'\\n\' + linewrap(p + ÂîÒ, d, p), *tspl(x, d))))(lines(áØÆ)), \'\\n\')))\n(linenum := áüíÞcache(lambda áØÆ, m=1, s=ÄÕÍÔ: (lambda ÂîÓ: Âøî(ËãÂ(ÂåÔ((l := (ÂóÍ(ãÊú(ÄÝöì(ãÊú(ÂîÓ) - 1)), m) * Ãù)), ÂÓÏ(ÂîÓ)), CUR(lambda ÂîÓ, ÂîÒ: ÂÞÅÞCAT(MOD(ÄÝöì, áØÁ=l)(ÂîÓ), s) + \' \' + ÂîÒ)), \'\\n\'))(lines(áØÆ))))\n(linewnum := áüíÞcache(lambda áØÆ, m=1, s=ÄÕÍÔ, d=80, p=6 * \' \': linewrap(linenum(áØÆ, m, s), d, p)))\n\n@áüíÞcache\ndef pads(áØÆ, w=ë, h=ë):\n    if ÁØö(áØÆ, ÁÜÙ):\n        (áØÆ := lines(\'\\n\'))\n    if w is ë:\n        (w := MOD(ÂóÍ, áØÁ=0)(Áÿú(áØÆ, áüíËðâ)))\n    if h is ë:\n        (h := ãÊú(áØÆ))\n    if h is not None:\n        getattr(áØÆ, \'extend\')([\' \' * (w or 0)] * (h - ãÊú(áØÆ)))\n    if w is not None:\n        (ÄÊÞPSH(áØÆ), ÄÊÞPSH(ÁØò(lambda ÂîÓ: ÂîÓ + \' \' * (w - áüíËðâ(ÂîÓ)))(ÄÊÞPKE(0))), (áØÆ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]\n    return áØÆ\n\n@áüíÞcache\ndef stackr(*áÖê):\n    if not áÖê:\n        return ÁØã\n    (ÄÊÞPSH(áÖê), ((áØÆ := ÄÊÞPKE(0)[0]), *(áÖë := ÄÊÞPKE(0)[slice(1, None, None)])), ÄÊÞDEL(1))[1]\n    if ãÊú(áÖë) == 0:\n        return áØÆ\n    if ãÊú(áÖë) > 1:\n        return stackr(áØÆ, stackr(*áÖë))\n    (áØÇ := getattr(áÖë[0], \'split\')(\'\\n\'))\n    if (ãÊú(áØÆ) == ÄÊÞPSH(1) and ÄÊÞPOP() == ÄÊÞPSH(ãÊú(áØÇ))) and (ÄÊÞDEL(1) or True) or (ÄÊÞDEL(1) or False):\n        return áØÆ[0] + áØÇ[0]\n    return Âøî(ËãÂ(MOD(ÄÕåØ, áØÁ=ÁØã)(pads(áØÆ, ë, ãÊú(áØÇ)), áØÇ), ì), \'\\n\')\n\n@áüíÞcache\ndef box_(áØÆ, fg=\'05059f\', big=False):\n    (áØÆ := pads(áØÆ))\n    (áØÅ := (áüíËðâ(áØÆ[0]) if áØÆ else 0))\n    (áÓÕ := ÄÊÞCUR((1,), {}, Åøáüì, ÂýÃ, fg))\n    if ãÊú(áØÆ) == 1 and (not big):\n        return áÓÕ(\'[\') + áØÆ[0] + áÓÕ(\']\')\n    (ÄÊÞPSH(MOD(Áÿú, áØÁ=2)(ÂÛê(\'⎡⎢⎣\\u2009⎤⎥⎦\'), áÓÕ)), ((O := ÄÊÞPKE(0)[0]), (C := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n    if big:\n        return Âøî([ÂÞÅÞCAT(\'┌\' + ÂÞÅÞCAT(\'─\', áØÅ) + \'┐\', áÓÕ), *ÁØò(lambda ÂîÓ: O[1] + ÂîÓ + C[1])(áØÆ), ÂÞÅÞCAT(\'└\' + ÂÞÅÞCAT(\'─\', áØÅ) + \'┘\', áÓÕ)], \'\\n\')\n    return Âøî(ËãÂ(Ááú(áØÆ, ÂÞÅÞCAT(2, [1])), lambda x, y, z: O[(n := (1 - (x is None) + (z is None)))] + y + C[n]), \'\\n\')\n(ÄÊÞPSH(ÁØò(lambda ÂîÓ: lambda x, *áÑË, **áÑÕ: box_(Âøî(x, \'\\n\') if ÁØö(x, áÍá | áÍé) else x, *áÑË, **áÑÕ, big=ÂîÓ))(ÂÿÇ(2))), ((box := ÄÊÞPKE(0)[0]), (BOX := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n(fmp := {**dict(ÄÕåØ([ÁØã, ÂÞÅ, ÂýÃ, ÄÔýò, True, False, None, ÃÆë, ÃÆì, ÃÆ, ÂÑõ, ÃÅ, ÂÑø, ÂÑü, ÂÑò, ÂÑÿ, ÂÑó, ÂÑô, ÂÑö, ÂÑù, ÄÝóú, ÄÝôÀ, ÃÇ, ÂÑú, ÄÝóû, ÂÒÀ, ÄÝôÏ, ÂÑû, ÄÝóü, ÄÝôË, ÂÑý, ÄÝóý, ÂÒÁ, ÄÝôÂ, ÄÝóÿ, ÂÒÂ, ÄÝôÃ, ÄÝôÐ, ÄÝôÄ, ÄÝôÑ, ÂÒî, ÄÝôÒ, Ïî, ÂÐæ, ÂÕË, Ãù, Ïò, ÄÝøà, ÄÝøá, ÄÝøâ, ÄÝîá, ÄÝîâ, ÄÝîä, ÄÝîå, ÄÝîæ, ÄÝîç, ÄÝîè, ÄÝîã, áÍÚ, áÍä, áÍÙ, áÍÖ, áÍá, áÍé, áÍè, ÁÜÙ, áÍÞ, áÍÛ, áÍî], \'ᐦ␀⬤\\U000f0b88✓✗□ⴳⴴ½⅓¼⅕⅙⅐⅛⅑⅒⅔⅖\\U000f7db2\\U000f7db7¾⅗\\U000f7db3⅜\\U000f7dc6⅘\\U000f7db4\\U000f7dc2⅚\\U000f7db5⅝\\U000f7db9\\U000f7db6⅞\\U000f7dba\\U000f7dc7\\U000f7dbb\\U000f7dc8↉\\U000f7dc9πℇ∞îτ\\U000f7e8d\\U000f7e8e\\U000f7e8f\\U000f7c69\\U000f7c6a\\U000f7c6c\\U000f7c6d\\U000f7c6e\\U000f7c6f\\U000f7c70\\U000f7c6b𝑒𝑜𝑑𝑏𝑙𝑡𝑠ᔐ𝑖𝑓𝑦\'))})\n(ÄÊÞPSH(fmp), ÄÊÞPSH(MOD(ËãÂ, áØÁ=ì)(ÄÊÞPKE(0), lambda x, y: H(y))), (fmp := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]\n(ÄÊÞPSH(ÁØò(lambda ÂîÓ: Åøáüì(ÂîÓ, \'ff3\'))(\',[]{}⟶\')), ((COM := ÄÊÞPKE(0)[0]), (BL := ÄÊÞPKE(0)[1]), (BR := ÄÊÞPKE(0)[2]), (CL := ÄÊÞPKE(0)[3]), (CR := ÄÊÞPKE(0)[4]), (ARW := ÄÊÞPKE(0)[5])), ÄÊÞDEL(1))[1]\n(ÄÊÞPSH((ÁØö(ÐÌü(ÂÑÖ())) | ÁØö(ÐÌü(ÂÑØ())) | áÍÙ, áÍá | áÍé)), ((áÌý := ÄÊÞPKE(0)[0]), (áÍÆ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n\ndef áÓÙáÓàáÓç(x):\n    try:\n        if x in fmp:\n            return fmp[x]\n    except:\n        None\n    (T := ÁØö(x))\n    if T is type:\n        return H(getattr(x, \'__name__\'))\n    if T is ÁÜÙ:\n        return Åøáüì(ÁÜÙ(x), bg=\'202\')\n    if T is áÍÞ:\n        return ÁÜÙ(áÍÞ(x))\n    if T is áÍÛ:\n        return ÁÜÙ(MOD(Âäû, áØÁ=5)(x))\n    if ÁØö(x, áÌý):\n        return (ÁØã if ÁØö(x) is áÍÙ else áÓÙáÓàáÓç(ÁØö(x))) + CL + Âøî(ËãÂ(getattr(x, \'items\')(), lambda x, y: \'%s%s%s\' % (áÓÙáÓàáÓç(x), ARW, áÓÙáÓàáÓç(y))), \' \') + CR\n    if ÁØö(x, áÍè):\n        return (ÁØã if ÁØö(x) is áÍè else áÓÙáÓàáÓç(ÁØö(x))) + CL + Âøî(Áÿú(x, áÓÙáÓàáÓç), \' \') + CR\n    if ÁØö(x, áÍÆ):\n        return (ÁØã if ÁØö(x) is áÍá else áÓÙáÓàáÓç(ÁØö(x))) + BL + Âøî(Áÿú(x, áÓÙáÓàáÓç), \' \') + BR\n    if ÁØö(x, áÓó):\n        return \'%s\' % (H(getattr(x, \'__name__\')),)\n    return ÁÜÙ(x)\n(Æø := (lambda *áÑË, **áÑÕ: áÑË[0] if ÂåÔ(Âçß(áÓÙáÓàáÓç(k[0] if ãÊú((k := (áÑË or [ÁØã]))) == 1 else k), **áÑÕ), áÑË) else ÁØã))\n__ÞÄÊÞADD_EXPORTS__(globals(), (\'rm_esc\', rm_esc), (\'lines\', lines), (\'padl\', padl), (\'padc\', padc), (\'padr\', padr), (\'pads\', pads), (\'stackr\', stackr), (\'box\', box), (\'BOX\', BOX), (\'linenum\', linenum), (\'linewnum\', linewnum), (\'dotrim\', dotrim), (\'slice_ÞáÖùáÖï\', slice_ÞáÖùáÖï), (\'áüíËðâ\', áüíËðâ), (\'Åøáüì\', Åøáüì), (\'áÓÙáÓàáÓç\', áÓÙáÓàáÓç), (\'Æø\', Æø))\n\ndef test_text_format():\n    Âçß(Âøî(tspl(Åøáüì(\'egg\', \'f00\') + Åøáüì(\'weeee\', \'0f0\'), 5), \'│\'))\n    Âçß(linewrap(Âçß(linenum("egg salad number twelve fortnite\\nthe last thing you\'d want on your burg")), 12, 3 * \' \'))\n    (a := Âçß(box(\'jo⭥∈ease\\nasoidasdeeee\')))\n    (b := Âçß(BOX(\'jo⭥∈ease\\nasoidasdeeee\')))\n    (c := Âçß(box(\'5⭥ᐵ²\')))\n    (d := Âçß(BOX(\'5⭥ᐵ²\')))\n    Âçß(stackr(a, \'a\\nb\\nc\\nd\\ne\', b, c, d))\n    Âçß(padl(\'egg\', 11, \'─\'))\n    Âçß(padl(\'egg\', 11, \' \'))\n    Âçß(padc(\'egg\', 11, \' \'))\n    Âçß(padc(\'egg\', 11, \'─\'))\n    Âçß(padc(\'lul\', 10, \'─\'))\n    Âçß(padc(\'lads\\nx\', 10, \'─\'))\n    Âçß(padc(\'lads\\nx\', \'jo\\naaa\', \'─\'))\n    Âçß(padc(\'egg\', 11, \' \'))\n    Âçß(padr(\'egg\', 11, \' \'))\n    Âçß(padr(\'egg\', 11, \'─\'))',__TMP__:=globals().copy())
for k,v in __TMP__.get("__EXPORTS__",{}).items():globals()[k]=v


# /home/ganer/Projects/Moon_BETA/NewMoon/Libraries/𝐍.☾⟶/tmp/α/compiled_$$home$$ganer$$Projects$$Moon_BETA$$NewMoon$$Libraries$$𝐍.☾.py
exec("\n__file__='/home/ganer/Projects/Moon_BETA/NewMoon/Libraries/𝐍.☾'\n__ÞÄÊÞIMPORT__('text_format', globals())\nfrom collections import deque as áÐòáÑÁ\n\nclass áÌÑ:\n    (__slots__ := ('t', 'c'))\n\n    def __init__(ÄÕÒü, t, *c):\n        (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH('t'), ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH('c'), ÄÊÞPSH((t, c or [])), (setattr(ÄÊÞPKE(4), ÄÊÞPKE(3), ÄÊÞPKE(0)[0]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)[1])), ÄÊÞDEL(5))[5]\n    (__getitem__ := (lambda ÄÕÒü, i: getattr(ÄÕÒü, 'c')[i]))\n    (__iter__ := (lambda ÄÕÒü: iter(getattr(ÄÕÒü, 'c'))))\n    (__repr__ := (lambda ÄÕÒü: '𝐍⟨%s⟩⟨%s⟩' % (getattr(ÄÕÒü, 't') or '∅', Âøî(ÄÕÒü, ', '))))\n    (__len__ := (lambda ÄÕÒü: ãÊú(getattr(ÄÕÒü, 'c'))))\n    (ft := staticmethod(lambda x: áÌÑ(x[0], *(Áÿú(x[1], getattr(áÌÑ, 'ft')) if ÁØö(x[1], áÍá | áÍé) and ãÊú(x[1]) == 2 else [x[1]]))))\n    (tt := (lambda ÄÕÒü: (getattr(ÄÕÒü, 't'), Áÿú(getattr(ÄÕÒü, 'c'), lambda x: ÐÌü(getattr(x, 'tt')) if ÁØö(x, áÌÑ) else x))))\n    (copy := (lambda ÄÕÒü, t=None, c=None: ÁØö(ÄÕÒü)(getattr(ÄÕÒü, 't') if t is None else t, *(getattr(ÄÕÒü, 'c') if c is None else c))))\n    (rcopy := (lambda ÄÕÒü, t=None: ÁØö(ÄÕÒü)(getattr(ÄÕÒü, 't') if t is None else t, *(Áÿú(getattr(ÄÕÒü, 'c'), getattr(ÁØö(ÄÕÒü), 'rcopy')) if ÁØö(ÄÕÒü, áÌÑ) else ÄÕÒü))))\n    (filter := (lambda ÄÕÒü, Æå, *áÑË, **áÑÕ: getattr(ÄÕÒü, 'extract')(Âåæ(Âó, f), *áÑË, **áÑÕ, Ïà=False, ÏÁ=False)))\n    (ftrp := (lambda ÄÕÒü, fs, *áÑË, **áÑÕ: getattr(ÄÕÒü, 'frp')(lambda x: getattr(x, 't') in fs, *áÑË, **áÑÕ)))\n\n    def frp(ÄÕÒü, Æå, r, pre=False):\n        (áÏï := (lambda x: getattr(x, 'copy')(c=Áÿú(x, lambda x: getattr(x, 'frp')(Æå, r, pre)))))\n        (ÄÕÒü := (áÏï(ÄÕÒü) if pre else ÄÕÒü))\n        if Æå(ÄÕÒü):\n            return r(ÄÕÒü)\n        return ÄÕÒü if pre else áÏï(ÄÕÒü)\n\n    def extract(ÄÕÒü, áÍÛ, E=None, Ïà=True, ÏÁ=False, pre=False):\n        (L := (ÄÊÞPSH(([], [] if (Ïá := (E is None)) else E)), ((r := ÄÊÞPKE(0)[0]), (E := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1])\n        (áÚì := ÄÊÞCUR((1,), {'pre': pre}, getattr((ÂÐá := ÁØö(ÄÕÒü)), 'extract'), ÂýÃ, áÍÛ, E))\n        Áÿú(ÄÕÒü, lambda x: getattr(L[ÂÞÅÞCAT(áÍÖ, ÂÞÅÞCAT(áÍÛ, (x := MOD(Áëý, áØÁ=pre)(x, áÚì))))], 'append')(x))\n        (n := getattr(ÄÕÒü, 'copy')(c=r if pre else Áÿú(r, áÚì)))\n        return ([n, E] if ÏÁ else E) if Ïà and Ïá else n\n\n    def P(ÄÕÒü, fs=True):\n        (ÄÊÞPSH(ËãÂ(ÂÛê('∅\\u2009f00\\u205f→\\u200900f\\u205f\\U000f0141\\u2009ff0\\u205f\\U000f0142\\u2009ff0'), Åøáüì)), ((NA := ÄÊÞPKE(0)[0]), (AR := ÄÊÞPKE(0)[1]), (yl := ÄÊÞPKE(0)[2]), (yr := ÄÊÞPKE(0)[3])), ÄÊÞDEL(1))[1]\n        if ÄÝøÇ(ÄÕÒü, áÌÑ):\n            return Åøáüì(ÁÜÙ(ÄÕÒü), 'f00')\n\n        def format_e(e):\n            if not e:\n                return ÁØã\n            (r := ËãÂ(e, lambda x, y: ÄÔýò if x in {'T', 'p'} else '%s%s%s' % (x, AR, getattr(y, 't')) if ÁØö(y, ÅÒ) else '%s=%s' % (x, y)))\n            return MOD(Áëý, áØÁ=r)(ÁØã if 'p' not in e else Åøáüì((lambda ÂîÓ: Âøî(ËãÂ(ÄÕåØ(Áÿú(ÂÿÇ(ÂîÓ), ÁÛÛ([ÄÝõà, ÄÝõá])), ÂîÓ), ÂÕÅ)) if ãÊú(ÂîÓ) == 4 else ÄÝõà(Âøî(ÂîÓ, '…')))(getattr(e, 'p')), 'ff0'), lambda ÂîÓ: stackr(ÂîÓ, Âøî(r, '\\n')))\n        (áØÀ := box((ÂÞÅÞCAT(False, getattr(getattr(ÄÕÒü, 't'), 'P')) if ÁØö(getattr(ÄÕÒü, 't'), áÌÑ) else stackr(Åøáüì(getattr(ÄÕÒü, 't'), 'f55'), ÂÞÅÞCAT(getattr(ÄÕÒü, 'e'), format_e)) if ÁØö(ÄÕÒü, ÅÒ) else ÁÜÙ(getattr(ÄÕÒü, 't'))) or NA, fg='0f0' if ÁØö(ÄÕÒü, ÅÒ) and getattr(getattr(ÄÕÒü, 'e'), 'T') else '00007f'))\n        if ãÊú(ÄÕÒü):\n            (ÄÊÞPSH(Áÿú('─╰├┬│', ÄÊÞCUR((1,), {'fg': '11a'}, Åøáüì, ÂýÃ))), ((ÂâÑ := ÄÊÞPKE(0)[0]), (ÂäÇ := ÄÊÞPKE(0)[1]), (Ââî := ÄÊÞPKE(0)[2]), (ÂãÀ := ÄÊÞPKE(0)[3]), (ÂâÓ := ÄÊÞPKE(0)[4])), ÄÊÞDEL(1))[1]\n            (áØÀ := stackr(áØÀ, Âøî(ËãÂ(ÂÓÏ(ÄÕÒü), lambda x, y: Âøî(ËãÂ(ÂÓÏ(ÂÞÅÞCAT(ÂÞÅÞCAT(False, getattr(y, 'P')), lines)), CUR(lambda ÂîÓ, ÂîÒ: ÂÁÍ(ì)(ÂîÒ, ÂâÑ if ((ÄÊÞDEL(1), False)[1] if ÄÊÞPSH(ÂîÓ) else ÄÊÞPOP() if ãÊú(ÄÕÒü) != 1 else (ÄÊÞDEL(1), True)[1]) else ÂîÓ and ' ' or ÂäÇ if x == ãÊú(ÄÕÒü) - 1 else x and Ââî or ÂãÀ if ((ÄÊÞDEL(1), False)[1] if ÄÊÞPSH(ÂîÓ) else ÄÊÞPOP() if ãÊú(ÄÕÒü) == 0 else (ÄÊÞDEL(1), True)[1]) else ÂâÓ))), '\\n')), '\\n')))\n        return ÂåÔ(Âçß(áØÀ), ÄÕÒü) if fs else áØÀ\n\nclass ÅÒ(áÌÑ):\n    (__slots__ := ('t', 'c', 'e'))\n\n    def __init__(ÄÕÒü, t, *c, e=ÂÞÅ):\n        (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH('t'), ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH('c'), ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH('e'), ÄÊÞPSH((t, [*c] if c else [], MOD(ÂÑÖ, áØÁ=None)() if e is ÂÞÅ else e)), (setattr(ÄÊÞPKE(6), ÄÊÞPKE(5), ÄÊÞPKE(0)[0]), setattr(ÄÊÞPKE(4), ÄÊÞPKE(3), ÄÊÞPKE(0)[1]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)[2])), ÄÊÞDEL(7))[7]\n    (__contains__ := (lambda ÄÕÒü, x: x in getattr(ÄÕÒü, 'e') if ÁØö(x, ÁÜÙ) else x in getattr(ÄÕÒü, 'c')))\n    (__repr__ := (lambda ÄÕÒü: 'Ń(%s│%s)⟨%s⟩' % (getattr(ÄÕÒü, 't') or '∅', getattr(ÄÕÒü, 'e') or '∅', Âøî(ÄÕÒü, ', '))))\n    (__setitem__ := (lambda ÄÕÒü, x, y: (ÄÊÞPSH(getattr(ÄÕÒü, 'c')), ÄÊÞPSH(x), ÄÊÞPSH(y), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]))\n    (__and__ := (lambda ÄÕÒü, x: getattr(ÄÕÒü, 't') == getattr(x, 't')))\n\n    def __getitem__(ÄÕÒü, i):\n        return getattr(ÄÕÒü, 'c')[i]\n\n    def __delitem__(ÄÕÒü, i):\n        del getattr(ÄÕÒü, 'c')[i]\n\n    def set(ÄÕÒü, t=None, c=None, e=None):\n        if t is not None:\n            (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH('t'), ÄÊÞPSH(t), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n        if c is not None:\n            (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH('c'), ÄÊÞPSH(c), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n        if e is not None:\n            (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH('e'), ÄÊÞPSH(e), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n        return ÄÕÒü\n    (cp := (copy := (lambda ÄÕÒü, t=None, c=None, e=ÂÞÅ: ÁØö(ÄÕÒü)(getattr(ÄÕÒü, 't') if t is None else t, *(getattr(ÄÕÒü, 'c') if c is None else c), e=ÐÌü(getattr(getattr(ÄÕÒü, 'e'), 'copy')) if e is ÂÞÅ else e))))\n    (cpr := (rcopy := (lambda ÄÕÒü, t=None: ÁØö(ÄÕÒü)(getattr(ÄÕÒü, 't') if t is None else t, *Áÿú(getattr(ÄÕÒü, 'c'), getattr(ÁØö(ÄÕÒü), 'rcopy')), e=getattr(getattr(ÄÕÒü, 'e'), 'copy')()) if ÁØö(ÄÕÒü, áÌÑ) else ÄÕÒü)))\n\n    def part(ÄÕÒü):\n        (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH('c'), ÄÊÞPSH(ÂÕÃ(getattr(ÄÕÒü, 'c'), getattr(ÄÕÒü, 'e') ** ì)), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n        return (ÄÕÒü, getattr(ÄÕÒü, 'e'))\n\n    def frp(ÄÕÒü, Æå, r, pre=False, not_T=True):\n        if r is None:\n            return lambda r: getattr(ÄÕÒü, 'frp')(Æå, r, pre, not_T)\n        if not_T:\n            (Æå := (lambda ÄÕÒü, Æå=Æå: not getattr(getattr(ÄÕÒü, 'e'), 'T') and Æå(ÄÕÒü)))\n        if pre:\n            if not ãÊú(ÄÕÒü):\n                return r(ÄÕÒü) if Æå(ÄÕÒü) else ÄÕÒü\n            (ÄÊÞPSH((áÐòáÑÁ([ÄÕÒü]), áÐòáÑÁ())), ((áÖå := ÄÊÞPKE(0)[0]), (áÖæ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n            (ÄÊÞPSH((getattr(áÖå, 'popleft'), getattr(áÖå, 'extend'), getattr(áÖæ, 'appendleft'))), ((pl := ÄÊÞPKE(0)[0]), (ex := ÄÊÞPKE(0)[1]), (al := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]\n            while áÖå:\n                (C := pl())\n                ex([c for c in C if getattr(c, 'c')])\n                al(C)\n            for C in áÖæ:\n                for i, c in enumerate(C):\n                    if not Æå(c):\n                        continue\n                    (ÄÊÞPSH(C), ÄÊÞPSH(i), ÄÊÞPSH(r(c)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n            return r(ÄÕÒü) if Æå(ÄÕÒü) else ÄÕÒü\n        else:\n\n            def áÏï(ÄÕÒü):\n                if Æå(ÄÕÒü):\n                    return r(ÄÕÒü)\n                for i, y in enumerate(ÄÕÒü):\n                    (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH(i), ÄÊÞPSH(áÏï(y)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n                return ÄÕÒü\n            return áÏï(ÄÕÒü)\n\n    def ftrp(ÄÕÒü, fs, Æå, pre=False, not_T=True, **áÏè):\n        if Æå is None:\n            return lambda Æå: getattr(ÄÕÒü, 'ftrp')(fs, Æå, pre, not_T, **áÏè)\n        if ÄÝøÇ(fs, ÁÜÙ):\n            (fs := frozenset(fs))\n        return ÄÕÒü if not_T and getattr(getattr(ÄÕÒü, 'e'), 'T') else getattr(ÄÕÒü, 'frp')((lambda x: getattr(x, 't') == fs) if ÁØö(fs, ÁÜÙ) else lambda x: getattr(x, 't') in fs, Æå, pre, not_T, **áÏè)\n\n    def gets(ÄÕÒü, Æå, not_T=True):\n        if not áÓó(Æå):\n            if ÁØö(Æå, ÁÜÙ):\n                (Æå := (lambda ÄÕÒü, t=Æå: getattr(ÄÕÒü, 't') == t))\n            else:\n                (Æå := (lambda ÄÕÒü, t=Æå: getattr(ÄÕÒü, 't') in t))\n        return [c for c in ÄÕÒü if (((ÄÊÞDEL(1), False)[1] if getattr(getattr(c, 'e'), 'T') else ÄÊÞPOP()) if ÄÊÞPSH(not_T) else (ÄÊÞDEL(1), True)[1]) and Æå(c)]\n\n    def find(ÄÕÒü, Æå, pre=True, not_T=True, R=None):\n        if R is None:\n            (R := [])\n        if not_T and getattr(getattr(ÄÕÒü, 'e'), 'T'):\n            return R\n        if pre:\n            for c in ÄÕÒü:\n                getattr(c, 'find')(Æå, True, not_T, R)\n        if (do := Æå(ÄÕÒü)):\n            getattr(R, 'append')(ÄÕÒü)\n        if do and (not pre):\n            for c in ÄÕÒü:\n                getattr(c, 'find')(Æå, False, not_T, R)\n        return R\n\n    def flat(ÄÕÒü, Æå, áÑÂ=True):\n        (C := [])\n        for c in ÄÕÒü:\n            (getattr(C, 'append') if getattr(getattr(c, 'e'), 'T') or not Æå((c := (getattr(c, 'flat')(Æå) if áÑÂ else c))) else getattr(C, 'extend'))(c)\n        (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH('c'), ÄÊÞPSH(C), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n        return ÄÕÒü\n\n    def rm(ÄÕÒü, Æå, not_T=True):\n        if ÁØö(Æå, ÁÜÙ):\n            (Æå := (lambda ÄÕÒü, t=Æå: getattr(ÄÕÒü, 't') == t))\n        for i, x in ÂÓÏ(ÄÕÒü)[slice(None, None, -1)]:\n            if not (((ÄÊÞDEL(1), False)[1] if getattr(getattr(x, 'e'), 'T') else ÄÊÞPOP()) if ÄÊÞPSH(not_T) else (ÄÊÞDEL(1), True)[1]):\n                continue\n            if Æå(x):\n                del ÄÕÒü[i]\n            else:\n                getattr(ÄÕÒü[i], 'rm')(Æå, not_T)\n        return ÄÕÒü\n\n    def __pos__(ÄÕÒü):\n        (áØÀ := '')\n        if getattr(getattr(ÄÕÒü, 'e'), 'T'):\n            return getattr(ÄÕÒü, 't')\n        (áÖã := áÐòáÑÁ(getattr(ÄÕÒü, 'c')))\n        while áÖã:\n            (v := getattr(áÖã, 'popleft')())\n            if getattr(getattr(v, 'e'), 'T'):\n                (ÄÊÞPSH(áØÀ), ÄÊÞPSH(ÄÊÞPKE(0) + getattr(v, 't')), (áØÀ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]\n            else:\n                getattr(áÖã, 'extendleft')(reversed(getattr(v, 'c')))\n        return áØÀ\n\n    def lchar(ÄÕÒü):\n        if getattr(getattr(ÄÕÒü, 'e'), 'T') and getattr(ÄÕÒü, 't'):\n            return getattr(ÄÕÒü, 't')[0]\n        for c in getattr(ÄÕÒü, 'c'):\n            if not (x := getattr(c, 'lchar')()):\n                continue\n            return x\n        return ''\n\n    def rchar(ÄÕÒü):\n        if getattr(getattr(ÄÕÒü, 'e'), 'T') and getattr(ÄÕÒü, 't'):\n            return getattr(ÄÕÒü, 't')[-1]\n        for c in getattr(ÄÕÒü, 'c')[slice(None, None, -1)]:\n            if not (x := getattr(c, 'rchar')()):\n                continue\n            return x\n        return ''\n\n    def farnodes(ÄÕÒü, Æå=lambda ÂîÓ: not getattr(getattr(ÂîÓ, 'e'), 'T')):\n        (Ïß := (Ïà := ÄÕÒü))\n        while Æå(Ïß) and ãÊú(Ïß):\n            (Ïß := Ïß[0])\n        while Æå(Ïà) and ãÊú(Ïà):\n            (Ïà := Ïà[-1])\n        return (Ïß, Ïà)\n\n    def first_l(ÄÕÒü, Æå):\n        if Æå(ÄÕÒü):\n            return ÄÕÒü\n        for áÎÚ in ÄÕÒü:\n            if not (l := getattr(áÎÚ, 'first_l')(Æå)) is not None:\n                continue\n            return l\n\n    def first_r(ÄÕÒü, Æå):\n        if Æå(ÄÕÒü):\n            return ÄÕÒü\n        for áÎÚ in ÄÕÒü[slice(None, None, -1)]:\n            if not (r := getattr(áÎÚ, 'first_r')(Æå)) is not None:\n                continue\n            return r\n\n    def first_sides(ÄÕÒü, Æå):\n        return (getattr(ÄÕÒü, 'first_l')(Æå), getattr(ÄÕÒü, 'first_r')(Æå))\n    (filter := (lambda ÄÕÒü, Æå, *áÑË, **áÑÕ: getattr(ÄÕÒü, 'rm')(Âåæ(Âó, Æå), *áÑË, **áÑÕ)))\n    (as_txt := __pos__)\n__ÞÄÊÞADD_EXPORTS__(globals(), ('ÅÒ', ÅÒ))\n\ndef test_ÞÅÒ():\n    ÐÌü(getattr(ÅÒ('the', ÅÒ('joe', e=ÂÞÅÞCAT({'T': True, 'p': [2, 4], 'swag': 'loog'}, MOD(ÂÑÖ, áØÁ=None)())), ÅÒ('egg', ÅÒ('egg2'), ÅÒ('egg3', e=ÂÞÅÞCAT({'T': True, 'p': [1, 2, 3, 4]}, MOD(ÂÑÖ, áØÁ=None)())))), 'P'))",__TMP__:=globals().copy())
for k,v in __TMP__.get("__EXPORTS__",{}).items():globals()[k]=v


# /home/ganer/Projects/Moon_BETA/NewMoon/Libraries/peggle2/main.☾⟶/tmp/α/compiled_$$home$$ganer$$Projects$$Moon_BETA$$NewMoon$$Libraries$$peggle2$$main.☾.py
exec('\n__file__=\'/home/ganer/Projects/Moon_BETA/NewMoon/Libraries/peggle2/main.☾\'\n(fcache := (lambda: lambda Æå: Æå))\n__ÞÄÊÞIMPORT__(\'𝐍\', globals())\n__ÞÄÊÞIMPORT__(\'text_format\', globals())\ntry:\n    import regex as re\nexcept Exception:\n    import re\n(show_cache_table := (lambda áÍÌ, ÂÑÎ: ËãÂ(ÂÓÏ(ÂÑÎ), lambda i, v: ËãÂ(ÄÔàÑ(ÂÑÖ()(v) ** ë), lambda x, y: Âçß(\'%s,%s\\t%s\\t%s\' % (i, x, áÍÌ[x], y))))))\n(áÐè := (lambda x: ÅÒ(x, e=MOD(ÂÑÖ, áØÁ=None)()(T=True))))\n(áÐÍÞ_ := None)\n\ndef áÏñ(s=ÁØã):\n    global áÐÍÞ_\n    if áÐÍÞ_ is None:\n        Âçß(\'Starting timer\')\n        (áÐÍÞ_ := ÐÌü(time))\n        return\n    Âçß(\'%s took %ss\' % (s, ÐÌü(time) - áÐÍÞ_))\n    (áÐÍÞ_ := None)\n\n@ÐÌü(fcache)\ndef gram_convert(ÄÕÒü):\n    (name_remaps := ÂÑÖ()(ÄÕåØ(ÂÛê(\'elm_o\\u2009elm_a\\u2009assign_cln\\u2009group_inner\\u2009group\'), \'∨∧←∧∧\')))\n    (TT := (lambda ÄÕÒü: (getattr(ÄÕÒü, \'t\'), *((getattr(ÄÕÒü[0], \'t\'),) if getattr(ÄÕÒü, \'t\') in \'ᔐ~\' else (getattr(ÄÕÒü[0], \'t\'), *Áÿú(ÄÕÒü[slice(1, None)], TT)) if getattr(ÄÕÒü, \'t\') == \'←\' else Áÿú(ÄÕÒü, TT)))))\n    (escape := (lambda x, t=\'ݺ\': getattr(getattr(getattr(x, \'replace\')(2 * \'␛\', t), \'replace\')(\'␛\', ÁØã), \'replace\')(t, \'␛\')))\n\n    def reduce_j(ÄÕÒü):\n        (ÄÊÞPSH(ÄÕÒü), ((Ïß := ÄÊÞPKE(0)[0]), (o := ÄÊÞPKE(0)[1]), (Ïà := ÄÊÞPKE(0)[2]), *(C := ÄÊÞPKE(0)[slice(3, None, None)])), ÄÊÞDEL(1))[1]\n        if C:\n            ÂùÆ(False)\n        if getattr(o, \'t\') == \'↷\':\n            return ÅÒ(\'∧\', Ïß, Ïà, Ïß)\n        elif getattr(o, \'t\') == \'⯆\':\n            return ÅÒ(\'∨\', ÅÒ(\'∧\', Ïà, ÅÒ(\'+\', ÅÒ(\'∧\', Ïß, Ïà))), Ïà)\n        elif getattr(o, \'t\') == \'△\':\n            return ÅÒ(\'∨\', ÅÒ(\'∧\', ÅÒ(\'*\', ÅÒ(\'∧\', Ïß, Ïà)), Ïß), Ïß)\n        elif getattr(o, \'t\') == \'▽\':\n            return ÅÒ(\'∨\', ÅÒ(\'∧\', ÅÒ(\'∧\', Ïà, ÅÒ(\'*\', ÅÒ(\'∧\', Ïß, Ïà)))), ÅÒ(\'✓\'))\n        elif getattr(o, \'t\') == \'⯅\':\n            return ÅÒ(\'∧\', ÅÒ(\'+\', ÅÒ(\'∧\', Ïß, Ïà)), Ïß)\n        ÂùÆ(False)\n\n    def bad(ÄÕÒü):\n        if getattr(ÄÕÒü, \'t\') in ÂÛê(\'comment\\u2009w\\u2009W\'):\n            return True\n        if ((not getattr(ÄÕÒü, \'t\') and ãÊú(ÄÕÒü) == 1) and getattr(getattr(getattr(ÄÕÒü, \'c\')[0], \'e\'), \'T\')) and getattr(getattr(ÄÕÒü, \'c\')[0], \'t\') in \'()∧∨:=\':\n            return True\n\n    def collapse_ao(ÄÕÒü):\n        if getattr(getattr(ÄÕÒü, \'e\'), \'T\'):\n            return ÄÕÒü\n        (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH(\'c\'), ÄÊÞPSH(getattr(ÄÊÞPKE(1), ÄÊÞPKE(0))), ÄÊÞPSH(MOD(ÂøÑ, áØÁ=ÂÚü())(Áÿú(ÄÊÞPKE(0), lambda x: getattr(x, \'c\') if (getattr((x := collapse_ao(x)), \'t\') == ÄÊÞPSH(getattr(ÄÕÒü, \'t\')) and ÄÊÞPOP() in ÄÊÞPSH(\'∧∨\')) and (ÄÊÞDEL(1) or True) or (ÄÊÞDEL(1) or False) else [x]))), setattr(ÄÊÞPKE(3), ÄÊÞPKE(2), ÄÊÞPKE(0)), ÄÊÞDEL(4))[4]\n        return ÄÕÒü\n\n    def parse_elm(N):\n        (ÄÊÞPSH((+N[0], N[1], +N[2])), ((Ïß := ÄÊÞPKE(0)[0]), (n := ÄÊÞPKE(0)[1]), (Ïà := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]\n        (ÄÊÞPSH(MOD(ÐÌÛ, áØÁ=áÍÖ)(Ïß, ÄÊÞCUR((1,), {}, ÂÔó, ÂýÃ, \'❗⠶ƨ\'))), ((l1 := ÄÊÞPKE(0)[0]), (l2 := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n        for o in (*l1, *Ïà, *l2):\n            if o == \'~\':\n                (n := ÅÒ(o, áÐè(getattr(re, \'compile\')(+n))))\n            else:\n                (n := ÅÒ(o, n))\n        return n\n    (rules := getattr(getattr(getattr(getattr(getattr(getattr(ÄÕÒü, \'rm\')(bad), \'ftrp\')(ÂÛê(\'prefix\\u2009suffix\'), lambda x: ÅÒ(getattr(x, \'t\'), áÐè(+x))), \'ftrp\')(\'str\', lambda x: ÅÒ(\'ᔐ\', áÐè(escape((+x)[slice(1, -1)])))), \'ftrp\')(name_remaps ** î, lambda x: ÅÒ(name_remaps[getattr(x, \'t\')], *[y for y in x if not getattr(getattr(y, \'e\'), \'T\')]), True), \'flat\')(lambda x: getattr(x, \'t\') == \'_elm_j\'), \'find\')(lambda x: getattr(x, \'t\') == \'assign_eql\'))\n    (rules := ÂÑÖ()(Áÿú(rules, lambda x: (+x[0], x[2]))))\n    for k, ÄÕÒü in rules:\n        (ÄÕÒü := getattr(getattr(getattr(getattr(collapse_ao(getattr(getattr(ÄÕÒü, \'ftrp\')(ÂÛê(\'assign_eql\'), lambda x: x[0], True), \'flat\')(lambda x: getattr(x, \'t\') in ÂÛê(\'∧\\u2009∨\\u2009elm_j\') and ãÊú(x) == 1)), \'ftrp\')(\'elm_j\', reduce_j, True), \'ftrp\')(\'elm\', parse_elm, True), \'ftrp\')(\'←\', lambda x: ÅÒ(getattr(x, \'t\'), áÐè(getattr(x[0][0], \'t\')), *x[slice(1, None)]), True), \'ftrp\')(\'rname\', lambda x: áÐè(\'_\' * (getattr(x[0], \'t\') not in \'✓✗\') + getattr(x[0], \'t\'))))\n        if getattr(ÄÕÒü, \'t\') in \'∧∨\' and ãÊú(ÄÕÒü) == 1:\n            (ÄÕÒü := ÄÕÒü[0])\n        (ÄÊÞPSH(rules), ÄÊÞPSH(k), ÄÊÞPSH(TT(ÄÕÒü)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n    return rules\n\ndef parse(áÌý, áÍÌ, start_rule=None, debug=False):\n    (ÄÊÞPSH((Áÿú(ÄÝöÊ(ãÊú(áÌý)), lambda x: {}), 0)), ((ÂÑÎ := ÄÊÞPKE(0)[0]), (Ïõ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n    (áÏð := [(None, ãÊú(áÍÌ) - 1 if start_rule is None else start_rule)])\n    while áÏð:\n        (ÄÊÞPSH(getattr(áÏð, \'pop\')(-1)), ((ÏÔ := ÄÊÞPKE(0)[0]), (Ïç := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n        if ÏÔ is not None:\n            (Ïõ := ÏÔ)\n        (ÄÊÞPSH(áÍÌ[Ïç]), ((Ïá := ÄÊÞPKE(0)[0]), *(áÌü := ÄÊÞPKE(0)[slice(1, None, None)])), ÄÊÞDEL(1))[1]\n        if debug:\n            (V := Âøî(ÁØò(lambda ÂîÓ: áÍÌ[ÂîÓ[1]][0])(áÏð), \' \'))\n            Âçß(\'%s%s%s%s %s %s %s\' % (áÌý[slice(None, Ïõ)], Åøáüì(\'│\', fg=\'0f0\'), áÌý[Ïõ] if Ïõ < ãÊú(áÌý) else ÁØã, áÌý[slice(Ïõ + 1, None)], V, Åøáüì(Ïá, \'f5f\'), dotrim(áÓÙáÓàáÓç(áÌü), 75)))\n        (áÐñ := ÂÑÎ[Ïõ])\n        if Ïá == \'ᔐ\':\n            if áÌü[0] == áÌý[slice(Ïõ, (áÚù := (Ïõ + ãÊú(áÌü[0]))))]:\n                (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH((True, áÚù)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n            else:\n                (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH((False, Ïõ)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n        elif Ïá == \'~\':\n            if (m := getattr(áÌü[0], \'match\')(áÌý, Ïõ)):\n                (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH((True, getattr(m, \'span\')()[1], m)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n            else:\n                (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH((False, Ïõ)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n        elif Ïá == \'∧\':\n            (ÄÊÞPSH(áÐñ[Ïç] if Ïç in áÐñ else (0, Ïõ)), ((n := ÄÊÞPKE(0)[0]), (áÚù := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n            while True:\n                (ÄÊÞPSH((áÌü[n], ÂÑÎ[áÚù])), ((áÚê := ÄÊÞPKE(0)[0]), (áÍØ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n                if áÚê not in áÍØ:\n                    getattr(áÏð, \'extend\')([(Ïõ, Ïç), (áÚù, áÚê)])\n                    (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH((n, áÚù)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n                    break\n                (ÄÊÞPSH(ÂÑÎ[áÚù][áÚê][slice(None, 2)]), ((áÍÜ := ÄÊÞPKE(0)[0]), (áÚù := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n                (ÄÊÞPSH(n), ÄÊÞPSH(ÄÊÞPKE(0) + 1), (n := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]\n                if not áÍÜ:\n                    (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH((False, Ïõ)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n                    break\n                if n == ãÊú(áÌü):\n                    (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH((True, áÚù)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n                    break\n        elif Ïá == \'∨\':\n            (n := (áÐñ[Ïç] if Ïç in áÐñ else 0))\n            while True:\n                (ÄÊÞPSH((áÌü[n], ÂÑÎ[Ïõ])), ((áÚê := ÄÊÞPKE(0)[0]), (áÍØ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n                if áÚê not in áÍØ:\n                    getattr(áÏð, \'extend\')([(Ïõ, Ïç), (Ïõ, áÚê)])\n                    (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH(n), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n                    break\n                (ÄÊÞPSH(ÂÑÎ[Ïõ][áÚê][slice(None, 2)]), ((áÍÜ := ÄÊÞPKE(0)[0]), (áÚù := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n                if áÍÜ:\n                    (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH((True, áÚù, n)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n                    break\n                (ÄÊÞPSH(n), ÄÊÞPSH(ÄÊÞPKE(0) + 1), (n := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]\n                if n == ãÊú(áÌü):\n                    (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH((False, Ïõ)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n                    break\n        elif Ïá == \'*\' or \'+\' == Ïá:\n            if Ïç in áÐñ:\n                (c := áÐñ[Ïç])\n            else:\n                (c := (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH([Ïõ]), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3])\n            (ÄÊÞPSH((áÌü[0], c[-1])), ((áÚê := ÄÊÞPKE(0)[0]), (áÚù := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n            while True:\n                (áÍØ := ÂÑÎ[áÚù])\n                if áÚê not in áÍØ:\n                    getattr(áÏð, \'extend\')([(Ïõ, Ïç), (áÚù, áÚê)])\n                    break\n                (ÄÊÞPSH(áÍØ[áÚê][slice(None, 2)]), ((áÍÜ := ÄÊÞPKE(0)[0]), (ÏÔ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n                if not áÍÜ:\n                    if Ïá == \'*\' or ãÊú(c) > 1:\n                        (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH((True, áÚù, c[slice(None, -1)])), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n                    else:\n                        (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH((False, Ïõ)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n                    break\n                getattr(c, \'append\')((áÚù := ÏÔ))\n        elif Ïá == \'✓\':\n            (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH((True, Ïõ)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n        elif Ïá == \'←\':\n            if áÌü[1] not in áÐñ:\n                getattr(áÏð, \'extend\')([(Ïõ, Ïç), (Ïõ, áÌü[1])])\n            else:\n                (ÄÊÞPSH(áÐñ[áÌü[1]][slice(None, 2)]), ((áÍÜ := ÄÊÞPKE(0)[0]), (áÚù := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n                (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH((áÍÜ, áÚù, áÌü[1])), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n        elif áÌü[0] not in áÐñ:\n            getattr(áÏð, \'extend\')([(Ïõ, Ïç), (Ïõ, áÌü[0])])\n        else:\n            (ÄÊÞPSH(áÐñ[áÌü[0]][slice(None, 2)]), ((áÍÜ := ÄÊÞPKE(0)[0]), (áÚù := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n            if Ïá == \'?\':\n                (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH((True, áÚù, áÍÜ)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n            elif Ïá == \'¬\':\n                (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH((not áÍÜ, Ïõ)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n            elif Ïá == \'⮞\':\n                (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH((áÍÜ, Ïõ)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n            elif Ïá == \'❗\':\n                ÂùÆ(áÍÜ)\n                (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH((áÍÜ, áÚù)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n            elif Ïá == \'✗\':\n                ÂùÆ(False, \'Hit an ✗\')\n            else:\n                (ÄÊÞPSH(áÐñ), ÄÊÞPSH(Ïç), ÄÊÞPSH((áÍÜ, áÚù)), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n    return ÂÑÎ\n\ndef make_rules(r):\n    (Æå := (lambda ÂîÓ: áÍé(Áÿú(ÂîÓ, Æå)) if ÁØö(ÂîÓ, áÍá | áÍé) else ÂîÓ))\n    (nmp := ÂÞÅÞCAT(ÄÕåØ(r ** î, ÂÿÇ(r)), ÂÑÖ()))\n    (ÄÊÞPSH(r), ÄÊÞPSH(MOD(ËãÂ, áØÁ=ë)(ÄÊÞPKE(0), CUR(lambda ÂîÓ, ÂîÒ: (\'_\' + ÂîÓ, Æå(ÂîÒ))))), (r := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]\n    (áÌÆ := ÂÑÖ()(ÄÕåØ(r ** î, (áÌÕ := Áÿú(r ** î, MOD(Âêà, áØÁ=áÍé))))))\n\n    def áÑÞ(r):\n        if ãÊú(r) == 1 and r[0][0] == \'_\':\n            return (r[0],)\n        if r in áÌÆ:\n            return áÌÆ[r]\n        if ÁØö(r[0], áÍÞ):\n            (r := (áÌÕ[(áÐø := r[0])][0], *r[slice(1, None)]))\n        else:\n            getattr(áÌÕ, \'append\')((áÐø := ãÊú(áÌÕ)))\n        if r[0] == \'←\':\n            (r := (r[0], r[1], áÑÞ(r[2])))\n        elif r[0] in \'✓✗\':\n            (r := (r[0], áÐø))\n        elif r[0] not in \'ᔐ~\':\n            (r := (r[0], *Áÿú(r[slice(1, None)], áÑÞ)))\n        return ÂåÔ((ÄÊÞPSH(áÌÕ), ÄÊÞPSH((ÄÊÞPSH(áÌÆ), ÄÊÞPSH(r), ÄÊÞPSH(áÐø), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]), ÄÊÞPSH(r), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3], áÐø)\n    áÑÞ((\'T_root\', *Áÿú(ÄÕåØ(nmp ** ì, r ** ì), áÍé)))\n    (ÄÊÞPSH(áÌÕ), ÄÊÞPSH(Áÿú(ÄÊÞPKE(0), lambda x: (x[0], *Áÿú(x[slice(1, None)], lambda ÂîÓ: ÂîÓ if ÄÝøÇ(ÂîÓ, áÍé) else MOD(ÄÔÞÔ, ÁÜñ=ÄÕøü)(r ** î, ÄÊÞCUR((1,), {}, ÂÖÑ, ÂýÃ, ÂîÓ[0])))))), (áÌÕ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]\n    return MOD(ÂÑÖ, áØÁ=áÌÕ)() | nmp\n\ndef parse_to_tree(áÍÌ, ÂÑÎ, Ïõ, Ïç, show_table=False, raise_failed=True):\n    (rec := (lambda *áÑË: parse_to_tree(áÍÌ, ÂÑÎ, *áÑË, raise_failed=raise_failed)))\n    (ÄÊÞPSH(áÍÌ[Ïç]), ((Ïá := ÄÊÞPKE(0)[0]), *(C := ÄÊÞPKE(0)[slice(1, None, None)])), ÄÊÞDEL(1))[1]\n    if Ïç not in (áÐñ := ÂÑÎ[Ïõ]):\n        return (Ïá, \'‼∄‼\')\n    (ÄÊÞPSH(áÐñ[Ïç]), ((áÍÜ := ÄÊÞPKE(0)[0]), (áÚù := ÄÊÞPKE(0)[1]), *(áÌú := ÄÊÞPKE(0)[slice(2, None, None)])), ÄÊÞDEL(1))[1]\n    if raise_failed:\n        ÂùÆ(áÍÜ, \'Failed to parse tree!\')\n    if Ïá == \'∧\':\n        (o := [])\n        for r in C:\n            getattr(o, \'append\')(rec(Ïõ, r))\n            if r not in (áÐñ := ÂÑÎ[Ïõ]):\n                break\n            (Ïõ := áÐñ[r][1])\n        return (Ïá, *o)\n    if Ïá == \'ᔐ\':\n        return (Ïá, C[0])\n    if Ïá == \'?\':\n        return (Ïá, *(áÌú and (áÌú[0] and MOD(Âêà, áØÁ=áÍé)(rec(Ïõ, C[0]))) or ()))\n    if not áÌú and Ïá in {*\'∨*+~←\'}:\n        return (Ïá, \'‼∅‼\')\n    if Ïá == \'~\':\n        return (Ïá, getattr(áÌú[0], \'group\')(0))\n    if Ïá == \'∨\':\n        return (Ïá, rec(Ïõ, C[áÌú[0]]))\n    if Ïá == \'←\':\n        return (Ïá, C[0], rec(Ïõ, áÌú[0]))\n    if Ïá in {*\'*+\'}:\n        return (Ïá, *[rec(x, C[0]) for x in áÌú[0]])\n    if Ïá in {*\'✓✗⮞¬\'}:\n        return (Ïá,)\n    return (getattr(Ïá, \'removeprefix\')(\'_\'), rec(Ïõ, C[0]))\n\ndef chop_tree(ÄÕÒü, áÌý, remove_trashes=True, remove_failed_questions=True, remove_lookaheads=True, include_positions=True, track_length=True, DEBUG=False):\n    (ÂÐñ := (áÏñ if DEBUG else ÃÆì))\n    (pops := {*\'∧∨*+❗⠶?\'})\n    (removes := {*\'\\U000f01b4\' * remove_trashes + \'⮞¬\' * remove_lookaheads})\n\n    def reform_str(ÄÕÒü):\n        if getattr(ÄÕÒü, \'t\') in {\'ᔐ\', \'~\'}:\n            (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH(\'t\'), ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH(\'c\'), ÄÊÞPSH(getattr(ÄÕÒü, \'e\')), ÄÊÞPSH(\'T\'), ÄÊÞPSH((getattr(getattr(ÄÕÒü, \'c\')[0], \'t\'), [], True)), (setattr(ÄÊÞPKE(6), ÄÊÞPKE(5), ÄÊÞPKE(0)[0]), setattr(ÄÊÞPKE(4), ÄÊÞPKE(3), ÄÊÞPKE(0)[1]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)[2])), ÄÊÞDEL(7))[7]\n        else:\n            for c in ÄÕÒü:\n                reform_str(c)\n        return ÄÕÒü\n    ÐÌü(ÂÐñ)\n    reform_str(ÄÕÒü)\n    ÂÐñ(\'Reform_str\')\n    if include_positions:\n        ÂÕÅ((Æå := (lambda ÄÕÒü, i=0: (ÄÊÞPSH(getattr(ÄÕÒü, \'e\')), ÄÊÞPSH(\'p\'), ÄÊÞPSH((i, MOD(Áëý, áØÁ=getattr(getattr(ÄÕÒü, \'e\'), \'T\'))(ÄÕÒü, (ÄÊÞCUR((1,), {\'áØÁ\': i}, ÆÑ, ÂýÃ, ÂÕì(Æå)), lambda ÂîÓ: ãÊú(+ÂîÓ) + i)))), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3][1])), ÄÕÒü)\n    (parsed_len := (ãÊú(+ÄÕÒü) if track_length else None))\n\n    def Æå(ÄÕÒü):\n        if getattr(getattr(ÄÕÒü, \'e\'), \'T\'):\n            return True\n        if getattr(ÄÕÒü, \'t\') in removes:\n            return\n        if remove_failed_questions and getattr(ÄÕÒü, \'t\') == \'?\':\n            if not getattr(ÄÕÒü, \'c\'):\n                return\n            (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH(\'c\'), ÄÊÞPSH([*filter(Æå, getattr(ÄÕÒü, \'c\'))]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n            if not getattr(ÄÕÒü, \'c\'):\n                return\n            return True\n        (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH(\'c\'), ÄÊÞPSH([*filter(Æå, getattr(ÄÕÒü, \'c\'))]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n        return True\n    ÐÌü(ÂÐñ)\n    Æå(ÄÕÒü)\n    ÂÐñ(\'Removes\')\n\n    def splat(ÄÕÒü):\n        (C := [])\n        for c in ÄÕÒü:\n            if getattr(getattr(c, \'e\'), \'T\'):\n                getattr(C, \'append\')(c)\n                continue\n            (v := splat(c))\n            if isinstance(v, áÍá):\n                getattr(C, \'extend\')(v)\n            elif getattr(c, \'t\') in pops:\n                if getattr(c, \'t\') == \'⠶\':\n                    for l in c:\n                        getattr(C, \'extend\')(getattr(l, \'c\'))\n                else:\n                    getattr(C, \'extend\')(getattr(c, \'c\'))\n            else:\n                getattr(C, \'append\')(c)\n        (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH(\'c\'), ÄÊÞPSH(C), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n    ÐÌü(ÂÐñ)\n    splat(ÄÕÒü)\n    ÂÐñ(\'Splats\')\n\n    def get_txt(ÄÕÒü):\n        if getattr(ÄÕÒü, \'t\') == \'ƨ\':\n            (l := \'\')\n\n            def Æå(ÄÕÒü):\n                nonlocal l\n                if getattr(getattr(ÄÕÒü, \'e\'), \'T\'):\n                    return (ÄÊÞPSH(l), ÄÊÞPSH(ÄÊÞPKE(0) + getattr(ÄÕÒü, \'t\')), (l := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]\n                for c in ÄÕÒü:\n                    Æå(c)\n            Æå(ÄÕÒü)\n            (e := ÂÑÖ()(T=True))\n            if include_positions:\n                (ÄÊÞPSH(ÐÌü(getattr(ÄÕÒü, \'farnodes\'))), ((Ïß := ÄÊÞPKE(0)[0]), (Ïà := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n                (ÄÊÞPSH(e), ÄÊÞPSH(\'p\'), ÄÊÞPSH((getattr(getattr(Ïß, \'e\'), \'p\')[0], getattr(getattr(Ïà, \'e\'), \'p\')[-1])), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n            (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH(\'t\'), ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH(\'c\'), ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH(\'e\'), ÄÊÞPSH((l, [], e)), (setattr(ÄÊÞPKE(6), ÄÊÞPKE(5), ÄÊÞPKE(0)[0]), setattr(ÄÊÞPKE(4), ÄÊÞPKE(3), ÄÊÞPKE(0)[1]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)[2])), ÄÊÞDEL(7))[7]\n            return\n        for c in ÄÕÒü:\n            get_txt(c)\n    ÐÌü(ÂÐñ)\n    get_txt(ÄÕÒü)\n    ÂÐñ(\'Get_txt\')\n\n    def set_arrows(ÄÕÒü):\n        if getattr(getattr(ÄÕÒü, \'e\'), \'T\'):\n            return\n        for i, c in enumerate(ÄÕÒü):\n            if getattr(getattr(c, \'e\'), \'T\'):\n                continue\n            if getattr(c, \'t\') == \'←\':\n                (ÄÊÞPSH(getattr(ÄÕÒü, \'e\')), ÄÊÞPSH(getattr(c[0], \'t\')), ÄÊÞPSH((ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH(i), ÄÊÞPSH(c[1]), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n            set_arrows(c)\n    ÐÌü(ÂÐñ)\n    set_arrows(ÄÕÒü)\n    ÂÐñ(\'Set arrows\')\n    if parsed_len is not None:\n        (ÄÊÞPSH(getattr(ÄÕÒü, \'e\')), ÄÊÞPSH(\'parse_len\'), ÄÊÞPSH(getattr(ÄÕÒü, \'e\')), ÄÊÞPSH(\'input_len\'), ÄÊÞPSH((parsed_len, ãÊú(áÌý))), (setattr(ÄÊÞPKE(4), ÄÊÞPKE(3), ÄÊÞPKE(0)[0]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)[1])), ÄÊÞDEL(5))[5]\n    return ÄÕÒü\n\ndef parse_to_node(ÄÕÒü):\n\n    def Æå(x, *áÑË):\n        return ÅÒ(x, *[Æå(*(x if isinstance(x, áÍé) else (x,))) for x in áÑË])\n    return Æå(*ÄÕÒü)\n\n@ÐÌü(fcache)\ndef peggle2_call(R, content, rule=\'main\', DEBUG=False, chop=True, **áÏè):\n    (ÄÊÞPSH((content, rule)), ((c := ÄÊÞPKE(0)[0]), (r := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n    (ÄÊÞPSH((getattr(R, \'T_root\'), R[r])), ((root := ÄÊÞPKE(0)[0]), (rule := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n    (ÂÐñ := (áÏñ if DEBUG else ÃÆì))\n    ÐÌü(ÂÐñ)\n    (ÂÑÎ := parse(c, root, rule, debug=DEBUG))\n    ÂÐñ(\'Parse\')\n    ÐÌü(ÂÐñ)\n    (ÄÕÒü := parse_to_tree(root, ÂÑÎ, 0, rule))\n    ÂÐñ(\'Convert\')\n    ÐÌü(ÂÐñ)\n    (ÄÕÒü := parse_to_node(ÄÕÒü))\n    ÂÐñ(\'Nodeing\')\n    (áÏÅ := (lambda **áÑÕ: chop_tree(ÄÕÒü, c, DEBUG=DEBUG, **áÏè | áÑÕ)))\n    return ÐÌü(áÏÅ) if chop else ÂÑÖ()(table=ÂÑÎ, tree=ÄÕÒü, chop=áÏÅ)\n\nclass peggle2:\n    (__slots__ := ÂÛê(\'rules\\u2009R\'))\n\n    def __init__(áÑÞ, g):\n        if ÁØö(g, ÁÜÙ):\n            (g := FROM_GRAM(g))\n        (ÄÊÞPSH(áÑÞ), ÄÊÞPSH(\'rules\'), ÄÊÞPSH(áÑÞ), ÄÊÞPSH(\'R\'), ÄÊÞPSH([getattr(g, \'rules\'), getattr(g, \'R\')] if ÁØö(g, peggle2) else [g, make_rules(g)]), (setattr(ÄÊÞPKE(4), ÄÊÞPKE(3), ÄÊÞPKE(0)[0]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)[1])), ÄÊÞDEL(5))[5]\n\n    def __repr__(áÑÞ):\n        return \'%s[%s Rules, %s Normalized]\' % (getattr(ÁØö(áÑÞ), \'__name__\'), ãÊú(getattr(áÑÞ, \'rules\')), ãÊú(getattr(getattr(áÑÞ, \'R\'), \'T_root\')))\n\n    def __contains__(áÑÞ, x):\n        return x in getattr(áÑÞ, \'rules\')\n\n    def __or__(áÑÞ, h, allow_conflict=False):\n        if ÁØö(h, áÑÞ):\n            (h := getattr(h, \'rules\'))\n        (conflict := ÂÕÖ(ÐÌü(getattr(getattr(áÑÞ, \'rules\'), \'keys\')), ÐÌü(getattr(h, \'keys\'))))\n        ÂùÆ(not (allow_conflict and conflict), \'Conflicting rules! %s\' % (conflict,))\n        return ÁØö(áÑÞ)(peggle2(getattr(áÑÞ, \'rules\') | h))\n\n    def __call__(áÑÞ, *áÑË, **áÑÕ):\n        return peggle2_call(getattr(áÑÞ, \'R\'), *áÑË, **áÑÕ)\n\n    def print_rules(áÑÞ):\n        ËãÂ(ÐÌü(getattr(getattr(áÑÞ, \'rules\'), \'items\')), lambda x, y: (Âçß(\'%s:\' % (x,)), Âçß(y)))\n\n    def print_normalized(áÑÞ):\n        ËãÂ(ÂÓÏ(getattr(getattr(áÑÞ, \'R\'), \'T_root\')), lambda x, y: Âçß(\'%s\\t%s\' % (x, Âøî(Áÿú(y, ÁÜÙ), \' \'))))\n(áÌÕ := Áÿú([\'[\\ueb26#][^\\n]*\', \'[⯅⯆△▽↷]\', \'"([^"␛]|␛.)*"\', "\'([^\'␛]|␛.)*\'", \'‹([^›␛]|␛.)*›\', \'[^⯅⯆△▽↷\\U000f01b4()?❗⮞.:⠶ƨ✗+*=¬∨∧~#\\ueb26‹\\\'" \\t\\n␛]+|✗\', \'[\\U000f01b4❗⮞⠶ƨ~¬]\', \'[*+?]\', \'([ \\t]|[\\\\\\\\␛]\\n)+\', \'([ \\t\\n]|[\\\\\\\\␛]\\n)+\'], getattr(re, \'compile\')))\n(GRANDMA_RULES := ÂÑÖ()({\'statements\': [\'∧\', (\'?\', [\'_W\']), (\'*\', [\'∧\', (\'∨\', [\'_comment\'], [\'_elm_o\']), (\'?\', [\'_W\'])])], \'comment\': [\'~\', áÌÕ[0]], \'elm_o\': [\'∧\', [\'_elm_a\'], (\'*\', [\'∧\', (\'?\', [\'_W\']), (\'ᔐ\', \'∨\'), (\'?\', [\'_W\']), [\'_elm_a\']])], \'elm_a\': [\'∧\', [\'_elm_j\'], (\'*\', [\'∧\', (\'∨\', [\'∧\', (\'?\', [\'_W\']), (\'ᔐ\', \'∧\'), (\'?\', [\'_W\'])], [\'?\', [\'_w\']]), [\'_elm_j\']])], \'elm_j\': [\'∨\', [\'__elm_j\'], [\'_elm\']], \'_elm_j\': [\'∧\', [\'_elm\'], (\'?\', [\'_W\']), (\'~\', áÌÕ[1]), (\'?\', [\'_W\']), (\'∨\', [\'__elm_j\'], [\'_elm\'])], \'elm\': [\'∧\', [\'_prefix\'], (\'∨\', [\'_assign_eql\'], [\'_assign_cln\'], [\'_group\'], [\'_str\'], [\'_rname\']), [\'_suffix\']], \'assign_eql\': [\'∧\', [\'_rname\'], (\'?\', [\'_W\']), (\'ᔐ\', \'=\'), (\'?\', [\'_W\']), [\'_elm_o\']], \'assign_cln\': [\'∧\', [\'_rname\'], (\'?\', [\'_W\']), (\'ᔐ\', \':\'), (\'?\', [\'_W\']), [\'_elm_j\']], \'group\': [\'∧\', (\'ᔐ\', \'(\'), (\'?\', [\'_W\']), [\'_group_inner\'], (\'ᔐ\', \')\')], \'group_inner\': [\'*\', (\'∧\', [\'_elm_o\'], [\'?\', [\'_W\']])], \'str1\': [\'~\', áÌÕ[2]], \'str2\': [\'~\', áÌÕ[3]], \'str3\': [\'~\', áÌÕ[4]], \'str\': [\'∨\', [\'_str1\'], [\'_str2\'], [\'_str3\']], \'rname\': [\'~\', áÌÕ[5]], \'prefix\': [\'∨\', (\'∧\', [\'?\', [\'_w\']], [\'+\', (\'∧\', [\'~\', áÌÕ[6]], [\'?\', [\'_W\']])]), (\'?\', [\'_w\'])], \'suffix\': [\'∨\', (\'∧\', [\'+\', (\'∧\', [\'?\', [\'_W\']], [\'~\', áÌÕ[7]])], [\'?\', [\'_w\']]), (\'?\', [\'_w\'])], \'w\': [\'~\', áÌÕ[8]], \'W\': [\'~\', áÌÕ[9]]}))\n(BOOTSTRAP := peggle2(GRANDMA_RULES))\n(FROM_GRAM := (lambda x: peggle2(gram_convert(BOOTSTRAP(x, \'statements\')))))\n__ÞÄÊÞADD_EXPORTS__(globals(), (\'peggle2\', peggle2))\n\ndef test_peggle2():\n    (GRAM := \'\\n                  main    = \\U000f01b4W? (entry \\U000f01b4W?)*\\n                  entry   = (\\n                      ƨ(section=\\U000f01b4\\\'[\\\' wrd \\U000f01b4\\\']\\\') \\U000f01b4W?\\n                      (pair = (\\n                          (bruh:key = ⠶wrd) \\U000f01b4(w? ↷ \\\'=\\\')\\n                          (value = (wrd ∨ str)+) \\U000f01b4W? ) )* )\\n                  str     = ~‹"[^"]+"›\\n                  wrd     = ~‹[-\\\\w]+›\\n                  w       = ~‹[ \\\\t]+›\\n                  W       = ~‹[ \\\\t\\\\n]+›\\n                  \')\n    (CONTENT := \'\\n                  [section1]\\n                  somekey = somevalue\\n                  someotherkey=someothervalue\\n                  [duawhdiawi]x=y\\n                  somekey =                 somevalue\\n                  someotherkey=✓□awhdapi\\n                  \')\n    (RULE := \'main\')\n    (gram := Âçß(peggle2(GRAM)))\n    (ÄÕÒü := gram(CONTENT, RULE))\n    ÐÌü(getattr(ÄÕÒü, \'P\'))',__TMP__:=globals().copy())
for k,v in __TMP__.get("__EXPORTS__",{}).items():globals()[k]=v


# /home/ganer/Projects/Moon_BETA/NewMoon/Libraries/peggle2/rgx_golfatron.☾⟶/tmp/α/compiled_$$home$$ganer$$Projects$$Moon_BETA$$NewMoon$$Libraries$$peggle2$$rgx_golfatron.☾.py
exec("\n__file__='/home/ganer/Projects/Moon_BETA/NewMoon/Libraries/peggle2/rgx_golfatron.☾'\n(fcache := (lambda: lambda Æå: Æå))\nfrom functools import cache\n(ÄÊÞPSH(('\\n\\\\^$.|?*+()[]{}', '\\\\]-')), ((ch1 := ÄÊÞPKE(0)[0]), (ch2 := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n(ST := 1113936)\n(CF := ((CT := ÂÑÖ()(ËãÂ(ÂÓÏ(ÁãÁ(ch1 + ch2)), ÂÕì(CUR(lambda ÂîÓ, ÂîÒ: [ÂîÓ, ÄÝöí(ST + ÂîÒ)]))))) ** ÂÕì))\n(IF := ((IT := ÂÑÖ()(ËãÂ(ÂÓÏ(ÁãÁ(ch1 + ch2)), ÂÕì(CUR(lambda ÂîÓ, ÂîÒ: [ÂîÓ, ÄÝöí(ãÊú(CF) + ST + ÂîÒ)]))))) ** ÂÕì))\n(OF := ((OT := ÂÑÖ()(ËãÂ(ÂÓÏ(ÁãÁ(ch1)), ÂÕì(CUR(lambda ÂîÓ, ÂîÒ: [ÂîÓ, ÄÝöí(ãÊú(IF) + ãÊú(CF) + ST + ÂîÒ)]))))) ** ÂÕì))\n(ÄÊÞPSH(ÁØò(lambda ÂîÓ: MOD(ËãÂ, áØÁ=î)(ÂîÓ, lambda x, y: ÄÝöí(x)))([CT, IT, OT])), ((CT := ÄÊÞPKE(0)[0]), (IT := ÄÊÞPKE(0)[1]), (OT := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]\n(ÄÊÞPSH(ÁØò(lambda ÂîÓ: MOD(ËãÂ, áØÁ=î)(ÂîÓ, lambda x, y: ÄÝöí(x)))([CF, IF, OF])), ((CF := ÄÊÞPKE(0)[0]), (IF := ÄÊÞPKE(0)[1]), (OF := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]\nÁØò(lambda ÂîÓ: (ÄÊÞPSH(IF), ÄÊÞPSH(ÄÝöí(IT[ÄÝöí(ÂîÓ)])), ÄÊÞPSH('\\\\' + ÂîÓ), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3])(ch2)\n(OF := MOD(ËãÂ, áØÁ=ì)(OF, lambda x, y: '\\\\' + y))\n(DASH := CT[ÄÝöí('-')])\n(ÄÊÞPSH((CT[ÄÝöí('[')], CT[ÄÝöí(']')])), ((BL := ÄÊÞPKE(0)[0]), (BR := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n(ÄÊÞPSH((CT[ÄÝöí('(')], CT[ÄÝöí(')')])), ((PL := ÄÊÞPKE(0)[0]), (PR := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n(ÄÊÞPSH((CT[ÄÝöí('?')], CT[ÄÝöí('|')])), ((Q := ÄÊÞPKE(0)[0]), (BAR := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n\ndef rgx_rans(x):\n    (ÄÊÞPSH(x), ÄÊÞPSH(ÄÔàÑ(ÄÊÞPKE(0), (áÚâ := (lambda x: ord(x[0]))))), (x := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]\n    (r := [])\n    for ÂîÓ in MOD(Ááú, áØÁ='!')(x):\n        (h := Áÿú(ÂîÓ, áÚâ))\n        getattr(r, 'append')(DASH if h[0] + h[1] + h[2] == ÂÞÅÞCAT(3, h[0]) + 3 else ÂîÓ[1])\n    return getattr(ÆÑ(r, lambda x, y: x + y * (y[-1] != x[-1])), 'translate')(IT)\n\n@ÐÌü(fcache)\ndef rgx_golfatron(áÑã):\n\n    @cache\n    def áüì(x):\n        (ÄÊÞPSH(MOD(ÐÌÛ, áØÁ=áÍÖ)(x)), ((t := ÄÊÞPKE(0)[0]), (Ïõ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n        return ËãÂ(ÂÑÖ()(ÐÌÛ(Ïõ, lambda x: x[0])), lambda x, y: (x, áüì((H := áÍé(Áÿú(y, lambda x: x[slice(1, None)])))), 1 if ÁØã in H and ÂØõ(H) else 0))\n\n    def ÐÉ(x):\n        (ÄÊÞPSH(MOD(ÐÌÛ, áØÁ=áÍÖ)(x, lambda x: len(x) != 1)), ((s := ÄÊÞPKE(0)[0]), (m := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n        (ÄÊÞPSH(m), ÄÊÞPSH(Áÿú(ÄÊÞPKE(0), lambda x: getattr(ÁØã, 'join')(getattr(x, 'translate')(OT)))), (m := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]\n        if (s := getattr(ÁØã, 'join')(s)):\n            getattr(m, 'append')(getattr(s, 'translate')(OT) if ãÊú(s) == 1 else BL + rgx_rans(s) + BR)\n        return m\n\n    def Åø(x):\n        (ÄÊÞPSH(x), ((Ïß := ÄÊÞPKE(0)[0]), (Ïà := ÄÊÞPKE(0)[1]), (Ïá := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]\n        (r := Ïß)\n        if Ïà and (Ïà := ÐÉ(Áÿú(Ïà, Åø))):\n            (h := getattr(BAR, 'join')(Ïà))\n            if Ïß and ãÊú(Ïà) > 1:\n                (h := (PL + h + PR))\n            (ÄÊÞPSH(r), ÄÊÞPSH(ÄÊÞPKE(0) + h), (r := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]\n        return r + Q if Ïá and Ïß else r\n    (áÑã := áüì(áÍé(sorted(áÑã, key=lambda x: (-ãÊú(x), x)))))\n    return getattr(getattr(getattr(Åø((ÁØã, áÑã, False)), 'translate')(CF), 'translate')(IF), 'translate')(OF)\n__ÞÄÊÞADD_EXPORTS__(globals(), ('rgx_golfatron', rgx_golfatron))",__TMP__:=globals().copy())
for k,v in __TMP__.get("__EXPORTS__",{}).items():globals()[k]=v


# /home/ganer/Projects/Moon_BETA/NewMoon/Libraries/peggle2/gram_tools.☾⟶/tmp/α/compiled_$$home$$ganer$$Projects$$Moon_BETA$$NewMoon$$Libraries$$peggle2$$gram_tools.☾.py
exec('\n__file__=\'/home/ganer/Projects/Moon_BETA/NewMoon/Libraries/peggle2/gram_tools.☾\'\n__ÞÄÊÞIMPORT__(\'𝐍\', globals())\n__ÞÄÊÞIMPORT__(\'peggle2$$main\', globals())\n__ÞÄÊÞIMPORT__(\'peggle2$$rgx_golfatron\', globals())\n__ÞÄÊÞIMPORT__(\'text_format\', globals())\n(nrm := (lambda ÄÕÒü: áÐè(ÄÕÒü) if ÁØö(ÄÕÒü, ÁÜÙ | ÂÑÅ) else ÄÕÒü))\n\ndef Âîë(ÄÕÒü, áÎÜ):\n    (ÄÕÒü := nrm(ÄÕÒü))\n    if ÁØö(áÎÜ, ÁÜÙ):\n        return ÄÕÒü\n    if ÄÝøÇ(áÎÜ, ÅÒ):\n        (áÎÜ := áÎÜ[0])\n    if \'p\' not in getattr(áÎÜ, \'e\'):\n        return ÄÕÒü\n    (ÄÊÞPSH(getattr(ÄÕÒü, \'e\')), ÄÊÞPSH(\'p\'), ÄÊÞPSH(getattr(getattr(áÎÜ, \'e\'), \'p\')[slice(None, 2)] * 2), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n    return ÄÕÒü\n\ndef Âîì(ÄÕÒü, áÎÜ):\n    (ÄÕÒü := nrm(ÄÕÒü))\n    if ÁØö(áÎÜ, ÁÜÙ):\n        return ÄÕÒü\n    if ÄÝøÇ(áÎÜ, ÅÒ):\n        (áÎÜ := áÎÜ[-1])\n    if \'p\' not in getattr(áÎÜ, \'e\'):\n        return ÄÕÒü\n    (ÄÊÞPSH(getattr(ÄÕÒü, \'e\')), ÄÊÞPSH(\'p\'), ÄÊÞPSH(getattr(getattr(áÎÜ, \'e\'), \'p\')[slice(2, None)] * 2), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n    return ÄÕÒü\n\ndef ÂØÙ(ÄÕÒü, áÎÜ):\n    (ÄÕÒü := nrm(ÄÕÒü))\n    if ÁØö(áÎÜ, ÁÜÙ) or ÄÝøÇ(áÎÜ, áÓö):\n        return ÄÕÒü\n    if ÄÝøÇ(áÎÜ, ÅÒ):\n        (áÎÜ := ÅÒ(ÁØã, *áÎÜ))\n    (ÄÊÞPSH(getattr(áÎÜ, \'first_sides\')(lambda ÂîÓ: ÂÔö(getattr(ÂîÓ, \'e\'), \'p\'))), ((l := ÄÊÞPKE(0)[0]), (r := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n    if l is None:\n        return ÄÕÒü\n    (ÄÊÞPSH(getattr(ÄÕÒü, \'e\')), ÄÊÞPSH(\'p\'), ÄÊÞPSH((*getattr(getattr(l, \'e\'), \'p\')[slice(None, 2)], *getattr(getattr(r, \'e\'), \'p\')[slice(2, None)])), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n    return ÄÕÒü\n\ndef ÂØØ(ÄÕÒü, áÎÜ):\n    (ÄÕÒü := nrm(ÄÕÒü))\n    (ÄÊÞPSH(getattr(ÄÕÒü, \'e\')), ÄÊÞPSH(\'p\'), ÄÊÞPSH((*getattr(getattr(áÎÜ[0], \'e\'), \'p\')[slice(2, None)], *getattr(getattr(áÎÜ[-1], \'e\'), \'p\')[slice(None, 2)])), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n    return ÄÕÒü\n\ndef áÍô(ÄÕÒü, áÎÜ):\n    (ÄÕÒü := nrm(ÄÕÒü))\n    if ÁØö(áÎÜ, ÁÜÙ):\n        return ÄÕÒü\n    (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH(\'e\'), ÄÊÞPSH(ÐÌü(getattr(getattr(áÎÜ, \'e\'), \'copy\'))), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n    return ÄÕÒü\n(áÎô := (lambda x, *áÑË, **áÑÕ: MOD(ÄÕéý, áØÁ=ÂØÙ)(ÅÒ(x, *áÑË, **áÑÕ), áÑË)))\n(áÐè := (lambda x, **áÑÕ: MOD(ÄÕéý, áØÁ=ÂØÙ)(ÅÒ(+x if ÁØö(x, ÅÒ) else ÁÜÙ(x), e=ÂÑÖ()(T=True, **getattr(áÑÕ, \'get\')(\'e\', {}))), x)))\n\ndef offset_ÞáÖï(ÄÕÒü, áÖý):\n    if \'p\' in getattr(ÄÕÒü, \'e\'):\n        (ÄÊÞPSH(getattr(ÄÕÒü, \'e\')), ÄÊÞPSH(\'p\'), ÄÊÞPSH((getattr(getattr(ÄÕÒü, \'e\'), \'p\')[0] + áÖý, getattr(getattr(ÄÕÒü, \'e\'), \'p\')[1] + áÖý)), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n    for c in ÄÕÒü:\n        offset_ÞáÖï(c, áÖý)\n    return ÄÕÒü\n\ndef offset_ÞáÖùáÖï(ÄÕÒü, áÖý):\n    if \'p\' in getattr(ÄÕÒü, \'e\'):\n        (áÖî := getattr(getattr(ÄÕÒü, \'e\'), \'p\'))\n        (ÄÊÞPSH(getattr(ÄÕÒü, \'e\')), ÄÊÞPSH(\'p\'), ÄÊÞPSH((áÖî[0] + áÖý[0], áÖî[1] if áÖî[0] else áÖî[1] + áÖý[1], áÖî[2] + áÖý[0], áÖî[3] if áÖî[2] else áÖî[3] + áÖý[1])), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n    for c in ÄÕÒü:\n        offset_ÞáÖùáÖï(c, áÖý)\n    return ÄÕÒü\n\ndef reform_positions(ÄÕÒü, áÖï):\n    (áÖß := (lambda ÂîÓ: ÄÕåØ(MOD(ÐÌ, áØÁ=0)(ÂîÓ, CUR(lambda ÂîÓ, ÂîÒ: ÂîÓ + 1 + ÂîÒ)), ÂîÓ))(Áÿú(lines(áÖï), ãÊú)))\n    (s := 0)\n\n    def Æå(ÄÕÒü):\n        nonlocal s\n        while áÖß[s][0] + áÖß[s][1] < getattr(getattr(ÄÕÒü, \'e\'), \'p\')[0]:\n            (ÄÊÞPSH(s), ÄÊÞPSH(ÄÊÞPKE(0) + 1), (s := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]\n        for i, x in enumerate(áÖß[slice(s, None)]):\n            if x[0] + x[1] >= getattr(getattr(ÄÕÒü, \'e\'), \'p\')[1]:\n                (ÄÊÞPSH(getattr(ÄÕÒü, \'e\')), ÄÊÞPSH(\'p\'), ÄÊÞPSH((s, getattr(getattr(ÄÕÒü, \'e\'), \'p\')[0] - áÖß[s][0], i + s, getattr(getattr(ÄÕÒü, \'e\'), \'p\')[1] - x[0])), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n                break\n        for z in ÄÕÒü:\n            Æå(z)\n    return ÂåÔ(Æå(ÄÕÒü), ÄÕÒü)\n(is_short := (lambda ÄÕÒü: getattr(getattr(ÄÕÒü, \'e\'), \'parse_len\') != getattr(getattr(ÄÕÒü, \'e\'), \'input_len\')))\n(warn_if_short := (lambda ÄÕÒü: MOD(ÂùÆ, áØÁ=ÂÄ)(not is_short(ÄÕÒü), \'Parse length warning %s<%s\' % (getattr(getattr(ÄÕÒü, \'e\'), \'parse_len\'), getattr(getattr(ÄÕÒü, \'e\'), \'input_len\')))))\n(gram_rp := (lambda áÖó, r, m=True: MOD(Áëý, áØÁ=m)(MOD(ÆÑ, áØÁ=áÖó)(MOD(ËãÂ, áØÁ=ì)(r, Âåæ(rgx_golfatron, ÂåÔ)), lambda x, y: MOD(ÄÔéÄ, áØÁ=x)(ÂîÌ([y[0]], \'%\'), y[1])), peggle2)))\n\ndef fill_ÞÄÕÒüÞ_holes_basic(ÄÕÒü):\n    if \'p\' not in getattr(ÄÕÒü, \'e\'):\n        (ÄÊÞPSH(getattr(ÄÕÒü, \'first_sides\')(lambda ÂîÓ: ÂÔö(getattr(ÂîÓ, \'e\'), \'p\'))), ((Ïß := ÄÊÞPKE(0)[0]), (Ïà := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n        if None is not Ïß and Ïà is not None:\n            (ÄÊÞPSH(getattr(ÄÕÒü, \'e\')), ÄÊÞPSH(\'p\'), ÄÊÞPSH((*getattr(getattr(Ïß, \'e\'), \'p\')[slice(None, 2)], *getattr(getattr(Ïà, \'e\'), \'p\')[slice(2, None)])), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n    for c in ÄÕÒü:\n        fill_ÞÄÕÒüÞ_holes_basic(c)\n    return ÄÕÒü\n\ndef gram_surgery(ÄÕÒü, holes=None, áÖÇ=0):\n\n    def Æå(ÄÕÒü):\n        nonlocal áÖÇ\n        if \'p\' not in getattr(ÄÕÒü, \'e\'):\n            return\n        if ÄÕÒü and (not getattr(getattr(ÄÕÒü, \'e\'), \'T\')):\n            for c in ÄÕÒü:\n                Æå(c)\n            (ÄÊÞPSH(ÐÌü(getattr(ÄÕÒü, \'farnodes\'))), ((Ïß := ÄÊÞPKE(0)[0]), (Ïà := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n            if \'p\' in getattr(Ïß, \'e\') and ÂÔö(getattr(Ïà, \'e\'), \'p\'):\n                (ÄÊÞPSH(getattr(ÄÕÒü, \'e\')), ÄÊÞPSH(\'p\'), ÄÊÞPSH((getattr(getattr(Ïß, \'e\'), \'p\')[0], getattr(getattr(Ïà, \'e\'), \'p\')[1])), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n            return\n        (ÄÊÞPSH((ÄÊÞPSH(getattr(ÄÕÒü, \'e\')), ÄÊÞPSH(\'p\'), ÄÊÞPSH((getattr(getattr(ÄÕÒü, \'e\'), \'p\')[0] + áÖÇ, getattr(getattr(ÄÕÒü, \'e\'), \'p\')[1] + áÖÇ)), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]), ((l := ÄÊÞPKE(0)[0]), (r := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n        while holes and holes[0][0] <= l:\n            (ÄÊÞPSH(áÖÇ), ÄÊÞPSH(ÄÊÞPKE(0) + (ÏÁ := getattr(holes, \'pop\')(0)[1])), (áÖÇ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]\n            (ÄÊÞPSH(getattr(ÄÕÒü, \'e\')), ÄÊÞPSH(\'p\'), ÄÊÞPSH((ÄÊÞPSH((l + ÏÁ, r + ÏÁ)), ((l := ÄÊÞPKE(0)[0]), (r := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]\n    Æå(ÄÕÒü)\n    return ÄÕÒü\n\ndef under_gram(ÄÕÒü):\n    (Ïâ := ÂÚü())\n    for r in getattr(ÄÕÒü, \'find\')(lambda ÂîÓ: ÂÔö(getattr(ÂîÓ, \'e\'), \'R\'), True, False):\n        getattr(Ïâ, \'append\')((getattr(getattr(r, \'e\'), \'p\')[0], ãÊú(+r)))\n    for r in getattr(ÄÕÒü, \'find\')(lambda ÂîÓ: ÂÔö(getattr(ÂîÓ, \'e\'), \'I\'), True, False):\n        getattr(Ïâ, \'append\')((getattr(getattr(r, \'e\'), \'p\')[1], ÄÝöâ(ãÊú(+r))))\n    getattr(ÄÕÒü, \'rm\')(lambda ÂîÓ: ÂÕÖ(getattr(ÂîÓ, \'e\') ** î, \'RI\'))\n    return (+ÄÕÒü, ÄÊÞCUR((1,), {}, gram_surgery, ÂýÃ, Ïâ))\n\ndef gram_subsup(x, áÔë=gram_rp(\'\\n            sup  = ~‹%SUP%+›\\n            sub  = ~‹%SUB%+›\\n            main = ((σscript = sup∨sub)∨~‹.|\\\\n›)*\\n        \', ÂÑÖ()(SUP=ÄÝõá(ë), SUB=ÄÝõà(ë))), r=\'main\'):\n    (Ëðá := (lambda x: getattr(áÔë(x, r, remove_trashes=False), \'ftrp\')(\'σscript\', lambda ÄÕÒü: getattr(ÄÕÒü, \'set\')(t=getattr(ÄÕÒü[0], \'t\'), c=[áÐè(\'\\U000f071e\\U000f071a\'[getattr(ÄÕÒü[0], \'t\')[-1] == \'p\'], e=MOD(ÂÑÖ, áØÁ=None)()(I=True, p=(getattr(getattr(ÄÕÒü, \'e\'), \'p\')[0], getattr(getattr(ÄÕÒü, \'e\'), \'p\')[0]))), *ÁØò(lambda ÂîÓ: offset_ÞáÖï(ÂîÓ, getattr(getattr(ÄÕÒü, \'e\'), \'p\')[0]))(Ëðá(ÄÝöË(+ÄÕÒü))), áÐè(\'\\U000f071b\', e=MOD(ÂÑÖ, áØÁ=None)()(I=True, p=(getattr(getattr(ÄÕÒü, \'e\'), \'p\')[1], getattr(getattr(ÄÕÒü, \'e\'), \'p\')[1])))]))))\n    return under_gram(Ëðá(x))\n\ndef peggrampeg(áÖï, ns={}, áÔë=peggle2(\'\\n           main = (brak∨~‹.|\\\\n›)*\\n           brak = \\U000f01b4‹%⦃› ~‹((?!⦄%).)*› \\U000f01b4‹⦄%›\\n        \'), m=True):\n    return MOD(Áëý, áØÁ=m)(+getattr(áÔë(áÖï), \'ftrp\')(\'brak\', lambda ÂîÓ: getattr(ÂîÓ, \'set\')(c=[áÐè(ÄÕôñ(+ÂîÓ, ns=ns))])), peggle2)\n__ÞÄÊÞADD_EXPORTS__(globals(), (\'peggle2\', peggle2), (\'ÅÒ\', ÅÒ), (\'áÎô\', áÎô), (\'áÐè\', áÐè), (\'Âîë\', Âîë), (\'Âîì\', Âîì), (\'ÂØÙ\', ÂØÙ), (\'ÂØØ\', ÂØØ), (\'áÍô\', áÍô), (\'offset_ÞáÖùáÖï\', offset_ÞáÖùáÖï), (\'offset_ÞáÖï\', offset_ÞáÖï), (\'reform_positions\', reform_positions), (\'gram_rp\', gram_rp), (\'under_gram\', under_gram), (\'gram_subsup\', gram_subsup), (\'peggrampeg\', peggrampeg), (\'is_short\', is_short), (\'warn_if_short\', warn_if_short), (\'fill_ÞÄÕÒüÞ_holes_basic\', fill_ÞÄÕÒüÞ_holes_basic))\n\ndef test_gram_tools():\n    (g := peggrampeg("\\n                        sub = \\U000f01b4\'\\U000f071e\' (sub ∨ sup ∨ ~‹[^\\U000f071b]›)* \\U000f01b4\'\\U000f071b\'\\n                        sup = \\U000f01b4\'\\U000f071a\' (sub ∨ sup ∨ ~‹[^\\U000f071b]›)* \\U000f01b4\'\\U000f071b\'\\n                        main = (sup ∨ sub ∨ (%⦃␛t+‹he›⦄%=~‹.›))*\\n                     "))\n    (ÄÊÞPSH(gram_subsup(Âçß(\'someᶜᵒᵒˡ\\U0010affe\\U0010aff5\\U0010aff6\\U0010affe\\U0010af7e₂k\'))), ((s := ÄÊÞPKE(0)[0]), (ÏÆ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]\n    (ÄÕÒü := ÐÌü(getattr(g(Âçß(s)), \'P\')))\n    ÐÌü(getattr(ÏÆ(ÄÕÒü), \'P\'))',__TMP__:=globals().copy())
for k,v in __TMP__.get("__EXPORTS__",{}).items():globals()[k]=v


__file__='/home/ganer/Projects/Moon_BETA/NewMoon/Libraries/Compiler/generate_operators.☾'
(OP_FILE := ð(getattr(ÂÞÅÞCAT(__file__, áÌî), 'parent'), 'operators'))
__ÞÄÊÞIMPORT__('peggle2', globals())

class áÍááÍá(áÍá):
    None
(ÄÊÞPSH((getattr(SCRIPT, 'sup'), getattr(SCRIPT, 'sub'), getattr(SCRIPT, 'nrm'))), ((sup := ÄÊÞPKE(0)[0]), (sub := ÄÊÞPKE(0)[1]), (nrm := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]
(ords := '0\U000f7c1c\U000f7c1d\U000f7c1e\U000f7c1f\U000f7c20\U000f7c21\U000f7c22\U000f7c23\U000f7c24\U000f7c25\U000f7c26\U000f7c27\U000f7c28\U000f7c29\U000f7c2a\U000f7c2b\U000f7c2c\U000f7c2d\U000f7c2e\U000f7c2f\U000f7c37\U000f7c30\U000f7c31\U000f7c3e')
(clrs := ÂÛê('0\u2009e3b\u2009f77\u2009c66\u2009b56\u20096cf\u2009b9d\u2009c08\u20090f5\u20091e6\u20092d7\u20093c8\u20094b9\u200985f\u200967f\u2009eae\u2009d8d\u2009c6c\u2009b4d\u2009ff5\u2009ce3\u2009bd2\u2009ad1\u2009fa2\u20090'))
(dummy_ords := {0, ãÊú(ords) - 1})
(minigram := Âåæ((Æå := (lambda ÂîÓ: getattr(ÂîÓ, 't') if getattr(getattr(ÂîÓ, 'e'), 'T') else (lambda ÂîÓ, ÂîÒ: Áÿú(ÂøÚ(ÂîÒ), Âøî) if ÂîÓ == '⨝' else ÄÔÙù(ÂîÒ))(getattr(ÂîÓ, 't'), Áÿú(ÂîÓ, Æå)))), peggle2("main=⨝=((∀=\U000f01b4'⟦'⠶⨝\U000f01b4'⟧') ∨ \U000f01b4'⁅'⨝\U000f01b4'⁆' ∨ ~'[^⟦⟧⁅⁆]')*")))

def parse_operator_file(contents):
    (p := UGX_CREATE(('B', (àìÒ := []), '*', None, ('B', (àìÒ := []), '', None, ('∨', ('∧', (lambda ÂîÓ: ãÊú(ÄÝöå(ÂîÓ, lambda ÂîÓ: ÂîÓ != ' ')) == 0, ''), ('P', (àìÒ := []), '*', MOD(ÁØò(lambda ÂîÓ: ÂîÓ[slice(MOD(ÂÛÒ, áØÁ=ÂÕË)()[0], None)])), ('∨', (Âåæ(Âó, Âüá), ''), (lambda ÂîÓ: ÄÝöç(ãÊú(ÄÝöå(ÂîÓ, lambda ÂîÓ: ÂîÓ != ' '))), '')))), (ÃÆë, ''))))))
    (g_order := (lambda ÂîÒ: MOD(ÄÔÞÔ, ÁÜñ=ÄÕøü)(ords, ÂîÒ)))
    (g_symbs := (lambda ÂîÓ: ÂÞÅÞCAT(MOD(ÄÕÊÄ, áØÁ=ÁØã)(áÇù(ÂîÓ, lambda ÂîÓ: ÂîÓ in sup('αλςν')), 2), ÐàÒ(CUR(ÁØòÁÙÄ(lambda ÂîÓ, ÂîÒ: [ÂîÓ, ÂîÒ]))))))
    (g_sig := ÄÕÍÔ)
    (g_combos := minigram)
    (g_desc := (lambda x: Áÿú(ÂøÚ(UGX_CREATE(('B', (àìÒ := []), '*', None, ('∨', ('B', (àìÒ := []), '*', lambda ÂîÓ: ÄÔÔè(ÄÝöÜ(ÂîÓ, ','), ','), ('∧', (lambda ÂîÓ: ÄÔýò if ÂîÓ == '{' else None, ''), (lambda ÂîÓ: ÂîÓ != '}', '*'), (lambda ÂîÓ: ÄÔýò if ÂîÓ == '}' else None, ''))), ('B', (àìÒ := []), '*', Âåæ(Âêà, Âøî), (lambda ÂîÓ: ÂîÓ != '{', '')))))(x)), Âøî)))
    (ÆåÞs := [g_order, g_symbs, g_sig, g_combos, g_desc])
    (áÖï := ÄÝöÞ(contents, '\n'))
    (ÄÊÞPSH(MOD(ÐÌÛ, áØÁ=áÍÖ)(áÖï, lambda ÂîÓ: ÂîÓ[0] == '>')), ((áÖï := ÄÊÞPKE(0)[0]), (áÖå := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    (áÖï := p(áÖï))
    (ops := ÄÔàÑ(ÁØò(lambda ÂîÓ: MOD(ËãÂ, áØÁ=0)(áÇù(ÄÝöÊ(ËãÂ(ÄÕåØ(MOD(ÁÞç, áØÁ=slice(None, 4))(MOD(ÁÞç, áØÁ=slice(None, 1))(Áÿú(MOD(ÄÝöÞ, áØÁ=3)(ÂîÓ[0], '\u2009'), Âüá), lambda ÂîÓ: ÄÝöÞ(ÂîÓ[0])), MOD(ÁØò(lambda ÂîÓ: MOD(ÄÔéÄ, áØÁ=ÂîÓ)(' ', ÁØã)))), ÆåÞs), lambda x, y: y(x)), [0, 2, 3, 1, 4]), 2), lambda x, y: ÁØÿÁÙÇ(lambda ÂîÓ, ÂîÒ: ÄÔÙù(ÂîÓ, ÂîÒ))(ÄÔÙù(x, Âêà(Âøî(ÄÝöÊ(1, ÂîÓ), '\n'))), ÄÕåØ(y))))(áÖï), MOD(ÁÛÛ, áØÁ=(0, 0))))
    (ops := áÍááÍá(ops))
    (ÄÊÞPSH(ops), ÄÊÞPSH('style'), ÄÊÞPSH(Áÿú(áÖå, MOD(ÁÝÖ, áØÁ=0))), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    return ops

def get_operator_table(parsed_ops, do_join=False):
    (infer := (lambda ÂîÓ: ('ᴮ' if ÂÔö(ÂîÓ, '∧') else 'ᴾ\U000f0012' if ÂÔö(ÂîÓ, '\U000f7ea4') else 'ᴾᴮʳ' if ÂÔö(ÂîÓ, '\U000f7e0f') else '\U000f0012ᴮˡ' if ÂÔö(ÂîÓ, '\U000f7e10') else 'ᴾ\U000f0012ᴮ' if ÂÕÖ(ÂîÓ, '∨⩚') else ('ᴾ' if ÂîÓ[0] == '.' else '\U000f0012') if ÂÔö(ÂîÓ, '.') else ÁØã) + 'ᴺ' + ('\U000f0037' if ÂÕÖ(ÂîÓ, '\U000f7ea4\U000f7e0f\U000f7e10∨⩚') and ÂîÓ[0] != ÂîÓ[-1] else ÁØã)))
    (áØÀ := ËãÂ(ÂÑÖ()(ÐÌÛ(ÄÔÔè(ÄÔÙù(parsed_ops), lambda ÂîÓ: ÂîÓ[0] in dummy_ords), MOD(ÁÛÛ, áØÁ=0))), CUR(lambda ÂîÓ, ÂîÒ: ÁØò(lambda ÂîÓ: MOD(ÁÞç, áØÁ=-1)(ÂîÓ[4], CURR(lambda ÂîÓ, ÂîÒ: ÂîÓ + ÂîÒ, infer(ÂîÓ[1]))))(ÂîÒ))))
    return Âøî(ÁØò(lambda ÂîÓ: Âøî(ÁØò(lambda ÂîÓ: Âøî(ÂîÓ))(ÂîÓ), ' '))(áØÀ), '\n') if do_join else áØÀ

def generate_fontcompose_conf(parsed_ops):
    (style := getattr(parsed_ops, 'style'))
    return Âøî(ËãÂ(ÂÑÖ()(ÐÌÛ(ÄÔÙù(parsed_ops), MOD(ÁÛÛ, áØÁ=0))), CUR(lambda ÂîÓ, ÂîÒ: '%s⟦⁅BLK%s𝕊⟶"%s"⁆%s⟧' % (ÁØã if ÂîÓ in dummy_ords else '⦑c⦑%s⦒⦒' % (clrs[ÂîÓ],), ÂîÓ, ords[ÂîÓ], Âøî(ÁØò(lambda ÂîÓ: '⁅%s⟶"%s"⁆' % (MOD(ÄÔéÄ, áØÁ=ÂîÓ[3])('"', '␛"')[slice(1, None)] if 'ᴍ' in ÂîÓ[3] else ';;%sᴍ' % (ÂîÓ[3],), MOD(Áëý, áØÁ=lambda ÂîÓ: ÂîÓ == '␛')(ÂîÓ[4][0], lambda ÂîÓ: ÂÞÅÞCAT(ÂîÓ, 2))))(ÂîÒ))))), '\n') + ÂîÊ(style, '\n')

def to_docs(parsed_ops):
    return ÁØò(lambda ÂîÓ: MOD(ÁÞç, áØÁ=-1)(ÂîÓ, MOD(ÁÛÛ, áØÁ=0)))(Áÿú(MOD(ËãÂ, áØÁ=2)(MOD(ÁÛÛ, áØÁ=(slice(None, None), slice(None, None), slice(1, None)))(parsed_ops), lambda x, y, z, w, v: (w[0], v, 'Sig:%s\n%s' % (x or '□', y))), ÄÕåØ))
(ops := parse_operator_file(ÐØó(OP_FILE)))
__ÞÄÊÞADD_EXPORTS__(globals(), ('ops', ops), ('generate_fontcompose_conf', generate_fontcompose_conf), ('get_operator_table', get_operator_table))

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/Libraries/Compiler/op_table.☾'
__ÞÄÊÞIMPORT__('text_format', globals())
__ÞÄÊÞIMPORT__('generate_operators', globals())
(áÖááÖæ := [*get_operator_table(ops), [ÂÛê('.\u2009ᴺ')]])
(add_before := (lambda p, n: getattr(áÖááÖæ, 'insert')(MOD(ÄÔÞÔ, ÁÜñ=ÄÕøü)(áÖááÖæ, lambda ÂîÓ: ÂÔö(MOD(ÁÛÛ, áØÁ=(slice(None, None), 0))(ÂîÓ), p)), n)))
MOD(ÄÕéý, áØÁ=add_before)('!', [ÂÛê('␀CAT\u2009ᴺᴮ')])
MOD(ÄÕéý, áØÁ=add_before)('ᴍ', [ÂÛê('␀TAC\u2009ᴮ')])
MOD(ÄÕéý, áØÁ=add_before)('⨳', [ÂÛê('␀A3\u2009ᴮ\U000f004c')])
MOD(ÄÕéý, áØÁ=add_before)('␀A3', ÁØò(lambda ÂîÓ: [ÂîÓ, 'ᴮ'])('≔\U000f7e09\U000f7e0a\U000f7e0b≕\U000f7e0e\U000f7e0c\U000f7e0d'))
MOD(ÄÕéý, áØÁ=add_before)('≔', [ÂÛê('␀A2\u2009ᴮ\U000f004c')])
MOD(ÄÕéý, áØÁ=add_before)('␀A2', [ÂÛê('⭜\u2009ᴮ\U000f004c')])
MOD(ÄÕéý, áØÁ=add_before)('⭜', [ÂÛê('⭝\u2009ᴺᴮ\U000f004c')])
MOD(ÄÕéý, áØÁ=add_before)('⭝', [ÂÛê('␀A1\u2009ᴮ\U000f004c')])
(áÖåáÖæ := Áÿú(ÄÝöÞ(ÂÁÍ(ÂÕÅ)('    \u2009␀T  \u2009ᴺ \U000f0012 \u2009    \n␀TAC\u2009␀T⟞ \u2009ᴺ \U000f0012 \u2009    \n    \u2009␀T⟝ \u2009ᴺᴾ  \u2009␀TAC\n␀TAC\u2009␀T⟞⟝\u2009ᴺᴾ\U000f0012ᴮ\u2009␀TAC\n    \u2009   ⬅\u2009 ᴾ  \u2009␀A1 \n␀A1 \u2009   ➡\u2009  \U000f0012 \u2009    \n    \u2009   ←\u2009 ᴾ  \u2009␀A2 \n␀A2 \u2009   ⥉\u2009   ᴮ\u2009␀A2 \n␀A2 \u2009   →\u2009  \U000f0012 \u2009    \n    \u2009   ⭠\u2009 ᴾ  \u2009␀A3 \n␀A3 \u2009   ⭢\u2009  \U000f0012 \u2009    ', ÄÔéÄ([' '], ÁØã)), '\n'), ÂÛê))
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
            return (ÄÊÞPSH(áÑÞ), ÄÊÞPSH('M'), ÄÊÞPSH(getattr(ÄÊÞPKE(1), ÄÊÞPKE(0))), ÄÊÞPSH(MOD(ÄÕéý, áØÁ=ÂÕØ if y else ÂÕÃ)(ÄÊÞPKE(0), x)), setattr(ÄÊÞPKE(3), ÄÊÞPKE(2), ÄÊÞPKE(0)), ÄÊÞDEL(4))[4]
        return getattr(super(), '__setitem__')(x, y)
    (__setattr__ := __setitem__)
    (__getattr__ := __getitem__)

def cb(áÎõ):
    for ÂÑÕ in áÎõ ** ì:
        (ÄÊÞPSH(ÂÑÕ), ÄÊÞPSH('R'), ÄÊÞPSH(getattr(ÄÊÞPKE(1), ÄÊÞPKE(0))), ÄÊÞPSH(ÂÕØ(ÄÊÞPKE(0), '≔\U000f7e09\U000f7e0a\U000f7e0b')), setattr(ÄÊÞPKE(3), ÄÊÞPKE(2), ÄÊÞPKE(0)), ÄÊÞDEL(4))[4]
    for k in '≔\U000f7e09\U000f7e0a\U000f7e0b':
        (ÄÊÞPSH(áÎõ[k]), ÄÊÞPSH('L'), ÄÊÞPSH(ÂÔð()), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    for k in '≕\U000f7e0e\U000f7e0c\U000f7e0d':
        (ÄÊÞPSH(áÎõ[k]), ÄÊÞPSH('R'), ÄÊÞPSH(ÂÔð()), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    (ÄÊÞPSH(áÎõ['⬅']), ÄÊÞPSH('R'), ÄÊÞPSH(getattr(ÄÊÞPKE(1), ÄÊÞPKE(0))), ÄÊÞPSH(ÂÕØ(ÄÊÞPKE(0), '→⭢')), setattr(ÄÊÞPKE(3), ÄÊÞPKE(2), ÄÊÞPKE(0)), ÄÊÞDEL(4))[4]
    (ÄÊÞPSH(áÎõ['←']), ÄÊÞPSH('R'), ÄÊÞPSH(getattr(ÄÊÞPKE(1), ÄÊÞPKE(0))), ÄÊÞPSH(ÂÕØ(ÄÊÞPKE(0), '⭢')), setattr(ÄÊÞPKE(3), ÄÊÞPKE(2), ÄÊÞPKE(0)), ÄÊÞDEL(4))[4]
    return áÎõ

def make_op_table(áÖááÖæ, áÖåáÖæ, cb):
    (áÎõ := ÐÌü(ÂÑÖ()))
    for áÖÞ in ÂÀÇ(áÖááÖæ):
        (ÄÊÞPSH(áÖÞ), ÄÊÞPSH(ÁØò(lambda ÂîÓ: (ÂîÓ[0], ÄÝöË(Âøî(ÂîÓ[slice(1, None)]))))(ÄÊÞPKE(0))), (áÖÞ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
        (ÄÊÞPSH((áÍè(MOD(ÁÛÛ, áØÁ=(slice(None, None), 0))(áÖÞ)), ÐÌü(ÂÑÖ()))), ((áØÂ := ÄÊÞPKE(0)[0]), (áÖá := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
        for t, m in áÖÞ:
            (food := ÂÕØ(áÍè(áÎõ ** î), ÐÌü(getattr(áØÂ, 'copy')) if 'α' in m else ÂÔð()))
            (ÄÊÞPSH(áÖá), ÄÊÞPSH(t), ÄÊÞPSH(OP(t=t, M=m, L=ÐÌü(getattr(food, 'copy')) if áÍè(ÂÕÖ(m, 'BS')) else ÂÔð(), R=ÐÌü(getattr(food, 'copy')) if áÍè(ÂÕÖ(m, 'BP')) else ÂÔð())), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
        (ÄÊÞPSH(áÎõ), ÄÊÞPSH(ÄÊÞPKE(0) | áÖá), (áÎõ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
    (áÏì := ÐÌü(ÂÑÖ()))
    for L, t, m, R in áÖåáÖæ:
        (ÄÊÞPSH(m), ÄÊÞPSH(ÄÝöË(ÄÊÞPKE(0))), (m := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
        (Lc := (ÂÕØ(getattr(áÎõ[L], 'L'), getattr(áÎõ[L], 'R')) if L else ÂÔð()))
        (Rc := (ÂÕØ(getattr(áÎõ[R], 'L'), getattr(áÎõ[R], 'R')) if R else ÂÔð()))
        for áÏÖ, ÂÑÕ in áÎõ:
            if áÏÖ not in Lc and ÂÕÖ('PB', getattr(ÂÑÕ, 'M')):
                getattr(getattr(ÂÑÕ, 'R'), 'add')(t)
            if áÏÖ not in Rc and ÂÕÖ('SB', getattr(ÂÑÕ, 'M')):
                getattr(getattr(ÂÑÕ, 'L'), 'add')(t)
        (ÄÊÞPSH(áÏì), ÄÊÞPSH(t), ÄÊÞPSH(OP(t=t, M=m, L=ÂÕØ(ÂÕÃ(áÍè(áÎõ ** î), getattr(áÎõ[L], 'L')), áÍè([L])) if L else ÂÔð(), R=ÂÕØ(getattr(áÎõ[R], 'R'), áÍè(ÁØò(lambda ÂîÓ: ÂîÓ[1])(áÖåáÖæ)) if 'α' in m else ÂÔð()) if R else ÂÔð())), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    (ÄÊÞPSH(áÎõ), ÄÊÞPSH(ÄÊÞPKE(0) | áÏì), (áÎõ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
    return cb(áÎõ)
(OP_TABLE := (áÎõ := make_op_table(áÖááÖæ, áÖåáÖæ, cb)))
(IS_OP := (lambda ÄÕÒü: getattr(getattr(ÄÕÒü, 'e'), 'O') if getattr(ÄÕÒü, 't') == '𝗈𝗉' and '´' not in getattr(ÄÕÒü, 'e') else None))
(MODIFIERS := ÂÛê('⟥≺\u2009⦣\u205f≻ᵜ꜠´⟤\u2009ᔨ⦢𐞑'))
(áÕÒ := ÂÑÖ()(OP_LIT=áÎõ ** î, OP_MOD_L_N=MODIFIERS[0][0], OP_MOD_L_Y=MODIFIERS[0][1], OP_MOD_R_N=MODIFIERS[1][0], OP_MOD_R_Y=MODIFIERS[1][1], VAR_SPEC='ⴳⴴ✓✗□ᐦ\U000f0b88\U000f18e9⬤îĵ\U000f7e88ℇτπ\U000f7e8d\U000f7e8f∞\U000f7c6a\U000f7c7d\U000f7c7e\U000f7c6b\U000f7c6c\U000f7c6d\U000f7c6e\U000f7c6f\U000f7c70\U000f7c69' + Âøî(ÐÌü(getattr(FRAC_CONV, 'values'))), BLK_KWDS='\ue00a', STD_KWDS='↪⮂↺⇥\U000f01b4', BLK_CLN_KWDS='\U000f1018¿⸘¡', SUP=ÄÝõá(ë), SUB=ÄÝõà(ë)))

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/Libraries/Compiler/node_types.☾'
from functools import cache
__ÞÄÊÞIMPORT__('peggle2/gram_tools', globals())
__ÞÄÊÞIMPORT__('text_format', globals())
(fix := ÄÔéÄ('﹕', 'ː'))

def Âçß(*áÑË, s='\n', sep=' ', ÂìÆ=False, **áÑÕ):
    getattr((Æå := (stderr if ÂìÆ else stdout)), 'write')(fix(Âøî(áÑË, ÁÜÙ(sep)) + ÁÜÙ(s)))
    ÐÌü(getattr(Æå, 'flush'))
    if áÑË:
        return áÑË[0]
(áÍñ := (lambda *áÑË: BOX(stackr(*áÑË))))
(áÍñáÎÚ := Âåæ(box, lambda ÂîÓ: ÂÕÅ(getattr(ÂîÓ, 'P'), False)))
(áÍñáÍñ := (lambda ÄÕÒü, *áÑË: ÂåÔ(Âçß(BOX(ÂÁÍ(ì)((d := ÂÕÅ(getattr(ÄÕÒü, 'P'), False)), Âøî(ÁØò(lambda ÂîÓ: padc(ÂîÌ([ÂîÓ], ' '), d, '─') + '\n')(áÑË))))), ÄÕÒü)))
(ÄÊÞPSH((áÐè(ÁØã), áÐè(' '))), ((áÚì := ÄÊÞPKE(0)[0]), (áÖÊ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((lambda x: áÎô('𝑣', áÐè(x)), lambda x: áÎô('𝑣_spec', áÐè(x)))), ((áÓé := ÄÊÞPKE(0)[0]), (áÓéáÓæ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((lambda *áÑË: áÎô('x', *áÑË), lambda *áÑË: áÎô('X', *áÑË))), ((áÓë := ÄÊÞPKE(0)[0]), (áÓÐ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((lambda *áÑË: áÎô('\U000f7e58', *áÑË), lambda *áÑË: áÎô('⍖', *áÑË), lambda *áÑË: áÎô('\U000f7e57', *áÑË))), ((áÓã := ÄÊÞPKE(0)[0]), (áÓà := ÄÊÞPKE(0)[1]), (áÓÖ := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]
(áÒÿ := (lambda: áÓÕáÓÓáÓßáÓß('globals')))
(áÓå := (lambda x: áÓÕáÓÓáÓßáÓß('þDEL', áÓá(x))))
(áÓá := (lambda x: áÎô('num', áÐè(x))))
(áÓäáÓé := (lambda x: áÎô('qvar', áÐè(x))))
(ÄÊÞPSH(ÁØò(lambda ÂîÓ: lambda *áÑË: áÓÜ(áÓÌ(*áÑË), áÓá(ÂîÓ)))(ÂÿÇ(2))), ((áÓÄ := ÄÊÞPKE(0)[0]), (áÓÊ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(ÄÊÞPSH((lambda *áÑË: áÎô('𝑖', *áÑË), lambda *áÑË: áÎô('𝑎', *áÑË), lambda *áÑË: áÎô('𝑇', *áÑË))), ((áÓÜ := ÄÊÞPKE(0)[0]), (áÓÓ := ÄÊÞPKE(0)[1]), (áÓÌ := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]
(áÓçáÓàáÓã := (lambda *áÑË: áÎô('tmp', *áÑË)))
(áÓâáÓãáÒú := (lambda x, *áÑË: áÎô('opC', MOD(Áëý, áØÁ=ÄÊÞCUR((1,), {}, ÁØö, ÂýÃ, ÁÜÙ))(x, áÓÇáÓÈ), *áÑË)))
(áÓæáÓçáÓå := (lambda *áÑË: áÎô('str', *áÑË)))
(áÓØáÓëáÓã := (lambda *áÑË: áÎô('exp', *áÑË)))
(áÓÜáÓçáÓØáÓà := (lambda *áÑË: áÎô('item', *áÑË)))
(áÓçáÓØáÓåáÓá := (lambda *áÑË: áÎô('tern', *áÑË)))
(áÓÓáÓçáÓçáÓå := (lambda *áÑË: áÎô('attr', *áÑË)))
(áÓàáÓÕáÓÓáÓß := (lambda *áÑË: áÎô('mcal', *áÑË)))
(áÓÕáÓÓáÓßáÓß := (lambda *áÑË: áÎô('∘', *ÁØò(lambda ÂîÓ: MOD(Áëý, áØÁ=lambda ÂîÓ: ÁØö(ÂîÓ, ÁÜÙ))(ÂîÓ, áÓé))(áÑË))))
(áÓßáÓÓáÓàáÓÔ := (lambda *áÑË: áÎô('lamb', *áÑË)))
(áÓæáÓçáÓåáÓÔ := (lambda *áÑË: áÎô('strb', *áÑË)))
(áÓÙáÓâáÓå := (lambda *áÑË: áÎô('∀', *áÑË)))
(áÓæáÓßáÓÜáÓÕáÓØ := (lambda *áÑË: áÓÕáÓÓáÓßáÓß('slice', *(lambda ÂîÓ: ÁØò(lambda ÂîÓ: áÓéáÓæ('□') if ÂîÓ is None else áÓá(ÂîÓ))((getattr(ÂîÓ, 'start'), getattr(ÂîÓ, 'stop'), getattr(ÂîÓ, 'step'))))(áÑË[0])) if áÑË and ÁØö(áÑË[0], slice) else áÎô('slice', *Âøî(áÑË, lambda *áÑË: MOD(ÄÕéý, áØÁ=ÂØØ)(áÐè(':'), áÑË)))))
(ÆåÞ_dec_ÞáÑË := (lambda x, *áÑË: áÎô('𝔸', áÐè(x))))
(ÆåÞ_dec_ÞáÑÕ := (lambda x, **áÑÕ: áÎô('𝕂', áÐè(x))))
(áÓÙáÓãáÓÓáÓåáÓÓáÓàáÓæ := (lambda *áÑË: áÎô('ƒ_dec_params', *áÑË)))
(áÓÚáÓåáÓã := (lambda x, *áÑË: áÎô('grp', MOD(ÄÕéý, áØÁ=Âîë)(áÐè(x[0]), áÑË), áÓë(*áÑË), MOD(ÄÕéý, áØÁ=Âîì)(áÐè(x[1]), áÑË))))
(áÓâáÓã := (lambda x: áÎô('op', MOD(ÄÕéý, áØÁ=Âîë)(ÅÒ('op_⸓_l'), x), áÎô('op_lit', áÐè(x)), MOD(ÄÕéý, áØÁ=Âîì)(ÅÒ('op_⸓_r'), x))))
(áÓÇáÓÈ := (lambda x: áÎô('𝗈𝗉', MOD(ÄÕéý, áØÁ=Âîë)(ÅÒ('op_⸓_l'), x), MOD(ÄÕéý, áØÁ=ÂØÙ)(áÎô('op_lit', áÐè(x)), x), MOD(ÄÕéý, áØÁ=Âîì)(ÅÒ('op_⸓_r'), x), e=MOD(ÂÑÖ, áØÁ=None)()(O=OP_TABLE[MOD(Áëý, áØÁ=ÄÊÞCUR((1,), {}, ÄÝøÇ, ÂýÃ, ÁÜÙ))(x, ì)]))))

def áÓÓáÓèáÓçáÓâ(x):
    if ÁØö(x, ÂÑÅ):
        return áÓá(x)
    if ÁØö(x, ÁÜÙ):
        return áÓæáÓçáÓå(áÐè(x))
    if ÁØö(x, áÍé):
        return áÓÌ(Áÿú(x, áÓÓáÓèáÓçáÓâ))
    if ÁØö(x, áÍá):
        return áÎô('𝐿', Áÿú(x, áÓÓáÓèáÓçáÓâ))
    if ÁØö(x, slice):
        return áÓæáÓßáÓÜáÓÕáÓØ(x)
    return x
(áÓÆáÓÍáÓÄáÓÄ := áÓé('NULL'))
(áÓÒ := áÎô('PLACEHOLDER'))

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/Libraries/Compiler/tree.☾'
__ÞÄÊÞIMPORT__('node_types', globals())

def ÄÕÒüÞ_is_hot_stuff(ÄÕÒü, Æå, *áÑË):
    if ÁØö(Æå, ÁÜÙ):
        if Æå != getattr(ÄÕÒü, 't'):
            return
    elif ÁØö(Æå, áÓó):
        if not Æå(ÄÕÒü):
            return
    elif getattr(ÄÕÒü, 't') not in Æå:
        return
    return ÂØõ(ÁØò(lambda ÂîÓ: ÄÕÒüÞ_is_hot_stuff(ÂîÓ, *áÑË))(ÄÕÒü)) if áÑË else True
(date_ÞÄÕÒü := (lambda *áÏÞ: lambda ÄÕÒü: getattr(ÄÕÒü, 'find')(lambda x: ÄÕÒüÞ_is_hot_stuff(x, *áÏÞ))))

def ÄÕÒüáÒÿ(ÄÕÒü, x, y):
    if getattr(ÄÕÒü, 't') != y[0]:
        return
    for i, t in ÄÕåØ(x, y[slice(1, None)]):
        if ãÊú(ÄÕÒü) <= i or getattr((ÄÕÒü := ÄÕÒü[i]), 't') != t:
            return
    return True

def try_pop_pos(ÄÕÒü, proxy=None, rec=False):
    (Æå := (lambda ÂîÓ: ÂÔö(getattr(ÂîÓ, 'e'), 'p')))
    (ÄÊÞPSH(getattr(ÄÕÒü if proxy is None else proxy, 'first_sides')(Æå)), ((l := ÄÊÞPKE(0)[0]), (r := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    if l is None:
        return ÄÕÒü
    (ÄÊÞPSH(getattr(ÄÕÒü, 'e')), ÄÊÞPSH('p'), ÄÊÞPSH((*getattr(getattr(l, 'e'), 'p')[slice(None, 2)], *getattr(getattr(r, 'e'), 'p')[slice(2, None)])), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    if not rec:
        return
    for áÎÚ in ÄÕÒü:
        try_pop_pos(áÎÚ)
    return ÄÕÒü

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/Libraries/Compiler/tree_txt.☾'
__ÞÄÊÞIMPORT__('tree', globals())

def rewrite_str_indent(ÄÕÒü):
    if 'p' not in getattr(ÄÕÒü, 'e'):
        return ÄÕÒü
    (ÄÊÞPSH((getattr(getattr(ÄÕÒü, 'e'), 'p')[0], getattr(getattr(ÄÕÒü, 'e'), 'p')[1] + 1)), ((pl := ÄÊÞPKE(0)[0]), (áÖð := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    for áÎÚ in getattr(ÄÕÒü, 'gets')('str_tsub_guts'):
        (ÄÊÞPSH((lines(getattr(áÎÚ[0], 't')), [])), ((áØÁ := ÄÊÞPKE(0)[0]), (h := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
        for i, ÂîÓ in ÂÓÏ(áØÁ):
            (I := (getattr(getattr(áÎÚ, 'e'), 'p')[0] + i))
            getattr(h, 'append')(ÂîÓ if pl == I else ÂîÓ[slice(ÂóÌ(MOD(Áëý, áØÁ=ÄÊÞCUR((1,), {}, ÂÕó, ÂýÃ, None))(MOD(ÄÔÞÔ, ÁÜñ=ÄÕøü)(ÂîÓ, lambda ÂîÓ: ÂîÓ not in ' \t'), MOD(ÄÕÍÔ, áØÁ=ãÊú(ÂîÓ))), áÖð), None)])
            (pl := I)
        (ÄÊÞPSH(áÎÚ[0]), ÄÊÞPSH('t'), ÄÊÞPSH(Âøî(h, '\n')), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    return ÄÕÒü

def add_blocks(ÄÕÒü):
    (start := (lambda ÄÕÒü: getattr(ÄÕÒü, 't') == 'stmt' and getattr(ÄÕÒü[0], 't') == 'blk_head'))
    (Æå := Âåæ(UGX_CREATE(('B', (àìÒ := []), '*', None, ('∨', ('B', (àìÒ := []), '', lambda C: áÎô('blk', C[0], *Áëý(C[slice(1, None)], Æå)), ('∧', (start, ''), (lambda ÂîÓ: ÄÝöç(getattr(getattr(ÂîÓ, 'e'), 'p')), ''), (lambda ÂîÓ: getattr(getattr(ÂîÓ, 'e'), 'p')[1] >= ÂÛÒ()[1], '*'))), (ÃÆë, '')))), áÍá))
    getattr(ÄÕÒü, 'ftrp')('stmts', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(c=Æå(ÄÕÒü)), True)
(flatten_statments := (lambda ÄÕÒü: getattr(ÄÕÒü, 'flat')(lambda ÂîÓ: getattr(ÂîÓ, 't') in ÂÛê('stmt'))))

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/Libraries/Compiler/expr.☾'
__ÞÄÊÞIMPORT__('tree_txt', globals())

def denode_op(ÄÕÒü):
    (ÄÊÞPSH(ÄÕÒü), ((l := ÄÊÞPKE(0)[0]), (o := ÄÊÞPKE(0)[1]), (r := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]
    (áÖü := OP_TABLE[getattr(o[0], 't')])
    (ÄÊÞPSH(ÁØò(lambda ÂîÓ: ÁØò(lambda ÂîÓ: ÂîÓ if getattr(ÂîÓ, 't') == '𝚜' else áÎô(getattr(ÂîÓ[0], 't'), *ÂîÓ[slice(1, None)]))(ÂîÓ))([l, r])), ((áÖù := ÄÊÞPKE(0)[0]), (áØÀ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    (ÄÊÞPSH(Áÿú(ÁØò(lambda ÂîÓ: ÁØò(lambda ÂîÓ: ÄÔýò if getattr(ÂîÓ, 't') == '𝚜' else getattr(ÂîÓ[0], 't'))(ÂîÓ))([l, r]), áÍè)), ((L := ÄÊÞPKE(0)[0]), (R := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    (áÖü := ÐÌü(getattr(áÖü, 'copy')))
    for t in L:
        if t == '⟥':
            (ÄÊÞPSH(áÖü), ÄÊÞPSH('L'), ÄÊÞPSH(áÖü), ÄÊÞPSH('P'), ÄÊÞPSH(áÖü), ÄÊÞPSH('S'), ÄÊÞPSH(áÖü), ÄÊÞPSH('B'), ÄÊÞPSH((ÂÚü(), False, True, False)), (setattr(ÄÊÞPKE(8), ÄÊÞPKE(7), ÄÊÞPKE(0)[0]), setattr(ÄÊÞPKE(6), ÄÊÞPKE(5), ÄÊÞPKE(0)[1]), setattr(ÄÊÞPKE(4), ÄÊÞPKE(3), ÄÊÞPKE(0)[2]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)[3])), ÄÊÞDEL(9))[9]
        elif t == '≺':
            (ÄÊÞPSH(áÖü), ÄÊÞPSH('L'), ÄÊÞPSH(áÖü), ÄÊÞPSH('R'), ÄÊÞPSH(áÖü), ÄÊÞPSH('P'), ÄÊÞPSH(áÖü), ÄÊÞPSH('S'), ÄÊÞPSH(áÖü), ÄÊÞPSH('B'), ÄÊÞPSH((getattr(áÎõ['ᴍ'], 'L'), ÂÚü(), False, True, False)), (setattr(ÄÊÞPKE(10), ÄÊÞPKE(9), ÄÊÞPKE(0)[0]), setattr(ÄÊÞPKE(8), ÄÊÞPKE(7), ÄÊÞPKE(0)[1]), setattr(ÄÊÞPKE(6), ÄÊÞPKE(5), ÄÊÞPKE(0)[2]), setattr(ÄÊÞPKE(4), ÄÊÞPKE(3), ÄÊÞPKE(0)[3]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)[4])), ÄÊÞDEL(11))[11]
    for t in R:
        if t == '⟤':
            (ÄÊÞPSH(áÖü), ÄÊÞPSH('R'), ÄÊÞPSH(áÖü), ÄÊÞPSH('P'), ÄÊÞPSH(áÖü), ÄÊÞPSH('S'), ÄÊÞPSH(áÖü), ÄÊÞPSH('B'), ÄÊÞPSH((ÂÚü(), True, False, False)), (setattr(ÄÊÞPKE(8), ÄÊÞPKE(7), ÄÊÞPKE(0)[0]), setattr(ÄÊÞPKE(6), ÄÊÞPKE(5), ÄÊÞPKE(0)[1]), setattr(ÄÊÞPKE(4), ÄÊÞPKE(3), ÄÊÞPKE(0)[2]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)[3])), ÄÊÞDEL(9))[9]
        elif t == '≻':
            (ÄÊÞPSH(áÖü), ÄÊÞPSH('L'), ÄÊÞPSH(áÖü), ÄÊÞPSH('R'), ÄÊÞPSH(áÖü), ÄÊÞPSH('P'), ÄÊÞPSH(áÖü), ÄÊÞPSH('S'), ÄÊÞPSH(áÖü), ÄÊÞPSH('B'), ÄÊÞPSH((ÂÚü(), getattr(áÎõ['ᴍ'], 'R'), True, False, False)), (setattr(ÄÊÞPKE(10), ÄÊÞPKE(9), ÄÊÞPKE(0)[0]), setattr(ÄÊÞPKE(8), ÄÊÞPKE(7), ÄÊÞPKE(0)[1]), setattr(ÄÊÞPKE(6), ÄÊÞPKE(5), ÄÊÞPKE(0)[2]), setattr(ÄÊÞPKE(4), ÄÊÞPKE(3), ÄÊÞPKE(0)[3]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)[4])), ÄÊÞDEL(11))[11]
        elif t == 'ᵜ':
            (ÄÊÞPSH(áÖü), ÄÊÞPSH('L'), ÄÊÞPSH(áÖü), ÄÊÞPSH('R'), ÄÊÞPSH((getattr(áÖü, 'R'), getattr(áÖü, 'L'))), (setattr(ÄÊÞPKE(4), ÄÊÞPKE(3), ÄÊÞPKE(0)[0]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)[1])), ÄÊÞDEL(5))[5]
        elif t == '꜠':
            if getattr(áÖü, 'B'):
                (ÄÊÞPSH(áÖü), ÄÊÞPSH('B'), ÄÊÞPSH(False), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
                if (ÄÊÞDEL(1), False)[1] if ÄÊÞPSH(getattr(áÖü, 'P')) else ÄÊÞPOP() if getattr(áÖü, 'S') else (ÄÊÞDEL(1), True)[1]:
                    (ÄÊÞPSH(áÖü), ÄÊÞPSH('P'), ÄÊÞPSH((ÄÊÞPSH(áÖü), ÄÊÞPSH('S'), ÄÊÞPSH(True), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
            elif getattr(áÖü, 'P') or getattr(áÖü, 'S'):
                (ÄÊÞPSH(áÖü), ÄÊÞPSH('L'), ÄÊÞPSH((ÄÊÞPSH(áÖü), ÄÊÞPSH('R'), ÄÊÞPSH(ÂÕØ(getattr(áÖü, 'L'), getattr(áÖü, 'R'))), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
                (ÄÊÞPSH(áÖü), ÄÊÞPSH('P'), ÄÊÞPSH((ÄÊÞPSH(áÖü), ÄÊÞPSH('S'), ÄÊÞPSH(True), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
            else:
                ÂùÆ(False)
    (áÖÉ := ÅÒ('𝗈𝗉', MOD(Áëý, áØÁ=not áÖù)(áÎô('op_⸓_l', *áÖù), lambda ÂîÓ: MOD(ÄÕéý, áØÁ=Âîë)(ÂîÓ, ÄÕÒü[1][0])), áÎô('op_lit', ÄÕÒü[1][0]), MOD(Áëý, áØÁ=not áØÀ)(áÎô('op_⸓_r', *áØÀ), lambda ÂîÓ: MOD(ÄÕéý, áØÁ=Âîì)(ÂîÓ, ÄÕÒü[1][0])), e=MOD(ÂÑÖ, áØÁ=None)()(**getattr(ÄÕÒü, 'e'), O=áÖü)))
    if '´' in R:
        (ÄÊÞPSH(getattr(áÖÉ, 'e')), ÄÊÞPSH('´'), ÄÊÞPSH('´'), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    return áÖÉ

def part(áÖü, áÖÔ, d):
    (ÄÊÞPSH((getattr(getattr(áÖü, 'e'), 'O'), 0)), ((áÏì := ÄÊÞPKE(0)[0]), (i := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    if d == -1:
        for i, n in ÂÓÏ(áÖÔ)[slice(None, None, -1)]:
            if not (ÂÑÕ := IS_OP(n)):
                continue
            if ÂÔø(getattr(áÏì, 'L'), getattr(ÂÑÕ, 't')):
                break
    elif d == 1:
        (áØÁáØÂáÖø := Âêà(getattr(áÏì, 'R')))
        for i, n in ÂÓÏ(áÖÔ):
            if not (ÂÑÕ := IS_OP(n)):
                continue
            while áØÁáØÂáÖø:
                if getattr(ÂÑÕ, 't') in áØÁáØÂáÖø[-1] or ((((getattr(áÏì, 'P') or (getattr(áÏì, 'B') and (not getattr(áÏì, 'S')))) and getattr(ÂÑÕ, 't') in getattr(áÎõ['⨳'], 'R')) and getattr(ÂÑÕ, 'P')) and (not i)):
                    getattr(áØÁáØÂáÖø, 'append')(getattr(ÂÑÕ, 'R'))
                    break
                getattr(áØÁáØÂáÖø, 'pop')()
            else:
                break
        else:
            (ÄÊÞPSH(i), ÄÊÞPSH(ÄÊÞPKE(0) + 1), (i := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
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
        (ÄÊÞPSH((áÖù is not áÓÆáÓÍáÓÄáÓÄ, áØÀ is not áÓÆáÓÍáÓÄáÓÄ)), ((Ïß := ÄÊÞPKE(0)[0]), (Ïà := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
        (U := ([áÖù, áØÀ] if Ïß and Ïà else [áÖù] if Ïß else [áØÀ] if Ïà else ÂÚü()))
    else:
        (U := (áÖù, áØÀ))
    return MOD(ÄÕéý, áØÁ=ÂØÙ)(áÓâáÓãáÒú(áÖü, *U), (áÖù, áØÀ))

def apply_op(áÖü, áÖÞ, áÖä):
    (ÄÊÞPSH(part(áÖü, áÖÞ, -1)), ((ll := ÄÊÞPKE(0)[0]), (lr := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    (ÄÊÞPSH(part(áÖü, áÖä, 1)), ((rl := ÄÊÞPKE(0)[0]), (rr := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    if rl:
        (rl := parse_expr(rl))
    (ÄÊÞPSH((getattr(getattr(áÖü, 'e'), 'O'), ÂÚü())), ((áÕÉ := ÄÊÞPKE(0)[0]), (áÑæ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    if '𝚜' in áÕÉ:
        getattr(áÑæ, 'append')(getattr(áÕÉ, 'pop')('𝚜'))

    def suffix(áÖä):
        if áÖä and (not (áÎÛ := IS_OP(áÖä[0])) or (getattr(áÎÛ, 'P') and ((ÄÊÞDEL(1), False)[1] if ÄÊÞPSH(getattr(áÎÛ, 'B')) else ÄÊÞPOP() if getattr(áÎÛ, 'S') else (ÄÊÞDEL(1), True)[1]))):
            getattr(áÖä, 'insert')(0, denode_op(áÓâáÓã(MOD(ÄÕéý, áØÁ=Âîì)('␀CAT', áÖä))))
        return áÖä
    (suf2 := (lambda áÖä: Âêà(getattr(áÖä, 'pop')(0)) if áÖä and getattr(áÖä[0], 't') == 'target_rhs' else ÂÚü()))
    if (getattr(áÕÉ, 'B') and lr) and rl:
        return (ll + [create_call(áÖü, áÓë(*lr), áÓë(*rl)), *áÑæ], rr)
    elif getattr(áÕÉ, 'S') and lr:
        return (ll + [create_call(áÖü, áÓë(*lr), áÓÆáÓÍáÓÄáÓÄ), *áÑæ, *suf2(áÖä)], suffix(áÖä))
    elif getattr(áÕÉ, 'P') and rl:
        return (áÖÞ + [create_call(áÖü, áÓÆáÓÍáÓÄáÓÄ, áÓë(*rl)), *áÑæ], rr)
    elif getattr(áÕÉ, 'N') and (getattr(áÕÉ, 'Ïë') or ((ÄÊÞDEL(1), False)[1] if ÄÊÞPSH(lr) else ÄÊÞPOP() if rl else (ÄÊÞDEL(1), True)[1])):
        return (áÖÞ + [create_call(áÖü, áÓÆáÓÍáÓÄáÓÄ, áÓÆáÓÍáÓÄáÓÄ) if getattr(áÕÉ, 'Ïë') else áÖü, *áÑæ, *suf2(áÖä)], áÖä)
    if getattr(áÕÉ, 'B'):
        if lr:
            return (ll + [create_call(áÖü, áÓë(*lr), áÓë(áÓéáÓæ('⬤'))), *áÑæ], áÖä)
        if rl:
            return (áÖÞ + [create_call(áÖü, áÓë(áÓéáÓæ('⬤')), áÓë(*rl)), *áÑæ], rr)
    áÍñáÍñ(áÖü)
    ÂùÆ(False, 'Unable to apply operator %s: ll=%s; lr=%s; rl=%s; rr=%s' % (áÖü, ll, lr, rl, rr))

def parse_expr(ÄÕÒü):
    (ÄÊÞPSH(([], [*ÄÕÒü])), ((áÖÞ := ÄÊÞPKE(0)[0]), (áÖä := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    while áÖä:
        (c := getattr(áÖä, 'pop')(0))
        if IS_OP(c):
            (ÄÊÞPSH(apply_op(c, áÖÞ, áÖä)), ((áÖÞ := ÄÊÞPKE(0)[0]), (áÖä := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
        else:
            getattr(áÖÞ, 'append')(c)
    return áÓë(*áÖÞ + áÖä)

def curry_ops(ÄÕÒü):

    @getattr(ÄÕÒü, 'ftrp')('∘', None, True)
    def _(ÄÕÒü):
        (Æå := (lambda ÂîÓ: getattr(ÂîÓ, 't') == '𝑣_spec' and getattr(ÂîÓ[0], 't') == '⬤'))
        (ÓÎ := (lambda ÂîÓ: getattr(ÂîÓ, 't') == 'kw_𝕒'))
        (Ëðá := (lambda ÂîÓ: ÓÎ(ÂîÓ) and Æå(ÂîÓ[1])))
        (C := ÁØò(lambda ÂîÓ: [ÂîÓ, 1] if Æå(ÂîÓ) else [áÓäáÓé(+ÂîÓ[0]), -1] if Ëðá(ÂîÓ) else [áÓÜáÓçáÓØáÓà(áÓäáÓé(+ÂîÓ[0]), ÂîÓ[1]), 0] if ÓÎ(ÂîÓ) else [ÂîÓ, 0])(getattr(ÄÕÒü, 'c')))
        if getattr(ÄÕÒü[0], 't') == '𝗈𝗉':
            (ÄÊÞPSH(C), ÄÊÞPSH(slice(2, 2)), ÄÊÞPSH(ÁØò(lambda ÂîÓ: [áÓäáÓé(getattr(ÂîÓ, 't')), -1] if ãÊú(ÂîÓ) == 1 and Æå(ÂîÓ[0]) else [áÓÜáÓçáÓØáÓà(áÓäáÓé(getattr(ÂîÓ, 't')), ÂîÓ[0]), 0])(ÄÔÔç(ÄÕÒü[0][2], ãÊú))), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
        if not ÂØõ(ÁØò(lambda ÂîÓ: ÂîÓ[1])(C)):
            return ÄÕÒü
        (ÄÊÞPSH(MOD(ÂÚü, áØÁ=3)()), ((áÑõ := ÄÊÞPKE(0)[0]), (áÑð := ÄÊÞPKE(0)[1]), (áÑæ := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]
        for c, k in C:
            if getattr(c, 't') == 'item':
                getattr(áÑð, 'append')(c)
            elif k == 0:
                getattr(áÑæ, 'append')(c)
            elif k == 1:
                (getattr(áÑõ, 'append')(áÓá(ãÊú(áÑæ))), getattr(áÑæ, 'append')(áÓéáÓæ('⬤')))
            elif getattr(c, 't') == 'qvar':
                getattr(áÑõ, 'append')(c)
        if getattr(ÄÕÒü[0], 't') == '𝗈𝗉':
            getattr(ÄÕÒü[0][2], 'set')(c=ÂÚü())
        return áÓÕáÓÓáÓßáÓß('þCUR', áÓÌ(*áÑõ), áÎô('𝐷', *áÑð), *áÑæ)

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/Libraries/Compiler/lambdas.☾'
def ÏéÞ_add_vk(ÄÕÒü, áÑæ='𝔸', áÑð='𝕂'):
    if 'VK' in getattr(ÄÕÒü, 'e'):
        return ÄÕÒü
    (ÄÊÞPSH((ÄÕÒü[0], MOD(ÄÝöË, áØÁ=2)(+ÄÕÒü[1]))), ((áÖâ := ÄÊÞPKE(0)[0]), (ÄÔÕý := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    (cur := {*ÁØò(lambda ÂîÓ: (lambda ÂîÓ: ÂîÓ[-1] if ÂîÓ in ÂÛê('𝔸\u2009𝕂') else ÄÔýò)(getattr(ÂîÓ, 't')))(áÖâ)})
    if '𝔸' not in cur and áÑæ in ÄÔÕý:
        getattr(getattr(áÖâ, 'c'), 'append')(ÆåÞ_dec_ÞáÑË(MOD(ÄÕéý, áØÁ=Âîì)(áÑæ, áÖâ)))
    if '𝕂' not in cur and áÑð in ÄÔÕý:
        getattr(getattr(áÖâ, 'c'), 'append')(ÆåÞ_dec_ÞáÑÕ(MOD(ÄÕéý, áØÁ=Âîì)(áÑð, áÖâ)))
    (ÄÊÞPSH(getattr(ÄÕÒü, 'e')), ÄÊÞPSH('VK'), ÄÊÞPSH(True), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    return ÄÕÒü

def preformat_whiskers(ÄÕÒü):
    if getattr(ÄÕÒü[2], 't') == '✓':
        (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH(2), ÄÊÞPSH(MOD(ÄÕéý, áØÁ=ÂØÙ)(áÎô('𝑋↓↑'), ÄÕÒü[2])), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    (c := (getattr(ÄÕÒü[2], 't') == '𝑋𝐶' and getattr((áÎÎ := ÄÕÒü[2][0]), 't') in ÂÛê('𝑇↑\u2009slice')))
    if getattr(ÄÕÒü[1], 't') in 'ᑀᐵ\U000f7eb9\U000f7eba':
        if c:
            (áÕÃ := (áÕÃ if (getattr(áÎÎ[0], 't') == '𝑋↓↑' and ãÊú(áÎÎ[0])) and getattr((áÕÃ := áÎÎ[0][0]), 't') == 'slice' else áÎÎ))
        if c and getattr(áÕÃ[0], 't') == 'ᗜ':
            (ÄÊÞPSH(áÕÃ), ÄÊÞPSH(0), ÄÊÞPSH(áÎô('𝑋↓↑', áÓé(MOD(ÄÕéý, áØÁ=Âîë)('⟞', ÄÕÒü)))), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
        elif c:
            getattr(getattr(áÕÃ[0], 'c'), 'insert')(0, áÓé(MOD(ÄÕéý, áØÁ=Âîë)('⟞', ÄÕÒü)))
        else:
            getattr(getattr(ÄÕÒü[2], 'c'), 'insert')(0, áÓé(MOD(ÄÕéý, áØÁ=Âîë)('⟞', ÄÕÒü)))
    if getattr(ÄÕÒü[3], 't') in 'ᑅᑈ\U000f7ebd\U000f7ebe':
        if c:
            (áÕÃ := (áÕÃ if (getattr(áÎÎ[-1], 't') == '𝑋↓↑' and ãÊú(áÎÎ[-1])) and getattr((áÕÃ := áÎÎ[-1][-1]), 't') == 'slice' else áÎÎ))
        if c and getattr(áÕÃ[-1], 't') == 'ᗜ':
            (ÄÊÞPSH(áÕÃ), ÄÊÞPSH(-1), ÄÊÞPSH(áÎô('𝑋↓↑', áÓé(MOD(ÄÕéý, áØÁ=Âîë)('⟝', ÄÕÒü)))), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
        elif c:
            getattr(getattr(áÕÃ[-1], 'c'), 'append')(áÓé(MOD(ÄÕéý, áØÁ=Âîë)('⟝', ÄÕÒü)))
        else:
            getattr(getattr(ÄÕÒü[2], 'c'), 'append')(áÓé(MOD(ÄÕéý, áØÁ=Âîë)('⟝', ÄÕÒü)))
    return ÄÕÒü

def format_whiskers(ÄÕÒü):
    (ÄÊÞPSH(Áÿú(ÂÛê('ᑀᐵᐒᐖ\u2009\U000f7eb9\U000f7eba\U000f7ebb\U000f7ebc\u205fᑅᑈᐘᐛ\u2009\U000f7ebd\U000f7ebe\U000f7ebf\U000f7ec0'), Âåæ(ÂÑÖ(), ÂÛÅ))), ((tl := ÄÊÞPKE(0)[0]), (tr := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    (ÄÊÞPSH(ÄÕÒü), ((lb := ÄÊÞPKE(0)[0]), (áÖù := ÄÊÞPKE(0)[1]), (áÖÔ := ÄÊÞPKE(0)[2]), (áØÀ := ÄÊÞPKE(0)[3]), (rb := ÄÊÞPKE(0)[4])), ÄÊÞDEL(1))[1]
    (ÄÊÞPSH((MOD(Áëý, áØÁ=+lb)(+áÖù, lambda ÂîÓ: tl[ÂîÓ]) or 'ᐳ', MOD(Áëý, áØÁ=+rb)(+áØÀ, lambda ÂîÓ: tr[ÂîÓ]) or 'ᐸ')), ((áÖù := ÄÊÞPKE(0)[0]), (áØÀ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    (áÖü := getattr(áÎõ['␀TAC'], 'copy')())
    (ÄÊÞPSH(áÖü), ÄÊÞPSH('t'), ÄÊÞPSH(áÖù + áØÀ), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    (ÄÊÞPSH(áÖü), ÄÊÞPSH('L'), ÄÊÞPSH(getattr(áÖü, 'L') if áÖù in tl ** î else ÂÚü()), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    (ÄÊÞPSH(áÖü), ÄÊÞPSH('R'), ÄÊÞPSH(getattr(áÖü, 'R') if áØÀ in tr ** î else ÂÚü()), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    (ÄÊÞPSH(áÖü), ÄÊÞPSH('N'), ÄÊÞPSH((ÄÊÞPSH(áÖü), ÄÊÞPSH('Ïë'), ÄÊÞPSH((ÄÊÞPSH(áÖü), ÄÊÞPSH('ÏÁ'), ÄÊÞPSH(True), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    if áÖù != 'ᐳ':
        (ÄÊÞPSH(áÖü), ÄÊÞPSH('S'), ÄÊÞPSH(True), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    if áØÀ != 'ᐸ':
        (ÄÊÞPSH(áÖü), ÄÊÞPSH('P'), ÄÊÞPSH(True), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    if áÖù != 'ᐳ' and áØÀ != 'ᐸ':
        (ÄÊÞPSH(áÖü), ÄÊÞPSH('B'), ÄÊÞPSH(True), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    (ÂÑÕ := áÓâáÓã(MOD(ÄÕéý, áØÁ=ÂØÙ)(getattr(áÖü, 't'), ÄÕÒü)))
    (ÄÊÞPSH(ÂÑÕ), ÄÊÞPSH('t'), ÄÊÞPSH(getattr(ÂÑÕ, 'e')), ÄÊÞPSH('O'), ÄÊÞPSH(('𝗈𝗉', áÖü)), (setattr(ÄÊÞPKE(4), ÄÊÞPKE(3), ÄÊÞPKE(0)[0]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)[1])), ÄÊÞDEL(5))[5]
    (ÄÊÞPSH(getattr(ÂÑÕ, 'e')), ÄÊÞPSH('k'), ÄÊÞPSH((0 if áÖù == 'ᐳ' else 1 if áÖù in 'ᑀᐒ\U000f7eb9\U000f7ebb' else 2, 0 if áØÀ == 'ᐸ' else 1 if áØÀ in 'ᑅᐘ\U000f7ebd\U000f7ebf' else 2)), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    (ÄÊÞPSH(áÖü), ÄÊÞPSH('t'), ÄÊÞPSH('␀T%s' % ((áÖù in 'ᑀᐵᐒᐖ') * '⟞' + '⟝' * (áØÀ in 'ᑅᑈᐘᐛ'),)), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    (ÄÊÞPSH((áÖù in 'ᑀᐵ\U000f7eb9\U000f7eba', áØÀ in 'ᑅᑈ\U000f7ebd\U000f7ebe')), ((il := ÄÊÞPKE(0)[0]), (ir := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    (ÄÊÞPSH(ÂÑÕ), ÄÊÞPSH(1), ÄÊÞPSH(ÏéÞ_add_vk(áÓßáÓÓáÓàáÓÔ(MOD(ÄÕéý, áØÁ=Âîë)(áÓÙáÓãáÓÓáÓåáÓÓáÓàáÓæ(*ÁØò(lambda ÂîÓ: áÓé(MOD(ÄÕéý, áØÁ=Âîë)(ÂîÓ, áÖÔ)))((áÖù != 'ᐳ') * '⟞' + '⟝' * ('ᐸ' != áØÀ))), áÖÔ), getattr(áÖÔ, 'set')(t='x')), '𝓐', '𝓚')), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    if not ÂØõ(getattr(getattr(ÂÑÕ, 'e'), 'k')):
        return ÂÑÕ[1]
    return ÂÑÕ

def reformat_whiskers(ÄÕÒü):

    @getattr(ÄÕÒü, 'frp')(lambda ÂîÓ: (getattr(ÂîÓ, 't') == '∘' and getattr(ÂîÓ[0], 't') == '𝗈𝗉') and getattr(getattr(getattr(ÂîÓ[0], 'e'), 'O'), 't') in ÂÛê('␀T\u2009␀T⟞\u2009␀T⟝\u2009␀T⟞⟝'), None, True)
    def _(ÄÕÒü):
        (ÄÊÞPSH(ÄÕÒü), ((Æå := ÄÊÞPKE(0)[0]), (áÖí := ÄÊÞPKE(0)[1]), (áÖî := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]
        (ÄÊÞPSH((áÖí != áÓÆáÓÍáÓÄáÓÄ, áÖî != áÓÆáÓÍáÓÄáÓÄ)), ((Ïß := ÄÊÞPKE(0)[0]), (Ïà := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
        (ÄÊÞPSH(getattr(getattr(Æå, 'e'), 'k')), ((áÖù := ÄÊÞPKE(0)[0]), (áØÀ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
        ÂùÆ(((ÄÊÞDEL(1), False)[1] if Ïß else ÄÊÞPOP()) if ÄÊÞPSH(not áÖù) else (ÄÊÞDEL(1), True)[1]) and (((ÄÊÞDEL(1), False)[1] if Ïà else ÄÊÞPOP()) if ÄÊÞPSH(not áØÀ) else (ÄÊÞDEL(1), True)[1])
        if (ÄÊÞDEL(1), False)[1] if ÄÊÞPSH(áÖù) else ÄÊÞPOP() if áØÀ else (ÄÊÞDEL(1), True)[1]:
            return Æå
        if not áÖù and 1 == áØÀ:
            return getattr(ÄÕÒü, 'set')(c=[Æå, áÖî]) if Ïà else Æå
        if áÖù == 1 and (not áØÀ):
            return getattr(ÄÕÒü, 'set')(c=[Æå, áÖí]) if Ïß else Æå
        if (((áÖù == ÄÊÞPSH(1) and ÄÊÞPOP() == ÄÊÞPSH(áØÀ)) and (ÄÊÞDEL(1) or True) or (ÄÊÞDEL(1) or False)) and Ïß) and Ïà:
            return ÄÕÒü
        if áÖù == 2 or áØÀ == 2:
            (Æå := áÎô('∘', áÓé((ÁØã, 'ᑀ', 'ᐵ')[áÖù] + (ÁØã, 'ᑅ', 'ᑈ')[áØÀ]), Æå))
        if (not áÖù or Ïß) and (not áØÀ or Ïà):
            return getattr(ÄÕÒü, 'set')(c=[Æå, *MOD(Âêà, áØÁ=Ïß)(áÖí), *MOD(Âêà, áØÁ=Ïà)(áÖî)])
        if ((ÄÊÞDEL(1), False)[1] if ÄÊÞPSH(áÖù) else ÄÊÞPOP() if áØÀ else (ÄÊÞDEL(1), True)[1]) and ((ÄÊÞDEL(1), False)[1] if ÄÊÞPSH(Ïß) else ÄÊÞPOP() if Ïà else (ÄÊÞDEL(1), True)[1]):
            return áÎô('∘', áÓé('CUR'), Æå)
        if áÖù and áØÀ:
            if (ÄÊÞDEL(1), False)[1] if ÄÊÞPSH(Ïß) else ÄÊÞPOP() if Ïà else (ÄÊÞDEL(1), True)[1]:
                return áÎô('∘', áÓé('CUR'), Æå)
            if (ÄÊÞDEL(1), False)[1] if ÄÊÞPSH(Ïß) else ÄÊÞPOP() if not Ïà else (ÄÊÞDEL(1), True)[1]:
                return áÎô('∘', áÓé('CURR'), Æå, áÖî)
            if (ÄÊÞDEL(1), False)[1] if ÄÊÞPSH(not Ïß) else ÄÊÞPOP() if Ïà else (ÄÊÞDEL(1), True)[1]:
                return áÎô('∘', áÓé('CUR'), Æå, áÖí)
        if ÄÝøø(áÖù, áØÀ) and ((ÄÊÞDEL(1), False)[1] if ÄÊÞPSH(Ïß) else ÄÊÞPOP() if Ïà else (ÄÊÞDEL(1), True)[1]):
            return áÎô('∘', áÓé('MOD'), Æå)
        ÂùÆ(False)

def rewrite_lambs(ÄÕÒü):
    getattr(ÄÕÒü, 'ftrp')('whiskers', format_whiskers, True)
    getattr(ÄÕÒü, 'ftrp')('lamb_h_preset', lambda ÄÕÒü: MOD(ÄÕéý, áØÁ=Âîì)(áÓÙáÓãáÓÓáÓåáÓÓáÓàáÓæ(*ÁØò(lambda ÂîÓ: áÓé(MOD(ÄÕéý, áØÁ=Âîì)(ÂîÓ, ÄÕÒü[0])))(ÄÝöÈ('xyzwvutsr', ÂóÍ(0, -1 + MOD(ÄÔÞÔ, ÁÜñ=ÄÕøü)('𝚲\U000f0c9f\U000f0ca1\U000f0ca3\U000f0ca5\U000f0ca7\U000f0ca9\U000f0cab\U000f0cad\U000f0caf\U000f0cb1', +ÄÕÒü[0]))))), ÄÕÒü[0]), True)
    getattr(ÄÕÒü, 'ftrp')('lamb_h_implicit', lambda ÄÕÒü: áÓÙáÓãáÓÓáÓåáÓÓáÓàáÓæ(áÓé(ÄÕÒü[0])), True)
    getattr(ÄÕÒü, 'ftrp')('lamb', ÏéÞ_add_vk, True)

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/Libraries/Compiler/rewriters.☾'
def rewrite_for(ÄÕÒü):
    getattr(ÄÕÒü, 'ftrp')('comp_∀', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(c=[MOD(ÄÕéý, áØÁ=ÂØÙ)(áÓÙáÓâáÓå(ÄÕÒü[0], ÄÕÒü[1], ÄÕÒü[2], ÄÕÒü[3] or áÓÒ), ÄÕÒü)]), True)
    getattr(ÄÕÒü, 'ftrp')('stmt_∀', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(c=[MOD(ÄÕéý, áØÁ=ÂØÙ)(áÓÙáÓâáÓå(áÓÒ, ÄÕÒü[0] or áÓÒ, ÄÕÒü[1] or áÓéáÓæ('✓'), ÄÕÒü[2] or áÓÒ), ÄÕÒü)]), True)

def grp_blks(ÄÕÒü):
    (áÎÙ := (lambda x: lambda ÄÕÒü: ((getattr(ÄÕÒü, 't') == 'blk' and getattr(ÄÕÒü[0], 't') == 'stmt') and getattr(ÄÕÒü[0][0], 't') == 'blk_head') and (lambda ÂîÓ: getattr(ÂîÓ, 't') == 'stmt_∀' if x == '∀' else getattr(ÂîÓ[0][0], 't') == x)(ÄÕÒü[0][0][0])))

    @getattr(ÄÕÒü, 'ftrp')(ÂÛê('stmts\u2009blk'), None, True)
    def _(ÄÕÒü):
        return getattr(ÄÕÒü, 'set')(c=UGX_CREATE(('B', (àìÒ := []), '*', None, ('∨', ('B', (àìÒ := []), '', lambda ÂîÓ: áÎô('¿⸘¡', *ÂîÓ), ('∧', (áÎÙ('¿'), ''), (áÎÙ('⸘'), '*'), (áÎÙ('¡'), '?'))), ('B', (àìÒ := []), '', lambda ÂîÓ: áÎô('\ue00a¡\ue80d', *ÂîÓ), ('∧', (áÎÙ('\ue00a'), ''), (áÎÙ('¡'), '*'))), ('B', (àìÒ := []), '', lambda ÂîÓ: áÎô('∀¡', *ÂîÓ), ('∧', (áÎÙ('∀'), ''), (áÎÙ('¡'), '?'))), (ÃÆë, ''))))(getattr(ÄÕÒü, 'c')))
(part_cont := (lambda áüì, Æå: lambda x: UGX_CREATE(('B', (àìÒ := []), '*', None, ('∨', ('B', (àìÒ := []), '*', Æå, (áüì, '')), (ÃÆë, ''))))(x) or ÂÚü()))
(T1 := MOD(ÂÑÖ, áØÁ=None)()(ÄÕåØ('𝗮𝗯𝗳𝗻𝗿𝘁𝘃', [7, 8, 12, 10, 13, 9, 11])))

def map_special(x, ÄÕÒü=ÂÚü()):
    (T2 := getattr(ÁÜÙ, 'maketrans')(áÍÙ(ÄÕåØ('𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝗮𝗯𝗰𝗱𝗲𝗳', '0123456789abcdef'))))
    return áÓæáÓçáÓå(áÐè(MOD(ÄÕéý, áØÁ=ÂØÙ)(' ' if x else ÁØã, ÄÕÒü)) if x in '𝘀' else áÓæáÓçáÓåáÓÔ(áÐè(MOD(ÄÕéý, áØÁ=ÂØÙ)(ÁÜÙ(T1[x] or MOD(ÄÝöì, áØÁ=16)(getattr(x, 'translate')(T2))), ÄÕÒü))))

def rewrite_strs(ÄÕÒü):
    getattr(ÄÕÒü, 'ftrp')('str_spec_char', lambda ÄÕÒü: map_special(+ÄÕÒü, ÄÕÒü))
    getattr(ÄÕÒü, 'ftrp')(ÂÛê('empty_str\u2009str_t\U000f09a5\u2009str_timp\u2009str_tsub\u2009str_nsub\u2009str_tsys_guts\u2009str_tsub_guts\u2009str_timp_guts\u2009str_nsub1_guts\u2009str_nsub2_guts\u2009str_escape'), lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(t='str'), True)
    getattr(ÄÕÒü, 'ftrp')('str', lambda ÄÕÒü: áÓæáÓçáÓå(*ÄÔÙù(ÁØò(lambda ÂîÓ: MOD(Áëý, áØÁ=lambda ÂîÓ: getattr(getattr(ÂîÓ, 'e'), 'T') or getattr(ÂîÓ, 't') != 'str')(ÂîÓ, Âêà))(ÄÕÒü))), True)
    getattr(ÄÕÒü, 'ftrp')('x', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(c=part_cont(lambda ÂîÓ: not getattr(getattr(ÂîÓ, 'e'), 'T') and getattr(ÂîÓ, 't') == 'str', lambda x: áÓæáÓçáÓå(*ÄÔÙù(x)))(ÄÕÒü)), True)
    getattr(ÄÕÒü, 'ftrp')('str', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(c=part_cont(lambda ÂîÓ: getattr(getattr(ÂîÓ, 'e'), 'T'), lambda x: áÐè(MOD(ÄÕéý, áØÁ=ÂØÙ)(Âøî(ÁÙÇ(lambda ÂîÒ: +ÂîÒ)(x)), x)))(ÄÕÒü)), True)

def rewrite_numbers(ÄÕÒü):
    getattr(ÄÕÒü, 'ftrp')('neg_num', lambda ÄÕÒü: áÓÚáÓåáÓã('()', áÓâáÓã(MOD(ÄÕéý, áØÁ=Âîë)('¯', ÄÕÒü)), áÓá(MOD(ÄÕéý, áØÁ=ÂØÙ)(getattr(UPSIDEDOWNSYNDROME, 'flip')(+ÄÕÒü), ÄÕÒü))))
    getattr(ÄÕÒü, 'ftrp')('pos_num', áÓá)
    getattr(ÄÕÒü, 'ftrp')('number', MOD(ÁÛÛ, áØÁ=0))
    getattr(ÄÕÒü, 'ftrp')('number_exp', lambda ÄÕÒü: áÓÚáÓåáÓã('()', ÄÕÒü[0], áÓâáÓã(MOD(ÄÕéý, áØÁ=Âîì)('⌃', ÄÕÒü[0])), áÓÚáÓåáÓã('()', *ÄÕÒü[1])), True)

def rewrite_ternary(ÄÕÒü):
    (is_xpr_atom := (lambda ÄÕÒü: getattr(ÄÕÒü, 't') == 'x'))

    @getattr(ÄÕÒü, 'ftrp')('opC', None, True)
    def _(ÄÕÒü):
        (ÄÊÞPSH(ÄÕÒü), ((áÖü := ÄÊÞPKE(0)[0]), *(Ïß := ÄÊÞPKE(0)[slice(1, None, None)])), ÄÊÞDEL(1))[1]
        if getattr(getattr(getattr(áÖü, 'e'), 'O'), 't') != '⭝' or ãÊú(áÖü[2]):
            return ÄÕÒü
        (ÄÊÞPSH(Ïß), ((Ïß := ÄÊÞPKE(0)[0]), *(Ïà := ÄÊÞPKE(0)[slice(1, None, None)])), ÄÊÞDEL(1))[1]
        (Ïá := Ïß[0])
        if (getattr(Ïá, 't') != 'opC' or getattr(getattr(getattr(Ïá[0], 'e'), 'O'), 't') != '⭜') or ãÊú(Ïá[0][2]):
            return ÄÕÒü
        return áÓçáÓØáÓåáÓá(*Ïá[slice(1, None)], *Ïà)

    @getattr(ÄÕÒü, 'ftrp')('opC', None, True)
    def _(ÄÕÒü):
        (ÄÊÞPSH(ÄÕÒü), ((áÖü := ÄÊÞPKE(0)[0]), *(Ïß := ÄÊÞPKE(0)[slice(1, None, None)])), ÄÊÞDEL(1))[1]
        if (t := getattr(getattr(getattr(áÖü, 'e'), 'O'), 't')) not in '⭜⭝':
            return ÄÕÒü
        (ÄÊÞPSH(Ïß), ((Ïß := ÄÊÞPKE(0)[0]), (Ïà := ÄÊÞPKE(0)[1]), *(_ := ÄÊÞPKE(0)[slice(2, None, None)])), ÄÊÞDEL(1))[1]
        ÂùÆ(is_xpr_atom(Ïà))
        ÂùÆ(not ãÊú(áÖü[2]) or (ãÊú(áÖü[2]) == 1 and getattr(áÖü[2][0], 't') == '𝚜'))
        (áÑæ := (Ïà, áÖü[2][0][0] if ãÊú(áÖü[2]) else MOD(ÄÕéý, áØÁ=Âîì)(áÓë(áÓéáÓæ('□')), ÄÕÒü)))
        return áÓçáÓØáÓåáÓá(Ïß, *MOD(Áëý, áØÁ=t == '⭝')(áÑæ, ÂÀÇ))

def group_targets(ÄÕÒü):
    (dot := (lambda ÂîÓ: getattr(ÂîÓ, 't') == '𝗈𝗉' and getattr(ÂîÓ[1][0], 't') == '.'))
    (exp := (lambda ÂîÓ: getattr(ÂîÓ, 't') == 'exp'))
    (ÄÊÞPSH(MOD(ÂÚü, áØÁ=2)()), ((R := ÄÊÞPKE(0)[0]), (C := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
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
            getattr(C, 'append')(áÓàáÓÕáÓÓáÓß(v))
        elif dot(v):
            getattr(C, 'append')(áÓÓáÓçáÓçáÓå((lambda ÂîÓ: áÓæáÓçáÓå(ÂîÓ) if getattr(ÂîÓ, 't') == '𝑣' else ÂîÓ)(getattr(áÖï, 'pop')(0))))
        elif exp(v):
            getattr(C, 'append')(áÓØáÓëáÓã(getattr(áÖï, 'pop')(0)))
        else:
            adds(v)
    adds(None)
    (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH('c'), ÄÊÞPSH(R), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    return ÄÕÒü

def regroup_elements(ÄÕÒü):
    (áüì := Âåæ(ÄÔÙù, MOD(ÁØò(lambda ÂîÓ: [áÓàáÓÕáÓÓáÓß(ÂîÓ)] if getattr(ÂîÓ, 't') == '𝑇' else ÂîÓ if getattr(ÂîÓ, 't') == 'target_rhs' else [ÂîÓ]))))
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
            return áÎô('opC', áÓÇáÓÈ('⌃'), áÖý, ÄÕÒü[0])
        ÂùÆ(False)
    getattr(ÄÕÒü, 'ftrp')('applier', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(c=[MOD(ÆÑ, áØÁ=áÓë(ÄÕÒü[0]))(getattr(ÄÕÒü, 'c')[slice(1, None)], áÕá)]), True)

def reduce_ÞÏð(ÄÕÒü):
    if not getattr((áÖü := getattr(getattr(ÄÕÒü[0], 'e'), 'O')), 'Ïð'):
        return ÄÕÒü
    (áÑæ := [ÄÕÒü[0]])
    for n in ÄÕÒü[slice(1, None)]:
        if (getattr(n, 't') == 'x' and ãÊú(n) == 1) and (lambda ÂîÓ: getattr(ÂîÓ, 't') == 'opC' and getattr(getattr(getattr(ÂîÓ[0], 'e'), 'O'), 't') == getattr(áÖü, 't'))(n[0]):
            getattr(áÑæ, 'extend')(n[0][slice(1, None)])
            continue
        getattr(áÑæ, 'append')(n)
    (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH('c'), ÄÊÞPSH(áÑæ), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    return ÄÕÒü

def add_cmp_op_chains(ÄÕÒü):
    for L in ÂÀÇ(áÖááÖæ):
        if not (áÖå := áÍè(ÁØò(lambda ÂîÓ: ÂîÓ[0] if ÂÔö(ÄÝöË(ÂîÓ[1]), 'λ') else ÄÔýò)(L))):
            continue
        (relv := (lambda ÂîÓ: áÖü if getattr(ÂîÓ, 't') == 'opC' and getattr((áÖü := getattr(getattr(ÂîÓ[0], 'e'), 'O')), 't') in áÖå else None))
        (charg := (lambda ÂîÓ: (ãÊú(ÂîÓ) == 1 and getattr(ÂîÓ, 't') == 'x') and relv(ÂîÓ[0])))

        @getattr(ÄÕÒü, 'ftrp')('opC', None, True)
        def _(ÄÕÒü):
            if not (áÖü := relv(ÄÕÒü)):
                return ÄÕÒü
            (ÄÊÞPSH(getattr(ÄÕÒü, 'c')), ÄÊÞPSH(slice(1, None)), ÄÊÞPSH(ÄÔÙù(ÁØò(lambda ÂîÓ: MOD(Áëý, áØÁ=charg)(ÂîÓ, [Âêà, MOD(ÁÛÛ, áØÁ=0)]))(getattr(ÄÕÒü, 'c')[slice(1, None)]))), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
            return ÄÕÒü
        getattr(ÄÕÒü, 'ftrp')('opC', lambda ÄÕÒü: getattr(ÄÕÒü, 'cp')(t='cmp') if relv(ÄÕÒü) else ÄÕÒü, True)
    return ÄÕÒü

def rewrite_cmp(ÄÕÒü):

    @getattr(ÄÕÒü, 'ftrp')('cmp', None, True)
    def _(ÄÕÒü):
        if ãÊú(ÄÕÒü) <= 3:
            return getattr(ÄÕÒü, 'set')(t='opC')
        (ÄÊÞPSH(áÇù(getattr(ÄÕÒü, 'c'), lambda ÂîÓ: getattr(ÂîÓ, 't') == '𝗈𝗉')), ((o := ÄÊÞPKE(0)[0]), (v := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
        (ÄÊÞPSH(o), ÄÊÞPSH(ÂÀÇ(ÄÊÞPKE(0))), (o := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2]
        (C := ÆÑ([áÓâáÓãáÒú(getattr(o, 'pop')(0), getattr(v, 'pop')(0), áÓÖ(getattr(v, 'pop')(0))), *ÁØò(lambda ÂîÓ: áÓâáÓãáÒú(getattr(o, 'pop')(0), ÐÌü(áÓã), áÓÖ(ÂîÓ)))(v), None], lambda *áÑË: áÓâáÓãáÒú('∧', *Âçß(áÑË))))
        return MOD(ÄÕéý, áØÁ=ÂØÙ)(áÓâáÓãáÒú('∨', áÓâáÓãáÒú('∧', getattr(ÄÕÒü, 'set')(t='opC', c=C), áÓâáÓãáÒú('∨', áÓå(1), áÓéáÓæ('✓'))), áÓâáÓãáÒú('∨', áÓå(1), áÓéáÓæ('✗'))), ÄÕÒü)

def rewrite_asgns(ÄÕÒü):
    getattr(ÄÕÒü, 'ftrp')('asgn', lambda ÄÕÒü: áÓë(áÓâáÓãáÒú(denode_op(áÓâáÓã(MOD(ÄÕéý, áØÁ=ÂØØ)('≔', ÄÕÒü))), *ÄÕÒü)), True)
    ÁØò(lambda ÂîÓ: getattr(getattr(ÂîÓ, 'flat')(lambda ÂîÓ: getattr(ÂîÓ, 't') == 'x', False), 'flat')(lambda ÂîÓ: getattr(ÂîÓ, 't') == 'applier', False))(date_ÞÄÕÒü(lambda ÂîÓ: getattr(ÂîÓ, 't') in ÂÛê('asgn_targs\u2009asgn_targ'), 'x')(ÄÕÒü))
    (ÄÔöà := (lambda x, **áÑÕ: ÅÒ('\U000f0a08', e=MOD(ÂÑÖ, áØÁ=None)()(I=x, **áÑÕ))))
    (âÛ := (lambda x, **áÑÕ: ÅÒ('߷', e=MOD(ÂÑÖ, áØÁ=None)()(I=x, **áÑÕ))))

    def p(ÄÕÒü, áÎÄ, *áÖÛ, áÎÜáÎØ=None):
        if getattr(ÄÕÒü, 't') in ÂÛê('x\u2009applier\u2009target_rhs'):
            return p(ÄÕÒü[0], áÎÄ, *áÖÛ, áÎÜáÎØ=áÎÜáÎØ)
        if getattr(ÄÕÒü, 't') == '𝗈𝗉':
            return áÎô('S𝑣', áÓé(ÄÕÒü[1][0]), ÄÔöà(áÖÛ))
        if getattr(ÄÕÒü, 't') == '𝑣':
            return áÎô('S𝑣', ÄÕÒü[0], ÄÔöà(áÖÛ))
        if getattr(ÄÕÒü, 't') == '𝑇':
            (i := MOD(Áëý, áØÁ=lambda ÂîÓ: ÂîÓ is None)(MOD(ÄÔÞÔ, ÁÜñ=ÄÕøü)(ÄÕÒü, lambda ÂîÓ: getattr(ÂîÓ, 't') == '𝔸' or ((getattr(ÂîÓ, 't') == 'x' and ãÊú(ÂîÓ) == 1) and getattr(ÂîÓ[0], 't') == '𝔸')), MOD(ÄÕÍÔ, áØÁ=ÂÕË)))
            return áÓÌ(*ËãÂ(ÂÓÏ(ÄÕÒü), lambda x, y: p(y, áÎÄ, *áÖÛ, x if x <= i else x - ãÊú(ÄÕÒü), áÎÜáÎØ=ãÊú(ÄÕÒü))))
        if getattr(ÄÕÒü, 't') == '𝔸':
            return áÎô('𝔸', p(ÄÕÒü[0], áÎÄ, *áÖÛ[slice(None, -1)], slice(None) if (not áÖÛ or None is áÎÜáÎØ) or áÎÜáÎØ == 1 else slice(áÖÛ[-1], o if (o := (áÖÛ[-1] - áÎÜáÎØ + 1)) else None)))
        if getattr(ÄÕÒü, 't') in '𝑖𝑎':
            getattr(áÎÄ, 'extend')(getattr(ÄÕÒü, 'c'))
            return áÎô('S' + getattr(ÄÕÒü, 't'), âÛ(ãÊú(áÎÄ) - 2), âÛ(ãÊú(áÎÄ) - 1), ÄÔöà(áÖÛ))
        ÂùÆ(False)

    @getattr(ÄÕÒü, 'frp')(lambda ÂîÓ: getattr(ÂîÓ, 't') == 'opC' and +ÂîÓ[0] in '≔\U000f7e09\U000f7e0a\U000f7e0b≕\U000f7e0e\U000f7e0c\U000f7e0d', None, True)
    def _(ÄÕÒü):
        (áÎÛ := ÄÕÒü[0])
        (áØÂ := getattr(áÎÛ[1][0], 't'))
        (ÄÊÞPSH((ÄÕÒü[1], ÄÕÒü[2]) if áØÂ in '≔\U000f7e09\U000f7e0a\U000f7e0b' else (ÄÕÒü[2], ÄÕÒü[1])), ((áÎÇ := ÄÊÞPKE(0)[0]), (áÍô := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
        if (áØÂ in '≔≕' and getattr(áÎÇ, 't') == 'x') and ãÊú(áÎÇ) == 1:
            if getattr(áÎÇ[0], 't') == '𝑣':
                return áÓë(áÎô('S𝑣', áÎÇ[0], áÍô))
            if getattr(áÎÇ[0], 't') == '𝗈𝗉':
                return áÓë(áÎô('S𝑣', áÓé(áÎÇ[0][1][0]), áÍô))
        (áÍö := p(áÎÇ, (áÎÄ := ÂÚü())))
        (is_ref_ÞáÍë := CURR(lambda ÂîÓ, ÂîÒ: getattr(ÂîÓ, 't') == '𝑣' and +ÂîÓ == ÂîÒ, getattr(getattr(áÎÛ, 'e'), 'áÖû')))
        (áÔê := (lambda ÄÕÒü, áÖõ: getattr(ÄÕÒü, 'ftrp')('\U000f0a08', lambda ÄÕÒü: MOD(ÆÑ, áØÁ=áÓà(áÐè(áÖõ)))(getattr(getattr(ÄÕÒü, 'e'), 'I'), CUR(lambda ÂîÓ, ÂîÒ: áÓÜ(ÂîÓ, áÓÓáÓèáÓçáÓâ(ÂîÒ)))))))
        (áÔë := (lambda ÄÕÒü, ÏÁ: getattr(ÄÕÒü, 'ftrp')('߷', lambda ÄÕÒü: áÓà(áÐè(ÏÁ + ~getattr(getattr(ÄÕÒü, 'e'), 'I'))))))
        (áÎÞ := áÎô('𝑇'))
        if áØÂ in '\U000f7e09\U000f7e0a\U000f7e0b\U000f7e0e\U000f7e0c\U000f7e0d':
            (áÎÜ := getattr(ÐÌü(getattr(áÍö, 'cpr')), 'ftrp')(ÂÛê('S𝑣\u2009S𝑖\u2009S𝑎'), lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(t=getattr(ÄÕÒü, 't')[slice(1, None)], c=getattr(ÄÕÒü, 'c')[slice(None, -1)])))
            getattr(áÎÄ, 'append')(MOD(ÄÕéý, áØÁ=áÔë)(áÎÜ, ãÊú(áÎÄ)))
        if áØÂ in '\U000f7e0a\U000f7e0b':
            (áÍô := getattr(áÍô, 'frp')(is_ref_ÞáÍë, lambda ÄÕÒü: áÓà(áÐè(0))))
        (áÍù := Áÿú(áÎÄ, áÓÖ))
        (áÍô := áÓÖ(áÍô))
        if áØÂ in '\U000f7e0c\U000f7e0d':
            (áÍô := getattr(áÍô, 'frp')(is_ref_ÞáÍë, lambda ÄÕÒü: áÓÜ(áÓÌ(*áÍù), áÐè(ãÊú(áÍù) - 1))))
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
        (ÄÊÞPSH((ÄÕÒü[1], ÄÕÒü[2])), ((a := ÄÊÞPKE(0)[0]), (b := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
        if getattr(ÄÕÒü[0][1][0], 't') == '\U000f7ea5':
            return áÓçáÓØáÓåáÓá(áÓÖ(a), áÓÊ(áÓå(1), áÓéáÓæ('✗')), áÓçáÓØáÓåáÓá(b, ÐÌü(áÓã), áÓÊ(áÓå(1), áÓéáÓæ('✓'))))
        else:
            return áÓçáÓØáÓåáÓá(áÓÖ(a), áÓçáÓØáÓåáÓá(b, áÓÊ(áÓå(1), áÓéáÓæ('✗')), ÐÌü(áÓã)), áÓÊ(áÓå(1), áÓéáÓæ('✓')))
        return ÄÕÒü
(part_ats := (lambda ÂîÓ: (getattr(ÂîÓ, 'copy')(c=(h := MOD(ÐÌÛ, áØÁ=áÍÖ)(getattr(ÂîÓ, 'c'), lambda ÂîÓ: getattr(ÂîÓ, 't')[-1] == '@'))[0]), áÍÙ(ÁØò(lambda ÂîÓ: (lambda ÂîÓ: (getattr(ÂîÓ, 't'), ÂîÓ))(getattr(ÂîÓ, 'copy')(t=getattr(ÂîÓ, 't')[slice(None, -1)])))(h[1])))))

def rewrite_ugex(ÄÕÒü):
    getattr(ÄÕÒü, 'flat')(lambda ÂîÓ: getattr(ÂîÓ, 't') in ÂÛê('ugx_and\u2009ugx_or') and ãÊú(ÂîÓ) == 1)
    getattr(ÄÕÒü, 'ftrp')('ugx_☾', lambda ÂîÓ: getattr(ÂîÓ, 'set')(t='𝑇', c=[ÂîÓ[0], áÓÓáÓèáÓçáÓâ(ÁØã if ãÊú(ÂîÓ) <= 1 else +ÂîÓ[1])]), True)

    @getattr(ÄÕÒü, 'ftrp')(ÂÛê('ugx_paren\u2009ugx_brack'), None, True)
    def _(ÄÕÒü):
        (ÄÊÞPSH(part_ats(ÄÕÒü)), ((n := ÄÊÞPKE(0)[0]), (e := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
        if ãÊú(n) > 1:
            (n := getattr(n, 'copy')(c=[áÎô('ugx_and', *n)]))
        (ÄÊÞPSH((getattr(e, 'get')('stk', áÎô('𝐿')), getattr(e, 'get')('apply', áÓéáÓæ('□')))), ((b := ÄÊÞPKE(0)[0]), (c := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
        (r := áÓÌ(áÓÓáÓèáÓçáÓâ('BP'[getattr(n, 't') == 'ugx_paren']), áÎô('S𝑣', áÓé('\U0001cce8'), b), áÓÓáÓèáÓçáÓâ((lambda ÂîÓ: ÂîÓ and +ÂîÓ)(getattr(e, 'get')('mod', ÁØã))), c, n))
        return r
    getattr(ÄÕÒü, 'ftrp')(ÂÛê('ugx_and\u2009ugx_or'), lambda ÄÕÒü: áÓÌ(áÓÓáÓèáÓçáÓâ('∧∨'[getattr(ÄÕÒü, 't') == 'ugx_or']), *ÄÕÒü), True)
    getattr(ÄÕÒü, 'ftrp')('ugx_x', lambda ÄÕÒü: áÓÕáÓÓáÓßáÓß('UGX_CREATE', *ÄÕÒü))

def rewrite_ports(ÄÕÒü):
    getattr(ÄÕÒü, 'ftrp')('str_timp_guts', lambda ÂîÓ: ÂåÔ(getattr(ÂîÓ[0], 'set')(t=getattr(getattr(ÂîÓ[0], 't'), 'rstrip')(' ')), ÂîÓ), True)
    getattr(ÄÕÒü, 'ftrp')('str_timp', lambda ÄÕÒü: áÓÕáÓÓáÓßáÓß('__þIMPORT__', ÄÕÒü[0], ÐÌü(áÒÿ)), True)

    @getattr(ÄÕÒü, 'ftrp')('import', None, True)
    def _(ÄÕÒü):
        if ãÊú(ÄÕÒü) < 2:
            return ÄÕÒü
        ÁØò(lambda ÂîÓ: ÂîÓ if +ÂîÓ[-1] != '@' else ÂåÔ((ÄÊÞPSH(ÂîÓ), ÄÊÞPSH(1), ÄÊÞPSH(áÓÕáÓÓáÓßáÓß(áÓÜ(ÐÌü(áÓà), áÓäáÓé('__þGET_GLOB_MODNAME__')))), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3], getattr(ÂîÓ, 'set')(t=' ')) if ãÊú(ÂîÓ) == 2 else (ÄÊÞPSH(ÂîÓ), ÄÊÞPSH(0), ÄÊÞPSH(áÓÕáÓÓáÓßáÓß(áÓÜ(ÐÌü(áÓà), áÓäáÓé('__þSET_GLOB_MODNAME__')))), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3])(getattr(ÄÕÒü[1], 'c'))
        return áÓÜ(áÓÌ(áÓÖ(ÄÕÒü[0]), *ÁØò(lambda ÂîÓ: ÂîÓ if getattr(ÂîÓ[0], 't') == '∘' else áÓÕáÓÓáÓßáÓß(ÐÌü(áÒÿ), '__þADDGLOBALS_CLEAN__', ÐÌü(áÓà)) if ãÊú(ÂîÓ) == 1 and +ÂîÓ == '*' else áÓë(áÓé(ÂîÓ[0][0]), áÓâáÓã('≔'), ÂîÓ[1] if ãÊú(ÂîÓ) == 2 and getattr(ÂîÓ, 't') == ' ' else áÓÜ(ÐÌü(áÓà), MOD(Áëý, áØÁ=getattr(ÂîÓ[0], 't') == '𝑣')(ÂîÓ[ãÊú(ÂîÓ) - 1][0], áÓäáÓé))))(getattr(ÄÕÒü[1], 'c')), ÐÌü(áÓã)), áÎô('neg_num', áÐè('\U000f7c3e')))
    getattr(ÄÕÒü, 'ftrp')('export', lambda ÄÕÒü: áÓÕáÓÓáÓßáÓß('__þADD_EXPORTS__', ÐÌü(áÒÿ), *ÁØò(lambda ÂîÓ: áÓÌ(áÓäáÓé(ÂîÓ[0]), ÂîÓ[ãÊú(ÂîÓ) - 1]))(getattr(ÄÕÒü[0], 'c'))), True)

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/Libraries/Compiler/to_ast.☾'
(gram := ÂÞÅÞCAT(ð(getattr(ÂÞÅÞCAT(__file__, áÌî), 'parent'), 'gram'), ÐØó))
(gram := gram_rp(MOD(ÄÔéÄ, áØÁ=gram)(ÂÛê('𝗐\u2009𝖶'), ÂÛê('𝘄?\u2009𝗪?')), áÕÒ, False))
(gram_comm := peggrampeg(gram, ÂÑÖ()(áÐü='comm')))
(gram_scrp := peggrampeg(gram, ÂÑÖ()(áÐü='scrp')))
(gram_main := peggrampeg(gram, ÂÑÖ()(áÐü='main')))

def to_ast(áÖïáÖüáÖðáÖñ, warn_short=True, trim_length_info=True, force_full_match=False, dbg_parser=0, dbg_show_gram_tree=False, **áÏè):
    (áÖïáÖüáÖðáÖñ := (+getattr(gram_comm(áÖïáÖüáÖðáÖñ, remove_trashes=False), 'ftrp')('comment', lambda ÂîÓ: ÂåÔ((ÄÊÞPSH(ÂîÓ[0]), ÄÊÞPSH('t'), ÄÊÞPSH(Âøî(ÁØò(lambda ÂîÓ: MOD(Áëý, áØÁ=ÄÊÞCUR((1,), {}, ÂÖÐ, ÂýÃ, '\n'))(ÂîÓ, MOD(ÄÕÍÔ, áØÁ=' ')))(getattr(ÂîÓ[0], 't')))), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3], ÂîÓ))))
    (ÄÊÞPSH(gram_subsup(áÖïáÖüáÖðáÖñ, gram_scrp)), ((áÖï := ÄÊÞPKE(0)[0]), (ÏÆ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    (ÄÕÒü := gram_main(áÖï, DEBUG=dbg_parser, remove_trashes=False))
    if dbg_show_gram_tree:
        áÍñáÍñ(ÄÕÒü, 'Initial parse')
    if warn_short:
        warn_if_short(ÄÕÒü)
    if force_full_match and is_short(ÄÕÒü):
        return None
    ÏÆ(ÄÕÒü)

    def Æå(ÄÕÒü, ÏÁ=0):
        if getattr(getattr(ÄÕÒü, 'e'), 'T'):
            (ÄÊÞPSH(getattr(ÄÕÒü, 'e')), ÄÊÞPSH('p'), ÄÊÞPSH((ÏÁ, (ÄÊÞPSH(ÏÁ), ÄÊÞPSH(ÄÊÞPKE(0) - ÂÖë(î)(getattr(getattr(ÄÕÒü, 'e'), 'p'))), (ÏÁ := ÄÊÞPKE(0)), ÄÊÞDEL(2))[2])), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
        elif getattr(ÄÕÒü, 't') in ÂÛê('SB\u2009SP\u2009SE'):
            (ÄÊÞPSH(getattr(ÄÕÒü, 'e')), ÄÊÞPSH('p'), ÄÊÞPSH((ÏÁ, ÏÁ)), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
        else:
            (ÄÊÞPSH(getattr(ÄÕÒü, 'e')), ÄÊÞPSH('p'), ÄÊÞPSH((ÏÁ, (ÏÁ := MOD(ÆÑ, áØÁ=ÏÁ)(ÄÕÒü, ÂÕì(Æå))))), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
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
    getattr(ÄÕÒü, 'ftrp')('𝐷', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(c=ÁØò(lambda ÂîÓ: áÓÜáÓçáÓØáÓà(MOD(Áëý, áØÁ=ÂÔø(getattr(ÂîÓ[0], 't'), 'str'))(ÂîÓ[0], lambda ÂîÓ: getattr(ÂîÓ, 'set')(t='str')), ÂîÓ[1]) if getattr(ÂîÓ, 't') == '𝐷_kv_nam' else áÓÜáÓçáÓØáÓà(*ÂîÓ) if getattr(ÂîÓ, 't') == '𝐷_kv_nrm' else ÂîÓ)(ÄÕÒü)), True)
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
        (ÄÊÞPSH(ÄÕÒü), ((áÖù := ÄÊÞPKE(0)[0]), (áÖá := ÄÊÞPKE(0)[1]), (áØÀ := ÄÊÞPKE(0)[2])), ÄÊÞDEL(1))[1]
        (áÎÚ := áÓçáÓàáÓã(getattr(ÄÕÒü, 'copy')(c=getattr(áÓâáÓã(áÖá), 'c'))))
        if +áÖá in '\U000f7e0a\U000f7e0b\U000f7e0c\U000f7e0d':
            (áØÄ := áÓé((ÄÊÞPSH(getattr(áÎÚ[0], 'e')), ÄÊÞPSH('áÖû'), ÄÊÞPSH('þ' + Âøî(getattr(getattr(ÄÕÒü, 'e'), 'p'), '_')), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]))
            getattr(getattr(áÎÚ, 'c'), 'append')(MOD(ÄÕéý, áØÁ=Âîì)(áØÄ, áÖá)) if +áÖá in '\U000f7e0a\U000f7e0b' else getattr(getattr(áÎÚ, 'c'), 'insert')(0, MOD(ÄÕéý, áØÁ=Âîë)(áØÄ, áÖá))
        if +áÖù:
            getattr(getattr(áÎÚ, 'c'), 'insert')(0, áÎô('sup', áÖù[0][0]))
        if +áØÀ:
            getattr(getattr(áÎÚ, 'c'), 'append')(áÎô('sup', áØÀ[0][0]))
        return áÎÚ
    getattr(ÄÕÒü, 'ftrp')('sup', lambda ÄÕÒü: áÓçáÓàáÓã(áÓâáÓã(MOD(ÄÕéý, áØÁ=Âîë)('.', ÄÕÒü)), ÄÕÒü[0][0]) if (getattr(ÄÕÒü[0], 't') == 'x' and ãÊú(ÄÕÒü[0]) == 1) and getattr(ÄÕÒü[0][0], 't') == '𝑣' else áÓçáÓàáÓã(áÓØáÓëáÓã(ÄÕÒü), áÓë(*ÄÕÒü)), True)
    getattr(ÄÕÒü, 'flat')(lambda ÂîÓ: getattr(ÂîÓ, 't') == 'tmp')
    getattr(ÄÕÒü, 'ftrp')('op', denode_op, True)
    getattr(ÄÕÒü, 'ftrp')('x', group_targets, True)
    rewrite_for(ÄÕÒü)
    grp_blks(ÄÕÒü)
    rewrite_strs(ÄÕÒü)
    flatten_statments(ÄÕÒü)
    getattr(ÄÕÒü, 'ftrp')('x', lambda ÄÕÒü: parse_expr(ÄÕÒü), True)
    getattr(ÄÕÒü, 'rm')(lambda ÂîÓ: ((getattr(ÂîÓ, 't') == 'opC' and +ÂîÓ[0][1] == '␀CAT') and ((getattr(ÂîÓ[1], 't') == ÄÊÞPSH(getattr(ÂîÓ[2], 't')) and ÄÊÞPOP() == ÄÊÞPSH('𝑣')) and (ÄÊÞDEL(1) or True) or (ÄÊÞDEL(1) or False))) and ((+ÂîÓ[1] == ÄÊÞPSH(+ÂîÓ[2]) and ÄÊÞPOP() == ÄÊÞPSH('NULL')) and (ÄÊÞDEL(1) or True) or (ÄÊÞDEL(1) or False)))
    getattr(ÄÕÒü, 'ftrp')('x', lambda ÄÕÒü: getattr(ÄÕÒü, 'copy')(c=ÄÔÙù(ÁØò(lambda ÂîÓ: MOD(Áëý, áØÁ=lambda ÂîÓ: getattr(ÂîÓ, 't') != 'x')(ÂîÓ, Âêà))(ÄÕÒü))), True)
    getattr(ÄÕÒü, 'ftrp')('X', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(t='x'), True)
    getattr(ÄÕÒü, 'ftrp')('opC', reduce_ÞÏð, True)
    add_cmp_op_chains(ÄÕÒü)
    rewrite_ternary(ÄÕÒü)
    regroup_elements(ÄÕÒü)
    rewrite_asgns(ÄÕÒü)
    rewrite_cmp(ÄÕÒü)
    getattr(ÄÕÒü, 'frp')(lambda ÂîÓ: getattr(ÂîÓ, 't') == 'opC' and +ÂîÓ[0] == '⋄', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(t='𝐿', c=getattr(ÄÕÒü, 'c')[slice(1, None)]), pre=True)
    getattr(ÄÕÒü, 'frp')(lambda ÂîÓ: getattr(ÂîÓ, 't') == 'opC' and +ÂîÓ[0][1][0] == ',', lambda ÄÕÒü: áÎô('𝑇', *ÄÕÒü[slice(1, None)]))
    (squashcat := (lambda ÄÕÒü: ÄÕÒü[0] if ãÊú(ÄÕÒü) == 1 else ÆÑ(getattr(ÄÕÒü, 'c'), lambda x, y: áÓâáÓãáÒú(denode_op(áÓâáÓã(MOD(ÄÕéý, áØÁ=Âîì)('␀CAT', x))), x, y))))
    (squashmul := (lambda ÄÕÒü: ÄÕÒü[0] if ãÊú(ÄÕÒü) == 1 else ÆÑ(getattr(ÄÕÒü, 'c'), lambda x, y: áÓÕáÓÓáÓßáÓß(denode_op(áÓâáÓã(MOD(ÄÕéý, áØÁ=Âîì)('⋅', x))), x, y))))
    getattr(ÄÕÒü, 'ftrp')('x', lambda ÄÕÒü: getattr(ÄÕÒü, 'set')(c=ÂÕÅ(part_cont(lambda ÂîÓ: getattr(ÂîÓ, 't') in ÂÛê('𝐿\u2009𝑇\u2009str\u2009num'), lambda x: áÎô('⋅', *x)), getattr(ÄÕÒü, 'c'))), True)
    getattr(ÄÕÒü, 'ftrp')('x', squashcat, True)
    getattr(ÄÕÒü, 'ftrp')('opC', lambda ÂîÓ: getattr(ÂîÓ, 'set')(t='∘'), True)
    getattr(ÄÕÒü, 'ftrp')('⋅', squashmul, True)
    reformat_whiskers(ÄÕÒü)
    getattr(ÄÕÒü, 'frp')(lambda ÂîÓ: getattr(ÂîÓ, 't') == '𝑇' and ãÊú(ÂîÓ) == 1, lambda ÄÕÒü: MOD(ÄÕéý, áØÁ=ÂØÙ)(áÎô('𝑃', *ÄÕÒü), ÄÕÒü), True)
    getattr(ÄÕÒü, 'frp')(lambda ÂîÓ: getattr(ÂîÓ, 't') == '𝑇', lambda ÂîÓ: getattr(ÂîÓ, 'set')(c=getattr(ÂîÓ, 'c')[slice(None, -1)]) if ÂîÓ and getattr(ÂîÓ[-1], 't') == 'ᗜ' else ÂîÓ, True)
    getattr(ÄÕÒü, 'ftrp')('ᗜ', lambda x: MOD(ÄÕéý, áØÁ=ÂØÙ)(áÓéáÓæ('□'), x))
    add_short_circuits(ÄÕÒü)
    curry_ops(ÄÕÒü)
    rewrite_ugex(ÄÕÒü)
    getattr(ÄÕÒü, 'ftrp')('∘', lambda ÄÕÒü, *áÑË: getattr(ÄÕÒü, 'set')(c=[ÄÕÒü[0], *ÁØò(lambda ÂîÓ: ÂîÓ[0] if (getattr(ÂîÓ, 't') == '𝑃' and ãÊú(ÂîÓ[0]) == 1) and getattr(ÂîÓ[0], 't') == '𝔸' else ÂîÓ)(ÄÕÒü[slice(1, None)])]), True)
    return ÄÕÒü
(__exports__ := ÂÛê('to_ast'))

__file__='/home/ganer/Projects/Moon_BETA/NewMoon/Libraries/Compiler/ast_to_py.☾'
from unicodedata import is_normalized
from keyword import kwlist
(áÌÐ := ÂÑÖ()(áÍëÞ_spec=ÂÞÅÞCAT(ÂÛê('✓\u2009True\u205f✗\u2009False\u205f□\u2009None'), ÂÑÖ()), std_kwd=ÂÞÅÞCAT(ÂÛê('↪\u2009return\u205f⮂\u2009yield\u205f\U000f01b4\u2009del\u205f↺\u2009continue\u205f⇥\u2009break'), ÂÑÖ()), blk_cln_kwd=ÂÞÅÞCAT(ÂÛê('¿\u2009if\u205f⸘\u2009elif\u205f¡\u2009else\u205f∀\u2009for\u205f\U000f1018\u2009class'), ÂÑÖ()), blk_kwd=ÂÞÅÞCAT(MOD(ÂÛê, áØÁ='\u205f\u2009')('\ue00a\u2009try'), ÂÑÖ()), op=ÂÞÅÞCAT(ÐÈÔ('~~%%^^&&||>><<++¯---⋅*÷/', [2]) + ÂÛê('⹏\u2009//\u205f⌃\u2009**\u205f≥\u2009>=\u205f≤\u2009<=\u205f≡\u2009==\u205f≠\u2009!=\u205f∨\u2009or\u205f∧\u2009and\u205f∨\u2009or\u205f¬\u2009not\u205f∈\u2009in\u205f∉\u2009not in\u205f≅\u2009is\u205f≇\u2009is not'), ÂÑÖ())))
(ENC := 'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýÿ')
(RCD := CURR(lambda ÂîÓ, ÂîÒ: ÂîÓ not in ÂîÒ, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'))
(SPE := (lambda ÂîÓ: ÂîÓ in ENC + 'þ'))
(bruh := (lambda x: ÄÝöì(x, C=ENC)))
(PEV := (lambda ÂîÓ: Âøî(MOD(ÄÔÔç, áØÁ=Âåæ(Âøî, MOD(ÁØò(lambda ÂîÓ: ÄÝöì(ÄÝöí(ÂîÓ), ãÊú(ENC), C=ENC)))))(áÇù(ÂîÓ, RCD), lambda ÂîÓ: ÂÁÍ(ÂÕÅ)(ÂîÓ[0], RCD)), 'Þ')))
(VEP := (lambda ÂîÓ: Âøî(MOD(ÄÔÔç, áØÁ=lambda ÂîÓ: Âøî(ÁØò(lambda ÂîÓ: MOD(Áëý, áØÁ=ÄÊÞCUR((1,), {}, ÂÖó, ÂýÃ, ENC))(ÂîÓ, ÄÔâÑ(Âåæ(Âåæ(Âøî, ÄÝöí), bruh), lambda x: '⸮%s?' % (x,))))(ÄÝöÞ(ÂîÓ, 'þ'))))(áÇù(ÂîÓ, SPE), lambda ÂîÓ: ÂÁÍ(ÂÕÅ)(ÂîÓ[0], SPE)))))
(py_esc_str := Âåæ(Âøî, MOD(ÁØò(lambda ÂîÓ: '\\u%s' % (MOD(ÄÝöì, áØÁ=16 + ÂÞÅÞCAT(4, Ãù))(ÄÝöí(ÂîÓ)),) if ÂîÓ in áÍè('\n\t\\\'"{}') else ÂîÓ))))
(áÓÄ := (lambda x=ÁØã, y=4 * ' ': Âøî(Áÿú(lines(x), ÄÊÞCUR((2,), {}, ì, y, ÂýÃ)), '\n')))

def expand_ast_py(ÄÕÒü, PEV=PEV):
    if getattr(getattr(ÄÕÒü, 'e'), 'T'):
        return ÄÕÒü
    if getattr(ÄÕÒü, 't') == '𝗈𝗉':
        if (m := ÄÔÙù(ÄÕÒü[0], ÄÕÒü[2])):
            (t := MOD(ÂÑÖ, áØÁ=[])()(ÐÌÛ(m, lambda ÂîÓ: 1 if getattr(ÂîÓ, 't') in áÍè('≺≻ᵜ꜠') else 2 if getattr(ÂîÓ, 't') in áÍè('ᔨ') else 0 if getattr(ÂîÓ, 't') in '𝚜' else ÄÔýò)))
            (a := (t[0] if ãÊú(t[0]) == 1 else [áÐè('('), *Âøî(t[0], áÐè(',')), áÐè(')')] if ãÊú(t[0]) else ÂÚü()))
            (áÑæ := ÁØò(lambda ÂîÓ: áÓë(áÓé(getattr(ÂîÓ, 't')), áÐè('='), ÂîÓ[0] if ãÊú(ÂîÓ) else áÓé('\U000f18e9')))(([áÎô('𝚜', áÓë(*a))] if a else ÂÚü()) + t[2]))
            (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH(1), ÄÊÞPSH(MOD(ÆÑ, áØÁ=ÄÕÒü[1])(t[1], CUR(lambda ÂîÓ, ÂîÒ: áÓÕáÓÓáÓßáÓß(getattr(ÂîÒ, 't'), ÂîÓ)))), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
            (ÄÕÒü := (áÓÕáÓÓáÓßáÓß(áÐè('MOD'), ÄÕÒü[1], *áÑæ) if áÑæ else ÄÕÒü[1]))
    if getattr(ÄÕÒü, 't') in ÂÛê('𝑇\u2009ƒ_dec_params'):
        getattr(ÄÕÒü, 'set')(c=[áÐè('('), *MOD(ÄÕéý, áØÁ=ÂîË if getattr(ÄÕÒü, 't') == '𝑇' and ãÊú(ÄÕÒü) == 1 else Âøî)(getattr(ÄÕÒü, 'c'), áÐè(',')), áÐè(')')])
    elif getattr(ÄÕÒü, 't') in '𝑆𝐷':
        if getattr(ÄÕÒü, 't') == '𝐷':
            for c in ÄÕÒü:
                if getattr(c, 't') != '𝔸':
                    continue
                getattr(c, 'set')(t='𝕂', c=[áÓÕáÓÓáÓßáÓß('dict', *c)])
        getattr(ÄÕÒü, 'set')(c=[áÐè('{'), *Âøî(getattr(ÄÕÒü, 'c'), áÐè(',')), áÐè('}')])
    elif getattr(ÄÕÒü, 't') == '𝑃':
        getattr(ÄÕÒü, 'set')(c=[áÐè('('), *Âøî(getattr(ÄÕÒü, 'c'), áÐè(',')), áÐè(')')])
    elif getattr(ÄÕÒü, 't') == '𝐿':
        getattr(ÄÕÒü, 'set')(c=[áÐè('['), *Âøî(getattr(ÄÕÒü, 'c'), áÐè(',')), áÐè(']')])
    elif getattr(ÄÕÒü, 't') == '𝑖':
        getattr(ÄÕÒü, 'set')(c=[ÄÕÒü[0], áÐè('['), *Âøî(ÄÕÒü[slice(1, None)], áÐè(',')), áÐè(']')])
    elif getattr(ÄÕÒü, 't') == '∘':
        (áÖò := ÄÕÒü[0])
        if (getattr(áÖò, 't') == '𝗈𝗉' and +áÖò[1] in getattr(áÌÐ, 'op')) and ((ÄÊÞDEL(1), False)[1] if ÄÊÞPSH(ãÊú(áÖò[0])) else ÄÊÞPOP() if ãÊú(áÖò[2]) else (ÄÊÞDEL(1), True)[1]):
            (p := (ãÊú(ÄÕÒü) < 3 and getattr((ÂÑÕ := getattr(getattr(áÖò, 'e'), 'O')), 'r') or +áÖò in '¯¬~'))
            getattr(ÄÕÒü, 'set')(c=[áÐè('('), *MOD(Áëý, áØÁ=p)([ÄÕÒü[1], áÖÊ, getattr(áÖò[1][0], 'set')(t=getattr(áÌÐ, 'op')[+áÖò])], ÂÀÇ), áÖÊ, *ÄÕÒü[slice(2, None)], áÐè(')')])
        else:
            getattr(ÄÕÒü, 'set')(c=[áÖò, áÐè('('), *Âøî(getattr(ÄÕÒü, 'c')[slice(1, None)], áÐè(',')), áÐè(')')])
    elif getattr(ÄÕÒü, 't') == '\U000f7e57':
        getattr(ÄÕÒü, 'set')(c=[áÓÕáÓÓáÓßáÓß('þPSH', *ÄÕÒü)])
    elif getattr(ÄÕÒü, 't') == '⍖':
        getattr(ÄÕÒü, 'set')(c=[áÓÕáÓÓáÓßáÓß('þPKE', *ÄÕÒü)])
    elif getattr(ÄÕÒü, 't') == '\U000f7e58':
        getattr(ÄÕÒü, 'set')(c=[áÓÕáÓÓáÓßáÓß('þPOP', *ÄÕÒü)])
    elif getattr(ÄÕÒü, 't') == '𝑎':
        getattr(ÄÕÒü, 'set')(c=[áÓÕáÓÓáÓßáÓß('getattr', *ÄÕÒü)])
    elif getattr(ÄÕÒü, 't') == 'S𝑎':
        getattr(ÄÕÒü, 'set')(c=[áÓÕáÓÓáÓßáÓß('setattr', *ÄÕÒü)])
    elif getattr(ÄÕÒü, 't') == 'S𝑖':
        getattr(ÄÕÒü, 'set')(c=[áÓÕáÓÓáÓßáÓß('setitem', *ÄÕÒü)])
    elif getattr(ÄÕÒü, 't') == 'S𝑣':
        getattr(ÄÕÒü, 'set')(c=[áÓÚáÓåáÓã('()', áÓé(ÄÕÒü[0]), áÐè(':='), ÄÕÒü[1])])
    elif getattr(ÄÕÒü, 't') == 'str':
        (sn := (lambda ÂîÓ: not getattr(getattr(ÂîÓ, 'e'), 'T') and getattr(ÂîÓ, 't') == 'str_sub'))
        (ÄÊÞPSH(MOD(ÐÌÛ, áØÁ=áÍÖ)(getattr(ÄÕÒü, 'c'), sn)), ((Ïß := ÄÊÞPKE(0)[0]), (Ïà := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
        getattr(ÄÕÒü, 'set')(c=[áÐè('("'), *ÁØò(lambda ÂîÓ: getattr(ÂîÓ, 'set')(t=py_esc_str(+ÂîÓ)) if getattr(getattr(ÂîÓ, 'e'), 'T') else áÐè('%s') if sn(ÂîÓ) else ÂîÓ)(ÄÕÒü), áÐè('")'), *([áÐè('%('), *ÂîË(Ïà, áÐè(',')), áÐè(')')] if Ïà else ÂÚü())])
    elif getattr(ÄÕÒü, 't') == 'strb':
        getattr(ÄÕÒü, 'set')(c=[áÐè('\\x%s' % (MOD(ÄÝöì, áØÁ=16 + ÂÞÅÞCAT(2, Ãù))(ÄÝöì(+ÄÕÒü)),))])
    elif getattr(ÄÕÒü, 't') == '𝑣_spec':
        getattr(ÄÕÒü, 'set')(c=[MOD(ÄÕéý, áØÁ=ÂØÙ)(áÓé(getattr(getattr(áÌÐ, 'áÍëÞ_spec'), 'get')(+ÄÕÒü, +ÄÕÒü)), ÄÕÒü)])
    elif getattr(ÄÕÒü, 't') == '𝔸':
        getattr(ÄÕÒü, 'set')(c=[áÐè('*'), *(Âêà(áÓé(ÄÕÒü[0])) if getattr(getattr(ÄÕÒü[0], 'e'), 'T') else Âêà(ÄÕÒü[0]) if getattr(ÄÕÒü[0], 't') == '𝑣' else [áÐè('('), *ÄÕÒü, áÐè(')')])])
    elif getattr(ÄÕÒü, 't') == '𝕂':
        getattr(ÄÕÒü, 'set')(c=[áÐè('**'), *(Âêà(áÓé(ÄÕÒü[0])) if getattr(getattr(ÄÕÒü[0], 'e'), 'T') else Âêà(ÄÕÒü[0]) if getattr(ÄÕÒü[0], 't') == '𝑣' else [áÐè('('), *ÄÕÒü, áÐè(')')])])
    elif getattr(ÄÕÒü, 't') in ÂÛê('𝑣\u2009op_lit\u2009ƒ_𝑣'):
        getattr(ÄÕÒü, 'set')(c=[MOD(ÄÕéý, áØÁ=ÂØÙ)(áÐè(MOD(Áëý, áØÁ=lambda ÂîÓ: ÂîÓ in ÂÕÃ(kwlist, ÂÛê('False\u2009None\u2009True')))(PEV(+ÄÕÒü), ÄÊÞCUR((1,), {}, ì, ÂýÃ, '_'))), ÄÕÒü)])
    elif getattr(ÄÕÒü, 't') == 'qvar':
        getattr(ÄÕÒü, 'set')(c=[MOD(ÄÕéý, áØÁ=ÂØÙ)(áÐè('"%s"' % (PEV(+ÄÕÒü),)), ÄÕÒü)])
    elif getattr(ÄÕÒü, 't') == '𝝀𝑃':
        getattr(ÄÕÒü, 'set')(c=Âøî(ÄÕÒü, áÐè(',')))
    elif getattr(ÄÕÒü, 't') in '𝝀eq\u2009kw_𝕒':
        (ÄÊÞPSH(ÄÕÒü), ÄÊÞPSH(0), ÄÊÞPSH(áÓé(ÄÕÒü[0])), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
        getattr(ÄÕÒü, 'set')(c=Âøî(getattr(ÄÕÒü, 'c'), áÐè('=')))
    elif getattr(ÄÕÒü, 't') == '⊢_dec':
        getattr(ÄÕÒü, 'set')(c=[*([áÐè('@'), ÄÕÒü[0], áÐè('\n')] if +ÄÕÒü[0] else ÂÚü()), áÐè('def '), ÄÕÒü[1] if +ÄÕÒü[1] else áÓé('_'), ÄÕÒü[2] if +ÄÕÒü[2] else áÐè('()'), áÐè(':')])
    elif getattr(ÄÕÒü, 't') == 'stmt_∀':
        getattr(ÄÕÒü, 'set')(c=(lambda ÂîÓ: [*([áÐè('while(')] if ÂîÓ[1] & áÓÒ else [áÐè('for '), ÂîÓ[1], áÐè(' in(')]), ÂîÓ[2], áÐè('):'), *(ÂÚü() if ÂîÓ[3] & áÓÒ else [áÐè('\n'), áÐè(áÓÄ('if not(')), ÂîÓ[3], áÐè('):continue')])])(ÄÕÒü[0]))
    elif getattr(ÄÕÒü, 't') == 'comp_∀':
        getattr(ÄÕÒü, 'set')(c=(lambda ÂîÓ: [áÐè('('), ÂîÓ[0], áÐè(')for '), ÂîÓ[1], áÐè(' in('), ÂîÓ[2], áÐè(')'), *(ÂÚü() if ÂîÓ[3] & áÓÒ else [áÐè('if('), ÂîÓ[3], áÐè(')')])])(ÄÕÒü[0]))
    elif getattr(ÄÕÒü, 't') == 'tern':
        getattr(ÄÕÒü, 'set')(c=[áÐè('('), ÄÕÒü[1], áÐè(')if('), ÄÕÒü[0], áÐè(')else('), ÄÕÒü[2], áÐè(')')])
    elif getattr(ÄÕÒü, 't') == 'lamb':
        getattr(ÄÕÒü, 'set')(c=[áÐè('(lambda '), *Âøî(getattr(ÄÕÒü[0], 'c'), áÐè(',')), áÐè(':'), ÄÕÒü[1], áÐè(')')])
    elif getattr(ÄÕÒü, 't') == 'item':
        getattr(ÄÕÒü, 'set')(c=[ÄÕÒü[0], áÐè(':'), ÄÕÒü[1]])
    elif getattr(ÄÕÒü, 't') == 'slice':
        getattr(ÄÕÒü, 'set')(c=[áÓÕáÓÓáÓßáÓß('slice', *(lambda ÂîÓ: Æå(ÄÕÒü[0]) * [áÓéáÓæ('□')] + ÂîÓ + [áÓéáÓæ('□')] * Æå(ÄÕÒü[-1]))(ÄÔÙù(ÁØò(lambda ÂîÓ: MOD(Âêà, áØÁ=ãÊú(ÂîÓ) - 1)(áÓéáÓæ('□')) if Æå(ÂîÓ[0]) else ÂîÓ)(áÇù(getattr(ÄÕÒü, 'c'), (Æå := (lambda ÂîÓ: getattr(ÂîÓ, 't') == ':')))))))])
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
        (ÄÊÞPSH((lambda x: expand_ast_py(x, PEV), '\n' + áÓÄ())), ((P := ÄÊÞPKE(0)[0]), (d := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
        return getattr(ÄÕÒü, 'set')(c=[P(ÄÕÒü[0]), *ÁØò(lambda ÂîÓ: getattr(ÂîÓ, 'frp')(lambda ÂîÓ: getattr(getattr(ÂîÓ, 'e'), 'T'), lambda ÂîÓ: getattr(ÂîÓ, 'cp')(t=MOD(ÄÔéÄ, áØÁ=getattr(ÂîÓ, 't'))('\n', d)), False, False))(Áÿú(ÂîÊ(ÄÕÒü[slice(1, None)], MOD(ÄÕÍÔ, áØÁ=áÐè('\n'))), P)), áÐè('\n')])
    return getattr(ÄÕÒü, 'set')(c=ÁØò(lambda ÂîÓ: expand_ast_py(ÂîÓ, PEV))(getattr(ÄÕÒü, 'c')))
(ast_clean_e := (lambda ÄÕÒü: getattr(ÄÕÒü, 'frp')(ÃÆë, lambda ÂîÓ: getattr(ÂîÓ, 'set')(e=MOD(ÂÑÖ, áØÁ=None)()(ÄÔÔç(getattr(ÂîÓ, 'e'), lambda ÂîÓ: ÂîÓ[0] in 'Tpρ'))), True, False)))
(ast_add_pos := (Æå := (lambda ÄÕÒü, i=0: (ÄÊÞPSH(getattr(ÄÕÒü, 'e')), ÄÊÞPSH('p'), ÄÊÞPSH((i, MOD(Áëý, áØÁ=getattr(getattr(ÄÕÒü, 'e'), 'T'))(ÄÕÒü, (ÄÊÞCUR((1,), {'áØÁ': i}, ÆÑ, ÂýÃ, ÂÕì(Æå)), lambda ÂîÓ: ãÊú(+ÂîÓ) + i)))), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3][1])))

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
            (ÄÊÞPSH(L[p[0]]), ÄÊÞPSH(slice(p[1], p[3])), ÄÊÞPSH([ÏÁ] * (p[3] - p[1])), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
        else:
            (ÄÊÞPSH(L[p[0]]), ÄÊÞPSH(slice(p[1], None)), ÄÊÞPSH([ÏÁ] * (ãÊú(L[p[0]]) - p[1])), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
            for r in ÄÝöÇ(p[0], p[2]):
                (ÄÊÞPSH(L), ÄÊÞPSH(r), ÄÊÞPSH(ãÊú([ÏÁ] * L[r])), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
            (ÄÊÞPSH(L[p[2]]), ÄÊÞPSH(slice(None, p[3])), ÄÊÞPSH([ÏÁ] * (ãÊú(L[p[2]]) - p[3])), setitem(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]

    def Æå(ÄÕÒü, n=0):
        R(getattr(getattr(ÄÕÒü, 'e'), 'p'), getattr(getattr(ÄÕÒü, 'e'), 'Ïï'))
        for c in ÄÕÒü:
            Æå(c, n + 1)
    Æå(ÄÕÒü)
    return L

def out_to_in_mapper(ÄÕÒü, Ïß, Ïø):
    (ÄÊÞPSH((into_srcmap(ÄÕÒü, Ïø), lines(Ïß))), ((SM := ÄÊÞPKE(0)[0]), (áÖÔ := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
    return lambda p: Âøî(get_region(áÖÔ, Âçß(map_region(SM, p))), '\n')

def ast_to_py(ÄÕÒü, áÖï, get_tree=False, no_rename_vars=False, reparse=False):
    (ÄÕÒü := fill_ÞÄÕÒüÞ_holes_basic(ast_clean_e(expand_ast_py(ÄÕÒü, *([ÄÕÍÔ] if no_rename_vars else ÂÚü())))))
    (pyc := (+ÄÕÒü))
    ÂÕÅ((Æå := (lambda ÄÕÒü: Áÿú(ÂåÔ((ÄÊÞPSH(getattr(ÄÕÒü, 'e')), ÄÊÞPSH('Ïï'), ÄÊÞPSH(getattr(getattr(ÄÕÒü, 'e'), 'pop')('p')), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3] if 'p' in getattr(ÄÕÒü, 'e') else None, ÄÕÒü), Æå))), ÄÕÒü)
    ast_add_pos(ÄÕÒü)
    if get_tree:
        return ÄÕÒü
    if not reparse:
        return pyc
    import ast
    try:
        return getattr(ast, 'unparse')(getattr(ast, 'parse')(pyc))
    except Exception as Ïã:
        Âçß('Code:\n%s' % (linewnum(pyc, d=175, s=ÄÊÞCUR((1,), {'fg': '915'}, Åøáüì, ÂýÃ)),))
        ÂùÆ(False, 'Error in python reparsing! %s' % (Ïã,))
(__exports__ := ÂÛê('ast_to_py\u2009PEV\u2009VEP'))
from sys import stdin as ÂÐðáÐâ, argv as áÑË
from time import time as áÏÖ
__ÞÄÊÞIMPORT__('text_format', globals())
__ÞÄÊÞIMPORT__('to_ast', globals())
__ÞÄÊÞIMPORT__('ast_to_py', globals())
(COMPILER := 'python3 "/home/ganer/Projects/Moon_BETA/STAGES/BOOTSTRAP_α.py"')
(BINARY := 'python3')
(BASE := áÌî('/home/ganer/Projects/Moon_BETA/NewMoon'))
(CODE := ÐØó(ð(BASE, 'Libraries/Compiler/main.☾')))
(DEST := ÐÌü(getattr(áÌî(ð(BASE, '../STAGES/BOOTSTRAP_β.py')), 'resolve')))
(TMP := mkd(áÌî('/tmp/β')))
(áÑð := ÂÑÖ()(show_preast=False, show_ast=False, show_py_ast=False, dbg_parser=0))
(mod_files := ÂÚü())
(áÌë := (lambda x: ÂåÔ(getattr(mod_files, 'append')(x), x)))
(tof := MOD(ÁØò(lambda ÂîÓ: ÐÌü(getattr(ð(BASE, '%s.☾' % (ÂîÓ,)), 'resolve')))))
(code_files := [*ÄÝöÞ(ÐØó(ð(BASE, 'builtins'))), MOD(ÄÕéý, áØÁ=áÌë)('Libraries/text_format'), MOD(ÄÕéý, áØÁ=áÌë)('Libraries/𝐍'), MOD(ÄÕéý, áØÁ=áÌë)('Libraries/peggle2/main'), MOD(ÄÕéý, áØÁ=áÌë)('Libraries/peggle2/rgx_golfatron'), MOD(ÄÕéý, áØÁ=áÌë)('Libraries/peggle2/gram_tools'), 'Libraries/Compiler/generate_operators', 'Libraries/Compiler/op_table', 'Libraries/Compiler/node_types', 'Libraries/Compiler/tree', 'Libraries/Compiler/tree_txt', 'Libraries/Compiler/expr', 'Libraries/Compiler/lambdas', 'Libraries/Compiler/rewriters', 'Libraries/Compiler/to_ast', 'Libraries/Compiler/ast_to_py'])
(ÄÊÞPSH(Áÿú([code_files, mod_files], tof)), ((code_files := ÄÊÞPKE(0)[0]), (mod_files := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
(show := (lambda x, y=True, d=100: MOD(Áëý, áØÁ=y)(BOX(linewnum(x, d=d, s=ÄÊÞCUR((1,), {'fg': '915'}, Åøáüì, ÂýÃ))), lambda ÂîÓ: ÂåÔ(Âçß(ÂîÓ), x))))
(to_py := (lambda áÖï, *áÑË, **áÑÕ: lambda *áÑË, **áÑÕ: ast_to_py(*áÑË, áÖï=áÖï, **áÑÕ)))
(moon_to_py := (lambda áÖï, áÖÝ={}, áÏè={}: to_py(áÖï)(to_ast(áÖï, **áÖÝ), **{'reparse': True, **áÏè})))

def moon_to_py_debug(áÖï, show_preast=True, show_ast=True, show_py_ast=False, **áÑÕ):
    (ÄÕÒü := to_ast(áÖï, dbg_show_gram_tree=show_preast, **áÑÕ))
    if show_ast:
        áÍñáÍñ(ÄÕÒü, 'AST')
    if show_py_ast:
        áÍñáÍñ(to_py(áÖï)(ÐÌü(getattr(ÄÕÒü, 'cpr')), get_tree=True, no_rename_vars=True), 'PY AST')
    (p := show(to_py(áÖï)(ÐÌü(getattr(ÄÕÒü, 'cpr')), no_rename_vars=True), False))
    Âçß(padc(' CODE ', p, '─') + '\n' + p)
    Âçß(show((pyc := to_py(áÖï)(ÐÌü(getattr(ÄÕÒü, 'cpr')), reparse=True)), False))
    return pyc

def wrap_as_module_dumb(áÖï, name=None):
    return '\n# %s\nexec(%s,__TMP:=globals().copy())\nfor k,v in __TMP.get("__EXPORTS__",{}).items():globals()[k]=v\n' % (name, repr(áÖï))
(reewrap := (lambda x, y: '\n__file__=%s\n%s' % (repr(ÂÕÅ(ÁÜÙ, x)), y)))

def make_header():
    (áØÂ := ÐÌü(áÏÖ))
    (compile := (lambda x, y: ÂåÔ(ÐÌü(getattr((p := getattr(subprocess, 'Popen')(ÂÛê("bash\u2009-c\u2009%s o '%s' '%s'" % (COMPILER, x, y)))), 'wait')), getattr(p, 'returncode'))))
    (pile := (lambda x: (MOD(ÄÕÍÔ, áØÁ=0) if ÐÌü(getattr((y := ÐÌü(getattr(áÌî(ð(TMP, 'compiled_%s.py' % (MOD(ÄÔéÄ, áØÁ=ÂÕÅ(ÁÜÙ, x))('/', 2 * '$'),))), 'resolve'))), 'is_file')) and x in code_files else compile(x, y), y, x)))
    (h := Âøî(ÁØò(lambda ÂîÓ: ÂåÔ(ÂùÆ(not ÐÌü(ÂîÓ[0])), (lambda ÂîÒ: wrap_as_module_dumb(ÂîÒ, '%s⟶%s' % (ÂîÓ[2], ÂîÓ[1])) if ÂîÓ[2] in mod_files else ÂîÒ)(reewrap(ÂîÓ[2], ÂÕÅ(ÐØó, ÂîÓ[1])))))(Áÿú(code_files, pile)), '\n'))
    Âçß('Head compile took: %s' % (ÐÌü(áÏÖ) - áØÂ,))
    return h
(ÄÊÞPSH((áÑË[slice(1, None)], ÁØã)), ((áÒø := ÄÊÞPKE(0)[0]), (pre := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
if ãÊú(áÒø) >= 2:
    if áÒø[0] == 'o':
        Âçß('Compiling %s…' % (áÒø[1],))
        ÐØì(áÒø[2], ÂÞÅÞCAT(ÂÞÅÞCAT(áÒø[1], ÐØó), moon_to_py))
        Âçß('Done - wrote %s to %s' % (áÒø[1], áÒø[2]))
        ÐÌü(exit)
    if áÒø[0] == 'e':
        ÂåÔ(ÁØò(lambda ÂîÓ: Âçß('%s ⟶ %s' % (ÂîÓ, PEV(ÂîÓ))))(áÒø[slice(1, None)]), ÐÌü(exit))
    elif áÒø[0] == 'd':
        ÂåÔ(ÁØò(lambda ÂîÓ: Âçß('%s ⟶ %s' % (ÂîÓ, VEP(ÂîÓ))))(áÒø[slice(1, None)]), ÐÌü(exit))
    if áÒø[0] == 'e':
        ÂåÔ(ÁØò(lambda ÂîÓ: Âçß('%s ⟶ %s' % (ÂîÓ, PEV(ÂîÓ))))(áÒø[slice(1, None)]), ÐÌü(exit))
    elif áÒø[0] == 'd':
        ÂåÔ(ÁØò(lambda ÂîÓ: Âçß('%s ⟶ %s' % (ÂîÓ, VEP(ÂîÓ))))(áÒø[slice(1, None)]), ÐÌü(exit))
    elif áÒø[0] == 'f':
        (code := ÐØó(áÒø[1]))
    elif áÒø[0] == 'F':
        (code := ÐØó(áÒø[1]))
        (pre := ÐÌü(make_header))
    else:
        (code := Âøî(áÒø[slice(1, None)], ' '))
    if áÒø[0] in 'rx':
        (ÄÊÞPSH(áÑð), ÄÊÞPSH('show_preast'), ÄÊÞPSH((ÄÊÞPSH(áÑð), ÄÊÞPSH('show_ast'), ÄÊÞPSH(True), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]), setattr(ÄÊÞPKE(2), ÄÊÞPKE(1), ÄÊÞPKE(0)), ÄÊÞDEL(3))[3]
    if áÒø[0] == 'x':
        (pre := ÐÌü(make_header))
    Âçß('Using code:\n%s' % (linewnum(code, d=175, s=ÄÊÞCUR((1,), {'fg': '915'}, Åøáüì, ÂýÃ)),))
else:
    if ãÊú(áÒø) == 1 and áÒø[0] == 'D':
        ÂåÔ(Âçß(VEP(ÐÌü(getattr(ÂÐðáÐâ, 'read')))), ÐÌü(exit))
    (ÄÊÞPSH((ÐÌü(make_header), reewrap(áÒø[0], ÂÞÅÞCAT(áÒø[0], ÐØó)) if áÒø else CODE)), ((pre := ÄÊÞPKE(0)[0]), (code := ÄÊÞPKE(0)[1])), ÄÊÞDEL(1))[1]
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
    (r := ÂåÔ(ÐÌü(getattr((p := getattr(subprocess, 'Popen')(ÂÛê('%s\u2009-u\u2009%s' % (BINARY, DEST)))), 'wait')), getattr(p, 'returncode')))
    Âçß('Execution took: %s' % (ÐÌü(áÏÖ) - áØÂ,))
    if r:
        Âçß(Åøáüì('%s: ERROR %s! ' % (__file__, r), 'f33'))