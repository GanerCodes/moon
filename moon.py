#!/bin/python
BOOTSTRAP_HASH='cq-s5a_Dc5fKXRqxgthKVq1_bbSXUVubufulqfgmjxI'
from pathlib import Path as áÌî
from os import environ as env
moon_dir = env.get("MOON_BASE_DIR")
moon_dir = áÌî(moon_dir) if moon_dir else áÌî(__file__).parent
#base.☾ (9706 ⟶ 21134)
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
            return (lambda *áÑË,**áÑÕ:Ëðá(*áÌú,*áÑË))
        
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
(ÄÊPSH(((lambda *áÑË,**áÑÕ:áÑË[0]),(lambda *áÑË,**áÑÕ:áÑË[((- 1 ))]))),((Âåß:=ÄÊPKE(0)[0]),(ÂåÔ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
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
(ÄÕÍÔ:=(lambda *áÑË,áØÁ=ÂÞÅ,**áÑÕ:((((áÑË[0])if((áØÁ is ÂÞÅ))else(áØÁ)))if(áÑË)else((((lambda *áÑË,**áÑÕ:((áÑË[0])if(áÑË)else(ÄÕÍÔ))))if((áØÁ is ÂÞÅ))else((lambda *áÑË,**áÑÕ:áØÁ)))))))
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
    
    (ÄÊPSH(áÓà),ÄÊPSH((ÄÊPKE(0) + (" ⟨%s⟩%s")%(áØÆ,((((" ") + ((("%s(%s)")%((ÁØö(áØÇ)).__name__,Âøî(getattr(áØÇ,("args"),ÂÚü()),(",")),))if(E)else(ÂÞÅCAT(áØÇ,ÁÜÙ)))))if((áØÇ is not ÂÞÅ))else(ÁØã)),))),(áÓà:=ÄÊPKE(0)),ÄÊDEL(2))[2]
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


#system.☾ (1427 ⟶ 1928)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/system.☾')).parent
from time import time,sleep
def PL_CPU_COUNT():
    import multiprocessing
    return ÐÌü((multiprocessing).cpu_count)

def PL_THREAD(Æå,*áÑË,**áÑÕ):
    from threading import Thread as T
    (atom:=[])
    ÐÌü(((t:=T(target=(lambda :ÂÞÅCAT(Æå(*áÑË,**áÑÕ),(atom).append))))).start)
    return (lambda *áÑË,**áÑÕ:ÂåÔ(ÐÌü((t).join),atom[0]))

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
        return (p,(lambda *áÑË,**áÑÕ:Âåß(ÂåÔ(ÂÞÅCAT(p,PL_WAIT_PID),ÂÞÅCAT(áÑÅ((áÓà).buf),pload)),(ÂåÔ(ÐÌü((áÓà).close),ÐÌü((áÓà).unlink))))))
    
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


#ops_A.☾ (3282 ⟶ 8533)
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
        for Æå in(ÁØò((lambda ÂîÓ:(lambda *áÑË,**áÑÕ:PL_FORK(áØÇ,ÂîÓ))))(áØÆ)):
            while((ãÊú((ÄÊPSH(P),ÄÊPSH(ÄÔÔç(ÄÊPKE(0),PL_CHECK_PID)),(P:=ÄÊPKE(0)),ÄÊDEL(2))[2]) >= áØÁ)):
                PL_SLEEP(ÄÝôÒ)
            
            ÁØòþÁÙÇ((lambda ÂîÓ,ÂîÒ:ÂÕÅ((ÂîÓ).append,ÂîÒ)))((P,G),ÐÌü(Æå))
        
        return Áÿú(G,ÐÌü)
    elif (m == ("t")):
        (O:=MOD(ÂÚü,áØÁ=ãÊú(áØÆ))())
        (Q:=ÁØòþë((lambda ÂîÓ,ÄÝõÌ,ÄÝõË:(lambda *áÑË,**áÑÕ:(ÄÊPSH(O),ÄÊPSH(ÄÝõÌ),ÄÊPSH(ÂÞÅCAT(ÂîÓ,áØÇ)),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3])))(áØÆ))
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
        
    


#.☾ (1647 ⟶ 2431)
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
(pwd:=(lambda *áÑË,**áÑÕ:áÌî(ÐÌü((os).getcwd))))
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


#Ń.☾ (4955 ⟶ 10623)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/Ń.☾')).parent
from collections import deque as áÐòþáÑÁ
class ÅÒ:
    (__slots__:=(("t"),("c"),("e")))
    (MCH:=(lambda Æå:(((CURR((lambda ÂîÓ,ÂîÒ:((ÂîÓ).t in ÂîÒ)),frozenset(Æå))))if(ÁØö(Æå,(áÍé | áÍá)))else((((CURR((lambda ÂîÓ,ÂîÒ:((ÂîÓ).t == ÂîÒ)),Æå)))if(ÁØö(Æå,ÁÜÙ))else(Æå))))))
    def __init__(ÄÕÒü,t,*c,e=ÂÞÅ):
        (ÄÊPSH(ÄÕÒü),ÄÊPSH(("t")),ÄÊPSH(ÄÕÒü),ÄÊPSH(("c")),ÄÊPSH(ÄÕÒü),ÄÊPSH(("e")),ÄÊPSH((t,(([*c])if(c)else([])),((MOD(ÂÑÖ,áØÁ=None)())if((e is ÂÞÅ))else(e)))),(setattr(ÄÊPKE(6),ÄÊPKE(5),ÄÊPKE(0)[0]),setattr(ÄÊPKE(4),ÄÊPKE(3),ÄÊPKE(0)[1]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)[2])),ÄÊDEL(7))[7]
        for z in((ÄÕÒü).c):
            if not(ÄÝøÇ(z,ÅÒ)):continue
            ((ÄÊPOP(0))if(ÄÊPSH(False))else(ÂùÆ(ÄÊPOP(0),("Cannot construct Ń(%s,%s), ⟨%s⟩ 􀊞 Ń")%(t,Âøî(Áÿú(c,ÁÜÙ),(", ")),z,))))
        
    
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
            return (lambda x:(ÄÕÒü).frp(Æå,x,pre,not_T))
        
        (ÄÊPSH(Æå),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),(ÅÒ).MCH)),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
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
            return (lambda x:(ÄÕÒü).ftrp(fs,x,pre,not_T,**áÏè))
        
        (ÄÊPSH(Æå),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),(ÅÒ).MCH)),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
        return ((ÄÕÒü)if((not_T and ((ÄÕÒü).e).T))else((ÄÕÒü).frp((((lambda x:((x).t == fs)))if(ÁØö(fs,ÁÜÙ))else((lambda x:((x).t in fs)))),Æå,pre,not_T,**áÏè)))
    
    def gets(ÄÕÒü,Æå,not_T=True):
        (ÄÊPSH(Æå),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),(ÅÒ).MCH)),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
        return [(c)for c in(ÄÕÒü)if((((((((ÄÊDEL(1),False)[1])if(((c).e).T)else(ÄÊPOP(0))))if(ÄÊPSH(not_T))else((ÄÊDEL(1),True)[1]))) and Æå(c)))]
    
    def find(ÄÕÒü,Æå,pre=True,not_T=True,R=None):
        (ÄÊPSH(Æå),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),(ÅÒ).MCH)),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
        if (R is None):
            (R:=ÂÚü())
        
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
        (ÄÊPSH(Æå),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),(ÅÒ).MCH)),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
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
        (ÄÊPSH(Æå),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),(ÅÒ).MCH)),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
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
        (ÄÊPSH(Æå),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),(ÅÒ).MCH)),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
        (Ïß:=(Ïà:=ÄÕÒü))
        while((Æå(Ïß) and ãÊú(Ïß))):
            (Ïß:=Ïß[0])
        
        while((Æå(Ïà) and ãÊú(Ïà))):
            (Ïà:=Ïà[((- 1 ))])
        
        return (Ïß,Ïà)
    
    def first_l(ÄÕÒü,Æå):
        (ÄÊPSH(Æå),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),(ÅÒ).MCH)),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
        if Æå(ÄÕÒü):
            return ÄÕÒü
        
        for áÎÚ in(ÄÕÒü):
            if not(((l:=(áÎÚ).first_l(Æå)) is not None)):continue
            return l
        
    
    def first_r(ÄÕÒü,Æå):
        (ÄÊPSH(Æå),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),(ÅÒ).MCH)),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
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
        if (not hasattr(ÅÒ,("txt_format_imported")) ):
            (ÄÊPSH(ÅÒ),ÄÊPSH(("txt_format_imported")),ÄÊPSH(True),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
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

#meta.☾ (4917 ⟶ 6860)
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
    

(dump_cached_imports:=(lambda *áÑË,**áÑÕ:("TP_CACHE.update(\u007B%s\u007D)")%((lambda ÂîÓ:Âøî(ÂîÓ,(",")))(ÁØò((lambda ÂîÓ:("%s:strd(%s)")%(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(moon_dir,(ÂîÓ[0]).relative_to),ÁÜÙ),repr),ÂÞÅCAT(ÂÞÅCAT((ÂîÓ[1]).native_code,stre),repr),)))(ÄÔÔç(__ÄÊIMPORTS__,MOD((lambda ÂîÓ:(ÂîÓ[0]).is_relative_to(moon_dir)))))),)))
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

(__ÄÊGET_GLOB_MODNAME__:=(lambda *áÑË,**áÑÕ:áÑË))
(__ÄÊSET_GLOB_MODNAME__:=(lambda *áÑË,**áÑÕ:áÑË))
def show_imports():
    (ÄÊPSH(__ÄÊIMPORT__(("text_format"),globals(),(""))),ÄÊPOP(0))[((- 1 ))]
    (show_table:=(lambda x,y:Âøî(Áÿú(ÂÛÅ(ÁØò((lambda ÂîÓ:ÂåÔ((m:=ÂóÍ(Áÿú(ÂîÓ,áüíþËðâ))),Áÿú(ÂîÓ,ÄÊCUR((1,),{},padc,ÂýÃ,m)))))(ÂÛÅ(MOD(Áÿú,áØÁ=2)(([x] + y),ÁÜÙ)))),ÄÊCUR((1,),{},Âøî,ÂýÃ,("│"))),("\x0A"))))
    Âçß(show_table(ÂÛê(("Static Name Path")),ËãÂ(__ÄÊIMPORTS__,(lambda x,y:(("✗✓")[(y).hardcoded],(y).name,x)))))

(BOOTSTRAP_GLOBALS:=(globals()).copy())

