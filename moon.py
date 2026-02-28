#!/bin/python
BOOTSTRAP_HASH='ZXQUp4XMseuik8OZJSTo2wCKV7-GHI3kK-me0fCWKgc'
from pathlib import Path as áÌî
from os import environ as env
moon_dir = env.get("MOON_BASE_DIR")
moon_dir = áÌî(moon_dir) if moon_dir else áÌî(__file__).parent
#base.☾ (9704 ⟶ 21098)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/base.☾')).parent
import os,sys,inspect,traceback,threading,errno,struct
from threading import get_ident as áÐèþÂÐðþáÐØ
from os import environ as env
from sys import stdin as ÂÐðþáÐâ,stdout as áÐãþáÐéþáÐè,stderr as áÐÙþÂÐüþÂÐü,argv as áÑË
from sys import exit,setrecursionlimit,path as syspath
from math import *
from site import getsitepackages
from json import dumps as jdumps__,loads as jloads__
from cmath import *
from types import UnionType
from random import shuffle,choice,uniform,randint
from tempfile import gettempdir
from builtins import setattr as setattr_
from operator import setitem as setitem_,__gt__,__lt__,__ge__,__le__,rshift,lshift,getitem,delitem
from itertools import chain,filterfalse,product,accumulate,zip_longest
from functools import reduce,partial as MOD,cache as cache_
from pickle import dumps as pdump,loads as pload
from hashlib import sha256 as _sha256
from base64 import urlsafe_b64encode,urlsafe_b64decode,b85encode as b85e,b85decode as b85d
from zlib import compress as zibe,decompress as zibd
(syspath).extend(getsitepackages())
setrecursionlimit(100000)
del (getsitepackages,factorial,e,pi,tau,sqrt,cbrt,pow)
(setattr:=(lambda x,y,z:(setattr_(x,y,z) or z)))
(setitem:=(lambda x,y,z:(setitem_(x,y,z) or z)))
(ÄÊSTK:={})
def ÄÊPSH(x):
    if ((t:=áÐèþÂÐðþáÐØ()) in ÄÊSTK):
        ÄÊSTK[t].append(x)
    else :
        ÄÊSTK[t]=[x]
    
    return x

def ÄÊPKE(x=0):
    return ÄÊSTK[áÐèþÂÐðþáÐØ()][~x]

def ÄÊPOP(x=0):
    return ÄÊSTK[áÐèþÂÐðþáÐØ()].pop(~x)

def ÄÊDEL(x):
    del ÄÊSTK[áÐèþÂÐðþáÐØ()][-x:]

(ÂÞÅCAT:=(lambda x,y:((y(x))if(callable(y))else((((ÁÜÙ(x) + y))if((isinstance(y,ÁÜÙ) and (not isinstance(x,int) )))else((x * y)))))))
def ÄÊCUR(áÍÊ,áÍÅ,*áÎç):
    def Ëðá(*áÌú):
        if (len(áÌú) < len(áÍÊ)):
            return (lambda *áÑË:Ëðá(*áÌú,*áÑË))
        
        (ÄÊPSH(([*áÎç],{**áÍÅ})),((áÖÒ:=ÄÊPKE(0)[0]),(áÖÝ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
        for (k,v) in(zip(áÍÊ,áÌú)):
            (ÄÊPSH(((áÖÒ)if(isinstance(k,int))else(áÖÝ))),ÄÊPSH(k),ÄÊPSH(v),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        
        return áÖÒ[0](*(áÖÒ[slice(1,None)]),*(áÌú[slice(len(áÍÊ),None)]),**áÖÝ)
    
    return Ëðá()

(ÄÊPSH((sys).modules),ÄÊPSH(("__main__")),ÄÊPSH((sys).modules[__name__]),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
(ÄÊPSH((Exception,object,dict,bool,list,tuple,set,str,int,float,bytes)),((áÍÚ:=ÄÊPKE(0)[0]),(áÍä:=ÄÊPKE(0)[1]),(áÍÙ:=ÄÊPKE(0)[2]),(áÍÖ:=ÄÊPKE(0)[3]),(áÍá:=ÄÊPKE(0)[4]),(áÍé:=ÄÊPKE(0)[5]),(áÍè:=ÄÊPKE(0)[6]),(ÁÜÙ:=ÄÊPKE(0)[7]),(áÍÞ:=ÄÊPKE(0)[8]),(áÍÛ:=ÄÊPKE(0)[9]),(áÍî:=ÄÊPKE(0)[10])),ÄÊDEL(1))[1]
(áÍÚþáÍÚ:=(Exception,BaseExceptionGroup,GeneratorExit))
(ÁØã:=(""))
(ÄÊPSH(((1 / 2),(1 / 3),(1 / 4),(1 / 5),(1 / 6),(1 / 7),(1 / 8),(1 / 9),(1 / 10),(2 / 3),(2 / 5),(2 / 7),(2 / 9),(3 / 4),(3 / 5),(3 / 7),(3 / 8),(3 / 10),(4 / 5),(4 / 7),(4 / 9),(5 / 6),(5 / 7),(5 / 8),(5 / 9),(6 / 7),(7 / 8),(7 / 9),(7 / 10),(8 / 9),(9 / 10),0,(1 / 100))),((ÃÆ:=ÄÊPKE(0)[0]),(ÂÑõ:=ÄÊPKE(0)[1]),(ÃÅ:=ÄÊPKE(0)[2]),(ÂÑø:=ÄÊPKE(0)[3]),(ÂÑü:=ÄÊPKE(0)[4]),(ÂÑò:=ÄÊPKE(0)[5]),(ÂÑÿ:=ÄÊPKE(0)[6]),(ÂÑó:=ÄÊPKE(0)[7]),(ÂÑô:=ÄÊPKE(0)[8]),(ÂÑö:=ÄÊPKE(0)[9]),(ÂÑù:=ÄÊPKE(0)[10]),(ÄÝóú:=ÄÊPKE(0)[11]),(ÄÝôÀ:=ÄÊPKE(0)[12]),(ÃÇ:=ÄÊPKE(0)[13]),(ÂÑú:=ÄÊPKE(0)[14]),(ÄÝóû:=ÄÊPKE(0)[15]),(ÂÒÀ:=ÄÊPKE(0)[16]),(ÄÝôÏ:=ÄÊPKE(0)[17]),(ÂÑû:=ÄÊPKE(0)[18]),(ÄÝóü:=ÄÊPKE(0)[19]),(ÄÝôË:=ÄÊPKE(0)[20]),(ÂÑý:=ÄÊPKE(0)[21]),(ÄÝóý:=ÄÊPKE(0)[22]),(ÂÒÁ:=ÄÊPKE(0)[23]),(ÄÝôÂ:=ÄÊPKE(0)[24]),(ÄÝóÿ:=ÄÊPKE(0)[25]),(ÂÒÂ:=ÄÊPKE(0)[26]),(ÄÝôÃ:=ÄÊPKE(0)[27]),(ÄÝôÐ:=ÄÊPKE(0)[28]),(ÄÝôÄ:=ÄÊPKE(0)[29]),(ÄÝôÑ:=ÄÊPKE(0)[30]),(ÂÒî:=ÄÊPKE(0)[31]),(ÄÝôÒ:=ÄÊPKE(0)[32])),ÄÊDEL(1))[1]
(ÄÊPSH((3.14159265358979323,2.71828182845904523)),((Ïî:=ÄÊPKE(0)[0]),(ÂÐæ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH((inf,complex(0,1),ÂÞÅCAT(2,Ïî),ÂÞÅCAT(ÃÆ,Ïî),ÂÞÅCAT(ÃÅ,Ïî),ÂÞÅCAT(ÂÑÿ,Ïî))),((ÂÕË:=ÄÊPKE(0)[0]),(Ãù:=ÄÊPKE(0)[1]),(Ïò:=ÄÊPKE(0)[2]),(ÄÝøà:=ÄÊPKE(0)[3]),(ÄÝøá:=ÄÊPKE(0)[4]),(ÄÝøâ:=ÄÊPKE(0)[5])),ÄÊDEL(1))[1]
(ÄÊPSH(((- ÂÕË ),(- Ãù ),(- Ïò ),(- Ïî ),(- ÄÝøà ),(- ÄÝøá ),(- ÄÝøâ ),(- ÂÐæ ))),((ÄÝîá:=ÄÊPKE(0)[0]),(ÄÝîâ:=ÄÊPKE(0)[1]),(ÄÝîä:=ÄÊPKE(0)[2]),(ÄÝîå:=ÄÊPKE(0)[3]),(ÄÝîæ:=ÄÊPKE(0)[4]),(ÄÝîç:=ÄÊPKE(0)[5]),(ÄÝîè:=ÄÊPKE(0)[6]),(ÄÝîã:=ÄÊPKE(0)[7])),ÄÊDEL(1))[1]
(ÂÒå:=((2 ** (((3 ** (4)))))))
(ÄÊPSH(((lambda *áÑË:áÑË[0]),(lambda *áÑË:áÑË[((- 1 ))]))),((Âåß:=ÄÊPKE(0)[0]),(ÂåÔ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
class Named:
    (ÄÊPSH(((lambda áÑÞ,s:ÂåÔ((ÄÊPSH(s),ÄÊPSH(áÑÞ),ÄÊPSH(("s")),setattr(ÄÊPKE(1),ÄÊPKE(0),ÄÊPKE(2)),ÄÊDEL(3))[3],None)),(lambda áÑÞ:(áÑÞ).s))),((__init__:=ÄÊPKE(0)[0]),(__repr__:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]

(ÂÞÅ:=(NULL:=Named(("␀"))))
(ÄÊPSH((Named(("󰮈")),Named(("󱣩")),Named(("⬤")))),((ÄÔýò:=ÄÊPKE(0)[0]),(ÄÕøü:=ÄÊPKE(0)[1]),(ÂýÃ:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
class ÂÐô:
    None

(ÂÑÅ:=áÍÞ)
(ÂÐý:=(áÍÛ | ÂÑÅ))
(ÂÐá:=complex)
(ÂÁÍ:=(lambda Æå,*áÑË,**áÑÕ:(lambda *áÑË,**áÑÕ:((Æå(áÑË[1],áÑË[0],*(áÑË[slice(2,None)]),**áÑÕ))if((ãÊú(áÑË) >= 2))else(Æå(*áÑË,**áÑÕ))))))
(ËßØ:=(lambda Æå,*áÑË,**áÑÕ:(lambda *áÑË,**áÑÕ:Æå(áÑË[0],*áÑË,**áÑÕ))))
(ÂÖë:=(lambda Æå,*áÑË,**áÑÕ:(lambda *áÑË,**áÑÕ:Æå(*(áÑË[0]),**áÑÕ))))
(ãÊú:=len)
(ÄÕÍÔ:=(lambda *áÑË,áØÁ=ÂÞÅ,**áÑÕ:((((áÑË[0])if((áØÁ is ÂÞÅ))else(áØÁ)))if(áÑË)else((((lambda *áÑË:((áÑË[0])if(áÑË)else(ÄÕÍÔ))))if((áØÁ is ÂÞÅ))else((lambda *áÑË,**áÑÕ:áØÁ)))))))
(CUR:=(lambda Æå,*áÖÒ,**áÖÝ:((Æå(*áÖÒ,**áÖÝ))if((ãÊú(áÖÒ) >= 2))else((lambda *áÖÓ,**áÖÞ:CUR(Æå,*áÖÒ,*áÖÓ,**((áÖÝ | áÖÞ))))))))
(CURR:=(lambda Æå,*áÖÒ,**áÖÝ:((Æå(*áÖÒ,**áÖÝ))if((ãÊú(áÖÒ) >= 2))else((lambda *áÖÓ,**áÖÞ:CUR(Æå,áÖÓ[0],*áÖÒ,*(áÖÓ[slice(1,None)]),**((áÖÝ | áÖÞ))))))))
(ÁØò:=(ÁÙÇ:=(lambda Æå:(lambda áØÆ,*áÖÒ,**áÖÝ:[(áÑÿ)for v in(áØÆ)if(((áÑÿ:=Æå(v,*áÖÒ,**áÖÝ)) is not ÄÔýò))]))))
(ÁØòþë:=(ÁÙÇþë:=(lambda Æå:(lambda áØÆ,*áÖÒ,**áÖÝ:[(áÑÿ)for (ÄÝõÌ,v) in(ÂÓÏ(áØÆ))if(((áÑÿ:=Æå(v,ÄÝõÌ,áØÆ,*áÖÒ,**áÖÝ)) is not ÄÔýò))]))))
(ÁØÿþÁÙÄ:=(lambda Æå:Æå))
(ÁØòþÁÙÄ:=(lambda Æå:(lambda áØÆ,áØÇ,*áÖÒ,**áÖÝ:[(áÑÿ)for v in(áØÆ)if(((áÑÿ:=Æå(v,áØÇ,*áÖÒ,**áÖÝ)) is not ÄÔýò))])))
(ÁØÿþÁÙÇ:=(lambda Æå:(lambda áØÆ,áØÇ,*áÖÒ,**áÖÝ:[(áÑÿ)for v in(áØÇ)if(((áÑÿ:=Æå(áØÆ,v,*áÖÒ,**áÖÝ)) is not ÄÔýò))])))
(ÁØòþÁÙÄþë:=(lambda Æå:(lambda áØÆ,áØÇ,*áÖÒ,**áÖÝ:[(áÑÿ)for (ÄÝõÌ,v) in(ÂÓÏ(áØÆ))if(((áÑÿ:=Æå(v,áØÇ,ÄÝõÌ,áØÆ,*áÖÒ,**áÖÝ)) is not ÄÔýò))])))
(ÁØÿþÁÙÇþë:=(lambda Æå:(lambda áØÆ,áØÇ,*áÖÒ,**áÖÝ:[(áÑÿ)for (ÄÝõÌ,v) in(ÂÓÏ(áØÇ))if(((áÑÿ:=Æå(áØÆ,v,ÄÝõÌ,áØÇ,*áÖÒ,**áÖÝ)) is not ÄÔýò))])))
(ÁØòþÁÙÇ:=(lambda Æå:(lambda áØÆ,áØÇ,*áÖÒ,**áÖÝ:[(áÑÿ)for (x,y) in(ÄÕåØ(áØÆ,áØÇ))if(((áÑÿ:=Æå(x,y,*áÖÒ,**áÖÝ)) is not ÄÔýò))])))
(ÁØòþÁÙÇþë:=(lambda Æå:(lambda áØÆ,áØÇ,*áÖÒ,**áÖÝ:[(áÑÿ)for (ÄÝõÌ,(x,y)) in(ÂÓÏ(ÄÕåØ(áØÆ,áØÇ)))if(((áÑÿ:=Æå(x,y,ÄÝõÌ,áØÆ,áØÇ,*áÖÒ,**áÖÝ)) is not ÄÔýò))])))
(ÄÊPSH(((lambda x,y:((((False)if(y)else(x)))if(x)else(y))),(lambda x,y:((((y)if(y)else(False)))if(x)else(((x)if(y)else(True))))))),((ÄÝøø:=ÄÊPKE(0)[0]),(ÄÝøú:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÂÕÕ:=(Âùè:=(lambda x,y:(x or y))))
(ÄÝøù:=(ÄÝùÀ:=(lambda x,y:(not (x or y) ))))
(ÂÕÔ:=(Âùç:=(lambda x,y:(x and y))))
(ÄÝøå:=(ÄÝùÁ:=(lambda x,y:((((False)if(y)else(x)))if(x)else(((y)if(y)else(True)))))))
(ÄÊPSH((__lt__,__gt__,__le__,__ge__)),((ÿ:=ÄÊPKE(0)[0]),(ÁÁ:=ÄÊPKE(0)[1]),(ÂÖÔ:=ÄÊPKE(0)[2]),(ÂÖÕ:=ÄÊPKE(0)[3])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda x,y:(x == y)),(lambda x,y:(x != y)))),((ÂÖÑ:=ÄÊPKE(0)[0]),(ÂÖÐ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda x,y:(gcd(x,y) == x)),(lambda x,y:(gcd(x,y) != x)))),((ÂÕÐ:=ÄÊPKE(0)[0]),(ÂÕÑ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda x,y:(x in y)),(lambda x,y:(x not in y)))),((ÂÔó:=ÄÊPKE(0)[0]),(ÂÔô:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda x,y:(y in x)),(lambda x,y:(y not in x)))),((ÂÔö:=ÄÊPKE(0)[0]),(ÂÔø:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda x,y:({*x}).issubset({*y})),(lambda x,y:({*y}).issubset({*x})))),((ÂÖó:=ÄÊPKE(0)[0]),(ÂÖô:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda x,y:(not ÂÖó(x,y) )),(lambda x,y:(not ÂÖô(x,y) )))),((ÂÖõ:=ÄÊPKE(0)[0]),(ÂÖö:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda x,y:((((Ïß:={*x})).issubset((Ïà:={*y})) and Ïß) != Ïà)),(lambda x,y:((((Ïß:={*y})).issubset((Ïà:={*x})) and Ïß) != Ïà)))),((ÂÖü:=ÄÊPKE(0)[0]),(ÂÖý:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda x,y:(not ÂÖü(x,y) )),(lambda x,y:(not ÂÖý(x,y) )))),((ÄÝøÄ:=ÄÊPKE(0)[0]),(ÄÝøÅ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÝöú:=(lambda x,y:ÂÕÃ(ÂÕØ(x,y),ÂÕÖ(x,y))))
(ÂÕØ:=(lambda x,y:((({*x} | {*y}))if(ÁØö(x,áÍè))else([*x,*([(z)for z in(y)if((z not in x))])]))))
(ÂÕÖ:=(lambda x,y:((({*x} & {*y}))if(ÁØö(x,áÍè))else([(z)for z in(x)if((z in y))]))))
(ÂÕÃ:=(lambda x,y:(((x - {*y}))if(ÁØö(x,áÍè))else([(z)for z in(x)if((z not in y))]))))
(ÂøÚ:=(lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:Áÿú(product(*(((([áØÆ] * áØÁ))if(((áØÇ is ÂÞÅ) and (áØÁ is not ÂÞÅ)))else(((([áØÆ,áØÇ])if((áØÇ is not ÂÞÅ))else(áØÆ)) * ((áØÁ)if((áØÁ is not ÂÞÅ))else(1))))))),áÍá)))
(ÂØÑ:=(lambda *áÑË,áØÁ=1:((Æå:=(lambda *áÑË,n=1,r=[]:(lambda ÂîÓ:Áÿú(ÂîÓ[0],(lambda x:((Æå(*(ÂîÓ[slice(1,None)]),r=(r + [x])))if((ãÊú(ÂîÓ) > 1))else((r + [x]))))))((áÑË * n)))))(*áÑË,n=áØÁ)))
(ÄÊPSH(((lambda x,y:(x % y)),(lambda x,y:(x // y)))),((æ:=ÄÊPKE(0)[0]),(ÃËÕ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda x,y:(x is y)),(lambda x,y:(x is not y)))),((ÂÕó:=ÄÊPKE(0)[0]),(ÂÕõ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda x:(~ x )),(lambda x,y:x@y))),((ÂÄ:=ÄÊPKE(0)[0]),(ÁÃ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda x,y:(x | y)),(lambda x,y:(x & y)),(lambda x,y:(x ^ y)))),((ÂÂ:=ÄÊPKE(0)[0]),(ç:=ÄÊPKE(0)[1]),(Áâ:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda x,y:(x ** y)),(lambda x:(not x )),(lambda áØÆ,áØÁ=ÂÞÅ:(lambda x:MOD(î,áØÁ=áØÁ)(áØÆ))))),((ÂÙû:=ÄÊPKE(0)[0]),(Âó:=ÄÊPKE(0)[1]),(Âö:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
(ÂÀÇ:=(lambda áØÆ:((ÄÝöì(ÂÀÇ(ÄÝöì(áØÆ))))if(ÁØö(áØÆ,áÍÞ))else(((áØÆ[slice(None,None,((- 1 )))])if(ÁØö(áØÆ,(((áÍî | ÁÜÙ) | áÍá) | áÍé)))else((((áØÆ).__reversed__())if(hasattr(áØÆ,("__reversed__")))else([*áØÆ][slice(None,None,((- 1 )))]))))))))
(ÄÝöí:=(lambda áØÆ=ÂÞÅ,áØÁ=ÂÞÅ:((chr(áØÆ))if(ÁØö(áØÆ,áÍÞ))else(((ord(áØÆ))if((ÁØö(áØÆ,ÁÜÙ) and (((ãÊú(áØÆ) == 1) and (áØÁ is not áÍá)))))else(MOD(Áëý,áØÁ=ÁØö(áØÆ[0],áÍÞ))(Áÿú(áØÆ,ÄÝöí),Âøî)))))))
(ÂÛê:=(lambda áØÆ,áØÁ=ÂÞÅ:((MOD(ÂÛê,áØÁ=((ÂÔö(áØÆ,(" ")) * (" ")) + (" ")))(áØÆ))if((áØÁ is ÂÞÅ))else(MOD(Áëý,áØÁ=(ãÊú(áØÁ) > 1))((áØÆ).split(áØÁ[0]),MOD(ÁØò((lambda ÂîÓ:MOD(ÂÛê,áØÁ=áØÁ[slice(1,None)])(ÂîÓ)))))))))
(Âäû:=(lambda áØÆ,áØÁ=ÂÞÅ:((ÄÝõé(Áÿú(ÄÝõé(áØÆ),MOD(Âäû,áØÁ=áØÁ))))if(MOD(ÁØö,áØÁ=ÂÕó)(áØÆ,ÂÐá))else(((áÍÞ(round(áØÆ)))if((áØÁ is ÂÞÅ))else(round(áØÆ,áØÁ)))))))
(ÄÊPSH((floor,ceil)),((Âüð:=ÄÊPKE(0)[0]),(Âüï:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda áØÆ:(áØÆ).real),(lambda áØÆ:(áØÆ).imag))),((ÄÝõè:=ÄÊPKE(0)[0]),(ÄÝõç:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÝõé:=(lambda áØÆ:((ÂÐá(*áØÆ))if(ÁØö(áØÆ,(áÍá | áÍé)))else((ÄÝõè(áØÆ),ÄÝõç(áØÆ))))))
(ÂÛÅ:=(lambda áØÆ,áØÁ=ÂÞÅ:MOD(ÄÕåØ,áØÁ=áØÁ)(áØÆ)))
(Âüá:=(ÁÜÙ).strip)
(ÂØú:=(lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:(((áØÆ * áØÇ))if((áØÁ is ÂÞÅ))else(((áØÆ * áØÇ) % MOD(Áëý,áØÁ=áÓö)(áØÁ,ãÊú))))))
(ÄÃ:=(lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:(((áØÆ / áØÇ))if((áØÁ is ÂÞÅ))else(((áØÆ / áØÇ) % MOD(Áëý,áØÁ=áÓö)(áØÁ,ãÊú))))))
(ÃËÕ:=(lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:(((áØÆ // áØÇ))if((áØÁ is ÂÞÅ))else(MOD(ÂÙû,áØÁ=(- MOD(Áëý,áØÁ=áÓö)(áØÁ,ãÊú) ))(áØÆ,áØÇ)))))
(ÂÙû:=(lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:(((áØÆ ** áØÇ))if((áØÁ is ÂÞÅ))else(pow(áØÆ,áØÇ,MOD(Áëý,áØÁ=áÓö)(áØÁ,ãÊú))))))
(ÂÕÀ:=(lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:(((MOD(î,áØÁ=áØÁ)(áØÆ),MOD(ì,áØÁ=áØÁ)(áØÆ)))if((áØÇ is ÂÞÅ))else((MOD(î,áØÁ=áØÁ)(áØÆ,áØÇ),MOD(ì,áØÁ=áØÁ)(áØÆ,áØÇ))))))
(Âù:=(lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:(((MOD(ì,áØÁ=áØÁ)(áØÆ),MOD(î,áØÁ=áØÁ)(áØÆ)))if((áØÇ is ÂÞÅ))else((MOD(ì,áØÁ=áØÁ)(áØÆ,áØÇ),MOD(î,áØÁ=áØÁ)(áØÆ,áØÇ))))))
def ì(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
    (v:=(((+ áØÆ ))if((áØÇ is ÂÞÅ))else((áØÆ + áØÇ))))
    return ((v)if((áØÁ is ÂÞÅ))else((v % MOD(Áëý,áØÁ=áÓö)(áØÁ,ãÊú))))

def î(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
    (v:=(((- áØÆ ))if((áØÇ is ÂÞÅ))else((áØÆ - áØÇ))))
    return ((v)if((áØÁ is ÂÞÅ))else((v % MOD(Áëý,áØÁ=áÓö)(áØÁ,ãÊú))))

def ÂØô(áÍÒ,áØÁ=True):
    for áØÁ in(áÍÒ):
        if not((not áØÁ )):continue
        break 
    
    return áØÁ

def ÂØõ(áÍÒ,áØÁ=False):
    for áØÁ in(áÍÒ):
        if not(áØÁ):continue
        break 
    
    return áØÁ

def ÄÝõÓ(áÍÒ,áØÁ=False):
    if (not ãÊú(áÍÒ) ):
        return áØÁ
    
    (r:=True)
    for áØÁ in(áÍÒ):
        if áØÁ:
            (r:=áØÁ)
        else :
            return r
        
    
    return (not r )

def ÄÝõÔ(áÍÒ,áØÁ=True):
    if (not ãÊú(áÍÒ) ):
        return áØÁ
    
    (r:=False)
    for áØÁ in(áÍÒ):
        if áØÁ:
            return r
        else :
            (r:=áØÁ)
        
    
    return (not r )

def ÐÌü(Æå,*áÑË,**áÑÕ):
    if áÓó(Æå):
        return Æå(*áÑË,**áÑÕ)
    
    if áÓö(Æå):
        for x in(Æå):
            None
        
        return Æå
    
    ((ÄÊPOP(0))if(ÄÊPSH(False))else(ÂùÆ(ÄÊPOP(0),("%s is not iterable or callable.")%(Æå,))))

class Ticker:
    (__slots__:=(("i"),))
    (__init__:=(lambda áÑÞ,i:ÂåÔ((ÄÊPSH(áÑÞ),ÄÊPSH(("i")),ÄÊPSH(i),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3],None)))
    (__call__:=(lambda áÑÞ,*áÑË,**áÑÕ:ÂåÔ((ÄÊPSH(áÑÞ),ÄÊPSH(("i")),ÄÊPSH(getattr(ÄÊPKE(1),ÄÊPKE(0))),ÄÊPSH((ÄÊPKE(0) - 1)),setattr(ÄÊPKE(3),ÄÊPKE(2),ÄÊPKE(0)),ÄÊDEL(4))[4],áÑÞ)))
    (__bool__:=(lambda áÑÞ:(not (áÑÞ).i )))
    (__repr__:=(lambda áÑÞ:("Ticker[i=%s]")%((áÑÞ).i,)))

class TimerState:
    (__init__:=(lambda áÑÞ,áÓË:ÂåÔ((ÄÊPSH(áÑÞ),ÄÊPSH(("áÓË")),ÄÊPSH(áÓË),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3],None)))
    (__bool__:=(lambda áÑÞ:((áÑÞ).áÓË).s))
    (__call__:=(lambda áÑÞ:((((áÑÞ).áÓË).r)if(áÑÞ)else(ÐÌü((((áÑÞ).áÓË).r).copy)))))
    (__repr__:=(lambda áÑÞ:("Timer[%s; %ss; %s; %s Remaining loops]=%s")%(("ID")[(((áÑÞ).áÓË).y >= 0)],ÂüÌ(((áÑÞ).áÓË).y),((("Running"))if(áÑÞ)else(("Completed"))),((áÑÞ).áÓË).n,((áÑÞ).áÓË).r,)))

(tmp:={("ᴍ"):("Áÿú"),("ꟿ"):("ËãÂ"),("ſ"):("ÆÑ"),("Ϝ"):("ÐÌ"),("󰈳"):("ÄÔÔè"),("󰈲"):("ÄÔÔç"),(""):("ÐÌÛ"),("󰒼"):("ÄÔàÑ"),("󰒽"):("ÄÔàÒ"),("ᙎ"):("Ááæ"),("ᙡ"):("Ááú"),("ᗢ"):("Áßô"),("ᙧ"):("ÁâÁ"),("⊚"):("ÂØÍ"),("⊜"):("ÂØÏ"),("🟕"):("ãéÜ"),("🟖"):("ãéÝ"),("⊛"):("ÂØÎ"),("⍟"):("ÂÛÜ"),("○"):("Âåæ"),("⍜"):("ÂÛÙ"),("󰬫"):("ÄÔüÑ"),("󰬩"):("ÄÔüÏ"),(""):("ÐâÄ"),("󰔶"):("ÄÔâÑ"),(""):("ÐÇò"),("󱑼"):("ÄÕåØ"),("󷹅"):("ÄÝöÔ"),("⪡"):("Âúù"),("⪢"):("Âúú"),("󰸵"):("ÄÕÊÂ"),("󰸷"):("ÄÕÊÄ"),("⤉"):("ÂóÍ"),("⤈"):("ÂóÌ"),("⟷"):("Âîí"),("󷹌"):("ÄÝöÜ"),("󷹍"):("ÄÝöÝ"),("󷹎"):("ÄÝöÞ"),("󷹑"):("ÄÝöá"),("󷸹"):("ÄÝöÈ"),("󷸺"):("ÄÝöÉ"),("󷸸"):("ÄÝöÇ"),("󷸻"):("ÄÝöÊ"),("⨝"):("Âøî"),("⟕"):("ÂîÊ"),("⟖"):("ÂîË"),("⟗"):("ÂîÌ"),("⫰"):("ÂüÌ"),("⫯"):("ÂüË"),("󷹒"):("ÄÝöâ"),("󷹓"):("ÄÝöã"),("󷹔"):("ÄÝöä"),("󷹕"):("ÄÝöå"),("󷹖"):("ÄÝöæ"),("󷸓"):("ÄÝõà"),("󷸼"):("ÄÝöË"),("󷸔"):("ÄÝõá"),(""):("ÏäÒ"),("󱅏"):("ÄÕØÃ"),(""):("ÐâÇ")})
(ENC:=("ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýÿ"))
(RCD:=CURR((lambda ÂîÓ,ÂîÒ:ÂÖõ(ÂîÓ,ÂîÒ)),(("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") + ("_"))))
(SPE:=CURR((lambda ÂîÓ,ÂîÒ:ÂÖó(ÂîÓ,ÂîÒ)),(ENC + ("þ"))))
(enc:=MOD((lambda ÂîÓ:Âøî(ÁØò((lambda ÂîÓ:ÄÝöì(ÄÝöí(ÂîÓ),ãÊú(ENC),C=ENC)))(ÂîÓ),("þ")))))
(dec:=MOD((lambda ÂîÓ:Âøî(ÁØò((lambda ÂîÓ:ÄÝöí(ÄÝöì(ÂîÓ,ãÊú(ENC),C=ENC))))(ÄÝöÞ(ÂîÓ,("þ")))))))
(PEV:=MOD((lambda ÂîÓ:Âøî(MOD(ÄÔÔç,áØÁ=enc)(áÇù(ÂîÓ,RCD),RCD)))))
(VEP:=MOD((lambda ÂîÓ:Âøî(MOD(ÄÔÔç,áØÁ=MOD((lambda ÂîÓ:MOD(Áëý,áØÁ=SPE)(ÂîÓ,ÄÔâÑ(dec,(lambda x:("⸮%s?")%(x,)))))))(áÇù(ÂîÓ,SPE),SPE)))))
def OPWRAP_(*áÖê):
    def R(Æå):
        for x in(áÖê):
            (ÄÊPSH(globals()),ÄÊPSH(((tmp[x])if((x in tmp))else(PEV(x)))),ÄÊPSH(MOD(Æå,x)),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        
    
    return R

(ÄÊPSH((callable,(lambda x:hasattr(x,("__iter__"))))),((áÓó:=ÄÊPKE(0)[0]),(áÓö:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
def áÓõ(x):
    try :
        return hash(x)
    except áÍÚ:pass
    return False

(áÍÇ:=(lambda x,y=("utf-8"),*áÑË,**áÑÕ:(((x).encode(y,*áÑË,**áÑÕ))if(ÁØö(x,ÁÜÙ))else((x).decode(y,*áÑË,**áÑÕ)))))
class ÃÆë(áÍÞ):
    (__new__:=(lambda ÂÑÎ:(áÍÞ).__new__(ÂÑÎ,1)))
    (__call__:=(lambda *áÑË,**áÑÕ:ÃÆë))
    (__repr__:=(lambda áÑÞ:("ⴳ")))

class ÃÆì(áÍÞ):
    (__new__:=(lambda ÂÑÎ:(áÍÞ).__new__(ÂÑÎ,0)))
    (__call__:=(lambda *áÑË,**áÑÕ:ÃÆì))
    (__repr__:=(lambda áÑÞ:("ⴴ")))

(ÃÆë:=ÃÆë())
(ÃÆì:=ÃÆì())
def ÂùÆ(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
    if ((ÂÞÅ is áØÇ) and ÁØö(áØÆ,áÍÚþáÍÚ)):
        (ÄÊPSH((False,áØÆ)),((áØÆ:=ÄÊPKE(0)[0]),(áØÇ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    elif áØÆ:
        return áØÆ
    
    (E:=((ÂÞÅ is not áØÇ) and ÁØö(áØÇ,áÍÚþáÍÚ)))
    (áØÅ:=(("MOON_WARNING_IS_ERR") in env))
    (áÖð:=(áØÅ or (("MOON_DEPRECATION_IS_ERR") in env)))
    if (áØÁ is ÄÔáô):
        (ÄÊPSH((áÖð,("Deprecation %s")%(((("Error"))if(áÖð)else(("Warning"))),))),((áÓÔ:=ÄÊPKE(0)[0]),(áÓà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    elif (áØÁ is ÂÄ):
        (ÄÊPSH((áØÅ,("Warning%s")%((((" [as Error]"))if(áØÅ)else(ÁØã)),))),((áÓÔ:=ÄÊPKE(0)[0]),(áÓà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    else :
        (ÄÊPSH((True,("Assertion failed"))),((áÓÔ:=ÄÊPKE(0)[0]),(áÓà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    
    (ÄÊPSH(áÓà),ÄÊPSH((ÄÊPKE(0) + (" ⟨%s⟩%s")%(áØÆ,((((" ") + ((("%s(%s)")%((ÁØö(áØÇ)).__name__,Âøî(getattr(áØÇ,("args"),ÂÚü()),(",")),))if(E)else(áØÇ))))if((áØÇ is not ÂÞÅ))else(ÁØã)),))),(áÓà:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    Âçß(termclr(áÓà,((("f22"))if(áÓÔ)else(("ff2")))))
    if áÓÔ:
        if E:
            raise áØÇ
        
        raise ÂÞÅCAT(áÓà,AssertionError)
    
    return áØÆ

@OPWRAP_(*(("󰔶")))
def _(áÑã,Æå=ÂÞÅ,Ëðá=ÂÞÅ,áØÁ=áÍÚ):
    (ÄÊPSH((áØÁ,ÂÕÃ([Æå,Ëðá],[ÂÞÅ]))),((áÍÎ:=ÄÊPKE(0)[0]),(v:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    if (ãÊú(v) == 1):
        (Æå:=v[0])
        if (áÑã == ("")):
            raise Æå
        
    elif (ãÊú(v) == 2):
        if ((áÑã == ("")) and ÄÝøÇ(Æå,áÓó)):
            if Æå:
                return Æå
            
            raise Ëðá
        
    
    def r(*áÑË,**áÑÕ):
        try :
            return Æå(*áÑË,**áÑÕ)
        except áÍÎ as Ïã:
            if (ãÊú(v) == 1):
                if (áÑã == ("󰔶")):
                    return ((áÑË[0])if(áÑË)else(None))
                
                if (áÑã == ("")):
                    return Ïã
                
            
            if (áÑã == ("")):
                return Ëðá
            
            if (áÑã == ("󰔶")):
                return Ëðá(*áÑË,**áÑÕ)
            
            if (áÑã == ("")):
                return Ëðá(Ïã)
            
        
    
    return r

def Âáõ(*áÑË,áÌÄ=None):
    (ÄÊPSH(áÑË),(*((áÑË:=ÄÊPKE(0)[slice(0,-1,None)])),(Æå:=ÄÊPKE(0)[-1])),ÄÊDEL(1))[1]
    if (not áÌÄ ):
        (áÌÄ:=ÂÚü())
    
    if (not áÑË ):
        return Æå(*áÌÄ)
    
    with áÑË[0] as áÌß:return ((áÌÄ).append(áÌß) or Âáõ(*(áÑË[slice(1,None)]),Æå,áÌÄ=áÌÄ))

def Âçß(*áÑË,ÂìÆ=False,áÖý=(" "),áØÁ=("\x0A")):
    (((Æå:=((áÐÙþÂÐüþÂÐü)if(ÂìÆ)else(áÐãþáÐéþáÐè))))).write((Âøî(áÑË,ÁÜÙ(áÖý)) + ÁÜÙ(áØÁ)))
    (Æå).flush()
    if áÑË:
        return áÑË[0]
    

def ÁØö(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ,TYPELIKE={áÓó,áÓõ,áÓö},TYPEE=(((áÍé | áÍá) | type) | UnionType)):
    if (áØÇ is ÂÞÅ):
        return type(áØÆ)
    
    if (áØÇ in TYPELIKE):
        return áØÇ(áØÆ)
    
    if (áØÁ is ÂÞÅ):
        if (áØÇ is ÂÐô):
            return (ÁØö(áØÆ,(áÍÖ | áÍÞ)) and (áØÆ >= 0))
        elif (áØÇ is ÂÑÅ):
            return ÁØö(áØÆ,(ÂÐô | áÍÞ))
        elif (áØÇ is ÂÐý):
            return ÁØö(áØÆ,(ÂÑÅ | ÂÐý))
        elif (áØÇ is ÂÐá):
            return ÁØö(áØÆ,(ÂÐý | complex))
        
    
    return isinstance(áØÆ,((áØÇ)if(isinstance(áØÇ,TYPEE))else(type(áØÇ))))

(ÄÊPSH(((lambda áØÆ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:MOD(ÁØö,áØÁ=áØÁ)(áØÇ,áØÆ)),(lambda áØÆ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:(not MOD(ÁØö,áØÁ=áØÁ)(áØÆ,áØÇ) )),(lambda áØÆ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:(not MOD(ÁØö,áØÁ=áØÁ)(áØÇ,áØÆ) )))),((ÁØñ:=ÄÊPKE(0)[0]),(ÄÝøÇ:=ÄÊPKE(0)[1]),(ÄÝøÆ:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
(Âõ:=(lambda áØÁ:ÁØò((lambda ÂîÓ:(ÄóÌÁ((ÂÞÅCAT(Ïò,(áØÁ ** ((- 1 )))) * (ÂîÓ + (ÃÆ * (áØÁ < 0))))) + ÂÞÅCAT(Ãù,ÄóÌÀ((ÂÞÅCAT(Ïò,(áØÁ ** ((- 1 )))) * (ÂîÓ + (ÃÆ * (áØÁ < 0)))))))))(ÂÿÇ(ÂüÌ(áØÁ)))))
(ÂÕÇ:=(lambda áØÆ=ÂÞÅ,áØÁ=2:(áØÆ ** (áØÁ ** ((- 1 ))))))
(ÚÑ:=(lambda áØÆ,áØÁ=2:ÁØò((lambda ÂîÓ:(ÂîÓ * (áØÆ ** (áØÁ ** ((- 1 )))))))(MOD(Âõ,áØÁ=ÂüÌ(áØÁ)))))
(ÐàÒ:=(lambda áØÆ,*áÑË,**áÑÕ:(lambda *áÑË,**áÑÕ:áØÆ(*(ÄÔÙù(áÑË)),**áÑÕ))))
(ÂÕì:=(lambda áØÆ,*áÑË,**áÑÕ:(lambda *áÑË,**áÑÕ:áØÆ(*(ÂÀÇ(áÑË)),**áÑÕ))))
(ë:=(lambda x,y:x*y))
(ð:=(lambda x,y:x/y))
(ÄÔáô:=áÍä())
(ÄÊPSH((gcd,lcm,log,sin,cos,tan)),((ÄóÌÐ:=ÄÊPKE(0)[0]),(ÄóÌÑ:=ÄÊPKE(0)[1]),(ÄóÍÀ:=ÄÊPKE(0)[2]),(ÄóÌÀ:=ÄÊPKE(0)[3]),(ÄóÌÁ:=ÄÊPKE(0)[4]),(ÄóÌÂ:=ÄÊPKE(0)[5])),ÄÊDEL(1))[1]
class Holder:
    (__slots__:=(("x"),))
    def __init__(áÑÞ,x=ÂÞÅ):
        (ÄÊPSH(áÑÞ),ÄÊPSH(("x")),ÄÊPSH(x),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
    
    def __pos__(áÑÞ):
        return Âåß((áÑÞ).x,((ÄÊPOP(0))if(ÄÊPSH(((áÑÞ).x is not ÂÞÅ)))else(ÂùÆ(ÄÊPOP(0),("Holder value unset!")))))
    
    def __call__(áÑÞ,x=ÂÞÅ):
        (ÄÊPSH(áÑÞ),ÄÊPSH(("x")),ÄÊPSH(x),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
    
    def __bool__(áÑÞ):
        return ((áÑÞ).x is not ÂÞÅ)
    

def proxy_chained_calls_pure(Æå,n=1):
    def j(*áÔå,_PAIRS=None,**áÔï):
        if (_PAIRS is None):
            (_PAIRS:=ÂÚü())
        
        (_PAIRS:=[*_PAIRS,(áÔå,áÔï)])
        if (ãÊú(_PAIRS) == n):
            (G:=Æå(*(_PAIRS[0][0]),**(_PAIRS[0][1])))
            for (A,K) in(_PAIRS[slice(1,None)]):
                (G:=G(*A,**K))
            
            return G
        
        return (lambda *áÑË,**áÑÕ:j(*áÑË,_PAIRS=_PAIRS,**áÑÕ))
    
    return j


#system.☾ (1427 ⟶ 1908)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/system.☾')).parent
from time import time,sleep
def PL_CPU_COUNT():
    import multiprocessing
    return ÐÌü((multiprocessing).cpu_count)

def PL_THREAD(Æå,*áÑË,**áÑÕ):
    from threading import Thread as T
    (atom:=[])
    ÐÌü(((t:=T(target=(lambda :ÂÞÅCAT(Æå(*áÑË,**áÑÕ),(atom).append))))).start)
    return (lambda :ÂåÔ(ÐÌü((t).join),atom[0]))

def PL_WAIT_PID(p):
    try :
        (os).kill(p,0)
    except áÍÚ as Ðáü:
        return None
    
    (os).waitpid(p,0)

def PL_CHECK_PID(p):
    return (not (os).waitpid(p,(os).WNOHANG)[0] )

def PL_FORK(Æå,*áÑË,**áÑÕ):
    if (env).get(("MOON_NO_FORK")):
        return ÂÞÅCAT(ÂÞÅCAT(Æå(*áÑË,**áÑÕ),pdump),pload)
    
    from multiprocessing import shared_memory
    (áÓà:=(shared_memory).SharedMemory(create=True,size=((2 ** (20)))))
    (áÑÅ:=MOD((lambda ÂîÓ:ÂîÓ[slice(4,(4 + (struct).unpack(("I"),ÂîÓ[slice(None,4)])[0]))])))
    (p:=ÐÌü((os).fork))
    if p:
        return (p,(lambda :Âåß(ÂåÔ(ÂÞÅCAT(p,PL_WAIT_PID),ÂÞÅCAT(áÑÅ((áÓà).buf),pload)),(ÂåÔ(ÐÌü((áÓà).close),ÐÌü((áÓà).unlink))))))
    
    (v:=ÂÞÅCAT(Æå(*áÑË,**áÑÕ),pdump))
    (ÄÊPSH((áÓà).buf),ÄÊPSH(slice(None,4)),ÄÊPSH((struct).pack(("I"),ãÊú(v))),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
    (ÄÊPSH((áÓà).buf),ÄÊPSH(slice(4,(4 + ãÊú(v)))),ÄÊPSH(v),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
    ÂÞÅCAT(0,(os)._exit)

def PL_SLEEP(x):
    sleep(x)

def PL_TIME():
    return ÐÌü(time)

def PL_TEXT_COPY(x):
    try :
        from clipboard import copy
        return copy(x)
    except áÍÚ:pass
    ((ÄÊPOP(0))if(ÄÊPSH(False))else(MOD(ÂùÆ,áØÁ=ÂÄ)(ÄÊPOP(0),("Failed to copy! Do you have clipboard installed?"))))

def PL_TEXT_PASTE():
    try :
        from clipboard import paste
        return paste()
    except áÍÚ:pass
    ((ÄÊPOP(0))if(ÄÊPSH(False))else(MOD(ÂùÆ,áØÁ=ÂÄ)(ÄÊPOP(0),("Failed to paste! Do you have clipboard installed?"))))

def PL_URANDOM(n):
    return (os).urandom(n)


#ops_A.☾ (3282 ⟶ 8513)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ops_A.☾')).parent
def _map_d(x,y,n=1):
    (mapwd:=(lambda x,y:[(áÑÿ)for z in(x)if(((áÑÿ:=y(z)) is not ÄÔýò))]))
    def _get_d(x):
        if (not áÓö(x) ):
            return {0}
        
        if ÁØö(x,ÁÜÙ):
            return {1}
        
        return {*(ÁØò((lambda ÂîÓ:(ÂîÓ + 1)))(ÄÔÒØ([(_get_d(z))for z in(x)])))}
    
    def _map_m_d(x,y,n):
        if ÁØö(x,ÁÜÙ):
            return ((y(x))if((n == 1))else(((x)if(n)else(mapwd(x,y)))))
        
        if ÂÔö((d:=_get_d(x)),0):
            return ((x)if(n)else(y(x)))
        
        (x:=mapwd(x,(lambda x:_map_m_d(x,y,n))))
        return ((y(x))if((n in d))else(x))
    
    def _map_p_d(x,y,i):
        if (not i ):
            return y(x)
        
        if ÁØö(x,ÁÜÙ):
            return mapwd(x,y)
        
        if áÓö(x):
            return mapwd(x,(lambda x:_map_p_d(x,y,(i - 1))))
        
        return y(x)
    
    return ((_map_m_d(x,y,(((- 1 )) - n)))if((n < 0))else(_map_p_d(x,y,((ÂÒå)if((n is ÂÕË))else(n)))))

@OPWRAP_(*(("ᴍꟿ")))
def _(áÑã,áØÆ=ÂÞÅ,Æå=ÂÞÅ,áØÁ=1):
    (áÖß:=((_map_d)if((áÑã == ("ᴍ")))else((lambda x,y,z:_map_d(x,(lambda x:y(*(((x)if(áÓö(x))else([x]))))),z)))))
    if ÄÝøÇ(áØÁ,áÍÞ):
        if (áØÁ is ë):
            return (ÁØö(áØÆ))(áÖß((áØÆ).items(),Æå,1))
        elif (áØÁ is î):
            return (ÁØö(áØÆ))(ÄÕåØ(áÖß((áØÆ).items(),Æå,1),(áØÆ).values()))
        elif (áØÁ is ì):
            return (ÁØö(áØÆ))(ÄÕåØ((áØÆ).keys(),áÖß((áØÆ).items(),Æå,1)))
        
    
    return _map_d(áØÆ,(((lambda x:Æå(*(((x)if(áÓö(x))else([x]))))))if((áÑã == ("ꟿ")))else(Æå)),áØÁ)

def ÐôÅ(áØÆ=ÂÞÅ,áØÇ=ÐÌü,áØÁ=ÐÌü(PL_CPU_COUNT),m=("f")):
    if (m == ("f")):
        if (env).get(("MOON_NO_FORK")):
            return ÁØò((lambda ÂîÓ:ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ,áØÇ),pdump),pload)))(áØÆ)
        
        (ÄÊPSH(MOD(ÂÚü,áØÁ=2)()),((P:=ÄÊPKE(0)[0]),(G:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
        for Æå in(ÁØò((lambda ÂîÓ:(lambda :PL_FORK(áØÇ,ÂîÓ))))(áØÆ)):
            while((ãÊú((ÄÊPSH(P),ÄÊPSH(ÄÔÔç(ÄÊPKE(0),PL_CHECK_PID)),(P:=ÄÊPKE(0)),ÄÊDEL(2))[2]) >= áØÁ)):
                PL_SLEEP(ÄÝôÒ)
            
            ÁØòþÁÙÇ((lambda ÂîÓ,ÂîÒ:ÂÕÅ((ÂîÓ).append,ÂîÒ)))((P,G),ÐÌü(Æå))
        
        return Áÿú(G,ÐÌü)
    elif (m == ("t")):
        (O:=MOD(ÂÚü,áØÁ=ãÊú(áØÆ))())
        (Q:=ÁØòþë((lambda ÂîÓ,ÄÝõÌ,ÄÝõË:(lambda :(ÄÊPSH(O),ÄÊPSH(ÄÝõÌ),ÄÊPSH(ÂÞÅCAT(ÂîÓ,áØÇ)),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3])))(áØÆ))
        def Æå():
            while(Q):
                try :
                    (Ëðà:=ÂÞÅCAT(0,(Q).pop))
                except áÍÚ as Ðáü:
                    continue 
                
                ÐÌü(Ëðà)
            
        
        Áÿú(ÁØò((lambda ÂîÓ:ÂÞÅCAT(Æå,PL_THREAD)))(ÂÿÇ(áØÁ)),ÐÌü)
        return O
    
    ((ÄÊPOP(0))if(ÄÊPSH(False))else(ÂùÆ(ÄÊPOP(0),("%s is an invalid mode for !")%(m,))))

@OPWRAP_(*(("󰒼󰒽")))
def _(áÑã,áØÆ=ÂÞÅ,Æå=ÄÕÍÔ,ÁÜñ=False):
    (áØÆ:=[*áØÆ])
    (áÖê:=[((áÑÿ,i))for (i,v) in(ÂÓÏ(áØÆ))if(((áÑÿ:=Æå(v)) is not ÄÔýò))])
    (áÖê).sort(reverse=(áÑã == ("󰒽")))
    return Áÿú(áÖê,(((lambda x:x[1]))if(ÁÜñ)else((lambda x:áØÆ[x[1]]))))

@OPWRAP_(*(("󰈳󰈲")))
def _(áÑã,áØÆ=ÂÞÅ,Æå=ÂÞÅ,áØÁ=ÂÞÅ,ÁÜñ=False):
    ((ÄÊPOP(0))if(ÄÊPSH(((not ÁÜñ ) or (áØÁ is ÂÞÅ))))else(ÂùÆ(ÄÊPOP(0),("\u0022%sˣᔨ\u0022 is invalid")%(áÑã,))))
    (Æå:=((ÄÕÍÔ)if((Æå is ÂÞÅ))else(((Æå)if(áÓó(Æå))else(ÄÊCUR((2,),{},ÂÖÑ,Æå,ÂýÃ))))))
    if (áÑã == ("󰈳")):
        (Æå:=CUR((lambda ÂîÓ,ÂîÒ:(not ÂîÓ(ÂîÒ) )),Æå))
    
    if ÁÜñ:
        return [(i)for (i,z) in(ÂÓÏ(áØÆ))if(((áÑÿ:=Æå(z)) and (áÑÿ is not ÄÔýò)))]
    
    if (áØÁ is ÂÞÅ):
        return [(z)for z in(áØÆ)if(((áÑÿ:=Æå(z)) and (áÑÿ is not ÄÔýò)))]
    
    if (áØÁ == ë):
        return [(áÑÿ)for z in(áØÆ)if(((áÑÿ:=Æå(z)) and (áÑÿ is not ÄÔýò)))]
    
    if (not áÓó(áØÁ) ):
        (áØÁ:=MOD(ÄÕÍÔ,áØÁ=áØÁ))
    
    return [(((áØÁ(z))if(áÑÿ)else(z)))for z in(áØÆ)if(((áÑÿ:=Æå(z)) is not ÄÔýò))]

@OPWRAP_(*(("ᙎᙡᗢᙧ")))
def _(áÑã,áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ,ÁÜñ=False):
    if ÁÜñ:
        (ÄÊPSH(áØÆ),ÄÊPSH(ÂÿÇ(ÄÊPKE(0))),(áØÆ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
    (chnk:=1)
    if (áÓö(áØÇ) and (ãÊú(áØÇ) > 2)):
        (ÄÊPSH(áØÇ),(*((áØÇ:=ÄÊPKE(0)[slice(0,-1,None)])),(chnk:=ÄÊPKE(0)[-1])),ÄÊDEL(1))[1]
    
    if (áØÇ is not ÂÞÅ):
        (ÄÊPSH((([áØÇ,áØÇ])if(ÁØö(áØÇ,áÍÞ))else(áØÇ))),((áÝÍ:=ÄÊPKE(0)[0]),(áÝÎ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    elif (áÑã in ("ᙎᙡ")):
        (ÄÊPSH([1,1]),((áÝÍ:=ÄÊPKE(0)[0]),(áÝÎ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    elif (áÑã in ("ᗢᙧ")):
        (ÄÊPSH((([1,1])if((áØÁ is ÂÞÅ))else([0,áØÁ]))),((áÝÍ:=ÄÊPKE(0)[0]),(áÝÎ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    
    (áÝÏ:=(áÑã in ("ᙡᙧ")))
    (áÝÐ:=((((None)if((áØÁ is ÂÞÅ))else(áØÁ)))if((áÑã in ("ᙎᙡ")))else(ÂÞÅ)))
    (áÝÑ:=((((chnk)if((áØÁ is ÂÞÅ))else((áØÁ + 1))))if((áÑã in ("ᗢᙧ")))else(chnk)))
    (ÄÊPSH((áØÆ,áÝÍ,áÝÎ,áÝÏ,áÝÐ,áÝÑ)),((áÖê:=ÄÊPKE(0)[0]),(l:=ÄÊPKE(0)[1]),(r:=ÄÊPKE(0)[2]),(m:=ÄÊPKE(0)[3]),(áØÁ:=ÄÊPKE(0)[4]),(ÏÁ:=ÄÊPKE(0)[5])),ÄÊDEL(1))[1]
    if ÁØö(l,áÍÛ):
        (l:=áÍÞ(l))
    
    if ÁØö(r,áÍÛ):
        (r:=áÍÞ(r))
    
    if ÁØö(ÏÁ,áÍÛ):
        (ÏÁ:=áÍÞ(ÏÁ))
    
    (c:=ãÊú((áÖê:=[*áÖê])))
    if (áØÁ is ÂÞÅ):
        return Áÿú(ÂÿÇ(áÖê)[slice(l,(c - r),ÏÁ)],(lambda x:((áÖê[slice((x - l),x)] + MOD(Âêà,áØÁ=áÍÖ(m))(áÖê[x])) + áÖê[slice((x + 1),((x + r) + 1))])))
    
    (V:=((MOD(Âêà,áØÁ=l)(áØÁ) + áÖê) + MOD(Âêà,áØÁ=r)(áØÁ)))
    (r:=Áÿú(ÂÿÇ(áÖê)[slice(None,None,ÏÁ)],(lambda x:((V[slice(x,(x + l))] + MOD(Âêà,áØÁ=áÍÖ(m))(V[(x + l)])) + V[slice(((x + l) + 1),(((x + l) + r) + 1))]))))
    if (áØÁ is ÄÔýò):
        return MOD(Áÿú,áØÁ=2)(r,ÄÕÍÔ)
    
    return r

def ÐÌÛ(áØÆ,Æå=áÍÖ,áØÁ=ÂÞÅ,ÁÜñ=False):
    if (not áÓó(Æå) ):
        (ÄÊPSH(Æå),ÄÊPSH(CUR((lambda ÂîÓ,ÂîÒ:(ÂîÓ == ÂîÒ)),ÄÊPKE(0))),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
    if (áØÁ is not ÂÞÅ):
        (X:=MOD(ÐÌÛ,ÁÜñ=ÁÜñ)(áØÆ,Æå))
        if (áØÁ is ë):
            return ÄÔàÑ((X).items())
        
        if (áØÁ is ì):
            return Áÿú(ÄÔàÑ((X).items()),(lambda x:x[1]))
        
        if (áØÁ is áÍÖ):
            return [(X).get(False,ÂÚü()),(X).get(True,ÂÚü())]
        
        ((ÄÊPOP(0))if(ÄÊPSH(False))else(ÂùÆ(ÄÊPOP(0),("Invalid modifier for !"))))
    
    (r:={})
    for (i,z) in(ÂÓÏ(áØÆ)):
        if ((áÑÿ:=Æå(z)) is ÄÔýò):
            continue 
        
        if ÁÜñ:
            (z:=i)
        
        if (áÑÿ in r):
            (r[áÑÿ]).append(z)
        else :
            (ÄÊPSH(r),ÄÊPSH(áÑÿ),ÄÊPSH([z]),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        
    
    return r

def ÁÞç(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
    if (áØÇ is ÂÞÅ):
        (ÄÊPSH((áØÇ,áØÆ)),((áØÆ:=ÄÊPKE(0)[0]),(áØÇ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    
    ((ÄÊPOP(0))if(ÄÊPSH((áØÇ is not ÂÞÅ)))else(ÂùÆ(ÄÊPOP(0),("ᖘ needs right side"))))
    def Æå(áØÆ):
        (áØÆ:=((ÄÔÙù(áØÆ))if(((is_str:=ÁØö(áØÆ,ÁÜÙ))))else(((ÐÌü((áØÆ).copy))if(ÁØö(áØÆ,áÍÙ))else([*áØÆ])))))
        (ÄÊPSH((MOD(Áëý,áØÁ=áÓó)(áØÁ,MOD((lambda ÂîÓ:ÂîÓ(áØÆ)))),[])),((ids:=ÄÊPKE(0)[0]),(TD:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
        if (((ÄÝøÆ(ÁÜÙ,ÄÊPSH(ids)) and ÁØö(ÄÊPOP(0),ÄÊPSH(áÓö))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)):
            ÁØòþÁÙÇ((lambda ÂîÓ,ÂîÒ:(((TD).append(ÂîÓ))if((ÂîÒ is ÄÔýò))else((ÄÊPSH(áØÆ),ÄÊPSH(ÂîÓ),ÄÊPSH(ÂîÒ),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]))))(ids,(V:=áØÇ(ÄÝöÊ(áØÆ,ids))))
        else :
            ÁØÿþÁÙÇ((lambda ÂîÓ,ÂîÒ:(((TD).append(ÂîÓ))if((ÂîÒ is ÄÔýò))else((ÄÊPSH(áØÆ),ÄÊPSH(ÂîÓ),ÄÊPSH(ÂîÒ),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]))))(ids,(V:=Âêà(áØÇ(áØÆ[ids]))))
        
        for x in(ÄÔàÒ(TD)):
            del áØÆ[x]
        
        return ((Âøî(áØÆ,ÁØã))if(is_str)else(áØÆ))
    
    return ((Æå)if((áØÆ is ÂÞÅ))else(Æå(áØÆ)))

(ÆÑ:=(lambda áØÆ,áØÇ,áØÁ=ÂÞÅ:reduce(áØÇ,áØÆ,*(((())if((áØÁ is ÂÞÅ))else((áØÁ,)))))))
(ÐÌ:=(lambda áØÆ,áØÇ,áØÁ=ÂÞÅ:[*(accumulate(áØÆ,áØÇ,initial=((None)if((áØÁ is ÂÞÅ))else(áØÁ))))]))
(ÂøÑ:=(lambda áØÆ,áØÁ=ÂÞÅ:(((((ÁØã)if(ÁØö(áØÆ,ÁÜÙ))else(0))))if((((ÄÊDEL(1),False)[1])if(ÄÊPSH(áØÆ))else(((ÄÊPOP(0))if((áØÁ is not ÂÞÅ))else((ÄÊDEL(1),True)[1])))))else(MOD(ÆÑ,áØÁ=áØÁ)(áØÆ,ì)))))
(ÂøÐ:=(lambda áØÆ,áØÁ=ÂÞÅ:((1)if((((ÄÊDEL(1),False)[1])if(ÄÊPSH(áØÆ))else(((ÄÊPOP(0))if((áØÁ is not ÂÞÅ))else((ÄÊDEL(1),True)[1])))))else(MOD(ÆÑ,áØÁ=áØÁ)(áØÆ,ÂØú)))))
(ÄÕéý:=(lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:(((lambda Æå:Æå(*(ÂÕÃ([áØÆ,áØÇ],[ÂÞÅ])))))if((áØÁ is ÂÞÅ))else(áØÁ(*(ÂÕÃ([áØÆ,áØÇ],[ÂÞÅ])))))))
(ÂÔð:=(lambda áØÁ=ÂÞÅ:(({*''})if((áØÁ is ÂÞÅ))else(ÁØò((lambda ÂîÓ:{*''}))(ÂÿÇ(áØÁ))))))
(ÂÚü:=(lambda áØÁ=ÂÞÅ:(([])if((áØÁ is ÂÞÅ))else(((ÁØò((lambda ÂîÓ:[]))(ÂÿÇ(áØÁ)))if((áØÁ > 0))else((ÂØÍ(Âêà,(- áØÁ )))([])))))))

#ops_B.☾ (6351 ⟶ 17705)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ops_B.☾')).parent
(ÃÆí:=(lambda áØÆ,áØÁ=ÂÞÅ:((((GET_CASE(áØÆ))if(ÁØö(áØÆ,ÁÜÙ))else((((1)if((áØÆ > 0))else(((((- 1 )))if((áØÆ < 0))else(None)))))))) or (((0)if((áØÁ is ÂÞÅ))else(áØÁ))))))
(ÄÕÇè:=(lambda áØÆ,áØÁ=ÂÞÅ:ÂåÔ(((ÄÊPOP(0))if(ÄÊPSH((ÁØö(áØÆ,ÂÐá) and (áØÁ is ÂÞÅ))))else(ÂùÆ(ÄÊPOP(0),("󰤱")))),(áØÆ + 1))))
(ÄÕÇæ:=(lambda áØÆ,áØÁ=ÂÞÅ:ÂåÔ(((ÄÊPOP(0))if(ÄÊPSH((ÁØö(áØÆ,ÂÐá) and (áØÁ is ÂÞÅ))))else(ÂùÆ(ÄÊPOP(0),("󰤱")))),(áØÆ - 1))))
def ÃÇÆ(áØÆ,áØÇ=ÄÕÍÔ,áØÁ=ÂÞÅ):
    (áØÇ:=((ÄÕÍÔ)if((áØÇ is ÂÞÅ))else(((áØÇ)if(áÓó(áØÇ))else(ÄÊCUR((2,),{},ÂÖÑ,áØÇ,ÂýÃ))))))
    ((ÄÊPOP(0))if(ÄÊPSH(áÓó(áØÇ)))else(ÂùÆ(ÄÊPOP(0),("𝚡 isn\u0027t iterable!"))))
    ((ÄÊPOP(0))if(ÄÊPSH((áØÁ is ÂÞÅ)))else(ÂùÆ(ÄÊPOP(0),("󰤱"))))
    (n:=0)
    for x in(áØÆ):
        if not(áØÇ(x)):continue
        (ÄÊPSH(n),ÄÊPSH(ÄÕÇè(ÄÊPKE(0))),(n:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
    return n

def ÁãÁ(áØÆ,áØÇ=ÄÕÍÔ,ÁÜñ=False):
    (ÄÊPSH(([],[])),((s:=ÄÊPKE(0)[0]),(r:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    for (i,z) in(ÂÓÏ(áØÆ)):
        if not((((v:=áØÇ(z)) not in s) and (v is not ÄÔýò))):continue
        (s).append(v)
        (r).append(((i)if(ÁÜñ)else(z)))
    
    return r

def Âêà(*áÑË,áØÁ=ÂÞÅ):
    if (áØÁ is ÂÞÅ):
        return [*áÑË]
    
    if (áØÁ is áÍé):
        return áÍé(áÑË)
    
    return ((([*áÑË] * áØÁ))if((áØÁ >= 0))else((ÂØÍ(Âêà,ÂüÌ(áØÁ)))(*áÑË)))

def ÄÔéÄ(áØÆ,áØÇ,áØÁ=ÂÞÅ):
    (R:=MOD((lambda ÂîÓ:(([ÁØã])if((ÂîÓ is ÂÞÅ))else((([ÂîÓ])if(ÁØö(ÂîÓ,ÁÜÙ))else(Áÿú(ÂîÓ,ÁÜÙ))))))))
    (Æå:=MOD((lambda ÂîÓ:MOD(ÆÑ,áØÁ=ÂîÓ)((lambda ÂîÓ,ÂîÒ:MOD(ÄÕåØ,áØÁ=ÄÝöÉ(ÂîÒ))(ÂîÓ,ÂîÒ))(R(áØÆ),R(áØÇ)),(lambda x,y:(x).replace(*y))))))
    return ((Æå)if((áØÁ is ÂÞÅ))else(Æå(áØÁ)))

(ÂÓÏ:=(lambda áØÆ,áØÁ=ÂÞÅ:((Áÿú(ÂÿÇ(áØÆ),(lambda x:(x,áØÆ[x]))))if((áØÁ is ÂÞÅ))else(((ÄÕåØ(Áÿú(ÂÿÇ(áØÆ),MOD(Âêà,áØÁ=áÍé)),áØÆ))if((ÂüÌ(áØÁ) == 1))else(MOD(Áëý,áØÁ=(áØÁ > 0))(ËãÂ(ÂÓÏ(áØÆ),(lambda x,y:ÁØò((lambda ÂîÓ:((x,*(ÂîÓ[0])),ÂîÓ[1])))(MOD(ÂÓÏ,áØÁ=(áØÁ - ÃÆí(áØÁ)))(y)))),ÄÔÙù)))))))
(ÂÿÇ:=(lambda áØÆ,áØÁ=ÂÞÅ:((ÄÝöÈ(MOD(Áëý,áØÁ=áÓö)(áØÆ,ãÊú)))if((áØÁ is ÂÞÅ))else(MOD(Áÿú,áØÁ=((ÂüÌ(áØÁ))if((áØÁ < 0))else(1)))(MOD(ÂÓÏ,áØÁ=áØÁ)(MOD(Áëý,áØÁ=Âåæ(Âó,áÓö))(áØÆ,(Âåæ(MOD(ÂØÑ,áØÁ=ÂüÌ(áØÁ)),ÂÿÇ)))),MOD((lambda ÂîÓ:ÂîÓ[0])))))))
@OPWRAP_(*(("⤉⤈⟷")))
def _(áÑã,áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ,ÁÜñ=False):
    if (áÑã == ("⟷")):
        return (MOD(ÂóÌ,áØÁ=áØÁ,ÁÜñ=ÁÜñ)(áØÆ,áØÇ),MOD(ÂóÍ,áØÁ=áØÁ,ÁÜñ=ÁÜñ)(áØÆ,áØÇ))
    
    (áÍÛ:=((ÿ)if((áÑã == ("⤉")))else(ÁÁ)))
    if (áØÇ is ÂÞÅ):
        (ÄÊPSH((áØÆ,ÄÕÍÔ)),((v:=ÄÊPKE(0)[0]),(Æå:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    elif áÓó(áØÇ):
        (ÄÊPSH((áØÆ,áØÇ)),((v:=ÄÊPKE(0)[0]),(Æå:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    else :
        (ÄÊPSH(([áØÆ,áØÇ],ÄÕÍÔ)),((v:=ÄÊPKE(0)[0]),(Æå:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    
    (áÐð:=(áÑÈ:=(áÐø:=ÂÞÅ)))
    for (áÖõ,áÖî) in(ÂÓÏ(v)):
        if not(((áØÆ:=Æå(áÖî)) is not ÄÔýò)):continue
        if (((ÄÊDEL(1),False)[1])if(ÄÊPSH((áÑÈ is ÂÞÅ)))else(((ÄÊPOP(0))if(áÍÛ(áÑÈ,áØÆ))else((ÄÊDEL(1),True)[1])))):
            continue 
        
        (ÄÊPSH((áÖî,áØÆ,áÖõ)),((áÐð:=ÄÊPKE(0)[0]),(áÑÈ:=ÄÊPKE(0)[1]),(áÐø:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
    
    return (((((áÐø)if(ÁÜñ)else(áÐð))))if((áÐð is not ÂÞÅ))else(((áØÁ)if((áØÁ is not ÂÞÅ))else(ÐâÄ(ValueError)))))

(ÄÝöÓ:=(lambda áØÆ,áØÇ,áØÁ=ÂÞÅ:(((lambda x:ÂóÌ(ÂóÍ(áØÆ,x),áØÇ)))if((áØÁ is ÂÞÅ))else(ÂóÌ(ÂóÍ(áØÆ,áØÁ),áØÇ)))))
def ÄÔÞÔ(áØÆ,Æå=áÍÖ,áØÁ=None,ÁÜñ=False):
    if (Æå is ÂÞÅ):
        (Æå:=áÍÖ)
    elif ÄÝøÇ(Æå,áÓó):
        (ÄÊPSH(Æå),ÄÊPSH(CUR((lambda ÂîÓ,ÂîÒ:(ÂîÓ == ÂîÒ)),ÄÊPKE(0))),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
    for (i,x) in(enumerate(áØÆ)):
        if Æå(x):
            return ((i)if(ÁÜñ)else(x))
        
    
    return áØÁ

@OPWRAP_(*(("󷹓󷹔󷹕󷹖")))
def _(áÑã,áØÆ,Æå=áÍÖ,áØÁ=ÂÞÅ,ÁÜñ=False):
    if (((ÁØö(áØÆ,ÄÊPSH(ÁÜÙ)) and ÁØñ(ÄÊPOP(0),ÄÊPSH(Æå))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)):
        (Æå:=CUR((lambda ÂîÓ,ÂîÒ:(ÂîÓ != ÂîÒ)),Æå))
    
    (áÖõ:=MOD(ÄÔÞÔ,ÁÜñ=ÄÕøü)(áØÆ,Æå))
    if ÄÝõÒ(áÖõ):
        if (áØÁ is not ÂÞÅ):
            return áØÁ
        
        return ((ÁØã)if(((not ÁÜñ ) and ÁØö(áØÆ,ÁÜÙ)))else(ÂÚü()))
    
    if ÁÜñ:
        (ÄÊPSH(áØÆ),ÄÊPSH(ÂÿÇ(ÄÊPKE(0))),(áØÆ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
    if (áÑã == ("󷹓")):
        return áØÆ[slice(None,(áÖõ + 1))]
    
    if (áÑã == ("󷹔")):
        return áØÆ[slice(áÖõ,None)]
    
    if (áÑã == ("󷹕")):
        return áØÆ[slice(None,áÖõ)]
    
    if (áÑã == ("󷹖")):
        return áØÆ[slice((1 + áÖõ),None)]
    

@OPWRAP_(*(("󰸵󰸷")))
def _(áÑã,áØÆ,áØÇ,áØÁ=ÂÞÅ):
    if ((((ÁØö(áØÆ,ÄÊPSH(áÍÞ)) and ÁØñ(ÄÊPOP(0),ÄÊPSH(áØÇ))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)) and (áØÁ is ÂÞÅ)):
        if (áÑã == ("󰸵")):
            return MOD(ÄÝöì,áØÁ=ÂÞÅCAT(áØÇ,Ãù))(áØÆ)
        
        (ÄÊPSH(áØÆ),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),ÁÜÙ)),(áØÆ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
        if (áØÁ is ÂÞÅ):
            (áØÁ:=(" "))
        
    
    if (not áÓö(áØÆ) ):
        (ÄÊPSH(áØÆ),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),ÁÜÙ)),(áØÆ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
    if ((l:=(áØÇ - ãÊú(áØÆ))) > 0):
        (r:=([((áØÁ)if((áØÁ is not ÂÞÅ))else((((" "))if(ÁØö(áØÆ,ÁÜÙ))else(False))))] * l))
        if (áÑã == ("󰸵")):
            (r:=ÄÔÙù(r,áØÆ))
        else :
            (r:=ÄÔÙù(áØÆ,r))
        
    else :
        (r:=áØÆ)
    
    return ((Âøî(r))if(ÁØö(áØÆ,ÁÜÙ))else(r))

@OPWRAP_(*(("󷸹󷸺󷸸󷸻")))
def _(áÑã,áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ,ÁÜñ=False):
    ((ÄÊPOP(0))if(ÄÊPSH(((áØÆ is not ÂÞÅ) or (ÂÞÅ is not áØÇ))))else(ÂùÆ(ÄÊPOP(0),("Range missing both values!"))))
    if (áÑÃ:=(áØÁ is ÂÞÅ)):
        (áØÁ:=1)
    
    (v:=((áØÇ)if((áØÆ is ÂÞÅ))else(((áØÆ)if((áØÇ is ÂÞÅ))else(ÂÞÅ)))))
    if (((((áØÆ is not ÂÞÅ) and (ÂÞÅ is not áØÇ)) and (((ÁØö(áØÆ,ÄÊPSH(áÍÞ)) and ÁØñ(ÄÊPOP(0),ÄÊPSH(áØÇ))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False))))if((v is ÂÞÅ))else(ÁØö(v,áÍÞ))):
        if (v is not ÂÞÅ):
            (ÄÊPSH((0,v)),((áØÆ:=ÄÊPKE(0)[0]),(áØÇ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
        
        (ÏÁ:=((((- 1 )))if((áØÇ < áØÆ))else(1)))
        if (áÑÃ and (ÏÁ == ((- 1 )))):
            (áØÁ:=((- 1 )))
        
        if (áÑã == ("󷸹")):
            return [*(range(áØÆ,áØÇ,áØÁ))]
        
        if (áÑã == ("󷸺")):
            return [*(range((áØÆ + ÏÁ),(áØÇ + ÏÁ),áØÁ))]
        
        if (áÑã == ("󷸸")):
            return [*(range((áØÆ + ÏÁ),áØÇ,áØÁ))]
        
        if (áÑã == ("󷸻")):
            return [*(range(áØÆ,(áØÇ + ÏÁ),áØÁ))]
        
    
    if (v is not ÂÞÅ):
        ÂùÆ(ÁØö(v,áÓö))
        (v:=[*v])
        if (áÑã == ("󷸸")):
            return (v[0],v[slice(1,((- 1 )),áØÁ)],v[((- 1 ))])
        
        if áÑÃ:
            (áØÁ:=0)
        
        if (áÑã == ("󷸹")):
            return v[(0 + áØÁ)]
        
        if (áÑã == ("󷸺")):
            return v[(((- 1 )) - áØÁ)]
        
        if (áÑã == ("󷸻")):
            return (v[(0 + áØÁ)],v[(((- 1 )) - áØÁ)])
        
    
    if ÁØö(áØÆ,slice):
        (áØÆ:=[*(range((áØÆ).start,(áØÆ).stop,(áØÆ).step))])
    
    if ÁÜñ:
        if áÓö(áØÆ):
            (ÄÊPSH(áØÆ),ÄÊPSH(ÂÿÇ(ÄÊPKE(0))),(áØÆ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
        elif áÓö(áØÇ):
            (ÄÊPSH(áØÇ),ÄÊPSH(ÂÿÇ(ÄÊPKE(0))),(áØÇ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
        
    
    if (áÓö(áØÆ) and áÓö(áØÇ)):
        return [(áØÆ[(h % ãÊú(áØÆ))])for h in(áØÇ[slice(None,None,áØÁ)])]
    
    if (áÓö(áØÆ) and ÁØö(áØÇ,slice)):
        return áØÆ[áØÇ]
    
    if (áÓö(áØÆ) and ÁØö(áØÇ,áÍÞ)):
        if (áÑã == ("󷸹")):
            return áØÆ[slice(None,áØÇ,áØÁ)]
        
        if (áÑã == ("󷸺")):
            return áØÆ[slice(1,(áØÇ + 1),áØÁ)]
        
        if (áÑã == ("󷸸")):
            return áØÆ[slice(1,áØÇ,áØÁ)]
        
        if (áÑã == ("󷸻")):
            return áØÆ[slice(None,(áØÇ + 1),áØÁ)]
        
    
    if (ÁØö(áØÆ,áÍÞ) and áÓö(áØÇ)):
        if (áÑã == ("󷸹")):
            return áØÇ[slice(áØÆ,((- 1 )),áØÁ)]
        
        if (áÑã == ("󷸺")):
            return áØÇ[slice((áØÆ + 1),None,áØÁ)]
        
        if (áÑã == ("󷸸")):
            return áØÇ[slice((áØÆ + 1),((- 1 )),áØÁ)]
        
        if (áÑã == ("󷸻")):
            return áØÇ[slice(áØÆ,None,áØÁ)]
        
    
    ((ÄÊPOP(0))if(ÄÊPSH(False))else(ÂùÆ(ÄÊPOP(0),("Invalid argument types! %s %s")%(ÁØö(áØÆ),ÁØö(áØÇ),))))

def áÇù(x,y=ÂÞÅ,áØÁ=ÂÒå,ÁÜñ=False):
    if (not x ):
        return []
    
    if ÁØö(x,áÍÞ):
        (ÄÊPSH(x),ÄÊPSH(ÂÿÇ(ÄÊPKE(0))),(x:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
    if (y is ÂÞÅ):
        (y:=ÄÕÍÔ)
    
    if ÁÜñ:
        return MOD(áÇù,áØÁ=áØÁ)(ÂÿÇ(x),(((lambda i:y(x[i])))if(áÓó(y))else(y)))
    elif ÁØö(y,áÍÞ):
        return [x[slice(None,y)],x[slice(y,None)]]
    elif (not áÓó(y) ):
        ÂùÆ(áÓö(y))
        (y:={*(MOD(ÄÔÔç,áØÁ=MOD((lambda ÂîÓ:ÂÁÍ(ì)(ÂîÓ,ãÊú(x)))))(y,MOD((lambda ÂîÓ:(ÂîÓ < 0)))))})
        (ÄÊPSH(([],[])),((R:=ÄÊPKE(0)[0]),(áÍÌ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
        for (áÑî,áÑü) in(ÂÓÏ(x)):
            if (áÑî in y):
                (áÍÌ).append(R)
                (R:=[])
            
            (R).append(áÑü)
        
        if R:
            (áÍÌ).append(R)
        
        return áÍÌ
    
    (ÄÊPSH((y((áÝÌ:=x[0])),(([áÝÌ])if((áÝÌ is not ÄÔýò))else(ÂÚü())),[])),((áÍç:=ÄÊPKE(0)[0]),(R:=ÄÊPKE(0)[1]),(áÍÌ:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
    for (áÑî,áÑü) in(ÂÓÏ(x)[slice(1,None)]):
        if ((r:=y(áÑü)) != áÍç):
            (áÍÌ).append(R)
            (ÄÊPSH((r,[])),((áÍç:=ÄÊPKE(0)[0]),(R:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
            if (not (ÄÊPSH(áØÁ),ÄÊPSH((ÄÊPKE(0) - 1)),(áØÁ:=ÄÊPKE(0)),ÄÊDEL(2))[2] ):
                (áÍÌ).append(x[slice((áÑî + (r is ÄÔýò)),None)])
                break 
            
        
        if (r is not ÄÔýò):
            (R).append(áÑü)
        
    
    if R:
        (áÍÌ).append(R)
    
    (áÍÌ:=ÄÔÔè(áÍÌ,MOD((lambda ÂîÓ:(ÂîÓ == [])))))
    if ÁØö(x,ÁÜÙ):
        (áÍÌ:=MOD(ÄÔÔç,áØÁ=MOD((lambda ÂîÓ:Âøî(ÂîÓ,ÁØã))))(áÍÌ,MOD((lambda ÂîÓ:ÄÝøÇ(ÂîÓ,ÁÜÙ)))))
    
    return áÍÌ

@OPWRAP_(*(("⨝⟕⟖⟗")))
def _(áÑã,áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ,LR_def=None,bound_mode=ÂÞÅ):
    ((ÄÊPOP(0))if(ÄÊPSH(((áØÆ is not ÂÞÅ) or (ÂÞÅ is not áØÇ))))else(ÂùÆ(ÄÊPOP(0),("Join missing both values!"))))
    if (áØÁ is not ÂÞÅ):
        (bound_mode:=áØÁ)
    
    if (bound_mode is ÂÞÅ):
        (bound_mode:=(((áÑã == ("⟗")) and 1) or 0))
    
    if (áØÆ is ÂÞÅ):
        (ÄÊPSH((áØÇ,áØÆ)),((áØÆ:=ÄÊPKE(0)[0]),(áØÇ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    
    if (áØÇ is ÂÞÅ):
        ((ÄÊPOP(0))if(ÄÊPSH(áÓö(áØÆ)))else(ÂùÆ(ÄÊPOP(0),("Single-arg %s needs an iterable")%(áÑã,))))
        return (((("\x0A") * ((áÑã in ("⟕⟗")))) + (ÁØã).join(Áÿú(áØÆ,ÁÜÙ))) + ((ÂÔö(("⟗⟖"),áÑã)) * ("\x0A")))
    
    (Y:=áØÇ)
    if (not áÓó(áØÇ) ):
        (ÄÊPSH(áØÇ),ÄÊPSH((lambda ÂîÓ:(lambda *áÑË:ÂîÓ))(ÄÊPKE(0))),(áØÇ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
    (ÄÊPSH(([*áØÆ],[])),((áØÆ:=ÄÊPKE(0)[0]),(R:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    if ((ãÊú(áØÆ) == 0) and (((áÑã != ("⨝")) or (bound_mode > 0)))):
        if ((v:=áØÇ(LR_def,LR_def)) is ÄÔýò):
            (R:=[])
        
        if ((áÑã in ("⟕⟖")) or (bound_mode == 1)):
            (R:=[v])
        else :
            (R:=[v,v])
        
    else :
        if ((áÑã in ("⟕⟗")) and (ÄÔýò is not (áÑÿ:=áØÇ(LR_def,áØÆ[0])))):
            (R).append(áÑÿ)
        
        for i in(ÄÝöÇ(ãÊú(áØÆ))):
            (R).extend((([áØÆ[(i - 1)]])if(((áÑÿ:=áØÇ(áØÆ[(i - 1)],áØÆ[i])) is ÄÔýò))else([áØÆ[(i - 1)],áÑÿ])))
        
        if ãÊú(áØÆ):
            (R).append(áØÆ[((- 1 ))])
        
        if ((áÑã in ("⟖⟗")) and (ÄÔýò is not (áÑÿ:=áØÇ(áØÆ[((- 1 ))],LR_def)))):
            (R).append(áÑÿ)
        
    
    return (((ÁØã).join(Áÿú(R,ÁÜÙ)))if(ÁØö(Y,ÁÜÙ))else(R))

@OPWRAP_(*(("󷹌󷹍󷹎󷹑")))
def _(áÑã,áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=((- 1 ))):
    if ÁØö(áØÁ,áÍé):
        (ÄÊPSH(((ÂÀÇ(áØÁ))if((áØÁ[0] == áÍá))else(áØÁ))),((n:=ÄÊPKE(0)[0]),(L:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    else :
        (ÄÊPSH((([((- 1 )),True])if((áØÁ == áÍá))else([áØÁ,False]))),((n:=ÄÊPKE(0)[0]),(L:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    
    if (((not L ) and ÁØö(áØÆ,ÁÜÙ)) and ((áØÇ is ÂÞÅ) or ÁØö(áØÇ,ÁÜÙ))):
        (áÏÞ:=((())if((áØÇ is ÂÞÅ))else((áØÇ,))))
        if (áÑã in ("󷹎󷹑")):
            (r:=(áØÆ).split(*áÏÞ,maxsplit=n))
            return ((ÄÔÔç(r))if((áÑã == ("󷹎")))else(r))
        
    
    if (áØÇ is ÂÞÅ):
        (áØÇ:=Âó)
    
    if (not ((YS:=ÁØö(áØÇ,ÁÜÙ)) and L) ):
        (ÄÊPSH((Áÿú(Ááú(áØÆ,[0,(ãÊú(áØÇ) - 1)]),MOD((lambda ÂîÓ:Âøî(ÄÔÔç(ÂîÓ))))),CUR((lambda ÂîÓ,ÂîÒ:(ÂîÓ == ÂîÒ)),áØÇ),ãÊú(áØÇ),(ãÊú(áØÇ) - 1))),((áØÆ:=ÄÊPKE(0)[0]),(áØÇ:=ÄÊPKE(0)[1]),(Y:=ÄÊPKE(0)[2]),(ÏÁ:=ÄÊPKE(0)[3])),ÄÊDEL(1))[1]
    else :
        (ÄÊPSH(([*áØÆ],((áØÇ)if(áÓó(áØÇ))else((CUR((lambda ÂîÓ,ÂîÒ:(ÂîÓ == ÂîÒ)),áØÇ)))),0)),((áØÆ:=ÄÊPKE(0)[0]),(áØÇ:=ÄÊPKE(0)[1]),(ÏÁ:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
    
    (ÄÊPSH(([],[],((- 1 )),0)),((r:=ÄÊPKE(0)[0]),(b:=ÄÊPKE(0)[1]),(Ïç:=ÄÊPKE(0)[2]),(Ïñ:=ÄÊPKE(0)[3])),ÄÊDEL(1))[1]
    (last_v:=False)
    while(((((ÄÊPSH(Ïç),ÄÊPSH((ÄÊPKE(0) + 1)),(Ïç:=ÄÊPKE(0)),ÄÊDEL(2))[2] < ãÊú(áØÆ))) and (Ïñ < (((ÂÕË)if((n == ((- 1 ))))else(n)))))):
        (áÐÏ:=áØÆ[Ïç])
        if (áÑÿ:=áØÇ(áÐÏ)):
            if (b or (áÑã != ("󷹎"))):
                if (áÑã == ("󷹎")):
                    (r).append(b)
                elif ((áÑã in ("󷹌󷹑")) or ((áÑã == ("󷹍")) and (not last_v ))):
                    (r).extend((([b])if((áÑÿ is ÄÔýò))else([b,áÐÏ])))
                    (last_v:=True)
                
            
            (b:=[])
            (ÄÊPSH(Ïç),ÄÊPSH((ÄÊPKE(0) + ÏÁ)),(Ïç:=ÄÊPKE(0)),ÄÊDEL(2))[2]
            (ÄÊPSH(Ïñ),ÄÊPSH((ÄÊPKE(0) + 1)),(Ïñ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
        elif (áÑÿ is not ÄÔýò):
            (b).append(áÐÏ)
            (last_v:=False)
        
    
    if (b or (áÑã != ("󷹎"))):
        (b).extend(áØÆ[slice(Ïç,None)])
        (r).append(b)
    elif áØÆ[slice(Ïç,None)]:
        (r).append(áØÆ[slice(Ïç,None)])
    
    return (((ÁØò((lambda ÂîÓ:(((Âøî(ÁØò((lambda ÂîÓ:ÂîÓ[0]))(ÂîÓ))))if(ÁØö(ÂîÓ,áÍá))else(ÂîÓ))))(r)))if(YS)else(r))

@OPWRAP_(*(("⫰⫯󷹒")))
def _(áÑã,áØÆ,áØÁ=ÂÞÅ,ÁÜñ=ÂÞÅ):
    if (ÁÜñ is not ÂÞÅ):
        ÂùÆ((ÁØö(áØÆ,ÁÜÙ) and (áÑã != ("󷹒"))))
        return MOD(ÄÔÔç,ÁÜñ=ÄÕøü)(áØÆ,CURR((lambda ÂîÓ,ÂîÒ:(ÃÆí(ÂîÓ) == ÂîÒ)),((áÑã == ("⫰")) or ((- 1 )))))
    
    if (áÑã == ("⫰")):
        (v:=((TO_UPPERCASE(áØÆ))if(ÁØö(áØÆ,ÁÜÙ))else((+ abs(áØÆ) ))))
    elif (áÑã == ("⫯")):
        (v:=((TO_LOWERCASE(áØÆ))if(ÁØö(áØÆ,ÁÜÙ))else((- abs(áØÆ) ))))
    elif (áÑã == ("󷹒")):
        if ((áØÁ is not ÂÞÅ) and ÁØö(áØÁ,ÂÑÅ)):
            return ((((((ÂüÌ)if((v == 1))else(ÂüË))))if((v:=ÃÆí(áØÁ)))else(ÄÝöâ)))(áØÆ,áØÁ=ÂÞÅ,ÁÜñ=ÁÜñ)
        
        (v:=((REVERSE_CASE(áØÆ))if(ÁØö(áØÆ,ÁÜÙ))else((- áØÆ ))))
    
    if (áØÁ is ÂÞÅ):
        return v
    
    ÂùÆ(áÓó(áØÁ))
    (áØÁ:=áØÁ(v))
    if ÄÝøÇ(áØÆ,ÁÜÙ):
        if (áÑã == ("⫰")):
            return (((- áØÁ ))if((áØÆ < 0))else(áØÁ))
        elif (áÑã == ("⫯")):
            return (((- áØÁ ))if((áØÆ > 0))else(áØÁ))
        elif (áÑã == ("󷹒")):
            return ((áØÁ)if((not áØÆ ))else((- áØÁ )))
        
    
    return Âøî(ËãÂ(ÂÛÅ([áØÆ,v,áØÁ]),(lambda x,y,z:MOD(Áëý,áØÁ=(ÃÆí(x) != ÃÆí(y)))(z,MOD(ÄÝöâ,áØÁ=ÃÆí(x))))))

def ÄÝöì(áØÆ=ÂÞÅ,áØÁ=ÂÞÅ,C=ÂÞÅ):
    (nc:=(C is ÂÞÅ))
    if nc:
        (C:=((num + ABC) + abc))
    elif (áØÁ is ÂÞÅ):
        (áØÁ:=ãÊú(C))
    
    if (áØÁ is ÂÞÅ):
        if ÄÝøÇ(áØÆ,ÁÜÙ):
            if (áØÆ != Âäû(áØÆ)):
                return ÁÜÙ(áØÆ)
            
        elif ((".") in áØÆ):
            return áÍÛ(áØÆ)
        
        (áØÇ:=10)
    elif ÁØö(áØÁ,áÓö):
        (ÄÊPSH((([áØÁ[0],ÂÞÅ])if((ãÊú(áØÁ) == 1))else(áØÁ))),((áØÇ:=ÄÊPKE(0)[0]),(áØÁ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    elif ÁØö(áØÁ,ÂÐý):
        (ÄÊPSH((Âüð(áØÁ),ÂÞÅ)),((áØÇ:=ÄÊPKE(0)[0]),(áØÁ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    else :
        (ÄÊPSH(MOD(ÁÞç,áØÁ=0)(Áÿú(ÄÝõé(áØÁ),Âüð),MOD((lambda ÂîÓ:(ÂîÓ or 10))))),((áØÇ:=ÄÊPKE(0)[0]),(áØÁ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    
    if MOD(ÁØö,áØÁ=ÂÕó)(áØÆ,áÍÛ):
        (ÄÊPSH(áØÆ),ÄÊPSH(Âäû(ÄÊPKE(0))),(áØÆ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    elif ÁØö(áØÆ,ÁÜÙ):
        if (áØÆ and (áØÆ[0] == ("-"))):
            (ÄÊPSH((áØÆ[slice(1,None)],((- 1 )))),((áØÆ:=ÄÊPKE(0)[0]),(p:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
        else :
            (p:=1)
        
        if (nc and (áØÇ <= 36)):
            (ÄÊPSH(áØÆ),ÄÊPSH(ÂüÌ(ÄÊPKE(0))),(áØÆ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
        
        (áØÆ:=(MOD(ÆÑ,áØÁ=0)(ÁØò((lambda ÂîÓ:MOD(ÄÔÞÔ,ÁÜñ=ÄÕøü)(C,ÂîÓ)))(áØÆ),CUR((lambda ÂîÓ,ÂîÒ:((ÂîÓ * áØÇ) + ÂîÒ)))) * p))
        if (áØÁ is ÂÞÅ):
            return áØÆ
        
    
    if (áØÁ is ÂÞÅ):
        (áØÁ:=1)
    
    (ÂÐôþáÏß:=CUR((lambda ÂîÓ,ÂîÒ:Âøî(ÂÀÇ(ÁØò((lambda ÂîÓ:ÂîÒ[(ÂîÓ % ãÊú(ÂîÒ))]))((ÂÛÜ(MOD((lambda ÂîÓ:(ÂîÓ // ãÊú(ÂîÒ)))),Âó))(ÂîÓ)))))))
    (ÂÑÅþáÏß:=CUR((lambda ÂîÓ,ÂîÒ,*áÏÞ:(((ÂîÓ < 0) * ("-")) + MOD(ÄÕÊÂ,áØÁ=ÂîÒ[0])(ÂÐôþáÏß(ÂüÌ(ÂîÓ),ÂîÒ),áÏÞ[0])))))
    return ÂÑÅþáÏß(áØÆ,ÄÝöÈ(C,áØÇ),áØÁ)

(ÄÔóÅ:=(lambda áØÆ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:((phase((áØÆ + ÂÞÅCAT(áØÇ,Ãù))))if((áØÇ is not ÂÞÅ))else(((phase(áØÆ))if(ÁØö(áØÆ,ÂÐá))else(phase(ÄÝõé(áØÆ))))))))
(Âõì:=(lambda áØÆ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:((rect(áØÆ,áØÇ))if((áØÇ is not ÂÞÅ))else(((rect(*áØÆ))if(ÁØö(áØÆ,áÓö))else(((polar(áØÆ))if((s is ÂÞÅ))else(ÂÞÅCAT(áØÆ,(ÂÐæ ** ÂÞÅCAT(áØÁ,Ãù)))))))))))
@OPWRAP_(*(("󷸓󷸼󷸔")))
def _(áÑã,áØÆ,áØÁ=ÂÞÅ,ÁÜñ=ÂÞÅ):
    if (áØÆ is ë):
        ((ÄÊPOP(0))if(ÄÊPSH(((ÁÜñ is ÂÞÅ) and (áØÁ is ÂÞÅ))))else(ÂùÆ(ÄÊPOP(0),("no"))))
        return ((SUBSCRIPT)if((áÑã == ("󷸓")))else(((SUPSCRIPT)if((áÑã == ("󷸔")))else((ÄÝõà(ë),ÄÝõá(ë))))))
    
    (áØÆ:=ÁÜÙ(áØÆ))
    if (ÁÜñ is not ÂÞÅ):
        if (áÑã == ("󷸼")):
            ((ÄÊPOP(0))if(ÄÊPSH((áØÁ is ÂÞÅ)))else(ÂùÆ(ÄÊPOP(0),("󰤱"))))
            ((ÄÊPOP(0))if(ÄÊPSH(ÁØö(ÁÜñ,áÓó)))else(ÂùÆ(ÄÊPOP(0),("󰤱"))))
            return under_script(áØÆ,ÁÜñ)
        
        ((ÄÊPOP(0))if(ÄÊPSH(False))else(ÂùÆ(ÄÊPOP(0),("󰤱"))))
    
    if (áØÁ is ÂÞÅ):
        (áØÁ:=1)
    
    if (áØÁ > 0):
        (Æå:=((subscript)if((áÑã == ("󷸓")))else(((supscript)if((áÑã == ("󷸔")))else(nrmscript)))))
        return ÂÕÅ(ÂØÍ(Æå,áØÁ),áØÆ)
    


#ops_C.☾ (3099 ⟶ 8895)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ops_C.☾')).parent
@OPWRAP_(*(("󱑼󷹅")))
def _(áÑã,áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
    (áÖÒ:=((áØÆ)if((áØÇ is ÂÞÅ))else((áØÆ,áØÇ))))
    (ÄÊPSH(MOD(ÐÌÛ,áØÁ=áÍÖ,ÁÜñ=ÄÕøü)(áÖÒ,áÓö)),((N:=ÄÊPKE(0)[0]),(I:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    (ÄÊPSH(Âîí(Áÿú(ÄÝöÊ(áÖÒ,I),ãÊú))),((l:=ÄÊPKE(0)[0]),(h:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    if N:
        (ÄÊPSH(áÖÒ),ÄÊPSH(MOD(ÁÞç,áØÁ=N)(ÄÊPKE(0),MOD(ÁØò((lambda ÂîÓ:MOD(Âêà,áØÁ=h)(ÂîÓ)))))),(áÖÒ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
    if (áØÁ is ÂÞÅ):
        if (áÑã == ("󷹅")):
            (áÖÒ:=ÁØòþÁÙÄ((lambda ÂîÓ,ÂîÒ:ÂîÓ[slice((ãÊú(ÂîÓ) - ÂîÒ),None)]))(áÖÒ,l))
        
    else :
        (ÄÊPSH(áÖÒ),ÄÊPSH(Áÿú(ÄÊPKE(0),Âåæ((((MOD((lambda ÂîÓ:MOD(ÄÕÊÄ,áØÁ=((ÂîÓ[((- 1 ))])if((áØÁ is ÄÕøü))else(áØÁ)))(ÂîÓ,h))))if((áÑã == ("󱑼")))else(MOD((lambda ÂîÓ:MOD(ÄÕÊÂ,áØÁ=((ÂîÓ[0])if((áØÁ is ÄÕøü))else(áØÁ)))(ÂîÓ,h)))))),áÍá))),(áÖÒ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
    (r:=[*(zip(*áÖÒ))])
    return ((Áÿú(r,ÄÊCUR((1,),{},ÄÔÔè,ÂýÃ,ÄÔýò)))if((áØÁ is ÄÔýò))else(r))

def ÁÛÛ(áØÆ,áØÁ=ÂÞÅ):
    def Æå(áØÁ):
        if (ÄÝøÇ(áØÁ,áÓö) or ÁØñ(ÁÜÙ,áØÁ)):
            (ÄÊPSH(áØÁ),ÄÊPSH(Âêà(ÄÊPKE(0))),(áØÁ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
        
        (áÓÕ:=((MOD(ÁÛÛ,áØÁ=áØÁ[slice(1,None)]))if((ãÊú(áØÁ) > 1))else(ÄÕÍÔ)))
        (áÓÙ:=(lambda x,y:((áÓÕ(x[(y % ãÊú(x))]))if(ÁØö(y,ÂÑÅ))else(((áÓÕ(x[y]))if((ÁØö(y,ÁÜÙ) or (((ÄÝøÆ(áÓö,ÄÊPSH(y)) and ÄÝøÇ(ÄÊPOP(0),ÄÊPSH(slice))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False))))else(MOD(Áëý,áØÁ=(áÓÕ is not ÄÕÍÔ))(ÄÝöÊ(x,y),MOD((lambda ÂîÓ:Áÿú(ÂîÓ,áÓÕ))))))))))
        return áÓÙ(áØÆ,áØÁ[0])
    
    return ((Æå)if((áØÁ is ÂÞÅ))else(Æå(áØÁ)))

def ÁÝÖ(áØÆ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
    ((ÄÊPOP(0))if(ÄÊPSH(ÁØö(áØÆ,áÓö)))else(ÂùÆ(ÄÊPOP(0),("%s󷹵𝗜")%(áØÆ,))))
    ((ÄÊPOP(0))if(ÄÊPSH((áØÁ is not ÂÞÅ)))else(ÂùÆ(ÄÊPOP(0),("ᕋ requires modifier"))))
    (áØÆ:=((ÄÔÙù(áØÆ))if(((is_str:=ÁØö(áØÆ,ÁÜÙ))))else(ÐÌü((áØÆ).copy))))
    (áØÇ:=((MOD(Áëý,áØÁ=ÄÝøÇ(áØÇ,áÓö))(áØÇ,Âêà))if((áØÇ is not ÂÞÅ))else(ÂÚü())))
    (áØÁ:=((slice((ÄÊPSH(áØÁ),ÄÊPSH((ÄÊPKE(0) % ãÊú(áØÆ))),(áØÁ:=ÄÊPKE(0)),ÄÊDEL(2))[2],(áØÁ + 1)))if(ÁØö(áØÁ,áÍÞ))else(áØÁ)))
    if ÁØö(áØÁ,slice):
        (ÄÊPSH(áØÆ),ÄÊPSH(áØÁ),ÄÊPSH(áØÇ),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
    elif ÁØö(áØÁ,áÓö):
        for (i,(z,n)) in(ÂÓÏ(ÁØò((lambda ÂîÓ:ãÊú([ÂîÓ[0],ÂîÓ])))(áÇù(ÄÔàÒ(ÁØò((lambda ÂîÓ:(ÂîÓ % ãÊú(áØÆ))))(áØÁ)))))):
            if ((áØÇ is ÂÞÅ) or (i >= ãÊú(áØÇ))):
                del áØÆ[z]
            else :
                (ÄÊPSH(áØÆ),ÄÊPSH(slice(z,(z + 1))),ÄÊPSH(MOD(Âêà,áØÁ=n)(áØÇ[i])),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
            
        
    else :
        ((ÄÊPOP(0))if(ÄÊPSH(False))else(ÂùÆ(ÄÊPOP(0),("Modifier 󷹵 slice|𝑖|𝗜"))))
    
    return ((Âøî(áØÆ,ÁØã))if(is_str)else(áØÆ))

(ÂÕÅ:=(lambda áØÆ,áØÇ,áØÁ=1:áØÆ(*(MOD(Âêà,áØÁ=áØÁ)(áØÇ)))))
def Áëý(áØÆ,áØÇ,áØÁ=ÂÞÅ):
    (v:=((áØÆ)if((áØÁ is ÂÞÅ))else(((áØÁ(áØÆ))if(áÓó(áØÁ))else(áØÁ)))))
    if áÓó(áØÇ):
        return ((áØÇ(áØÆ))if(v)else(áØÆ))
    
    if áÓö(áØÇ):
        if (ãÊú(áØÇ) == 1):
            return ((áØÇ[0](áØÆ))if(v)else(v))
        
        if (ãÊú(áØÇ) == 2):
            return áØÇ[áÍÖ(v)](áØÆ)
        
    
    ((ÄÊPOP(0))if(ÄÊPSH(False))else(ÂùÆ(ÄÊPOP(0),("Unsupport type of 𝚢 in ᣆ: %s")%(ÁØö(áØÇ),))))

@OPWRAP_(*(("○⍜󰬫󰬩")))
def _(áÑã,áÍÛ,áÍÜ,áØÁ=1):
    if (áÑã in ("󰬩󰬫")):
        ((ÄÊPOP(0))if(ÄÊPSH((((ÄÊDEL(1),False)[1])if(ÄÊPSH((áØÁ == ì)))else(((ÄÊPOP(0))if((î == áØÁ))else((ÄÊDEL(1),True)[1]))))))else(ÂùÆ(ÄÊPOP(0),("󰤱 generalize"))))
        if ((not áØÁ ) or ÁØö(áÍÜ,áÓö)):
            def Æå(*áÑË):
                if (áØÁ == 0):
                    (áÖÒ:=[Áÿú((MOD(Áëý,áØÁ=ÁØö(áÍÜ,áÓó))(áÍÜ,Âêà)),ÐÌü),áÑË])
                else :
                    (áÖû:=(ãÊú(áÍÜ) * (S:=ÂüÌ(áØÁ))))
                    if (áØÁ < 0):
                        (ÄÊPSH(áÑË),ÄÊPSH(Âúú(ÄÊPKE(0),(ãÊú(áÑË) - áÖû))),(áÑË:=ÄÊPKE(0)),ÄÊDEL(2))[2]
                    
                    if (áÑã == ("󰬫")):
                        (ÄÊPSH(MOD(ÄÕÊÄ,áØÁ=[])(áÇù(áÑË,áÖû),2)),((Ïß:=ÄÊPKE(0)[0]),(Ïà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
                    elif (áÑã == ("󰬩")):
                        (ÄÊPSH(MOD(ÄÕÊÂ,áØÁ=[])(áÇù(áÑË,ÂóÍ((ãÊú(áÑË) - áÖû),0)),2)),((Ïà:=ÄÊPKE(0)[0]),(Ïß:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
                    
                    (áÖÒ:=[ÁØò((lambda ÂîÓ:ÂîÓ[1](*(ÂîÓ[0]))))((((ÄÕåØ)if((áØÁ < 0))else(ÄÝöÔ)))[[]](MOD(Ááú,áØÁ=ÄÔýò)(Ïß,[0,(S - 1),S]),áÍÜ)),Ïà])
                
                return ÄÔÙù(MOD(Áëý,áØÁ=(áÑã == ("󰬩")))(áÖÒ,ÂÀÇ))
            
        else :
            def Æå(*áÑË):
                (áÖí:=((ãÊú(áÑË) // (((S:=ÂüÌ(áØÁ)) or 1))) * S))
                (ÄÊPSH(áÇù(ÂÿÇ(áÑË),(((áÖí)if((áÑã == ("󰬫")))else((ãÊú(áÑË) - áÖí)))))),((Ïß:=ÄÊPKE(0)[0]),(Ïà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
                if (Ïß and (áØÁ < 0)):
                    (ÄÊPSH((ÁØò((lambda ÂîÓ:(ÂîÓ + ãÊú(Ïà))))(Ïß),ÂÿÇ(Ïà))),((Ïß:=ÄÊPKE(0)[0]),(Ïà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
                
                (ÄÊPSH((ÄÝöÊ(áÑË,Ïß),ÄÝöÊ(áÑË,Ïà))),((Ïß:=ÄÊPKE(0)[0]),(Ïà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
                if (áÑã == ("󰬫")):
                    return (*(ËãÂ(MOD(ÁâÁ,áØÁ=ÂóÍ((S - 1),0))(Ïß),áÍÜ)),*Ïà)
                elif (áÑã == ("󰬩")):
                    return (*Ïß,*(ËãÂ(MOD(ÁâÁ,áØÁ=ÂóÍ((S - 1),0))(Ïà),áÍÜ)))
                
            
        
    elif ÁØö(áÍÜ,áÓó):
        def Æå(*áÑË):
            (ÄÊPSH((((L:=ãÊú(áÑË)) // (S:=ÂüÌ(áØÁ))),(L % S))),((n:=ÄÊPKE(0)[0]),(m:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
            ((ÄÊPOP(0))if(ÄÊPSH((n != 0)))else(ÂùÆ(ÄÊPOP(0),("󰤱 generalize"))))
            (áÖÒ:=(((MOD(ÄÕÊÄ,áØÁ=ÂýÃ))if((áÑã == ("○")))else(MOD(ÄÕÊÂ,áØÁ=ÂýÃ))))(áÑË,(L + ((n - m) % n))))
            (v:=MOD(ÁâÁ,áØÁ=(n - 1))(áÖÒ))
            if (m != 0):
                (ÄÊPSH((([((- 1 )),0])if((áÑã == ("○")))else([0,((- 1 ))]))),((Ïß:=ÄÊPKE(0)[0]),(Ïà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
                if ÄÝøø((áÑã == ("⍜")),(áØÁ < 0)):
                    (ÄÊPSH(v),ÄÊPSH(Ïß),ÄÊPSH(ÄÔÙù(ÂÀÇ(áÇù(v[Ïß],MOD((lambda ÂîÓ:(ÂîÓ is (ÂýÃ)))))))),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
                
                (ÄÊPSH(v),ÄÊPSH(Ïß),ÄÊPSH(ÁØòþÁÙÇ((lambda ÂîÓ,ÂîÒ:((ÂîÓ)if((ÂîÓ is not (ÂýÃ)))else(ÂîÒ))))(v[Ïß],v[Ïà])),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
            
            return ËãÂ(v,áÍÜ)
        
    elif ÁØö(áÍÜ,áÓö):
        def Æå(*áÑË):
            ((ÄÊPOP(0))if(ÄÊPSH((ãÊú(áÑË) >= ((ãÊú(áÍÜ) * (S:=ÂüÌ(áØÁ)))))))else(ÂùÆ(ÄÊPOP(0),("󰤱 generalize"))))
            ((ÄÊPOP(0))if(ÄÊPSH((áØÁ > 0)))else(ÂùÆ(ÄÊPOP(0),("󰤱 generalize"))))
            ((ÄÊPOP(0))if(ÄÊPSH((áÑã != ("⍜"))))else(ÂùÆ(ÄÊPOP(0),("󰤱 generalize"))))
            (ÄÊPSH(áÇù(áÑË,(ãÊú(áÍÜ) * (S:=ÂüÌ(áØÁ))))),((l:=ÄÊPKE(0)[0]),(r:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
            (áÖÒ:=ÁØòþÁÙÄ((lambda ÂîÓ,ÂîÒ:ÄÔÙù(ÂîÓ,ÂîÒ)))(MOD(ÁâÁ,áØÁ=(S - 1))(l),r))
            return ËãÂ(ÄÕåØ(áÖÒ,áÍÜ),(lambda x,y:y(*x)))
        
    
    return (lambda *áÑË,**áÑÕ:áÍÛ(*(Æå(*áÑË)),**áÑÕ))

@OPWRAP_(*(("⊚⊜🟕🟖⊛⍟")))
def _(áÑã,Æå=ÂÞÅ,áÍÜ=ÂÞÅ,áØÁ=ÂÕË):
    if (not áÓó(Æå) ):
        (ÄÊPSH((áÍÜ,Æå)),((Æå:=ÄÊPKE(0)[0]),(áÍÜ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    
    if (áÍÜ is ÂÞÅ):
        (áÍÜ:=ÄÕÍÔ)
    elif (ÁØö(áÍÜ,áÍÞ) and (áÑã in ("⊚⊛⍟"))):
        (áÍÜ:=Ticker((áÍÜ + 1)))
    
    def r(*áÑË,**áÑÕ):
        (ÄÊPSH((ÂüÌ(áØÁ),((áÑË[0])if(áÑË)else(None)),áÍÜ(*áÑË,**áÑÕ))),((n:=ÄÊPKE(0)[0]),(f:=ÄÊPKE(0)[1]),(g:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
        if (áÑã == ("⊚")):
            if g:
                return f
            
            while((0 < (ÄÊPSH(n),ÄÊPSH((ÄÊPKE(0) - 1)),(n:=ÄÊPKE(0)),ÄÊDEL(2))[2])):
                if áÍÜ((f:=Æå(f))):
                    return f
                
            
        elif (áÑã == ("⊜")):
            while((0 < (ÄÊPSH(n),ÄÊPSH((ÄÊPKE(0) - 1)),(n:=ÄÊPKE(0)),ÄÊDEL(2))[2])):
                if (g == ((g:=áÍÜ((nf:=Æå(f)))))):
                    return f
                
                (f:=nf)
            
        elif (áÑã in ("⊛⍟")):
            (rf:=[f])
            if g:
                return ((rf)if((áÑã == ("⊛")))else([]))
            
            while((0 < (ÄÊPSH(n),ÄÊPSH((ÄÊPKE(0) - 1)),(n:=ÄÊPKE(0)),ÄÊDEL(2))[2])):
                (g:=áÍÜ((f:=Æå(f))))
                if ((not g ) or (áÑã == ("⊛"))):
                    (rf).append(f)
                
                if g:
                    return rf
                
            
            if (áØÁ < 0):
                return rf
            
        elif (áÑã in ("🟕🟖")):
            (ÄÊPSH(([f],[g])),((rf:=ÄÊPKE(0)[0]),(rg:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
            while((0 < (ÄÊPSH(n),ÄÊPSH((ÄÊPKE(0) - 1)),(n:=ÄÊPKE(0)),ÄÊDEL(2))[2])):
                if ((g:=áÍÜ((f:=Æå(f)))) in rg):
                    if (áÑã == ("🟖")):
                        return rf
                    
                    return ÄÝöÊ((MOD(ÄÔÞÔ,ÁÜñ=ÄÕøü)(rg,(lambda x:(x == g)))),rf)
                
                (rf).append(f)
                (rg).append(g)
            
        
        return None
    
    return r


#ops_.☾ (1379 ⟶ 3476)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ops_\uea8c.☾')).parent
(áÍù:=áÓö)
def adjust_depth(áØÆ,áØÁ,áÍù=áÓö):
    if (áØÁ is ÂÞÅ):
        return 1
    
    if (áØÁ >= 0):
        return áØÁ
    
    (ÄÊPSH((áØÆ,0)),((áØÆ:=ÄÊPKE(0)[0]),(k:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    while((((ÄÊPSH(k),ÄÊPSH((ÄÊPKE(0) + 1)),(k:=ÄÊPKE(0)),ÄÊDEL(2))[2])if(áÍù(áØÆ))else(None))):
        if ÁØö(áØÆ,ÁÜÙ):
            break 
        
        if (ÁØö(áØÆ,ÁÜÙ) or (not ãÊú(áØÆ) )):
            break 
        
        (ÄÊPSH(áØÆ),ÄÊPSH(ÄÊPKE(0)[0]),(áØÆ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
    return ÂóÍ(((áØÁ + k) - 1),0)

def flatten(áØÆ,áØÁ=ÂÞÅ,áÖÞ=None,áÍù=áÓö):
    (áØÁ:=adjust_depth(áØÆ,áØÁ))
    if (áÖÞ is None):
        (áÖÞ:=ÂÚü())
    
    if (((áØÁ <= 0) or (not áÍù(áØÆ) )) or ÁØñ(ÁÜÙ,áØÆ)):
        return ÂåÔ(((((áÖÞ).extend)if(áÍù(áØÆ))else((áÖÞ).append)))(áØÆ),áÖÞ)
    
    for x in(áØÆ):
        flatten(x,(áØÁ - 1),áÖÞ,áÍù=áÍù)
    
    return áÖÞ

def chain_structure(áØÆ,áØÁ=ÂÞÅ,áÍù=áÓö):
    (áØÁ:=adjust_depth(áØÆ,áØÁ))
    if (((áØÁ <= 0) or (not áÍù(áØÆ) )) or ÁØö(áØÆ,ÁÜÙ)):
        return ((MOD(Âêà,áØÁ=ãÊú(áØÆ))(None))if(áÍù(áØÆ))else(None))
    
    return ÁØò((lambda ÂîÓ:chain_structure(ÂîÓ,(áØÁ - 1),áÍù=áÍù)))(áØÆ)

def deflatten(áØÆ,áÖÛ,áÍù=áÓö):
    if (áÖÛ is None):
        return (((áØÆ).pop(0))if(áØÆ)else(ÄÔýò))
    
    return ÁØò((lambda ÂîÓ:deflatten(áØÆ,ÂîÓ,áÍù=áÍù)))(áÖÛ)

def flatten_under(áØÆ,Æå,áØÁ=ÂÞÅ,ÁÜñ=ÂÞÅ,áÍù=áÓö):
    (áØÁ:=adjust_depth(áØÆ,áØÁ))
    if (ÁÜñ is ÂÞÅ):
        (ÁÜñ:=flatten(áØÆ,áØÁ,áÍù=áÍù))
    
    return deflatten(Æå(ÁÜñ),chain_structure(áØÆ,áØÁ,áÍù=áÍù))

def ÄÔÙù(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ,ÁÜñ=ÂÞÅ):
    if (((((áØÆ is not ÄÊPSH(ÂÞÅ)) and (ÄÊPOP(0) is not ÄÊPSH(áØÇ))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)) and (((ÁØö(áØÆ,ÄÊPSH(áÍÞ)) and ÁØñ(ÄÊPOP(0),ÄÊPSH(áØÇ))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False))):
        ((ÄÊPOP(0))if(ÄÊPSH((ÁÜñ is ÂÞÅ)))else(ÂùÆ(ÄÊPOP(0),("󰤱"))))
        return (ÄÝöì(("%s%s")%(ÄÝöì(ÂüÌ(áØÆ)),ÄÝöì(ÂüÌ(áØÇ)),)) * (ÂÞÅCAT(ÃÆí(ÄÊCUR((2,),{},ÂØú,ÃÆí(áØÆ),ÂýÃ)),áØÇ) or 1))
    
    if (áØÇ is not ÂÞÅ):
        (áØÆ:=[áØÆ,áØÇ])
    
    if (ÁÜñ is not ÂÞÅ):
        if áÍù(ÁÜñ):
            return flatten_under(áØÆ,ÄÕÍÔ,áØÁ,[*ÁÜñ])
        
        return flatten_under(áØÆ,ÁÜñ,áØÁ)
    
    return flatten(áØÆ,áØÁ,áÍù=áÓö)

(ÄÝõÞ:=(lambda áØÆ,áØÁ=ÂÕË:((ÂÚü())if(ÄÝøÇ(áØÆ,áÓö))else(ÁØò((lambda ÂîÓ:((ãÊú(ÂîÓ))if(ÁØö(ÂîÓ,áÓö))else(ÄÔýò))))(ÂÕÅ(MOD(ÂØÎ,áØÁ=(- áØÁ ))(MOD((lambda ÂîÓ:((ÂîÓ[0])if(ãÊú(ÂîÓ))else(0)))),MOD((lambda ÂîÓ:(ÄÝøÇ(ÂîÓ,áÓö) or ÁØö(ÂîÓ,ÁÜÙ))))),áØÆ))))))
(ÄÝõß:=(lambda áØÆ,áØÁ=ÂÕË:ãÊú(MOD(ÄÝõÞ,áØÁ=áØÁ)(áØÆ))))
(ÐÈÔ:=(lambda áØÆ,áØÇ,áØÁ=ÂÞÅ:MOD(ÆÑ,áØÁ=áØÆ)(ÂÀÇ(áØÇ),(lambda x,y:MOD(ÁâÁ,áØÁ=(y - 1))(x)))))
(ÄÔÒØ:=(lambda áØÆ,áØÁ=ÂÕË:MOD(ÄÔÙù,áØÁ=(MOD(ÄÝõß,áØÁ=áØÁ)(áØÆ) - 1))(áØÆ)))
@OPWRAP_(*(("⪡⪢")))
def _(áÑã,áØÆ=ÂÞÅ,áØÇ=1,áØÁ=ÂÞÅ):
    if ÁØö(áØÆ,ÂÑÅ):
        return ((áØÆ>>áØÇ)if((áÑã == ("⪢")))else(áØÆ<<áØÇ))
    
    if (((ÁØö(áØÆ,ÄÊPSH(((ÁÜÙ | áÍá) | áÍé))) and ÁØñ(ÄÊPOP(0),ÄÊPSH(áØÇ))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)):
        ((ÄÊPOP(0))if(ÄÊPSH((áØÁ is ÂÞÅ)))else(ÂùÆ(ÄÊPOP(0),("󰤱 idk what this should do"))))
        return (((áØÆ + áØÇ))if((áÑã == ("⪢")))else((áØÇ + áØÆ)))
    
    ÂùÆ(ÁØö(áØÇ,ÂÑÅ))
    if (áÑã == ("⪡")):
        (ÄÊPSH(áØÇ),ÄÊPSH(ÄÝöâ(ÄÊPKE(0))),(áØÇ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
    if (áØÁ is ÂÞÅ):
        return (áØÆ and (áØÆ[slice((i:=((- áØÇ ) % ãÊú(áØÆ))),None)] + áØÆ[slice(None,i)]))
    
    return ÐÈÔ(MOD(ÄÔÒØ,áØÁ=áØÁ)(áØÆ),Âúú(MOD(ÄÝõÞ,áØÁ=áØÁ)(áØÆ),áØÇ))


#ℵ.☾ (2836 ⟶ 4211)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ℵ.☾')).parent
class aleph_wrapper:
    (__slots__:=(("x"),))
    (__init__:=(lambda áÑÞ,y:Âåß(None,(ÄÊPSH(áÑÞ),ÄÊPSH(("x")),ÄÊPSH(y),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3])))
    (__repr__:=(lambda áÑÞ:(áÑÞ).x))
    (__call__:=(lambda áÑÞ,*áÑË,**áÑÕ:(áÑÞ).x(*áÑË,**áÑÕ)))

class ÂÑÖ(áÍÙ):
    (áÌüþáÍã:=("ℵ"))
    def __getitem__(áÑÞ,x):
        if (x in áÑÞ):
            return (áÍÙ).__getitem__(áÑÞ,x)
        
        if (áÑÞ).hasdef():
            return (áÑÞ).getdef(x)
        
        ÐâÄ(KeyError(("%s ∉ %s, and I have no default value!")%(x,áÑÞ,)))
    
    def __contains__(áÑÞ,x):
        return (super()).__contains__(x)
    
    def __init__(áÑÞ,*áÑË,áØÁ=ÂÞÅ,**áÑÕ):
        (super()).__init__(*áÑË,**áÑÕ)
        if (áØÁ is not ÂÞÅ):
            (áÑÞ).setdef(áØÁ)
        
    
    (__repr__:=(lambda áÑÞ:("%s%s(%s)")%(((áÑÞ).__class__).áÌüþáÍã,((("[%s]")%((h[0] or ("ᐦ")),))if((0 in (h:=(áÑÞ).__dict__)))else(ÁØã)),Âøî(ËãÂ(ÐÌü((áÑÞ).items),(lambda x,y:("%s=%s")%(x,y,))),(", ")),)))
    (__json__:=(lambda áÑÞ,cb,*áÏÞ,**áÏè:MOD(ËãÂ,áØÁ=ì)(áÍÙ(áÑÞ),(lambda x,y:cb(y,*áÏÞ,**áÏè)))))
    (__iter__:=(lambda áÑÞ:iter((áÑÞ).items())))
    (__call__:=(lambda áÑÞ,*áÑË,**áÑÕ:ÂåÔ((áÍÙ).update(áÑÞ,*áÑË,**áÑÕ),áÑÞ)))
    (__bool__:=(lambda áÑÞ:(ãÊú(áÑÞ) > 0)))
    (__or__:=(lambda áÑÞ,x:(áÑÞ).copy()(x)))
    (__ror__:=(lambda áÑÞ,x:(ÂÞÅCAT(x,ÂÑÖ()) | áÑÞ)))
    def __and__(áÑÞ,y):
        (r:=ÂÑÖ())
        if (áÑÞ).hasdef():
            (r).setdef((áÑÞ).getdef())
        
        if ÁØö(y,(((áÍè | áÍá) | áÍé) | ÁÜÙ)):
            for k in({*y}):
                if not((k in áÑÞ)):continue
                (ÄÊPSH(r),ÄÊPSH(k),ÄÊPSH(áÑÞ[k]),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
            
        else :
            for (k,v) in((y).items()):
                if not((k in áÑÞ)):continue
                (ÄÊPSH(r),ÄÊPSH(k),ÄÊPSH(v),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
            
        
        return r
    
    def __rand__(áÑÞ,y):
        if ÁØö(y,(((áÍè | áÍá) | áÍé) | ÁÜÙ)):
            return (áÑÞ & y)
        
        if ÁØö(y,áÍÙ):
            return (ÂÞÅCAT(y,ÂÑÖ()) & áÑÞ)
        
        return NotImplemented
    
    def __sub__(áÑÞ,y):
        (r:=ÂÑÖ())
        if (áÑÞ).hasdef():
            (r).setdef((áÑÞ).getdef())
        
        ÂùÆ(áÓö(y))
        for (k,v) in(áÑÞ):
            if not((k not in y)):continue
            (ÄÊPSH(r),ÄÊPSH(k),ÄÊPSH(v),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        
        return r
    
    def __rsub__(áÑÞ,y):
        if ÁØö(y,áÍÙ):
            return (ÂÞÅCAT(y,ÂÑÖ()) - áÑÞ)
        
        return NotImplemented
    
    (__setattr__:=(áÍÙ).__setitem__)
    (__getattr__:=__getitem__)
    def __getstate__(áÑÞ):
        if (áÑÞ).hasdef():
            return (áÍÙ(áÑÞ),(áÑÞ).getdef())
        else :
            return (áÍÙ(áÑÞ),)
        
    
    def __setstate__(áÑÞ,s):
        (áÑÞ).__init__(s[0])
        if (ãÊú(s) > 1):
            (áÑÞ).setdef(s[1])
        
    
    def __pow__(áÑÞ,x):
        if (x is î):
            return [*(ÐÌü((áÑÞ).keys))]
        
        if (x is ì):
            return [*(ÐÌü((áÑÞ).values))]
        
        if (x is ë):
            return [*(ÐÌü((áÑÞ).items))]
        
        if (x is ÂÕì):
            return MOD(Áÿú,áØÁ=ë)(áÑÞ,ÂÀÇ)
        
        if (x is Áâ):
            return MOD(Áëý,áØÁ=ÄÝøÇ((v:=ÐÌü((áÑÞ).getdef)),(C:=aleph_wrapper)))(ÐÌü((áÑÞ).copy),(lambda x:(x).setdef(C(v))))
        
        ÂùÆ(False)
    
    (hasdef:=(lambda áÑÞ:(0 in (áÑÞ).__dict__)))
    (setdef:=(lambda áÑÞ,x:ÂåÔ((ÄÊPSH((áÑÞ).__dict__),ÄÊPSH(0),ÄÊPSH(x),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3],áÑÞ)))
    def getdef(áÑÞ,k=ÂÞÅ):
        (d:=(áÑÞ).__dict__[0])
        if ÁØö(d,aleph_wrapper):
            (ÄÊPSH(d),ÄÊPSH(ÐÌü(ÄÊPKE(0))),(d:=ÄÊPKE(0)),ÄÊDEL(2))[2]
            (ÄÊPSH(áÑÞ),ÄÊPSH(k),ÄÊPSH(d),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        
        return d
    
    def copy(áÑÞ):
        (r:=type(áÑÞ)((super()).copy()))
        if (áÑÞ).hasdef():
            (r).setdef((áÑÞ).getdef())
        
        return r
    

class ÂÑØ(ÂÑÖ):
    (áÌüþáÍã:=("ℶ"))
    (__iter__:=(lambda áÑÞ:iter((áÑÞ).values())))

class áÍáþáÍá(áÍá):
    None


#crypto.☾ (2607 ⟶ 5108)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/crypto.☾')).parent
class Cmap(ÂÑÖ):
    def __init__(áÑÞ,d,*áÑË,**áÑÕ):
        (super()).__init__(*áÑË,**áÑÕ)
        (ÄÊPSH((áÑÞ).__dict__),ÄÊPSH(1),ÄÊPSH(d),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
    
    (__call__:=(lambda áÑÞ,*áÑË,**áÑÕ:áÑÞ[(áÑÞ).__dict__[1]](*áÑË,**áÑÕ)))
    (__pow__:=(lambda x,y:x[y]))

def SR_bytes(x=None,y=None):
    if ((((x is ÄÊPSH(None)) and (ÄÊPOP(0) is ÄÊPSH(y))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)):
        return PL_URANDOM(1)[0]
    
    if (y is None):
        return PL_URANDOM(x)
    
    if (x is None):
        (x:=0)
    
    return SR_bytes(SR_int(x,y))

def SR_int(x=None,y=None):
    if (x is None):
        ÂùÆ((y is None))
        return ÐÌü(SR_bytes)
    
    if (y is None):
        (ÄÊPSH((0,x)),((x:=ÄÊPKE(0)[0]),(y:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    
    if (x > y):
        (ÄÊPSH((y,x)),((x:=ÄÊPKE(0)[0]),(y:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    
    (r:=(y - x))
    (l:=ÐÌü((r).bit_length))
    while(((s:=(((áÍÞ).from_bytes(SR_bytes(Âüï((l / 8)))) & (((2 ** (l))) - 1)))) > r)):
        None
    
    return (x + s)

def SR_float(x=None,y=None):
    if (x is None):
        ÂùÆ((y is None))
        (ÄÊPSH((0,1)),((x:=ÄÊPKE(0)[0]),(y:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    else :
        if (y is None):
            (ÄÊPSH((0,x)),((x:=ÄÊPKE(0)[0]),(y:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
        
        if (x > y):
            (ÄÊPSH((y,x)),((x:=ÄÊPKE(0)[0]),(y:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
        
    
    return (x + (SR_int((((2 ** (64))) - 1)) * ((y - x) / (((2 ** (64))) - 1))))

def SR_choice(x):
    return x[SR_int((ãÊú(x) - 1))]

def SR_shuffle(x,n=None):
    if (n is None):
        (n:=ãÊú(x))
    elif ((ÄÊPSH(n),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),áÍÞ)),(n:=ÄÊPKE(0)),ÄÊDEL(2))[2] > ãÊú(x)):
        ((ÄÊPOP(0))if(ÄÊPSH(False))else(ÂùÆ(ÄÊPOP(0),("Cannot shuffle (%s > %s)")%(n,ãÊú(x),))))
    
    (ÄÊPSH(([*x],ÂÚü())),((X:=ÄÊPKE(0)[0]),(Y:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    for _ in(ÂÿÇ(n)):
        (Y).append((X).pop(SR_int((ãÊú(X) - 1))))
    
    return Y

def SR_str(n=24,chars=None):
    return Âøî(ÁØò((lambda ÂîÓ:SR_choice(((abcABC123)if((chars is None))else(chars)))))(ÂÿÇ(n)),ÁØã)

@OPWRAP_(*(("󱅏")))
def _(áÑã,áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
    def Æå():
        if (áÑã == ("")):
            ÂùÆ((áÓö(áØÆ) or áÓö(áØÇ)))
            (ÄÊPSH((((áØÆ,áØÇ))if(áÓö(áØÆ))else((áØÇ,áØÆ)))),((áÏË:=ÄÊPKE(0)[0]),(n:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
            if (n is ÂÞÅ):
                return SR_shuffle(áÏË)
            
            return ÁØò((lambda ÂîÓ:SR_choice(áÏË)))(ÂÿÇ(n))
        
        if ((((áØÆ is ÄÊPSH(ÂÞÅ)) and (ÄÊPOP(0) is ÄÊPSH(áØÇ))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)):
            return SR_float(*(((ÂÕÀ(1))if((áÑã == ("")))else(ÂÿÇ(1)))))
        
        (Æå:=((SR_float)if((áÑã == ("")))else(SR_int)))
        if ((((áØÆ is not ÄÊPSH(ÂÞÅ)) and (ÄÊPOP(0) is not ÄÊPSH(áØÇ))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)):
            return Æå(áØÆ,áØÇ)
        
        if áÓö((áÑÿ:=((áØÇ)if((áØÆ is ÂÞÅ))else(áØÆ)))):
            return Æå(*áÑÿ)
        else :
            return Æå(0,áÑÿ)
        
        ÂùÆ(False)
    
    return ((ÐÌü(Æå))if((áØÁ is ÂÞÅ))else(ËãÂ(MOD(ÂÚü,áØÁ=áØÁ)(),Æå)))

(ÄïÉð:=(sha:=Cmap(ÁÁ,{ÁÁ:(lambda *áÑË,**áÑÕ:ÂÞÅCAT((_sha256(áÍÇ((ÁÜÙ(áÑË) + ÁÜÙ(áÑÕ))))).digest(),ÄïÊÀ)),áÍî:(lambda x:(_sha256(MOD(Áëý,áØÁ=ÄÊCUR((1,),{},ÄÝøÇ,ÂýÃ,áÍî))(x,áÍÇ))).digest())})))
(ÄÊPSH((MOD((lambda ÂîÓ:ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ,áÍÇ),zibe),b85e),áÍÇ))),MOD((lambda ÂîÓ:ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ,áÍÇ),b85d),zibd),áÍÇ))))),((stre:=ÄÊPKE(0)[0]),(strd:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄïÉö:=(ÄïÉù:=(áÐÞ:=Cmap(ÁÁ,{ÁÁ:ÄÊCUR((1,),{"ensure_ascii":False,"indent":None,"separators":(",:")},jdumps__,ÂýÃ),ÿ:jloads__}))))
(ÄïÊÀ:=Cmap(ÁÁ,{ÁÁ:(lambda x:(áÍÇ(urlsafe_b64encode(MOD(Áëý,áØÁ=ÄÊCUR((1,),{},ÄÝøÇ,ÂýÃ,áÍî))(x,áÍÇ)))).rstrip(("="))),ÿ:(lambda x:urlsafe_b64decode(áÍÇ((MOD(Áëý,áØÁ=ÄÊCUR((1,),{},ÁØö,ÂýÃ,áÍî))(x,áÍÇ) + (("=") * (4 - (ãÊú(x) % 4)))))))}))
try :
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad,unpad
except áÍÚ as Ðáü:
    ((ÄÊPOP(0))if(ÄÊPSH(False))else(MOD(ÂùÆ,áØÁ=ÂÄ)(ÄÊPOP(0),("Failed to import AES libraries! Do you have pycryptodome installed?"))))

def AES_ENC_SIV(áÖú,k):
    return ÂøÑ(((AES).new(k,(AES).MODE_SIV)).encrypt_and_digest(áÖú))

def AES_DEC_SIV(m,k):
    return ((AES).new(k,(AES).MODE_SIV)).decrypt_and_verify(*(áÇù(m,((- 16 )))))

def ENC_BYTES(áÖú,k,áÕÎ=True):
    if áÕÎ:
        (áÖú:=(SR_bytes(8) + áÖú))
    
    (n:=((16 - ((ãÊú(áÖú) + 1) % 16)) % 16))
    return AES_ENC_SIV(ÂÞÅCAT([((n + 1) + ((8)if(áÕÎ)else(0))),*(ÂÞÅCAT([0],n)),*áÖú],áÍî),(lambda ÂîÓ:(ÂîÓ + ÂÞÅCAT(ÂîÓ,ÄïÉð[áÍî])))(ÂÞÅCAT(k,ÄïÉð[áÍî])))

def DEC_BYTES(m,k):
    return (lambda ÂîÓ:ÂîÓ[slice(ÂîÓ[0],None)])(AES_DEC_SIV(m,(lambda ÂîÓ:(ÂîÓ + ÂÞÅCAT(ÂîÓ,ÄïÉð[áÍî])))(ÂÞÅCAT(k,ÄïÉð[áÍî]))))

class ÄïÉï:
    (__getitem__:=(lambda x,y:Cmap(ÁÁ,{ÁÁ:(lambda x:ENC_BYTES(ÂÞÅCAT(ÂÞÅCAT(x,ÄïÉù[ÁÁ]),áÍÇ),y,True)),Âúú:(lambda x:ENC_BYTES(ÂÞÅCAT(ÂÞÅCAT(x,ÄïÉù[ÁÁ]),áÍÇ),y,False)),ÿ:(lambda x:ÂÞÅCAT(ÂÞÅCAT(DEC_BYTES(x,y),áÍÇ),ÄïÉù[ÿ]))})))
    (__getattr__:=__getitem__)

(ÄïÉï:=ÐÌü(ÄïÉï))

#ugex.☾ (2460 ⟶ 4855)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ugex.☾')).parent
class winder:
    def __init__(áÑÞ,áÖï,áÖõ=((- 1 ))):
        (ÄÊPSH(áÑÞ),ÄÊPSH(("áÖï")),ÄÊPSH(áÑÞ),ÄÊPSH(("áÖõ")),ÄÊPSH(áÑÞ),ÄÊPSH(("áÖà")),ÄÊPSH((áÖï,áÖõ,ÂÚü())),(setattr(ÄÊPKE(6),ÄÊPKE(5),ÄÊPKE(0)[0]),setattr(ÄÊPKE(4),ÄÊPKE(3),ÄÊPKE(0)[1]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)[2])),ÄÊDEL(7))[7]
    
    (__bool__:=(lambda áÑÞ:(((áÑÞ).áÖõ + 1) < ãÊú((áÑÞ).áÖï))))
    (__repr__:=(lambda áÑÞ:("[%s│%s]⟨%s⟩")%(ÂîË((áÑÞ).áÖï[slice(None,((áÑÞ).áÖõ + 1))],(" ")),ÂîÊ((áÑÞ).áÖï[slice(((áÑÞ).áÖõ + 1),None)],(" ")),Âøî((áÑÞ).áÖà,(" ")),)))
    (peek:=(lambda áÑÞ:(áÑÞ).áÖï[((áÑÞ).áÖõ + 1)]))
    (next:=(lambda áÑÞ:(áÑÞ).áÖï[(ÄÊPSH(áÑÞ),ÄÊPSH(("áÖõ")),ÄÊPSH(getattr(ÄÊPKE(1),ÄÊPKE(0))),ÄÊPSH((ÄÊPKE(0) + 1)),setattr(ÄÊPKE(3),ÄÊPKE(2),ÄÊPKE(0)),ÄÊDEL(4))[4]]))
    (note:=(lambda áÑÞ:ÂåÔ(((áÑÞ).áÖà).append((áÑÞ).áÖõ),áÑÞ)))
    (eton:=(lambda áÑÞ:ÂåÔ(ÐÌü(((áÑÞ).áÖà).pop),áÑÞ)))
    (wind:=(lambda áÑÞ:ÂåÔ((ÄÊPSH(áÑÞ),ÄÊPSH(("áÖõ")),ÄÊPSH(ÐÌü(((áÑÞ).áÖà).pop)),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3],áÑÞ)))

(ARROW_TARG:=ÂÚü())
def ÄÝöç(áØÆ,áØÁ=ÂÞÅ):
    (áÖí:=ARROW_TARG[((- 1 ))])
    if (áØÁ is ÂÞÅ):
        (áÖí).append(áØÆ)
        return áØÆ
    
    if (áØÁ == ÂÕË):
        (áÖí).extend(áØÆ)
        return áØÆ
    
    (áÖí).extend((h:=MOD(Âêà,áØÁ=áØÁ)(áØÆ)))
    return h

def ÄÝöè(áØÁ=ÂÞÅ):
    (áÖí:=ARROW_TARG[((- 1 ))])
    if (áØÁ is ÂÞÅ):
        return (áÖí).pop(((- 1 )))
    
    if (áØÁ == ÂÕË):
        (r:=áÖí[slice(None,None)])
        del áÖí[slice(None,None)]
        return r
    
    if ((ÄÊPSH(áØÁ),ÄÊPSH((ÄÊPKE(0) * ((- 1 )))),(áØÁ:=ÄÊPKE(0)),ÄÊDEL(2))[2] == 0):
        return ÂÚü()
    
    (r:=áÖí[slice(áØÁ,None)])
    del áÖí[slice(áØÁ,None)]
    return r

def ÂÛÒ(áØÁ=ÂÞÅ):
    (áÖí:=ARROW_TARG[((- 1 ))])
    if (áØÁ is ÂÞÅ):
        return áÖí[((- 1 ))]
    
    if (áØÁ == ÂÕË):
        return áÖí[slice(None,None)]
    
    if ((ÄÊPSH(áØÁ),ÄÊPSH((ÄÊPKE(0) * ((- 1 )))),(áØÁ:=ÄÊPKE(0)),ÄÊDEL(2))[2] == 0):
        return ÂÚü()
    
    return áÖí[slice(áØÁ,None)]

(UGX_CREATE:=(lambda x,d=False:MOD((lambda ÂîÓ:((d)if(((y:=UGX_RUN(winder([*ÂîÓ]),x)) is ÂÞÅ))else(y[0]))))))
def UGX_SCAN(áÖÿ,Æå,áÓà):
    if (not áÖÿ ):
        return ((ÂÚü())if(((("*") == áÓà) or (áÓà == ("?"))))else(ÂÞÅ))
    
    (áÍí:=Æå((p:=ÐÌü((áÖÿ).peek))))
    if (áÓà == ("¬")):
        return ((ÂÞÅ)if(áÍí)else(ÂÚü()))
    
    if (áÓà == ("⮞")):
        return ((ÂÚü())if(áÍí)else(ÂÞÅ))
    
    if (not áÍí ):
        return ((ÂÞÅ)if((áÓà in ("+")))else(ÂÚü()))
    
    (V:=((ÂÚü())if(((ÐÌü((áÖÿ).next) is ÄÔýò) or (ÄÔýò is áÍí)))else(Âêà(p))))
    if (áÓà in ("?")):
        return V
    
    while(áÖÿ):
        if (not (v:=Æå((p:=ÐÌü((áÖÿ).peek)))) ):
            break 
        
        if ((v is ÄÔýò) or (ÄÔýò is ÐÌü((áÖÿ).next))):
            continue 
        
        (V).append(p)
    
    return V

def UGX_RUN(áÖÿ,áØÃ):
    (ÄÊPSH(áØÃ),((áÓç:=ÄÊPKE(0)[0]),*((áÒø:=ÄÊPKE(0)[slice(1,None,None)]))),ÄÊDEL(1))[1]
    if ÁØö(áÓç,áÓó):
        return UGX_SCAN(áÖÿ,áÓç,áÒø[0])
    elif (áÓç in ("BP")):
        (ÄÊPSH(áÒø),((áÓæ:=ÄÊPKE(0)[0]),(áÓà:=ÄÊPKE(0)[1]),(áÓå:=ÄÊPKE(0)[2]),(áÓÕ:=ÄÊPKE(0)[3])),ÄÊDEL(1))[1]
        (ARROW_TARG).append(áÓæ)
        ÂåÔ(ÐÌü((áÖÿ).note),(V:=(r:=UGX_RUN(áÖÿ,áÓÕ))))
        if (áÓà == ("⮞")):
            ÂåÔ(ÐÌü((áÖÿ).wind),(V:=(((ÂÞÅ)if((r is ÂÞÅ))else(ÂÚü())))))
        elif (áÓà == ("¬")):
            ÂåÔ(ÐÌü((áÖÿ).wind),(V:=(((ÂÚü())if((r is ÂÞÅ))else(ÂÞÅ)))))
        elif (áÓà == ("?")):
            ÂåÔ(ÐÌü((áÖÿ).wind),(V:=(((ÂÚü())if((r is ÂÞÅ))else(ÂÞÅ)))))
        elif (r is ÂÞÅ):
            ÂåÔ(ÐÌü((áÖÿ).wind),(V:=(((ÂÚü())if((áÓà == ("∗")))else(ÂÞÅ)))))
        elif (áÓà not in ("?")):
            while(áÖÿ):
                ÂåÔ(ÐÌü((áÖÿ).note),(r:=UGX_RUN(áÖÿ,áÓÕ)))
                if (r is ÂÞÅ):
                    ÐÌü((áÖÿ).wind)
                    break 
                
                ÂåÔ(ÐÌü((áÖÿ).eton),(V).extend(r))
            
            ÐÌü((áÖÿ).eton)
        
        if (áÓå is ÄÔýò):
            (V:=ÂÚü())
        
        if ((V is not ÂÞÅ) and áÓó(áÓå)):
            (V:=áÓå(V))
        
        (ARROW_TARG).pop(((- 1 )))
        if (V is ÂÞÅ):
            return V
        
        return MOD(Áëý,áØÁ=(áÓç == ("B")))(V,Âêà)
    elif (áÓç in ("∧∨")):
        if (áÓç == ("∧")):
            ÂåÔ(ÐÌü((áÖÿ).note),(V:=ÂÚü()))
            for U in(áÒø):
                if ((r:=UGX_RUN(áÖÿ,U)) is ÂÞÅ):
                    return ÂåÔ(ÐÌü((áÖÿ).wind),ÂÞÅ)
                
                (V).extend(r)
            
            return ÂåÔ(ÐÌü((áÖÿ).eton),V)
        elif (áÓç == ("∨")):
            for U in(áÒø):
                ÐÌü((áÖÿ).note)
                if ((r:=UGX_RUN(áÖÿ,U)) is not ÂÞÅ):
                    return ÂåÔ(ÐÌü((áÖÿ).eton),r)
                
                ÐÌü((áÖÿ).wind)
            
            return ÂÞÅ
        
    


#.☾ (1647 ⟶ 2421)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/\uea7b.☾')).parent
(TMPDIR:=ÂÞÅCAT((env).get(("MOON_TMPDIR"),ð(ÂÞÅCAT(("/dev/shm"),áÌî),("☾_tmp"))),áÌî))
(CACHEDIR:=ÂÞÅCAT((env).get(("MOON_CACHEDIR"),ð(TMPDIR,("cache"))),áÌî))
(mkd:=(lambda f,e=True,p=True:ÂåÔ(((p:=ÂÞÅCAT(f,áÌî))).mkdir(exist_ok=e,parents=p),p)))
(mkf:=(lambda f,e=True:ÂåÔ((ÂåÔ(mkd(((p:=ÂÞÅCAT(f,áÌî))).parent),p)).touch(exist_ok=e),p)))
(tmpf:=(lambda b=ÁØã,f=ÂÞÅ,n=14:mkf(ð((lambda ÂîÓ:MOD(Áëý,áØÁ=b)(ÂîÓ,ÄÊCUR((1,),{},ð,ÂýÃ,b)))(TMPDIR),(((ÂÞÅCAT(n,SR_str))if((f is ÂÞÅ))else(f)))))))
(tmpd:=(lambda b=ÁØã,f=ÂÞÅ,n=14:mkd(ð((lambda ÂîÓ:MOD(Áëý,áØÁ=b)(ÂîÓ,ÄÊCUR((1,),{},ð,ÂýÃ,b)))(TMPDIR),(((ÂÞÅCAT(n,SR_str))if((f is ÂÞÅ))else(f)))))))
class suppar2:
    (__init__:=(lambda áÑÞ,Æå:ÂåÔ((ÄÊPSH(Æå),ÄÊPSH(áÑÞ),ÄÊPSH(("Æå")),setattr(ÄÊPKE(1),ÄÊPKE(0),ÄÊPKE(2)),ÄÊDEL(3))[3],None)))
    (__call__:=(lambda áÑÞ,*áÑË,**áÑÕ:(áÑÞ).Æå(*áÑË,**áÑÕ)))
    (__getitem__:=(__getattr__:=(lambda áÑÞ,x,*áÑË,**áÑÕ:(lambda *áÑË,**áÑÕ:(áÑÞ).Æå(*áÑË,x,**áÑÕ)))))

(ÐâÒ:=(lambda x=ÂÞÅ:((ÐÌü(PL_TEXT_PASTE))if((x is ÂÞÅ))else(ÂåÔ(ÂÞÅCAT(ÂÞÅCAT(x,ÁÜÙ),PL_TEXT_COPY),x)))))
(ÐÈÃ:=suppar2((lambda f,o=ÁØã:(áÌî(f)).open(o))))
(ÐØó:=suppar2((lambda f,o=ÁØã:Âáõ((y:=ÐÈÃ[(("r") + o)](f)),(lambda x:ÐÌü((x).read))))))
(ÐØì:=suppar2((lambda f,áÏû,o=ÁØã:Âáõ((y:=ÐÈÃ[(("w") + o)](f)),(lambda x:ÂåÔ((x).write(áÏû),y))))))
(pwd:=(lambda :áÌî(ÐÌü((os).getcwd))))
class cd:
    (ÄÊPSH(MOD(ÂÚü,áØÁ=2)()),((s:=ÄÊPKE(0)[0]),(c:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    def __init__(áÑÞ,d=None):
        (ÄÊPSH(áÑÞ),ÄÊPSH(("d")),ÄÊPSH(d),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
    
    def __enter__(áÑÞ):
        (x:=(áÑÞ).d)
        ((cd).s).append((ãÊú((cd).c),(x:=ÐÌü(pwd))))
        if (x is not None):
            (os).chdir(áÌî(x))
        
        return ÐÌü(pwd)
    
    def __exit__(áÑÞ,*áÑË):
        (ÄÊPSH(((cd).s).pop(((- 1 )))),((i:=ÄÊPKE(0)[0]),(d:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
        (ÄÊPSH(cd),ÄÊPSH(("c")),ÄÊPSH((cd).c[slice(None,i)]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        (os).chdir(d)
        return ÐÌü(pwd)
    
    def __call__(áÑÞ,d=None):
        if (d is ÁÃ):
            return cd((áÌî(((inspect).stack()[1]).filename)).parent)
        
        if (d is None):
            (os).chdir(((cd).c).pop(((- 1 ))))
            return ÐÌü(pwd)
        
        ((cd).c).append(ÐÌü(pwd))
        (os).chdir(d)
        return ÐÌü(pwd)
    
    def __getitem__(áÑÞ,d):
        return (áÑÞ).__class__(d)
    

(cd:=ÐÌü(cd))

#🌈.☾ (1631 ⟶ 3281)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/🌈.☾')).parent
def h2r(c=ÁØã):
    if ÁØö(c,áÍÞ):
        (ÄÊPSH(c),ÄÊPSH(MOD(ÄÝöì,áØÁ=16)(ÄÊPKE(0))),(c:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
    (c:=((c).strip()).lstrip(("#")))
    if (c).startswith(("0x")):
        (ÄÊPSH(c),ÄÊPSH(ÄÊPKE(0)[slice(2,None)]),(c:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
    (ÄÊPSH((ÄÊCUR((1,),{},áÍÞ,ÂýÃ,16),ãÊú(c))),((ÂÐí:=ÄÊPKE(0)[0]),(n:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    if (n == 0):
        return (0,0,0,255)
    
    if (n == 1):
        return (ÂÐí(ÂÞÅCAT(c[0],2)),ÂÐí(ÂÞÅCAT(c[0],2)),ÂÐí(ÂÞÅCAT(c[0],2)),255)
    
    if (n == 2):
        return (ÂÐí(ÂÞÅCAT(c[0],2)),ÂÐí(ÂÞÅCAT(c[0],2)),ÂÐí(ÂÞÅCAT(c[0],2)),ÂÐí(ÂÞÅCAT(c[1],2)))
    
    if (n == 3):
        return (ÂÐí(ÂÞÅCAT(c[0],2)),ÂÐí(ÂÞÅCAT(c[1],2)),ÂÐí(ÂÞÅCAT(c[2],2)),255)
    
    if (n == 4):
        return (ÂÐí(ÂÞÅCAT(c[0],2)),ÂÐí(ÂÞÅCAT(c[1],2)),ÂÐí(ÂÞÅCAT(c[2],2)),ÂÐí(ÂÞÅCAT(c[3],2)))
    
    if (n == 5):
        return (ÂÐí(ÂÞÅCAT(c[0],2)),ÂÐí(ÂÞÅCAT(c[1],2)),ÂÐí(ÂÞÅCAT(c[2],2)),ÂÐí(c[slice(3,5)]))
    
    if (n == 6):
        return (ÂÐí(c[slice(0,2)]),ÂÐí(c[slice(2,4)]),ÂÐí(c[slice(4,6)]),255)
    
    if (n == 7):
        return (ÂÐí(c[slice(0,2)]),ÂÐí(c[slice(2,4)]),ÂÐí(c[slice(4,6)]),ÂÐí(ÂÞÅCAT(c[6],2)))
    
    if (n == 8):
        return (ÂÐí(c[slice(0,2)]),ÂÐí(c[slice(2,4)]),ÂÐí(c[slice(4,6)]),ÂÐí(c[slice(6,8)]))
    

(r2hl:=(lambda x:("#%s")%(Âøî(Áÿú(x,MOD(ÄÝöì,áØÁ=(16 + ÂÞÅCAT(2,Ãù))))),)))
(h2hl:=Âåæ(r2hl,h2r))
def rgb2hsv(r,g,b):
    (ÄÊPSH(Âîí([r,g,b])),((m:=ÄÊPKE(0)[0]),(v:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    (s:=(((((ÏÁ:=(v - m))) / v))if(v)else(0)))
    (h:=((((((((((g - b) / ÏÁ) % 6))if((v == r))else((((((b - r) / ÏÁ) + 2))if((v == g))else((((r - g) / ÏÁ) + 4)))))) * 60) % 360))if(v)else(0)))
    return ((h / 360),s,v)

def hsv2rgb(h,s,v):
    (ÄÊPSH(h),ÄÊPSH(((ÄÊPKE(0) * 360) % 360)),(h:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    (ÄÊPSH((s,v)),ÄÊPSH(Áÿú(ÄÊPKE(0),ÄÝöÓ(0,1))),((s:=ÄÊPKE(0)[0]),(v:=ÄÊPKE(0)[1])),ÄÊDEL(2))[2]
    (x:=(((c:=(v * s))) * ((1 - ÂüÌ((((h / 60) % 2) - 1))))))
    return ÁØòþÁÙÄ((lambda ÂîÓ,ÂîÒ:(ÂîÓ + ÂîÒ)))(((([c,x,0])if((h <= 60))else((([x,c,0])if((h <= 120))else((([0,c,x])if((h <= 180))else((([0,x,c])if((h <= 240))else((([x,0,c])if((h <= 300))else([c,0,x]))))))))))),(v - c))

(TERM_RESET_B:=("\x1B[49m"))
(TERM_RESET_F:=("\x1B[39m"))
(TERM_RESET:=("\x1B[0m"))
(styd:=ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT((ð(moon_dir,("Builtins/Data/style.json"))),ÐØó),áÐÞ[ÿ]),ÂÑÖ()))
def termclr(t,fg=None,bg=None,rst=True,rl=False):
    (rlw:=(lambda x:((("\x01%s\x02")%(x,))if(rl)else(x))))
    (mkc:=(lambda x,y,z,w,v:ÂÞÅCAT(("\x1B[%s;2;%s;%s;%sm")%(x,y,z,w,),rlw)))
    (R:=Âøî([(mkc(n,*(h2r(c))))for (c,n) in(ÄÕåØ([fg,bg],[38,48]))if((c is not None))]))
    return ("%s%s%s")%(R,t,((rlw(((ÁØã)if(((fg is None) and (bg is None)))else(((TERM_RESET_B)if((fg is None))else(((TERM_RESET_F)if((bg is None))else(TERM_RESET))))))))if(rst)else(ÁØã)),)

@cache_
def sty(s,bg=0,def_=("bec")):
    for (k,v) in(styd):
        if not(((s in k) and ÂÔö(v,("fg")))):continue
        return termclr(s,v[("fg")],bg)
    
    return termclr(s,def_,bg)

(__highlighter__:=(lambda l,b=None,clr=("bec"):Âøî(Áÿú(ÂÞÅCAT(ÂÞÅCAT(l,ÁÜÙ),VEP),ÄÊCUR((1,),{},sty,ÂýÃ,b,clr)))))
def highlight_tester():
    while((l:=ÐÌü((ÂÐðþáÐâ).readline))):
        Âçß(ÂÞÅCAT(ÂÞÅCAT(("\x0A"),(l).rstrip),__highlighter__))
    


#!.☾ (669 ⟶ 1522)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/!.☾')).parent
def ÏÀ(z):
    if (ÄÝõè(z) < ÃÆ):
        return (ÂÞÅCAT(Ïò,Ãù) / ((((ÂÐæ ** ÂÞÅCAT(ÂÞÅCAT(Ãù,Ïî),z)) - (ÂÐæ ** ÂÞÅCAT(ÂÞÅCAT(ÄÝîâ,Ïî),z)))) * ÏÀ((1 - z))))
    
    (p:=[1.0000000001900148240,76.180091729471463483,(- 86.505320329416767652 ),24.014098240830910490,(- 1.2317395724501553875 ),0.0012086509738661785061,(- 5.3952393849531283785e-6 )])
    return ((((MOD(ÂøÑ,áØÁ=p[0])(ÁÙÇ((lambda ÂîÒ:(p[ÂîÒ] / (z + ÂîÒ))))(ÄÝöÊ(1,6))) * (ÂÐæ ** ((- 5.5 ) - z))) * (((5.5 + z)) ** (ÃÆ + z))) * ÂÕÇ(Ïò)) / z)

def â(áØÆ,áØÁ=ÂÞÅ):
    if (áØÁ is ÂÞÅ):
        if ÁØö(áØÆ,ÂÑÅ):
            return ((nan)if((áØÆ < 0))else(MOD(ÂøÐ,áØÁ=1)(ÄÝöÉ(0,áÍÞ(áØÆ)))))
        
        return (áØÆ * ÏÀ(áØÆ))
    
    if ÁØö(áØÁ,áÍÞ):
        return MOD(ÂøÐ,áØÁ=1)(ÁØò((lambda ÂîÓ:(ÂîÓ + áØÆ)))(ÂÿÇ(áØÁ)))
    
    if ÁØö(áØÁ,ÂÐá):
        if (áØÆ == 0):
            return 1
        
        if (((d:=ÂÞÅCAT(ÄÝõç(Âüð),áØÁ)) >= 0) and (áØÆ > 0)):
            return ÂÕË
        
        if ((d <= 0) and (áØÆ < 0)):
            return nan
        
        (ÄÊPSH((1,áØÆ)),((t:=ÄÊPKE(0)[0]),(c:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
        while((ÃÆí(c) == ÃÆí(áØÆ))):
            (ÄÊPSH(t),ÄÊPSH((ÄÊPKE(0) * c)),(t:=ÄÊPKE(0)),ÄÊDEL(2))[2]
            (ÄÊPSH(c),ÄÊPSH((ÄÊPKE(0) + d)),(c:=ÄÊPKE(0)),ÄÊDEL(2))[2]
        
        return t
    
    if ÁØö(áØÁ,áÓö):
        return MOD(ÂøÐ,áØÁ=1)(ÁØò((lambda ÂîÓ:((ÂîÓ * áØÁ[((- 1 ))]) + áØÆ)))(ÂÿÇ(áØÁ[0])))
    
    ((ÄÊPOP(0))if(ÄÊPSH(False))else(ÂùÆ(ÄÊPOP(0),("what do you meeeeaaaaaannnnnn!?!?!?"))))


#?.☾ (424 ⟶ 1174)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/?.☾')).parent
class qproxy:
    (__slots__:=(("v"),("a")))
    def __init__(áÑÞ,v,a=None):
        (ÄÊPSH(áÑÞ),ÄÊPSH(("v")),ÄÊPSH(áÑÞ),ÄÊPSH(("a")),ÄÊPSH((v,a)),(setattr(ÄÊPKE(4),ÄÊPKE(3),ÄÊPKE(0)[0]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)[1])),ÄÊDEL(5))[5]
    
    def __call__(áÑÞ,*áÑË,**áÑÕ):
        return (((áÑÞ).v(*áÑË,**áÑÕ))if(áÓó((áÑÞ).v))else((áÑÞ).a))
    
    def __getattr__(áÑÞ,x):
        return ((getattr((áÑÞ).v,x))if(getattr((áÑÞ).v,("__contains__"))(x))else((áÑÞ).a))
    
    def __getitem__(áÑÞ,x):
        (v:=(áÑÞ).v)
        if ÁØö(v,áÍÙ):
            if (x in v):
                return v[x]
            
        elif ÁØö(v,((áÍá | áÍé) | ÁÜÙ)):
            try :
                return v[x]
            except áÍÚ:pass
        elif hasattr(v,("__getitem__")):
            try :
                return v[x]
            except áÍÚ:pass
        
        return (áÑÞ).a
    

def ÁÂ(áØÆ,áØÁ=ÂÞÅ):
    return qproxy(áØÆ,((áØÁ)if((áØÁ is not ÂÞÅ))else(None)))

def ÂÛí(áØÆ,áØÁ=ÂÞÅ):
    return ((((áØÁ)if((áØÁ is not ÂÞÅ))else(False)))if((áØÆ is None))else(True))

def ÄÝõÒ(áØÆ,áØÁ=ÂÞÅ):
    return ((True)if((áØÆ is None))else(((áØÁ)if((áØÁ is not ÂÞÅ))else(False))))


#extra_globals.☾ (2780 ⟶ 4025)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/extra_globals.☾')).parent
(FRAC_CONV:={**(dict(ÄÕåØ(ÂÛê(("12 13 14 15 16 17 18 19 110 23 25 27 29 34 35 37 38 310 45 47 49 56 57 58 59 67 78 79 710 89 910 03 1100")),("½⅓¼⅕⅙⅐⅛⅑⅒⅔⅖󷶲󷶷¾⅗󷶳⅜󷷆⅘󷶴󷷂⅚󷶵⅝󷶹󷶶⅞󷶺󷷇󷶻󷷈↉󷷉"))))})
(TOFRAC:=(lambda x:(FRAC_CONV).get(x,x)))
class UPSIDEDOWNSYNDROME:
    (NRM:=("0123456789abcdefoxABCDEFOXîĵ󷺈ℇτπ󷺍󷺏∞"))
    (USD:=("󷰽󷰾󷰿󷱀󷱁󷱂󷱃󷱄󷱅󷱆󷱇󷱈󷱉󷱊󷱋󷱌󷱍󷱎󷱏󷱐󷱑󷱒󷱓󷱔󷱕󷱖󷱪󷱽󷱾󷱫󷱬󷱭󷱮󷱰󷱩"))
    (MAP:=({**(dict(ÄÕåØ(NRM,USD)))} | {**(dict(ÄÕåØ(USD,NRM)))}))
    (flip:=(lambda x,m=MAP:Âøî(ÁØò((lambda ÂîÓ:(m).get(ÂîÓ,ÂîÓ)))(x),ÁØã)))

class SCRIPT:
    (SCRIPT_FILE_LOC:=ð(moon_dir,("Builtins/Data/script.map")))
    (ÄÊPSH(ÄÝöÞ((ÐØó(SCRIPT_FILE_LOC)).strip(("\x0A")),("\x0A"))),((CHAR_NRM:=ÄÊPKE(0)[0]),(CHAR_SUP:=ÄÊPKE(0)[1]),(CHAR_SUB:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
    (SUP:=(ÁÜÙ).maketrans(CHAR_NRM,CHAR_SUP))
    (SUB:=(ÁÜÙ).maketrans(CHAR_NRM,CHAR_SUB))
    (NRM:=(ÁÜÙ).maketrans((CHAR_SUP + CHAR_SUB),ÂÞÅCAT(2,CHAR_NRM)))
    (ÄÊPSH(Áÿú([SUP,SUB,NRM],(lambda áÖæ:(lambda x:(x).translate(áÖæ))))),((sup:=ÄÊPKE(0)[0]),(sub:=ÄÊPKE(0)[1]),(nrm:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]

(ÄÊPSH(((SCRIPT).sup,(SCRIPT).sub,(SCRIPT).nrm)),((supscript:=ÄÊPKE(0)[0]),(subscript:=ÄÊPKE(0)[1]),(nrmscript:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
(ÄÊPSH(((SCRIPT).CHAR_SUP,(SCRIPT).CHAR_SUB)),((SUPSCRIPT:=ÄÊPKE(0)[0]),(SUBSCRIPT:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ALPHABETS:=Áÿú(ÄÝöÞ(Âüá(("\u000A    abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789\u000A    𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫 𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ 𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡\u000A    𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳 𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙 𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗\u000A    𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧 𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍 ◌◌◌◌◌◌◌◌◌◌\u000A    𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇 𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭 𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵\u000A    𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣 𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉 𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿\u000A    ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ ◌󰲡󰲣󰲥󰲧󰲩󰲫󰲭󰲯󰲱\u000A    ⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵ 🄐🄑🄒🄓🄔🄕🄖🄗🄘🄙🄚🄛🄜🄝🄞🄟🄠🄡🄢🄣🄤🄥🄦🄧🄨🄩 ◌⑴⑵⑶⑷⑸⑹⑺⑻⑼\u000A    󰫮󰫯󰫰󰫱󰫲󰫳󰫴󰫵󰫶󰫷󰫸󰫹󰫺󰫻󰫼󰫽󰫾󰫿󰬀󰬁󰬂󰬃󰬄󰬅󰬆󰬇 󰫮󰫯󰫰󰫱󰫲󰫳󰫴󰫵󰫶󰫷󰫸󰫹󰫺󰫻󰫼󰫽󰫾󰫿󰬀󰬁󰬂󰬃󰬄󰬅󰬆󰬇 󰬹󰬺󰬻󰬼󰬽󰬾󰬿󰭀󰭁󰭂\u000A    𜳖𜳗𜳘𜳙𜳚𜳛𜳜𜳝𜳞𜳟𜳠𜳡𜳢𜳣𜳤𜳥𜳦𜳧𜳨𜳩𜳪𜳫𜳬𜳭𜳮𜳯 𜳖𜳗𜳘𜳙𜳚𜳛𜳜𜳝𜳞𜳟𜳠𜳡𜳢𜳣𜳤𜳥𜳦𜳧𜳨𜳩𜳪𜳫𜳬𜳭𜳮𜳯 𜳰𜳱𜳲𜳳𜳴𜳵𜳶𜳷𜳸𜳹\u000A    𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓 𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹 𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫\u000A    ɒც𝼝𝼥⋿ꬵꬶҕї𝼚𝼐ꬷӍꬼϙƿ𝼛Ʀ𝼞ŧꭒѵꭐꭘꭚƶ ѦƁƇƊᗴҒႺⴼΙɈⴿꝈⱮͶⴲƤꝖⴽႽƬŲѴϢҲⵖΖ ◌◌◌◌◌◌◌◌◌◌\u000A    𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻 𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡 ◌◌◌◌◌◌◌◌◌◌\u000A    𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏 𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵 ◌◌◌◌◌◌◌◌◌◌\u000A    𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃 𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩 ◌◌◌◌◌◌◌◌◌◌\u000A    𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛 𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁 ◌◌◌◌◌◌◌◌◌◌\u000A    𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷 𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ ◌◌◌◌◌◌◌◌◌◌\u000A    𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟 𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅 ◌◌◌◌◌◌◌◌◌◌\u000A    𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯 𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕 ◌◌◌◌◌◌◌◌◌◌\u000A")),("\x0A")),Âåæ(ÂÛê,Âüá)))
(LOWERCASE:=Âøî(Áÿú(ALPHABETS,MOD(ÁÛÛ,áØÁ=0))))
(UPPERCASE:=Âøî(Áÿú(ALPHABETS,MOD(ÁÛÛ,áØÁ=1))))
(LETTERS:=(LOWERCASE + UPPERCASE))
(TERLETS:=(UPPERCASE + LOWERCASE))
(ÄÊPSH(ALPHABETS[0][slice(None,3)]),((abc:=ÄÊPKE(0)[0]),(ABC:=ÄÊPKE(0)[1]),(num:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
(ÄÊPSH(((abc + ABC),(abc + num),(ABC + num),((abc + ABC) + num))),((abcABC:=ÄÊPKE(0)[0]),(abc123:=ÄÊPKE(0)[1]),(ABC123:=ÄÊPKE(0)[2]),(abcABC123:=ÄÊPKE(0)[3])),ÄÊDEL(1))[1]
(TO_LOWERCASE:=CUR((lambda ÂîÓ,ÂîÒ:under_script(ÂîÒ,ÂîÓ)),(lambda ÂîÓ:(lambda x:(x).translate(ÂîÓ)))((ÁÜÙ).maketrans(UPPERCASE,LOWERCASE))))
(TO_UPPERCASE:=CUR((lambda ÂîÓ,ÂîÒ:under_script(ÂîÒ,ÂîÓ)),(lambda ÂîÓ:(lambda x:(x).translate(ÂîÓ)))((ÁÜÙ).maketrans(LOWERCASE,UPPERCASE))))
(REVERSE_CASE:=CUR((lambda ÂîÓ,ÂîÒ:under_script(ÂîÒ,ÂîÓ)),(lambda ÂîÓ:(lambda x:(x).translate(ÂîÓ)))((ÁÜÙ).maketrans(LETTERS,TERLETS))))
(GET_CASE:=(lambda x:((TO_UPPERCASE(x) == x) - (x == TO_LOWERCASE(x)))))
def under_script(áØÆ,Æå,áÕÉ=ÂÞÅ):
    (áÓÕ:=MOD((lambda ÂîÓ:((supscript)if((ÂîÓ in SUPSCRIPT))else(((subscript)if((ÂîÓ in SUBSCRIPT))else(None)))))))
    return Âøî(ËãÂ(ÄÕåØ(ÁØò((lambda ÂîÓ:MOD(ÆÑ,áØÁ=ÄÕÍÔ)(Áÿú(ÂÕÅ(ÂÛÜ(nrmscript,(Âåæ(Âó,áÓÕ))),ÂîÓ),áÓÕ),Âåæ)))((((áØÆ)if((áÕÉ is ÂÞÅ))else(áÕÉ)))),Æå(ÂÕÅ(ÂØÏ(nrmscript),áØÆ))),ÂÕÅ))


#subproca.☾ (1557 ⟶ 3221)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/subproca.☾')).parent
def ÄÊSUBPROCA(cmd,áÏÃ=ÁØã):
    from subprocess import Popen as áÐä, DEVNULL as NULL, PIPE, STDOUT
    ((ÄÊPOP(0))if(ÄÊPSH((not (((("M") in áÏÃ) and ÂÕÖ(áÏÃ,("OEoe")))) )))else(ÂùÆ(ÄÊPOP(0),("Cannot use stdout/err and MERGE at once"))))
    ((ÄÊPOP(0))if(ÄÊPSH((not ((((((("o") in ÄÊPSH(áÏÃ)) and ÂÔö(ÄÊPOP(0),ÄÊPSH(("O")))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)) or ((((("e") in ÄÊPSH(áÏÃ)) and ÂÔö(ÄÊPOP(0),ÄÊPSH(("E")))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)))) )))else(ÂùÆ(ÄÊPOP(0),("Cannot suppress and ignore stdout/err"))))
    (K:=ÐÌü(ÂÑÖ()))
    (ÄÊPSH(ÁØò((lambda ÂîÓ:(ÂîÓ in áÏÃ)))((vs:=("toeBPSD")))),((áÐÍ:=ÄÊPKE(0)[0]),(áÐÈ:=ÄÊPKE(0)[1]),(áÏý:=ÄÊPKE(0)[2]),(áÏß:=ÄÊPKE(0)[3]),(áÏí:=ÄÊPKE(0)[4]),(áÏð:=ÄÊPKE(0)[5]),(áÏá:=ÄÊPKE(0)[6])),ÄÊDEL(1))[1]
    (ÄÊPSH(áÏÃ),ÄÊPSH((ÂÕÃ(ÄÊPKE(0),vs) or {("R")})),(áÏÃ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    if áÏð:
        (ÄÊPSH(K),ÄÊPSH(("shell")),ÄÊPSH(True),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
    
    if (("M") in áÏÃ):
        (ÄÊPSH(K),ÄÊPSH(("stdout")),ÄÊPSH(K),ÄÊPSH(("stderr")),ÄÊPSH((PIPE,STDOUT)),(setattr(ÄÊPKE(4),ÄÊPKE(3),ÄÊPKE(0)[0]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)[1])),ÄÊDEL(5))[5]
    else :
        if (not áÐÈ ):
            (ÄÊPSH(K),ÄÊPSH(("stdout")),ÄÊPSH(((PIPE)if((("O") in áÏÃ))else(NULL))),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        
        if (not áÏý ):
            (ÄÊPSH(K),ÄÊPSH(("stderr")),ÄÊPSH(((PIPE)if((("E") in áÏÃ))else(NULL))),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        
    
    (ÄÊPSH(K),ÄÊPSH(("bufsize")),ÄÊPSH(ÂÞÅCAT(((2 ** (6))),((2 ** (10))))),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
    def p_stream(x):
        (t:=ÐÌü((getattr(p,x)).read))
        if áÏß:
            return t
        
        (t:=(t).decode(("UTF8")))
        return ((t)if(áÐÍ)else((t).removesuffix(("\x0A"))))
    
    def extract(p):
        (r:=ÐÌü(ÂÑØ()))
        if ÂÔö(áÏÃ,(v:=("R"))):
            (ÄÊPSH(r),ÄÊPSH(v),ÄÊPSH((p).returncode),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        
        if ÂÔö(áÏÃ,(v:=("M"))):
            (ÄÊPSH(r),ÄÊPSH(v),ÄÊPSH(p_stream(("stdout"))),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        else :
            if ÂÔö(áÏÃ,(v:=("O"))):
                (ÄÊPSH(r),ÄÊPSH(v),ÄÊPSH(p_stream(("stdout"))),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
            
            if ÂÔö(áÏÃ,(v:=("E"))):
                (ÄÊPSH(r),ÄÊPSH(v),ÄÊPSH(p_stream(("stderr"))),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
            
        
        return ((r[ÐÌü((áÏÃ).pop)])if((ãÊú(áÏÃ) == 1))else(r))
    
    class Popen_Proxy:
        (__slots__:=(("p"),))
        (__init__:=(lambda áÑÞ,p:ÂåÔ((ÄÊPSH(áÑÞ),ÄÊPSH(("p")),ÄÊPSH(p),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3],None)))
        (__call__:=(lambda áÑÞ:ÂåÔ(ÐÌü(((áÑÞ).p).wait),extract(p))))
        (__getitem__:=(lambda áÑÞ,*áÑË:(ÐÌü(áÑÞ)).__getitem__(*áÑË)))
        (__getattr__:=(lambda áÑÞ,*áÑË:(ÐÌü(áÑÞ)).__getattr__(*áÑË)))
        (__iter__:=(lambda áÑÞ,*áÑË:(ÐÌü(áÑÞ)).__iter__(*áÑË)))
    
    if áÏá:
        Âçß(("Running: \u0022%s\u0022")%(termclr(cmd,("3d3")),))
    
    (p:=áÐä(ÂÛê(cmd),**K))
    return MOD(Áëý,áØÁ=(not áÏí ))(ÂÞÅCAT(p,Popen_Proxy),ÐÌü)


#Ń.☾ (4885 ⟶ 9928)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/Ń.☾')).parent
from collections import deque as áÐòþáÑÁ
class ÅÒ:
    (__slots__:=(("t"),("c"),("e")))
    def __init__(ÄÕÒü,t,*c,e=ÂÞÅ):
        (ÄÊPSH(ÄÕÒü),ÄÊPSH(("t")),ÄÊPSH(ÄÕÒü),ÄÊPSH(("c")),ÄÊPSH(ÄÕÒü),ÄÊPSH(("e")),ÄÊPSH((t,(([*c])if(c)else([])),((MOD(ÂÑÖ,áØÁ=None)())if((e is ÂÞÅ))else(e)))),(setattr(ÄÊPKE(6),ÄÊPKE(5),ÄÊPKE(0)[0]),setattr(ÄÊPKE(4),ÄÊPKE(3),ÄÊPKE(0)[1]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)[2])),ÄÊDEL(7))[7]
        for z in((ÄÕÒü).c):
            if not(ÄÝøÇ(z,ÅÒ)):continue
            ((ÄÊPOP(0))if(ÄÊPSH(False))else(ÂùÆ(ÄÊPOP(0),("%s; %s; %s")%(t,z,c,))))
        
    
    (__contains__:=(lambda ÄÕÒü,x:(((x in (ÄÕÒü).e))if(ÁØö(x,ÁÜÙ))else((x in (ÄÕÒü).c)))))
    (__repr__:=(lambda ÄÕÒü:("Ń(%s│%s)⟨%s⟩")%(((ÄÕÒü).t or ("∅")),((ÄÕÒü).e or ("∅")),Âøî(ÄÕÒü,(", ")),)))
    (__setitem__:=(lambda ÄÕÒü,x,y:(ÄÊPSH((ÄÕÒü).c),ÄÊPSH(x),ÄÊPSH(y),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]))
    (__and__:=(lambda ÄÕÒü,x:((ÄÕÒü).t == (x).t)))
    (__len__:=(lambda ÄÕÒü:ãÊú((ÄÕÒü).c)))
    (__iter__:=(lambda ÄÕÒü:iter((ÄÕÒü).c)))
    def __getitem__(ÄÕÒü,i):
        return (ÄÕÒü).c[i]
    
    def __delitem__(ÄÕÒü,i):
        del (ÄÕÒü).c[i]
    
    def set(ÄÕÒü,t=None,c=None,e=None):
        if (t is not None):
            (ÄÊPSH(ÄÕÒü),ÄÊPSH(("t")),ÄÊPSH(t),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        
        if (c is not None):
            (ÄÊPSH(ÄÕÒü),ÄÊPSH(("c")),ÄÊPSH(c),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        
        if (e is not None):
            (ÄÊPSH(ÄÕÒü),ÄÊPSH(("e")),ÄÊPSH(e),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        
        return ÄÕÒü
    
    def from_(ÄÕÒü,R):
        (ÄÊPSH(ÄÕÒü),ÄÊPSH(("t")),ÄÊPSH((R).t),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        (ÄÊPSH(ÄÕÒü),ÄÊPSH(("c")),ÄÊPSH((R).c),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        (ÄÊPSH(ÄÕÒü),ÄÊPSH(("e")),ÄÊPSH((R).e),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        return ÄÕÒü
    
    (cp:=(copy:=(lambda ÄÕÒü,t=None,c=None,e=ÂÞÅ:ÅÒ((((ÄÕÒü).t)if((t is None))else(t)),*((((ÄÕÒü).c)if((c is None))else(c))),e=((((ÄÕÒü).e).copy())if((e is ÂÞÅ))else(e))))))
    (cpr:=(rcopy:=(lambda ÄÕÒü:ÅÒ((ÄÕÒü).t,*(Áÿú((ÄÕÒü).c,(ÅÒ).cpr)),e=((ÄÕÒü).e).copy()))))
    def part(ÄÕÒü):
        (ÄÊPSH(ÄÕÒü),ÄÊPSH(("c")),ÄÊPSH(ÂÕÃ((ÄÕÒü).c,((ÄÕÒü).e ** ì))),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        return (ÄÕÒü,(ÄÕÒü).e)
    
    def frp(ÄÕÒü,Æå,r,pre=False,not_T=True):
        if (r is None):
            return (lambda r:(ÄÕÒü).frp(Æå,r,pre,not_T))
        
        if not_T:
            (Æå:=(lambda ÄÕÒü,Æå=Æå:((not ((ÄÕÒü).e).T ) and Æå(ÄÕÒü))))
        
        if pre:
            if (not ãÊú(ÄÕÒü) ):
                return ((r(ÄÕÒü))if(Æå(ÄÕÒü))else(ÄÕÒü))
            
            (ÄÊPSH((áÐòþáÑÁ([ÄÕÒü]),áÐòþáÑÁ())),((áÖå:=ÄÊPKE(0)[0]),(áÖæ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
            (ÄÊPSH(((áÖå).popleft,(áÖå).extend,(áÖæ).appendleft)),((pl:=ÄÊPKE(0)[0]),(ex:=ÄÊPKE(0)[1]),(al:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
            while(áÖå):
                (C:=pl())
                ex([(c)for c in(C)if((c).c)])
                al(C)
            
            for C in(áÖæ):
                for (i,c) in(enumerate(C)):
                    if not(Æå(c)):continue
                    (ÄÊPSH(C),ÄÊPSH(i),ÄÊPSH(r(c)),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
                
            
            return ((r(ÄÕÒü))if(Æå(ÄÕÒü))else(ÄÕÒü))
        else :
            def áÏï(ÄÕÒü):
                if Æå(ÄÕÒü):
                    return r(ÄÕÒü)
                
                for (i,y) in(enumerate(ÄÕÒü)):
                    (ÄÊPSH(ÄÕÒü),ÄÊPSH(i),ÄÊPSH(áÏï(y)),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
                
                return ÄÕÒü
            
            return áÏï(ÄÕÒü)
        
    
    def ftrp(ÄÕÒü,fs,Æå,pre=False,not_T=True,**áÏè):
        if (Æå is None):
            return (lambda Æå:(ÄÕÒü).ftrp(fs,Æå,pre,not_T,**áÏè))
        
        if ÄÝøÇ(fs,ÁÜÙ):
            (fs:=frozenset(fs))
        
        return ((ÄÕÒü)if((not_T and ((ÄÕÒü).e).T))else((ÄÕÒü).frp((((lambda x:((x).t == fs)))if(ÁØö(fs,ÁÜÙ))else((lambda x:((x).t in fs)))),Æå,pre,not_T,**áÏè)))
    
    def gets(ÄÕÒü,Æå,not_T=True):
        if (not áÓó(Æå) ):
            if ÁØö(Æå,ÁÜÙ):
                (Æå:=(lambda ÄÕÒü,t=Æå:((ÄÕÒü).t == t)))
            else :
                (Æå:=(lambda ÄÕÒü,t=Æå:((ÄÕÒü).t in t)))
            
        
        return [(c)for c in(ÄÕÒü)if((((((((ÄÊDEL(1),False)[1])if(((c).e).T)else(ÄÊPOP(0))))if(ÄÊPSH(not_T))else((ÄÊDEL(1),True)[1]))) and Æå(c)))]
    
    def find(ÄÕÒü,Æå,pre=True,not_T=True,R=None):
        if (R is None):
            (R:=[])
        
        if (not_T and ((ÄÕÒü).e).T):
            return R
        
        if pre:
            for c in(ÄÕÒü):
                (c).find(Æå,True,not_T,R)
            
        
        if (do:=Æå(ÄÕÒü)):
            (R).append(ÄÕÒü)
        
        if (do and (not pre )):
            for c in(ÄÕÒü):
                (c).find(Æå,False,not_T,R)
            
        
        return R
    
    def rm(ÄÕÒü,Æå,not_T=True):
        if ÁØö(Æå,ÁÜÙ):
            (Æå:=(lambda ÄÕÒü,t=Æå:((ÄÕÒü).t == t)))
        
        for (i,x) in(ÂÓÏ(ÄÕÒü)[slice(None,None,((- 1 )))]):
            if not((((((ÄÊDEL(1),False)[1])if(((x).e).T)else(ÄÊPOP(0))))if(ÄÊPSH(not_T))else((ÄÊDEL(1),True)[1]))):continue
            if Æå(x):
                del ÄÕÒü[i]
            else :
                (ÄÕÒü[i]).rm(Æå,not_T)
            
        
        return ÄÕÒü
    
    def sep(ÄÕÒü,*áÑË,**áÑÕ):
        (M:=(ÄÕÒü).find(*áÑË,**áÑÕ))
        (ÄÕÒü).rm(CURR((lambda ÂîÓ,ÂîÒ:(ÂÞÅCAT(ÂîÓ,id) in ÂîÒ)),frozenset(Áÿú(M,id))))
        return M
    
    def flat(ÄÕÒü,Æå,áÑÂ=True):
        (C:=[])
        for c in(ÄÕÒü):
            ((((C).append)if((((c).e).T or (not Æå((c:=(((c).flat(Æå))if(áÑÂ)else(c)))) )))else((C).extend)))(c)
        
        (ÄÊPSH(ÄÕÒü),ÄÊPSH(("c")),ÄÊPSH(C),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        return ÄÕÒü
    
    def __pos__(ÄÕÒü):
        (áØÀ:=(""))
        if ((ÄÕÒü).e).T:
            return (ÄÕÒü).t
        
        (áÖã:=áÐòþáÑÁ((ÄÕÒü).c))
        while(áÖã):
            (v:=(áÖã).popleft())
            if ((v).e).T:
                (ÄÊPSH(áØÀ),ÄÊPSH((ÄÊPKE(0) + (v).t)),(áØÀ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
            else :
                (áÖã).extendleft(reversed((v).c))
            
        
        return áØÀ
    
    def lchar(ÄÕÒü):
        if (((ÄÕÒü).e).T and (ÄÕÒü).t):
            return (ÄÕÒü).t[0]
        
        for c in((ÄÕÒü).c):
            if not((x:=(c).lchar())):continue
            return x
        
        return ("")
    
    def rchar(ÄÕÒü):
        if (((ÄÕÒü).e).T and (ÄÕÒü).t):
            return (ÄÕÒü).t[((- 1 ))]
        
        for c in((ÄÕÒü).c[slice(None,None,((- 1 )))]):
            if not((x:=(c).rchar())):continue
            return x
        
        return ("")
    
    def farnodes(ÄÕÒü,Æå=MOD((lambda ÂîÓ:(not ((ÂîÓ).e).T )))):
        (Ïß:=(Ïà:=ÄÕÒü))
        while((Æå(Ïß) and ãÊú(Ïß))):
            (Ïß:=Ïß[0])
        
        while((Æå(Ïà) and ãÊú(Ïà))):
            (Ïà:=Ïà[((- 1 ))])
        
        return (Ïß,Ïà)
    
    def first_l(ÄÕÒü,Æå):
        if Æå(ÄÕÒü):
            return ÄÕÒü
        
        for áÎÚ in(ÄÕÒü):
            if not(((l:=(áÎÚ).first_l(Æå)) is not None)):continue
            return l
        
    
    def first_r(ÄÕÒü,Æå):
        if Æå(ÄÕÒü):
            return ÄÕÒü
        
        for áÎÚ in(ÄÕÒü[slice(None,None,((- 1 )))]):
            if not(((r:=(áÎÚ).first_r(Æå)) is not None)):continue
            return r
        
    
    (first_sides:=(lambda ÄÕÒü,Æå:((ÄÕÒü).first_l(Æå),(ÄÕÒü).first_r(Æå))))
    (filter:=(lambda ÄÕÒü,Æå,*áÑË,**áÑÕ:(ÄÕÒü).rm(Âåæ(Âó,Æå),*áÑË,**áÑÕ)))
    @property
    def ÄÔÕý(áÑÞ):
        return (+ áÑÞ )
    
    def P(ÄÕÒü,fs=True):
        if (not hasattr(ÅÒ,(attr:=("txt_format_imported"))) ):
            (ÄÊPSH(__ÄÊIMPORT__(("text_format"),globals(),(""))),ÄÊPOP(0))[((- 1 ))]
        
        (ÄÊPSH(ËãÂ(ÂÛê(("∅ f00 → 00f 󰅁 ff0 󰅂 ff0")),Åøþáüì)),((NA:=ÄÊPKE(0)[0]),(AR:=ÄÊPKE(0)[1]),(yl:=ÄÊPKE(0)[2]),(yr:=ÄÊPKE(0)[3])),ÄÊDEL(1))[1]
        if ÄÝøÇ(ÄÕÒü,ÅÒ):
            return Åøþáüì(ÁÜÙ(ÄÕÒü),("f00"))
        
        def format_e(e):
            if (not e ):
                return ÁØã
            
            (r:=ËãÂ(e,(lambda x,y:((ÄÔýò)if((x in {*(("Tpρ"))}))else(((("%s%s%s")%(x,AR,(y).t,))if(ÁØö(y,ÅÒ))else(("%s=%s")%(x,y,))))))))
            return MOD(Áëý,áØÁ=r)(((((Åøþáüì((lambda ÂîÓ:((Âøî(ËãÂ(ÄÕåØ(Áÿú(ÂÿÇ(ÂîÓ),ÁÛÛ([ÄÝõà,ÄÝõá])),ÂîÓ),ÂÕÅ)))if((ãÊú(ÂîÓ) == 4))else(ÄÝõà(Âøî(ÂîÓ,("…"))))))((e).p),("ff0")))if((("p") in e))else(ÁØã))) + (((Åøþáüì((lambda ÂîÓ:((Âøî(ËãÂ(ÄÕåØ(Áÿú(ÂÿÇ(ÂîÓ),ÁÛÛ([ÄÝõà,ÄÝõá])),ÂîÓ),ÂÕÅ)))if((ãÊú(ÂîÓ) == 4))else(ÄÝõà(Âøî(ÂîÓ,("…"))))))(getattr(e,("ρ"))),("0ff")))if((("ρ") in e))else(ÁØã)))),MOD((lambda ÂîÓ:stackr(ÂîÓ,Âøî(r,("\x0A"))))))
        
        (áØÀ:=box(((((ÂÞÅCAT(False,((ÄÕÒü).t).P))if(ÁØö((ÄÕÒü).t,ÅÒ))else(((stackr(Åøþáüì((ÄÕÒü).t,("f55")),ÂÞÅCAT((ÄÕÒü).e,format_e)))if(ÁØö(ÄÕÒü,ÅÒ))else(ÁÜÙ((ÄÕÒü).t)))))) or NA),fg=((("0f0"))if((ÁØö(ÄÕÒü,ÅÒ) and ((ÄÕÒü).e).T))else(("00007f")))))
        if ãÊú(ÄÕÒü):
            (ÄÊPSH(Áÿú(("─╰├┬│"),ÄÊCUR((1,),{"fg":("11a")},Åøþáüì,ÂýÃ))),((ÂâÑ:=ÄÊPKE(0)[0]),(ÂäÇ:=ÄÊPKE(0)[1]),(Ââî:=ÄÊPKE(0)[2]),(ÂãÀ:=ÄÊPKE(0)[3]),(ÂâÓ:=ÄÊPKE(0)[4])),ÄÊDEL(1))[1]
            (áØÀ:=stackr(áØÀ,Âøî(ËãÂ(ÂÓÏ(ÄÕÒü),(lambda x,y:Âøî(ËãÂ(ÂÓÏ(ÂÞÅCAT(ÂÞÅCAT(False,(y).P),lines)),CUR((lambda ÂîÓ,ÂîÒ:ÂÁÍ(ì)(ÂîÒ,(((ÂâÑ)if((((ÄÊDEL(1),False)[1])if(ÄÊPSH(ÂîÓ))else(((ÄÊPOP(0))if((ãÊú(ÄÕÒü) != 1))else((ÄÊDEL(1),True)[1])))))else(((((ÂîÓ and (" ")) or ÂäÇ))if((x == (ãÊú(ÄÕÒü) - 1)))else(((((x and Ââî) or ÂãÀ))if((((ÄÊDEL(1),False)[1])if(ÄÊPSH(ÂîÓ))else(((ÄÊPOP(0))if((ãÊú(ÄÕÒü) == 0))else((ÄÊDEL(1),True)[1])))))else(ÂâÓ))))))))))),("\x0A")))),("\x0A"))))
        
        return ((ÂåÔ(Âçß(áØÀ),ÄÕÒü))if(fs)else(áØÀ))
    


#cache.☾ (1312 ⟶ 2688)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/cache.☾')).parent
class Cacher:
    def __init__(áÑÞ,Æå,áÕÈ,áÕÅ,áÕÄ):
        (ÄÊPSH(áÑÞ),ÄÊPSH(("Æå")),ÄÊPSH(áÑÞ),ÄÊPSH(("áÕÈ")),ÄÊPSH(áÑÞ),ÄÊPSH(("áÕÅ")),ÄÊPSH(áÑÞ),ÄÊPSH(("áÕÄ")),ÄÊPSH(áÑÞ),ÄÊPSH(("áÍò")),ÄÊPSH((Æå,áÕÈ,áÕÅ,áÕÄ,{})),(setattr(ÄÊPKE(10),ÄÊPKE(9),ÄÊPKE(0)[0]),setattr(ÄÊPKE(8),ÄÊPKE(7),ÄÊPKE(0)[1]),setattr(ÄÊPKE(6),ÄÊPKE(5),ÄÊPKE(0)[2]),setattr(ÄÊPKE(4),ÄÊPKE(3),ÄÊPKE(0)[3]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)[4])),ÄÊDEL(11))[11]
    
    def __call__(áÑÞ,*áÑË,**áÑÕ):
        (áÖñ:=(áÑÞ).áÕÈ(getattr((áÑÞ).Æå,("__name__"),("")),*áÑË,**áÑÕ))
        if ((v:=(áÑÞ).chk_cache(áÖñ)) is not ÂÞÅ):
            return (áÑÞ).áÕÄ(v)
        
        (v:=(áÑÞ).Æå(*áÑË,**áÑÕ))
        (áÑÞ).add_cache(áÖñ,(áÑÞ).áÕÅ(v))
        return v
    
    def chk_cache(áÑÞ,x):
        return ((áÑÞ).áÍò).get(x,ÂÞÅ)
    
    def add_cache(áÑÞ,x,y):
        return (ÄÊPSH((áÑÞ).áÍò),ÄÊPSH(x),ÄÊPSH(y),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
    

class FileCacher(Cacher):
    def __init__(áÑÞ,Æå,áÕÈ,áÕÅ,áÕÄ,fp=ÁØã,file_only=False):
        (super()).__init__(Æå,áÕÈ,áÕÅ,áÕÄ)
        (ÄÊPSH(áÑÞ),ÄÊPSH(("áÖòþáÖü")),ÄÊPSH(áÑÞ),ÄÊPSH(("áÖòþáÖý")),ÄÊPSH((file_only,mkd(((fp)if((ÁØö(fp,áÌî) and ÐÌü((fp).is_absolute)))else(ð(CACHEDIR,fp)))))),(setattr(ÄÊPKE(4),ÄÊPKE(3),ÄÊPKE(0)[0]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)[1])),ÄÊDEL(5))[5]
    
    def __call__(áÑÞ,*áÑË,**áÑÕ):
        (log:=(("MOON_LOG_FCACHE") in env))
        (áÖñ:=(áÑÞ).áÕÈ((fname:=getattr((áÑÞ).Æå,("__name__"),(""))),*áÑË,**áÑÕ))
        if ((v:=(áÑÞ).chk_cache(áÖñ)) is not ÂÞÅ):
            if log:
                Âçß(("Cache hit (%s)!\x0A𝔸=%s\x0A𝕂=%s\x0A⇒%s")%((fname or None),ÁÜÙ(áÑË),ÁÜÙ(áÑÕ),ÁÜÙ(v),))
            
            return (áÑÞ).áÕÄ(v)
        
        (v:=(áÑÞ).Æå(*áÑË,**áÑÕ))
        (áÑÞ).add_cache(áÖñ,(áÑÞ).áÕÅ(v))
        if log:
            Âçß(("Cache fail (%s)!\x0A𝔸=%s\x0A𝕂=%s\x0A⇒%s")%((fname or None),ÁÜÙ(áÑË),ÁÜÙ(áÑÕ),ÁÜÙ(v),))
        
        return v
    
    def chk_cache(áÑÞ,x):
        if ((not (áÑÞ).áÖòþáÖü ) and (x in (áÑÞ).áÍò)):
            return (áÑÞ).áÍò[x]
        
        if ÐÌü((((f:=ð((áÑÞ).áÖòþáÖý,x)))).exists):
            (v:=(ÐØó).b(f))
            return (((ÄÊPSH((áÑÞ).áÍò),ÄÊPSH(x),ÄÊPSH(v),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3])if((áÑÞ).áÖòþáÖü)else(v))
        
        return ÂÞÅ
    
    def add_cache(áÑÞ,x,y):
        (ÐØì).b(ð((áÑÞ).áÖòþáÖý,x),(ÄÊPSH((áÑÞ).áÍò),ÄÊPSH(x),ÄÊPSH(y),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3])
    

(mkmk_cache:=(lambda ÆÚ:(lambda áÕÈ=sha,áÕÅ=pdump,áÕÄ=pload,*áÔå,**áÔï:(lambda Æå:ÆÚ(Æå,áÕÈ,áÕÅ,áÕÄ,*áÔå,**áÔï)))))
(ÄÊPSH(Áÿú([Cacher,FileCacher],mkmk_cache)),((cache:=ÄÊPKE(0)[0]),(fcache:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]

#meta.☾ (4917 ⟶ 6838)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/meta.☾')).parent
(IMPSIMPS:=((("ℍ"),("ℍ󷸙󷸘󷸛󷸚󷸗󷸖󷸜󷸽󷸕ĵ󷺈󷱽󷱾")),(("⫚"),("⫚")),(("¶"),("¶✿"))))
(ÄÊPSH((ÐÌü(ÂÑÖ()),{})),((__ÄÊIMPORTS__:=ÄÊPKE(0)[0]),(TP_CACHE:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(TRANSPILE_REF:=ÐÌü(Holder))
def EXEC_NATIVE(áÖï,*áÑË,**áÑÕ):
    try :
        exec(áÖï,*áÑË,**áÑÕ)
    except áÍÚ as Ïã:
        Âçß(("Exec failed! Writing to %s")%((o:=ÂÞÅCAT(("/tmp/%s")%(Âøî(ÐâÇ(abc,NULL)),),áÌî)),))
        MOD(ÄÕéý,áØÁ=ÐØì)(o,áÖï)
        raise Ïã
    

(dump_cached_imports:=(lambda :("TP_CACHE.update(\u007B%s\u007D)")%((lambda ÂîÓ:Âøî(ÂîÓ,(",")))(ÁØò((lambda ÂîÓ:("%s:strd(%s)")%(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(moon_dir,(ÂîÓ[0]).relative_to),ÁÜÙ),repr),ÂÞÅCAT(ÂÞÅCAT((ÂîÓ[1]).native_code,stre),repr),)))(ÄÔÔç(__ÄÊIMPORTS__,MOD((lambda ÂîÓ:(ÂîÓ[0]).is_relative_to(moon_dir)))))),)))
@cache_
def moon_to_py_cached(áÖï):
    ((ÄÊPOP(0))if(ÄÊPSH(TRANSPILE_REF))else(ÂùÆ(ÄÊPOP(0),("Cannot transpile without transpiler!"))))
    return ÂÞÅCAT(áÖï,((+ TRANSPILE_REF )))

def ÄÕôñ(áÖï,ns=None,get_code=False,include_builtins=True,native=False,Æå=EXEC_NATIVE,ret=False,init_ns=True,code_ref=True,custom_errors=True,show_error_áÑÕ={}):
    if (env).get(("MOON_DISABLE_CUSTOM_ERRORS")):
        (custom_errors:=False)
    
    (áÕÃ:=áÖï)
    if (not native ):
        (áÖï:=moon_to_py_cached(áÖï))
    
    if get_code:
        return áÖï
    
    if init_ns:
        (ns:=(ÐÌü((BOOTSTRAP_GLOBALS).copy) | ((({})if((ns is None))else(ns)))))
    
    if (code_ref and (not native )):
        (ÄÊPSH(ns),ÄÊPSH(("__moon_code__")),ÄÊPSH(áÕÃ),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
    
    try :
        (r:=Æå(áÖï,ns))
    except áÍÚþáÍÚ as Ïã:
        if (not custom_errors ):
            raise Ïã
        
        (ÄÊPSH(__ÄÊIMPORT__(("errors"),globals(),(""))),ÄÊPOP(0))[((- 1 ))]
        return show_error(Ïã,**show_error_áÑÕ)
    
    return ((r)if(ret)else(ns))

class Module(ÁØö(ÐÌü(ÂÑÖ()))):
    def __init__(áÑÞ,name,ns,code=None,native_code=None,hardcoded=False):
        (super()).__init__(ns)
        (ÄÊPSH(áÑÞ),ÄÊPSH(("name")),ÄÊPSH(áÑÞ),ÄÊPSH(("code")),ÄÊPSH(áÑÞ),ÄÊPSH(("native_code")),ÄÊPSH(áÑÞ),ÄÊPSH(("hardcoded")),ÄÊPSH((name,code,native_code,hardcoded)),(setattr(ÄÊPKE(8),ÄÊPKE(7),ÄÊPKE(0)[0]),setattr(ÄÊPKE(6),ÄÊPKE(5),ÄÊPKE(0)[1]),setattr(ÄÊPKE(4),ÄÊPKE(3),ÄÊPKE(0)[2]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)[3])),ÄÊDEL(9))[9]
    
    def __repr__(áÑÞ):
        return ("Module[%s,%s]")%((áÑÞ).name,("✗✓")[(áÑÞ).hardcoded],)
    

def IMPORT_find_file(p,g_dir=None,w_dir=None,flags=ÁØã):
    (ÄÊPSH(((((ÄÊPSH(p),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),áÌî)),(p:=ÄÊPKE(0)),ÄÊDEL(2))[2])).name,None,None,ÂÚü())),((name:=ÄÊPKE(0)[0]),(F:=ÄÊPKE(0)[1]),(native:=ÄÊPKE(0)[2]),(failed:=ÄÊPKE(0)[3])),ÄÊDEL(1))[1]
    (dirs:=ÄÔÔè(((((p).parent)if(ÐÌü((p).is_absolute))else(None)),g_dir,((ÐÌü(pwd))if((w_dir is None))else(w_dir)),ð(moon_dir,("Libraries"))),None))
    (sufs:=(p,("%s.py")%(p,),("%s.☾")%(p,),ð(p,("main.py")),ð(p,("main.☾")),ð(p,(p).name)))
    for F in(ËãÂ(ÂøÚ(dirs,sufs),ð)):
        (ÄÊPSH(F),ÄÊPSH(ÐÌü((ÄÊPKE(0)).resolve)),(F:=ÄÊPKE(0)),ÄÊDEL(2))[2]
        if (((("↺") not in flags) and ÂÞÅCAT(moon_dir,(F).is_relative_to)) and ((h:=ÂÞÅCAT(ÂÞÅCAT(moon_dir,(F).relative_to),ÁÜÙ)) in TP_CACHE)):
            (native:=h)
            break 
        
        if ÐÌü((F).is_file):
            break 
        
        (failed).append(F)
        (F:=None)
    
    return (name,F,native,failed)

def __ÄÊIMPORT__(p,áÒÿ,flags=ÁØã):
    if (("Ń") in p):
        return 
    
    (ÄÊPSH(MOD(Áëý,áØÁ=ÄÊCUR((1,),{},ÄÝøÇ,ÂýÃ,áÍé))(p,ÄÊCUR((1,),{},IMPORT_find_file,ÂýÃ,(áÒÿ).get(("__dir__")),ÐÌü(pwd),flags))),((name:=ÄÊPKE(0)[0]),(F:=ÄÊPKE(0)[1]),(native:=ÄÊPKE(0)[2]),(failed:=ÄÊPKE(0)[3])),ÄÊDEL(1))[1]
    if (("MOON_LOG_IMPORTS") in env):
        Âçß(("⨡%s %s = \u0022%s\u0022 : %s (native=%s) (→ %s)")%(ÄÝõá(flags),p,name,F,native,áÒÿ[("__file__")],))
        Âçß(("\x0Amoon_dir=%s\x0A__þIMPORTS__:\x0A%s")%(moon_dir,ÂîË(ÁØò((lambda ÂîÓ:(("\x09") + Âøî(ÂîÓ,(" → ")))))(__ÄÊIMPORTS__),("\x0A")),))
    
    ((ÄÊPOP(0))if(ÄÊPSH((F is not None)))else(ÂùÆ(ÄÊPOP(0),("Unable to find module \u0022%s\u0022! Paths checked:%s")%(name,ÂîÊ(failed,("\x0A")),))))
    if ((("↺") in flags) or (F not in __ÄÊIMPORTS__)):
        (ÄÊPSH(__ÄÊIMPORTS__),ÄÊPSH(F),ÄÊPSH(None),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        try :
            (ns:={("__name__"):name,("__file__"):F,("__dir__"):(F).parent,("__path__"):ÂÞÅCAT((F).parent,ÁÜÙ),("__EXPORTS__"):{},("__þIMPORTS__"):__ÄÊIMPORTS__,("TP_CACHE"):TP_CACHE,("TRANSPILE_REF"):TRANSPILE_REF})
            (áÑÕ:=ÂÞÅCAT({("code"):ÂÞÅCAT(F,ÐØó)},ÂÑÖ()))
            if ((F).suffix == (".py")):
                (ÄÊPSH(áÑÕ),ÄÊPSH(("native_code")),ÄÊPSH((áÑÕ).code),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
                (ÄÊPSH(ns),ÄÊPSH(("__moon_code__")),ÄÊPSH(ÂÞÅCAT((F).with_suffix((".☾")),ÐØó)),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
            else :
                (ÄÊPSH(ns),ÄÊPSH(("__moon_code__")),ÄÊPSH((áÑÕ).code),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
                (ÄÊPSH(áÑÕ),ÄÊPSH(("native_code")),ÄÊPSH(((ÄÕôñ((áÑÕ).code,get_code=True))if((native is None))else(TP_CACHE[native]))),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
            
            (ns:=ÄÕôñ((áÑÕ).native_code,ns=ns,native=True))
            (ÄÊPSH(__ÄÊIMPORTS__),ÄÊPSH(F),ÄÊPSH(Module(name,ns,hardcoded=(native is not None),**áÑÕ)),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
            if (name not in (sys).modules):
                (ÄÊPSH((sys).modules),ÄÊPSH(name),ÄÊPSH(__ÄÊIMPORTS__[F]),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
            
        except áÍÚ as Ïã:
            (__ÄÊIMPORTS__).pop(F,None)
            Âçß(("Error importing \u0022%s\u0022!")%(F,))
            raise Ïã
        
    
    (mod:=__ÄÊIMPORTS__[F])
    if ((k:=("__EXPORTS__")) in mod):
        ÂÞÅCAT(mod[k],(áÒÿ).update)
    else :
        ((ÄÊPOP(0))if(ÄÊPSH(False))else(MOD(ÂùÆ,áØÁ=ÂÄ)(ÄÊPOP(0),("%s has no \u0022%s\u0022 symbol! This is strange!")%(mod,k,))))
    
    return mod

def __ÄÊADD_EXPORTS__(áÒÿ,*áÑË):
    (E:=(áÒÿ).setdefault(("__EXPORTS__"),{}))
    (E).update({**(dict(áÑË))})
    return E

def __ÄÊADDGLOBALS_CLEAN__(M,áÒÿ):
    (áÒÿ).update(MOD(ËãÂ,áØÁ=ë)(ÂÞÅCAT(M,áÍÙ),(lambda x,y:((ÄÔýò)if((x).startswith(("_")))else((x,y))))))

(__ÄÊGET_GLOB_MODNAME__:=(lambda *áÑË:áÑË))
(__ÄÊSET_GLOB_MODNAME__:=(lambda *áÑË:áÑË))
def show_imports():
    (ÄÊPSH(__ÄÊIMPORT__(("text_format"),globals(),(""))),ÄÊPOP(0))[((- 1 ))]
    (show_table:=(lambda x,y:Âøî(Áÿú(ÂÛÅ(ÁØò((lambda ÂîÓ:ÂåÔ((m:=ÂóÍ(Áÿú(ÂîÓ,áüíþËðâ))),Áÿú(ÂîÓ,ÄÊCUR((1,),{},padc,ÂýÃ,m)))))(ÂÛÅ(MOD(Áÿú,áØÁ=2)(([x] + y),ÁÜÙ)))),ÄÊCUR((1,),{},Âøî,ÂýÃ,("│"))),("\x0A"))))
    Âçß(show_table(ÂÛê(("Static Name Path")),ËãÂ(__ÄÊIMPORTS__,(lambda x,y:(("✗✓")[(y).hardcoded],(y).name,x)))))

(BOOTSTRAP_GLOBALS:=(globals()).copy())

TP_CACHE.update({'Libraries/peggle3/rgx_golfatron.☾':strd('c$}?S|8E?{7609T#j<Lonajko9aTuDZqpE(HiD8UF%r`Dx?11uIhWk+9(!k4%UB{NUnmJ`N$m)lmIe@tl>~%ZKu{&(hxt$VOZwiMFFSj?c3jH+;M?1odGp?9KJU$E#!P-9|04I>0UO4nwO;HMqSb<TAIQD7ye{uB_#F2NkMlvF$*b~1`7J91ws4*dCkej$yZne1oO6)`zdyIk<PMC!E5OKy@@nu(mL{BWwi>MF8wnU^Oqu8N>&cWcKk>QP+UE3`>m_{;n*R(F!`EH8C$5kM(F?%r$MU+!^#gCudGHzZJ$A)Qv#B>oJvBtPnAV;*n0S>j=94GWjXcG+@8u2lVhrJM+rd7dBe&&O?VzU`F>0?}Z`Ka;`EfR8SGekIeaz7dbhG9Olh@>X=P&-wj2GtjmGUv?Vv<Y;(`2N2zqG=ZbSpeAmX8ZuJuk1k%uaG1p6rxvm~hG8IfA-3m|V^VX|$ea8{<i&*ODB0s9n^*+QC*!J#BLv6!GCRi~K`gg$3Wt=gBC0Bhg)FKp{M+pXUrMm*sEr33G;MgxZ<`XHKswv;Sg-ywLEa{A)W@-vYjN<yVY%IA>cegl<=UB)>Pl@og>?SsB;sg`f<xF3`F3=gmulVPd$iTnLMfP+;*HPO$>qGkqG^q=PHUsQOv%QLfwoAXy#AVLL#NAWLrp98C52T(1X=g499EnFtQ0)UbTqQlmx7gf#4M;bPQ?Y&ADE%y}^68sV$*2l*fEq5!uMW5W68qpzL<{oIugG#-0itL4eZYV?^`FEF+!u&m(kf5`9TP4xAte8;YuAOrX12Yha>giG7rk@w_7C{1DO_$kK!u(7c4{0sDV`K@2f|M>Qw{@6az@xcaGyBUCJ?#e5L(w#O_KULXN?{pI<8Xn4MR@&12n2#R)@{G^*GGP5Qb2zldk6>u_zI->$M?g;tcDMj*uAA~Wtu!rmoV8fw_<~ACzFtJocLKY>C^+d<VWj3~@;$(>;9d}T22>d9#c5BI^4xha?)}QPj=0;b=JFsTaI@g_G}EBUbYr>D$P^Hku<^R}qo4?B+09zhhDDEN!&)K~&1%eaFGQC20GL;Q`&xA7!piB@6$smZ!ABVH%g3<HL5P_8EqFy67c~F)?ml*C>{sdb0NWc#1z(@bT}E8~7C3KKS%IX?G>t^kU6XtArrbA!_kk07bsSrF6id)+dXVqP8}gB|OK-ZDaw64t@=N%pW!CjZ!w<=FYywGfjHzA+@fhMfHaT%@qI(*cskK};AXp_QR5N2IyhTtVm0l!F4D&QF-me31Wb}!3=Lg%t8BZTnF9Hhzl6x(l47#o!x=hNYJrjv0&LjEM5a%*yA*dS`+7vN!o9MuGl2P_Ic?d+{RC-+(A>AAfW5~0Gjcl8;#{9QvsT7}atGH*}g0J`GUGi<KRcwQ)28PuD^cJ}z$%a|Fo=m1ue^5XQOg8#~N<*9dG%Zr<8$?%4Ozf=eq?#)WRTWUF8jB5?t=kc>>b7~7cFY}s?IwQxTi!17)R5FI6>QKB>gxvKaCR1vyyono<QZoF$B=nNI2jJQ31Clhwj*FAo>Aw+LC1S8@N9)g_u(C%6%0DavsI~3+3`#YpXExmjpKZhL{K!N?j_Kg70K{ySw%vuoCFO{vuK(pNrU(>Wg232D4_dcIfl)<-clAOHm>hClV|QTcKVBuhm0xgA^9hss+J%p=#{FR^q#9aFahR{b>=gt)7T6dD+An>O9q)+z?q$<40^;(V9muDm-`|FM~Pe(j?LMcfz{9Fq?dICZ?QTbO%N<BlvRMyu8`j9spc8gV)lIV+ejlvRbfq6J~-HyxGw?jOC4J<Nq1Ax*^zI{n@U+U>p>IzA_mVkEv}YZ1l*^PkmEp~0UUbeq~+Cg_AO>Mi^ZDgB2<+ELW5o>QuwEQ1w)tQLtGw5aSq4a439&wOI4Vm-ch1{&B{Vuk-K6|t)-R>75;7>nZMPk)kz!T5o(*Lul(zpXP*L)Wx-$41s~4bg2L8CU+*TH&MwmVnS9Rqd^{c}X|I8vN8de~xQ(?b^@!Y}wP_h9!h<twq2p$izLn5wsZ~(W2cEM4b<-U+SSzo{g<QKz0OmB2d)mahdq+O0oHxrSRS<Mya-kMZ8^G2l@^QNnEM`vvl&O32sq#s`OhWMX>!&`~`Dir>_IN1oHw@=xJyX){8&|(<D#!|vIDu?2f7R!0x|7lKnI9=UZf=VMuX3EZFy<%KxsFB{-D}74qAuW|CIOWJ4<3?F9ayVPbI37LUnrm(vPH=w<}>ajjCTAtc5V55f0~cW6Cbb&&UZi-_=^QbiF4Y{Y(<O8(bbzK$LbWdjH*!w-8mT^(Rz_AK1HIKFtw&o6EA=`#Xqjsc{Yj~Xz%DL+j&-2HM`-=cf@(>;ZjZ>G2j_pu1(ctF2P}BE|wMe^Z$6bU-Qsb=!3PhW2k$81~A9+dKwFDMW4jedUekJr|JxmrPT;13b5;xio<RZ+{(e=2&IqIb(3*h<$SG$R3-}Ag^t2Ctf5*%H^t!NTJWt|L|mn<<u*SYkjlEdc&L3=6E21nGRLob@(X4Z!_4t3ty7T3yA<qH5ou<VrHmD3%<uZ#`I&mhy^Pb{SUjEPKkaVJe9VS7lNpS;sa-iMSL=h8PlqR`F1G5liHPjUTNNo?JG?ml7}Du;_Ift#$J0DZX@A|5*Uc4YzZ-WiC5^Xh#xJ9Ab;f=zubYfL$!nLvE$6_EbgL}T`*Ig~8J3q*iX--?+g;y`ngcpFdeP}FfKI9j|8@>Lkk8(4h{oIaMjV{WHnU?s<HpTtt_&p6^V6>2sGe2NqMX~C2p~li;keVw%hAef=g(bOy%<GoeVDDmaE2W#Ebv9;Ck)3T6Gdq}N}@<rnJ5~?fKOzL4aD$3{<BIa_3x!yGbeViH}_vLTwhx'),'Libraries/text_format.☾':strd('c$~#MYi}DzlHc_!1_K!AQ953dvNo|2X3wvj59d7xwhsxw5ClbzByK25N75&1*9+LPX*=teY)OtCJKiXM<Y7mbwPVT87)bws{SBF4uz>%-)uVf+hcnb8xWft<_DnyjtE#K2tEyY==BzU^;J{yPa(b%ScBU&$Kj)NNPSdAqacJMa?)#{8;NNzS<b_MEuICN-or*u*cGR-Epgza$Y98KSFsOD2)B@b}$Ni24I0>A3AaHD2cY+vL{8%5XfjKZx8?zdneBOyjV#rm0j4>4-$U&I!vN|UR`DMwACKpYB-1NQem8r?;THUvL|Do2-A88)-qhX#k%-as_B{M2&Y5MJ>&4$xtJpFnKqJ}+NLR7=;gKIco-D&?{=Nu5Ytm^wpxiaAcQ|sl)(Q4UIr`6rWkP$Vf?y5y0)H(HoS{}*MppwAOo+r)N#4uq-c(pNjol{TLWuZ=}YwDp0C!A9&Y5}^c+v+dsnc!~^M^MjIT_XYJf?D-Fzuxji)`LI6^Ld{0u9MB=cIY<7$`c8~@ozwk)f&~3->Q^a{(rTAaA^Eo-5bd>gT-MK-H$uj-5(##WQO+?#P3G<t@_40xp%_X#LKbFvBJ=f;!bb!SmEPNCJRrl=-P8O{0>OqM7bHx<qCklt>q1F|DET0+r(i>y#b^1>Xp@tI=x}_*gulDR!@{l6SeV)Iy`N^St=2XE-?Ei>hvJq8M;hX>P_s_oJ2;%o7E}xmp%V^NQfcn$v^#Bk~FoBj>;I{B(2SD32XCGog|#9Q|)GLG7iiva!1bQhchS-okFW#tN7wSrW(E!v(B3iEM?Jo0|Y)eeh>LYqCzkLf0UlDU=)Bop>C?{q60mg_ncY1)*a2@@uTHtH9q(65AN+1GLpa*Y5_7A)phk0#p;?mk<WT4Zm(DXZ>jE{T}O=IwWjM}I@+{)Q}wB4E0Xw*0cpmbQeUW5wG3qDiW220vkPdFAyc!=RC{$a59Oc%5@S)$E6QeWqK;%n0L|ZksMi`kNO20Wz-*@Ugu1U@8alPO!;<>tW@Un?M!ssblf+1Xyq%~P(Tu2%NZk{4#xO?ECb8@s<K5z0&nTc)VL}k3#&5JE1JjYUe9o{<8v|g)30RC%JtRmfu3+b9>ZyoTqJk6cAOaF7tvQ1rLXN?dEk_MIUshd>SFM+c1ELLN+PKY*n3Y^sXJAf}ew6%jz22k65+<JYBvWGa){<HaY-HV7<49~HG&_<P!Io(Y8kKQqy-Q8&Jf|M13uc`&wmfU|X(5L)8Mn6)JJ&%CzELW9X>nId=mzu{8_!2Nv_lp$o%i1_dU7;Toyio<4u=}fX16f(HrUy1t;uaIG<aH2#>Q=>81hiL-a*akNWIOYXV7PBNw4NYgUvBrMch>8)RH=xFaw25QHIK+B|-}m*?JTxsk>&2v^$*wKzG$O3sgsH<8FZ<OSGuIPVYtxW_}ZuxVfdOd)xxu5;5|IK}EpQIshi*9O>+>2r_zBdh{X-)Vw-x#Hlbg4hvZHL{r+zLfuZQ%cfh$6SKr9tB(+c4%XptwC%G!E6Lu@j-8XPu^%u3rt1J3*BddE7_t5gnOOIT*|U-yhK=WY`yCqq(UgF)E{PTZ82D737Vnqg!;AmPb;T7$3%psgYTD)NBlv@TL|<=!OJD#_g$4t()HB9nhv#{b+!s(!Wwg_6fSqOjjTvpq^xc@@6Ey?>Vr|}JTc*oZLCBqE9M5oZHcxgQKd!15`B1R6A;GQogTwn1J_JMZWLotZ+7|@u1T^~J_lb;$cuCzHtIrnohQ4>-0rW$mg5x-F;p@(Oc}Igx_~ncNd*6)eC3S)wQ0NbyP+c!7LSpJjaN-2ojy^*~=Ltc<4#*5LQCAXHCIu^8h4Z3-zB&Tg=H$Ex62R7s1EuB;zxhq9N8h=!DG2xA89}$W!Yg?21K_oGI%qw$s@U2Sbp)HXtreX8^!3^gKfPXi@;pmh2caVSOIOQ?*GyjBmlN=#Q3gUx?4jk4H$f{7<%W?wZ<?Bl9$w5iH3*;Y+rwtqcK6+@LvfGo)je=0l5i(LMD>22h6>DgLwzqMk`#E`Vej@ERe=(KdWC+}j5E~)SpmZ}h_k)v^uSJsK9k0uep@n?D7n_8Z#uoo8Ceo9g|N6@C6~C>E>}KjQXF_yeHX2*XiQOp11g;qg`mjBR#Pp38jKVXadB%gD7er4SPO3jS#mH!FQcyoi8u{#ynZ^{V@Xm5zL%zdnju=sV(htZGd47Pp>#tBGSuO8LWsCfAgYE_K$BB$R2@r0?Phx*nqI3ja|Fc?Q#l^J^)zTh(9aqIn#Qc0L6no?qW7_LfX18%w?c5#j6Sjic)~UjU?6(X)|(QP53HafMGQx$Iwb=Jd}HuLhBL!E$6yN^t&QiIoDqxfAXwJSq2q^NUDz(tH#S-wG?zSx%w)#11}~^37R!y|(6MoQnUjm0)ysuS1Ozx~OQ9zO<t_kELNkv@@&`9kek4WHbl3_O(JV=h+=?6OI~WyQTn;XN6<oX>9RD=9cqh1cH@J9Dd$bFf<^c^onB2<uY<3q1qSAIr6dKEI6o|><d6x)^YN779t7W50q+`{*g`Vu^l>yd(1%pGg2XA{!D4|6`_Rhb!x%sbI^ILg|4Riz0T(&l)aFU#4_E}!O{3D?+8YrMyu;ikHn-m9&h{PYGPfGX9GI@<+EF>Qwg&A+wsvJks0IeGsb7Q`)KsyG)NM<+mPJ|*X3WLavr5}T(Rp3dm^cdIx3=0;aW(}4E7B5(Q5G>9Gi+6&>o5A7>7o($uifB1x<=CtOMVhBYy2H{&=5I4Ok2DwE*rlGpo_!N5FA|BlT+i9)Xp6>Kk&dk%k!s{XHFB&P;(&HudNs2XIV@Bf+CS{K{rAJFe_)Y`2NrA$y5c~{=l%b8bM*u<I7vu9B?r1ulGG*c|IO9XV3LY@(pM&CIYD7c&e7ncW@8EtWcfRVknCb1#HuJiv_JM+oxBu@Gp1Y5HP<Ue9kz?QSBFEOnWWvE*p%JGyt$Sunvg6=+<ITb<UcV*fK&MfCVr*)p5bpVo;e_uFT~CbK*sJTR0gvak1<)nFXya`VLX*fIghJeI0DzBFpGKUcbyqbCV|;{*O@>Mt;o(PnNx62d$|Zg^r2UnEqb08<p5JmX`fuPuBK#5xG>o5rFs}DXnZUQTE4&J=s?coW&!g#*SO9M?|@{rNlQo*w#I@*DN=bjZk|Qlh$XhLaP<;rLF5Gqlh5nOcxKsT8~de{K|B*6$$g631eB#5OES!tl;zzAKiW{5(d~=pgw4!WvVUU(PT32)hT{eRgQ&2lhKE<2PvXpVBBx;|x#Kog%xaSCY&OhU`R8Ju`4uQP|G6k<w~8|MooSY*(~r8ew^Yr)osrXdu_HW}h!d2$O(jlhQi5TK?5g4ZWF172Hm5R2Skbnj1Ktf8LQET<^NJ^{a+<_$kd8(`Bda<sDdL%q*jW_wq;a&*>7QoFWIiifd2(tlpw+vCW^^QJ#cU5$pF5*I@+KYzBy2n%h~9%^qy->*e6r}tNy=57R8QGXFQ`l5-Yz%bnch1rTm8T+PTjM(O7nTL#oo4~BOc?9*{teeVkAym<eibO-$v3EE~j1!<F-!%US?GXL~CMdrc{}#`nJwh^Vv*h1Z-o73$A;<$}?K~ggZ9wjtF;WcG&e&eP2ydyVkD9W-z9^lGi(GpJgwg1*6c$p}?jSu~eU}$chf2uA|#v10gF=5nBJleIdLgP_)-!J--+N2fa*M78!R-;AN+n%+b*~|0Gz2KMf9wYOT_a4uA^LX*tN06-&^5&zT_*(bIff`5523{QiWC7hF8#;uRN<xcHHaRW6>gZ}SKpbbR?y9Y=6yxb>N7eU9H(u#G!i;`ZmJ{e@{b#|<w{!%H4`!nDtshF9D$XBtkLmwEGY%Dh}QFIUhAkk>J<?n&~k&mp!?vHqdd=gnW5mu2(v6~C;Qnw6;Lj(NFjUhbKfug%Lh=H)g!gr9S9hl}glOXOmii*LF3Mn_xv@QjNaT&$pg{W5<qm_Hsoxbymlm9xRs<)2>$-G!fD1l^^edp+pR2i+S%_j1s^5_A`X?$y_8s}JE>`}wD!`x(4E3c5F6udSU9y4T?AM|hnJx}U@A<DmNm6i?w<4Z63Wcm|DUpnMMHS$IDE`|;q^nc(a#wet5<uh*VkfafASmtL>^?OS-hgXaM}-@~&4&;P*l13dTt@x|pU@Z5ywGCY^yxem`VJYW8@I1j~DcoyKH>lxmky~qm$d5_}Sq~EU|#DY=Vx8Dz2E7?X;nRO!14LnZU2t~f{*w_%^3Wh`$ig-omExOP1*52T+t1df;dk+3S#X&sK>mNehp;%pxl1cG?LsS><w*%{T9r`d<Ih^Kjh7p?(;hm>>bzZ#?q<dEd<w%b?X^q#Y(K8P7buZ0@W^d@cdYO8_b)hGfo#qr{T88pR*NNE+>PuaI4Ng<)<-;*b0W};Hk*L}Vkf5Q^DTXb{%ZFgkTP+SQkLc)r6$61VIe7$gO6}QcKbe69W_G;orBb6j>6c19=O;8yhl0sWpDj?ZTiyIDxVhkZg(G-^oyV;yGnR2FYB^&3$+1kvO`MA8X?jnN(xwUTHqjJrj&2k5!}(U~kp<o1q2`c9DPwQ+9jiCQJGcd~@(z3JL0U=4`nua%d}%|A@ohQ`x5wz?yL3T1LQZ*)K3kWoIx@`@6WQO!GN3uh&K?3IZVnCM;>eyOtMGaYne~3eY(UUAn;>Y<0ohANdUx~_$<f(!XdPrhiGL-s*SCsndXB-q?PgufOd$tsADLiK#9G^*Yzc33B!WHql_V~2g2dfhUXR`DA-kX+ZNd7)b*@7RmDB1;<SM6Jp^e9}91ubAwfbv6I)(T|cQ>(-_=N8n03bX<)BY$XulPiV+4c$YC%i2yjpNKLWqzZPE0u6_*tK_WY2Qa596WU7aH%B5>r<oUIxI0TjqkX*l1r>f+!AwBFIBqacDs@a{N}rZuH+JHFer5;{^A#AYFvrG`l~`;75&wuucrQL(HFtxlTTNlfMU()RL7O@gYOUsxe|Ve7P|W_sle~>j<zeqSFFb)3s>T=p#!2QrUYJ0-Aq_HqigxntSh-B+)RW9=$Tid9AhdV9Si)9#~*HQJYx5t((OrYP!G%4x-rwM$EQe_yN<e`EW3CS>WRJ{*!Ej`k;kT*ljXM1x?<#)6_GLxqG#jv$H!fS$$KlB_;~w_4}a8y_hU~Edr{WYo+XTot#6ERX%44Vu9vG0e2@A~r#<7>|J!!}*>(eL7P^d?UF`|qsh3-Ar#(??j61VaN3lNlR@Ip)H`>lr1FM?O=+Wjl;gQWrF%(@#)oJ-M9UkEPAZ9T4AEtuu?*?bj`sJ37fn~WhRjZa;RVFJOHX07Y_<YmDDm}9e!>C{8AOHN&>Qn6jozh3Q>ze{);BOfx9mSst{#5Y?mtj;^FjZuaLcI(ZGMkk;^xvqHlhUQK<u2({VW;}hI(Eve-w7-QlGfQ;S6m-jm2%nj)*ZD0HO(z|v8Tc_n|^2LSJi!e7}I;sumqJSt<G80C{C)|2Q#4)Ft5JiyWraMDvwrVcwrpm|1Az92rK~0W~@`HzV3x(7Q$!_AnxQuWBSd22~MSai|JuKJ&gLt7oR=1q<uV;_6Xw%w%Bpj@@6B((`zML9$paow<fdA^CizxX|h~vluF_M?&x5x*Al|u{{^7EUDN'),'Libraries/peggle3/main.☾':strd('c%02V+m0K@mGAnB27@fBIPJj<$BwdexXM_!1d=6XG=TyzT!JE-BPP71*&|V~Wyp#o$FZ|ktc#P_R^)gUDUMe1t^==aSTW!R{1<u1e86IX{eeA~s_Lq~kQ{3tmVk!cbvgGs=hUg9y5VTxwY%M(*BgvSVdNb;^!+^|z8wGZ#L4f8W)q*j|NM#L8=K9h5Tz)XM$PUh9JHd6^tbw>)2;qQNMDpnQc9oZ9X}yfq^t|^l(*_h*#L0w#n<Bd)tczH2B$kMZ|axJ(Dv*2X7%~w2N2uM_)qa;AKHEszg&wi!Pjr4h_A$N3ivE}Q-IU!iuh&d_*hJR?2$6)PXcUvC;qLNBKn|4;4T5=TN>E0(J+ugip|<)xE%muAsDq>-U=dMDF8-ZxFB&p0@)*mM9-V?=Yxb|-BcBd8KGNj!gQOjsPbO)h?px<6Kf^`qE68DnAKz=0RNZx9a-Ju!N)XLYY9yj3>wtydImjB_8GVIMj?{@Zv07n6}zs-A8YUmK7PU=+75??KWf)-)$CUcV3c|?RW(;@q$i@`eZQ<xB#?|XsR?qq+Y2XAbJFVs6M-5tQoa;FjIUSW>jtnR_*E_kU|wUiFVqnX28;;t$U(5P`bq=ZLZ@l9p-l0>!J}eTVuKM?-|J00vWW#`U{S7xz8okk$5x^$c?HuFeH^hou21^Cb|4UuUy(o}_JvMg#V0Zv$kZf=T2T}V%|t~(g~!$8am8Y54cJ;^w$kLYVZ9gsD*nq88dk1dEoeK=R6*qY3D*NYyeAzq+KrIGCT_=9_OEXmstEFv$`DtlmqU{w$)YE4=(!fZ9)B(p+XfA{N8|HPN>ILLS&si6|CPV9{>f**`WmjGyYUSa*S+}n;<@8L!pE26Uy1mE6rxkDC4xKzE*zFvBK;Fc(j{2=4|!GpM|y#ZajVnj<@vg(b7KP*sfUv3z{Adsi}2_zd7|{=>B>5-U3R;#@hY|)Aux3{zFe*4JAxTRz^8P!gjiG%c{lzzexUvS>bInB`#0@LBsuF$v-eM4<(X%+i#9{8M<5bHBnXYQ4KY$RfwEz>Syl-QZ?CMZtVid^0j|UC;iR`U3_4!>Oe^%Zd&B74&FI;JG0^MLn6*k~&?E}C+mSbJhe4&;9(4liF@NaaZ(Q@RWAAesuUDQtYv6nRXSw?Tj?4$KvE2`B7&I@kV6>0gFB|YO?2U$M3K9Sa6FSRYXmEB~k$FZm`2;-QirQx~6!bd&*az~RLFFSBDZ?WMIQ1&%^j!AFtq?SgSj*mjzx%tF{bVA(!oRnC5+6Lh?mKwB)1y(}i^A6Aj8s5v{@}3{1<f$n3Z?=foY12n%RoCvyXp5%+w0FVp7=vZxjMbD*@Q&|!^XkZRzFx<o{TuXVh`-I<#qa_aWF)H$DGuP*IANc@#tZ2&cZZhVlsnuUeX59iitl62DKN;Dz?iDK5D0C8#}OAHk_&8G68BP;0T8(5*V``b)Wh+($C%N&}}G!UN+5o1Her57{Du+Tb+(rm$oBJ<{=@zSoh=i<6p*~0XmquM}(l!jYJlaA68$0oV6sY5y-QHIV(1V@P$f%#cQi8;Vbl!f66T`TtERM;FC7sNloWFTFQBdCh(O&ofxPW%rpc2unoO^w6@~6H{eem`1VnFXdlI=4Sd>gp=~setv`Q|4D7S`Q?cr=u5k0_#>wy5&8yse=;%5k=V=h3c_8$CS9!Z`yVX7uuw870tw9s%Z4RKZHw@6L--`d$9}Ze$lU-bbnV(m6GX6VGKPa<jb@3eVuv*`s>bw9z=J`f^yGps>T?k|v0AZjgrG#5oLm>>Q&gIq^mPbeXd;(~aKjZ5OC?gYAj&aQn`6>>WcY}*!d@l+HyN>ak%o6jItzC`p3X;)9KdhzFQzx6k5fuDyTO+I`Qs*%Z(>DW5I-fJ!3F`N1H3;83?_4j*)EGN8LBf@uKZx%bJ#$hf^n5>*4ulNK5H&L#Md{Q$Nyvz%YOM|+Fa7~t4)f{4O{H;Z*`SeX0X6ao%1HrfJZ?PT36hq~?t^!fH{yFv4=4Gnl;m5Pe$KYU5<7s0Bml(zKObKG%g&vTGor_FdLZkE26?SvCoRM|N<-cJ;$8{)B5eFb>hh%)?`*{}AwRFyn0*vRo-G+#8BH-=^|H_l0l)%kA_Jxu=n6lydR~h^jNj9W%7V{WzOeS^yq0jYta^bB)&az}um1SeeM(-lKy7)_yv&FqHWNI4c~)*qs`YgeYE>DuyGrqpIJG3Pz=13tsdI2dZ5t=qWwC(My0Q0Ps3iqGS6hYVo#$0FA`JVX0wouKMQU0InxEL|0&w^3JiPtogRkzByIBajEgHsyiP2rT2)3n}IK;48V_dwneZ6=KaauiKO8eC6CW{(Mxj0?rIlMD$2iX#PXC>*yQ2|Fgzqp^lC)mPrQe0RjEFBS2j2B6Ifg4TO7_Lh6JV`Uqq?d^jq|)6~*|8|=U220?9KX<nskGNgrU;^@<Es3^AXCgI(?C$4##edEZI#Gi_WSWAGxt(_J$^%|G|4NMJ=nC9kT1rsD1p+nE_$t=4{9i%g&@!y>ZvM&agzv$3_|tPdku7R7%QAL1li<h81;tRK{gJawGyJsz#OnAl6dFmZQmV#rP2*9;+?f)WfB!D5EUzKR74ujdMTUGROZC(uJYtJ<5zuUUSuyf<6Cn?<cNvwauESJLdv9$M2M9-YKn>-zsgjXyt8)Zis}MW?&VY|6mL(Ejk;2FN>9WOmlT2Xvq2a&aSx!={sRY}`{Cgln{!fI)U0EYpI5m{tcGj#f^32(%ry*95n-*`iwcWeqI4n*p2E$^q*}7qoLXE=apFbJSItDv`{twy|4Q<kur)sKo2AYyMWZG-;Qc?`NbgVR>&>cC5x-$Q8WT-ti(j~~AKDAs2t)6SU^6>=$0g^AWHgCp$b<>nkY7hEXcOH*1P&;Zd5OVTZT|?5*%tg+ibA3A8si|qu@|xg9e%Si@{83`*BR0(tRilsBu8eQS}M7}UXa|U)BfEh_ads+24i0O*R34c1i<T@AA<mjqAe95M5Mx%lW7-%E6$3jPBI6YHS{nHo$IjBK_$h59@Ru|SlO!1{@H(JreX2H_`4hNC&@f}hm*|tj+d$>IF1onl8JYG(_PNI9BRkF=CB4xrKik-0LwPZaM&8)1ULD`HE66+uVr^f-}ZZ*8m2^pR&Q8h_Vf$J6@se>r)Q$u4}-zzY|x}4V=&=!%TvvMFyzOB^vG5FQ_XIx*H<qG`Gp2$9W!wvtP@()kv`PGKu1$NEl9Pghit_<mc1-30H7P5LQ!%s?gxWl7zLe@yVOF=+_2cjRaX+euG`Uzq`H`BOG;jih<hC${cc(u*<^}8$=dUoYdi)77D-y>^i}ija8I(;hH1e;LGo!LTi<LnDEoPMXv{1`()A7~*)W~_U<aeaU8@3`Q!**gby%oiT6>pq>?xZY(g>|3TlI%vK+y4`5m(b)r8}O)@+Ns@7F<b>>|ojE0@o`kS&$-`V^mjalTc*Xc<9=9Hvxc77F)S3gv4_4WpMHg-k2c%Js7(coq=Ha9gdetrP6j8kL-hCqD?joyLwf$rSC}73M8XuyEv~PX0FArYgSgI9$-W|BWfmzXF~cza-A|aM=?~PyXyqw<Nz_ff5WZNqnx`G`4PoF4lzfPN6aZBU{YsuU&OE2Lxx8(Cde}X1E5C1)vdwfhR;oQ8=hAtuYHW^ImI_Kpx2=|D?|mozgUADReDdso^wX!jZfv<$_kh~a(ny)E<iu03!94}ugpizw`z1@HXm7T6&2H%6bb*}iI+S+Lh#bU*9xGlYNH-CGW9_%(<mFw^XqL^hBKq|Glz8!w2@kN3o0XDP_B0D+^eW;z6-i?^|V_$zRK29c1Z?mU3tk*;$NFwfKLRAl0toRhYAHZ<Hu6E+dp$B<p%p=zn(}xQAFa3BHZ52<2~1C7vZ!#len2!GmVZ47BJE$bqx7xpJjf#^#=JEW*C->;Qx>P%r4M7FWEAkGej5iog-rkOprE&c6~8hP=S2`ms7TaVG!c!Gw$%IrlKn-`_a#;qZmFvHSsptxaJCOZglr`P&elaQt!N%%KOx*6Q6m&o_MmrO*>zlaGEOEbkb>B!=@iNO;2OfrqlEcHXU%9zJ*PPoTj}6cl%}w#vCLU3Me^h&TUQ!%#^B8O6yrE9bf1^Vp3yMMub-eA}|TuN8#Opb?0KyDKLj0*tPa`aU7c4qXCY`3V$i+51J!YE=kRk{z+*K0oeT9D!CwMVnojG(?yLO488$q<7!#Beo{)4zW}~_MflvdbE?f?vWbA#D$1&<si5W(_3JiGWhs|8yQ#kO=*rHct2?(o+PU?3=jwlA{UFSpm5b9n5yo*CbbHehk8MrxCRj80S)aylg`@2;J;4T<zC#RJO!s8FOB3<go<~sCxOtq^=IC<7;1wMydlWM!(~M?s2re!~h2(oa=`mH?E)4PlJJtdrox;<qmQh7NtTEwQxYe|!oy)EzN5kX^-+gQ6;cfDVFMau-P|4CiQD}-<M=AVst-fAf+Q$eHdM@w+gd_}m4@LJ8D-}`yXMWhZ_IBe%__Hj_+`xQk@nxs()l>JTr|z|;uBE2#T>KQ~?OgoKngnlphO$p*3JiDG6)Hi<eXNJ&DrsWpowt_CwJ#rl9|G6#(l`F=!5;w?lf(RYKc24qBi=ei%u6rA1dY^qN*67F_(lVGgei@(9(yh|O4JE1v4SJzk{)>~e<XoRjlSU9XDE1MO~-!P)PE4)(P_hXF<elvTJ`bg3H~@7P0u&mXIi~s&}p_?{r;pm-VOt_gU9jD`F57NE+`J?l>ab+)7a>WL*^R1388vea(1(lx$vCHUgQ%VKba`5E~Y0UJ?vX_+a=j%7z|qD35}(q1W&&k{|49B+wlk5k?dT2l|m7GTTVy6mDG9qeTwS$DB_rWYjZRAM<8O!ym_jwYu{d9-ZW)yuEYE8g!GJvlj@hO`nc6eKORV0Pzumk1cXl!%#UNJKBP0|%}tqnn89GuZjA%`bUmtx(%(MAJCZ_7<#HH|`z_d$V5I@K7T4ZJfk8%{^l+oElKP|rZ!7Y6t1=!2o$Yqe{7GKDDCgciaQH_2`)rCe$|j;P@J=Qd1=;P-IlEa~{9@Mr>TdQ1RHqpkZGamqI)%|&FTThDOyZwA^pwC=g&zyxqpNcPVv3fAen+<~<#aM?5(9qEz<%qauYsLk$}<o%*K>Kl_4sRJ&kAA|Ju>N{o$*YCTv<%R^TnUyf8MPTTurB2oxFvVsut2M2ICV|90dP&4*s1gW$w2r^6^-rz`*&$$ibkG=u{z3_n?qglM|F=Mw|Q?`O2bBb@@U_-fvZFyCBs_s6FcUAxZ?z)@T7qAwBuJw14H~2xR7uh1&Lyg|<?^2y&xhGA^fHqRRl5OV@WOjOSJkyUl@tKGSN==AZ5`vEdpLEghO;R&&Tfc4L@Hw!PLscA9uFL&sR^Dy7rGhO1&yeX7o8Ge3}8OT<yh&ljGSSUO18VI0*Mz0<J_Zob5^++UkPL_UUzko1p%!}sa6((rgspC5CEi^ZJcivW&-F_C)PxiNi93ibx6<d2TTKT@e4##G3Nb(w~K5xJVBwO?7N27w>EGBv`hQKH;m^~>ZV%l*tz0<n*tYlK$_3#($o>`A+D@)yVt1_JyRSYkH{$4RcnyESl0*4Eb8Hv7yeW<D|h0$2Smm`s`gnQd}v5~oCZ8YevFXT|0&hyJ~?Y&bBjL{lB|r{P;8>O>$`l<VTWM7f?vxlU<ClE;K*@-ZIc;iF%`)o(?@UdU4uUv&L|Y3dC-1>@`*K$6}m4I~*dyAM8vw*i4Pcr{GPgf#%VPWRK~_j<?<pW3@?N@eXJR@>j$N_TbbP-_t~CF?Dc3bSj+GIU87U&Z8|b9@q%6N#oe1lfk7Yce_+H5g4dbQ%wm>ea;+%MO%9PC0C4&hay`*z%<_!)E#@HQ63nn}Hc2NnNneuRl#5H<Lp8|H;-(t$yc{AX^#lMd>eWdHKH-SU+%}dGJU0-wK>;HiiBF2&g@5$yX0aThb)={4auTwqX'),'Libraries/peggle3/gram_tools.☾':strd('c%0o@>u(g-760zPVmcDiz2;)=+Nmn7I;|*B6*VaqI8vp}cC=oPmlgZc%(z+7hhpQH3a1IU1{ve<Xa!Ab#G^F`qL_TRAN!$yL;NqKe?ZT<uetMB<438~tS~!s=H7G9`~2>mC6g78@I`)Q^4!me@8i|!cP7uAo$`G`+<wq(wu1?mvSzzCU2jK(GUB?FQYPk{nIt7jtAreL$_}M9Ix?JB*c|xHUVFA4hrRBeIqt$R4hFG5+Y3AO_yFt(nWSU<9{(eM%3sNErbt)$=i;&pW3TfS{#8dlS>S8@CNuN4U=c#nEGnMh|MOF@Y_(K_0g_*eUPgMtJoRi`%n>W4=o5+;ESsXgRa2^-JoPpyQ)E7Z<37Q0q+Rb!&(xg(8wJuezRX7D#r4WNXHF6!!54g+0d0-XdvaMy_(yz&<mXT(31HljnPAp|;g9$x(Rwhk>ISWhIPfv#ikE0=h`<2{wSdVytod9@yusjZ10;|v@Dm2{T-bH=JV7^87x`!W1;1=2gV@$o9Pt-^g?~v>g6WT<f-%K6I?Fr{+EL)7hZhNAgfS8=@KyeT=mp0Dh{Zkx;~w-$;?me?EKos=RKdsG!a}$CM<<R?5o<9z)~`nGRwE$4=yd}&PHXT-Sro+eI1Y&pnsLPjF3ZVf$qJ(hit#p5ByZyQhu;;)TgB_U;{S1m5%4DczsA=N<Ny6>OGb^Fn5IRVQf7@wJX(|#^o`i0H#-YVeURV=f1EPS4Zf{R0}&!sb6Q;|rFjw{`?L&6j{{{(HRq_KmSy?JW$W=_4I%!62JAFIp=6;%nY2+F+8W8^*P8OBXsm}dDb9EV?J#2udSI(dj<&63v)2!x!?$LWQ4|Y`^)Q)L7U8I$j1S{CVe=c$@SDi;`=9zX@z7rV+irCOKdg6~K_pdpoc5_C-i87_&%cH$ZdE%q963ZFuS{%XFs3hs9RUp0m}~?|*C9z~fF-Eoc`z<lo~ss5V_1C!zK~|hbcxr`y)B$NN<{1XJJ@ZLXoMzO>YteCY|r?|`eM1FgKb*{n;Jlcf~>^kL~yxMN!g^#bP>dYhk=yV`<R-YQAs+e;m18cY-CdIamqb+5_Bm=sEE<`p)Uw%c@>qAu(CvnQt!mOXLB0k*Gh$`Awn(GQ;<a{YYmAChau5mTutrBv+{X1>=S;8FY!%gWYDb&c;4r$WPfF#naQzqVp+|45m3PjHcX{}8Ds<*R5HfY79#_2l{9!&l4=-4U=0P}SHT#o5<Wfkgw!uUYULw_g9<pm;Mddw)cKL;45<F(>c&K((|B>+c#GmDge480O@(s->-J)Q%KIto$O0;(Dh`9dmwUEWyB*AA!;AGj;yMN`nJ|;tl2t>fzrg>-?^?STREYHHeq%*onk9a}sMHa`eWBu6kShs}SeGI*9?K?avxo)Ql1Q%B-C?;dl*6YwZlv4WwIq~eawBsqyo7*N(uPPWKm)X9;~x^hs0fP!y1EqyorATAH1y46Sy9yKctf$KkSEx?AX4n6fpPlCcv2cq5^<0J-k@|Gf<?ww7~na8-|t1OxYg@M|JS99L={;0wUOEFb=$p0z3oJX^#1u)JJ22DPBp4o2u0iiJaB$k7$w7kFtW;D5)-n$GL*C^P+;2uJvbdGCOKMcAW|df&UJ#Y9tTET72FEZXCx9xZy*&K2t}ZB6~Nofw3IS?Lw8XDY=&izIks6r`4&hL4Z+yQoPn&<heKlaXF3e(7n~Hi*uozSL2dXE!Sn$w$l)aGuoI?(E~)M^-LQcBn&zMHwS&l?u1Bp#cG(1;LzeGz*E8D+qu7sHGf+AUDvH=^Key_N+G~r%1M;V$cVrLaKIM0_M{&91vsA=kFgmSB$d5d!Q}50=f{`YRcpa8M``F+j_reV;Q;+W!Z+-t8LAE#CKiuz)-9SHShV_mg_N}^$ne-19vW|y6Kz8$azL}gwb|{h6c!^&#9bU{*&}SKn=7M?hkdlyz*nL1!2hEbWN-eC#E>;Y9`hqWN9s^bDKPJ_S5G}BqaF3vqE~-rxlZWB@^fL@Py<Z2?2$^=XuG>w=h7Dr9oBSmy1~kP~-F`|6)T}`tc?I7$`Q>5l$aEvqh!jceNEU#>Wld1KMWUppOrff4{D!tlnG(~NAOz<tUU82^u0_>&x5jBC?MQ69BE>0!6biT(*8u_Dt&B5B<FLp*=L|4F)ff}3Y2BA=HMFG7=Ad9Y0S*dG7l5PGj(V;;6NElySvG4^R$1p?5sIOt4;I$*6*AmYdBh?iAq-ZERMGCv45`-F`3+(@#~B@UB$7LQR+Md9)y!$GF7*=2iBf;o&6ivm#bfn;KL9BR2_dwsSqkYWw3R#%iFsX|hwXL(yeIx;3D!U3&-tIpE(_6o>o%?mhe57g_+=bd2*t8_6?P8jsq_xp;;01@tBb@hGs=GRJ7yP44DM}yNta3mDMX8i=BA^$zTDBw<A7DZ>8a)cISkJn$8&za^Wn=Q=iZ$>a&+gzFW;Lhl}g8*T|dCqn)j1E&+F6yu^`C&*QKZtw)!#LfDAi-_#8M=_(G0jzeQHxKhXuIbkr5O3-yyw0wQ|qyyhO^o0P%Yns65h;HD7vyts_D?Oo<i_&w|0U4=+PkOA~dWym<JN9Th`?V2F%VqqXHr%Urk9G07)E|J(X1aYPwvxZld?<#@Ow@)^1!{54#uTInBlGAlOJd=gB#sV+jIs`lcJDe6h9=G=eusXLLR<L<=NSn-@v#V2*LLSPLMCIdhQKZUknx*zFu-yTbDHkXsI&3YMG!`nbw}c|<h0v5GHC<&0!VkEEFTH#0MjqsrN)w4rK#5#r>oA@U>lX@xHa7!D!i;a9ENx-V>^!&x<3#=t^5gIAJXkzJ$LJ{1)DR@)k_tPn#CIyTmGZ@4@2I2WT$MKy)hLZihn;1K8if&^#INwd7Jr)5FjJVoWZg)4#4(U=WJLbB;P}at{;6N$4-C%vKCypMAP2g70#NX!qbpxM;$7-j04_`4s}Y~@EmyuQ+fo#e)>YvrDB_K}E8G93p*&QShl;YsZwd;&tk;w^MOib_Y$++kT7@U}E-NHw$7jZg=h*`nmt`q9N|kPxsSBhfaqZeMu1Cujpk~M$ZGRd3(g*SypA6lTxNPVnoM)ZPxy-u3XX*glW$FTH+2c!>WhrW75C^br72?Oe9)^!9?9Ga2rEo!>W;&M4KO8mw1FXmL$|3j+(il6D_{OxX{t8Q1O=NR=+AVpt`(pj<V(V{gF<p!_L%jeIRp#og7@G6T^8ql&n&OFKg)0?QDXY$8-YTcS!~*{-zk}$Z*9pFPzVXeo75Mkhd;h-j^(**$27k}x_4ccsg@p^QIzWgDPY;&%1dpwE;J8x)*iD*R5U4(MY*I<ApCV`L9XUK78Tk(hbtXs'),'Libraries/Compiler/gram.data.☾':strd('c$}RYYi|_S^?QHCl*ZDG4G~yHs6ngc;iQTJ0U6q)-7cfGy)i5AE4%9el2tj_7(;@)W&=ikumpo4t$BuE<Fp_-Qoi;Z-#tGdMe-l$IrrShxihni9m}(OALpKP?z!iAXMO*t@t-aq?CJ5}|Md8=-jgSM-yO`C`ZD>d>+N)R{IU1o(H-#px8dEpcORtBQrQny8-Bj%;9tV|docQ<<JfWk=&>IEi2rd%FuG;~o{I(iO9ZeIhp{&XV<iq_ZwO;PS93yOM?O4hK;A4&FZ$JTw%>yK^TA&K#PRnJ8#tV-)&~5cGXo0f#K|82qfdHH7@)rVkl&v#a-c&;KJpJA`8WiK*bq1bXamt_A(JZt%wQ!`@H>un@F_7S=c~0st?C4m_nkKj*PpZb{!*a;^KNkKxm&GO1V}Mc%YBiBse!B~1`sG)tcf;q^X>>@*n7AL%y^v)TeZJZMr`hX$Do-j*RTWa;c|jx@~7h+UAPD^iSa%)eu&12UiDnn@6Y7(ezi7S&JFm4%RimzAEJ55Xe(amllBY@U_<VG=AWXm`FP?P0(I}(PhVb_S%b%n(m$Qe3<zjA2H=F+nd)Fs;+p>I%|iXT))Uc#r64R&z{ybo1!BdiU}75nIdhso!U-<l_6I=2grq?|%AcK;yBuKcLd_tZdt|s3qsTJ;nSH@1HSoM0*D%3hmTxf_4bmVY^NqM6csz%28bs@_+T!sT&G+bw_}8LB{^MD+w$TD6ejC$H<nOI4PivNmL3K2OK}PZNZ7$q1l?-Y<o%I+=M{gZPzbLxW-RK#8GGn2!7Sd8`D9o8$4JdToI$WE5rA=rAjuSk*Dfj*@eLLJC5jTcg<M|Bl5&jab&pk#BjB`_eIO8a9XLAxgz35*IjrJl`CM7LgQKLy=+D=#(TkRMHZ#e^k_mnp*>xdy%bf<zZF9gk{H1&kTg;fji)U{vs81O{UyeEOBF3vqt`%c7@PLe(_JtapW*$q1)@K>)awN6R3Xu+ESOiMuJN;e<R-)y%E=I6AZ9J6S;Tczpoa|Eaf+ai}PZ52_lblFB#U$Ic(=e|P<8yPdAtgraFTDHKQ$WEsI9LDQx0R=}C$C4n~!?`lN5m86^mv2_zEL=Npe2f4Y`ob?(3U)tJU^pazQtSp=OuU^iQ*J2r4<X7BBHLYX=XUEk1n5@2LIrRi@gc5wFu6RI6UEQ9tB|7<2Lw0QuEH}f`V=&U7ECEkFiUJOOCqj4|MS&QuApKDxoQ;=<5z_T{oH^T#{__ff{USoTbP}XUj_JDteS6dDGi<RZ9&0#g(MzaYFf54J0FTiv9eT%izTI45yU(?#Nzm6dC8G@NWU$llzJKVExJ*7TQ{TwP@1YU4Q)7X99xmhhFiEB21Ya+GxH=RuT!5d13~iAWR+IXQLxQ1H{M{*Sw|ot+>0u@yE>(mRxwjo$tw$oYE2`$rV(BvP-9F9v8rk4eZ~of5|H)_ZDNf!#2UYrSR;;@;v=EYuBFr(BsB{zBB?2jubR*GXIX|X7la@M#*Pm=983o!yJN~tzta9%O-*R`Nwt%4rdCxHuF<Tt3g>c#a;ZYgvuAa4c<`)$R^iNN3Vl=$7KaOc*@_Q<tSeo51hbtKV$ZY9P96<bLExsWqXMdErg~77036P8$MFlSA!%RAw$2+iQ1Z;h-MYh~kE?uW6mWB8<%tPEq;9kGut?;V;h?0?TX160dmc|O3<&g|ZkwK>x-cr!DWQYd1836CgN5N#y{rdOoC~Ab&y8ja8dDa<DN*6CFQX3mr+v^iFb0VI>&xc6Eo-xo*~Yu*g=|bve|tEIV@#`rtNM0|sB}QdbkS3RK<xf}2>N*#nrM;bh=R&Jb2?WY%2uigQLUiw_{2YA>N>g+Fu_#J_r{b#;gTqdiAz$TlBKv8#wM0y1Nlt2*mUJVl`Gk5w&ti?tQ2V4)6K_EoA7)K&muf`;kgITckuiRo(J$eg6ByZZ&$X!xFm%}n#qR}o8a!(ak@A?mgGPaOVV<-K~Ae+LY0M!4hhfMK58#~fXrGSUpUX~+8m6h4}v}^JS5oJg#(*wW!*3*8>5m(kC*nb@r^#qnaW_*&rwn6Vh=jZjZO=BSXCh}VaqjGL3SXUZU~ykUc4lf1e2bZ<Q!x<2e@^Ct{rL4;;-N!%Qz6ED32!CPIgMvJYb(&>pKoYDMM&jgYT=G6W4WRVLMC4bP8+SG~QwAiZ_%+lXA7vJiL7MYt`XCT^|*Brv?nQSsc#jAFMJ<Gb&<RPyCgP#%P^^ye8Gl=hY<-oe9f0gjXW8GWiG#@xh8j#<-J7jNU2*HEjBW!?h~%b7R~Zf*KpC(>env)(K&P`21Y4D3ck5nbuk+#8Royox+$pZ8~BY2$sf!`W*bzQCsz4H_cF+?xrI!45<$7=wy<SqHJkgIjhdNVao@Usy^gx!2Hkm1*^N=RNtX=YWJRW*GQ^#3|hPPVe{;#*!)9g*JlTJeUR?*MqKQsyM!~^d-z?^>-3T%)Zn9Co|{c|(a5fJQjR4}SSV%(Z6-EX9{<NpZLU0-gr}ZPVIQ8C$Ow#Ff#({H?t<pH9G-&bx*48;=OQ+~hUXvH_=fn_0E~MxCicL(Q3%)%e1FBa#3%X2C?h5{R-zWEGVPc{i8MN)lIZHN%%IJ?5U_Kw>V&y9v$Vh{0s4=KapFr8z-gAxwq4GyB3s=;h9aHqu-e>3(q{<~tM_;621vbqQy|dE`-5bc=3O6_HN)j31FD38DiI(_2aB|aH(m3BQTlGe4B;a(C0QVcH9Id;&Q8z9T#?yBj5Bo2yGM<&5`$4?qqFn06|DfeE?g8rl3m-#Zy7|^pBcXbW+ZRj`BkA>;3*gv({2c3eVGC6bG$Bd7eO;36_GE$5DHjWx{EOT4*gzy^`vm*fAyPbZzKg-2xQAx3&AF^M0pQB9w&lJ&HcfZhdYDIx7S|<%eR8LN5SN1a0Lu}^%=xQ2s_~1gXZ0!c_(-P-9@1Ja2L4li*FX1%g|{4u(`4}vr%8&sDHmPePLsIbfbP_qkeT`dUB)w!$y5>qkbJAUVs_?I12e9q-@*CQZYY!$LJ|}$-ReD^p$o!+A(c7Sh^G}T}FHO61>dHGCU8!G(gpZ=KY}g9eH~+QnWO*D3F^&J|6!^*V5JtTNYXM+fS~VAw><}nz9vkTB6?dV4J@tQGIAzxhED5aNIIpH1FyRQ&_gpGa>y^lsgJtNF1IY;aP*{-)3J>t}v^RYgh5);MnlY<^UeN`r0daUgDwQT0{JfMcm4e+q~jcS=>83@q2hvyhk>&6~mM@ovYeNtuW59Y%ghx;;*5T$QH`AbH2KjaVc{{>oJK&Y#v8fIsRa_NO_4}`Wh@MU7{%3(oWIN$(G&ZZ`+u&tKX1&UZ>jX+i{0dM7=F5LmGXdG9<aVn4}AbWWvT*uJJrZiCHOIJ9Kcy5p<g?FJ6T4srL(SMJWL#R+}M}RH|5bD&C_>m(W~7M$%n8R9Z6F1}5oZqPSS9yH#BK$vHcu2Q{e<QQTY-=tH)OpR^~jvjqViby5)kRJ8SFt2nfib8SH;vB&Nn%e=Zh8+eb@Ql+2WLZ2sAv=V3=Boo%_v|xpIXt!&^o2DPFblT**L*(~uk$m?y$?vnt%c4trr-Wr7YctYRS$t$iZ_FYQaa3B?0AyB}=>%;dTkX%3v!Qy25!P5Bvibd|GZpUoBCe&WE^9({5(l{#wt0=(+;K_KNny@>pC*sjO*%W0(o#lFP2^)6O1!PaV=~#AU6OSR1D9J-IHUf9KI!tFY7lJqRUlBBsX}Q$hYb_nlAT=;HrJQaJiwVnnIbKM;}+dosnBI+OBF*6A^DN6KI3QON(7~fe$N04JcBB@@lvuLtyJXxuRNqi(vjOqn&s8(=MG&iF)EB{`TniTx`4kj$yv;l%lUH$5{kUXup<V69Xo@S(r{VtLh|jgSI-7Wt|(_J*`i({j)m=fu$IY*iUoFbAR%8lPTo_S^t`0JX~Ds2ZRkJ(?0|De=;MAcp)OICgd)F`P?LfOgHf;;GPV0}#R>UvORV%Ms#%q}VTaqM$gJ4pTxfEZPtNkmjhT6&Hy|T3Y<|0OW1J^Tt}#!DE+abJq&*R699<PbCA5WQDoTmf>L*q5r;rJmdi}DzH1azybxOf@y2*q>MBjh)yb<?JvpEg!06qZ%zxd?qsnn_0Q!w#*$_$5o=efi4yx;sEC!AE0'),'Libraries/Compiler/generate_operators.☾':strd('c$}qJeNPle82_J7vE77ZMyK@dz?fWeO;NBl)j|*xlk>Vc?iRfExFffxLX8ces70G10-++v)gt&(#Fv6n(Ld(DHnE?fd<DKhpJ!fn=gvK>_Q<fa^ZLB}p5HvPgkR+2oyWc)j)S$sM>{*Zx*dlQd%*4M%e&1sWqtW#Pde`r%7|@KN|~6`(MckdCJFi2idvMW8c0W{bLjAq_IQG?!E)JL$#GytalkF5%f*t1QyWN6{#!4eAokA2+AS#aP!^!vhO!8y0_7Jdcc3gmxeH|($_kYGP#!}04azE%M^HAPtU-Bf<Ko3qRxiHQ=)wP2Hf<DJGVIReOVG_n`5eCw8b-E<e`xgJUj#=%^K-sR_y~W^H_6eCHdST3!e{wNB1Q?n%J1+|Y@g*%_$&T^kbJtoC!4ll@+!Z9hMDKT^J}_tHBR8CTdhwlm_H7y>uyS|J(hTR#;;RruhrDDkFqF>f~kbql%4X<#7ccV(&z_|cM%e0l$|@zV9QyQZj^8F3oN#8A2_BIJC#Q-flgo#CJdfE-QPdtNXwjyFrq}j25N!t=y@2_pDX10O6h)Koh5!3gucX=;t4cEwT`HftkI@2&Gj0uE^X?jZr*d>G7CN?VWu*!F!fD2Z;~=;c`6o@Gpt0y0xeeN5i?>%(0+>l%wOn9XrMq27A!3G1KFwkF$rVvc7HloNWhW_Lbk6ACwA5@Jv(_i5{d2KzI|6!7T2NQ>{yl+x_xEEXdW3;m8!ubmsI7-%J;IC{2G>qMPLH-rqo({P$$~(8K2<S_)F58NoP*Ev?1&ES_A2l=Q=uIoZcJ=o+%c}ZlUbac!LE$G7wK3|NMk=u&cebyB&;gAAkrYe33r{3n!8(bU$ptzA6@67T#_2g0R?+m1V4i`P;<oI$zR84jn4J_Yr!}vZV*mml5=YAP?NDGhAX7au8az>&i#c%jYt#j7$vSNgbK+HVv^vXfl!#n$Z-c)KE`h8Xiv(Y%h7mmnK9DrRehiRovHERQLrz<paL~5Fp&yhmq-)LLzN4E;L2lFYqZu_$~f80q@fgEib7EU=~D!Ud|ip@9{zd7aj|I>|kp*Q43FldKY~oqUG-Z$5r@c9cH`gnk!g}#wuXxH;>=^@%QMPEu|fcL0C_Kk0%Lomd}_Y5W^Si&_lB7HAQRe<mLL}QvDzKl;4^u_V*M)Urk_sN7nT+a1^MW2IJM#^Ijq32T7fA;TW2NzZDIhTiT$+W&(HOLEja6(*0Zf$y?lrWU~K&PmcoiMv%P=qhflS5&@O?Fag@?2tao;R}hW&`JyKO|0wbS+uQ`sfI%9ZAIkU0{(y+23N5B$f(ZyQ4H+gOlG2kZe1<;~07HK*_`C~yog9p`+QITFVG==v96slVPz9hlL)BWl#18P3G~%Z^T!<;ac;}bxkXykhv>&!FRkcS`DhF$8KSCf?fQD)%22@RpTpaMk0#o3O>vcF*s3Y<ltxhB$18J0TKLNrhT;j7jOIqN|dXnU55jid3o?Qok=vC>KGQA$zOapTTIgRG;`oz5uOcS=Pf3Elhd(YrOnNtwK<4m!lSV!OrJfbOu4aJ8Lf0QL7EXJB4Z)-^j<}-(g6<#aqyIhC*s<WFL0j&pl&mc?c3{`t0%9OAHMpFV9(m6vaL=+aZ9p(bSk_d|g6f04J7_NZ0;)!jwxW^`@Ux@9Mhw`pXgC<S10=Ih8c|H@s3I=;_IbAN7h(>ix&4+3<s74H&Hv`U_CC*E3`E;pZfglYcZR&H&LDE!C_dwPpGN~-IdMsOXz9~ZLcL=U9uFj%zh2GFZSERR~)j!WxZIO^d>l9xP*jtdb;ygL<)y~@RWcc8njm=+cN5jg0KCL(W`A=2Dab+0)SEcUwi7;VI;ivhGDg4Uzy_@C~ImtG2Z=al+f`PWuF;t9ToDnVR2Ui;0VbhjXrPM~SVU>JnFEj!w=F4iO3t7vM4GshK;$J;O_xCArmJb826?2X9>#!qL%uUR5TE<y`oKTK21c3x7xLcV_V?>w$ySTN5$9;WTsv=FTsn3WlDO|PQvijWIYiS~30`PivG^Loq&mO56Sn^7zF2mvJ_`5qLGx-uDN6Exkxx^qX0R|PO%8_yi)$v`x;C7u}IFsS@9w@>s3C`zU(^)F81sy@&XY@3QHiZX~6>84M<ZF1-7B}XJIZ>^#gw|#k^n`)ty+A<hMh`EFBV!$1ZCG939)5w}B{t#Ki0{kzc>+Uc`}PXH-@|wOmZ37{6sx*B7mDRtY*s~wIyD$}`77+|Q`mWAtX4Ah%|u-(6tbFA3@j|RFz*^8`~lz6=GZ0Clh^)<IorS|f*mt}U2il>rI-jqA%Tf+rjka5Hysz_5-nziC-7D-I@w~zdmCK}6(1V4b)Zq51XZPAF+YPcPi-TG5@|Q9(-37UE3d+*k({va*jaWaPR^oz&ww3{!5yp7Lu)j80(65`v4k#}!6OJJ$V5nG7-%n*HJFZ2HT5+RuYt4tDP<uaH(&wz*|D{)&1pY@pB|4n4l%zs!tyqga@%!zz-D#3<h<Ja04LP8fiV99N|o#y'),'Libraries/Compiler/operator.☾':strd('c$}?PTTdHD6n^)w*zVIzGa)!pRmqYoaZ8Iruw@gf%C%M|ULp&#YuQWWDvD$X5N>I>7(xUX$b~imT+=v#(m*Aq@A(bvV;`zW{sTQTJA1K#hc-1jnq}r(zH{bW2GLPE6^?#`6oq|t-VBE#J&J;mY^Zrd>DRM^2}8!@PFn9vq;m)pB+D3M!sS9?)QoWqq05qA!Z_|j7pl9XYHBuNsEVFptDepM3$1#lKM<rNv_!|+T6z$zpg~>Nlw>Lkf~`ZTw2{(sSK1Rs;)<Tpvq_n$nx)J14aPondnjk<gSkNP-scFE9MCd@xklg764MMSzRx$efJ`ixPTf|KpLFY*isKmH2kB5aszgI|=0|CfKBd1QI!&L`5k!Z<(ys`m6N7!pganLbx)4Ct8f%Ud@ztmuGnN%Pb^#jZ!w6lZJE-keL>QsRus#L;W4hg7(6Ta5xU#o&#{QVLk&qa=8ER*Ww&@X}o1kwvh+LRbN|QvWu$0h}60%iEUrGKiIbM(MDTWHX!Q|e3LU)+?Bl>`RA#ei}=A!M!99=?~T?Rntyx!RniSmf9(ASU~=K4!>^3W_ynp@A!;dOKJ_tUqlf30quRL%7luzgzm+1z^eakexka~*IcAU#WG=zHYV9r{`cg#$r5F8Kfww-?LDWBxc!^&^yLZd$t-tLdDI@|X*EM(c#Z!$mqz--8Z>?0;~Rikm`Qk9X6Mf<Xz%AJ?8t08Ii&D}G2msmfT=bb}eK(;{s1RN&^}K9+!v`MSk}Q=kt~jHj$fJUx>mcT~eEA;n1ar9qy=oKQBga8(ZhLOd?iKBiON?6u2^G?>Iq89l>963L{}r$XhcZZtAP3!LGHnp3lel~k-GO0-BIyH@F5kh^*St~Lk}#@tXSuoUS#J2zM8ij$jG!LS%vHA9-MngJ<HGCZ|37CeDqk-l;h+w}rNSU!`zK{96x5D6<%r`0kG)|nfCOUfInmP9ctgv2W?WNVe-<yxh%&vKS+u9xin!u*-DHQV0tIbwCEg?RvFGs#x{2-CaIfRAx7+1(8;bX?CeKJQ@}pLJP0{_n0j&V!v97J#~A3ypi`9+fsd+IPkr?GQkSwS)!;N|C!z04Yt>9uD{<_@(+;9U!Yl(Ezqe228P%4&2r?XyHRDXLW{%P(bYe2i(sXN=cU_KPGqMnB-I=WvGLe+>H)&Rq(;5-~DVB^QFC`3tfX|e=Y8_FsDc_#|vIA(8rB=An-FzEA<#_uh?yb>jHGzs=IamfFKB^SV!T#ehFgS8kI!{T@YP@AwR<vK8Fj+gUvW=oJ`vo{CtvqLYSDBJ|EJcAHcwyqKAz!k}gZo_k9-)!i(eM2@bdf9yPOy{?AA;t95g-Sld6C1eyYxmj54M8f!kE3TzPo{RlJz^hmZwnbOtS!~3&%mlWv+ofFqsgukDVm~<Rw(}4Oz4xiUXovX3%v-<K|<JW!lu;h8*d1XlanQ@=>(4^WAV-bd-Q?5K{?@*r5F*@(b_pE9RWnrAbFV6=ej3n?b#B}k=SU>eRk9XQx=_HIe^Z2X**o3+5ayPUEIOA0j2)beC<%aaSEtdVxZ9qg|!{>G5!dIJHaiWMkJ~SL&jn|KJ1~H~XPvlbthCaVw{!S4$9<&w$3*4pBrE~|Kmk}6e_MM~e>W}=+QKU}F@0E(wN%^@{Z%agphCAAVEElV9%xcwKT`*Ulm`j_dvs<-Fd7`%W{FS-$f|mb$TiZXJFh?JL82wOy&qqLy&52TNfA2NW5zsNvHqZ{xE>Ich7oZBzE4cqllAU!TeXmDa+LX3XcQ0<bn@A6-IhLEPT{n~)-?m4CNdCJpRjaHlLajx6+U-qq{IyvgF~<+hhc9cDaY!sK($>{&bJX?<%O`)B2g@g$O!QVbC|;?Xh;FluR(oTEZ9xA018WG3vH'),'Libraries/Compiler/node_types.☾':strd('c$}?Q-A)@v6u$RUtoCXq-BJwgjU_G|piNZ=TO^SprD(OlLao}^T`%oQRi%dV*Aybam>2{F<C<WBkXltOiIQ+JQg8Yeyg-rq0zET3v;Vu$rk1SPJu~y2zi-c+L1dmhDcrk*RFyt`e7BGvy|1bW$yI%Nx}^8NH*IKT)vQ!XH5n_@rOLQgsv)c(S;iPEY<s?ddNF>4(7RGv!gwr&Vo^=qGS#VyQP#}=1Flll4b7|=QCRlk?9k9hx%};H?w&fB8_tfvHiq`eFeq_1#j2hvTA2Zu+az5w4;ue^(U7T%Ki8;|)TBNokva05?4w(xMb^m=N^JnipIW_HSXR@k@FKwztT`o%10RAiUAbj1ZQx8wf*(R;k#sTxFt*4V*(Psb^%{94MqHdi_I|9xc6(JDX6e}F<1tu+d%iM?rcP}}bjLY4L)<9xnCy~m1O{O&y(5WNx{28U2rJ~3Z3*s~D$UkDvnPt+AA_)Mr9VSAXN?&ye$+e0CQ>P?YL)y9ew4KG_@pNBfMjmxAEKJ6O?+;M7%{bcJ+uEQ*?}m}kq$XR;}uJ}n;${~2E=Eio`Io37MNe~ihBwQ3nu1RoFR5_juAN6ByEVh{mPO+Nx>HEkW-dZ&H``&CP2PLp7`YHG0uyj;T%e1DsVM14Zj4f4EXM(I>Vg&m0Pa_r>SjVr1kLc-(Nht+FRd(|5Nxc$&S%=auR8Dova0o=JG9{yw8#E`sDqNyzY~~@5ont@(=!dP^^L8kmrHGFoi8-;kXb%fSQ-9Ti&>|W8!jfgJjZm9hb6JhDjQXln@a<?u!u&Aa4Lb#;&D4{@sWbwvt^QUFV|^keuPnVR*hEOQ_G|?tF~9|AM>7=PwOEl7Ve)+4*2BrZ9SyTC3_4*Dw9zOU>}Fa((E=_|WBnK8m6APkg=`q;_O#H^_yX+UqmR4+Gh$PLPZMHEhpjX3GJ``10o*?SPN%a4~d1%yLzBSnfg`imhziATK=@C?Swabr3*kwFKgwkk{0xCV9+)Gx%T>p|paPufI_kEq|k@&};G?KMa6fmQA@Ou5&rUo+CadT<avbR5OhzmzsR*$qk~STai)O4Ok%{4-%l@BrHc^1u;5&Y$YX2H)f)+>H)iM5+%)y4wE2Fh@uHt<q546g%wNl1gy*DCWVSAVPTF%ozaYDPA%s&v&)!M-MdWS^Z~-;{ea0L9GeLyQ+bs8A=2Ie3&<OZwaxb)-XOJ?%ikuMBV61KWV#uKMCh7CQj1H)37w@ZDh=U7C{SXly<06>?V!Kp8Ip=MX{0g(U6trGg9nn^fI&-Vn2P7MQuV&kPE+KWR(LEFF^QzjOiF?-VvWK)!me_j8OKk5PaBLGqv$+@tm`R+b1*cqXbX{?kufXXf_<EU(Dtg6`h?1%l4|bN-sX9@{QCeJK7c@{LlGKt(FceiTRV{UPRz$~lt9KmHkd(G4K8rCC|d3Wz}ty#Pa9Qn)P!SvMoyd<TkJe1-k#>f?QvoOPCWqWF>j87Cu8K9T)Eb|1+u}`sh8(<wM1!PF)d=hS}K~ptR&m&gEMS6=SJu|RRN1%^bBZQe6CP6_LOMN41N=(U7Bpl*!z05_iP#d-&1K#H|as*TxR?DLU>HOkG-D8s2|g2->(hS_2^y|d9OzB^+&QWn7!{@tH9hIb{TF!MDm5VwS(Uzjg%WT!SLfi2|skANN=Qe;jm~!vrZOp)ZNr>&h5KtXq$a9MQ;lo9v<go;OIrR8w0mOkIf76QZ!q!4kn_vBGE-TS-YUbeLFRF?M)6z>;dMBG~a2Z_=mg5SFQ4KUX1)}=z<R;4{|x#{nj_wl<i(2mmM6wlg|wekFpj20F&*k00'),'Libraries/Compiler/tree.☾':strd('c$|$?O>fgc5WV|XEII8|OO&KH3m*arA0llc+FKM^X}tkU#<uLO6d$P&ha!P!K`IC#Rj5}EAUGfdhy7#BuGd~CQK6P1ZDw}f%)EKCR6ds{lfC=Y_toja&Sd;(-}fnP#Yw<@QKUR?0ec)J2lFVWz-X%l0Ia;;9}Mn|#<%;UJ^#*V*x$uKjrVX!JB=V<+B%+~6{eKlBwYe9a{|5~=y@kk<u5<X{U?d=b8)m-(8|i>3wg=5<b`}AUxMop{6Y+RCeP&$s-1ZLDBl~O@oNvc;gK2$+M;nqeHj-=Sxjo1KJaKA{X(9}Z)@mrB8c)@baHKQ+AN7Eq%hWC4TNU2(=cG{F_!k7>I%P78qJ>`1apGcFY?U2f=cbIIRvl;0EFl-?L5jk-Or9VfaB0$F1TOabG<5&0(mVzxpm^|Mx&`k7zcG_%PWdnG6MzrTTz1ijjmJq$BJOd3OoB%0&&L0v@`n`d5a_?G-Lvh=`!|Go?`{YG>^hVPP=S3i8;(*ZOT-BmM8LOW5~BW5&}_h)K=ko)oB_chAB$GbrjJYuHxR&M2M{L(<H@TZaGM^WLbEsQkL;U?=CJDHz~AIU2kVR*igi=e2Ypp8h|#(^-WtP<z=MV{$@i;6jY}pVNNtRr8=}t#o~;!97h=jJlDx_!!fmH!Ysd<38UGHsXH?-!C*L|T~LO4s8OA3W0F-}mN8qll>#@9jI!z;?cXhIE>btzsTsMZv4<mP%9pM9dbJ#Y<y_2#$m&O}XHfCjwZ~4Qt!->;+qR|l8^=Zdr%zP;EBT=osOrc@tmr{sgbnr7BsqTpev2kL'),'Libraries/Compiler/tree_txt.☾':strd('c$|$?TWb?R6n@XI824$Wt|75c23AOuP=l!{Z3Q8QWz(HBOShY_J3(Jti%78wX)EFli`0shqIjW*KAnH!FY(MJ*`$r&JS?+kzB%VR=X_@<Y{Smt@(t>`a#vkgtS_y&E~S=;Ik%X-7Is@+m{4X@%VLb#8dxls=WF%3Vr|(i)hfkXctv@-S)sYHOUzc*`XX9cgVHM`PZ(=veBLH8zZVCByNQV1Ao6)6q>BR>z%N$F5L`i<Ad#NMNYoW1h)4>^a)Xg8=As`*WO%6T>O+Uw;Tpf1?KN^u`=T-5B$r8EW=Ux;EI4UOh({wF!ZY|hVb3>BlI2Q`;#D-L(Cuza5dH*SAo1})Yg{ClmCRZs{g%7d7l|xvnoi0(3?hzT?MG6`3T8K&iXR%E!{$Yfo&TaYq(}oBw%`=@n52o@J$Pzdk5f{#ss)D*$&9Lq1q&FP1a?@~>-Bi#OStmhNWx&1%b&0Cm@d@I6gJ@me%m^fWc(Vw!+`0tZP<r5ux}&i6?}12@y@V##+xlcH1sxFzDKmFV2(ygvB=%~xofhpSODYn0CuHQ6Y?GGz)y2cf^>74eXARB)?`6jYJgmFNR=@jCOm~sW-EnKO>Gz3n6}Rzb=DFVOMlVx8JyA%&KR;TsyR!z@Pvp*V|CTQahp%Kxv}=nVtZ$ssrt{4g_=6g_uW?5U0qMkPa92y7Ypq1u(0O1Ffk{BI1Z8W-H;g&FY-xxtR<=ut#IA#aL?B*Fyr_Tj!>Rka0Kt^?fE-yX{l0NsbBzW&XV)>7CynC;54L=tr<%<1I2FrdGtX7rsAZ<a4r>8vA<Cj9}h}$&}WR=Xvyd>Z<=gNLQKy)hB%g<R2B4NXVWP{Q&Rl_$0Kd)QBY3)dFdQjJ~Y=IdH50rR8OhNSZ&||5<4+3u9oI59FD3uYDQbcJ*u0Lj8!4+Tna@w(N#z0n;OycO5EoxlcDVp#l|Cij6Jb|PjNC$2V;Q|K0VK2nraGFf*<KfE_!AD0{B~P9s'),'Libraries/Compiler/expr.☾':strd('c%0o@TXPi06@J&R7*7>dJ<3G2THfTW%OHr8vW!#+o|LVvWp`w6G3;(;M=^f0v5}D-Sx74pg>VsO!6A^8FOUF6xGMeb|6o1liJy>jx=&B{%=Abrz@#c$g=V*>`}Db=?{vfXC;YRS+262Q4Zr>Notf$5Cu%ju+&Bt?T6{KkJ^$UXbE+QpnCCOs^*qm)lMfv^^48S!;X_liwaKZYhmOHALGA6MtYj?md@(vb1Eby?W50C99nY(dG=q7k8MHgipw{W)$_>88pLi1^4t$v6D;f703nwaigSk=_#yY8?aU6<LL**(laOCI|8~1QddIR8#@pF8YZ%kBJ#~Xw3b=Yzn<%Bmk_$B@%zpog7l;0f2H~EMA<A8qzYrX~X>Ss<h>kcsU58j`!j|z^y;P(a3Fo4{Q#r~-J*$Z2ZfQ|ddI_<!NjlI@9Q*&XW^IFAW?z5|xub>@+uotLz@X=q{T<Awtt$=F<3K(P+u&1Cu@W=a<Hznv0;-LAq`L|YqeBgSS|5XS!m6z%GP~yyYA}4lQZ8k-|il5fJ!(yj`?Ce~>1>ERYDHR|~8+=nfJ|_2qu$npSB3JG#K1#lHqo3OY@e_n5>r0PckadhE_ow^IuGqydy$TUVl0S)Qju)6_>HGc5H%s!(NYj`SmaDJcMAru|D1zkb)tDy5`cDt8<XFc%WuN_@D_gnQ@ESy0=l|5A9nMWkryMblN)Y}g&FDJC+{weDs9AKO<thtn=k}2dZSYG*ILul(!cU{qj$7@8z{$PcrvRI20mPR37eJ_cNcIzl&>nD(f5(?;JV{vI|45Qv;8>Vu2J(Q)p?3Z?;F3U>zejx0nCJ`Fa~kz_yAwNSI?dMn2TrGp-vZ}%3#C%Ie4r<vuesg<r8zGvyCprzxi_Q|g}SBo97tQGB)H@+q9$i7fhNxLHHNkBPZ!|d5}>korjKALz00?y_CKmH<X9GL2df_;1-H|!?L6$)LRd5^U(3~*S}O=5+`6MlidT14CG`~=gBZs=;mLH8>=L#RE@md}%ILtxXp}HI*dL?!c4IWCh;<0{E~!-lCNYnVjxvoj#{#Hh6=^GF2TV-N{r7#>gYx2-<;6(8!c<~;GA5SffA@m86$fV$=P%O~_&Tn?nqGepy#8QS`%)Cd3sGAtacM+==|&XP<Dk~4hoN#XX>Ff$nSs_S`(tKLU@z7;id0b`;(Tq8?;mH1!!C8BuynvHtR8mM2s=-|RReZn!v<L0u?qhE%bmrwoohEz$x7>_&o46N>RM+h0$V$a7kBQR-;=-~M?lu$TT8a31+KZt|18`b$!4hg8FrNt6RTzRXYP;d;Ds1LEwcY(n>!ZZY58<oJ%?hj&lmYq@m!|oC+aDHbBY<lJ1hLU1v0Ggt)T$4VDlto!5nc!_ek8Sx0?>qqa>Zo6jN|UdVHY9x00lOnLlA3eMT%bLNHLM=wYq-C8_GBc&=e{BLi>rq{WURO1t$aPKD>X-^@j(4no3dwwNmw$6Tp6=1Nt9t*s%Ow{!e^{vBEiz5%zg1#^G=My5h?K+^jUX1;8SNTGh;a8X3*tmU_HJreEn6)D5INBt|NWzoX=$?|F*3W_SinD%(l#Z!V>;VV{DyTZS)qS_U{z89*M?ny@lV4=3^IYkxm91Co+Bfgv<1OtBMNCqv0PC;%zT|kB0J5l*~Djf)~74EqSygwCNJrwZmZ+wd>+%}AH{$DNd{(G%3C{UDzBFbHm7$8tQ64AHQ)8}6v;yflk*q0fxl)S*^MvR*X8e&bRM{I;1n!r_q41uEMG^RC(bWcPJs3_ba{em#DS|pL^8_FSR*yI$<tA<4_O2@eQDN^lNz1t1iO|pHyb13lpoc(s)quc4SH0gq7VYdjgEJ=L6Whh>Iuk#BC!)%f*>|t_+2gUi6KcdL<Tf#&HUoXqTfi71D>`G+?bQyji4pN6eez_WSO($A$&}unp4Wl9JMbRDuUuc9y7UI!x#3A%xbsp<PVXCdX#?Mb4I$?H}z)UZw1!ubvvXJJ$Y8CMZ_1asQpKqOIDLoP^G)SQ#bD?Nu{vwi-d@H&SN5!-eKQIm7(P{z4WGfC~KkHIoC8tOfll4Ez(O9e93qaE)i6cKHKym@d>|Fd1)Zm(psRii*5u-x|am!Ha6=;-)ydvjfwMaI_s4CIva!LzY=rIDyaXorBh-=Y%J&}}h_$+rCueuL=qw%s%rv#KXQY@ujlp>7e6TB*i@7dgF82a{3tIzMUQCOUO2LfKzk0J#?<(`<GEnB|8R>c6`9~Bl=b^~tG{+!`#CeK-c5-4jFaaYLEUb;D!=Rly%ZCi!ZX7y$HB8Z@z2^6IIg!DlWY%a$Q3ZgQK%##kboXm_pr_{UjS%j&#ZJ1hxL(Y`k)}CfPI+d{?ho_RrzC10-tB_gl4P5fQJ0!&IEJvwylS$k|`_f)}7PwQgxA<dJghZ@m{*534Ps%{gc~*F`T|X5DPTY|d*y(hGs2+oV9_URtVOTlPdmYp+9+CVN;V<Ll5L6#VeiQ=t@)S|EiBz!^{Lc1>b5);oxBk+u>JliNE_SS;nq{5)P1}Mp8bx;!2{377Fv&||S*8yQK9k2O3S>5Ho?)K%fD<Wx0K6$4$r_D?C_*86*?a0Yjbp?4IO?LKUf2Xj72T`IDG8LQWfx067x}G;ish6ub<tUo7oDp&YrSsJa1%goUXIFkTLy}8@F92UW7lQfC9}!t_iN9tZmhXk0-y7*@#xw{0*Na!vNr*l6l;`GHKj=~Yr$Rb9G%`$8rM`(=RkcvpagIyr2ut=>G`_JLNbDLJE1E?=qq||(sPRqwT~9jFUh?OO~{>;NTsSejWSP~8|gUGuS^7`&-{yGY*NEtd4N*(%f_j5vAV57;yrs>h4AJk{|ryJ$jIW9A!lkKBT4-{+7%mXTBI|1rN7R<GL-|k&X+uSFM6DwWCLXc!s46!LD7Fz(4Gyd&mB9ctU}!8H%aW4@8}L<M<)~GDt};2jH~=>EAn0Cw}-x$6{kE6|Fk&enY0}2K)zJ&hng+C69i^#DHcBx)15{lrNY&>hgdysTTL1=4-xtp<>aT5wwGuoJud+eM!K}@ZYbgRf2c>hDB(eo7<Lcaf0!G7?~Q@GvqmLpqIT=<`mj>U+NbAr^#s}Z)5(*^6{`B9xPm}g^qt<bs~7)8mvLxm`f{5v=Ll;Cy*g}#xUJJQ`bJ_HBjpxfXNJJ?qDY7kR}6fYouKcd@D7OXh-B6TiT?|n*Q*!'),'Libraries/Compiler/lambdas.☾':strd('c%02zSx+2C5PtWsn2cnp+nyj6oEM~(;>6@od?|5~2ZUB@7?PFOfM(Z65?O+cO^A<pIYVL-Ajpo0j}Rv@_`p2$FM(fRi9e94uI`?mi(Lb;vQo2iRM+u!RdrP_Ok5UMPk!<ND-`hR!(%5;e0-`<V9fO|4hAmwz9<izE|x2dd(3q?=N=IrK62#!qbJ@ueDssTyGJ_@ABQQD(?^}G)tbaT`Sip|c*?sNd(+7|oOkc*_4^!gQ!EvVy}gC=XK?P67#Ghyu^`68-8^$&&Q7j^czM4p@26@Yzhj>RpHiO#8h-YX%bilcV`lRfUlHIZ@T=#7en-EQ&*dMcZ8j6TTD!etCywC#tavQ0q1YKQoNwb6O|F}_z|ADwt|1WcYC%kkUpw-l<-iDDXsXB?m`-RM={(AE93PN2J?Das{5J=f7zUY-7%Lagp6)F=q9z`SiH`U!ql*wrUh2~i5e#5N;3>c^aqgEZKIyb39)aeXoVQf*j;uh+5L=DE(?3u}uAn1#iv7I~qXoieAr>L#8WY~q!&{1jgMNQ66C>hIq1W#z$f?(u0(wd;i8T$hROmie+&!%l4;Rg-g;r&#wY+n+rW&iYoTgUNm(U44^He%%cz-H52X8BWwOFkNCSuwY0bJ(7%T~)@+QDDi$zS4bEn{gg@cRaWv&CxR!k4AW89%6m`dA@je7OyLx$5Ne4s$nePq-1Rw62DM(Y`Ib%s^{K{3Ox(LHsQjYwX(Q$i(Kzn8Lsaml%|){@I;jpaQ2O&(du|!7pd)k3lTC2V<nw4>BY*Jw_|XN$55;aZCJ8N`D6$Zw`H5DVKVD%z2!rK$z=RGnu<FHndUyXKUr@6Bth;Xu_PH@Q(0Z01n@x?sO#s*eHlP*=890q#<HaToq3((ujSMt$8P3YgU#mlnx}7w#;Cv&FoQZiK(sA#*ep=P248!Gh~r*lh*Ju)hp0-Cd5*9@ZE!K<!;XX;)ec%Htf!Q@Z*<Lmd3UhGDWGs;s;gMx<f53Sry+&h_d~54~4~2rV-O_`|FjBu~G2VH5e~;>965N)U4ZvGcvu`kl4g~<I72XU(KcU{5|sQ+1KmYmi5+FxFc0x&As<VROsBP+hBt|FkI7Nv5x+zb3P^Tjr#aTeHs$K&g3wj!FawoJVzn3QJ>kU-y#YbJ22L_R-O&X{jDbMh`Y#iOiVL*e@k4UO0il_R*BW1x%x1<A483JI;HBw6}}$l=~3x38F}7j=*J_^+wpl2<$b7;Uht92IV|pliwPQ9)v|KG>)|6=ZpUidYPpN9a98HeK!CAX|I3vKrichqM2t5O5u}M&mC3|oX%Mz%K$X2*2=}}!O<JiomrPZvk>*g^Vld5mA663M%Kx4j(l(`^#c*6RTuo;<9;W*GjB?lYC_@!jr15=|;IHfITB=JyA=g0hwcf5$K)5kpOBOGyKuWT*cB3>-&<X%2cYkGn#pV0a(P-a8D+y*?9@+!2d0Lbpsr+FP<>EvU8NbQ3l2SrBTPv$W!~+BRFL6Wh;s|>iPZ7Gcva+scXx+9Wei0?kr4y4GH9%{c$<_{MqH;>yB^}>(ZyI3{nmQwD2<K*f=u|eOOU*#Kv<;+~{-)$cJ|VsnFXZ=VqkaKYOXPd2wURtzjn(HL*o{>>&6x-ZHea4vMzAX0g&hia*LHiOl_{XvmMxkW-h#aFmd*<|F)kv99th2xf@ng0&#UjrZTCn?@{=N6jIp?r!SXK4I%H^KS0+kNIUAiK&{4oahr&qaDD^({N&t>k!Rs!{!y~MbChD%b_}R5vE6gj>CH^t7mU5Z{_@#8;YW2-p=d9`sX6&-60_{|$NOsBTj@Nl|kGuXz%_AjJ#nZ6wf7?2k=nDo}%BIMy10i)LFgjyO_ZnoC$L81xJ0ssy(T6K~e4yX=q=8Z#>Qsp9kXgo<WRcu&r^SPeQs!a2lu6x(?U<8NkVDGyDOt`Nc}GUUhzgb)>ie?(HsYHgrDEcym`gG3CKd-x6cTYYjhnTcF=vlYQlXm>L$4sACZ329Mjf4@@!l&!c9&Bz=Yu8Y6j7h%(r%#jlff%ha!fg5v6BuW6$x9u?ZnMDCk`xaBrehlZX+}7<-i70P+1Dl-Ukx56_@BD7sPe3OnKk#n4~r~Xaq|R<4=jnVr89qQF`skcOiSqy$`#23`3O66S9?D5SLT3Bbe?;_5&k(Zd=)m+494jt<Q1|==N)kibX{5V-+t~fa>|^3tD8A%1|$THJ`as+P?JD1WWNYC6F+q>MhQc5|BP1ka<;~3`9y!s-rwvD$DH=>Sf5VT_mmBvk9&c!PuxG0O{SbNIRfPO4@(urxBAj67`x#tCL}7)H%V<5WQ&lsdw|)K9lY-2dLbriQmP%DK=1s%E+K#2Fbi4c_>eXlFs#?$GA>m4F#b&8DdO)W(mpk&kSdJ_tTHv<f0NNY8|EPlYLR<P3Fekm=hJa3ybWf-i5~G!=Sda{r<5-#f|2kcGVpjptYO}x4GAhyr-iv!X@rs_`B(<SXGYZDJT11#tEd9)Hq3;VXDfAG)`toU5ra{RHLhk{6YY&MgeQ=<OyVC1MRCqLC#!Vx`URnVx9~&gvhe+WnnPzA(7%HpzC<Wv7^Cnn6I;CydSoV;g9UHZxr++`zRQ6@vE;doIh8s;6ECuW0qFWoUlV@sn}17U&N#birf}|(gwW>_{kIZpC4^4KbnKF0Amrx9T>mCSb}j6#se6C!1xmZJLp*2I9z?ADyD;8Iy+b{^^{U!-yyUL!YDo|(p~aab!?!Tt$qIj-C&?w'),'Libraries/Compiler/rewriters.☾':strd('c%0QdYi|@+mf!gmmHt#^Dwez1okweWH^g|dXcIs{w6pSBt#-RGE!y3!?zU-bv@0MaU;-u>+t{%Q5Y`C^Bq2{A1dwv2`MC2FM)Jq~u!_X~fI0Wxb8p>ORhMnhXe^qpuDXwN&OPsYZu#Uaxp3&nzxd@cz1siQp@WBymdn1Mt5>GRCn}v>5Kh*c<CS{H4?;he3xXizZTIfm_r{wCU*G%Yk@E1HBYO`(FE-e}j`%}Lryyi^4<3TM!Km-Q>gBy47~AEyD(!B$+H7=-C7(~`kz3>^axWzBk&U9b*DLyOzww9i@ZpiYM@M`B>~#RiCpXDGvQR9Ij!~!v;MRd=BMRa1=J`9cL1H^PINawmAwoWR2X5cRpF!aF0<YQj$Qkk>`N?OucF`_Z$!eK>eM+9P?-l&s!0%fcF7xC{$iC+I*Jb*(L{>^bktK48EEZX(yL{*i{A=0gJ%ccPCf<4pe_qA!8{(TkzU|{MIO<#wAPn+3Hn^a509XT#_C$2dYey&BwQf}IwCa^^$7j$lke`C$E)V|b??v*MJSvv{=;wa9zW6W~6zRnW&*%!k#nKsZ=Rq#`&w%xMEgoj@ShwBsf!J&0bDxi}d1{V#!*xB{o{o4w3QyStf&SHwdA__qIy4pxcD-7|lfwe1O_cw%P^RO;@bOOyZ=eh$aAIO1CjyQFx?CdP6iYFe(`iDatad*?hJ3$o<V`;x&>PzL99T9Uf?6thz`N^Lb0#P{IIIhb6#O2FFWK^ajLUx;5Pp9D@l(d#ou~_|HzlRBfSuqnA72hB5bptq_vjF7KiW}uy4~=UC4@QrYH4&Jo0P<;Yx41(WTjDo>0mcj89>uuEZAj1gwP0JcFBhpk0BS(HRtS=nY&&lLm>Qb9o)x9|BO7L^jIOMOTfJ=WHs=G^bS^=tyxOwO!P(KN-`VtWdnA{C{aU+7N?#j_KarG{tEeoO>l+WH%a86G!S@!b=@hIIjHjnnI)y|72w3)>M974<W%AEc;X~g7Ymk5vbGX3Y%XArSvLs0N@D`CVg^uahvKfb;&4&h!>Glsj0e95s~WkKgi8#Z(yM9{ifxF9EWZ%dCP(*$>JOzUFHuG)A}<Pq5Dq|7&d}?~z$Rng^wWfcHTiFB`k6o`7-Y=8M4q5UTMoh=uzKwnH#J{?kq;uErLUTK<_-9K0w+0^$tRh~K}Yuz42v&JrKHXP6Rr0(@=yzk_g^e%7Ta@<^<GIbLoq9$CSh=d+gJAhE%!Cxf;t+eeDMjm9HKAaGK`3J8WA68M6}0H<dbm+t`G_uV-d!FXUHS+p2B=*1EnW8I{$m`2mj}1|9|1hk0(kqfp@Z2uY1u<)aXuE>h)Q#3jce5TJZm4dT6LnIKjWdnSiMPx3oHx)BLtqDRp^ZV6iAdD~L5xq1%eh5=)(8S(>eGt=XVqg2SgwHYd`>#zsY$a)Y|O_?sDx*b}6Jz#Nor38@xVX+S_1TWy&ib0~hUo2}uxk}((HvtAbNWNm^iCu16_?3mQXmd}lsHG+*{U;TGC#Q~I)s-Pq}_1eQ!(=XO?V!9fY$z|Is0ImfX7s*3zDwhF|lHsFA!QjDwsxXkBKkG7{=+^lhAPDM|q0lir1{Sgbet$emr(UZ@exCUtp#F`30sb0tHG6Ws$!&6h{0NWegS@ya7Uc~2l3XoPq}Y}0-)s#l9K)Uoei62aH8hz?8Y+l98<Z?Au?CERT)l48m|%@e#Iz1HtgbbtBZn%HV^vx$Hddfg*7Cn%Z>5?Gv}l74LSu_cx7*%cY+<gjrW;@-Ev?}4=ciib&GV;RGGm7)eWhp>#Yc$IhPqavqAB9*0<f<9v1g3s4QST|Rq)1y=t;mk-Kp-&1)Kp9st72sg{s<<_dmnlpTy3o(y-7EIlh3C?N)ibe!`*CsX<tcZFR3`W3DP>DOWI>QxnSul$g1|sjQV&FiiP)RGCm(S`uxFbi7R5T=Xzd=XaQzS4CaU)?;ZT9S|<r!ki{2K<J#E%~Nw6?aaYbQc(WFvS)CI@}WUA>1qA^Z1dsD&$pPf#fiuqRv7ZroCqaWSv!gqOSLI?p)bEZpx>th(%b)>LkD;pkp17O3qRj_et&JLFKp1#1)KoFfQ=8iQ|N$~GEj|kTq0xw05g%Pa6>gvU9hQ23rv4htySuNPs(yh#zH8wNAtxJI=@%QvQRzD<oL+n8)Sv~G1tC?&sXsI7Cw*R^X!-FE2rV}4j?l6>+m;Wz7Xbz!u+1_w_%<JC+HI$Er3oSry=@V4F;zwC!%h<(&+G@VO5{w#y$9a0Uwy_2F!KiK7780&o}Uad2f6NpYIh|;Q2Lpe(f6y7fVMD<qLcM;U9nX>)-sgGF}Br<YJK&_K2xKBNW{b0sjZ&PHHqt|8icAsf!*4n5W^<ZQT<S>ZI0SZsba=Pu$bv_hJ?hI4ylxywM)h+1U6x`GIEFdE@-A0M;I;D@tr|0V7z4z=V-fMo$5E+qPndo8|6oE9w+WQi(-Vt?n#s4vLIDe}4ay4RKwYYKhCv^f+EN;>&Jlwu6^6err^wln3R>>262quKk9Q)!*1#y+x<Vn>PyTji^(tw4$8kPu(U-``u>pQ?4Gbv|UDA6)=Cdyzl7*=EF$>_Vop52m`Hify1G2f|0<?13VSDN*;0U{KiyIjAc%fyD@h;beLi<!I3}8vQ>%&eT7@lHW#q~pM>!BIk~CY#~`rr>1Fba<R+5u1h3KTdIpTTf36sM1T)T7WuRRz2n;;3t;$yMP%$t;?5hpVkcZ?;x|plvoIdnIk#Z)x^7ytF&5=1V($zp?dTKm!Xabj{G@?n`K9M;;G*lc7UHu@3`%-a0n}Fk&<ZeI>;a52=(8bh7s-}MX(2@Q7M)n>2w*yE1{lLD%2j3b2pzF1kF0ZCW6nM3o9mI>z6+hwBL9-8ZUn6T`?xDbJR*rhDZO}#yOES{w9;MUf#dq}Xf>w!B4QLsX1cvBF?M9_NYcWKvQ|`6e<x00XrEHDH?!M*g_u_PzV^e`e*gM{|VTlMMfjR(BE|VMDeKo=sVRoMlgoAIC4;~Ve=)pZ^?Y_94<9U6|F<{fem>KjZ<?|ir0pJWZ6M-19n>#>^_P+)FVRSm8l|Z47rMkx)2(<))7Vy~0bO>UsvtW$b4M8=Y6ry42t6rWr6l2IoIt6ipZIDp)_>%LZ1AGc2;Q|gj&{fHv{5|q(w^&MH*}$U)l)0#|RGf8R3X|F_n&&u{9S9aOBFGc=stRJ$DCul$!TkhF9zA4C`vFS|3O_>JR#OeXT>o%g2`o4vFl)(x2=$J%FWq{uR07X1q^Wc@`>W+|mTwu!Uk#jWoKF`Emce!geNnN%cp^aLsB3qMoC~x_bF$r>Zk4;0_GIKJ9+_x%i+x;6Nz-fR;WKBYSo56pT8cF{m{Sn;!Nw-cVobt}aokTZFNVMn8Vdpx0-puyhizUS&a?~1SNSW-4@!tG6+~rXq67YzmaZOl>_Q{U4C_oetTN+NwNkfBTo??8Wg2*Z_tDeHjtxwso6KVH^)0uL(~7Zy;iMfc)_oW-tw)u%@7P$PNI_KGVVZ}DxRDBv=k6KZ*?%XG*Xj|{R#mMtl+gU{V5`}pDQR63&M1sV_g&3-hvmF8anGo3^}TW~tuK?Sn<!sa@fHkZj1A%eH`9l^YD6eX%EIDycSIvHPi#ZX61yw6<J^QuQTZk@O~65r`T{QW&E44LG)GO_OJ^c7<6;8#gfY(+w>1vGoE;6W0;75~6*XK1bgUSWB~Lc!1}sLGB7AT}=b~UDnUip(#*)_boRz<Jwp7I$+mG@lW1?OnX=gKA08b}eBJaMq8qb^&9&_~sY*(+bm}~&a&0}{Z)!N5AFo%`JdqJFs?b8R7dsohFo|@AsNk`c2&e?{VK``o26*n@yUd&t#O+UMWO^Z%SFwG`4cJe7_6Ix1oiwo_Okk}rrR+MQPB)2CSr^Q!tScLFIjX^ad)n_87CRaV5bpiW;j$DSZsgg(?`>IJ7EqLlPI`>1;Da3;dHrF|n`|~2gmy}DNoaNZRW}V^Nw~3IYI0n7wxFN9e{>DtDUYqbx=Xo@{=^blMgLeW#!I{wmW_%?M_Y>4e%#m65N#EmT*GwMJIaZlR+Y>Q@I$j)o%iPigds41WwaU#FP50IswhC`Y^_e6;HbFn|LbOHlL%e?og!`YzQqf}lh`PZj3MO2tnn&Jx>B$R9q);AZsZ<e+QgoFZp||Czuv3|eveJtp`YpL6s9=QQtfUef@VLon5Fn)~tu(sAy^qMd!+Vb^3qTPI1bs0Y<6ZTjPbYoPF8WaeKUo;6=ymCGXwWJJ7F$ivQ;NzI`zX(`I}?y&=Dwg!u$`BTCl>G6yVM#-x+((f9T1R3+>kdIk?W)M+%<I0P`=Ej*ph$<b`ej#-<7;QZozP%#HBYae{u`7{3C7QT-(ZNVKX{BO*>?r$y_)p;b|(o%A$T>VG9^in<XBu0K*lO;b^c73LE`dnZ;(`3qVeo2ZMo-hFN$?_?edYPQV;Hr>OKFn0!Dkf`7#u#0O?XtP{|%Y|K@s>l_#TNu_Mpl#0I9Jnm8NSbHMYq)ChwR!hUFo#ogYOu!S0fp#{;wVb}ctmKHOf$bb`(mk+RyE<L7gCtEvK|(X7jF=B;733v|#?FNOl|*6BkQ<e$a;09#$Z9EjHhT40kdh?!D^^a`AJ=Xb`kaX110yx>e4Fa<_BpDy>{pO2ZZm1NoHqq~rQLX<zpujf{K1bKF9tX~2$#yl{R*nb75K9Zdez7kr=e+|M%fmceSyzThud7iXT~#m8%FaMG^0J;sWm1|VRZNsiJHMu4QpQs)u8)%f%i|e;x|*cA;JqZ80t2uIB^95OlPuT?AT_l=DsaVXB@qZxt$t1NrozVgvGttY?hEq?LHATniI5I->flD#AAhRHP0<-d-7UNLCs_&<+#L>9jjOR)J151c!<Gi_I@(PRC)*gL<I;dAkL8Lk+n~h%51}fRust}BD=$&RGd_~R1gZ%O)#0g3J16ku~a1Qk_A?8c;`G&G)k$++h2;iDY?0i$y(aLe|fN-VJZK`t~6)(v&`>V=JCcn9_X4UD<vb9Z)H7H`t>N;_>x$OGpFin`G)OC0Yv|~g;bLC71FaZM|i><)t{;qm`N7v%+>nZR&rS^51(;zl^i>m(Xp3N!-7yP_$0Kr@O!cl2$ir1q4i?O3K75N$K4;o$T72I-0@>)vt@aJE$rH94J}Yl^ZNLSZzhdWgI%KFN)5JT9~D!r>_u7<@IFj?hK_%gTvm7NrIgJUTmG!cjkM;HSAIfxSQ9Dup7*L}x|D%1A`0)?O}4U}4DWOX!ZV3(fkF<#d;uoo`QdC@58?aq197;DZLG6id^cS%if@P^o^;i2;zDu~@u3j_c_f@hvuvg&J6U8rr9{=I@pi`}%1lir5{gv*GJNI}&fT4r2XyQ`-2{Sz$mS?i>Rhnwps&@s13EMyQwS0t<%3MBh5T*uy_HU<HYw7+X3BS4k)3+fN(4`_q|2ZQYggtLpFemw2cHY@d4F?m3BKmxa}hq5wix|!qOTQ8&dfSLad}3qs)5E<Fz3n+`lE`iP$N9PhsOtYBBX51#l6&caV!u~;ygL$JUe`ee7Cie@+Le$R3+4A6X|Z5uBv$hlyFyB18bnGZHN6c74zM=AVIOie58=0nO2#QICX;U&o(`C1H_=x4@d>ZptXyj8mU!i6=xRP@RXl~fE`0Jb`6qFsSm$>*bv50R1OP?l&_?aNpwLA)-VY10cGSMY{EZ$L4$v?U1=q}bKu;L4%y3rnO%2gRVn#@D3)3{9Zq|;7@vSqg|yZwx1(ca*6VJu1XM{ROHu&^t_9XxU-iVs1tn1|ooj4|hbi#KM)BAp`P?p{<=cGU7wu3Fg9Z0VVsne^rZ`r@hr?YbIV6CzKTKu?f?KJ0Q!PZeW7L{_>`Rml)5}r3>q7A|Iqg7@1ugDKR-!`-*iKXP`d^-jkLQG7o_r(^&&PEVW<EwLK2-}FHpS&2tkWVSo@_=A1o3IL1M>tRQyvid(C=mZp3h~-Np#g}vaY$gS=DOI65Ke`@0G3%R_-`seztUY<bOTXy_1x@mP$uq$!xkY+k_X~MbN~t9}f&AxOjZTN3h(d$ukKqX8#Sg;N}t2Jf`M$Ad}1l+e2pE7jXv%n%NJ|;F8w#HunVWHAL2?-l$T6MM3D>E^WONpM4%6e}^p7t9z^52e%9_k`VKp4)Ud7LX%O1r!TFs9ZT>G7jqp)6Q@NqNI#O)OtUo<@^+!l>;~P-r_K;_FS+dpjFR44Lf31s*62j-u0IsImLsYBQglvP$>e3l2nEM@*~?F9;|+MGMhI=bg@!KGld@RuFi7#01uMl4vbDmyExwy)juST-1pwWp?|GZV;1QMkGv<{Ue7fNfSr_X&whgIQgCo0MrZPPl^{fmqJ6BfecKTF5qYvl%$1%G@jnta5rk6k^D$V=sJS!nM!|64VZ;4&s)uhVC#6d%mpf|womXwJTZJK`^PcO++or*(|m?ut1@J>(m%HYm{Wu{lnwjJMSsVMp<ycXJFbLFY~Ot_p*Y~FGQB(%NjWdF(+$BmgF=-~X0fx{(17SC(%9~sj#^T{tMpm+dtMGYjvc)L>F((4Ljj3HQ5No&E{HSEA3+ERoXzruy?=NN_<MyKz6QQoG<9X?!Gx_#dWoEwiyybfOEB&-uX<ar{eZ1`Z+A%$49pfTBO&b24TPiZie$8D6W+3Paes3tG^{TL+o`k@?s6Knk98@ZS{{xZOXAQn(t|Mm`D<nf>{8#+0g3rQRUQDK%unrc$Q$A{&sVZ&B}?Kp8{Rk^0gXM$sufm)mAKV`)YqmG=a9DdAEFssSDvl^Psk^Bl*KNnX;>lL}i?q93f?o%<r0jW*VmODL>2I_LMWAiEuZdV)3RN5W0;DDa%8gZQK+LQG>B1fZ)44+27a+y38?=%Lqp`%jlvjBFqFB|Xn7`mQjkTC-$!NWa6in5Y3rMSm_hn7|y5lT27f~^MHs4do!^w~dUnRp>{ifP6}n6K$40XE2@A1^x}K~{R@<I6s@7cQGpT6Ghtt-Pv{EzlbyN6Yk0(q*uS2ll=-LYIoE#O+oghL#=m*oY2`2vS@Kl*Mo%ZN6mpg&=+8MI+7K49;{`VTBe$VjPQ7lw3IHIvAq8t(a9;N!H0Ci}pLib9(vR&A<@Q{<XMzMvcFuM}3uwI2)<IrpY`tkL3z15hp#PgsBS&Wx$>>b3aZnB~rd1N?A&?I#IFC@rxBiG5~^y`%n8;)JHwE0$aC7xQ6ACKTw@|#8^J2P*ck=k@+kVumv%w5vXO#7)r(7>8`&5pzrdg'),'Libraries/Compiler/to_ast.☾':strd('c$~diUvJ#T5r5aGVED9jSV3~$1RPRXQr)1kWmqy0z%>Ypw~`LNBUzGXpHKvlEm^UxI?;bCY1CRaocdqfq$m=(jgyB3^4ibP`veC11v2}G%O$zIJ1am1-I2H4otd4TncvJ1ku`Gn!t8I6<IuYg&Rv+fIOjMBnGwDoH4+@fre!ZSgL$_ZBg;mnX<3%dXOB-#o}HdKGd?}*OiWLWpNDmf-0!B)h_cAC+33s#7_}}V^ebc3u&gUXsFL?$<hF+EZsO{AR}iCX#%lE2i9&R4W|ETMB~QtkO^(O`xlucNar~Tx$W8KR@(h@~IlRBwUAgn-aQ|DAlFh~s*4}3i?mv5<b37t@WZV7?h=DDOvvRzkrSPLyN@9!bBMY6Y!R<5h0I1Pvl>7(zA?zpJ+fV+p8hcSAq_>RGT-44Oz@u;g26S41K~J(Rx8V;!mQE{>RcY1nf{_G{8z%^~vrqm`eqh({#r11({l>oTM!pj-1yNF?Ywd*~^02eeZZ<)b#9OK{wc7RhMJIHl7)P}c_5+q&cbJ$-gt3@)>J(7@lsvJ<h79=Y!+WfT-Ziq*>L+Q0TfsF9?A&+>$2D=>!wU)MNuC;5B(*KnbX)Uv*8t_bBs*hpc}#YZv}itjdE|;PR~SNOVp_^im~u>BB60(4^B+Ze%zST<=j3&2ymZ~frHcrS+LrytkLa20lTCVgO;*7*e%~1xrw1fh+rk0%$UU-~(m<v`r@$mdz~O|B*fCDrB#ER0pBAFR?Pzv8B6cu2HI3c_|9kI>%_&hD;D_Q=#2&dBx98(_*iZM;;(-AYlgDZqTc%0`N57sM9lfFmG-}ZSDFV1G`CeE$wPr!po}4;!>1-{tHz9Rn!6=&@H#7PNi|>(dn7nY6^g;7;k?UP;_=^U2I*6B?Ap1(9WkVqX^2?=`9PY!qH~UG<`8F0BxSsNs{Bz2%hNBkJSZ`_$U<*dWH+Tr7;g4I3B;+~Z@{yNu?|rD*LbqOb=9__cHP-B20F4tuh|oPp;xF5U@W?lZo8N&u%FU!luFM3hMqW+tW6aEU$QMl99r8DEJrLIiNaKVz0a1?g-UCMvCz0ZMFsus^QpZ%Lq$XE!=%MSVF*g>FdK$Hw!T0H0z2^8XMG^}`SVDb;Kb87rPl{1SG4o@(lT?E;;-^XnshtFT8Wf)%935)-bqJ1yx!t=DojUe<hfFD(m!Wy4q@T7a1?s78D>kLB%5q&_YQ$H0wh~4dKnB3YNe6Rt6`<eR08M<$uzqW!yS_#Ll^;9u$Bz1BCw+3b0t270+uh?ghkG}vfF*O3k@#uOkPgUa7C*%2a9F9n?M(BPLa%a3K9(}U-Ok&yzD2e<y^ld>ZzTcU_wKP&LB+lcZV0ED4J680XKX~?R`OGg{ZgSV!}aSB-5!y<<X`C&I$<<@lyg+R6kt4by0=$^>%Hx1eM0`pBhQb$l~#&wluxhd=eJw)V5yoJzg8n(rHTp~3PP!$nX?XL%P0#n!z?l0Bd;wU?f>`P@m=_Az~@i!x!3*bLHDbN-Sy4x`gZrlt?plrx{vP&eVq?{T-YH^1)WUBJZ@zfkyMp{_g5Ntr{hOOfM??eWF<F#x&rt!zVxg<hc#+=d?2omR5bB|a2Y^?`{F}6g9`&@>8TJX;94q`PwJ;pP+ndwsfY(;O^En3OCE*n%xbZkKr(Ls&SjA>_=9N~?;0YVR5ymL;SkWtF@I5lSJ?d9DL}h%4(fc9RK3G)7-GMUDqQa+d0`1%+3BH_Xi^9>24L0jA>&KXh+WC-d4Fa@l|QIvxOHbL(VV<iA{kvET{bPw{S_DiwF9d!OK^~ZSqgoZ83K|13?rPhBj4ckG})#uRpT7W5P>S(v*3%p4hxyXW-k7wx9Lt;0+h+5f<dPQBFdx!lH{o>Nc4#L7tf)3>?Tdko@c`udKA+DOHFW^ZqhGnXR;)%kVk2$c8UTvBxXS!J3&~;m^!q%5(VwhN!(}=CvgRG1yEZAK5fBNqZi~`nx~6V2x))Mq#tre-DA4v1pDyVO=#6!Sr?Qnt)sIuR_Hmn6Dm?l{Z`dPI#8W3%c(^UQu)O0=E}tQ96by%8RhVoky9H1^ucLfiVJg;J+9o;%-phR8~}|VGWdSzUEzV~Wax!aCD+L$BYPjw&R?3IKDlVB)oPEh4A@Mt&&aERTPS^e=$$koC|wlZ`zlmK#nR)$0g6ys%XG~0T4qvEN!8mPcF3pX>w*)~%GraAH3%JV$px(F;Y$gQd^cLw&ft!Yo4CrGQX=iR;V<@h?#7Efg#cl-zIvh@cA_GQ9myrJ+~qdbs#1E*QHTWIQ)?3Ma@=fq7>%+dmlY;ZN!I!nCxZrwoYZ`-T_v(oY4Gwa!=Iv%3RI)`4{bMI^4w&sro&nV+$bm(FfRo>j%4d(E0-io89Vm!SRS6)bsH#2q!}2$Ur_u`qov)Ux&Znj9u)W0YB&EM``Qy??}+PP)9Z=%w{ff2<_1QwQeO*TEpfcS@0%V#POg;in?I&)gOxjgzwiykXTcIXnF(_7Pjz_TIMZA?m{F;v32Fn~Abqj!?E_O2Ww{vA5=zNRq2*JNFq|L^^=~%(f<D65YTxEdm7IDpExnRaPR%s#$*vm@D6Ftgn=+P2oB5=CEK{0vg7bgxf1#wnvW-|cKQ`+G-La>_%f6&GuzzG)s*;qx<Z|qIZnHU%<6Q3J=xId`#r5o^GZ!w-OpL31A(-=&{mVl8^)X$!NuCs{jVy)A+Fdz>XRpT`uMv6eh8CT@b`&i`;OU9ni@4Jddeg@F{oC-l!-|90g>ueKGz9{4#F92``U-A~Z0NL_ZJHuhRo7i&cv_j240%=WZ<?yC)Ze3>Nu4!T18Dw8aL2=8!r!-iZn!ahXY*)~*FaNI1o<pP<7-gP)7L>sV2sbsy`#R8iQGnv8O7`kQCdz5N<%~P-MTaNA$=o0>o`b#3C>@;nl`@z^`8MWJ4PD'),'Libraries/Compiler/ast_to_py.☾':strd('c%0Q6Yi|@s@;kp`vXY~2GdT8=yXaOdcf|M}iW4m0&`CaLwcZ_vmDjtIopEemLS$aXCLzIKJ3Ir#A-o|WFCY*kw{&0cH^d+BLoQPOz*Y5YdR{wgxG%Se-JYKAdUaKGRdsu;)ts;<8?{Qa>Qu{q*{V&r&6aP~yi%jtnkd(6|8T0C#&FcQGc(m}Rn>^`sd~-xHxYJ(9Ut2BXHqI*>o2bl?b^M!R3aqTa;91}-)VU{YQI%)j+W~lp*G3oD5bU-y<_LjKMn4Bb;sbIQvcw<jyGT)2lv_l=`|)%oA>S-f?hgI$QG;5qI3jsUtu4zlZ7HX#1`2Kq1bVP-70ymQ^C$p+0p(TdkM78vztKD`i0Z$vkQA$lg|3VOY0Xtfrmc=2L7~i1)kn$Hk=&dlK`ph`PI_+R5cOW+)bF$a{S3w10mc!1dlT{r(T7pU%#CD1|F+U9be5of_A0Z@M{f$``A_J7;QP_@i4m4`go~QZ=|7IdkWKPV+i5F8E86n{;+n1w*@2fv+yw1Y#|X}&Elv^z3h2$JSjMSo;?n8{MHQT;`}l~t2N5?`b-!^(=}!jc9PArC7AyH`(0gczWL&d@4dHu`?hVHH?Q5>vSrKq2S>Zv_b-7a4ChCvwb=@U`0!&u@X||2`G<$0+1-uJ1(eVBB5!^U&26HId=^FXGBjV{&H3xl<ovGBUxQ}3Q4M#m-G)}9>GR%slptTP`32E!iN}Sb_{QVSW4vj>ORlY&X-YSdfj9aKMUrE)>>%_X2Gu;u=GZY{e}NrmAAm-lU>~uMK_H9l6g$n9*fLvTXV_VG4tT!6E`rQ1vCE*UpRrZ;IlIcfVAt4nc7xqyx7clVhuvlO*q7`pcAtICzG2_8@7M$OkUe5Qu*d8PdzwQkcK7cr6#M_Wdp9BV^2BJhj3T|uPTTzFQ~`cg*taCq37nAfXl2K%{eAhZum~hq$_bwK3=L#M`#KH{WWnLEA0;5CQ7IH(-?cLW2LU`_cL|8>47(qDc?5*=9lK3r<BmiGf?oxZK0-9q?l0mGrTV2t3wW!}v*W!(0s<t1323Pr^{E;a;71CE2KKe10N((BCHQyEhP6M#4i-UJ++`hO4;4&UR?5Ew(0v0#8wHv$nh!e&%JoDIg7v1FSp@JITSOV!YUXqSO!L9rF7Nj_+C`>q$!3IF1jD}sweC#G@hT<HZ*i9licJKewxl3o4G8#vzfbn|{-%Gj%R^j}C%ztvT+;Vj;WMPSdD#ZLduXhQ)))$u*2ai@1k1MG?M4jKy*uFl?*u0N&cDLH^Z5PBtNeQ>Eam}9(T{3yk~5&=G&=%juf$X2+^pI&Me?%M4HjU*WJBAYg8I~J4aXzXV)p{$A|!89``rUJFgAlm^n@KoBjVHv`>8r(mNV^w2P>65zvRv!gUjGX9^0T_Mfgt(n=JU$#w?=W(H@8P>=iHYBeo<<z2^N%vwW*q1k!)G_{lu{UqB8t3>-QE%ZSQx7FS%(8txsjbsK!SF$F)w7y2qZrdq$@5sI7hN$`#5$%LJtqJ;GEbyI@x@%7rRFFaab_~EB-FZ}z$Wn+avnrSnBTDl$@*qbmA**<pxr7qSR`Fz6e)8G^4s|<@zeBfTFmv9jL8HL!VaSa2@C)stNg5Y-9EiHf#we>rjFL&@v;h94=0c%Y>#~za;nqc}O`=U@x@ouQIw}k56Ft|6+7Li2tO7bQtPzE4qkT7z;ezkf-xjaH7yC1P{h!UqQv38dwL**D3V97q$oG3RkkktBVtDe4~$#rXvEh^2@s@MlA=EJwm4J~;SL(-PnkNo$v{Jo@pr5H|uglxn5ZO`!`ik;AbX<iZo&Ay=7D}&UX1A}BM1gTp`V$5+mQHwI@(5nNy<^)*9qTMZ)oclQ0RO+k6V92$N<%0?680?peix}|y^Hd48fRbBol_xM<G)&u=3i2S8Voc4Y+g^q+M(;9Gq#p?LOL9Dm$6&Sv?#|MBrv^#0(&__7#FZ|9QpvI>PCkanao#!dxnC}x{66OOlIV;K!w*E*Rs}!>!^7_-I0zwu^@;&&=>eCm$_8SSa4-tlFXHIsLts=w-ffjPSFKebShc$=it&&V7?Ma_hdI3t7!b$SBIf4Pjg{moIT}0$iqdUtyRY!|LE9?(e(Tw7s}ltkJAB9)ccw%-C`i{NCBDPCjakcv=xDFZN<*J^O2Y6nkTBAb6jriGFk^^ha`X_dUaL5y&&G_Lw%Iv5pzPQ0AAXW8oc7kmegtJk^U_l@kglJ|ltu?QUmMs6PGI!R{{ZQ(p^YGgb^oY6(pXTGs0Xwsvf07g5w&xK{SoeRVtWuSEA&Fq1z8BHN_+&yIR^2oT%q_blP#UMgu{x+hqjl{o@^0iWA+j;XX1TsC6wXMM)9t8g7=)nb5;JXqJmHrMBXrS4#VOL#fYM0n&N!aDz2~<cE3<G;fF&2BF7}<NK&I9ALT=U0E_aFLR2GZPt(<dI5m9Zg8ht_8YvQt(VN;prD_XU81<`6!l-!~VYwKWSJ{CHAM2V_M1VB5VY?W4#)GVF)>chx4z!CiBC@w-8LM(JK!Ujowq8!31(8p{zhpkQc5m(W`?-W9rK89(RGn}s88+58SbB@+D_ZW{l4YnA2!A*jKzn#zx6Gc5;2v^_&9Y<W=3&XbC%oz8<))Lo1q)5{94j6X#rOm&>?pel`)<dZU4)FbS}**cq4i!Pv6Mu3#24g;SW2+8+tewuf?4t=M{|*6R4X%IN}lEG{0s~7E0M6>YlyV-V|Ixfp^WmlnPczeP%kR99jG~WbQEcc`i>NOTJ1?OD6}Z9ibxGL3R_(7MQuq?wFC*z5kS`kZj0o3DX2@zCscGmv1-d!G<NYc3&wekNWyKDp8_5uv1vX}1$X8K+ZCu8WL{jFos=Dr&1j;Y;Z{K!qn*Z_qV6``d4(?@t?=D8DNt6;%YE7L$tph(%AhqVfdzWbu(MRxKeU%I&Y5Tr1O-XN*~tWV9#`>1u_N(zn|cu4Ib{%Kc7?Rj49k<oMnWYWDVbhPS1BW^)qxs`6t_b@|4$i>6kAsDV9G7kYrd$uD2&gco=8jFdnLL1pfV1vWp<c|gIrq^C{9GhS*ScM)g`~7fqjW~7?imCbctIOxNUXF)Uo2f{Z6^{e70)3$SzOq16}FVZ^$e!&Soe4k!&{VfintI7iXQfLGt5Mpc%`jI>Iz;9OQ<xE3gu7GU@S#8F3Wb(kH^{<DX%jFk^|ryV4(0(>{6jA<OEfIqKz!?n}XBJT8$XY$F{ALF$V`QpIekm&V|HWO6=fvUCSDvX>UJ3lW|_;g{CuXEV~}u)#(oIkmr5cSs;HQM!j5<VA}!b}Ht$uuv&a?!{0e{;f5LbYJRq-b~30%H3+|8#uSN!6{c&f#RbuN|FW9oPls_2%)NqN~%U^NGIBhx6+(&H!j{tX+j-^7(`_YFj08VDmxgKOA*hrNX2(rjgG66;qr{hDOF@8)^0cpq1Pc%bWp*>Rq2>axrE6H6?YzOYMF&}9<#|5wUCWhIipCkJOw)F=Pum{AgF}#yl0MG4M_|#7a3DY2w&jQ>&g`_5=$jL*dnRp07e+DzN)427<rbQl8woO<C`L7;b}qmG}79FM?xe8zo?UN0`!4qG@Vix7()4|5JyUO97%x-Di-P_wp~AeuT!0#s`>k^R0GqFSWi$s*4k`I?@FT@W*k%p1s|X*A3s^n;N$1n<7-#&E?AfwQ-Orl(VnvFI*lp`Q64U?#Yox?iyAGaVC`h7P;3{qgk}i3`K&<e1X+qWRV0tH5wN2m&>pwxf?NP+M_l12<!n&EOF*VdCaTZ}%}Q`;7A=ZY%!)`*4S|)!7)4SEdb~eYPXVRr4|SSSRH95Tu*B#!h)g}{bEYef>&wWj-|zyck^Q{1)NdH4ipL<VJ{9rRR@u{F!dEZ)h2BI!{O91!#IWr7PZ~pOoK*iaRW+_KQY2ko!R2=`Wiq08wqvLE8Cj&fmWr21gBzpr30f)HWV~QHY+@MMU@arT6L98h4bN%$pktvzYew(}EVyIS>8J71hF=hYbX9V>p+yK=ZDy$MWoBMjVGHdfIx#)LmW&c;C@9X71T0|;v2+#sa$fk3*fd@a<5rTiDPaFlyv|zfxX3E6lf^f$q3{V!YME7Sp<^wVwB2KQwT33%4^u-buBy|@+G`Lh=nGC-4tACE&np`8_yt1%aXpWZKc0Hx+}TpvL*Xj}Dw_>%-lRz{SyqwDf8zcUU)^vG9dw9a76f}OwVbzV%?25?-QaQ{hyES(LE{2DYpT;=p(t)94pM_m)I}GT5p~eTO(k}naCmSS2aHHTxfnXT;3DbBNQ~R0u~M$xWKi}Be4D|G+Z-dP5KhbMX?%-PC^)+lWmmDg=XK3*aNltW#B)Z7?M_y_$wF6I^PvdU5G%(ctacN@b*a>ya--w~mqB%vr#W8a_Ye2F|2ha-aG+qU80tPd3~}bIw(5<#;UwIk<iaD8!X<Xiu$eaSP`<EhG{;rE%FhV3B?x}X)oRIYdI|j0ioJ!v`vkl=W(?q(F#xIA@hW8WqH2)6@@>Va8|K7}T%mTr7PtIF4UtzWZ=2Mnc?l65XyNF+3e>EoWbmx90C$o?X5JJiVxrIrfp@uze-9D5ZzWbYewSNT?%pLiRGdH?TpN_h?AUw2PSuUDhj7#Z6fTfBo;Kg{u!&DJYoE5s8<qEwvCnUY?jrNB_MVMa;<p^9C>(5~2{zLxPdKG_$}LZJwj388<Pd4E8W3zjcv|?Fkd#Z$-MVZKUYN&!VI&DxWMPMBNyld5G5^jbQYf_ztETo?tzIvwSEc>Uy5p5b%U-RbfVwl4P-3EWjK59+uZ7xfkkW1Ckd=HpyxEQCxKi9!+<gPt#&GdBT!1vRN5M1gnQU+nL_CQ$Oh*5w|7xo=@HhNBuRWy_G5@qnt4hw+P3(saEXQ{-Xzv>s%GvM*@cs+belxB'),'Libraries/Compiler/main.☾':strd('c$}?T?{3`25&y2IpjjB$HR!V>BMopcQ%LeT793lGBnJT$fuN3icZ7N5fu!tH4S#SNyKR~xt`nzD8Yc*Xv<;f3HCm)WY9}A~CVqkdeSyyGF3DYzC!M4_SmvMIot>STo%ziyNjLJC)AIx7blvX25BqI<E8b&tj%;0BZ`;Eg9?AZR_ZL?;tn97q)9l{L(iSQ295LFlvIp7Y>|fMM1}=r)92qdzW3khXhHX2$3ynW!Kfv{)?AL?@?r_(04IuMP_P)h058FWD-Rv2`31tH@PbaMxkAE=fY4Pfz1*BUsOQPT=gInx7jH1x-{1|#K@A*OMhlxq4mA#!k$-d1#C4#XDJ<siyLj>C+Hys52uHz3!QJl7IV)o)_Xvo)wcx|l1qv0mT>EzA5`T6-J-X}`(W)|M`<0w>n<dYjVwzm2#CD^dIcy(><nzOvL*>OO|;uWn8Ih_>TQ^W5WMH34WhON0CXlvxgEKH@yq?U;J(~}2ZnbcbEyiP6kJ@C@>dQx}wJxVK$oY6iADOc#{*@xLbtTS-^L-srCjJSE!&f9AZZjw5j2FaTQ2|K4GJ96E4OfH;{a6GoV*C(=LGKg+DK#iNPc#8HaPfi#)ARBkc>`N}lO*D*RhU1hsekh-c+1qml{6OxqT|DCtg!7l|GqSw)21)%iU?8K_Yo;nRl|kHYd?`4T|3|=1A7u}-XKfo+1&rkVz1_aU$Mj=&=%g`Yw!*F=7>zY(DtSZN@2qcL2IIiH)vN1k8(WS8ERI;eAF%W11nnpa!2Yd%5beUU35ETE+ri?)*Vf5ArQ3v@H5Lp?cgmH2p8Y<13VWJgi*>-@rOho<U*qS{_A9<Z(6m?}CB=T1BWbHUifLs*n%WK&``UGwwG^|QRF}3w^+>d)VcaU%bZ)wFBK)X6eazCmI5Y%jbKIU$#$JTp1_WQ28P{BC>a;a*6DM$gx$gv#>y@lag1R{!tn#=&cKT7!b5n3oN7MRb;wc-aPA`gwZaOQHE75QS9xXm6w#CfJ7M|yrlq(vt^7q8lbY;@AiCct~u+&Y{SP;6>A&asD+%A;2^K#t9&THg6aB+U8w3l+)+*$C;6TG~a{Z*Qgv{J>usA`0|N$b9cI~O2G#U0X|n>)$MxjQ|<(kpX1Jwz+4ZHp`Ejcf?-D@!YvJBU+=*%ey$oYM&g!sWHKt<9~CrFG}>(&pvuB=Eb8T#G_xE&QDBKp?Yt@QlJ>Uu@gz8mqBKm%DxYjubuIDVvxK+TgR@W+g!w4-L|V*s1PwXnc@8rL?xiyW4}Enj<Mx(k(?jP!vL%<wpG;sR2KVNTRlGI)QmqrJu6lF|4>?y4i+=1XSYznI7MAP;b&2im*_u=ef;|AiJM^X_wqsLDUxjKy}Exzu_kaH;{%POKKrMhs1J|fp?KD0Ei2Yx94}DL6FzpFYG9*S)ll$A*9wPg~gOHRN*^}QUjN(@h+(l^Jk|MgTUX5&%OmXDFLX15Yut&0$sLk1&E%5emUF}{l#vRbJ7;ZLM!_sdnfxocQnc)2Ina-XVYB?<nyUw7PzT@lYs_d@ZIc_>?3N$48yXR%BsKs&~Xg`6w$#05#YZU_a7Q!O;^`0ig5o`_8cib&hFY?l*ay$R`ve8nE(7s)H-OOZ2JJ(-p<={hfK^j$MZ`jMx>vf{PDlIAC5^5<vfYp0pNt>y9PC%v~8rW=WT7ce3yNLaOmIJy*y__i(R?CLCAtdt=lHZ*=*yMxnrr@5Ec9!v?4%~m9tmC{5}g=?551wjiNM3V|PS61}I%5qtG8spoPIZ_mxCCvoH$VwvrCr^3#En?Dcy77^EPwNxAG|>#o1%Tw2?>LNpFbdYnt{6>@fo)3AkM<4v`J$!Nc;q)bAVumew>+x5e9qy2Ocg<?PHam&tANnw%`wg~C~bMV~y#T$wyP>!!&k)EFTDm$=D<Sor6s3jqWw>KQ|FaiNrj4s=_JF*m1k7`tQ9=gb{NuddBEj_=outKb8+3#lGpcXhOyUF=4g0vTRED$s;on4dwP#+8<j}NrwqnBTPsc!!;Mj$PKvt0&=UaZKGOOJ^TuQY_Yi3ZmVm>W~A&(^xb!HM3OJDpWN0fb;<0!F8YVA^S*{fqnGAA)Qf_|ahfVO&hk0gg4dT-4O7pW&QZT0E`rC#KTJ;-pAZkZj9yQ}=LAn#RnMliVdoBfLiO6v8=h@C<p&sUCr&a>xw%2oY7M`y+M~*{FkN$P1Q?j=+WJKI8eFbUcOUXc#g>KG=A46uS`JXE?uz^G7j=V#Ex&h}o?e61F34T4l^E?LyXbrnicw0?^5LP>MfOvoWb)bRtfQ`4JHw%EM7+7IXnTUfWz>eXZkcbS@FnrL9Vaui_L@+?D`N#Y7Sj)j_!vK+Z*~Rs9^1OR^Jy6y%N#D4%DKKnyXp-;)obHbKmyn?(K^kjm~sHiFgYX9y_GS0!!FC`O&)`A=`Y$1{Mkq|*(20^lWfyZJGI?~0RyIIxv;UmosYN4D#BZxl(k?;39C8F8TG*0OU9;5qO^R>IKBtD9TSB~Xc$ycdUTpw`DfAWP1`Par<wLapJA9xah<6Y?*p7TG7sr^f8q^>T6?yQ{_dQEv>K=)!yP$rD2g3qb^k0oEohHB30>egsM1Q^F7SzK~74J_&fA_~B?Tt<)KK*`qM=Fi~qhjwAGdfzVM)Kb#Ob16HvOY;ue6U0JDmEBhFXOB~xByBt*t74?WE62YpWaIb8HVkf^Ed012FN0E2RR8*sqivyj8q7d#^HI0-CY$hf}XxO$v%x-{=qme_N<s|zF3IjVrx-p5rMzd8m6i*n(3(MOJOY-Il&l7v&`stPfi|Ir9*dIW=fGo&T=Hy3|jWZldrh)Ovl`l1W*LO>0E_EQ5hF<Ti(*ve1D}2H^+$N?Fw!>l&uBdMCsz6e&3P6|9R8;}|rSZOTklmHrPB0!OR>;d<!dvk=CcEhdko(J{Pe1fiCrs4SP2ebs9pR~MWKUJqxXVVVINJNTJ#v#|3f`t*s`Ex?#ksb$wfcJJh`cqkh6n4}d)XJ0tcsVVN;N}Iixh5~wnUcd2$Fsj@{(cc#|nGP9lQ(<wW2((t?YPffcv;o9<GZ`@sQQUU19sXksEufA=qHN2XAnl56~?)uT*edZIa8Lx7gTEt4rcx50(=qJPPyRhjII1_FW#gxhlM<o0L_mcHtAQCvKm$jTgVUXViWKh(Sn&?I#LL^7RE?O2hinD@D(EFEk*~89W+kz0VHnbde(?1%FxT+BGilpaED02qJZY_TRw6*_DQ_W7cizx@=qk%pd>`mWp1{o0)L|+K><nkz}RWE1Esl&>Tr|_`rj>i}uoAB&i3NS4vP*I-PB)ogMVL9{^CG`AGu2tUH|ERNh9|swBdr0DpKtd%taqmq-o%M8G-A8EdQ217am^u`ja^%IaNDE8RWH9;<b`YV{aaChp{U+=9hVCw6$0mz7MNfjsU*13#HkEM2aIwnov2RtR!{pv$FJDU^#hPQhf0#+hQtwB3zDK<s-ZfJ361cYsZ?Ve;d=9@Q$FjmNJ_+azGD9`o>`GEvXUP&yo_poBk!$z81L_oz_{2$j+>zcukQoZ444)gIcXGTaWoB|ZGqLw+}<oHz+{5cXz?V>C2F1oMTNNI*}N%te5G)S+loh;Wz6O<A?U1J)_u<=|d2$AXiwC!}7SUm>fx%%|d3Ggi!MxUtq^N)b*~m?Ac0aiR!O^ESd}amWD}r0jyP`KcYeZKfgX=knx^58z*|@DYf`T|dN!J0f=HMl-hd+e#cK@NDf<Rkn&<w9MwkYj-?KbG~4N!Erx7EkGCEOt!0$tvD2Z{&hF|TX`}D4S&l1PK%={9>X-xF+D%c4E^svPk(zNo_Gh&SJ6R2ky*02auRhYN^hn<(5WlM1OySyWBM#T3uap73o%CVp`#qAWe*3rRegqwwG@erdDbA(My;h0y5+w*gliC_U`xO{i;QW@9gSG%(b_l(^*U>pItX?rA-w#z3oiGDQEQr;_)r1Cce5YCUGa?V%k0mjlI8H!M?HR3k~UqMUQL=!d6hDyv?QKeNpqT<VpV5j2h3KVgMTp~=9o-!xrt;`MyR_<YeLa$@<h8cn`rVJQGE`12!9vI6@uBGw-&6$oigx`+a(A3S24xwu^MN101#e4hC_a|zlcZscSNtRtuX{Ud7jVXBt92VggabH4=o4qP+rtYLvUrj$FVs{Xj^`S(ZesbYVM_$;E3|+(#4BT=M8x(OVqMy33g0N{RT;G5im$?7jJ0!ahW&-H>+pj=-R4^G@FzQJ@quqwDjkKBi^Qf8NH~h7IP8c<k4IJ=Q5m2gQ=!|dA+rYndcNeH96h6{{wXbj6e')})
#main.☾ (6359 ⟶ 10948)
__dir__=(__file__:=áÌî(moon_dir/'Libraries/Compiler/main.☾')).parent
(code_file_caching:=True)
(TMP:=mkd(ð(TMPDIR,ÂÞÅCAT(ÂÞÅCAT(__file__,ÐØó),sha))))
(header_com:=ÁØÿþÁÙÇ((lambda ÂîÓ,ÂîÒ:ÐÌü((ð(ÂîÓ,("%s.☾")%(ÂîÒ,))).resolve)))(ð(moon_dir,("Builtins")),ÄÝöÞ(ÐØó(ð(moon_dir,("Builtins/builtins"))))))
(pathlib_import:=("from pathlib import Path as %s\u000Afrom os import environ as %s\u000Amoon_dir = env.get(\u0022MOON_BASE_DIR\u0022)\u000Amoon_dir = %s(moon_dir) if moon_dir else %s(__file__).parent")%(ÂÞÅCAT(("𝐩"),PEV),ÂÞÅCAT(("env"),PEV),ÂÞÅCAT(("𝐩"),PEV),ÂÞÅCAT(("𝐩"),PEV),))
(to_py:=(lambda áÖï,*áÑË,**áÑÕ:(lambda *áÑË,**áÑÕ:ast_to_py(*áÑË,áÖï=áÖï,**áÑÕ))))
def moon_to_py_debug(áÖï,show_ast=True,show_out=True,show_out_no_rename=False,show_preast=False,show_in=False,**áÑÕ):
    if show_in:
        Âçß(BOX(title(("IN"),ÂÞÅCAT(áÖï,show_code))))
    
    (ÄÕÒü:=to_ast(áÖï,dbg_show_gram_tree=show_preast,**áÑÕ))
    if show_ast:
        (ÄÊPSH(__ÄÊIMPORT__(("peggle3/gram_tools"),globals(),(""))),ÄÊPOP(0))[((- 1 ))]
        áÍñþáÍñ(ÄÕÒü,("AST"))
    
    (áÕÃ:=to_py(áÖï)(ÐÌü((ÄÕÒü).cpr)))
    if show_out_no_rename:
        Âçß(BOX(title(("OUT"),show_code(áÕÃ))))
    
    if show_out:
        Âçß(BOX(title(("OUT"),show_code(to_py(áÖï)(ÐÌü((ÄÕÒü).cpr),no_rename_vars=True)))))
    
    return áÕÃ

def ÄÊdo_imps():
    if (ÄÊmoon_to_py).has_lazy_load:
        return 
    
    (ÄÊPSH(__ÄÊIMPORT__(("peggle3/rgx_golfatron"),globals(),(""))),ÄÊPOP(0))[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("text_format"),globals(),(""))),ÄÊPOP(0))[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/to_ast"),globals(),(""))),ÄÊPOP(0))[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/ast_to_py"),globals(),(""))),ÄÊPOP(0))[((- 1 ))]
    (ÄÊPSH(ÄÊmoon_to_py),ÄÊPSH(("has_lazy_load")),ÄÊPSH(True),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]

def ÄÊmoon_to_py(áÖï,áÖÝ,áÏè):
    ÐÌü(ÄÊdo_imps)
    return to_py(áÖï)(to_ast(áÖï,**áÖÝ),**áÏè)

(ÄÊPSH(ÄÊmoon_to_py),ÄÊPSH(("has_lazy_load")),ÄÊPSH(False),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
(ÄÊmoon_to_py_fcache:=fcache(fp=ð(CACHEDIR,("compiled_%s")%(BOOTSTRAP_HASH[slice(None,16)],)),file_only=True)(ÄÊmoon_to_py))
def moon_to_py(áÖï,áÖÝ={},áÏè={}):
    if ((h:=sha(áÖï,áÖÝ,áÏè)) in (c:=(moon_to_py).áÐñ)):
        return c[h]
    
    return (ÄÊPSH(c),ÄÊPSH(h),ÄÊPSH((((ÄÊmoon_to_py_fcache)if(code_file_caching)else(ÄÊmoon_to_py)))(áÖï,áÖÝ,áÏè)),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]

(ÄÊPSH(moon_to_py),ÄÊPSH(("áÐñ")),ÄÊPSH({}),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
def compile_code(áÖï,áÖý=None,Æå=moon_to_py,log=False):
    if (áÖý is True):
        (ÄÊPSH((ÂÞÅCAT(áÖï,ÐØó),áÖï)),((áÖï:=ÄÊPKE(0)[0]),(áÖý:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    
    (áÕÃ:=ÂÞÅCAT(áÖï,Æå))
    if (áÖý is not None):
        (áÕÃ:=("#%s (%s ⟶ %s)\u000A__dir__=(__file__:=%s(moon_dir/%s)).parent\u000A%s")%((áÖý).name,ãÊú(áÖï),ãÊú(áÕÃ),ÂÞÅCAT(("𝐩"),PEV),ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(moon_dir,(áÖý).relative_to),ÁÜÙ),repr),áÕÃ,))
    
    if log:
        Âçß(("Compiled %s %s → %s")%(MOD(ÄÕéý,áØÁ=dotrim)(ÂÞÅCAT(áÖý,ÁÜÙ),35),MOD(ÄÕéý,áØÁ=dotrim)(MOD(ÄÔéÄ,áØÁ=áÖï)(("\x0A"),("𝗻")),35),MOD(ÄÕéý,áØÁ=dotrim)(MOD(ÄÔéÄ,áØÁ=áÕÃ)(("\x0A"),("𝗻")),35),))
    
    return áÕÃ

(compile_files:=MOD((lambda ÂîÓ:Âøî(ÐôÅ(ÂîÓ,ÄÊCUR((1,),{"log":True},compile_code,ÂýÃ,True)),("\x0A")))))
def generate_bootstrap(dest=ð(TMP,("moon.py"))):
    (file_canon:=(__file__).with_suffix((".☾")))
    (ÄÊPSH(PL_FORK(compile_code,file_canon,True,log=True)),((_:=ÄÊPKE(0)[0]),(Æå:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    (pyc:=(lambda ÂîÓ:("#!/bin/python\u000ABOOTSTRAP_HASH=%s\u000A%s")%(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ,sha),repr),ÂîÓ,))(("%s\u000A%s\u000A%s\u000A%s")%(pathlib_import,ÂÞÅCAT(header_com,compile_files),ÐÌü(dump_cached_imports),ÐÌü(Æå),)))
    if dest:
        ÐØì((ÄÊPSH(dest),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),áÌî)),(dest:=ÄÊPKE(0)),ÄÊDEL(2))[2],pyc)
        (os).chmod(dest,0o775)
    
    return pyc

def force_reimport_compiler():
    ÐÌü((__ÄÊIMPORTS__).clear)
    ÐÌü((TP_CACHE).clear)
    Âçß(("Importing peggle3/rgx_golfatron"))
    (ÄÊPSH(__ÄÊIMPORT__(("peggle3/rgx_golfatron"),globals(),("↺"))),ÄÊPOP(0))[((- 1 ))]
    Âçß(("Importing text_format"))
    (ÄÊPSH(__ÄÊIMPORT__(("text_format"),globals(),("↺"))),ÄÊPOP(0))[((- 1 ))]
    Âçß(("Importing peggle3"))
    (ÄÊPSH(__ÄÊIMPORT__(("peggle3"),globals(),("↺"))),ÄÊPOP(0))[((- 1 ))]
    Âçß(("Importing peggle3/gram_tools"))
    (ÄÊPSH(__ÄÊIMPORT__(("peggle3/gram_tools"),globals(),("↺"))),ÄÊPOP(0))[((- 1 ))]
    Âçß(("Importing Compiler/gram.data"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/gram.data"),globals(),("↺"))),ÄÊPOP(0))[((- 1 ))]
    Âçß(("Importing Compiler/generate_operators"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/generate_operators"),globals(),("↺"))),ÄÊPOP(0))[((- 1 ))]
    Âçß(("Importing Compiler/operator"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/operator"),globals(),("↺"))),ÄÊPOP(0))[((- 1 ))]
    Âçß(("Importing Compiler/node_types"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/node_types"),globals(),("↺"))),ÄÊPOP(0))[((- 1 ))]
    Âçß(("Importing Compiler/tree"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/tree"),globals(),("↺"))),ÄÊPOP(0))[((- 1 ))]
    Âçß(("Importing Compiler/tree_txt"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/tree_txt"),globals(),("↺"))),ÄÊPOP(0))[((- 1 ))]
    Âçß(("Importing Compiler/expr"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/expr"),globals(),("↺"))),ÄÊPOP(0))[((- 1 ))]
    Âçß(("Importing Compiler/lambdas"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/lambdas"),globals(),("↺"))),ÄÊPOP(0))[((- 1 ))]
    Âçß(("Importing Compiler/rewriters"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/rewriters"),globals(),("↺"))),ÄÊPOP(0))[((- 1 ))]
    Âçß(("Importing Compiler/to_ast"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/to_ast"),globals(),("↺"))),ÄÊPOP(0))[((- 1 ))]
    Âçß(("Importing Compiler/ast_to_py"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/ast_to_py"),globals(),("↺"))),ÄÊPOP(0))[((- 1 ))]
    Âçß(("Importing Compiler"))
    (c:=(ÄÊPSH(__ÄÊIMPORT__(("Compiler"),globals(),("↺"))),ÄÊPOP(0))[((- 1 ))])
    TRANSPILE_REF((c).ÄÊmoon_to_py)
    ÐÌü(show_imports)
    return c

def generate_bootstrap_live(*áÑË,**áÑÕ):
    (ÐÌü(force_reimport_compiler)).generate_bootstrap(((áÑË[0])if(áÑË)else(("bootstrap.py"))))
    Âçß(Åøþáüì(("Generated bootstrap!"),("f0f")))

def moon_cli(extract=False,ia=True,rl=True):
    import traceback
    if (ia and rl):
        import readline
        (HIST_FILE:=ÂÞÅCAT(ð(TMPDIR,("☾_cli_history")),mkf))
        ÂÞÅCAT(ÂÞÅCAT(HIST_FILE,ÁÜÙ),(readline).read_history_file)
    
    (pfx:=Åøþáüì(("✝ "),("f0a"),rl=rl))
    (ns:=ÄÕôñ(ÁØã))
    def Æå(input):
        (áÖï:=(ÄÊPSH(ns),ÄÊPSH(("__moon_code__")),ÄÊPSH(input(*((([pfx])if(ia)else(ÂÚü()))))),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3])
        if (not áÖï ):
            return Âçß(("God is good!"))
        
        if rl:
            (readline).write_history_file(HIST_FILE)
        
        if (áÖï == ("clr")):
            return (os).system(("clear"))
        
        if (ia and rl):
            Âçß(("%s\x1B[1A%s\x1B[K")%(pfx,ÂÞÅCAT(áÖï,__highlighter__),))
        else :
            Âçß(ÂÞÅCAT(áÖï,__highlighter__))
        
        (áÕÃ:=ÂÞÅCAT(áÖï,compile_code))
        Âçß(ÂÞÅCAT(ÂÞÅCAT(áÕÃ,VEP),__highlighter__))
        (ÄÊPSH((False,{("return_err"):True})),((s:=ÄÊPKE(0)[0]),(errp:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
        try :
            return Âçß(ÄÕôñ(áÕÃ,ns,native=True,Æå=eval,ret=True,init_ns=False,show_error_áÑÕ=errp))
        except áÍÚ:pass
        try :
            return ÄÕôñ(áÕÃ,ns,native=True,Æå=EXEC_NATIVE,ret=True,init_ns=False,show_error_áÑÕ=errp)
        except áÍÚ as Ïã:
            Âçß(Âøî(ÂÞÅCAT(Ïã,(traceback).format_exception),ÁØã))
        
    
    if extract:
        return Æå
    
    while(True):
        try :
            Æå(input)
        except KeyboardInterrupt as Ðáü:
            Âçß(ÁØã)
            ÂÞÅCAT(0,exit)
        
    

def transpiler_cli(*áÒø):
    (show_docs:=(lambda :Âçß(("Usage: ∅                  (cli mode)\u000A       <file_path>        (run ☾ file)\u000A       -h                 (show this)\u000A       -c <code_to_run>   (eval mode)\u000A       -C <code_to_run>   (exec mode)\u000A       -B <boostrap_dest>\u000A       -e <str_to_encode>\u000A       -d <str_to_decode>\u000A       -o <file_in> <file_out?stdout>"))))
    (ÄÊPSH(([*áÒø],ÂÔð())),((áÒø:=ÄÊPKE(0)[0]),(f:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    while((áÒø and ((áÓÓ:=áÒø[0])[0] == ("-")))):
        if not(ÂåÔ((ÄÊPSH(f),ÄÊPSH(ÂÕØ(ÄÊPKE(0),((lambda ÂîÓ:(([ÂîÓ[slice(1,None)]])if((ÂîÓ[0] == ("-")))else(ÂîÓ)))(ÂÞÅCAT(0,(áÒø).pop)[slice(1,None)])))),(f:=ÄÊPKE(0)),ÄÊDEL(2))[2],(áÓÓ != (2 * ("-"))))):continue
        None
    
    if (("R") in f):
        ÐÌü(ÄÊdo_imps)
        ÐÌü(force_reimport_compiler)
    
    (Æå:=((moon_to_py)if((not ÂÕÖ(("aA"),f) ))else(ÂåÔ(ÐÌü(ÄÊdo_imps),(lambda *áÑË,**áÑÕ:moon_to_py_debug(*áÑË,**áÑÕ,show_preast=ÂÔö(f,("A"))))))))
    if (((ÄÊDEL(1),False)[1])if(ÄÊPSH(f))else(((ÄÊPOP(0))if(áÒø)else((ÄÊDEL(1),True)[1])))):
        ÂåÔ(ÐÌü(ÄÊdo_imps),ÐÌü(moon_cli))
    elif (((ÄÊDEL(1),False)[1])if(ÄÊPSH(f))else(((ÄÊPOP(0))if((not ãÊú(áÒø) ))else((ÄÊDEL(1),True)[1])))):
        ÂÞÅCAT(0,(áÑË).pop)
        return ÄÕôñ(ÂÞÅCAT(áÒø[0],ÐØó),ns={("__file__"):áÒø[0],("__dir__"):(ÂÞÅCAT(áÒø[0],áÌî)).parent,("__name__"):("__main__")},Æå=(lambda x,y:EXEC_NATIVE(x,y,y)))
    elif ÂÔö(f,(".")):
        ÂÞÅCAT(ÂÞÅCAT(Âøî(áÒø,(" ")),Æå),eval)
    elif ÂÔö(f,("c")):
        (lambda ÂîÓ:MOD(Áëý,áØÁ=ÂÛí)(ÂîÓ,Âçß))(ÂÞÅCAT(ÂÞÅCAT(Âøî(áÒø,(" ")),Æå),eval))
    elif ÂÔö(f,("󷱉")):
        (lambda ÂîÓ:MOD(Áëý,áØÁ=ÂÛí)(ÂîÓ,MOD(Âçß,áØÁ=ÁØã)))(ÂÞÅCAT(ÂÞÅCAT(Âøî(áÒø,(" ")),Æå),eval))
    elif ÂÔö(f,("C")):
        ÂÞÅCAT(ÂÞÅCAT(Âøî(áÒø,(" ")),Æå),EXEC_NATIVE)
    elif ÂÔö(f,("h")):
        ÐÌü(show_docs)
    elif ÂÔö(f,("get-dir")):
        Âçß(moon_dir)
    else :
        ÐÌü(ÄÊdo_imps)
        if ÂÔö(f,("D")):
            (x:=ÂÚü())
            while(True):
                try :
                    ÂÞÅCAT(ÐÌü(input),(x).append)
                except EOFError as Ðáü:
                    break 
                
            
            Âçß(Âøî(Áÿú(x,Âåæ(__highlighter__,VEP)),("\x0A")))
        elif ÂÔö(f,("d")):
            Âçß(ÂÞÅCAT(Âøî(Áÿú(áÒø,VEP),(" ")),__highlighter__))
        elif ÂÔö(f,("e")):
            Âçß(Âøî(Áÿú(áÒø,PEV),(" ")))
        elif ÂÔö(f,("B")):
            ÂÞÅCAT(ÂÞÅCAT(áÒø[0],áÌî),generate_bootstrap_live)
        elif ÂÔö(f,("b")):
            ÂÞÅCAT(ÂÞÅCAT(áÒø[0],áÌî),generate_bootstrap)
        elif ÂÔö(f,("o")):
            ÐôÅ(Ááú(áÒø,[0,1,2]),(lambda x:ÂÞÅCAT(compile_code(ÂÞÅCAT(x[0],ÐØó),Æå=Æå),(((ÄÊCUR((2,),{},ÐØì,x[1],ÂýÃ))if(x[1])else(Âçß))))))
        else :
            ÂåÔ(Âçß(("Invalid mode(s): %s")%(f,)),ÐÌü(show_docs))
        
    

__ÄÊADD_EXPORTS__(globals(),("moon_to_py",moon_to_py),("moon_to_py_debug",moon_to_py_debug),("compile_files",compile_files),("generate_bootstrap",generate_bootstrap),("transpiler_cli",transpiler_cli),("moon_cli",moon_cli))
TRANSPILE_REF(moon_to_py)
if (__name__ == ("__main__")):
    transpiler_cli(*(áÑË[slice(1,None)]))
else :
    ÐÌü(ÄÊdo_imps)

