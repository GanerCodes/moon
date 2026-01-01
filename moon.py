#!/bin/python
BOOTSTRAP_HASH='KrgTATe-e3SAM7IcdYXdfSFjZa4UoD4i6SvJCC2upNY'
from pathlib import Path as áÌî
moon_dir = áÌî(__file__).parent
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
(ÂøÚ:=(lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:Áÿú(product(*(((([áØÆ] * áØÁ))if(((áØÇ is ÂÞÅ) and (áØÁ is not ÂÞÅ)))else(((((áØÆ)if((áØÇ is ÂÞÅ))else([áØÆ,áØÇ]))) * (((1)if((áØÁ is ÂÞÅ))else(áØÁ)))))))),áÍá)))
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
(Âõ:=(lambda áØÁ:(lambda x:ÁØò((lambda ÂîÓ:(ÄóÌÁ((ÂÞÅCAT(Ïò,(áØÁ ** ((- 1 )))) * (ÂîÓ + (ÃÆ * (áØÁ < 0))))) + ÂÞÅCAT(Ãù,ÄóÌÀ((ÂÞÅCAT(Ïò,(áØÁ ** ((- 1 )))) * (ÂîÓ + (ÃÆ * (áØÁ < 0)))))))))(ÂÿÇ(ÂüÌ(áØÁ))))))
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
    
    (ÄÊPSH((y((áÝÌ:=x[0])),([áÝÌ] * ((áÝÌ is not ÄÔýò))),[])),((áÍç:=ÄÊPKE(0)[0]),(R:=ÄÊPKE(0)[1]),(áÍÌ:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
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


__dir__=(__file__:=áÌî(moon_dir/'Builtins/crypto.☾')).parent
def SR_int(x=None,y=None):
    if (x is None):
        ÂùÆ((y is None))
        return PL_URANDOM(1)[0]
    
    if (y is None):
        (ÄÊPSH((0,x)),((x:=ÄÊPKE(0)[0]),(y:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    
    if (x > y):
        (ÄÊPSH((y,x)),((x:=ÄÊPKE(0)[0]),(y:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    
    (r:=(y - x))
    (l:=ÐÌü((r).bit_length))
    while(((s:=(((áÍÞ).from_bytes(PL_URANDOM(Âüï(ð(l,8)))) & (((2 ** (l))) - 1)))) > r)):
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

def sha(*áÑË,**áÑÕ):
    return (áÍÇ(urlsafe_b64encode((_sha256(áÍÇ((ÁÜÙ(áÑË) + ÁÜÙ(áÑÕ))))).digest()))).rstrip(("="))

(ÄÊPSH((MOD((lambda ÂîÓ:ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ,áÍÇ),zibe),b85e),áÍÇ))),MOD((lambda ÂîÓ:ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ,áÍÇ),b85d),zibd),áÍÇ))))),((stre:=ÄÊPKE(0)[0]),(strd:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]

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


__dir__=(__file__:=áÌî(moon_dir/'Builtins/𝔍.☾')).parent
(áÐÞ:=ÂÞÅCAT({ÁÁ:ÄÊCUR((1,),{"ensure_ascii":False,"indent":None,"separators":(",:")},jdumps__,ÂýÃ),ÿ:jloads__},ÂÑÖ()))

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

TP_CACHE.update({'Libraries/text_format.☾':strd('c$~#LX>S`xmf!U&8VwkzQYs#jvNo|2X4Y5Mi}kDn+lvHX2!bM;5+@X?C8-rP;{j~hw4L!KTasfXjwgzb9CADvJC=OLK<Wp~Z%F@w0sIH{y;oJ;)dwZp*u_X_R&^b(UcGvEb+<j|j14*PSD%`0wY$!ArS0XMa>r?V)XWa;`?q}`l@9#-?y)>`sn_Lv$m><S>8>MJ<$3uz4wnm1f2u%r1E3b*wm0GREWk<NGy;KR*QN_Zz~am1U=7Tnp?b~gbn<y8+>(M^^=b-J_JJ6N1ux07Vpvs{dAK-h1LU^Hw^v$I)AfdDjsAVTn?KT?@xp1`n#Q+7f62@Wd)i)irrmVf3Qw<*f~X<SD<P`k4!|{-u<5e@uWJr5JXZNbrCgcxfT)e~)OfY*$W!uGV#=7Dm$&2+WAd#0QLc{VX%fS+oC`BGF^icAyk3LqynHAxF?n2GmG@Y%-n_gk7h$NpA^$8NGxg4K28~?TEdpRJ%5~1YM#p1W4u4Fo$GP*alg;FI=stxNXNi5|-w><So7Ixnsgye2e|KQt(D}K%J(gGWWrvY-Kkj9Be>{`PjP5D0-;SwT^^JFO?*!FE<!I(;VPr>fC!ac6__&wJ!jmhy_L@zv2Mjn_ZU<|*44`l8@Zs&h<u2dG4htF$7@d>Ptx+`S4Qs^yvAlJ7tW=t;PfRx8>3Z!_iD2}B*gw;tJJG=~WUA6=<Dm8w5+d3yPs%^<`L9EajR-FO_$NWk)R`F<5xNOFn;Qbo=9xS}I8|HSc6}-e%p7u0%;iTj$Pc|jr%|tX>_1ygPp~=XO$Uy$=)3{^?jO62^deRv7=S-=&(|;uz#f;^<O=J-2<JU#PM>v86L?~#+^$B~{@ua7aV8@Uyh}Z>%_X@aA0b;^mB;g0j_meaG2nIC-?Qt8VZ6?C12jjMPOsHywL2ll_Y6og_oVz%uFF-}X09lZk21SpPa+^{RuR=c9Zf?qY=A^al;cIw&P_IOn;}5+H^dtCrUzV{vRNRu+Uaq*CZCyoYIcVs^~&waB<&jMs>MzaAp!Ds+BFMTM0v#BJ(Q;nVHnwnRp+QO7T<9rfLeqJ!7cy_wF@x9n4#6GJS`tF;xFW_a-$KG6Vc;hjtfO%BN-N7SYSi_p?I1YBUB+hp|)vrjRlR$D6}{+iIVg3zC3RznXx%WD<}&&JoTtX<La<BM-ATb+!gUq?I*YoM${(qA(!qDg-q}L_lsPNCz>;vqA?*TLrSp~M&1TZwyiU@t%E8>b8v0KX1fuN?E4P#Zck`Cil%pf@=kA7g$A2b`zoT^o|nt=L_*LCnW6~TQ*(sodD5oHg+dR_7D@k~1VFdsRSQ&4X!U7<AX#6M-=q&C0xNpcF426X3RG0aud~SZMg?P_%Nzg`P>!VHdI%X^7d?APG1P)QXV|Gwn}7o>a@H2Mu+Xqm@{$?W<7|!yWsPC1(8D&Ij@olBc9P1S*s*iUH4+LlV7VTUakCjCi5Z)(kckWri9ILCByYXm+wa%_Xio_!n{Lqp023d{Q|$dRyzuCs*pyw7wZL68r>1?X0gOL9fc3SBSq24gGEf*GrQ9fs9h~!!?+YlWBD5u2U}q^<qej~z-QFqqv>T;PkZdKGbOp%sGnId3st{B>Gx~zwu9Hm#>@~gB5F@Er&7tu|8?MNOeyq`Z1c2kwWNi=L04}HsZa)G%Thy2oMvA<s;o_M(uLeZv8?>uxi0aQ;g35*NGEGIBt&&JY7(yQw0SGPg(9pkHP6&~Fx?E*M#8ZkBPOIV!sAI>~C_K#vSQ+wz%kaVB{Rv-4LE<8<`7}8R4D2n<{*Qeu!}0Wm?vAu)i`p^SyYB${)6fu{V8eMY?`V*T@Iqk_5`@W%^0;!OVLW(r4Q}xQ?T*AVx<NZ$Q4rAyL{QGKTH*}1s2+utNx=$v{TwS`%z;3*IXNCe0@#{xz`1I`Z+;UQF>tMH3c@iwL+Bw8TmJxiZ0q=EK7FzA<IgWP9zMyE-K7=8AeQMEo|(<dH8BZ48V|tE1V);vl>ZPF4(J%mD}O_y7Te&gQ-{!g&7L-^%-%pZC*a|Tn-haOnS?tDd>5#M6jW$Rv(<G-ViWt|+rjzqnpK8}iy{Mr2lQKQU<1(n!wBF_C$>WBc2n2Tau&#yc^}~EP>HN+q4K5^m&Q;*a~8@RH<EbDmc&pBb0CGeVp7#8flIPUr(3Rk(xyQ7iu^w04~836jZTWBQ0QjMZ%6_JBUlQOq(+9B8nYJZF?yAhrg8EHsutTgtnop@98)nV6W>b{Oid8YsS)z5*&Gq*!$3k{0NKf4ImTF&r4Us^DcF-!ZdNtv4t~HQz4km*$<|m!5aeCVRB@`sI<&_!NJ|2iM%|o7j0YN~vw+4t3mg$}lZ{9#2H?!rGN5B(Xlr8y<sH7MeH(A}N(Kx>Cg2B-W=40`z_g9mC-Q1LV;0$gudI~=w;SL3U`Emn9vu!wO==Rkco}X@UX;s<E4PZXYZLY<C(k&mj|*i8HsGWkg<cSJKmlkHsDDIKy{Jyg|D*_-4$DEQnj^`PQ}>1Z9%lI$R{aZK`xkEb$3FEh-1INp@-N)h@x&sgu|Pl%CQbaFm$mM&sWj_}Ok+9i3^7?c=hBA4R%kosYToG6*0E{9LQf3xi2-ZCLV-i=2(>*XkkhOn;_ENH-1=9o^{u?i7P0|ou3C02SR^MD`K%aA{DIJCO=Qq4D16pKgQ7xpMB)$OE2XpM)b^UiNZv;I;1lh7RYmcZF=CkUz<gwZ3=6_Y$==i^B6f_k!Z6Zg`6qvQ9Vp{3KLBC?+59DF*?@zABlMT<_)GKt(oKKqn!oha#RxSaD4H9Uh`g*A8SYl+4I_@r6?rmt?kZ%zoEj1tO%zL{D2GN*ME(dQr)L>x%YagXaG*gIn|U=ot@i?5azJ}Qarx|po)48~{D*_GB7;^P9NcB1!JSeGeRd$gZU6t>TCqS97YX)H37USG3U=v4{^n|KFsW0$=yMa%9H$^A=V)+3lQ9Jc(*M0eu<c?Yz^W)dv|sjHgSefg3Bn_#!1Y@5an9-~?WjlfRDd*_)Si<sr9JU>K=TbPNO~ly!>{5M2N8vVUrM2|Fz>VKokz1bB>08M?FjJLT0)F4bMyccMyhfaPx3K@{)vP&<(;nZU<RH?VGgtH?>e)X&;#Z5t}}^lT2Xnjq*TF|jZ+br=tEwZD{{`mJZy?W9gtDi&6My84hDxkllKAvjLs!S%Ma!p9p;$~G+;jO8b4dXJ0O(Uq@~>nTcg3k+_pFzRnnnHoNma1(@WfVkuStdPPHeZ`E!%;9h5i+_Dp~zCn~BFke70blVQCiFYiA1(U#nd&R;YyZ&tRhG`3dil-sadRPX>`5EbRG;T4_A>7ilc$&81U8IS2$HmA1~UVISdm47bgnb$zM{m(@?`>H78*x7b@I{iXV`%KmR+Zi#PXFD(srUj!LN;Ol7`>2%28N$12V4tk(Hj?I4;xH>TH~WCP*#=|N#`C<)MO91_+YQt86i8%Mr-oTHWfHk@Q#5JL47lUeB$>)*MJG>=&Uw^&7g3FlCAFCChw969lt*R6gRn#?&pRxBJ&t<;$Xwl@axq1jtP}E)($kCbVqn|F7Bthg!_w7v%;7Y+MO9jli;nWS9Ub==7tJPBjEEsSy&~-lcl}GqUBPkcqcG0<6yRk}b%=E)TeGD~tLoV@SIuWLnK96f0WNs%`KnscvJ-A?!X0Do&g`hmQ+;2(rEb03h^$~#cO|ba>VRV}pa!D=$D#117m`%pZ;6TyqgK#uuz`>ks4y-6fn5kbg(%wRu$kWrfrCD#Ad!u@TMRFH#bmONzGj#Lt?<X;VOFhIy5S{UA^au)c*=?;$lj~;5U?mkT9@PltoK#@p(>uL;+`s=tKz;Yep1D{Djq4{<~};;SoujFLvW{6?_<;Z1m7=XpBi*g^*=HFPff>J)$z=9JW~^ooBnyz@mzJxn~oEvvS2DFP34lQTt+28UdMvGEy%Y%i`YKG_IpC#s()oFtETd`s@yd#cf*#OrgF<vZkx(Crt+<++)xhT=c>4=iWTi8s$x|Y->KqT9f9c!OjUfLio3{Qzb@SN7moRNZoc^O?iv5e>Mzgy{^BoB{r<AwU-A13e*X)<f64D(_WMhI|H_Mv^?UGa{PMHk{|qYk{r<HV8ylzm{#AJU399pc|8uB5@cUmv@d%!EzkeNy$Iy8i$|q2sf#=h|AM;P1_Rn0GcmIC!#m3|F@LYiB;){*HeFx9?@Z5pt2YBwn^H+F&glFv^UtYQl&oy{1!E+Iw6?j(R`RdoD1t_k-vj`7;gu?&CLoX2cJq$aOe!sk9=XfK&{eCd5q#H?OHc9zz;c?nZDD-`6wGqM<6p1Jl@k6Ay=&Pl-_WFNWca?*<=iu*B9K-{0{}9>^McQ(dQi_fnp|<F_9oV+((1(%6(KLrMh}h7W=?jbnc}_lMBzspFWlE1aX`NT8lN*P5g{QgD${RW-pQT=ZosZ?S)0|>V&QKO<g^0Z<ztZJ5;54OvVOgU@P}4yc37f3|2|5bBV$hTP!V>g(r=x<)BRaZY$3P%RQ69mJPj_zGOXeYgm_5F|RBD!|yizH4<3aOuD45Lm*$f5N>e^@iwMCZ~j^I}Wc{EL#TE?ZQ<%sboYnhCjyjW4o#IK;zmI=P#q9xoMebF%p=j*BW7WAbObq6F$nft}Sx!NG!L=&Kdca$d}g&*b+H>IV210KGiK36lR7NB50=NZ6F;W2Y^qxKvi7a-~u;@Q@_-c*Oh5(e(J4*u&)#B^>IAd_N1?;ID(VWS9v);~0u1Yi$div-`k4hb{`tmItk>=64ckw5iX$gjQ{^1ELf`Q4i!zbNmgAn&S^kIBABNp>4~!-U2u`7m@<Q$Ey<#*r!@f#Mtamq9dO>=QlQ#3t+$^%VdB!iy~J4`T92-K!{)euBIge3L7T<EqH5&IFZAsf5aT*WSIQeII>r@X(RNr4pNHw8qN~k_T6P=jRGlVoTynIXCswO_$tWS5SfP7y`NifAJ0TBCfz+{Z^s3ihgU;TU)<%=#8ML%SKmUI%3OstLF;%!8(K;u7DrHoIWQPRN#B?*|#f#Dz@V_fh+LWU=1;g!W$~4Z8m6})vfA7Tvw=)a5M1`pl7PIbBthM>sZjZl#hd8N=hq^j>ZOVJXWwrQ0d0f4m83t5N;&a((_X|&mAOJI0N|H#Sg_E>dz;;UPm)Pt<|0?cbS$b!`n(^DGR`2M$wy?a1o}mdnn)0{#g(HXoRwrT#WKCBWbS^M6K34#-Fr?(<wK~RR`Y3y|&Yx^&0=<Ie=`p3CbVcxy-Kaq~|osovzcJtT!i|xz-G}=iaJ1v*l*jX*IE_?TpW~CkT&hPOy<6Xf`SHG9~tLePBvh`}ZyXhg<%cGhVslVbE9ZwCdGzr>eFUOdAiTVeI_U(<-smMq$>k3lDy|XN{@GK&On+{rW1u4D>DIqT~2e!JjJr;4zGg3Z`-FSt!N9L1wc;hvi!ha#Ds=UU^9RQaGqF)4)NQ%?E*A!L9XPZ77}(ol3dv@=a%Lv77cQ53!fR`;<Yq+*jn9z9@;`0W3q~32Sf`B}yf{?Mss&eYPOKR$rs*99DU}B7#rWf&br9E<S+;VA+gygEa7Z!BPuBqy-Rnsw80g-TkCWb9{%XTfIEY`p1`_JxOqKi0!1(?O>k&7nv4jF#'),'Libraries/cache.☾':strd('c%02vTTc@~6n^io7&jrAA(MuJcxkc^go_vv2>4)v&1PwLVZ(OYbeE>Y_y7Slq6r!>Y7|2Z@x^$-#25qmF#p6~;7{<(%+lE@OSwhjyzI>Mn{&Q%=FE3m^zAT2{dRHIspT^WM#*uJWqE-YSr%qn>?zx%>^|G3FyCMg<!42HmWe#W2WHFc(fH(We1_2dH8%KhgQ%Spgs^=K%*rt^%SU3Ku$?3Z9~vLMdk=6pbRs*7YBIzdgE-d}ABOo=HSHo(T?Im0(N`4WvIfqjfG;UTuLkZ;0bf*z9u3@+0`69boCdyFh;uP8ID&II0>p9!aj%JjDB8ZS3ZhedS81o5Y-n|`#h$Y-d2>JYS(#Wo6Z28~JnPu7tiUcimSsSq4Sp>LjFYBu&qWy56Sj-9b3hHMH+D-1@<J3;BE**1CR<4m<D=$8^R)o!)Ru8wc~EgA-EgY74X-B9E|oMsRCl!kuGFcRO<m8m77|Z(BN4=Y07<h@%_Ixi#SIz<tsB%h34?SY#iV)-y6NUKX{hOfC@(K^%14%$Dy<&E3sZ8-6ov2%dA=jX2g?sRg$Pl%YO+Q4g1w_I*t05uzhDm8e&{62GMul17ecbi?xCu7EK%e4yTg8p@9vS3qp*9L^fVdM@>~hSx=K73?tsVh4OX1eWA>3CJ18Nx2J>A3%6g$?PlpwMK5_^l4n&LDXWZY{KRh^aeFAbq#5gEkhl)m;b{#4jxuj_H!p-)cK{EWx3_Lb$+#DMlwMNFSSwkWY10HjLoS@$F(o*FGyIe-{=5b}_pXv;p=P_w}d;s`8dkc|@YDcqPgm6blF5GE!_5FFX{@v^d<#b~yp8kIDtRpl?M;srj)X-=pa3J@K>@|BS39jnPjpnjWXd)_2-~K;2OiNlz!d%<)&og6Zk!n#xyh4&OCnN*OH;o&-$XiAC=)MK0sYc--Q*gU46Oe(t38IirU=P^B$T|%#jKUU&^19bRguasOG<I96sM&^2)HUj-?;27RQ}Zabuioa?<P$wnQ<SlP;IX$&AU&_P8Ta%IF3*+YqJtaq?ecWVM(`eA<(mtkhh{iy$6d{=mgdXVxVM>Azhak!_N{|1cFM`8e8SXrp4)5lr?~a7XfzqsD;L=>_5)AJj!spNFHl9EcP1Q%(b9vkdvITCH{vg9A!Av5qi<lq8oWI|HgRhbn$3(~nTF1fxyVbW295t&z>cC~Bxvzpghzu)YOr?W4Y#?Ys2f@snZNI#Eqn'),'Libraries/peggle3/rgx_golfatron.☾':strd('c$~FYU27Xh6n)pPn20{yaVBPE6ABAzVoP2unpBFkg@U3AMOs;EC9T<&VFh`SNeWF{64z}AEp6iZsgUNOkWxaR5A(-*@9gZCyhUyxdXRSK<KDC9o_j_M@_~HRXzfF{OINkqje67Wb^(h0UVr2ixj2}(_j(f_xPW4jb1u}5dILCb16*Sz#(AeO^xP>M9?kl5*PZxmJUw*1Ia4tT5aqzAcLQVR?vY_!uYCT&=KUKRSAn-XH1OfB`mPo!Pq?CUP2~gVk4k1)1^IXn4Bj?6INBd=Wd=(fjjg(O3rd^@3ed96vJsRF%erpx0#q!sj3_ENDv#xfd<q=oH}YH_1Kyv?#~_z@w^S+FRfaj#6CcYT<x8l1+60*NruPOthC{F9sZc-Po9*cKf&4}OCI0|SjN8Lmq=$zewz0v&SRBFBLNK-W4+b#IBl!j&pJSYs&DUb9huG?Cu_3f~#1w(5DNqT*%R-Dqg+QLkKUeaax9e36SjaP6uq?}095jk(Z6FqAj3`h!pk1*=%@%dLqok*#vZB12y(&BrGL?*N<%#jVA+|)#5_L->wsH_#If$*bi1UHQ&w-T_@iRrBYIZxm4ma>9a%2Ijxr=dyPjT9J=Ht0Dg$U4=-hr2;<kCn%+(wAo7@2%P3pR(rmmFs@>}3Hgh`|C>cUt>qxsrkoMKYgGN@tLrZqu~Lj&;-)D#Grqi$&ONuJ^0|NCr8{c$}<}ldSRX$!_E%yB{aJlk;FZ>yr(fA@dG`uGgFSC|t9^@Dn2lGD7-6zK|!71QdYf{7L?XmJ}7zbiDxtl%A_2B1i*BlA~dwu)|!QS#D!J>3ZmTT6%0e10|a!rg#&{28vhkd8xlboNE6FQ!M2_Xi|}vDNvjzOFX{WJ3Mq|1C%*QijRk6bR)!xS{o5D>KA*BmCK9*{VE?;c5K)dw1{R=*W8)-j?SXU3{$8t&zT>2GluT@6>{Wdr5)gYSg;NJN{(iBrObllR(t8@oGLNt%^mDmUMSp@Pvp1qEezF>&Et9<xRYUT?zuCn!HGQAjNA-QcDkgMIQJI)KS=Wx6;#nn!GDgs@=SgwpDKP)Q1gp|l8@!<wTg-oX-1OMNuO3Kr3#ghWNOK*&?Yo~Kod~leg|FZMP{!*8TTD1iBH^_!z1Y-9#v*#mgguaw$E8_HXwyPldoYvDyX40B&AfuJ&|AkZ`x9rqC+&`ROXUK<X@z8dTBmm1k+SgYT>6^G6g|BIN$uj#b!bzDQVShP11C2f6`|>WQ08%(NA}w0ys^z8BVX{qhe@QeAQ+p%|E#^Hc0G3zWS@N+l;FcS0*K^=}NsG%D?mL6%g^Lw&%HWesS^q#nH31CvajdxD<o)3|ACbNi9l2YKm%wBZA=4<E;>gRz{|+38s}P22#PF>);`qY90HC_{_$OW8z6f{zkMmnkyl*2qM<J)IWoS3Kaw?@-C&C)skVMJ&bTiO95#P+mYxCmEfh@P#c@-d@=!T06xCII0HQ?zH}C;!-vc?X*@2%KVm#<(4e%UwJdZT3*V%ito_no-n1KMZ|fGCbNFtyQ>}LQKBM=u7QUdRU&}H^T@;yHg!L~~UjpL'),'Libraries/peggle3/main.☾':strd('c%02U+m0K@mGAnB27@fBIPJj<$BwdexXM_!1d=6XG=TyzT!JE-BPP71*&|V~Wyp#o$FZ|ktc#P_R^)gUDUMe1t^==aSTW!R{1<u1e86IX{eeA~y7i6ZSo^R9q^Yj1I`=x~)T!!jI2w5EZnx+42IEl}d4~>te~*YS$G<#r@_VA$#MbwpKXH6xv)L4)6a~|$*&T(0R#cMyR)2K5)t?CIi&9BS>C?R9Cxn!BA)fM9Jt-SAptW1=Gr=z4ycb`K?^kQ0-x{3mw7jWbE<@k1<D1pzj~_rZH{(CWkA3L-P5g2#z65`MD@A-IepA42$(sV4URT5~!;6o_)W<hc2K`BZeecA-6;s3>)Ck-qfP6~>J2n~yQb@5`+YGk@Kr95Kmdjf~1iT<0FI<o~AA#%<L!#%+`166KSa(&0Vn*m5moVMuE2_K~JtF3c)Wn)efT$C6J!aKT1mOP?zay)AJouUJYR%H*z@S0Bu4mBGWS?<MZxkZg@5Z0RSMk;L_+t%T!N*@1MBCxe@JIa`uA2Rd0gO_&Q&o4hMtUL|-uKHIg@t6yNKKH--Cj6}nv-59m<ZIEk@BVZVSK#`e{KLff*<8_0M<1|^FkfLV8DnFj~o;$vcA%QzA(|X+EA8w;NVfQDzU?es_*qC9@)eKGH@u@LSGJ)kz+4WWgo$`L?1^ikL#0uuN??P<X0q+i0{J0yNXX_G?1xD5VfKx6q<>Of(p%5+gx$jS_8J$n5{JVY*_Ebzl#6zgoc%CR}0!sVyYl={)FoR8}G@48SO^MU=z3FEBn_s4OImBNo9zu)61dBkmS%4B<Q&ozaD=stZjpa+oSRMCnYFfvn<DdkN?Vlv;N6vzxo=kp}X-76xY4@_u{$ZKf>nA@vlVuKnl^RqLaNDUvY(g!aoGQJV1Ib!LonIOZq?3t5b|yoi?w{*F~K>8?Zt>6iWvhJ2x&u(_8XH>BrNRby~RWb6?{n?07-o=xThqTFdtWGl+m+>1+wHs0i|I{Bit1JN?yfN!|Bv+Kou^)R}JYpS;R5&uIT_hB{3k62dG<j8zSBR&{}<VW~ML2@G$qtgNg@=f?pq!tLRtw>1npUi(Zd^tOA$=-bWc*@7|f)}t|NmCT??6mGX8Z`=-pO0zxc1Wq%5=-+Q#^YF#q=QLigJbBi@_xjKB>jOA4AH>FXKX75tyvTvkKI%Sfz{9XN8mcKs03ft<mc7v6?6e}&Ml|^ZJl~4iXEGG@I{w%P@)Lu~M;uayM+|U!tDsZ6?2TI?Xd1DWz5jmqcQ5;PB0j>uw|o*Gv|jfUc)io3QQwQg*5r&-KwbWz*@}W@7;FVofe=pUQIKMwoul3Kd#7pfX)k7tC;ku;txhj&HenILuyL@p)eqK|CnHX+*!}u!d7b`f91IcQu|!_Q>&)g?JbD<Mb1+Srn9N|El(a##V&V^iLG6XI3heTNkJ_oZ#ttl&4QDE{On{mRc)=lx1jcMf-KV~d^z-X=cx@<xw``jA27sC9F@RStw>llME?qBZ=OH1!Soh=i<6p*~0XmquM}(l!4J(Vt534Ug-dmE@2;|wpycat{_=8G-#p|le@)i2XKP46yE}(!B@JSc&q^6S{E#*8!6Zm7HP7KrwW}1P1*oEFcT3hkk8}MHq`1Vm~w2xwI16vzOXdBIA>(3t~1N$ugRIK`|E8M-gaq@d^_bPWEI=YU?c^ZUg9tiKgtGr#8Qhm0It*|v{BE8K4boPb;di7iJzxu;LYiv@BOEB~Es?NlJ$GHck^{g(Q10GiE8&sVa0LVPwh;LUZ5xfggOamYc6s44K>uM;3A@y>(HHPKU(LSF5n#|AmdIHMGgp*)gbK|{=1LoP_q5$8Eg2Ao>JZG}RJf&(^<GX@nbkPrMsoXS?O5q5K{I{JE&JwBfn1*>b157%ZGkXbo@6~D$zIWcaUXrOXZeD_fD?NV@-!XdTj7;eHekc<VGAKjT%y1N?^KzSw5lz)v9Y9|E1G*gMGYL19!=+_|MydtW$R{W#|D*A^>wp#{Et#zcZzpfW_Y!Y7!(XKg-%0ax_9Twj0X!rDAol<H@akW7?tGjPJ&w}@SwA$$YYjVTA<j`6>gE^sO2`*s;})sQms-5D6~~19yjo-SQ5bo)WN2kH#dOunLN5dW3#f?<m|mbO{L$)pE&ecmPb(@5K4ba9*_`uQ!kw~u3v93sAhvz=$FJ^F@|p$e%9G}0MijAW@%ZIgxh<*I*GZ^TV$kj?#e;QfHnG5gEFP(Ia767IC)s7OfYZ8hH(#hF1wB_=h31{-RWu?D`=J6Q7l1`-S_qnN?Q{XS`*t4Q{_??B_sQKX1l<)4<H5w}u3QA$(o7s;SgkQGUfRB1yoETOH(*Np)aoXS8cMl1UFA8vGwcMiCHBrr(u<=4j&^==KZ8%Oh2^BUuuNDwBBU5EY<htkP1qQ&O7uLo8)(wYL<v&qZmR59l=UvPK`V|QXu?#w>m*YFQPXi%eqoR)=It~P)Ti-P!Mkj`%ZJ(T$Cu39OY!yi4WZH`uUz(E$4)}N7{8(fO4GXNwR%3Np?nsCKyRq0sthKXL_lN^>P@}ZKsSf6BC&=bn;Z?J-f%m}#=)~rLUb9J1NMZCcYfaXJ>joZy1^B^vu>=kQLzG1v6766NaI;AWfPjpoVeXpp8RI~s;|t8?B!;BYmSH#Vq&{oL_i54Wl~2X#7P}BMa7O^WvWZwSvPY<b%81Oa;g-Hw<pL(lTu97oroW<Cj#eZgD`619zdu42M#{>!^1T;XIog*tYea&SGKcO!-aZ5Ho+6-8V0C{uvXngg%vJQIuQm>;pSvgExBt>EiR_mdXe*0Gtu+DIjO?GlKduYjnDgLsWVH_s0j{u{|`6P`xE-}W>u+(pRgE>iDqJpU%0Rzx(nL~L+^`VGdp|7CFhD{G>K-&gbCV^Uq>ux6Wu`s4k(j(iNRQH{|JxS7W`R?LZR>);~>DX7qSE$ezP+2i`7xr8PY1OBJQIkM`oQ`D!IR2kld%!{@o?_BC6H~V_y2#ogCQ&!0VhJg8+)6EfpX{q{3Aq(=G&8oE1@>WDYcE=wTQ-*I}W9vc-cQ)kJSN*{aU|*?(oGVe!HEyBqN*cAmS#v2(uTrD_QY$A~OR>mA=rE@xg2wPRp&SOcWeQ)WScWt(L<Yz=TiGWo?dXsl7M<>ZdO?e{u0Oo;}q-mt{%=?9D}1XmGGZKB%`gTd%*(4-<`FyTYXQ_X%b<mN$YlFx<iZmZW<4+r^y24x*H{?tw#QV{2$^)l?!G0@Qz4|7XyQScj#`@tX>MnT7QA9&iv6*MlTl0<bejvgcxyF^=3Mr!2N>-gwQ(>!J~B>ve2r4A<WU=O57A~5Hv>bRM$PAzPbmo_#B3<`&j2ic-#V?lY&K|@1k;gQJ&k5UcO`3$~bY`76sK(l+!tomrVTt<pcxx|vZ(flz%KLq_j$BRZ>_bx54+siA5pv6COgIb#lQLm&JB;7C@sDdOHvpKLzH4M;^X+N3810A#lI(Y^!JrGkKOx=pkK&<)>hbvnsbXV*n_fVD~%ZA}X+ix2SAUP5M!)+G_b>i$={JQ3AMd|@YPBTK5&H60i56N%I+yuc;g}$Z}jO`g-dh>+)kViSU81mh@dlq3%1&^2`KER|7#=eMOafb|#Bn;hJ%pU+X3a;)99yfgMa{KVG&_4DtpypJ*%z$2pf}9W)biHB?5=7}e1slE@WiLJtZz~&M^2j}L3l^(xr>lyKA+O9w&i7e#RWu)2ZV3}}h!hF`;E9(!uHSoU;cEp@O0!Xq8kyppmT8m?rTN7!C%u?acbUUFN4ZEXx&@VyFQ}w;+{CA-X1xo#a`m)ZI=;#lGj>S^YF)X^PvT#jn9av=MH!jCGef)doAF~QlY1|78{`K1QQ)d>rEe8sT~UO4%Xz%#8to#SmS++-6Kke3p@IdB^hq5<zS?J*-)_A@K86{Fl|=CW$9`s4#}g0P8d+k9uA(Q-Ybh{64iUP=y=*lDl5(zPYz4z0#G_x_UQ<CsmoN6CpH=4|e0XW%t=%=|3T|$6_jOP=MSZEay-VeN>d1!=9AHB_S>TSFFHR)7D%f>0(Y1zMKS*>vja{3Gu4l08K%(ng*mWq;wYT6_-E6^_Q`|xU*>m39?v%hxofxIGo|V$^g>C}c0+%u(Jg<+yByhKb2lwlVTRo@19Dd*yy4S^VyahWN;CL*rmxBJFIa0NX)I8~*l+F-<&Fxkx334Vz<orI}lE}f}8-OmZmV@gjr8M~q;Ja6ZFWGla^%+bq5%5?=Sv55k)Lo+Yx=&MC%H_@Ns_#6yvh(Qb&aIDjZav<)`k%OY4|8Yb;xsM7I1YnuZ(8E9tqESkY6d^+)A+4$v^}O4Y-H(gh(U|#o@{q%BDURm1XYcj$4PCDE=LSr(UG!8F=H~#X!eHS;!;#dzGRagQ+4gaATO|EEfCTvv{to@D!Q@8glpke)0TEFyOt6fCQtb8TRRVLlRtdv%Lj!@mi~!CQ`9<2;h$^u_43j_Mu^aJffpboVYquJx(ryUi26TsW9Qo2jThm+Wm)D9=1Yq&J9V#~x;H&_uQPQmHFf9Wr!a5l;%Ckzc+xYJeI};B@Z`EeB?!5X^{`weP3*k$)>66l<pc0T;2K`~#(zEdBcNh(m>=)Q)0Kb3E1!sY=|z~Jks42#L<=Ck(EuJ{N~5gDo=c4qb%IN*;7GZoN1n<bN#IhWFZk{O23{A_v7a{eAH;Wb+VEWr7Zj{kef%)MABUsq`DXh}t2Ycf&33EbpESqYVSsk<IQ}_bjZ$~@#NnLU8zyiX8{IF+TtGJ=R1dQUCo7q&#+mFzKH=GqiQ?)?xE1MP-=W*Bhc?4t&>Bx@EEOeq`rY_9xW3+wKhTb3=i;jrir}x~bo5h69cJIBsD6(kj>)$+H*-I~5KHFCQ$<zx-uUvSsWEdA+)qwO&xkmwe#t3LJ1^<lzU@INKxYvUF5#QcQm8(pGv>`rX@AUMFlo2OfqS$a)kNuUpWy{XA*OOU495Ky>`AcFfLn`eZ==8<qqc9j(^pBoeSud6dAw7W4uj5iJ81qSuU?dM;~hABBmR9h#TsQ3Q5bk9lZ%4v_U9a&tSx>kYJYV%djqP|jEpwGjTIe%=&cvuq5vlGzdO{ja8=>Q0r=?ZT!5IOrJ>)^Jxe(+88wLk|IWaE>!YuMogd0G5Hr_vdB64eYh%v}VirBpzM`G+Ood!oOvCfVpW=Vsl?_}?r(2!8g_Nom(iH;Z6IC1p|91}lohoH6mnrh`0HMIZ`M4&5L7$JQLY{tuLRz&)9d<^W{22MlqL=FCgOI%6s@8Tvs*zB8)bB%-2%4?Y0+K>{@^$HcUz8BY%+GY%?q@n%sc&(TQPGaesh8+7faB8j1qS1}mBVgxV4&Z$T66iQ3q)+VhD1k)=8RLHG?CdDUhJ;d8OJ^o4_oNGNnK-1yigzXa7e08)wyWq%cM0cjY@vH@U+CrLAnf+(2P+#oyp+dOB~Dn%nJhYG0cOce+>M+Pmh&`$6NaRkTYB?<P;ymC-jSX)Z2;M%D1FoXOPPM=s5Z#mFZzfg@jmFY3NhL)hw<3%0eXw{NZ(_5nf9Y<^HN)CKp-mXHF7`eRNzSyuMdh6dPtwxkVy<f%IS?z-@sccB61?Q#IbKfk$$7w#KyCWlk~iiTTr4^+7IKGyyWZ<kTe2i1akhcg**^<{pLqP*^q+Fr7S89k8e2J0t2uAQqJC;=Dw;o=3S(X+e_1gl=*%9^>INTENwBMZ#UjQxjfv`G9Ha4Lb$n+!BDz?vw^>g3R8756fLZAPrs(Q!-%<fUdIr)P5_6?C{}wa!skE9mMLo8&~N`T_>n@2$_=g7D<KKbwe4tq>Ha&?#?Mb2`UkYraA(-hN4R{Iu|t<&1-mRJV@%TuB|wBpe%CAQ7d!co(aW{FP#}R(<iBRcjW8^W<(@)4?;iw)HXM59sU1g=cZPF;({Jq8E-}Df7tQzNBrvt4m1z`2tVXM*=!2;`+c>AE%~Zp`)rro^S>3-oel'),'Libraries/peggle3/gram_tools.☾':strd('c%0o@>u(g-760zPVmcDiz2;)=+Nmn7I;|*B6*VaqI8vp}cC=oPmlgZc%(z+7hhpQH3a1IU1{ve<Xa!Ab#G^F`qL_TRAN!$yL;NqKe?ZT<uetMB<438~tS~!s=H7G9`~2>mC6g78@I`)Q^4!me@8i|!cP7uAo$`G`+<wq(wu1?mvSzzCU2jK(GUB?FQYPk{nIx1}2|4DJ9ZG9-WH_s^Iq;jk_G~>4d)>V<+=X8p3}Sz_7k29L{<#q{Nyqp-{zv|lzmnffk*@O3#bp=9Ugs<PtB!oKz}NUqX69|d8ib@-R6N1|=ch=CR!cP)Ao-=}Wuzy}Q_sf59I;Z0KB0KQvMKsoHKpmvQ*V<pMdl+o?h_nG+V#%#Ox+o<Q6OF8%WPC$T(7)y<|Gjke8IOF(AN08Czqv!f5cZvehy`l0Ja^O31%G_{)lf9tp^jUZqUkz10O@Kc!{Ql2pn)w3z*Eqn$M-g8w~C?Kmy4EKVcBhg<VI_6Ld3mk$=Wt@XKa0h;2>95r5%V_?ILlnEog#7*l+sv&{3L9R*H$c#$AR7$eaFU*#`|UT`dcQ0zl2?m?d<E{%=G0u{qZ6@1JsEOeWHbmI6Fu@<9a{c6;1H3IUBUN>Olv<82aML}GT<B;f}8CPuJvYcF&tT39O7;hs*@+OXd_+4?lRl2?_{vT%;0dLa(Ykci6{@<UrWYnmMX<DQyW!9L)qeV$U--u0mv$Md|2MKQQ$0^g?;M>YH5Ft`Er`2^*nkNCWPs@<>I8e4!bB;P{S(blXwjLkW5aK`RzfJ=bN)}3#NgJi1t&vQAttnrM#(G$j;*3Yo4l~A}2e!K8Xxmygd;I`9d}}rtMX{h*50hDC5sv!F_%MDGHox%<zlkir|EXUS5AD^z?N&GN!+N(FL{f#vX`f2sZ79(5{A;M<R<%>ZkwXOX%EUGXWBO9q5x`K5$wrWL9g=hgSb{p92jg<(xoYt=hSgW#3u&fImw5f$+rp`%M6|xYgWWcXMrfj?{)vgs_Kbh5FP1Ah*tS)$sR2|d$VyC31eYt7lugP^7eOp|7)WWokEz)im863je%$lJMkeJRr`&TVL6=g5iWq$#`htL#S5XNGD@&9p^-jEdHm5OutyG8_BGf`X1zCi$){v-h7!nP})zpqWE1ze>KH-=665nJ-2HmQF=Y76P_E!d)nH)<emes5m0TrxZ!&C~GK}L{4C1Xr&F){#GNrP7<sfIxW)=&U`6^yYe;nP!3Nc{q&Rz6}lsDSeeeoZYvogaD5fa*`KZcHRPjThIAw<vBxSkmCxR5%x~ZZGzyyr05`ETA%~;xGt&xn*m$+rdmWyjb5Ou4B-W2{V~3Sv7?E3;b{VuC;qXg-D<7H&z6uS>pGLN*xj07b>0wxsu?Bbty9Av22nyi&%gyiR5bC9hU1tIee<)M!LOSOF~H|H!`=vO9)scZHSZtG(c-M{viR3im)i4t6Oo<IarHGL*Go66-AwnHxz3Md4jzQBE@bR7^jbnC#CTu5x4m74NAu$SY&L40UiVR{a)0HTfJ`de_gsrRDp$G8=2i+x7};h+fHOi@1JkA1Klz1RHK@OP{b|31Luc@Q8FwDBdh!+F(KP4LrIGQ1-2c~gVTXxlB2~2A~k~UTqg+YabUz%!L1N|Mk0aq22!DcPy{Mh0ldvjODVHAbQcxCW?1%^W1AI}Z-FGy5R84y8OS<)I3#9&ro*6q!AX&eE&Ra{)P^4sOdrsK98R(hJ7GHLlIkwg4GXxhY5w_MJBa-0demxUmrdX~WcfaKJ+rMaiv6fH1EsT|qKLirbE~eXy|zd^Ab%=)NA@u8Q+_vl6qh?bOGO+8qtl9n{K%6!_3n%#7-_PI*J1gyj}0zzFWj&)_4sb_*7v^=WP8K?!~Nda4fK;{Snv2@->SQqN&jFW>v-4$WH+DZo5@*ZhZ0$hm-sc);l(TkeU_nUE|@0|DG8Z~-3KIf%q)qk)WTZqV#R=`FZiP7F;KPsV^X~c(E_^(_Xs-aqS{n3c@nNqKf|EY`*k3VkZCvTy4`ea*dW%s$zPIUKvPWB?Wd$b%^LKPSMYt4Umn(uOgA!(NRh;jWC0jl)&#X%BuZ+^6so$$Z)mHODKUKsLU6v~757NwT2zg9Yn(>Xj>NVrQk)`4p@4gF9T3pn$~c2G4vXA#&Hw{cjWNNR)_u8FLrdCh4hp6d;Gn>C0XRzSsOP#fLFi+aWwSPAm396Vp%_Z~U|~I9A;UeDM=TN&!eFIH747cKkZOIM-yoKAoY7H7BDvFNMcKAh&79`yQZKQbDD`LEe94tjJXY`b1CWA{5JJnErI3z7Tgd~FnAgR5*ls7ld*WY~VEr@xod22ZvJlO;ZsV$O806Z8U&e8TP%N8QVdsFJO7E~Oj#?nGx=8#oqwF`oV|KB`;NIq!bg5L3LbQlzZaSLl%N@-;4p`-zo@ySD!|=>;Jm>d2AHF<t?%l~FM|VE_^1ZoIsdU`g^#g3Jc|Y0nyiOeu3xdplU5XlEs~^J+$guN=&w(R_FXTA(TV(b96J20RM_rM-P(KMJAfl(vYwi)gNg1rI33rhIZVF+~i_2Ks-evxT-?QG`RfseM89={OhK$2{bUujGt_jjE76#ICx-@^pVYvzF5{W%S5NGN!Yj{=pt`Zo1`()!b{H?qA>NGtrIbFxYGg(+`Eb#KJL%<WT!)ejuaeH3?t8?371)E2Qw8_jlyE-K)<e^MSR6Z^jMXKDUS!&+`+Z|Aua)C0U!`5<1W1#|jODLjV2u)d1(^ZBb{D3?7(!0lQ<Uww!G?C~8l*mQ44&&*texWdEb2D%x%=q@n(iY~-&Vx%ZPUH_EKmOj%gT*6sjE*8r4M9>asj%Zpe5YbtDPIisjygKdRe3W}jncSu*jbjSQ5exl{0bjz@ux`*GldCE){T@$90Tb_M&xe`j-Nc~pZX>KzTlki6Z;1Ra-gdx00mz<y7JW{-lcv8;Ij0+8u1C=a^=giEkyxoT@`+UBHpOGvi)xw%0oqYs3>dvrl8=<dQDkVlr<yGmXboORd{0WvO;opd}f?@o;`4JS(bvMROxn^x<FbI*RCDodbDf-YKFYg_LspgeIT##$<RHC%Z5I}dDh9C%d8uGrVhYerY?|{J-&2VmZCNWaRA#^A%5KJVfd)R-mG|53K!&Qren$c!%^cuz<MmN9D>gvjj<DnZ%oVTudsC0L^h|V-I7<kFV@d4w*JNz)5S<L)C&+%Wv<?ep*g=i9{_W#DV``+xKcrtvg%Cct#S%XEbzbbJBS{7o#3128{a%zfq(zJ_wOrTzk<JK@b_F^Z@=1ESh(P-1B9sX^k8XE@Ys3>jyolQ-K41nf$BrYCY8kcDRQ>nk;C(mk^capXC=4'),'Libraries/Compiler/gram.data.☾':strd('c$}RYYi|_S^?QHCmd4VI7e`<TSq&O352sZW2*}VT?RFWh?TJ}=Uzu44kgRHp!8jzi>uiFNu~`xaLt5jKgy2V7kQ}LB`;G5AKcKSYKhSgUxsP*aX4iICp56O6_q@-!=iagF{(R%-+b0JH-M2qDe{SgF1=qF4ik0DfF|h2z)}h}HojiL8e*ZLa<j9ee_+6>G;YQOfmQ(EGr2ZV%H+#;Vch8<1bkDf&^@Q~;6YyFh;2&aueiFu^1dM(X#-RwtVxg9bfSq~gq6XPnnp<{*syAXl{r=>Td*S@sr!^d#3~Hn9_?1x!bm8Kl`|kUL7c|gtaoim#mMPGwGw-^m&%74_WY`#R1keP+?^3={2ADBFUvhiS_RuLlCgy`$sTQQdnJ1~8rMoZ4{79u#f_W=^_`(WmJ_jl1YlV+Jm>TtLKEQyya*ekcH*Zcd498BFff>7(U<*e4D#K>|X9}8yYK?WEJyCT~C%-%2lV*zm6CWRz<EL;O=>^vUcO+jdx<PHCS{QW^mwP!sGLG|t(N4VJH_8kQu!fL*{%^do`)v9-1L_|*jz4x<uVH3p+Q01OM>#Z@0XV^SJ{T(tTyvl9EHz$GigFAPfXcuPXX+dll*^{V={fkL3lteA72f{Z9R)w*`UWSdet1>LI!fB58bhji<s=;Ln_4CT(Lca!ow77(3bXo<z$lO=^1Ikf8iL18Ax@2G`&CywHlg_z{vh{CK~5@}K|_cRFv&v9rDC5w8J<%NBYV;uJm?9<+h1ct=;4Z=XAX}Bp29&TIn(?y?}|*LW|U#3B4ZttB|VTwGG-a@<%VHflYi+#%>PrVaP5H*{wu*g%|*zK=2j;?&3lYLhw33>_XIc4iA{dkOiE@tla;vr5<Uq;x+_sel86_XV0A*|v5giddQFxa)o)}2gtuintg0=8ujtQ)f4Ld9R&v<m85dS9!P8KQ*(Si#Ve7E~mf5B8%5cW4FhK`Y8ZajSW$N2~w)mjiDww~oGTM|u)7mdho2nk5rp-87`DDL{!j;=5s>Zs3ihU29lGrc;8Op}GTc~*@8v2K+&r%?}w-cD1No0x>9gOmY1krz>H~z6(&X>e`(f3PwNBCl6XX(r9!~y9lr$hR9_yTsn{X}C^I&TEG&v0v)W`~&Rf=byGjpiVzO6V#H5@XEGD)8tAVi?7WLNh$=`9&1i?zI)|Swi0$zv6-_KgYmb?y8&!0h@$xQ|-<q{Lv1#bW`d>ah52HPR<6fokoI|DhY&c=NqyFA$d*FZW^?k2cg~UPP>^vyD5Yfs_MvNQ!qy1V)$kizMxnb@kl)+7DOO9#-4Y2QY?cC+f2zAdZmI%PED(*z<M(pTsmfq$}(E#8ru__E0n4gAJKVNRdZtOs(V%9EapqYSW}lLO2eM-0wC#%$c<q(cURW4&9GXki>%A#U_J2cu2B;Oly$HgWO1=n_de3<;Y4N)lC!*W-(F>MxtCqg02mC?&i1O-rr{9=GNNxTQ^XHA^?ihA5@!N64*~3(d&$FZA}MRxmidRve?0>JA_k7s(4f3vvaVb%1mm6`IJ_8PF8;oIM%Qgv=Ii2(&krS3InjzIj)^LhqY{<29mU3%vj*eSu~^d*wyOGG;MG#{fSTP|TKInV+4n7YzJg~No=5OJhUZ&&{tnMmc>V#;cR6-&+6Uu;RJr1p^2KOb{OGepf1I1jP^jq@0d)X+$_*V=_ARH7OzPmc?WhSghTUg3uai1So5ohAkWNV*a!+TJSfoqt>5g)Ns9Jf}+&lg2ZM$Ror$SWo{#f7^xE(Ev^`PSr@?6z`Dk)B3xLSiHD3fSf5pZKaV%H0TWX85Lln0OUz$E4Px)P^c{y#i;ga=Lx3v~qUB~F0N6Q)~qJ|rPZv2{d4<cU0bS(YV=>;;V0ORV0`vHK5IeMgRk=)0X9n_b+vwP0dcUXHkB+Nl9U-Bw4^arktDI;3_KGd`0Kbqb|n264%v*DuO*BASJ4wmkD8Ua{{+_4sr>&YmYvcv4!vd9tQEHc<;0L-%eNLs0QE>bOn=@^xIFph34#E{lC!V#c*bB#|m2a>SXE21hHyK)7-vY}|)Gw6<{-)sHjcc*w7|VlV`$$`&k*Wukj35R&PzH)+^N1(m>sk_DLm_Y=<Q5i2`<DwjQSG?$*tR?b1IZ-6zge!!Z)&i8$IvhO#!v^{CDZZ6HwgvU<5$$PzaW)d58G;Ld6HjN{Fxr`Xg=&h&hjhRgBu0Q*imEB$cZU&x4F3bAxykv~P$Q^jT#L+%z-VnpH@Z8nI)9~D4jnCluD{Fj#d@BILy&mH-kZv3T<bmH$sYrB^3WmiXy0KI>uM$yW3dJi(N7j$QgeV^MRVsu!1h%6O@rD;@CtxWg7M<+Q6>#e13tg9!i;PZp7?Hiy%voJ-GVr^?5X<X-dB&BO_Ywp;MRyG2Qokx-75zjtLxB7UkRJmQbl7=i?SZA=Pl)u5m|+WvO$in-VJ$3*%C^@wG5fMWiDyGgzq(Ku{RE7%yjWO7QIrFyBhoV8Dal=?_!axe_H&(AAdJM#9lf`Z3v3BvvFaXnvf=!w$~kaQ)D-y)FF(ZHIS<ZfD~}k+z^P;WXK*rm{H?>`>O&`-sc*ju??BLQJP+@z!LA4U3FPds^(bt86F!CRGN4-PgN%G@XQ{Ocjn<F5>s#~f#zwpGLwoLKd#>JY+-o;JZ_mxN8$Y%i_uGxT0I><t^-~>6O{nz_QsA<}?hWmJnEZ~N&f-tbvQZKgBwYC<T)EBMoVo1^cy8Ew61Kj@<jrD^1r7@kP(un+Hv6k@<&4)iWT#Z`La3)j{4RRULspoDhP?h|ZF+Gk`_MLuRd&{3E??hd7N~Cl91l_MFkIhtrfH^Tu48z9f@ce!e`<-~Y(v~ztleO?0z)w?-3NF`&s(qHdCAPg)(W!UXtI>EZZCOcE%t^{zpXvsuadMv`7jng*8&r(u@xI=4pw}{3Dj7md!=gank#P=EUds-ROo6Uu^z*#2zSgYV{u^~lQkAu^H_<|#$uFnZ&{gN#%66xy%V$TUMW~dOp$6%N-HjQI+Q|8&7zDVC#dz!O<G<kH5g@4eKS%Gl1$l!APmI_3jZ|e3C_r-btyUFh{$cNFurqXx<MHv4}eKzf;cWxVD1;!am<}5G-XX#G>*HB8kTh{>mD^6uirL-j|zK8OZ0Omm|j=vSKf)vt=1_Cc-(YjAMxh!m2R&|zCS{KV4vjs4@iE%BrnbsDsCOaaku7$Q<8mx=vX_X6ANLbYXH(K^t6K_c)>`%>P5<VLReveOz)0d&igbe#Db_LZ#yE#01EOr8XF3=z9tf?6Uv<bA&1$aU+(Hk%ZyXK9}t0@y-qMhC;JNk3?m*%LKKNJ9;o<@*Roh*v-YqLn~0t&RYp}p)rmjTn}!`_do@Q>zh0Ct<03FO@75}%w4SZ_ni_+oCf#^WZDR=p6<^&T!vb5Q3h%uXtj7y+A^)8<Y-CbGoQz%`cps(k0)<c^Op7-sX?j-#^%-R`U#%9eop2<1n_y=cICj<<^D7foC57PICNG9GkXQkybFZvcaI+A}$7=ZkFUUcn6OMRWH1k*rY1<iblfVXp+V}|v;(&68=#ySg%4<leq1by#Imvm@7&(iPP<yf`PN)w%V#RNMSd&!^>(JQbH3ylzADLXBlM8gRJ-^8P26Uu{^&821H)t7Q>F|V&WHKvvmYmJ2pOh;4q0ryQGPxn~)$+d%#6Jo-qB{BS>dNG=?Cd28+iPVUi3orHXv1-Qr`4K+bO7G~!G7rE>)Gt3*RwG3dR7ld{tN1mZQH;2ACsT*q5'),'Libraries/Compiler/generate_operators.☾':strd('c$}qJZBJB36#mYyxV;I<j85t9f-%`-o1$QAs)e8?Cb+#>*b8pE?2^5!LX8ces70G10-+)=TZ`aJ5vv8Iq95j4o7mq_{sMoX=giB!v+KS1(j~*r&Yd}PUY_&JnM?R3KGuHh3*tD~JAAagt>d`k5MuYcy}fz2(Wb07U+l`{Jwh3=ZAvK<YuefgrJaO)Y{e}~({&_LQg^2NwEOOI+S;8%hmW)-Q+y3%WpgFRfd$2Wx0ERtOCGMQBVGA#y=02mI~!}aq0K>?hqeH15n2V>FVOBlTY`2M+A_2iX!oH#g!UV>RcMc(Z9rRt_Si<@#Zp!a->UcE|4W<Ji!B*G?#`FsF(2Wx{63f$+aCI%-h+QJoCU+r_$uMU{1x9MN84Idm+=ap;lrr}CHxw{!$)v@hX2lA@&|<EGksmzj0KBV`Azi89RGt~*PUxg0v|nUePY4-F_5kwQ)=z8#E+-^2DSED4Ndzfi?cYmN~lfQY42>J)Y~O}e(*#GA#q08`3nrToI&kI_!hs&68rW+TuO=4c?=TR1pZ*c;n_2NeS?nl%=s82N(CIC7Q~KTfJuG1Law)z=@Z^r;&(ym%X}%BLN`>~h!)8nZ79=RkMYx`4acdQ_uMz!f?pG`QaM++`j%WbL7DVC6~g2SE0waqij_IUjF1S{Px7DnbG-;16zIVM!D2tqoyrfB*#Ob*%j60v5Sb!m`|40?XYKOSQ)gna#QyDtyQ;Ie4$sX8%d$haudW!w!=tKGHF@~5>Res<UiLb_2GJk{7QoZAlC=kIqII9~aeke@AUz_<XkFIrvHCM5&vkUdI6XN~yt`N^yM?kxlXVt+NPjYQ;`5Wv!H(AE<E`L)`v4>;;fwqscsSLW#_+=y?5kqIW#NyFr=To8$Idc#!s2aWcAYP2Cx=dz(fbIaXW23W7|R$&LU0G})gG>~N;ycaTDkJ8)63_&U74Af!V@|(;nx)85}}>3w6Kh(DW!&a3e)iQ1i|)#SA1<ktWbt7|6jv>n?;9T1XMoo2LJ&goV}QtZYd<wCX&KZ#Qi*<M1<ewk5lk_3bN$|6$#9OY|!Go!M-jpG;!f;o{t`EK2DV2DKPJn??m+c9pJbMzoOG@S6g!hOVL;bJpKCd>p%Y)dA+5qV+ly>aftB*LC*3Sa~N{?QUpD8R{c!V8b5it-lR1DM?UF~b{G4)ieRrMF#kc;^}69GP&*AItEuO`Qpit|h<V`{nuNa<4W8TDp~PkacjAk_E%jvhxA^aGa3hk*{sTTe3e+1(_BM=)<t<7DG~&Y)Xo*mO?&hu_8}IW)P5$qw@&Vi21kQi~8k`?0_Q?K#h)$JSOyvX<5MmlKOhP2B7ghK)e<T2g@tXH}7xp?e5Noyr@v2%9NrW6e>!(l!pgB#ItX*;kcuG3)Q=KlvRA8+A%T^LYHbej6_)^t)JgrKwmewN#N(C6GHlknkw93VPPY9TVVBCn{SYeK+Z?rkFfDEKl#{2>Zvv7&e=qhQRFY85;qebR4L3nnZ0IFA&Tgvr%W+M&U71T7EzoUtJK3FDv8-1?$1bffmL0MA}!Q)J^qL3qS1rgDd!UmIrh(F3YV=TcMp>AtR3+6MY2nnwg^<9aezUu1cW<cvf-7~;s!Vteu)j^3frLzH52@n~iL6s^B6WSlM0dPr-#R968XhAGjKyC4jW3~9lA*O#2+ba*|U7H3&ns5bv^`>)tI)E2U_S|x&TrLrf?u1$o-FVQA8F+65yf;d`m)!E1Qo#a6>O}d}>z0G!shsJ8>Pb{oSs3+Lw&;9Qgc9%&++<u`P2~zbp@*+1bHS>ApRU@XFon@cz8<i+AZ^8ca^lOKwV{dd$vYdHzt+wM$$veGn*Qvks_7^h=Ko!ZoIf6>jH&z-pEi|W*}iwnT%uOlW)beQR6{V+Rz}iLMS_V&-lz{;Zg7iDTXvOM8^MlM8luP04QQILt(7TcEkijt7Ss>_5*oU{PmVKu2#~EfY=qx{9jW4QVxHJC;{xo2vW=k#ltRHR%j6s*#{}HP{VkjUq6w;sKDDJjH#VhFYLr-gg6_36r7!_`y*i#&+~C)d)J&~_Y@+J&w?CBJ<SUFUB`ahV5tFt63Mx%i808GA^Sgk_?K(YhHp402UxeEdoYOsKs8nJLI)eJoc+w!o6dFWzsJS1Du%S&`+?>Z}MYqNe+L&Fi69$?0f&j7WJ-jdukG6HRV0V3c=s9$^7v_`rnqm_!kvP1JZ!3s~xKWqYz))rE_QDFTx`(Uq1&AuM(~Qc~6g9vF{`js@1$o1xS~;zidVQj97YbU9X$DRfTbS35Vg7(`X^-qu^T{^=<FmE_P((Wx1G`>slt~GZhe87r;7rwz3UN9y#w1|OVoyM>Ty(O<ZtqQiDPVkP+D4$Gx*n>k#u9!pWggr{H6<!=7BLWKsz9%Ts8Oe|@7OtZHc8H*f6sy+j=^=S-a~KHdjfC+R<VR3nZ{EH7E~1(=r2_`n1N6|^<ofjgfsjJWg+i5K!AMx*xb_Mw4TIQkjET{m~S3Iyv?NEb|e+pEb@_DS6d?Bg4!`q=06+S2+s'),'Libraries/Compiler/operator.☾':strd('c$}?PTTdHD6n^)w*zVIzGa)!pRmsv;;+7VLV9O>{m20g`yhIje*Rq$$RTRk(Al%XrFoXzVAQ##MaG`MmrGZLJ-}4*T$39e%{0DkwcJ^WeQq|PxXqK6C{pMT-(NQ`TiG71qm3?(ykA$N=s)~?oY6Vm6H*$kXQ^w?0#^_6C@(2?o%NS$A<-!q!aU7wGQc%J;5kTi^yQS$`E@^72k!7oq%l~_&Mz%ks&=FduV{I)xi0+_4!_d`KItOyCL+Ol}*7KLzlV<Xgku`EDnQ5A(OY{xK0d#XHZyJO7kaFj91WNX4g?aguzN2NP8B}~<Xl?<Scs`T9si7e0HgpXqFun`Y;Ydu4h3m|Z(h_|_e?xSdKBpsy4uhp%5y~V7`%*~>7%Ox>gzPomoFL+>Q9EWV%XI7<Z&(Z?bb)T6wi{7lgdV~A1o)5WW`jZ7${gX!-qIQ8W7_eA#L@L|J5#ht4+&ideZva!+?3L~B%s1lQcp?9Q6+sP1;6C}`gBh*uOJ#s?%XAGi<v*9_sAE*Z*YZ$=!EfzF2bDxoZv#|)y|G+j3c^CUqfnGt1qp|1FJY`Z9KPzSFOq4Pu{NlwX$|xwN_ui_DShyYvb9++43Wq>wqf(=~+5M-y^^7@YiZM5>gyo3LzwJFJ4H*g9)7ON2tKUw0AMqGI<RZFc<EO)d@p{3v`aY2OS7G|KKJKH-)(#|E4J^iiG5kPajVJO@fm)en>v9%2?73lNqhkB5d<i;O5~z7J-iVy1~II()%dRQ&uFNk<F7^n(0=MY9{+KAWz~hluZn->H)ZrNC>qL>6AZvow6bgCUH~N$TE>+Dy8;mQ1_aLMwaNIQ~XeKTF$hSij_o}mI!3m3f)zBsQVCVgAifN4TS<riN14kbD1u?xoH;+!^o}~(rniZNMVxYsiiaUga-@sm6zCF6c}LnO!k9h%@zR(8>y3Og@JYI2H=tkrlzM*+=h_&rG;#5XLzZ$Q`}=Y%Qjcb&VF(3)Y((V-q9Iib*IHSaLQql?fMa>x1RwY<6yGeYh384o@IQ_$1*<avH0TOUU7p5J2MP`x?|fL@60<Yuluxbjk($ZK)_l;0|ceXZ76`WE@}^l0uubv{j3g<U886K+a&|0SV@O&8alM_A&s-TGejsL&i@16XB?%a3sMl1+X+nanwd7WL0j%x2f8fy;4|obHjDAn-qD4wK(oJ+2-rTSNiX*oqMWA>8}mT;&p7SWW30Vmx6xhCLAR}XTW1dlf>4@u6yEC>0pr$~EIR1C=n~BHQ(TcVxS%}PjI+ndwBtjNPqI&diA5O*ARYPv47@3N(1?+AQG&i7IByW1kB<)=2nix;W)=OPJ;kint;tetZ+{YK3TRsXe;m_U^Z8WA7Qmq&fo6an$o42xyE=P#e-`hO5?!N@#5I=S?<XWC9e1;7K>Hz&&uXLY)!6>C`U=|P*L(G_<hkd2Wk~#)ahLVbl-3Vp5r&~#t{k*?s6gl#o%7{;PBVvcFwWpt-~$mx5=0kfy7*+QpL(3fKke*v5=Pv4eA)nP!rb<_8`=V#@u~<Z9_+l_kWshAvfsT8Km;}d{xHscwRsgMipUp3!{Oyb{WxbX#trC+e5%0E=NHW1DdNTzdm*sEU8-Gbx8lBxz&Nw-9(`AT6m*ZGby7jURJ2Yi$fbH)qG~MC(WbCmtiG|TRcmG5T6t_OuAj_q)OIQpwcY2htgRQc^5@&y-ob=5djG@dha!AF0D5RmlxustuYnGMj(|3Swt%*QDnP#g?Et-k`@bMLStru>YP6+IZ3}nz;-=fl%#fC6x!KxvO}+MQdrU#{-^D4Yvsh2Nvtf<Dwkjjm_<?o*Wo>61l8Uppb#*%&wcX;<@gLUy((yVIy%ABw3w0gQO}5eMY^<>j$i066-Q0<P'),'Libraries/Compiler/node_types.☾':strd('c$}?Q-EI>{6u$RUtoCY#Zqo$rEaf63X{l;(#E*nTqt)W9gH=20t~c#URi%<9kkWvXI1T}Yf^m~#1tGPnT0lT9j?|mJMP8styg<*)&aC%mcCi3U*6hxn`ObHK=FFL@>om0L;zGr9oO(;EHJXm=X%(w-#V!z7h8r{IP7%{&PoJNjDW5%WnuO?0dw#xdpZH|nwHhX0sZ(RV?p(I&EkX^V>y%Q1FE7s!N-q)eu{NerI-3LP*}i919k*e59{|m1+OFj}t_ms;o|u~YtW-WZQ95T%mZm4p;4+T(#Wabm$x>Xc`NeVkv;}=wMt%Q1>*!3uzw1mzVa~2<umr!seR2%CumL|Ct#P7%>5opJSj%qWi-u1q^BAs;e~P+n<5(ctp~ZrRKSJOd>=nmx?7}+SfmbNK4lm?LYgH1gr#3DRq<Z+3jeRjbLN;{dTes%fj5A>?p28C%NWoRug*yZZQL25U$yc_Bb3lYOco8t6Bh~t1>q_vUhW2rYfGhjCwzudmi0MnCv;0G$z*OCY-_ee`)wn!oX~H4JljVz~<yn=lT<IgOR>*Vyx8N>%c?tGlpIml)<8*n7NEn=c0_`FW9a!OZ;VT`PF}O3Sz!LcpIOh>T19zZ@eh*%G5LilZfxGaS$CT&5C`A+S1I};5joAFytVoNg=@J>EY$Bpb^7D(_fIm^m>w6nLJyhy*g=#6Y)wC;dQOT|ieI>iLh;<wG-+`qJM##cP?O`~KOtFhmu>r+{42tU?g4&zEpY06C?&#+BaDoVVTWv`%!;%L{OT_$kZ2q{?!Y*vW;b0>a`NEEfUR#X!<%sk|8Pdaz(dGpqnmhRb@Cpe8`P7DPkWT`rn*a(Nvar}lq@NJ~RiO5j%f9}`a?|TXMER!sBe`)EF=@kYplmIy2$H$j-t5Po58*mF9*Nd+Mzr2#<ED}XH|CJ(gp#+0mb|V`yxj~_+8K$rHdNxZ@hl1g_&|)kbVUx?d5va_oPc;Jm-2BFo=0-QNP#%bNd#df8x!CFUb0Z`z*Ww6^1@j{#tdqF_r1Z><1cm;zJwpeiG)%1gV0|WI#(5Z_Qf}8+Fp)HEzeb%v?G=t4B-{qS9)bP!9qel$brJ+xS_&IV(f{rn-?tGT~J}Q6TF7;lI5x0B$FmpYjUs}6|1ho%B)v8SVyb8@@JHibdISS1)gT2kc4R#loLL~s~evP_oSqJKS5c#V=IR;n^&2iO4=c?FnN_&cf{I<LxlEd^@lt<(!||Fq<7MgguEq?jB&kIv3bZ;VMreaiB5*`-R`n;51U*OA+6TZ&NvI$+R1h|c`yvRK<q1B&xpJ_&FC9zcV(PeiKS8zpV6#^IZdXElrgwPbf8>BCbTo&SSNkPQ*;?!){hjzB^-9B>`jSY)G0skWcG;+#NOMSvn!^6%B#7r?`=IzpTjYLP7FX?Iid)iC3OcNldYEs`(DQ8*w0DEe>ORxriC}imMSgpCct~SX3x7#dDNtR`~(g{AN%}3g=lYaFz7Wh0Uk#H#%7~2N}i0$?#Ov7yA{~va^}&~wpnLs;Bzf<y;-k$v8d#8jlsDATzD;wovMf>ZksOl5iwJkn&6Xckz8>bX5EtR=`{NK`rhqT{QtyeTeimzlJGu#TnOUh*x+$A(y5%lPUXaGTpOwzv7;)=QH^NpFR(H>aX!4;A>9#vBk!O`$}{iFLtJOw!oX`X!yhF|_`}eP>{=WY4xcqN8?ZuE7v!K94=%{5Wx>g$UY0sMBF1OHvD<V%18$8Sn}_gRHd~nn=Aw6%=(3!wAF{-KKQ%$^&38%W0T%PLSm_tU#=Rz_Zi;bPj$$|T(S|b@N+o@;*Ejj6z`U8##N_m;a%pP%ESLBnQIY4v'),'Libraries/Compiler/tree.☾':strd('c$|$?O>fgc5WV|XEII8|OO&KH3m*arA0llc+FKM^X}tkU#*XZ*6d$P&ha!P!K`IC#Rj5}EAUGfdhxud7t{tzFs8CChCNn#4X5PGAj?eLAw0EETzP29hjE0Z)eV_A2oCMNW`CMiV5RaqeU>ao{1aC9|KorNjz23dS@OF2w=ieFhyStQV@E-PgEeC{g4o75;Ilsx;3}E5}a>gj|4o~ryA7=iOMERLIn$7sqEARzgiY>grH~11<htU^O(lb2AAKV1V{)q3(SQ$4FcEe*85HwZoi2hQkj?$P_K4Zve9sL5&@Y@=CoG7NF7M)!ioYz}o8YzqoSPh|`?bIBUdrYl;=cdE2oJZ5A2f>t)_Y0o6S5Rq!6^8(}0f3O=g<nRQ<ooH71aKT4OqKMP=Ui`DNQ1n_Pi|Fsd7?JdER2Jyv&9unEkp?g=37w${-)3={;?uhh}`ael|b5YK5k9^Mcyn)84ra5V!Ft^#B=H(A7@c`D0y4#Cb5JGtZkX&XFS25wI$#3SO`qRaodIKEv<1#7-drmuA_+hay9pkAws3OKTqcL%Pa@;G+E@H?o_1m(7Q|bN|q&zQeAIn*xOLVF}@`wml}Ykq{};R6qFa4<=w9jq(#9^ITmKja8szm_;fDqIL&C4VIVV8oGv((HcXhS-vYf8!P6C2ds03Gz5al=K|89YMpdniO)mSgjM=uW6lD3vXs?;k{@tSCB7LGcFIR48?9j@Ej-@NHP9+BrnN(Ay(&|a;l&EC3t=X!LwM}Df+p+ZhrggFZ>5~-y3O`f=)f3r_6+M`Pu%VucB<C+KIVIW'),'Libraries/Compiler/tree_txt.☾':strd('c$|$?TWb?R6n@XI81`wVt|75c23AOuP=l#0y?_wIvguBmrQ1!|ouD8-^nysS3cZMU!y>g}r6?6CVxP`G@t1h!l5Cnra2}G`GvA!^o$s786t-Y{Zs9g{UAe2y%+1a(x-O-bh&i{Iy%KhsUYJm3Q_EtE*&0|Zm#1s9Q^neXTdGxxckznybf-dx?l4;!XXkKRr}R3>6UG`DpSMWNAH;#+ZX#kgh<qLi>EHl%;WsN}2(F+-kVe;HB<ctfL?i`dxxvU4bJ2?<(mzyo^+Wr);Tpc0?bdS*`>HYDAlFD<=16HbEI9pyat!fkghO}<-!9qn4U=QJQloek4Jvf26BC3#hu27aIM50g31%g;7D=z^uJlAAWlhsbS%*Qy5v=`43R%JIdPDI;<11Ld%CY@l^!gNOV8aHS!XA?}ak~dEjO$@aidMDY&_0=giYQpX*kxdwWxZ~fN4|t>??Fo{N*sq&8RKEX%|Sg0gJtz`2G8isY?;D3oWO;xIjB@hOY@ZGZDv1uEXf|gnf$weP5W*q;*9BQTd)uBVc*94Z{fS61V2Z?O(0u>Xy~mqeUE5U!5j^`%Odw5=5ESjplHVF0qjVphRsLVhF|@hq_V0Zm?nZ!j|d@qsG8cYRyeJ!Jt(>*ES7#^taCV}Z5%!%S5yO-aN!9N59aNLf#WuxZgWGGpTx>fHqyZuoftKcp6|QOu(Q0Hj1D4Agcl1ee_uayT(~qsLY7x{_L|Iqc#%)iW8J+P(F|AJHurq3w3*Z=aD<(^0Y~tOE=}KaOY@cDVg&<OQ<faP5AYRs3r=13xHVyE&2bK_KTkhPz*wBL7|x}F68i^L@$sM}-+&3zZ?t4OF>h*VOF~RP1sLL3dQvLrSJ0+o`U!J=2S4FBZF@B(%E>=3jezAFbjy*4Z(x_|0X7+{4QwK@6Y~`74%~smfr^7-v_#ycx){lj3Tfq1D7F(_c4WS(5j`))J<c*2+6uARc!ck?C)V(lPR8}YP+)|Q&$FMV8a9>S7dmJcy)u6Rn7DU2'),'Libraries/Compiler/expr.☾':strd('c%0o?TW=f36@J&R*eqaRR^18|jlQTQP+NA>B8nwg_LE8wG`UI$uSs^fYMi&kjTI}cEK8(Z)%8V=X{WB;A{V=j9m@ea@A(hWW1svJdd|$5+1cG$iHcnpC;@57*_kuvKHoXR_(%Mcx%pqRS`EMb>g~DNlc#Dm#@sjxf?9k&c0K={uydv!_L%20*Y!Nlmy?eiJND+x?9n4L^R?-j<3~=wGC}RF<IGs&`C@Q(4!$lh_G4$#@x1C-Ggx$*LA%ooYMm~w+vFSknKw1&z=tWW^tjJhI8{;POWs1M3S*tr&?F8;siAU}_CI!fhD~}nC%pl%#rOrj&Nrtjtm93<_yD%tK`G(QZGM$M%kL}3pX4`(@h$$r!8qU_!kRBZy!yE_&AJ23{GIow?4yFC%lwhx83vG>iP#@kKYL-T5wJ=BM5i5iu(8)#WNI!<bl#{q%zbg=+I6&I5cUG~4nE0Owh;PJHBrFL0tF1S3fNcBZ~4;$%9|2&1aZ)OJN!$lKt6E2%Kst+o5{;`awKsUJCPGRtu~t>U&T*r(P6PuL3Va;-34xvS1A=BOPhR4K7L2;1wl1;)J3k`d3=<7=|=x;55!LpnyjxpeM#0an%wUnt-4|tzw|mp7}Ni>X-*cHX62iM%QsK*%}LXk5|*p4-$b{DFDZiL>h+i=#rpS;ujg3DJY}E#@9W#S+3*@f8}NT5q8-gmN~at#k4_-`O`6f{1BvOQ;z+aTB9W^stex9OGPKFB8sRW+<p@8GPCIV3mjWmE_J9Ixr3DaM9$WyS?h)D74v~1k1^yLZrE#6Gy#J9Ty}-#c4LdyH%j_3`LIPiSl+&oU+nv}s*J-vE-*-A){1!OBUMiK!<wHIBe8cq)DTQPNvg8~&^S0EC(4ka`1G%WABS!urYI4R3h<A~1Fg(EicnSVi0BF5EdkoLV2Yg4W^ur26e&s3b;E_hhzuW27cE9e|LRd5|U(3~*15^-140S&tDPBEL$D^+x76dK^zbA8q-X&}y0?bU>lhL7#(MU5oJQ$-7_hK}th;@kHuBuf6`!J7<kFx|mP6Ti`Riv$y9WdK4_g{}(56%q7JTr`pDoiDo>oKt;|GO8&tvEQRJ-SR&;Ok`a)pX^<;L3-qi7!P#ycD&i5?96qLT*GsJq~J(dKfAPlh*c0ml?dQQaYw<jb-uBqVN-0Kh7t7`Tl7p<L_}86rKn03XcRk6oj2;->d;Uv0(!|vhis9+o!wB8@o4er!r8YlRm$~l&dE?OA*-KUB0sW@Z!D%hB*TAaJ{=?TUy|nTl`PL&5>+|x}RZJDN$Q3vp;jc8-N#L1hvTiPi^j40Fvd?Y4se6!9HK+&&6|<o*${FK*K3!2*j-MTNWI!#<xd8#e&V#kOgzZ5wat3r`~QlNRN=Zo++l_jP&?Wjc@Bh<r;s+Jo=1T62D-eP|>4W^HWmQ9r4`2ibV$A_-TtBMU-~yQJf0Tf#1wUW)g%1zHBj9Dvr5Qam<yfghg8;R%93WH~cHK7JLJ4WnJZd_k~P_<bb62Z_Rw!6p=zjyy2n<y;;j|<9a08=W9}ifk#Ctre#r=`g(aakMG1O!dT+*qBN%jwZ_-1P<4%8wnEi4KG+YcO82DtA1u^Xg`_w|Jja5C>@dzQh-A+BnN;Z$E4?$2;?EWkBQMvQpG;*1;k?32w?KsFVvnx{H2W*xW(t#yVx#|8L%jEHD+~%0Wub_2%h(`keEZU*jpZS-WAcObl@UJl21^uk6w@FR<#Hz9d-P7~3w&nsC!U_3kOtkWVX+<qsi5E}5`3cG?FQ{8?Ucvt1zwrc?w)&eJ6)D0T>#Vf@_)+`?U5}5f+fD?{0M?1n+Xf6hurCa;(W}XP+a&eVMW52*JO6b1EUN8lX5@kGJIdOFh_uAxr5?nk_|<R)6(M%qY;yO(H=uzXoN);;?ZctAuwQd9*{&~s-U~cFHRphW!7}SOfRSf=erTIkmkT@74Z-C+FM#&Y@KH*JrXN4NU@<a?PdOFkvimCQ6e}x3X=eWY50y-3&bRgU<lQDmx>=bMM90N|4EJ}TJ2r{nl4GO_c5V{OF(A#$_JnZ*DQxEa1@9bWh97Oh67n4JK0_p84+{2-V~#%M19?q780Q+2+hXz=$#<0Mep{IlRSvZ^}$t%V6O&VRbNQpU3*##Bl!fc%7JjUFdl}!y&UTE2W%V`>+e9otNKx-P@>#Z<lOw0FR@iI%J#>FMU~xvo3uY?IGf9JR-gpR8b#a{a<rdrPS{Q<fP_1?Gc7TzFS;x009Vcg3Q}M`x%+|lu(upG2%L(R<oZmk<wR!e2MWDMEkw9?$A)`VG~_JFZ6##Zp;HM9Qg|wd9LUjhT7|^&aOjfj-6tXLWjRV^n@rvw*_HO&v%s75-r}EeAZW2x`4@r+JUunZY|@=>*UyB36L;jf>U6q6RFA>y4)vy-FsvNv{S>q*9+CVN;V+|Q2O13{KMH{<->A>%6jFdUTbwOaeNxEam0f&k@R>fqSVL8*Nj^6X2Eo!O>hNo@(a7M8SH!YR2^P#H`xpv1Hf-iL8!g}&iXQ-Eibt|WV=0PIh+g*A_vc2xZZVF!=zW*A!23kmC=!K+2es^C$>%b^J5{l?7gN`U6?tvAey7&!1`SuEZ1bv7*16LAjgEudrH^%vb(hR0XWy&6xUsq6W(oYBe~vw48wn(?$jF`v$fQ`KG?`GE2D292oGwt?lu~m-CDnlG^C3m`{geV!@6hv;S_jDp&h3P*6QR%Oxkb-yHqt(ch<-`#WoSa~q(mxJRU61`@ix+Nl)N%gQPONLim~Yg(#p<7*)JRI-ePrIg~VIyv<l(P9sUWnmB`4VuFsiT$VgKE5bcVM6I!G*c|ktlpP9-5tmaFeyqE1`>ujKmK=^u#KQ6lXPdpn`pDXlLRv~Wln`pb`tF*&drOCv&&L3M7<2wJ`ie}gOy^(J@MPH@ipA~(TX-g{w@}+V=)NJ7m8!%%_vG|cV?JN>06|TNF!s<!eYSNI|80ce^lb=f3p4Loyo<;>my0q+WDB(B1tw(z(;c<}|b`Lvvm>YiYO@O<zMnxA!dsS?GSSe-g)AN>kg6#bH^y!ldD*Zw9{!y0XGVR5UEB~ZhFtjv%xko^9j5UK^9kxO+*6A9xATf-Qa+eR7A+Wrm5hBDD1GHr)Bo{$=`9ha7GHZgw{{i~0WHS'),'Libraries/Compiler/lambdas.☾':strd('c%02zS#K0a5Ps)ZOh!WLCKJnRhZjpLg#bAe2na~>U|Flh9w#dn+nQaDB#LBjf^j(4XUrAbL4eE^2Ld+tL;n){7ew+ONL5#NPtWCD)(*-_?VY2#j<2h#t9s4EFXG(6!=JH20k1yafAGMeBZUHEu77$caJlzwdGKhlTw&Z}uFE<1h;Y}QJ)iD7@bRvFhYP#+?cMbyOp%<v*vqUr+>;Lv9E8hm#y)Uz4(C1F`uu)JTo#LkVqah3<T0E%EhfZEPb`RWaXZi4e{M{zfN*)gB=4tdAiZmw1D{gA1Nwdah0C4NfMaI!HeV6oC-AE$f&oXrl+WcKrY$xTyW4xb{Rj5o{SEO{oJX;<VkF<eEt*^pZ-bjDxP65%z^er@BmU^hYrESyFoGAFD)I)V6Bv8;?qfNQ4@jHd6G2!0#~n<JfXqjXm5axZ_7xpb6A#5?SNxXIMTjLY_3MWS1~4M<6ktDb?w2b*>GVoG0?jo!Z>!=RS%H)xwi<tDV6ci@K}YTs2l^aF3xv-?EJDmRCcLeew-twm{DD3uM#Zf{pWj=MQ_nL6^t4zMuQbq7q5E8M_q0kpTr{H=T9u*JQtN6>H&$yYO|7Iap%Z%MsdUot{zz~F-d6l-v04pGymTl6xXgu@?UuiEg1>Z<zr@{I#?nyW_YVfgi`BxZ?@E<peozVZu|mf9atHWw)yd}_=B{0zbR$@4T@3@HeMfkif!3_JBGI}e{+5e1etvCqa&2^6VPJ$y3`$l1cxxD_!0F1fbemA{KR4=6K`glkW2Dt38IqbFqm|<%beo#EChn5bXF=n&;a@A|Qm>C0kMk4=b3JM%b63ZQSL;vKm!Cg_@jQYi%;^p92;T+Z@H6U8S2BQ&f~b>ihQUu7B5sOv;<-f{u}`u!@8oOE%Cd#hfuz!w8BDdAy^1X{wRKwk?K-lF+oXMlEHZA=9$uz;1-j0pSj-N-dyuW%wYlHj(0|Z|&AAVL{Bp|D*!DuEC=FEnpvu}?)Y6hw@tuSy+i$l}SS)24F`c%*o>?6q17Cdw<Mk%}HQb1rb=z=8ruP~Wn|Nz{IjQg4xwM|YMV@`*-FmiVy|op#r0Uzb_tuCCojY|KY_JE0YdRv{pg-!IPYHarKCxP#fyA#fIgA%DUapPIQOK;;XIJajh(g8=j5q7cFNWp*Rui|xZDcwwW|+LcCeBc$SS=^3#A?u7eVE*jp+-EKQgz}AUx@ScsPvhNJnt~{6Oreg_&kX6{;-i=@R7?oBJPEY2^w0}vU0x*;UigY$7<VZxtp$VSLV)OfU#MB>`DYvL<A`!CK`wc(nPGtWa6<j2-`ED%3dyndtR0%?NpmfrYhA)b0}>wm}b2XD~So^e=iJahtkhtIH4J?q%)idQ+<6_x$B!KLlsw~@qLrvFX-x8s!Ks3*Ff>L-mXwUxG`Rf7B8znO0u$cqcl#?3IHc}du4mY<=fHGXx~FC31(a#+5@n8x+y_Y`NJa0#fc&^?#Q*0QbIZF%PYgg0|WZ8xTtt>guR2O2wh)Zexqk--8LeA9VO1C6O$P=Kx>A{)(&T)a!TA!I==1RG{Pb@byn06&b9jRk!(m8n}Kw314uFbP0NjZQk)g9<@Z>legRZV<a?{Nl00LL)i<Bnja53$u?Pt^U!Gb<uqxh#eHiYpo%Tj6Q$VvVTQo21guJj*=Y`7{7m-5`gl0}bG^xJl)%Vnfd!!_}qDXJXSlr5Bd7EV&GBmL(6Q!q|jZP8hDByjE!bs*Q^*;1U0FG6`>rTs~Bdn1o>#n-E>e{Up<`wA@PfV<(oaO+2Dc!ePeY4g%t2%=jo2;rpJC!MtU2?kP?LD}~U4NwJkrJumY1sFFWF1WO2SY4nQ)JeGkUA3>n>D3-4YJBpbL@njk?*PK!xjB<aKQJZfl?gmREX=4S;m-Tk=$=*#Dk1d=3%^)N!^F-n3GbFL(1|gS<ZWTM@GS@3YLrN`xpIf#5X}o#l&SXmtxvwEDo9|B;slsH)}g)&K{qoLN_ah-$Fu7JQJggIyyt+eNu$%E~jG72TRN;qB_i_%|NRsV^?bAm}<o0CjCR|5q5kVNt<s<8ra!LTBH%&KxEj-feEIZ3gy$r2Ld;gmS`at#09ZLN#Aalq%t;S1WFErPl?H5WgU1?Ztcx?BYR4`4|{kFL6poBvXxvAms7GMkhUcIfssA8p=`!%`C-D=2e}$^`>h7Wq9OFLf|m<GwS4piEwM^tsFuE(&s->NUiwLbrFVxCNRUzG7H3MyM;{KzoT^U+BIPF4P@XK4<<<zbGGy0olGfwd1ZRj~d`uC5^d4ED?NH?;?LG9fh)EfVTFs-y$uKkOn_y>%UNrdByZLOFNq3kXRBF`3T`_M84V0m>F({ZpGOtJ;$`hfaZ~fO1uG3dTIcQC~6ce0TGBUk0!<BY_b;wOFDM6xEQ93@E7iHdLUfhH=QF)s%$X@5x6(;`$t(}c`ju!PcihJ5kThd=^ITvnl?-qAY2V#Uv+_~`Q(iO3yyv$P`_J52KNG7Q<k~q0k^$;nX%#XSRm*S{0S9SQQ02+(}R@TXL$H>mvUxhN9xw>EnEn_7-8EOcTW#PNRP~bxf#q_VMcg3-*!7rEZvQfMrHj3d->#|!E^watn7<BskA5NV-QLW%V7pTLPcF&xvLqDn5Pl?~fln07j7k|;#yaM>ibM~u`)|Vd5!B~KC6UHqVcVH~SxCi3_j6Y%gg@C>9SlT#TeWEI+gI+p5R4(<FQekfqS_NSgpA_jXd8;}sP%YNBe*v;2o*M'),'Libraries/Compiler/rewriters.☾':strd('c%0QdS#K0qy6^montnQED#&f_Y^~{;5aXLclVAiycSe>~Dz^*MO1ryN-6qY;2*|<`AORaN!2}57gv6PIER&GQf|T<<^AoP*A25oPKXAYAY<0G(?q+$oD3xwko%5Y<-_EHf^fh|!z@a~qIL2@LUOX^+@NgUxQfVd23yVpw5=Kj{&O*}akuV~aN*IO_AG>Go-sfMKeQwVShvMlMX7=odSq#{pW{5T?jM&ZD1Mqc@kY|Ew5Qg(RNH@v)aii1j*Xo2X70^5MJNj`%-=Lc{d2di7FFpU~c>3VXp2IT)(0UFKBJ?)>m|m{c=jIWo3AnYt(@rCJynW^#4k#Rlz~Me$NsvS6t8jZu{27L15C)wrpr`0N^gF_C?O05Y1X;Sc(nw?a7QK&@UZI!icVTTu0RNgtaQGU104M_RtMoe{OAVTvoDX-U;jUR=!Q?!w^Y2rz5}%3xvb4XFwF5bv-Dm$pSeNMgK!65nK4j010E+FP+0Iw#wVI8TR2eVAc?~{bNAO=e+|>{2^?+0cuzrxV7h#3F^c?*sJi-T6c~?s06#ay*){rRnP0jCgrxgV83^1Fk0-b=)8X)vN8>pdeJVY+Hku5qKG>U;;gMQjxWP@zNj0vbh&Gt$fsJlBHSV_0bV1+toh2AScM)D4+G%8{KrvMW5(tgtKXG+JX#1Qye&A(2HnR{nmAiF`_yXSZKBrNplm8{uMW00h+Pr2@dyN>j;E+W-g?#A0^PM}^(@rW@sZ8V@s8uhssXZP}(AJXq5AYq-Jtb?4^>GcpPTBX<N5A5?j@wutXDpKF8+V?3?UG>NAd1fOx^)jcKBLE_e4reQAs1Wb<m-|l_afU>s6QJRy-LK~NKNPdyN1w5=D*QlB=@8<$0GG0EywG~N=SUA`UZmG^&o-#Jl;gjgdSO=pO|vWAeTV_bOhnclqK^VF@zFF{)J8fMZJTs1rZ8+CA!NXBi#utnmlEC7)oKIgGEGFdWuxCjc06k<GeEgPKN70Z+dgrYlg*tt=P%Af7RNSkHEVK|=ZQrMxPy9VF^x&}OPKNF!|ey_Ki+{+6M~6h$U%O<U@_^laYz*lE81O{%WqGZ_Yol8{sW6bkA~TQPMrJk&VO!S7>XJU^x-CPn0O2vKx0PW4cDte1SAve(5%V4A=Hc8;&RfBd)>6rOj=~1EVizKxUkH_)mojom{Z`@uSy5Q0t*pZyh+yqk)Li}`vk5};raruZ{d3Q)6MmhaJ>qI%>6q0O;nwVs*_Q5cl6t+TAi2bP7Y6j<<paN1ANx5<>ckGpC#=c(s%)AG}gHFF<gI#3)Z>?Yu&mJ*Jp5j4i~I@>r1%)q2U70ufg+cpCew#(8^?WYWIKr@>jq9&2N*125_R18=j0h%+U#l_knVogy$-6(|e@M>EgdiP+?AC!2JNwwodPcx@S~QqX~8igstaZ!@s=vTpI-i&PxKqn;S6CEC%1CUtzw;2UmXuxDLQ6A+uXaKLt62Hjc;{Blh<Cnd`pcX52sCO?$Pva#iVaw|^XmgS%qSf4=|zru^Pq?#i#dl?Cy&oqz53j`y^$@zP4ar%f>a23Y#v2&HP@n9^^gy++baD@y&$z@mb1#>^vb98EG`B-ZVR>{RyylYbnX;?K~4-mkNzS$MUx0xuc`x;jBv=6Icc!<FxI+xsw$I7zp1<?*;EE$Bfuei$`L4}-tpVKCzs6pAMie0)T2>p_k^w&)p*l-{VShj`Izclv>aqnTuD(ORGx<vGT1-VMUgqGL3vj7x`3fsNu&V?RY7&`(g9*Xd~!^yM0ACi@ofIxUO_eu_*hZ?7ybq#i@}SxP%y!tsU5`Htnm?!p`rVri*orFV;H{Df|W80S8%=$6GN-zj&*FC93vZ|}_B+5g#p=r8;C9-Mt~29RzwyQaO`4o}k6?eqj)e69Qm=Z=W#!1o*UhFp6xw1>s%p!*2C(QAtl`SdaJY5V-E=5)!c!lfqkd_OEuh<=*2lkB*o5Y1jZ=w@-!?<{M5i9Ba_681r*IL#Gh^2lkerzXw233-8uOaLkgeT&{Q?(1c;td+HL6pDM`h}jgFeLkK&AQv$!bnXtf|9%q-60C-Jqd*Lunzt)=UlYSB$0d1yI3vv_ASdkhV-SY(@4$S3ju4$L2tHQsUNkZ=5=dUaW2apqnX$ntDi${+*LY_KYs+VXDjz6es7EFT#R8AOLOr3A4u0J-ggfZ)aS5wy0{J-bRcnF#f7I80tzM$CVSoXYWuPD`uDVY}NnI7KavEa~fm0(A2u|-C`iAa;*fL>gkKlQNV~>GQO!oon?8!Vr-q!mCKizz1L#rD&BSh<wArYAqaW16$u1nx;f-;xRbaacjO_-~9DsHwurskutKn!j&NCcr=Cqh9SrgkUj>Ch-7m$J@EH|{6dQrdSjhQ&_5HYBxFJiT@XuCq>`w8~j;^hqnbDjLBAVr;=G)*>tz=kuiUiV7DhU&(-}kgz)ZpsUN%wjz5qluP+j)Ca8sR}LasT<k$UX7rq=P1|DzEL3LNRLW^x8J8PLtKu|<84d?kFL#2^F?+$NeL?9o)uiC^jkBY;!7(vy0Ww?C(?Dq}O)?U?{sM`DqPNF94>NJApPjEgu%@&By>hhKN(FCq*Ln;Y&F}8&cDmSCHa+1nP0`+d=r}q=TC964pP9CtxtC6t&1H6VTiDkX@wqBKZvh|+Hkb$8EC;u0RVZ3V!qIkrMI#$a*l}>p?$X`7^&mS?#Ac?AI2h7U#HGL4%2Q4oss_|iMP?$$d`iHcFy$F@Z{pz7*_PlgFm0vFY1`ui`R*C(jckJNmer*!A3W7LA#+1CNl0qGNT#QqCbV~?Zq{P_93LVY(z>fObDz-)cwF!bef`O8N>;4$n7b!XyH=CcWD|njymr?*sYAj8OITUG7v^o&A#+6U?$YV)6K73MB7~j(mTY7M1Z(3|OCw85TSpp(fA$rd4xhAQnk|}V5-Lc+v@4h;pwWIGQ8%OIA<C}tL_qRql6lvAotM@KTB|{gAT?wmuP4_tpACuogh|{8u+d4B!d|ucViZq9pz}PWoI||0U~8Qgc7H}z_=<Doi?bH`XKXTj5|;@gL;mjsEFUy<U;9|nYAy!Cl?B+e432bGAn5>I=Q<XEj{Tw%YK4)jjk%hQx`X)!y`+>}WW2gY82cDjr515DwKp3fNW_ihZrtf&54YKN{c@JJjuj=R1xAlaJf2(lD&N@yw*Bi{<vkfnh;KeX9%b<PUtUfdQ=e3K1Qn0<M`eYH<Z6w-VC+(_mn^5F@(T(5f?kkZuxe{0UJl^JkToC_oJL+5e1&`O($}Z=9M%MYgoTp7qQv4;%}UN>J?}($I4@P2ClI=`R(XVht#<Tb+@3pfRQ1j0c;npLRh+l?@?3^tX4CAa%a4}X6ls8-_7rKPZ?E3n)&N@+TjiD_^31cmAq|sl9rqXrTVgB&k?JC!2EVHZyZwgYA&FaWSySW=xbANZ!TGj=%W7ef#dO>{^w>yssDV#M(^Xc=6HP4uq_Ij4ZVJFnY2dH|28S(@RMnbhpO=B1u#U*^BdndoS2pM>$?t?LTl1RAaKQ9!dLEJ{K0pCi1x$#w*1S^93D&@Pvk<OG62&lICuQh48$Z;0&PIo`Xpv$?jrw%yWCeSZ8F;}loyP-ltzzy8YmFZau)U)l+}LVnjg_Wb`4}b&7U~Zjw(_&g&^asTwGBQ<b~v?Tbw<Z1<ca#vU;lFxuFE0~AG>R-?~~|<yqJ9^u6-_yY@bGss1YD2M#M`~(UJxqH;Y8b_8b{5>}Uwc1+VE1fxK#UOFiZOBN0@J=I9g~1dT&c@s@)TM2%RM^p-rysGCE>u)>YQts<YZn6^8MDI~qtfa0Cfb+&DIcFovdHR?mXDlO_)NE<%VN`~xl8|hcXDvxlCd8)L~W`|@k0me#<M=0CXF%{%8YhL5&5cP+w)ESmqZlXj56##B%s7^#Q!9&ND8hxE!2Dm@pzjp>WnwA`%+E>q~X?>RW=#4VK|NHf$fJObwGpLBwn6I&Lca^7^7wHC5m5X$}Znb5d3RdUe0NKVx;xs|L_TAMT-4H~~KgVbbs0dMBVIShnPhsA=e`g+C%9+<FH^%8pu%7COi|g!oj1@h7>83clH}sqj|HQVuEQO@MSc7tFEn)}CKC823AHcG?CXKkYv-Y5(?E|}>z&KlP6mMmT0E5a+Rk^ndh^}&PS6DJv7-!Do-tU{R>?wr5O5f7AW|avZuXV|BTUGJw96!MaB|}s8S_i>1fn8IGm})4tJ7gSLGrG&Qiw}zY)+W?T)R3a<%HK4>jc-Eo2coRzJE&}y*fzz7s4$j|@`vV4AxO?54q70f-fzJQhpp6M?}1oPk*Ve~!Ok3_s@_Lpq3qdSh3legGMq)~bqaU$u7KfS&lSW<Ukk(z&RpMMM$kaaR9N_^8jj?5=o4-1CB0sAN%r^5-ri^_e97A`c5?2d<&b*({PlygaGite&F!;S;Nv1(=i$0AcCwC~yiu!r`=W$7hEw{P2pH^?3%)iGnbV?!p8fM37!KG=khZas&(dEQndcQgL*}&S=md)R%kgRn8y{e*R#LHr%tXxezkGl&Ti>QM8({ikPsFpm?N+{>tVLc9DdJ?7?JE~9T@dX@Tb>1e2~<V?Qe-S%`xt7lTE|vPU&R>S+ff*>H$klSu<fIyQck~g&@#qIp8J#*+30kSW0O7amP%f*fng*bpdyD+2ma&QMaU~z()DVit)*q!=&AE^z${pM+h@rBuWI$KSWYbaS}lJ)K{wK7FV4~<F`Knjs{>aG*;2IqEo321%dQ5pLyauTt@8$J<ukARt#$Ngjeg`FfaIGr|ERgeohT2S;?BDla$BDH=itQlf&vLB?Td<4fr^bVaZ}$$zGs~jc#kNOt$4~w-13q57Cq@9kd-O^+EtN*$B#~8%=~L$(-U|xxJcg>rovMkzRPVkbT!APdtoc4_@e#>9wFhK0HJ|kKHV&|U&3O}1BxB|yed8~R>I+XU48v5P~YCgY8WSl3UV_$nN|6UICtT#@|oyDL1bj697Q>k#YY**T)wf`B);$z!7#^RIxty~w{eKyfVfZ6hYDTM=C#y<hey!>wmr9pm|`V(G-5W0EG9V8EPikWSG>mCJiT*eC{!C$Ozr#(qA+w^nY;_1eH04)j<7**rJy{qb^@<pq3B0?*jGXcwx1~P$~mw-B6ui-xgns*v;GFA?<#JV#Tvvsn`*JRft$9N46*c*$9|y5ONNlwu4cQJW_>al`NUClcur0(kz}!0McE->JZ<qKZ-R-y_6U)yw=mG>dP;=luWhtkS*lW=AUhJ?>FC`>mN@Z{F$Jjm{5>C2SP=^6{*Yy5mY!~UOxCCRp8X-rY6N6`lSDRsSC-O&)AMC-1ttC7kh7~Iha=>u=;vUNx}nMR0=PtN_>e6|t*&M?Ju90idFp$;=v-PM&`9pQS!nm`+QNk~jT{y4o~U>7w1lFtGhEQpU0E8$kj_D5#&4a>t#6F}68@7}3r^Tx|H1#lu3Ap+((wc&a<l8={EEnTL75?#==_eM!!1D_eKvjqV&3e<7r!TtbbxZDZNY?vENP7O#<;36q>5_2Dv({<Eez7JD%AW}G=2|6TY(s$<4<p>(nThGLa?|`+YY_Q#I$-HvdATn6TYJNvMe-t*2vC`A;xk9)?~*kzFi)E#-5S9;F8=JeFHudZt^@CrXZE)4pi`mU-I7`QNpaS?p#q33#4s)aSw&O5DryCfB%;mNnQh?F)Jo5caZV<o6L=<?K;6sI}}!`oR)nSBvvDEYx~RxY!`dZ(<oKo=RL<A4V(9#Wu@Mex9S8gspMx`&GVGj*_Cc58?rUd5os>t$j5!32;AjT&(&1`?!13PjwP8nbc(-~Gvj$HXZNUYlW{U)q3~t=i(~qO`~f8(8zyQyv6mr^4prlw0V6js0<!3UDfGlHA(D)T$^_4l_B`)UKe+@WW~2|!AuwTx5H;qhxgi^-th+8vPK(Uq4Z3H|W89l`jpS125Y&mDYW{Ty>t)8KZF}Dq%>J7g^r4W?^D~EI{MD)$0^<HXFV3K(m`8ln(`JzqMgs=X6A;0Or$S8_KB6a|2GNI}G|@cE;5z4=6fjCiQN{`*Dn20PJJqlE8Tla^r8=XSqWk+~74vAs?a;E%;b$(*hMN4Hl>BEd<cn?Q59QdeJd5)QtPiIWqk^TU3XXdQ*2=>)!L~^C6Fr(Jy(dR_aL(U~m%RX}9q#{-9~vn*^^p!l5Ewrk2^q#Se@2&j$Pyp(r=`d3gz`BoU;?qY5$eZLMJ1Idr#t=+#*R}k'),'Libraries/Compiler/to_ast.☾':strd('c$~diZEqa65&o`UvAIuNXDdj~HvxxKmQ**WY#Eje1aOVTYLAi*zLza`&px3jAX~CxTXm`zOIFgjwQM-`Tim2561$C)4+QeHzoGXF4D=6l__8E-mwR_sfeO0g9+#XM4rk_>Aral6x6jT068S!R`smELx$_IYk5Gl+tE8S_5?5SrxzSz>8ZmM`RH?YG>xt2m)6=JC=T1$|&ihldGm~dw9w+y!8Dz|HJ>EHY4jwNe^fPDNaotNJsFd?E37Vs|APH=o?X=jGi7NZ{NrcYKO*86u=~KGl(Ia|DuT@W<pFHCtdY%4}J_8<a@88?*t=)Qi|KQsSqpJH4H$LPq?mhcZFg&9Bbl3X@NP%5fu=2xp)8NNiMq-B^AQzpf!s9dg0I0EHjQmI0F5F6bH=q1#Jq}4dVvn5B0_kW5@G2UD0UMTM(3fm8sJDh7%ZBC1nzU+o$w}IN5GM$<b3p$}f8g!+vi(}N-*{I8((>b#Hc6^%uD8@CA@-L#jRuI4gez69R<E|W>_-8KF{zI6A28*r&&5m##&Xn&6F~J3^oct$;=tbk-V;^yzN2?*kfa1R+gC8K3*r?VSLJq(E+wERwQFFI%(hS?XfD<Q2bA-Y?oB}RnBGOophfq^u}jigp$k=#imQLZh*$I_qSwGQ|CT4mt@j#zPT!=q%cf0TIFHb{=X$^W9ow=4y3Lw5bR8Vy*WIy6wm*`yC+&Zq-l2C>8mQv1Au!00Z!}@M8sj8L5~6(fq!bh$$Mxfwlz)0=7JUHT_rWDk5Mo5Z3+0~36$&HnEXJK^kmi-W0|O)nPgFHqu1EwMznSSBzhnqB?y?Rg0yr%FUfMacWl7bWo;h{lbX8lMl)Ap;6pc<88T*6Dcjz}<UT774Q2YW3!prs6vLjp$LZu+czY?<Q7(_sRHPuz!16cQGKaB<7`cfU&Qr?PxMj7rXX(Eg5rq%$a;M7}=2!Jg331d-&LLVHSgqnN*P1O^FTFqZ<w8P7>W%Uwc{0IVs?LCrzdKJ<i-`?N;4xCXfCf#ylBv>^Ht9BRTX0}Ja;NtGlzsUAbwhxfS2d@L3yvjNcY(bn5!}Flq79f<4nM_Gl%@V-F<}qWgFClX`s#Qm<)4zPhZv_lTTns@84HW)F>X&^f5=~M2F<VKhK^5;)rGwOd0zM6jPdAQr)mt?Pjk&SC+YkL34*Lg8C0nSmTr26PT}FX<YS4@;N>@d>uCCPM%OX*U2nL7&Xz|m|%vb~FceX$i-*Tki+3IcXuz%ynp8Bz8zS&FP++Tx^PnlE&8&uKvX~udE>1VFkx#zG$sggad?ovtD1^Z8wAn>&J?yPUnT|w^?P}Dm~z!rP=m0I`ybu06n@4*)8j>Ont%|@nb1?RLFEfd;xf>sSe+9P_K{v#d228^e#GTtes0&+)w@8+8Hw|CvGPwC%9xcRZa(h4Ds@#z=xTAk)1n5SjL&&_aGs-m2R+L6-F+-V>3W27U?D9?rW=^Iys`2T$O>Nb3~;PZR<-06Mwp!e0o-sX01bGP^6M(<BYy~nqtzRtE=IJZKU{rOtPELiCzNU2I<`fCfOv;Lzzs`LIsx|ZobS%UVOFWalnVU8ISAISER2_a!SS_NbfzW7j$5W;|2h9>Swj8;k&g9d37l$TXYD&isCkRm?S`J$AaTP-$oM$YY@X5z>?f2g?5`;JT@&4poiGy+KS`PLmftII9^-4tM5xIl8TNT%M=Ac}CShDu!TC4J#aU3uxI6lgNsa)w}4Z$X-upfRtM+4I57MoND$%?Rt(DzWUmRU#E#AV;pag8OSQ0%iy9K$hSjL$j3nE;0lngBcQ>bV$n)^eic+Ek6?+iV%TH+%xBk{Wc3#Mk|^4n?9y1;aQKC$pnLL0Yr>JIV8zaHIV2L_b-t+^;u1tk3HAj8a?u9fNN$ojUXA6s&iSAW+bAtQaeKd53;d#4g2jVmnL=DaSCa7B0mYpGEU+W<bnjsf=bIIf;_%&77xjw?KN9Zf?M!9NLUeFn&=m-sB5z!Ub*?W8yQk6-IWzNHo%;!6w`(bT#A9c?X{`N1*T{@7-g`Plhcu0yf`UJYiVlfiB)E#wj@1DV4Kq>j#v(R%Ds^15_VZk!EGX`pxs}xvlnJ(k1v^NkJb$=LNS-?Gx~by1CasV@m}id#+isX$jTKs`AXvBA!<rinsh70x!j<jFsgMz>_fHxb<Vw5Asj+3+K&8iB>)uY<4Fl7t$?grM+g_j4P53+DUl#v?#l#(v3laMvd^iK^m8neehP=$+9*rLEvlBOcW71<;l;R74>20&=_xNMpzx~>EGvc$0U4>qSg%ZEqec*gl}3)dkOs)2_&1#(UI~L_qH04)1C|(^<<KgHDuF?pbSIPEDjB=p>O>Y;dAkdg6h;h<ye}B?rm@iLGF<?D>F@b<H9L*}$GY~V*n6`5bJ`wzeOovBEpBLxDjY)rXeEBwZVd!>$fk|Ld;7<<;9t81=nCIZHs&m`t4&adf1)c+d9~(>!HP+(Owbz0hB?OS-8`&VqNor<SwbPr$eqxXqyxtYLxYbA{)ZEQo%MmoCS`Kk#dPgTMj17;xTg-uL_pysd3v1U%7j-8%EmI|OignB_q{KS<W-&e<@S${I>x!yQ|V=2G8;HJs<@_-jAO*r*bjq7V<^YDIKa`<S{lmY`3tAcou8YUH2Fd>7s>XQxzp0eZ00t7lB*MRhNKUwG6>G^viz`4!cN_azF~)uRR}!&khimpyMv%NJ?Fl66F#?iS|0~chy{rywdaml(5A=k%Xa9NO{;p*46(`%$rXmDHC4fo*X{mhsiz7jbL>pfW{u?ln%xrI4RMr+>ygi$AZAxAkA}ImnIQ!7Rfxt{pb%%bH%Z%>oL_j)yg?yBJ;t1(zR*bvVM%FZMBRe>Gas|t>v`Wt=7qJmBdvI%1?v9=5|<+t'),'Libraries/Compiler/ast_to_py.☾':strd('c%0Q6S#K0a`rW^x(~_fV(>V5!EXs&sml*G%IKcuIt>krD<C!*$Jf7)Hw_|$~B6As=gn*6h5MlzvA>5FV3kU?sCGG3}hWK$GvXSx!_WSDU>SLzIurE83XR5oazpK8x%A<|?xG_<yl<H--TnvgvW!$Sb0;A$PwR&T`SgriSEq9FKtTA_bvfe1m8Do>xiXU_kdYqmb-1leVI5_&t8-siH?sptQ%!WJJs041qH!b^MwLVg;`oyw{X<C+L^Vz$0@BY)kp4WB_>~s1C`ggqv?=f(%_Y>_M%VszC48m}TkgZ0qVOhg~`3n7zp3N8NQMy1^h=n&!(_4=3xh1^$89mXrYd?X}r}QQew6S__V`hGTW5V4ya%p4rW4QPuAYfN3SK#W+dd)Qvod9Ureo%JCCd;YNW^ckP4L6u*)DXhmqi{K0ajRvx`t7UPZ{f1+R`Jp7BN&(JwV+btxKCb%8zT+3I2J`WQXO+j)mk%@>rdge$|yp3a2|$km0he~VPnq7+zecd)*DE~*E2Y)R4w{`5>FJz8+&#OJT^%2JUvnX4guWEJiH00f0;Q2<DfAe1yuJm7=)gsb94!2zyE$`=UZ>R_~Lu-?cBLz$CfSY_qJ}`y79q@F8aeupbbO0VawQJgra<S27tfx5+eNY7!13*a5#@r+F4-3FJQQX50TpfA6|yx3v4)d9fpkSjk#+uEY`}=+v~SsRI3N<?i|XIt=il?zisf#`4jlWXTy_hXuw0Jv5INS>LC4Z_T@oBbcP;*`^P{(PtaL<64;-or|1Wum#67R^b81OfiBW>bcrt06%gwu^aAj_N-u)UF44;%>d)yK{eoVlU(##zI=w+}(p&U4y+iNPd-N;%HN8*2q2JQ)==byieMleCAL(QIgg!NqioJci^M$^@?%hjBwKzUfE}}^9(sMTZS<J)F3jK~mZUQHyI8xg6T3>H&8!Q4b9h394Z?Hcb+BZpPAPWYE{v-gowNk!-3KfNe03Oi01Vnb8-cLL{4np~!-X>yjM<4>huYpJ(AsWl>E8q`kq<pB*0^YLw?0D~xkO0A83R+9f`b^FW@goI;{Rdi6z>MrTD8mxHCd~|l#T?g3`cT4zWwqEB2YR4?aI-*DX0vHWK)IgCNwD6QVio~>P8U#ywtRCc52pFxZm0iy)9NHswqP?xErMZRoLX<%as86x2My+!L9q!Z)D{$^tN{TZ@b`(Ho>%%NI(@_?cw+0J{88`kxX%#Y=4Bh~?xD6ON@Fabv@%M>C0MrcZWm&h>e&T<uX0TIo!id7bNIdeHTJz57W1%Wp*L0F1ZP0UIeHw-UW%u{xLLEO3*=>^3oO8Zmo;sB3hGm>)LfrT@el^aMM%!J>~{~_z}Pez(Gz+Mjfhdl?WgRH8t#+_9?U8Ff#XdhgUjGX9^0T_1^Bb_9R_?VqXtpWtZvup-p?Q4hX*D@K4$mR-U^ID0Z9M#;>UCFhu%Jffm6p}8BsYt!4(&84fPD$Y7D+ydj&rv;QGovrd+?FVGBd_S@4aYl5smlMG5I;>m~)?9jLY2n18e}|Krc!t^RxUvbI7X&1P@>ymUP>u_t9BvVCC{rOwwI`Fuj}Tj3|lR}mJU1i(F4FYX}NH43p;;Ti&#&(iBa1;KFHB`knVwbe75Eq8cr!8L=d16G=Nfj%Z_G{Nf&^visqiFZSty~S1chQ_^ywtytcM}jv&fiwV4gMeZF_VwBg>GB8>?0!VQB~qNWz}i(53>6bxfF%b^bK=~HWK!v;E${S(L#A7^bU|vCQpH|Su>ihpW@za_3`tw2Ke69);`fsL6=GNf3E7(U+rAq>COfW@)0`j%hP~miM`WtI`v=H2NL9BDCzxY&q84S)p;iZYH91(xqTR)pocTC0l<KR*pvkp`<%0>R9PHPN3z+cybJ2ki;CRJGaU7FI&9t>wK^~-3NT|7R+slx~s3;>u`T;k;G{>`W65ckz-5E;n<RoEMN`1hHn9_w%N?G>A$j3xE$vZ<n`|HKCKP0?f8lACe_<=mzC;_N&di1#f2Pq`5UeaJKJz%nxH9_JfoQy&a3OIZDC>Rx&cT43p%asx&t9DmOG9FO^O%kc=Fss%96XL{LB;0&+V<l$Ew8G0!QM$CSyPd5M+Ey_L8qaQ9?I<XZ@DXR+o)W2~pt&YV@f|ZaXDyqeqqQ<i4Sm`!2}937!f;zsSji$m&mq#uQB(YCrR0)c8|!kbMdWOQvfqAq_;I#yT3Z+W36vSlOTC(bbmMfUG}^%VdjDo{0;A{u2T1n}ZU!l=`$w&jCX%95J+QiC!494d%g7P+M;PUJc;GH8@<7rBRS2p|at7u(8u4pPp;(m3md-)$uwwGDT1#kOwurJZ`>B{S@jkZ_iu7l*c-Pv&dqLp2Dt^~cK`fa>-q33f&EoTgn4)Bw;#}M+uFw^FKVQ({M^gYI=A_j~LZhG_WmA9v!(u4~?@3zSbx%!V)Udz>@r*SbEhHGTHyJ>MYI9ha^~*{kY<y~2IiHr3#eohUo0}F-0Ifv4_Av2G=2$z7ZHiPAl#B7fi??Nwsxm1+eYpoBFC))@#3y85@NTZ(TfhCjnNp*)l{iM46P`tewB-#~-eBd55<4?wktv0;9||W}-K?xzrcZ`3gdC+a^rRj;3=w*wF()TtPI?69isrjUG9gOv2~^l|c2mM`+p#W2MoXpV?oU&Czn0obA}rwx%R}rW7|Ls^idn*R{D~1WR*NcKW=qM6d{v%dSAHdywfi+*b)KP@m<@^~k6Ah1y&SoV3T=mKjyKv$w0L_*2)$YBNixW_D5;7_jivRqnBMc&5~pej>Yd|&t`oc#$+1pQr;tyi=YV2WhAnCAWK|Z-^J}qsTkAfBJjPPfT+ZU$>G8EQR5K{Nm^9nzIv|_zIz7Xyf;2|jO*whnZL0kSUoPI@yRB0ot(tZFveT0_wkwoDYg+vZ^qi-kSgQS@yo|QlWOYMMkVc%HPH_8a6{{255^tBT2l2ouawz>)L>u+2JZ)|)Q&NeN?$uP2GNxK>s1dJl+vM~Al+jqPWexYGJf~U-c+*8<d=B+QT9V!?&E1EMaTqPrV}$SJ+KNEFEy_1U#g?h+_zm_SNVUVT!`-Vo+`PYS%RQ#H760vbijC*9Roz8)`Z5l5Hm815W_fWYyWWo#vvCic(U-b7<Gu}&ADaZtSYB)k(~!1f94)TEN|?zs&o}gpqtKE*o=u<n9NUB$OB9Vte`s3uiLDRORoBf?El)fyg)if7iRfT!)j$MNZxWL1WedI3Cg)-==h9vl?!b!0(tLIw!Vks+XJc+Aqgsv{Y)q1qhbmQ<gc9SOdniF(G#F!x3CD$fO0jXzr)v3crACDNl8<wGMV^=LR!LvOxvd3Gv8oajn}u1D=!cpb!fg?RvMDO48nz-j(OSHv`nb1w@y0q6awkM1DqDc5!h2TP!8Egpc%DTnf!nCH-JFbeXLL?2Nmgp>hOrQN91%qu4NP2>w#gJrm|jpZ=h32-nQzWxHkrH?viT-w9BG!PKnMNYof{4Wl`vWN%+jk7i9zKeaw-AgOWb)~xxz$Z$f5^Fr0G0>5rwPHYsorBY$Z3T#>BqyO<uCFvLLz{X>7$EA<_gt?~^bB)P82XoRa4kBK0U2N0aI}Rs!c`F4RtL`^(I!^(((zJ{?_2UG7|2t?r`dxwSHh=u5OEm1y1U1X*P4NW}wva)U~h?y}zm!&10;6EDt7dSxC~<vFOzAyx`zK%R#Zbv-CyU*x7vnxwCJp`V~vBeLm+lRH&%y+C9LeVR6+C+=e{jy_FEWL^O2-D1pV7)4)!iJk!H;|mc3@t-3%Q`3Xz-|)gu%RZE@*-5<;BI)$=9y=H)l48lTo!C6isAj|&Nj%XQ9$yq!FltiOBpY`_I)>p**3>Dc#h9<ue76yRjzt=N8A$}N;Ehf--xL<5;tM>XD+?|+wFpt;&P*Bo%nATIJrR$l3Z&C?No&PLlCvyHz!D}93s<4eh((VoP2m|OW+eiLvBeOnpUAWall{JO+s!_4swo)>2csJWP1}9am5(+&($d$nu7Q<$Oi4~Dd9q(9dVpcbQs-=x9PBdVpH<dk7XU*MKPATIpK7}C+1^sxgVCL9SyhDxK$=M}T~@I(X#5xrTis|c7j%f7Sp$1@8t%bLy+#IXFFd2hpnnhdV6Y11xu#A7`2s&6H(+UGqAq%{jHrVi29?CAwxNL`oG>f|<zWivfs3?;hZEeU%@uO(A_L+s$F~K%xXmzv3gK%x^%@IN5(Q&-yy!`G_r0O`4UgR|fq2eyvE9kaduZfDWiFB_X<}t~xYc$LT$fVSE!G@2Jd>!p4fU}CI|jGk`_~cBg2Q=j#ZdR@G01mrwN!7^4L9W=9}^xC6fV(gn$5I;hw_D}Q6H0e6Wgm&mcaQbmdlP;_fz<(6ngTZ_X&A%^&G&{a{yAYlijfRdC9PfVqrz=Uzz+3GhaDu^TTGmm&H0}w{>cpc?q5zDB-AB1!`82GI-WpfH_GnGk+2kF;!^!(7Rm4WBHL|KYVqQM~X!U>0M%?;)L4Z*`Q4Njs1u1rn(XJ5U$(^!3E;Gr1~?KHnA7=9-OW7W{G35crU0&j>NJpwtF^ONzicJ0(Y>rI@nCDIPN;{6dS&{*>F9$5L1M`DnJl|aM$WFAx+NScB%F;cwv_RMUkYO)PxAp5ROg9qyJ+^tYK$sR&Cj%m1@<IkDNpGs_Q!=MZZ##K)q?m#?$g4_P7anCDc}vq;5-xEaltg0b|@x6yi3L?i<L~rt^O%0;KFRXiOW47f{iy?ui-$Nca^W11Oop@U)g~%Ur-@ot~j<Atd1Q8Y_wW>SZ^N!IAGoVf>k_O^hQXyIknq{)+7vVy<BHpqVG;tG%z77C3_w^Z~0oAFBp8OPX~|59uu7I!Da@MgwZH3UVDBs@H^ADz$?z7@Pv6Q@-EPq5d(->Hi!4E7d;7A^Lw$DHAYlHN^W6m`xU)VSJ!}(6r$Tfc_WfJo~W'),'Libraries/errors.☾':strd('c$~#pTaVmC7Ji>!QEMquRZ?l}>5LGD1|^vxATEg@Af!&q@_4FeEV}K+_9#6fJWL=+1i~d31iL^Oq6nk~c3Bp7K?yt*@BD}PC7e?iU%H)4KOo_`v|V-T+|PH8J04HctRO`eMq)jTUgnutqVf%S`ONcA&>+COC!aZU`nj_~K&exRX%P(5Y#bI2<C~*&Jsjnfaq2jXF|N*?K0_JnQ+kwmgt5VWxSdSLlXxVu2g1AviZqz){FzLFA@KbZI8Mao=16oO*v!H)sF{xPg_&-MAsNQWMv#lBh|>gx+>lr09WM9eM{<{kJ>U=L{UridJS0>-lO!!joRE^9b%de8D-*?bmJs!<{*}tp#)-}Z)T8n}d2{6V6v<O-)Mb5l0PDCMHI_ZI{CSgl*)BJ!y8~nO>e|!PV|ctWLMvjn_~YOyq4>u`O0@{`DA7JZ{v^$aUGMek8)33Rv~cohxq+e?6Tp;KZfD56<_ENzJYtWyH6b_aLfo2=n-O`W-0+kTEv0VE*=$?ea=(B;jgSZ;ScRh^1_wcS(M6fxYh*`MrUhdp&Q%sXn<m0&2nTdj$=`ZpF4CY+lqN--Y>QdFvPv<GPIz!?*-d>=<?(j1A+jJ7o2Y5QGcMnhx6R4Y?}aG@xRn>>XY$g?<7a7=G<*~%B8R-8MLn0QJX&U$Z%v-rUzEgErXaVPk1A{P$%qzxML6K<6GDhWkS!>^C$GtC^IAt+Eh;1J^;w-;l~Xz(4=aHjAs7r;gS<IHG%LmwG3GDvo9BvtK8houEi~SOb0A{C=B)&-Wl-Jfw!Ul;uNM8c<t=%U(tflBHgn|~a1lI}=x9B~(T&Pq?G95u%S90vVqE6ZF(V3YyVb3x_muZ%Pb^ntUgLx}Fu61z0Z%ilqObx{SUDgHkof<X-@+EOhI3Q*IJSqmuq@S!O&{nVrZzBG^vY)=hzJKx)mAN9Tw%iiJXs1_TB2e)0kklM3fhgr@%l!H(m#~{;+fyiFd#0^AisE3r1g5$q^4H;NH{=bx+A}lzd&IBEx!P%Y>7tcD7BD~SE8o;Fi?LW-}aw5y-L9+9~fNgfs7mS5>=e}lrgI5_{kTZqotx3<+t)0S07jX2I@4nR9Zn;)LD-+{_1O7UII`4qE!7F$?nS6!F7h-06JU>&&J_oA~Iua4aXGj`Mo)J=y}3~4;SB+pZL9UbfNNn`Hs9(hvjGj&}B|<3ZTn`=&AO>O!#q>3MOeDBmC!vDL0?21FWtCv%9Pbh(_fFkycYL0JnP}>Uu4TKBeum3)m7CMK-&wm7hW~{=SPj-x1}lZBa@RI$srv$&xl?H9M7wyO2NsnaL5qU$b1TsGLxCFm6`7!2t8DGG4m`v-2RASht`iojA!wR#2BW3(RJR3e{Elk@nJUyg~Wj&}yUA1laym{wOck4CuQYk>3^vY79%R!lAxG2K+Z*HK@+&`P!&TtDp6?&5L=L(?yDjI$;<(IP|(J_~RJQ9ei%MGHjkxh(8<`EnOW}&(C(qdv`*_Nub`9|CDzv_+}+qDzkMLfnRczEUTKVFV+Ec#u^8h?>c@v8z*;sG~hMm)MR^XtYr=N0$krqyBV&$xv)GiJ^3K*X4x3M&L5=L-eO)edbDZRT|m2bW{dc)*&bCPU6)@{HD{^e0srk`!j$cAuC)TrKu=UaCGrTs>J?~IP#a<jZ(8)+)H`u*+jUn?_UU6j{Px|W4-Jky%y99+6UWrYs$RU{Ug&p^4IX0S3w;ph!5@^VW7~;tR3L*+TPI`i^sn+~syZTeihq<n@oR?uzb4<KO+8r$=AyWu&?h+_n?a5WF~}jvMrNq)0W%g1nJK(zzUuOYO0Fd+AIqP#T?YC}%TSeDj5cgH2RN*KBERe1SLFt_Yp>!(BZclDA5_dS04f6cR(d`VS(av)+_$*a6jyrc1(b_vTm(_NA$p#T&ekXxYO@zWuyu`Kp6fZRoCDsHKS0k!fvgh*<@YE-U<oWbwU|haX{<AhM<NNw&@t^w^GOv+T0H~C*B=F>%`6G7DKhjJEfs@}DL%kBvaYnROtDDS77RPw*qj5E1M?loEdTT2=;c}FL-p=G<Ox3vGtntlz8b4eY3rG_jRM(0QviH?FRxhL0Ga__TsGJAvxWLSzWCv5cR4oEQ>+6651>U5jMFqx2^0jF0i>obUZB92@+MFo%E_VJVTWpy*^pzZvD(0$@E6z4FkZtuyzDDHDOVe#$PIa=Wi-{JY>iV*6NE7L_^djo`e+Yk9hx#Q%2gPqMNyiWiGw=buIF{T4jZ&|{2<thH@8OcSHStemP|RTu+q$>ns)UnQ>yyLYX%dbF*T6nM_tw@!d$FPBQe3L6Qf-1-47?RI<cmpFwp|!gvC5Wn~ZW0`wBDWzY>8X4I7LrOH=^_-N~`M;=&+Oww(mSFo||FEamtvbXyOomwNDVMgCnm06rH%t0LPW^J?KFZC>@2SBU0M!d$6b9k@3>R<cZ#mh_jP$5&T_wU_XV(C34I*1z(scsabf2R~x{SV!Y`C#r11I8ha2TcUj<xd@@(gV5_7#l8K@Uyv!?VLtK5{#V~u8}?eBU)uj_kL<s3Wq#wgALRe`KisP}rcmwGQyKTUFxd?9=PFHM)_>)9s_Faz7Ae_g'),'Libraries/Compiler/main.☾':strd('c$}>oYj51f@w<Kn&BDO0LCcbiG{C`3A<J?sB(?-gF#;&Uf;#f<i15e*N!h0w0qP`9i=;(TJ5HS-PT>YY6SPemv<-qZj}QDO{ssAvAJCb7kh>&Lx|2^ZOmZJHv-6(WBgLD=+gsaL2xIuRadm6+`VM1+*j=wX2yE)~qh#NUGD00<+mup=@7UZTl<pF8)>^hG-CH2t#1B|6i~@!m!?@pZchZA^E|8t8TOD`!s!xi4;rpeH>rU}{@kw!aZFPrKZ%piFPVrvxu=qE1vVjNa0Kg#d{2*oBWY}?wJ23fU@dG?REPhK!<PG<I&jK)C7WW<gxYq#)zc0Qch)_-t`*gPW<lzrCJuQarIRJVw4YDM<8Ne&99VSW4{4j;p7Z1WH597=h=Y3RsU3@|WVG~xK+po3=vPWJ%h{Amq4o69vcU)rk(qw4KVM`2KTkvUlnRPmQ<zQ)PX;p!?To@{uLKjC~8pJu$zqNh?#Pidm_r5^t%rC^7Cv0>G=oD)n7atV=bk4x@kHtIA8S(O<qvjhEUY0WsgQzJ1!c~yuLVij==vka(zJvL}{z0F}h1npv#Q+*t1o4#|)V^4pFgTbu4BX40WpZMa2Dncf31j(HV(%<i@E7(hIWNBP4+Q+z;?Lyb=F21x^C$rRY+SRc0EBuf3FHUB4g5a>a(+<UE57Tva27zXj^Xe38Q<DZy&=ofAaFGzHFg*T!Bj;NnP_FBpx=*z^XCNYB#E-AO|Crd<Khp+S6~wSSsnxSu5Rzx<`Eym+#CFWAYRD@Qksk0Nf*1Ll-AB;$m&R5Z@#osXEq=;nXN&c3Dz`(J0+Ryrk7^I4VmcEAU{ZBOHj7Jl^9v<Cupp|_fogG;41y5ivurXk@xFE7A2lvkuCw6+SD%bJQ(M!m!v~4pGnk{A+9CE5qOF8oY32OLoNNm$pF_l=%{gG8@#k>HN_?7WI^ubc`5+CuufLw0(f1nUYF#)OY1L^^FYP<y-J=HT4l@p@dzL97N1KoOD)nAfa*$Os+{Q>xa|W#D&7$0!ot&>ocp+^IC>2y>+vYwamADLMlM9JwbivN>llV1$O|F+>~w~q<>Kb%&i2mr)h%{qb^FS07KPn_Tub7>S^g#6gXrS$aFoQ+p)jlZ8S4ST<hy(OHOYE-(~OJ^I^a^hb|FzKj4jfIfTr6aOukoqMQOtXySszEhM|`t=~k>BXaXVae4}Bnnb*(&MASGpoj^Q_GR%YF3ADH*x?P6^2Xy5Do<4=<_(3;Gy*%KKwvj&Y$M+p#GfYkxbIa7E<3gUIvX*nFGpcfxSH?@LLaodkr7iiZ-m26}pu{9C^78Oz04#vbcZ!dT52=#|=;<YKDiM*|tjBmsxQj}xyLCQlg_*_GxFu5S#7RgpFICBdL*xu(r6pf?m-eV4-56iq(|Ep2aiAqIH!P=$!WzwSl3Ut=Om{1yZK)L6F-l_i<l0Nu30Zci14e1c9tHG$@rI*=L_r(_@-cYPFKO%HtAnq=!B_UET*i+)dD+BxO_ZQf1G7q3FFUa-i0i=Po8n8%5dKr#C6}G6o0n?E0xtOs(v6Z3LwhRG>N?76450>86dU)&3+63l$n+s|$A3@$@fS-N0AlA!$`{4=$f<|L9oJ9tG#paWL?Bgs<r(T6wNcK!4|8v-ITfaejn-#lnEvU}pZ<qtcm8DHP?;uy6P1pmW|bNCgE-*Yw4Wq-mZ#nboC~D$qW**BsO5{8PbmLQq=Su<xZ`R?&#f>Yu<W4M3&%i%DBz?;l-jxVBD=hK{RN_n&#B-!BK-qnWi594R`J<XR!T;PUCk#71tRt@PMzBi<8!0Ke2~PVeltU;tI9f|2NPT$N*$|R<<-OpMZQ=2>raGdmYAAntx9IcuoddaY{x$sj(9|a*e`ZhbI27gT;+ODdRm%}2Jm-M3IJ!Pb`BiW5jO7tqiN;Uk_>YC!7%apMrSE`_St8ec|7b{n4ozqg2+MYHLjWY8M*H^>RmSqyp$SicD5MLo6JdN`A<H7{PR1%`NqiY>4^)0CvSawbaGwCD|<D^VQg#Z%#2G_tZ9GD`bpID@-&H$$30=&TxgjZ`@GJsSL@Rrd}4(^GZkfJh9DPxFZYh8qHWK-s8B|ijPRMHQ!wSo&2yqlL7ah_YRjBxh_QOe4@bc)JkdAJi4N>q%|L-zK1bXvA5Y;CTei%JhG0CJMGwUCIpG#b!z>C=?wAt=X>corB6KFh)b`9v4`g?0dM#*cXPq3s*2kKfgh{=xnW+fUbSlTF)}0Vr*R7qp#E9wZvFDuuuK){)?zQc$jThJ1_4Uhybm?NPF(Q%E#g?Lg7g>;&VJ;r_<cDal5W8F^3k4(LD(*schYj!VFcGz%m#}@S+;xf<E4`&2FBqz>R5uC<<Xx%PRo4rlCvGIt$kloQ@^%In2K!$3)v^i?J<E%ID~+_`TP{u^>5jrUsM6Of8{0eVGO)*}Bg<<r;PAsAkR&z;GYC6)P-pmRk5(CQTg6a9ElWkBP-C~m^A$Lr^XvWpQEv>Cn9O_f@gqwz3v&Ws1Ds9DEzWqZ{s4;TuL!?-`&3Tx7Aw>VB#cJ~xzUJ_g>$KGai+Je7!z{97{~PP6$eDlfL81RnOq}6Pd3|LFFt}CT$Y<B?Wk2uMLA**MUZM~)Emb1eBxubrJp4JDO-~X(qx%?0Ad=ML!23vT(~zi1XIb88XN0?B}XmSwZOn5H0c&hSSe+P88Sw#G8VNEt>Cw*bSp!k_#7`^++ALkFE8*Kv^UmUdZJgx;G}&hP5T1~Ay82{HENEaNW*w6*e1{>W6C~L9hlxQXo1wEK?eXJog3?0bPAHHmZEStw}~z4RtC=ArXBP;ukj8=*6dKglF?Kh3jHrn4<|5IHPYnSO4AkxiZdtXtybX?(Z1c_rWZM|O$>!`n6o(3Z)SPKVxq2gk=!;>kGsJr7dMq3bw*y6oq*;kh+ThqeT`jP-PyRYJ|oRXlZ+Si#k<9)$7w5XIaX={I~-Dm5V|OeeI`JMNzB{Xl~2|G+C74CfhxmT;|2sdQ7ybRKvz@ia%-MjtmFX_z{MHQ19+IkUdg@U8`YxYjPsMO)^F{Up5dj;>jxd{$?xtq*+T#r1Ya;R(Ylhu7kG~jJ6O+^E7OD6f{<wOxMi$9J7~g1imV)5YHexPy1>H=WFP<#p%c{N78=g3wJaS6-L|C{tqYJ{h^7)Yqn<OT1M33JA)p{ekhN*QoW@>zV>*%S2!RIimK@~2%5onb&sFJ9<w|y?boS8qz7Ht{RTmO4*mNVkseFjg6$ymL1d*fNFYb3-F^b?2rieyoIcZuV)Wf?8!aM8lR~^Eh(H?wIJk)!G^|m~mO}xqL$7P3Kb?otsKz2(_0#uH`yYYHMeaVq$p^KwrL~8&=@49znH&UM7It9p9tTW}2X{VdSc^Ds5$sPjLZ*+KTndp~yNIy?IkOv=t)p*!a?@_Bd0<x{;KH8c1W1YrtZ|W<IAJlMN`I_|bw;}R(O4<dJ5SY*jN8CiCs$gnf3R0%$q$&wS=8jAjQyL8Jb-1?aN;2ubU7J&>x|j%}r=pG&pB8Ty-zqAt3)V87n%0^wVS&PRso`|X=%i-}!eGjqLkL2*F#{IY8xZ=dCFR8`jJCs&Ep&Og$~W-exbPjAR(oNLAFqi}s5EBm9Coy@NZ{K!R8r@h)s$k*Za=*7#)BNE3wBsMh36Lr8kTnGT?2Z}?D_T6o#JoR#Z>*0lAFzc)$Js=VXAIV_--DI%H1-u(n*&tla7I*Vgh>xc8eaDaj|_*KgiF5VC#&<u&J)P)kY&7KFUf=43`=OL2JyfA#df1z$p@gY0_J*Br<988#J|{<s!IK{8$>Nz$wKs8Fd|7a0Ip{j;-|@3ddxS7u!I#6#}MtIumZ7CL`LP8=}cLk|qvuFAj`(Trp;M$ys(*_Nr(z?o<?*zpW^T$C`h`SWZf-U6EGHZws9<xK?Sp+$rOC8TCL^S|}1HXw-%(I;xa&BL+haeV(e3jCSNzdk=r5)G*Bovdniy3vBh$CAR*uy!In{>#K^Zwxj?4MxPN8SDzOnwEAI{xOKJbm$2v->f*E8L<%d-tlW0Y?~)=uSH?}cV0Py8jvNM46+1*0RRs^JCiO}{HR|dK)Pg3bHixzFe`8JXbN')})
__dir__=(__file__:=áÌî(moon_dir/'Libraries/Compiler/main.☾')).parent
(ÄÊPSH(__ÄÊIMPORT__(("cache"),globals(),(""))),ÄÊPOP())[((- 1 ))]
(code_file_caching:=True)
(TMP:=mkd(ð(TMPDIR,ÂÞÅCAT(ÂÞÅCAT(__file__,ÐØó),sha))))
(header_com:=ÁØÿþÁÙÇ((lambda ÂîÓ,ÂîÒ:ÐÌü((ð(ÂîÓ,("%s.☾")%(ÂîÒ,))).resolve)))(ð(moon_dir,("Builtins")),ÄÝöÞ(ÐØó(ð(moon_dir,("Builtins/builtins"))))))
(pathlib_import:=("from pathlib import Path as %s\u000Amoon_dir = %s(__file__).parent")%(PEV(("𝐩")),PEV(("𝐩")),))
(to_py:=(lambda áÖï,*áÑË,**áÑÕ:(lambda *áÑË,**áÑÕ:ast_to_py(*áÑË,áÖï=áÖï,**áÑÕ))))
def moon_to_py_debug(áÖï,show_ast=True,show_out=True,show_out_no_rename=False,show_preast=False,show_in=False,**áÑÕ):
    if show_in:
        Âçß(BOX(title(("IN"),show_code(áÖï))))
    
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
(decorate_code:=(lambda áÖï,áÖý:("__dir__=(__file__:=%s(moon_dir/%s)).parent\x0A%s")%(PEV(("𝐩")),ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(moon_dir,(áÖý).relative_to),ÁÜÙ),repr),áÖï,)))
def compile_code(áÖï,áÖý=None):
    if (áÖý is True):
        (ÄÊPSH((ÂÞÅCAT(áÖï,ÐØó),áÖï)),((áÖï:=ÄÊPKE(0)[0]),(áÖý:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    
    (áÕÃ:=moon_to_py(áÖï))
    if (áÖý is not None):
        (ÄÊPSH(áÕÃ),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),ÄÊCUR((1,),{},decorate_code,ÂýÃ,(ÄÊPSH(áÖý),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),áÌî)),(áÖý:=ÄÊPKE(0)),ÄÊDEL(2))[2]))),(áÕÃ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
    return áÕÃ

(compile_files:=(lambda F,n=ÂÞÅ:Âøî(ÐôÅ(F,MOD((lambda ÂîÓ:Âåß((áÕÃ:=compile_code((áÖï:=ÂÞÅCAT(ÂîÓ,ÐØó)),ÂîÓ)),Âçß(("Compiled %s %s ⭢ %s")%(MOD(ÄÕéý,áØÁ=dotrim)(ÂÞÅCAT(ÂîÓ,ÁÜÙ),25),MOD(ÄÕéý,áØÁ=dotrim)(MOD(ÄÔéÄ,áØÁ=áÖï)(("\x0A"),("𝗻")),35),MOD(ÄÕéý,áØÁ=dotrim)(MOD(ÄÔéÄ,áØÁ=áÕÃ)(("\x0A"),("𝗻")),35),)))))),("\x0A"))))
def generate_bootstrap(dest=ð(TMP,("moon.py"))):
    (file_canon:=(__file__).with_suffix((".☾")))
    (ÄÊPSH(PL_FORK(compile_code,file_canon,True)),((_:=ÄÊPKE(0)[0]),(Æå:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    (pyc:=(lambda ÂîÓ:("#!/bin/python\u000ABOOTSTRAP_HASH=%s\u000A%s")%(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ,sha),repr),ÂîÓ,))(("%s\u000A%s\u000A%s\u000A%s")%(pathlib_import,ÂÞÅCAT(header_com,compile_files),ÐÌü(dump_cached_imports),ÐÌü(Æå),)))
    if dest:
        ÐØì((ÄÊPSH(dest),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),áÌî)),(dest:=ÄÊPKE(0)),ÄÊDEL(2))[2],pyc)
        (os).chmod(dest,0o775)
    
    return pyc

