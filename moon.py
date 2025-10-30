#!/bin/python
BOOTSTRAP_HASH='Mc8NFT6OcqTVX7WbhjNVNawK2bpsj_sOj5ITcQADaGU'
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
from time import time,sleep
from cmath import *
from types import UnionType
from random import shuffle,choice,uniform,randint
from tempfile import gettempdir
from builtins import setattr as setattr_
from operator import setitem as setitem_,__gt__,__lt__,__ge__,__le__,rshift,lshift,getitem,delitem
from itertools import chain,filterfalse,product,accumulate,zip_longest
from functools import partial as MOD,reduce,cache
from pickle import dumps as pdump,loads as pload
from zlib import compress as zibe,decompress as zibd
from base64 import b85encode as b85e,b85decode as b85d
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
(ÂÖë:=(lambda Æå,*áÑË,**áÑÕ:(lambda *áÑË,**áÑÕ:Æå(*(áÑË[0]),**áÑÕ))))
(ãÊú:=len)
(ÄÕÍÔ:=(lambda *áÑË,áØÁ=ÂÞÅ,**áÑÕ:(((((áÑË[0])if((áØÁ is ÂÞÅ))else(áØÁ))))if(áÑË)else((((lambda *áÑË:((áÑË[0])if(áÑË)else(ÄÕÍÔ))))if((áØÁ is ÂÞÅ))else((lambda *áÑË,**áÑÕ:áØÁ)))))))
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
(ÄÊPSH(((lambda x,y:(((((False)if(y)else(x))))if(x)else(y))),(lambda x,y:(((((y)if(y)else(False))))if(x)else(((x)if(y)else(True))))))),((ÄÝøø:=ÄÊPKE(0)[0]),(ÄÝøú:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÂÕÕ:=(Âùè:=(lambda x,y:(x or y))))
(ÄÝøù:=(ÄÝùÀ:=(lambda x,y:(not (x or y) ))))
(ÂÕÔ:=(Âùç:=(lambda x,y:(x and y))))
(ÄÝøå:=(ÄÝùÁ:=(lambda x,y:(((((False)if(y)else(x))))if(x)else(((y)if(y)else(True)))))))
(ÄÊPSH((__lt__,__gt__,__le__,__ge__)),((ÿ:=ÄÊPKE(0)[0]),(ÁÁ:=ÄÊPKE(0)[1]),(ÂÖÔ:=ÄÊPKE(0)[2]),(ÂÖÕ:=ÄÊPKE(0)[3])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda x,y:(x == y)),(lambda x,y:(x != y)))),((ÂÖÑ:=ÄÊPKE(0)[0]),(ÂÖÐ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda x,y:(gcd(x,y) == x)),(lambda x,y:(gcd(x,y) != x)))),((ÂÕÐ:=ÄÊPKE(0)[0]),(ÂÕÑ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda x,y:(x in y)),(lambda x,y:(x not in y)))),((ÂÔó:=ÄÊPKE(0)[0]),(ÂÔô:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda x,y:(y in x)),(lambda x,y:(y not in x)))),((ÂÔö:=ÄÊPKE(0)[0]),(ÂÔø:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda x,y:({*x}).issubset({*y})),(lambda x,y:({*y}).issubset({*x})))),((ÂÖó:=ÄÊPKE(0)[0]),(ÂÖô:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda x,y:(not ÂÖó(x,y) )),(lambda x,y:(not ÂÖô(x,y) )))),((ÂÖõ:=ÄÊPKE(0)[0]),(ÂÖö:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH(((lambda x,y:((((Ïß:={*x}))).issubset((Ïà:={*y})) and (Ïß != Ïà))),(lambda x,y:((((Ïß:={*y}))).issubset((Ïà:={*x})) and (Ïß != Ïà))))),((ÂÖü:=ÄÊPKE(0)[0]),(ÂÖý:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
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
def _(t,Æå=ÂÞÅ,áÍÜ=ÂÞÅ,áØÁ=áÍÚ):
    (ÄÊPSH((áØÁ,ÂÕÃ([Æå,áÍÜ],[ÂÞÅ]))),((áÍÎ:=ÄÊPKE(0)[0]),(v:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    if (ãÊú(v) == 1):
        (Æå:=v[0])
        if (t == ("")):
            raise Æå
        
    
    def r(*áÑË,**áÑÕ):
        try :
            return Æå(*áÑË,**áÑÕ)
        except áÍÎ as Ïã:
            if (ãÊú(v) == 1):
                if (t == ("󰔶")):
                    return ((áÑË[0])if(áÑË)else(None))
                
                if (t == ("")):
                    return Ïã
                
            
            if (t == ("")):
                return áÍÜ
            
            if (t == ("󰔶")):
                return áÍÜ(*áÑË,**áÑÕ)
            
            if (t == ("")):
                return áÍÜ(Ïã)
            
        
    
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
    


__dir__=(__file__:=áÌî(moon_dir/'Builtins/system.☾')).parent
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
    from time import sleep
    ÂÞÅCAT(x,sleep)

def PL_TIME():
    from time import time
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
def _(áÑã,áØÆ=ÂÞÅ,áØÇ=ÄÕÍÔ,ÁÜñ=False):
    (áØÆ:=[*áØÆ])
    (áÖê:=[((áÑÿ,i))for (i,v) in(ÂÓÏ(áØÆ))if(((áÑÿ:=áØÇ(v)) is not ÄÔýò))])
    (áÖê).sort(reverse=(áÑã == ("󰒽")))
    return Áÿú(áÖê,(lambda x:((x[1])if(ÁÜñ)else(áØÆ[x[1]]))))

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
(ÂÔð:=(lambda áØÁ=ÂÞÅ:(({})if((áØÁ is ÂÞÅ))else(ÁØò((lambda ÂîÓ:{}))(ÂÿÇ(áØÁ))))))
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
    

@OPWRAP_(*(("󱅏")))
def _(áÑã,áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
    def Æå():
        if (áÑã == ("")):
            ÂùÆ((áÓö(áØÆ) or áÓö(áØÇ)))
            (ÄÊPSH((((áØÆ,áØÇ))if(áÓö(áØÆ))else((áØÇ,áØÆ)))),((áÏË:=ÄÊPKE(0)[0]),(n:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
            if (n is ÂÞÅ):
                return ÂåÔ(shuffle((áÑÿ:=[*áÏË])),áÑÿ)
            
            return ÁØò((lambda ÂîÓ:choice(áÏË)))(ÂÿÇ(n))
        
        if ((ÂÞÅ is áØÆ) and (áØÇ is ÂÞÅ)):
            return uniform(*(((ÂÕÀ(1))if((áÑã == ("")))else([0,1]))))
        
        (Æå:=((uniform)if((áÑã == ("")))else(randint)))
        if ((ÂÞÅ is not áØÆ) and (áØÇ is not ÂÞÅ)):
            return Æå(áØÆ,áØÇ)
        
        if (ÄÊPSH((((áØÇ)if((áØÆ is ÂÞÅ))else(áØÆ)))),(áÑÿ:=ÄÊPKE(0)),ÄÊDEL(1))[1]:
            return Æå(*áÑÿ)
        else :
            return Æå(0,áÑÿ)
        
        ÂùÆ(False)
    
    return ((ÐÌü(Æå))if((áØÁ is ÂÞÅ))else(ËãÂ(MOD(ÂÚü,áØÁ=áØÁ)(),Æå)))


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
    
    return [*(zip(*áÖÒ))]

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
    def __and__(áÑÞ,y):
        (r:=ÂÑÖ())
        if (áÑÞ).hasdef():
            (r).setdef((áÑÞ).getdef())
        
        if ÁØö(y,((áÍè | áÍá) | áÍé)):
            for k in({*y}):
                if not((k in áÑÞ)):continue
                (ÄÊPSH(r),ÄÊPSH(k),ÄÊPSH(áÑÞ[k]),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
            
        else :
            for (k,v) in((y).items()):
                if not((k in áÑÞ)):continue
                (ÄÊPSH(r),ÄÊPSH(k),ÄÊPSH(v),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
            
        
        return r
    
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
(tmpf:=(lambda b=ÁØã,f=ÂÞÅ,n=14:mkf(ð((lambda ÂîÓ:MOD(Áëý,áØÁ=b)(ÂîÓ,ÄÊCUR((1,),{},ð,ÂýÃ,b)))(TMPDIR),(((Âøî(ÄÔÙù(MOD(ÐâÇ,áØÁ=1)(abcABC123,n))))if((f is ÂÞÅ))else(f)))))))
(tmpd:=(lambda b=ÁØã,f=ÂÞÅ,n=14:mkd(ð((lambda ÂîÓ:MOD(Áëý,áØÁ=b)(ÂîÓ,ÄÊCUR((1,),{},ð,ÂýÃ,b)))(TMPDIR),(((Âøî(ÄÔÙù(MOD(ÐâÇ,áØÁ=1)(abcABC123,n))))if((f is ÂÞÅ))else(f)))))))
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
def sha(*áÑË,**áÑÕ):
    from hashlib import sha256 as _sha256
    from base64 import urlsafe_b64encode,urlsafe_b64decode
    return (áÍÇ(urlsafe_b64encode((_sha256(áÍÇ((ÁÜÙ(áÑË) + ÁÜÙ(áÑÕ))))).digest()))).rstrip(("="))


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
    
    def flat(ÄÕÒü,Æå,áÑÂ=True):
        (C:=[])
        for c in(ÄÕÒü):
            ((((C).append)if((((c).e).T or (not Æå((c:=(((c).flat(Æå))if(áÑÂ)else(c)))) )))else((C).extend)))(c)
        
        (ÄÊPSH(ÄÕÒü),ÄÊPSH(("c")),ÄÊPSH(C),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        return ÄÕÒü
    
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
(ÄÊPSH((MOD((lambda ÂîÓ:ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ,áÍÇ),zibe),b85e),áÍÇ))),MOD((lambda ÂîÓ:ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ,áÍÇ),b85d),zibd),áÍÇ))))),((stre:=ÄÊPKE(0)[0]),(strd:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
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

TP_CACHE.update({'Libraries/text_format.☾':strd('c$~!=Yj0CW_B+4g>Pkp6>6F?I*%o)rE{|4~wp}V<wUu1Ua{NfV^&@LL8>gib1e~Phm5`7UplMTHZJ{X(ZNe)>Vtzn>L+>wGi9fLCoSC_Iu6>;pz7%vlbLVm9%z2-4Q?8EH8!e|%+`;6kd?J6y=klY)WQtXC)!{<Uk<;>q7=WpHd0Gsp&c&phk~iccWAe1TD_4^#+Qe`z=fZ65*~QETUM@j*N<NVDOrDUJ<UQt}Hzn8P0xXr+<md7cQ|}yi(8_f^A^_%sT<5%4X%<<W!#}3Z<J|eP6OSc!>p6uLXWi)F77n*QB|m@v$UDrwKFelD%Oj%|cv{6qHp_)Q2}9L<rNQy4?44waApGqu7USty2F7FuF7^xUxD%R<XJ8AyAAIXwL>UHluu{2J$QGOVY_s_9CeXc6<h%0q>R7o_Wb6nGxF5FT`#&6y#fA=~*<X^XS9s;k#G8J%r*kZJEIqh8vxirYr9W)P;_xIguDUQCSSz+$+5Bj((S4%J;EbJ3KCtUA+~qsj5kZ?8Rm2f)W6=R`a^N3_85<N_eDbLvK+W-C5xSBfwp|mzwoQ4GfEDVkM!6aWX87M0lc}K?ib^}(td#Rb_V;?NDA=U)sskj;IIlR&^^V`f%a9Zi3?MfO);F*Vz@Cs-<uYr-3TLk~sl}kJ`CTd3ia_W04jt^3Ih3sx**UQ9s4ry%i^ILfD&-bKX2kaCv*G?<0;gxpTEyk7Ty>5))cKAZ0n{Q)$F~4bpj~j=BpmS+1$|Y{$cK!Ghy=`4DqXA+Z7wFcAiY^rvKzX*1vbzh#W=csph9i`UIA$=Xw-(Gb(0Fo2mSl<EULyOc_J0#%-qCRPzyPf{IEuI#fq&_gLmYAx2|?cn9ns3Uy|NewCD<3xRt^JT9@U`2(4X}XXMju^|eqeIV20&7V)KCsW;#bqBN2U(AX`~vG&_<1K8o7;TW98lRF&vhr+7VJ3aUY==08Ib!QVXS1e|w5nBZYc}6hzO%OiO2BlOG8YJ#f1~htDH5zO}(Kdsob4p&6Cwt@{NFy}Ge5nLlxyGiTCJ4P0sl|~+7r{4NvOu*BaV-$AY!Uw7ie5$pRy?O$!uXQB7pb&H=1>>c<q8X3a0vJfX2StMKJ7?1R|42*0rl=hCDwEDj1lT|X#`l9;jAHSm8E6Va^5U!b2dq&veqzWHlvxEbW$lWT!VY6t}zR0fw~%-<a(XW@dTJVz0Ka`Zwa7B?|Q?vOwdC)&EC$z3lIK@ErkRb${IeU8pYOlqvrGxw}CzaN2EfT_*|ayO$F!%H)dit=RA-$)J0?Bwie-d#^1+{_eTTT5K&TM;L~lC5+lX3M9YU{^Ood~O3;2(OxZMAN^dLVt^j*YYPH1Z2X+(ao6toma+OPtAHxs;j$DarpdrADqbqp*5b$_LW0D@s@Qj9w{B&Lnh|+Q~px5g8xTPFi=qWRlu_dY(iI6~OW)T44d&nI-{%ZMmBKcUZz=(*`N)l#NGYdx0aWx80Qa)CO{NVu2cl8Pq7g57A%GOsR%{)wRYvv6HE6(1Oqd^8lH#a8?0)jAkUY<a6LhB)5sc=gc=ys%;;R{*-^_?)rK~T<sI%1YvR1d?7MPP-peukwnoIxNvodgdc0c=gUjL-{Sdo8r0?^*E(guCzzpa(!~+XLdUv+2!#_I%^+FV8m~JdTsMqZ33wk!c#4nMldoVibNf9)O)m3A9kD$RVs8Fp*5DNJFF6b-@Xz+;n`Pv~5DUn!W*!FT<e#rwi_AFWga(JKrQkph8<}^_D{#+j9@T3qp=!t-z4Es4_r!K)>DqF#w}KfB;@~x=x6^ZsZwS&wRZy?|tG6YEe`zR9<zuwJ|WzoCP|^jV4apniyzd0<<uZ=`}S<;d;fS*~;ZVYEX)|B)<>jgW*NhpcA1fl$qH28;}6OsA#bZNirh?Os%;cnlW~jjHU^#`kEHoIo#&`l)1~qL~Ps}rI?x^T2e#gxot~?Zx4M9fd%9z{o@#8VUa>q4W-~tPOetaq&xIJ3(ea5&?H-H6+uvTk2c03Cc$3UgpOAFSxLasn41~IxUXY64QNa;KM;Z7)Tp!)0M2YH12(1$ZSAa}y~DTkZ^QL=)_{S0fVr`u*wCI5xVGW)NJ?ENX^|b|$~xH!b}z{exRGdwN6f)|No}I=E@nr{3-Y3pO3KaSDmS-l5;_$J6m2f|@;I*9g*pTmaH3eD4+I;K2AcThACXiqYLaRX5sF4kA){(olAxgOiu@jSdFNKWbKiL9u6f5l^UhuO&fW0N-PAGs0v2#UK@au1_yfP!yThfTyeA4x+R7;rlf^SGUC7Eby~X3MmW>Ww9f#&D^hCdy7_bH`6gaew&^ut#CoKx1`~1b<cm5^o{EQ{6Tk8g(xoY_}|B!@G<g@Y`@iC##YAB#_F!-#E4n-yDh{VUiD^+VI)%9v*3N7tn+xQp%$euDHsTng#a$AIpGNz2suNu<^G`c~Oeg>`zK|hr<=!H<k;JjWT+kfbT?Q46W-Qi-7IXM~1a6mCn$Ypt|iv}vOzL2D_*&b1T3BVvK$`oMTQ{{)~jCpS`ZIxSsz=c{!B-NFCGIGK^|Hon;dkK^qe=N%J7eyJ@PBe03(WOwWj)l}4F)@~6yD`L~1H%`J%(zd;+j7&`)E-Bo&CXt@;OEeRjwi`)L=uNtQJ=X7^vyLG8#6}j0v81_Mq)QWHBZpUg04ESa5Qd{MAM`;-lsaONm5P4MKeX-{H$CQn1iHZ$=;mbHgWok1?r=U>wS->ia&Q)_csT;3qa<o^2|k*lBARJp)$`4^1L73ifw47?WvAI=s3fi3b&|A=W)?g=G@UPRS`5~Kf8$-h|>$w&Pdmv0_pPEsaawCLKW~bT;0K%qxFewzFsKWI#)==V=?n}2u!4p60$#4PzPIqiCY?Rlg!-{A98tQkb;+PtHOD?RSBJCjCek!ePJH~NTV$yFY1sFZ3o2FrAv|5zIqvqeh3KJgFMrgAgEkxBVfB&zGY23JzyB-S4$9gOY}uMqXSRP%~BQY!Y2a*tWeIkg1Txt_?`k%Wnww1r*6u7D)#^(B{x1Vf5v`C^&hC_iE8et=BaA#tL7)wtgGgsAYr|a(HVArlE)F;jGBF9W*_7G1)Nih&a3&yX8wtpIISi&&BUhKc*4w2nTe-rV#-XMG@UuqIb}NYrgH(!z#49xlQ#v`vri+o4{`jS&>w5QHl0<|`9^it%*a|Wa@}-pn9fbpxn(-vn$9&<S-z~A>#A8+&5~+XRr8%{zSZ>#U6EGJ71gYvVEs0C)0;c)-MRk!?%J%kwEAq*>nuEb;&m>1on@~x=XI`loq4Zw!Rst~ou%g+>-XT<c=n6e`2srkz0TF=8ynMJ=MudA1l=jGa~Zlndz~+#c?i$C*I9w)5lqfN`xx3;cs~2}xOZyCn_ZD>zn*%&@#ri(=ioX2eB;00!Sg*lci{N}o;7%Wgy$|ixBvI$`~`Tf!ZQ!gd3cuLS%v58-xlYfS%PN)9{PaCKeayUfV>Aq2ht_7+<vZh$1Wg*O6~7}b0zCYDzimBVVjuKwm-gGbW5c{!W9gNNN4a1>+AG6_Vt6_SL?0{5f2=CFCs*Iw>v_FvBROU1m!E?b%Qh(Ubh>^_8tCbXmBVh<n*hh=+1O?Y)+n$PZ;Um5~DQym=iU5i6*%TnU{G~5Ut{&GjcPswtBX!Skmtk8l@=9MC=9mwQg@g*rXD&R%6ntabtc8Sw_u45ebH^bOt8U?TkO83gzv5ajc~fzYKP~*;KjbQT@qm9a8~6|2>LnOKWnh*qh`6G247sHe1V8i`i^fIgR!yC6B1y*a8J!>gpHX)diQQk7n@0AiAVjDdtk%a@0hWrC7}Et=g$$y6c-!$M|2r=?FJLAL;txyb@Uy!~JU7CsD-SD}DEBM|d4wfKuKe-UBK4-b>OHRa@|7_?r6EZ@A{8V7?Ofk*0vnoC2u>?~>~e2ZqSoa;sQvvanIXN;Ur173yed6`+%%&+H@@DrBP^fzChNp9J6!UWx?Yz6=R81x#?#?sJ6z`)!e*ektTvUkv&EFOB^EEs$T3_al&Z73aHjUqn<=jJ{z>V_H54Lez-Ae+p-kDolpvmi($84H)}KFE`l<`$&Ca0zg<L)$t&fS5(nXk@O>!J^xRggb7#`xfM^)$Yir<ocA3(n0@Pm_YWODdL)}=BbEAau0s0Ysy`obg=%r6=Z_y;(KCeWDBN`gHTaH6peyhf->@>`3jEb?d3ww1w+6j6^jnkO2#Ts?ySk!{Bg6H!E8qwFka4&Ie$4rhcqj~@W5y=@!3jO8{v62_s-;s*ZUYCIF5Llh5V!<3v@YTsGHi($#ns^~-0l8;gexpV?uODKy+1-i+<x+pJ3t;`9)5w<=yqGhre;*B-l*nUOiR9zL8V%hud^=aRU8>{5vKA_sE6VCi6Z=?70Rb^F@!JP;*?+e)u;IRrS*;}BAwwhbCq1df%oBJ!)Z+vEB`4vfNZM<MjFGe*uK_i(W&H`EvGeFu8la8^>G|eyk2l7a<!IIui;R`86Izp5FYV_V1s^oYbxcrWJ;e8!UJdjtM2`9!<(Hg=9)!J%5u$mxsYoX)V2I=!~Ql*Z-4i;eAj71u<N(EpP${c))cxxN37BF`g=|e=$peshw&$mKLz|jHVlhA7F_IIsBJzY<8h(W=Is_a5liwfyd?T4TvQpa;G)>pi$MSJYV8+Wiu@t2<Z>?Ga@RJuX}s_fbJULi13f1IUH'),'Libraries/cache.☾':strd('c$~dfO>5gQ7{2FM7@wpfLfwyj1ac@%O2-B(?GA%tj1$|fshxz_2`OWTmSl{5KnLp>I~2<3ZS13i9Y(ty^vCu}av~{lnzo1OB3XU(>Um$i&y&_8H%W|Dx4!GQO9cal=Ld%4gpDwD97Ip)J9<Ls3wlOieN119X&|OP7H8N%v`=4cY^`T!Fd2R$lN~p)+{r=k*w?@eu7T;##Jr{FDh5r>k34%0IF$IQo2G4%;=?Mk=Ci}FzAu;aczfQ)WE_1@BJOHnD+hc>B9=AqLJoLIA{I69Vh(sgA}kHOWM{RgR39PB!a&Tj`MW9&QFo(AHpCpCUz0hpIM({$lzyN;O66hci=way$qgtsE;>%bjeW<N42DO+!oWbNtHi4B?g16(*6bRLjW979&D5ZW^n?x+B5bt%w9{@FI+Z@^${Qqa^%}+yUBPPvbUjbwL-eZ#aFsljvFYly)ly=`?I}qN6HvoK_u}G?pQ0YglGX!ioOnR8pA%AczaDxdi=JHW^L7eTKc3l6vXvGwYed1VQ0GRo7Dm1>8zd%t3)3M%t4t5*NBWrr5YK5gqW$uk8zsKlhDoOdw_w(1!?;sj>{=$q-uImT;q%2zi;>t%&1y!BNxbKQCW00Y19$_L&oB65l-|&<*l-)3L62a4!9m3^aok$cj5?{0G4>%_M8BiemDTlX<-sP@1oJUzR#QzP&#R`Igr%CqGQ8}veS<dUI%X<Wn@uUFA@W5%Bh=N(8gjO#0kz$;Cp8V%4oe6{ER~^P`2;S3EsUby3zIY%yHGg85j@aOT&$r$QM4w}8!4)Ldqs(c$*rU43)OSRWiK4#Mus7B|H5*=vVi1&SxV-21r+baS<}G_MQ&X4Tmw}8sWkfFYA+|dZl?Hh%j?9gO!wth)O0=m`|}>GVNNW*m6T9tB^K|Be-OqGa}gG#j~vjy^f%fTZbzj5*+i0Oszq5EWBNqF<h~|F{&Q^?9EWYJR4PvO>Bi&DCtKimJ5jR+u81ItDK0fh=DM&WshA2a_7{GmNdz_c4zi74v?HmTS{j9a@ktuE'),'Libraries/peggle2/rgx_golfatron.☾':strd('c$~FYU27Xh6n)pPn20{yaVBPE6ABAzVoP2unpBFkg@U3AMOs;EC9T<&VFh`SNeWF{64z}AEp6iZsgUNOkWxaR5A(-*@9gZCyhUyxdXRSK<KDC9o_j_M@_~HRXzfF{OINkqje67Wb^(h0UVr2ixj2}(_j(f_xPW4jb1u}5dILCb16*Sz#(AeO^xP>M9?kl5*PZxmJUw*1Ia4tT5aqzAcLQVR?vY_!uYCT&=KUKRSAn-XH1OfB`mPo!Pq?CUP2~gVk4k1)1^IXn4Bj?6INBd=Wd=(fjjg(O3rd^@3ed96vJsRF%erpx0#q!sj3_ENDv#xfd<q=oH}YH_1Kyv?#~_z@w^S+FRfaj#6CcYT<x8l1+60*NruPOthC{F9sZc-Po9*cKf&4}OCI0|SjN8Lmq=$zewz0v&SRBFBLNK-W4+b#IBl!j&pJSYs&DUb9huG?Cu_3f~#1w(5DNqT*%R-Dqg+QLkKUeaax9e36SjaP6uq?}095jk(Z6FqAj3`h!pk1*=%@%dLqok*#vZB12y(&BrGL?*N<%#jVA+|)#5_L->wsH_#If$*bi1UHQ&w-T_@iRrBYIZxm4ma>9a%2Ijxr=dyPjT9J=Ht0Dg$U4=-hr2;<kCn%+(wAo7@2%P3pR(rmmFs@>}3Hgh`|C>cUt>qxsrkoMKYgGN@tLrZqu~Lj&;-)D#Grqi$&ONuJ^0|NCr8{c$}<}ldSRX$!_E%yB{aJlk;FZ>yr(fA@dG`uGgFSC|t9^@Dn2lGD7-6zK|!71QdYf{7L?XmJ}7zbiDxtl%A_2B1i*BlA~dwu)|!QS#D!J>3ZmTT6%0e10|a!rg#&{28vhkd8xlboNE6FQ!M2_Xi|}vDNvjzOFX{WJ3Mq|1C%*QijRk6bR)!xS{o5D>KA*BmCK9*{VE?;c5K)dw1{R=*W8)-j?SXU3{$8t&zT>2GluT@6>{Wdr5)gYSg;NJN{(iBrObllR(t8@oGLNt%^mDmUMSp@Pvp1qEezF>&Et9<xRYUT?zuCn!HGQAjNA-QcDkgMIQJI)KS=Wx6;#nn!GDgs@=SgwpDKP)Q1gp|l8@!<wTg-oX-1OMNuO3Kr3#ghWNOK*&?Yo~Kod~leg|FZMP{!*8TTD1iBH^_!z1Y-9#v*#mgguaw$E8_HXwyPldoYvDyX40B&AfuJ&|AkZ`x9rqC+&`ROXUK<X@z8dTBmm1k+SgYT>6^G6g|BIN$uj#b!bzDQVShP11C2f6`|>WQ08%(NA}w0ys^z8BVX{qhe@QeAQ+p%|E#^Hc0G3zWS@N+l;FcS0*K^=}NsG%D?mL6%g^Lw&%HWesS^q#nH31CvajdxD<o)3|ACbNi9l2YKm%wBZA=4<E;>gRz{|+38s}P22#PF>);`qY90HC_{_$OW8z6f{zkMmnkyl*2qM<J)IWoS3Kaw?@-C&C)skVMJ&bTiO95#P+mYxCmEfh@P#c@-d@=!T06xCII0HQ?zH}C;!-vc?X*@2%KVm#<(4e%UwJdZT3*V%ito_no-n1KMZ|fGCbNFtyQ>}LQKBM=u7QUdRU&}H^T@;yHg!L~~UjpL'),'Libraries/peggle2/main.☾':strd('c%0=ue{&qgmH+EgOg81Jp4Fg|WE@|%ZqMh)hFo3zqht|Z)n+p_UX7&1yEB{Fk+nXs%Mh#pfndNk1dL-B#o2%hLbxM_GM6f*if?g$L?7V(xi4`2-s_(JF*B=`EC;S`6SO<i-LK!Te(!bn>o&_?$X-5q>Zi>2;nzPMJ9%Pp$@dwnrQs;`SK_1}q&3%D?Zsz;-jKN-tJPfB^|0NElgxEnj6LSeIj-BDVwKQ3L1!(T7*3j;cN$X;|8)C<I7yu(Tn$G~Fyud`!ciw2q)v7_do_C}`%n6Yvg``~{lIDm57cgo4cFogA2IRM;7l)UG+8g`pIHtF*ehQ4eD-?wyGHig?EUO{#-HBIUSsr<BP{B6y>oeu7qY9_t?YG1m98_FopYUf-N`<7RfCatzQN1yWPjj{*f;d{4SzA3{jvO8bN8{XH}VLD)~M~B_gwMe486^%x~mW!HL}au8*Jo-&0{Byh;E_n+u3u?<8c(a9EYXmQnDUu0ABSQR5-O9t^l#GWuLKOGkcCVd*3CFkz^cEpP0Df$o5Wm=pY2D44<5&Q)!T--DuTGyZtcXQq8NV-uc%n*#ibOwDKfO*OSP>=P3i`zM+%G@mXiz5E(S|m=3{tOycQ!0-R0g)IW*_D=2WHd^HLBekYF3g-Hs+yOzC?JrE?ZDCmcN683|^kmD=miM2k+-Ue2`n|;Jl3wwP(-n#S>d<XnH7!JFuk>BY>{9!eT*9U$#io!%b)j$<$TQA<-dhyQI<`ww+;++~w2m4)G()3W^)L;s|nbfN@_{cY{**3g%-R=rA>N(A(!)kxMdIg||y<y0VcJ55*&LoxXE*h<@&gzUS%U`mu)cawt+X>m6hwN^9OG`jeIb=?C4%-4F+DUy!hJ?dTFwh3)$V;27_FrGsT+S9Y;xvSVUcftN^G+SWUwIdJoVr>Gz4U~JtAf;%^+j)>7D>3g-U<DuZIvLs5+*G#^EidCWq;s00ww=^l+C)pB#*_$t2ubZE8a5R&hxiinhVBDV&#5hrQoMDjYp3DjLo?KEyswD$_0g=7&TvJo9qd0SVJ|q^ahN@nl%2*$u}X0frz#RboCDKjuQ!gZs9KlH|*H}Ki%9G;9US{LBA#6OqUc=*T@F=9@G2v&v(%~J=Di^OjK`6`}MDP-FuM{<M44+(Tz82t~*vBmnW0(_UyOl*NwlWa`|XF6D*evB*alS4c*AeZE7d(_roaVCUb-TcN)kmMIZcHg@Q8{#i?WT;5tFH%wN5qy{wrW7nsDy6cy??b<o&xBe_&rh-kAKbJ2`*$Gihna}IUlUXOd3&=2AXI0g8W%TiP+GNi<4$v2$WHCH{ZhG~$d36s`nP86YG(&~v|<9_zK3^w@FJKVjxu4d9jI~Dl|gWVy=fS*yLsnb6K%_haoQPgB8#gvDMs5Ut*Bn7nQsvg-)Cr%s+gW#7{Kzb`&5|6pa{dhx*8~YVE<_*T=w)t^xn;%!UxlA&-*atzvY35-AJ6`5s7@KyEb0u?J?>M*j9zM?VN4MJLM3cFkN?*bZ`9i?-ZZ2PlN3Xk#i~+B<@YEvX{@(STxd4Ik)$DWl`a1hHxYYOF+Pd|{w<HOUZEvoKYj560wh}Eq?Qmi)X~yckIj@c;vfi7wM;Z*2SOqU;A(99D0m~MTjhB-qOZX_`MrhFOg&>E>QSpfUfUY=W`-rR-#epgGBT|aNlJ#E515P_sOZto(Qa&_R(qy25&p{HdbVuAq4%b)skD5Nsps4|jx74F~1CTNzQUoAY8>T!&FEpa4Q8uFpjLGJCtS4t^ZrgyVMb0?+`J@0}tI<LP+dK+tvGXoS`aDQ_geC$_IDd^s&!K)i8pSg!y&z?}Wf|oT4+fS0bWPyYjg~9wiBLWKRj;PSn?eFA<R^QEuMJbixk2M|go8=~02<g?Px%*44mP$%IYss;Y25<qQa6QdpsQgr!U0vq7NS@8u3#lEy#zB5nzbOO4Bt4CPEpqsQPq>-ao%HI%nNg)W|d;hKVCP1405Uv6OXJJg)VslnSd6VKm{aT=+|7B3=mXc0H_lBY920a-FS<9#Iz&J&GAhUgcY4=?qzHsVcG;u()t`~jFTo^$zAPP^>b-Sb%x%ln}&T>;*#ddz0-a^cK5fHu@UA6JDi%zeG<%_U&+1}OAy`==JP&OLJR3FhiBGTo8&UZTv@s5-1onieUZJKvj_niO8d+O{y0m%jFwpn9)jEX|Cq=}FkHg;W24z(h#|->@0gPS3j}jC8&$;QOBm$!RRP*FguAf@_Md>4x@b`}Gl;oDN@FP8^VL#<?o90TaJ7Yl0X#u@t>qR%ggC@&jZ-MGlmxxE1#-6w$kiE1=|Ra<bZ+vgC@P1A<<HTW-p@W^IRE}rZl3ttPqH@~5<h(6@X!jllDRybaE$p4e6)oj`ky2J56eTOZUT8k9T?@dVOnz^mk1wZ_rNG!eV*HomDMJz&92PWNOIH`8njVk;Ft6Fj-|=@>IJSRct(%ZWSXm-Tn+iT*)s@$leKbS1^Qf$)1=#%?03C`2l7=cOP*lfJ`<klcLGIQUvBHGKE?QmIsvx@5w?ysfb*dIo$O2Ql>`ks*=V?Mbd-cWnzC^umCXXJ)216>!aeHbVNIC)R0U!aVuXf_6l9MOvS#8+D8;B0%KO0WoWC>uAnmN>CK%CrNOrTnJ2M;v5re_%_5c6zofcS&ep$@32vK1l#gM;)5ff1$RzYV4vS=ov66-F8&V=?IKIC99tQo^dsU1<<lS3c7YD<IlPWDkLI<IDL?+6{KkpxnPOa!O|K|)fvz;Kj?JkV~D9U)l@me6?r$Zfk7ASP3oXpilN{G3U`;H*<98l%{T5a|1(w(f4`-L??TtJ#e`(G&xLNaKovfgZ<R1W-WvbeT_6O63iLCS09LF@INsdZ$uCdeFJ)o~z7;?u4#K;I?)`*ci)pw`kcSm{d+?)Mo9#YS$JCgOTsOJ;L96VU42iixC38|LsgrcSRVAJsVE2O7<PIa?j1_o|~WV)~wn)OUnGzYhpPaca4y2URFBqFs)CCZRs?chRvEN*6cv+JP{9th1xauDwc8$DXK8u>!|dV?X2P+2aVFqnvvr7AkN#li9>{TW8Cc3mq{JX_JL5<01(5y<2wIPTm!74Zc-E3(P`Hg-S^fOR1C76V*coi)x)V($DIiV15jQy>R{!pVq_OWE!<|Wm_$w_%st{r0kO@oOFeUKZGczU-id-H0%niy$yNbcdHcWRJZT%LP`92kUV_3$v>cJIyp0pb<f520L{TD!3K7gcY7v;)d8m9Rb{AHVP~5xKD-+Le?mZNuhU?f<<5w8&pWJ*XOr_R8N)+FFs}x0%B_ss7H{<q^(Qsod4dmol?Wf(;2_lDT@8$C7BO%h<RM7VTDO{vYz<zKx#GSAqOY$AQ&Fq5)=1f?dHv-cS^Q}L8?LmD?0L49$FXVfwecO4K2Fr)}P6`%lyYNwefI;ld?DE3lC6#x}5}8xL3;&Y+hNI|ua<4v5{uNwI6hkrH1JktgjFyjGJxK}kSq$1d{CcAy_mii^dl#uAl;04kLM+*Knn)gCvn-id5k-}*HJXB*szl_gd<5x%T1w7`TB@wb=6*f9nF|g+6thx*nuuL$+QCj}%UxtmROYT>J+C5_G!edxlU9*qh-Iy$UD{r#2ljvj-LySoBKJqGwP?`XZ!{Bhf6%7Rn-($!#=Av?Wdwr=Q=hS4bIW$%kldVKWpNiGi?k%L*CK^M`5{(7fRN0TgeqW!VmX97vEi>*uM{_!6pTD&+vb<R(k&%fnTHRut4uduz$9zkL>6qS0&N5eB6dFm*MaU9h-9TQfI>!mj4$~~9K-1rGrJuJC^ttq5bwcI7r$IjjX=}x*z6gb5;-!YW9Pki<u;cL5tvs<wYbmiptM;6CA6w&GvH9l&Fm^9zu(9{qb!vB*#p<GIxiFw`mRH6CnfZWo%z|etA8|GHQw+^D^kq36MSMW_XnKAu9k%2r?H<VVJNZ}#5%K=N5dYT-obM_l#AjeL6<jM3A(*-xv4FWuq5oL(*t#s_ir2HIuUhDi26gBz$Z$vC`<I8B)cMCLX)FCE6WAY#=hjaNHy5H^kD177x-Tpr4-Ot3vWA~4dl5aUzJcdKN)p8ca1YeDq!SfJb~p-8k3GVAiEzJB#qzrg)<o~ZPo;-df>m<f^9bA+&^&bp?Ozg1$gBACKZVMlq^?R?ul}GNFqra7+h(VNxb#Ak^y!ah|z8#Pedzed8oP_9zP<1i@bPx0B;1(m63|#<$^ROxOk=_m>dx~pMpMQx*g!gS^Z3%j#1R7FOmzsu$|&xwiSO|T80TAr_7zf(_3KUs<rKIH6)Gn9A<kAtj%o%rvNGx%b-by)u)kDl_G7Sa7IEhFfc|iFck3d;3<URb5op0SN5ZUkngboPGt4tb0Ot3Q@rhZmb#F4=&Z#9VYKC;v5b;s2m~(+hHK#vU4VQ?hQ<HYdN@qGaby<u;`nT^76!}WbvNqt)|W$n5D&XrZ4S3{*6)SUYPv>mjvW2TQ%_o%kk6AD5V?V$fs4j!Vw&@7K6SX4yN^K(hYN*5-$9+G)cHfmMCrZ&OHq&4{GUH={yS#3n)G5eD=rU!2vo76&dp)cDK|LH>ksLC!z9OZo{?$cIAktVu7#EyGD-DACS?_jQz*u17p>BgQK{rKj@N37Bw>%)hc|wt!omZ3govKauKc*FvEQgXS5mnu_B4-L9OVA)puUP*n3=$!>)@a(%0rE&Txy*OPZwl`(<kC6Ea|E{Wx>sRr@B~)Gk-C!Ax$aQk-|_heD}5NGDr!R4(ubXUbi{hVB1N2U`V`6li=sFk10DDT#J1)%2j5;ifU`rqSokMfC;=F-Cl#FOkA-j4Y$S2kjVuA2UEwpG7g?pAMCjZuB75ijo-pBKzOqZ#s*D^>R;4#Xl+F|Nn~Isqgh)Hz?F*KA1WJj!p^b|!c3K~0aVPT%Z;-PD(rK^hl&dna??&X1!Y@zHW~&h$nlAdQ>)Hay1g_^P-8s3XV{b5wKhB&y2gs}dqlL2XO*2Y_1U&isDU+2{f7fM4pXB4FcY(90^@8iYJ8_`pb)ftx?ovl_;lhZ?MCb2IQ2W%XcDfS;w+;(>_)>hi1=*k9L?`<m#zOV<eNt4?3HMVJq}a|I!fBBIuwB3`l59GTQaK$%<7EW=vMf!9_UGF&BDtuo6tJMPANo-?D7TpN?AS309km*F;J!NmI9j!e+mi>eP0bzKOL27e8Fa;n7=K_AMA0TQ?s`-#yJ!DiQ=dicY>bNE7z`Z{ziWC>4IQvuPQl9rv*<I?I=&H@M4nS3z-i**iQ9~hZ2(|KP=RC1LQR=h2dWvW94viJtYm&c(W2DQM}Cka`ma<%swK#qfPcP@fvlA(jLH+6`ya3XFWe^PkiR1nvIlI2n{-WFz@)kFzJ9#Wkj~!2#~f#Q~t50t6+;v<MkvJ8{V3~3X&w=7(PtMT22|CJaq6VZWyii!z4)6`axMxS?%j5@aDEFE!il7&vvt)jyw%(8o*MO?5dv~sV}?SW!c-EX834wom6?sRKaq7Vd_u~Z9b|^oGQ*uZa?M3jR6i|k`;+=G+0jyl@$`6eQdC3A}U9HnTe<z^@hnlz~ynEc+OYSVC}Mid$7k_?(Ii%Go-kpCvF~tr9-S*$Ft^qR;tCTBXd8BKhvC9Uta{^#^R!ck3g05ORw-6gsZE)aNg%pM~^LfFgU{~_3*SZtM!8}myEtn=fUzJt=`q^xI}liaEMt4f^M@@^qI*-4pYHoi`<yt{-U?oN+>57o=PCE!%cJ(0pH15W62oH4_?!$?~aG)LI2{6HvzN8-ASli8wWK%@NVw0A#}0BHY=EGf?lAj*melq)L#qaabDPsR%`i&9dPQhwjD_7eXUWltlSZbgMYcY2tMDX<dxSkNx*e=m1Qyjqi%4G1_0+dE)?m}uBBiF^x0H>f_lo<T<1HzU^tXoE)>=GhrKu*`aTAabf*KR>ug<mX|blS{`h`3>ZZO=!|bNFO55L`HLdJ%m4~rP+r+=O=LD;b<`au2j`>e69zMoa%a13k%|u8i(5xgPXM|LRDvM^|*y4T6h#NQfuf?{ONwn$-cF6mBRy{3aX_a;vzY8-<98bbQl5@OdAEdT#*xEOA7LhnOvwj>d)$DcuHC%4P;q^RWN@Qis_&#2j;!9s5OJ?Ln5#n|JJ~uV4zTZOFfo<bPaj0}+RD$D3ZfR=$*pOmHrMKpB^9z@0#?eZz+ewW*5mUj|yaH!Xd)D}vTr>JIwM&9VoxjG1Q9jqP@SHgtp2yjaEMJqaG_4gI%i@9=6M0;Iln<`!z<$Sqc!X;$v6~-=s|I8}{ltDgg*64qgxcB|b91t0?0*VLajX=FWlDnX%B1Zw`HVFR7Xs3435)Ad1SFh9Oq_XVqnoZd=~~D`WZ*$gUc;XL=MzhT`5@^=bX`W7v;+qX=d9GzB1W25L5#@<t)JqMlGm<QC;~*WL-XEMrd=G-0Qo^c;)$2%-GUgX`zRlw)i}`Qu%&~r;^J3z-|NUz_hUc~(0OTu#oZU4LTt)T5Nxqp>%Z^)+Yj5VUvhwl+jZQZYi)gcdF#{7t?Qp}UH^J(^UrO3`-}D2+4*_KYvPZsEAO_S<$q?}I=xVp4$4Xg?Mer+($=Lfd5x`0UunhsiTeJf)j4cfGWQVdY<_ZcrhzwuZQXcly59We9^Hd_@rRrQ4wHHyWE|iRkOW;!KZ^-+03DzaC<Juzn|nlDt3G{*ez6v|Z9m%rNCy_^FMt7X?zCPBc~)Jq?dey6!3Db90Ukec?6AN1)X$Ed(pGPtfvdFmtP<`m<U(z<<n4(JH!eK>?4PbtvOQkxs8^s%A)$)6`4D<;iHoda*~$RZ2Ha|Sb?EOR-Pi?*lCy0n6|EI65@djs74aw_D))OSwV_x=2S^x+r(&N^SM-_FJ_#0g%CJCI$u}E_iP5V<>}iRZWVgahG=S=!YFi*f5K%x;<NaKTv`itF^(t|+`=pEr(X9fZ-v!pz-*kGBd?T(KrU%@&rJv&BEWssta~#sGgEjGxjm8S7IaWzxvlGO07o9Z5cJj37L=bO`LkWRZLeTDO7HG&eE^m{=l{El*U8=FJ>~YQ1%G0?TayiTuhU<J=6wMck_RFIEg`&r0k*(F#M=tky?e~7c9>Hk~;sGp^DyM+z^ce#Ueob2yG<ZL1mvO=1{f5+isfXpg+MO66tzHkd%WXnguNws({2lV(bm9Gv+wBYB0Df}f#L}sy#lt806jTIshEH&5VPbi`Kk#`4Gh&c|5tL#UuQ=XdhAy;d@_P(S><Wvj&<=Ze$gvuxymMFPO7-GkSt9Xv_M3dA0~_eaD+DE;{DHHMaKrZtiLUBI27>ek&<8DNh<g*Q^^C>houtbXT}Zl@6H0})V6Z$eqOo|<D<&u}yUhI#rjzRA1gDC}d;?tZYBXu(3#h%8U2aMh^YHnFrj#~lX+BxkrL5hQsKl86$`zZ(qh>JUdiqWIu9|;)gc$FT{)LCbM~?VM{{{Y)hf{p&qW|L#qDf7)MFma6Vd~3aB-NA9rbu-5uw#8-O%J}C4n%^d4>^n@nVc6-6r~nhQ5|T-$}7O<+q+!O9oS=Q0yK(7TlD2@B+HI^+oms9bXyIR4T5emzFVwzCRtx=@Odh)%Hvwz8G&XSha4V4JJelM^tuhKb3t!CggyahZc80*_}yuVtHY<Xb*BObujvqXFUoj)Ud|WV(_-Fm>8tX_(4A`BdW_=fjrMeP3-K*lIMgB?)8ce_3;K%2G|ZO(7fu{sI(mGmTEkjG3Fg`rJc|1vNeX@;v#Tq{e0H7i+Rgl7OoP_)da$v!+zmFm?NRgmcHNhiOo|R9>|VbOy#<5rHXH-L*2tIB#Y->=Xk1`Et9im>`r!z%Rtt3{-#vh4uJCHRD<`?<`d=ZcKXm'),'Libraries/peggle2/gram_tools.☾':strd('c%0oD+in}j^<7^vSwO&yJQgGwMFGNW;n*%}w21{<0RkxOf}&OwVRDz)T{Tpi7Pc%)g`JBpvLRm*M+xjEkl;A2EW|<NJj`Ps`VG-9q#uxT=C&6tWm=S4AcSS^o|!rK+su%PMR9ff{O_sj;?tQo#?PLca9v8BwpXt=y)lRJdNY`+HY3V7bsWYRmut?BQ^qDKJxWFiW0e8g6;oL6xb>hpQ;oyGKLC8O*NNSkAZ%6RSHQL=J`~@G7wWrIrp;<=YPw2b_HA)fe9wnq<c7Fb5)0yySfTLs5Al$`e)esAyd*xPVuMjST`I%tZE=NCvyu&u^WOmn9@1VA--;&`=C6u>QcGh&JQ24_v|XL9QTg%#om9XIa7}=1J`E2$D;MFB93j+sr!#T_rD0UDg^yA+MUpWo(MMu4k)&fp;6v)+cIl0?rxcrCiER$BRdET~Uln%&?-g;A?q0*VB`8T;7hh&b^o$xlM@R>h-<VPQ*aB)e!k7ojLf8Xwmv&GtuPo6m0OmUe*_(myG0Nyfc_N(ifH0++!{NFYgBy5Y{J;EF>ZK#O^^JO3yUkmoTA0LaDaNc5Xs*cnL^5-Q8D<m3vw>-EMwxUyStyP1fRzRad@Q(BPIyY;kdqpKL{pb*xgxDm;3xFrxzM*FNVr|PC_VvKTegc)vB^@L@rAf5zM~n&%tu4Pm*w~5NQK#Pl$T_u7cpX)u^cUk74a=K1cyCv=r*`;5AxVhPsNm{0~w(bk9`F~pNcCdPfXAhF*e+ujGB#_N6~Ni7^}b^<B=Cv<2Y0V{&1R(X*BRSnmmqZ?59ruksgDzajY^>#BXBwjbDo4ZG!ye*nf=6%yEeJhaA_Z{b`{CkRUYXUBaPTV#}aE80Sc=j|p1x@P#Y@l0>0Bw0>tAVHCSjW7>--rs`Z}leXWYs<z!qY%h~DOa_Wp)tGEJ4Ktw8O3DJG3;|YEP11;nH0gnR5`~&Vn}ykfaU2T^J&PTlW3Be%So;t@$^V6d^3<FpRTS#$aCCyr+UEZ$*;;j4lqpqunT&K@d?3EhrlVTWo<9_w1T!;$)CE#^#Mc?s+!5PaE{q##Zqo2c#v9Vf;FY|EX6Jzej8vdg)nxhZ;nCD^zlxCmLB~&OAW%Xm5hkmYn$bqG_@%0RF1H5#suWi|f$lS>47P8rD~xGftNdvOAai0HYi6l#H5p7+jmi);BV*n09ZTaI%i%kg$M-+AYhs~Z?HhWyOLW^o)QB5_ALUH@wM``W_As?+&{Yj*KZ2YrHzyF|W@|FSbfx1b-#VA8g<O8!ESX{m8XLteodT;}oT`!xEAS84so91`vBjGW--}?LY~+~9?okN{%SV|Sm&BtYjroD!3~JRTi7e>d*+$bdzVvW1s-)aWzJe{uaZ(WAY*+iJ9WzS#Xkue2D>ze>F7Aopp&<j8%65;&0cZm@ap(k|KiBfYYV28dWu1v^?agu|!?L3U>PSI;Q{F8Jz_ZKt5sFbkjsvnsNm{KSd;>U%x+KJ-q$9Q3XV|1aQ=wPAKr-NB4ZqhV#PB1X={=TRn29TWD3Woy<TzqrfHopGnhnCZaO<5@MKz2(x9R!hwOzJq`0cqE$K;Ow-D>E&jhU{P^{K&gv6MQ3SY(v?K}-xs2?2s<MB_-E0EK!yOOQaruam*(_+aF)!LF?GZhUfkBrwxxHeEBxoei2^<W5ziMlG-Pq?AZDU#UX(*NBUcG0o+Bae#i-Q#)>%$5_O+9Qj9_j8y$;A`uy|4A*Yy;}sfI#NNF@M~a8jqi4fluNu|e?zNW{sCrm!xzSu$_rm$4I7t-p{7coTWyt%b-V?uClQmcm-j-r=cLI@nR=rHw8j<B<VuIuizL(lExu?d8Gg!uJOq-pG1_<8(LgApC+v+RT>1hX)QrqxSZfAn4@7j{_^N|YAIJRW?K<Y(rw$AW=Ks$uxy>|%9{e){@Ck*(}{gDhi<=pZS(4Yjz%cQx>#)(gA>597{G~*?xTM{3L9JCEDrWIfAsa4vCOC@G$qLzUV)QNfA_p!`@X4Pye>z*d({An+AF<Isl2`cz=c_niXGK21vG3$hwbux9+pYF9_o|6TW%WDUHv6C*!K#>hs+iedprp|~UZ1u@2f`IZ0(B5Y0bG3dMJF_pwMk{EEPsEn^oECGKJNna{g{>}p-4=IfiZL=YM8p$pt<EV1GnP!tYDh}YkXxrwj(0dbT?cV{v@I@kDGqj)axiSC+CL1OfANsF<kgVs0xya6<RYpCEue%hi5s>vl&hG6Ujs!f*pUrJLoQp~$24<UsemgOE%pX%-dugHh_A$=!O>y%Vs9Q?0k8E2F&^jjMw#pDRMRYKiKn8uHeQRZ0k-wBmK0+7ow<>bkrVl<lKsF^LdxWCI~Si1o_}k6@W{@^?|NG|m0I_D&+A%MsE63F|L1a43mfeiUVw+4zkdlB8GIqe;r9{MuTJ`alnuQMts^(XH^8451rf^9PoIf3D%KeX-VER~1b`C5GIfv*d#!+$d@9ybH<Tr+lnGi5dFZu*KYMN*R-;*HsdUT?&%{#6Mh+)2Z?b1eycQB3jms7w4@+ZSD^KbRMe6+Y^ued_chA8a=j^=X*p!q(cQQ#=_Pp;rqwYJ~<)V6;--fjHc5<l8m2>W}P@PZ|<It+4I#*mP3S4!3krMm9v-jog9>R<k2qR;qvMYzA4oK`11dZgE@uWI1RW2~p;0?aafr=lMA<O6}(~(#dWyZy)!s><I92#fBil3e?ZDKs_JiZL`WNcCT+t+p;FAlO{HiR%e1wp$44l{*HX4<c{;KiBk2r)jckFl&rBR61?g0yYZHF|U6yHfv~;+rI$+Z+u#^CN8ylH{*}0rh)~6Q@qOr{BikWSn<hn*I@n`QeCN0x-OAa@2JczGZ%k;qdIcp7D{`bku?WriK8+j`ltYkyr4JI!;@+kPQvl(2!MeS3>ZY2?nyNA*+^~P0fX*Re0*?@Ir8Yer}!|&!0m&JP*NHI{Q0ZKOijeZ71#LX0|FI4o|%p3#b54Mo`Z<V$MVyZk`aDIc9Nq<`u`g?r<I6bx7B_*o$Jxvl|BiI*88O^-?(%rh6AWELbYUaMswbG2N;sLU9ZtRTe}1#>kue6K1B04A|_l`|4?LV(mP!dxu8M<Qs#~5TG)VT)!VfZGJxM0dh<mWtoqV(jJx7Vfov@bgQ9%)kK{rXn8+wJ^1n2P5Afkwf|oI;RXCXgTF2Hy!~QlVc~+K500Y3jrCGbTddSQo!P<H4I_|X*zmaK*zWH?#`|x3j|bxe13v?iOA6B'),'Libraries/Compiler/gram.data.☾':strd('c$}RYYi|_S^?QHCmd4VI7e`<TSp|)jhtnzw1Y~HFcDsz$_GDRkU)fm)kgRHp!8jzi>uiFNu~`y>A+2$pgy2V7kQ}LB`;G5AKcKSYKhSgUxsP*aX4iICp56O6_q@-!=iagF{(ST2JEsN*-FH5`aDM30Mc1`*h4OH=;9K@#>(Fn9PMtdhzkeD(a^%P<{4Q7AV58|4N(uIH5`PZrn?2_*xaZCfx@X<@dxH9w33xpg@DCBdY8=L)7>w08j6)%eg?ud$0z3QeB@ME(IJ@Nf6>r3V`u(XP_u_?j&S*F`>DNZxv8$sJ=;Eb8_q`7WFKVFS!k9Z!C{du(XWw(roP9q8$gnZs5TFT!-^Fac1TeX3w&?bp>!DM8Ow9YWV$Dwk)6Wt+i}zlV`H^z52=i9(=%wY?svM-0t>r)QU~1H}`2Yj*N;TeQ+`K)(FdREm0%q)9g3TYPRv0$xKa<eRS8A*S?eU6(I{Dp&o+MiYnE3dx96ycYNYB6SyCc~`!S!q7mHeoSxZEq*kujVXjCSG$zfopjfHj2dbARKF-L<I~45)wL1pe4by@r{YY5$6s9p%tq2H*tSSwB}2xMn}wS!}$d6y+Eo0F{9oPS-gsD3?tIQ?u|#7br4LBDnL7I|_cr^$ku^`RJOEb(FM=HHK94%1JofH?>RxqJMzdI$>$j6lUcSfl(k$<aePNHw2HJK%5%U_Uo>AY(n!m{vh{CK~5r`K|_cRF!4gnCL*6b8J<-PBYV;uJm?9<JKtbK=;3NL%N!mJJc)x!a;Etu-W8cf%_zf6hQ>N5OL`!WWXv+)%MHV}CjZifnExjd!RkXH{MUkgnv0Md&8<#)n)e8Q4%I`*?lEql6Px_7nS{)ACM!|<#e8CjbXTH`BoQw%!Rmy_V;e0_^cpWWs^7>42ye@DSW#OBU(ufq{&Fj5EoZRDGcK%Jgr}hrvrT}fg4R<3EVE1Fwc(6uVS)~*G+;&m%G9^Jw(zjqDwuzuGTNj;)7mdho2nk5rp!26{&c^Hg5^6Vs>Zs3ihU29me?=?8Op}Go3D9A8v2K+&r%?}w-cD1ie-uu9Srk@1krz>H};8J$`-|X(XSTuj_~Ei&f-@$hy&79PKWgI=q2oa`-#S;blwo|D#NW|njK=M3o2z(G@65;Dxs?+NQ^N%qrk%(h+z~f49)Pg=N3?4yVq8<X9#_3?5Yc@`~m}asjG5A1Z)z%O|?6d@JBn`)=jAo#aXN@IyoD_b`l9%sw5D)oomPvgyc0vyJ^sF9)xzYJMCr+?WPb`sH!86O~Dw2i{P74`20eC#3S{PSP+8b7<=CBNw5qmY%?ii=(P$aIW?uC0_)9iaOs#aD$8)4Yiv(!E?=yatBB6KrkdlqYwk6Pvyd$gV@+KeFAjTE7XV3DL~aDLxx2ESZHCoiU1VJ@2kU`nca54bpsa({Ad8E|y7#eG4<|BXkeuO_`}PWx%e~@)2EbsDcD7fvHVuz3kP&@znL>WRsqZ5^<2Vzjc?e+N+)Exk4yCLmTjn1w|BVp%%Lq79Lxb{y$+~(a?~i#^-{HjwbMX({v$}4>GG7;Oe10gV$_ZCIQA|{s9F?fF?JzdJoHZDqj>VdmuvMk%`Ccs{52)###rf}d*S>GT^EEt6@H~O%DLmi8^LKcj!}AY#zRR$K(>@p%q)O##F<S_i#ZNwu^~c%C6or~v7ElMEr`*s{W#3W)$s`Vr+YXyhW7u80b%WGN+BCK@g>*{lkb63##3EgCPj{3HMAgc(=HBUFZ`&QyKNX^qt>%0;&+TYgtOp&3kmsrfRB>?%!<8B=L77C;3V|E@5xZUxBvZDXqC9w%2PP@U*OfTs^8ew%BRp_oSg0d#FL45Fo;2N}^C1aQimf9YBG2T}%d#v{WY1%?US{=nhTVUt>N|8SMBnY?*zDrQt@-1_@^Zv2(M}B*>b5$Rj)UhL)FHK_nDH5Zs8c8nGl)wTy?#NS6VWVWv*no&@rr#ntjFi;QT9A}!jsbS&673V+<47r4BfwJ3_-=usN*^f$k%awf(G4usU-Gsi5b@#kwmJ9&=F@+8XT<*1Htmmpz#3y(AvgTR6ov$;~~G=iog)0DqFBLmJ08wKuD&;-nd~S6_kA!N)}-L-_JO!N38Vl=}h{_(M)n8T|N)3z5&*}_91KjI@|ZrslMN2lJ<nfx|t+D6COMBHt+S?sR?Y*(WGs8=_HQyWl~}+rMI4vmou5zU0?f`mEK+dZW^9OCe8Zrykd;N$X$58!qGlx-W0<#@Z8hGQ}EnojnCovD{Fj-d@BILy&mH-kZu$L<bmJMs7Q2@3WmiXy0KI>uM$yW3dJi(N7j%2xF{a=RVsu!1h%6O@rD;@CtxWg5}oYM6>#e1^Ieydi;PZp7@@t?%voJ-GVr_15X<X-dB&BO_Ywp;1viIrsb3YaihjJ3B0$v;P&EQ1=&<w3>O)JvpAhLAF~b%TnG!5u!kS+Ym2IzWVy?;pC7KN_{pvzttj1uJ<;DC0ilQ7q9g&v!PD$=E#jn^$wqNMH0%0U>?&!URTwqHWi&giqlMQD_RnCEfqNd1ac=;jj&UtXIEk9u(1E-JipTUXriQ|WZl}Ao6UEh8k+=ZascoE!Pg<TK!6Uf;?>q*dh96X2a5};b`gN%H8XR);cjn<F5>sxc}#zwpGLwojCd$!(g+;2C&XwOc!8$Y%i5891;0I><t^-~>6O{nz_QsA<}?k(+pnEZ~NN#jq(vQZKgBv}45SiZyDoVo2Xcy7>o7PP*_<jrD^1r7@kP(uP!Hv6k@WsKK1WT#Z`La3*O{4RXWLspoDhP?h|ZF+Gk`_MLuRd&{3E??hd7N~Cl91l_MFkIhtrfH^Tu48z9f@ce!e`<-~Y(v~ztleO?0z)w?Jpgz}&s(qIdBx1c)(WzZHCf78x0gJ!7JJL6-&P;;S4mo-d>D(L>%NKA*oqA_2P?j!1ZphOy<(+y-Iccr7FJ*^Ds;6FTaV#Ygq!n9SX`LLWQ|4EJXUP9u^8ptTUP3qky+bP@5F4oR|?h<Q>dDg(u#|n4y6!NvnZp;32J?Fla?1s4Mtg1-waiQBvW=F2tyHq!aq%Vf-|ydU5-yUB63^HjPFd6Zcqlv17H%FAc~6=nES<b0&`~qO<5Bbjp8n$hGpH#x<?Ji>$gqdqrx8268+o>rq-4Em3N|Zt942O9yi_CN4yz)rQ2(g?+=k5*eCh^1Ck#w$%`|Eid)BU+^sp`lw_YEI@S*9L_%2U8i4c)J?)?fo<EYUc%gEh5LQ?q)4L;AvQ?TCB0<!Ww;iEl00ns(jtzxcUlR${31!axkiqQGFL!mNWyY!A4~Rg{UMCo$ll=t%h7pe>A&SHq4OINbYgsI@S$nt&n~0t&mPb`W)rmjVn}i)@dnH3tzh0Cr;UX|M@7Bu2q@FETH8loFO}g=d+Qt$H%2joP3=3?HD!BhjupTYMh5UC{v5`txAj@$flPo}4*Y`e7;57=NMOYW_Pm=V;2&y#7Xtq)*TtDeZCMb4>fn#T#T(vx2QL+f`ZSs0Z1Bn%IM)yi;1vd_nKUd4<d07r3opi)Iqv@v!DW#nf_X%v!uZ^8_AQ~ulh(7KmrM!%k8j8G~l#`qXjghk$3b<!`;)E)(BUb$8M>bj8unvt-UU`to2cgM%Iyp}#+j9%tdq78eSihINf0GsymJU+bPA1ZFf63Uq21=;XAIklGER)+3UoHRlK>WLqBWjfYt}IXd%1&RFu)S8wk%;j3k2W02cUrAkNDA-`5bTFezL`m1elr6TZ)Wsx=zpOO*|z<Q{{eqn^lb'),'Libraries/Compiler/generate_operators.☾':strd('c$}qJZBJB36#mYyxV;I<j85t9f-%`-o1$QAs)e8?Cb+#>*b8pE?2^5!LX8ces70G10-+)=TZ`aJ5vv8Iq95j4o7mq_{sMoX=giB!v+KS1(j~*r&Yd}PUY_&JnM?R3KGuHh3*tD~JAAagt>d`k5MuYcy}fxiVN=$dFLq_}9-)lbHl>t_HEr#L(oRA?w&E70={gcAsXNns+I@F9ZSBsX!$(?^DZU1>vbmDuz=C4GTgsG+B@b8Dk*@r=UNS}OosG5I(B`1cLtB8h2(1F`7if2&EkU~rZ5i4MwENH=Li-KcDzrz?HlVFRdu*fdVkxVIZ`FJ7|D{dq#g+^ocjrs+n2+#Tejm(>Z4doW@4>$q&Vu1*e3kHF{)%ssqirp!%Xo#)@ZnT~5`K-};UhRc!++;5`2#}onZB-U#)8GG{3iNkj{m{0>&~?#fsY=wKCxi^7)aNTDYf=k;>S~dgIas7hNgX##aSF&CDf+uw0Aa9>g|#~KX{^pkT|34`~?PE&Y*T9e2ZUXiGBMZE~UijJO&AD0)H^!@a&nszClNN=6sA1r2-C63t~qvz@)xhA=g{V^a<}Q@w=e(WxkY5p&P1gM2lpPHk4_u$N1^ehU3)Dd+r-<!LJEeshlfZeM_#JpiFw63Sn}El}cG)#mXFFMo0wfC;89(xn6`03iM!sV6h+QPUVNGY=Ch0WpafS$V?HkeRU|cvv&FEsWY)yV*mESUDa7!hv(*lW!a(IS67VT;ZfD8nml}2b*`>_FMFL|gJ=)}3*c#5$=ZWP(Ynw0IKR$ckRFj`v@YxRSpAuj=Q=uLoSt0XCEdkB*)5bknyj<nL;91c6Q7@S4tBIQA8!Tk+Xo;+318$7!NsZ0G{zscU|$srE(?EbJOyR(Id+z@6Bck2wCj9HdpUHf4Btl>KFgLNz+lEO6oNc(ul8__Rn9?f)ykD$onAiI?aI`|9G=jr3BRTwnF#HSrG;fQO(`|ZQ=o>gCy2Heyy9yUVudnv`TrX3+blZ#BEa&2KL7|2;q1lKbW0(rHjxyTBJk(=BtrZ)f1HBfQ;;q%sK{Uzq=Odc4fb_;p_vO`^L+GR^KqgCPl0)td?%vk?*PeF_!XUJyV{y7Sc=Cg;OW<oU;p{f$m=a-9ZNu7k3)<n2$GghnZuC8mm>I~v+8G>*7(WG^(LkHKk`X`w7b~XRRnuAgZU4#uGbA`f!b*xS<OA~l|p`!M9d4v&?Nk=Xz<+D4kb1dxD#LWZK)^2zr}xlgB+1e_8;*1QJ~&PvbSMWEN@XNpb;OYKud%IbT@Ye*?6BXYW9Cel@HkFCU6K0(BJ@3u}As`M0BduVk#$?fDqG=VG<%~y{N*c`6B@^jMu!+yRg@(fmpL0h*#y3NFwC$SwDp;0L^KtWbKkWz*EwRpXziWrUGN_U$&AMvKjgh$Cs+c<7ricwX_}~P%FSdwGsWQr&TWYdqTh@1mi{o#|m>qfuqfd1!N$dGUiu6n1xGxMwdzRd|5A&94#`Z3Bt4M1W>)I-cqjDGaG5(uAr#V{2fi)^T9IV+vsz}C)j%i56Yr~2p(sO6@?suD~O1u6gHR~MEp_K8Dk072!&fyS}>nEMM!w1sP9Sy^;MTQHv?J^3ZDTc6NdPest!t=DV+_dN`S~94XRX8n9%;14S-8xEEZ6$L<?fM0&0tI9IM4Y4l(_M*j{-s@7gpN(u6DUt2dqF(*e9-vgejF<#LH=bSKn$=*EL?%)omi;Js1ez2uh9lnNFoQYXr%Ubh?+PvuM(R8OL!%EG9}vPI{cB9wrK;40(lYARRg2|av8oeNg|`*hV7l_`u)^7Vkl1!*hplM`R=tPM?sPu|(s{IzyANdD_d)bwXRRZU09F#qpL<oxk4WlZI#__V3~%J#im<`T8aHmh)-r5b{nwlb22DiTaI@<x5&c7t1N+On(6+6Z>6(hxm{Za~v~ZLLfpYZ=PHv7mnVx6si2eR7=PLx60>VI%wo>_`=d6Z6ED85dwDlx++}pcD$OStjQgIVRvPE^y%t5KT~3^r<cNxv?pYQlrG`6LhboDTN8h>(%kJ;s(Etq-JUbWD`}Fzx|=)CSPG>DOn+_h?ukmP*7>A!YF4@o!<paZrAC7vl&kD{vzC#;GFI;L!}a1&=J&s#*+pyrqCd&L(TnIgbi)l;_5s;E4np)(8lb7oiNC}7X*l1@8N}Uc(kpf1-t9pL(ieRy)d7|_Y|9OiNxV$d|g2_#ErVF28JqQw-;7$)jeE=Z$MO;on};?rl<if@W*$JD##li)yiqD)cX^4yHL<-Ofzt@*uuPa4D$zkOM7IOnoqt07@xHbfFjzl7})i4qfAPOJQNz30B5RxREX1wF(v_H7JCA6<)V`<c6)CEOabFV(>4Mf)%8$SHJ0#;Df8eqswq){vxtE>Qw4ezM2$LyeaFtRvq^Fe{d*Sta15?n^&Wbo-V=Zuu!<!N$uyoqu%N2QK!2&i!3>1zsW*doBb?z+C<}Sd0RrUv$L5w6r}ZShgFNOq#C-J#;%z4Nwj-&)W|5ENy4n%}7u1e{GXDYp#0dZ'),'Libraries/Compiler/operator.☾':strd('c$}?PTTdHD6n^)w*zVIzGa)!pRmsv;;+7VLV9O>{m20g`yhJO^u4ONgt0<BoK)9tL+(HB~As5;NaG`Mmr3saozUMcvkA0{j`49BW?Ciw`q^haW(JV9P`pvlvqN8*wmiPv#D*NiZ8jHqzR23oF(u$VaZ{`QnmW;`btl5{&77!*#mNCYJ%SB@d<0L}orLcr?Dum9|c0)6?eA?1fGsjjlU-<V*&0K#(p(C_R$J$zY5Zyt8rfH}dJr8oNLweTIjlzZYw3WVK=FEIXW}0T{GJTD42wfj4Smt0MqTKo%fs%b%VO~C_Z)urn1{L2In_EC8S;*?wH54Y@rlH{!#<xK_8cV2&Xr1{{x<DV%-w>Uq&*%uE!(i!GgtF<uzD!yI#tNN}AZJZBr-=A!)Q%a;3LQJc8y3R|U8Gy6?OI$Ip@*<O0{%m~*<jGIGDo<wH+07Rn07rONpv;Z&J=CZ_k^y4zF`IVZc4f#38=7?HZl@&RY_k-;V-$r0o_x~D~JY@Tek__V&>n|JLC)DH@Lz=bi;T+m*7qTPH>^~a%V?8!4X}duOKz-wHNl}fnA!kH=fzUYxd;t$8T2uT77a<wb!1*_VL2c_QunXv*iae*8x`o(zA4izC%IX(XZ8LETXu$6eCF7Ub2`<hErJYN2ticbapY;vIPwlF&FMk)Cog`i*$~@104vt|KKJKH$}Og;HD)hiiG5kj~`9|O@fmSen>v5%2+Z?iy5ucB5d<i;O5~zmVgfVy1~II(Yq+gQ&uFNnJbVRn&nlHYNh+KAWxDWluZn->H)ZrN(r_1=~OU#-LfJLCUH~F%rTL4CZqOgQ1_aTMvfSf6Z}wfTHbP!ij_o}E)dABRl2M2Q1>C!1|h<j8wv%M1^U*_%@w-h<)%|G3?rvzNV8KjAcaYer<TFM6CNzmmwsaVQDA`OGdT#7JzD}K9Hfq`6$aLc8-PnHTAGnTNe4m_loqnJo#Ex$PHB(jEZbZwyZfcN6K9WIdxxip)t#2+z$uqWcIro%-hK*vjDyK;KjA`$^(^Ca0haMupCu6g_No^=*qLDf)EztC_-Fo6c|D+gYs}LQ00Pz$8X!m~H=zJ@L)0FQge3Us{j3g<Q=@1AJ0%0ASV>2&n+CM-A&s+oGejsL?*9Y+XA<esIVp_E%@igD&C)Gx(2={+fi4O@_ze4>&0@T?cXXjk(CjazLXOWm>E-@Hl=Jj{V;%_q8K;wajI~$nHoEIO=(SaU>+}IZ5Ykyk;k|wdFm6rAqJz$hF2OuM!4*4&3(AAdIA@$pyFP^ZB>M!ISd^g<GN2#8z?-56jTlMiCFuL1vj*YW_yoX#kRYOFR?+|2Q_O1Jo?NKy?N0(t0Zq&Qk7EXFKA-B?A~^IT&<xN$*%@VOS7#6J&+J{|+};BG{e;AT<K8t5Xg?J2Y2DMi5yx#-R$*uA`i~u!Gj{@y3yHrjASFT>tsjOVj6knQIaF^^k<c+Z7s&FwW)0<Gh{3PO#~=(Mh$+fc@p)K3>o`wv#yLqOjCfP{qygB3Y3*}2Gy^!}wGdH!uz8Uovu=y!ymtox2yBFcVVwC^^Xp8MP9TPc!;7i<A<kS(n$QXPEP+waua&<}#62s{LSTWbRJ+t}#d{Bdac18;`mX*c>>b7Hq{2a|c%4+3OZB$I)kLhLO<@^WeQj5(_UgR7`p{llKc3yF?NlaeyU$+QThD3b&o{Nbg9&@|?uXG2CHTAtbl;vR*Y<W_0lf!01lk1J0@?<u0Q~~A1N0K^|D5C|oygwH@s>8VE!y3Sn{KAFLt25QW^30K^~$&H2?fc2m!_b)5<TtihCTkuu8i2@2lm|;wViQDD$d^4)$MZBc1z1gf7tuWN9#=VT1*k|(se{P*+#3o@q}$a?)?MWVuRT'),'Libraries/Compiler/node_types.☾':strd('c$}?Q-EI>{6u$RUtoCY#Zqp>(S;|F7(o)snD1d}Sqt)W9gH=20t~c#URi%<9kkWucj6*=7VBDlwK}fBt77&n&BlV_lkryZuFVHiyGwc1CT`a(oHM_HCzVn@*Idi7!It{J5yj1ZVr{2<Pji%#zTE(hdvI_)O;o9t(lf*RH)90sV%X4Q<lMuaWFD};Y@lO_At6}n$IyDyS&PA)<BGe$dPAN6`^71U9^a3FtYhxOv^EsfN?R#d`aT}KR0nnVL?OLAWs-Obl$?56OO63!ir8DMKX=d^?F5_rl%#g^MEXCEDU!1^Cx1bNJsPDgL9i1uocay0oEZ9{IR^T_dPmVzsZo<z-Yl7%s`lFL5*0P)UqTv(DJccV1pQ0|?I2MR@XtAK-j}W*5d&LPHyRZp&;1x=5!V5XlT9pLrsg276sUCi1V_%GqkPRLA)~$Iq<4o9!r|^UbQg9h|;SNDUlxiPo@|7*(91vjxUIa|&NVUG)x)gk<p?w@8;L3ik?Jc`YV*0}9JpWKAFjd##ceJB!H7+h#ns7+*MEN{vc~<2sSNe#n74n?_4Y-S5UV%N>Cl?*xI8~k|5(cNAK)Z-T2iCY<_)14+4em@Tuta_Y&Ur-8z#ZtJ--A~k1eOw9;4VDoG37ZhO3?)Tfb-jMEjB+kFVbRqrbNaln}}$V{QM#};7?TY`rgf+9xC;@Lba6HYTA{!sASiMzLH&A#JUap@4!+9BV^&D_Aneqrr7zY*nr|e2F1+}LG8`o&vu4mcXWMwI6;KGt+u3>VabD}C1QR%Hb1VkunSvoIM@h9zOW;r*B0Y_IU+q#hV*b_w0S{@=1x8Uyg~v&KDD76<dXpECV&EmEG;(@=_ka06{vmXvai3f-1IsTQNHQ^NN!w3Oxmy;DBB1tf@ChXH~X>YL%2%DBhgyTh}OGo+*Fd_#vC%8Q1Zsml2_G<x0_)~J0tNnhDy9Po<%_bABeG+uE-%fuhEQ=6A%yOQa*0M^GGfjDG;YQg&?eCV*(t&OBTu<xXjs3otq<M%%H}1-y1wV{$fYrOZZWoNEl^52>n%|b6vq_Uwo6M?d6!%@?4ckJ7Vd<5MHr;rB`+nEF|QE94I`F8!D_M#-13vdBL*XB^6dX!D|>VS)STWGHFt^CI_ogvFa+U%zBlBb+pbae?}=u=a{Nd;AtibNtk9qIpH(By77r{PfE)76O^SpZskyB^D6UGNjn4<Ca)6fj#&F}h|nIb|By#Vnz);Y^iCR*khcVqF|OAtHV>I94C%ul(aA8r+g*0<VUsH&q}5v5X=e#rJK63g4~9V(h<&B&8If0~8GU2zu8cD)u~aJJGn%!upviQRG6uJZ4wQ??gm%Uo>!i<kimsx|`jJAog2N7#y(!U)I^_qR%s!EU*n67`cEuD>c{TU-y<1Py=Wq<569W)ejwnKBMco0&Wa}luzL&8%_H&Z)pDj+PY2gjBrAo`Y3GiO7*^6#d9yMtnKY@eL$38z$A=+CU40?@BfX5MlvH56>k|(3GJ96I2ZVk4$oO$%LZPr;D_*{!zZ`NyGEGqe2V{mQ&7hX$arz&EJ+op?sM9dVXCio;<Bv;&qS+}HnI*q=*zIS^a|39(WmhG{FB)m_L3qgDw8$6CiI+f$tsT`k=YeRJ-c2q?<su6Ad1=gk}&xUt9q&vcI<Q?=#dG>vIi0iCd7<f%)_@hJ#e;9g^U5kUl;j@P3Cah7_1v%)&g9~zMS#UC`m!%Gmi18V4>^9xcfZJfl<{><n%~qy?x#(Rbx-2J~hb(d5PfbvJ^Iej8fW<s5R{908ajyue>tbA$qu337wBhu*Qb`}|^)3D>FmJXrIW=>#T$-Ml;}ZV^K7HrH'),'Libraries/Compiler/tree.☾':strd('c$|$?O>fgc5WV|XEII8|OO&KH3m*arA0llc+FKM^X}tkU#*XZ*6d$P&ha!P!K`IC#Rj5}EAUGfdhxud7t{tzFs8CChCNn#4X5PGAj?eLAw0EETzP29hjE0Z)eV_A2oCMNW`CMiV5RaqeU>ao{1aC9|KorNjz23dS@OF2w=ieFhyStQV@E-PgEeC{g4o75;Ilsx;3}E5}a>gj|4o~ryA7=iOMERLIn$7sqEARzgiY>grH~11<htU^O(lb2AAKV1V{)q3(SQ$4FcEe*85HwZoi2hQkj?$P_K4Zve9sL5&@Y@=CoG7NF7M)!ioYz}o8YzqoSPh|`?bIBUdrYl;=cdE2oJZ5A2f>t)_Y0o6S5Rq!6^8(}0f3O=g<nRQ<ooH71aKT4OqKMP=Ui`DNQ1n_Pi|Fsd7?JdER2Jyv&9unEkp?g=37w${-)3={;?uhh}`ael|b5YK5k9^Mcyn)84ra5V!Ft^#B=H(A7@c`D0y4#Cb5JGtZkX&XFS25wI$#3SO`qRaodIKEv<1#7-drmuA_+hay9pkAws3OKTqcL%Pa@;G+E@H?o_1m(7Q|bN|q&zQeAIn*xOLVF}@`wml}Ykq{};R6qFa4<=w9jq(#9^ITmKja8szm_;fDqIL&C4VIVV8oGv((HcXhS-vYf8!P6C2ds03Gz5al=K|89YMpdniO)mSgjM=uW6lD3vXs?;k{@tSCB7LGcFIR48?9j@Ej-@NHP9+BrnN(Ay(&|a;l&EC3t=X!LwM}Df+p+ZhrggFZ>5~-y3O`f=)f3r_6+M`Pu%VucB<C+KIVIW'),'Libraries/Compiler/tree_txt.☾':strd('c$|$?TWb?R6n@XI81`wVt|75c23AOuP=l#0y?_wIvguBmrQ1!|ouD8-^nysS3cZMU!y>g}r6?6CVxP`G@t1h!l5Cnra2}G`GvA!^o$s786t-Y{Zs9g{UAe2y%+1a(x-O-bh&i{Iy%KhsUYJm3Q_EtE*&0|Zm#1s9Q^neXTdGxxckznybf-dx?l4;!XXkKRr}R3>6UG`DpSMWNAH;#+ZX#kgh<qLi>EHl%;WsN}2(F+-kVe;HB<ctfL?i`dxxvU4bJ2?<(mzyo^+Wr);Tpc0?bdS*`>HYDAlFD<=16HbEI9pyat!fkghO}<-!9qn4U=QJQloek4Jvf26BC3#hu27aIM50g31%g;7D=z^uJlAAWlhsbS%*Qy5v=`43R%JIdPDI;<11Ld%CY@l^!gNOV8aHS!XA?}ak~dEjO$@aidMDY&_0=giYQpX*kxdwWxZ~fN4|t>??Fo{N*sq&8RKEX%|Sg0gJtz`2G8isY?;D3oWO;xIjB@hOY@ZGZDv1uEXf|gnf$weP5W*q;*9BQTd)uBVc*94Z{fS61V2Z?O(0u>Xy~mqeUE5U!5j^`%Odw5=5ESjplHVF0qjVphRsLVhF|@hq_V0Zm?nZ!j|d@qsG8cYRyeJ!Jt(>*ES7#^taCV}Z5%!%S5yO-aN!9N59aNLf#WuxZgWGGpTx>fHqyZuoftKcp6|QOu(Q0Hj1D4Agcl1ee_uayT(~qsLY7x{_L|Iqc#%)iW8J+P(F|AJHurq3w3*Z=aD<(^0Y~tOE=}KaOY@cDVg&<OQ<faP5AYRs3r=13xHVyE&2bK_KTkhPz*wBL7|x}F68i^L@$sM}-+&3zZ?t4OF>h*VOF~RP1sLL3dQvLrSJ0+o`U!J=2S4FBZF@B(%E>=3jezAFbjy*4Z(x_|0X7+{4QwK@6Y~`74%~smfr^7-v_#ycx){lj3Tfq1D7F(_c4WS(5j`))J<c*2+6uARc!ck?C)V(lPR8}YP+)|Q&$FMV8a9>S7dmJcy)u6Rn7DU2'),'Libraries/Compiler/expr.☾':strd('c%0o?TW=Ic7Jm1y=xqt9+UZzhqr5mf(t=^Lt97u2;mI0}hM9IUqBAqw)83G`gaijCF~*)T>m^)F7|61)t6X3=5KN@hd;UZGm?wTh&Z#<8UEN)6j{{4jjAZvrb=A3_Q{Sm#`~&{c?A)JNwTj>V{QB(7@e|c5V{RM;K{Y-TyPp3>*gjPYyUg>M>w2E&%gKk19C>Ye=J28Ex$4yP(L={znV|NUqs&<2`C@Qp7QW6i_OdhXcwS|s5iB^3pw(^!)piHhZSZye*qa=2;KP(udfaC$oGdHyC2zh|fw6XKXdH*4)X+qQ_#Zhs&Bi^PlV$*7F@Bb>@r}tcYkOlb-UpW3s3p9)!7uU0dA?%&VV*gRZ}NBdCjoyC)_eu()!sVQs5v0ae|T@wJ}M--!0!v0VF0BWi~Ujcvl}++0UP&^wOfG)jJ@UpQ*&XW^SiRc+^1JBUqLShVK-3k;FEl1^PwMA5(8W-Fu)*dfISucjz8L`z9~hAPzT+&&A+lL<b%{J{GURx>AX(Ihf-&u9XYYnY_VyIRs1v;92Pre6ldr9Es!R8l`;W}w81y!<9!M*NUGVxE=uLj;iKfsF#3N-Abx_-6n**8Gl~u`ukmwJhfYBK`0@S<l#ZEM<mZ=Ogfb)gpLWvm0w*nhyMImRNYhzzl2zA<%8Pf~^}#bLBc*yVPD+XX<AW<X(Xn>fXa96%D>oZngKB;L-$b>;xk>3VB<9hsgulr$T6}-%u&4A**&)$s!b2r<Jftui{F0F#b5?2aQ*XE8W@|BUa&Px3{H7^9vE07`!qh{GuY)1+{#pJtU!iebz`S2clWySTg$51}`4amhppqahn5BY9o;Re1!WL3B2P#WRN4@+-YRVbQAm%x~&TwP;`+4|VhRX2z%n{u8?(%JEn)k}A)s7vxyE?d4(YEfkJJp?UdesmXjmp<@b!KA}1Q8qENl1!Uch$D%E9eBthY9S-Jl9;pCL+7cq+JCa*aVHVpo9GhdT%#DgR)qMxa^WzB`^*1*yt!rVBuH*Ww$JSrTl;ugSp?|cRknv9CHUSs-kd}Sgyy!lKk&(5I5uCEghK?GzGqnCtuBwJP09qu#&`56vT^BOB!)`L?GXK6x8CNTCatn3NYzypKO`I!Ky4{$<-JYHXM~kqH@RiqAlM)%2e%L3VLBphgVqE?GO(*&%9Ozabm*<xB=t#^zYAhmezN!-AGlE#3ns{k*QEmY?dOhwX<|_=ia$J2@G-s<OX?b*|xMGG&lJ_M3^Jl40S&vt}>$bT82M!f9OLLVg@zI|Br0pSO9+I(`j}c%E2CA;!nhLg`OX%r$D(WVF-w<^6Qqpe3fqvg?5FQC!q@Fh$9q7;!dsAaF8A$a6MB@!5QiCfg0b^4ajBwn0fRWu@rD2K%t?B_2y?}s+;1uj-7~1ywQ^uKZ-2v)S@_*o_)WO%giJR2|(F$u2h_JrQ)0`RR~WuhwQY@@^AUq=q>mL(#n3x{ozYl3Ml}|?%$d9vLP~snsXyW5lFM9-@^4sw8vMa4t<ZBO)Sfz-}LqJN*<$$U4*eD;zi3%1!|SATH)p@zhH%%tGvG#+?3%-eLZ-nr5Z%Bi+GL&)7asdT@fjq^LuI1hgN#0pv0dpAVyKHEkB;B3L<z#lx~6wPXv!|1jPCm-(m_|4dbKVsw3Whvl#{jhO$sZy=88YHokpnay;cBvSadtJ(7_=^ak4ua}>)U6K!y&-h1>;+6!W4{1s16Pe_C9)v#EPiB!-y6e&Jd>vV!vgE-}}cR^I<th+0ZPP@a>qzmBoZt-tfq9d|tK(HjXoR=U;vX!u~3&`ybsLqG{A?1bN6ka5Zd0AF>+%P5pU{dV|TZZq5qsbxQS#G1amQ+J=bZI%e45J~7dJ&I-FD$|$3-M?;;*c1yIuA&qFx8mRIfv1kfiT^m8l34wC_-8St5?K7v}<>9VWD}3rR+$e&>-c8uCy2Ur=oPox1vRGbQUHF1k>;xtrmz$HnWhbb1pSMa*Bi++4z$ZjWt`{04!aSVDCdh4d;Q(&c%1Z46fPMTHq)UG1^E_cLFwKh3w?9si=rp%QaKXsuG>ormT=CJw|9Yu0?MIaW#6gi<0C)RPKCRwFvfZ;CY?x2)t`Ai(w?65LG!4&gMtM(6_fkJ${#s!ead$2zV7giWEweJVnjTvwQ|t#VFe!6&_W718LInoRMrcFIj;RsA?2RS18e5wmD|or2rCc+xE1?t-d@Zp$%LG6BtN=`Q%Oq-UDwrY!EmREz0$oT+6A<*e_IimtKf)@3sy1s%*%4lG|FyY(S?97L@Q*4cS+q8OO&v_XaM7-W^inc2=TPwaL`&p+jjeo(0jQd5eF>hM?72;a>_O@buIqec0wR_hhSfDh!;sE%#NY-3g*v3{iKWJL!aB`9Swou%>uK@>hhvT<?Hl0u~J;KMFx8-{{Y17gB&X+nmi;d@@M?xm{>!@R{DgSY36gNj*0m2FX${I;GcOqn^PT&q-ui5-gZYo?|HBShu;`JZOQ)Q1SpEQ!<h_>Wfi?N_4ZgxqmRu>lWgugVA?>6QWPFjiOL!cu>tQmU1rfTa#tW@nY&auq>|w*KSt3ouKY&lx<!i%05>{zj5Lqx%9Blv2w{UIsJC^>D7&OH%s7S{so>H+ejdBMMj>PfKEy@Dw7GNDR67Sjp#fbn^I{`sH6^HdVD}xeJ5oAb$00aNw0%sgyeQYSBTK(^xUN978{CBqM~1tybMc7PD-UxMI8f~N4)iP9wo0#RFoXH7v<Pg0%_&R#e_d$9QPKR+o~kqMyE{(Z*KCB@K}kQEc*JKtA&oF^)IomV4Tn*o5_psKL6Y_4q!E3%H%!kIkv6_$_a$8H~E923;iUr!SuOCUsV;7HqS)+E#IXb#4b%1#x?%HS{T>(7gjX8#%~XOQz_0>>i%hQt}<mgN`ZQ*!VfK5cvA+#*h(yZBu+bxL`sFLZx6A0+_su5WF8FkFv}@UC2dbzCOuE10;617xEn_J>)&e8E=G7zq=r4h_MhfP+<RjX?yO$cjnQr$TMt%BU3>JruAZPfe=>FQxPnTbh_ipxCAmy{diCP}=oSn;O<!&kkQ`x+pj!i02*%nSqZcHBF;i~wJ~I@SH#9<pxNLy7?1bbZ2rpmgaz<87(D-L_Tv@9'),'Libraries/Compiler/lambdas.☾':strd('c%02zS#K0a5Ps)ZOh!WLCKJnRhZjpLg#bAe2na~>U|Flh9w#dn+nQaDB#LBjf^j(4XUrAbL4eE^2Ld+tL;n){7ew+ONL5#NPtWCD)(*-_?VY2#j<2h#t9s4EFXG(6!=JH20k1yafAGMeBZUHEu77$caJlzwdGKhlTw&Z}uFE<1h;Y}QJ)iD7@bRvFhYP#+?cMbyOp%<v*vqUr+>;Lv9E8hm#y)Uz4(C1F`uu)JTo#LkVqah3<T0E%EhfZEPb`RWaXZi4e{M{zfN*)gB=4tdAiZmw1D{gA1Nwdah0C4NfMaI!HeV6oC-AE$f&oXrl+WcKrY$xTyW4xb{Rj5o{SEO{oJX;<VkF<eEt*^pZ-bjDxP65%z^er@BmU^hYrESyFoGAFD)I)V6Bv8;?qfNQ4@jHd6G2!0#~n<JfXqjXm5axZ_7xpb6A#5?SNxXIMTjLY_3MWS1~4M<6ktDb?w2b*>GVoG0?jo!Z>!=RS%H)xwi<tDV6ci@K}YTs2l^aF3xv-?EJDmRCcLeew-twm{DD3uM#Zf{pWj=MQ_nL6^t4zMuQbq7q5E8M_q0kpTr{H=T9u*JQtN6>H&$yYO|7Iap%Z%MsdUot{zz~F-d6l-v04pGymTl6xXgu@?UuiEg1>Z<zr@{I#?nyW_YVfgi`BxZ?@E<peozVZu|mf9atHWw)yd}_=B{0zbR$@4T@3@HeMfkif!3_JBGI}e{+5e1etvCqa&2^6VPJ$y3`$l1cxxD_!0F1fbemA{KR4=6K`glkW2Dt38IqbFqm|<%beo#EChn5bXF=n&;a@A|Qm>C0kMk4=b3JM%b63ZQSL;vKm!Cg_@jQYi%;^p92;T+Z@H6U8S2BQ&f~b>ihQUu7B5sOv;<-f{u}`u!@8oOE%Cd#hfuz!w8BDdAy^1X{wRKwk?K-lF+oXMlEHZA=9$uz;1-j0pSj-N-dyuW%wYlHj(0|Z|&AAVL{Bp|D*!DuEC=FEnpvu}?)Y6hw@tuSy+i$l}SS)24F`c%*o>?6q17Cdw<Mk%}HQb1rb=z=8ruP~Wn|Nz{IjQg4xwM|YMV@`*-FmiVy|op#r0Uzb_tuCCojY|KY_JE0YdRv{pg-!IPYHarKCxP#fyA#fIgA%DUapPIQOK;;XIJajh(g8=j5q7cFNWp*Rui|xZDcwwW|+LcCeBc$SS=^3#A?u7eVE*jp+-EKQgz}AUx@ScsPvhNJnt~{6Oreg_&kX6{;-i=@R7?oBJPEY2^w0}vU0x*;UigY$7<VZxtp$VSLV)OfU#MB>`DYvL<A`!CK`wc(nPGtWa6<j2-`ED%3dyndtR0%?NpmfrYhA)b0}>wm}b2XD~So^e=iJahtkhtIH4J?q%)idQ+<6_x$B!KLlsw~@qLrvFX-x8s!Ks3*Ff>L-mXwUxG`Rf7B8znO0u$cqcl#?3IHc}du4mY<=fHGXx~FC31(a#+5@n8x+y_Y`NJa0#fc&^?#Q*0QbIZF%PYgg0|WZ8xTtt>guR2O2wh)Zexqk--8LeA9VO1C6O$P=Kx>A{)(&T)a!TA!I==1RG{Pb@byn06&b9jRk!(m8n}Kw314uFbP0NjZQk)g9<@Z>legRZV<a?{Nl00LL)i<Bnja53$u?Pt^U!Gb<uqxh#eHiYpo%Tj6Q$VvVTQo21guJj*=Y`7{7m-5`gl0}bG^xJl)%Vnfd!!_}qDXJXSlr5Bd7EV&GBmL(6Q!q|jZP8hDByjE!bs*Q^*;1U0FG6`>rTs~Bdn1o>#n-E>e{Up<`wA@PfV<(oaO+2Dc!ePeY4g%t2%=jo2;rpJC!MtU2?kP?LD}~U4NwJkrJumY1sFFWF1WO2SY4nQ)JeGkUA3>n>D3-4YJBpbL@njk?*PK!xjB<aKQJZfl?gmREX=4S;m-Tk=$=*#Dk1d=3%^)N!^F-n3GbFL(1|gS<ZWTM@GS@3YLrN`xpIf#5X}o#l&SXmtxvwEDo9|B;slsH)}g)&K{qoLN_ah-$Fu7JQJggIyyt+eNu$%E~jG72TRN;qB_i_%|NRsV^?bAm}<o0CjCR|5q5kVNt<s<8ra!LTBH%&KxEj-feEIZ3gy$r2Ld;gmS`at#09ZLN#Aalq%t;S1WFErPl?H5WgU1?Ztcx?BYR4`4|{kFL6poBvXxvAms7GMkhUcIfssA8p=`!%`C-D=2e}$^`>h7Wq9OFLf|m<GwS4piEwM^tsFuE(&s->NUiwLbrFVxCNRUzG7H3MyM;{KzoT^U+BIPF4P@XK4<<<zbGGy0olGfwd1ZRj~d`uC5^d4ED?NH?;?LG9fh)EfVTFs-y$uKkOn_y>%UNrdByZLOFNq3kXRBF`3T`_M84V0m>F({ZpGOtJ;$`hfaZ~fO1uG3dTIcQC~6ce0TGBUk0!<BY_b;wOFDM6xEQ93@E7iHdLUfhH=QF)s%$X@5x6(;`$t(}c`ju!PcihJ5kThd=^ITvnl?-qAY2V#Uv+_~`Q(iO3yyv$P`_J52KNG7Q<k~q0k^$;nX%#XSRm*S{0S9SQQ02+(}R@TXL$H>mvUxhN9xw>EnEn_7-8EOcTW#PNRP~bxf#q_VMcg3-*!7rEZvQfMrHj3d->#|!E^watn7<BskA5NV-QLW%V7pTLPcF&xvLqDn5Pl?~fln07j7k|;#yaM>ibM~u`)|Vd5!B~KC6UHqVcVH~SxCi3_j6Y%gg@C>9SlT#TeWEI+gI+p5R4(<FQekfqS_NSgpA_jXd8;}sP%YNBe*v;2o*M'),'Libraries/Compiler/rewriters.☾':strd('c%0QdS#K0qy6^montnQED#&f_Y^~{;5aXLclVAiycSe>~Dz^*MO1ryN-6qY;2*|<`AORaN!2}57gv6PIER&GQf|T<<^AoP*A25oPKXAYAY<0G(?q+$oD3xwko%5Y<-_EHf^fh|!z@a~qIL2@LUOX^+@NgUxQfVd23yVpw5=Kj{&O*}akuV~aN*IO_AG>Go-sfMKeQwVShvMlMX7=odSq#{pW{5T?jM&ZD1Mqc@kY|Ew5Qg(RNH@v)aii1j*Xo2X70^5MJNj`%-=Lc{d2di7FFpU~c>3VXp2IT)(0UFKBJ?)>m|m{c=jIWo3AnYt(@rCJynW^#4k#Rlz~Me$NsvS6t8jZu{27L15C)wrpr`0N^gF_C?O05Y1X;Sc(nw?a7QK&@UZI!icVTTu0RNgtaQGU104M_RtMoe{OAVTvoDX-U;jUR=!Q?!w^Y2rz5}%3xvb4XFwF5bv-Dm$pSeNMgK!65nK4j010E+FP+0Iw#wVI8TR2eVAc?~{bNAO=e+|>{2^?+0cuzrxV7h#3F^c?*sJi-T6c~?s06#ay*){rRnP0jCgrxgV83^1Fk0-b=)8X)vN8>pdeJVY+Hku5qKG>U;;gMQjxWP@zNj0vbh&Gt$fsJlBHSV_0bV1+toh2AScM)D4+G%8{KrvMW5(tgtKXG+JX#1Qye&A(2HnR{nmAiF`_yXSZKBrNplm8{uMW00h+Pr2@dyN>j;E+W-g?#A0^PM}^(@rW@sZ8V@s8uhssXZP}(AJXq5AYq-Jtb?4^>GcpPTBX<N5A5?j@wutXDpKF8+V?3?UG>NAd1fOx^)jcKBLE_e4reQAs1Wb<m-|l_afU>s6QJRy-LK~NKNPdyN1w5=D*QlB=@8<$0GG0EywG~N=SUA`UZmG^&o-#Jl;gjgdSO=pO|vWAeTV_bOhnclqK^VF@zFF{)J8fMZJTs1rZ8+CA!NXBi#utnmlEC7)oKIgGEGFdWuxCjc06k<GeEgPKN70Z+dgrYlg*tt=P%Af7RNSkHEVK|=ZQrMxPy9VF^x&}OPKNF!|ey_Ki+{+6M~6h$U%O<U@_^laYz*lE81O{%WqGZ_Yol8{sW6bkA~TQPMrJk&VO!S7>XJU^x-CPn0O2vKx0PW4cDte1SAve(5%V4A=Hc8;&RfBd)>6rOj=~1EVizKxUkH_)mojom{Z`@uSy5Q0t*pZyh+yqk)Li}`vk5};raruZ{d3Q)6MmhaJ>qI%>6q0O;nwVs*_Q5cl6t+TAi2bP7Y6j<<paN1ANx5<>ckGpC#=c(s%)AG}gHFF<gI#3)Z>?Yu&mJ*Jp5j4i~I@>r1%)q2U70ufg+cpCew#(8^?WYWIKr@>jq9&2N*125_R18=j0h%+U#l_knVogy$-6(|e@M>EgdiP+?AC!2JNwwodPcx@S~QqX~8igstaZ!@s=vTpI-i&PxKqn;S6CEC%1CUtzw;2UmXuxDLQ6A+uXaKLt62Hjc;{Blh<Cnd`pcX52sCO?$Pva#iVaw|^XmgS%qSf4=|zru^Pq?#i#dl?Cy&oqz53j`y^$@zP4ar%f>a23Y#v2&HP@n9^^gy++baD@y&$z@mb1#>^vb98EG`B-ZVR>{RyylYbnX;?K~4-mkNzS$MUx0xuc`x;jBv=6Icc!<FxI+xsw$I7zp1<?*;EE$Bfuei$`L4}-tpVKCzs6pAMie0)T2>p_k^w&)p*l-{VShj`Izclv>aqnTuD(ORGx<vGT1-VMUgqGL3vj7x`3fsNu&V?RY7&`(g9*Xd~!^yM0ACi@ofIxUO_eu_*hZ?7ybq#i@}SxP%y!tsU5`Htnm?!p`rVri*orFV;H{Df|W80S8%=$6GN-zj&*FC93vZ|}_B+5g#p=r8;C9-Mt~29RzwyQaO`4o}k6?eqj)e69Qm=Z=W#!1o*UhFp6xw1>s%p!*2C(QAtl`SdaJY5V-E=5)!c!lfqkd_OEuh<=*2lkB*o5Y1jZ=w@-!?<{M5i9Ba_681r*IL#Gh^2lkerzXw233-8uOaLkgeT&{Q?(1c;td+HL6pDM`h}jgFeLkK&AQv$!bnXtf|9%q-60C-Jqd*Lunzt)=UlYSB$0d1yI3vv_ASdkhV-SY(@4$S3ju4$L2tHQsUNkZ=5=dUaW2apqnX$ntDi${+*LY_KYs+VXDjz6es7EFT#R8AOLOr3A4u0J-ggfZ)aS5wy0{J-bRcnF#f7I80tzM$CVSoXYWuPD`uDVY}NnI7KavEa~fm0(A2u|-C`iAa;*fL>gkKlQNV~>GQO!oon?8!Vr-q!mCKizz1L#rD&BSh<wArYAqaW16$u1nx;f-;xRbaacjO_-~9DsHwurskutKn!j&NCcr=Cqh9SrgkUj>Ch-7m$J@EH|{6dQrdSjhQ&_5HYBxFJiT@XuCq>`w8~j;^hqnbDjLBAVr;=G)*>tz=kuiUiV7DhU&(-}kgz)ZpsUN%wjz5qluP+j)Ca8sR}LasT<k$UX7rq=P1|DzEL3LNRLW^x8J8PLtKu|<84d?kFL#2^F?+$NeL?9o)uiC^jkBY;!7(vy0Ww?C(?Dq}O)?U?{sM`DqPNF94>NJApPjEgu%@&By>hhKN(FCq*Ln;Y&F}8&cDmSCHa+1nP0`+d=r}q=TC964pP9CtxtC6t&1H6VTiDkX@wqBKZvh|+Hkb$8EC;u0RVZ3V!qIkrMI#$a*l}>p?$X`7^&mS?#Ac?AI2h7U#HGL4%2Q4oss_|iMP?$$d`iHcFy$F@Z{pz7*_PlgFm0vFY1`ui`R*C(jckJNmer*!A3W7LA#+1CNl0qGNT#QqCbV~?Zq{P_93LVY(z>fObDz-)cwF!bef`O8N>;4$n7b!XyH=CcWD|njymr?*sYAj8OITUG7v^o&A#+6U?$YV)6K73MB7~j(mTY7M1Z(3|OCw85TSpp(fA$rd4xhAQnk|}V5-Lc+v@4h;pwWIGQ8%OIA<C}tL_qRql6lvAotM@KTB|{gAT?wmuP4_tpACuogh|{8u+d4B!d|ucViZq9pz}PWoI||0U~8Qgc7H}z_=<Doi?bH`XKXTj5|;@gL;mjsEFUy<U;9|nYAy!Cl?B+e432bGAn5>I=Q<XEj{Tw%YK4)jjk%hQx`X)!y`+>}WW2gY82cDjr515DwKp3fNW_ihZrtf&54YKN{c@JJjuj=R1xAlaJf2(lD&N@yw*Bi{<vkfnh;KeX9%b<PUtUfdQ=e3K1Qn0<M`eYH<Z6w-VC+(_mn^5F@(T(5f?kkZuxe{0UJl^JkToC_oJL+5e1&`O($}Z=9M%MYgoTp7qQv4;%}UN>J?}($I4@P2ClI=`R(XVht#<Tb+@3pfRQ1j0c;npLRh+l?@?3^tX4CAa%a4}X6ls8-_7rKPZ?E3n)&N@+TjiD_^31cmAq|sl9rqXrTVgB&k?JC!2EVHZyZwgYA&FaWSySW=xbANZ!TGj=%W7ef#dO>{^w>yssDV#M(^Xc=6HP4uq_Ij4ZVJFnY2dH|28S(@RMnbhpO=B1u#U*^BdndoS2pM>$?t?LTl1RAaKQ9!dLEJ{K0pCi1x$#w*1S^93D&@Pvk<OG62&lICuQh48$Z;0&PIo`Xpv$?jrw%yWCeSZ8F;}loyP-ltzzy8YmFZau)U)l+}LVnjg_Wb`4}b&7U~Zjw(_&g&^asTwGBQ<b~v?Tbw<Z1<ca#vU;lFxuFE0~AG>R-?~~|<yqJ9^u6-_yY@bGss1YD2M#M`~(UJxqH;Y8b_8b{5>}Uwc1+VE1fxK#UOFiZOBN0@J=I9g~1dT&c@s@)TM2%RM^p-rysGCE>u)>YQts<YZn6^8MDI~qtfa0Cfb+&DIcFovdHR?mXDlO_)NE<%VN`~xl8|hcXDvxlCd8)L~W`|@k0me#<M=0CXF%{%8YhL5&5cP+w)ESmqZlXj56##B%s7^#Q!9&ND8hxE!2Dm@pzjp>WnwA`%+E>q~X?>RW=#4VK|NHf$fJObwGpLBwn6I&Lca^7^7wHC5m5X$}Znb5d3RdUe0NKVx;xs|L_TAMT-4H~~KgVbbs0dMBVIShnPhsA=e`g+C%9+<FH^%8pu%7COi|g!oj1@h7>83clH}sqj|HQVuEQO@MSc7tFEn)}CKC823AHcG?CXKkYv-Y5(?E|}>z&KlP6mMmT0E5a+Rk^ndh^}&PS6DJv7-!Do-tU{R>?wr5O5f7AW|avZuXV|BTUGJw96!MaB|}s8S_i>1fn8IGm})4tJ7gSLGrG&Qiw}zY)+W?T)R3a<%HK4>jc-Eo2coRzJE&}y*fzz7s4$j|@`vV4AxO?54q70f-fzJQhpp6M?}1oPk*Ve~!Ok3_s@_Lpq3qdSh3legGMq)~bqaU$u7KfS&lSW<Ukk(z&RpMMM$kaaR9N_^8jj?5=o4-1CB0sAN%r^5-ri^_e97A`c5?2d<&b*({PlygaGite&F!;S;Nv1(=i$0AcCwC~yiu!r`=W$7hEw{P2pH^?3%)iGnbV?!p8fM37!KG=khZas&(dEQndcQgL*}&S=md)R%kgRn8y{e*R#LHr%tXxezkGl&Ti>QM8({ikPsFpm?N+{>tVLc9DdJ?7?JE~9T@dX@Tb>1e2~<V?Qe-S%`xt7lTE|vPU&R>S+ff*>H$klSu<fIyQck~g&@#qIp8J#*+30kSW0O7amP%f*fng*bpdyD+2ma&QMaU~z()DVit)*q!=&AE^z${pM+h@rBuWI$KSWYbaS}lJ)K{wK7FV4~<F`Knjs{>aG*;2IqEo321%dQ5pLyauTt@8$J<ukARt#$Ngjeg`FfaIGr|ERgeohT2S;?BDla$BDH=itQlf&vLB?Td<4fr^bVaZ}$$zGs~jc#kNOt$4~w-13q57Cq@9kd-O^+EtN*$B#~8%=~L$(-U|xxJcg>rovMkzRPVkbT!APdtoc4_@e#>9wFhK0HJ|kKHV&|U&3O}1BxB|yed8~R>I+XU48v5P~YCgY8WSl3UV_$nN|6UICtT#@|oyDL1bj697Q>k#YY**T)wf`B);$z!7#^RIxty~w{eKyfVfZ6hYDTM=C#y<hey!>wmr9pm|`V(G-5W0EG9V8EPikWSG>mCJiT*eC{!C$Ozr#(qA+w^nY;_1eH04)j<7**rJy{qb^@<pq3B0?*jGXcwx1~P$~mw-B6ui-xgns*v;GFA?<#JV#Tvvsn`*JRft$9N46*c*$9|y5ONNlwu4cQJW_>al`NUClcur0(kz}!0McE->JZ<qKZ-R-y_6U)yw=mG>dP;=luWhtkS*lW=AUhJ?>FC`>mN@Z{F$Jjm{5>C2SP=^6{*Yy5mY!~UOxCCRp8X-rY6N6`lSDRsSC-O&)AMC-1ttC7kh7~Iha=>u=;vUNx}nMR0=PtN_>e6|t*&M?Ju90idFp$;=v-PM&`9pQS!nm`+QNk~jT{y4o~U>7w1lFtGhEQpU0E8$kj_D5#&4a>t#6F}68@7}3r^Tx|H1#lu3Ap+((wc&a<l8={EEnTL75?#==_eM!!1D_eKvjqV&3e<7r!TtbbxZDZNY?vENP7O#<;36q>5_2Dv({<Eez7JD%AW}G=2|6TY(s$<4<p>(nThGLa?|`+YY_Q#I$-HvdATn6TYJNvMe-t*2vC`A;xk9)?~*kzFi)E#-5S9;F8=JeFHudZt^@CrXZE)4pi`mU-I7`QNpaS?p#q33#4s)aSw&O5DryCfB%;mNnQh?F)Jo5caZV<o6L=<?K;6sI}}!`oR)nSBvvDEYx~RxY!`dZ(<oKo=RL<A4V(9#Wu@Mex9S8gspMx`&GVGj*_Cc58?rUd5os>t$j5!32;AjT&(&1`?!13PjwP8nbc(-~Gvj$HXZNUYlW{U)q3~t=i(~qO`~f8(8zyQyv6mr^4prlw0V6js0<!3UDfGlHA(D)T$^_4l_B`)UKe+@WW~2|!AuwTx5H;qhxgi^-th+8vPK(Uq4Z3H|W89l`jpS125Y&mDYW{Ty>t)8KZF}Dq%>J7g^r4W?^D~EI{MD)$0^<HXFV3K(m`8ln(`JzqMgs=X6A;0Or$S8_KB6a|2GNI}G|@cE;5z4=6fjCiQN{`*Dn20PJJqlE8Tla^r8=XSqWk+~74vAs?a;E%;b$(*hMN4Hl>BEd<cn?Q59QdeJd5)QtPiIWqk^TU3XXdQ*2=>)!L~^C6Fr(Jy(dR_aL(U~m%RX}9q#{-9~vn*^^p!l5Ewrk2^q#Se@2&j$Pyp(r=`d3gz`BoU;?qY5$eZLMJ1Idr#t=+#*R}k'),'Libraries/Compiler/to_ast.☾':strd('c$~dj-EQ2*6~6aVFuWSNj37C80v4$(scul&GAtPgpb7-Vr6j_;T$be8D+C23OIB>FcJyP(iesmi4W<5z>l8s^w{dbYKyUjD-6t^67sxp?LvqL+?yhB{f>z`XXU;iue!nvmp=<Q|*{R<X%fh=)PM@7TH*Hyj=%ITl^kO%Rbi-VzHRkMEL=2PYx?vb5pFJ`*c4}hs<jBO7H99dqat78ha(@^n(i+2LgOg|Bc7~7-wIR(gW{;6l&I_SkAE?@~t>Ubvg-eDj_}2;pa(Z$Mso$cH>6%Fo=ssPkoH{ph+932Y{fa&T9&hg5-fS;ldvkB^2OX(q<NIqLvj?}Ie9Rdh&|SK1{tl#Y4TH0?oJL*ZhgT%AMfZq7PFLXe3B3>0a2k^TBtPW(ar^3{|Exw%=mmJo7)^)Gi~&3f`e1<53JkiEt=pd82U(m}AS=_Vy7OAxu<R%%pq)MXcltBC{v@t1#PvJ#k{$Y1wAcva3a&Nd(5qWD*I$SiEzh5C@X`53=(yH=vsMEEV`s6#lx<e$7OcPyBR8xJvM)gBlEs9NL)R6vjvohJU(iR!@G%X3dPp=}A-~Zw8}^bvbnA_aF0iwsMK`JlCm5KIL3^n!!A;TQNX@R#Rc#Ga_MGkv!{w0PBB`76;hDi%;lnUQ^jJ5tuQ1~!eNN~KIP5=)<d{#d(5Liu;?cNl^!zzOhD^i!?9XV(J-UgP*K`%a<&Ukw5wx1%Y>KGZr8nrUga*+yoC1?1`37RNb>zl&9EWK{pAdq=?ND|*DC8d-pCBJWOnx+LazaQHVpG^e?2x;5b1rHIy)>Uj0Wct9@^B?%%M?k#@awtJp;<|wAp-|e5g?4|Ps01r!v$4yZ2aW;Q<coyO03T4c=KAPCvwljAE0=He#bTe*OVz(V>+~*3!cBA@#uuC$_cVRak!*qM1V&YH`y@$uyJpmKT63P=^U8`DTbA1`&G@0ii?dri_ndmp|723_--dz)VG2yCIq@p53>!!#Fffmfiw!0tsZcVf$98&oU`O+N--12F@qkkVrD@G-{gm>V`v|0EIytR`W&1+FGYa<&eqDll=;yK@S_v6?+_EYO}e#$9%9Y&HKPCT#oe#r^A&vV=tZj>RWnQ>?@jQ?)!vuEn6g<)TBloSN<(QSC%Ozb&v3>eOH%J=8!B%{#tLtjT{`o2X`f-8C{lltOv_Ab7=|3E-4Y5Dqco|ExjdVA^PXGP4MiSEGbfb2WT9rf+g{ecN0fvJsj!#Og_Kjbf=1-UUc-+hOEM{PyDmb3{GO|BEuSl9z>hFH;}YGNH4D!?KWN6{nL-VAwQ9}P8qS4CVNZc{LGCbCJtyKP<0$I?n|qr-Lh(;EmXsK2CU`7yD(aHX%GwUS%PhM?|0b^c;(DJbYW`(FwJ-C<8vG!NL#fikunLf*hD4d-O1g@}UtEX9)0-!<$tx9&@6)<)(eiCXvj*k?(o^{32@dE=G0Z4txWO=_>Xe|)MCl;46$6F<#V3ZtA<wS@6f4YaUw>d#U8g%hOJ#Gijv`aizqgSBA_Kb~>8Y+d<+`-!MHhIx6!1W>V=EcV&6S#stqst`53JwV+GwwD;ji>%C;hS`KiNs1+*^i$n<!O>52k4Ean5`8>6Zq#+*7bnqGU5ucd4YSoc-siAaJ+y_N=eaZBFlVP}EyVfSbMbGTry?WhL`M?12fTLMs_KV<Q^Ij^I={EedTg7)9tqdY%3=nSv9Bl1I7d<V&Gb2(0$iWf5<0Ypt8~d!BB7>8`Ynl!kn|r98h`p9A+)%=oRG?n+fu&`={t^@H^$$ts#5O2>~cuft~pK7WDFjrO<q+uuHDuWz>3x7*LIw7))RA6^qGLi}0S6rxNk6DwaZG6<MzN3;#E6m0{J9~2u0Hoi}nbK@sU8Vb3<-lTV6jhqJWi|a$VYB-Hx35o#^zX$0IE)000BiB+<C7B-Cgfb<TKt<finvm)-kuVw)m-%K6q%kJ{${{rv{8=|NW=L#Ii>Mh2kEOp8E-UOeDYjfjRLFoG1g>8tCGqi`J~PBt%|wm7-jr!AU%wJAo)2wbOa{$TK2JOO80DxE4JRacrK!xLWS#~(w8y%^8NC8ap|Sd52Cmzanb2n^D_Go{Rf3ioJq6fQfh5kMGf$I}fGI>rH;WK`K+h$?<Tlv}bA?PMIU~0^GPyLVkk0c|rE>6)xj#oQU3QazqNmw#mcom**pQ(`&5nD4awbb$4|v{8)sCsy1W44Vx>h47V3ii0tcHzdV8wR0;Kor&`2ZB7C=Cl?0ARW+lm<kmdW`#tT^}CXF`k^2qU{bZYN>pPHw11gkfcm?SJuv`s@AC9S-Y_!46sw=UHY0&Y;P`)j!dJX#pIM0o6N{%iIzV&!Ozo#t0jlmxtW<KWwUs-(Hfz~w}W?u2jW;tEsHF;N~Gj@56RA)pO`qhWU@ah4cJ*6nOtAeSACy?_K1!Tl314xLiw3?q01=3`A_?3?65y*>78qtLqT^^Z91++zo0J);f39(1Awp*Sk9vD`Q0KZc0=C|my|Pj2)i}6ES3@?cC^ry2?(Q%#3Mn#ESM%wS>RGK98TR%1k}b_86sAwTHs$thV;%%RP!8{3^BmSa6NQim7dtX-xQFOn$I=MM3#U$?{2cnQ4~@>fr<Xqw4+7Gj)yC%Dk+sEEN6vkm6R%8gVyO*4sfP2w#=pBd|_qRZJ?Cah`uZDGpxKxE;L)H3!pFJy|}M>v-bbk*RBwIM_m7!T#vlJjVs+Y*LRKTI17TJ6<bcj?^)OZw@Tgb<}XRty?hO-EBuAtt>B5R%muml$6Nf>PNuoeWQ9_vE~rdo{hTGWukP!LEXu`5J)r|;6pl$s;J^{mQ14#-9oq1%)t+Y;Wpb*;G}KBaIW=S6OHZnJLSapEa;9Mjz{@A)bD4CoB{={0_FW0QrbllD`>|O^I9z%xqU;;=fxQFWkd-8z<t;^)W7leZ1<p*5Ku=m-=vt@FpFDeRa&$!I3(1^=?QaT4mWQ}<lRhf+2^m7lPK$CCoV`Y~94~a5p0fHn%`jYo#M7<vHW%DhuhN?wHs8JqpKA=(M>aHKcC3K*ED$@iY2r)rExMu7YPM;tSY;>GX$?<$st!k9RmYp6pXxXs!-GAQH<lOByh+@a;|4K*QF2GKBYdCpu%EZG<6#JR6|(U~Xu<LAY~0XBrlvoT-=&1M7rBgL_QE!4gaxHz$I^d@vBp2ee`J}mEF%B!3jcQr-Q-uG{wpM;l9m'),'Libraries/Compiler/ast_to_py.☾':strd('c%0Q6Yi|@s^1FY<WF$vDW^n8!xhN}^J7Rnf#R(R0=p>&rTJMfw<@N4lXB^v?5Sf>;NeI~34k0E$9Kss{c>#eSxuyGhzajp3A99iM2d=7L)AQJ!HQbk5$-6y0-Sz6K>Z<DYXrn%EOw=l+df6=(gQ8Ix_v($nsQ6B;-WV@dEB|oI9iupE%$=UBH_CFv*krZh2OWeSqbCRV{+T!qw*K<w;O;&99ET9I;Z8Oxf!pv+%RW%8j})suv20?RmSx#|^v+$o{xq=r^_>HIoxXwooo~TB2JVf1qRp{v*13BSnnQ$aHF^!p8V1al=|}WTzCe%A1-e2k>^MblI=<(Yu=8_zyl>||0<F*J4IpS^_3XyX{JzG7yK(s9#_A{V@JB$vo>nfy(_8hLYa%)U(6arY?2Jv8Q=!e?fGG_(m}t}x!kr`VI9+k8WqA7S>)CJNvFujy)$Ai^m+G~kQscN!T!D^}hFctqq8q7>Ii+f?8OrsiFs(9*5FVU^rdwqX>z7%ZGcq>=52N)45^-+^N0q8Y-%sL+;&^lSE`i4eDW0Q;3&0_Oo0*51fclr2lh6(t(@{WmPlG||89GOoVDtwcbauY|_KPpR|Nf30+qZAovVM2#)~y>K9`B+*yad`XlpD5;Ek-EHho=GfOD`e9kB&mKs|%a+D5V_**8CEh+j$eYE%4?gXuiOjbJw8BxZaq%3e94z9PM7e1+7{=V7+rFN49En^Ss;OkMqazjnA4VSkr))Ok)+(meoP}-|EYQgy;-C4E;wzKabN{dIH#=rzh!$pqHoU$MiG^WPvWyvvi3r(-jcwr}RAVyh<;C%r4SPAnGsZ8vT-9p<mIf^cuZRZ_u0c7QIdH(7W_&dXL_x-_URAcl3MufIg&;=#TU<eL|m_NX4GMUHL-aU-#@Gq*@#wDHl<scj#H0{Ve9;XN7)8BAvhqDUOtOzTVfH+Xjn3OvmIr?H%mThW1So8pwjdp+5;gZmpCrph89AAb<z-4gry!qxTapkAYCWr?-e`+!lyH@M|E_M~KF<`wI928Yy2Yw1BtlK0DsqBqTsEn1a@lqdu3TLi|X<VE_JB6fh$@2FkERuSzomVKK*bf<BZmVOcHq#ewecAKWa^l+kS1VNk9oauBSyrI<wkU(f}Vp)F@l<-s%`-0AdxZ(5yX$`)+Ks6{aBi&N`OJFZ`H{Gh=cGblFUgxZ3Flr<pW1O7hI)ALH-M5m9q1W#-|lt1eI9rqc++q`Up-96OSL}`o#lvYNGcm&Hf-s?gPQ$0K3?=_AIzjLp$?;L)=`a1jG1&eveve26<aDp?S<19S}W-rB4VBD<P(*^Rf(FGP@z+_F^o`U*RD>c_AQ+x{p<02$yTlRa0Y+!5}jpzwIiblk!<MvZ_M-6w%0}tjD{lM|2k-=qfBady+uLAs8`3?g<l~IGJcUHG+b?@UZ@WVGIL%wGHX|n>OPyo_@z3|B#{GqoGVc^hlSVmNiPjSV?tf8J^TeZQLYg6z;0<N#zW6Jd#8n$qYJ_Ek-Gcs<cs3;-5Y~7^by92d$8}pAg=70S8yVZZMUeZ<wq}go7&r8=L1A9^iBHQOzQR;lXk<Taez7>9=d=+8wNdVk)_2LeKJ);nN6|Ny*`3$`VR1n-QyMzU>p|*Nwv*iw-EqG>-b-+p!&(p^wjV74BK)=ctns_(V*_&K-uWQ_EXbVW9d?k1j6i5T$Gzb{xZ}--&OP5E8VE1GCEs^511=g;jV5pej0xUUTniJ<n1d~cXZQ0WsHkoeC(gmqmN)>xS#RB-YnW3d`Vo2ID{fYga6~7nduMoo`NXXW#-}c=ABH3{joaO{E(CiJHJt9)w)jvSCL8!WIIKdpF6SXLV4z)VKtI5Gi7VR#+<jlv3rc_@g22HLlEFVlj#bCc)SipeipNkG`0ghK}6vr`W)J$8O3i2SOLPE`j+g^q+M(r{}q#ttgOLII6Ct$V#?#@tpCkF|$QtAUn#FQ?CQp&O?Mm`40N!}Uq*<UZ5`61!;(&&s0!w<ySMhQTL!=vv7I0zwu^^yi_=>e0i%n1^ca4-rvDB$SjBVbfq-Yu2aELTbptlC{A$#_HwB8?WS$+yFZ=W0*lY6opDcDd$9&CRLSrs!zB@^U$!woAg$GmtRcmK0X9NYFRjbaK=Xzgj7|q}RqI)@rfMv_aW#KRo;-TR5#%k^Tg(8g)@k%|N<wDpMM5;C!QhGdO|KbN>URy9YOe6xRLY)<_c(M5-QG-Lahk-VRGQ8+D|(C2(KL{cPlgqzgiJRF&ii3<@;j*O)>vmz*t~18z_Z5O733R%;3E%@$EMW<M2kCf?^(LJ=!$7Vla+c+U$wSH$lcDu^W`uIqY$u33D(5L1*)Q=E%i#brqS@8=6T{OEp3#F(^%LTD5uZ)^w<U|4Mb<pn&eyY8t$j2ad}L14wIa~2Yep^gj<g=%wH7$VECJFF6FAuJ!3laaIz9xH(skCv=N4&z~zmJCR?8`~7ACMXx<gJ(L+BCcanfMjepgn*1Z1EPeGeZjlAes}%W2WCn@-&T|r$>cqY3~9?7uDrowdnI;e$Rex=Wj_=Su)0|ev`n82;}&v+&d?M3-eHKXC%Wh4#GaGB19L_5T_c~(Cs1L>*-hDY+urM9WVBRz?*25T_iL$T7ecUH80J!#b{ooTs`OIAbo_}CGnTk1U1m$kGGdj>U<rFA7UKFfo}!(m7nu!;Y=c=j_FjtgqC(rDnqx;>fflcY2%$Ht(?|xn79~{?sj;*o5Yu~Jhv8H$L2_^m&~<{>A~{wz=@jybB<LtsW!RF&PL`6uIKLK4PPI}^$YU%t&E+i4oxZ<zhH3^`3X^6#DLS$lPiix~DoA6b-H?;lsHWPlhUMbbuv<C>(yCc$EIT||V@D_%w5BC{K+ie)sikTK%FAdcGgddm1Zl+C=>)eQR<We2E%A2gdJx|@MGU2PMYK_m%G1WiA|(|l>0V7$^kS;jh8pp7uuVSyPZ^CBCf4u}$8)NcfLACa#^+E^q$TOS(%gMmMTXWgJxch&r>zL&XNdgtP@FHS^4MVi{!}{*%fY>>9L$Tswmgt&Tk+p{x7c_-Th(1;r!V(`&gRr_$}BI;Was;_WH#=BGm1DDX54o`@?(>r8Ow`pVH(noSEI=lSP3(k=JAFeaTHq8$D`?!UtmowV~L`>(jS^;ed3%zl%REURLc|Jm%_<-v>?j8S~d`Y)SHAP3%^1ywZXaA<XqZh;SQ|WUYgIYL-@gX;B3szWMs=xgN;dY@?fRvl2Bs2%nd2Xiw0wCG2ytds3%Uj`A{wXt<;EcU-ETM&&c!A-74v8IJdRHDOOd2Vxurh62(JPL%1!1P*xBHRl`<9Ct8cQR3G;?FWy*XLLM7vL}d#wRd~-TI~Zm*5zn(oC2$+Hwu_U|>Wt2*CCN%H-7pp+uOp&pqkxI4(l(i53DXlQ<~&-IGV{%O%qEkULN;IIj3dqR6zHIzyK=*Upb{qYo>_V&A~DEZL`)?he1*r9E0>u_44L#`i!>bvFrskP<tCZOh;!E_*_b$Fy}?r!mKH=$?u@N?d_tPw=XDZBfI9q(r&IE<Ka!7faWu(}V<~W6#zO7Hw!h4rT)+IwrBl(B)aA~V)#@&Ko?9!Eh`vNiQi;;d4v<C0@lAZAPoCze)Lqt_pjir!CgaI@Nzcr~tUL!<Iqa2!8Ib3}L|zX{*ca*4Nt5(7PxKS?YD9wPH?8n7^b_t>$@KyeA@ph5h@QBQl{oq|C6RFfgm;TEpJ5bz1txl2-p3ar2I4=5Z={9?wy5Gh-^pvsI+U*2Nxc#x>Gbm+yG190V#%|eIBCtuX2gX;y#5#7^%GCfYLe9?3wJ|0hT%=-)G4OLn6K1)w-JDjMGAfyK?JbijZQT`K^3Xu3p}7J3obXc2vOtC3>p2*3;-)V5s#)4q*HWBE5${Evn)x#5+)D}SD`LcMep@Y;e{S%B?5=B#So#Nh_nZj^}cf3#XfNbD7h03Mh^;_miweDA8mM~rLSjI11t4Tj~r6+WW7+-0K+XyT}n}Mu*-~pmRXBa0NjfBl`1y=WYdGs_LkBfjGkP}tSY=M(M)>jvWi{U;&)Ei>PBn1phN6}7uc)Qa1T`KH8Nm(;e{>+{d?$x#ww)enmP^S3;Z_OfTfX%y6C|&q7HhvsU)s|4Gj$8fMFph4?{Q)T%<KToZvQXtdMIL84$f3-xl!VHp2)igwt|r8rz~I3dZhu(Ua`%eN*up-cefu@tosgyPXyH(8%?}TqIJ`#LDn+tL-4TE~TnltT}FYflpN%>SG0VXKbJMufw1Phw|Erq3+Y85bxY<sotm?Zpy7UCOjf2T%uPsn`r?L<qNw;eN4tp?5s*z0_Ue#E<0Y`PvNIh=*frPC*;M|V*pQ&0Z7G8R>R_#3&SjmZ7W*+%H%W5eC3eMZ)WjY7OR-u(y49cC3tY4groK<P_v4Z!L!B!%t>;Y`IDfCsY1(#-sKA3VUOHZ;;Wmye=90T?-3IfC)5Vd24&Ja_8qdD>PFN<xbh$b7l@yd>hD<C#3t%BI9un<5_d?kFQ`ZEkFq1SyEa-$&~V)Xcd)fO*i5ZB?mF)l8@}jlxE?%+A;Ml2AlQQN)ao%IO)jc-sq!&+VHW>Ik)&K}gdL(G9Gi|u|1XGG!OqsK+OkJ0)v6<3IS1=i*LOyWex)RVdeab%r^Q3;brbMPsI3M`-Ifkn%D2tixOko@#BC(qH;}Cj=l^>HNZDi1m^Km<P|>aKi5de)_!DmfC>g`>u$CRmoX23Do~COdB;fNZONsmHWjBwTBR`44{b#Z^F^-Vza-sLtS8Tr!a|NRZ%seq)>wU$vz!@B;4_My$SQWTg(5z#6NM{MxIb!xV8jzD!kn7-Jy(Yv`sU3L1;1nR8a(+jL`Y$4<|8MwzM|&NI=>KY@Ou)2N6Z>IfHrehB?fw0OrVU>J^uPZru6q'),'Libraries/Compiler/main.☾':strd('c$~Fb>yF#T75=|ZL9;M0V{orV8bGjI?9KJUmlbx`hJnq3;EE%OFhvR^Wov8rhm$xh(iU-jNu3~0;Tl03v~_E=4T98me(+8F1bKv>GczP-NNO$bWnowpXXebAbN$X4k@VyA)7IvBV%zw%cB!?#v1QwYm~E%sV<xq_ez@!SF`*VQO-iZ7SFE=PrQ3u|8}kOGJ5!_`y3Fo)KC^M57jzrVt!T*T6xq7eYBc-TU6TF_pI6p4tn|b5>-6sO;ua~MY_Zz5(tGLS^xxEqdk$;|1bWPIS!B1vexsS*fx#cs*YNp8`fEabr@!ku29SB4KCt-5{RU9@UHX#XhH`+IC*zqnk6)Ygq<D4T0@5=Pi$nhggGZd(55vHAy$EJ64Lv{cg4h)2eUg5ceoX{pV`k3o7E1)%11IVE-mdNS2Vs;nn#AlxVc(Fi4e{D&!B@kHjg#>Q!@0S+#f-Gkgjcyx=*+;0Sdbw9t<|fbo}ZrF`xd#=zu~?~Xb<*ayG%4s)6dg?TBqRi59x2MQ{v%KBO9*_IB{Zg8YCMMB$^o|Igy{zWgUaF%vabh+Z}d^oEZ1Qn>JA6h9JI$!_qf92yHl+(`U_dU}bV(5HVb*yzv70E#JK{Wx$`;G32=Tj(?!wzodU6OY7H2;w3%<`K(<wsUU=QDjDPlzy<t20(yRw-cMgPns64_K0AiH+qL=9ZshdsBx0<oFsX<`V+e){j>uRq8?bKIXA84}b{P8c#4eW~_i6h3^aZ#C|ICj8YZo`SO#O&YVeBJ*Kv1ug0?FM)uB0>VK}1XE(R8)1tk<t>m4ywP>cUp2z7wrU7`JjZ?Hf)Mi!h{bAF*T@1%}{kiW@PC*bUKHLGHP2am5w(O=o&eZ2Qiy_G~|N+=6vUP`9RfjVElB*qt!yJIOn#dOXGDus?t(5zPv_J!-0XJUAHPk_4^nJux*|nzR_=8na@SI7t!-LKjxaf}8-4^Tp$wT(`1%k(>rDPVW@@EVj*jnSVUNkI&M-N;OL>QVf8qMxvXX9vZms13@aDkml6XVNT9t+#!x$+SBgvEZ%5}PtqAQA$u(^E}vh;G>lmhGs@EX`qt*w#$wApzqomRJNCUcBbUQ~S@S=qJCIZ?o`u4|-xJ<cK3X{s=;ChPx-BIRPg3Za2Tq`++!sl&0g>0KpG6HXFi0Enp6aeJcrSfHX~k39+r6DiJjgZIE;Q0p^hWB%JBA^zQw2qofquy(r^Y|D1219y1GqqblzIaca#1Z0G;;{Eb6Go#oP_ZxUBMpw<5h#0HX<9_ZsxeA(FBl_L7v%@G0lL^2cx+~VVpX^sY8y%Q-RCGmWc3tC-H7D5CJT{lYW(cL9K{knvl$8D5fpqoeB^n<4tr0H7D@5h8G*$8EVqJ%ABMmL2ZUSEFwn$(&lpAp4*`r>)QMI9YyBz6kpV2^@>RqDO}+>2opm&kRGc=s?Lo<IY!P5A6&k&LCCyCEpTm3_o$#(=|`4I5*6_ll20K7Kc}^aFAlx{2VdBsavDGK_-SL4J;@Y}78n<{daePieV;x@RPmqmE;(miT3;y@7&zq{fGGL?n$Z**RZWxEB|`gD6ethG17e*#&ANd0@!y+&{Mit8kGpeV^KJSH1@t(*({#fm^7@oiH;|US@E*1HTPVjK!q~^zSeDv|iB4x?YX9lUAODBmcKTrC(1ym56V;KGjb`50WdY+xv>S#=oJ7t5VhWT1qGp8YXxuZ1L9$>@WLyoxpwUzcrJG*Tv*Tf><Bfm^QS?bi$c?gf(LT4nae=7nvkH2afQ;ayc8z;}l72IhbCSVcTM322fQb3C6SKQsFgw^wdSM`HK0W_7vr<sl!I+4LTE_}G3ufXCMY$L2%b!S3FH4nxT9nzA<|5RR2+1Ax2RxB6SFSF`P%2!xS;Rr@DbOAr;O`_?0FF)^6F8}TT-^de(;}FKG1LLQe(3Ur)?E1h`|nk;KdhM=V|lg@34@gDVjV4NczF};uI)1?qS~CTmd&x2Hh7TA;LRsL92CaawQ&wXE~{6g?#S+je#c3oFgSAZN6+ur`uY&G^9l)x&$v$F90%>pJi`HghS6~xAftT@qyvP&$=-k+2jAF?IVQ4pGCD#p%t^D+;5ei#lFV_4IAS*=s6md!>}vZJM?rX8%i`^{F=M}#{yR_=F&}dK<;~XG#Z`M_^&Elnaz-i3M9L6&Fue;96gzn@F<Y7&Y+58*z=tv?M<+O>>dbWtSOfHG@Ds<QkiihPKrJf1hys+D`80{C_T%E0lD2E)t8^xc>c8!K1hQD<w6pH5=ZJ=H<TsUSNjAT6BHMM^*Yi5Xa||bNjmTHZ6FE5oeByfnD>D80waqR29Eeqe-1#j7Xy);2WXbM%F+?{!sMWvTp#@l|16MiK995HSYpf?7HzUX4k=kAzbVk65F1$BiJu#%PFg<`6;A~QFLCj&zBd9lC5Pq}qOb+o57C<WE1%qLtm1?ra$gMPp)xzGkg&r{K+G>5z36WD^72Cijw+PRX?T8Q4F9EL5!}S~rp`sqK$`q^`3ipbQfmwwv)}!4pbWfOyPLL-<Ujq~)Uw_4gQRsySDNQkj9;vplOjt_PXf_Q%OFlR^t=S1dWxN-oV6s`-q#C9(`gJB<D-gixqxq%n`9=9~fy4FA$f|S`Y&dBbP<*!skr}|JRpMqJj+7nWO14V0Dww<yFB4O1s~SpG9#jHA(z?3Zq7$%GG+ji%xkXF?@og4?ni?2&Zu4R;t`>7JWiU}Or~W0;-Wb7Vtp<6v+_lAlg4hapGfG56^zSCS;rLL($y+fm@De+S)r&9SFpO+bf;5rcI#rL_Y><eHpf4K(Cyo!m^90PUURzzZFE4JbU0r=gp7&=N??2Pe(r0h8R^FW{%mh|gBu^o9MwCvrAnk<#Z}=54RsE}v2-^LWOk<VKF-oGCc(aG0rql;iBDa{y6C{ueVxGczn#8j5e)@gZ&ESG_!?x0qYUGjOO6+u5!+7(XyH)WJAO^`7oJ>^t^7R?s&cI^-Y(6s@1_q==gXb-6_H?gG7dbK#2&tv1ZQ~42FMwWvAW|o2#Wg%kFV{>Rv3A|mCF2aB3sHY#-F{XdX2uy9LqaS-lBHocAI5HEWjK`L@PG&L6b_SL#EA<ZXAAgKgpzHkogIw54*^optYr%?t6`)wQ4A5bB8l*vATZj4^g*L3-Xb}qDYDTtXH5Y@9qir`-h_NuG*dcSC*@K4SZ$+}JD6}b@g%Q#<}Ka~-r<NqHkNb-GK|0*mul~E&XQ-LGlOtIO9Vxmud{FCMxNd{0h=utr}87yMmr1=FBleJ4~eQhZ{CF?>h%Wl&tV73;B)XA2fL3QY7|F6vDIAnSz~_-QTb^@d4~3T1#T<fkq%zH%b$TLEqI|YVH1|P=tEOMXr3!l!gErT5(2rSkj0QfgGU{1ZK{!syUtX`GN>*Fn13klNct@OH2opt(l}$x(}{U4*%B5g+?FaqH_uKgN)Qf{->pCrx`hZ>bb=xE7gO@9CwN;=Lv|bG^%Gyfe?q`lAgp%00KeQ8sW7vck+s)Q(jtNH)?TJ{E?LDWmd*OZYfn7MalT-M!67{Fttz|JQ*Ue3OK#6Q^>@<06+Qg&H4b;1|7Q0$+=pq_Xy&VVGRjxW%u2`gr^g)wQ^gqZ^voJN&hujZnl4MGL9u1QV%p3u1G9x19Ny1M^c_|z1wn1jFKu2c6|tuP29v;Br6kgMaw|O5ZOc_~C;c&ZPO+y{$M~(wyRm(CtM1WSy_)SYp5#&;$+|*7cTa0fvwr+WyGORs_&vhv9^wiS1oN~I%=Vl$Z!PQ;*=E!zIM8pO^VcIKzF{sWxz{d8ujLmj)(AqYbX^{l@q3>2KvhaA5+|tChFNyZAm>^Dj_SD_s*#vB<gH`}e+^P`&4RMTyP|crxUyoeUXwQ@L~WTBdDXPkUnr;}BIBy#;tkHyE~w1%eHDg<vii(AmBLINm7A9SJ?Dsz<$04%=^Z__n}^9X%N+tm70E-INx2fp8g*p=HKpjOE?`alA9Z)(Cj')})
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
        (ÄÊPSH(__ÄÊIMPORT__(("peggle2/gram_tools"),globals(),(""))),ÄÊPOP())[((- 1 ))]
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
(ÄÊmoon_to_py_fcache:=fcache(fp=ð(CACHEDIR,("%s")%(BOOTSTRAP_HASH[slice(None,16)],)),file_only=True)(ÄÊmoon_to_py))
def moon_to_py(áÖï,áÖÝ={},áÏè={}):
    return ÄÊmoon_to_py(áÖï,áÖÝ,áÏè)
    if ((h:=sha(áÖï,áÖÝ,áÏè)) in (c:=(moon_to_py).áÐñ)):
        return c[h]
    
    return (ÄÊPSH(c),ÄÊPSH(h),ÄÊPSH((((ÄÊmoon_to_py_fcache(áÖï,áÖÝ,áÏè))if(code_file_caching)else(ÄÊmoon_to_py(áÖï,áÖÝ,áÏè))))),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]

(ÄÊPSH(moon_to_py),ÄÊPSH(("áÐñ")),ÄÊPSH({}),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
(decorate_code:=(lambda áÖï,áÖý:("__dir__=(__file__:=%s(moon_dir/%s)).parent\x0A%s")%(PEV(("𝐩")),ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(moon_dir,(áÖý).relative_to),ÁÜÙ),repr),áÖï,)))
def compile_code(áÖï,áÖý=None):
    if (áÖý is True):
        (ÄÊPSH((ÂÞÅCAT(áÖï,ÐØó),áÖï)),((áÖï:=ÄÊPKE(0)[0]),(áÖý:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    
    (áÕÃ:=moon_to_py(áÖï))
    if (áÖý is not None):
        (ÄÊPSH(áÕÃ),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),ÄÊCUR((1,),{},decorate_code,ÂýÃ,(ÄÊPSH(áÖý),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),áÌî)),(áÖý:=ÄÊPKE(0)),ÄÊDEL(2))[2]))),(áÕÃ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
    
    return áÕÃ

(compile_files:=(lambda F:Âøî(ÐôÅ(F,MOD((lambda ÂîÓ:Âåß((áÕÃ:=compile_code((áÖï:=ÂÞÅCAT(ÂîÓ,ÐØó)),ÂîÓ)),Âçß(("Compiled %s %s ⭢ %s")%(MOD(ÄÕéý,áØÁ=dotrim)(ÂÞÅCAT(ÂîÓ,ÁÜÙ),25),MOD(ÄÕéý,áØÁ=dotrim)(MOD(ÄÔéÄ,áØÁ=áÖï)(("\x0A"),("𝗻")),35),MOD(ÄÕéý,áØÁ=dotrim)(MOD(ÄÔéÄ,áØÁ=áÕÃ)(("\x0A"),("𝗻")),35),)))))),("\x0A"))))
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
    (ÄÊPSH(__ÄÊIMPORT__(("text_format"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("cache"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("peggle2/rgx_golfatron"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("peggle2"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("peggle2/gram_tools"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/gram.data"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/generate_operators"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/operator"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/node_types"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/tree"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/tree_txt"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/expr"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/lambdas"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/rewriters"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/to_ast"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("Compiler/ast_to_py"),globals(),("↺"))),ÄÊPOP())[((- 1 ))]
    (c:=(ÄÊPSH(__ÄÊIMPORT__(("Compiler"),globals(),("↺"))),ÄÊPOP())[((- 1 ))])
    TRANSPILE_REF((c).moon_to_py)
    Âçß(Åøþáüì(("Re-imported compiler!"),("f0f")))
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