TP_CACHE.update({'Libraries/peggle3/rgx_golfatron.☾':strd('c$}?S|8E?{7609T#j<Lonajko9aTuDZqpE(HiD8UF%r`Dx?11uIhWk+9(!k4%UB{NUnmJ`N$m)lmIe@tl>~%ZKu{&(hxt$VOZwiMFFSj?c3jH+;M?1odGp?9KJU$E#!P-9|04I>0UO4nwO;HMqSb<TAIQD7ye{uB_#F2NkMlvF$*b~1`7J91ws4*dCkej$yZne1oO6)`zdyIk<PMC!E5OKy@@nu(mL{BWwi>MF8wnU^Oqu8N>&cWcKk>QP+UE3`>m_{;n*R(F!`EH8C$5kM(F?%r$MU+!^#gCudGHzZJ$A)Qv#B>oJvBtPnAV;*n0S>j=94GWjXcG+@8u2lVhrJM+rd7dBe&&O?VzU`F>0?}Z`Ka;`EfR8SGekIeaz7dbhG9Olh@>X=P&-wj2GtjmGUv?Vv<Y;(`2N2zqG=ZbSpeAmX8ZuJuk1k%uaG1p6rxvm~hG8IfA-3m|V^VX|$ea8{<i&*ODB0s9n^*+QC*!J#BLv6!GCRi~K`gg$3Wt=gBC0Bhg)FKp{M+pXUrMm*sEr33G;MgxZ<`XHKswv;Sg-ywLEa{A)W@-vYjN<yVY%IA>cegl<=UB)>Pl@og>?SsB;sg`f<xF3`F3=gmulVPd$iTnLMfP+;*HPO$>qGkqG^q=PHUsQOv%QLfwoAXy#AVLL#NAWLrp98C52T(1X=g499EnFtQ0)UbTqQlmx7gf#4M;bPQ?Y&ADE%y}^68sV$*2l*fEq5!uMW5W68qpzL<{oIugG#-0itL4eZYV?^`FEF+!u&m(kf5`9TP4xAte8;YuAOrX12Yha>giG7rk@w_7C{1DO_$kK!u(7c4{0sDV`K@2f|M>Qw{@6az@xcaGyBUCJ?#e5L(w#O_KULXN?{pI<8Xn4MR@&12n2#R)@{G^*GGP5Qb2zldk6>u_zI->$M?g;tcDMj*uAA~Wtu!rmoV8fw_<~ACzFtJocLKY>C^+d<VWj3~@;$(>;9d}T22>d9#c5BI^4xha?)}QPj=0;b=JFsTaI@g_G}EBUbYr>D$P^Hku<^R}qo4?B+09zhhDDEN!&)K~&1%eaFGQC20GL;Q`&xA7!piB@6$smZ!ABVH%g3<HL5P_8EqFy67c~F)?ml*C>{sdb0NWc#1z(@bT}E8~7C3KKS%IX?G>t^kU6XtArrbA!_kk07bsSrF6id)+dXVqP8}gB|OK-ZDaw64t@=N%pW!CjZ!w<=FYywGfjHzA+@fhMfHaT%@qI(*cskK};AXp_QR5N2IyhTtVm0l!F4D&QF-me31Wb}!3=Lg%t8BZTnF9Hhzl6x(l47#o!x=hNYJrjv0&LjEM5a%*yA*dS`+7vN!o9MuGl2P_Ic?d+{RC-+(A>AAfW5~0Gjcl8;#{9QvsT7}atGH*}g0J`GUGi<KRcwQ)28PuD^cJ}z$%a|Fo=m1ue^5XQOg8#~N<*9dG%Zr<8$?%4Ozf=eq?#)WRTWUF8jB5?t=kc>>b7~7cFY}s?IwQxTi!17)R5FI6>QKB>gxvKaCR1vyyono<QZoF$B=nNI2jJQ31Clhwj*FAo>Aw+LC1S8@N9)g_u(C%6%0DavsI~3+3`#YpXExmjpKZhL{K!N?j_Kg70K{ySw%vuoCFO{vuK(pNrU(>Wg232D4_dcIfl)<-clAOHm>hClV|QTcKVBuhm0xgA^9hss+J%p=#{FR^q#9aFahR{b>=gt)7T6dD+An>O9q)+z?q$<40^;(V9muDm-`|FM~Pe(j?LMcfz{9Fq?dICZ?QTbO%N<BlvRMyu8`j9spc8gV)lIV+ejlvRbfq6J~-HyxGw?jOC4J<Nq1Ax*^zI{n@U+U>p>IzA_mVkEv}YZ1l*^PkmEp~0UUbeq~+Cg_AO>Mi^ZDgB2<+ELW5o>QuwEQ1w)tQLtGw5aSq4a439&wOI4Vm-ch1{&B{Vuk-K6|t)-R>75;7>nZMPk)kz!T5o(*Lul(zpXP*L)Wx-$41s~4bg2L8CU+*TH&MwmVnS9Rqd^{c}X|I8vN8de~xQ(?b^@!Y}wP_h9!h<twq2p$izLn5wsZ~(W2cEM4b<-U+SSzo{g<QKz0OmB2d)mahdq+O0oHxrSRS<Mya-kMZ8^G2l@^QNnEM`vvl&O32sq#s`OhWMX>!&`~`Dir>_IN1oHw@=xJyX){8&|(<D#!|vIDu?2f7R!0x|7lKnI9=UZf=VMuX3EZFy<%KxsFB{-D}74qAuW|CIOWJ4<3?F9ayVPbI37LUnrm(vPH=w<}>ajjCTAtc5V55f0~cW6Cbb&&UZi-_=^QbiF4Y{Y(<O8(bbzK$LbWdjH*!w-8mT^(Rz_AK1HIKFtw&o6EA=`#Xqjsc{Yj~Xz%DL+j&-2HM`-=cf@(>;ZjZ>G2j_pu1(ctF2P}BE|wMe^Z$6bU-Qsb=!3PhW2k$81~A9+dKwFDMW4jedUekJr|JxmrPT;13b5;xio<RZ+{(e=2&IqIb(3*h<$SG$R3-}Ag^t2Ctf5*%H^t!NTJWt|L|mn<<u*SYkjlEdc&L3=6E21nGRLob@(X4Z!_4t3ty7T3yA<qH5ou<VrHmD3%<uZ#`I&mhy^Pb{SUjEPKkaVJe9VS7lNpS;sa-iMSL=h8PlqR`F1G5liHPjUTNNo?JG?ml7}Du;_Ift#$J0DZX@A|5*Uc4YzZ-WiC5^Xh#xJ9Ab;f=zubYfL$!nLvE$6_EbgL}T`*Ig~8J3q*iX--?+g;y`ngcpFdeP}FfKI9j|8@>Lkk8(4h{oIaMjV{WHnU?s<HpTtt_&p6^V6>2sGe2NqMX~C2p~li;keVw%hAef=g(bOy%<GoeVDDmaE2W#Ebv9;Ck)3T6Gdq}N}@<rnJ5~?fKOzL4aD$3{<BIa_3x!yGbeViH}_vLTwhx'),'Libraries/text_format.☾':strd('c$~#MX>S`xmf!U&8VwkzRw^EnvL>+-X4Y5Mi}kDn+lvHX2!bM8A`>23l3KN9Jb*2mwlj8Y*^(S9c05sh<gla3*s<g@22wv@ena{f4B$Vo@4c$(u0E(EyNeOftnNBqy?R%@_o~$E%vxhZ7W~zlQ|(UAnyPf%oK@~x9ha)vkpusF;Dgekf7?5jXEwFkjx*$X6?dv<i52mw_#C^7d3b*=LG=Ql2H=i6>3Rm>Byj41z_Dq=2_j(eV`H!y=Fm`m!f3Sec`IC!gj{teB&O^=J`59H7U%h}d|7hB$yo;=cU)&@rQMvWH(aClNA+I*SZCS|hdIVDXD76m^r*0<<MyUIEvqB(bQ>v%YVvFgQ3ZDZuEBr}r~QAObBG~Z#rKtRrRD-r8|CJBwQPwq;!a}7n3xlH#3Ezjy!b(^jOA%iiD75Q;d*Rh7}F!1`UJeriO1qH6DP$r@qh&r&WTmA0A0l`@n`Xr$!`ZoP|r10!vW@kSaTe=(REqYfj=haa~$h!E1SvfQf(3|hb0z{e?x4d-l~?|Zl%<9|EmiNhsMvv-LbqRFguE(`=OWJ`{8sZGrF(9em5rHs;|A3dn<TNyd2LQFO2Le?sl5T3m<x!EIhfQZO++pJ&?d!xf9G~Gl0IM>kRMwont#Y*ilZs0iz4zrO}Hzy=L?{IF>iK$4aGIeX`bor{{J`C4$ihV*f;)?ngUAmu98W!A_kf5+d3xPK!V9`_Chcjc|wm@lTwjsXIN+BXr}$n_C=s^Fo{=oT}|!r{0VL(@ggGY<@I@^57M^je5mp|Iu!_oXuLVTfoYq^%@Agf8s9Ei$sNB0RAXFU%@B<ds5sG%glow);rd$;<cv;JULzNRHJkM{_y^|kdXwgQVT3|Q7nrmC|1|R$$Zv9aeFBR@TTbR+jC3{UU#YirlUvPYd6}RZYc4d2C2uM7GH=pu>#A?6*<aLW)G~12Sm+EqMF=MG~~k?NQ6W=r^q|GS_79E0@Qy)tWj^dAjK(*1!BvUo)q`Q3%yPy?!Z#F+^N)P)ks&RcAN+akayCmSvVu=Bd+eTII9W6Xp>m6j?3NRTSqIPQei?6q{eOaLIdORdOoMg7UvI{1|ZByV9n`RE2rWL4t*+~ut+5t1BDc0b!!;J$<kO$D^ka<mqlOUSa;MI#cPifC8I<hVm%;(iTmuB=Jbj<3s{hLpk|aCjhL2m&*8HUmn+qJZAi5NHne_HBT1}7)IBblWXik&jmjvrxG0bu%!!BMQ!NJ>Q{I(%HIPG@joM>JirU7g!8b~+Vtv((v%Z-Ja96~g|0Vz7OX-NLlam$=A)v)x2#VA#M=ua9!J_zDE6bcFku-6RX0^uRv{(XRUv!*8236dW>KM?8H@7BP!0DN8X|Vcg!=kZEm?a4nsq!2)*obWyLWdz?wg8if$$SWB7cXSIci$~Kd^}N|$rQEofyP(vh=q|iVGG>RZSLseUZgObm^AIxh=W9V3yq$~l?R4S+kjnv0B1}V=OWx)5~mWRAVz4rrj$_;gtlQM3RhjTMdA)J@s79_VUyZ-4G<~BH@XplCB12t=y#;EGO{_`WRc~Kg2jSO&;l?4<;a}g3?ZY_t41$MF`X9|w3rqqCV_!PhjqAVr>NT*aanis95zdYGWsx9@URYt<F-2+<D_&%ckOQ4+O)$6n9c(-ZZu*fF=FExGLh~fv1d8?a+}Zh=36EJT2lhbhD$U6z`!Ts412c>A5Qd-Zz!%PS`cVxt|@PPfZz`g5PjvFEP-h{9oTBn(!jLs3XKgcvw(WaLnmYt?2MgRo3##4H$D<Rt!C(748MwO%T&3_2)Q#7$Fs6HmnVCOA6Lcmd?47$kf0az-qC{z_fA4`cv|&Y@_QI;!ZiBd53mdxUWcpZNPV`be69Tl4q=D@6*9zz=&E78leZMeM93sDkb#jz^^!O#V*}_9PHICj6(Pyhk>ErZXvSa?BKoxm3LFwiARQ1VVP#UVLM~ij1q`DQ$PO##gpdHXA{;2S?C_i4M0yOIE1QCF49^g{K^4it!|wsDl|M-QRH|ZXPuLM`+K#S&?vq#RKm7D+{qeIbZ5@OPA1qy6EnYKuagW#FN1+T0(P5#IKk0uMDFWFrmY4pDT1AW&GgiH81wd)ojI`YY-K0R=BW_X*ZY>G71|q6FjWkqXzU$(9R!gqH*$I2M+p02@0MsjVYiF!>2V?~d*D%iZx)p<+4t*w#K7+PoDp7KcNnf|(${AV`CuLz#y-KpU+bdT-?ofz+ReTrnmbKcHdxA<UMIp!|Gu2c{paR2LxVWgb7-q81y-17P3bN#21YX8K3ldTq;5dVHHfBju2ELP~e~KVV$|B^sXA(9rdx3OA2Qt*bbd0g6P#~(BQm`hg+^SlJhMLXhKs3EZXGswhKg_Z@^cHJShG3921T?i-Ig2PK#YOF7=K+m57Hoy!sKtG9(?o!Qh@q`EB`EJ3j&X_@j<>y%1_Qn^cp{^j(cKfUg^kxI^Kv<32HiohjF|(+55M}bU8HYp#2qx3auAuxjAIO55KB@lH%k#rOqy&?GC8Z*g-Qequ+mteCIsa!08Iijk4VZ7*+{9Y6irh>5?Dmdk{r1e*Tr`*%D=ecU;N6yc*{TWiGT67fANlg@vib{7cc_{8hSXnmG9f?E)I)I+a*zG47ZUXCW{wrT2NREbth~k8+}?jR?Qpe@j+f0U=3JEaA@}6ZJ!P$lqm4{{EJ(g|C%wskuusuHvr8QV^azy$#F?O!^`J?AoN)a1vCqmoO!rO$v7R6_(S+fnYdZGyjC%iavCCqne5c7GLEDHN;fdwfvMC2?HC9nnRrq=5sEM?3?ns`e)N~tfF}OZBOn71%wL3>bzliF&tJUnFV6XkxBbN%{^D~Rqoah1C^?kMu~h{MHBX7OC#8+d-&PV3X)bz@D~RS)q;Fy-sRA+Q8#x=EvS>2v=b7peszwe}BPUgZ9a7FqTr<7UVWCp5{ry4P{~)Xe2Ns!VU?Gh`pB)P5eDMEnu2>L*lLYIh<Ul{nU)x0ezu8I}biP+j`clU%Cn-$HSqdCiWK6+<EWcL>mR&3aSQYvE=Ep&!lanHG+H?=fIC;`8s$QN9fo76+v$iF>iANeru4qECAW`dm4bNqWC=8s+*Dxo~_4kbYcA}XBQu#vUNC#x>UP5IsYw-w^74qf0k-m+lvnc0r)d@x*KMJ#WMDVsXgUKW?TW?!6^w5gZIVE!n?rEHgAVlvwh1sIxIAQuV#gq;>22j<MYzY{H-Cl?Xfr3WIlAz@WOO6WUbaE0fpR={=Ea4sEQf<=C3J6<m!NN2jKN>a9ENa9OTUfxo#4#OtK}_fKJRVK@>qPIMY(I!+0wlRlQJa9Wl#`MS^Ce|@@8J(Nm1cDNqUm@&vvCfyxdEr_g;^ux1^|PoNKXyV6=gn2W_S}h4I?2Qv$1SeEy+yx!km?VF6NnEfpX`ci*k0mC}ZE5PI)T*6jFIh)%=?oK9y&?f@7lSf>O7s#35QrFbt7h)i{F)&SOZMQ;EZjXj`uX-t{sVo6<h#6^B>(6p7t1ol1d5R#jS(MKc}IqX24bO%FJjRU~QVv%H(vM;jbdLHW#B(u$cLsJaq>`Y1PX79Oae@x0ICXZpAnfb7UaUpy(neA6lMMB3>EaVb1S*@R|l?=Wojea)PPV^Edmb9h&J+m?!Wv^!>!Dn`UmoVH0jEnUA2r7K{kVug0wn}C<*>JaPJ+B2m}yXu-cSIuWLnK7`90WQe*d{xe9>=X9Hq&>#$-PuvwN%eizl6v)CBQk?F-IcuBQ3tTSfEJ8G8;b%PFC?itTj3QIKrN%&U;-g4P|=5V!M+gO-zb`V*vK!2z(KJ|$)d#F5P0qtlQ}xNg3$!4@W<g{R;^ch;Q>$~yvP7DWyBJ+-^<Jpi0B!4di)6A`||y<ES}5afh=Ci;-M^ll*O7Xo=D&3Av);z@}oF`;Lgg{r@HkSeqX^h+3AvOf2P}?>xT2P;e~E^AqSq+?Q^=}rEHkf4X5<WynZ>YUoPvHD`*7B>zEgJIr-M-5!)wN|A4Ej0AK2t75(y+d|A~st6|M;{c=aY+|@5%>z8lz%Pr{;elCmKvRGDLqAXTq@vSVrQPGw<Jd?$BS*)Uf{W5>opFiQ>zy0cm)pP#Um7ibu{e_>O`~4-qzwGzt{r+{of7$O}@%xK@|LUvtwFmI5|NN8R{|sIp`u!WP*4NMY{cG^`BfQS}{m<d`k>CFUiYM@_`Td(vJcY)yP(Fk596X=={e*w|tbgvNSpECySL;tdh36tXmtL*^?OS-hgXcax-@~&C&tKvB0iJvR_~P;vcy7RR8J<h<EW@(`&zHX}&O>n(o&|X5=8W?vC-eeA-ov;y>GzBKkzmyH?GM7%O16<yW`oFc6OYq0LZR<FF)>28f+69BBHo^QgRWY=vETp8nk^l~eTRRa;vgQ1`-f0>BvO~7WKy)>2-QXV?ZUb}N8XQAj;1-BLBxienL2lv7Z=2HM!I*EQI7PumDYHT8XfI0FFR>2wDg89h!?2`T%X2L*=bHOre!F9v`oZa5MQeDYjB!U?}biK3aDkFh=kQffCLQ%uNbr>?}dUr?{;Nyc}zw3YZwRw$;o4wQ|ir5xycM95YuyZmP)O1(=C-^=O;8yg@VaUpD9qVTiy7~zp-FDg=2VvoyV;yGm)_=YB{F;$%#zHPMnIUY2qhGY10JP&S(ldN4E(E;e0do$bzm{QFB0|l(E+bj#V4tZQKH+@{T$iL0V18`r13X^3sM9<6CqXZjMpMcj<z3jGXeAJ{$MmJf7x>vFvXn8PFV;&K?3IYL1K`b9n5?D!5rhW_{3NHd)X&TUgM(Lp;8W^zM$j=fn3M*#KEk;$MmE@^+C;&oP)65sf>uDa!%dM<y5)vEFl=UFK|UiC~X@<q}u6u*ALF=EvTRkX;ZDw_$yvI_FVB<&1b7y2>fHo1<~842YokTKr|uIvM*|b=R>G`&iyH06=(zru<P%Uda<3Nw$xXKEXw1t{rDdQb}(#a-|Y(4tw_RFCF;cy~9V29W9mEWTQP^ZUBpcX!3fY&1H!-iCbcJ>U~$6+-_T6I%BrH)@gHDVhskRHpgH5!c2|L@mGCS=&Pc>I`q|1UtRhlxbo!FRwtlXGv4-W4nOz~fsoDNht}f4I$ZgN7xXz5_#IrNw|Vf2^>}z;bNtmSf_O@<30`#FOi($aYURylo6C~0)Ug^Ms$Yo)7+nDou%MByq>?NZ2lTZ+VuSv`wrJd9$Kx2Y2bFd#B|<$6BW*`awi=%zmG%Z|hB{#51**sDT4B%aD&d%DcberMQ#z*QUMetUC|GR6b|)uogemuA+!~_oGcNp554n#!eAEfErRFR_L~VRyY)o@l-EyN`wcvZ)?O44TxAEVu1<3YVVC&G;%<SpaT&q#;_N-p5-kP*#+tXN|d!uU2lv_Qk-NLGlH9p;$Bs{V?&PKvp#VVa&rb7puAH);p{;2JLf5$&}&MkLc3`on}cD-8eR^_sSVdKFtjO({NtP-1T6h{3r|LErjMxSa7bV?u9u5K8Vfxcy&bR2&w_*2CnWWzYGV2a5ch58&YGMnWpWw2Q%E2T?i+g;M9!cL9p26oD9+zBiUF3sCsSL6?IrChe14M%OVn$EVnm{Z|d&!DsStKyzI#EG9zEJ5WdqjMHDN+#pY1D(Kmm=|Bk>;1}OE00%r@IL?`|8L0fgTMl?Y{od<8t9f7W+8|I0pf0TaXNKXHJO6>7SqaVdKmSOFFt!_Nc&_U?IFfBY2Txym75fsOt0nA@+26d%{TK;Jh7~r+i0{A0SKpRZpZacJaz2o0M#9MD|;i}s`s{G^X#^uL-!bbV{eg@ApDQoE*3OZtzM_Pl!cgMaXy?1hGIdp;!vG&lmFYN9V&U9wp41C>#b5L_y;x>7RUDv82mp6%cln'),'Libraries/peggle3/main.☾':strd('c%02V+m0K@mGAnB27@fBIPJj<$BwdexXM_!1d=6XG=TyzT!JE-BPP71*&|V~Wyp#o$FZ|ktc#P_R^)gUDUMe1t^==aSTW!R{1<u1e86IX{eeA~s_Lq~kQ{3tmVk!cbvgGs=hUg9y5VTxwY%M(*BgvSVdNb;^!+^|z8wGZ#L4f8W)q*j|NM#L8=K9h5Tz)XM$PUh9JHd6^tbw>)2;qQNMDpnQc9oZ9X}yfq^t|^l(*_h*#L0w#n<Bd)tczH2B$kMZ|axJ(Dv*2X7%~w2N2uM_)qa;AKHEszg&wi!Pjr4h_A$N3ivE}Q-IU!iuh&d_*hJR?2$6)PXcUvC;qLNBKn|4;4T5=TN>E0(J+ugip|<)xE%muAsDq>-U=dMDF8-ZxFB&p0@)*mM9-V?=Yxb|-BcBd8KGNj!gQOjsPbO)h?px<6Kf^`qE68DnAKz=0RNZx9a-Ju!N)XLYY9yj3>wtydImjB_8GVIMj?{@Zv07n6}zs-A8YUmK7PU=+75??KWf)-)$CUcV3c|?RW(;@q$i@`eZQ<xB#?|XsR?qq+Y2XAbJFVs6M-5tQoa;FjIUSW>jtnR_*E_kU|wUiFVqnX28;;t$U(5P`bq=ZLZ@l9p-l0>!J}eTVuKM?-|J00vWW#`U{S7xz8okk$5x^$c?HuFeH^hou21^Cb|4UuUy(o}_JvMg#V0Zv$kZf=T2T}V%|t~(g~!$8am8Y54cJ;^w$kLYVZ9gsD*nq88dk1dEoeK=R6*qY3D*NYyeAzq+KrIGCT_=9_OEXmstEFv$`DtlmqU{w$)YE4=(!fZ9)B(p+XfA{N8|HPN>ILLS&si6|CPV9{>f**`WmjGyYUSa*S+}n;<@8L!pE26Uy1mE6rxkDC4xKzE*zFvBK;Fc(j{2=4|!GpM|y#ZajVnj<@vg(b7KP*sfUv3z{Adsi}2_zd7|{=>B>5-U3R;#@hY|)Aux3{zFe*4JAxTRz^8P!gjiG%c{lzzexUvS>bInB`#0@LBsuF$v-eM4<(X%+i#9{8M<5bHBnXYQ4KY$RfwEz>Syl-QZ?CMZtVid^0j|UC;iR`U3_4!>Oe^%Zd&B74&FI;JG0^MLn6*k~&?E}C+mSbJhe4&;9(4liF@NaaZ(Q@RWAAesuUDQtYv6nRXSw?Tj?4$KvE2`B7&I@kV6>0gFB|YO?2U$M3K9Sa6FSRYXmEB~k$FZm`2;-QirQx~6!bd&*az~RLFFSBDZ?WMIQ1&%^j!AFtq?SgSj*mjzx%tF{bVA(!oRnC5+6Lh?mKwB)1y(}i^A6Aj8s5v{@}3{1<f$n3Z?=foY12n%RoCvyXp5%+w0FVp7=vZxjMbD*@Q&|!^XkZRzFx<o{TuXVh`-I<#qa_aWF)H$DGuP*IANc@#tZ2&cZZhVlsnuUeX59iitl62DKN;Dz?iDK5D0C8#}OAHk_&8G68BP;0T8(5*V``b)Wh+($C%N&}}G!UN+5o1Her57{Du+Tb+(rm$oBJ<{=@zSoh=i<6p*~0XmquM}(l!jYJlaA68$0oV6sY5y-QHIV(1V@P$f%#cQi8;Vbl!f66T`TtERM;FC7sNloWFTFQBdCh(O&ofxPW%rpc2unoO^w6@~6H{eem`1VnFXdlI=4Sd>gp=~setv`Q|4D7S`Q?cr=u5k0_#>wy5&8yse=;%5k=V=h3c_8$CS9!Z`yVX7uuw870tw9s%Z4RKZHw@6L--`d$9}Ze$lU-bbnV(m6GX6VGKPa<jb@3eVuv*`s>bw9z=J`f^yGps>T?k|v0AZjgrG#5oLm>>Q&gIq^mPbeXd;(~aKjZ5OC?gYAj&aQn`6>>WcY}*!d@l+HyN>ak%o6jItzC`p3X;)9KdhzFQzx6k5fuDyTO+I`Qs*%Z(>DW5I-fJ!3F`N1H3;83?_4j*)EGN8LBf@uKZx%bJ#$hf^n5>*4ulNK5H&L#Md{Q$Nyvz%YOM|+Fa7~t4)f{4O{H;Z*`SeX0X6ao%1HrfJZ?PT36hq~?t^!fH{yFv4=4Gnl;m5Pe$KYU5<7s0Bml(zKObKG%g&vTGor_FdLZkE26?SvCoRM|N<-cJ;$8{)B5eFb>hh%)?`*{}AwRFyn0*vRo-G+#8BH-=^|H_l0l)%kA_Jxu=n6lydR~h^jNj9W%7V{WzOeS^yq0jYta^bB)&az}um1SeeM(-lKy7)_yv&FqHWNI4c~)*qs`YgeYE>DuyGrqpIJG3Pz=13tsdI2dZ5t=qWwC(My0Q0Ps3iqGS6hYVo#$0FA`JVX0wouKMQU0InxEL|0&w^3JiPtogRkzByIBajEgHsyiP2rT2)3n}IK;48V_dwneZ6=KaauiKO8eC6CW{(Mxj0?rIlMD$2iX#PXC>*yQ2|Fgzqp^lC)mPrQe0RjEFBS2j2B6Ifg4TO7_Lh6JV`Uqq?d^jq|)6~*|8|=U220?9KX<nskGNgrU;^@<Es3^AXCgI(?C$4##edEZI#Gi_WSWAGxt(_J$^%|G|4NMJ=nC9kT1rsD1p+nE_$t=4{9i%g&@!y>ZvM&agzv$3_|tPdku7R7%QAL1li<h81;tRK{gJawGyJsz#OnAl6dFmZQmV#rP2*9;+?f)WfB!D5EUzKR74ujdMTUGROZC(uJYtJ<5zuUUSuyf<6Cn?<cNvwauESJLdv9$M2M9-YKn>-zsgjXyt8)Zis}MW?&VY|6mL(Ejk;2FN>9WOmlT2Xvq2a&aSx!={sRY}`{Cgln{!fI)U0EYpI5m{tcGj#f^32(%ry*95n-*`iwcWeqI4n*p2E$^q*}7qoLXE=apFbJSItDv`{twy|4Q<kur)sKo2AYyMWZG-;Qc?`NbgVR>&>cC5x-$Q8WT-ti(j~~AKDAs2t)6SU^6>=$0g^AWHgCp$b<>nkY7hEXcOH*1P&;Zd5OVTZT|?5*%tg+ibA3A8si|qu@|xg9e%Si@{83`*BR0(tRilsBu8eQS}M7}UXa|U)BfEh_ads+24i0O*R34c1i<T@AA<mjqAe95M5Mx%lW7-%E6$3jPBI6YHS{nHo$IjBK_$h59@Ru|SlO!1{@H(JreX2H_`4hNC&@f}hm*|tj+d$>IF1onl8JYG(_PNI9BRkF=CB4xrKik-0LwPZaM&8)1ULD`HE66+uVr^f-}ZZ*8m2^pR&Q8h_Vf$J6@se>r)Q$u4}-zzY|x}4V=&=!%TvvMFyzOB^vG5FQ_XIx*H<qG`Gp2$9W!wvtP@()kv`PGKu1$NEl9Pghit_<mc1-30H7P5LQ!%s?gxWl7zLe@yVOF=+_2cjRaX+euG`Uzq`H`BOG;jih<hC${cc(u*<^}8$=dUoYdi)77D-y>^i}ija8I(;hH1e;LGo!LTi<LnDEoPMXv{1`()A7~*)W~_U<aeaU8@3`Q!**gby%oiT6>pq>?xZY(g>|3TlI%vK+y4`5m(b)r8}O)@+Ns@7F<b>>|ojE0@o`kS&$-`V^mjalTc*Xc<9=9Hvxc77F)S3gv4_4WpMHg-k2c%Js7(coq=Ha9gdetrP6j8kL-hCqD?joyLwf$rSC}73M8XuyEv~PX0FArYgSgI9$-W|BWfmzXF~cza-A|aM=?~PyXyqw<Nz_ff5WZNqnx`G`4PoF4lzfPN6aZBU{YsuU&OE2Lxx8(Cde}X1E5C1)vdwfhR;oQ8=hAtuYHW^ImI_Kpx2=|D?|mozgUADReDdso^wX!jZfv<$_kh~a(ny)E<iu03!94}ugpizw`z1@HXm7T6&2H%6bb*}iI+S+Lh#bU*9xGlYNH-CGW9_%(<mFw^XqL^hBKq|Glz8!w2@kN3o0XDP_B0D+^eW;z6-i?^|V_$zRK29c1Z?mU3tk*;$NFwfKLRAl0toRhYAHZ<Hu6E+dp$B<p%p=zn(}xQAFa3BHZ52<2~1C7vZ!#len2!GmVZ47BJE$bqx7xpJjf#^#=JEW*C->;Qx>P%r4M7FWEAkGej5iog-rkOprE&c6~8hP=S2`ms7TaVG!c!Gw$%IrlKn-`_a#;qZmFvHSsptxaJCOZglr`P&elaQt!N%%KOx*6Q6m&o_MmrO*>zlaGEOEbkb>B!=@iNO;2OfrqlEcHXU%9zJ*PPoTj}6cl%}w#vCLU3Me^h&TUQ!%#^B8O6yrE9bf1^Vp3yMMub-eA}|TuN8#Opb?0KyDKLj0*tPa`aU7c4qXCY`3V$i+51J!YE=kRk{z+*K0oeT9D!CwMVnojG(?yLO488$q<7!#Beo{)4zW}~_MflvdbE?f?vWbA#D$1&<si5W(_3JiGWhs|8yQ#kO=*rHct2?(o+PU?3=jwlA{UFSpm5b9n5yo*CbbHehk8MrxCRj80S)aylg`@2;J;4T<zC#RJO!s8FOB3<go<~sCxOtq^=IC<7;1wMydlWM!(~M?s2re!~h2(oa=`mH?E)4PlJJtdrox;<qmQh7NtTEwQxYe|!oy)EzN5kX^-+gQ6;cfDVFMau-P|4CiQD}-<M=AVst-fAf+Q$eHdM@w+gd_}m4@LJ8D-}`yXMWhZ_IBe%__Hj_+`xQk@nxs()l>JTr|z|;uBE2#T>KQ~?OgoKngnlphO$p*3JiDG6)Hi<eXNJ&DrsWpowt_CwJ#rl9|G6#(l`F=!5;w?lf(RYKc24qBi=ei%u6rA1dY^qN*67F_(lVGgei@(9(yh|O4JE1v4SJzk{)>~e<XoRjlSU9XDE1MO~-!P)PE4)(P_hXF<elvTJ`bg3H~@7P0u&mXIi~s&}p_?{r;pm-VOt_gU9jD`F57NE+`J?l>ab+)7a>WL*^R1388vea(1(lx$vCHUgQ%VKba`5E~Y0UJ?vX_+a=j%7z|qD35}(q1W&&k{|49B+wlk5k?dT2l|m7GTTVy6mDG9qeTwS$DB_rWYjZRAM<8O!ym_jwYu{d9-ZW)yuEYE8g!GJvlj@hO`nc6eKORV0Pzumk1cXl!%#UNJKBP0|%}tqnn89GuZjA%`bUmtx(%(MAJCZ_7<#HH|`z_d$V5I@K7T4ZJfk8%{^l+oElKP|rZ!7Y6t1=!2o$Yqe{7GKDDCgciaQH_2`)rCe$|j;P@J=Qd1=;P-IlEa~{9@Mr>TdQ1RHqpkZGamqI)%|&FTThDOyZwA^pwC=g&zyxqpNcPVv3fAen+<~<#aM?5(9qEz<%qauYsLk$}<o%*K>Kl_4sRJ&kAA|Ju>N{o$*YCTv<%R^TnUyf8MPTTurB2oxFvVsut2M2ICV|90dP&4*s1gW$w2r^6^-rz`*&$$ibkG=u{z3_n?qglM|F=Mw|Q?`O2bBb@@U_-fvZFyCBs_s6FcUAxZ?z)@T7qAwBuJw14H~2xR7uh1&Lyg|<?^2y&xhGA^fHqRRl5OV@WOjOSJkyUl@tKGSN==AZ5`vEdpLEghO;R&&Tfc4L@Hw!PLscA9uFL&sR^Dy7rGhO1&yeX7o8Ge3}8OT<yh&ljGSSUO18VI0*Mz0<J_Zob5^++UkPL_UUzko1p%!}sa6((rgspC5CEi^ZJcivW&-F_C)PxiNi93ibx6<d2TTKT@e4##G3Nb(w~K5xJVBwO?7N27w>EGBv`hQKH;m^~>ZV%l*tz0<n*tYlK$_3#($o>`A+D@)yVt1_JyRSYkH{$4RcnyESl0*4Eb8Hv7yeW<D|h0$2Smm`s`gnQd}v5~oCZ8YevFXT|0&hyJ~?Y&bBjL{lB|r{P;8>O>$`l<VTWM7f?vxlU<ClE;K*@-ZIc;iF%`)o(?@UdU4uUv&L|Y3dC-1>@`*K$6}m4I~*dyAM8vw*i4Pcr{GPgf#%VPWRK~_j<?<pW3@?N@eXJR@>j$N_TbbP-_t~CF?Dc3bSj+GIU87U&Z8|b9@q%6N#oe1lfk7Yce_+H5g4dbQ%wm>ea;+%MO%9PC0C4&hay`*z%<_!)E#@HQ63nn}Hc2NnNneuRl#5H<Lp8|H;-(t$yc{AX^#lMd>eWdHKH-SU+%}dGJU0-wK>;HiiBF2&g@5$yX0aThb)={4auTwqX'),'Libraries/peggle3/gram_tools.☾':strd('c%0o@>u(g-760zPVmcDiz2;)=+Nmn7I;|*B6*VaqI8vp}cC=oPmlgZc%(z+7hhpQH3a1IU1{ve<Xa!Ab#G^F`qL_TRAN!$yL;NqKe?ZT<uetMB<438~tS~!s=H7G9`~2>mC6g78@I`)Q^4!me@8i|!cP7uAo$`G`+<wq(wu1?mvSzzCU2jK(GUB?FQYPk{nIt7jtAreL$_}M9Ix?JB*c|xHUVFA4hrRBeIqt$R4hFG5+Y3AO_yFt(nWSU<9{(eM%3sNErbt)$=i;&pW3TfS{#8dlS>S8@CNuN4U=c#nEGnMh|MOF@Y_(K_0g_*eUPgMtJoRi`%n>W4=o5+;ESsXgRa2^-JoPpyQ)E7Z<37Q0q+Rb!&(xg(8wJuezRX7D#r4WNXHF6!!54g+0d0-XdvaMy_(yz&<mXT(31HljnPAp|;g9$x(Rwhk>ISWhIPfv#ikE0=h`<2{wSdVytod9@yusjZ10;|v@Dm2{T-bH=JV7^87x`!W1;1=2gV@$o9Pt-^g?~v>g6WT<f-%K6I?Fr{+EL)7hZhNAgfS8=@KyeT=mp0Dh{Zkx;~w-$;?me?EKos=RKdsG!a}$CM<<R?5o<9z)~`nGRwE$4=yd}&PHXT-Sro+eI1Y&pnsLPjF3ZVf$qJ(hit#p5ByZyQhu;;)TgB_U;{S1m5%4DczsA=N<Ny6>OGb^Fn5IRVQf7@wJX(|#^o`i0H#-YVeURV=f1EPS4Zf{R0}&!sb6Q;|rFjw{`?L&6j{{{(HRq_KmSy?JW$W=_4I%!62JAFIp=6;%nY2+F+8W8^*P8OBXsm}dDb9EV?J#2udSI(dj<&63v)2!x!?$LWQ4|Y`^)Q)L7U8I$j1S{CVe=c$@SDi;`=9zX@z7rV+irCOKdg6~K_pdpoc5_C-i87_&%cH$ZdE%q963ZFuS{%XFs3hs9RUp0m}~?|*C9z~fF-Eoc`z<lo~ss5V_1C!zK~|hbcxr`y)B$NN<{1XJJ@ZLXoMzO>YteCY|r?|`eM1FgKb*{n;Jlcf~>^kL~yxMN!g^#bP>dYhk=yV`<R-YQAs+e;m18cY-CdIamqb+5_Bm=sEE<`p)Uw%c@>qAu(CvnQt!mOXLB0k*Gh$`Awn(GQ;<a{YYmAChau5mTutrBv+{X1>=S;8FY!%gWYDb&c;4r$WPfF#naQzqVp+|45m3PjHcX{}8Ds<*R5HfY79#_2l{9!&l4=-4U=0P}SHT#o5<Wfkgw!uUYULw_g9<pm;Mddw)cKL;45<F(>c&K((|B>+c#GmDge480O@(s->-J)Q%KIto$O0;(Dh`9dmwUEWyB*AA!;AGj;yMN`nJ|;tl2t>fzrg>-?^?STREYHHeq%*onk9a}sMHa`eWBu6kShs}SeGI*9?K?avxo)Ql1Q%B-C?;dl*6YwZlv4WwIq~eawBsqyo7*N(uPPWKm)X9;~x^hs0fP!y1EqyorATAH1y46Sy9yKctf$KkSEx?AX4n6fpPlCcv2cq5^<0J-k@|Gf<?ww7~na8-|t1OxYg@M|JS99L={;0wUOEFb=$p0z3oJX^#1u)JJ22DPBp4o2u0iiJaB$k7$w7kFtW;D5)-n$GL*C^P+;2uJvbdGCOKMcAW|df&UJ#Y9tTET72FEZXCx9xZy*&K2t}ZB6~Nofw3IS?Lw8XDY=&izIks6r`4&hL4Z+yQoPn&<heKlaXF3e(7n~Hi*uozSL2dXE!Sn$w$l)aGuoI?(E~)M^-LQcBn&zMHwS&l?u1Bp#cG(1;LzeGz*E8D+qu7sHGf+AUDvH=^Key_N+G~r%1M;V$cVrLaKIM0_M{&91vsA=kFgmSB$d5d!Q}50=f{`YRcpa8M``F+j_reV;Q;+W!Z+-t8LAE#CKiuz)-9SHShV_mg_N}^$ne-19vW|y6Kz8$azL}gwb|{h6c!^&#9bU{*&}SKn=7M?hkdlyz*nL1!2hEbWN-eC#E>;Y9`hqWN9s^bDKPJ_S5G}BqaF3vqE~-rxlZWB@^fL@Py<Z2?2$^=XuG>w=h7Dr9oBSmy1~kP~-F`|6)T}`tc?I7$`Q>5l$aEvqh!jceNEU#>Wld1KMWUppOrff4{D!tlnG(~NAOz<tUU82^u0_>&x5jBC?MQ69BE>0!6biT(*8u_Dt&B5B<FLp*=L|4F)ff}3Y2BA=HMFG7=Ad9Y0S*dG7l5PGj(V;;6NElySvG4^R$1p?5sIOt4;I$*6*AmYdBh?iAq-ZERMGCv45`-F`3+(@#~B@UB$7LQR+Md9)y!$GF7*=2iBf;o&6ivm#bfn;KL9BR2_dwsSqkYWw3R#%iFsX|hwXL(yeIx;3D!U3&-tIpE(_6o>o%?mhe57g_+=bd2*t8_6?P8jsq_xp;;01@tBb@hGs=GRJ7yP44DM}yNta3mDMX8i=BA^$zTDBw<A7DZ>8a)cISkJn$8&za^Wn=Q=iZ$>a&+gzFW;Lhl}g8*T|dCqn)j1E&+F6yu^`C&*QKZtw)!#LfDAi-_#8M=_(G0jzeQHxKhXuIbkr5O3-yyw0wQ|qyyhO^o0P%Yns65h;HD7vyts_D?Oo<i_&w|0U4=+PkOA~dWym<JN9Th`?V2F%VqqXHr%Urk9G07)E|J(X1aYPwvxZld?<#@Ow@)^1!{54#uTInBlGAlOJd=gB#sV+jIs`lcJDe6h9=G=eusXLLR<L<=NSn-@v#V2*LLSPLMCIdhQKZUknx*zFu-yTbDHkXsI&3YMG!`nbw}c|<h0v5GHC<&0!VkEEFTH#0MjqsrN)w4rK#5#r>oA@U>lX@xHa7!D!i;a9ENx-V>^!&x<3#=t^5gIAJXkzJ$LJ{1)DR@)k_tPn#CIyTmGZ@4@2I2WT$MKy)hLZihn;1K8if&^#INwd7Jr)5FjJVoWZg)4#4(U=WJLbB;P}at{;6N$4-C%vKCypMAP2g70#NX!qbpxM;$7-j04_`4s}Y~@EmyuQ+fo#e)>YvrDB_K}E8G93p*&QShl;YsZwd;&tk;w^MOib_Y$++kT7@U}E-NHw$7jZg=h*`nmt`q9N|kPxsSBhfaqZeMu1Cujpk~M$ZGRd3(g*SypA6lTxNPVnoM)ZPxy-u3XX*glW$FTH+2c!>WhrW75C^br72?Oe9)^!9?9Ga2rEo!>W;&M4KO8mw1FXmL$|3j+(il6D_{OxX{t8Q1O=NR=+AVpt`(pj<V(V{gF<p!_L%jeIRp#og7@G6T^8ql&n&OFKg)0?QDXY$8-YTcS!~*{-zk}$Z*9pFPzVXeo75Mkhd;h-j^(**$27k}x_4ccsg@p^QIzWgDPY;&%1dpwE;J8x)*iD*R5U4(MY*I<ApCV`L9XUK78Tk(hbtXs'),'Libraries/Compiler/gram.data.☾':strd('c$}RYYj0CW_WS;dyKE!fn?ME8BD6)8d8A!cg@S<HcGqjJoWu=LY{#{o0#dYc34}mP*1<qf9+);@=x%^ODGBK=NU6lv{l@p)e(xgX59~Q}=5glUYm+p}*z-7Z&Y3gkH8b}8pU(eud4Erj|Nf^(j~qL3-1psq+;DFuS9ZPa?zTT3+kbc)eE)4^=gyt`>2tW~2P<_yS8(tz;ru<QKJPek)IWTr$3NtM+!0h)ZNRg!fPaYqmf|oTi@{im!+0!&F*jIoLSTnJJYhiI%ug-&<zlwag8K9RWB&1@?;kX9I9RUq`$MPu70~e$J^n|Z^c*)py}2R3FIV6|2M&GYA3XGN2oSL$a0t)_qR)J0umCUvrA*%MINZU9M4uclSMrsz6HMH9-pt>4#>V@G^LZF|gWJ#Ca-}3d3Yp5_7g-qU&w8Q*fwF~)s3SM;jv|KL2MfTA*U7Mz`$|Q`=KgmKs)NM}HlRLIOpr|ebhM)jCjlnW->do$P(RTtpDp`+nOx2%B>t&P-w+K*4qGunpR`z@j1{@)>3@pK#?tsx1nS<im%h9%GY9t<#eOQA=@-x-e;;;L)HCIQg2XlT)tmX+Gp!(^1yeyvpm`Hj0R{5Jp<sLp{yB4+K*9+wf9v;yY6%g8UKBq&BUjna>iLR6I{V0QD|(S-{4?u<UaH_mJFa1Z!z|urFdC#zMCR&oT~IuSa2iBwFWchr7|r+Si}=@~LjL1fw3g8VCVm-HPUP>cEKg~ci9xkBf<Z>{^0!>Lr%M@BciQVQl8#<Fihe;frJvCwdS}K$eJ!M=)KJ(l`4~{>nzgw$`%0V82plJPcuTJR8~S#*Cn9bPx5nie-Xr`aTJL*|8W^vp{&2)mZqDW;x_i;T7#i(Gs7y*)xS~db!nB>RF1A`R3f^)C1n(&~Sk$3H%;-)9UtS0r%`~-yr-fPbP-@yCdklCyXxx*)QWs|*sdXpfNhe7kn4XfOknDyX5%{Z@mRhHzTD0KJ0H!6Na-|zfbGO>fg7I1HC&w(B?q+Fvd>;X7+_uQ(rOhG=nwM=<wPgzxe(pJ-u#qt%%G$C&SjpzO6WPwxpTl^aEudhF;#d+SdpK8yHzMjN|8i~R&HVLq#>WVdp)dSGDQ~wkd4@v*D8;U$#l+hQGv&Hc{}7@KA+p^CcW$?zL4a=MD^vjY5g+1;2b0rdIZ^yvzY57op<i%w{VJ3>(Wam&v|v(cf|+82SrT#W@mE(vxq^xr<f>IfjGq<m^auOBI3@r*6kH4yT*Ay;{4BuNV%A)pOKIq|Zwm_cD<tvYQp2*HnYmCrij}28To_i06+z6SLoAM87MqU5L;7tYrPRx?Z_$my+qxkgfYMZ*X=uZ7<JgL1Hr&G9FfgK7pPnNrd7XNH83>Y>Cabi9wt_8=x$!!4&N>1K;a*hH-PI|jw2JAPN?utwRCDUlIrZ=yff{2<h*eEPuQN_Clz_CKXcMcqAy)sj#OiUx6dwt_cP*t>C#hL*5lKyIeC6C=UzTO~azY4FVC?v?!@+bwvOA{S^h@op)zG+hpLA$4&eS>%g%4*|T7_eS`QmVirf1LS>d3$u|BS+!%jA3MAXpg5_hw5z0J5fZ=@HC!Qiv_jHaodBcnShHWo;EuMKjf%>IlH$EO#6~!RnIsrEKe*VFM-4T-@zDEc&?0heiQ6mX{x!07U9GGY6AIZW#_rdcOrH7QJWj^umBZ@5z?wDXQ~TnNA5E#1=S{b{;GYr_Rf|6U8}S&3<k)ThN%aC{Bu_{n{exkblYtZ3AO~*uS=D_S>>H3z==a3tq^^1ogLvlQ_n-O1P?Rr-(`iluQ>q6$r%Y&xN3$g`tTSS&leRxu;JJmWQ&XazdO|(06>|A2R1Ux)CtJRE!^sIR=G~L{Us!k^+@HihE&fVmelk&xDIrS8i0Xlr3i~j=H`|fu=p#SbEZc@(q*)D0iXUgYq4ee?fTw<q?#}X}n$81mltv8fhjMN^F9=U&ra<)L4=OjW?y`Y=N9s!Gt;%E;uASXX~iF@CGt#UAl0N*|pgiPj3W$Qg}$Py$c66*UGwKOjfFrM~@%vW8)ir7Bi)RvOh?NLKj=mU~Y6u$iq4n@*`}q0yD@CWYrBp^Vo~GgOXs<^OBr{Eaw21F3`0j%~|{v9Ap^>f)wS^1l!4WiK_eTeQSNkK`3Pi4Qudyb#vmnt~}VzkTIRaGj19$FZGExltq(rwbDGib@eOdkzRd1D)2@H7-};)oY6m6VU}i8#I~OJD;bT^+5>q_s;AGXOCH)2mT?HLL}+F55f<WuWr>V&CzBYxR0?WX^#?{OW#s4Pd8-S~*hrn`89*^l2ouET4;BhCnNgT&u4O_jl?vS{jH%tGEryPuc|NGk!ar@bbw2E-5vtSObOeSW)uA1oOfqsPYo1rmsxz+J@&UtTAM!R}{?&cK>P|P+dmx?Kxhvf@ni@U=wH<q~dgfEC{vosDv;8|hNOyUoE;iF$!Wr#8_^xPmddX3$@ZK)Z&8E7jXGc0I`;sOs6tV+06C2A*|8Y|r%a13Z)Y2(zLwSLWK+hE@*Qs|0RL{%qNhmi=_c)Y`Sos>tKd^F*_|^c7d($V@z?xAASPy)E#h1hf`NAk8CN)-~7O66=m_vy)I-!#2@`%i!%_9idIaqbV+?rWhV3Yv;N5nYswFGdQ=`(Gov#ZEfw~(PoXFIGmcaiitjEL34ow@;1&u$6?8aaP}?9x2);jw0<m}Eeu5Kt)sB<bKG?cpugyevxJO_(8kM1~{_<gjMuWXjp;*_cZ*dx&v{u6cCS7)vo2RW>>^M@!KPpwER1B1p1p8~H7R$l6omSHO(qtvkOeR1-V}<6_zkVXQaPuYHc!W$q$qM5H3}@e84Vh2~v^*>m9c;;ScxJ^!oSN_(Rz$U-1n#<LJC0*@%~!N*b}xYXDiTzR-Xxcu$f%V6<#F#9N&s0LTSz*n9^Y=p1_&OK<{4H|cX2hdyqnh$q?>%RDAzOe|E#t$3ItJCYXmG#>9>r)rjr>g6<o9nf!>r)f!wI9}Nv+K1R0P!5m@W(3Ti;%KyB}>Kp>>Z=0<Ry0>Owm``^=QSk;GlUaXkJEp_!7L#@*<Q6U>cz6KUc5)T)iGN?gx$U$mgS}qP?MAf%F{m^!Q(0O<V7^EWYZ;Pp+ULbq(L0vKe-AqF#Kk&L2xu8|qdDipK}obQv`ocXggA>|1D?*n=ucA4M<Z4&_HEt5E)J)&++aW*c(u3hp0l9`4*Mz=LmJeF^0SZXM1w#P3+dtvosIg;ynU@9@0u;VtogY=kPhDQP-ewy{}JoMYKq&KAXAK_8LL7b|Cdbt&Ug;)cd!@{HItj&5@Nfoy@&68q$9u&8W_f@n)KMKdQ;c9XwtW6iF9AosjZwbZxc4rPdXSyqBneXbHDxwx2|3%g{##%HebG)9S8X<0jTu*VT}8_Un1hw-WBg}0)VfD)_Ckjg1lC_EYO(4;R|yaS#CTnMt0?&9&%lEjwrNk0?C$g<weVQe(_lAm@+Cn{1kqPV$K(2;BwKWS28dkX?O0Hq=TsB~+K);ZD6)3r6393PvzEK}?DY~Wo|W0kIU3*8=H)(WBRk<3}o(}ESAqTQ+qZ<>C%(rJ_L4w2upN%GxWB)`WdFVA1vQza~8S)G<<%R(jFdSfDqh||)t<}MB=yt---80ZA8C|mB!6tkg|5aUB5f@tUWoywHBS42vo6J(>QoVs;{;t==3{(zXY@PKvk;6MqR3Xv^wLu$a-7B7GXKO|eZT!Q~LMFu~nmU@-uB2I3q+~(=;)8v=C$(lw}djC;qCNMMECf;@qW!tkkkI`tN_fc7nT#iB;b#e4bj|_BH!g_BBBDxvM5BKZ6G;uiD*#+@^Z86Owv6+-9&?ML&(X0&TyUgft$xuT`u3#%FyVmb_a)x>jfeD^L72JFwS&yEm<od5Xq)O6}%SoE)<?QDUU4k(xjA{8!*kwHwT$$i3W{Sn!*?kE`-ecGigTRiBfzt3uQLjSs?Xf3v10-h@Go@@n&k)<fRz6V442qK#tY}|CK8;S?Q;YPxq`VQr&T?gFUjo#fb4Tdoe%PTddzFMDzvxhdf(L_9uoyD?`)|bw8GB2t^eIl=D#gSGcN8K8WP`Jz!5Ka{!w1)==Y-yXj7+!rjmgdPJgak!g+k~X)v++`i74pk(;J-FHZe_wP%&Hm^h^F$Ga+-tUlyCAzw=Tj6>O)QOejS3{a4Q$b>B1^Q{WNc6Cm)555AsEoqRnB1Ft7dcj$+x+dR+v&Hn*kJEFk'),'Libraries/Compiler/generate_operators.☾':strd('c$}qJeNPle82_J7vE77ZMyK@dz?fWeO;NBl)j|*xlk>Vc?iRfExFffxLX8ces70G10-++v)gt&(#Fv6n(Ld(DHnE?fd<DKhpJ!fn=gvK>_Q<fa^ZLB}p5HvPgkR+2oyWc)j)S$sM>{*Zx*dlQd%*4M%e&1sWqtW#Pde`r%7|@KN|~6`(MckdCJFi2idvMW8c0W{bLjAq_IQG?!E)JL$#GytalkF5%f*t1QyWN6{#!4eAokA2+AS#aP!^!vhO!8y0_7Jdcc3gmxeH|($_kYGP#!}04azE%M^HAPtU-Bf<Ko3qRxiHQ=)wP2Hf<DJGVIReOVG_n`5eCw8b-E<e`xgJUj#=%^K-sR_y~W^H_6eCHdST3!e{wNB1Q?n%J1+|Y@g*%_$&T^kbJtoC!4ll@+!Z9hMDKT^J}_tHBR8CTdhwlm_H7y>uyS|J(hTR#;;RruhrDDkFqF>f~kbql%4X<#7ccV(&z_|cM%e0l$|@zV9QyQZj^8F3oN#8A2_BIJC#Q-flgo#CJdfE-QPdtNXwjyFrq}j25N!t=y@2_pDX10O6h)Koh5!3gucX=;t4cEwT`HftkI@2&Gj0uE^X?jZr*d>G7CN?VWu*!F!fD2Z;~=;c`6o@Gpt0y0xeeN5i?>%(0+>l%wOn9XrMq27A!3G1KFwkF$rVvc7HloNWhW_Lbk6ACwA5@Jv(_i5{d2KzI|6!7T2NQ>{yl+x_xEEXdW3;m8!ubmsI7-%J;IC{2G>qMPLH-rqo({P$$~(8K2<S_)F58NoP*Ev?1&ES_A2l=Q=uIoZcJ=o+%c}ZlUbac!LE$G7wK3|NMk=u&cebyB&;gAAkrYe33r{3n!8(bU$ptzA6@67T#_2g0R?+m1V4i`P;<oI$zR84jn4J_Yr!}vZV*mml5=YAP?NDGhAX7au8az>&i#c%jYt#j7$vSNgbK+HVv^vXfl!#n$Z-c)KE`h8Xiv(Y%h7mmnK9DrRehiRovHERQLrz<paL~5Fp&yhmq-)LLzN4E;L2lFYqZu_$~f80q@fgEib7EU=~D!Ud|ip@9{zd7aj|I>|kp*Q43FldKY~oqUG-Z$5r@c9cH`gnk!g}#wuXxH;>=^@%QMPEu|fcL0C_Kk0%Lomd}_Y5W^Si&_lB7HAQRe<mLL}QvDzKl;4^u_V*M)Urk_sN7nT+a1^MW2IJM#^Ijq32T7fA;TW2NzZDIhTiT$+W&(HOLEja6(*0Zf$y?lrWU~K&PmcoiMv%P=qhflS5&@O?Fag@?2tao;R}hW&`JyKO|0wbS+uQ`sfI%9ZAIkU0{(y+23N5B$f(ZyQ4H+gOlG2kZe1<;~07HK*_`C~yog9p`+QITFVG==v96slVPz9hlL)BWl#18P3G~%Z^T!<;ac;}bxkXykhv>&!FRkcS`DhF$8KSCf?fQD)%22@RpTpaMk0#o3O>vcF*s3Y<ltxhB$18J0TKLNrhT;j7jOIqN|dXnU55jid3o?Qok=vC>KGQA$zOapTTIgRG;`oz5uOcS=Pf3Elhd(YrOnNtwK<4m!lSV!OrJfbOu4aJ8Lf0QL7EXJB4Z)-^j<}-(g6<#aqyIhC*s<WFL0j&pl&mc?c3{`t0%9OAHMpFV9(m6vaL=+aZ9p(bSk_d|g6f04J7_NZ0;)!jwxW^`@Ux@9Mhw`pXgC<S10=Ih8c|H@s3I=;_IbAN7h(>ix&4+3<s74H&Hv`U_CC*E3`E;pZfglYcZR&H&LDE!C_dwPpGN~-IdMsOXz9~ZLcL=U9uFj%zh2GFZSERR~)j!WxZIO^d>l9xP*jtdb;ygL<)y~@RWcc8njm=+cN5jg0KCL(W`A=2Dab+0)SEcUwi7;VI;ivhGDg4Uzy_@C~ImtG2Z=al+f`PWuF;t9ToDnVR2Ui;0VbhjXrPM~SVU>JnFEj!w=F4iO3t7vM4GshK;$J;O_xCArmJb826?2X9>#!qL%uUR5TE<y`oKTK21c3x7xLcV_V?>w$ySTN5$9;WTsv=FTsn3WlDO|PQvijWIYiS~30`PivG^Loq&mO56Sn^7zF2mvJ_`5qLGx-uDN6Exkxx^qX0R|PO%8_yi)$v`x;C7u}IFsS@9w@>s3C`zU(^)F81sy@&XY@3QHiZX~6>84M<ZF1-7B}XJIZ>^#gw|#k^n`)ty+A<hMh`EFBV!$1ZCG939)5w}B{t#Ki0{kzc>+Uc`}PXH-@|wOmZ37{6sx*B7mDRtY*s~wIyD$}`77+|Q`mWAtX4Ah%|u-(6tbFA3@j|RFz*^8`~lz6=GZ0Clh^)<IorS|f*mt}U2il>rI-jqA%Tf+rjka5Hysz_5-nziC-7D-I@w~zdmCK}6(1V4b)Zq51XZPAF+YPcPi-TG5@|Q9(-37UE3d+*k({va*jaWaPR^oz&ww3{!5yp7Lu)j80(65`v4k#}!6OJJ$V5nG7-%n*HJFZ2HT5+RuYt4tDP<uaH(&wz*|D{)&1pY@pB|4n4l%zs!tyqga@%!zz-D#3<h<Ja04LP8fiV99N|o#y'),'Libraries/Compiler/operator.☾':strd('c$}?PTTdHD6n^)w*zVIzGa)!pRmqYoaZ8Iruw@gf%C%M|ULp&#YuQWWDvD$X5N>I>7(xUX$b~imT+=v#(m*Aq@A(bvV;`zW{sTQTJA1K#hc-1jnq}r(zH{bW2GLPE6^?#`6oq|t-VBE#J&J;mY^Zrd>DRM^2}8!@PFn9vq;m)pB+D3M!sS9?)QoWqq05qA!Z_|j7pl9XYHBuNsEVFptDepM3$1#lKM<rNv_!|+T6z$zpg~>Nlw>Lkf~`ZTw2{(sSK1Rs;)<Tpvq_n$nx)J14aPondnjk<gSkNP-scFE9MCd@xklg764MMSzRx$efJ`ixPTf|KpLFY*isKmH2kB5aszgI|=0|CfKBd1QI!&L`5k!Z<(ys`m6N7!pganLbx)4Ct8f%Ud@ztmuGnN%Pb^#jZ!w6lZJE-keL>QsRus#L;W4hg7(6Ta5xU#o&#{QVLk&qa=8ER*Ww&@X}o1kwvh+LRbN|QvWu$0h}60%iEUrGKiIbM(MDTWHX!Q|e3LU)+?Bl>`RA#ei}=A!M!99=?~T?Rntyx!RniSmf9(ASU~=K4!>^3W_ynp@A!;dOKJ_tUqlf30quRL%7luzgzm+1z^eakexka~*IcAU#WG=zHYV9r{`cg#$r5F8Kfww-?LDWBxc!^&^yLZd$t-tLdDI@|X*EM(c#Z!$mqz--8Z>?0;~Rikm`Qk9X6Mf<Xz%AJ?8t08Ii&D}G2msmfT=bb}eK(;{s1RN&^}K9+!v`MSk}Q=kt~jHj$fJUx>mcT~eEA;n1ar9qy=oKQBga8(ZhLOd?iKBiON?6u2^G?>Iq89l>963L{}r$XhcZZtAP3!LGHnp3lel~k-GO0-BIyH@F5kh^*St~Lk}#@tXSuoUS#J2zM8ij$jG!LS%vHA9-MngJ<HGCZ|37CeDqk-l;h+w}rNSU!`zK{96x5D6<%r`0kG)|nfCOUfInmP9ctgv2W?WNVe-<yxh%&vKS+u9xin!u*-DHQV0tIbwCEg?RvFGs#x{2-CaIfRAx7+1(8;bX?CeKJQ@}pLJP0{_n0j&V!v97J#~A3ypi`9+fsd+IPkr?GQkSwS)!;N|C!z04Yt>9uD{<_@(+;9U!Yl(Ezqe228P%4&2r?XyHRDXLW{%P(bYe2i(sXN=cU_KPGqMnB-I=WvGLe+>H)&Rq(;5-~DVB^QFC`3tfX|e=Y8_FsDc_#|vIA(8rB=An-FzEA<#_uh?yb>jHGzs=IamfFKB^SV!T#ehFgS8kI!{T@YP@AwR<vK8Fj+gUvW=oJ`vo{CtvqLYSDBJ|EJcAHcwyqKAz!k}gZo_k9-)!i(eM2@bdf9yPOy{?AA;t95g-Sld6C1eyYxmj54M8f!kE3TzPo{RlJz^hmZwnbOtS!~3&%mlWv+ofFqsgukDVm~<Rw(}4Oz4xiUXovX3%v-<K|<JW!lu;h8*d1XlanQ@=>(4^WAV-bd-Q?5K{?@*r5F*@(b_pE9RWnrAbFV6=ej3n?b#B}k=SU>eRk9XQx=_HIe^Z2X**o3+5ayPUEIOA0j2)beC<%aaSEtdVxZ9qg|!{>G5!dIJHaiWMkJ~SL&jn|KJ1~H~XPvlbthCaVw{!S4$9<&w$3*4pBrE~|Kmk}6e_MM~e>W}=+QKU}F@0E(wN%^@{Z%agphCAAVEElV9%xcwKT`*Ulm`j_dvs<-Fd7`%W{FS-$f|mb$TiZXJFh?JL82wOy&qqLy&52TNfA2NW5zsNvHqZ{xE>Ich7oZBzE4cqllAU!TeXmDa+LX3XcQ0<bn@A6-IhLEPT{n~)-?m4CNdCJpRjaHlLajx6+U-qq{IyvgF~<+hhc9cDaY!sK($>{&bJX?<%O`)B2g@g$O!QVbC|;?Xh;FluR(oTEZ9xA018WG3vH'),'Libraries/Compiler/node_types.☾':strd('c$}?Q-A)@v6u$RUtoCXq-BJwgjU`_=K%1%#wn!pHO3`Y8g<7?-yI$Irs!9#zuPH=;F);`V#x=nLA+@Sn5+&hcq~7!`c!41G1$t(7X8*iv?538i*_}D_oxgAAoIzxPJjvd>gH)A1eR?;W8N08l2+1XVW+tx>elTNb1=TDT^JN(;Gx_3#mM<f$AX&y3D{Olvi~2EsgwXp^T*7!fh9Xf--7?kbqEXPy{{yaA(hbcl8ev$raB6t?lXT{GDt%8KN{^&QVH-pHYy_0Jn<7<D=d45$*0xBCEP%$hFRC(C@%K7a5}VSeB{EN*lLK^%)X4_<Nhv3h{JGVi0<p4Qf)@#%K<11rB|ipbx^l}Ft>Q#Xf*(R;i8K>Q80%!6?2tDgy-r?<5$C3ny&vna-Ii*=Dji#VJOOKP-#13i)Tzyg?zkZ5h#N&7lRdJ7z#xpJ_ayO3H!&LkVU@hHEx~=$`ML5J_CgN)V-U8j^k?YioH5I%AN7y3g;<QLS|h)LA9<}XF{Mc&Ai~|m?aV_|Hnqtw4G}D+pKoN2JSDpj?s?KA$7rHxDR(o&NZ`TrIjJOIsFFqIAiUzftiqy-IToji9i<Zlp4LbM5@5fwY*2PEfn9ROlFR7;zQ6*^Z<8m!`S>^|$nZ!S#W9_5H8Bmp1+9z>0(0_rZoLv*rnZ5R*291PeDUmhe`6c|PvO5TJ4RQ?X{gZ^vK};=&u{zY2b}pm-~6C6U-8X<=*+MB=0E!HL9vqkZJq}L!xYw$g`+|Q0jgcCZF}R=h=|K!7s;e@O_#e?g3VMJDIp?!JP;!oK;8g=j9p88{Og?+kPjYa=j#yIoa)STc)lddXu#w5LWJKvkQn(Kr+Gj!(5@jnUyj8ThD)jCl0JE}=vQBBhF{9{p%vjni%0x8g4@6F^;VGMp*h|pmmSWh8&l59h3p(#kemQ#Y)@zB3IRvC_;ZeS$j3%!b8IxTP?DYRz{NTe7;M}mFFmFRX&0ne8Uhe{o&q&b$!ls|jXY*i8+tH?P+Y;vx8Es@xPQ=s^_u*^>ju!yvbng-b*_ZibIjL-kIim;E1O1`Z#9l_+Dn{tD>P1f0lNhDVK<miPYYq7L9iwt>s=*OH)g{?D*;P;ilk<Shf+|jjo96Q7ACcP7--~I(hca<N{wPhoRRGm4Qm1zOPylDS!y4TPWfoD38&EzwjTs+7XjMp#&#+Y7LYdb_W}wZK`7`B2RZ762UjcKcQR0TzZalItphefH)Ngqkk3u(EUjUwYOjQW<DDA5U8g52bh|u@Qm!nG7H6Tg6Mb*67`j~`^p%FGcwUPo?;GuV1s7;_!9o$6k+j(<Nl;42D9j`5D(AU!{PcI&k-=kpUVzxOJcsT)3^gp8R3s;4%<6@pDyJ)S<LZ<?sq(|T)A@eAzje`Gb9?|*A3z&%uJ^0+;Z;lUuo1|AGvZ4+?uMs-Z8FPB8eA~TVT|1kXlZoxf5s?@`qm!ob8_kg+hW}X@pf3JZpRe~aOMGsk9(69EXSc8LGecG7Re@)Q?D*6YM%1JVp_z0HJ>wm>FI2%56-aRoExjJlmiyOh#JsD`COrD>?P4C8vLeAdq&xmvG?_Q|Je%sf26Zz-J}J{xoi(`L3oV2kNuuDZ4lEth+iA1>(jj|GG2|~>(69yD0Sbt?SZ*{?6O{kh-9+wY6rjR8ZkF&g6b!M^Zv+*BE2!&M~Owds134+!|u-Zox#34w{5fQS@^cLO5<@p0*>CVTM=-pwAfyfm!iXqbg(0OJrrG>E9;k(xbLRMK8-tvB(k>oBF%SNG5+B$aj7*vE{KtT4K46t^g%i;yWjdITe98Drc*;BcQWbWkufImFLP=Azy'),'Libraries/Compiler/tree.☾':strd('c$|$?O>fgc5WV|XEII8|OO&KH3m*arA0llc+FKM^X}tkU#<uLO6d$P&ha!P!K`IC#Rj5}EAUGfdhy7#BuGd~CQK6P1ZDw}f%)EKCR6ds{lfC=Y_toja&Sd;(-}fnP#Yw<@QKUR?0ec)J2lFVWz-X%l0Ia;;9}Mn|#<%;UJ^#*V*x$uKjrVX!JB=V<+B%+~6{eKlBwYe9a{|5~=y@kk<u5<X{U?d=b8)m-(8|i>3wg=5<b`}AUxMop{6Y+RCeP&$s-1ZLDBl~O@oNvc;gK2$+M;nqeHj-=Sxjo1KJaKA{X(9}Z)@mrB8c)@baHKQ+AN7Eq%hWC4TNU2(=cG{F_!k7>I%P78qJ>`1apGcFY?U2f=cbIIRvl;0EFl-?L5jk-Or9VfaB0$F1TOabG<5&0(mVzxpm^|Mx&`k7zcG_%PWdnG6MzrTTz1ijjmJq$BJOd3OoB%0&&L0v@`n`d5a_?G-Lvh=`!|Go?`{YG>^hVPP=S3i8;(*ZOT-BmM8LOW5~BW5&}_h)K=ko)oB_chAB$GbrjJYuHxR&M2M{L(<H@TZaGM^WLbEsQkL;U?=CJDHz~AIU2kVR*igi=e2Ypp8h|#(^-WtP<z=MV{$@i;6jY}pVNNtRr8=}t#o~;!97h=jJlDx_!!fmH!Ysd<38UGHsXH?-!C*L|T~LO4s8OA3W0F-}mN8qll>#@9jI!z;?cXhIE>btzsTsMZv4<mP%9pM9dbJ#Y<y_2#$m&O}XHfCjwZ~4Qt!->;+qR|l8^=Zdr%zP;EBT=osOrc@tmr{sgbnr7BsqTpev2kL'),'Libraries/Compiler/tree_txt.☾':strd('c$|$?TWb?R6n@XI824$Wt|75c23AOuP=l!{Z3Q8QWz(HBOShY_J3(Jti%78wX)EFli`0shqIjW*KAnH!FY(MJ*`$r&JS?+kzB%VR=X_@<Y{Smt@(t>`a#vkgtS_y&E~S=;Ik%X-7Is@+m{4X@%VLb#8dxls=WF%3Vr|(i)hfkXctv@-S)sYHOUzc*`XX9cgVHM`PZ(=veBLH8zZVCByNQV1Ao6)6q>BR>z%N$F5L`i<Ad#NMNYoW1h)4>^a)Xg8=As`*WO%6T>O+Uw;Tpf1?KN^u`=T-5B$r8EW=Ux;EI4UOh({wF!ZY|hVb3>BlI2Q`;#D-L(Cuza5dH*SAo1})Yg{ClmCRZs{g%7d7l|xvnoi0(3?hzT?MG6`3T8K&iXR%E!{$Yfo&TaYq(}oBw%`=@n52o@J$Pzdk5f{#ss)D*$&9Lq1q&FP1a?@~>-Bi#OStmhNWx&1%b&0Cm@d@I6gJ@me%m^fWc(Vw!+`0tZP<r5ux}&i6?}12@y@V##+xlcH1sxFzDKmFV2(ygvB=%~xofhpSODYn0CuHQ6Y?GGz)y2cf^>74eXARB)?`6jYJgmFNR=@jCOm~sW-EnKO>Gz3n6}Rzb=DFVOMlVx8JyA%&KR;TsyR!z@Pvp*V|CTQahp%Kxv}=nVtZ$ssrt{4g_=6g_uW?5U0qMkPa92y7Ypq1u(0O1Ffk{BI1Z8W-H;g&FY-xxtR<=ut#IA#aL?B*Fyr_Tj!>Rka0Kt^?fE-yX{l0NsbBzW&XV)>7CynC;54L=tr<%<1I2FrdGtX7rsAZ<a4r>8vA<Cj9}h}$&}WR=Xvyd>Z<=gNLQKy)hB%g<R2B4NXVWP{Q&Rl_$0Kd)QBY3)dFdQjJ~Y=IdH50rR8OhNSZ&||5<4+3u9oI59FD3uYDQbcJ*u0Lj8!4+Tna@w(N#z0n;OycO5EoxlcDVp#l|Cij6Jb|PjNC$2V;Q|K0VK2nraGFf*<KfE_!AD0{B~P9s'),'Libraries/Compiler/expr.☾':strd('c%0o@TXPi06@J&R7*7>dJ<3G2THfTW%OHr8vW!#+o|LVvWp`w6G3;(;M=^f0v5}D-Sx74pg>VsO!6A^8FOUF6xGMeb|6o1liJy>jx=&B{%=Abrz@#c$g=V*>`}Db=?{vfXC;YRS+262Q4Zr>Notf$5Cu%ju+&Bt?T6{KkJ^$UXbE+QpnCCOs^*qm)lMfv^^48S!;X_liwaKZYhmOHALGA6MtYj?md@(vb1Eby?W50C99nY(dG=q7k8MHgipw{W)$_>88pLi1^4t$v6D;f703nwaigSk=_#yY8?aU6<LL**(laOCI|8~1QddIR8#@pF8YZ%kBJ#~Xw3b=Yzn<%Bmk_$B@%zpog7l;0f2H~EMA<A8qzYrX~X>Ss<h>kcsU58j`!j|z^y;P(a3Fo4{Q#r~-J*$Z2ZfQ|ddI_<!NjlI@9Q*&XW^IFAW?z5|xub>@+uotLz@X=q{T<Awtt$=F<3K(P+u&1Cu@W=a<Hznv0;-LAq`L|YqeBgSS|5XS!m6z%GP~yyYA}4lQZ8k-|il5fJ!(yj`?Ce~>1>ERYDHR|~8+=nfJ|_2qu$npSB3JG#K1#lHqo3OY@e_n5>r0PckadhE_ow^IuGqydy$TUVl0S)Qju)6_>HGc5H%s!(NYj`SmaDJcMAru|D1zkb)tDy5`cDt8<XFc%WuN_@D_gnQ@ESy0=l|5A9nMWkryMblN)Y}g&FDJC+{weDs9AKO<thtn=k}2dZSYG*ILul(!cU{qj$7@8z{$PcrvRI20mPR37eJ_cNcIzl&>nD(f5(?;JV{vI|45Qv;8>Vu2J(Q)p?3Z?;F3U>zejx0nCJ`Fa~kz_yAwNSI?dMn2TrGp-vZ}%3#C%Ie4r<vuesg<r8zGvyCprzxi_Q|g}SBo97tQGB)H@+q9$i7fhNxLHHNkBPZ!|d5}>korjKALz00?y_CKmH<X9GL2df_;1-H|!?L6$)LRd5^U(3~*S}O=5+`6MlidT14CG`~=gBZs=;mLH8>=L#RE@md}%ILtxXp}HI*dL?!c4IWCh;<0{E~!-lCNYnVjxvoj#{#Hh6=^GF2TV-N{r7#>gYx2-<;6(8!c<~;GA5SffA@m86$fV$=P%O~_&Tn?nqGepy#8QS`%)Cd3sGAtacM+==|&XP<Dk~4hoN#XX>Ff$nSs_S`(tKLU@z7;id0b`;(Tq8?;mH1!!C8BuynvHtR8mM2s=-|RReZn!v<L0u?qhE%bmrwoohEz$x7>_&o46N>RM+h0$V$a7kBQR-;=-~M?lu$TT8a31+KZt|18`b$!4hg8FrNt6RTzRXYP;d;Ds1LEwcY(n>!ZZY58<oJ%?hj&lmYq@m!|oC+aDHbBY<lJ1hLU1v0Ggt)T$4VDlto!5nc!_ek8Sx0?>qqa>Zo6jN|UdVHY9x00lOnLlA3eMT%bLNHLM=wYq-C8_GBc&=e{BLi>rq{WURO1t$aPKD>X-^@j(4no3dwwNmw$6Tp6=1Nt9t*s%Ow{!e^{vBEiz5%zg1#^G=My5h?K+^jUX1;8SNTGh;a8X3*tmU_HJreEn6)D5INBt|NWzoX=$?|F*3W_SinD%(l#Z!V>;VV{DyTZS)qS_U{z89*M?ny@lV4=3^IYkxm91Co+Bfgv<1OtBMNCqv0PC;%zT|kB0J5l*~Djf)~74EqSygwCNJrwZmZ+wd>+%}AH{$DNd{(G%3C{UDzBFbHm7$8tQ64AHQ)8}6v;yflk*q0fxl)S*^MvR*X8e&bRM{I;1n!r_q41uEMG^RC(bWcPJs3_ba{em#DS|pL^8_FSR*yI$<tA<4_O2@eQDN^lNz1t1iO|pHyb13lpoc(s)quc4SH0gq7VYdjgEJ=L6Whh>Iuk#BC!)%f*>|t_+2gUi6KcdL<Tf#&HUoXqTfi71D>`G+?bQyji4pN6eez_WSO($A$&}unp4Wl9JMbRDuUuc9y7UI!x#3A%xbsp<PVXCdX#?Mb4I$?H}z)UZw1!ubvvXJJ$Y8CMZ_1asQpKqOIDLoP^G)SQ#bD?Nu{vwi-d@H&SN5!-eKQIm7(P{z4WGfC~KkHIoC8tOfll4Ez(O9e93qaE)i6cKHKym@d>|Fd1)Zm(psRii*5u-x|am!Ha6=;-)ydvjfwMaI_s4CIva!LzY=rIDyaXorBh-=Y%J&}}h_$+rCueuL=qw%s%rv#KXQY@ujlp>7e6TB*i@7dgF82a{3tIzMUQCOUO2LfKzk0J#?<(`<GEnB|8R>c6`9~Bl=b^~tG{+!`#CeK-c5-4jFaaYLEUb;D!=Rly%ZCi!ZX7y$HB8Z@z2^6IIg!DlWY%a$Q3ZgQK%##kboXm_pr_{UjS%j&#ZJ1hxL(Y`k)}CfPI+d{?ho_RrzC10-tB_gl4P5fQJ0!&IEJvwylS$k|`_f)}7PwQgxA<dJghZ@m{*534Ps%{gc~*F`T|X5DPTY|d*y(hGs2+oV9_URtVOTlPdmYp+9+CVN;V<Ll5L6#VeiQ=t@)S|EiBz!^{Lc1>b5);oxBk+u>JliNE_SS;nq{5)P1}Mp8bx;!2{377Fv&||S*8yQK9k2O3S>5Ho?)K%fD<Wx0K6$4$r_D?C_*86*?a0Yjbp?4IO?LKUf2Xj72T`IDG8LQWfx067x}G;ish6ub<tUo7oDp&YrSsJa1%goUXIFkTLy}8@F92UW7lQfC9}!t_iN9tZmhXk0-y7*@#xw{0*Na!vNr*l6l;`GHKj=~Yr$Rb9G%`$8rM`(=RkcvpagIyr2ut=>G`_JLNbDLJE1E?=qq||(sPRqwT~9jFUh?OO~{>;NTsSejWSP~8|gUGuS^7`&-{yGY*NEtd4N*(%f_j5vAV57;yrs>h4AJk{|ryJ$jIW9A!lkKBT4-{+7%mXTBI|1rN7R<GL-|k&X+uSFM6DwWCLXc!s46!LD7Fz(4Gyd&mB9ctU}!8H%aW4@8}L<M<)~GDt};2jH~=>EAn0Cw}-x$6{kE6|Fk&enY0}2K)zJ&hng+C69i^#DHcBx)15{lrNY&>hgdysTTL1=4-xtp<>aT5wwGuoJud+eM!K}@ZYbgRf2c>hDB(eo7<Lcaf0!G7?~Q@GvqmLpqIT=<`mj>U+NbAr^#s}Z)5(*^6{`B9xPm}g^qt<bs~7)8mvLxm`f{5v=Ll;Cy*g}#xUJJQ`bJ_HBjpxfXNJJ?qDY7kR}6fYouKcd@D7OXh-B6TiT?|n*Q*!'),'Libraries/Compiler/lambdas.☾':strd('c%02zTW=Fb6n^JdY*#{>p<84p@Dj;VDbR}u7llh7BFi$#rnN9hv^JL(A%$>DxjGlpKmms$pyAdO3JLdz`6bCOK*}HJIdf)aXV<%Na3a)5!>-q7&uzXr=bJH1oDmoH?ERh<3V8R!&ON)k_7w_@x&HCNz~$ag<$;66a)oh^xi072Bf%}(wtd&R`<pGDdkb4Tw{O`6uSiWhwzG`&68GfO-Fx6E?`G^PC+l#YU)SsRIfH@UHxL{yRtv{|E>#ZsK?PM@6Jz2n?^x%+U#ZVw=2>@Jo^Px=xtzn?#hc^c3kl&L(@_`&o_^96-tOGJjRa=IJ5SsZQ{q%k48!F*XYlcg_!q+dcx&|H;<@p~bE7VKZ;W%V;#W&m|FDTv>xSEGc$-mCZ`<C<+9B%py!2E4!+JV$EIB4L{P9-pC75-J{k;%5Bd@M><ShB_40wVsmHHiU{txkxoIVd8FAn`yDVKVDoF~o`Qkc!FH<`OII<!!Gu{8Jk6^z%BY{EM|;U~)P9nf$ZeWyEK>SLjU=#w3W$)5~F+!YtZYfCf|pHyqUlV599RxEzG;wue0GLussW{*-!N^PGOe!q!o;xTE=P(%hMnea9d6$qViF_Q+Tr{WQZHx}!+-4H(*!|LFJe||Y(YV3G>_{LIy#Sf}1)1sG_t%~n7n6h!ZhQ`7L62)t~jn}gaqa%RTcQD?s60fEZtr)i98>#3uBDV0_V7bxXPlL36e~plR>+>SpiXJdm931rfds%C)ej2>j##9LIz^@(&plmClb+QeLt74{5?CmWaJ!Bj}^`qi`4yR{go+f5g%*xN#h7I`TVsQ`baJgI~#`s3x0!G}Z@y4Jfj60L}2-jfT`O+b)oEDFJpetramK<LJT4m>!cquOG?6mP%?|}~!@bR5o2cEPvDgKoGO(6tzdQ8hjzRBh-{A4*kP(AfX(2+Z_fr(RK^%-O3;^Bk6MMuufcn4kVHA(6x#DkPK7+qnlajsk>!&~=vF_!hXcjBZ6G85uCUfzk*9$2TjQuA{X13YQ9U_Fyg|9~uL;Ik?uD%&MFMJhWMv(XMj@u=6X21iZ&m5$HHTp96{E{)Epd+2zId$TRNhbmX>-fW_KjVMLTg_TXhKm5EeIO5BCRIFBm*6LBiDh<nO8o+Lgvs<_9W0H@Z)$l=VjEYHy@i0Txh<7d2#ujRmz}GYZgYgE&+r?9L>U0aWsfF4fBq3WKj1Nn5Z-!j8cB<vZbyE$Rt{5yiO=x!ln}(PVCM;8|&zIsRJ;KC9<awKsAB#M1$LB#*_olRk9=0<=(<$*N#1eRD6&Te#E`^Ugd?hw@)p9r8A*bffK!BaK_S}^TPB0N9m>6qfB1keZ?}imHp2AE@s#5EpO!u_hSY%|aCZ&of$Z)7eL-De|5BC9M3WjftXq)oSQaGj+&L=Az3yE57N}={cRH0hf<nd!e&o1e*Bi*I7A?HBpwZ5IFb>YTz%~-mu?M<U9i%TYHf+7i;-1U|96_>9^pb=}uC@IZ2J;dO!7~GXfQr+JY%EpBvHXg{il2$@HOLOx>qyvk^b8%Ve;+Xa}o?vuoZtjDAL;JRz@cXE6Hd&a$7=~<3GTGMfO>|C~JE_;V-OeK_!ceEgFs5^{HncB2r86r@>C7@I#WH(M((rL{Uc8srk!HJnaIJx@S-nQ;jCGnHzqdP0vdp1~2zDb+O(R4VZ%doPUes>4C0PPi+QXuCVKdZ)&AKjJ#dQ(kmzbKmO3}EwPOIz0vJ6*>TvwuZV=C^YsJzcoSy^*VO_H7h8#d7xGkqXyl=?nIB_xhj0d>daaTU^#@tUh{Zn)OLh@`78AZ|57jhq=$m%v2S#G7f(hPU{}Dz`)E7!`@e<E>=OZQrxT3@Ac_q($1QG(E8U+9GLv!5~ZMhm3{vS{>$%Oqo45lIoXQg7z1lT6j2_y9WAwPX;K>p-+Xl52*~s)QQGcJ1L%|u$ZTD7L(Y5?d2w|poWC$Q?{Hha*kX8=hQm6tgdJD)tFy_DDjA^qMi`iRpbRL;1F>)4a_zkGW)bwiK&|sLo2obYF~+SjQ&Cy@7p32cKIr{C+zlQ(9w-0JVU0A5U#emW+Ik42@vUsIjTvuh8bGki1r5pb@;N@tUW(%s#1-HhcFPO;Zl|d)b_yS^7a}}y)KDaD*5(NhxEoytJ&INP_PKIsj95QYO1U~xo%WXW%p^G$C8Mad4ugN8d1@b?MPBvvi-!^u79F!7Kxk+4{FhO)9H!T?j)busR<=oC8>UBsI5^c)eF5_mSs?%z%kZMJjat%R<<wTvo6nflZ`wyL0jZ3iHwdY5wM!)AcIV5gR75luv5?xj#=O_>INRjG^Pazd6I!e7O6_BJ*Oy?luFfAQYLl-5rSdyP)r*-fK#IiC%Bg)GOa|O;t5Y20-s?e8e}yyWR<MA8MBJgj3nnW1wroC{avn}&sav(%t^dca8b=GEMKdMC2FwMaO_E5g}Ve@@Y!in;9K$9xUFhtYu;-Y>tPf6tT|UjH|l&GR!FGl#k|6or?B-uTpLhB8o?CjDdZ$EV#R-t1wiZz$Y>i+%_8lpuL|^+xtb`0?HF|?=Zzq$Ec{#;41B1ESj#nQRvJ5EG&<pMDta!j_vZTNtsBo=bq<M}ssv&VmwTeF1tMDx$=0KXu3c-l<&d-2?0EQd?mZuedrvE)oPIdKA2>!J1IK^)_1MuP)e8O}33XnhHBN}zV!{L4H^o0h8Rh{JjAmhJ_E{aq9T<0E+=KA|#te){FrL8p8^%8_{S4ALq14s&?|B*87)2dT##ZU@V7b&&N<>$S8CIEWYTc!!rj8-h4sP9lGSmT<'),'Libraries/Compiler/rewriters.☾':strd('c%0Qe+in!smhXH;rJt%y#j?%JxwKBtgczR;ngkFK%^7*DQoCK47VYj<ciS`?%?Jnyn1Bh!Hg;?R4&#Ibl8`G95|FZ`^El@dj^xLA7)4?}VAk5V+PA8%HlWd1X}Y><U)ElG-PhU`pPVBX4;}djKZ@{b|67L+9zGgHzF(-7XC|l0?LrVv*BX=MTH6mozfcH*AY^U#?%Vgqn+IRt`{t2o^v$uo2cQ=n>>tPcA*E9g(z^!_!QEio_h0pfy&#y_<u}W%PE={sJH?XECiBQ9`H9>M$$Mn0DDHKO{@ZW-DH=UIw)g0m4}iT6Ao=7Lxkna@rSS=bY5;B>Xw>5n9&cZ`gAG#K;oxwe&BPbvlXu|uUH&r&{BGbiS{^w|J|sW+^wuuya*eD-^y^ddgnqB`?=AklsjX#!Tn*{hJo~zWU&~~*1Q=N+m&sC*cDl=kzR12-eAY7vvu9$hm-)|Y{QIW(W{+?Cd>B6Jd=PLL<a6HOqSgUm4cM}$;$vPbKG~{v;;7xMl{;;pLcd6U3W~ct_`}~z<S}_vEd8rr`1Qup!$MHRiw~aS4#36oS#jq<A^5j|_IfQDX7E_2)${?`>*RBvjj(-so^|8<dbBkgvwjFqWP*Ty)nlG7?~e~n1cM!~TKD9zKxtFapBEz>7lu!MBD{ezkXRFC3po)`6yW7D`KDM(s2ryWIcBx{!xNnD_l>>j4+nTd8=nD7$K#-uN*>Ve#<hY8iVhC#!dVJ_4<(m$`#$E|e;XG3?Ed2?l)Bq-2X=2pa_0!|1ee3f<&XmL9)Ng{4zc#56?bM^bx+wsn8UA>#s~6oNwRc}KfaTsG%i*;*hxeN;53*Bc3BW{Xaq33<U@<bI2GWYGxEw!T`!X$IQ(xN+{Z@$jQouFSS4plK)tJEE${{R4pth?Q;6tX_~pozXg2Um2kcBBQbV~chCPk#DbAq%Rq_d);3~OqqR4@1K=2~%`n*_Xpe`6_mYBA8fFZlzT@WnEu)_H9#7PtvixyAPwh}VlT)>`?ZV-6o`V?OkRe)MM&hBa}1{dlciY<C&JoqDM)z~E@Tx{UvUR9dlYD2z|l@}t~<mkQ-{h?IlB_xC*r$wO<!U1T?2zrAPuu0gr{4D06P5y&7{Y)$-7^K9$On&AXZ6yf1K<d?FOx1h=N<N4Im%ggzsWsrU37qIyA)n+%2afKgC>CF+N{O8T%3AM-1MFg1!xO4f-r&W;Xwg3-UGJ4NeU#7y7bz5uaOZL#pk+n}T%g5aG8&tJF(fw%TpE%uI~O(|XxOv|Q#h8=3*R%&dX#7=L7pX#$a@Moo(q(oVEX*my&wEvp8n6ppMN}2nhU&>)mqJq=i+*2wp^>7@+$DJ_vc0bUuK7fMn+DsuW&A)Lcz_y4so@x<L%1aCm2}lj*t^#vsCE%(PCoHGjvU(*{L?_=r}m6%yb1Kjc(qk2vcsM5zK#6HImqd$Pv_J>6AFu!V0<wxY=sU;R%N-VA9$et|KXQ5k4D{FfglAbUP{0p!lQgo9IIKx~viG750>fcQZ^vIjIUtnwhUX%rpkXUQW$c;)q<a?F67&fN_aDWXf{|)=@I7_Ba?k7@#Zz{`rf}?5T#H&j129PZ^4vipM}_*1;1<W@*=|mDnGqRtYEs!-asqy4=mK+;4K5TqHljBYZF{?ut!0OTHx6inu6xCHps;qYA~)XM$dYcA^bUVv?#0e9=0h#l_aJVnA276W6C`BXeO|2XwTn_1V}VO5|AOW|NK;sF<}Zvc!I=6avlvz(LU4D0e!oop~GP4r{UjcG8jxE(?FA8Es!U?cy2RVd=?5Yn*)q8*Qn36)KV<xgG)1l|S}O&`1JyT~rxwLa?3$yxp1Uyj;L35TUvN1-4KXd-DEgy!R)GxvDfA>9shvfzz#KG+8_0km;xp))J-NE!rzr1+wHT7|kh(WdlTJA#e(7r4<Yl9goXXN=u8QO_ol!iK&Y&ciq_?D&|#Im$P+gU`YprakfyW=^+uEv%P(Ko-I4KJC)|9zp!{3+(9}tkR~myU!HD1T>WK}8e0sB)N+L(KP?F7VvV-LRng#^au@ot+XMQ291w5+eSurTJAmxJPhb3H^V$9N<({xXOBZkg2m>}Y<nuxYw3GvDjN(!u69AZ@O@$gNfog)yl$)UX<4Uz$^ShFlOVT^yJbQGwSmMU-Rk9*P4^=rnr|&JYO6{2IU&7}r_<ReW$MAXj>y6bj@OcLoGXC4}cj53zI6M>%?+Je&4x^XCZK9(iAQQ+L@CVm|!I|=jxYH`v+su1d)91K(4?bVO2j;p7bKSfTpReKb4SZnUo8Q6bdj%GFejT1){|4cr0m`A_kv)I&x4-%A?|xsNtN<no2}=rnL`9(CoNkE_zz5_`rhkfm1+PHGMVGsrXW-Fo-4YYxq*|wD<Z2>M+|%>#r92=oT>7wi<6SDVdE*=82aLC~#>2k>Si2yu5ZPb?#;^~82_s@g4+?i$wqS>wQRh@MZWl{Zh{ZF_&M9mTf{Z?YcK?$tab2Bhip%!wB)_aDm!0;hHorvwtzMo{9z@f#owm|l`wb(jzj<%<7EUv4-WXAD#O+GC85bmd8cInj@K%JggULP#p52a&_VavKFC^BwhJI}>VAiN|yxellq;j(YsxT}agUUVYX?~#B1g#5!!-jDJlfpj(EFQT=9x;aa#*~N@U1!MM1X&KTsi<i19gfnFnWD5`VM@EjxH{lZLiqZe+)`C?5ZLSK<}$`)Cd+q%S8sGY14i8?P;3hhW)d>XfxB)H80*NlEB&rRU4aQ=PXTn6JS1P@X0DO*`p}C-e>cDKSndr2b<P!8l85peX7q9dq!||aNGDPG_&o|(Cvo<<v0OA1%+1pMy0jo};;hw+rJ=;NL+{qFhLwPNxMzVhuB46)O9F_2T`DPX6@`;%2fHiz(o|Q-O)Bv}BJYmwJ?ht4oN3b)V-tR3UGXRr@6g+gPIic^b-9e7m%#bZ26Y5m6__aec|zirn_EpTd&aiDOSC|N=T*}av=!<!(y+ImpiG8^nfnFb06#K7<wa!j`i#~k;0o|>sa6MDFmgq7JgPTZGv!(#2uTuXWeZ7No7R?Q3iP(@7H_NQ!ORF^eRgItc9<kCja`qYv3;t_`p~eoFoxy_0;nXimV(AF$=v`g@~;Y7#Er*TGfl>~4;|URZ*1See>!mFpAYOieDJL?0J>Ifx^%f|po!Hr8*RQi!G&_&6i3_(0qM3*)&&GZf!QpIyUiV7NR5)@#MV8;*7l`$^zH&<sZ$MT0oxR1(TQ92a_f{u7S(ptZMLFvr!k|{ZY0qMEA-G!qVo<VLj!)#omHlBQKBby27Do2llyAGPelECWH=AL5gj}vCedS!Jc;ndjRH$N@{lKQIx^9}u9C|`85TMgkSy%hb1V$|Z$f_<T@&*%O$(2uDab>zs5b>J;IS2W70B42u_0<x3aqghHAcx^1tmoriZSFP9fN#=9iUKkK-1GT18fQ-{u>S;UX@_(|3`Z56iXQ-8=ytQJZ9J`M!GMBNNo}wW^0Tb3mnP0K$bsLMG&1vv6grXW@=je=yAfdAJ80yFh#{})r9-?#)lh9oP!~PCs8O6q23YuVkXoQ2`u25CDPSolon22*)(!d8aVkVA2$oO!FCjVVXIP_2>9aAz&K6L2U_53y49F%MxAnNI(AgIO*J~j9&V?^>GccnnYS`N!wmIA&G-}s3(A6h(6K4A7?V(Cob=O7QyQrg2p9=`8aF&_)ADGp>HxOOUm-mx5kn~;%2QKq@YOVrY1C0B!%1dTC(2Qk7-uSII66Iw!!j#1!20M$e45dpbdwe)+ux{l97|dUM$;1PwEHNmv=*0Jz9Y|#i|TsSHkCY-#f{8dGI!VLPX9T1yjqJnZdK7bhlpl(2b+y1TJgFhoKpx5>p{$UN9DY8Nzb@u^}TvNtFLC|Th0p%WQ+~$0XMUUyJkc$lnAOt?e1uY2!zx8yv24`ZzrKr5i$2oWSW2jBlQGa$eX)~$!U(7RqR7qWX?qd^a&-NKC`TcUrvIRiNLrP&%||Cg)gm^rk?#4)`RfKlW-rL!IAMEl*D&xB5hC4Tj?}sOO>s8`*GHUr`A+asoOsJf_pgOGI{sK6`>c5&>0g?Kz6k%^~nY}x>;OL$^7(C57c0#{$7xzg?jYixrVFfw@=UOn8XowyHiM^rVxxmdBu#(E@(A(LzB-gXVb!y;!@K|jj#YxHo;o=O~$lJ%sZuO+*C+zOESsQtrmDq)X%C9swt@+6FDWhYWZvk*a!5*<ro`<MCRDnOuT5$Q;*S^9g>Y9=3H2L4eH@b%w<nbFy;3(?F`?(jf6b4dfbXm8UiWrug{fh)hUn5JP$J;-m%6kSSP>~j2Jy2##a(|KShir6q&bd<2`mRgz^J7j#c8(QnZFs$4+l-niUqHPom09Gio$3Aylo~BD@vX=F;rg6#2j^WtYegNjU=`?mr((LCee8)OrU|zvU9u%=6YO;a*T61!<H<<ApPd%T)s5Uf*6}yF3%;#TPF0TXI=o!EnQA%{Onr{3fG8z%h-u((sx@Lz4}_g#`k?+#6$Eb*E29eb=r*R2@Gh{x0RZG&wYAm3ps!Q+J3_nSL8*`8Q_(a>6WAuo3qBk?_=7Lc3^2qexeQlFsFr9R*(G^+5(9GI^Ap*MiPD(phwhz8FN1i+Jk&q2%pxGlpYHjC-@<Cz~MUA88xss&dJ4o4LW$uwB-<+y(6to`yoJ)azH$OE^s<S89nm%OJ41Ju9Qw^m`G|3G;AgAVfEdUlMlcF1Zs>!_LVny$2>AkV{}+u?ESBKH=*G=$1`n9wcy1zzs{~TtVOYA@`_vtQ3hgX&QxvmC|TtXF2v3<@A&y#pfI1Iv>K3W<pKdKHk7Yd9_uUt=is_#;d@pxnf7un6wIoQ+VY0xc-$?uFnx9l`(Urj?oBjDajkXDmKW77W-u@xav=8w?=xL-C_fCY~J}c)AH?csCLCKbF#Qi+1j$=l+`QkCQ}W66}D#&e%yL7!0{uynMB;{pvR;Ff1W|F8A0Q$W!mTFcC^f%z~{%qZ6@h+uQNR#qnQnw_MUB5>(eGPI*f``$zX|w^{<3z&<(!8`#UU>$mMqkKZ9!yHD8(};mhsmx{<ogd&=at(4mPNGvT&waFQISdpIoath0HvMN0RnxZaq;Q$*(3m(+Ev(wy`Bl9r;^f(vR$BQ4k^w(MA~+@p9(Gsr{krRMJ^olT{8;7^qSu>#^8F&|lziCCtY53F>QKSY>^LaA7*a;v~6#B7)hV=1P_yJV4;F5bBS7>zS3h4+_|Zc32uW3rw#@LwP7WLTuX#HMBhe~#KcE6nj&;73mv$ZE-m>099s6@Ohs8`}~qg60%`P2bQR8Gz_N`-mw?TOm6<bA(0Cx%g9s0#(UkpP5)+?<c551M)d1SJCktGdhwQRbHsBd7*?A^(_WMBrJiCy%f>{>95&~IUd5u39;l%{n58b$T|U=*|k$-n#Z1H^|5zTP;QhG>@tEYCD^ikgjLnDm#{YAeVF#FRUMc_p~F+frhm$$Myv&A73tt7Rz)nn>%HokCS@R$h(fz|lYX|7t~;B6cqy5ip*RKczyXiSv)4#qVTA7|55%EQnqjBCSXx~Wif^zXKa;QB<QvIQ#D?Yo$d^~3TT5qZ&=ZfwQ$(sh4J&{&LN>WjC}R36@L5PX4}4A@9JG_WDF_FaEg)3tT(IpRuhjws92yog5~MyF4swYW@_!TfEw|g%X%YW5W4}A{?9?Nm!g)$KT{=y?h-H51*@K7k@VN+|_qXSl;cEdtm*8``Pw$T*eZ5$6hS=Fj@Uv=p4K%i#Iaip_A6ImR>fy0u9vj%XASFka^iuuBi9mRX3*@}><p!6@cm2K7!-NNrs<_&8BHb+0MKx={Iows>KpW^{+oAtV!F)HVOi=VN8!2SV%qmexojOJL=bN6I0b)>T2V??c;M#>y4b>{NiZRREu-Ko3fF6%D(g$hp(-?jGu)&O>I9?z)QocM#M$-i@Xu}}n50H?9umS(^SIPJ%TjgfT+fmNvrbgH6K;*zwuRFu5i2fgnr6!+_PkXMIoXk_1wAzkZ@v(^Zx?3y(R#MTDR!PD4f*;Db=7|gjqA20cb(-p-0{pR2MYcpfw`*xxzVG{@?dox7!F^cD%$3~|$KBX)JpCkx1d#TJ>7+n-PL<zOD-!M)MJFHoa><73WlOy4TH+OQ#<4)^w75N4xg4xyJA>-=-#v3Zo)dxv@{xS0M^Z3h#$%-5Q>Cz>Q(OkZ238}ns57TPV4r3yFi$2^;Q_7>ey{NFg+h*)L`N+v>zG;2idJ-%V#b+vuQY9V36Im~r(4I5YixwNb&?U+Qt>D>nT<E9oA?DY5j1w}MFT@ACLSB{5p4Gv@>GJ$(*OopF!jj8Jf`G!EGC@@cD9%eU-%siXsSOLflFNDZDtADd&o%}tx=^E3qk1FE^EJ2pM4&1`VMKNSGQJ~4Q?r3jzS*ibf7O|B^Zn%EPQE=?bw2+d^0!rXyWjQ2I)r<n_0RBA#aV;sNTS&J{m*Rykxo`R+RQ)CETyUYP}t|I{r}T+K$x2SG;q^PNr`w_fYs4FMInDH{O6}N`%m+TWIJKJsF$jc7qgKS&&j<AX_`U+oHP#YB({KF#@2w<UMPX>O6Ac{*+o}2Ays>Sk^`Qj<g|KHGE{(5v|$jxNAj#>EY9Ir`@9rn%i)`f1F2mP)V&TdwLl}qSCxa3R-c&>6%^>@s`B&T}vx*OdT{70eS=MPDz<KRj2vK`7tJW+FUUxQscxa0p8i^ZUp8WXlA@>v~2%I3q|3duv)Og_UaS&yDH>#B6-UUkkGcS)9ou?yas_Xf)36fC^(E0WEH*kUZe><GN1nP6kG=oS6t^vm~53ReZ59S`WS*lm9Q4<UEOvJ;=Vl8<keD`&oLA+jE?W4Qr`Q?3_iZGn7*$E&cvhQuY(mi4f}+LQ%~q8G->%ELM&RKPj;%{%89Y#8g$8%_L3|43p83>OkVPP5lG?nLj`<ibn-$jxtRs_+R_v!7M8a0?H%0Y$)G10Iw_kmN#X+`GfO1RG!XI0OFSxJ-4=qaByePvyJqocieZ%lTiX{trNs^7j+m+(e!@{XtMR<EESk=dewNuUB<0b1X|9p|Yc^UvDkc~p)fsI0yhqbOTu!%bT7|*wYJ<6Qt8Eq>-~q2O#{sWBc@HMCWkj6dv+x&1<cWCuIxHJHDpfy=phtU>@otYU*V7a-kAO+=c+L=)ti()l?TOu?g;mFd5Ke}myTNr-pLHZX@~1QsFL+K-&HOaxYx<FZEwbb%+s;OiC11nIWe?m7lTE3yy2Y`ryi}HM&>Le%BYfw51RC+c-nYhZtEfoaX*ptO=~0i4=+KD3#Up{T8LmZ}uLFM}i$3zA7tPEJMs!wTh2}$YKbCV*dIg>9goyUS3R+zyNhc34+W&Whf?kJrD=-+ecTuh$QDZL;Q(y5U4oT{-k28<Y^Ku0mh?AC4%G4t%^}wDnb1zCTIa0p3PT5McOi|I!$$J(=FaVr~`%ik7*2i701^U-Vd=I0sKcP%LVr(B3sG0ScocJsh&<!!L5vcXb+?7hK(_Q}yYW>qJ'),'Libraries/Compiler/to_ast.☾':strd('c$~diZExJh5&o`U!SK`4VFk(gCg70DlIjMPEyI$50Isp1c$9ST9my_v_6bD**^(98suR6iNu$=X;nZ(&lcGrEHcmb)kgxp>y<cFUe;~6jTrS`4&I(XLcjPU1XJ%(-=9w8Hx<>C_nEfrnnB9GF?!wH)IgAl9iFcheVvj_oWiK{^d8Zj6%SNVYS(Ytkk55jXot`-}K0S*krl-cw!#YmxcT;FYTV&aMbmjt#T9*;}l`(2q)|DYt$$ODFt>L;8J7v5ph_N+eHTI23h|bMSGV;6hDP6Pa5j~(cYG*HwpR*9XN&ifr0h2d}_cyyMcitTCe`_+b>G;9g`~1QEXYUJ+M|6*F+rI%ZJj)WSup6{Ae(cIfY|(vWp>s93eMTPuH8zcr{~$Z$`EmF5lmDznE@_19mNS|o?UVsL3I|}orsWv)B-?Tt{s3gzv>aKTR^3}L;s85Qj6gg4^zZZse*Iovzn0f;?CTEkakLbWxW?An3juLGywGkoL6q2Cs&Td2_4!2{IwbN)ZG``TCD$<*GbWxVXPr6)R6nIptg#^j{`&A9tD$#|^tAd(O1xHZ%>#B$wB$uKdECPbG3ZI18dxN=E!1>c^L57n<-DXjV{my)cagGaF?@OCiZoXkLS}4Q+E18rOkW~;18nmjd3xM@Z_wxTbz;11-NdDf2#wm7{l|~kneEd}c6m)#!8Ly085w5>Bw5?i0ru!Ux|`5IropDbBu&8Kn2p$x7dvrGlmnlZqQdQHdOIR_FgZ1i-UI)8?}{xbF&f~9@>Jv=g&DW!qjuO&_sZgd0g{u)YAIW;N(4v0o*5mzq6su=u>mClxGeo%S~|04N!6a5I&<l4Ewwi(bz{LOnw>B+_6Lja(QmlCa8>j{^K-;;uQvQeLpUA8OF@u-#bnvgh=BZRsilVdu<p%%(i40e3k|QH@K*dY%CLq>3zb-JVh&&nM#DEm2xQ?;Sc@X$VsLrlrrdiUYP!&=*YSKaaIZ!syO%(NLkJON&yoB~cOgCU&Ee*E;ErlD$&qU_!K#s4EB7&OW;^r?F76Kfo4g*#>jPBcgf{_Ej<enaM-atCb3GU?3lU1kOs2S|Rte}~>zFY&7La}#wVEOJiLYM6zQd5j@*pgszQUhM{IVxSl2T0lnC&Fdpo;j3(m`q*gHMCvlY?VJ4ZjY-F*mn+_aUx(Ztsw(WOGwAPnGo3Hlx5i)oDeh(p6Ee>r0L3s>oJC;sMA2xZq?kGgkxptqst`w;b!YHoEIu>|gt_qkin@Pj-?ghbu7f3BTPvesj2YlL=TbM-_>mW(?_oerAb7d=7_|=-W;;Un%sekmO?}6Wr~*J?mR^ThRL$boN#fuzl|yD-~4iJLiUQn(08Sops7a=4}N(EwNuFv}HJc9irPKdYAqynZhQFCXX_XDwYC_hq!xtMY`VGp4KPypCa=7*js6Z=*IZ;ihh2(H4m0rGUL~J<f~LsPD4Sc^fPl7L$-|4AT!Jp<30M?64CyD-yPqD&jx({1fP4|uO4*2de~jx?5=NjU)<{c<*57kj?~xr!1r=HWT_xdWz6DMnh_~gNqB!%0`F}6C=c*_{D7`x#!puOf6AAg)#tEA504Mz^^uMyZV)a5NC;nisAdRZz${%I0wr84rHV=YGz!YgswENefUZdqpQg#9l$~3xrzen{+rKkeBn<vwTE@GEOegh?dDd_U=!DH*l;Gty|8@!}-M9dCu}P-hVJ8edzm6(g?<IX<NnP2=p%iE`2r~v?)$k$Xi_wT($?SQ5W<!-fm}Z1^rz$Bq`BI5gbb)l)v;_B8U<Aw#tiCM4K?Y_i^<88LMEWx%Ufd?WA?TH4n`Nn*;827JRN<aEU+i^Q$Q(8^@i)0mcES^&R3;q^It38XCgqSMOI1UnN8G<e4%K5fNow{y9Zu0Bp9WZZg41;3epx%0C2oZxN-MQ96tE#N3+f&Y!d%AGVa*j1v_l*_WYLSG3gil)wg`OIf~iI?$hS(KE|L(^{+>xc<c?*J*`8z1hsRFLs_x3VpkQg8GCSji9`-t+CZ*DERZUa|suN~0wa7rKnAqK1nHZmAhao4U4E}O*dLw{6I4w$XX^yJLm6@8FTRKeupb-#5?1$au9>`8cxiGrqWiqMA-bb|am!_vrE}Cw&rAJr<Y%bVm^wq#Els-Q6P7)EcE{f=V<tn0l>G9zJMJTIfI%aV#Hz}y3>TTD<^i%qE&IwuN>_WyGgxFnj04sX<QtT1mA<LyRgrj>+ugaSeBJHT*FZOuuM2kIz0AWjg^+Y-BL`4!il1XBP%WbSxrSv67Arp94uSwj?QM2KCXp|?pyfA@Evevga88k>_q!x4SDv`BHLzHJJ{^W(!pc+MgXgkr8>%?QVGOX3Wje%kg^Af-lNVZP5GD)(Mv12cfW#O4$w}FyEnt}2A1;g(oTG}0^3!pFKL4IGYcJu$SuRSUDj=cUgxt@4`8@GCGZeSEE^tAxiV(bQf-}C@-a;<#d{4r@8tlR<og>NW6bC%diO;Ct`sw4Wwspg8oj7hCbur$yO(iiLAJ}^t7tPn$4LLphnwR|cPh7*LL{>_G8&_~!>?c02*lCxY)t6a$_qh=QORM$-e6kgaTO&Lq3&0<nEmT65o$@#zcztB=()ke&nAD?xC?$}f5WnVHI*grBYT}fJBayi1T(`*jpIG6i4dQy=?aXowK%!P|H6XQBx2<9SX|1#Hpeau#F(kHoUBTb>wc2@@B`Rg(4Hi+A9l%liSCS(}`Pfz4t^g6vWZT2n(Lj-)>522I(`u*GRxx;IS$bqWQiA(AT?ym)<+w4u<7TqXQeySS=Y*o#91@%b*SFrcha<?og-U@9%*1#+?+G?E5o}AZly)YK9Wj;5Yh`ri*G|1bcDMBFag`j;6s($v?C=QJA*|~T0H#fv-L>{M@zDP={Zb@lqNWFr`Qy;Py=d&0i{av|uJ8RnF3e<lF7z0*Z'),'Libraries/Compiler/ast_to_py.☾':strd('c%0Q6Yi|@s@;kp`vXY~2GdT8=yXaOdcf|M}iW4m0&`CaLwcZ_vmDjtIopEemLS$aXCLzIKJ3Ir#A-o|WFCY*kw{&0cH^d+BLoQPOz*Y5YdR{wgxG%Se-JYKAdUaKGRdsu;)ts;<8?{Qa>Qu{q*{V&r&6aP~yi%jtnkd(6|8T0C#&FcQGc(m}Rn>^`sd~-xHxYJ(9Ut2BXHqI*>o2bl?b^M!R3aqTa;91}-)VU{YQI%)j+W~lp*G3oD5bU-y<_LjKMn4Bb;sbIQvcw<jyGT)2lv_l=`|)%oA>S-f?hgI$QG;5qI3jsUtu4zlZ7HX#1`2Kq1bVP-70ymQ^C$p+0p(TdkM78vztKD`i0Z$vkQA$lg|3VOY0Xtfrmc=2L7~i1)kn$Hk=&dlK`ph`PI_+R5cOW+)bF$a{S3w10mc!1dlT{r(T7pU%#CD1|F+U9be5of_A0Z@M{f$``A_J7;QP_@i4m4`go~QZ=|7IdkWKPV+i5F8E86n{;+n1w*@2fv+yw1Y#|X}&Elv^z3h2$JSjMSo;?n8{MHQT;`}l~t2N5?`b-!^(=}!jc9PArC7AyH`(0gczWL&d@4dHu`?hVHH?Q5>vSrKq2S>Zv_b-7a4ChCvwb=@U`0!&u@X||2`G<$0+1-uJ1(eVBB5!^U&26HId=^FXGBjV{&H3xl<ovGBUxQ}3Q4M#m-G)}9>GR%slptTP`32E!iN}Sb_{QVSW4vj>ORlY&X-YSdfj9aKMUrE)>>%_X2Gu;u=GZY{e}NrmAAm-lU>~uMK_H9l6g$n9*fLvTXV_VG4tT!6E`rQ1vCE*UpRrZ;IlIcfVAt4nc7xqyx7clVhuvlO*q7`pcAtICzG2_8@7M$OkUe5Qu*d8PdzwQkcK7cr6#M_Wdp9BV^2BJhj3T|uPTTzFQ~`cg*taCq37nAfXl2K%{eAhZum~hq$_bwK3=L#M`#KH{WWnLEA0;5CQ7IH(-?cLW2LU`_cL|8>47(qDc?5*=9lK3r<BmiGf?oxZK0-9q?l0mGrTV2t3wW!}v*W!(0s<t1323Pr^{E;a;71CE2KKe10N((BCHQyEhP6M#4i-UJ++`hO4;4&UR?5Ew(0v0#8wHv$nh!e&%JoDIg7v1FSp@JITSOV!YUXqSO!L9rF7Nj_+C`>q$!3IF1jD}sweC#G@hT<HZ*i9licJKewxl3o4G8#vzfbn|{-%Gj%R^j}C%ztvT+;Vj;WMPSdD#ZLduXhQ)))$u*2ai@1k1MG?M4jKy*uFl?*u0N&cDLH^Z5PBtNeQ>Eam}9(T{3yk~5&=G&=%juf$X2+^pI&Me?%M4HjU*WJBAYg8I~J4aXzXV)p{$A|!89``rUJFgAlm^n@KoBjVHv`>8r(mNV^w2P>65zvRv!gUjGX9^0T_Mfgt(n=JU$#w?=W(H@8P>=iHYBeo<<z2^N%vwW*q1k!)G_{lu{UqB8t3>-QE%ZSQx7FS%(8txsjbsK!SF$F)w7y2qZrdq$@5sI7hN$`#5$%LJtqJ;GEbyI@x@%7rRFFaab_~EB-FZ}z$Wn+avnrSnBTDl$@*qbmA**<pxr7qSR`Fz6e)8G^4s|<@zeBfTFmv9jL8HL!VaSa2@C)stNg5Y-9EiHf#we>rjFL&@v;h94=0c%Y>#~za;nqc}O`=U@x@ouQIw}k56Ft|6+7Li2tO7bQtPzE4qkT7z;ezkf-xjaH7yC1P{h!UqQv38dwL**D3V97q$oG3RkkktBVtDe4~$#rXvEh^2@s@MlA=EJwm4J~;SL(-PnkNo$v{Jo@pr5H|uglxn5ZO`!`ik;AbX<iZo&Ay=7D}&UX1A}BM1gTp`V$5+mQHwI@(5nNy<^)*9qTMZ)oclQ0RO+k6V92$N<%0?680?peix}|y^Hd48fRbBol_xM<G)&u=3i2S8Voc4Y+g^q+M(;9Gq#p?LOL9Dm$6&Sv?#|MBrv^#0(&__7#FZ|9QpvI>PCkanao#!dxnC}x{66OOlIV;K!w*E*Rs}!>!^7_-I0zwu^@;&&=>eCm$_8SSa4-tlFXHIsLts=w-ffjPSFKebShc$=it&&V7?Ma_hdI3t7!b$SBIf4Pjg{moIT}0$iqdUtyRY!|LE9?(e(Tw7s}ltkJAB9)ccw%-C`i{NCBDPCjakcv=xDFZN<*J^O2Y6nkTBAb6jriGFk^^ha`X_dUaL5y&&G_Lw%Iv5pzPQ0AAXW8oc7kmegtJk^U_l@kglJ|ltu?QUmMs6PGI!R{{ZQ(p^YGgb^oY6(pXTGs0Xwsvf07g5w&xK{SoeRVtWuSEA&Fq1z8BHN_+&yIR^2oT%q_blP#UMgu{x+hqjl{o@^0iWA+j;XX1TsC6wXMM)9t8g7=)nb5;JXqJmHrMBXrS4#VOL#fYM0n&N!aDz2~<cE3<G;fF&2BF7}<NK&I9ALT=U0E_aFLR2GZPt(<dI5m9Zg8ht_8YvQt(VN;prD_XU81<`6!l-!~VYwKWSJ{CHAM2V_M1VB5VY?W4#)GVF)>chx4z!CiBC@w-8LM(JK!Ujowq8!31(8p{zhpkQc5m(W`?-W9rK89(RGn}s88+58SbB@+D_ZW{l4YnA2!A*jKzn#zx6Gc5;2v^_&9Y<W=3&XbC%oz8<))Lo1q)5{94j6X#rOm&>?pel`)<dZU4)FbS}**cq4i!Pv6Mu3#24g;SW2+8+tewuf?4t=M{|*6R4X%IN}lEG{0s~7E0M6>YlyV-V|Ixfp^WmlnPczeP%kR99jG~WbQEcc`i>NOTJ1?OD6}Z9ibxGL3R_(7MQuq?wFC*z5kS`kZj0o3DX2@zCscGmv1-d!G<NYc3&wekNWyKDp8_5uv1vX}1$X8K+ZCu8WL{jFos=Dr&1j;Y;Z{K!qn*Z_qV6``d4(?@t?=D8DNt6;%YE7L$tph(%AhqVfdzWbu(MRxKeU%I&Y5Tr1O-XN*~tWV9#`>1u_N(zn|cu4Ib{%Kc7?Rj49k<oMnWYWDVbhPS1BW^)qxs`6t_b@|4$i>6kAsDV9G7kYrd$uD2&gco=8jFdnLL1pfV1vWp<c|gIrq^C{9GhS*ScM)g`~7fqjW~7?imCbctIOxNUXF)Uo2f{Z6^{e70)3$SzOq16}FVZ^$e!&Soe4k!&{VfintI7iXQfLGt5Mpc%`jI>Iz;9OQ<xE3gu7GU@S#8F3Wb(kH^{<DX%jFk^|ryV4(0(>{6jA<OEfIqKz!?n}XBJT8$XY$F{ALF$V`QpIekm&V|HWO6=fvUCSDvX>UJ3lW|_;g{CuXEV~}u)#(oIkmr5cSs;HQM!j5<VA}!b}Ht$uuv&a?!{0e{;f5LbYJRq-b~30%H3+|8#uSN!6{c&f#RbuN|FW9oPls_2%)NqN~%U^NGIBhx6+(&H!j{tX+j-^7(`_YFj08VDmxgKOA*hrNX2(rjgG66;qr{hDOF@8)^0cpq1Pc%bWp*>Rq2>axrE6H6?YzOYMF&}9<#|5wUCWhIipCkJOw)F=Pum{AgF}#yl0MG4M_|#7a3DY2w&jQ>&g`_5=$jL*dnRp07e+DzN)427<rbQl8woO<C`L7;b}qmG}79FM?xe8zo?UN0`!4qG@Vix7()4|5JyUO97%x-Di-P_wp~AeuT!0#s`>k^R0GqFSWi$s*4k`I?@FT@W*k%p1s|X*A3s^n;N$1n<7-#&E?AfwQ-Orl(VnvFI*lp`Q64U?#Yox?iyAGaVC`h7P;3{qgk}i3`K&<e1X+qWRV0tH5wN2m&>pwxf?NP+M_l12<!n&EOF*VdCaTZ}%}Q`;7A=ZY%!)`*4S|)!7)4SEdb~eYPXVRr4|SSSRH95Tu*B#!h)g}{bEYef>&wWj-|zyck^Q{1)NdH4ipL<VJ{9rRR@u{F!dEZ)h2BI!{O91!#IWr7PZ~pOoK*iaRW+_KQY2ko!R2=`Wiq08wqvLE8Cj&fmWr21gBzpr30f)HWV~QHY+@MMU@arT6L98h4bN%$pktvzYew(}EVyIS>8J71hF=hYbX9V>p+yK=ZDy$MWoBMjVGHdfIx#)LmW&c;C@9X71T0|;v2+#sa$fk3*fd@a<5rTiDPaFlyv|zfxX3E6lf^f$q3{V!YME7Sp<^wVwB2KQwT33%4^u-buBy|@+G`Lh=nGC-4tACE&np`8_yt1%aXpWZKc0Hx+}TpvL*Xj}Dw_>%-lRz{SyqwDf8zcUU)^vG9dw9a76f}OwVbzV%?25?-QaQ{hyES(LE{2DYpT;=p(t)94pM_m)I}GT5p~eTO(k}naCmSS2aHHTxfnXT;3DbBNQ~R0u~M$xWKi}Be4D|G+Z-dP5KhbMX?%-PC^)+lWmmDg=XK3*aNltW#B)Z7?M_y_$wF6I^PvdU5G%(ctacN@b*a>ya--w~mqB%vr#W8a_Ye2F|2ha-aG+qU80tPd3~}bIw(5<#;UwIk<iaD8!X<Xiu$eaSP`<EhG{;rE%FhV3B?x}X)oRIYdI|j0ioJ!v`vkl=W(?q(F#xIA@hW8WqH2)6@@>Va8|K7}T%mTr7PtIF4UtzWZ=2Mnc?l65XyNF+3e>EoWbmx90C$o?X5JJiVxrIrfp@uze-9D5ZzWbYewSNT?%pLiRGdH?TpN_h?AUw2PSuUDhj7#Z6fTfBo;Kg{u!&DJYoE5s8<qEwvCnUY?jrNB_MVMa;<p^9C>(5~2{zLxPdKG_$}LZJwj388<Pd4E8W3zjcv|?Fkd#Z$-MVZKUYN&!VI&DxWMPMBNyld5G5^jbQYf_ztETo?tzIvwSEc>Uy5p5b%U-RbfVwl4P-3EWjK59+uZ7xfkkW1Ckd=HpyxEQCxKi9!+<gPt#&GdBT!1vRN5M1gnQU+nL_CQ$Oh*5w|7xo=@HhNBuRWy_G5@qnt4hw+P3(saEXQ{-Xzv>s%GvM*@cs+belxB'),'Libraries/Compiler/main.☾':strd('c$}?T?{3`25&y2Ipcxq0HR!V>BMopcQ%LeT77|;6r33*KfuN3icZ7N5f#lhz8vfukPTMp^TqjPQG)`ayX&W?68?;D+)J{I|P5cA_@&cXNU6Q*bPdZ6=u*^TZJ3BiwJM)`al5XTNr{@RE>AKy4ANJe!c06WufoxydY}>=@9?AZN_ZQc%S=pP}r`g@Lm2FbqIbyV9W%sg&*}tik3|tDo1u|f+$6}`&4cm5h2O59Oet_#o*>4C5+~J<*8bIdj?0t)0?ze%$yV(<h6Uqi+o=#fN9{ym`)8f^A3rM$OmPEk~2DjLE7)7Du`7!if9s5D*hlxq4mA#cc%D&A$C4#XjJ<sixLj>C+Hys52p5qTkQJl7IV)o)_Xvo)wcx`OLqv0mT>Ew;^;^N{8?-M0?GYfC{aTKaO^2rSwTU&jW5^PvrzOu1#)mdHH>Np@{@ru@loK6bvsp0pGqKO3w!`566v^8>L7N$~UQcJ}A>CwF}O=@j+UZa-!9(ZYbJ*~U?9;KB=&S)Qmlq>Xc_F?u<>kM4~nEl>5BW@nF^Y&VUo1_k>LGmU+!p<qlj$Ah$lMCk~9FOgd`$Tq32GLCisB!ZZPtmyY<b;s}vT=vZzT|@3M8ha%I8J%vhw`bIy}e+-59BV}#WVguIDgGPBdZ&)lhjWG1~OW|YN|q08N}_zmx4q2e+2CGL3TfT(zan$z)0TT+v_`gOh0yqP8u_2E9@$Q(O83~k~gIN&gRx-Fb=$1zp}Y;ZQF5x#S!cG19twLpdCd4*uT{eqCHqPp|C%2J6L@9#wJ;$bcc|$#*#tlZn^Tu*&niRU{CXFu?`r#vbAmMYkUlCzve3hO^XFmQtWp*lD4{|m{t~~sqH|qZ@db#mSUEZ>e5!I9*Nd0j9Uep&J8zCgdf$Xk6Aj7Lql-3!0j1j>_zBpK=6f`am|&cPFn*vaRT>O`%VzKUdg&7sGHNlDv$dUrym79Hw6cEG_6l3p0Y{m^rCp^rt>1X77a(>(c*JrTg;to;dzcpxuPK}e@{$JS0*i+xJ6hAOWib$1)-NaWLb8A+oke$QI5OVd4-$@F3#_k_EJupI}3h!gqQcSzezKaR;m~nRgF+LY2Ej5=K=(&xI>x?3ny7Qcc&*<dSy<hhiHYhZE+>NkqzN}ZDs9p2XP89yF$yJb2`C5xVo{iy|sO9Wz)I5vUPbU3H&Z2SEG<wOTVDI5XdYZJfkq!7u&YF#%k=*<!;})EkzG^$|fd*Hu!9}SxFGaLxXf7cB=av8t-M_P+HsK-JQX1&5;x;>6W4%C<-CXa-)8a)PNsFBvD&8ox(h-(ofm&7*<>`-E2cb0;=(VOpk9ls5fa1MOY}-^VH@>kiDIKVVB%kLDUxjKy}Exzu_kaH;{%POKKrMhs1J|fp?KD0Ei2YcNTY{L6FzpFYPL;S)%x&A*9wPg~gOHRN*^}QUjN(@h+(l^SRTBLE!J%XWs&xlmOI0i0L?XfiBy&0z}V2zZ`Cg{$jVuIcW=Hp_P4}y_0>PI~wH?gYyiSv+1q`^7&LT3*6Md!9asB_)hjo_7SyWhGAJuWmRAR=(vUeis;~h2=L#tx9=NbO;<K9ig5pB_7o{T%<kA;l*ay$R`ve0nE(9q)H-OOZ2JJ(-pbo@hfK^jCW|X3Mx>t}{po+WAC5^5<vfkt0pNt>y9PC%v~8rW=WT7ce3yMqV7Wh{N@X$!7Q6Q9HA0pwYTYtH&So38%xz2EhN$4DpcMg<tem|9=J#31VmD>ZUKFKC8oMLnF+k}e8HN660xb;QxvwPBnT1i<wv}|~rk@U+WZdid6Oe+)CgrjT?iD3@5v$4{+u|8qpyofyX*l!TSxBfSh>rHVb(-dLr_Sy9;knU%I*3BCTlA=8=ZT^)xG5U|C5#z%ZrkDwMFp4Rt5>9_r?txdD${gJ(>S#xfbhn{5f2g&PQ~c5jXN7l!R)9cWnZBK{E8GV5?f2Zt}LwZdT6)rW?!R8a8h=YYhMOuxV&qDplRvKq6A?0U>JFPptTsi@WS(T>xMA`M*&#vGQjI%MUGs0Omy(1;m0jBr*6R9m}-5tHysW=^v2w!tn&#Vz#3B!I6VZh&H~(@z5V?mxV3>F4YVJ|#dL&!thwc)W?uaq=hTwkS%p6}Q9c$YMG}H!Tb`S`hjY?2W}ckn4mTR%HHv2t&VhsH$XibJ2pp9|=Ez5gm^s}av7^XF9W+N?upo2<E=2b^&+nv@89YbBkU8?fCZnU+h3G!V`9+*Ria``3=Ez0NZpM&~9cj}lW9DfWvRX5{RWy}%PR4^$+L@V+Y2~03aZ=2Wi11Jzjxw{L3*hnU*5>*v9p_r-5+PmMs^sq~P7$SR3E)&rBoR>^aytQJRHRz7&+)b-I|WEVX4rt?d2R^AFzNMs@<CJ{h*@-#xLyNN*<Hvru-5zp0j2qpr0p5Ss8c+<=`Hp+zAp<l-M}XRUShYK7x{fxoD0N(tt9jE=mtBoJ-2(kNTGe#a6`|C10{2oonrvcfgiFGhF)IZ+IB91O0?9xI6?!pKKub$at3|^@d+1d4X^iTiDa9Qe?hg#ElEB#=Dx0%ljGQ3ExnI=6W~M_-m_008B$mXB0vnVHfgD0!ZG)Q>_1r3$78$CWfQMH0^TQnI2xywDgrNR6eb=fYDLF!gdQ*uI%;8u6C!88Dt3TPZV|pK>riiIAA@m;L%CxYn@XXg9<cx-STz*xm5osB<d-53D<=IY@=lqGYE*J@pwmzk!u_hIky3%p#H0uf+ct>V4bX8ka>%osWIsV+U`I$drt#Nkw#tU$3FBmGb!TZs-n`87#NMQScICig`j9^M2M{kH3$m0s`2l3(42P0wV0?OAOHIP{-BOuL9f*aW*E*Z@fT_#+op27fh$)2auo#3ZY8SkAm(<I4&}B4J(GGuUyl)(2cjdMdjE9L8@}idTR=i5dZny#D{_<ec5B<~$6ZPy8IErFNcxoHjQ&lzTvQa7y?mljh+$5QSw;7n~yxv)JuC8pazt%Y-Z_TXXv3d4h_W3lc;zg%Y&Ct^#h1;erk)=9<q#uR6AXxgb!rpQRFM~s^<c@1AJKh}NKCTph>ta(pWOZ>bv;DoujlJ~{Y%m_f8(il-bj!^v6<k-F<gynnHu2Nyl6csI<%9{3!aVq4+`gZEm&a|c3NPv=WtFOSEMNGDR};6-+Qzfr-Zg4J0>mN2!gdseCi(gTuaIHA>BXXFJPr*Ad<KtBTJN)iI$h+@NWp(rx^|5VJct0c0fI=K;C^V};p|#N*9q%3bzL<s0EQ5N2TMmU>dnl!0BuN!g-Ei}>=n%(YiN$7IDFti+(qN`mr3fu<;4=@lul?zYHJt0@CN`KXnt-0FY6AdH<R}fwkwJ7sK6iI&)#p_;w4gpKM{b=a>m+fG=bQOTkebOgR+{}(@J>{vWIFNuUadHm5Dof`nF{8vxr?D^<`yKXCTJ`yauaQ*%vLj651L?BU&NI0fR1=TIEnK-Z%x5EgNTwCDV2{3IV~7OF)N2HE#i%;+n}1?|M|LbT%HgDs9t%vU;c^>e1@S7)pl&7nJaaFu99W{2nz*0ijYF=C`Kq?%Fpr)gIc1G29NnB|ZGGLw+TtoG%G;5cXz?Lo+l(1owrRNPth2Oh$lz)S+loh;SFnO<A?U1J)_u<zQbj$AXiwC!}7SRw1jo%xB_OGgi!UxUtq^Oc7pH*djJ$aefF<^cKQsaijs5r0jyP`57I&ZKfgX>GGV858&UZ@DYg3T|dN!+ai|dMl-SY+e%y~@NDf<Rkn&<w9MwkYj-?qbG~4N!SeuqdVnsxnQT`hTX87-wChgx_wpPJ8vdO9gBAx-JcenWV|IR;8T$FZ-~8@GJn;^kucCv5Ci7%-?Ih|@l-^8zpi@_h3kWKj$Mjix7R<ED7h;U!vqm{k%O(zTtNIKVYbg_%@GL^4ky=Y5l*@m0NY@}p!Ipq|7MakNI~uXjqqT7o`gJxgbrAecLwxyf4_xkbqt>)A^`Qca#YrsB;J(QILMmAgPleRORwaqkrRmkA*_3Cghrhy-c&;VQX?n_4osAtZTYV1xeSnx_I?2^0l1&++?k24%MX>1;?aghX>2pN&IqpHwxQl{$Tnc7q(OR;Wcgw&(X_p-6-@p{FCu*GG0YG>G84meD{xTlq-xj^TvL+Dh<mo++llWXf5$<p)J+wT)LwQj*4Z)T99>?Y+p>6reMGwErs=1e1!XwJ5D;F<1o!8|lEm6y;CD<`7^@}65MZh4nUA&>?r)1(#+^n9Fqid@w(ri*L^wiTb)6$;{j(D2_X7nPjTHHl|lSgv_oXc=74W^n3=JnSqW?oSA)Z}y*{tu~>jI9')})
#main.☾ (6449 ⟶ 10926)
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

(compile_files:=MOD((lambda ÂîÓ:Âøî(Áÿú(ÂîÓ,ÄÊCUR((1,),{"log":True},compile_code,ÂýÃ,True)),("\x0A")))))
def generate_bootstrap(dest=ð(TMP,("moon.py"))):
    (file_canon:=(__file__).with_suffix((".☾")))
    (Æå:=(lambda ÂîÓ:(lambda :ÂîÓ))(compile_code(file_canon,True,log=True)))
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
    (show_docs:=(lambda *áÑË,**áÑÕ:Âçß(("Usage: ∅                  (cli mode)\u000A       <file_path>        (run ☾ file)\u000A       -h                 (show this)\u000A       -c <code_to_run>   (eval mode)\u000A       -C <code_to_run>   (exec mode)\u000A       -B <boostrap_dest>\u000A       -e <str_to_encode>\u000A       -d <str_to_decode>\u000A       -o <file_in> <file_out?stdout>"))))
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