def generate_bootstrap_live(*áÑË,**áÑÕ):
    ÐÌü((__ÄÊIMPORTS__).clear)
    ÐÌü((TP_CACHE).clear)
    Âçß(("⨡􋀸text_format"))
    (ÄÊPSH(__ÄÊIMPORT__(("text_format"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("⨡􋀸cache"))
    (ÄÊPSH(__ÄÊIMPORT__(("cache"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("⨡􋀸peggle3/rgx_golfatron"))
    (ÄÊPSH(__ÄÊIMPORT__(("peggle3/rgx_golfatron"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("⨡􋀸peggle3"))
    (ÄÊPSH(__ÄÊIMPORT__(("peggle3"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("⨡􋀸peggle3/gram_tools"))
    (ÄÊPSH(__ÄÊIMPORT__(("peggle3/gram_tools"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("⨡􋀸Compiler/gram.data"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/gram.data"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("⨡􋀸Compiler/generate_operators"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/generate_operators"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("⨡􋀸Compiler/operator"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/operator"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("⨡􋀸Compiler/node_types"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/node_types"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("⨡􋀸Compiler/tree"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/tree"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("⨡􋀸Compiler/tree_txt"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/tree_txt"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("⨡􋀸Compiler/expr"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/expr"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("⨡􋀸Compiler/lambdas"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/lambdas"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("⨡􋀸Compiler/rewriters"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/rewriters"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("⨡􋀸Compiler/to_ast"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/to_ast"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("⨡􋀸Compiler/ast_to_py"))
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/ast_to_py"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("⨡􋀸errors"))
    (ÄÊPSH(__ÄÊIMPORT__(("errors"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    Âçß(("c=⨡􋀸Compiler"))
    (c:=(ÄÊPSH(__ÄÊIMPORT__(("Compiler"),globals(),("↺"))),ÄÊPOP())[((- 1 ))])
    TRANSPILE_REF((c).ÄÊmoon_to_py)
    (c).generate_bootstrap(((áÑË[0])if(áÑË)else(("bootstrap.py"))))
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
    while((áÒø and (((áÓÓ:=áÒø[0]))[0] == ("-")))):
        if not(ÂåÔ((ÄÊPSH(f),ÄÊPSH(ÂÕØ(ÄÊPKE(0),((lambda ÂîÓ:(([ÂîÓ[slice(1,None)]])if((ÂîÓ[0] == ("-")))else(ÂîÓ)))(ÂÞÅCAT(0,(áÒø).pop)[slice(1,None)])))),(f:=ÄÊPKE(0)),ÄÊDEL(2))[2],(áÓÓ != (2 * ("-"))))):continue
        None
    
    (Æå:=((moon_to_py)if((not ÂÕÖ(("aA"),f) ))else(ÂåÔ(ÐÌü(ÄÊdo_imps),(lambda *áÑË,**áÑÕ:moon_to_py_debug(*áÑË,**áÑÕ,show_preast=ÂÔö(f,("A"))))))))
    if (((ÄÊDEL(1),False)[1])if(ÄÊPSH(f))else(((ÄÊPOP())if(áÒø)else((ÄÊDEL(1),True)[1])))):
        ÐÌü(ÄÊdo_imps)
        ÐÌü(moon_cli)
    elif (((ÄÊDEL(1),False)[1])if(ÄÊPSH(f))else(((ÄÊPOP())if((ãÊú(áÒø) < 1))else((ÄÊDEL(1),True)[1])))):
        ÂÞÅCAT(0,(áÑË).pop)
        return ÄÕôñ(ÂÞÅCAT(áÒø[0],ÐØó),ns={("__file__"):áÒø[0],("__dir__"):(ÂÞÅCAT(áÒø[0],áÌî)).parent,("__name__"):("__main__")},Æå=(lambda x,y:EXEC_NATIVE(x,y,y)))
    elif ÂÔö(f,("C")):
        ÂÞÅCAT(ÂÞÅCAT(Âøî(áÒø,(" ")),Æå),EXEC_NATIVE)
    elif ÂÔö(f,("c")):
        (lambda ÂîÓ:MOD(Áëý,áØÁ=ÄÊCUR((1,),{},ÂÕõ,ÂýÃ,None))(ÂîÓ,MOD(Âçß,áØÁ=ÁØã)))(ÂÞÅCAT(ÂÞÅCAT(Âøî(áÒø,(" ")),Æå),eval))
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
            ÐôÅ(Ááú(áÒø,[0,1,2]),(lambda x:ÂÞÅCAT(compile_code(ÂÞÅCAT(x[0],ÐØó)),(((ÄÊCUR((2,),{},ÐØì,x[1],ÂýÃ))if(x[1])else(Âçß))))))
        else :
            ÂåÔ(Âçß(("Invalid mode(s): %s")%(f,)),ÐÌü(show_docs))
        
    

__ÄÊADD_EXPORTS__(globals(),("moon_to_py",moon_to_py),("moon_to_py_debug",moon_to_py_debug),("compile_files",compile_files),("generate_bootstrap",generate_bootstrap),("transpiler_cli",transpiler_cli),("moon_cli",moon_cli))
TRANSPILE_REF(moon_to_py)
if (__name__ == ("__main__")):
    transpiler_cli(*(áÑË[slice(1,None)]))
else :
    ÐÌü(ÄÊdo_imps)

