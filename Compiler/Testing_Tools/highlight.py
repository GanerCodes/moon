import os, sys, inspect, traceback, threading
from os import environ as env
from sys import stdout, stderr, path as syspath, exit, argv as Üíâ
from math import *
from site import getsitepackages
from json import dumps as jdumps__, loads as jloads__
from cmath import *
from types import UnionType
from random import shuffle, choice, uniform, randint
from pathlib import Path as Üñú
from tempfile import gettempdir
from builtins import setattr as setattr_
from operator import __gt__, __lt__, __ge__, __le__, rshift, lshift, getitem, setitem, delitem
from itertools import chain, filterfalse, product, accumulate, zip_longest
from functools import partial as MOD, reduce, cache
getattr(syspath, 'extend')(getsitepackages())
(moon_dir := Üñú('..'))
del (getsitepackages, factorial, e, pi, tau, sqrt, cbrt, pow)
(þSTK := [])
(þPSH := (lambda x: getattr(þSTK, 'append')(x) or x))
(þPKE := (lambda x: þSTK[-1 - x]))
(þPOP := (lambda x=0: getattr(þSTK, 'pop')(-1 - x)))
(þDEL := (lambda x: getattr(þSTK, '__delitem__')(slice(-x, None))))
(ûäÒCAT := (lambda x, y: y(x) if callable(y) else x * y))

def þCUR(Üñß, Üñä, *ÜðÂ):

    def ñäÀ(*Üñî):
        if len(Üñî) < len(Üñß):
            return lambda *Üíâ: ñäÀ(*Üñî, *Üíâ)
        (þPSH(([*ÜðÂ], {**Üñä})), ((Üèà := þPKE(0)[0]), (ÜèÔ := þPKE(0)[1])), þDEL(1))[1]
        for k, v in zip(Üñß, Üñî):
            (þPSH(Üèà if isinstance(k, int) else ÜèÔ), þPSH(k), þPSH(v), setitem(þPKE(2), þPKE(1), þPKE(0)), þDEL(3))[3]
        return Üèà[0](*Üèà[slice(1, None)], *Üñî[slice(len(Üñß), None)], **ÜèÔ)
    return ñäÀ()
(setattr := (lambda x, y, z: setattr_(x, y, z) or z))
(þPSH((Exception, object, dict, bool, list, tuple, set, str, int, float, bytes)), ((ÜñÎ := þPKE(0)[0]), (ÜñÄ := þPKE(0)[1]), (ÜñÏ := þPKE(0)[2]), (ÜñÑ := þPKE(0)[3]), (ÜñÇ := þPKE(0)[4]), (Üño := þPKE(0)[5]), (ÜñÀ := þPKE(0)[6]), (üäμ := þPKE(0)[7]), (ÜñÊ := þPKE(0)[8]), (ÜñÍ := þPKE(0)[9]), (Üðû := þPKE(0)[10])), þDEL(1))[1]
(üçð := '')
(þPSH((1 / 2, 1 / 3, 1 / 4, 1 / 5, 1 / 6, 1 / 7, 1 / 8, 1 / 9, 1 / 10, 2 / 3, 2 / 5, 2 / 7, 2 / 9, 3 / 4, 3 / 5, 3 / 7, 3 / 8, 3 / 10, 4 / 5, 4 / 7, 4 / 9, 5 / 6, 5 / 7, 5 / 8, 5 / 9, 6 / 7, 7 / 8, 7 / 9, 7 / 10, 8 / 9, 9 / 10, 0, 1 / 100)), ((úú := þPKE(0)[0]), (ûïÕ := þPKE(0)[1]), (úû := þPKE(0)[2]), (ûïÓ := þPKE(0)[3]), (ûïÏ := þPKE(0)[4]), (ûïÙ := þPKE(0)[5]), (ûïÍ := þPKE(0)[6]), (ûïØ := þPKE(0)[7]), (ûïÖ := þPKE(0)[8]), (ûïÔ := þPKE(0)[9]), (ûïÒ := þPKE(0)[10]), (ùìöÝ := þPKE(0)[11]), (ùìöØ := þPKE(0)[12]), (úù := þPKE(0)[13]), (ûïÑ := þPKE(0)[14]), (ùìöÜ := þPKE(0)[15]), (ûïÌ := þPKE(0)[16]), (ùìöÈ := þPKE(0)[17]), (ûïÐ := þPKE(0)[18]), (ùìöÛ := þPKE(0)[19]), (ùìöÌ := þPKE(0)[20]), (ûïÎ := þPKE(0)[21]), (ùìöÚ := þPKE(0)[22]), (ûïË := þPKE(0)[23]), (ùìöÕ := þPKE(0)[24]), (ùìöÙ := þPKE(0)[25]), (ûïÊ := þPKE(0)[26]), (ùìöÔ := þPKE(0)[27]), (ùìöÇ := þPKE(0)[28]), (ùìöÓ := þPKE(0)[29]), (ùìöÆ := þPKE(0)[30]), (ûîß := þPKE(0)[31]), (ùìöÅ := þPKE(0)[32])), þDEL(1))[1]
(þPSH((3.141592653589793, 2.718281828459045)), ((íÝ := þPKE(0)[0]), (ûðå := þPKE(0)[1])), þDEL(1))[1]
(þPSH((inf, complex(0, 1), ûäÒCAT(2, íÝ), ûäÒCAT(úú, íÝ), ûäÒCAT(úû, íÝ), ûäÒCAT(ûïÍ, íÝ))), ((ûìÄ := þPKE(0)[0]), (úÆ := þPKE(0)[1]), (íÙ := þPKE(0)[2]), (ùìòü := þPKE(0)[3]), (ùìòû := þPKE(0)[4]), (ùìòú := þPKE(0)[5])), þDEL(1))[1]
(þPSH((-ûìÄ, -úÆ, -íÙ, -íÝ, -ùìòü, -ùìòû, -ùìòú, -ûðå)), ((ùìüñ := þPKE(0)[0]), (ùìüð := þPKE(0)[1]), (ùìüî := þPKE(0)[2]), (ùìüí := þPKE(0)[3]), (ùìüì := þPKE(0)[4]), (ùìüë := þPKE(0)[5]), (ùìüê := þPKE(0)[6]), (ùìüï := þPKE(0)[7])), þDEL(1))[1]
(ûîè := (2 ** 3 ** 4))
(þPSH((lambda *Üíâ: Üíâ[0], lambda *Üíâ: Üíâ[-1])), ((ûÜÀ := þPKE(0)[0]), (ûÜÊ := þPKE(0)[1])), þDEL(1))[1]

class Named:
    (þPSH((lambda ÜíÎ, s: ûÜÊ((þPSH(s), þPSH(ÜíÎ), þPSH('s'), setattr(þPKE(1), þPKE(0), þPKE(2)), þDEL(3))[3], None), lambda ÜíÎ: getattr(ÜíÎ, 's'))), ((__init__ := þPKE(0)[0]), (__repr__ := þPKE(0)[1])), þDEL(1))[1]
(ûäÒ := (NULL := Named('␀')))
(þPSH((Named('\U000f0b88'), Named('\U000f18e9'), Named('⬤'))), ((ùôÜö := þPKE(0)[0]), (ùóäç := þPKE(0)[1]), (ûÄô := þPKE(0)[2])), þDEL(1))[1]

class ûðÕ:
    None
