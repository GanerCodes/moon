#!/bin/python
BOOTSTRAP_HASH='f5tFXP7aT-kW_ShBCptH0rQlu_WUAPDqkoxE13QMFAA'
from pathlib import Path as áÌî
from os import environ as env
moon_dir = env.get("MOON_BASE_DIR")
moon_dir = áÌî(moon_dir) if moon_dir else áÌî(__file__).parent
#base.☾ (9465 ⟶ 20293)
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
from functools import partial as MOD,reduce,cache
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
(áÍÚþáÍÚ:=(BaseExceptionGroup,GeneratorExit,KeyboardInterrupt,Exception))
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
(ÂÀÇ:=(lambda áØÆ:((ÄÝöì(ÂÀÇ(ÄÝöì(áØÆ))))if(ÁØö(áØÆ,áÍÞ))else(((áØÆ[slice(None,None,((- 1 )))])if(ÁØö(áØÆ,((ÁÜÙ | áÍá) | áÍé)))else((((áØÆ).__reversed__())if(hasattr(áØÆ,("__reversed__")))else([*áØÆ][slice(None,None,((- 1 )))]))))))))
(ÄÝöí:=(lambda áØÆ=ÂÞÅ,áØÁ=ÂÞÅ:((chr(áØÆ))if(ÁØö(áØÆ,áÍÞ))else(((ord(áØÆ))if((ÁØö(áØÆ,ÁÜÙ) and (((ãÊú(áØÆ) == 1) and (áØÁ is not áÍá)))))else(MOD(Áëý,áØÁ=ÁØö(áØÆ[0],áÍÞ))(Áÿú(áØÆ,ÄÝöí),Âøî)))))))
(ÂÛê:=(lambda áØÆ,áØÁ=ÂÞÅ:((MOD(ÂÛê,áØÁ=((ÂÔö(áØÆ,(" ")) * (" ")) + (" ")))(áØÆ))if((áØÁ is ÂÞÅ))else(MOD(Áëý,áØÁ=(ãÊú(áØÁ) > 1))((áØÆ).split(áØÁ[0]),MOD(ÁØò((lambda ÂîÓ:MOD(ÂÛê,áØÁ=áØÁ[slice(1,None)])(ÂîÓ)))))))))
(Âäû:=(lambda áØÆ,áØÁ=ÂÞÅ:((ÄÝõé(Áÿú(ÄÝõé(áØÆ),MOD(Âäû,áØÁ=áØÁ))))if(MOD(ÁØö,áØÁ=ÂÕó)(áØÆ,ÂÐá))else(((áÍÞ(round(áØÆ)))if((áØÁ is ÂÞÅ))else(round(áØÆ,áØÁ)))))))
(ÄÊPSH((floor,ceil)),((Âüð:=ÄÊPKE(0)[0]),(Âüï:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda áØÆ:(áØÆ).real),(lambda áØÆ:(áØÆ).imag))),((ÄÝõè:=ÄÊPKE(0)[0]),(ÄÝõç:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÝõé:=(lambda áØÆ:((ÂÐá(*áØÆ))if(ÁØö(áØÆ,(áÍá | áÍé)))else((ÄÝõè(áØÆ),ÄÝõç(áØÆ))))))
(ÂÛÅ:=(lambda áØÆ,áØÁ=ÂÞÅ:MOD(ÄÕåØ,áØÁ=áØÁ)(áØÆ)))
(Âüá:=(ÁÜÙ).strip)
(ÂÕÀ:=(lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:(((MOD(î,áØÁ=áØÁ)(áØÆ),MOD(ì,áØÁ=áØÁ)(áØÆ)))if((áØÇ is ÂÞÅ))else((MOD(î,áØÁ=áØÁ)(áØÆ,áØÇ),MOD(ì,áØÁ=áØÁ)(áØÆ,áØÇ))))))
(Âù:=(lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:(((MOD(ì,áØÁ=áØÁ)(áØÆ),MOD(î,áØÁ=áØÁ)(áØÆ)))if((áØÇ is ÂÞÅ))else((MOD(ì,áØÁ=áØÁ)(áØÆ,áØÇ),MOD(î,áØÁ=áØÁ)(áØÆ,áØÇ))))))
def ì(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
    (v:=(((+ áØÆ ))if((áØÇ is ÂÞÅ))else((áØÆ + áØÇ))))
    return ((v)if((áØÁ is ÂÞÅ))else((v % MOD(Áëý,áØÁ=áÓö)(áØÁ,ãÊú))))

def î(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
    (v:=(((- áØÆ ))if((áØÇ is ÂÞÅ))else((áØÆ - áØÇ))))
    return ((v)if((áØÁ is ÂÞÅ))else((v % MOD(Áëý,áØÁ=áÓö)(áØÁ,ãÊú))))

def ÂØú(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
    return (((áØÆ * áØÇ))if((áØÁ is ÂÞÅ))else(((áØÆ * áØÇ) % MOD(Áëý,áØÁ=áÓö)(áØÁ,ãÊú))))

def ÄÃ(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
    return (((áØÆ / áØÇ))if((áØÁ is ÂÞÅ))else(((áØÆ / áØÇ) % MOD(Áëý,áØÁ=áÓö)(áØÁ,ãÊú))))

def ÃËÕ(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
    return (((áØÆ // áØÇ))if((áØÁ is ÂÞÅ))else(MOD(ÂÙû,áØÁ=(- MOD(Áëý,áØÁ=áÓö)(áØÁ,ãÊú) ))(áØÆ,áØÇ)))

def ÂÙû(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
    return (((áØÆ ** áØÇ))if((áØÁ is ÂÞÅ))else(pow(áØÆ,áØÇ,MOD(Áëý,áØÁ=áÓö)(áØÁ,ãÊú))))

def ÐÌü(Æå,*áÑË,**áÑÕ):
    if áÓó(Æå):
        return Æå(*áÑË,**áÑÕ)
    
    if áÓö(Æå):
        for x in(Æå):
            None
        
        return Æå
    
    ÂùÆ(False,("%s is not iterable or callable.")%(Æå,))

def ÂØô(áÍÒ,áØÁ=True):
    for áØÁ in(áÍÒ):
        if (not áØÁ ):
            break 
        
    
    return áØÁ

def ÂØõ(áÍÒ,áØÁ=False):
    for áØÁ in(áÍÒ):
        if áØÁ:
            break 
        
    
    return áØÁ

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
    if áØÆ:
        return áØÆ
    
    (áØÅ:=(("MOON_WARNING_IS_ERR") in env))
    (áÖð:=(áØÅ or (("MOON_DEPRECATION_IS_ERR") in env)))
    if (áØÁ is ÄÔáô):
        (ÄÊPSH((áÖð,("Deprecation %s")%(((("Error"))if(áÖð)else(("Warning"))),))),((áÓÔ:=ÄÊPKE(0)[0]),(áÓà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    elif (áØÁ is ÂÄ):
        (ÄÊPSH((áØÅ,("Warning%s")%((((" [as Error]"))if(áØÅ)else(ÁØã)),))),((áÓÔ:=ÄÊPKE(0)[0]),(áÓà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    else :
        (ÄÊPSH((True,("Assertion failed"))),((áÓÔ:=ÄÊPKE(0)[0]),(áÓà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    
    try :
        (áÓà:=("%s ⟨%s⟩%s")%(áÓà,áØÆ,((((" - ") + ÂÞÅCAT(áØÇ,ÁÜÙ)))if((áØÇ is not ÂÞÅ))else(ÁØã)),))
        Âçß(termclr(áÓà,((("f22"))if(áÓÔ)else(("ff2")))))
    except áÍÚ:pass
    if áÓÔ:
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
    

def ÁØö(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ,TYPELIKE={áÓó,áÓõ,áÓö},TYPEE=(type | UnionType)):
    if (áØÇ is ÂÞÅ):
        return type(áØÆ)
    elif (áØÇ in TYPELIKE):
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
        return Âåß((áÑÞ).x,ÂùÆ(((áÑÞ).x is not ÂÞÅ),("Holder value unset!")))
    
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


#system.☾ (1370 ⟶ 1750)
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
    Âçß(("WARNING: Failed to copy."))

def PL_TEXT_PASTE():
    try :
        from clipboard import paste
        return paste()
    except áÍÚ:pass
    Âçß(("WARNING: Failed to paste."))

def PL_URANDOM(n):
    return (os).urandom(n)


#ops_A.☾ (3389 ⟶ 8429)
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
        
        if ((d:=_get_d(x)) in 0):
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
    
    ÂùÆ(False,("%s is an invalid mode for !")%(m,))

@OPWRAP_(*(("󰒼󰒽")))
def _(áÑã,áØÆ=ÂÞÅ,Æå=ÄÕÍÔ,ÁÜñ=False):
    (áØÆ:=[*áØÆ])
    (áÖê:=[((áÑÿ,i))for (i,v) in(ÂÓÏ(áØÆ))if(((áÑÿ:=Æå(v)) is not ÄÔýò))])
    (áÖê).sort(reverse=(áÑã == ("󰒽")))
    return Áÿú(áÖê,(((lambda x:x[1]))if(ÁÜñ)else((lambda x:áØÆ[x[1]]))))

@OPWRAP_(*(("󰈳󰈲")))
def _(áÑã,áØÆ=ÂÞÅ,Æå=ÂÞÅ,áØÁ=ÂÞÅ,ÁÜñ=False):
    if ÁÜñ:
        ÂùÆ((áØÁ is ÂÞÅ),("\u0022%sˣᔨ\u0022 is invalid")%(áÑã,))
    
    (Æå:=((ÄÕÍÔ)if((Æå is ÂÞÅ))else(((Æå)if(áÓó(Æå))else(CUR((lambda ÂîÓ,ÂîÒ:(ÂîÓ == ÂîÒ)),Æå))))))
    if (áÑã == ("󰈳")):
        (ÄÊPSH(Æå),ÄÊPSH(CUR((lambda ÂîÓ,ÂîÒ:(not ÂîÓ(ÂîÒ) )),ÄÊPKE(0))),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
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
    (áÝÐ:=(((((None)if((áØÁ is ÂÞÅ))else(áØÁ))))if((áÑã in ("ᙎᙡ")))else(ÂÞÅ)))
    (áÝÑ:=(((((chnk)if((áØÁ is ÂÞÅ))else((áØÁ + 1)))))if((áÑã in ("ᗢᙧ")))else(chnk)))
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
        
        ÂùÆ(False,("Invalid modifier for !"))
    
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
    
    ÂùÆ((áØÇ is not ÂÞÅ),("ᖘ needs right side"))
    def Æå(áØÆ):
        (áØÆ:=((ÄÔÙù(áØÆ))if(((is_str:=ÁØö(áØÆ,ÁÜÙ))))else(((ÐÌü((áØÆ).copy))if(ÁØö(áØÆ,áÍÙ))else([*áØÆ])))))
        (ÄÊPSH((MOD(Áëý,áØÁ=áÓó)(áØÁ,MOD((lambda ÂîÓ:ÂîÓ(áØÆ)))),[])),((ids:=ÄÊPKE(0)[0]),(TD:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
        if (((ÄÝøÆ(ÁÜÙ,ÄÊPSH(ids)) and ÁØö(ÄÊPOP(),ÄÊPSH(áÓö))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)):
            ÁØòþÁÙÇ((lambda ÂîÓ,ÂîÒ:(((TD).append(ÂîÓ))if((ÂîÒ is ÄÔýò))else((ÄÊPSH(áØÆ),ÄÊPSH(ÂîÓ),ÄÊPSH(ÂîÒ),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]))))(ids,(V:=áØÇ(ÄÝöÊ(áØÆ,ids))))
        else :
            ÁØÿþÁÙÇ((lambda ÂîÓ,ÂîÒ:(((TD).append(ÂîÓ))if((ÂîÒ is ÄÔýò))else((ÄÊPSH(áØÆ),ÄÊPSH(ÂîÓ),ÄÊPSH(ÂîÒ),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]))))(ids,(V:=Âêà(áØÇ(áØÆ[ids]))))
        
        for x in(ÄÔàÒ(TD)):
            del áØÆ[x]
        
        return ((Âøî(áØÆ,ÁØã))if(is_str)else(áØÆ))
    
    return ((Æå)if((áØÆ is ÂÞÅ))else(Æå(áØÆ)))

(ÆÑ:=(lambda áØÆ,áØÇ,áØÁ=ÂÞÅ:reduce(áØÇ,áØÆ,*(((())if((áØÁ is ÂÞÅ))else((áØÁ,)))))))
(ÐÌ:=(lambda áØÆ,áØÇ,áØÁ=ÂÞÅ:[*(accumulate(áØÆ,áØÇ,initial=((None)if((áØÁ is ÂÞÅ))else(áØÁ))))]))
(ÂøÑ:=(lambda áØÆ,áØÁ=ÂÞÅ:(((((ÁØã)if(ÁØö(áØÆ,ÁÜÙ))else(0))))if((((ÄÊDEL(1),False)[1])if(ÄÊPSH(áØÆ))else(((ÄÊPOP())if((áØÁ is not ÂÞÅ))else((ÄÊDEL(1),True)[1])))))else(MOD(ÆÑ,áØÁ=áØÁ)(áØÆ,ì)))))
(ÂøÐ:=(lambda áØÆ,áØÁ=ÂÞÅ:((1)if((((ÄÊDEL(1),False)[1])if(ÄÊPSH(áØÆ))else(((ÄÊPOP())if((áØÁ is not ÂÞÅ))else((ÄÊDEL(1),True)[1])))))else(MOD(ÆÑ,áØÁ=áØÁ)(áØÆ,ÂØú)))))
(ÄÕéý:=(lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:(((lambda Æå:Æå(*(ÂÕÃ([áØÆ,áØÇ],[ÂÞÅ])))))if((áØÁ is ÂÞÅ))else(áØÁ(*(ÂÕÃ([áØÆ,áØÇ],[ÂÞÅ])))))))
(ÂÔð:=(lambda áØÁ=ÂÞÅ:(({*''})if((áØÁ is ÂÞÅ))else(ÁØò((lambda ÂîÓ:{*''}))(ÂÿÇ(áØÁ))))))
(ÂÚü:=(lambda áØÁ=ÂÞÅ:(([])if((áØÁ is ÂÞÅ))else(((ÁØò((lambda ÂîÓ:[]))(ÂÿÇ(áØÁ)))if((áØÁ > 0))else((ÂØÍ(Âêà,(- áØÁ )))([])))))))

#ops_B.☾ (6307 ⟶ 16704)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ops_B.☾')).parent
(ÃÆí:=(lambda áØÆ,áØÁ=ÂÞÅ:((((GET_CASE(áØÆ))if(ÁØö(áØÆ,ÁÜÙ))else((((1)if((áØÆ > 0))else(((((- 1 )))if((áØÆ < 0))else(None)))))))) or (((0)if((áØÁ is ÂÞÅ))else(áØÁ))))))
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
        if (((ÄÊDEL(1),False)[1])if(ÄÊPSH((áÑÈ is ÂÞÅ)))else(((ÄÊPOP())if(áÍÛ(áÑÈ,áØÆ))else((ÄÊDEL(1),True)[1])))):
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
    if (((ÁØö(áØÆ,ÄÊPSH(ÁÜÙ)) and ÁØñ(ÄÊPOP(),ÄÊPSH(Æå))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)):
        (ÄÊPSH(Æå),ÄÊPSH(CUR((lambda ÂîÓ,ÂîÒ:(ÂîÓ != ÂîÒ)),ÄÊPKE(0))),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
    (áÖõ:=MOD(ÄÔÞÔ,ÁÜñ=ÄÕøü)(áØÆ,Æå))
    if (áÖõ is None):
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

(ÂÓÏ:=(lambda áØÆ,áØÁ=ÂÞÅ:((Áÿú(ÂÿÇ(áØÆ),(lambda x:(x,áØÆ[x]))))if((áØÁ is ÂÞÅ))else(((ÄÕåØ(Áÿú(ÂÿÇ(áØÆ),MOD(Âêà,áØÁ=áÍé)),áØÆ))if((ÂüÌ(áØÁ) == 1))else(MOD(Áëý,áØÁ=(áØÁ > 0))(ËãÂ(ÂÓÏ(áØÆ),(lambda x,y:ÁØò((lambda ÂîÓ:((x,*(ÂîÓ[0])),ÂîÓ[1])))(MOD(ÂÓÏ,áØÁ=(áØÁ - ÃÆí(áØÁ)))(y)))),ÄÔÙù)))))))
(ÂÿÇ:=(lambda áØÆ,áØÁ=ÂÞÅ:((ÄÝöÈ(MOD(Áëý,áØÁ=áÓö)(áØÆ,ãÊú)))if((áØÁ is ÂÞÅ))else(MOD(Áÿú,áØÁ=((ÂüÌ(áØÁ))if((áØÁ < 0))else(1)))(MOD(ÂÓÏ,áØÁ=áØÁ)(MOD(Áëý,áØÁ=Âåæ(Âó,áÓö))(áØÆ,(Âåæ(MOD(ÂØÑ,áØÁ=ÂüÌ(áØÁ)),ÂÿÇ)))),MOD((lambda ÂîÓ:ÂîÓ[0])))))))
(ÄÔéÄ:=(lambda áØÆ,áØÇ,áØÁ=ÂÞÅ:ÂåÔ(ÂåÔ((R:=MOD((lambda ÂîÓ:((Âêà(ÁØã))if((ÂîÓ is ÂÞÅ))else(((Âêà(ÂîÓ))if(ÁØö(ÂîÓ,ÁÜÙ))else(Áÿú(ÁãÁ(ÂîÓ),ÁÜÙ)))))))),(Æå:=MOD((lambda ÂîÓ:MOD(ÆÑ,áØÁ=ÂîÓ)((lambda ÂîÓ,ÂîÒ:MOD(ÄÕåØ,áØÁ=ÄÝöÉ(ÂîÒ))(ÂîÓ,ÂîÒ))(R(áØÆ),R(áØÇ)),(lambda x,y:(x).replace(*y))))))),(((Æå)if((áØÁ is ÂÞÅ))else(ÂÞÅCAT(áØÁ,Æå)))))))
@OPWRAP_(*(("󰸵󰸷")))
def _(áÑã,áØÆ,áØÇ,áØÁ=ÂÞÅ):
    if ((((ÁØö(áØÆ,ÄÊPSH(áÍÞ)) and ÁØñ(ÄÊPOP(),ÄÊPSH(áØÇ))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)) and (áØÁ is ÂÞÅ)):
        if (áÑã == ("󰸵")):
            return MOD(ÄÝöì,áØÁ=ÂÞÅCAT(áØÇ,Ãù))(áØÆ)
        
        (ÄÊPSH(áØÆ),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),ÁÜÙ)),(áØÆ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
        if (áØÁ is ÂÞÅ):
            (áØÁ:=(" "))
        
    
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
    ÂùÆ(((áØÆ is not ÂÞÅ) or (ÂÞÅ is not áØÇ)),("Range missing both values!"))
    if (áÑÃ:=(áØÁ is ÂÞÅ)):
        (áØÁ:=1)
    
    (v:=((áØÇ)if((áØÆ is ÂÞÅ))else(((áØÆ)if((áØÇ is ÂÞÅ))else(ÂÞÅ)))))
    if (((((áØÆ is not ÂÞÅ) and (ÂÞÅ is not áØÇ)) and (((ÁØö(áØÆ,ÄÊPSH(áÍÞ)) and ÁØñ(ÄÊPOP(),ÄÊPSH(áØÇ))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False))))if((v is ÂÞÅ))else(ÁØö(v,áÍÞ))):
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
        
    
    ÂùÆ(False,("Invalid argument types! %s %s")%(ÁØö(áØÆ),ÁØö(áØÇ),))

def áÇù(x,y=ÂÞÅ,áØÁ=ÂÒå,ÁÜñ=False):
    if (not x ):
        return []
    
    if ÁØö(x,áÍÞ):
        (ÄÊPSH(x),ÄÊPSH(ÂÿÇ(ÄÊPKE(0))),(x:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
    if (y is ÂÞÅ):
        (y:=ÄÕÍÔ)
    
    if ÁÜñ:
        return MOD(áÇù,áØÁ=áØÁ)(ÂÿÇ(x),((((lambda i:y(x[i])))if(áÓó(y))else(y))))
    elif ÁØö(y,áÍÞ):
        return [x[slice(None,y)],x[slice(y,None)]]
    elif (not áÓó(y) ):
        ÂùÆ(áÓö(y))
        (y:=áÍè(MOD(ÄÔÔç,áØÁ=MOD((lambda ÂîÓ:ÂÁÍ(ì)(ÂîÓ,ãÊú(x)))))(y,MOD((lambda ÂîÓ:(ÂîÓ < 0))))))
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
    for (áÑî,áÑü) in((ÂÓÏ(x))[slice(1,None)]):
        if ((r:=y(áÑü)) != áÍç):
            (áÍÌ).append(R)
            (ÄÊPSH((r,[])),((áÍç:=ÄÊPKE(0)[0]),(R:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
            if (not (ÄÊPSH(áØÁ),ÄÊPSH((ÄÊPKE(0) - 1)),(áØÁ:=ÄÊPKE(0)),ÄÊDEL(2))[2] ):
                (áÍÌ).append(x[slice((áÑî + ((r is ÄÔýò))),None)])
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
    ÂùÆ(((áØÆ is not ÂÞÅ) or (ÂÞÅ is not áØÇ)),("Join missing both values!"))
    if (áØÁ is not ÂÞÅ):
        (bound_mode:=áØÁ)
    
    if (bound_mode is ÂÞÅ):
        (bound_mode:=(((áÑã == ("⟗")) and 1) or 0))
    
    if (áØÆ is ÂÞÅ):
        (ÄÊPSH((áØÇ,áØÆ)),((áØÆ:=ÄÊPKE(0)[0]),(áØÇ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    
    if (áØÇ is ÂÞÅ):
        ÂùÆ(áÓö(áØÆ),("Single-arg %s needs an iterable")%(áÑã,))
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
    
    if (((not L ) and ÁØö(áØÆ,ÁÜÙ)) and (((áØÇ is ÂÞÅ) or ÁØö(áØÇ,ÁÜÙ)))):
        (áÏÞ:=((())if((áØÇ is ÂÞÅ))else((áØÇ,))))
        if (áÑã in ("󷹎󷹑")):
            (r:=(áØÆ).split(*áÏÞ,maxsplit=n))
            return ((ÄÔÔç(r))if((áÑã == ("󷹎")))else(r))
        
    
    if (áØÇ is ÂÞÅ):
        (áØÇ:=Âó)
    
    if ((YS:=ÁØö(áØÇ,ÁÜÙ)) and (not L )):
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
    
    return (((ÁØò((lambda ÂîÓ:((Âøî(ÁØò((lambda ÂîÓ:ÂîÓ[0]))(ÂîÓ)))if(ÁØö(ÂîÓ,áÍá))else(ÂîÓ))))(r)))if(YS)else(r))

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
        ÂùÆ(((ÁÜñ is ÂÞÅ) and (áØÁ is ÂÞÅ)),("no"))
        return ((SUBSCRIPT)if((áÑã == ("󷸓")))else(((SUPSCRIPT)if((áÑã == ("󷸔")))else((ÄÝõà(ë),ÄÝõá(ë))))))
    
    (áØÆ:=ÁÜÙ(áØÆ))
    if (ÁÜñ is not ÂÞÅ):
        if (áÑã == ("󷸼")):
            ÂùÆ((áØÁ is ÂÞÅ),("󰤱"))
            ÂùÆ(ÁØö(ÁÜñ,áÓó),("󰤱"))
            return under_script(áØÆ,ÁÜñ)
        
        ÂùÆ(False,("󰤱"))
    
    if (áØÁ is ÂÞÅ):
        (áØÁ:=1)
    
    if (áØÁ > 0):
        (Æå:=((subscript)if((áÑã == ("󷸓")))else(((supscript)if((áÑã == ("󷸔")))else(nrmscript)))))
        return ÂÕÅ(ÂØÍ(Æå,áØÁ),áØÆ)
    


#ops_C.☾ (3246 ⟶ 8565)
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
            (ÄÊPSH(áÖÒ),ÄÊPSH(ÁØòþÁÙÄ((lambda ÂîÓ,ÂîÒ:ÂîÓ[slice((ãÊú(ÂîÓ) - ÂîÒ),None)]))(ÄÊPKE(0),l)),(áÖÒ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
        
    else :
        (ÄÊPSH(áÖÒ),ÄÊPSH(Áÿú(ÄÊPKE(0),Âåæ((((MOD((lambda ÂîÓ:MOD(ÄÕÊÄ,áØÁ=((ÂîÓ[((- 1 ))])if((áØÁ is ÄÕøü))else(áØÁ)))(ÂîÓ,h))))if((áÑã == ("󱑼")))else(MOD((lambda ÂîÓ:MOD(ÄÕÊÂ,áØÁ=((ÂîÓ[0])if((áØÁ is ÄÕøü))else(áØÁ)))(ÂîÓ,h)))))),áÍá))),(áÖÒ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
    (r:=[*(zip(*áÖÒ))])
    return ((Áÿú(r,ÄÊCUR((1,),{},ÄÔÔè,ÂýÃ,ÄÔýò)))if((áØÁ is ÄÔýò))else(r))

def ÁÛÛ(áØÆ,áØÁ=ÂÞÅ):
    def Æå(áØÁ):
        if (ÄÝøÇ(áØÁ,áÓö) or ÁØñ(ÁÜÙ,áØÁ)):
            (ÄÊPSH(áØÁ),ÄÊPSH(Âêà(ÄÊPKE(0))),(áØÁ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
        
        (áÓÕ:=((MOD(ÁÛÛ,áØÁ=áØÁ[slice(1,None)]))if((ãÊú(áØÁ) > 1))else(ÄÕÍÔ)))
        (áÓÙ:=(lambda x,y:((áÓÕ(x[(y % ãÊú(x))]))if(ÁØö(y,ÂÑÅ))else(((áÓÕ(x[y]))if((ÁØö(y,ÁÜÙ) or (((ÄÝøÆ(áÓö,ÄÊPSH(y)) and ÄÝøÇ(ÄÊPOP(),ÄÊPSH(slice))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False))))else(MOD(Áëý,áØÁ=(áÓÕ is not ÄÕÍÔ))((ÄÝöÊ(x,y)),MOD((lambda ÂîÓ:Áÿú(ÂîÓ,áÓÕ))))))))))
        return áÓÙ(áØÆ,áØÁ[0])
    
    return ((Æå)if((áØÁ is ÂÞÅ))else(Æå(áØÁ)))

def ÁÝÖ(áØÆ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
    ÂùÆ(ÁØö(áØÆ,áÓö),("%s󷹵𝗜")%(áØÆ,))
    ÂùÆ((áØÁ is not ÂÞÅ),("ᕋ requires modifier"))
    (áØÆ:=((ÄÔÙù(áØÆ))if(((is_str:=ÁØö(áØÆ,ÁÜÙ))))else(ÐÌü((áØÆ).copy))))
    (áØÇ:=((ÂÚü())if((áØÇ is ÂÞÅ))else(MOD(Áëý,áØÁ=ÄÝøÇ(áØÇ,áÓö))(áØÇ,Âêà))))
    (áØÁ:=((slice((ÄÊPSH(áØÁ),ÄÊPSH((ÄÊPKE(0) % ãÊú(áØÆ))),(áØÁ:=ÄÊPKE(0)),ÄÊDEL(2))[2],(áØÁ + 1)))if(ÁØö(áØÁ,áÍÞ))else(áØÁ)))
    if ÁØö(áØÁ,slice):
        (ÄÊPSH(áØÆ),ÄÊPSH(áØÁ),ÄÊPSH(áØÇ),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
    elif ÁØö(áØÁ,áÓö):
        for (i,(z,n)) in(ÂÓÏ(ÁØò((lambda ÂîÓ:[ÂîÓ[0],ãÊú(ÂîÓ)]))(áÇù(ÄÔàÒ(ÁØò((lambda ÂîÓ:(ÂîÓ % ãÊú(áØÆ))))(áØÁ)))))):
            if ((áØÇ is ÂÞÅ) or (i >= ãÊú(áØÇ))):
                del áØÆ[z]
            else :
                (ÄÊPSH(áØÆ),ÄÊPSH(slice(z,(z + 1))),ÄÊPSH(MOD(Âêà,áØÁ=n)(áØÇ[i])),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
            
        
    else :
        ÂùÆ(False,("Modifier 󷹵 slice|𝑖|𝗜"))
    
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
        
    
    ÂùÆ(False)

@OPWRAP_(*(("○⍜󰬫󰬩")))
def _(áÑã,áÍÛ,áÍÜ,áØÁ=1):
    if (áÑã in ("󰬩󰬫")):
        ÂùÆ((((ÄÊDEL(1),False)[1])if(ÄÊPSH((áØÁ == ì)))else(((ÄÊPOP())if((î == áØÁ))else((ÄÊDEL(1),True)[1])))),("󰤱 generalize"))
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
                        (ÄÊPSH(MOD(ÄÕÊÂ,áØÁ=[])(áÇù(áÑË,(ÂóÍ((ãÊú(áÑË) - áÖû),0))),2)),((Ïà:=ÄÊPKE(0)[0]),(Ïß:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
                    
                    (áÖÒ:=[ÁØò((lambda ÂîÓ:ÂîÓ[1](*(ÂîÓ[0]))))((((ÄÕåØ)if((áØÁ < 0))else(ÄÝöÔ)))[[]](MOD(Ááú,áØÁ=ÄÔýò)(Ïß,[0,((S - 1)),S]),áÍÜ)),Ïà])
                
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
            ÂùÆ((n != 0),("󰤱 generalize"))
            (áÖÒ:=(((MOD(ÄÕÊÄ,áØÁ=ÂýÃ))if((áÑã == ("○")))else(MOD(ÄÕÊÂ,áØÁ=ÂýÃ))))(áÑË,(L + (((n - m)) % n))))
            (v:=MOD(ÁâÁ,áØÁ=(n - 1))(áÖÒ))
            if (m != 0):
                (ÄÊPSH((((((- 1 )),0))if((áÑã == ("○")))else((0,((- 1 )))))),((Ïß:=ÄÊPKE(0)[0]),(Ïà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
                if ÄÝøø((áÑã == ("⍜")),(áØÁ < 0)):
                    (ÄÊPSH(v),ÄÊPSH(Ïß),ÄÊPSH(ÄÔÙù(ÂÀÇ(áÇù(v[Ïß],MOD((lambda ÂîÓ:(ÂîÓ is (ÂýÃ)))))))),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
                
                (ÄÊPSH(v),ÄÊPSH(Ïß),ÄÊPSH(ÁØòþÁÙÇ((lambda ÂîÓ,ÂîÒ:((ÂîÓ)if((ÂîÓ is not (ÂýÃ)))else(ÂîÒ))))(v[Ïß],v[Ïà])),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
            
            return ËãÂ(v,áÍÜ)
        
    elif ÁØö(áÍÜ,áÓö):
        def Æå(*áÑË):
            ÂùÆ((ãÊú(áÑË) >= ((ãÊú(áÍÜ) * (S:=ÂüÌ(áØÁ))))),("󰤱 generalize"))
            ÂùÆ((áØÁ > 0),("󰤱 generalize"))
            ÂùÆ((áÑã != ("⍜")),("󰤱 generalize"))
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


#ops_.☾ (1307 ⟶ 3099)
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
    if (((((áØÆ is not ÄÊPSH(ÂÞÅ)) and (ÄÊPOP() is not ÄÊPSH(áØÇ))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)) and (((ÁØö(áØÆ,ÄÊPSH(áÍÞ)) and ÁØñ(ÄÊPOP(),ÄÊPSH(áØÇ))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False))):
        ÂùÆ((ÁÜñ is ÂÞÅ),("󰤱"))
        return (ÄÝöì(("%s%s")%(ÄÝöì(ÂüÌ(áØÆ)),ÄÝöì(ÂüÌ(áØÇ)),)) * ((ÃÆí(áØÆ) * ÃÆí(áØÇ)) or 1))
    
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


#crypto.☾ (2596 ⟶ 5006)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/crypto.☾')).parent
class Cmap(ÂÑÖ):
    def __init__(áÑÞ,d,*áÑË,**áÑÕ):
        (super()).__init__(*áÑË,**áÑÕ)
        (ÄÊPSH((áÑÞ).__dict__),ÄÊPSH(1),ÄÊPSH(d),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
    
    (__call__:=(lambda áÑÞ,*áÑË,**áÑÕ:áÑÞ[(áÑÞ).__dict__[1]](*áÑË,**áÑÕ)))
    (__pow__:=(lambda x,y:x[y]))

def SR_bytes(x=None,y=None):
    if ((((x is ÄÊPSH(None)) and (ÄÊPOP() is ÄÊPSH(y))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)):
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
        ÂùÆ(False,("Cannot shuffle (%s > %s)")%(n,ãÊú(x),))
    
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
        
        if ((((áØÆ is ÄÊPSH(ÂÞÅ)) and (ÄÊPOP() is ÄÊPSH(áØÇ))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)):
            return SR_float(*(((ÂÕÀ(1))if((áÑã == ("")))else(ÂÿÇ(1)))))
        
        (Æå:=((SR_float)if((áÑã == ("")))else(SR_int)))
        if ((((áØÆ is not ÄÊPSH(ÂÞÅ)) and (ÄÊPOP() is not ÄÊPSH(áØÇ))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)):
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
    Âçß(("Failed to import Crypto! Do you have pycryptodome installed?"))

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

#🌈.☾ (1630 ⟶ 3280)
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

@cache
def sty(s,bg=0,def_=("bec")):
    for (k,v) in(styd):
        if not(((s in k) and ÂÔö(v,("fg")))):continue
        return termclr(s,v[("fg")],bg)
    
    return termclr(s,def_,bg)

(__highlighter__:=(lambda l,b=None,clr=("bec"):Âøî(Áÿú(ÂÞÅCAT(ÂÞÅCAT(l,ÁÜÙ),VEP),ÄÊCUR((1,),{},sty,ÂýÃ,b,clr)))))
def highlight_tester():
    while((l:=ÐÌü((ÂÐðþáÐâ).readline))):
        Âçß(ÂÞÅCAT(ÂÞÅCAT(("\x0A"),(l).rstrip),__highlighter__))
    


#!.☾ (669 ⟶ 1478)
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
        
        if (((d:=Âüð(ÄÝõç(áØÁ))) >= 0) and (áØÆ > 0)):
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
    
    ÂùÆ(False,("what do you meeeeaaaaaannnnnn!?!?!?"))


#?.☾ (429 ⟶ 1069)
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


#extra_globals.☾ (2782 ⟶ 4025)
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


#subproca.☾ (1557 ⟶ 3145)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/subproca.☾')).parent
def ÄÊSUBPROCA(cmd,áÏÃ=ÁØã):
    from subprocess import Popen as áÐä, DEVNULL as NULL, PIPE, STDOUT
    ÂùÆ((not (((("M") in áÏÃ) and ÂÕÖ(áÏÃ,("OEoe")))) ),("Cannot use stdout/err and MERGE at once"))
    ÂùÆ((not ((((((("o") in ÄÊPSH(áÏÃ)) and ÂÔö(ÄÊPOP(),ÄÊPSH(("O")))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)) or ((((("e") in ÄÊPSH(áÏÃ)) and ÂÔö(ÄÊPOP(),ÄÊPSH(("E")))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)))) ),("Cannot suppress and ignore stdout/err"))
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


#Ń.☾ (4792 ⟶ 9550)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/Ń.☾')).parent
from collections import deque as áÐòþáÑÁ
class ÅÒ:
    (__slots__:=(("t"),("c"),("e")))
    def __init__(ÄÕÒü,t,*c,e=ÂÞÅ):
        (ÄÊPSH(ÄÕÒü),ÄÊPSH(("t")),ÄÊPSH(ÄÕÒü),ÄÊPSH(("c")),ÄÊPSH(ÄÕÒü),ÄÊPSH(("e")),ÄÊPSH((t,(([*c])if(c)else([])),((MOD(ÂÑÖ,áØÁ=None)())if((e is ÂÞÅ))else(e)))),(setattr(ÄÊPKE(6),ÄÊPKE(5),ÄÊPKE(0)[0]),setattr(ÄÊPKE(4),ÄÊPKE(3),ÄÊPKE(0)[1]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)[2])),ÄÊDEL(7))[7]
        for z in((ÄÕÒü).c):
            if not(ÄÝøÇ(z,ÅÒ)):continue
            ÂùÆ(False,("%s; %s; %s")%(t,z,c,))
        
    
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
            
        
        return [(c)for c in(ÄÕÒü)if((((((((ÄÊDEL(1),False)[1])if(((c).e).T)else(ÄÊPOP())))if(ÄÊPSH(not_T))else((ÄÊDEL(1),True)[1]))) and Æå(c)))]
    
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
            if not((((((ÄÊDEL(1),False)[1])if(((x).e).T)else(ÄÊPOP())))if(ÄÊPSH(not_T))else((ÄÊDEL(1),True)[1]))):continue
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
            (ÄÊPSH(__ÄÊIMPORT__(("text_format"),globals(),(""))),ÄÊPOP())[((- 1 ))]
        
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
            (áØÀ:=stackr(áØÀ,Âøî(ËãÂ(ÂÓÏ(ÄÕÒü),(lambda x,y:Âøî(ËãÂ(ÂÓÏ(ÂÞÅCAT(ÂÞÅCAT(False,(y).P),lines)),CUR((lambda ÂîÓ,ÂîÒ:ÂÁÍ(ì)(ÂîÒ,(((ÂâÑ)if((((ÄÊDEL(1),False)[1])if(ÄÊPSH(ÂîÓ))else(((ÄÊPOP())if((ãÊú(ÄÕÒü) != 1))else((ÄÊDEL(1),True)[1])))))else(((((ÂîÓ and (" ")) or ÂäÇ))if((x == (ãÊú(ÄÕÒü) - 1)))else(((((x and Ââî) or ÂãÀ))if((((ÄÊDEL(1),False)[1])if(ÄÊPSH(ÂîÓ))else(((ÄÊPOP())if((ãÊú(ÄÕÒü) == 0))else((ÄÊDEL(1),True)[1])))))else(ÂâÓ))))))))))),("\x0A")))),("\x0A"))))
        
        return ((ÂåÔ(Âçß(áØÀ),ÄÕÒü))if(fs)else(áØÀ))
    


#meta.☾ (4790 ⟶ 6528)
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
@cache
def moon_to_py_cached(áÖï):
    ÂùÆ(TRANSPILE_REF,("Cannot transpile without transpiler!"))
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
        
        (ÄÊPSH(__ÄÊIMPORT__(("errors"),globals(),(""))),ÄÊPOP())[((- 1 ))]
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
    
    ÂùÆ((F is not None),("Unable to find module \u0022%s\u0022! Paths checked:%s")%(name,ÂîÊ(failed,("\x0A")),))
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
            raise Ïã
        
    
    (mod:=__ÄÊIMPORTS__[F])
    ÂÞÅCAT(mod[("__EXPORTS__")],(áÒÿ).update)
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
    (ÄÊPSH(__ÄÊIMPORT__(("text_format"),globals(),(""))),ÄÊPOP())[((- 1 ))]
    (show_table:=(lambda x,y:Âøî(Áÿú(ÂÛÅ(ÁØò((lambda ÂîÓ:ÂåÔ((m:=ÂóÍ(Áÿú(ÂîÓ,áüíþËðâ))),Áÿú(ÂîÓ,ÄÊCUR((1,),{},padc,ÂýÃ,m)))))(ÂÛÅ(MOD(Áÿú,áØÁ=2)(([x] + y),ÁÜÙ)))),ÄÊCUR((1,),{},Âøî,ÂýÃ,("│"))),("\x0A"))))
    Âçß(show_table(ÂÛê(("Static Name Path")),ËãÂ(__ÄÊIMPORTS__,(lambda x,y:(("✗✓")[(y).hardcoded],(y).name,x)))))

(BOOTSTRAP_GLOBALS:=(globals()).copy())

TP_CACHE.update({'Libraries/text_format.☾':strd('c$~#LYj0b}vETJ84h~>oSJ}8EWi_!9ru8e=7uUTGY!?Z@5ClaYNo*)lC8?{U)&*?Yw4M4TTasfXjvK{~JmjdU9ZP=3K=udpH{|?+0{#PcW_I_SJv@h$RkSF9!+p=r&d$uv%x=3m=Zp+E@T*NuH=1o{y3+J=PPyeYJ*s9$4*b`F4@!srd+$h|xzy@%KH&KkZ@TTsRe4c<irwV`<ew=}?GUI1xap01z6Cf5oO&Q|Z0b8f3@jG<gEcS*25Mtgqm$1&(UKJ8syC)EW$%eWnDB}`F9ua+nMaeeCO~d_d}pOGIbExJR`1`{+WBM687~^ftzmp8w3p1NsHN$(XPQ$^Q{m~=QxG-e*%qQ2ZVz0;0ez?ax6V1ha9ibfm2zdm1ESW;lcUwLBhSb?i6J9$Ufz*QjLGxzd$~H2r$G$+axTo!#3*J4@Y)z;=j9`Lg~^lhy1dWA`R3)iT!gOjmi)7P!c>{#2<o|^YXrbtlpCCT^_Iu79DYpA$GP*ilg;FI={AKGXNh&=Z-9-}rm7{cRVlT+-?w1h(D<pmJCaxQWk->7KlHPEKb*;AhW8cNuSQg^`r2E$x58{9b3AjrFtn?<n@=7ueCTJg@a2lGJ?E6?0|QQ!o8eq81L!+id~oNlxXX92qk?(^Mi=A@s~2^8&FXP*ByVjVE0rc{;}doG+Fr9%A{ZSY_K(!*Uc57OnXJ^C*r_>*goroG)AG;zetU$mA;HBT|0IZ+S~H^}MmIrwb4$S9JeQ{kr)s0!tWCy&nN9Y^Tz)u%{NNW_^;*Sa|J#`I1e<eScVH`v&TGK$!HK&_FJcvf0r(^Ld<mlf>`8e;t}q{ZIPW-fdar#=;PIJqvl^fKH;4CkGZ}H<I<>$um*k3kjBIsXp3G-CvfB&AfH!4l-=1TJ@mkY$&>U^ry+*y!Y(*UJ8<1w~Y5BR_kgKrFTu~q&W%j_DL`c-EBC5SRnucP~0Ev+($BUwwo2cV5BY@^N!0NRr54bpGu|RCK(vxycJ~!*s><(M%m7A3bS~b#Di=7}s0_2^vY8K6i@`$T@B+nYcFghbvo#X1T_=Xz+)FMm>wgFJ2U4Rir46Rn>S^1a|e<5#`>-8=<5k41lTqqJ7$*}ms0vqWM#nZ$XkqYsJTBgl47BouZ(7K69l$@6j<V8ctjLk7xL0QP*uE#YRSDV!zH7Mi0E8?NrPjDaf7#q(=T)ImXGXA^o7P%NrRA(|pbA+G_DaBS8dJ{C+j@IOk7OE7@!DHh#+YNDK-?xx=eWA}$JbHU5@APVwXs|i8t|F@KdATf4B?PUIDT<IiHAiTkCvA#cD0J6sk@Wv*0CY!Qw?O$qt4|9A$@-G~D!m&KSkaqSiN{B(K*eSJCW|d^STF{<%mFYV<wz=SMv&2T(W93XLoLV)hMfvy<FJ86&YHp&7V36JUNPN#&gO_vRv*R+KGxxI)Sh!)JE_cxUAre;BcU(?rt^V}{YDHWM)aQ{6YCxkdrr`iy!Cu<zGVZTH6@_*U7`g520oT&*t=yY@c2*kWmjY^Fc;0PX`8AC;}7;=eSO3%g911mDh!ZPZj{9?&UwW51(Z_}oh4gfXDL{tMw=r2yi@RLHA<Zz*-9|z8j$BlO8?4KA}D!o^aYh}(wPd_YkI3LMp7}G!^0cTa78Y(V~yS;035d_Yg_OJa6x5o`7z+xqQ;~!ROCes7x&cJ9uTE(@LW}0RD0GER4#OrsVdrRl|&-O5PGu+Ky)$>4E)+MLWtzk<tig0o>81|Rwd^^9XqZ@;aNV!%8(yShWCyhOxQvS5*KOJXURxlaNg4B|2e=i9Cu&n=2(5Us11|-2M(b<4He-I)}43qjs}@<FBAq5L72QOPbxzi`h!JR=N2!}>PS4}3$*<e1rd!v1mz5>Db8_=>Ty_^6s(ZfFR%jo90+8Glj9L2fUOA!oU1zg;uo<VJ?F}%Al!v#1U&*`>mOi`9j)Np$1gX(|MBJKqo-LqcWDOEi)C7dXJ+$qO-#U_#sjc3j*(_6Wk1A)0~$v1%HGhZbuDn#sex<1W)GWH$6ik}C*<LnnbQS#A_;c__%2ilDX7qpsYcr&iA}77?*!w=o2oM0Tof4~JfPob0vmwlA4CAJJ6$uRE;n@!EoY%znQ{+Hhf-u!3zgTMZfT4ZG-r{_aU+RmY)OoyFb7hYD<)Nq61XIrwA$s$M@@2cugPyC{$RLJRq3Qi3b}5!{6-`|FoLBZNor(}sXlA57Nb{5X&NK1r)seehc(_yn7dR=%D{Kh1XB}4b83t{Yc@xO`Y@Cb=s@RWI2~gw&Qge~p%kpiDNj{3=?=fgVy*T#RLNFfMG)j&j8t*Tbv0;<rI(fjERDK3ix~Gjn9c(l^DHz(z)UtGtr&naTg!ls=|Wo{R*>G~eb2YihF>yZz%v0ma5yu(dkl`Y(b{-kEoa0cJMfh?b7*#BsRPGI`hiEAgI<#wL?&K_TZ0$nvf|3E{OqxDdzX`YoYmWfG6V~7(zZfR2s)quGzrx|BB=_hk>Woof~MVaP^xB2a%9wfCclMI!KKyU(wD)dTfvEsgG;xAOLu}xceOvUh+!-c(8I|ie&4H}?y#t|(-WD-GTIqpvUI_v1x2+`cf!@Y(V?Yd)q;hd=w%ZF)_{cqhuRTx`-~%}SwVEqzw~PJU$^GB;x1dr2B5iWoonGFIibjB`B>r)gg%=>2F-%PXFeV%%2h`s{ty)@oHeJGH&u+qZIlf@-mF!X7jGR#3?m*Gk1Wu^f-q8|H)G?mbBwdXAkt*{hhTXFC=)C{1Y!W$f+eWggpGkM43_Q%OY_0f?O^Ffu=LDD4>chunj4jfys8*Q@~0Ww?>;|a)JeG_Pj~Txa^tV2x=BVmbp=<Hk)sF3k5$pnYVoyRQvo!8%Y&C4(pFHneEN~)L#bK&`@Nzfy|C)-+-2g<ol*%Mb||Ft!GGOcU5+G960V;DG@U3E>=O0==4x&*p;JBS3**t8Bqt{4XmCQ4F$D+G|9&A{cCip*RTS^rg@aZnp2BfPf$O>EySd0$+EMrNm4h^!)SeTsq&@L=K=Tz%NO~l$!>{8N2N8vVT}rO8Fy&cQ=JDta34S4VI|4kmmJk_?96iK<k;<IMoqPhWe<EN_ai?oM9D(~$n8RrM+s-To^gwyN?M$GVR#cWODOIp#yQv6F^gb`l6*=co95zLv_K2wKY6^IT8-v}R%ln~##>Wz)<$H6EcJoXG8Ze)Cjh(IF9TG}x(!%b9t<hjnY+D?SD`_VCI|1SDC2qXP7Gfr*>Wg^%+(dkP1<rvz6ClZmit7aArJUkqm@mo8dk=rGB{!q-7mv%EnXN00tra-MHtZVZJOCI(McHe3MW<qVc(Czg#KVe=cj;I*r<W96d=Tc9|19R2e*)#^e-`EJc2UN@v(55!`h}jhnX36WGh#Z=cA+0k6UG;mdQ2tmqf$I)aPO+&`D9(Uku;|ghgq(<SqJ3JG8mgSmgiM2s$!bhZji30Kq9L;G|b{5lh}=$qRG@uk2_9HlF58lwDM%sTtuyR8P(`WQj6JksJ>iBc~pmZ=$0tud5?8pkK<YZGFSJfTuf3V>y&(~^z@><9G>lB3!3S(!_w9F%;wa&MOB)Qi<Yvv9qsoRbIc}H7ZD?N+9vG`cl|Qru5df`Rv6=b67Vv+I>1^JjoDJAQT1$@tLC$r%n0bl5EtC{d{xb8ofGcZxI4n!-PvK6r`o=HN$py@9-G0a?n+*ts6Dp5fEtV(9EaQ+KO(8V-x3w=My;UPU;`m7P+?mB!*d~g3Q@H8p`Tq0j)UH&Fp!P7TMRG!VlvoAuNfvmEBtYAkX37yc613>h~5MMPg%YMo%bp{1T0FP))n~>^Bt9cq>^VUxv!EJDtVxiA5^lTlE=!nd4L8wW`2+-5ZqbS`oy$8#qw2bQ=KlW_NS)(nQ1t$8lIbm=W5_d(>`w+UZ{q7({RdU7EI=}$y_m+tEdFX>R6C>1=-f;5!=UDe_!ZZ^)F0j)nvX@nRQdM9@X47nL8$P*JQpjnXgUemNE!GRmp9YtY|AyC95j=MkQZsZ%bcbs^l}3tRsW{yl^*II1${t{qp<ubHTOMpPmPu#h;!9o#mjj5_A@V&SydAO3=9)be4k7wU?V4_u<?8>Bpe+31l7wof|JVH_rr}>rnauvhzXbQ^-CHI-f)G7`~05a}$y$(0CTor;wh5@8iFp2u`03&fS#je?R?l^T|c{F2Q&C<>ueMf$v-R?!osReCzQ26~6D`Tl>f7SFXZ$1HLQpU50N3zE$|X_<3mol56lS!bgu#_@8)W1p>cEer?k3m-k}MsBPOHgrk*oBZ*8O&vOfl(^f)}?K?I$M7V+?5rrZ?M0$f>ExoZn_{)Z?48(nhf0JS$9_qFaq3%emE=M7yc)ua4i}%}wb$gDyAFCWrGdM$!4G%MYfw3Sj$Y+dX?;4{>>2W8m@j5kfV=%AqG!t4`Ll@-p)a$Q{UGeNRqZorT6h&GgVlT=sbovz-O{p&|$0!gq<sgeh)s}+<4F$g#wj^Izf<AAxlyiAZd-ogY2!tWZV;J#i&rN&DI3y6$=Q~TKsq&;(Ds|m>&^YZ1CgXiJL&0fv<CEaVqRR`%@D)KGkEYC6#wD-in6W3vG8s2{v7)BwzJf}dCVas~Q@A;L(a{U%o2mB}^iqkMLlUKo{jBF$eIVY(BR~o7Fz*LxJtg+*?r5opGn$QW(SrngjDCQS&Pd0|DDRSI>j{}J(kwBS{bei;niI;{LtsSBp&{HH5noC4#E8^-uf=S!ps!zHLHiDg?q#HRM>~-Woqb38AbTNvhOk{^SGJ36dW^w-(`P+DO<4};K2pITh_$vi*<$?FmI(UjpIqYVD=cyEw)bOiKV%o>gKcP^xXk$!P&p$XMW%AfL*cj|s~jRozLJ0GwNA!9(%p@3#6D855C9Nfq-lE;gIDTaN0IF#q)+%JSQx`ukyOzem0YQWhr^!z`%4Etc<=C$V@FFRHePRxmg}&^Ks5Ev&=o4hn#4;zH}&bLOJ=t#D8Vwipsv7wEMZ*675J}96)IJ9sY#`#F14scP}F6ot1msVX0+kE0{$=$ZjUSAk1(g_?1B<3htJMk5oWO-uPI!C{|0ODnH1iTF?F+H<*cq%4}o2wQo_ynV}PE?(#p|;f~8|Z{Zbw$!H|?%>>c+_+-_gR?m?;B751PWmLhgzYFUp@;XJpGC?TJ__)zVUe!kiETABgI8qLXan`t>Rysd<kq7ba>Q1-^hU4*I5T~z<^_E`^p)I*)sTnzIlB5KbPdd*fD{a>2HX_f2cssrUwuj#aBz54%o4j|i}0)2+&WM)r$!gK27R@-S$)TYLrxyB6E=iaC~v*oF_)0o1lrZYOz949=oIl+cPr`?3?%XG1T^8-`D+`nrC-`xq$o%6~q51r0(t5K_#TUE8JaM)-#41M=k9#-j^Z5T%Vyzua+`&OT77wD8ex?MjdC<A@VIO!<<Rq(Hhf4B{!qJm*0dlX7>xRKec&|!hCIyos_D%<XoJ{5MV&(yI~rhg~UE4Va&dtGsVXjjT*m-ijD#cG<{?qW}c_c^_8*{{hpeNoeW2eAy5r>xFdlqeN&w=Zo%17Sgasb0fttE@a)5#f`0;Qu$2i$P!kST<wbVD&UTEVU4NdH`{^3PPs89hgvImTxe0tfz-j|M>iqrwLAuu$@r49ggS!2jiBW@&'),'Libraries/cache.☾':strd('c%02vTTc@~6n^io7&jrAA(MuJcxkc^go_vv2>4)v&1PwLVZ(OYbeE>Y_y7Slq6r!>Y7|2Z@x^$-#25qmF#p6~;7{<(%+lE@OSwhjyzI>Mn{&Q%=FE3m^zAT2{dRHIspT^WM#*uJWqE-YSr%qn>?zx%>^|G3FyCMg<!42HmWe#W2WHFc(fH(We1_2dH8%KhgQ%Spgs^=K%*rt^%SU3Ku$?3Z9~vLMdk=6pbRs*7YBIzdgE-d}ABOo=HSHo(T?Im0(N`4WvIfqjfG;UTuLkZ;0bf*z9u3@+0`69boCdyFh;uP8ID&II0>p9!aj%JjDB8ZS3ZhedS81o5Y-n|`#h$Y-d2>JYS(#Wo6Z28~JnPu7tiUcimSsSq4Sp>LjFYBu&qWy56Sj-9b3hHMH+D-1@<J3;BE**1CR<4m<D=$8^R)o!)Ru8wc~EgA-EgY74X-B9E|oMsRCl!kuGFcRO<m8m77|Z(BN4=Y07<h@%_Ixi#SIz<tsB%h34?SY#iV)-y6NUKX{hOfC@(K^%14%$Dy<&E3sZ8-6ov2%dA=jX2g?sRg$Pl%YO+Q4g1w_I*t05uzhDm8e&{62GMul17ecbi?xCu7EK%e4yTg8p@9vS3qp*9L^fVdM@>~hSx=K73?tsVh4OX1eWA>3CJ18Nx2J>A3%6g$?PlpwMK5_^l4n&LDXWZY{KRh^aeFAbq#5gEkhl)m;b{#4jxuj_H!p-)cK{EWx3_Lb$+#DMlwMNFSSwkWY10HjLoS@$F(o*FGyIe-{=5b}_pXv;p=P_w}d;s`8dkc|@YDcqPgm6blF5GE!_5FFX{@v^d<#b~yp8kIDtRpl?M;srj)X-=pa3J@K>@|BS39jnPjpnjWXd)_2-~K;2OiNlz!d%<)&og6Zk!n#xyh4&OCnN*OH;o&-$XiAC=)MK0sYc--Q*gU46Oe(t38IirU=P^B$T|%#jKUU&^19bRguasOG<I96sM&^2)HUj-?;27RQ}Zabuioa?<P$wnQ<SlP;IX$&AU&_P8Ta%IF3*+YqJtaq?ecWVM(`eA<(mtkhh{iy$6d{=mgdXVxVM>Azhak!_N{|1cFM`8e8SXrp4)5lr?~a7XfzqsD;L=>_5)AJj!spNFHl9EcP1Q%(b9vkdvITCH{vg9A!Av5qi<lq8oWI|HgRhbn$3(~nTF1fxyVbW295t&z>cC~Bxvzpghzu)YOr?W4Y#?Ys2f@snZNI#Eqn'),'Libraries/peggle3/rgx_golfatron.☾':strd('c$~FYU27Xh6n)pPn20{yaVBPE6ABAzVoP2unpBFkg@U3AMOs;EC9T<&VFh`SNeWF{64z}AEp6iZsgUNOkWxaR5A(-*@9gZCyhUyxdXRSK<KDC9o_j_M@_~HRXzfF{OINkqje67Wb^(h0UVr2ixj2}(_j(f_xPW4jb1u}5dILCb16*Sz#(AeO^xP>M9?kl5*PZxmJUw*1Ia4tT5aqzAcLQVR?vY_!uYCT&=KUKRSAn-XH1OfB`mPo!Pq?CUP2~gVk4k1)1^IXn4Bj?6INBd=Wd=(fjjg(O3rd^@3ed96vJsRF%erpx0#q!sj3_ENDv#xfd<q=oH}YH_1Kyv?#~_z@w^S+FRfaj#6CcYT<x8l1+60*NruPOthC{F9sZc-Po9*cKf&4}OCI0|SjN8Lmq=$zewz0v&SRBFBLNK-W4+b#IBl!j&pJSYs&DUb9huG?Cu_3f~#1w(5DNqT*%R-Dqg+QLkKUeaax9e36SjaP6uq?}095jk(Z6FqAj3`h!pk1*=%@%dLqok*#vZB12y(&BrGL?*N<%#jVA+|)#5_L->wsH_#If$*bi1UHQ&w-T_@iRrBYIZxm4ma>9a%2Ijxr=dyPjT9J=Ht0Dg$U4=-hr2;<kCn%+(wAo7@2%P3pR(rmmFs@>}3Hgh`|C>cUt>qxsrkoMKYgGN@tLrZqu~Lj&;-)D#Grqi$&ONuJ^0|NCr8{c$}<}ldSRX$!_E%yB{aJlk;FZ>yr(fA@dG`uGgFSC|t9^@Dn2lGD7-6zK|!71QdYf{7L?XmJ}7zbiDxtl%A_2B1i*BlA~dwu)|!QS#D!J>3ZmTT6%0e10|a!rg#&{28vhkd8xlboNE6FQ!M2_Xi|}vDNvjzOFX{WJ3Mq|1C%*QijRk6bR)!xS{o5D>KA*BmCK9*{VE?;c5K)dw1{R=*W8)-j?SXU3{$8t&zT>2GluT@6>{Wdr5)gYSg;NJN{(iBrObllR(t8@oGLNt%^mDmUMSp@Pvp1qEezF>&Et9<xRYUT?zuCn!HGQAjNA-QcDkgMIQJI)KS=Wx6;#nn!GDgs@=SgwpDKP)Q1gp|l8@!<wTg-oX-1OMNuO3Kr3#ghWNOK*&?Yo~Kod~leg|FZMP{!*8TTD1iBH^_!z1Y-9#v*#mgguaw$E8_HXwyPldoYvDyX40B&AfuJ&|AkZ`x9rqC+&`ROXUK<X@z8dTBmm1k+SgYT>6^G6g|BIN$uj#b!bzDQVShP11C2f6`|>WQ08%(NA}w0ys^z8BVX{qhe@QeAQ+p%|E#^Hc0G3zWS@N+l;FcS0*K^=}NsG%D?mL6%g^Lw&%HWesS^q#nH31CvajdxD<o)3|ACbNi9l2YKm%wBZA=4<E;>gRz{|+38s}P22#PF>);`qY90HC_{_$OW8z6f{zkMmnkyl*2qM<J)IWoS3Kaw?@-C&C)skVMJ&bTiO95#P+mYxCmEfh@P#c@-d@=!T06xCII0HQ?zH}C;!-vc?X*@2%KVm#<(4e%UwJdZT3*V%ito_no-n1KMZ|fGCbNFtyQ>}LQKBM=u7QUdRU&}H^T@;yHg!L~~UjpL'),'Libraries/peggle3/main.☾':strd('c%02U+m0K@mGAnB27@fBIPJj<$BwdexXM_!1d=6XG=TyzT!JE-BPP71*&|V~Wyp#o$FZ|ktc#P_R^)gUDUMe1t^==aSTW!R{1<u1e86IX{eeA~y7i6ZSo^R9q^Yj1I`=x~)T!!jI2w5EZnx+42IEl}d4~>te~*YS$G<#r@_VA$#MbwpKXH6xv)L4)6a~|$*&T(0R#cMyR)2K5)t?CIi&9BS>C?R9Cxn!BA)fM9Jt-SAptW1=Gr=z4ycb`K?^kQ0-x{3mw7jWbE<@k1<D1pzj~_rZH{(CWkA3L-P5g2#z65`MD@A-IepA42$(sV4URT5~!;6o_)W<hc2K`BZeecA-6;s3>)Ck-qfP6~>J2n~yQb@5`+YGk@Kr95Kmdjf~1iT<0FI<o~AA#%<L!#%+`166KSa(&0Vn*m5moVMuE2_K~JtF3c)Wn)efT$C6J!aKT1mOP?zay)AJouUJYR%H*z@S0Bu4mBGWS?<MZxkZg@5Z0RSMk;L_+t%T!N*@1MBCxe@JIa`uA2Rd0gO_&Q&o4hMtUL|-uKHIg@t6yNKKH--Cj6}nv-59m<ZIEk@BVZVSK#`e{KLff*<8_0M<1|^FkfLV8DnFj~o;$vcA%QzA(|X+EA8w;NVfQDzU?es_*qC9@)eKGH@u@LSGJ)kz+4WWgo$`L?1^ikL#0uuN??P<X0q+i0{J0yNXX_G?1xD5VfKx6q<>Of(p%5+gx$jS_8J$n5{JVY*_Ebzl#6zgoc%CR}0!sVyYl={)FoR8}G@48SO^MU=z3FEBn_s4OImBNo9zu)61dBkmS%4B<Q&ozaD=stZjpa+oSRMCnYFfvn<DdkN?Vlv;N6vzxo=kp}X-76xY4@_u{$ZKf>nA@vlVuKnl^R)~p~8fd_{rW~F}uNxB3p{~@pH|41)TF>ZC*ygXkQb?$7yBK1%*9cb*_xCl*e$rGg?PgmAy?Xuf_jaRYb2!W}q@#ShQ-x16p0)C~lCB&kF$h+~!@dNGmSHC57-@j>3BFR~2y1jq$D$hKlU9=hMG=WHnv>-IrHiTN$1<Hoi=2#^#yuGrrvL2lu2e=Nmhm+pcFz9&gGp*3u?hT`FH=}0@#=u*T#;jE`gC<e9-HyC*I}9q#_NWs$&HSN%zj4jO7ki)6c)jxESp(neKg+KV;K+Os8{7TBg+cQo2S)p-`>+8I!`^79rXT@;(9&7<LW8r@icA~P<P-3GD{7y~P|)l6V;{&*3@RUSNEse6!0D}mPVKTcZiS#}#9H?L``zEY?AwX>2>;&lNqo?H-A~~4PLD=?FA7_eGg1L{`GaOF3YuZC6-)&}IH5;DmVtJTcGK^jcGsU{Jn@H+Yjt{Ivk8j`hK+-*t$wh!JQ;Cz#U9va%j@(<<6wvYk0nwoUS~GN;?cw4oP%k~#AF8Ryrd1H6%&6D3~DcwRcx0ReAG_OHFjXJY&cWFWdhVpz!45nBrs+>>OS>tq@Q1}!)rqkyk*m@Hvr5;j{&@Lxz*{2b?G`nI}Zu*#kwEAAOAA`4A8;MJt72+Zdh4Fepr10Qs0uSMj+1)roPw_!XH!uEM8Y#maou9{wcS(Z~+C3fKR%BCpDe#Xes9*n!q0mbz-1iFw+e5!!Gpp(b|gN-hlt|z_*V=qkR-x8`#=NLfdE_TYvr_8Q5p>r()G#UE%J{jg#MVyH~mU(9v~7&eI@5^FVm_UFGe%l<l)!Y=x~s6X|UZptCm&(5v5y|J5H3T4R%4T!NXOS9LP}J5E0+vuAbj9PqGO-=ONe06^yXMtr+Ux!_$0WEucrpeUt;TUSFN45^pPtuZW*j`sNk&?JAx*Aq}iCY&7Onj7*}95BxY7sdEq6byD9<2jin<|$jd8s8Npql<o6OQolYYzjwE@W1VhaF$4&$282l8DP@+oY_v$d#_f5@V)cS^^#1DaZ?i{T<Q6P_>R#tCuKs<_d}V0kU<%uW`?6EotoQ(jA*LX>HzZMAJFA6pGml>G%hV0G*T^~Mm|9~DIkr<jR&+KY02z9ct?37zL$8zN&YG&`A(*vvn_GN4&WgP0I~nihgbiybLZoX=y9AL$oio{UTfG%3vrIpP&dE0S3<rB8@EVZzSQEKtvDv+=hYgskHW~aB||HtDW<Dl7J4B7SU^o=!1MxL;g43&Yw?Hids<Oh@EOY&&i<U&5^k2&TVR8A0I}_>KYn$elGiLySDrL4Gopx1i^ng|%56!tzD`1&DuZ@cDITm-vxx-`WbsIygClC!ILR)H1)SE6yZ=HhDd@S{Dm3pruc8rQ*bfybxd1Fu(?ZaEYo`mq-M91b_LmR7x=-$AA?U7X7!M{!cjY43mS*A*!)lFj@zVD7;w{AKya7|%r&c#v)KJRB=_=3Rona@CEwOi2l3pAYaJ2J_`x$(KEi5O+g=NCh5h2BRVbcrTXu`&DRifvy-9VFGCQ6V>cT;7@qO5nR4O(&hKoh3YT_>3$h?<V8@(Y7ZF>j}VpgxVS@|N2vk-_Zu<4b1lrTBXMhEQpeS1x<7X(u6Hj9*a#rD<LCT0I}sP(BMmpf}W0RR)txA|Nsd^`_oypqs;3kyt~JO^$|9Z@3*~<KS5*A-W9A0eiy6J3nvxp72*H-QXhLSvOYNs91rhSV=}jr17kmvI$LPPTcM)Pku9g)mP?4_Hr}6HAh4VF|l1PBA|qjGN~gG;-rq6qGHFdGSwyTted%_y1<lsIaLb9+Y@A?Nhu~uPs9(G6oK=zK^Qf051`Zj0|%e`;o%yav#l*^)-lP?tK3<u;aa^Qo8Sp^4Fgm}SgY=$!XlR_od|=caC0)LmfSU`78g@&y~z2hndo`noK)doNq!Ty#^-&r)S0Dd)C32-|A!mt{R#bfv#M0YPgsw}L^H9)FI?CU-Gyz0q4!0wnVr4kl5<5ennW{X!US!|uOk+;iS8f*2b9UY#9*wpe}u<u3;rxcp-^~@aS-6x3t55=zgZdi#p<Z*3~3cs5%*D&BePB|mE2!1Nbb{V|L&4|5mjr0F)#h=PL6B>;C0TAK>$V3mI@FeQsF9*X%~Vk&Wfl`G6$M7^e_ya>#)#4+2TQuYN9usY*lCf?7uS8u=rs7-HrGYJI~$W*g4<vQniGHV?>su^^R{QmoqPi+A**>tN~K#DYGEJvduCawgxyMnf&4!G}frsa&kxC_IsTgrbL5QZ&+gX^aI8ff~yFpHqq^e!C-VYXi||enDDvfsb)VIa`PZHxoUr^*=_au>fs<i(4eei#-G}$Lki-YwO)pOItDtL;$d#dEed{vaX%OY!zk#u?gJ0pxPr!|RFbGJ#?gbMVwY%3%1DjedL18~X`07uhQvR+pnPTp&-OryBm#4!s!p8Q>eRv}d1+&Fz@TvWgpe(2HWrlU95gg!79N>g@F>+VozLJ4#)cbF1vI<o%&L!;%VnhKluInh8_gdR^h3}ebi8Q9b??#wyS=<}2wMCjH>kC_5cNumLDCJgfhtIHF`EOcRKozBn)Z`fJkUW~pp$3t-UBh^!PKqj48*GMaJaICLU+YJa?fQ6vTPVGwEecR0FomCFx+-=P$$l=#jk6=R-_(a<TN8>*{shJ{*e5Z%uNssRp@Iv!PuVOr8iHw4|$Yxks;rmyJr#RJn)D);sZ?TVC;+d6?e$+NW##q#ry$Kqu}b!;Bmv}F1HU43+-bc18Pp?%M9psD98y>LDwtRAVHMgQ?TKiQTE~^@wT!7CXd_`w_vgAcDky#81l+|<b0(?S4H!Y<(4ophe(m|51x3*<NCdq7QR*hr8FD$sF5koX_-dZP?}%ta?*<#b(cA;bCiqJqFYcI`GQJn$4z{SYSz1;D_2jurQ@q?F=Llxpw^Yk{3QOhiP?M{SCo<IYcsS<zZpN4GP(CM7ea2J9|f-JR{B;E))hs#x17g&uF)>SX?Z4bGqGkm6DnB1NT1X(<g0y_`R&#l<YSm&SV;u`f9z*=bv*Hqt&t^$=qh^Ryp{qJ<Pf1-+{;!oASvfs##S&4LOlA#?KKrNbopXG`dM`j!iSe8-r8MbuHfcIcV7o}Q`DDw+q+cWr;dF1zyUU-lLfB1`Qk*PtAbr86J2ZA^@Bv$)7Z6{=z0db4kWt1g<XddU3&{I*3A}-ImIm$kUi(k?M?~I)QM3_>scusU+6NREpRC#!t?qFOaga1cyPa-xYctC%;5)ap?h5%$BVF|0glJ=dMW4+nj=-KNX?V}N$Cs$*xYWFk|1YdM9%NiEr}cqz5(dsYB{)mQc9D*0KR)g_>z6+RG-1*5&@4@lvPtxLER;KulqEWrCi?JuKLcSD?5*_?%eul=how$tN)3c_b_)>E>6=TjN>rq_NFBs+nV4ttY+}DK8@cBN84j+!A6$;h8VP%?#XtSCSu#2M^M$cd7RYd=yJs16&)#i6f-8%jAm~LE-pod<V!Z`F;&+t4Dtdy)&e1&LTgpasG=KdOt=<qHEn6<vTG@!Ve*9UzP0o4Hu=MszI;%qWa*zMG)1kW6#ltZUoS81V}uAj7kB|e5{A2nqRW7lim3lHH+HVQ-FOlHTb5<+V7|2YvQzi!se98?_c~M8Qd4&>ehTw;E`H`rf+syg*=J%33{S2rRDzKESP#op(!|a?Z!MK;Up@do1g_zwZ~WJTKLRQyhxze-JYD%myz+^dmtKSk8maM=Nwfgs8x7zQrZmcW?77q^Q75>>3XYUZdgQ76kpwO^`hxEsVBmEz9s6lh|3Q35rw!l5a6!Rp)yHoG{Bby%o^Q6#w0gs!(`>i;{Yi7Y9R_FzkK>>7)hKmWPaMvvy<q~UvC;j4%pG(SLiI3vaI%uQZJfzo<P)C#m?*Apg<Fvx_8q$2dT28Y2Ceag#!^v&r{9f#gX`<<_yg@ob}qh3p$PsuPDekL)M560it6_$;+TAEb2Ik~46$UMJXKV6uZ}Noni?|~!Tscf^o)p;>X)42wDXc~?%N)e0(2Gu;S#?2GKK0xI%D44l=jCA29tJc9Joi@QB9Qo_8DGK6k;lu!(iNR!JY&w4Y;+q_BIL(GHUyVJAIYZ+ZT9MkjFb^=`iSQw}a+S^6Eu7m)?QHH{#!CQ>;-o5ru(wGPx+oZhy|f$=c$#qV`vJvp1kR&B$m2+*r{Oh~9efEec=~|GPsi3s)6>9Dt9m&IO1mS{nKt-LsVQl2MZw@b3)lw?6tB*!iJ612J<wm-kzbzc%))AZF1c?JL?D&s4~j#WXx${3-tDUD?3Zbh_2aTS%#DAzdLbK2gO%@PFsv->FjOa+x9@4-g6roR4b~81(s=D&*-mD5O<;)M00|$&Zn*EPAPKJ_yPCt!ix-q#6meNBurTiJ;jUEg&hRCtsKDCq@Z@%=}WP?S84VmHHef85QlgoO+2a12`^SUtlnvTRH4D2L}30t2LK@x<JH+Ye;l-XwEqGNfVik;l=KHopJ0l@vw!?o76SN#0$1t6_V;xbuOCuIBCsFqmrL4JT0+ukS@a{G-K3GXEM0=6324C^n!qV4D%rA9|M2y(_^LK@s>V6<O~-JImL(Y3H@Ro^>*U6@+~RY8KiPQI*$HGWqKG=AtBaP8u}V>HA`#1vQP;Ee|TMKgx8Wpxxea{$wij?nUe%!A05{SukRHW#fI5aZjne|AUzlea9d!A-6$N}RE;-l;E|l2tubwOnNv)BV*dJ7eUnQTO@PcUIW>thB0Y`s9rH=AxksVD6_$+zOefD&2kdG1&WJh@hy~@kI4@DI=TWXxT9D*0p_^Qc$9VXR7I5`jk#N`X)PxsZK46-9!%o3Cw*+9bJEZ}eAhY-2!*Ul8NP}0yluTFypsQ>@wcpAiJAAmFTvIA(2eG>D##MS!*9mGJLZ)QBMN(mQ-B5-u>Ef%HyK{<9f=UFUsg6Ldq3Du~&P5GI^BP_n50ZMTYb%Z&D2tqO)XE&VXF{>#OJ_#S^hv7S9XWe}84*d{gV2vZwaraiNB=+BxvABkxS+>Y##>SPA9lR_9sl})1I>d!!f*LcHk-ozgkNo8OTKE@KHDYt{4erdo$m'),'Libraries/peggle3/gram_tools.☾':strd('c%0o@>u(g-760zPVmcDiz2;)=+Nmn7I;|*B6*VaqI8vp}cC=oPmlgZc%(z+7hhpQH3a1IU1{ve<Xa!Ab#G^F`qL_TRAN!$yL;NqKe?ZT<uetMB<438~tS~!s=H7G9`~2>mC6g78@I`)Q^4!me@8i|!cP7uAo$`G`+<wq(wu1?mvSzzCU2jK(GUB?FQYPk{nIx1}2|4DJ9ZG9-WH_s^Iq;jk_G~>4d)>V<+=X8p3}Sz_7k29L{<#q{Nyqp-{zv|lzmnffk*@O3#bp=9Ugs<PtB!oKz}NUqX69|d8ib@-R6N1|=ch=CR!cP)Ao-=}Wuzy}Q_sf59I;Z0KB0KQvMKsoHKpmvQ*V<pMdl+o?h_nG+V#%#Ox+o<Q6OF8%WPC$T(7)y<|Gjke8IOF(AN08Czqv!f5cZvehy`l0Ja^O31%G_{)lf9tp^jUZqUkz10O@Kc!{Ql2pn)w3z*Eqn$M-g8w~C?Kmy4EKVcBhg<VI_6Ld3mk$=Wt@XKa0h;2>95r5%V_?ILlnEog#7*l+sv&{3L9R*H$c#$AR7$eaFU*#`|UT`dcQ0zl2?m?d<E{%=G0u{qZ6@1JsEOeWHbmI6Fu@<9a{c6;1H3IUBUN>Olv<82aML}GT<B;f}8CPuJvYcF&tT39O7;hs*@+OXd_+4?lRl2?_{vT%;0dLa(Ykci6{@<UrWYnmMX<DQyW!9L)qeV$U--u0mv$Md|2MKQQ$0^g?;M>YH5Ft`Er`2^*nkNCWPs@<>I8e4!bB;P{S(blXwjLkW5aK`RzfJ=bN)}3#NgJi1t&vQAttnrM#(G$j;*3Yo4l~A}2e!K8Xxmygd;I`9d}}rtMX{h*50hDC5sv!F_%MDGHox%<zlkir|EXUS5AD^z?N&GN!+N(FL{f#vX`f2sZ79(5{A;M<R<%>ZkwXOX%EUGXWBO9q5x`K5$wrWL9g=hgSb{p92jg<(xoYt=hSgW#3u&fImw5f$+rp`%M6|xYgWWcXMrfj?{)vgs_Kbh5FP1Ah*tS)$sR2|d$VyC31eYt7lugP^7eOp|7)WWokEz)im863je%$lJMkeJRr`&TVL6=g5iWq$#`htL#S5XNGD@&9p^-jEdHm5OutyG8_BGf`X1zCi$){v-h7!nP})zpqWE1ze>KH-=665nJ-2HmQF=Y76P_E!d)nH)<emes5m0TrxZ!&C~GK}L{4C1Xr&F){#GNrP7<sfIxW)=&U`6^yYe;nP!3Nc{q&Rz6}lsDSeeeoZYvogaD5fa*`KZcHRPjThIAw<vBxSkmCxR5%x~ZZGzyyr05`ETA%~;xGt&xn*m$+rdmWyjb5Ou4B-W2{V~3Sv7?E3;b{VuC;qXg-D<7H&z6uS>pGLN*xj07b>0wxsu?Bbty9Av22nyi&%gyiR5bC9hU1tIee<)M!LOSOF~H|H!`=vO9)scZHSZtG(c-M{viR3im)i4t6Oo<IarHGL*Go66-AwnHxz3Md4jzQBE@bR7^jbnC#CTu5x4m74NAu$SY&L40UiVR{a)0HTfJ`de_gsrRDp$G8=2i+x7};h+fHOi@1JkA1Klz1RHK@OP{b|31Luc@Q8FwDBdh!+F(KP4LrIGQ1-2c~gVTXxlB2~2A~k~UTqg+YabUz%!L1N|Mk0aq22!DcPy{Mh0ldvjODVHAbQcxCW?1%^W1AI}Z-FGy5R84y8OS<)I3#9&ro*6q!AX&eE&Ra{)P^4sOdrsK98R(hJ7GHLlIkwg4GXxhY5w_MJBa-0demxUmrdX~WcfaKJ+rMaiv6fH1EsT|qKLirbE~eXy|zd^Ab%=)NA@u8Q+_vl6qh?bOGO+8qtl9n{K%6!_3n%#7-_PI*J1gyj}0zzFWj&)_4sb_*7v^=WP8K?!~Nda4fK;{Snv2@->SQqN&jFW>v-4$WH+DZo5@*ZhZ0$hm-sc);l(TkeU_nUE|@0|DG8Z~-3KIf%q)qk)WTZqV#R=`FZiP7F;KPsV^X~c(E_^(_Xs-aqS{n3c@nNqKf|EY`*k3VkZCvTy4`ea*dW%s$zPIUKvPWB?Wd$b%^LKPSMYt4Umn(uOgA!(NRh;jWC0jl)&#X%BuZ+^6so$$Z)mHODKUKsLU6v~757NwT2zg9Yn(>Xj>NVrQk)`4p@4gF9T3pn$~c2G4vXA#&Hw{cjWNNR)_u8FLrdCh4hp6d;Gn>C0XRzSsOP#fLFi+aWwSPAm396Vp%_Z~U|~I9A;UeDM=TN&!eFIH747cKkZOIM-yoKAoY7H7BDvFNMcKAh&79`yQZKQbDD`LEe94tjJXY`b1CWA{5JJnErI3z7Tgd~FnAgR5*ls7ld*WY~VEr@xod22ZvJlO;ZsV$O806Z8U&e8TP%N8QVdsFJO7E~Oj#?nGx=8#oqwF`oV|KB`;NIq!bg5L3LbQlzZaSLl%N@-;4p`-zo@ySD!|=>;Jm>d2AHF<t?%l~FM|VE_^1ZoIsdU`g^#g3Jc|Y0nyiOeu3xdplU5XlEs~^J+$guN=&w(R_FXTA(TV(b96J20RM_rM-P(KMJAfl(vYwi)gNg1rI33rhIZVF+~i_2Ks-evxT-?QG`RfseM89={OhK$2{bUujGt_jjE76#ICx-@^pVYvzF5{W%S5NGN!Yj{=pt`Zo1`()!b{H?qA>NGtrIbFxYGg(+`Eb#KJL%<WT!)ejuaeH3?t8?371)E2Qw8_jlyE-K)<e^MSR6Z^jMXKDUS!&+`+Z|Aua)C0U!`5<1W1#|jODLjV2u)d1(^ZBb{D3?7(!0lQ<Uww!G?C~8l*mQ44&&*texWdEb2D%x%=q@n(iY~-&Vx%ZPUH_EKmOj%gT*6sjE*8r4M9>asj%Zpe5YbtDPIisjygKdRe3W}jncSu*jbjSQ5exl{0bjz@ux`*GldCE){T@$90Tb_M&xe`j-Nc~pZX>KzTlki6Z;1Ra-gdx00mz<y7JW{-lcv8;Ij0+8u1C=a^=giEkyxoT@`+UBHpOGvi)xw%0oqYs3>dvrl8=<dQDkVlr<yGmXboORd{0WvO;opd}f?@o;`4JS(bvMROxn^x<FbI*RCDodbDf-YKFYg_LspgeIT##$<RHC%Z5I}dDh9C%d8uGrVhYerY?|{J-&2VmZCNWaRA#^A%5KJVfd)R-mG|53K!&Qren$c!%^cuz<MmN9D>gvjj<DnZ%oVTudsC0L^h|V-I7<kFV@d4w*JNz)5S<L)C&+%Wv<?ep*g=i9{_W#DV``+xKcrtvg%Cct#S%XEbzbbJBS{7o#3128{a%zfq(zJ_wOrTzk<JK@b_F^Z@=1ESh(P-1B9sX^k8XE@Ys3>jyolQ-K41nf$BrYCY8kcDRQ>nk;C(mk^capXC=4'),'Libraries/Compiler/gram.data.☾':strd('c$}RYYj0G?^?QHCEsdpnZHT}svKq8n9!{$$5Rjow+U;_+wl`+wePwqYK(Z<a8)Hat*KEMZ*et<dNNcDe1RJLX$&vE4-}vtP15zaafu1vG9%t^oyV$WjyK`sGoO9;PdCpzm|8e5SD~Eb}{r5jPalG%;N#A#e@}>SvzUq3r-Ccj^J9KOpeE)T1@7}$K=(AMzgSCdAFFN>_aQ+sIz34c8!asJr*FWli)DeuW+kod|0skBUti)mLi@{il!`K(Xn9tRm5ZKWVP8pCl3p0y;wVWNWp#F5I&p&zM{UZhrC#$tVfB5X60y=rB*Z=V2-jfEXKR@gb<cl2W@X-(bBS$|90U|a84guOg^jXN{iU2cI$rSvKV;y`-jLG?Gtx&5v!PG<N&BBf6Y<{3rD8RfM+<ER+YZU=f%+zw9XJKkE>xlsb$`)&)kKDXFiWv4EDFQQIC&N}9sFV?#``>Zs=E^mEfc{81K{EN{iH<H@1enBlzZySG<3z7|zUmKT@_D~n8!6`oeZu9R$qWqBykxW$FZ4-!1_rPr_dfd%(b-y=e1<^XJqPH^>oRNbm{Iy?vY9~v4aWeSP(M>0DoR{4U%pwWKj#$H7$5+Vff`PY30M#=P6d-Q@Xr@$G6^TRa@QXOJrnW<B`JS;PVRM(^$RsbYIqeSkYW5YyOJ>7J$TxVYlw50<vR>UgEWZa`9|CjG|wTN2GPc=ws<^7^F8_^{<VmZ|9BRyZM1-i-^Pp+`FktNGn!>$P#uY2kWsvHmkal7C4)LoXFN{Q(OXB+FN#O$Z1jvineotA3u!4O6vj-B2GqH39j?v3(jqhg#|a+amV5t(z8&t4h#SML@q32%2!Dyz=N_X5#<i(GoN<(|vpI>LUi2@9Mtcz|Q<C<rsL`Y_Y$vRXt#*upw_E|id&(D<b-WNOx>Lay7lY<fnx2Hag;fjC>e?%N40tkVK9Io5wbWl(T9}fj*aDRSOiMuJ_qJB%Z?{_o^S87+8@Fh>+okDou>;hkZ9q$xw~HuPx?-cMuUe?^v*)nFMz)72>#KgQmMw6b-_5j@!+4!7puA)(OM+xC=gRO#L>=W0zFvE?aQ%XD2?AvJbH7+A*w2{)!yy5b9yU<H<JFp3UPEbX2vLR*+1AZ{(VgcIO<S3^inc!DLtOD-a(OH#il6J(AfYG@3U01ngElXoDYgkMm{yu#me^pHL|l9Rr)#0Wu3S8MRu#bFSA_@t+@Kf71b~NPfuVw1n46DZ1^8O5ns0C^4WIRGLBV;2BpzIDTDCJc9||9_vQ&tRC8byq#N3(3;`n)a$&q+Szb&McCmHrFx>5L0)<h0KX{t^PwBfjMY()|gZsBei7}0Fb&Xbh9PJO-%1j$R2Ra!wu!8XSnenTg7EMN%XUQ)r>)tR5PirKo#G+FdgYZ}otjqn<Q8Y6m$RZT<hGfps+FSK816Kk{~*7&8w8gaxF9|?VSEv42VsabFlNlj~f)qHLs%Mx+9AOtBec6`v`VDy&kjw?6)O8aXyHL2Yv6*|V5S|v=lpt7<coXZu;r3x+2p3~itp>zH@g)^Ti^i%Ox94Yi?D?R|SN9ocdnC%=6pFG>_<k4WU0&dDWDxivHss~lZ&fzR~9KXOClJ=!+>w;keCC^;koqH_$xXOn{0k>9HpO^qd>NYnIi$p3I4odpG1t%80=kfHyfI#o*j_E0?3u7{!5;}-a;7r<iurQn|ZuKCFb73s|nbB-PW7?uPEz0qYWz-@6j1Srd#sIN@W7(XyWo;HR+jtkfkc|oIZx1JNjA@l{)w7)<DjiTVUG!8S5WBw+f_@%`CR$`UqW*Eup2<~*vz2N>6c^|_KK75AGK>m$6HLW?Urf~!u3(~=xFiKCSvh-QY+^Zfkk5pRT~{7dxst7BYmT~dN`a<5-CB9tg!T=zMQHb-J%IKtw0}Z-1npnYo}}?AWE+f2QfQ=^e7MNH|5cnW&WtBH(BzV|oE?zUDwt4J+@eFmb9Ro}3m+h})|HDFm|dHL@$^B+vQUJF1UtL<z^0RKQ+3D2GWslMDnnI2C&cQy_yiBkWzLAb1FHDyvRs1|r1P@thM;+z#oIecFzI<o&Ow%QfZG)4+L7ig{sIoNi~~W6a%O_<WG6!1gZ3G<zJ4H-GF*nW^`W}da9vjxv2$cNr?H+*<K?2RZbKO}DN-vf!&_0mRvqcrwNQ~i)PSKji^JLbqcvt#Mn!B(iN7t;7_Bpq_m_J4yt;p(Ghx|<@IZuCCK_QOK3bK?7<V#Z(OabehFyPXq*g_KZcbQ3P){RuT4w;oIw4FDpPwrhW#XbR(^|`fSlSf2KNwf1O-Bp^!O}!fzXktv)K)FnO*7P|OXCO(L#o3#I+SFj09%?+j;S+l*zy6Tst-9DF#pp-!RlT&)qgmh+Pg2^HJU0Nhu)qZ?4J7syT8lq`Sj49->190Q5PT6UE;!J|B-jaQ>T|4r4AqM^4x5yi$?aOlX5I+LO?M)WHYg~y7C`4wYB<W3R*p#!e?kNkr5cV3hg?L?t$)v9G-@D!wgSCyM&#up#2>?UlZRNfN^ie#2(mV6aw}G-(T`A@kzch%6>_Wm8eBpOgrXKB4tjfgt<B*vt{#=0_+^DI$>_eEG;lffc_(5ocJ~aaGK?FZI`oK!d4fAp{Qm%tTxw#^jSj0>cyJ6?NP7A6bL-z{UNeT^AZkAn2~al0aZdkl?afeg9X{++pc-@Cw(_zhVT)Yk}QzJnwyvDWv6FjuE<Ow#u>WirJ%-GiNUBc&$)TpidFz!11^dn$*ySRw+td1&x~IIGm;nL{8~^g@Dz-TDK><${>-5EIbN5!cc2-OcF4C<2n8%G-A9<7!@m_@y(t{|U;TF48%;r4j71OZ0Be!=;A15bTy7o+u0Gx!T)DgPDp<Y~OpOIs!L-+&K~#i*18zNN-Vd7hf=BSU2-F_$0jGWG%|de-I?eC5R@Y}Y>ua0!?>1*HZqAHt)^BdsuWimuZPvfvtl!$K-vEdgV1Pf2K~@Nf*-mm%%);I=8cP0g|B)1ZrCpEqN?Q$<E(c3j&=S4?|FXIa?GYFSD0$F)7&N~nKab{#HiotY5_8DA<Nw%t+Iok|Vyb>2$(1ssqT#zyw!%(G)C(Bw^LH2O8TwX+iRA$tw2TzZ`?5oYBWakB{us&~g)Srx?FVS<(Ee@q1w{$72f20)PY#X^&+Hb!gFjz?1??ps8m=|O?^(pHJh;tUSCzlL!&AP;x5cYnBU>>{`O^8SjnoR@9LvtqwJ81?x`%9`Ts!ZpyBC*oHnba)V#H=}bYbHUWs8)N*afb^q7o&FpDisEEu5^_P5!!#A-npewdZxJt-c+1C^^*IvT~!b7b-WBn~O=ea7d<VeC0aNV3e4Zvb948XB<Jdwff>k7@vBJ@K%%(P-3+iQt70Mf~Vs>nsf=xC1fPs#e<|JgB@U!E+&eLCAr(hb%30+LwZn?>JY`vC4oL<yZA|a61!Uv(D5b}0YF9DShmVSJ1y51WKw#3+-I3rw`T+IlUl0uvs>u%<f>KzZG&XOdYu-m@DA;EO?cDvJCaVDe0PX^&o;?-?~r_tO<tB;+B+pI16iMyrpn?YJ9=XliHM`pvIZct!b~S<3)$*Grko8`I*hQ!0+G!hIFqSx*B5auO?4#`s*pIygRsqO)aE8jicSi1_PaEByl&Fj(Ug`la%v(U+fd?d#T}E$_Uw|ZTNt?9iozN7AM{CA^i+LdzrO;3(o7XfgF0-O@RscCg0Q)<oaO<}EXovV5gfO8td$B~X0}u@)DV&%>Dn`XHm*cas_3@~u)s5@f}1ZT>(LrT?*Hmz>LeYxoupY_&3@+4wGyMkn3iwZx~yyVt5clCOu3vte=woQdki~b5ZLiys8Sj!>s?5`J@$gx0Lc~QOeI^?E5xy|oe$MAIZ>;?jt(Z|i^Zu2YLlLqly@vRSgj2oOn@D5?g)L{&mz=Ssgh9S_Yi7Q@L(_s7DJ}?@U1u@A8v`2K1Cg?GB<qSwka|zHhC*FImajG_~hp7ywDqvkr_6>(6~9llO@-fCq$P~9d6Q|2sDnahoA=9#xfP9#A@|BC;98dgiO7DUS1mgjh8yDU_0GpLLs8>zj)rL`=;5P0e1kO0D)h8^7VA;^y_Jucs*@~LqEOT<$2z({tvUqAo2'),'Libraries/Compiler/generate_operators.☾':strd('c$}qJZBJB36#mYyxV;I<j85t9f-%`-o1$QAs)e8?Cb+#>*b8pE?2^5!LX8ces70G10-+)=TZ`aJ5vv8Iq95j4o7mq_{sMoX=giB!v+KS1(j~*r&Yd}PUY_&JnM?R3KGuHh3*tD~JAAagt>d`k5MuYcy}fz2(Wb07U+l`{Jwh3=ZAvK<YuefgrJaO)Y{e}~({&_LQg^2NwEOOI+S;8%hmW)-Q+y3%WpgFRfd$2Wx0ERtOCGMQBVGA#y=02mI~!}aq0K>?hqeH15n2V>FVOBlTY`2M+A_2iX!oH#g!UV>RcMc(Z9rRt_Si<@#Zp!a->UcE|4W<Ji!B*G?#`FsF(2Wx{63f$+aCI%-h+QJoCU+r_$uMU{1x9MN84Idm+=ap;lrr}CHxw{!$)v@hX2lA@&|<EGksmzj0KBV`Azi89RGt~*PUxg0v|nUePY4-F_5kwQ)=z8#E+-^2DSED4Ndzfi?cYmN~lfQY42>J)Y~O}e(*#GA#q08`3nrToI&kI_!hs&68rW+TuO=4c?=TR1pZ*c;n_2NeS?nl%=s82N(CIC7Q~KTfJuG1Law)z=@Z^r;&(ym%X}%BLN`>~h!)8nZ79=RkMYx`4acdQ_uMz!f?pG`QaM++`j%WbL7DVC6~g2SE0waqij_IUjF1S{Px7DnbG-;16zIVM!D2tqoyrfB*#Ob*%j60v5Sb!m`|40?XYKOSQ)gna#QyDtyQ;Ie4$sX8%d$haudW!w!=tKGHF@~5>Res<UiLb_2GJk{7QoZAlC=kIqII9~aeke@AUz_<XkFIrvHCM5&vkUdI6XN~yt`N^yM?kxlXVt+NPjYQ;`5Wv!H(AE<E`L)`v4>;;fwqscsSLW#_+=y?5kqIW#NyFr=To8$Idc#!s2aWcAYP2Cx=dz(fbIaXW23W7|R$&LU0G})gG>~N;ycaTDkJ8)63_&U74Af!V@|(;nx)85}}>3w6Kh(DW!&a3e)iQ1i|)#SA1<ktWbt7|6jv>n?;9T1XMoo2LJ&goV}QtZYd<wCX&KZ#Qi*<M1<ewk5lk_3bN$|6$#9OY|!Go!M-jpG;!f;o{t`EK2DV2DKPJn??m+c9pJbMzoOG@S6g!hOVL;bJpKCd>p%Y)dA+5qV+ly>aftB*LC*3Sa~N{?QUpD8R{c!V8b5it-lR1DM?UF~b{G4)ieRrMF#kc;^}69GP&*AItEuO`Qpit|h<V`{nuNa<4W8TDp~PkacjAk_E%jvhxA^aGa3hk*{sTTe3e+1(_BM=)<t<7DG~&Y)Xo*mO?&hu_8}IW)P5$qw@&Vi21kQi~8k`?0_Q?K#h)$JSOyvX<5MmlKOhP2B7ghK)e<T2g@tXH}7xp?e5Noyr@v2%9NrW6e>!(l!pgB#ItX*;kcuG3)Q=KlvRA8+A%T^LYHbej6_)^t)JgrKwmewN#N(C6GHlknkw93VPPY9TVVBCn{SYeK+Z?rkFfDEKl#{2>Zvv7&e=qhQRFY85;qebR4L3nnZ0IFA&Tgvr%W+M&U71T7EzoUtJK3FDv8-1?$1bffmL0MA}!Q)J^qL3qS1rgDd!UmIrh(F3YV=TcMp>AtR3+6MY2nnwg^<9aezUu1cW<cvf-7~;s!Vteu)j^3frLzH52@n~iL6s^B6WSlM0dPr-#R968XhAGjKyC4jW3~9lA*O#2+ba*|U7H3&ns5bv^`>)tI)E2U_S|x&TrLrf?u1$o-FVQA8F+65yf;d`m)!E1Qo#a6>O}d}>z0G!shsJ8>Pb{oSs3+Lw&;9Qgc9%&++<u`P2~zbp@*+1bHS>ApRU@XFon@cz8<i+AZ^8ca^lOKwV{dd$vYdHzt+wM$$veGn*Qvks_7^h=Ko!ZoIf6>jH&z-pEi|W*}iwnT%uOlW)beQR6{V+Rz}iLMS_V&-lz{;Zg7iDTXvOM8^MlM8luP04QQILt(7TcEkijt7Ss>_5*oU{PmVKu2#~EfY=qx{9jW4QVxHJC;{xo2vW=k#ltRHR%j6s*#{}HP{VkjUq6w;sKDDJjH#VhFYLr-gg6_36r7!_`y*i#&+~C)d)J&~_Y@+J&w?CBJ<SUFUB`ahV5tFt63Mx%i808GA^Sgk_?K(YhHp402UxeEdoYOsKs8nJLI)eJoc+w!o6dFWzsJS1Du%S&`+?>Z}MYqNe+L&Fi69$?0f&j7WJ-jdukG6HRV0V3c=s9$^7v_`rnqm_!kvP1JZ!3s~xKWqYz))rE_QDFTx`(Uq1&AuM(~Qc~6g9vF{`js@1$o1xS~;zidVQj97YbU9X$DRfTbS35Vg7(`X^-qu^T{^=<FmE_P((Wx1G`>slt~GZhe87r;7rwz3UN9y#w1|OVoyM>Ty(O<ZtqQiDPVkP+D4$Gx*n>k#u9!pWggr{H6<!=7BLWKsz9%Ts8Oe|@7OtZHc8H*f6sy+j=^=S-a~KHdjfC+R<VR3nZ{EH7E~1(=r2_`n1N6|^<ofjgfsjJWg+i5K!AMx*xb_Mw4TIQkjET{m~S3Iyv?NEb|e+pEb@_DS6d?Bg4!`q=06+S2+s'),'Libraries/Compiler/operator.☾':strd('c$}?PTTdHD6n^)w*zVIzGa)!pRmsv;;+7VLV9O>{m20g`yhIje*Rq$$RTRk(Al%XrFoXzVAQ##MaG`MmrGZLJ-}4*T$39e%{0DkwcJ^WeQq|PxXqK6C{pMT-(NQ`TiG71qm3?(ykA$N=s)~?oY6Vm6H*$kXQ^w?0#^_6C@(2?o%NS$A<-!q!aU7wGQc%J;5kTi^yQS$`E@^72k!7oq%l~_&Mz%ks&=FduV{I)xi0+_4!_d`KItOyCL+Ol}*7KLzlV<Xgku`EDnQ5A(OY{xK0d#XHZyJO7kaFj91WNX4g?aguzN2NP8B}~<Xl?<Scs`T9si7e0HgpXqFun`Y;Ydu4h3m|Z(h_|_e?xSdKBpsy4uhp%5y~V7`%*~>7%Ox>gzPomoFL+>Q9EWV%XI7<Z&(Z?bb)T6wi{7lgdV~A1o)5WW`jZ7${gX!-qIQ8W7_eA#L@L|J5#ht4+&ideZva!+?3L~B%s1lQcp?9Q6+sP1;6C}`gBh*uOJ#s?%XAGi<v*9_sAE*Z*YZ$=!EfzF2bDxoZv#|)y|G+j3c^CUqfnGt1qp|1FJY`Z9KPzSFOq4Pu{NlwX$|xwN_ui_DShyYvb9++43Wq>wqf(=~+5M-y^^7@YiZM5>gyo3LzwJFJ4H*g9)7ON2tKUw0AMqGI<RZFc<EO)d@p{3v`aY2OS7G|KKJKH-)(#|E4J^iiG5kPajVJO@fm)en>v9%2?73lNqhkB5d<i;O5~z7J-iVy1~II()%dRQ&uFNk<F7^n(0=MY9{+KAWz~hluZn->H)ZrNC>qL>6AZvow6bgCUH~N$TE>+Dy8;mQ1_aLMwaNIQ~XeKTF$hSij_o}mI!3m3f)zBsQVCVgAifN4TS<riN14kbD1u?xoH;+!^o}~(rniZNMVxYsiiaUga-@sm6zCF6c}LnO!k9h%@zR(8>y3Og@JYI2H=tkrlzM*+=h_&rG;#5XLzZ$Q`}=Y%Qjcb&VF(3)Y((V-q9Iib*IHSaLQql?fMa>x1RwY<6yGeYh384o@IQ_$1*<avH0TOUU7p5J2MP`x?|fL@60<Yuluxbjk($ZK)_l;0|ceXZ76`WE@}^l0uubv{j3g<U886K+a&|0SV@O&8alM_A&s-TGejsL&i@16XB?%a3sMl1+X+nanwd7WL0j%x2f8fy;4|obHjDAn-qD4wK(oJ+2-rTSNiX*oqMWA>8}mT;&p7SWW30Vmx6xhCLAR}XTW1dlf>4@u6yEC>0pr$~EIR1C=n~BHQ(TcVxS%}PjI+ndwBtjNPqI&diA5O*ARYPv47@3N(1?+AQG&i7IByW1kB<)=2nix;W)=OPJ;kint;tetZ+{YK3TRsXe;m_U^Z8WA7Qmq&fo6an$o42xyE=P#e-`hO5?!N@#5I=S?<XWC9e1;7K>Hz&&uXLY)!6>C`U=|P*L(G_<hkd2Wk~#)ahLVbl-3Vp5r&~#t{k*?s6gl#o%7{;PBVvcFwWpt-~$mx5=0kfy7*+QpL(3fKke*v5=Pv4eA)nP!rb<_8`=V#@u~<Z9_+l_kWshAvfsT8Km;}d{xHscwRsgMipUp3!{Oyb{WxbX#trC+e5%0E=NHW1DdNTzdm*sEU8-Gbx8lBxz&Nw-9(`AT6m*ZGby7jURJ2Yi$fbH)qG~MC(WbCmtiG|TRcmG5T6t_OuAj_q)OIQpwcY2htgRQc^5@&y-ob=5djG@dha!AF0D5RmlxustuYnGMj(|3Swt%*QDnP#g?Et-k`@bMLStru>YP6+IZ3}nz;-=fl%#fC6x!KxvO}+MQdrU#{-^D4Yvsh2Nvtf<Dwkjjm_<?o*Wo>61l8Uppb#*%&wcX;<@gLUy((yVIy%ABw3w0gQO}5eMY^<>j$i066-Q0<P'),'Libraries/Compiler/node_types.☾':strd('c$}?QTWcFf6n@vQSoUcq-MW_33mE*M*lts*L?Ramq-NR3D@RoFs;hOoPzsIfTT?qYR^%wbsV%E^ENl!drFB9QKOE>w{)PWQ4gCW>Gdr`|U9C1Qi9pQm**V|&&ShrK6m6@b6lbOjj%Af=N~uz{Y)2^=h1+I|z#QDoU%g0lojrYiDWAJ?P1gxgtLD^H**yQjlx<XWuBlROs%+gd$~8hYqN<cqjjQMKgwmUYysxAcN+%LP9n*F6qGeYM=N+I~Rns;c%Z`KcCTGURKFj7VWU^QF(d>BUGOBU3FUCngr=Q_s$sHcSPY<92b7=3MXAPAZc)iL@q$bUx0<-WGHpw|?!F~8ytBnx#OLs7X(`sfFUle@8IR~&X@+sOfwR7Io1|3c*_#*@sU}ty)#}=%@BY1_gSK);mX{ks&eQKh*H>-_b+1L@|9<reW-`XX|WSj}pID$hWNWmT0fJX!gQL4PB$XBMsIUvF^yzrRNfns^4cH8?<LjO2~$CdqT)0wfSh4|*+1pkmqF;gq>8~RZ;Dz_#LMFeE{Lhc5sIY!|tTgHf+74td&d+->eJPSLpOKw@Nb}2VTBn*lVp+1a51LnD3_(})z8V@EFSfW0>;Or4}unBF9yZ6eIz)FHocnk+Tr@RIRDY}3kP`(a#L-O>5D2uW2EJ;%)=vv|yevh(@`p$j(Ly*=2?jt4l#=n0(dx-z$$;$fall$y{5C4m*&$JHvu}tf*8f7Zv>mm7&FK>tB=Y9EBNdBQO-w4S+^5ylA{9|9f9Fl+XP9lda1h`)~8h>xeD&UdC=VMqTLxHHx^@-a5$gj`Ol}RKjCa10XMdfmX@w4<=)hvXkcG-3Mu=Cb(9d^&avIT2!++Ay4xEcbWF2+qcA}g`ess7rl^F1d>KN$dCApzCTfExg6MS#3GOwUvz5fIaV6{ww9wXeT1?0CJWLT^iq?cTk{M{z1u1nDj~0kJJr`M3tp0~E9#5UV<hAZ#<jn%#$&j8qfu@a&9Uzd}e_quO`hYrLZWWSjg;_)+Y&SeULCt3_dRDTdFk_$FQ3NpPv=*l{j3h3ftpqGGzSQQ3&FkdRvmP<YT(;;^C^J7R1lCCjv@<FM)xUT2At;lzhY7EMoyCty_yMmY|v?=nfiI$3Hms6M-2Z;izrfxOJ*VIs@S+X1<RFDfqZ&lyR1GeTL0<3R#tCXaK!r)bZBg~c0-^+@P$pCPp;OFtyhkuGjTGTrQjB;*Z=WQ@zDg2_`BmxkW+E3$_(zUwWv-D3MDGNhDh%4KUBn-<x~MbENse}f&9?P!5ls~UV`jhxIgJ3^>5#3hO`J*miYk#jWe5$zfmneqJ$w~W!4@e-ZGkaYqZ;VceKD!VSC4y%-J-Lm>b1!7mJPnrc?Kqc+Dr%xUn^=|(mfJO*FG}A$Z#%%lnB8#mZN&8Np#j%@EjDN3jLRACrMzy%Id>jF9C%QdlSLIRD8{<RR_hanxh5>@@(0;c)>I-lX07y>+a}+%pV-IEPjqK)OjnC6hj_P`um4VBxNPWFraza^2<{E;tJvjfu6*^TBOWdPu?3+TaFf-mK+11(Np2r$I)lq5i_4LWZCH()yq&3rF2Z?`E91;`pG2ML}40LAaDQm04*3jI588nd#T0~!ef%(zQHUHLvbO-odvw;!G<=>WvxTx8wZq#Ij??txoZ9j_a!sl%qE^BD+!#s_<`gtv&clGO0^G>FCwVuNx;CvrAc2Df|fm>$B<}o~%%~oFr6VY3-=yE$*J!Xabc4oZ2H#sDI53o?Ag{GSl3wJ@xS`p)%9K~wrpbwX?XR~T|t*`M<o_qOhW_0{wE;}}Uh0pj8dq{3Y'),'Libraries/Compiler/tree.☾':strd('c$|$?O>fgc5WV|XEII8|OO&KH3m*arA0llc+FKM^X}tkU#*XZ*6d$P&ha!P!K`IC#Rj5}EAUGfdhxud7t{tzFs8CChCNn#4X5PGAj?eLAw0EETzP29hjE0Z)eV_A2oCMNW`CMiV5RaqeU>ao{1aC9|KorNjz23dS@OF2w=ieFhyStQV@E-PgEeC{g4o75;Ilsx;3}E5}a>gj|4o~ryA7=iOMERLIn$7sqEARzgiY>grH~11<htU^O(lb2AAKV1V{)q3(SQ$4FcEe*85HwZoi2hQkj?$P_K4Zve9sL5&@Y@=CoG7NF7M)!ioYz}o8YzqoSPh|`?bIBUdrYl;=cdE2oJZ5A2f>t)_Y0o6S5Rq!6^8(}0f3O=g<nRQ<ooH71aKT4OqKMP=Ui`DNQ1n_Pi|Fsd7?JdER2Jyv&9unEkp?g=37w${-)3={;?uhh}`ael|b5YK5k9^Mcyn)84ra5V!Ft^#B=H(A7@c`D0y4#Cb5JGtZkX&XFS25wI$#3SO`qRaodIKEv<1#7-drmuA_+hay9pkAws3OKTqcL%Pa@;G+E@H?o_1m(7Q|bN|q&zQeAIn*xOLVF}@`wml}Ykq{};R6qFa4<=w9jq(#9^ITmKja8szm_;fDqIL&C4VIVV8oGv((HcXhS-vYf8!P6C2ds03Gz5al=K|89YMpdniO)mSgjM=uW6lD3vXs?;k{@tSCB7LGcFIR48?9j@Ej-@NHP9+BrnN(Ay(&|a;l&EC3t=X!LwM}Df+p+ZhrggFZ>5~-y3O`f=)f3r_6+M`Pu%VucB<C+KIVIW'),'Libraries/Compiler/tree_txt.☾':strd('c$|$?TWb?R6n@XI81`wVt|75c23AOuP=l#0y?_wIvguBmrQ1!|ouD8-^nysS3cZMU!y>g}r6?6CVxP`G@t1h!l5Cnra2}G`GvA!^o$s786t-Y{Zs9g{UAe2y%+1a(x-O-bh&i{Iy%KhsUYJm3Q_EtE*&0|Zm#1s9Q^neXTdGxxckznybf-dx?l4;!XXkKRr}R3>6UG`DpSMWNAH;#+ZX#kgh<qLi>EHl%;WsN}2(F+-kVe;HB<ctfL?i`dxxvU4bJ2?<(mzyo^+Wr);Tpc0?bdS*`>HYDAlFD<=16HbEI9pyat!fkghO}<-!9qn4U=QJQloek4Jvf26BC3#hu27aIM50g31%g;7D=z^uJlAAWlhsbS%*Qy5v=`43R%JIdPDI;<11Ld%CY@l^!gNOV8aHS!XA?}ak~dEjO$@aidMDY&_0=giYQpX*kxdwWxZ~fN4|t>??Fo{N*sq&8RKEX%|Sg0gJtz`2G8isY?;D3oWO;xIjB@hOY@ZGZDv1uEXf|gnf$weP5W*q;*9BQTd)uBVc*94Z{fS61V2Z?O(0u>Xy~mqeUE5U!5j^`%Odw5=5ESjplHVF0qjVphRsLVhF|@hq_V0Zm?nZ!j|d@qsG8cYRyeJ!Jt(>*ES7#^taCV}Z5%!%S5yO-aN!9N59aNLf#WuxZgWGGpTx>fHqyZuoftKcp6|QOu(Q0Hj1D4Agcl1ee_uayT(~qsLY7x{_L|Iqc#%)iW8J+P(F|AJHurq3w3*Z=aD<(^0Y~tOE=}KaOY@cDVg&<OQ<faP5AYRs3r=13xHVyE&2bK_KTkhPz*wBL7|x}F68i^L@$sM}-+&3zZ?t4OF>h*VOF~RP1sLL3dQvLrSJ0+o`U!J=2S4FBZF@B(%E>=3jezAFbjy*4Z(x_|0X7+{4QwK@6Y~`74%~smfr^7-v_#ycx){lj3Tfq1D7F(_c4WS(5j`))J<c*2+6uARc!ck?C)V(lPR8}YP+)|Q&$FMV8a9>S7dmJcy)u6Rn7DU2'),'Libraries/Compiler/expr.☾':strd('c%0o?TW=f36@J&R*eqaRR^18|jlQTQP+NA>B8nwg_LE8wG`UI$uSs^fYMi&kjTI}cEK8(Z)%8V=X{WB;A{V=j9m@ea@A(hWW1svJdd|$5+1cG$iHcnpC;@57*_kuvKHoXR_(%Mcx%pqRS`EMb>g~DNlc#Dm#@sjxf?9k&c0K={uydv!_L%20*Y!Nlmy?eiJND+x?9n4L^R?-j<3~=wGC}RF<IGs&`C@Q(4!$lh_G4$#@x1C-Ggx$*LA%ooYMm~w+vFSknKw1&z=tWW^tjJhI8{;POWs1M3S*tr&?F8;siAU}_CI!fhD~}nC%pl%#rOrj&Nrtjtm93<_yD%tK`G(QZGM$M%kL}3pX4`(@h$$r!8qU_!kRBZy!yE_&AJ23{GIow?4yFC%lwhx83vG>iP#@kKYL-T5wJ=BM5i5iu(8)#WNI!<bl#{q%zbg=+I6&I5cUG~4nE0Owh;PJHBrFL0tF1S3fNcBZ~4;$%9|2&1aZ)OJN!$lKt6E2%Kst+o5{;`awKsUJCPGRtu~t>U&T*r(P6PuL3Va;-34xvS1A=BOPhR4K7L2;1wl1;)J3k`d3=<7=|=x;55!LpnyjxpeM#0an%wUnt-4|tzw|mp7}Ni>X-*cHX62iM%QsK*%}LXk5|*p4-$b{DFDZiL>h+i=#rpS;ujg3DJY}E#@9W#S+3*@f8}NT5q8-gmN~at#k4_-`O`6f{1BvOQ;z+aTB9W^stex9OGPKFB8sRW+<p@8GPCIV3mjWmE_J9Ixr3DaM9$WyS?h)D74v~1k1^yLZrE#6Gy#J9Ty}-#c4LdyH%j_3`LIPiSl+&oU+nv}s*J-vE-*-A){1!OBUMiK!<wHIBe8cq)DTQPNvg8~&^S0EC(4ka`1G%WABS!urYI4R3h<A~1Fg(EicnSVi0BF5EdkoLV2Yg4W^ur26e&s3b;E_hhzuW27cE9e|LRd5|U(3~*15^-140S&tDPBEL$D^+x76dK^zbA8q-X&}y0?bU>lhL7#(MU5oJQ$-7_hK}th;@kHuBuf6`!J7<kFx|mP6Ti`Riv$y9WdK4_g{}(56%q7JTr`pDoiDo>oKt;|GO8&tvEQRJ-SR&;Ok`a)pX^<;L3-qi7!P#ycD&i5?96qLT*GsJq~J(dKfAPlh*c0ml?dQQaYw<jb-uBqVN-0Kh7t7`Tl7p<L_}86rKn03XcRk6oj2;->d;Uv0(!|vhis9+o!wB8@o4er!r8YlRm$~l&dE?OA*-KUB0sW@Z!D%hB*TAaJ{=?TUy|nTl`PL&5>+|x}RZJDN$Q3vp;jc8-N#L1hvTiPi^j40Fvd?Y4se6!9HK+&&6|<o*${FK*K3!2*j-MTNWI!#<xd8#e&V#kOgzZ5wat3r`~QlNRN=Zo++l_jP&?Wjc@Bh<r;s+Jo=1T62D-eP|>4W^HWmQ9r4`2ibV$A_-TtBMU-~yQJf0Tf#1wUW)g%1zHBj9Dvr5Qam<yfghg8;R%93WH~cHK7JLJ4WnJZd_k~P_<bb62Z_Rw!6p=zjyy2n<y;;j|<9a08=W9}ifk#Ctre#r=`g(aakMG1O!dT+*qBN%jwZ_-1P<4%8wnEi4KG+YcO82DtA1u^Xg`_w|Jja5C>@dzQh-A+BnN;Z$E4?$2;?EWkBQMvQpG;*1;k?32w?KsFVvnx{H2W*xW(t#yVx#|8L%jEHD+~%0Wub_2%h(`keEZU*jpZS-WAcObl@UJl21^uk6w@FR<#Hz9d-P7~3w&nsC!U_3kOtkWVX+<qsi5E}5`3cG?FQ{8?Ucvt1zwrc?w)&eJ6)D0T>#Vf@_)+`?U5}5f+fD?{0M?1n+Xf6hurCa;(W}XP+a&eVMW52*JO6b1EUN8lX5@kGJIdOFh_uAxr5?nk_|<R)6(M%qY;yO(H=uzXoN);;?ZctAuwQd9*{&~s-U~cFHRphW!7}SOfRSf=erTIkmkT@74Z-C+FM#&Y@KH*JrXN4NU@<a?PdOFkvimCQ6e}x3X=eWY50y-3&bRgU<lQDmx>=bMM90N|4EJ}TJ2r{nl4GO_c5V{OF(A#$_JnZ*DQxEa1@9bWh97Oh67n4JK0_p84+{2-V~#%M19?q780Q+2+hXz=$#<0Mep{IlRSvZ^}$t%V6O&VRbNQpU3*##Bl!fc%7JjUFdl}!y&UTE2W%V`>+e9otNKx-P@>#Z<lOw0FR@iI%J#>FMU~xvo3uY?IGf9JR-gpR8b#a{a<rdrPS{Q<fP_1?Gc7TzFS;x009Vcg3Q}M`x%+|lu(upG2%L(R<oZmk<wR!e2MWDMEkw9?$A)`VG~_JFZ6##Zp;HM9Qg|wd9LUjhT7|^&aOjfj-6tXLWjRV^n@rvw*_HO&v%s75-r}EeAZW2x`4@r+JUunZY|@=>*UyB36L;jf>U6q6RFA>y4)vy-FsvNv{S>q*9+CVN;V+|Q2O13{KMH{<->A>%6jFdUTbwOaeNxEam0f&k@R>fqSVL8*Nj^6X2Eo!O>hNo@(a7M8SH!YR2^P#H`xpv1Hf-iL8!g}&iXQ-Eibt|WV=0PIh+g*A_vc2xZZVF!=zW*A!23kmC=!K+2es^C$>%b^J5{l?7gN`U6?tvAey7&!1`SuEZ1bv7*16LAjgEudrH^%vb(hR0XWy&6xUsq6W(oYBe~vw48wn(?$jF`v$fQ`KG?`GE2D292oGwt?lu~m-CDnlG^C3m`{geV!@6hv;S_jDp&h3P*6QR%Oxkb-yHqt(ch<-`#WoSa~q(mxJRU61`@ix+Nl)N%gQPONLim~Yg(#p<7*)JRI-ePrIg~VIyv<l(P9sUWnmB`4VuFsiT$VgKE5bcVM6I!G*c|ktlpP9-5tmaFeyqE1`>ujKmK=^u#KQ6lXPdpn`pDXlLRv~Wln`pb`tF*&drOCv&&L3M7<2wJ`ie}gOy^(J@MPH@ipA~(TX-g{w@}+V=)NJ7m8!%%_vG|cV?JN>06|TNF!s<!eYSNI|80ce^lb=f3p4Loyo<;>my0q+WDB(B1tw(z(;c<}|b`Lvvm>YiYO@O<zMnxA!dsS?GSSe-g)AN>kg6#bH^y!ldD*Zw9{!y0XGVR5UEB~ZhFtjv%xko^9j5UK^9kxO+*6A9xATf-Qa+eR7A+Wrm5hBDD1GHr)Bo{$=`9ha7GHZgw{{i~0WHS'),'Libraries/Compiler/lambdas.☾':strd('c%02zS#K0a5Ps)ZOh!WLCKJnRhZjpLg#bAe2na~>U|Flh9w#dn+nQaDB#LBjf^j(4XUrAbL4eE^2Ld+tL;n){7ew+ONL5#NPtWCD)(*-_?VY2#j<2h#t9s4EFXG(6!=JH20k1yafAGMeBZUHEu77$caJlzwdGKhlTw&Z}uFE<1h;Y}QJ)iD7@bRvFhYP#+?cMbyOp%<v*vqUr+>;Lv9E8hm#y)Uz4(C1F`uu)JTo#LkVqah3<T0E%EhfZEPb`RWaXZi4e{M{zfN*)gB=4tdAiZmw1D{gA1Nwdah0C4NfMaI!HeV6oC-AE$f&oXrl+WcKrY$xTyW4xb{Rj5o{SEO{oJX;<VkF<eEt*^pZ-bjDxP65%z^er@BmU^hYrESyFoGAFD)I)V6Bv8;?qfNQ4@jHd6G2!0#~n<JfXqjXm5axZ_7xpb6A#5?SNxXIMTjLY_3MWS1~4M<6ktDb?w2b*>GVoG0?jo!Z>!=RS%H)xwi<tDV6ci@K}YTs2l^aF3xv-?EJDmRCcLeew-twm{DD3uM#Zf{pWj=MQ_nL6^t4zMuQbq7q5E8M_q0kpTr{H=T9u*JQtN6>H&$yYO|7Iap%Z%MsdUot{zz~F-d6l-v04pGymTl6xXgu@?UuiEg1>Z<zr@{I#?nyW_YVfgi`BxZ?@E<peozVZu|mf9atHWw)yd}_=B{0zbR$@4T@3@HeMfkif!3_JBGI}e{+5e1etvCqa&2^6VPJ$y3`$l1cxxD_!0F1fbemA{KR4=6K`glkW2Dt38IqbFqm|<%beo#EChn5bXF=n&;a@A|Qm>C0kMk4=b3JM%b63ZQSL;vKm!Cg_@jQYi%;^p92;T+Z@H6U8S2BQ&f~b>ihQUu7B5sOv;<-f{u}`u!@8oOE%Cd#hfuz!w8BDdAy^1X{wRKwk?K-lF+oXMlEHZA=9$uz;1-j0pSj-N-dyuW%wYlHj(0|Z|&AAVL{Bp|D*!DuEC=FEnpvu}?)Y6hw@tuSy+i$l}SS)24F`c%*o>?6q17Cdw<Mk%}HQb1rb=z=8ruP~Wn|Nz{IjQg4xwM|YMV@`*-FmiVy|op#r0Uzb_tuCCojY|KY_JE0YdRv{pg-!IPYHarKCxP#fyA#fIgA%DUapPIQOK;;XIJajh(g8=j5q7cFNWp*Rui|xZDcwwW|+LcCeBc$SS=^3#A?u7eVE*jp+-EKQgz}AUx@ScsPvhNJnt~{6Oreg_&kX6{;-i=@R7?oBJPEY2^w0}vU0x*;UigY$7<VZxtp$VSLV)OfU#MB>`DYvL<A`!CK`wc(nPGtWa6<j2-`ED%3dyndtR0%?NpmfrYhA)b0}>wm}b2XD~So^e=iJahtkhtIH4J?q%)idQ+<6_x$B!KLlsw~@qLrvFX-x8s!Ks3*Ff>L-mXwUxG`Rf7B8znO0u$cqcl#?3IHc}du4mY<=fHGXx~FC31(a#+5@n8x+y_Y`NJa0#fc&^?#Q*0QbIZF%PYgg0|WZ8xTtt>guR2O2wh)Zexqk--8LeA9VO1C6O$P=Kx>A{)(&T)a!TA!I==1RG{Pb@byn06&b9jRk!(m8n}Kw314uFbP0NjZQk)g9<@Z>legRZV<a?{Nl00LL)i<Bnja53$u?Pt^U!Gb<uqxh#eHiYpo%Tj6Q$VvVTQo21guJj*=Y`7{7m-5`gl0}bG^xJl)%Vnfd!!_}qDXJXSlr5Bd7EV&GBmL(6Q!q|jZP8hDByjE!bs*Q^*;1U0FG6`>rTs~Bdn1o>#n-E>e{Up<`wA@PfV<(oaO+2Dc!ePeY4g%t2%=jo2;rpJC!MtU2?kP?LD}~U4NwJkrJumY1sFFWF1WO2SY4nQ)JeGkUA3>n>D3-4YJBpbL@njk?*PK!xjB<aKQJZfl?gmREX=4S;m-Tk=$=*#Dk1d=3%^)N!^F-n3GbFL(1|gS<ZWTM@GS@3YLrN`xpIf#5X}o#l&SXmtxvwEDo9|B;slsH)}g)&K{qoLN_ah-$Fu7JQJggIyyt+eNu$%E~jG72TRN;qB_i_%|NRsV^?bAm}<o0CjCR|5q5kVNt<s<8ra!LTBH%&KxEj-feEIZ3gy$r2Ld;gmS`at#09ZLN#Aalq%t;S1WFErPl?H5WgU1?Ztcx?BYR4`4|{kFL6poBvXxvAms7GMkhUcIfssA8p=`!%`C-D=2e}$^`>h7Wq9OFLf|m<GwS4piEwM^tsFuE(&s->NUiwLbrFVxCNRUzG7H3MyM;{KzoT^U+BIPF4P@XK4<<<zbGGy0olGfwd1ZRj~d`uC5^d4ED?NH?;?LG9fh)EfVTFs-y$uKkOn_y>%UNrdByZLOFNq3kXRBF`3T`_M84V0m>F({ZpGOtJ;$`hfaZ~fO1uG3dTIcQC~6ce0TGBUk0!<BY_b;wOFDM6xEQ93@E7iHdLUfhH=QF)s%$X@5x6(;`$t(}c`ju!PcihJ5kThd=^ITvnl?-qAY2V#Uv+_~`Q(iO3yyv$P`_J52KNG7Q<k~q0k^$;nX%#XSRm*S{0S9SQQ02+(}R@TXL$H>mvUxhN9xw>EnEn_7-8EOcTW#PNRP~bxf#q_VMcg3-*!7rEZvQfMrHj3d->#|!E^watn7<BskA5NV-QLW%V7pTLPcF&xvLqDn5Pl?~fln07j7k|;#yaM>ibM~u`)|Vd5!B~KC6UHqVcVH~SxCi3_j6Y%gg@C>9SlT#TeWEI+gI+p5R4(<FQekfqS_NSgpA_jXd8;}sP%YNBe*v;2o*M'),'Libraries/Compiler/rewriters.☾':strd('c%0QdYi|_Cmf!gmo%z&lI+ksA?_+dlH^lg6(I$X^Xz$8vjmG1~j2O?1X2xdFYF9u=cmzx^#+YCNgmpqf9^`QYgaA@Xx*vCc!b<+QAFd*0f54tob*j2v-7_}uVJ(K~>8{5)r_Q@hb;wS!bNdebLs%~3)$X_U?cIN{Tn@uRy)rjFQ|T0<c(&f0uGBkW6o-XE6h*OUyK~pBH{RU)`p!2Gl*iwk*trLK@xlIaBGmdsF~7NYA6!m`;j6)D5Jgkl!d9i-Emxb3Zm|@KsRDMJ{lvbA*?VlgDDU-(;oEQgsXV@aV&}n$5WspJ01DYH_61uimL{hVrXjesr`bqic)W4uE;h()hl9g?F%zK^vUlM2J^C3%VJ`}r?SP$RAF`i9erp?cxy-JW`PZlHDgR!j?{)gVZQ!!VF2(%otoXW!Usu>_2?%n9U0};a-szqg`keS$2}RE+&YwxNzCu4Q)AvpJEgs(qX&4&yY!nd;>NzzyXLJBqBZ2lzawupgN87b-Qtq_sm2M~G&@Zu{qT;py{_yuQd(0jcOaB@cez~#yun-mT;)7?n0&sEVq`dQ>5dB-kd%czpGkmDqZiPVX>+JJTjIeS1tmsDTdaym8h<*r9*#-gsYKMYQ-JcwpiiW#Etr4hUfzxKne_1NyxG;SB6XA`tfh0~`DAYv2Q9zdq?Au~V^7u%E)5Jts<NoLrvHh-zH^b2gZy4hXVEK3iYN-?e@2*`g*r1r;@Gc}#@Ovb^<jeOlE&m-r_}BZ7pK|W*Bwbj&IVGE8)Cn#})5{SJ;vE3-4ijSIM?2}xw;O@BgfK@~Elmy$CM7BAhJ1XlSZPvXI^0cF2GBH`incir5i}B*ZR(-JW5flx=7PNj=B}5?5Cs2Qdv}S^KVwgj9;@s`3AlHaU5i2~y~EXJ>lhMxAo>z<6`3vi@&UV3NYq%NC8%eJJ*OG8zr;S_6I^2VZ4!AX4Fq1|U7wfA0@Ou|%!<<P3J79vb`_*Z3aSWsJaQD(#gZeFysd(anoHPI){UZ|(wHHv(Eb_CNZR#A0xUE=oLKzIdhkcEsfkZV_@uxqyt*<$WMjf(<%MWAHF_vDf2=Hd3HhK%tSIe4JOoVzKd%x0+I)R0%##h?<UgqCXA+rcnDhD-_Jj=DN)-2i(`$!>rTG$Ue3Sq!L*2@AXCM?4c*(KCJ{g!CIC_v_S3+qi6?KNVWW8^Y2Ms9Qf3cuBTrU_lcqPjUrK~`Tgu@YUUE2e+!qtEa^fPSn5)%k9Bv-&^7YXe=B0eyP=#0Tx>m+-`-qRTCR1|VS1NY^BzW5>h`Pu)Td-CIv(n1s*t<~#6vXC^o^Obu2SWt!kgTE|=|1v)^GB$QZe8me<!I~<Y^rS(yMEYEs!@!c#Qq(2kbwX^$4$1Y)u@=o%x7KW+=kM_ovrU9@o2gL|rd&rimVR?Xka~B>-Q4NumWXO`6`g#PZ@uN{lt-Bhh3gF0Rou1&pS7}d5o<GCO><>|8jOo#YR&w3IU~3j_El>4a-2FfsSZk(qi#IRHRp0IXXdL(nO$@(J#a0+xXd03^S1(clq|nHiH7$^sFy%`{>v2HOjj)w070Op4Moo0AuxLl@a5B4I`vvL2}ikK0Xp3Z0^qNqR<ozpo84jO*pKiCAB@Voa#2pQuh``xBE_#%|7L4k;~4%-@{2SuyrIoZ%KAVw*+8=R#2PRLa`n1NV}>`f5i>eqs9bBzCmvOz#;UYhe5^>Ptm9LqE=aWy84&~yg7HG7+ih<xUa(i#&<(JXj#lvb=yR>|#+l<jnQ=pozEX6J#7BzJy1rJirYX|vF<@QwW5*QF1z^`DUGS!)=qbQE-MQ||1)KvB>j-GD#k$&4_dlcFpQIkA)^MyJa$*5z+pY3+{fI}Wqd~Zq8sJ{h#avg&O0HluuO?OvkeG$YtE{zFFiiPyQkl_OIudP*bh=E!T=XdT7I(Os*F{~;*5j!m6A&TU(wt@|HE_<(#__WP?STWLtU&vPWyIhP@}WgE<v#uVY~$hT&$qb;C5XtqP#E&lf{YKY@pgz6PoHUbp|7|-WZuUC@%G;r$gAA~WPd$=?&sToy>+24Xwc9Hn}lKLIbZ;e8Gtr|uQCCUM6gqk+L~7*-O-w>w7|e8)mo(<_LRhyR2V~&d2qB?BH#8BTagNe8<vo`c%7|sZ{_M&@c9}(-@)fGe4hPsWAy}l-T_1=e;fZU9vzEEN8-^P@$chNj4R0VIXDKA&rU$#b}bs7s~kzX?MkB~{QYa@95=s!&zJClxo*N-H}Ave8~A(+ADH*%_wf0%1`9mD3eT^8i*WHo;>hUOj=%Za-~9G>zpqSJff9vO@TAq@iq486*JY^w0lS+UNa9~1C~&3FquB5SJi250TT*G%8r)f2O|^!9diq`-1O!3L5EgH;$2BuGzQKOLytrsQ`Wt|?2TBQv4US#{>k!#6B4y0vZMW^JZ@5|R9&06?Vo9m0WUkdchRs1;@#nwZ|72ZW*XCOCvNJzTmyPtY+d0;uOANgll{xJ}d3L_r(YhPIVPyR`_116UG^6&7G5to;sa9G^LGh<)d6boIbNMM(4_DegQ>_bFxLw^3OahDH6ao8Md<;~ebs_S&4PG!Zn0ZJf@vgB)f;+#p)e~o#6YO5fT^=2#Sw(Qy5AsBlW+z_}cCsx*ETShde0|Pt=~gg`Tzq;1`9Es=C-j2XXm$e&M$-$|%sGLXCYlDIT`!6(JO*2p&ElbBV1w9K8=Pbh*;lxj*Vt)u=%pfZCcg^Ah83o_ycn5kpfNu;op>~XPf{AmEVj>N&JQgWhXHCB6=+8(4O=sC{EFR+&=7uIFv3|%VB~7*xAz^`y=!9E-hbM2;Gg&G+Q0X$2>`lYYnk$DYeb1xtJxvE#9ZkUK^-#tK=<qHx}19?vYVBYUTX`q(Swfx>GTECY2*AmW_L-e%&CTqJV*vZbdz?Y(mv)eM6FZqwc6!Mw>hV6YNk%T<I(pD*?us^(a*iz!qW{_?sEv9Tx2(m`+6KLgXuo0|GjUN_wJLEm?1pn=Dxg95Gi@eBv8|_DLb^!O2vE71Hd_IHUcSPx1Iwr?0*~j!{|7olP1B(O5IbY11*811w3~08Il-lJmlhbLsCtoelYlaH5e5Q<rwObNkN)m3nbJ%zU(aMkeI?stAN7}bk%Ys{~!6aTP)?UY!sjY<t{2Lm0;bM!lW*XjtU&h9t6h*L{Q}8brr;?(UR8GLih=eJO;#=?gO6slYWG}ttS+Ix$)te7FY;EP;Qa~5t|*cFYYNhDnaBC@>IH><2AB0E4Qr_uK~_roR5nI%iubLp{zCFJP{Fc=-M4;rz0cMoNYJfTjg%0J)3ySK4zNTVjtI1(e&yW_?&eTsiT7QMk2K^T+k2>!Nz9HVok!0aoSHZFNMGm8cPC<MIjH=_q)72KF|i5Smm#gAG8o%DTvC<Ob7fiBPl)Z**_+h88?}7TxZ6)YNhTLr*Ihdt7Pwx=wl{}J$sK<H<iT@>sxLg#!9cD@vMC--hCV}ttXXs=-EC(q#!EpaLvO-+)8+-bN8(7{J*1zYxRU^tE<)pB(%6Y+-kNk@oZ|s1&z^g%haBCT+O?X_Dt$d-%F?S`f|CtMe^m8UBN)s*dQKoGk>_tR)nIZEF5n4M>I0?#J9a1vAc99%}vM@RcI5_1{?&bFW^$&+)G_fd(^yba4sSXJ|^H#IP+|B^J4$Y*|!iXFsUbVNyAtA#>)tK@?;&iSt+`d;e#hSm$eSroJ1=%m9?g)oh-Gtr7qUgeo{1<lBEt=`<H_S@HpWW_U?<T&Ma8ru~1LIcJ&&M$%csBB6inOt$oY`cUXD67o~aFK7A;;cj@%T@v|l+afI#uoNa6v1gnBnb0hOBz3kO6^s_J6bm*i7(|l5EzaBZ8VG-zUA+%3o=6bY7Ii+oo{GMc*7GEt;slgLH1~rUSpNYJhT=#s|B<w>bas!NwN+Ngc%Qjt%;Hl5(!Vk%(kO(gLT&GFy&&UX0Q7(USo@4)pcZToKB?5WKvW#VSW1&*7%><;%0!&&4hnn-?bO5gl9t(iSUXg_>8M+~5vq85w-xF2PoXN@K)j7i0=&&L+QLB90-i-t!QLfIl%FPz$aBB@$FSnEWLY8xyA@rg!Y?=L#Zv6q-{`0ZYo>cmw?+waY2cP~G;j~#b@`AD>$ap+IDkDrpS4;c_n-29lmAPb4dLg3Uu?vz4R&32n9I1f_hO7n=Q5tDw&=u}|#NHj>c~DybL@bi@r4UPWH6uBb^gXv;M~~)Iou;O&l^<b1tJOwqHs_8MReAGCkvR8e6{qaYK9^w6U%{POcjIm_8yxA|%y+jnKo)5)-C{)HdFCgiq4NOM#C(cP35aAD`84=LDcIo`3=c{|dh?PZw?TD3G8WFaSDY6MlNZx;<IshH3po`$O^sK1C?9HU0Ye(Iq{EHDaAVqV7y*OACMQ*;rup|0kQ3%14?o7(i7uHqVv^p8xVPpNmHq>>57>EdnnZ*2{E7@<B8;`Be08(lamh*4%4lt==v#>6AN8)Y(cw&*#aMB*G@jd8jlIqVJfn{1`G&Y!FgK00#19(S&fz9*Y}MM;`I;N~7$OQ1>Ng!W^K;M8DW>zvhG--+oLb$Tkui#dqyFoIAJ^ftL~i(|v$py^iCzW9<+I|-=k%sd6-Xqs!XXC@jz6N2>zMXA47L(h%+p-COW&`8csi!gey}kwTUk?2*uN!I`T{sOuFh$<d|a|O9Sk#SShGrJ*5i)4UNkhz+&Z+&ewA3yB#q__R#@A0!I>Itm2VuLT{d=DjR;YXOS3W-Qi>1ND}8pk4F@cyvnqr4Q^AGSI|^qiKv)U!0D-%zWI-zP^flIps2?&`=TK_iiCQX%0dPx0<s#xCVLYxB*}H6s7h&H$0~Aei>Z^8_(r#L&<zsd|Z{Yuau$5tv|56`HoUu5?4c>}yG#BY)%_3VZS&3OEhSllUL$Zk_anc}O$!_UNt`8vQ&rKu-l#R%bu@8v!CyBSN;kgc%>nx&_>zm0;@T}^9lk4Poju}0f=^B;y^{w;~-<X(}!I0D!%Mfra$Gqn38*wK2AxxWc(tw*g`~a=m33fGsQGRcPZ+WhOIF`#rRjIcN2(D6ZSKI?Vx`jE9yT9+lv?p==%j}}QIjcnQSg{ozvso3(>qL<s1PwKrZS4iG26j|Iw#8s<x5;MKn&X|%U37BHFKxtL6h%_rRh*#3t?w{QAIQ@(d=HiPqK#90hzw)ND4j<%Zqh;u5{aP+0CjE`V;nwHlOGkao+44rX@c$Ph$?;`h=ek0y8@rZjDu9C)QJms`!0jvAkPJaN}mgs9hAAg#f(D(GGkHZqtR#}y~AE;YOm7i)MjOd&&=)(=EUb5h_T&s$1w-j<JSid&%);%eBR$Udj-B0;d3577dGv#BPFjFOWw?=I2U(PuZn=ij;HNQ1cj5Db<q8Pu?Hgt_9CQht)#v5GbK}zJhr*WPJ54SUSQvE?u@bx4-i!gs`x~vBWCJf(SXF(w=K;Zn7Y_w@oa5-FWpeqEUy?T7HH<}EN4!gVeJQ-o*RBSsIvUIz*w~Q5!4{H4z1?CQX7%oQ4sLMB36Pp>wxh1+xsnHjAiAglt}e50F^J5wBQY+m>wV_M{yJW(b4$uXuHzNIPQJ=xz0DMfw{5vCeV=lKNL$XnvSMDRZLGX=t5fSl-tRnGVgV-SOThKk|k>coYsQsWiJOZM~x&(rSm#Z=5ww5*ed>6W}mwykYbzW&qX)5qwv6g-qYR<xh0PUh~a31K@ABY?T)iqfzehN-PAXd?^?A2ABPHM%bp4p@A*)?$WC|=<Y9_Gc2($L0n!Pyng1Tx_yk@E7THJYh;zEnZKiZJ#iwgw%cl6O{u&mMh`b_kAc#+^9ogr!xblEt2ftV7d$ADp-|gz^)j(Z)AFFEA3T60awlk~z6{@`OM)`c{=wS9*Y`Pp-K9fa9X~|r=aoa=}!bLE|u^$hNWcY1j#7D5)C)hIuE+u*`wh-o#Qoy$6_8^nZ1Y1L9EtJ880Gitm!QhJ4cw4x4?ivznql>9k&>#qX+vTly=CjWu;_nz!^p*=M9Baq$5(y~>=^<YZCYXL=A|L0B?OB3nw3ur&nymIWApJ;DGtbr_<n6IKw;Q-^i_Q>tFNN&~jIv%Cf$KF~Yjl!!Hynw5%aK(+Cp+h?WcIRB*g<2w?Bz$=1Ve$X5n`8bp`lOp<Sdpyw$XfL$x5k%?5yy1hwm1-<0MSR7=Z56_o7W^L`cg08TZO8K3(^StdI3QJ4EQ!(8#`5Ud+!XJtybO&jnSwoj%p8<imyGVan&Ak-Dy}=><@UTJt`ej9OgHae7TAQBv3UT2^IR=Ag0Md$Yjqmb8g8ZCZGkPM@e#d749!nHkPV>CVsg%HYm{WyY&!+l_CG{1X02uLV17tUmRh=~dIoeLCTQ#IARp?O%oRxF{C{6P!PAaD*hN;%DP65mRO^KKm#+;sMN+G>8b(?Mii1hssrqAz4(*Rl(Xd+`u5&RD_zoXyfkyY0D79==gRH?LB6~;iHAco!Um^Efmw@b?_o*VV&@h-VqsSrmsvwEL01O$&M9#yF8-Go})bNqFfz(3%*Ti@_g8jK?<+$E8sgY)7O)z#Vm-|uw?|XfZE!3cX5%YqrPnD&;N2ENn;=sW<{jACK5h9>|Bi-t`cl(WnsC@X~}1XV>JM^HqLy?_pv8EiBdKEl&9d)ka=%4EA!Ugsv6v|kXE&t6_r-?N~_uKvpFsRsm)=_=RHvb>T<T@@+u7OoWKbeDs8jrm^ha+;W?MHW6<+t0*x{;d>;MEW%g9QOBT?Ej#^#E64=qcY`i_-=mv&CrVN+@k9G+WWh^Trnj!9~-=W?<3oRz34o*kli$Nx8lXY`_HcWYTU5cD$nduDOYi1$$I$I9YRTm?unx4`0vJdH{$EFq0+#+IYFUjNU^Tx!%GQPmK3<hz}&bKCTrMO1iYQ0(Pn9+cb=rM>O#AA`R7(S%!x0}8Yqz}Akq=lCuc+RO5FhWQQV@ZgzOQd{t{l;rzc^Qpjok2v=eN}V8EVQ~6S@PMx>e5W8$yceQZ^DpA+st?A*oU5}K7r@qlw*`J^;ky1XJF0Tj}vT(RB!RomeQ_6(~NU^E?(vWAa=O_G%Xs*sQO5HWCS*Ej%W?b6MsULdcayfu1|9d?uhvu67U7Fs1fM}sT4`2&gr)Q10;Fj_W'),'Libraries/Compiler/to_ast.☾':strd('c$~diUvJ#T5r5aGVED9jSV3~$1RPRXQr)1kWmqy0z%>Ypw~`LNBiSX-KA{L8Te4zXb)x@P(x|m;IQ74{Nl_$n8z&D7<h7rn_X!O23uN{W$tAhGJ1am1-I2H4otd4TncvJ1(KUMa!t8I6<FLCA&Rv+fIOjMBnFL=ajTn>2wCu%ZFz+@aWZB3xEz7dS?D5ITv(qzY#;0eUiRr2F^RSMS``r{$)>t+loVftEml67vF=|-Wl_6Bgd6BrS;kp~UI?j4pY{^)SeLEyX=Vm4u^<DauuG#d69?%=LvlqwDS%}`Gf2PlX$D70Zo86T=Zw~jrH5t`x{9x^U{^0(z_XWcvx<|L|-+&a@vIHx~3t9?4c4Z{C=svR0xf<L)qYr=@o5sk0kRQT++`aweKdX^P8X>#ojOIu?V*roB0T{4p1qMCIw%mq409iJzKvtzy#|uUrIBpap(9S;nJN<!Qzn9mq<@Fo;x=VZ~S_(*9V{7e&fOyzhXg8Z6O6)DwxLWP{{Gt=OB*LUN!hgV$>kbz)CK$_Er%nOYPw5kDY{-DWKD@_j=v^Z_t$vac+zPH?VCP0lII79x9$tt+PwA<FK{DGyO}8~)cMVX^OS&@#m&bG$r3NjAFOOW2)(S(&j7>}V2~&>gOGIygZT_Q3kDKoe`kcN_jF+vOxO5SrQQNZr_z^p^eY(jmujwjy#_u~L<LrPWYg;<N9=%6*6B@`g*c6zg2sj+G5j(=M8^<K|-qTW4xE;-IN8}DBr>4<+;D7I3u>~bY1N=~)irk|x<Mw>i4*TgowRm8F<m9nh#+IuR!O^ehMn|tG0*zX1AQb^zmVPfSomsP_YEMp`xpcOc*_)KQv0#+VPM8_{gT?pgH(Xx0ru0GcbHw$oHvC0HI2{B_L6CpNWZ6)Nfc)uFD;@5`x;OhtEciAS8n~YDPWk7QVGWZO(pYa|4qyvL!#6|-WZ_R(OG?Odz~zaTaqoSo*+REocjlXccQw-NUZRW>LWs~kNAfS*h4jcbhnwGlJEogSj$D}uR*k%x-p9C^?a(i{xI6T3@_Hbz50J(QZvvtm=e-AxAc~3NdN8aD5vh)uOmQt;C7_3`W5(QAK<a7KYKGXSbM>0zy9`Mz3}FfN75-G>mpv(xjAG`;Y$u5Z(}<ra9i(<*@M%zda&T;@;nyKJ7Up*EK6L8X>m4#v*}M$RGbR1B%_uNWbz6~{>Z&Z)^`%C1Rir8*!2mJ<E>1F-o2vl*)&^+eTaNWx8{PFS_OJZdNq_99Pj-?ghbu7f3BTPvesj2YlL=Td$21Z@%^A`G{mc@F_#6%^(YKvxzEbE_A<4(7OmMgJ_N;HwZ9(s2(Air_!1ld+oT{K=-vu{>)6529<*YL{GH)ySsm6Yp(3au)b%<_{=w14+WD1)wnmo!ms#ppz9y;CIE7JAe_Ow2s{}hqu$KFaSMK{K$SM>ASt$DCi&5U2Gk*`uk1q}sZs-Ky&4kXJc3o^qzG2WxEEfMYi_ucVb_-w%EPw=_d{pvyYtB2k7&F=bk_r<O5Uyizu??`=}4}4tMAxj0FOvXHJWf@VbDhcneH1N*GkBR`##}DXAZv1ow@MnD4S$z&`)bRK~ULUDw;sxO{fQ0bHhv^I<449>-LZF1}RH<T8KaGO&@@h#$JfLe*#HU&EC}rnXi`4{@bNhELi-f@+Ov`xJkm;nlF>DQofKHD2ixRxT=HE^M+KmfP7n@}29d^SI`*l>|dN1h<OX|u_4y8nsL6|WBtA-C5UyMfVN@madGaIV>!89YRJ5!0~<h2r|(FM|F(-PcYfe|n}u==tD2N{^9)OVR75b4j5;J8hEL(tP?o4Qm@a416rs&LPOFZMbtWDc9T_?z4&JK+gXCX)&Vof3#BlL|<Zr>Y>)Bko@!hw8DLBsF`U4QJ?4Oam-6!D+g2zpS0h61PGTrBk&t6tE#N3+mVj!a~N>VZ9X+v_mI$$s&%U3gil)wg`OIfvH9>$hS047fA?df6t^Ja!1``w&xi8@Ys!6)m>Q^lq{{Ivol`kIk*!lQl|Q?s)=-<I$@SmiyWkiiQUbWiSaph7;-Yo;V&nrHUij#)1nlY=9sj&ax*h)%Vr7uGXi3W?XbJT1KG&X%c2Ud6DbYsy(K$;X?ptPlBqVUJ-{+tbGbgFuLf?Q^zoo~l6au>P(<geP!AOgj}HeZL0Ki!G0SVYK|vi=Z+qCGpVF@jF39R;5AxL@bi5@OkfMht#hCamS=P=FZjPI{%9j!%ZnW5w2?(S0#1mzx6BQ}yNG?Sc4z;mXm9T46Ez@&PtvI~PQM2J;G|E$0UUop8SnFGQ3>pG*Qj58EmB>mRA&RdIU5Y{~K#Zb4wB2aQbK|j^4oMa0Vvturv;@usPOa0eTne1Z*s+(#^5Dy_+dwJBk%7_q1w-c~7TO)A3!pFky|}MdyZQgv*Pax6M_&J$Tu;2eja$7oH!wz(x>f*MvEv1PU+{;FTPe;re@vPJD|Y~0;TuZJf+cn`6BOc~>WHpzrnz#kVp69js10O;biKN_4@^xI6=I~8P)bD#4V{W~-~?f)e=Fe^bP2Xr`?gl9<kX94>6MIfYG!dS?Wu`?!prug<zmUCSWL>tGNlD4Isf<m7fOPgHVF&o$7h|O_w`hI*_X@)_K!?URg%(mT#g*iZ8isToXdS2J*l^$be_F*=EB99iE))L1apy)e_3d*K4vR7>61b&k!46(Gb@MS{N<P9HHg=4Xwlbe6S53}rx)_J7jdT_^d@cb`?uk9ho}CL3&olnYtn!2h$U^>>;>Bv-Oy<@+cZP0s-Aj^;Yr<9GUQdgziDc&QumJa9d*`N4WRiW!5t5Wv3Q&Ex#33ajm)D#Uh+&40{JRL<7-f?vzI+_V2sbsy`#QxA#NkWoMQI=Cn=UCrJ<qpwYf9(A$#3D>o`b#!!2H_nzpzC^`8N&$vD;'),'Libraries/Compiler/ast_to_py.☾':strd('c%0Q6S#K0a`rW^x(~_fV(>V5!EXs&sml*G%IKcuIt>krD<C!*$Jf7)Hw_|$~B6As=gn*6h5MlzvA>5FV3kU?sCGG3}hWK$GvXSx!_WSDU>SLzIurE83XR5oazpK8x%A<|?xG_<yl<H--TnvgvW!$Sb0;A$PwR&T`SgriSEq9FKtTA_bvfe1m8Do>xiXU_kdYqmb-1leVI5_&t8-siH?sptQ%!WJJs041qH!b^MwLVg;`oyw{X<C+L^Vz$0@BY)kp4WB_>~s1C`ggqv?=f(%_Y>_M%VszC48m}TkgZ0qVOhg~`3n7zp3N8NQMy1^h=n&!(_4=3xh1^$89mXrYd?X}r}QQew6S__V`hGTW5V4ya%p4rW4QPuAYfN3SK#W+dd)Qvod9Ureo%JCCd;YNW^ckP4L6u*)DXhmqi{K0ajRvx`t7UPZ{f1+R`Jp7BN&(JwV+btxKCb%8zT+3I2J`WQXO+j)mk%@>rdge$|yp3a2|$km0he~VPnq7+zecd)*DE~*E2Y)R4w{`5>FJz8+&#OJT^%2JUvnX4guWEJiH00f0;Q2<DfAe1yuJm7=)gsb94!2zyE$`=UZ>R_~Lu-?cBLz$CfSY_qJ}`y79q@F8aeupbbO0VawQJgra<S27tfx5+eNY7!13*a5#@r+F4-3FJQQX50TpfA6|yx3v4)d9fpkSjk#+uEY`}=+v~SsRI3N<?i|XIt=il?zisf#`4jlWXTy_hXuw0Jv5INS>LC4Z_T@oBbcP;*`^P{(PtaL<64;-or|1Wum#67R^b81OfiBW>bcrt06%gwu^aAj_N-u)UF44;%>d)yK{eoVlU(##zI=w+}(p&U4y+iNPd-N;%HN8*2q2JQ)==byieMleCAL(QIgg!NqioJci^M$^@?%hjBwKzUfE}}^9(sMTZS<J)F3jK~mZUQHyI8xg6T3>H&8!Q4b9h394Z?Hcb+BZpPAPWYE{v-gowNk!-3KfNe03Oi01Vnb8-cLL{4np~!-X>yjM<4>huYpJ(AsWl>E8q`kq<pB*0^YLw?0D~xkO0A83R+9f`b^FW@goI;{Rdi6z>MrTD8mxHCd~|l#T?g3`cT4zWwqEB2YR4?aI-*DX0vHWK)IgCNwD6QVio~>P8U#ywtRCc52pFxZm0iy)9NHswqP?xErMZRoLX<%as86x2My+!L9q!Z)D{$^tN{TZ@b`(Ho>%%NI(@_?cw+0J{88`kxX%#Y=4Bh~?xD6ON@Fabv@%M>C0MrcZWm&h>e&T<uX0TIo!id7bNIdeHTJz57W1%Wp*L0F1ZP0UIeHw-UW%u{xLLEO3*=>^3oO8Zmo;sB3hGm>)LfrT@el^aMM%!J>~{~_z}Pez(Gz+Mjfhdl?WgRH8t#+_9?U8Ff#XdhgUjGX9^0T_1^Bb_9R_?VqXtpWtZvup-p?Q4hX*D@K4$mR-U^ID0Z9M#;>UCFhu%Jffm6p}8BsYt!4(&84fPD$Y7D+ydj&rv;QGovrd+?FVGBd_S@4aYl5smlMG5I;>m~)?9jLY2n18e}|Krc!t^RxUvbI7X&1P@>ymUP>u_t9BvVCC{rOwwI`Fuj}Tj3|lR}mJU1i(F4FYX}NH43p;;Ti&#&(iBa1;KFHB`knVwbe75Eq8cr!8L=d16G=Nfj%Z_G{Nf&^visqiFZSty~S1chQ_^ywtytcM}jv&fiwV4gMeZF_VwBg>GB8>?0!VQB~qNWz}i(53>6bxfF%b^bK=~HWK!v;E${S(L#A7^bU|vCQpH|Su>ihpW@za_3`tw2Ke69);`fsL6=GNf3E7(U+rAq>COfW@)0`j%hP~miM`WtI`v=H2NL9BDCzxY&q84S)p;iZYH91(xqTR)pocTC0l<KR*pvkp`<%0>R9PHPN3z+cybJ2ki;CRJGaU7FI&9t>wK^~-3NT|7R+slx~s3;>u`T;k;G{>`W65ckz-5E;n<RoEMN`1hHn9_w%N?G>A$j3xE$vZ<n`|HKCKP0?f8lACe_<=mzC;_N&di1#f2Pq`5UeaJKJz%nxH9_JfoQy&a3OIZDC>Rx&cT43p%asx&t9DmOG9FO^O%kc=Fss%96XL{LB;0&+V<l$Ew8G0!QM$CSyPd5M+Ey_L8qaQ9?I<XZ@DXR+o)W2~pt&YV@f|ZaXDyqeqqQ<i4Sm`!2}937!f;zsSji$m&mq#uQB(YCrR0)c8|!kbMdWOQvfqAq_;I#yT3Z+W36vSlOTC(bbmMfUG}^%VdjDo{0;A{u2T1n}ZU!l=`$w&jCX%95J+QiC!494d%g7P+M;PUJc;GH8@<7rBRS2p|at7u(8u4pPp;(m3md-)$uwwGDT1#kOwurJZ`>B{S@jkZ_iu7l*c-Pv&dqLp2Dt^~cK`fa>-q33f&EoTgn4)Bw;#}M+uFw^FKVQ({M^gYI=A_j~LZhG_WmA9v!(u4~?@3zSbx%!V)Udz>@r*SbEhHGTHyJ>MYI9ha^~*{kY<y~2IiHr3#eohUo0}F-0Ifv4_Av2G=2$z7ZHiPAl#B7fi??Nwsxm1+eYpoBFC))@#3y85@NTZ(TfhCjnNp*)l{iM46P`tewB-#~-eBd55<4?wktv0;9||W}-K?xzrcZ`3gdC+a^rRj;3=w*wF()TtPI?69isrjUG9gOv2~^l|c2mM`+p#W2MoXpV?oU&Czn0obA}rwx%R}rW7|Ls^idn*R{D~1WR*NcKW=qM6d{v%dSAHdywfi+*b)KP@m<@^~k6Ah1y&SoV3T=mKjyKv$w0L_*2)$YBNixW_D5;7_jivRqnBMc&5~pej>Yd|&t`oc#$+1pQr;tyi=YV2WhAnCAWK|Z-^J}qsTkAfBJjPPfT+ZU$>G8EQR5K{Nm^9nzIv|_zIz7Xyf;2|jO*whnZL0kSUoPI@yRB0ot(tZFveT0_wkwoDYg+vZ^qi-kSgQS@yo|QlWOYMMkVc%HPH_8a6{{255^tBT2l2ouawz>)L>u+2JZ)|)Q&NeN?$uP2GNxK>s1dJl+vM~Al+jqPWexYGJf~U-c+*8<d=B+QT9V!?&E1EMaTqPrV}$SJ+KNEFEy_1U#g?h+_zm_SNVUVT!`-Vo+`PYS%RQ#H760vbijC*9Roz8)`Z5l5Hm815W_fWYyWWo#vvCic(U-b7<Gu}&ADaZtSYB)k(~!1f94)TEN|?zs&o}gpqtKE*o=u<n9NUB$OB9Vte`s3uiLDRORoBf?El)fyg)if7iRfT!)j$MNZxWL1WedI3Cg)-==h9vl?!b!0(tLIw!Vks+XJc+Aqgsv{Y)q1qhbmQ<gc9SOdniF(G#F!x3CD$fO0jXzr)v3crACDNl8<wGMV^=LR!LvOxvd3Gv8oajn}u1D=!cpb!fg?RvMDO48nz-j(OSHv`nb1w@y0q6awkM1DqDc5!h2TP!8Egpc%DTnf!nCH-JFbeXLL?2Nmgp>hOrQN91%qu4NP2>w#gJrm|jpZ=h32-nQzWxHkrH?viT-w9BG!PKnMNYof{4Wl`vWN%+jk7i9zKeaw-AgOWb)~xxz$Z$f5^Fr0G0>5rwPHYsorBY$Z3T#>BqyO<uCFvLLz{X>7$EA<_gt?~^bB)P82XoRa4kBK0U2N0aI}Rs!c`F4RtL`^(I!^(((zJ{?_2UG7|2t?r`dxwSHh=u5OEm1y1U1X*P4NW}wva)U~h?y}zm!&10;6EDt7dSxC~<vFOzAyx`zK%R#Zbv-CyU*x7vnxwCJp`V~vBeLm+lRH&%y+C9LeVR6+C+=e{jy_FEWL^O2-D1pV7)4)!iJk!H;|mc3@t-3%Q`3Xz-|)gu%RZE@*-5<;BI)$=9y=H)l48lTo!C6isAj|&Nj%XQ9$yq!FltiOBpY`_I)>p**3>Dc#h9<ue76yRjzt=N8A$}N;Ehf--xL<5;tM>XD+?|+wFpt;&P*Bo%nATIJrR$l3Z&C?No&PLlCvyHz!D}93s<4eh((VoP2m|OW+eiLvBeOnpUAWall{JO+s!_4swo)>2csJWP1}9am5(+&($d$nu7Q<$Oi4~Dd9q(9dVpcbQs-=x9PBdVpH<dk7XU*MKPATIpK7}C+1^sxgVCL9SyhDxK$=M}T~@I(X#5xrTis|c7j%f7Sp$1@8t%bLy+#IXFFd2hpnnhdV6Y11xu#A7`2s&6H(+UGqAq%{jHrVi29?CAwxNL`oG>f|<zWivfs3?;hZEeU%@uO(A_L+s$F~K%xXmzv3gK%x^%@IN5(Q&-yy!`G_r0O`4UgR|fq2eyvE9kaduZfDWiFB_X<}t~xYc$LT$fVSE!G@2Jd>!p4fU}CI|jGk`_~cBg2Q=j#ZdR@G01mrwN!7^4L9W=9}^xC6fV(gn$5I;hw_D}Q6H0e6Wgm&mcaQbmdlP;_fz<(6ngTZ_X&A%^&G&{a{yAYlijfRdC9PfVqrz=Uzz+3GhaDu^TTGmm&H0}w{>cpc?q5zDB-AB1!`82GI-WpfH_GnGk+2kF;!^!(7Rm4WBHL|KYVqQM~X!U>0M%?;)L4Z*`Q4Njs1u1rn(XJ5U$(^!3E;Gr1~?KHnA7=9-OW7W{G35crU0&j>NJpwtF^ONzicJ0(Y>rI@nCDIPN;{6dS&{*>F9$5L1M`DnJl|aM$WFAx+NScB%F;cwv_RMUkYO)PxAp5ROg9qyJ+^tYK$sR&Cj%m1@<IkDNpGs_Q!=MZZ##K)q?m#?$g4_P7anCDc}vq;5-xEaltg0b|@x6yi3L?i<L~rt^O%0;KFRXiOW47f{iy?ui-$Nca^W11Oop@U)g~%Ur-@ot~j<Atd1Q8Y_wW>SZ^N!IAGoVf>k_O^hQXyIknq{)+7vVy<BHpqVG;tG%z77C3_w^Z~0oAFBp8OPX~|59uu7I!Da@MgwZH3UVDBs@H^ADz$?z7@Pv6Q@-EPq5d(->Hi!4E7d;7A^Lw$DHAYlHN^W6m`xU)VSJ!}(6r$Tfc_WfJo~W'),'Libraries/errors.☾':strd('c$~#pTaVmC7JlzvQCNypl~fvgIwORaW|d@SvxrL~2&<JkEz9Gnp0Vh*8{4Dwi109hth9k}$px{%Zgz+wkhm?&eU-2eweS3g`6YW!U3}?wGW~#r=hAl7sdGQyIqrBeO|ya&Ss00pFnWn+qC@5D^6I%4{z!uW@1A=0+}Y>P2LYu{A!bD|O0!8=IE-(N(~WSPQ^u*|Fvhq#clI1*Y(VL8;t|G%58-w?olN7g$Q}*zA}G>ey8CM~1%|-)SKv4mTU%q%dvq%cC!l6J&X;Ejd!0=&BBMCj3~~__ahjl{Tk^WR$K}3!U+(d+4?=*6-yv|tBSO_PNz#JE2`TAWR~Q<+GEwYg2~p4LUugktoajzLM=IZzx5s{8kvzRlT{dusu#U@7W7#vy|7=pP*ySd5Z)i+kTYrXn43AevXhqBx{{y&7DE{$?QZ0f!Nwg1;KS?uU*ZckYMwo08Eu1`AZlGw!1TdwQ?-??$`2npaPuL@FO~~!K5Vt1ec0`^iH#{XoOQ{=kKHJf@JS-qkC?tXiR^h0K!9fsSbW!H_8`%++X~7tYbCm_prHL>a!T}vs@<^X7L>lyo(xix!9Wk$0Rw;(j2@g*#yQvSVJl;t*MHXaY3pFix#^qn+U30SZdts^pZsle94|(PE$@8>I8a|E_kwf0lqMl1t9<4CUw<gc*H%j6vQ;=KDN0qhtbWDqZA{=t{2_Zxw$QG2|mp9~%MXjUl7L}3q=Dg0W$|)U?hm}B%5ex>bLEaoAniXS;81t9-&2z;dAIFi<78-BCIS?^qi&g^HGN^8KTVJ-YSBw4|@{YVr=^)w$o4IlgxCov~h_s&K=tkwQc84jS<)VlSF)4HDgb@X|z3Nued&>LsCsryluW`Z~np|3pfTx*NQCNj2tR4~tNc<n=m#_u>;lj*4i9KQ=ES-9>=>vnK)CLBNUioYc5#hk8+Nwp1D{L5oCrd${4i&R0poJ+^&~6+~Ha0_){+|4bXZ|3=fVez^{Nh!S*6UT1npzzo;SiDOp8P`o41xWZ{1~LN4vo@rY9S%7M9uh7png}r;XiwJje<|!HMrIX8MovWsyOo*V^q`e(=R?xOGPisFXaucKCb%>)M;#~w1TjxvmR&sl~=jE0-pR?srosR-IuR{>kPdCbhs3rO~UC^WX9MUjw#&p`wQ;SLxl++F1{r{^84ldLghR1O?j^l%h42|%bea4K$i*8SM7tD@Z&rcOw&9@_|FYfZa!HTSlt9>_gNDVjmk?Rt)^ZAZuddd%~}+FO50}_uq7;tY<^oSKZ9iaWe;<{E6Q8jqLd_bzA6-xC2h!Rb}AG1Ab<Wnmm~h5X1Q8XIic)e+^l%RA?8_Symkp@=V30fZb41DagvLype}C~n9U9qs_XK7?WMbTgYv(i)kdocu>E)Wy}Vj8VBm5@ep?)<F)X<XhXx86@ZXTtpgODPYojWye%9AEFBV-+mnkOdgkk95<m;~Dk7GP{__@*QsCiBy{%BIPbahz0INu>3+zAmUfqGAVChuGD%}TUXX6r5jzvMVsQ8ig#tOMwrH4ZS}bNqHTPVV?<z^lrs$<D-B%Np(lxPFj!b6k0IVP$A~@?qM|voU&IJWQ|s<-BI}Xw$B@gm&%BmhoM)J*q;wDL<iV&Qikz{@cfdDcj#dYXzKvo~VFI<Pm_?%h0HxHpC3xwCIJIck059>#m+2(BJ#;J8+LbK0Nk2hKrA#I-x$+^x`G=(x7)@_&A$f8h|(t{-8`9+fH<&0vUAHIvInf|11APRY$~5@nP8$KWFIw8}e=1)RT2#E{Y2ZeUjs`IpnAigB*cuWQOViFk``xnZk<}t1e%v<XVFAH~Evc%Rpag8LD!J(T45j0Ee}Y<k$U&s@%YK?Nz*Jq|hDYgNiu@Kt&+mPA>)`%hC*!`wrKd;!0n=fO0X5iy%rjMc=d0*&YWYZT1ofwxJQsb3KQZbHHEachECYAnOJ}`DIEFSOSYqEhbW98tabYu}H!RbWFR_d{RY{R?mR(^+y3|Gf#qRiVQtQOT}Pgh7T}~Y$)w3Q!G-o1;Y+EHs?U)z<d!h&;MdLercZhNWFWHc*2juOmv2oug0oV+InVfqd<1p6aXLJ$ZJ+NfM$Rfmn}5?Y^i>aFMjyiU5-uk4C}(c185NhlQd0K0tEqP0I8{q7bx(FybY8`a&jbh*pb>~HsY9StTu2b{7>uW7_Z?SUiKB9l&g(V<d(eFGMeg9w#KQZ2|}2Aa$cP?1GERT4ow*v<thx*qA1PG#6g{2&+~dchYedgeh_TOTiav!E8u)!OQxJvSZQXbrd_?tl&Ze*n!yBUObsOYUYGT$Fc<5yNKA3+#3)yL55q~UPOK>?Otb(wVKI-;CZin0zQT;fuSDQT!v^EZ5>)^}cXKSSxG;#6?Igh{Orl*4OF6y^-PHr?l|Fo2lOHGtz~?e(Rb;zlQ7xRL&8xoh3eo&Ym@Ad50}sZ>N|uRIM}HG~a&0YG|1*9Y`a%%U`uCm{FNat6;76<<>uCJ$M3qe#C#qs>OSEq!mm&1~5PF@XxOZ^%V=|+=%qJc>`1G4<!(J<kO9!9slY`f<EpGhpJNd)Gd;8VK4640)D&xKoCYwS2LZvCp`c{6en$G_L^;Oyh'),'Libraries/Compiler/main.☾':strd('c$}>o?QY!0@xPveW?^90pk+x$8sK22kYqU)5?g{K8vztyK^^z*i15e*N!h0w{^2xE+cZT|Cr+I-P7nk^8#GO8v`B+APJZxB`~(5=0-f1ilDi~NKFKG<IdVT{W@l#SlO%s5e`|C5GGPp#)~{@CZ0#^ch~4$N18!5NAIAG$m=fv`+oqH{V#mfNp>&s!v(}<T>E0aa#y)4gAmj`;22sD`?j#4C&XJufn;m!fnosh7;q%4yEhm3H|0KV=y1YZGCnk3@Cx178kpG)H>A(YY0ARp9pC_yv4?Avt2PS{ae}LZ)^WPE@dc%F+vjEK3`FoD|xz_;*Z|C0=M5rc+eL9_g^56%Xo|Z%R8~{C^@H7r@aCpSE!#IwZA0)7P<sb;NAWCg{-iP@&`6omYHeuzt{c4LOd*o$<FxY3oa1<w5$0c?ziHDXNw&bw239puyTBp-j4;B^{mc^PlEv9*NBS_*%Ur`{pT%4Wn^Nirc($bZUjjL>Bd3%ikkL3_;Y&o5l)Ke?yS>+TDQ;xHR9O(SWOL&wimMJL_`=^KRehF%^xptj8`Z&<iHauy$K91bVVm3MiCKUqxEdL<?r*j5=|CIm1IU^tLcZ&JOgqLPaz#zqx1mPBt)IuQ}pR0q59n9zZ2YsRzri1t<1872h<y(AEdt*_|fH&TdyO-c@sEJX+ai2C4MCz@?-kG!D5BRR;<vacXbN-rtN>(;rAz6@x9C);T)z+D&6NuMM90j+E{}IsB`}w{6`;H5z0z!)Q{(hf{J^jQRvMk};)yUNtV~_?@6>Vgql^F4UKji1nN!W25rc;}Y^5CE4f6O1jl@`C{F<|fV_Ks~H@iUnFjW{3(TAq)R^17>?biO-EXze_P)Q;r(#x=lNaakcXnXN%R7OZIqcS<tZ4KGQh88y)-JUd7tOHwu`)EQaq$7pPT@1>Rr!Bv`0=LcTOLhsjyEQ~$BB3%JAwW(d=86Rh?7bin6JC>*?LtKrABQQD1IjOg^hFV&NlL4-A&?&}=ZSc~j)s&E!lk&{VvP1%UX^kwY1@O37Juawy7uQ}U=YfjzdzCyZw8dQ(KM(Qeo&0Y~%u0(i1)#c;m?~$Q266WRAeB!Db8hZgPA;t7GaS8!ll4Rt(sAW4>5W|QzN^ctm)9_ifFMN**=MIy^iwMv8#~)OTg#j5^78iO-82lkoLr3~?kxV2?t!0igl~(Z@K9c>`Wfr4!Q{Jp>$YM&JZYDV3_4&^y>=mimyIma1=ptELzsLwe?)2H3U+q~dyR`;ilkeydY}n}wDXMyy=GiS(a|@~O(zhKq6{)VJb@OMM7QgZ<bbX`z|)g!4$4hwLut0l^E`Hi669~@U$_-DP8j#4f7T7ASZ@WXB^0E^2a<+IE+STS$-ua%8HiU)igy?GU_yd7#uxXr(=1XPXmNQ>q;QzZ$7ys&ac1Fh4cZkHV*lcFY7zMN<kN2;+Eei%!w8Tuw+#L|t`;YrgLOqTDA&u|rf|}E^i@v&dHz=ZU14anS9G3JgoJHRRh(U*N_gmH!3_=)gw1#IkMj?ylW=sK5|vYP(;(x9hc2Ci4=lj{p1gU_l4rWIaZ$SCFZ0I;@j-sa_2VoFhO{pC$0h#r&r#>7jcV?Fn0up`D-1HRUmY(j+vt#fdidx6;e9wEIOOvra7P3Wq_{OG`LyFAbTh5$z|Xh&*BGw+C%;>yRH(75*R}{*bf|O720q&zyfU{P{TiZxAA?k65aSf&l~H(~M?CQ|&i3OtOS8lq5uZa4EptU!k18;azPqrML>aRvjykTEt=tT<0ZR{hy<iMnkjb7pc6oI-UuKs!wq7Czg%vzOrLYPGxrDV`VYqlxU0^ag>}nZ}<R#p|Q|I=B=-lWq8^n>kPp02;i%d_d<b*4NGQbqM(0(~WQ3a~~^<RW%=B3&VtnzHf&<X0O5W_zhj)WTlhbwnibHW@sTGWkV)NUS{$gfB#37oAgzjm;at*F^==U<}~1Sq%7_%8vsm-ZZBG_8zXoI)Ty7{<QX=q$v~KmS})|6z}ev>=x4a)`L)iI_TiLd@{W2r#!%;kqIB5^Aj3*<>O(F((V7vn~*T3$~0Hnw~h|e)8sbM+dPjs8w0#X-M0uKPN#~<cCRr%=&TI^Rgt4o{oOPwpo!gH32i^fSw^wd;E!6^+^aR6C#8<?|Yf|bVAzp%#e`6_{Sssjgu)@bL8gPkyZdb20_)9*^v=p^qw7#_;EO+Z<-w`SU5Tc5pwx#(X(tkg}rRqGCMN(cyt_{kjrO>Ud9r~QHFBI?1)JC%>;77W8GG5&kS`!)r+Rrh_(XLGm)Sbm!_s-QbFn@gzzMp%4`<vW_I!tC5E_9J@YXTORx|OU)|nZe|e2<tz9CdOXq793q9_VwR9Db>M@>*@R~^m3n7Oj^(I1*VJNT@0z=4!Te23B4FfRD5rUq2k+l|Lm&;TpV+4lzUC6Gm`u#ly$o7j0wr`cYPKkW3x6l(AO;w`mh5>=#F!8!Y*CFs^qaq1it$d++Nw|>jd)?Q{qCwzUUgTRzsMQM8;sla`Fo<{+R$pG<-eH$OBt|i!?CF72AN+tMu|bf68^nV;!`FJWip<+GnG$N5O_KsOX8WFBfD^fh-V7M^#z2Y5yeA(&v=p;2QUNx=*_5J2smLMjLlXOlh(6-yYD&~wA%7u3G&;y?brVs>DK$Jw^%@pqQV!^FnO@2gfXErpid`U6Xhh(t%G>MtN1$A?OL*e)TE$e9BbIz5sg_2)af4rseJl?3<JdoCYcdgSKXVU2OhR)=Fr$)-u;qqeDmhYPV;!*KsO7pABpD%^krqst!KH^OGNxE%ENUUTfZwLltqg&rc)Yl>ySS_#UJ|)+Z`^FSF*s=-Qs({u92jJNPK}x)DAF)K6>Jk|lQ9#kfqF%w1yYj+9RQZiuCHy<DM+fSpwi&nBDS=(3_OfYWd%r7PSR%O1eT1Zs+{P5S#mgmu|*+Eovpmu@<37QM50tEEuyIX@*7_0z&1G)L_x-)RBzY{H_4<oaFN_LQIETPl*zW`N1c(ErYE3z3S!q@SzBdSmv`2$uN{--qe;eZ3G#RH&!48PqU2Yp3G8r4=|bqdtVl2kI*21tj;(B}{?~31j54iqV~utQa-v#zbAYC%R+!f;w_GV4B!G)j;je|8L=S&2|F-b(f^mM_O{@A`r?d>$Qm@ZD)|21eZL)^|FmS$b$z(}Q4POvNM69g6P_9f4A`4uiCH$7L`s|<y7b&tbFsZerUF(8yFA((rK!i?Ei(6<oyV|mJ%)4z%SF8&VUC2-fi)1gD)7-iMa|nn>2(mWqm(xCPnT{1Z0-!-Y#Ru81(#(gS7pm~5G9|l8I(uk)--nQb7CjUgY?_hYR5nEFiUJ~hf_Ql^f3M@pL4*eXq%S%v2-Cu#9yU_&0(_CbU)3#pM$z(q{y?u-*6ZeQGWn!Bk&BM#%j}7GK-F+f0*VL$CPYuJynYLgItiU0#Uok+C_)L7FO3?hI=poXkS$qf$|KWGH;y2*Kd3@I1Zvz)xD;EqXk_-NQPXX0JZp24LTJ6gCCceU?-C++L`Z`i{s54B*wN@wt6~rer3Jq;@%y00=RWln#y31d55FNj{0K#T(53a-q&i4_b7TV%)eyt}QcYCoPpTA0W(6ohIi<l67ENffu7XD#Q;ii_fTE3u&qST%dD*u^N(+upMXaH!nEeP<ZCLcu_30sqypClj6+GN646kK#2jYrq2@Z>HC5*PiP<;c{u@oD`*EC`W#_V1Y;md95XA6}XJBJ<3=Ms2#4yn#sO)KW@_QM-b!h;IBV23601JNZx1Ktj{Yk;kp6Vdm(lmETy2*Si)@_*2>B_}+XVK=6yr=6gm|NH3o&qR}0Am}O=s4!ucWUfAoI5eTRLm!yXwW0%t5bb;VJUa_&TBi#mjPm<Swb95NjxwqyhKr5dsWm*RA#df4#3^H_X)*yVdo*eC8#J|{6@s{v|5(}?iBkz>GU_@uegw8A4)MK##4#D<N*l<woXIpc&V&-vWJLQjLo^vj+{B?;_;&zY$(Y>*XVF>OtDNV!Q&C`kQ&SF)b!#omsJu(cr-%;&mhi)X+j7-c&KO*V`WirZ8+<R_xiDLl9$l9x{9##?jKClSzKCy0N;~QkjvjvJ)wrY;WR)byTIKS^i)`%`)zc+<jj{?DY)AisNuQCSgg!4vX!U8DY@yrrjyf8Mx*+W~;lfHYm9ZW3y`)IYX%T^0Le)#B7$p=wQ3jutQ&b95PoIkFW<Bnl)8y1<y5{~5AS;O`')})
#main.☾ (6313 ⟶ 10987)
__dir__=(__file__:=áÌî(moon_dir/'Libraries/Compiler/main.☾')).parent
(ÄÊPSH(__ÄÊIMPORT__(("cache"),globals(),(""))),ÄÊPOP())[((- 1 ))]
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
        (ÄÊPSH(__ÄÊIMPORT__(("peggle3/gram_tools"),globals(),(""))),ÄÊPOP())[((- 1 ))]
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
    
    (ÄÊPSH(__ÄÊIMPORT__(("text_format"),globals(),(""))),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/to_ast"),globals(),(""))),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/ast_to_py"),globals(),(""))),ÄÊPOP())[((- 1 ))]
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
    Âçß(("Importing text_format"))
    (ÄÊPSH(__ÄÊIMPORT__(("text_format"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("Importing cache"))
    (ÄÊPSH(__ÄÊIMPORT__(("cache"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("Importing peggle3/rgx_golfatron"))
    (ÄÊPSH(__ÄÊIMPORT__(("peggle3/rgx_golfatron"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("Importing peggle3"))
    (ÄÊPSH(__ÄÊIMPORT__(("peggle3"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("Importing peggle3/gram_tools"))
    (ÄÊPSH(__ÄÊIMPORT__(("peggle3/gram_tools"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("Importing Compiler/gram.data"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/gram.data"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("Importing Compiler/generate_operators"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/generate_operators"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("Importing Compiler/operator"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/operator"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("Importing Compiler/node_types"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/node_types"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("Importing Compiler/tree"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/tree"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("Importing Compiler/tree_txt"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/tree_txt"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("Importing Compiler/expr"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/expr"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("Importing Compiler/lambdas"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/lambdas"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("Importing Compiler/rewriters"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/rewriters"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("Importing Compiler/to_ast"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/to_ast"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("Importing Compiler/ast_to_py"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/ast_to_py"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("Importing errors"))
    (ÄÊPSH(__ÄÊIMPORT__(("errors"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("Importing Compiler"))
    (c:=(ÄÊPSH(__ÄÊIMPORT__(("Compiler"),globals(),("↺"))),ÄÊPOP())[((- 1 ))])
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
            Âçß(("God is good!"))
        else :
            if rl:
                (readline).write_history_file(HIST_FILE)
            
            if (áÖï == ("clr")):
                (os).system(("clr"))
            else :
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
        Æå(input)
    

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
    if (((ÄÊDEL(1),False)[1])if(ÄÊPSH(f))else(((ÄÊPOP())if(áÒø)else((ÄÊDEL(1),True)[1])))):
        ÂåÔ(ÐÌü(ÄÊdo_imps),ÐÌü(moon_cli))
    elif (((ÄÊDEL(1),False)[1])if(ÄÊPSH(f))else(((ÄÊPOP())if((not ãÊú(áÒø) ))else((ÄÊDEL(1),True)[1])))):
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
            while(True):
                Âçß(ÂÞÅCAT(ÂÞÅCAT(ÐÌü(input),VEP),__highlighter__))
            
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