(ûðÆ := ÜñÊ)
(ûðÍ := (ÜñÍ | ûðÆ))
(ûðê := complex)
(Úøê := len)
(üoî := (lambda öÝ, *Üíâ, **ÜíÖ: lambda *Üíâ, **ÜíÖ: öÝ(Üíâ[1], Üíâ[0], *Üíâ[slice(2, None)], **ÜíÖ) if Úøê(Üíâ) >= 2 else öÝ(*Üíâ, **ÜíÖ)))
(ùôÍä := (lambda *Üíâ, Üçò=ûäÒ: (Üíâ[0] if Üçò is ûäÒ else Üçò) if Üíâ else (lambda *Üíâ: Üíâ[0] if Üíâ else ùôÍä) if Üçò is ûäÒ else lambda: Üçò))
(CUR := (lambda öÝ, *Üèà, **ÜèÔ: öÝ(*Üèà, **ÜèÔ) if Úøê(Üèà) >= 2 else lambda *Üèß, **ÜèÓ: CUR(öÝ, *Üèà, *Üèß, **ÜèÔ | ÜèÓ)))
(CURR := (lambda öÝ, *Üèà, **ÜèÔ: öÝ(*Üèà, **ÜèÔ) if Úøê(Üèà) >= 2 else lambda *Üèß, **ÜèÓ: CUR(öÝ, Üèß[0], *Üèà, *Üèß[slice(1, None)], **ÜèÔ | ÜèÓ)))
(üçá := (üçÌ := (lambda öÝ: lambda Üçí, *Üèà, **ÜèÔ: [Üìï for v in Üçí if (Üìï := öÝ(v, *Üèà, **ÜèÔ)) is not ùôÜö])))
(üçÔÞüçÏ := (lambda öÝ: öÝ))
(üçáÞüçÏ := (lambda öÝ: lambda Üçí, Üçì, *Üèà, **ÜèÔ: [Üìï for x in Üçí if (Üìï := öÝ(x, Üçì, *Üèà, **ÜèÔ)) is not ùôÜö]))
(üçÔÞüçÌ := (lambda öÝ: lambda Üçí, Üçì, *Üèà, **ÜèÔ: [Üìï for y in Üçì if (Üìï := öÝ(Üçí, y, *Üèà, **ÜèÔ)) is not ùôÜö]))
(üçáÞüçÌ := (lambda öÝ: lambda Üçí, Üçì, *Üèà, **ÜèÔ: [Üìï for x, y in ùóöù(Üçí, Üçì) if (Üìï := öÝ(x, y, *Üèà, **ÜèÔ)) is not ùôÜö]))
(þPSH((lambda x, y: (False if y else x) if x else y, lambda x, y: (y if y else False) if x else x if y else True)), ((ùìòä := þPKE(0)[0]), (ùìòâ := þPKE(0)[1])), þDEL(1))[1]
(ûëû := (ûÈÊ := (lambda x, y: x or y)))
(ùìòã := (ùìòÜ := (lambda x, y: not (x or y))))
(ûëü := (ûÈË := (lambda x, y: x and y)))
(ùìòö := (ùìòÛ := (lambda x, y: (False if y else x) if x else y if y else True)))
(þPSH((lambda x, y: __lt__, __gt__, __le__, __ge__)), ((μ := þPKE(0)[0]), (üý := þPKE(0)[1]), (ûêý := þPKE(0)[2]), (ûêü := þPKE(0)[3])), þDEL(1))[1]
(þPSH((lambda x, y: x == y, lambda x, y: x != y)), ((ûëo := þPKE(0)[0]), (ûëÀ := þPKE(0)[1])), þDEL(1))[1]
(þPSH((lambda x, y: gcd(x, y) == x, lambda x, y: gcd(x, y) != x)), ((ûìo := þPKE(0)[0]), (ûìμ := þPKE(0)[1])), þDEL(1))[1]
(þPSH((lambda x, y: x in y, lambda x, y: x not in y)), ((ûìÛ := þPKE(0)[0]), (ûìÚ := þPKE(0)[1])), þDEL(1))[1]
(þPSH((lambda x, y: y in x, lambda x, y: y not in x)), ((ûìØ := þPKE(0)[0]), (ûìÖ := þPKE(0)[1])), þDEL(1))[1]
(þPSH((lambda x, y: getattr({*x}, 'issubset')({*y}), lambda x, y: getattr({*y}, 'issubset')({*x}))), ((ûêÝ := þPKE(0)[0]), (ûêÜ := þPKE(0)[1])), þDEL(1))[1]
(þPSH((lambda x, y: not ûêÝ(x, y), lambda x, y: not ûêÜ(x, y))), ((ûêÛ := þPKE(0)[0]), (ûêÚ := þPKE(0)[1])), þDEL(1))[1]
(þPSH((lambda x, y: getattr((íí := {*x}), 'issubset')((íì := {*y})) and íí != íì, lambda x, y: getattr((íí := {*y}), 'issubset')((íì := {*x})) and íí != íì)), ((ûêÔ := þPKE(0)[0]), (ûêÓ := þPKE(0)[1])), þDEL(1))[1]
(þPSH((lambda x, y: not ûêÔ(x, y), lambda x, y: not ûêÓ(x, y))), ((ùìóÖ := þPKE(0)[0]), (ùìóÕ := þPKE(0)[1])), þDEL(1))[1]
(ùìóá := (lambda x, y: ûìÌ(ûëù(x, y), ûëú(x, y))))
(ûëù := (lambda x, y: {*x} | {*y} if üçÜ(x, ÜñÀ) else [*x, *[z for z in y if z not in x]]))
(ûëú := (lambda x, y: {*x} & {*y} if üçÜ(x, ÜñÀ) else [z for z in x if z in y]))
(ûìÌ := (lambda x, y: x - {*y} if üçÜ(x, ÜñÀ) else [z for z in x if z not in y]))
(ûÉØ := (lambda Üçí=ûäÒ, Üçì=ûäÒ, Üçò=ûäÒ: üÁo(product(*([Üçí] * Üçò if Üçì is ûäÒ and Üçò is not ûäÒ else (Üçí if Üçì is ûäÒ else [Üçí, Üçì]) * (1 if Üçò is ûäÒ else Üçò))), ÜñÇ)))
(ûêÀ := (lambda *Üíâ, Üçò=1: (öÝ := (lambda *Üíâ, n=1, r=[]: (lambda ûÒÔ: üÁo(ûÒÔ[0], lambda x: öÝ(*ûÒÔ[slice(1, None)], r=r + [Üçí]) if Úøê(ûÒÔ) > 1 else r + [Üçí]))(Üíâ * n)))(*Üíâ, n=Üçò)))
(þPSH((lambda x, y: x % y, lambda x, y: x // y)), ((Õ := þPKE(0)[0]), (úøï := þPKE(0)[1])), þDEL(1))[1]
(þPSH((lambda x, y: x is y, lambda x, y: x is not y)), ((ûëÜ := þPKE(0)[0]), (ûëÚ := þPKE(0)[1])), þDEL(1))[1]
(þPSH((lambda x: ~x, lambda x, y: x @ y)), ((ûû := þPKE(0)[0]), (üû := þPKE(0)[1])), þDEL(1))[1]
(þPSH((lambda x, y: x | y, lambda x, y: x & y, lambda x, y: x ^ y)), ((ûý := þPKE(0)[0]), (Ô := þPKE(0)[1]), (üÛ := þPKE(0)[2])), þDEL(1))[1]
(þPSH((lshift, rshift)), ((ûÆü := þPKE(0)[0]), (ûÆû := þPKE(0)[1])), þDEL(1))[1]
(þPSH((lambda x, y: x ** y, lambda x: not x, lambda Üçí, Üçò=ûäÒ: lambda x: MOD(Í, Üçò=Üçò)(Üçí))), ((ûèØ := þPKE(0)[0]), (ûÊ := þPKE(0)[1]), (ûÇ := þPKE(0)[2])), þDEL(1))[1]
(üÀó := (lambda Üçí: ùìóî(üÀó(ùìóî(Üçí))) if üçÜ(Üçí, ÜñÊ) else Üçí[slice(None, None, -1)] if üçÜ(Üçí, üäμ | ÜñÇ | Üño) else getattr(Üçí, '__reversed__')() if hasattr(Üçí, '__reversed__') else [*Üçí][slice(None, None, -1)]))
(ùìóí := (lambda Üçí=ûäÒ, Üçò=ûäÒ: chr(Üçí) if üçÜ(Üçí, ÜñÊ) else ord(Üçí) if üçÜ(Üçí, üäμ) and (Úøê(Üçí) == 1 and Üçò is not ÜñÇ) else MOD(üÒê, Üçò=üçÜ(Üçí[0], ÜñÊ))(üÁo(Üçí, ùìóí), ûÉÃ)))
(ûæë := (lambda Üçí, Üçò=ûäÒ: (MOD(ûæë, Üçò='\u205f\u2009')(Üçí) if '\u205f' in Üçí else MOD(ûæë, Üçò='\u2009')(Üçí)) if Üçò is ûäÒ else MOD(üÒê, Üçò=Úøê(Üçò) > 1)(getattr(Üçí, 'split')(Üçò[0]), MOD(üçá(lambda ûÒÔ: MOD(ûæë, Üçò=Üçò[slice(1, None)])(ûÒÔ))))))
(ûÜä := (lambda Üçí, Üçò=ûäÒ: ùìôð(üÁo(ùìôð(Üçí), MOD(ûÜä, Üçò=Üçò))) if MOD(üçÜ, Üçò=ûëÜ)(Üçí, ûðê) else ÜñÊ(round(Üçí)) if Üçò is ûäÒ else round(Üçí, Üçò)))
(þPSH((floor, ceil)), ((ûÅÅ := þPKE(0)[0]), (ûÅÆ := þPKE(0)[1])), þDEL(1))[1]
(þPSH((lambda Üçí: getattr(Üçí, 'real'), lambda Üçí: getattr(Üçí, 'imag'))), ((ùìôñ := þPKE(0)[0]), (ùìôò := þPKE(0)[1])), þDEL(1))[1]
(ùìôð := (lambda Üçí: ûðê(*Üçí) if üçÜ(Üçí, ÜñÇ | Üño) else (ùìôñ(Üçí), ùìôò(Üçí))))
(ûçÏ := (lambda Üçí, Üçò=ûäÒ: MOD(ùóöù, Üçò=Üçò)(Üçí)))
(ûÅÔ := getattr(üäμ, 'strip'))
(ûôÌ := (lambda Üçí, Üçì: [*range(Üçí, Üçì)]))
(ûìÏ := (lambda Üçí=ûäÒ, Üçì=ûäÒ, Üçò=ûäÒ: (MOD(Í, Üçò=Üçò)(Üçí), MOD(Ï, Üçò=Üçò)(Üçí)) if Üçì is ûäÒ else (MOD(Í, Üçò=Üçò)(Üçí, Üçì), MOD(Ï, Üçò=Üçò)(Üçí, Üçì))))
(ûÅ := (lambda Üçí=ûäÒ, Üçì=ûäÒ, Üçò=ûäÒ: (MOD(Ï, Üçò=Üçò)(Üçí), MOD(Í, Üçò=Üçò)(Üçí)) if Üçì is ûäÒ else (MOD(Ï, Üçò=Üçò)(Üçí, Üçì), MOD(Í, Üçò=Üçò)(Üçí, Üçì))))

def Ï(Üçí=ûäÒ, Üçì=ûäÒ, Üçò=ûäÒ):
    (v := (+Üçí if Üçì is ûäÒ else Üçí + Üçì))
    return v if Üçò is ûäÒ else v % MOD(üÒê, Üçò=Üêù)(Üçò, Úøê)

def Í(Üçí=ûäÒ, Üçì=ûäÒ, Üçò=ûäÒ):
    (v := (-Üçí if Üçì is ûäÒ else Üçí - Üçì))
    return v if Üçò is ûäÒ else v % MOD(üÒê, Üçò=Üêù)(Üçò, Úøê)

def ûéØ(Üçí=ûäÒ, Üçì=ûäÒ, Üçò=ûäÒ):
    return Üçí * Üçì if Üçò is ûäÒ else Üçí * Üçì % MOD(üÒê, Üçò=Üêù)(Üçò, Úøê)

def úa(Üçí=ûäÒ, Üçì=ûäÒ, Üçò=ûäÒ):
    return Üçí / Üçì if Üçò is ûäÒ else Üçí / Üçì % MOD(üÒê, Üçò=Üêù)(Üçò, Úøê)

def úøï(Üçí=ûäÒ, Üçì=ûäÒ, Üçò=ûäÒ):
    return Üçí // Üçì if Üçò is ûäÒ else MOD(ûèØ, Üçò=-MOD(üÒê, Üçò=Üêù)(Üçò, Úøê))(Üçí, Üçì)

def ûèØ(Üçí=ûäÒ, Üçì=ûäÒ, Üçò=ûäÒ):
    return Üçí ** Üçì if Üçò is ûäÒ else pow(Üçí, Üçì, MOD(üÒê, Üçò=Üêù)(Üçò, Úøê))

def íÏý(öÝ, *Üíâ, **ÜíÖ):
    if Üêü(öÝ):
        return öÝ(*Üíâ, **ÜíÖ)
    if Üêù(öÝ):
        for x in öÝ:
            None
        return öÝ
    ûÈí(False, '%sis not iterable or callable.' % (öÝ,))

def ûéÝ(ÜñÕ, Üçò=True):
    for Üçò in ÜñÕ:
        if not Üçò:
            break
    return Üçò

def ûéÜ(ÜñÕ, Üçò=False):
    for Üçò in ÜñÕ:
        if Üçò:
            break
    return Üçò

class Ticker:
    (__slots__ := ('i',))
    (__init__ := (lambda ÜíÎ, i: ûÜÊ((þPSH(ÜíÎ), þPSH('i'), þPSH(i), setattr(þPKE(2), þPKE(1), þPKE(0)), þDEL(3))[3], None)))
    (__call__ := (lambda ÜíÎ: ûÜÊ((þPSH(ÜíÎ), þPSH('i'), þPSH(getattr(þPKE(1), þPKE(0))), þPSH(þPKE(0) - 1), setattr(þPKE(3), þPKE(2), þPKE(0)), þDEL(4))[4], ÜíÎ)))
    (__bool__ := (lambda ÜíÎ: not getattr(ÜíÎ, 'i')))
    (__repr__ := (lambda ÜíÎ: 'Ticker[i=%s]' % (getattr(ÜíÎ, 'i'),)))

class TimerState:
    (__init__ := (lambda ÜíÎ, Üëä: ûÜÊ((þPSH(ÜíÎ), þPSH('Üëä'), þPSH(Üëä), setattr(þPKE(2), þPKE(1), þPKE(0)), þDEL(3))[3], None)))
    (__bool__ := (lambda ÜíÎ: getattr(getattr(ÜíÎ, 'Üëä'), 's')))
    (__call__ := (lambda ÜíÎ: getattr(getattr(ÜíÎ, 'Üëä'), 'r') if ÜíÎ else íÏý(getattr(getattr(getattr(ÜíÎ, 'Üëä'), 'r'), 'copy'))))
    (__repr__ := (lambda ÜíÎ: 'Timer[%s; %ss; %s; %s Remaining loops]=%s' % ('ID'[getattr(getattr(ÜíÎ, 'Üëä'), 'y') >= 0], ûÅê(getattr(getattr(ÜíÎ, 'Üëä'), 'y')), ûæë('Running\u2009Completed')[ûìÊ(ÜñÑ, ÜíÎ)], getattr(getattr(ÜíÎ, 'Üëä'), 'n'), getattr(getattr(ÜíÎ, 'Üëä'), 'r'))))
(tmp := {'ᴍ': 'üÁo', 'ꟿ': 'ññÑ', 'ſ': 'öñ', 'Ϝ': 'íÀ', '\U000f0233': 'ùõÄØ', '\U000f0232': 'ùõÄÙ', '\ueb86': 'íÐÝ', '\U000f04bc': 'ùôúû', '\U000f04bd': 'ùôúú', 'ᙎ': 'üÝö', 'ᙡ': 'üÝã', 'ᗢ': 'üàæ', 'ᙧ': 'üÝÜ', '⊚': 'ûêÄ', '⊜': 'ûêÂ', '🟕': 'ÚÙç', '🟖': 'ÚÙæ', '⊛': 'ûêÃ', '⍟': 'ûæú', '○': 'ûÛú', '⍜': 'ûæý', '\U000f0b2b': 'ùôßÕ', '\U000f0b29': 'ùôßØ', '\uf071': 'ìýÉ', '\U000f0536': 'ùôøý', '\uea6c': 'íÕÀ', '\U000f147c': 'ùóöù', '\U000f7e45': 'ùìôÅ', '⪡': 'ûÆü', '⪢': 'ûÆû', '\U000f0e35': 'ùôÐó', '\U000f0e37': 'ùôÐñ', '⤉': 'ûÍá', '⤈': 'ûÍâ', '⟷': 'ûÑü', '\U000f7e4c': 'ùìôµ', '\U000f7e4d': 'ùìôª', '\U000f7e4e': 'ùìóý', '\U000f7e39': 'ùìôÑ', '\U000f7e3a': 'ùìôÐ', '\U000f7e38': 'ùìôÒ', '\U000f7e3b': 'ùìôÏ', '⨝': 'ûÉÃ', '⟕': 'ûÒß', '⟖': 'ûÒÝ', '⟗': 'ûÒÜ', '⫰': 'ûÅê', '⫯': 'ûÅë', '\U000f7e52': 'ùìóù', '\U000f7e53': 'ùìóø', '\U000f7e54': 'ùìóö', '\U000f7e55': 'ùìóõ', '\U000f7e56': 'ùìóô'})
(ENC := 'ýüûúùøöõôóòñðïîíìëêéèçæåäãâáàßÝÜÛÚÙØÖÕÔÓÒÑÐÏÎÍÌËÊÉÈÇÆÅÄÃÂÁÀºµª')
(abcABC123 := ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789þ' + ENC))
(val := (lambda ûÒÔ: ùìóí(ûÒÔ) < 127 and ûÒÔ not in '~!@#$%^&*-=+\\|,./<>?' or ûÒÔ == 'þ'))
(PEV := (lambda ûÒÔ: ûÉÃ(üçá(lambda ûÒÔ: ûÒÔ if val(ûÒÔ[0]) else ûÉÃ(üçá(lambda ûÒÔ: ùìóî(ùìóí(ûÒÔ), Úøê(ENC), C=ENC))(ûÒÔ), 'Þ'))(Üöê(ûÒÔ, val)))))
(VEP_ := (lambda ûÒÔ: ûÉÃ(üçá(lambda ûÒÔ: ûÒÔ if val(ûÒÔ[0]) else ûÉÃ(üçá(lambda ûÒÔ: ùìóí(ùìóî(ûÒÔ, C=ENC)) if ûêÝ(ûÒÔ, ENC) else ûÒÔ)(ùìóý(ûÒÔ, 'Þ'))))(Üöê(ûÒÔ, lambda ûÒÔ: ûÒÔ in ENC)))))
(VEP := CURR(lambda ûÒÔ, ûÒÕ: ûÉÃ(üçá(lambda ûÒÔ: VEP_(ûÒÔ) if ûêÝ(ûÒÔ, ûÒÕ) else ûÒÔ)(Üöê(ûÒÔ, lambda ûÒÔ: ûÒÔ in ûÒÕ))), abcABC123 + ENC + 'þ'))

def OPWRAP_(*ÜèÇ):

    def R(öÝ):
        for x in ÜèÇ:
            (þPSH(globals()), þPSH(tmp[x] if x in tmp else PEV(x)), þPSH(MOD(öÝ, x)), setitem(þPKE(2), þPKE(1), þPKE(0)), þDEL(3))[3]
    return R
(þPSH((callable, lambda x: hasattr(x, '__iter__'))), ((Üêü := þPKE(0)[0]), (Üêù := þPKE(0)[1])), þDEL(1))[1]

def Üêú(x):
    try:
        return hash(x)
    except:
        pass
    return False
(Üñâ := (lambda x, y='utf-8', *Üíâ, **ÜíÖ: getattr(x, 'encode')(y, *Üíâ, **ÜíÖ) if üçÜ(x, üäμ) else getattr(x, 'decode')(y, *Üíâ, **ÜíÖ)))

class úýÓ(ÜñÊ):
    (__new__ := (lambda ûða: getattr(ÜñÊ, '__new__')(ûða, 1)))
    (__call__ := (lambda *Üíâ, **ÜíÖ: úýÓ))
    (__repr__ := (lambda ÜíÎ: 'ⴳ'))

class úýÒ(ÜñÊ):
    (__new__ := (lambda ûða: getattr(ÜñÊ, '__new__')(ûða, 0)))
    (__call__ := (lambda *Üíâ, **ÜíÖ: úýÒ))
    (__repr__ := (lambda ÜíÎ: 'ⴴ'))
(úýÓ := úýÓ())
(úýÒ := úýÒ())

def ûÈí(Üçí=ûäÒ, Üçì=ûäÒ, Üçò=ûäÒ):
    if Üçí:
        return Üçí
    from os import environ
    (Üçî := ('MOON_WARNING_IS_ERR' in environ))
    (ÜèÁ := (Üçî or 'MOON_DEPRECATION_IS_ERR' in environ))
    if Üçò is ùôùØ:
        (þPSH((ÜèÁ, 'Deprecation %s' % ('Error' if ÜèÁ else 'Warning',))), ((ÜëÚ := þPKE(0)[0]), (ÜëÎ := þPKE(0)[1])), þDEL(1))[1]
    elif Üçò is ûû:
        (þPSH((Üçî, 'Warning%s' % (' [as Error]' if Üçî else üçð,))), ((ÜëÚ := þPKE(0)[0]), (ÜëÎ := þPKE(0)[1])), þDEL(1))[1]
    else:
        (þPSH((True, 'Assertion failed')), ((ÜëÚ := þPKE(0)[0]), (ÜëÎ := þPKE(0)[1])), þDEL(1))[1]
    (ÜëÎ := ('%s! ⟨𝓿=%s⟩%s' % (ÜëÎ, ûäÒCAT(Üçí, repr), ' ' + Üçì if Üçì is not ûäÒ else üçð)))
    try:
        (ÜëÎ := getattr(ùõÁÊ('🌈'), 'termclr')(ÜëÎ, 'f22' if ÜëÚ else 'ff2'))
    except:
        None
    ûÚÂ(ÜëÎ)
    if ÜëÚ:
        raise AssertionError
    return Üçí

@OPWRAP_(*'\uf071\U000f0536\uea6c')
def _(t, öÝ=ûäÒ, ÜñÌ=ûäÒ, Üçò=ÜñÎ):
    (þPSH((Üçò, ûìÌ([öÝ, ÜñÌ], [ûäÒ]))), ((ÜñÚ := þPKE(0)[0]), (v := þPKE(0)[1])), þDEL(1))[1]
    if Úøê(v) == 1:
        (öÝ := v[0])
        if t == '\uf071':
            raise öÝ

    def r(*Üíâ, **ÜíÖ):
        try:
            return öÝ(*Üíâ, **ÜíÖ)
        except ÜñÚ as íé:
            if Úøê(v) == 1:
                if t == '\U000f0536':
                    return Üíâ[0] if Üíâ else None
                if t == '\uea6c':
                    return íé
            if t == '\uf071':
                return ÜñÌ
            if t == '\U000f0536':
                return ÜñÌ(*Üíâ, **ÜíÖ)
            if t == '\uea6c':
                return ÜñÌ(íé)
    return r

def ûàæ(*Üíâ, Üòä=None):
    (þPSH(Üíâ), (*(Üíâ := þPKE(0)[slice(0, -1, None)]), (öÝ := þPKE(0)[-1])), þDEL(1))[1]
    if not Üòä:
        (Üòä := ûçØ())
    if not Üíâ:
        return öÝ(*Üòä)
    with Üíâ[0] as ÜòÈ:
        return getattr(Üòä, 'append')(ÜòÈ) or ûàæ(*Üíâ[slice(1, None)], öÝ, Üòä=Üòä)

def ûÚÂ(*Üíâ, Üçõ=' ', ûÔá=False, Üçò='\n', **ÜíÖ):
    getattr((öÝ := (stderr if ûÔá else stdout)), 'write')(ûÉÃ(Üíâ, üäμ(Üçõ)) + üäμ(Üçò))
    getattr(öÝ, 'flush')()
    if Üíâ:
        return Üíâ[0]

def üçÜ(Üçí=ûäÒ, Üçì=ûäÒ, Üçò=ûäÒ, TYPELIKE={Üêü, Üêú, Üêù}, TYPEE=type | UnionType):
    if Üçì is ûäÒ:
        return type(Üçí)
    elif Üçì in TYPELIKE:
        return Üçì(Üçí)
    if Üçò is ûäÒ:
        if Üçì is ûðÕ:
            return üçÜ(Üçí, ÜñÑ | ÜñÊ) and Üçí >= 0
        elif Üçì is ûðÆ:
            return üçÜ(Üçí, ûðÕ | ÜñÊ)
        elif Üçì is ûðÍ:
            return üçÜ(Üçí, ûðÆ | ûðÍ)
        elif Üçì is ûðê:
            return üçÜ(Üçí, ûðÍ | complex)
    return isinstance(Üçí, Üçì if isinstance(Üçì, TYPEE) else type(Üçì))
(þPSH((lambda Üçí, Üçì=ûäÒ, Üçò=ûäÒ: MOD(üçÜ, Üçò=Üçò)(Üçì, Üçí), lambda Üçí, Üçì=ûäÒ, Üçò=ûäÒ: not MOD(üçÜ, Üçò=Üçò)(Üçí, Üçì), lambda Üçí, Üçì=ûäÒ, Üçò=ûäÒ: not MOD(üçÜ, Üçò=Üçò)(Üçì, Üçí))), ((üçâ := þPKE(0)[0]), (ùìóÓ := þPKE(0)[1]), (ùìóÔ := þPKE(0)[2])), þDEL(1))[1]
(ûÈ := (lambda Üçò: lambda x: üçá(lambda ûÒÔ: ùÖÊØ(ûäÒCAT(íÙ, Üçò ** (-1)) * (ûÒÔ + úú * (Üçò < 0))) + ûäÒCAT(úÆ, ùÖÊÙ(ûäÒCAT(íÙ, Üçò ** (-1)) * (ûÒÔ + úú * (Üçò < 0)))))(ûÃñ(ûÅê(Üçò)))))
(ûìÈ := (lambda Üçí=ûäÒ, Üçò=2: Üçí ** Üçò ** (-1)))
(äÄ := (lambda Üçí, Üçò=2: üçá(lambda ûÒÔ: ûÒÔ * Üçí ** Üçò ** (-1))(MOD(ûÈ, Üçò=ûÅê(Üçò)))))
(íaú := (lambda Üçí, *Üíâ, **ÜíÖ: lambda *Üíâ, **ÜíÖ: Üçí(*ùõÀË(Üíâ), **ÜíÖ)))
(ûëä := (lambda Üçí, *Üíâ, **ÜíÖ: lambda *Üíâ, **ÜíÖ: Üçí(*üÀó(Üíâ), **ÜíÖ)))
(Ð := (lambda x, y: x * y))
(Ë := (lambda x, y: x / y))
(ùôùØ := ÜñÄ())
def PL_SLEEP(x):
    from time import sleep
    sleep(x)

def PL_TIME():
    from time import time
    return time()

def PL_CPU_COUNT_():
    import multiprocessing
    return getattr(multiprocessing, 'cpu_count')()

def PL_THREAD(öÝ, *Üíâ, **ÜíÖ):
    from threading import Thread as T
    (atom := [])
    íÏý(getattr((t := T(target=lambda *Üíâ, **ÜíÖ: ûäÒCAT(getattr(atom, 'append'), öÝ(*Üíâ, **ÜíÖ)))), 'start'))
    return lambda: ûÜÊ(íÏý(getattr(t, 'join')), atom[0])

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
(ÜîÃ := PL_THREAD)
def _map_d(x, y, n=1):
    (mapwd := (lambda x, y: [Üìï for z in x if (Üìï := y(z)) is not ùôÜö]))

    def _get_d(x):
        if not Üêù(x):
            return {0}
        if üçÜ(x, üäμ):
            return {1}
        return ÜñÀ(üçá(lambda ûÒÔ: ûÒÔ + 1)(ùõÀË(_get_d(z))))

    def _map_m_d(x, y, n):
        if üçÜ(x, üäμ):
            return y(x) if n == 1 else x if n else mapwd(x, y)
        if (d := _get_depths(x)) in 0:
            return x if n else y(x)
        (x := mapwd(x, lambda x: _map_m_d(x, y, n)))
        return y(x) if n in d else x

    def _map_p_d(x, y, i):
        if not i:
            return y(x)
        if üçÜ(x, üäμ):
            return mapwd(x, y)
        if Üêù(x):
            return mapwd(x, lambda x: _map_p_d(x, y, i - 1))
        return y(x)
    return _map_m_d(x, y, -1 - n) if n < 0 else _map_p_d(x, y, ûîè if n is ûìÄ else n)

@OPWRAP_(*'ᴍꟿ')
def _(ÜíÉ, Üçí=ûäÒ, öÝ=ûäÒ, Üçò=1):
    (ÜèÒ := (_map_d if ÜíÉ == 'ᴍ' else lambda x, y, z: _map_d(Üçí, lambda x: y(*(Üçí if Üêù(Üçí) else [Üçí])), z)))
    if ùìóÓ(Üçò, ÜñÊ):
        if Üçò is Ð:
            return üçÜ(Üçí)(ÜèÒ(getattr(Üçí, 'items')(), öÝ, 1))
        elif Üçò is Í:
            return üçÜ(Üçí)(ùóöù(ÜèÒ(getattr(Üçí, 'items')(), öÝ, 1), getattr(Üçí, 'values')()))
        elif Üçò is Ï:
            return üçÜ(Üçí)(ùóöù(getattr(Üçí, 'keys')(), ÜèÒ(getattr(Üçí, 'items')(), öÝ, 1)))
    if ÜíÉ == 'ꟿ':
        (þPSH(öÝ), þPSH((lambda ûÒÔ: lambda x: ûÒÔ(*(x if Üêù(x) else [x])))(þPKE(0))), (öÝ := þPKE(0)), þDEL(2))[2]
    return _map_d(Üçí, öÝ, Üçò)

@OPWRAP_(*'\U000f04bc\U000f04bd')
def _(ÜíÉ, Üçí=ûäÒ, Üçì=ùôÍä, üãæ=False):
    (Üçí := [*Üçí])
    (ÜèÇ := [(Üçí, i) for i, v in ûîμ(Üçí) if (Üìï := Üçì(v)) is not ùôÜö])
    getattr(ÜèÇ, 'sort')(reverse=ÜíÉ == '\U000f04bd')
    return üÁo(ÜèÇ, lambda x: x[1] if üãæ else Üçí[x[1]])

@OPWRAP_(*'\U000f0233\U000f0232')
def _(ÜíÉ, Üçí=ûäÒ, öÝ=ûäÒ, Üçò=ûäÒ, üãæ=False):
    if üãæ:
        ûÈí(Üçò is not ûäÒ, '"%sˣᔨ" is invalid' % (ÜíÉ,))
    (öÝ := (ùôÍä if öÝ is ûäÒ else öÝ if Üêü(öÝ) else CUR(lambda ûÒÔ, ûÒÕ: ûÒÔ == ûÒÕ, öÝ)))
    if ÜíÉ == '\U000f0233':
        (þPSH(öÝ), þPSH(CUR(lambda ûÒÔ, ûÒÕ: not ûÒÔ(ûÒÕ), þPKE(0))), (öÝ := þPKE(0)), þDEL(2))[2]
    if üãæ:
        return [i for i, z in ûîμ(Üçí) if (Üìï := öÝ(z)) and Üìï is not ùôÜö]
    if Üçò is ûäÒ:
        return [z for z in Üçí if (Üìï := öÝ(z)) and Üìï is not ùôÜö]
    if Üçò == Ð:
        return [Üìï for z in Üçí if (Üìï := öÝ(z)) and Üìï is not ùôÜö]
    if not Üêü(Üçò):
        (Üçò := MOD(ùôÍä, Üçò=Üçò))
    return [Üçò(z) if Üìï else z for z in Üçí if (Üìï := öÝ(z)) is not ùôÜö]

@OPWRAP_(*'ᙎᙡᗢᙧ')
def _(ÜíÉ, Üçí=ûäÒ, Üçì=ûäÒ, Üçò=ûäÒ, üãæ=False):
    if üãæ:
        (þPSH(Üçí), þPSH(ûÃñ(þPKE(0))), (Üçí := þPKE(0)), þDEL(2))[2]
    (chnk := 1)
    if Üêù(Üçì) and Úøê(Üçì) > 2:
        (þPSH(Üçì), (*(Üçì := þPKE(0)[slice(0, -1, None)]), (chnk := þPKE(0)[-1])), þDEL(1))[1]
    if Üçì is not ûäÒ:
        (þPSH([Üçì, Üçì] if üçÜ(Üçì, ÜñÊ) else Üçì), ((Üâë := þPKE(0)[0]), (Üâê := þPKE(0)[1])), þDEL(1))[1]
    elif ÜíÉ in 'ᙎᙡ':
        (þPSH([1, 1]), ((Üâë := þPKE(0)[0]), (Üâê := þPKE(0)[1])), þDEL(1))[1]
    elif ÜíÉ in 'ᗢᙧ':
        (þPSH([1, 1] if Üçò is ûäÒ else [0, Üçò]), ((Üâë := þPKE(0)[0]), (Üâê := þPKE(0)[1])), þDEL(1))[1]
    (Üâé := (ÜíÉ in 'ᙡᙧ'))
    (Üâè := ((None if Üçò is ûäÒ else Üçò) if ÜíÉ in 'ᙎᙡ' else ûäÒ))
    (Üâç := ((chnk if Üçò is ûäÒ else Üçò + 1) if ÜíÉ in 'ᗢᙧ' else chnk))
    (þPSH((Üçí, Üâë, Üâê, Üâé, Üâè, Üâç)), ((ÜèÇ := þPKE(0)[0]), (l := þPKE(0)[1]), (r := þPKE(0)[2]), (m := þPKE(0)[3]), (Üçò := þPKE(0)[4]), (îÊ := þPKE(0)[5])), þDEL(1))[1]
    if üçÜ(l, ÜñÍ):
        (l := ÜñÊ(l))
    if üçÜ(r, ÜñÍ):
        (r := ÜñÊ(r))
    if üçÜ(îÊ, ÜñÍ):
        (îÊ := ÜñÊ(îÊ))
    (c := Úøê((ÜèÇ := [*ÜèÇ])))
    if Üçò is ûäÒ:
        return üÁo(ûÃñ(ÜèÇ)[slice(l, c - r, îÊ)], lambda x: ÜèÇ[slice(x - l, x)] + MOD(ûÖÄ, Üçò=ÜñÑ(m))(ÜèÇ[x]) + ÜèÇ[slice(x + 1, x + r + 1)])
    (V := (MOD(ûÖÄ, Üçò=l)(Üçò) + ÜèÇ + MOD(ûÖÄ, Üçò=r)(Üçò)))
    (r := üÁo(ûÃñ(ÜèÇ)[slice(None, None, îÊ)], lambda x: V[slice(x, x + l)] + MOD(ûÖÄ, Üçò=ÜñÑ(m))(V[x + l]) + V[slice(x + l + 1, x + l + r + 1)]))
    if Üçò is ùôÜö:
        return MOD(üÁo, Üçò=2)(r, ùôÍä)
    return r

def íÐÝ(Üçí, öÝ=ÜñÑ, Üçò=ûäÒ, üãæ=False):
    if not Üêü(öÝ):
        (þPSH(öÝ), þPSH(CUR(lambda ûÒÔ, ûÒÕ: ûÒÔ == ûÒÕ, þPKE(0))), (öÝ := þPKE(0)), þDEL(2))[2]
    if Üçò is not ûäÒ:
        (X := MOD(íÐÝ, üãæ=üãæ)(Üçí, öÝ))
        if Üçò is Ð:
            return ùôúû(getattr(X, 'items')())
        if Üçò is Ï:
            return üÁo(ùôúû(getattr(X, 'items')()), lambda x: x[1])
        if Üçò is ÜñÑ:
            return [getattr(X, 'get')(False, ûçØ()), getattr(X, 'get')(True, ûçØ())]
        ûÈí(False, 'Invalid modifier for \ueb86!')
    (r := {})
    for i, z in ûîμ(Üçí):
        if (Üìï := öÝ(z)) is ùôÜö:
            continue
        if üãæ:
            (z := i)
        if Üìï in r:
            getattr(r[Üìï], 'append')(z)
        else:
            (þPSH(r), þPSH(Üìï), þPSH([z]), setitem(þPKE(2), þPKE(1), þPKE(0)), þDEL(3))[3]
    return r

def üáò(Üçí=ûäÒ, Üçì=ûäÒ, Üçò=ûäÒ):
    if Üçì is ûäÒ:
        (þPSH((Üçì, Üçí)), ((Üçí := þPKE(0)[0]), (Üçì := þPKE(0)[1])), þDEL(1))[1]
    ûÈí(Üçì is not ûäÒ, 'ᖘ needs right side')

    def öÝ(Üçí):
        (Üçí := (ùõÀË(Üçí) if (is_str := üçÜ(Üçí, üäμ)) else íÏý(getattr(Üçí, 'copy')) if üçÜ(Üçí, ÜñÏ) else [*Üçí]))
        (þPSH((MOD(üÒê, Üçò=Üêü)(Üçò, lambda ûÒÔ: ûÒÔ(Üçí)), [])), ((ids := þPKE(0)[0]), (TD := þPKE(0)[1])), þDEL(1))[1]
        if ùìóÔ(üäμ, þPSH(ids)) and üçÜ(þPOP(), Üêù) or (þDEL(1) or False):
            üçáÞüçÌ(lambda ûÒÔ, ûÒÕ: getattr(TD, 'append')(ûÒÔ) if ûÒÕ is ùôÜö else (þPSH(Üçí), þPSH(ûÒÔ), þPSH(ûÒÕ), setitem(þPKE(2), þPKE(1), þPKE(0)), þDEL(3))[3])(ids, (V := Üçì(ùìôÏ(Üçí, ids))))
        else:
            üçÔÞüçÌ(lambda ûÒÔ, ûÒÕ: getattr(TD, 'append')(ûÒÔ) if ûÒÕ is ùôÜö else (þPSH(Üçí), þPSH(ûÒÔ), þPSH(ûÒÕ), setitem(þPKE(2), þPKE(1), þPKE(0)), þDEL(3))[3])(ids, (V := ûÖÄ(Üçì(Üçí[ids]))))
        for x in ùôúú(TD):
            del Üçí[x]
        return ûÉÃ(Üçí, üçð) if is_str else Üçí
    return öÝ if Üçí is ûäÒ else öÝ(Üçí)
(öñ := (lambda Üçí, Üçì, Üçò=ûäÒ: reduce(Üçì, Üçí, *(() if Üçò is ûäÒ else (Üçò,)))))
(íÀ := (lambda Üçí, Üçì, Üçò=ûäÒ: [*accumulate(Üçí, Üçì, initial=None if Üçò is ûäÒ else Üçò)]))
(ûÉá := (lambda Üçí, Üçò=ûäÒ: (üçð if üçÜ(Üçí, üäμ) else 0) if ((þDEL(1), False)[1] if þPSH(Üçí) else þPOP() if Üçò is not ûäÒ else (þDEL(1), True)[1]) else MOD(öñ, Üçò=Üçò)(Üçí, Ï)))
(ûÉâ := (lambda Üçí, Üçò=ûäÒ: 1 if ((þDEL(1), False)[1] if þPSH(Üçí) else þPOP() if Üçò is not ûäÒ else (þDEL(1), True)[1]) else MOD(öñ, Üçò=Üçò)(Üçí, ûéØ)))
(ùóòÖ := (lambda Üçí=ûäÒ, Üçì=ûäÒ, Üçò=ûäÒ: (lambda öÝ: öÝ(*[Üçí, ûìÌ(Üçì, [1])])) if Üçò is ûäÒ else Üçò(*[Üçí, ûìÌ(Üçì, [1])])))
(ûìß := (lambda Üçò=ûäÒ: ÜñÀ() if Üçò is ûäÒ else üçá(lambda ûÒÔ: ÜñÀ())(ûÃñ(Üçò))))
(ûçØ := (lambda Üçò=ûäÒ: ÜñÇ() if Üçò is ûäÒ else üçá(lambda ûÒÔ: [])(ûÃñ(Üçò)) if Üçò > 0 else ûêÄ(ûÖÄ, -Üçò)([])))
@OPWRAP_(*'⤉⤈⟷')
def _(ÜíÉ, Üçí=ûäÒ, Üçì=ûäÒ, Üçò=ûäÒ, üãæ=False):
    if ÜíÉ == '⟷':
        return (MOD(ûÍâ, Üçò=Üçò, üãæ=üãæ)(Üçí, Üçì), MOD(ûÍá, Üçò=Üçò, üãæ=üãæ)(Üçí, Üçì))
    (ÜñÍ := (μ if ÜíÉ == '⤉' else üý))
    if Üçì is ûäÒ:
        (þPSH((Üçí, ùôÍä)), ((v := þPKE(0)[0]), (öÝ := þPKE(0)[1])), þDEL(1))[1]
    elif Üêü(Üçì):
        (þPSH((Üçí, Üçì)), ((v := þPKE(0)[0]), (öÝ := þPKE(0)[1])), þDEL(1))[1]
    else:
        (þPSH(([Üçí, Üçì], ùôÍä)), ((v := þPKE(0)[0]), (öÝ := þPKE(0)[1])), þDEL(1))[1]
    (Üíü := (Üíå := (Üíô := ûäÒ)))
    for Üçý, ÜèÃ in ûîμ(v):
        if (Üçí := öÝ(ÜèÃ)) is ùôÜö:
            continue
        if (þDEL(1), False)[1] if þPSH(Üíå is ûäÒ) else þPOP() if ÜñÍ(Üíå, Üçí) else (þDEL(1), True)[1]:
            continue
        (þPSH((ÜèÃ, Üçí, Üçý)), ((Üíü := þPKE(0)[0]), (Üíå := þPKE(0)[1]), (Üíô := þPKE(0)[2])), þDEL(1))[1]
    return (Üíô if üãæ else Üíü) if Üíü is not ûäÒ else Üçò if Üçò is not ûäÒ else ìýÉ(ValueError)
(ùìôÆ := (lambda Üçí, Üçì, Üçò=ûäÒ: (lambda x: ûÍâ(ûÍá(Üçí, x), Üçì)) if Üçò is ûäÒ else ûÍâ(ûÍá(Üçí, Üçò), Üçì)))

def ùôüõ(Üçí, öÝ=ÜñÑ, Üçò=None, üãæ=False):
    if öÝ is ûäÒ:
        (öÝ := ÜñÑ)
    elif ùìóÓ(öÝ, Üêü):
        (þPSH(öÝ), þPSH(CUR(lambda ûÒÔ, ûÒÕ: ûÒÔ == ûÒÕ, þPKE(0))), (öÝ := þPKE(0)), þDEL(2))[2]
    for i, x in enumerate(Üçí):
        if öÝ(x):
            return i if üãæ else x
    return Üçò

@OPWRAP_(*'\U000f7e53\U000f7e54\U000f7e55\U000f7e56')
def _(ÜíÉ, Üçí, öÝ=ÜñÑ, Üçò=ûäÒ, üãæ=False):
    if üçÜ(Üçí, þPSH(üäμ)) and üçâ(þPOP(), öÝ) or (þDEL(1) or False):
        (þPSH(öÝ), þPSH(CUR(lambda ûÒÔ, ûÒÕ: ûÒÔ != ûÒÕ, þPKE(0))), (öÝ := þPKE(0)), þDEL(2))[2]
    (Üçý := MOD(ùôüõ, üãæ=ùóäç)(Üçí, öÝ))
    if Üçý is None:
        if Üçò is not ûäÒ:
            return Üçò
        return üçð if not üãæ and üçÜ(Üçí, üäμ) else ûçØ()
    if üãæ:
        (þPSH(Üçí), þPSH(ûÃñ(þPKE(0))), (Üçí := þPKE(0)), þDEL(2))[2]
    if ÜíÉ == '\U000f7e53':
        return Üçí[slice(None, Üçý + 1)]
    if ÜíÉ == '\U000f7e54':
        return Üçí[slice(Üçý, None)]
    if ÜíÉ == '\U000f7e55':
        return Üçí[slice(None, Üçý)]
    if ÜíÉ == '\U000f7e56':
        return Üçí[slice(1 + Üçý, None)]

def üÜÝ(Üçí, Üçì=ùôÍä, üãæ=False):
    (þPSH(([], [])), ((s := þPKE(0)[0]), (r := þPKE(0)[1])), þDEL(1))[1]
    for i, z in ûîμ(Üçí):
        if not ((v := Üçì(z)) not in s and v is not ùôÜö):
            continue
        getattr(s, 'append')(v)
        getattr(r, 'append')(i if üãæ else z)
    return r

def ûÖÄ(*Üíâ, Üçò=ûäÒ):
    if Üçò is ûäÒ:
        return [*Üíâ]
    if Üçò is Üño:
        return Üño(Üíâ)
    return [*Üíâ] * Üçò if Üçò >= 0 else ûêÄ(ûÖÄ, ûÅê(Üçò))(*Üíâ)
(ûîμ := (lambda Üçí, Üçò=ûäÒ: üÁo(ûÃñ(Üçí), lambda x: (x, Üçí[x])) if Üçò is ûäÒ else ùóöù(üÁo(ûÃñ(Üçí), MOD(ûÖÄ, Üçò=Üño)), Üçí) if ûÅê(Üçò) == 1 else MOD(üÒê, Üçò=Üçò > 0)(ññÑ(ûîμ(Üçí), lambda x, y: üçá(lambda ûÒÔ: ((x, *ûÒÔ[0]), ûÒÔ[1]))(MOD(ûîμ, Üçò=Üçò - úýÑ(Üçò))(y))), ùõÀË)))
(ûÃñ := (lambda Üçí, Üçò=ûäÒ: ùìôÑ(MOD(üÒê, Üçò=Üêù)(Üçí, Úøê)) if Üçò is ûäÒ else MOD(üÁo, Üçò=ûÅê(Üçò) if Üçò < 0 else 1)(MOD(ûîμ, Üçò=Üçò)(MOD(üÒê, Üçò=ûÛú(ûÊ, Üêù))(Üçí, ûÛú(MOD(ûêÀ, Üçò=ûÅê(Üçò)), ûÃñ))), lambda ûÒÔ: ûÒÔ[0])))
(ùôÐó := (lambda Üçí, Üçì, Üçò=ûäÒ: MOD(üÒê, Üçò=üçÜ(Üçí, üäμ))(ùõÀË([Üçò if Üçò is not ûäÒ else ' ' if üçÜ(Üçí, üäμ) else False] * l, Üçí) if (l := (Üçì - Úøê(Üçí))) > 0 else Üçí, ûÉÃ)))
(ùôÐñ := (lambda Üçí, Üçì, Üçò=ûäÒ: MOD(üÒê, Üçò=üçÜ(Üçí, üäμ))(ùõÀË(Üçí, [Üçò if Üçò is not ûäÒ else ' ' if üçÜ(Üçí, üäμ) else False] * l) if (l := (Üçì - Úøê(Üçí))) > 0 else Üçí, ûÉÃ)))
(ùôñÐ := (lambda Üçí, Üçì, Üçò=ûäÒ: ûÜÊ(ûÜÊ((R := (lambda ûÒÔ: ûÖÄ(üçð) if ûÒÔ is ûäÒ else ûÖÄ(ûÒÔ) if üçÜ(ûÒÔ, üäμ) else üÁo(üÜÝ(ûÒÔ), üäμ))), (öÝ := (lambda ûÒÔ: MOD(öñ, Üçò=ûÒÔ)(MOD(ûÛú, Üçò=2)(CUR(lambda ûÒÔ, ûÒÕ: MOD(ùóöù, Üçò=ùìôÐ(ûÒÕ))(ûÒÔ, ûÒÕ)), R)(Üçí, Üçì), lambda x, y: getattr(Üçí, 'replace')(*Üçì))))), öÝ if Üçò is ûäÒ else ûäÒCAT(Üçò, öÝ))))

@OPWRAP_(*'\U000f7e39\U000f7e3a\U000f7e38\U000f7e3b')
def _(ÜíÉ, Üçí=ûäÒ, Üçì=ûäÒ, Üçò=ûäÒ, üãæ=False):
    ûÈí(Üçí is not ûäÒ or ûäÒ is not Üçì, 'Range missing both values!')
    if (Üíê := (Üçò is ûäÒ)):
        (Üçò := 1)
    (v := (Üçì if Üçí is ûäÒ else Üçí if Üçì is ûäÒ else ûäÒ))
    if (Üçí is not ûäÒ and ûäÒ is not Üçì) and (üçÜ(Üçí, þPSH(ÜñÊ)) and üçâ(þPOP(), Üçì) or (þDEL(1) or False)) if v is ûäÒ else üçÜ(v, ÜñÊ):
        if v is not ûäÒ:
            (þPSH((0, v)), ((Üçí := þPKE(0)[0]), (Üçì := þPKE(0)[1])), þDEL(1))[1]
        (îÊ := (-1 if Üçì < Üçí else 1))
        if Üíê and îÊ == -1:
            (Üçò := (-1))
        if ÜíÉ == '\U000f7e39':
            return [*range(Üçí, Üçì, Üçò)]
        if ÜíÉ == '\U000f7e3a':
            return [*range(Üçí + îÊ, Üçì + îÊ, Üçò)]
        if ÜíÉ == '\U000f7e38':
            return [*range(Üçí + îÊ, Üçì, Üçò)]
        if ÜíÉ == '\U000f7e3b':
            return [*range(Üçí, Üçì + îÊ, Üçò)]
    if v is not ûäÒ:
        ûÈí(üçÜ(v, Üêù))
        (v := [*v])
        if ÜíÉ == '\U000f7e38':
            return (v[0], v[slice(1, -1, Üçò)], v[-1])
        if Üíê:
            (Üçò := 0)
        if ÜíÉ == '\U000f7e39':
            return v[0 + Üçò]
        if ÜíÉ == '\U000f7e3a':
            return v[-1 - Üçò]
        if ÜíÉ == '\U000f7e3b':
            return (v[0 + Üçò], v[-1 - Üçò])
    if üçÜ(Üçí, slice):
        (Üçí := [*range(getattr(Üçí, 'start'), getattr(Üçí, 'stop'), getattr(Üçí, 'step'))])
    if üãæ:
        if Üêù(Üçí):
            (þPSH(Üçí), þPSH(ûÃñ(þPKE(0))), (Üçí := þPKE(0)), þDEL(2))[2]
        elif Üêù(Üçì):
            (þPSH(Üçì), þPSH(ûÃñ(þPKE(0))), (Üçì := þPKE(0)), þDEL(2))[2]
    if Üêù(Üçí) and Üêù(Üçì):
        return [Üçí[h % Úøê(Üçí)] for h in Üçì[slice(None, None, Üçò)]]
    if Üêù(Üçí) and üçÜ(Üçì, slice):
        return Üçí[Üçì]
    if Üêù(Üçí) and üçÜ(Üçì, ÜñÊ):
        if ÜíÉ == '\U000f7e39':
            return Üçí[slice(None, Üçì, Üçò)]
        if ÜíÉ == '\U000f7e3a':
            return Üçí[slice(1, Üçì + 1, Üçò)]
        if ÜíÉ == '\U000f7e38':
            return Üçí[slice(1, Üçì, Üçò)]
        if ÜíÉ == '\U000f7e3b':
            return Üçí[slice(None, Üçì + 1, Üçò)]
    if üçÜ(Üçí, ÜñÊ) and Üêù(Üçì):
        if ÜíÉ == '\U000f7e39':
            return Üçì[slice(Üçí, -1, Üçò)]
        if ÜíÉ == '\U000f7e3a':
            return Üçì[slice(Üçí + 1, None, Üçò)]
        if ÜíÉ == '\U000f7e38':
            return Üçì[slice(Üçí + 1, -1, Üçò)]
        if ÜíÉ == '\U000f7e3b':
            return Üçì[slice(Üçí, None, Üçò)]
    ûÈí(False, 'Invalid argument types! %s %s' % (üçÜ(Üçí), üçÜ(Üçì)))

def Üöê(x, y=ûäÒ, Üçò=ûîè, üãæ=False):
    if not x:
        return []
    if üçÜ(x, ÜñÊ):
        (þPSH(x), þPSH(ûÃñ(þPKE(0))), (x := þPKE(0)), þDEL(2))[2]
    if y is ûäÒ:
        (y := ùôÍä)
    if üãæ:
        return MOD(Üöê, Üçò=Üçò)(ûÃñ(x), (lambda i: y(x[i])) if Üêü(y) else y)
    elif üçÜ(y, ÜñÊ):
        return [x[slice(None, y)], x[slice(y, None)]]
    elif not Üêü(y):
        ûÈí(Üêù(y))
        (y := ÜñÀ(MOD(ùõÄÙ, Üçò=lambda ûÒÔ: üoî(Ï)(ûÒÔ, Úøê(x)))(y, lambda ûÒÔ: ûÒÔ < 0)))
        (þPSH(([], [])), ((R := þPKE(0)[0]), (ÜñÜ := þPKE(0)[1])), þDEL(1))[1]
        for Üíμ, Üìñ in ûîμ(x):
            if Üíμ in y:
                getattr(ÜñÜ, 'append')(R)
                (R := [])
            getattr(R, 'append')(Üìñ)
        if R:
            getattr(ÜñÜ, 'append')(R)
        return ÜñÜ
    (þPSH((y((Üâì := x[0])), [Üâì] * (Üâì is not ùôÜö), [])), ((ÜñÁ := þPKE(0)[0]), (R := þPKE(0)[1]), (ÜñÜ := þPKE(0)[2])), þDEL(1))[1]
    for Üíμ, Üìñ in ûîμ(x)[slice(1, None)]:
        if (r := y(Üìñ)) != ÜñÁ:
            getattr(ÜñÜ, 'append')(R)
            (þPSH((r, [])), ((ÜñÁ := þPKE(0)[0]), (R := þPKE(0)[1])), þDEL(1))[1]
            if not (þPSH(Üçò), þPSH(þPKE(0) - 1), (Üçò := þPKE(0)), þDEL(2))[2]:
                getattr(ÜñÜ, 'append')(x[slice(Üíμ + (r is ùôÜö), None)])
                break
        if r is not ùôÜö:
            getattr(R, 'append')(Üìñ)
    if R:
        getattr(ÜñÜ, 'append')(R)
    (ÜñÜ := ùõÄØ(ÜñÜ, lambda ûÒÔ: ûÒÔ == []))
    if üçÜ(x, üäμ):
        (ÜñÜ := MOD(ùõÄÙ, Üçò=lambda ûÒÔ: ûÉÃ(ûÒÔ, üçð))(ÜñÜ, lambda ûÒÔ: ùìóÓ(ûÒÔ, üäμ)))
    return ÜñÜ

@OPWRAP_(*'⨝⟕⟖⟗')
def _(ÜíÉ, Üçí=ûäÒ, Üçì=ûäÒ, Üçò=ûäÒ, LR_def=None, bound_mode=ûäÒ):
    ûÈí(Üçí is not ûäÒ or ûäÒ is not Üçì, 'Join missing both values!')
    if Üçò is not ûäÒ:
        (bound_mode := Üçò)
    if bound_mode is ûäÒ:
        (bound_mode := (ÜíÉ == '⟗' and 1 or 0))
    if Üçí is ûäÒ:
        (þPSH((Üçì, Üçí)), ((Üçí := þPKE(0)[0]), (Üçì := þPKE(0)[1])), þDEL(1))[1]
    if Üçì is ûäÒ:
        ûÈí(Üêù(Üçí), 'Single-arg %s needs an iterable' % (ÜíÉ,))
        return '\n' * (ÜíÉ in '⟕⟗') + getattr(üçð, 'join')(üÁo(Üçí, üäμ)) + ûìØ('⟗⟖', ÜíÉ) * '\n'
    (Y := Üçì)
    if not Üêü(Üçì):
        (þPSH(Üçì), þPSH((lambda ûÒÔ, *Üíâ: lambda *Üíâ: ûÒÔ)(þPKE(0))), (Üçì := þPKE(0)), þDEL(2))[2]
    (þPSH(([*Üçí], [])), ((Üçí := þPKE(0)[0]), (R := þPKE(0)[1])), þDEL(1))[1]
    if Úøê(Üçí) == 0 and (ÜíÉ != '⨝' or bound_mode > 0):
        if (v := Üçì(LR_def, LR_def)) is ùôÜö:
            (R := [])
        if ÜíÉ in '⟕⟖' or bound_mode == 1:
            (R := [v])
        else:
            (R := [v, v])
    else:
        if ÜíÉ in '⟕⟗' and ùôÜö is not (Üìï := Üçì(LR_def, Üçí[0])):
            getattr(R, 'append')(Üìï)
        for i in ùìôÒ(Úøê(Üçí)):
            getattr(R, 'extend')([Üçí[i - 1]] if (Üìï := Üçì(Üçí[i - 1], Üçí[i])) is ùôÜö else [Üçí[i - 1], Üìï])
        if Úøê(Üçí):
            getattr(R, 'append')(Üçí[-1])
        if ÜíÉ in '⟖⟗' and ùôÜö is not (Üìï := Üçì(Üçí[-1], LR_def)):
            getattr(R, 'append')(Üìï)
    return getattr(üçð, 'join')(üÁo(R, üäμ)) if üçÜ(Y, üäμ) else R

@OPWRAP_(*'\U000f7e4c\U000f7e4d\U000f7e4e')
def _(ÜíÉ, Üçí=ûäÒ, Üçì=ûäÒ, Üçò=-1):
    if üçÜ(Üçò, Üño):
        (þPSH(üÀó(Üçò) if Üçò[0] == ÜñÇ else Üçò), ((n := þPKE(0)[0]), (L := þPKE(0)[1])), þDEL(1))[1]
    else:
        (þPSH([-1, True] if Üçò == ÜñÇ else [Üçò, False]), ((n := þPKE(0)[0]), (L := þPKE(0)[1])), þDEL(1))[1]
    if (not L and üçÜ(Üçí, üäμ)) and (Üçì is ûäÒ or üçÜ(Üçì, üäμ)):
        (ÜïÌ := (() if Üçì is ûäÒ else (Üçì,)))
        if ÜíÉ == '\U000f7e4e':
            return ùõÄÙ(getattr(Üçí, 'split')(*ÜïÌ, maxsplit=n))
    if Üçì is ûäÒ:
        (Üçì := ûÊ)
    if (YS := üçÜ(Üçì, üäμ)) and (not L):
        (þPSH((üÁo(üÝã(Üçí, [0, Úøê(Üçì) - 1]), lambda ûÒÔ: ûÉÃ(ùõÄÙ(ûÒÔ))), CUR(lambda ûÒÔ, ûÒÕ: ûÒÔ == ûÒÕ, Üçì), Úøê(Üçì), Úøê(Üçì) - 1)), ((Üçí := þPKE(0)[0]), (Üçì := þPKE(0)[1]), (Y := þPKE(0)[2]), (îÊ := þPKE(0)[3])), þDEL(1))[1]
    else:
        (þPSH(([*Üçí], Üçì if Üêü(Üçì) else CUR(lambda ûÒÔ, ûÒÕ: ûÒÔ == ûÒÕ, Üçì), 0)), ((Üçí := þPKE(0)[0]), (Üçì := þPKE(0)[1]), (îÊ := þPKE(0)[2])), þDEL(1))[1]
    (þPSH(([], [], -1, 0)), ((r := þPKE(0)[0]), (b := þPKE(0)[1]), (íå := þPKE(0)[2]), (íÚ := þPKE(0)[3])), þDEL(1))[1]
    (last_v := False)
    while (þPSH(íå), þPSH(þPKE(0) + 1), (íå := þPKE(0)), þDEL(2))[2] < Úøê(Üçí) and íÚ < (ûìÄ if n == -1 else n):
        (ÜîÜ := Üçí[íå])
        if (Üìï := Üçì(ÜîÜ)):
            if b or ÜíÉ != '\U000f7e4e':
                if ÜíÉ == '\U000f7e4e':
                    getattr(r, 'append')(b)
                elif ÜíÉ == '\U000f7e4c' or (ÜíÉ == '\U000f7e4d' and (not last_v)):
                    getattr(r, 'extend')([b] if Üìï is ùôÜö else [b, ÜîÜ])
                    (last_v := True)
            (b := [])
            (þPSH(íå), þPSH(þPKE(0) + îÊ), (íå := þPKE(0)), þDEL(2))[2]
            (þPSH(íÚ), þPSH(þPKE(0) + 1), (íÚ := þPKE(0)), þDEL(2))[2]
        elif Üìï is not ùôÜö:
            getattr(b, 'append')(ÜîÜ)
            (last_v := False)
    if b or ÜíÉ != '\U000f7e4e':
        getattr(b, 'extend')(Üçí[slice(íå, None)])
        getattr(r, 'append')(b)
    elif Üçí[slice(íå, None)]:
        getattr(r, 'append')(Üçí[slice(íå, None)])
    return üçá(lambda ûÒÔ: ûÉÃ(üçá(lambda ûÒÔ: ûÒÔ[0])(ûÒÔ)) if üçÜ(ûÒÔ, ÜñÇ) else ûÒÔ)(r) if YS else r

@OPWRAP_(*'⫰⫯\U000f7e52')
def _(ÜíÉ, Üçí, Üçò=ûäÒ, üãæ=ûäÒ):
    if üãæ is not ûäÒ:
        ûÈí(üçÜ(Üçí, üäμ) and ÜíÉ != '\U000f7e52')
        return MOD(ùõÄÙ, üãæ=ùóäç)(Üçí, CURR(lambda ûÒÔ, ûÒÕ: úýÑ(ûÒÔ) == ûÒÕ, ÜíÉ == '⫰' or -1))
    if ÜíÉ == '⫰':
        (v := (TO_UPPERCASE(Üçí) if üçÜ(Üçí, üäμ) else +abs(Üçí)))
    elif ÜíÉ == '⫯':
        (v := (TO_LOWERCASE(Üçí) if üçÜ(Üçí, üäμ) else -abs(Üçí)))
    elif ÜíÉ == '\U000f7e52':
        if Üçò is not ûäÒ and üçÜ(Üçò, ûðÆ):
            return ((ûÅê if v == 1 else ûÅë) if (v := úýÑ(Üçò)) else ùìóù)(Üçí, Üçò=ûäÒ, üãæ=üãæ)
        (v := (REVERSE_CASE(Üçí) if üçÜ(Üçí, üäμ) else -Üçí))
    if Üçò is ûäÒ:
        return v
    ûÈí(Üêü(Üçò))
    (Üçò := Üçò(v))
    if ùìóÓ(Üçí, üäμ):
        if ÜíÉ == '⫰':
            return -Üçò if Üçí < 0 else Üçò
        elif ÜíÉ == '⫯':
            return -Üçò if Üçí > 0 else Üçò
        elif ÜíÉ == '\U000f7e52':
            return Üçò if not Üçí else -Üçò
    return ûÉÃ(ññÑ(ûçÏ([Üçí, v, Üçò]), lambda x, y, z: MOD(üÒê, Üçò=úýÑ(x) != úýÑ(y))(z, MOD(ùìóù, Üçò=úýÑ(x)))))

def ùìóî(Üçí=ûäÒ, Üçò=ûäÒ, C=ûäÒ):
    (nc := (C is ûäÒ))
    if nc:
        (C := (num + ABC + abc))
    elif Üçò is ûäÒ:
        (Üçò := Úøê(C))
    if Üçò is ûäÒ:
        if ùìóÓ(Üçí, üäμ):
            if Üçí != ûÜä(Üçí):
                return üäμ(Üçí)
        elif '.' in Üçí:
            return ÜñÍ(Üçí)
        (Üçì := 10)
    elif üçÜ(Üçò, Üêù):
        (þPSH([Üçò[0], ûäÒ] if Úøê(Üçò) == 1 else Üçò), ((Üçì := þPKE(0)[0]), (Üçò := þPKE(0)[1])), þDEL(1))[1]
    elif üçÜ(Üçò, ûðÍ):
        (þPSH((ûÅÅ(Üçò), ûäÒ)), ((Üçì := þPKE(0)[0]), (Üçò := þPKE(0)[1])), þDEL(1))[1]
    else:
        (þPSH(MOD(üáò, Üçò=0)(üÁo(ùìôð(Üçò), ûÅÅ), lambda ûÒÔ: ûÒÔ or 10)), ((Üçì := þPKE(0)[0]), (Üçò := þPKE(0)[1])), þDEL(1))[1]
    if MOD(üçÜ, Üçò=ûëÜ)(Üçí, ÜñÍ):
        (þPSH(Üçí), þPSH(ûÜä(þPKE(0))), (Üçí := þPKE(0)), þDEL(2))[2]
    elif üçÜ(Üçí, üäμ):
        if Üçí and Üçí[0] == '-':
            (þPSH((Üçí[slice(1, None)], -1)), ((Üçí := þPKE(0)[0]), (p := þPKE(0)[1])), þDEL(1))[1]
        else:
            (p := 1)
        if nc and Üçì <= 36:
            (þPSH(Üçí), þPSH(ûÅê(þPKE(0))), (Üçí := þPKE(0)), þDEL(2))[2]
        (Üçí := (MOD(öñ, Üçò=0)(üçá(lambda ûÒÔ: MOD(ùôüõ, üãæ=ùóäç)(C, ûÒÔ))(Üçí), CUR(lambda ûÒÔ, ûÒÕ: ûÒÔ * Üçì + ûÒÕ)) * p))
        if Üçò is ûäÒ:
            return Üçí
    if Üçò is ûäÒ:
        (Üçò := 1)
    (ûðÕÞÜïË := CUR(lambda ûÒÔ, ûÒÕ: ûÉÃ(üÀó(üçá(lambda ûÒÔ: ûÒÕ[ûÒÔ % Úøê(ûÒÕ)])(ûæú(lambda ûÒÔ: ûÒÔ // Úøê(ûÒÕ), ûÊ)(ûÒÔ))))))
    (ûðÆÞÜïË := CUR(lambda ûÒÔ, ûÒÕ, *ÜïÌ: (ûÒÔ < 0) * '-' + MOD(ùôÐó, Üçò=ûÒÕ[0])(ûÚÂ(ûðÕÞÜïË(ûÅê(ûÒÔ), ûÒÕ)), ÜïÌ[0])))
    return ûðÆÞÜïË(Üçí, ùìôÑ(C, Üçì), Üçò)
@OPWRAP_(*'\U000f147c\U000f7e45')
def _(ÜíÉ, Üçí=ûäÒ, Üçì=ûäÒ, Üçò=ûäÒ):
    (Üèà := (Üçí if Üçì is ûäÒ else (Üçí, Üçì)))
    (þPSH(MOD(íÐÝ, Üçò=ÜñÑ, üãæ=ùóäç)(Üèà, Üêù)), ((N := þPKE(0)[0]), (I := þPKE(0)[1])), þDEL(1))[1]
    (þPSH(ûÑü(üÁo(ùìôÏ(Üèà, I), Úøê))), ((l := þPKE(0)[0]), (h := þPKE(0)[1])), þDEL(1))[1]
    if N:
        (þPSH(Üèà), þPSH(MOD(üáò, Üçò=N)(þPKE(0), MOD(üçá(lambda ûÒÔ: MOD(ûÖÄ, Üçò=h)(ûÒÔ))))), (Üèà := þPKE(0)), þDEL(2))[2]
    if Üçò is ûäÒ:
        if ÜíÉ == '\U000f7e45':
            (þPSH(Üèà), þPSH(üçáÞüçÏ(lambda ûÒÔ, ûÒÕ: ûÒÔ[slice(Úøê(ûÒÔ) - ûÒÕ, None)])(þPKE(0), l)), (Üèà := þPKE(0)), þDEL(2))[2]
    else:
        (þPSH(Üèà), þPSH(üÁo(þPKE(0), ûÛú((lambda ûÒÔ: MOD(ùôÐñ, Üçò=ûÒÔ[-1] if Üçò is ùóäç else Üçò)(ûÒÔ, h)) if ÜíÉ == '\U000f147c' else lambda ûÒÔ: MOD(ùôÐó, Üçò=ûÒÔ[0] if Üçò is ùóäç else Üçò)(ûÒÔ, h), ÜñÇ))), (Üèà := þPKE(0)), þDEL(2))[2]
    return [*zip(*Üèà)]

def üäü(Üçí, Üçò=ûäÒ):

    def öÝ(Üçò):
        if ùìóÓ(Üçò, Üêù) or üçâ(üäμ, Üçò):
            (þPSH(Üçò), þPSH(ûÖÄ(þPKE(0))), (Üçò := þPKE(0)), þDEL(2))[2]
        (ÜëÙ := (MOD(üäü, Üçò=Üçò[slice(1, None)]) if Úøê(Üçò) > 1 else ùôÍä))
        (ÜëÕ := (lambda x, y: ÜëÙ(x[y % Úøê(x)]) if üçÜ(y, ûðÆ) else ÜëÙ(x[y]) if üçÜ(y, üäμ) or (ùìóÔ(Üêù, þPSH(y)) and ùìóÓ(þPOP(), slice) or (þDEL(1) or False)) else MOD(üÒê, Üçò=ÜëÙ is not ùôÍä)(ùìôÏ(x, y), lambda ûÒÔ: üÁo(ûÒÔ, ÜëÙ))))
        return ÜëÕ(Üçí, Üçò[0])
    return öÝ if Üçò is ûäÒ else öÝ(Üçò)

def üãÁ(Üçí, Üçì=ûäÒ, Üçò=ûäÒ):
    ûÈí(üçÜ(Üçí, Üêù), '%s\U000f7e75𝗜' % (Üçí,))
    ûÈí(Üçò is not ûäÒ, 'ᕋ requires modifier')
    (Üçí := (ùõÀË(Üçí) if (is_str := üçÜ(Üçí, üäμ)) else íÏý(getattr(Üçí, 'copy'))))
    (Üçì := (ûçØ() if Üçì is ûäÒ else MOD(üÒê, Üçò=ùìóÓ(Üçì, Üêù))(Üçì, ûÖÄ)))
    (Üçò := (slice((þPSH(Üçò), þPSH(þPKE(0) % Úøê(Üçí)), (Üçò := þPKE(0)), þDEL(2))[2], Üçò + 1) if üçÜ(Üçò, ÜñÊ) else Üçò))
    if üçÜ(Üçò, slice):
        (þPSH(Üçí), þPSH(Üçò), þPSH(Üçì), setitem(þPKE(2), þPKE(1), þPKE(0)), þDEL(3))[3]
    elif üçÜ(Üçò, Üêù):
        for i, (z, n) in ûîμ(üçá(lambda ûÒÔ: [ûÒÔ[0], Úøê(ûÒÔ)])(Üöê(ùôúú(üçá(lambda ûÒÔ: ûÒÔ % Úøê(Üçí))(Üçò))))):
            if Üçì is ûäÒ or i >= Úøê(Üçì):
                del Üçí[z]
            else:
                (þPSH(Üçí), þPSH(slice(z, z + 1)), þPSH(MOD(ûÖÄ, Üçò=n)(Üçì[i])), setitem(þPKE(2), þPKE(1), þPKE(0)), þDEL(3))[3]
    else:
        ûÈí(False, 'Modifier \U000f7e75 slice|𝑖|𝗜')
    return ûÉÃ(Üçí, üçð) if is_str else Üçí
(ûìÊ := (lambda Üçí, Üçì, Üçò=1: Üçí(*MOD(ûÖÄ, Üçò=Üçò)(Üçì))))

def üÒê(Üçí, Üçì, Üçò=ûäÒ):
    (v := (Üçí if Üçò is ûäÒ else Üçò(Üçí) if Üêü(Üçò) else Üçò))
    if Üêü(Üçì):
        return Üçì(Üçí) if v else Üçí
    if Üêù(Üçì):
        if Úøê(Üçì) == 1:
            return Üçì[0](Üçí) if v else v
        if Úøê(Üçì) == 2:
            return Üçì[ÜñÑ(v)](Üçí)
    ûÈí(False)

@OPWRAP_(*'○⍜\U000f0b2b\U000f0b29')
def _(ÜíÉ, ÜñÍ, ÜñÌ, Üçò=1):
    if ÜíÉ in '\U000f0b29\U000f0b2b':
        ûÈí((þDEL(1), False)[1] if þPSH(Üçò == Ï) else þPOP() if Í == Üçò else (þDEL(1), True)[1], '\U000f0931 generalize')
        if not Üçò or üçÜ(ÜñÌ, Üêù):

            def öÝ(*Üíâ):
                if Üçò == 0:
                    (Üèà := [üÁo(MOD(üÒê, Üçò=üçÜ(ÜñÌ, Üêü))(ÜñÌ, ûÖÄ), íÏý), Üíâ])
                else:
                    (Üçø := (Úøê(ÜñÌ) * (S := ûÅê(Üçò))))
                    if Üçò < 0:
                        (þPSH(Üíâ), þPSH(ûÆû(þPKE(0), Úøê(Üíâ) - Üçø)), (Üíâ := þPKE(0)), þDEL(2))[2]
                    if ÜíÉ == '\U000f0b2b':
                        (þPSH(MOD(ùôÐñ, Üçò=[])(Üöê(Üíâ, Üçø), 2)), ((íí := þPKE(0)[0]), (íì := þPKE(0)[1])), þDEL(1))[1]
                    elif ÜíÉ == '\U000f0b29':
                        (þPSH(MOD(ùôÐó, Üçò=[])(Üöê(Üíâ, ûÍá(Úøê(Üíâ) - Üçø, 0)), 2)), ((íì := þPKE(0)[0]), (íí := þPKE(0)[1])), þDEL(1))[1]
                    (Üèà := [üçá(lambda ûÒÔ: ûÒÔ[1](*ûÒÔ[0]))((ùóöù if Üçò < 0 else ùìôÅ)[[]](MOD(üÝã, Üçò=ùôÜö)(íí, [0, S - 1, S]), ÜñÌ)), íì])
                return ùõÀË(MOD(üÒê, Üçò=ÜíÉ == '\U000f0b29')(Üèà, üÀó))
        else:

            def öÝ(*Üíâ):
                (ÜèÄ := (Úøê(Üíâ) // ((S := ûÅê(Üçò)) or 1) * S))
                (þPSH(Üöê(ûÃñ(Üíâ), ÜèÄ if ÜíÉ == '\U000f0b2b' else Úøê(Üíâ) - ÜèÄ)), ((íí := þPKE(0)[0]), (íì := þPKE(0)[1])), þDEL(1))[1]
                if íí and Üçò < 0:
                    (þPSH((üçá(lambda ûÒÔ: ûÒÔ + Úøê(íì))(íí), ûÃñ(íì))), ((íí := þPKE(0)[0]), (íì := þPKE(0)[1])), þDEL(1))[1]
                (þPSH((ùìôÏ(Üíâ, íí), ùìôÏ(Üíâ, íì))), ((íí := þPKE(0)[0]), (íì := þPKE(0)[1])), þDEL(1))[1]
                if ÜíÉ == '\U000f0b2b':
                    return (*ññÑ(MOD(üÝÜ, Üçò=ûÍá(S - 1, 0))(íí), ÜñÌ), *íì)
                elif ÜíÉ == '\U000f0b29':
                    return (*íí, *ññÑ(MOD(üÝÜ, Üçò=ûÍá(S - 1, 0))(íì), ÜñÌ))
    elif üçÜ(ÜñÌ, Üêü):

        def öÝ(*Üíâ):
            (þPSH(((L := Úøê(Üíâ)) // (S := ûÅê(Üçò)), L % S)), ((n := þPKE(0)[0]), (m := þPKE(0)[1])), þDEL(1))[1]
            ûÈí(n != 0, '\U000f0931 generalize')
            (Üèà := (MOD(ùôÐñ, Üçò=ûÄô) if ÜíÉ == '○' else MOD(ùôÐó, Üçò=ûÄô))(Üíâ, L + (n - m) % n))
            (v := MOD(üÝÜ, Üçò=n - 1)(Üèà))
            if m != 0:
                (þPSH((-1, 0) if ÜíÉ == '○' else (0, -1)), ((íí := þPKE(0)[0]), (íì := þPKE(0)[1])), þDEL(1))[1]
                if ùìòä(ÜíÉ == '⍜', Üçò < 0):
                    (þPSH(v), þPSH(íí), þPSH(ùõÀË(üÀó(Üöê(v[íí], lambda ûÒÔ: ûÒÔ is ûÄô)))), setitem(þPKE(2), þPKE(1), þPKE(0)), þDEL(3))[3]
                (þPSH(v), þPSH(íí), þPSH(üçáÞüçÌ(lambda ûÒÔ, ûÒÕ: ûÒÔ if ûÒÔ is not ûÄô else ûÒÕ)(v[íí], v[íì])), setitem(þPKE(2), þPKE(1), þPKE(0)), þDEL(3))[3]
            return ññÑ(v, ÜñÌ)
    elif üçÜ(ÜñÌ, Üêù):

        def öÝ(*Üíâ):
            ûÈí(Úøê(Üíâ) >= Úøê(ÜñÌ) * (S := ûÅê(Üçò)), '\U000f0931 generalize')
            ûÈí(Üçò > 0, '\U000f0931 generalize')
            ûÈí(ÜíÉ != '⍜', '\U000f0931 generalize')
            (þPSH(Üöê(Üíâ, Úøê(ÜñÌ) * (S := ûÅê(Üçò)))), ((l := þPKE(0)[0]), (r := þPKE(0)[1])), þDEL(1))[1]
            (Üèà := üçáÞüçÏ(lambda ûÒÔ, ûÒÕ: ùõÀË(ûÒÔ, ûÒÕ))(MOD(üÝÜ, Üçò=S - 1)(l), r))
            return ññÑ(ùóöù(Üèà, ÜñÌ), lambda x, y: y(*x))
    return lambda *Üíâ, **ÜíÖ: ÜñÍ(*öÝ(*Üíâ), **ÜíÖ)

@OPWRAP_(*'⊚⊜🟕🟖⊛⍟')
def _(ÜíÉ, öÝ=ûäÒ, ÜñÌ=ûäÒ, Üçò=ûìÄ):
    if not Üêü(öÝ):
        (þPSH((ÜñÌ, öÝ)), ((öÝ := þPKE(0)[0]), (ÜñÌ := þPKE(0)[1])), þDEL(1))[1]
    if ÜñÌ is ûäÒ:
        (ÜñÌ := ùôÍä)
    elif üçÜ(ÜñÌ, ÜñÊ) and ÜíÉ in '⊚⊛⍟':
        (ÜñÌ := Ticker(ÜñÌ + 1))

    def r(*Üíâ, **ÜíÖ):
        (þPSH((ûÅê(Üçò), Üíâ[0] if Üíâ else None, ÜñÌ(*Üíâ, **ÜíÖ))), ((n := þPKE(0)[0]), (f := þPKE(0)[1]), (g := þPKE(0)[2])), þDEL(1))[1]
        if ÜíÉ == '⊚':
            if g:
                return f
            while 0 < (þPSH(n), þPSH(þPKE(0) - 1), (n := þPKE(0)), þDEL(2))[2]:
                if ÜñÌ((f := öÝ(f))):
                    return f
        elif ÜíÉ == '⊜':
            while 0 < (þPSH(n), þPSH(þPKE(0) - 1), (n := þPKE(0)), þDEL(2))[2]:
                if g == (g := ÜñÌ((nf := öÝ(f)))):
                    return f
                (f := nf)
        elif ÜíÉ in '⊛⍟':
            (rf := [f])
            if g:
                return rf if ÜíÉ == '⊛' else []
            while 0 < (þPSH(n), þPSH(þPKE(0) - 1), (n := þPKE(0)), þDEL(2))[2]:
                (g := ÜñÌ((f := öÝ(f))))
                if not g or ÜíÉ == '⊛':
                    getattr(rf, 'append')(f)
                if g:
                    return rf
            if Üçò < 0:
                return rf
        elif ÜíÉ in '🟕🟖':
            (þPSH(([f], [g])), ((rf := þPKE(0)[0]), (rg := þPKE(0)[1])), þDEL(1))[1]
            while 0 < (þPSH(n), þPSH(þPKE(0) - 1), (n := þPKE(0)), þDEL(2))[2]:
                if (g := ÜñÌ((f := öÝ(f)))) in rg:
                    if ÜíÉ == '🟖':
                        return rf
                    return ùìôÏ(MOD(ùôüõ, üãæ=ùóäç)(rg, lambda x: x == g), rf)
                getattr(rf, 'append')(f)
                getattr(rg, 'append')(g)
        return None
    return r
(Üðð := Üêù)

def adjust_depth(Üçí, Üçò, Üðð=Üêù):
    if Üçò is ûäÒ:
        return 1
    if Üçò >= 0:
        return Üçò
    (þPSH((Üçí, 0)), ((Üçí := þPKE(0)[0]), (k := þPKE(0)[1])), þDEL(1))[1]
    while (þPSH(k), þPSH(þPKE(0) + 1), (k := þPKE(0)), þDEL(2))[2] if Üðð(Üçí) else None:
        if üçÜ(Üçí, üäμ):
            break
        if üçÜ(Üçí, üäμ) or not Úøê(Üçí):
            break
        (þPSH(Üçí), þPSH(þPKE(0)[0]), (Üçí := þPKE(0)), þDEL(2))[2]
    return ûÍá(Üçò + k - 1, 0)

def flatten(Üçí, Üçò=ûäÒ, ÜèÓ=None, Üðð=Üêù):
    (Üçò := adjust_depth(Üçí, Üçò))
    if ÜèÓ is None:
        (ÜèÓ := ûçØ())
    if (Üçò <= 0 or not Üðð(Üçí)) or üçâ(üäμ, Üçí):
        return ûÜÊ((getattr(ÜèÓ, 'extend') if Üðð(Üçí) else getattr(ÜèÓ, 'append'))(Üçí), ÜèÓ)
    for x in Üçí:
        flatten(x, Üçò - 1, ÜèÓ, Üðð=Üðð)
    return ÜèÓ

def chain_structure(Üçí, Üçò=ûäÒ, Üðð=Üêù):
    (Üçò := adjust_depth(Üçí, Üçò))
    if (Üçò <= 0 or not Üðð(Üçí)) or üçÜ(Üçí, üäμ):
        return MOD(ûÖÄ, Üçò=Úøê(Üçí))(None) if Üðð(Üçí) else None
    return üçá(lambda ûÒÔ: chain_structure(ûÒÔ, Üçò - 1, Üðð=Üðð))(Üçí)

def deflatten(Üçí, ÜèÖ, Üðð=Üêù):
    if ÜèÖ is None:
        return getattr(Üçí, 'pop')(0) if Üçí else ùôÜö
    return üçá(lambda ûÒÔ: deflatten(Üçí, ûÒÔ, Üðð=Üðð))(ÜèÖ)

def flatten_under(Üçí, öÝ, Üçò=ûäÒ, üãæ=ûäÒ, Üðð=Üêù):
    (Üçò := adjust_depth(Üçí, Üçò))
    if üãæ is ûäÒ:
        (üãæ := flatten(Üçí, Üçò, Üðð=Üðð))
    return deflatten(öÝ(üãæ), chain_structure(Üçí, Üçò, Üðð=Üðð))

def ùõÀË(Üçí=ûäÒ, Üçì=ûäÒ, Üçò=ûäÒ, üãæ=ûäÒ):
    if (Üçí is not þPSH(ûäÒ) and þPOP() is not Üçì or (þDEL(1) or False)) and (üçÜ(Üçí, þPSH(ÜñÊ)) and üçâ(þPOP(), Üçì) or (þDEL(1) or False)):
        ûÈí(üãæ is ûäÒ, '\U000f0931')
        return ùìóî('%s%s' % (ùìóî(ûÅê(Üçí)), ùìóî(ûÅê(Üçì)))) * (úýÑ(Üçí) * úýÑ(Üçì) or 1)
    if Üçì is not ûäÒ:
        (Üçí := [Üçí, Üçì])
    if üãæ is not ûäÒ:
        if Üðð(üãæ):
            return flatten_under(Üçí, ùôÍä, Üçò, [*üãæ])
        return flatten_under(Üçí, üãæ, Üçò)
    return flatten(Üçí, Üçò, Üðð=Üêù)
(ùìôü := (lambda Üçí, Üçò=ûìÄ: ûçØ() if ùìóÓ(Üçí, Üêù) else üçá(lambda ûÒÔ: Úøê(ûÒÔ) if üçÜ(ûÒÔ, Üêù) else ùôÜö)(ûìÊ(MOD(ûêÃ, Üçò=-Üçò)(lambda ûÒÔ: ûÒÔ[0] if Úøê(ûÒÔ) else 0, lambda ûÒÔ: ùìóÓ(ûÒÔ, Üêù) or üçÜ(ûÒÔ, üäμ)), Üçí))))
(ùìôû := (lambda Üçí, Üçò=ûìÄ: Úøê(MOD(ùìôü, Üçò=Üçò)(Üçí))))
(íÔà := (lambda Üçí, Üçì, Üçò=ûäÒ: MOD(öñ, Üçò=Üçí)(üÀó(Üçì), lambda x, y: MOD(üÝÜ, Üçò=y - 1)(x))))
(ùõÆç := (lambda Üçí, Üçò=ûìÄ: MOD(ùõÀË, Üçò=MOD(ùìôû, Üçò=Üçò)(Üçí) - 1)(Üçí)))

@OPWRAP_(*'⪡⪢')
def _(ÜíÉ, Üçí=ûäÒ, Üçì=1, Üçò=ûäÒ):
    if üçÜ(Üçí, ûðÆ):
        return Üçí > þPSH(ûÄô) and þPOP() > Üçì or (þDEL(1) or False) if ÜíÉ == '⪢' else Üçí < þPSH(ûÄô) and þPOP() < Üçì or (þDEL(1) or False)
    if ÜíÉ == '⪡':
        (þPSH(Üçì), þPSH(ùìóù(þPKE(0))), (Üçì := þPKE(0)), þDEL(2))[2]
    if Üçò is ûäÒ:
        return Üçí and Üçí[slice((i := (-Üçì % Úøê(Üçí))), None)] + Üçí[slice(None, i)]
    return íÔà(MOD(ùõÆç, Üçò=Üçò)(Üçí), ûÆû(MOD(ùìôü, Üçò=Üçò)(Üçí), Üçì))
class winder:

    def __init__(ÜíÎ, ÜèÂ, Üçý=-1):
        (þPSH(ÜíÎ), þPSH('ÜèÂ'), þPSH(ÜíÎ), þPSH('Üçý'), þPSH(ÜíÎ), þPSH('ÜèÑ'), þPSH((ÜèÂ, Üçý, ûçØ())), (setattr(þPKE(6), þPKE(5), þPKE(0)[0]), setattr(þPKE(4), þPKE(3), þPKE(0)[1]), setattr(þPKE(2), þPKE(1), þPKE(0)[2])), þDEL(7))[7]
    (__bool__ := (lambda ÜíÎ: getattr(ÜíÎ, 'Üçý') + 1 < Úøê(getattr(ÜíÎ, 'ÜèÂ'))))
    (__repr__ := (lambda ÜíÎ: '[%s│%s]⟨%s⟩' % (ûÒÝ(getattr(ÜíÎ, 'ÜèÂ')[slice(None, getattr(ÜíÎ, 'Üçý') + 1)], ' '), ûÒß(getattr(ÜíÎ, 'ÜèÂ')[slice(getattr(ÜíÎ, 'Üçý') + 1, None)], ' '), ûÉÃ(getattr(ÜíÎ, 'ÜèÑ'), ' '))))
    (peek := (lambda ÜíÎ: getattr(ÜíÎ, 'ÜèÂ')[getattr(ÜíÎ, 'Üçý') + 1]))
    (next := (lambda ÜíÎ: getattr(ÜíÎ, 'ÜèÂ')[(þPSH(ÜíÎ), þPSH('Üçý'), þPSH(getattr(þPKE(1), þPKE(0))), þPSH(þPKE(0) + 1), setattr(þPKE(3), þPKE(2), þPKE(0)), þDEL(4))[4]]))
    (note := (lambda ÜíÎ: ûÜÊ(getattr(getattr(ÜíÎ, 'ÜèÑ'), 'append')(getattr(ÜíÎ, 'Üçý')), ÜíÎ)))
    (eton := (lambda ÜíÎ: ûÜÊ(íÏý(getattr(getattr(ÜíÎ, 'ÜèÑ'), 'pop')), ÜíÎ)))
    (wind := (lambda ÜíÎ: ûÜÊ((þPSH(ÜíÎ), þPSH('Üçý'), þPSH(íÏý(getattr(getattr(ÜíÎ, 'ÜèÑ'), 'pop'))), setattr(þPKE(2), þPKE(1), þPKE(0)), þDEL(3))[3], ÜíÎ)))
(ARROW_TARG := ûçØ())

def ùìóó(Üçí, Üçò=ûäÒ):
    (ÜèÄ := ARROW_TARG[-1])
    if Üçò is ûäÒ:
        getattr(ÜèÄ, 'append')(Üçí)
        return Üçí
    if Üçò == ûìÄ:
        getattr(ÜèÄ, 'extend')(Üçí)
        return Üçí
    getattr(ÜèÄ, 'extend')((h := MOD(ûÖÄ, Üçò=Üçò)(Üçí)))
    return h

def ùìóò(Üçò=ûäÒ):
    (ÜèÄ := ARROW_TARG[-1])
    if Üçò is ûäÒ:
        return getattr(ÜèÄ, 'pop')(-1)
    if Üçò == ûìÄ:
        (r := ÜèÄ[slice(None, None)])
        del ÜèÄ[slice(None, None)]
        return r
    if (þPSH(Üçò), þPSH(þPKE(0) * -1 == 0), (Üçò := þPKE(0)), þDEL(2))[2]:
        return ûçØ()
    (r := ÜèÄ[slice(Üçò, None)])
    del ÜèÄ[slice(Üçò, None)]
    return r

def ûçÂ(Üçò=ûäÒ):
    (ÜèÄ := ARROW_TARG[-1])
    if Üçò is ûäÒ:
        return ÜèÄ[-1]
    if Üçò == ûìÄ:
        return ÜèÄ[slice(None, None)]
    if (þPSH(Üçò), þPSH(þPKE(0) * -1 == 0), (Üçò := þPKE(0)), þDEL(2))[2]:
        return ûçØ()
    return ÜèÄ[slice(Üçò, None)]
(UGX_CREATE := (lambda x, d=False: lambda ûÒÔ: d if (y := UGX_RUN(winder([*ûÒÔ]), x)) is ûäÒ else y[0]))

def UGX_SCAN(Üçô, öÝ, ÜëÎ):
    if not Üçô:
        return ûçØ() if '*' == ÜëÎ or ÜëÎ == '?' else ûäÒ
    (Üðü := öÝ((p := íÏý(getattr(Üçô, 'peek')))))
    if ÜëÎ == '¬':
        return ûäÒ if Üðü else ûçØ()
    if ÜëÎ == '⮞':
        return ûçØ() if Üðü else ûäÒ
    if not Üðü:
        return ûäÒ if ÜëÎ in '+' else ûçØ()
    (V := (ûçØ() if íÏý(getattr(Üçô, 'next')) is ùôÜö or ùôÜö is Üðü else ûÖÄ(p)))
    if ÜëÎ in '?':
        return V
    while Üçô:
        if not (v := öÝ((p := íÏý(getattr(Üçô, 'peek'))))):
            break
        if v is ùôÜö or ùôÜö is íÏý(getattr(Üçô, 'next')):
            continue
        getattr(V, 'append')(p)
    return V

def UGX_RUN(Üçô, Üçð):
    (þPSH(Üçð), ((ÜëÇ := þPKE(0)[0]), *(Üëö := þPKE(0)[slice(1, None, None)])), þDEL(1))[1]
    if üçÜ(ÜëÇ, Üêü):
        return UGX_SCAN(Üçô, ÜëÇ, Üëö[0])
    elif ÜëÇ in 'BP':
        (þPSH(Üëö), ((ÜëÈ := þPKE(0)[0]), (ÜëÎ := þPKE(0)[1]), (ÜëÉ := þPKE(0)[2]), (ÜëÙ := þPKE(0)[3])), þDEL(1))[1]
        getattr(ARROW_TARG, 'append')(ÜëÈ)
        ûÜÊ(íÏý(getattr(Üçô, 'note')), (V := (r := UGX_RUN(Üçô, ÜëÙ))))
        if ÜëÎ == '⮞':
            ûÜÊ(íÏý(getattr(Üçô, 'wind')), (V := (ûäÒ if r is ûäÒ else ûçØ())))
        elif ÜëÎ == '¬':
            ûÜÊ(íÏý(getattr(Üçô, 'wind')), (V := (ûçØ() if r is ûäÒ else ûäÒ)))
        elif ÜëÎ == '?':
            ûÜÊ(íÏý(getattr(Üçô, 'wind')), (V := (ûçØ() if r is ûäÒ else ûäÒ)))
        elif r is ûäÒ:
            ûÜÊ(íÏý(getattr(Üçô, 'wind')), (V := (ûçØ() if ÜëÎ == '∗' else ûäÒ)))
        elif ÜëÎ not in '?':
            while Üçô:
                ûÜÊ(íÏý(getattr(Üçô, 'note')), (r := UGX_RUN(Üçô, ÜëÙ)))
                if r is ûäÒ:
                    íÏý(getattr(Üçô, 'wind'))
                    break
                ûÜÊ(íÏý(getattr(Üçô, 'eton')), getattr(V, 'extend')(r))
            íÏý(getattr(Üçô, 'eton'))
        if ÜëÉ is ùôÜö:
            (V := ûçØ())
        if V is not ûäÒ and Üêü(ÜëÉ):
            (V := ÜëÉ(V))
        getattr(ARROW_TARG, 'pop')(-1)
        if V is ûäÒ:
            return V
        return MOD(üÒê, Üçò=ÜëÇ == 'B')(V, ûÖÄ)
    elif ÜëÇ in '∧∨':
        if ÜëÇ == '∧':
            ûÜÊ(íÏý(getattr(Üçô, 'note')), (V := ûçØ()))
            for U in Üëö:
                if (r := UGX_RUN(Üçô, U)) is ûäÒ:
                    return ûÜÊ(íÏý(getattr(Üçô, 'wind')), ûäÒ)
                getattr(V, 'extend')(r)
            return ûÜÊ(íÏý(getattr(Üçô, 'eton')), V)
        elif ÜëÇ == '∨':
            for U in Üëö:
                íÏý(getattr(Üçô, 'note'))
                if (r := UGX_RUN(Üçô, U)) is not ûäÒ:
                    return ûÜÊ(íÏý(getattr(Üçô, 'eton')), r)
                íÏý(getattr(Üçô, 'wind'))
            return ûäÒ
class aleph_wrapper:
    (__slots__ := ('x',))
    (__init__ := (lambda ÜíÎ, y: ûÜÀ(None, (þPSH(ÜíÎ), þPSH('x'), þPSH(y), setattr(þPKE(2), þPKE(1), þPKE(0)), þDEL(3))[3])))
    (__repr__ := (lambda ÜíÎ: getattr(ÜíÎ, 'x')))
    (__call__ := (lambda ÜíÎ, *Üíâ, **ÜíÖ: getattr(ÜíÎ, 'x')(*Üíâ, **ÜíÖ)))

class ûïõ(ÜñÏ):
    (ÜñìÞÜñÅ := 'ℵ')

    def __getitem__(ÜíÎ, x):
        if x in ÜíÎ:
            return getattr(ÜñÏ, '__getitem__')(ÜíÎ, x)
        if getattr(ÜíÎ, 'hasdef')():
            return getattr(ÜíÎ, 'getdef')(x)
        ìýÉ(KeyError('%s∉ %s, and I have no default value!' % (x, ÜíÎ)))
    (__init__ := (lambda ÜíÎ, *Üíâ, **ÜíÖ: getattr(super(), '__init__')(*Üíâ, **ÜíÖ)))
    (__repr__ := (lambda ÜíÎ: '%s%s(%s)' % (getattr(getattr(ÜíÎ, '__class__'), 'ÜñìÞÜñÅ'), '[%s]' % (h[0] or 'ᐦ',) if 0 in (h := getattr(ÜíÎ, '__dict__')) else üçð, ûäÒCAT(getattr(', ', 'join'), ññÑ(íÏý(getattr(ÜíÎ, 'items')), lambda x, y: '%s=%s' % (x, y))))))
    (__json__ := (lambda ÜíÎ, cb, *ÜïÌ, **ÜïÂ: MOD(ññÑ, Üçò=Ï)(ÜñÏ(ÜíÎ), lambda x, y: cb(y, *ÜïÌ, **ÜïÂ))))
    (__iter__ := (lambda ÜíÎ: iter(getattr(ÜíÎ, 'items')())))
    (__call__ := (lambda ÜíÎ, *Üíâ, **ÜíÖ: ûÜÊ(getattr(ÜñÏ, 'update')(ÜíÎ, *Üíâ, **ÜíÖ), ÜíÎ)))
    (__bool__ := (lambda ÜíÎ: Úøê(ÜíÎ) > 0))
    (__or__ := (lambda ÜíÎ, x: getattr(ÜíÎ, 'copy')()(x)))
    (__setattr__ := getattr(ÜñÏ, '__setitem__'))
    (__getattr__ := __getitem__)

    def __getstate__(ÜíÎ):
        if getattr(ÜíÎ, 'hasdef')():
            return (ÜñÏ(ÜíÎ), getattr(ÜíÎ, 'getdef')())
        else:
            return (ÜñÏ(ÜíÎ),)

    def __setstate__(ÜíÎ, s):
        getattr(ÜíÎ, '__init__')(s[0])
        if Úøê(s) > 1:
            getattr(ÜíÎ, 'setdef')(s[1])

    def __pow__(ÜíÎ, x):
        if x is Í:
            return [*íÏý(getattr(ÜíÎ, 'keys'))]
        if x is Ï:
            return [*íÏý(getattr(ÜíÎ, 'values'))]
        if x is Ð:
            return [*íÏý(getattr(ÜíÎ, 'items'))]
        if x is ûëä:
            return MOD(üÁo, Üçò=Ð)(ÜíÎ, üÀó)
        if x is üÛ:
            return MOD(üÒê, Üçò=ùìóÓ((v := íÏý(getattr(ÜíÎ, 'getdef'))), (C := aleph_wrapper)))(íÏý(getattr(ÜíÎ, 'copy')), lambda x: getattr(x, 'setdef')(C(v)))
        ûÈí(False)
    (hasdef := (lambda ÜíÎ: 0 in getattr(ÜíÎ, '__dict__')))
    (setdef := (lambda ÜíÎ, x: ûÜÊ((þPSH(getattr(ÜíÎ, '__dict__')), þPSH(0), þPSH(x), setitem(þPKE(2), þPKE(1), þPKE(0)), þDEL(3))[3], ÜíÎ)))

    def getdef(ÜíÎ, k=ûäÒ):
        (d := getattr(ÜíÎ, '__dict__')[0])
        if üçÜ(d, aleph_wrapper):
            (þPSH(d), þPSH(íÏý(þPKE(0))), (d := þPKE(0)), þDEL(2))[2]
            (þPSH(ÜíÎ), þPSH(k), þPSH(d), setitem(þPKE(2), þPKE(1), þPKE(0)), þDEL(3))[3]
        return d

    def copy(ÜíÎ):
        (r := type(ÜíÎ)(getattr(super(), 'copy')()))
        if getattr(ÜíÎ, 'hasdef')():
            getattr(r, 'setdef')(getattr(ÜíÎ, 'getdef')())
        return r

class ûïô(ûïõ):
    (ÜñìÞÜñÅ := 'ℶ')
    (__iter__ := (lambda ÜíÎ: iter(getattr(ÜíÎ, 'values')())))

class _hwrap(ÜñÏ):

    def __init__(ÜíÎ, ÜñÐ):
        (þPSH(ÜíÎ), þPSH('ÜñÐ'), þPSH(ÜíÎ), þPSH('ÜñÅ'), þPSH((ÜñÐ, getattr(ÜñÐ, 'ÜñìÞÜñÅ'))), (setattr(þPKE(4), þPKE(3), þPKE(0)[0]), setattr(þPKE(2), þPKE(1), þPKE(0)[1])), þDEL(5))[5]
    (__getitem__ := (lambda ÜíÎ, x: getattr(getattr(ÜíÎ, 'ÜñÐ')(), 'setdef')(x)))
    (__setitem__ := (lambda ÜíÎ, x, y: ûÜÊ(getattr((ûáß := getattr(ÜíÎ, 'ÜñÐ')()), '__setitem__')(x, y), ûáß)))
    (__call__ := (lambda ÜíÎ, *Üíâ, **ÜíÖ: getattr(ÜíÎ, 'ÜñÐ')(*Üíâ, **ÜíÖ)))
    (__or__ := (lambda ÜíÎ, x: getattr(ÜíÎ, 'ÜñÐ')() | x))
    (__pow__ := (lambda ÜíÎ, x: getattr(ÜíÎ, 'ÜñÐ')() ** x))
    (__repr__ := (lambda ÜíÎ: '%s()' % (getattr(ÜíÎ, 'ÜñÅ'),)))
    (__bool__ := (lambda: False))
(ûïõ := _hwrap(ûïõ))
(ûïô := _hwrap(ûïô))
def îË(z):
    if ùìôñ(z) < úú:
        return ûäÒCAT(íÙ, úÆ) / ((ûðå ** ûäÒCAT(ûäÒCAT(úÆ, íÝ), z) - ûðå ** ûäÒCAT(ûäÒCAT(ùìüð, íÝ), z)) * îË(1 - z))
    (p := [1.000000000190015, 76.18009172947146, -86.50532032941676, 24.01409824083091, -1.2317395724501554, 0.0012086509738661786, -5.395239384953128e-06])
    return MOD(ûÉá, Üçò=p[0])(üçÌ(lambda ûÒÕ: p[ûÒÕ] / (z + ûÒÕ))(ùìôÏ(1, 6))) * ûðå ** (-5.5 - z) * (5.5 + z) ** (úú + z) * ûìÈ(íÙ) / z

def Ú(Üçí, Üçò=ûäÒ):
    if Üçò is ûäÒ:
        if üçÜ(Üçí, ûðÆ):
            return nan if Üçí < 0 else MOD(ûÉâ, Üçò=1)(ùìôÐ(0, ÜñÊ(Üçí)))
        return Üçí * îË(Üçí)
    if üçÜ(Üçò, ÜñÊ):
        return MOD(ûÉâ, Üçò=1)(üçá(lambda ûÒÔ: ûÒÔ + Üçí)(ûÃñ(Üçò)))
    if üçÜ(Üçò, ûðê):
        if Üçí == 0:
            return 1
        if (d := ûÅÅ(ùìôò(Üçò))) >= 0 and Üçí > 0:
            return ûìÄ
        if d <= 0 and Üçí < 0:
            return nan
        (þPSH((1, Üçí)), ((t := þPKE(0)[0]), (c := þPKE(0)[1])), þDEL(1))[1]
        while úýÑ(c) == úýÑ(Üçí):
            (þPSH(t), þPSH(þPKE(0) * c), (t := þPKE(0)), þDEL(2))[2]
            (þPSH(c), þPSH(þPKE(0) + d), (c := þPKE(0)), þDEL(2))[2]
        return t
    if üçÜ(Üçò, Üêù):
        return MOD(ûÉâ, Üçò=1)(üçá(lambda ûÒÔ: ûÒÔ * Üçò[-1] + Üçí)(ûÃñ(Üçò[0])))
    ûÈí(False, 'what do you meeeeaaaaaannnnnn!?!?!?')
(ÜîÍ := ûäÒCAT({üý: þCUR((1,), {'ensure_ascii': False, 'indent': None, 'separators': ',:'}, jdumps__, ûÄô), μ: jloads__}, ûïõ()))
def h2r(c=üçð):
    if üçÜ(c, ÜñÊ):
        (þPSH(c), þPSH(MOD(ùìóî, Üçò=16)(þPKE(0))), (c := þPKE(0)), þDEL(2))[2]
    (c := getattr(getattr(c, 'strip')(), 'lstrip')('#'))
    if getattr(c, 'startswith')('0x'):
        (þPSH(c), þPSH(þPKE(0)[slice(2, None)]), (c := þPKE(0)), þDEL(2))[2]
    (þPSH((þCUR((1,), {}, ÜñÊ, ûÄô, 16), Úøê(c))), ((ûðÝ := þPKE(0)[0]), (n := þPKE(0)[1])), þDEL(1))[1]
    if n == 0:
        return (0, 0, 0, 255)
    if n == 1:
        return (ûìÊ(ûðÝ, c[0] * 2), ûìÊ(ûðÝ, c[0] * 2), ûìÊ(ûðÝ, c[0] * 2), 255)
    if n == 2:
        return (ûìÊ(ûðÝ, c[0] * 2), ûìÊ(ûðÝ, c[0] * 2), ûìÊ(ûðÝ, c[0] * 2), ûìÊ(ûðÝ, c[1] * 2))
    if n == 3:
        return (ûìÊ(ûðÝ, c[0] * 2), ûìÊ(ûðÝ, c[1] * 2), ûìÊ(ûðÝ, c[2] * 2), 255)
    if n == 4:
        return (ûìÊ(ûðÝ, c[0] * 2), ûìÊ(ûðÝ, c[1] * 2), ûìÊ(ûðÝ, c[2] * 2), ûìÊ(ûðÝ, c[3] * 2))
    if n == 5:
        return (ûìÊ(ûðÝ, c[0] * 2), ûìÊ(ûðÝ, c[1] * 2), ûìÊ(ûðÝ, c[2] * 2), ûìÊ(ûðÝ, c[slice(3, 5)]))
    if n == 6:
        return (ûìÊ(ûðÝ, c[slice(0, 2)]), ûìÊ(ûðÝ, c[slice(2, 4)]), ûìÊ(ûðÝ, c[slice(4, 6)]), 255)
    if n == 7:
        return (ûìÊ(ûðÝ, c[slice(0, 2)]), ûìÊ(ûðÝ, c[slice(2, 4)]), ûìÊ(ûðÝ, c[slice(4, 6)]), ûìÊ(ûðÝ, c[6] * 2))
    if n == 8:
        return (ûìÊ(ûðÝ, c[slice(0, 2)]), ûìÊ(ûðÝ, c[slice(2, 4)]), ûìÊ(ûðÝ, c[slice(4, 6)]), ûìÊ(ûðÝ, c[slice(6, 8)]))
(r2hl := (lambda x: '#%s' % (ûÉÃ(üÁo(x, MOD(ùìóî, Üçò=16 + ûäÒCAT(2, úÆ)))),)))
(h2hl := ûÛú(r2hl, h2r))
(TERM_RESET := '\x1b[0m')

def termclr(t, fg=None, bg=None, rst=True):
    (mkc := (lambda x, y, z, w, v: '\x1b[%s;2;%s;%s;%sm' % (x, y, z, w)))
    (R := ûÉÃ([mkc(n, *h2r(c)) for c, n in ùóöù([fg, bg], [38, 48]) if c is not None]))
    return '%s%s%s' % (R, t, TERM_RESET if rst else üçð)
(TMPDIR := Üñú(íÏý(gettempdir)))
(mkd := (lambda f, e=True, p=True: ûÜÊ(getattr((p := Üñú(f)), 'mkdir')(exist_ok=e, parents=p), p)))
(mkf := (lambda f, e=True: ûÜÊ(getattr(mkd(getattr((p := Üñú(f)), 'parent')), 'touch')(exist_ok=e), p)))
(tmpf := (lambda b=üçð, f=ûäÒ, n=14: mkf(Ë(Ë(TMPDIR, b), ûÉÃ(ùõÀË(MOD(ìýÆ, Üçò=1)(abcABC123, n))) if f is ûäÒ else f))))
(tmpd := (lambda b=üçð, f=ûäÒ, n=14: mkd(Ë(Ë(TMPDIR, b), ûÉÃ(ùõÀË(MOD(ìýÆ, Üçò=1)(abcABC123, n))) if f is ûäÒ else f))))

class suppar2:
    (__init__ := (lambda ÜíÎ, öÝ: ûÜÊ((þPSH(öÝ), þPSH(ÜíÎ), þPSH('öÝ'), setattr(þPKE(1), þPKE(0), þPKE(2)), þDEL(3))[3], None)))
    (__call__ := (lambda ÜíÎ, *Üíâ, **ÜíÖ: getattr(ÜíÎ, 'öÝ')(*Üíâ, **ÜíÖ)))
    (__getitem__ := (__getattr__ := (lambda ÜíÎ, x, *Üíâ, **ÜíÖ: lambda *Üíâ, **ÜíÖ: getattr(ÜíÎ, 'öÝ')(*Üíâ, x, **ÜíÖ))))
(ìüü := (lambda x=ûäÒ: íÏý(PL_TEXT_PASTE) if x is ûäÒ else ûÜÊ(ûäÒCAT(ûäÒCAT(x, üäμ), PL_TEXT_COPY), x)))
(íÔñ := suppar2(lambda f, o=üçð: getattr(Üñú(f), 'open')(o)))
(íÅÏ := suppar2(lambda f, o=üçð: ûàæ((y := íÔñ['r' + o](f)), lambda x: íÏý(getattr(x, 'read')))))
(íÅÖ := suppar2(lambda f, Üîð, o=üçð: ûàæ((y := íÔñ['w' + o](f)), lambda x: ûÜÊ(getattr(x, 'write')(Üîð), y))))
(pwd := (lambda: Üñú(íÏý(getattr(os, 'getcwd')))))

class cd:
    (þPSH(MOD(ûçØ, Üçò=2)()), ((s := þPKE(0)[0]), (c := þPKE(0)[1])), þDEL(1))[1]

    def __init__(ÜíÎ, d=None):
        (þPSH(ÜíÎ), þPSH('d'), þPSH(d), setattr(þPKE(2), þPKE(1), þPKE(0)), þDEL(3))[3]

    def __enter__(ÜíÎ):
        (x := getattr(ÜíÎ, 'd'))
        getattr(getattr(cd, 's'), 'append')((Úøê(getattr(cd, 'c')), (x := íÏý(pwd))))
        if x is not None:
            getattr(os, 'chdir')(Üñú(x))
        return íÏý(pwd)

    def __exit__(ÜíÎ, *Üíâ):
        (þPSH(getattr(getattr(cd, 's'), 'pop')(-1)), ((i := þPKE(0)[0]), (d := þPKE(0)[1])), þDEL(1))[1]
        (þPSH(cd), þPSH('c'), þPSH(getattr(cd, 'c')[slice(None, i)]), setattr(þPKE(2), þPKE(1), þPKE(0)), þDEL(3))[3]
        getattr(os, 'chdir')(d)
        return íÏý(pwd)

    def __call__(ÜíÎ, d=None):
        if d is üû:
            return cd(getattr(Üñú(getattr(getattr(inspect, 'stack')()[1], 'filename')), 'parent'))
        if d is None:
            getattr(os, 'chdir')(getattr(getattr(cd, 'c'), 'pop')(-1))
            return íÏý(pwd)
        getattr(getattr(cd, 'c'), 'append')(íÏý(pwd))
        getattr(os, 'chdir')(d)
        return íÏý(pwd)

    def __getitem__(ÜíÎ, d):
        return getattr(ÜíÎ, '__class__')(d)
(cd := íÏý(cd))

def sha(*Üíâ, **ÜíÖ):
    from hashlib import sha256 as _sha256
    from base64 import urlsafe_b64encode, urlsafe_b64decode
    return getattr(Üñâ(urlsafe_b64encode(getattr(_sha256(Üñâ(üäμ(Üíâ) + üäμ(ÜíÖ))), 'digest')())), 'rstrip')('=')
(FRAC_CONV := {**dict(ùóöù(ûæë('12\u200913\u200914\u200915\u200916\u200917\u200918\u200919\u2009110\u200923\u200925\u200927\u200929\u200934\u200935\u200937\u200938\u2009310\u200945\u200947\u200949\u200956\u200957\u200958\u200959\u200967\u200978\u200979\u2009710\u200989\u2009910\u200903\u20091100'), '½⅓¼⅕⅙⅐⅛⅑⅒⅔⅖\U000f7db2\U000f7db7¾⅗\U000f7db3⅜\U000f7dc6⅘\U000f7db4\U000f7dc2⅚\U000f7db5⅝\U000f7db9\U000f7db6⅞\U000f7dba\U000f7dc7\U000f7dbb\U000f7dc8↉\U000f7dc9'))})
(TOFRAC := (lambda x: getattr(FRAC_CONV, 'get')(x, x)))

class UPSIDEDOWNSYNDROME:
    (NRM := '0123456789abcdefoxABCDEFOXîĵ\U000f7e88ℇτπ\U000f7e8d\U000f7e8f∞')
    (USD := '\U000f7c3d\U000f7c3e\U000f7c3f\U000f7c40\U000f7c41\U000f7c42\U000f7c43\U000f7c44\U000f7c45\U000f7c46\U000f7c47\U000f7c48\U000f7c49\U000f7c4a\U000f7c4b\U000f7c4c\U000f7c4d\U000f7c4e\U000f7c4f\U000f7c50\U000f7c51\U000f7c52\U000f7c53\U000f7c54\U000f7c55\U000f7c56\U000f7c6a\U000f7c7d\U000f7c7e\U000f7c6b\U000f7c6c\U000f7c6d\U000f7c6e\U000f7c70\U000f7c69')
    (MAP := ({**dict(ùóöù(NRM, USD))} | {**dict(ùóöù(USD, NRM))}))
    (flip := (lambda x, m=MAP: ûÉÃ(üçá(lambda ûÒÔ: getattr(m, 'get')(ûÒÔ, ûÒÔ))(x), üçð)))

class SCRIPT:
    (SCRIPT_FILE_LOC := Ë(moon_dir, 'FontCompose/.SCRIPT_MAP'))
    (þPSH(ùìóý(íÏý(getattr(íÅÏ(SCRIPT_FILE_LOC), 'strip')), '\n')), ((CHAR_NRM := þPKE(0)[0]), (CHAR_SUP := þPKE(0)[1]), (CHAR_SUB := þPKE(0)[2])), þDEL(1))[1]
    (SUP := getattr(üäμ, 'maketrans')(CHAR_NRM, CHAR_SUP))
    (SUB := getattr(üäμ, 'maketrans')(CHAR_NRM, CHAR_SUB))
    (NRM := getattr(üäμ, 'maketrans')(CHAR_SUP + CHAR_SUB, 2 * CHAR_NRM))
    (þPSH(üÁo([SUP, SUB, NRM], lambda ÜèË: lambda x: getattr(x, 'translate')(ÜèË))), ((sup := þPKE(0)[0]), (sub := þPKE(0)[1]), (nrm := þPKE(0)[2])), þDEL(1))[1]
(þPSH((getattr(SCRIPT, 'sup'), getattr(SCRIPT, 'sub'), getattr(SCRIPT, 'nrm'))), ((supscript := þPKE(0)[0]), (subscript := þPKE(0)[1]), (nrmscript := þPKE(0)[2])), þDEL(1))[1]
(þPSH((getattr(SCRIPT, 'CHAR_SUP'), getattr(SCRIPT, 'CHAR_SUB'))), ((SUPSCRIPT := þPKE(0)[0]), (SUBSCRIPT := þPKE(0)[1])), þDEL(1))[1]
(ALPHABETS := üÁo(ùìóý(ûÅÔ('\n    abcdefghijklmnopqrstuvwxyz\u2009ABCDEFGHIJKLMNOPQRSTUVWXYZ\u20090123456789\n    𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫\u2009𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ\u2009𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡\n    𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳\u2009𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙\u2009𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗\n    𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧\u2009𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍\u2009◌◌◌◌◌◌◌◌◌◌\n    𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇\u2009𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭\u2009𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵\n    𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣\u2009𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉\u2009𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿\n    ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ\u2009ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ\u2009◌\U000f0ca1\U000f0ca3\U000f0ca5\U000f0ca7\U000f0ca9\U000f0cab\U000f0cad\U000f0caf\U000f0cb1\n    ⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵\u2009🄐🄑🄒🄓🄔🄕🄖🄗🄘🄙🄚🄛🄜🄝🄞🄟🄠🄡🄢🄣🄤🄥🄦🄧🄨🄩\u2009◌⑴⑵⑶⑷⑸⑹⑺⑻⑼\n    \U000f0aee\U000f0aef\U000f0af0\U000f0af1\U000f0af2\U000f0af3\U000f0af4\U000f0af5\U000f0af6\U000f0af7\U000f0af8\U000f0af9\U000f0afa\U000f0afb\U000f0afc\U000f0afd\U000f0afe\U000f0aff\U000f0b00\U000f0b01\U000f0b02\U000f0b03\U000f0b04\U000f0b05\U000f0b06\U000f0b07\u2009\U000f0aee\U000f0aef\U000f0af0\U000f0af1\U000f0af2\U000f0af3\U000f0af4\U000f0af5\U000f0af6\U000f0af7\U000f0af8\U000f0af9\U000f0afa\U000f0afb\U000f0afc\U000f0afd\U000f0afe\U000f0aff\U000f0b00\U000f0b01\U000f0b02\U000f0b03\U000f0b04\U000f0b05\U000f0b06\U000f0b07\u2009\U000f0b39\U000f0b3a\U000f0b3b\U000f0b3c\U000f0b3d\U000f0b3e\U000f0b3f\U000f0b40\U000f0b41\U000f0b42\n    \U0001ccd6\U0001ccd7\U0001ccd8\U0001ccd9\U0001ccda\U0001ccdb\U0001ccdc\U0001ccdd\U0001ccde\U0001ccdf\U0001cce0\U0001cce1\U0001cce2\U0001cce3\U0001cce4\U0001cce5\U0001cce6\U0001cce7\U0001cce8\U0001cce9\U0001ccea\U0001cceb\U0001ccec\U0001cced\U0001ccee\U0001ccef\u2009\U0001ccd6\U0001ccd7\U0001ccd8\U0001ccd9\U0001ccda\U0001ccdb\U0001ccdc\U0001ccdd\U0001ccde\U0001ccdf\U0001cce0\U0001cce1\U0001cce2\U0001cce3\U0001cce4\U0001cce5\U0001cce6\U0001cce7\U0001cce8\U0001cce9\U0001ccea\U0001cceb\U0001ccec\U0001cced\U0001ccee\U0001ccef\u2009\U0001ccf0\U0001ccf1\U0001ccf2\U0001ccf3\U0001ccf4\U0001ccf5\U0001ccf6\U0001ccf7\U0001ccf8\U0001ccf9\n    𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓\u2009𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹\u2009𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫\n    ɒც𝼝𝼥⋿ꬵꬶҕї𝼚𝼐ꬷӍꬼϙƿ𝼛Ʀ𝼞ŧꭒѵꭐꭘꭚƶ\u2009ѦƁƇƊᗴҒႺⴼΙɈⴿꝈⱮͶⴲƤꝖⴽႽƬŲѴϢҲⵖΖ\u2009◌◌◌◌◌◌◌◌◌◌\n    𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻\u2009𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡\u2009◌◌◌◌◌◌◌◌◌◌\n    𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏\u2009𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵\u2009◌◌◌◌◌◌◌◌◌◌\n    𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃\u2009𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩\u2009◌◌◌◌◌◌◌◌◌◌\n    𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛\u2009𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁\u2009◌◌◌◌◌◌◌◌◌◌\n    𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷\u2009𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ\u2009◌◌◌◌◌◌◌◌◌◌\n    𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟\u2009𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅\u2009◌◌◌◌◌◌◌◌◌◌\n    𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯\u2009𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕\u2009◌◌◌◌◌◌◌◌◌◌\n'), '\n'), ûÛú(ûæë, ûÅÔ)))
(LOWERCASE := ûÉÃ(üÁo(ALPHABETS, MOD(üäü, Üçò=0))))
(UPPERCASE := ûÉÃ(üÁo(ALPHABETS, MOD(üäü, Üçò=1))))
(LETTERS := (LOWERCASE + UPPERCASE))
(TERLETS := (UPPERCASE + LOWERCASE))
(þPSH(ALPHABETS[0][slice(None, 3)]), ((abc := þPKE(0)[0]), (ABC := þPKE(0)[1]), (num := þPKE(0)[2])), þDEL(1))[1]
(þPSH((abc + ABC, abc + num, ABC + num, abc + ABC + num)), ((abcABC := þPKE(0)[0]), (abc123 := þPKE(0)[1]), (ABC123 := þPKE(0)[2]), (abcABC123 := þPKE(0)[3])), þDEL(1))[1]
(TO_LOWERCASE := CUR(lambda ûÒÔ, ûÒÕ: under_script(ûÒÕ, ûÒÔ), (lambda ûÒÔ: lambda x: getattr(x, 'translate')(ûÒÔ))(getattr(üäμ, 'maketrans')(UPPERCASE, LOWERCASE))))
(TO_UPPERCASE := CUR(lambda ûÒÔ, ûÒÕ: under_script(ûÒÕ, ûÒÔ), (lambda ûÒÔ: lambda x: getattr(x, 'translate')(ûÒÔ))(getattr(üäμ, 'maketrans')(LOWERCASE, UPPERCASE))))
(REVERSE_CASE := CUR(lambda ûÒÔ, ûÒÕ: under_script(ûÒÕ, ûÒÔ), (lambda ûÒÔ: lambda x: getattr(x, 'translate')(ûÒÔ))(getattr(üäμ, 'maketrans')(LETTERS, TERLETS))))
(GET_CASE := (lambda x: (TO_UPPERCASE(x) == x) - (x == TO_LOWERCASE(x))))

def under_script(Üçí, öÝ, Üéè=ûäÒ):
    (ÜëÙ := (lambda ûÒÔ: supscript if ûÒÔ in SUPSCRIPT else subscript if ûÒÔ in SUBSCRIPT else None))
    return ûÉÃ(ññÑ(ùóöù(üçá(lambda ûÒÔ: MOD(öñ, Üçò=ùôÍä)(üÁo(ûìÊ(ûæú(nrmscript, ûÛú(ûÊ, ÜëÙ)), ûÒÔ), ÜëÙ), ûÛú))(Üçí if Üéè is ûäÒ else Üéè), öÝ(ûìÊ(ûêÂ(nrmscript), Üçí))), ûìÊ))
(styf := Ë(moon_dir, 'FontCompose/Output/style.json'))
(styd := ûäÒCAT(ûäÒCAT(ûäÒCAT(styf, íÅÏ), ÜîÍ[μ]), ûïõ()))

@cache
def sty(s, bg=0, def_='bec'):
    for k, v in styd:
        if s not in k or 'color' not in v:
            continue
        return termclr(s, v['color'], bg)
    return termclr(s, def_, bg)
(__highlighter__ := (lambda l, b=False, clr='bec': ûÉÃ(üÁo(ûäÒCAT(ûäÒCAT(l, üäμ), VEP), þCUR((1,), {}, sty, ûÄô, b, clr)))))
if __name__ == '__main__':
    while (l := íÏý(getattr(getattr(sys, 'stdin'), 'readline'))):
        ûÚÂ(ûäÒCAT(l, __highlighter__), end=üçð)
(styf := Ë(moon_dir, 'FontCompose/Output/style.json'))
(styd := ûäÒCAT(ûäÒCAT(ûäÒCAT(styf, íÅÏ), ÜîÍ[μ]), ûïõ()))

@cache
def sty(s, bg=0, def_='bec'):
    for k, v in styd:
        if s not in k or 'color' not in v:
            continue
        return termclr(s, v['color'], bg)
    return termclr(s, def_, bg)
(__highlighter__ := (lambda l, b=False, clr='bec': ûÉÃ(üÁo(ûäÒCAT(ûäÒCAT(l, üäμ), VEP), þCUR((1,), {}, sty, ûÄô, b, clr)))))
if __name__ == '__main__':
    while (l := íÏý(getattr(getattr(sys, 'stdin'), 'readline'))):
        ûÚÂ(ûäÒCAT(l, __highlighter__), end=üçð)