#!/bin/python
BOOTSTRAP_HASH='CydGB_KCXqgKfcCn1H_Bz5Vg5NPaeri4PHhsuA3ukiA'
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
from multiprocessing import shared_memory
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

(ÄÊPSH((Exception,object,dict,bool,list,tuple,set,str,int,float,bytes)),((áÍÚ:=ÄÊPKE(0)[0]),(áÍä:=ÄÊPKE(0)[1]),(áÍÙ:=ÄÊPKE(0)[2]),(áÍÖ:=ÄÊPKE(0)[3]),(áÍá:=ÄÊPKE(0)[4]),(áÍé:=ÄÊPKE(0)[5]),(áÍè:=ÄÊPKE(0)[6]),(ÁÜÙ:=ÄÊPKE(0)[7]),(áÍÞ:=ÄÊPKE(0)[8]),(áÍÛ:=ÄÊPKE(0)[9]),(áÍî:=ÄÊPKE(0)[10])),ÄÊDEL(1))[1]
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
(ÄÊPSH((lshift,rshift)),((Âúù:=ÄÊPKE(0)[0]),(Âúú:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
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
(ÂÌú:=(lambda áØÆ,áØÇ:[*(range(áØÆ,áØÇ))]))
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

(tmp:={("ᴍ"):("Áÿú"),("ꟿ"):("ËãÂ"),("ſ"):("ÆÑ"),("Ϝ"):("ÐÌ"),("󰈳"):("ÄÔÔè"),("󰈲"):("ÄÔÔç"),(""):("ÐÌÛ"),("󰒼"):("ÄÔàÑ"),("󰒽"):("ÄÔàÒ"),("ᙎ"):("Ááæ"),("ᙡ"):("Ááú"),("ᗢ"):("Áßô"),("ᙧ"):("ÁâÁ"),("⊚"):("ÂØÍ"),("⊜"):("ÂØÏ"),("🟕"):("ãéÜ"),("🟖"):("ãéÝ"),("⊛"):("ÂØÎ"),("⍟"):("ÂÛÜ"),("○"):("Âåæ"),("⍜"):("ÂÛÙ"),("󰬫"):("ÄÔüÑ"),("󰬩"):("ÄÔüÏ"),(""):("ÐâÄ"),("󰔶"):("ÄÔâÑ"),(""):("ÐÇò"),("󱑼"):("ÄÕåØ"),("󷹅"):("ÄÝöÔ"),("⪡"):("Âúù"),("⪢"):("Âúú"),("󰸵"):("ÄÕÊÂ"),("󰸷"):("ÄÕÊÄ"),("⤉"):("ÂóÍ"),("⤈"):("ÂóÌ"),("⟷"):("Âîí"),("󷹌"):("ÄÝöÜ"),("󷹍"):("ÄÝöÝ"),("󷹎"):("ÄÝöÞ"),("󷸹"):("ÄÝöÈ"),("󷸺"):("ÄÝöÉ"),("󷸸"):("ÄÝöÇ"),("󷸻"):("ÄÝöÊ"),("⨝"):("Âøî"),("⟕"):("ÂîÊ"),("⟖"):("ÂîË"),("⟗"):("ÂîÌ"),("⫰"):("ÂüÌ"),("⫯"):("ÂüË"),("󷹒"):("ÄÝöâ"),("󷹓"):("ÄÝöã"),("󷹔"):("ÄÝöä"),("󷹕"):("ÄÝöå"),("󷹖"):("ÄÝöæ"),("󷸓"):("ÄÝõà"),("󷸼"):("ÄÝöË"),("󷸔"):("ÄÝõá"),(""):("ÏäÒ"),("󱅏"):("ÄÕØÃ"),(""):("ÐâÇ")})
(ENC:=("ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýÿ"))
(RCD:=CURR((lambda ÂîÓ,ÂîÒ:(ÂîÓ not in ÂîÒ)),("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")))
(SPE:=MOD((lambda ÂîÓ:(ÂîÓ in (ENC + ("þ"))))))
(PEV:=MOD((lambda ÂîÓ:Âøî(MOD(ÄÔÔç,áØÁ=Âåæ(Âøî,MOD(ÁØò((lambda ÂîÓ:ÄÝöì(ÄÝöí(ÂîÓ),ãÊú(ENC),C=ENC))))))(áÇù(ÂîÓ,RCD),MOD((lambda ÂîÓ:ÂÞÅCAT(ÂîÓ[0],RCD)))),("Þ")))))
(VEP:=MOD((lambda ÂîÓ:Âøî(MOD(ÄÔÔç,áØÁ=MOD((lambda ÂîÓ:Âøî(ÁØò((lambda ÂîÓ:MOD(Áëý,áØÁ=ÄÊCUR((1,),{},ÂÖó,ÂýÃ,ENC))(ÂîÓ,ÄÔâÑ((Âåæ(Âåæ(Âøî,ÄÝöí),ÄÊCUR((1,),{"C":ENC},ÄÝöì,ÂýÃ))),(lambda x:("⸮%s?")%(x,))))))(ÄÝöÞ(ÂîÓ,("þ")))))))(áÇù(ÂîÓ,SPE),MOD((lambda ÂîÓ:ÂÞÅCAT(ÂîÓ[0],SPE))))))))
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
    
    (áÓà:=("%s! ⟨𝓿=%s⟩%s")%(áÓà,ÂÞÅCAT(áØÆ,repr),((((" ") + áØÇ))if((áØÇ is not ÂÞÅ))else(ÁØã)),))
    try :
        (áÓà:=termclr(áÓà,((("f22"))if(áÓÔ)else(("ff2")))))
    except áÍÚ:pass
    Âçß(áÓà)
    if áÓÔ:
        raise AssertionError
    
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

def ÐôÅ(áØÆ=ÂÞÅ,áØÇ=ÐÌü,áØÁ=ÐÌü(PL_CPU_COUNT)):
    (ÄÊPSH(MOD(ÂÚü,áØÁ=2)()),((P:=ÄÊPKE(0)[0]),(G:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    for Æå in(ÁØò((lambda ÂîÓ:(lambda :PL_FORK(áØÇ,ÂîÓ))))(áØÆ)):
        while((ãÊú((ÄÊPSH(P),ÄÊPSH(ÄÔÔç(ÄÊPKE(0),PL_CHECK_PID)),(P:=ÄÊPKE(0)),ÄÊDEL(2))[2]) >= áØÁ)):
            PL_SLEEP(ÄÝôÒ)
        
        ÁØòþÁÙÇ((lambda ÂîÓ,ÂîÒ:ÂÕÅ((ÂîÓ).append,ÂîÒ)))((P,G),ÐÌü(Æå))
    
    return Áÿú(G,ÐÌü)

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
(ÂÔð:=(lambda áØÁ=ÂÞÅ:((áÍè())if((áØÁ is ÂÞÅ))else(ÁØò((lambda ÂîÓ:áÍè()))(ÂÿÇ(áØÁ))))))
(ÂÚü:=(lambda áØÁ=ÂÞÅ:((áÍá())if((áØÁ is ÂÞÅ))else(((ÁØò((lambda ÂîÓ:[]))(ÂÿÇ(áØÁ)))if((áØÁ > 0))else((ÂØÍ(Âêà,(- áØÁ )))([])))))))

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
(ÄÕÊÂ:=(lambda áØÆ,áØÇ,áØÁ=ÂÞÅ:MOD(Áëý,áØÁ=ÁØö(áØÆ,ÁÜÙ))((((ÄÔÙù((([((áØÁ)if((áØÁ is not ÂÞÅ))else((((" "))if(ÁØö(áØÆ,ÁÜÙ))else(False))))] * l)),áØÆ))if(((l:=(áØÇ - ãÊú(áØÆ))) > 0))else(áØÆ))),Âøî)))
(ÄÕÊÄ:=(lambda áØÆ,áØÇ,áØÁ=ÂÞÅ:MOD(Áëý,áØÁ=ÁØö(áØÆ,ÁÜÙ))((((ÄÔÙù(áØÆ,(([((áØÁ)if((áØÁ is not ÂÞÅ))else((((" "))if(ÁØö(áØÆ,ÁÜÙ))else(False))))] * l))))if(((l:=(áØÇ - ãÊú(áØÆ))) > 0))else(áØÆ))),Âøî)))
(ÄÔéÄ:=(lambda áØÆ,áØÇ,áØÁ=ÂÞÅ:ÂåÔ(ÂåÔ((R:=MOD((lambda ÂîÓ:((Âêà(ÁØã))if((ÂîÓ is ÂÞÅ))else(((Âêà(ÂîÓ))if(ÁØö(ÂîÓ,ÁÜÙ))else(Áÿú(ÁãÁ(ÂîÓ),ÁÜÙ)))))))),(Æå:=MOD((lambda ÂîÓ:MOD(ÆÑ,áØÁ=ÂîÓ)((lambda ÂîÓ,ÂîÒ:MOD(ÄÕåØ,áØÁ=ÄÝöÉ(ÂîÒ))(ÂîÓ,ÂîÒ))(R(áØÆ),R(áØÇ)),(lambda x,y:(x).replace(*y))))))),(((Æå)if((áØÁ is ÂÞÅ))else(ÂÞÅCAT(áØÁ,Æå)))))))
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

@OPWRAP_(*(("󷹌󷹍󷹎")))
def _(áÑã,áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=((- 1 ))):
    if ÁØö(áØÁ,áÍé):
        (ÄÊPSH(((ÂÀÇ(áØÁ))if((áØÁ[0] == áÍá))else(áØÁ))),((n:=ÄÊPKE(0)[0]),(L:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    else :
        (ÄÊPSH((([((- 1 )),True])if((áØÁ == áÍá))else([áØÁ,False]))),((n:=ÄÊPKE(0)[0]),(L:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    
    if (((not L ) and ÁØö(áØÆ,ÁÜÙ)) and (((áØÇ is ÂÞÅ) or ÁØö(áØÇ,ÁÜÙ)))):
        (áÏÞ:=((())if((áØÇ is ÂÞÅ))else((áØÇ,))))
        if (áÑã == ("󷹎")):
            return ÄÔÔç((áØÆ).split(*áÏÞ,maxsplit=n))
        
    
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
                elif ((áÑã == ("󷹌")) or ((áÑã == ("󷹍")) and (not last_v ))):
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
        return ((((((áØÆ > ÄÊPSH(ÂýÃ)) and (ÄÊPOP() > ÄÊPSH(áØÇ))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False)))if((áÑã == ("⪢")))else(((((áØÆ < ÄÊPSH(ÂýÃ)) and (ÄÊPOP() < ÄÊPSH(áØÇ))) and (ÄÊDEL(1) or True)) or (ÄÊDEL(1) or False))))
    
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
    
    if (ÄÊPSH(áØÁ),ÄÊPSH(((ÄÊPKE(0) * ((- 1 ))) == 0)),(áØÁ:=ÄÊPKE(0)),ÄÊDEL(2))[2]:
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
    
    if (ÄÊPSH(áØÁ),ÄÊPSH(((ÄÊPKE(0) * ((- 1 ))) == 0)),(áØÁ:=ÄÊPKE(0)),ÄÊDEL(2))[2]:
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

(ÄÊPSH((sys).modules),ÄÊPSH(ÂÞÅCAT(("𝑙𝑙"),PEV)),ÄÊPSH(áÍáþáÍá),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
(ÄÊPSH((sys).modules),ÄÊPSH(ÂÞÅCAT(("ℵ"),PEV)),ÄÊPSH(ÂÑÖ()),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
(ÄÊPSH((sys).modules),ÄÊPSH(ÂÞÅCAT(("ℶ"),PEV)),ÄÊPSH(ÂÑØ()),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]

__dir__=(__file__:=áÌî(moon_dir/'Builtins/𝔍.☾')).parent
(áÐÞ:=ÂÞÅCAT({ÁÁ:ÄÊCUR((1,),{"ensure_ascii":False,"indent":None,"separators":(",:")},jdumps__,ÂýÃ),ÿ:jloads__},ÂÑÖ()))

__dir__=(__file__:=áÌî(moon_dir/'Builtins/\uea7b.☾')).parent
(TMPDIR:=ð(ÂÞÅCAT(("/dev/shm"),áÌî),("☾_tmp")))
(CACHEDIR:=ð(TMPDIR,("cache")))
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
        if not(((s in k) and ÂÔö(v,("color")))):continue
        return termclr(s,v[("color")],bg)
    
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


__dir__=(__file__:=áÌî(moon_dir/'Builtins/meta.☾')).parent
(IMPSIMPS:=((("ℍ"),("ℍ󷸙󷸘󷸛󷸚󷸗󷸖󷸜󷸽󷸕ĵ󷺈󷱽󷱾")),(("⫚"),("⫚")),(("¶"),("¶✿"))))
(ÄÊPSH((MOD((lambda ÂîÓ:ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ,áÍÇ),zibe),b85e),áÍÇ))),MOD((lambda ÂîÓ:ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ,áÍÇ),b85d),zibd),áÍÇ))))),((stre:=ÄÊPKE(0)[0]),(strd:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(__ÄÊIMPORTS__:=ÐÌü(ÂÑÖ()))
(TP_CACHE:={})
(TRANSPILE_REF:=ÐÌü(Holder))
(EXEC_NATIVE:=exec)
(dump_cached_imports:=(lambda :("TP_CACHE.update(\u007B%s\u007D)")%((lambda ÂîÓ:Âøî(ÂîÓ,(",")))(ÁØò((lambda ÂîÓ:("%s:strd(%s)")%(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(moon_dir,(ÂîÓ[0]).relative_to),ÁÜÙ),repr),ÂÞÅCAT(ÂÞÅCAT((ÂîÓ[1]).native_code,stre),repr),)))(ÄÔÔç(__ÄÊIMPORTS__,MOD((lambda ÂîÓ:(ÂîÓ[0]).is_relative_to(moon_dir)))))),)))
@cache
def moon_to_py_cached(áÖï):
    ÂùÆ(TRANSPILE_REF,("Cannot transpile without transpiler!"))
    return ÂÞÅCAT(áÖï,((+ TRANSPILE_REF )))

def ÄÕôñ(áÖï,ns=None,get_code=False,include_builtins=True,native=False,Æå=EXEC_NATIVE,ret=False,init_ns=True,code_ref=True):
    (áÕÃ:=áÖï)
    if (not native ):
        (áÖï:=moon_to_py_cached(áÖï))
    
    if get_code:
        return áÖï
    
    if init_ns:
        (ns:=(ÐÌü((BOOTSTRAP_GLOBALS).copy) | ((({})if((ns is None))else(ns)))))
    
    if (code_ref and (not native )):
        (ÄÊPSH(ns),ÄÊPSH(("__moon_code__")),ÄÊPSH(áÕÃ),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
    
    (r:=Æå(áÖï,ns))
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
    (sufs:=(p,("%s.☾")%(p,),ð(p,("main.☾")),ð(p,(p).name)))
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
    (ÄÊPSH(MOD(Áëý,áØÁ=ÄÊCUR((1,),{},ÄÝøÇ,ÂýÃ,áÍé))(p,ÄÊCUR((1,),{},IMPORT_find_file,ÂýÃ,(áÒÿ).get(("__dir__")),ÐÌü(pwd),flags))),((name:=ÄÊPKE(0)[0]),(F:=ÄÊPKE(0)[1]),(native:=ÄÊPKE(0)[2]),(failed:=ÄÊPKE(0)[3])),ÄÊDEL(1))[1]
    ÂùÆ((F is not None),("Unable to find module \u0022%s\u0022! Paths checked:%s")%(name,ÂîÊ(failed,("\x0A")),))
    if ((("↺") in flags) or (F not in __ÄÊIMPORTS__)):
        (ÄÊPSH(__ÄÊIMPORTS__),ÄÊPSH(F),ÄÊPSH(None),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
        try :
            (ÄÊPSH(({("__name__"):name,("__file__"):F,("__dir__"):(F).parent,("__EXPORTS__"):{},("__þIMPORTS__"):__ÄÊIMPORTS__,("TP_CACHE"):TP_CACHE,("TRANSPILE_REF"):TRANSPILE_REF},{})),((ns:=ÄÊPKE(0)[0]),(áÑÕ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
            (ÄÊPSH(áÑÕ),ÄÊPSH(("code")),ÄÊPSH((ÄÊPSH(ns),ÄÊPSH(("__moon_code__")),ÄÊPSH(ÂÞÅCAT(F,ÐØó)),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
            if (native is None):
                (ÄÊPSH(áÑÕ),ÄÊPSH(("native_code")),ÄÊPSH(ÄÕôñ(áÑÕ[("code")],get_code=True)),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
            else :
                (ÄÊPSH(áÑÕ),ÄÊPSH(("native_code")),ÄÊPSH(TP_CACHE[native]),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
            
            (ns:=ÄÕôñ(áÑÕ[("native_code")],ns=ns,native=True))
            (ÄÊPSH(__ÄÊIMPORTS__),ÄÊPSH(F),ÄÊPSH(Module(name,ns,hardcoded=(native is not None),**áÑÕ)),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
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

TP_CACHE.update({'Libraries/Compiler/main.☾':strd('c$~#qdvDyv5&!=_1<k_1uCbCO8EJrn&xM}0VA(oIXCr`eAgCixNBE9Bkd!Pn$RAGPws2a+^&@qHIE8BjZP3=K(KZNL+xdgv#GfD^Av62p@^Kf%4%&ktK6ZCzc4l_wH$#$rklku;Um%Wyck7qhn_C^nA;j*vy@792wl|D+-C;r~BeqQ`WqieEn^3w#$c!~_QQB>gUgY^sKN$KBE)2rGW~&qL`?Ntim)gzN=$c2ef8hPf`WDOH%RbL;E-!XSe&>kQ4$E$553+w!mJD2A2LuMb>-n+Mi$={>b^`{#&0fIulkC@o4BgSL=UPDKNp_d<%bg}r_-*!#AVWDo?32mt%LgxPdQ!Z)!+`W`>?hIiz=vC$JBp&v@q!p;FYO1zGzb%0?Dt{zb@n+Cf=!rtdN*Gp#2&lpU>NK=!Dt-CX|qM_ejJS~`Pve%tu{PbZepEG-rk>^n_E<*tron}N};o3H}=C6<!`TE1@nCO@b;G|UGWL|rjau~0(MF@kFt-muh=QL{yzJVof0?qn`*o=;3lcVX%ICeNVF6sIg#(u^ZOPTnXhm>e|LY6$cf1yy6ylq?g-*3+AlphVdTKZ+>zf}122;U<JiY_#+x9NPnvtPVZkrxTXI}H;|~n{=j@MUY4a_T2I<fT{j6WMsUU=YDh1>lzy<st0XyH%?qtuJE!YdNSKIJ*_Z+@-FLp;x8vB0B5YkXbK_D11BzlznE_(`I%deUfxX<Et$1Y0o2*%#$GJpl7phSDLTuEnp<CvCM7SuUa9h+A=WqknCqCO0&KZ@3I1ZP@I=fI5<5h;r7V?W)GLrX~3;C_aI$BXbhK{V3lN7A=)7o@WTH*tpUFOQsI<a)X2l3>x`^`S5I4^yWf#UnR8b^!bVirk~>h>59-D=X(WHkTGRww>jT)y2!Oh|{{bN{ltH#9ANc{|k3KF8>S0B`09&J+TY!VAFhvI~_~>)J@Y^^Ieb=;C4R0os;WURyW8Qkm5`?cgdWsiWvOz5HBBPf03Rl4}#&t)b#V>sVN2^9$|nW6?aIp(RiJm^GNy{TQBi+`W!1XTjEOk;}+z|<;CR-tC;LD_hQ~!+T84HceWPW&V|M83p>d$==tPw6#8ub=d=r{i}73+g~KBe5XxICXPctBTkpIpH4b-1cp!r&#A~<SHq;72i}WB{nh^vBZ)Z;_tptzW&Y)WfQQ8u{T*Cvy4y0aP69fwSRVYP$uopRwui+2v8l?W{6<k_xrQV^0UQAB{O}~a4d44a7-PGraqk>rY<$06X4&oulX=yanYymV<K<V_!gerLS_Tk*3aJC{Ws>7T4U5@4iOT>jkHw_MaPysByk$skZLRsu%=90oG>;s^5%q^9}3MqICUE54k{H+xv7I*I4x3tnt;Upyqg%w_5M2-Lu)_UEU>ry3p;r)Eq(D^*Y7d1em;!-)PFk}v+)G{_yjJ*OqXs0l?p@rdt%U8AtnP-&2Q7zaW4fH&FpP3}l5I;cj5rotyw086P#us4Y3tcLw@hwlDHW7aiWoY!kB=^;|CW!V;_5^{>zp|TTja}MYDU~HS<qJSfnt#D*a*LX-$*UP*eJaYDyW$4n7qOQG1rKTj{CoNLKUu=>kvqp)UuMryK@YMUEiX#rU_?okf%NQ!Hz=F7P>$V$u@BUkN>#+hLuX@R|L)-*{)?yW%&U<@ADTo?)KpB3s?!(yeJJ4uJWl$ath6*ZRM@lAc6c%Z>^bz^ShzQdeN4h!?VrLd>Ggp6EOLz<U}7LUr%XJv?KoY-{o#DTp@8UqP&gl!8+sPLMIah`XkyPoqWA_8uhnW<+JLdF7Mr~&gyM1EH_0pcNgw<TR_kJr&ISp;H^edaL}%Uc*bhC@r+PR)wWTdV=#0kXnt{Bt53|SFd&;2&$!T7V$rV%RWdDWZj)@|l&|_v=&)vEcyJ4anTi5D$wfUt0hwP}CN6nhdt>eaFetY!li4lB*yW5^0`aEXsMp2riu{(wo26d`vY=C#ZeDGoxfwqDUTFCZ>v$nZ)k(ei+>5hjee;~L!HF5n{*%!x(>STP>Gjgb~5wU-E;`DA1o*o~igD4a&h9VGasm_DecwMSQD_}!LWkF>Zg6K}IFJF;fu?u4OK;G41h1g1&^m}iAG%lTNJ%(E0Q9-3Dw1ZKmqUZgMX!Yahv6BfWH6=$dP;`E<NCfAtHyA}8U&!X7H{X1tTF1hgNj~HZ0cntO8>Se;>I0o%BTr9u6Y>yt7@pzI?JcnaPLfz7`%TFS9$Wi!eOqads8|HvGqH}#<JIx%VOsQmwcJFL6`1=|mMGH{Gb2=is*z$<l>*1(@^*WDW7XMOT{A-rAFT-l75hyQ;k;b#S$cg@g1pe_4Flcl5Di0^-Sc<d-ZeOit~U%qku%7J_3e(c1`-z{v2MBY;DqFyL6D?Tj8Te>uJx%Fv~uh<MGX{)Vu=vh^%N<Qi)0k)AA$hI{l5I{p(Xd{!ZjYshL2bgCj7MBhjjCl@c!;&IdpvhbV&s+SMU<>WI;IIPboF?C&8pFW?Q99sWZ;`$iwu#7e(F)+gOejmsQEGYV+4)$RmZ_=gOjmMH)qaCGtK;AT}+DqXS8Dlwg9&=M|>a2vyh&MBc;srJeajd2^8mU{Fq_uy8>5J&4PDgA`)0!yCsHfizq$uQsz-%|hk$b(w^dWLH<)v?4=|1mGDW5LAZJ_^3t`CU@;of@PSnkk@pg|BMNw<sZ01I7PB09fU#Zgo)%>Wr;rp)2zy<f7tWKsp#~6+8nz{@?&H^j<AP*Z<4UnrNPe&*+<#q>H3moOl~Sz!HAAFbXGJ(9YH#XLS7l?ht>QwY9B;W<gqPPKriMI4rAt>>>Guecr)3HdPbeq)J}dSargYD_3}42t9v0p4B{qurGOyv^;w=}5Q&`AGvocxf{1AG&{dc{GpN!<iL4Y3d}(UWI?K}-<OU#!)CoFOjSMr(HB-T)byJtDvyd1BI6zQwt~l&lXJHHp`5}@l4SRYRYwXH!B-Igs4B{@@Pk)i59$e1Zx(T1->m6yGE{2hNkWr{=M8L}`VC^3Zt%}etiKv<hp6&u@ZHc!?4rz+OIm1P(lwZ6ExtAloegWp)&mNc<uUx^v-o%}3M$R){!gagYg_EeaD1d0h$#UGRsOOm63$LeWiJ+)n`cqM*+`V-Im@QbR^p<OCLnLZ;a(IbQD1=acp8Ze<ALCa5tf~9d%C~@Ot7%HJiQfe)pZUr&3g7OyuY67V_>D^zxkh727)<yC6EO^31;ow`DI}Gq<?s@Rg_6aPL4$(??ro-%OlrCtV+v)70e|>f(h;bfZ)N{cQd(!Nd3tPFOTGk}6~0t%Lg&fCOsnF+=#C+zhIg=YDk@ByHuEXEp$c#7X~<GYHdXlo{;iI$fQOMAg!u5T$V_Hgjv<Y}4Lefi<|;M3VcD+Vb>WVuA}$cDuy|p>D?TJ&PqtSeTRP~x<8&kYYu<}0w<GyM`M2sr@>5Gy-OE?=^rKhH#78HU%M;~?<S;=m1G~m^btbG|v*)KXV9K&aF;S|fwpv&~j?>OXk;6&_tJZ?@67yQE2%Z9`9|r*%SiC5cSCOfXEjPi9>|1>t1y5;?$*jxV{3+b3Jld;Q6_3dzm+DB?Vddh1WD|M^lNs&)WQ->Bh^jn9=MWV0C|AtR9GhngU89NDH2Q&suPFNUp%KwAdlP+X7v!nseI9lQ!Biey9)|H*=Q%Kyk$l7sDrJ<)hYDn_hj35>kApLk(57rh_VFua<!F|=tc`~Lxb3XICEKjT?3(16)HWNTg%Ocs&2jMtXBGNocDa3qVWDh3yUwHxKhK*u+-AjREfF8nnG)XC_oHk!p-)8{llv){a8-U0NGne;(y_|bf=rJUkkv3OTNmOQ-vi8VVmt'),'Libraries/cache.☾':strd('c$~dfO>5gQ7{2FM7@wpfLfwyj1ac@%O2-B(?GA%tj1$|fshxz_2`OWTmSl{5KnLp>I~2<3ZS13i9Y(ty^vCu}av~{lnzo1OB3XU(>Um$i&y&_8H%W|Dx4!GQO9cal=Ld%4gpDwD97Ip)J9<Ls3wlOieN119X&|OP7H8N%v`=4cY^`T!Fd2R$lN~p)+{r=k*w?@eu7T;##Jr{FDh5r>k34%0IF$IQo2G4%;=?Mk=Ci}FzAu;aczfQ)WE_1@BJOHnD+hc>B9=AqLJoLIA{I69Vh(sgA}kHOWM{RgR39PB!a&Tj`MW9&QFo(AHpCpCUz0hpIM({$lzyN;O66hci=way$qgtsE;>%bjeW<N42DO+!oWbNtHi4B?g16(*6bRLjW979&D5ZW^n?x+B5bt%w9{@FI+Z@^${Qqa^%}+yUBPPvbUjbwL-eZ#aFsljvFYly)ly=`?I}qN6HvoK_u}G?pQ0YglGX!ioOnR8pA%AczaDxdi=JHW^L7eTKc3l6vXvGwYed1VQ0GRo7Dm1>8zd%t3)3M%t4t5*NBWrr5YK5gqW$uk8zsKlhDoOdw_w(1!?;sj>{=$q-uImT;q%2zi;>t%&1y!BNxbKQCW00Y19$_L&oB65l-|&<*l-)3L62a4!9m3^aok$cj5?{0G4>%_M8BiemDTlX<-sP@1oJUzR#QzP&#R`Igr%CqGQ8}veS<dUI%X<Wn@uUFA@W5%Bh=N(8gjO#0kz$;Cp8V%4oe6{ER~^P`2;S3EsUby3zIY%yHGg85j@aOT&$r$QM4w}8!4)Ldqs(c$*rU43)OSRWiK4#Mus7B|H5*=vVi1&SxV-21r+baS<}G_MQ&X4Tmw}8sWkfFYA+|dZl?Hh%j?9gO!wth)O0=m`|}>GVNNW*m6T9tB^K|Be-OqGa}gG#j~vjy^f%fTZbzj5*+i0Oszq5EWBNqF<h~|F{&Q^?9EWYJR4PvO>Bi&DCtKimJ5jR+u81ItDK0fh=DM&WshA2a_7{GmNdz_c4zi74v?HmTS{j9a@ktuE'),'Libraries/text_format.☾':strd('c$~!=Yj0CW_B+4g>Pkp6>6F@rY`5;3E`+WsZM&%;tF7c(mSf)}Ui`?~&c<n}1OX>$fsl}pl0s=y9(_Pl3T?u(NX!rDZ|MC6E9DRDIdf+2%hyT6mj+$W+<BZi=gfIu%GL3Dqh&RmJxs32C-VDZp*ZHGGptgm4wnj+oRK$0A51OEv!ahWm(p@t-jvIX$+PmVTuW!vCWdP{7iMeME@n3H@(6UN<pa6M<SBVs-ecZ*({f!d!BTl$ej*<+dgr)9t=!Nf0$?u54bGiP(_u*te~ixK-1>`^Or#FzIl_vwC_1=>1J!5bC+{A6iv`JN`TSUUbgTkT%W35ETm&a!s9LNvIFicVN@o;=zrV>6Je$bDnCt*yzo;E|LbJ&nY{B;<Z@!Hv!@wRkQm&QqPP3SAI{#?`-y06!SFBgZ%N2*QV=!R9-%cKWe<G3SAIP#d($p)x^m^)buiMo*kvNgve<1f7ub#-h-%cdqN#$%JSRGh%+O2$Xtk8&_XfrrtZ<F`!dxP72FFPjGrbZQU1Zo0&KuQMwd6cpJf{PD75(-drVpxPo66)Hn3%ItY^0We0s<#^DY8aTg|F)RQ^e0eM+Sz8MTy)q!>NQ8ODeGkmSeCP1vY73jyoJOlDN-<i-6&XJ!7c!MN?w(#tPLxygVvN5gSNi!O1b6$pWhig(k*i+Ti0Y~;LwmKWeOGty2dNz7Q@R(9MWe4{hz~4&ziM}%XztGov>8rTW$nUi?BMr1%Q0*0&3H6#4{B1H90FEGQ~t>V4+fpT$N~ZF~x<_n{|@i5b*)9zW&g~De8R{YI}6~tO-C<Z5UdVRmeW*-<Ri6H7?6jnFMEs5>G(`$f4wiHJZ~^Y>yhe<NXu!O3sL-WFil+SL8#5>Wch<Q6p6Il&AMt@JEB!l#~H}T9{}F=&3N>6p9o|7FXNKBbH}+6aa2zGB8g-Lx8i?0bpU^$(+U{yFbTs8ZJ^}?GA_{JSY0}T0NfxqXVj7aYR|@DKnG{>P$Bh>ZjqfCK@%1#7M&yo?!3U^Vfh{DwdBIN=z|vhVFWnnmI5{maS2ElJT%I><`;jPeTb37jeV0WK%0KHdRgUXid!xR;+^=OM~>8ZYWn6_zYq4f;<J{PV2$WRCquZ6m=*A5ds4MHBD%m5R}zNN6hg6*Tb+9F<7BmoMTzELI`B9mEt}mfUOw^l1mF-c_p->=UK@Zgd=$R(0w3)&qF!G{#F3N1@YM1bmu<a+PwSA*5-r9N%RbKg6JhOO(Qdt8F^cb!H>oRurr=q3l%ARSUF%Kogo9EQHu~bX_cFn2UKmFB(vVrE_pH>vP%)TW8HAaK<+$~5QB=^QmeNtrLkRf@O@yxomz?E<)X>};{pA81H=FvS|0*<*@~PHOK$8LTF*SaGVk$m6}2d;0aRYLqT1-YEY5tL<3<x_f|}@SVG6V`mFqS&q;TD0(rguq#~Ug#Tan-S^1+Z$8nj|GMFkW={q<RZU<8XnQkjuHMr&?|W{h1`Mw5&#?`>Lw&fzxirOXi%6SMJPoMLK*Xh{vR=XOvcJbUPA2rNJneZ$2V3yTz@YB&WnS%q3jvu^NR7Mcz2Lz5g>OAJBT9coN~TgF~wLRpO7RuZr@=4KW#?&+A$0vgj4Xq=IkAm6xbRGI{Uv!Im$8xuiWJ1c1K@NNCuaJ`*3U`9s4t0npq{jZIHYa1?)W{8}0fbAexfs-}M>8%59B;Mhv%fT>*HmTqy!2_F@AVJD_A$5{M>R>9NBWOS|c+1^)oYdEaIs^n*aaW-a1RIbAo_OXTk)#)zR4GG@qNz(!M%7$NilfcABEN%O?);iN|CKv`-97oSJAcESzv<3nyiO_GCFSA=yIuUi@Ad9LRGjxjp~?CIJVQ*D&)JF~e-y?}+FCX`igX-W2%v`nSC5=@5U?O{XdR(9pz!3LD2V9!%fIjZ%YpNA0b$)<HvrAGfM4?tNeN<KAj=RRDD+tk1vCi;pS97UP;8AzeBi&TBx{Put0_|$&>psffANm&%Knv_>9l_x;`(qdWupIHNfcxWT_BZy`mPE=KZA5EMNuT2*DYj+2jAN{B?s*e=V<2SwBf&^9TfAFT$N`cJP@k6m{wtPaD@C4fI(Eq6kxf6@*H%=ygQf<WJ!MDqFOekN%Gjp73Rf17W2dlpxpRlQBLj_Wn4SiD2&HfFtj?BGJj5p@eDhFA(lEYOi)yFv`xJ&pBkIm<w&&IIcSwg*j3TNOVYt_9PPm!76|(cA<#E;Fg9+i+C?r(VjP*%r%Dx|ktNQ9g6NsL082DaY7;$*I+`WbOj0y6%A22;%K~$dOd=iOL&U`CLL=%U#r2-Y!|Kb1yu+fULL>zsb1E2dQB_IOY59=M^OC&ag||Za+TJYF_Eg6p>Ns;b6&_%!I**GcnR83KRN`mIeny$-i_<Q7XQb;-zI1uFsjtHLg(~2sFBJ}Jj@2jg#d^sJ>Rc(4Oe9QE7fhsw5?+6%L<a`~6MJOTPBZ(pWWUX0gA^pXP4%vFs}efP81Z68`@$XqkVRXjyr`voXxnG5&{tK|zIqjmeh7%N2SuhWfnRXaMj+^7`L?C3Y@fL>uUdk*2Si`Ab2{+Uw>eS;yYOLOA1jrMEiZJ1$iypyf>fDU4yKo(bB}Tl5K`sF7v;~`?@<2%HBYFyN6j;8?o;y<H5=4C6iQg{V|0d{pX5mdH%qgR%<N-)zld|R=mO0@HuF!+#95knY9^l2##3f~+Dts7iD@%&+H@97=Zxtrn$ATu1M9ePLEggV5}tP&iMW8oQjPUX(^)f}uc)(bM%Mk28>Vy9bZ(i>*QWE0>0B2o&iIU)8`P{)vqH@pHQ!S6jjmVF+cj#gP_vGL_1nTNcj2Ua=f>9E^*MKC?fFx;v-JFl+qvX+R^85m+qvR)7TwN8x3lbaR<<@b?!mM9{1><LDRl0;ovT}$n=@|bGQ9l+-D$V;8FYVkJD)@I5S|UUa}AnDFgXkDV`%5#`S{n9?wMJ4?wVZx^~~1hqx100!*gM4^T%)D`3{~t@O%%?Iy^tXa~Gc5|NDILB0N{&S%l{TJge}m!Sm&B%L~w~z_SF8s=M=#0^dzQ-u<G3(j{fNy<F{1uz(N@Nz-qEb5+(+smwO@gdJkep#AaOqCGOQU*QS{L}YXLVdPcy73I|<?iU+2g@^-#@5F?NZ$~3U7&{soOR0P%yl%f53$HtXV~39ZD>T?27jk;lQgmm!I<_Fs$tO(d-U?G`_z5d+^0J!bCS+daaX~c2L+9kv*xKs(NU<a?EXGt>r6{Y4*-P?E-F^*W6D4G=##Erjjrl2L88r(<#2*f%Gcb{D=e!vzl(&n{c#9DK4D5KbNxA1xI%ATAK>j;~X-jKr-04nofthW-FQ2a!s!l#1DW|D@q~tNxo1j2}m%93?dv(d?*`b^m9?hUjN{l3ImA4F;h;k&6u)C{vbWF6q8F!5L(Mla*rxGbU9+<K^u|+Z5PtzWYV)kC?xmP>F8|VT^dHZ=6B>yvwlBT%Yf+xe*=?k5?H4g>zai@ng`Pa-<AT{u|a{b}J5bw6!a;i-hHY!-D#(%m(9WSi{bW-$~o#KK*HkBi&^N;ps0r-O#V!<~r!UD|!6P&brkl<s#Bl0sZg#6m>kU#vw$RFMY`6YQj26>xqKBD^~rjlax4NDp`@_`?s#{9R1a3)D%GBjVyFM9ESvEzEV$xhgD`osi)uu7`qK`gIO(T-SpT%}&-e<%nOuoAoJPSD8Y^Jtt89XXPJ^SyTmj}9Hn=h<kbK3u3MeX!}PuPvy>5f#STLN)k~$(=3m7vHerVGI1#Z$<T1)Nc*-*3fTF^`@Xuh1%AYY8)A^w`~DG*oREQ7Vu-vhlGMKfQ}iP^adyODE;pMTTrV`F*yqyWV(t5%q@TjY}C4#Z^N)9W)xS4vuiv0T?khM4743ebM*e0o40$(HSPd8gL(MXAG2Fdvz2e*_x+K2qgrS&Ezw4{NM%$W&LU3986C9|CixxIukie&1Al4-`6@2@@x@)9_G-HN6fbWKykqL8&aj$=N}*)I`>@lnT9Z!Yzm5gSwrXH}F`P;qYK=KorO<3yt+8@#)S9YK;CSlQk~LYVwXAv#hZ@%KL}OIpkxU7;-%DFf1-y{X=<`8%;Ou|b-S2O@b8}9i>0q)|Xx7W6LbF6<dE17)ZJ4(H?rp`$Y5lP4w}qdd-wUiMML@@_(ewH{O#%2@z(a@er-(l#{K0D&7DX(i1b3mfc^8>X3Y`w`w8)BCQrz{D_@i)9Wuk(M65B5V{YTQ;yIYF)qi&^8u=%#TcA%!Q>m}x>J^u&b06jb'),'Libraries/Compiler/to_ast.☾':strd('c$~c&?{Cz|^*eus&!5KB7bUrGkyh7`r1aE45DC&rX=FKGC$ZS|y0#ZKswyQU<bV_|KOp2dxDrsVKsd@(r#oox$A^*nwSPnRFF@))(D!D>_Sie#T>@&9&3I?ty!Yn)e&Z0jPH&u>{w=XAeEQ_fxvBFrmPLpjx|c&QcEd<F%*9$`-mXQ&Fo~`khGBB((ed%qlT)WgC#S8k$%)aku#chp-2{>L7$%#XItP!lgnXzCX@)U(f|OET4DI?r)sAfyWi>9`GE%|6Rv3^oQ{#yJHhoIhO?p80>1yTl`Oz~5p;zda^cm22^Wg4Qd*%9@2YcV^h&7wvU;mgb+<o>jCwM^b&>izPz=dlVoRsA>>JmL15ydv$BL+EBfyZa`Az(u=ME^;C%Jt*+wI}~xi=5C4@R1Rk37Z)KSPJ?efM5jzUD4KU&+h{*f)&upxT@}g7B?(AiU~+(kN%DR%*G$Z_)?7DnwRa+x1yy+7*}ww8HZlos=5ARykvR)LW9pPG(yL<7MishFc>>a6((%6I=^TIb{M%~WsrRVM3*hbd>p#2fI4{+Xnjtf7$YY%`02sXNQL}L%XHX_|In>BF1bL?j+Wf0B8*^QAqMHCx&$*tiz79=K3}yp5ZMd5I|9QYy-iXx=hL%;bHavUis-R!WM2W|6@5YIDj4kFi|Ck5uhJv>Q)1D$ZS2B%LWWGk{NtZck$ZFtho9&gxXbTbgQKW5LD>{uafjZdw-X#h*AN7NB>o0s)OF;>b{vPPM-K}|;c+N?92ESIPfU`Jz$ZVNGdUte3ce|HB2LInyEz{<gI<zPy#NRh0X$O4$TC3^Q2a)2c4$swXvn~clm&2O`lGOZv~Ypd9G^IK;dCXlwi2x~Jl=xVX^GtO@CPv7q~Eebz?c#RZOnwWbJ6n`HSV1dRXIZTCk~gj3<=Q4{3e^mA2#nT@TC;Jk;2G0NYSk{+plU~RNQRjNrZ0P41Miv!*@H;qP!JkF(A+ldYBy;09Px61=Pq?wtK)e24?aAIb+E|N<I_FK7$spYGzIb-{i&AFtiUf<{w9dz5rv-a}l7uv%Rt{Wp*?Sb~HTq4nC1Pq+2V<A=W%!Bl>?|-v0_dU&7~}UewBQCBp>r-WZQu?R_bX37dta4Z59%G~`w?qAT$593c)_ka|DIP+2<?R#>}i(wVhO=M3va5&Dy0TBcgVFl0yV7El-)r9oxf<<Z1j@Z73yDB?gGIU(&O8#UwI&a&|xR!LYP70wd65OV5P(1^U)Yxt3*NybI))WuRDf99%N%g2gYup^AlxJ5VS%)*-I2hCWlDa2q`tJZw2;arRq`V^He@Eyjgbs~N;iX#8Nd9d{ZB>z-mNs5sm!D5M1QKxj4)^_QArrBNkS26C3@gY&<{3}q^zRD+Su!ATLrA!ags)8g{B=Qtj(p|j##eJAOy#*qxyi(ElIjxJAEZ@dz*1$MGdNO}9sRO!V3^R;b-C!6}c1o(wMCib^6+;aHf=?8OQ=VUiQmg>mzVXPax=!~3E#=M0I*Lq4|Jp$eSQ*&$NKa+e$=Bs2FS^LvrGPtv9b3s{4pwS5wl_f%-?M&Wd$YZ<jla^D-So?@yt13DJXnE=TgX+14W`xJ)139}(=QCJxg*d}B4jfYcPXc9ocw1gBk;8Q_N1@U9ggoa5Y$_7fQP;PDn0j|D@x)8-vbp&iB?i@Mn*J@9nPsRT4dT_WfY;0=?(gi1Ox$wlBJw?@~zM*1Xlanitx9$)z&Tg9S=9ZbQfAjNJBc^LZ08O&x3g?Abu@}yHXJqB-98}`Cz_DqKamS)bYcs8}QkL&!6FQv;ED(_BW5(8(Zy-o%Zvq?XM2nhu4LOu>LF@3ad;jV=JF9vJx<rj%XWRE7}H}KPWa1Y<{1v<mQJ<8VWhV-lF$lj~oUcit(|WHJnDU49S4I-=h?QGXs|B$hlNxNhU`IP$tBZQV~zGF1UJ1q#BK}%WN}Oq%k7@%vEYI`Lk|lOp(}_7OQ4RJeK}Wby?xONwVcUqCf`hAaMOEDe;dN^tmC9Y9?aj`KC;2`TUho@qB3eVlrr!(mCp+W0Y5ws5rsFYfYsdCGphJp*_|OPUtmg3YFClF)-bp#DqLMNx|mcq>^fx;Zqcwsv?O~=#0~(#9<2F(M=;nAJB6_FnLT)!b~CKNsh>^jz}&66~cKQtCS8NGxO)wOPA9mMbS|<orUmXE;i)SqGrdvigLzFTn~8MOvR3&*o2a(QFX0GP^eW}c(WQdnt>JD;i4NyCFujI7)5GW3<D^pyOz>Wk*SvPJhAJ;vK`~iS!uQ1VMQ&K4e^G+Z3PmSsqD(y8CBLAQ=~0WHp^TLq`kE=HadeM7GNnBOdK3h7Gn9rFuzF?MwVP#=O8m1%Ak0j(Hfz~4}wpH1#uxI@sdxrGKq9$7*=|4bN0gI<ng(Ytxu`0&QwV8lKu<&y6-#B9=`BF;@Q%*C%?fi^c2P7{nI|$IP3;mdgoqdKG2I)n~rPI&*{s8Ghy%PK>61QEN98~{BC{|yP<D~%Ss6Dux`yQ^PB{U9W8bx0?a7=?pOt%+I3RD*<3Fxc@@$X1+F94?9Oad^Bk89v5Jrt?$BOUdKT~f`?$oeS;nkXgY(8EOA1By<ja-l4^2B-a_o4dqDp{L#=%TgNJL2%;^}3BZs%&rl*g92Jd)3uY}^4%Y54CusXoV~nglzug|Yzr!nup*syA!@k8|A-Z10NkFUff9^KD-3cDTONPv<oc-dA2Fkd|W0Y4|-;H&mulf4lWd(pRrshx`eDp*t%WWGk~oeu|SVes`S-uroj*^Qk2&gI7PdMeS?*x*~FNHd2G=C?pCOAted_7@?<kH~tQd_V!xO+lewh)odDSA(Nb#G4Q2#Q9Q1&HaNMpFhohqf%2CP($$rq{GYq`rSderTr230K}q)2^WNyG@UpK_`FjW0F}CE?A1z0gW7leZdCY7N4^P@x=tQS4oH}=YYHU=O>-?cPUO<0cxQ0B$om=z?k*>X2oHwMqpInA!FU2g!3!SE?%&tx|43{C+bjz&GMYq-cg+byq=u92*G4WOQHr-UoDLVuvpR)Vp^x`S$d^(JAP3<#^uBYP?3$Nc)7FC`L^P+ZJjvK`Mb;do-j_|F^<9^<qPJ|)UnGjJgL8FZCP~(O+Iz97&{Kg}+y~t%4v)8IgyDBi9IFbI_iZ$^m{=3PvWfA#5O!z-F=q4Wl`~Lvj=3A5'),'Libraries/Compiler/rewriters.☾':strd('c%0Qd+inzBw(opJO+VE(HJ00)xwWRxgcwf-9Rdi5&Ky~-R=Hi6R@&XI>NaU!j(}vsB|rigV}c1dj1v-P5^|Y@OfE>-@8=gr@&}9}<p*Z1eXD(|sy2j&gHq{s)!u8bwf4I2RUOjT=*7cF{}eWx_-+4-hYuY&)@+7hr4ujBFT{fii55G(`M5I(NfcHpgpi1j-Meq!3kME8zxTk==FEZFy$4|y1NL9Dp*Dv^?B=1v@O3T>e;HH*LK?fmew+@QtzLIntA~84fNs!l=|>TLoo?3Ty-_WE>4iTxXO7J7JvJKxTF(PQA-zXGqStEmxd!4i0k;nJx=93&x6ePo0lDK4INawe335XED%{=@e-aXoNYG0IdX~OTzYW=~T?@(aAWdFL+ry-Jyq6-SH|RC`EvfAa;9r>Cm^?mA`+z{Jx72TLpFfRwNCL%}nl^fn48vA^?!`m<_{|UKcM+hsM$gm%fi-%IAhy@(E&4tCd{=yKDj0K9jYxg3YTu_DQ8s8#gVBUjuklUc2sGf2W9f226yk&7((u_L&X9<70yNyT`_=6J2V(YnxX0_)#lB^fmJqj#ZQx?sZ_amK9yq%PGq2EFnIw*CF6H<yqkb6F>p@rnXn;x(cNa7f0D9B_WF{i(4$(&enC6KjUeHF$_0Q6e>2<a`|7t+y+eAqFco>fOZE+{*3=%cRSZ%~a+(ZPQaydtKJZB3tK)Fpn6rwTMK7E0c&6SSx7v~|1n>KIpUz!Y;({A7h&(EgWa0lhkVjA1kFJQ(GkGCJK{jdR}CIk}+;UM2<u-NXiaYz+21KM4f%WqGZ_Yol8{sXfbPlnmQPG9_C<6rkKm!bv(eYi;+CY}NZkeD%e!{sU$0m%g0lxln465_>maVhRM2mPegjyvH<X>45?U7?xBs<k>ZF=y#jx+)C}$^;386mQZsK;*|eH$R5!6SzKy>l?Tp|9EHZ3|y}QA#=Zpej8P%qv}*t-4p#Ts#Y6P+{0tjp!xI+T?d;rxfH*g4AZzfKpHOtjm8>xKZ5ITaKT!4VXeCl;rbM=&)|Y}?|uQ--!)v|`Av9!^E1Q?8CsdDPVf1TU;X+wzx`c2-vUllGQ|^m!VR4;c<(E-$!x#|eTzN_i;OP*s{|Eh6h_<*0BvjZKG7|sG8%2rOCW45vl{;8#plX6C~#heuz7PMW|_s{JM>HR?|g9e*MRE?j1n@t6Au&E2V&!hoH2awV3@k*8*Vm-r~1jDR#&DfS?Ui@;czfl?D<a*-`kYm+e>}<b+9}yzIL;(!@;S6_O-dVJRE2fjK2Yv{x?FY+Bc^48_A#*_mheeKhv=&C!8|%Xtqwosm~MZ`V;O}_XCrE9Gv1$sY4&u+0x9t+EIZQjT~8>K)5U5`@iPG_nB>dm_(eRTbb~9OqAyI5;A!VB}sRKzu;~#<r+l9lL$UOr1x|u#~xesjK&IYRFoQe(d+hxfrX>;^tQJaXhvC#QO>&&Ar>9u?aEH+&?&G{ELHZi^b!3SH}e)fXM(;~L&;>{0v=bBXym8J)bj4~(tP4kbf2bllSLe#E1Yjz7VJLE2??eGdQ^HpkH(Mb7C}GvNk!KzK6#_q5WjTz=>C1P`wsp0!K43kaNm(bFU|teop#^USKHu8y869=po_1SJ>lFDULE*;o8FddPZ4`qGa2=tfH!(>F(#irLOyL@dexjRd6m1=gdXpc9Dx`nX*W(!IReohG)Mik84r6)S{|9j>`uTws^o{cVWrofsf-`ihB9|n&m!ibS7GV8OogWiG6ARz>6`SfaevThx00~R*JB|~L-@ao`(_V>RY;ht4YgYPcpyW7RYVzd^^mfH+kd-*c?c#!_vuCY4>1Z7BcdU!#~1=-^~^&R;L9ko@y_VE_Z0Nt{0*27&=I0dCq7l=v3()j{_{sHpRri5&eA812YlR<FhP&Rq-9>SBzOZYH7=pkO^`Rp84>ILe-$(=%Q&(|0(5vRVgzn;nR_PE<;qr-lh*XmH9aO>V5GjLuj?j*EklSsg8Owxkpdxr?gOwaRps~PZ9TvL@y^@pTAa@ru>l#)dzg6u5|KF(=R$by>M~F3i%c*R&8^TanyhYA+~|6T0*{*o+u#Oop&*pY1QEnxD0Z5jBSzx4nD&<Y&0(A_CPUZ5FZ71Bl2B0b^yYcEE@<@^UhJqEte>oCl!o98bHH2Bnb*wbNvRd7D5R*8@@W#Xg!zao#51-8dqtCP?<Xh-TB@uJLcFjrfWWDytLKcVbWCA|tjw6wIHR*-sTFsSD04Q$;Ru<G`~9T505*-yA;uUKyP$BIswVJ_ZKfx%ay&6(0W$soWG7plBu+!(8VV!|veN-GIZU_B^|iG})^zs2S5CA$iQuhnN>3uA`Q6EWuMaz8xt^1nguV6Hv2cjASodT$GwC>UubwNK%M|LKP^=r`^Sb!F3xF)xpcinn7~FL$mC#BDj<owz4_N`i(txXPSMO&v0$C~wZD!htgCdn8E)C6A78}}7HK2|tG8H-L69V>x36H79nIDyR!b+<`vOkZI2ok4wI84=<#<X|}U#r>IDNU*OfKu;i7?m992SqT;ZC}z!mXfZ=`0-;2R>ar@qb<`w8RvV_=rEisktDHGjl4ZQ=TwWmBXzYF<LCGgQ90I4r5WptmucgIH|Sq}zSEwHmB(`P1Y*}|v*c+)u$w2@TFJA-J+NStC1xb6hnCC{MYgNwwohL$If)Q<`)j9>;Sj77DJ^U)%t4*qFzmB0D|GmzWxZ_CEQC-_3Z~t_@Bo$eyNJ3GEO$|MGA107KZMN6(`!5jM$lTaXgH~og}jzr4|&!l?h__)W57luQ3(6G%@-rxDS^)8kYWz;WP+`APU!u4nTjjU6)(<e-Ji0_@EN*H5TWrOW6*q%(EZ($ai_fy2vZhdbul>JTZW(mWSz@c05bNA3egfFR~j=h8~3R3b$V3^xd?T2i7*ZvtjsLpVrriXrpdx`D``S(`_Q(?xF@{Er_wF!n2%*fgiPY>z&-LZ5+P;eS=>LT!4X?>9CW-349u3WQcFvrFjFxq8$9Y0p<q{pg5qvjJS}o;9ye+yhgq79!(>J{MBm@#=Z2PZ=LEvE(GWd64zlSmCSX~z-Ca%sS1c7Q5iN8rVH(ew3n0(HqeFbrY%TShy*}3I+g-<{<BlF+JIXR4&b|$%XRCmcxuGCwLe4g8b*70Aa@~HmJ(wq+g+Sp;dBXBWmI$GD`M+<ns0{;(@91Z&1bYDgUz5zwSe_=GlX*E3-+UGyl!;HKE|wq>;Sf2Y5;Z0mW`c|-AB(xkph%555@rT&A~sTo>PVS}j<MRfH5&YvTc<HhhU5TWRr%1slYZq@O$=QyWZno3l%N}0rpf<Kk75|-)p^PsKTz>jn;Z5SudV5Xsa<=REIpapm9fYuEcy1&*T|va+h<2!pu?h#!rCpVHr8Q<S~(}q=S6FPYD<Yn%-GsvmjY3|r0mP5!SCzA9)FDBIo{)nT2z_afH2}~gG;{tfue$ph^TvRP2}WQH4y`!o+in{ie@qcAdOWraMJ*8S_6mG7ziFj!lceK*ylB1C#)l~%?R^&@s$l)4YNChWe#3NDhEv8qL(0m=K~aQl}r=N`x{DRCz#`UBNwhnSi~@2Ij^)i%MbN|b2{cMnkQIMt3FdWS;5|9+Mm<g^>iR^R?J2Mt@?-_dvKzMr=jh%wcK{Ia6?5wL;e287JincScOQV0G#QDJt!+!vNZ9hul}(K*ENv@?)Z#AKTgwo0hva|u13y}t&v8CVj#|FM8pddp@O<HSA<yX=Ebmld!rJN^Il~ufqdO6(tC<cPef25n&VS!5VRAD@(;L-{KW8H@nF%7XFVAl49h)V-paEw3rV-PkU-pQ4ah%GUt_1s7gmg8c%wR@JLlrC8IR%Pl2!=gyf|WcFWJF7mDp;tNw^RLV<pC86pd6j6LOiInP3x<`a{-<7?xU?qP7aM0z5}kb+BlHJBu4N`WJc);QsXR!Fk|lQqW_!zn)Fgs(kO#+eLu?`PGwvMfuBOrifKIUSke!l}DXd=sFXXD|D@H9SS)06P<q}WE<ZSrv&HK@4jy6N)R#s+(A)F`Gn&7&QV@^7wWCscV@xmKJ$#@_D-r|tfD{W;yOE?VnxrXNL#dcmbQcOPdpTo>7uk3EA$<@60yF+PwQ;iN3d)rNn@TUt~}D)3|vcK)K`q$v&i)`s9aT*dAp40D)V-Og>Sij<`Q-qyaCIeMflh0n|dRFQo&QTet60jRcx{3jh>Jsv}L7#6#O!<vk2i+4Z(JY>}0PQ-Nn+y2St8u6XGRON>TIYFOXoHMHpre#E}(0xM#D(X+1tffw6RyKQwQOjpQuipalZzwH3^1*h)QC*|44>Q_W?9-5Eqx;TVgB^2A^jt}Cv}a2BZ=n|pMe!*I~&3Sy<N1=|kBT<>c@&_K*I$$eBMW7!@0vzC?P!Jxe;tIK9(dAy*#sAMG?6;X9Tba;=;g_WPadUOG<i*UWMec=XtT!HHnT$gtopCj{b*XrIve8_CUS$;MR!&GRk50L?WIH$P)J;djSd>oXQ1nulDo29=z)ZmFbL*ksLEeH4Ui=8D5Ha@^cEmL9(d1`fr$eoi$*4OvI2ABrd<JN4Gx|MY-XzrCmia41?tqZwJ=eYFomS^5w0#)w45E=VGz{603)jGCXjH>Fky;?oPfE7tiZE*~d6v~;Gj#wHO$sS;-cCB9j6rSTKMT;aa*gz7A2PnuS>cM|py29|4H12z)(U#I8Y4jv>8DQp-y;U(}|ChCTUo0n<eXW+gs-hRI+k<AB9B;B&TeUiHC6_IE9Tt{B3YhQ<7G>Ibo0Zd<>HWrPD_fx-y3Mfs9PsZoH-i&7fRn*_kK69a_dhr|R{qsM0!sU%d{Lm{tX169I~5*S%_#4Nie$@aauT<EB)&<{cnD;<h(AG9<X~&t8FY;Q8`$&&UJS0#cZ90&IEFV;m~~ps@ab0A@*+OhzK))Nr~5(zu~wZD`-MDaJRqaN&sFhxr9#S&Q-^xH+0Z^HZ5hpIIRTg*v8td%9M*YLdA4;#5E+?qMP6WJ@lkp*mv78Bi7z}3Fx0V32Bva?GY;`<*zPm*u|ii=Z!NLl?orfrZOiQ;CSM4ijF|OMW(*u@=0CWAD_-Mm9>ckNC`23MNUcQ+Q79c(wBNbUJ|sfEBdohyaVC$R9mgwJD2k3A_7zZqH73eSZw_qF7CaW4xh|l|_dX0v-%;Ew@->KgI^AJ@15ax)7-9h>_x(VTmkhCAlkM&xNr&N7<lBzC{!BT!U?=mpRpb@|#<Sjj<V`RU*cKsj<rW6|Oi#gP`4bo|R+gfa1<1}0?+%>NS6B)loW?XD@3Z)9P+)tIT?QusbrzRdlDg?pTA%QH4t_AM5s>xM4_Vt?UQ9+#X_vht77qs{4bmct3&RtlY=ds<wzjL6!6<6OOU@3p^qJB0oUD~(!SAiSE{I&9kvvkf&>q&cg>$`HctX61q~6ffLW<l1a8BiRd2!T)fDU{!e(R-fhGUeG@SluZaKiT5_x{(n)pGLqjfWtS8(-%~SfP9~n5lw^&hHsITo+VsTx~E(ZkWaP{ND>e3P7xqt{{ItjaxhV<p7mmNa56qQLt-WHz`PVl$~a+QvV6$T22_CV}F%OTV${&wiJ(EyTsdtsO9PqK`z1$;j5Z2%OsOWjI1RQF_t4RA3Ig?9pmtKHyFwDF3GL&&(u?4A}@tyqEUJNa0P#`C2KHKn^|Gyx4Z-vNL&B>0dDd<DHT9}ftRUAmj9p{D<&=Vkn!0Y?X9Tmn!hxw3^^^ZMVgrtRE@!{?ep)mgXuX>B~*cLc)Do~ZTGfHQ*UFpYVZy#S<AH9u4}zR+3%$#r`;Tp_7aYK+Sk*-P%aK!Sq0$EdtKqlI5me(^S8ZbJ#TyM8Ta)<PDWD*d=dYeP5Qn3;Ugd$CTd5m*T938it+A%ksBDUSX93hdg2%mNyeT%!84>ii#gO!CBcYUaaV)DHbXe49lm&1aw5vg=gQ7!KAG@-_vg&F1UBhPnC&`;pqg~5MDM&TV!e#kv~%ryg4ur+gFX=Z^TO=0CjQz~6I|iJy)Vw<PBDx4q}^qa<3Ixj(c=n1iKmIS89t(?o(0iIe{Q0Ae8FYTX$3ISN0Gt`CCcx4^1U>o*BE(Uj1rx3RMGuiv5MLIaF1B}DPLI1?+G=FY4Z1SvY$JVFHD+0m}I~DE*cP64NkS#<}5v((~cTgE0;-vt&!@dnzXI-wuW%$oc%h2tOG#S@bLSrD<r3_BN+)Nuyc1L_OLnoXEdott?gs>w6KFt2%p0OwjmZbh~9oGa;Pjg-Suw)%N-2'),'Libraries/Compiler/lambdas.☾':strd('c%01|Yfltc^t-=eI!Tjz>6Gj)_6x}-RiTd*g{bWpve~RK)Qu}_W=F*~O@LO5wXKVQQWXJ>HohpewSvzN_m{vgFyRmM+;bmu=e4X0*pdu8k8{uKp7#u4Kd_(rj(kRnMSk}A!M@(ZM~g*5Y<INk+0^;EGIFd`sS)ZB+oqH{0&rhf*QY(b`}g%6DIVzQ-ggL=Af_+6iLr({c(b<;PWuV@(8^kr7WNFfLl(Ql?iEXegT>P)_{v#!nZ0n>5}RUo^Td8LKeGzN@p=WXXD5Jq=N=3G%0m|L_th6RwaUYmUQOFw3Bdn6*FWVATk0X+$A3ggtQYoY3eLgaE`B}F{$Uq6**P|z&rw1?&=~r&1z;XTf`v=$3cJ;rR}yC^pnwN(Jp;fmLr<~=sfMoZ9+IW}hTvo1l-HU6wvDiHp!S%MO6laW!IH%$*fN{$j9wCP5@?Z@hty531~|LU?h~Q9jj;<-W0bm;nkzVa$sWVCT14A@ekEj~^g9~pR_Wgw9`QMD;FMaW;X#Xt4MKWSR%+;6X@<5B(DqWb>JASQcAniS4!Q$HTzZj6MbEN(?4?pPGW3v2?2clI2AihY;zFgcwbD9Uvs<&ZlEhZrmbei*`Ysx2aDCJ}1y5_PU-ErV`%6v&z-cx(%@|hG0anu?tR`yK=u1`49UAdYmi*$G<K@~3*Q*8m7%rnNIah$qxAJ+5*c&&d?U1e%uNr~oJ{O#(XlsuBhT8g-{f(P7b#deT^v3xqsRK<Mbx`)*ldb7Mx=&}GB+JAJznQQ917wAH5F)tx6&+K-bDyPrQP_K?eguxefohfVfQueP6I7Tj$d$xipBh`QKiPcxYz>ZQA#K8%f#6E$cL^|j&v_ST=*F5s&XXyI)*lMOZnK}*GXpdvAEMRI@UcQ=$Rff4LMh3#PL-Gg60JaL^0a>S21gT>N!g5$NSjF}I8C$)ZaUNKUb^!=fM{iJEZnpM`@s;rE%V`jZY5!BOnD(vl!t4s=aWo}TpF}$t`#F?+U*V!i-b%~ro*(?bL&%+V5=|Tc(qM?4boAwW*e+XwO$Qk0`H71$N7CblUD0@$g=0(tz{e18>z4*R^QINcZO78+=*#$iyRp2={S4M?NP;i5y02$m)Gl8An>b54##siUTlmn2$xx}&#l+53kdWbI9_i)eLjZyZGzolcRA82c7@>eb#_kFi+&|uEBan@Rbo6JL#22uq4wm}$yyYrygw7VpOg3J*jVU(2fy!yaqr!VFZjdl9A^)L&4jYKa?GNlen!SDiY0cWs`V@V;*4ivYK?f@AM1bFsI^42o`DwlPeJP?p<T7j@_j8)g;ABHZwtrq0>UD?|C4?&+xpnieFtpxt&!?kBJI|UBv;IGirBtc8%nM$B^ljjq1b?KPlzs25bZspr4W4ZRN+^wwl<3`>rgwvuCW(H1*%<P?r;iohZS>t*O58z-7|M6ykn_w(A+*~9&~)?dW8RCrLH!l<-C{IUYyid#58bZhg&3*A8ss?pVemh>Dw)S5)`D{*9fD{ak_suI29>u7K^cIc8k5j-`fp)KJBG`EN=(wBiaV>PdpFz&%NPj05#UtNjNTu3X7A3xE+;wZy;!gDKkd-W)&0;{U3pnK8j|(M2=5H;#bBDs`+5&MbIKZG!k@0IdWN6A<s2vPG+x+83^-+$wU#VK#2u^eNGlFufqs;F<6GT7xUx$HJiRqbXYe9mh~6s&T6w{i$ftDs)~@`jftg-GSLq>J0?vMgGPt%Brsw$RJc#&grcw9WYOo2`d+D6#R&&$Yl8j7ej%pGwV$AT_j6KRn@?BAl)fTxKspTh6m3AL7Oq}N-9}br)hhS{i-KpfP}qLkCKqvn64iH(D)VM6osIcW^Y)fOARC;92Esh#EXdF^Eq@o~?@Yt~0YQFKQ7eMtP72DqBy9}aM8_f^MLe3JIAJv`+z9rK3|o3J2UqnU0!d3io01e%O;6jw)`_1d_9zbKd32nv+w$a^z3p}qa+Wg0cs5Foe%-s4Jo(HQ)6J8Z8zfBq@wsxRJ+UXEU)*wP`mr(A9rCIqq1BLXBj)LHq&hhlOdjRbJ~Y--Da;&z1YjUjZ*(fjV<+^T__J_RpUoThxFv}ocxYtUbx`#v1edfJl`OTj<a6<q=JHWWbGaOCE)!!~Qh0qN&3ziE3P=1!{{EnTHIXJjMRRwFEhGqVi7hr2dZTQDI;5HHOyj63tTlFCh6xShd{TnQiA#CB1v&J)8~F-N1Y*S;dW3AQRrWWqp#>lxftfX;w%8Ok?716L3yt3zkTeU2HC?_0^f`<Og^j4i26s#BXSM=+!FMh^6$`6OC?(6CQbpVpRK{xt5pxIf{T#gr$jb#9(IBTxW3+=3Fe_<?RN4~lN1FCRL)u0@;^OM$tNIV6bMvWALjjD?KA)%H28hW@_<`7BIrrsksk6n@jZ)$z&u<OBbCRGgeRFZOiSVUHvKWfhESBp4s}ct*I!u&M)<M|p7c>eyDH|Z?1jy8+1OciARbgSK6R)3Th!EMmO_YCPA5tU=n<0o4C@Sn{^4Vg#btKzHo2XYN*nPIBs})W|hFxGV1!PfzEaS*MZbrN9%qmiCNry|5Ohx-)8jVy#Otu>Pz?Whs72Z;z61j_L<3hYJ@+L#zHlzvD+lD~qKDW-WuwUTXYMdlm<XbcDC^Kz|f5qiOkjvh!-W}zLAuLhj;@_jJvQ=qij<m4<qmMu^N%WD}t07tX2!`YFQB~<kP89F5R6pZEBU9wXcl^apC`k_aP^lAJ)%3t+q{<h9YCw*%c)VEkTnM2&;;RB*V(i@F(~x)BZ9WXT&EVT5Y&n_uc4-m>8a?~XnbW8I8vlAr4h}MoesKx;OQN4)H`$B>jND*<iY&Ye`okgHwa1$)j~C!rg5x$Eci{LPj(c!Cfa4Jyf57o4SD5jQR7QLwMXCA42WK%^>E)BvN_n81sP-0BD^(cQPXcwWoM7T0`=veq0-*$d=>'),'Libraries/Compiler/expr.☾':strd('c%0=LS#KN1`CY$av4DXYW=e=udRPU4O0wGoWh{cSp9q4WsZ~OFL$b?N<GjU&qef|L%cAV6t`8}eow#-jH?>eZaZ(`jOTx!K`6u+7dyiQjjuWH}0cm!3X1@9EYZuWA^ux-^YpBs+SFgWOS+1UJG!Syb!1Eg6+0e!0O}~4(>Gu&P$aOKsL@Zu7cI-Fh<;8{aN@J;feBlIa<IsM497XnE!XGYI;If9$Pn?2-aeZdhTXR;uPIuL7bbD;yRk}@|;rST{en?@ZpA&@q`H})Zi)*uWc-D<QDzHaE>`}2U&p&p&j0%{okq7M4YxLQCX}Qukxv*G1UPE05G9T7)0)umOmwpDPH{U+J+H~l7`gb~*w?9QlT;TQ^(%1RWDU}@LKEHYW24kM*_dRy}CHh#c5hs(Jy6yYzmWK-DM7QH%pn&}pIJm0$Bw%zQLB-QFU*P#JeJ{zJ3{DtA|4l!imfj0=hki*v8&7eJR4YLQu)at?<%E^fG*u@gM+%m1(U0ge$)aaC-|F_>#X`1g-M|T*b_bQEy0Kq-%|R0H;qAMCwwa2vNx&oO9=T-~o7?nsW%TsQ=;_7iG-KIyAPSRTgK2r>WU%guOUAUm7dFE%&^GuBxe+dZZZ0J|lZ$_5R{S)!xL{fQs#!4?TU@j(E}9jE*y6dU2#<mYkJdHIJwGas&Cg$=JgVQLxTFpWb3d#h_nXHTU9jkUSt=x%N}`2X!@#3sMVcvpn@BU|Zxd;z{O6{T|En<*<~Cd~8Ze{(X>+Y+nd`wc>hXQbUkTTU^+#c@U;K}ns}fhX-By*|P9o7Clexw;;G4r6DGgw`jD7WgZtSI2vuPE%7voc7)F~!XA)1M4H1y43#+}r;3@x7Y$h1Sso{0z&AfreU^NPxSkV%1AqNL_mRBB`ZGQASnO_C)O&|ZnF^JG@RPkdn(y+r259taIFoOB=vMEEw9N|YyLOWf6*hstBuU{EIdvWkBY{QAFC1ZEIUTDl;Or*uQwb8Oa<FbG07p$2%LZX;HQ{OJSu+k{H?jpbvk!g)ZyB)mpCS3;d`=!iPXVMU27%-n9TF?=#;_^>G_rp4|=3B&=iBK5uj$)_Hu0*6pp!-7>a$It5L=qY}imDq_zBM^nc&W30p5rygL5PdibQLn`Jou^mmHMNUZr3j;34w?Eq52~|Vk{TxKEN;Q>*N<Hc*_#v1-V&~IlW#X_$+o2LLBHCe_x6kF7ylP{;d;;!(%zimEr?z-2&G{VKJ1XyWD^1zFW}+)GMQDi_htGpU8lAus#6(nR(brB9gzrkSi+0iq{G<8ct4<*1p+%*wg#98cz1y4?R858Wf~)dcXht>`bq-=PzPhj;yqj4PT20Odyd_<BtQVQL!T(pg-_(rSxKJ;dOGl$XEGr23*qEB8wxS);EG1S;^TQfUZYRunZEv&?wRwe7*E2q@0v63yw&!-45Td(WfGwn$85vC*L2G;4}VB%BBxzMM18yHG&`$`F8OSQ>4kV6KhET}!%zPy^IEx3t*c-Iu<eY>M(kwgo4uabSv3b&v30*iM^gM9c}}m}LwJ%9GD;gQTeS7JlaZ7gw(|<8Y|`3|r57<v#VxT(x*$f*ALvu5p`^_PEM4t&;fk26ErOrL!cnyV{m^T)n!X?NS5Jv_`pRiZrH=coh(nHRf;;@%$HR^7;jR5x4sJZ<fNmib01X*-NPEMLt>MG>$3SApW<nAb<lRjhjEoSrOaIKnA%mYdh9n5UGKtenOCS<)3pfu(bk4B`EeXVF_Z=CO2Xuq0<bYn3;{`S9cI<@9MR2)HZ(G{Bm+9U_(S@UXiYY-YMsHn|9{`+NH-o236uDAVGO!~0Ty5nWL<3va%JMg3u_BH@Cc7t<>Bo{Wclfx?I@Ch@bEhoQ<fa0y$A6c<RfyQhEioJ<gL^6gxMgB0f9qg*?cfK~wboN-91!k2P+$QbOa>g(6?PkDGf;3&-)nehdjZ@=nVp%+7%_^B<|<E{lWMmQ261oVv_>`lWncr4iP#RnBJn}2;C|e^GBBt!f%eze*4k%LOn~Y%@lZxN9se%Tzo@t_7Vw1D!8&Nd0v1E%wuwr5zGX4Hr04TvN_w1*q>8M3yVLhTPi9HvwOGso(5M_9yyn(>OA9AmtP~wbvLlN-h9waN0Tvg*Tvg4$r^Wj$m2q(#nUo;TnJ$Lnyy3EP;$bs*(+eBHTYV<bwAV2DqIEzdF@7L&4^ZJ$2w?UIp|@s_h6DNl<zTzMW>&zfB2YQd<RDOvN;Mbwu`BA>Z*|;=03b0SInHLqOw4NLm}XnCtBhcVa9E=-%*1L+9-T09=JyZ@9>}D0ob3RItTqD&kFk}J6eIM4G>-_qQmr+G`eiMzYDdUXUdFQtt=2J*1;Ha`|1YH3e7G+WzsHRK;Q=?Zh$N#p#e6^_bWEvH*@ur)DUAgGN7>une{d);Dkh7mNVkU|_f)5O+V`BWD<Zqo?Rh~n1m!!@pLcw}bfo`F;3^*iaTl;V7aviG`#$jl68L}$QCUJHSkjEI4^XX6YB@C<dF6h~8YG#^oFqu<dNCf&P)p@Y#?eM)Cc;@O>&=SJdRmEu=Otk+oPwoJ;-GavZ`ouWEdoG4B5I~%m8^2sgMbmyPs-$1kyg`M7_eMn_`xm&JKhE1ZbPRFjpSy5=LWqyU$S(@Y#%OMxzp(Pyp|iSpY_)ZqHUv1E*fVM5O^u$l*A!t-f29)d3D=O0{A0+MEC6=7;ptfB=A6!LQOhN18E7wn(^62O?LdGqc%`t)xdxrNF%?G&?}B+fx}fwwI&z<j<X%a4GH2CIqu4F4~;p&kVR(2DG}<$8H$Wqom)jalC8M;n5k%%VtT__cC}>cf6;s^l4A5dK_-h6<Z1CIm<Ka==!dMXk%Hyju#|W?jgso=_!>Fbz>+)@AMotZPom7J73)OcguiXuReJy>1YQ8M`tC66OCzJr!1`26PI(fEZTb)`w{$mUj&)OnGrU3%GwPg2=}*cm^-tD!W$ed0ku7qDcOsW8%}4N&O8ppTQ>v%jDj;KXtL!JTvoj3HZ07EJ6YMV7c1sTF?Oc=gwVn#tSaT-6&X$$fUhNqs{O<S7U<4Bmv&gV(*z{%|(R-W+bw{m|E>uQUPy^U0XdTG$wi<zU`qk2@sw<PCk5Eq1V&45czq$1<SLI2MbiyQ)$eI5FuROn%'),'Libraries/Compiler/tree_txt.☾':strd('c$|$?TWb?R6n@XI81`wVt|75c23AOuP=l#0y?_wIvguBmrQ1!|ouD8-^nysS3cZMU!y>g}r6?6CVxP`G@t1h!l5Cnra2}G`GvA!^o$s786t-Y{Zs9g{UAe2y%+1a(x-O-bh&i{Iy%KhsUYJm3Q_EtE*&0|Zm#1s9Q^neXTdGxxckznybf-dx?l4;!XXkKRr}R3>6UG`DpSMWNAH;#+ZX#kgh<qLi>EHl%;WsN}2(F+-kVe;HB<ctfL?i`dxxvU4bJ2?<(mzyo^+Wr);Tpc0?bdS*`>HYDAlFD<=16HbEI9pyat!fkghO}<-!9qn4U=QJQloek4Jvf26BC3#hu27aIM50g31%g;7D=z^uJlAAWlhsbS%*Qy5v=`43R%JIdPDI;<11Ld%CY@l^!gNOV8aHS!XA?}ak~dEjO$@aidMDY&_0=giYQpX*kxdwWxZ~fN4|t>??Fo{N*sq&8RKEX%|Sg0gJtz`2G8isY?;D3oWO;xIjB@hOY@ZGZDv1uEXf|gnf$weP5W*q;*9BQTd)uBVc*94Z{fS61V2Z?O(0u>Xy~mqeUE5U!5j^`%Odw5=5ESjplHVF0qjVphRsLVhF|@hq_V0Zm?nZ!j|d@qsG8cYRyeJ!Jt(>*ES7#^taCV}Z5%!%S5yO-aN!9N59aNLf#WuxZgWGGpTx>fHqyZuoftKcp6|QOu(Q0Hj1D4Agcl1ee_uayT(~qsLY7x{_L|Iqc#%)iW8J+P(F|AJHurq3w3*Z=aD<(^0Y~tOE=}KaOY@cDVg&<OQ<faP5AYRs3r=13xHVyE&2bK_KTkhPz*wBL7|x}F68i^L@$sM}-+&3zZ?t4OF>h*VOF~RP1sLL3dQvLrSJ0+o`U!J=2S4FBZF@B(%E>=3jezAFbjy*4Z(x_|0X7+{4QwK@6Y~`74%~smfr^7-v_#ycx){lj3Tfq1D7F(_c4WS(5j`))J<c*2+6uARc!ck?C)V(lPR8}YP+)|Q&$FMV8a9>S7dmJcy)u6Rn7DU2'),'Libraries/Compiler/tree.☾':strd('c$|$?O>fgc5WV|XEII8|OO&KH3m*arA0llc+FKM^X}tkU#*XZ*6d$P&ha!P!K`IC#Rj5}EAUGfdhxud7t{tzFs8CChCNn#4X5PGAj?eLAw0EETzP29hjE0Z)eV_A2oCMNW`CMiV5RaqeU>ao{1aC9|KorNjz23dS@OF2w=ieFhyStQV@E-PgEeC{g4o75;Ilsx;3}E5}a>gj|4o~ryA7=iOMERLIn$7sqEARzgiY>grH~11<htU^O(lb2AAKV1V{)q3(SQ$4FcEe*85HwZoi2hQkj?$P_K4Zve9sL5&@Y@=CoG7NF7M)!ioYz}o8YzqoSPh|`?bIBUdrYl;=cdE2oJZ5A2f>t)_Y0o6S5Rq!6^8(}0f3O=g<nRQ<ooH71aKT4OqKMP=Ui`DNQ1n_Pi|Fsd7?JdER2Jyv&9unEkp?g=37w${-)3={;?uhh}`ael|b5YK5k9^Mcyn)84ra5V!Ft^#B=H(A7@c`D0y4#Cb5JGtZkX&XFS25wI$#3SO`qRaodIKEv<1#7-drmuA_+hay9pkAws3OKTqcL%Pa@;G+E@H?o_1m(7Q|bN|q&zQeAIn*xOLVF}@`wml}Ykq{};R6qFa4<=w9jq(#9^ITmKja8szm_;fDqIL&C4VIVV8oGv((HcXhS-vYf8!P6C2ds03Gz5al=K|89YMpdniO)mSgjM=uW6lD3vXs?;k{@tSCB7LGcFIR48?9j@Ej-@NHP9+BrnN(Ay(&|a;l&EC3t=X!LwM}Df+p+ZhrggFZ>5~-y3O`f=)f3r_6+M`Pu%VucB<C+KIVIW'),'Libraries/Compiler/node_types.☾':strd('c$}?R-A)@v6u##vR=%1^w`t(g5*Gw$Q`LzPNu)>=trmMttlHRJFYQWIr9dIj6e5B#0R#f$LW4j^t*SPOl5laP-t;Yafkx^J^vs{V-ksf8X^^7v&Yts~@BGY}vnjZhvQe0w$$6DZsb&<*)r#vGIXidX=_9ZJkH&7_AeO~`eSUK+JATKq2uW3)>FJU)@X54mmo2WDqULm|GG&))gqkFkqLi9kJv&Ayogn06qu-!(G6B?ce9tOW+_LR`0JKWg^6aUSqk|H{Ln9-fWwO_YGPkYa%;?Z9RO4u0jFNy(oZ&*zPY>d&4LE@XwD-@8Mv58udySds%R2=F=HVCECs&{ePv9rBHb_!m`qzd~tmahl!N6ZAa|RCwKSf)Pc}0jeXu8k9KSJOk9Hj?wZNeIC!yA-dgI8*$#R3uf)IoJ2)xx)IJ(24(WJ9lh>lQtSaVAXTIh+$o3g%!Jwh0oV)cD9yk4%YkK!g=|C795wh0<*8zIahY|2Tx;%Klu(n{{X8_QbVG{-UpsnOcQk(T|c{p32*X3`qKV_8zHucJ3=z#fY1g@|^!;*uf~z!x0>lsfusj%#IKRgWKm&Pvg>nMeY|q(yL=84<?OZb#cJVHDDcHnTiZIvO#3d7&ZJk2df0mC?R>yLfDa-0ZXQe=^SjqZ()L@YUgu;-U^uzo0BF_KQ;6C<8tFcibr472mX;xKzIcTliVX&@gm*NgwYlXiARBpN?c$E&Ulsbs=h`sDfj~SH{ns&e*dH_^pVjF>8ETXU`aXTr+G?#M<Z|dp0rYJqdqsNm$GVAC)X{i*wx`g%dRe~w+_ee!LprE#llDH?E*7n#qI^gIuuW1D6V}7YXAQEVyicHm#dq-2_ocEy(g_0PY%MK$o<W({Q<3qO{~j{&ap~!#fHpYU9S6TMS8NarrO7|&Rbltc9H?$4H6LbREMUhCkfOH0f~Uj%$7stC&ho3s3%&rufMU~sGiJd%t?>tqz=2n*h;&{Ddw_aiPJt07qCPI0@+%K$=3TE+(?n&!R)b|Q1Wrll1uu++l_Ih9#eQLJr!OZJGDsQfm~bBJEqOfD_6V7Nr*$G%GY&x8K?y_0#d0CBM7^MumDcsHB03d%yG8EcgG3oH>vsE_a-loKiIYK8h(&>EN0mksb7*dmo<Ej<vZotQG!b~&(*oKB~?#*h>GKDqp}-fp&$<upm4w_>#)KYM{;c@CChPVbXfHeuU?{Ld-^b`qKWjH1gvt-F6pph`&9zg<udR5F|8z8W4h6YmziuN?J^VXgzxa~7Mdm`<^2$46^@Mr%4}cfexzu7z{29yVr@&^!yZz5x%?oBj&gA~l<BP~Bq8reBx77E<{X|fT^gd7L1>a;d^ely-ovq7X2>Ykj9Zl%93j;JAHEnmb1hEFu4e`wE7jl=8{k!*S&OC05Z^KEnY^LOMah`lBib=8Gt>67`%@ttGhU)>GCc`2!g*Y_sG3blD$R!6K=sKA#IFe}@8m2AmDF?J?rl7e-osr0jV=KB5fwye%<CrrRcx(L+K*xm$8kb2{<Y2tRc-txuIb8hCj{O~bbH#Zs;ed%<8wG|$Jpl=Dg<YX)6T3B3vd<y=${PcD10+&r=!X{*)77l_zb^%UbjlD418`y>070u*OirIu3d1hfa{QLU#VKMZ}*-q<G&x@i*jt4Z&Q-!PP}fsN2bI3Jjy(QO{Kv*1fe85m>sk33|-HRPV_K>EWjR~-X+}-az=T75dTRLtn+7~Mt+Enq}!kSqJ8)#XSYaoAO2z@7a#r+HNily7P&%5Cz3I6?2G;+25yB#=K@};kt^20MD(T>UDedu1<UvUGb1{1a!6vYv93r<O}|f`h=)>YRjvza#o3zQOX$O`yO~U?bBNaYE8*T)W@vcyMm94tI?g5j1Bg~-69'),'Libraries/peggle2/gram_tools.☾':strd('c%0Q)ZEsY^75?sDF}aeZ88cX3qbkyh+lm5JQJZ3cBUN&@SL^lN^%cAKuI{~V)@d3AW9$k-1H>Tnk`N~fO=Lu9Ypj4`@?q3Z{m|bK|Aq7i^qhIQZ@z05zclFzv$JPr&N*{lo;fo^#iF<}asHRoaj<pfjfu18CLM=T>z|h_##`-Ry55c`<J7VkV_XhDJ3$$nqVy=K5XNdlv@erR-SZECP1x!=t)Shk$6;^~{9?BkJIx^M)Z<s+wkG}}HmWvl*E`cQb<*P_K)NBW@)6azRej^^DHM83d?~g#&{oAoTP(oW9Y)1vag*+x!?+@VTq)wZ_#!7_VAk+CLVBR8*QDYibZmk&>|xApM=sLti#xQ33v_Yn4RM<?I%!Xab1ulCR4X*va$~TO3zqrgpBN7BN#%Sg{-*e*lPYLPRjPHThLY98(70BDyhEh?%gpGOOaehOZWFs7i}iG(wEcZn9U|~a$W=SlDZ@h!@_>n!F6VM3TC>1U=*DxQpDaPrlc|g1Bk{FZP9~!r)2W(Vwbl33SdHbUFNhWKHPyq|s0)$Rh0q#6coMYff<|2(l1P<&lAj>xV{!T9iAkCf#zwnSQQK>{^f!U;@^My!KgJ_BuE%kx1pMkW9oKB2SxK8?n)|8Kzoy3^0gly%%JfaW^yvS_OGz&OIGr`l(Ork>EC7prI*XQiiv*$Z#S(UXC^ilIgZ3mMoz&qoiKJ3QsXw%Rn_d{jPUOwF5k&}1fD1$S!>aWCCZ+0U>U#-$Fc>5zrp7GiG|Z7IwTuTU3<-&;+Qf^9bm@Ud5(TuT?b1|d9Q(r3$YO^VSgZR9tUW9~1>Vwy^30et?Mv--I5t@m*TlvTgp7$f6P6iMx;aF;F5Va4<l(3hbmtGnCPA|aOdSw)TYQx>&26!z*M)f_-Az27<f0)92Coz?G(QdkV5~-t5G|JP?5<?G_iG6G9~7FT0Sih6rHjcMrD3d*PJXE=pNSU-U{aj%80xx$G1#81t~h3Gt?<)y0CHl1Xhx|zFzrldRb+~qp7DPCj%E3c7x*13^826qHTBS-{taC`oH*Se@?tOWqk?O{N`M4^J;;>fdRN2Ip93b#Lj&ZvIWUYdz0>iNZ=Ngcg<O8!teVXbELLG?Hc6Hy)4L?Y9r#=EJX6ppwRqd}-3Z2gCa#F*%%FQz1;Mf@p>aukUS=^r@Y_M7-X>8(dTZ8eyC#+%OhvU!ILV*jOLCl)BzU&&$VG3IiP6-@a;*?dQFe1r9S;Q=gjB*XX<z_Q4~|C|1g<~Val?A-ChE$4CQA0+yhbuDdul;FxsadQJ68hq{Ior!VpM{0AoeK9niUrBfhJKOKs-u%(yIGRo9t&gbn6#Lj$CfxxBH|Req=Dc&GHj-d9?tEutM`e$CK935cMJ_nhnCZ^iW$cMLmpMr|tUWwH?0l{O(+gee$gQRz36`ui2NgOw0v9hNa9|evwh?2Qe`kr2+_EO-!J40uoyBEI|RD-y*}&@!`l~!+lld{q*F?VY}(I+m0FJ%m!^Ya;EE%*C<*&-AbgIue3w&uMig>Aj}nOaiD%OP&u9`kGY6tIqHu*8L9g-L^3jDnXdid;}r^2<letPM~R11qvz9Lw>_%A-y1L6pju(Q<3w{|%MIt#%}KJb<w7O4ECcRW2M2yNC-1NUqAjE3P5_Z-Ry|Gm8krSxVv-aczMI){*wbL;2$qW)Q)Xwf0n#^sR5+;MPVAMb^mG8qRVV4C!p<buzW0_~oR8IbF0iG-2eMxb=Ifm92XsPM-u;BIyq|R4*9`-HbbTb#P6fAY0vlYxahtSv_&AM8y}I&h2;F!Q_ASW|mK=1AE~XS;9;j5>LrA4=X`_`v544GC?)h5gKv6XhW&L4t&Yy8Z2f?xkBxvAItGMgm1!T~bGNMk1sFT|_{h2{G%yV+X<nluQ7j-xQvD~H%64_|I+jW6s=8g!`Ru$}$1d>-k_7=<DtL;~@Gka33QbSLCBsRsTv|Pi&)t}ZZ?DWy=mbgtbijk2KA|7LDbxtXm^CUi}Bs+(S33+I$aC{fx*&PrMMqA<%mkYs~Qg(*jOyP$q^A8^Kj(l!W_1{IYp1$RDp!k#2C2=FE3FR!N=vTo63rWu-Mnf)(+lMswI;My#m?z02(!6;+S`lB0MZ=?~4}<U1sd)$j0B>s;GjU!Yk$Kl`wc75uDHHXIr=z(pzAUW)w{=^u6tehtb7Ny;CyM(?{sU79vB|sJ?>!qn|K`N-k?r@M4>oT)Gw<gE&%@_Of~ESuFGY>e>&EZ{blCp$7r>Fh7jhhZ2U-2(qz_El$jjJT@))e%&R_|)jL@fIjf!=~K{rGA1PNfo&^E82N#<V_PsCd0k*`XXF~O=K58Y1i2iJ+idNd2gl+KpXW-N_t)?uaYO;0On1_0F2*iH!Ynl$DOdrCjjQS19B_dkZeyB0oi=EtQMro;x@NqDYt*VbniSh|TIS+Rm0&ZsxUu3fg177rj@eUKbc_xOJ==4s)YP~A<G^U$WG8YQmgQ&wGBWEOnSVtZXirDPd0OKLlCBa8V;y&hr$W)LP6(BaEmnD~(mSfX=D=UZ7WnLwTn>lX$KTO0{9zJIc`fmyTt@DhxZ8AR#NUfX`SILt=b2-5TrB<)Bm!~+FcI(qdY%kk?7F_EmVsgk%wZNT~^u$;g##%vm)($*W|Z_=geK8m5W{7BoJr1&&6q#pQBoI2&4{w+T8pLZOZebv_^tz-(&@F~es4^8+>KJHuUqJBeDKoLtvkfg{*X-i#$ttXU6n(|0fR>d7j!KZmcS=E$P&H0*^bxp}Cy)CqODY-blFi!Rt?+-0rq~Iux-4@pkq@~eo@wA<cR`74}%nxH<71+wes*OG7F2mxch1A^jh{bb1vA^%h)Z%@+^ez><Q7m<K;vhixYt(I3?M(XZzFpyVqf!S)jlYgysak|$A7r51%J3UAYU=lhE;X5m`Dyo5Yj<JYqOiM%Cd}Z7VQ2(U2@u!s#jvwJn{|OX!htPu1|{vXFIuelikB@EAnN}r9)P{0pyPhGdH=hoH{svE*8X$l+ZXWn6#h0<d+Wva!omehU-(3&2jZoHjz*dHHFNTA8ASj-*yx1TI60SpfbZ7H`y2ER4gD9RX;-K'),'Libraries/Ń.☾':strd('c%0Q5Yi}G^^}Bz?FjAy@ovF396C$m&5|$GLf+mq`BqXz1ZN_(<h4Jn(GfCG(mEsL<p#{=7PE|<TID~`(Rj68lDwNO<SA6C_>|fvyaL#?q+<WKlBQGSzl6M|w&OPtf9m0Rk-@W+8cSx&+XWxDO;)RXPR*R4@XT!YJ>8HExJfzW1(!bPBGD0H~hLqAsym#Rup>&Io*MjAM(&j=Z?e7M0KS@}ecl*68=<W{sX&!8|pI%`>I}7-I{yzVL{}X<1@%@E3X=iZrfFITu0yuz*Ea~T2t5t6x2_Y^Qi~kH)6+qjp6SP|0UN;9ifs8x+kUxp?XfcjhgOB(p{D4Yy0;Oh9Ln_kYj#!|)^Z~@P0GJ6t@`#YF#kfhk9THQPWQ=Sz0f3O#FPtSn+b#Y<1iXL9_Z#Q?Jw`!%07_WU1u;m{<!g+hkV(e!cAlq_iSL~w-&Bji>FM&cMz?BB8o9uyN{Cepc-aHIQbH_Sz$;C~;n{QFCucz2XPQE|T48a&m$$n;sk5ZLduh8J6j~Y92_eIv+Y3tREiu6~-v=@LoeU#5`H25k@m&FqQ4mxwma;+WTc}RLf88J_vhmUAL`KK=K84eJe+uadSiZ!S2mLf4;rJH^p-_rJlJx{M@fCku+7=0;0Ph=wfcUyO+x0UY?bQpjvsfuCWmul>30)wvnYt+TunKxuZI<M;d)pJ`Z}Q)01hDo}Zg7&Yo>!v$0e_eOgE*?tZvnl2Mc@PPOVVw3wA@PRb`5V$S$-w8^}p3M>`fxsX2~=p@OU}~khc*ygeOL^{9)2BOJv<nKyq}?UOx|<XU`U2^7)<4RdlhUMOOU0WLZ%ye%WNP=OxRErR-&rrOZk%YQ(R205%-=2YVjpaV<jz=sKn=V#gH`#D$dzo@FQlCyN$sz*qpr4j{S+ptnI8Km%FR6NL81c#s19sh<x;ut6@61wr>~$GanffN(NM6+J#`Om`l%)6$XV&AE0;9Ra`%hYTw&FD?fBGZfGZTZ0>0B8xveLUhtW3CG{&52G|1q^$96sDW4n#@*U%Y^GP-K#>-jwas2Htu&L?jitp>#R?L)lCkSr;+gAE@T$jl@peNzBLscXQRZeq1IQTxLX=PFgmr-~dsXBWv8o(VAP5}3P2NdrEQI;rURoG+d1;~XhY(^HlVnT34b_eFh{|+-pMQYDa>^!o|B-cn*(`dNDc+bsgu+Uf2K_<8I(bywfclyBwl#XX)E*4r8es%AgQQ9c8@g0Pq;12k%%JSe%iV-&8mihL>-EMUA&!9YU_-J6p$IDe00LBxtjk!1L91DXZYKaRSxJax9kD3ptAro~=|(X{DAv2O%hGnv0I3HS4{83=Y9L_NvFz;jt}rifp`P_J)O5?!6frz^)m2$>vKU^__VIpTivxob$n+-vt1s{x!m^j}%T$qP5I3DSJe1z{9KDs)`<I%M5)8#C&h}oJb_}kqV!#Wm0UdGMA+k&vxtTLMnM@nLq!BGH3Y?!h*#lpgFM-IwZsZVL+gMUAR<7d@>+t@^(CEA)-jq$4lUzDky#YP_&sYyj=1%5ARM>by4#o{ZfJiZJ=FyFwodMxcykW~SRJ{tWX!MFDoeGEh3bc;m6*^fGPNIi?By%$T#Oy9I-hF<Xe<@T|$#y7GNvOc%6{!&Ggq)r0gza=}Id#IdCoViQUJz9U??mNViNVsdJj#3&31b(jOFWL1(shVaGb5>0<@KuMDa=Bn5-Jd>*eF)8Sa#aEPPe!1=n&mbxSHX08@|?VV}iqxje29N>Gzvy#_e_6jrppos)Ri{27yX`k<F6DXk(Ttk?`$)z2W2@mu+3AOp13UDk%VT3g9GgF+DpoMwpz<jV0OA5|VcASc0ekN3J_#8Dy$=7PV;P>smC*@Rezc$&m;RC|DBX<WevuXu&ukY+aC1_InUKw8gLMQW5UJvnsFiw^QpcuT84<$|&G;cg|orGZ4N|5VZ6L)yPm(BhXCV<~Pe1x3Z)gGa|Zo@lOw`p`fiqZY(Zm#IoVbiDmxMRhMi-kDuT`OLL`%S^Aim3rcvpgla3aHK%L&4WQK;^fP1dW_A5I*uD-r#T^1GSU6GAU)vZ8_xS)e5)UAJ*`1v|X)M5vF6e=4cvpc!^+Y#qZa*YwzUm`Z%T|}Gz_8(srF#V@14JNNJuMfX^Q};9>E_d@qFDwDL3YZnvNU7cg4lT8Y%b}s^_s+&+o?~hLKN=sKtz6X{xwsh(BJyKS43S)i+<M};+&2yNjfKbky?2;xl9GybVAyz=Dge<n@<4G9=4Qh(w8oqPCM=Ox0zERH*hnn2;3w7nBT7JA(Ob$BPL3%@NkpgL)W{>kA*L|-LCXm)f)q>D*Duj32#)Y6^Ro6<NTz`n1k}zMS1K+c`Q&Kmx`Ox_2Al(z~t7XX_mJVTX0T_oYJ9B>QODr0YCl?|J{_TrATXu40!;J1(%{slqS}!e!Af#lNw)vF#R91`W(qUtw<q#b}6J&rI2+i-s0KaGJ9WB8&TzfCa_$Kbh=5-(g`EqXi?<F_hiF+i{CM)1Xu-(_(T2(f4-E&RbJ3#*0%;}f56gwuiy|69RaGRvX=eC!`I0`J_;OXxM<ErDy4XlP2U5@93gFY`Jai{j2&P9Wv5mf@8280eF*2ZS_jVm^ZCI(KIqis#YkR=I{1KpB}#)QxMu(+ael2jWL?{+4q5jqLsqz#TK86`3|`G)N~sUrP4U~hK_-#au~FNT5O@xK)vmBJ@kK@pH-P*zc{XJTFRJnf{whJ}0$G-70Eg1k72M7yLi<no7orpvoAlQfK}nl~fA0gWZ|Ra3Zk@>R5BJ`O(b@*c5qF%-G0vV8jd}y%8yb8sqSV;ea;O*IQ0()+@TdA4ij>Nd-IS-Bn26rZSLTIse#k%6J7DniYt))dT-dAJ<#)wi!pHn?{5Vo4_nY#&011S<RtK{1Cpw$RXV|KoDkr)EM?rxA0sW4zKMEzA1k|`R5IPqYEE|n*5Mo0U=nX=tHf$PC2LIpe?x^k*tSc0TgRIv&osxCD>*bwBp0Xp$+wo6Qy_8xw1)M(`*49GDl&YP|rT$PFkl0yWU)v;d2w`vTE?qRO*V;%m4Vh?SEcKYspyku2)dwbOJ+r=yv~OEOPdlCzLcy3}Q7H}_Mx0-xQD+CI5FlAJDxo$XvZ?dgum;DOPH4*zBb~G9H))4o?J$SqqwC{4pO23|8XtW&J{pBGimv})gOKHjM%Tj5PFN@5@^U+*Z&@K6<@A)_P`h^{{(FAQvwJt<f8g&_L%M)}Tn+1R|AF0&VQ5$Ix2^l9X6^ziJJOmLmyzRv&Q!vRtA5bJIx2R#hsGEs-5$$;G$BLFA*9b9BHn%eYXVtN`o>{Iv;@`kYSNgaP@i;gZQJFz!wdq&zVA00!SeK}N0}fLYH55SeprQ8E7eF<dcp6MDvP{^Ym{h)vX~cY)+j);^p!9O1l8tZP?`}f4>K5<=aYL1S*0D}&mZ|cbIMTeAa*jfoP4MXt_ArO=i1q`t#d!bFFD_6wTSuYCc1s7BFO@l6FGw_Q+yzz{FuMbf5o4OBy)&gFkNP$sH^be$9=reAHtwnUV{oCq;)Ze7HO-#wGy3b!g=;)dj~E_nDqNQ=-89LfGqH{ot@CUSP89XtFsqhj#i>oAYkfpaDW#rEc_RNE=OV'),'Libraries/peggle2/main.☾':strd('c%0=uYjYgOao_PP*5_i?>|uohK+%k^a$#tYl2b7s1wv-3&gZS=VF8?Yw|m}O5XVSlQ4hkBELoI9QnEzRWT_O=5=*k8M5a_!T&1n(U*v=F1M($*Ak*D5JCEHx96-=gDrXCKyED_%uj%fY=^3)@#q5=nr+&(OAAbGAv6CkjmwcbG+JC-KbG_AGd?x4(nd`Ay&2?Q5tDiW@T(`y8W6qr8y6q`e2_y|islO5@{UF@~Xq}+57ETN&P0l-wDTjZ${Xv|hP7<z$BPSU0A5-C|6An@*yPdt3y$kQMEByBZt3EtX{V6tFi#L44z)yoSy|B?_y`X<)IUpdfdfD^Y8`*Cg*>AEBvga9pdMkUK(Myh~sN40<<uzW+u4cEgHyBmA&RllRb?S8|``A?tM&9`bFTa!ho-<(I(Azis#c1}&@^8)E$GYCgBNSSrws+oh#fLNUHmB;YLUh!~E@yADkry_Poj4-8g|_cx&oz(7QRs3UmYPe+dZ+<-&2LcQ)N;52#J-+=#)i%8Io|98mpDceaYTJ$;))~NJKdp!5U4VIa*|G^L6UZ(RVVHC!-PvSucCVAU$15l7}U_plQ3ORA_t$R44C_dP8!E&oqa=O(9mN#1m`h{r|SuDHlb60FB+_%z=`tJB<TB{I64<5DG2Xc_Gb1#ki?>(ANony4+cYyuaqa&`Y?M3Sp8o15l1cT_5FD3(#!B2@b6$a?5;+Brx)>u)g)dY_}wT96ZupFRj6&fba(5eJ6oGq;O|R!YA7A-cWFt}LxEF+DfDJiug>5j-?V1i@X~d=E6k|pG@A~q{pIQvfFAaSAv4;!God?^RJOZlw6Z#@Gp;Ou&c0IbhrMnmWOE*}yX`G40Y&AIIn_CA3yf$d^&J@!4m-g>8=NCAZL->beN}TgTiA%x5Dt0)@0`s$bpU_mJ>YTbY9;j26B@1xQcu<wy@6UJ;qrPX^q;m>g7iw5vb@aW6uzGQp6dvd{NqtJ>jINJ78|eT;1#cU%XmA_-*Ra#7%z#H`;nD`pVA~AIr=j;=K{1GBR(n@6n<jVe3@;sC%8ck)!@<_Fcxdl_!B4JgdheY+7{5&JHR_mB>cIBzZBfCX9N6nb6bFS0iXr_mV7f^Qb=7R8{m6P@7F)yMep=bAJZ{Wy)Et6zutB4MMjLn$5ll)-m1CoSb<!gOv2l<-=beP{+7z+qv=erTsDvpN8L1ZBPX}1ow(l*qm-M>4gTM0Ag>gC@M{$c&R7(uj?shb1ko~o^+EQEW^!C$5+74ksN>W@W5<o;Qe`2c&1%d=GtM3J4p7ZG)QNjN?qxzhh$r9_;8QM3QKiU`5~C&Ga9-D3^|%_QL7FB^TBA8pgoa70CxVUp*&8z0;7{*z_v*TuNf+%@<Rc7rha3ZbMvbOU{|Gdj6gNjvlc5w-9v-6F<g}0!(3-1yWHX&OaVQLeUseI>t#C;^<|6mw4J~f$SKOF47?a!P$GL5OT-oL_$>d@m1PP~^hYjp_nS)_$+BwdZ%yGTr+}?ZmIL{y5YL^pD=5i{12{Ysi0n>ZAd?6ma?lLk4yxPK3i;Vkw*L&sy1j<*l&*AIq>;-VC@4vlu>x*wm5**v!ToKpayp3!nT70_U#9Y#h)q8VZ9Zh7tH*b$L7$~s{Ud%!y5BLL?Egl;$Cry^{QO1qXpxX;U4w0kc5%~dKamMx$SuKhKQ|L#e6oVz}y^sf-cBq#088@VSXso2kKn0(JBwXo^xQ!gHukar=eVRd20~l|qNAm_CWkjS1K&&=Qd5B(UL{Xz`MiCg3&GT4K&dl7l0aJ^daq{y?0lrqFg$TBJ6x3qpU6Ay7kn{*m1e$RE8jYSq{dhErXI6Sa%5=*z${ijID*x%4z^NN8SJV@sdibkeO^Y{$1XRdR_6%Peri^og#^(qJl>`7Zu(O`>FPt1~Y>je?>`~IX1=OW(3fn+e!(@a5s){W{ukKyJN?v*yW*{_cK~5RIaU`9ht|_9bC&S~s$Gn&q=0?pb#h8D*ZUPzPR3RoFSu+Y<@&qygEi!=$NW9RmxiA?ZsK5YFCG^!iT-v(vHu;EYN0yu8n<5A+I?>$A*g(Rx37Vw!In)>@O}di1+Oz8C(vs>7y;C<0`>ezz&6Rtn{e0~1Z!2RX%nx=rHI@4$m^;6keJz$CydlizeW-*M(pwJCtgkl7Ws147a@D!-e?R*odnIQP0yLENnG5`JmV6m4vlKi8xAXr#k&j@wgz?8lv&9fYkX_y}Cjk}+=4dvmh{=~Q$m^>Dv}Xu+V-4&-0WWpYqG)CibA^<~P`Kx-r3BrX*y-VF3kL&ug7R9+ErbYhh}RmYP+}<wdT$HlZWoZNGm_GSlBww2<Wo^p4hzelqcOdoeZp}5{ja%s;%`66-fBqv@QK4iE8t4z@^Hd2<~Q)s7KZ45j{H9?50SbF<PmjXl-q`B&Hd~@U|BG`2S(}Y^W1){tTtI~c4f9klB2fJpp6;>zns5yEKSZ=FK|7<GkT;Z(_H1`YRJ#co<RVdtd#>R(C2cTCf&Ydzv~@5kgsA{@&xntnea@%6)4*Ja$8^ZDaJ?C3AinYuyw2foCoFaW?yozBxumdM#F`pqa^Inl#L^)Y!+ypHr)Ud?olTXYr^EGDiE6xBQ#{BAbW(6H4|4tDMqDG-Un{y{GI6sX=g1r!HCvFvYYkYnc*Oa7z|dg|NoEgw7^>Q%VM5Ihzk2ChWs6jn1}+g3OXy0MKckVSa&gWCbaMHAqRtD%@{^X?TFf*9QxQ*TN<o)vyV#Ac`bWqN9ah6B#<&>B0wbw5|Y9NhNCp(fp&}R2+3NogvR?vZriN@F`2?ddu%u4=S&g?XPrXP7{xY(K;Iv=b$2uGwuNY3%Wmw6rWgoB8dnqy^f>k+fC9>=%Y2$rDsK=p;p$Y1`MVm_JCzdBgU(I&TxB+NCv-gmx3v?(##pwyMave!q;fK&Hfsk~yS7LejC}9y5&qr_YZQH7j1chsuV;d~E5cCh*>HkYvhSFcdu~qm-28mEX4T$VQs$>#6U*tiYlLL;veJ2nX?;p;OQ+E^Y}Q1vW(Q*DiFhb1)ULT#v6O2_QHAkdN2RT7XBGE2Xq0Bwj1<2Iao)~N93r$E<7ThEOzLR14}_`)fEex_*ZI5R8ekQ5lbXnmPP@M7zPGlZVvy|=^G9c_9!{+~?o2QkfbyzQ2P<b4BfAi4;Wm54Byu8Q?h!`{h;5Et>X~b61H8iaP82i|Fne@QwhGY7+y6D^N!v(;y7iRt5)?k7<%oRcZJanJ7sae0iV`tYh+y_ni@?;*L*+ZMyRd?U;@+)ZnRtG4@1YPiT*saozrt|;<mN+RDz*MmqWJ#Xr6`IlAtA`U8Mlv&h8tsPAScIaKkcSY5IIzPFPBFj36bWeg1!ex;UaAU_Jgw_?t~3llJD?sW*;^%XTsXN5t#lV-}=MX9@M7<P~0Q=LcXWkx1DEcu>2w4Nx@=m7e49_Fo?aGU0yi6r1EZAB6A9O;h(c#a}-@q?$zhXzk-X2VkoA2V48NG(ekmYCn;e*i$R-*UvD<#e)6<<?;>@C@|z-6h$Y)j6UhT?mL(G_qNvifMpLj;m56+mk03ozOUe0zmMSZ<x!=fc=7NI{#jF&dCSsSGcCZuLau-<>mAPwJ&#Oo!O@uGwq*de?Vp%I`m$nz`fjuBWH*JrY$o-LPEgCfU8_fjWAGE3SriDy_@oo`e8NndJ)MxD1+_D`wBsb?*S=@!lA}tB*wMb!5euxziAS5#-p$ZtGSPmgiZ1~I7E5!{a1tU+{w)rKnbW2HA=HbKaD$|V@Fv(gskp-KoKpTOAh~3Y?b)dTiB3Y>nppX$C<4b-L$8f5}%x=d4%FPiD#CtH*#V^-WBha)vHhadVM2-yU*m*Brxy>a*1m+b|E$(wWC~cNN39TyH3^<f>GrJ1O?>Dl~C=2C&_P{l)&WnYFzUz?NNeO*oXMVQr>L1NkjW>MKiWD>M1fQ78{Q>8&t0kfMY3!#-7>eu#vCiz}(XfZ7cktW}<)U~=(B;imf^IKdZfeUTED1a6^gtcu{hP+PPDC9OqW(}O@QG3^$`bu2$*#zk(Bx>(%5nj;u`hWpQVq5)J=l8bMgCVtDFyV^!rP8#19|SqS0&WVPez^2UE@rV3K%&VPhh!|#-t+-$nFOQN#i$u;Y>zLn>9hI9{4Y|V4KZ2_YYiqXx^1r0UkNONd+Q5CCe3-d!n2kl1S1923MM85^p`OWPqIpVzgVx6VXaq9;$AK$B#(hA}^jEz#GAHWu&5bxgd=RE}p3fCPzfhr=Sm+ZU?w=RzFjxV-)r2i{yeYY^V5_ZN(p#mSF<ODRXD=^cL8-YHhn)4M`(ChuIzjYjYdHDS!&aGH8-v^=af(rAS*SoRN?W42%&B3<Z2VcnV?o+!W{0mHlWS<a;cD6IuQETuAxM6mPqpr7q+hI&1Mj7;SlIETd!@0>R6I;aWIE7a-q}Vex;p9uCuP9GQi^I6fP!g~76T-HkfE_2tkX#KW#uo5Ss#^?PBony%5CBS(Mo)RR^w<nv?(L~h_`;G(gbnC85|rw;dW_c4g!aG_A>JE+r?I)4b6DBTxeDeCc>|MSPqf5YrnlU~eb#pMAIfhtzixj9Ta<p!sC{UM!inB;iQGcqk4hs=e_wa}77CaHeNq^yE*3dK0>qE%WlDwUkZ@mg(>B<wN!@Wzi+Sa?8>5Ye;Ql^<6%_8XPwN-9^yp5{@DgWTU8)K_r}GZPqe9UOE;d8pBpORY2E>4L0q`a~RsC0%u=EVy~^R2M68<}c<oq$%Y(QWz?R@4l8@1}WjvfqkUa>o#W_Y&(e$42gGX68v2DF=Z!%Yq5_;xyme9QEiP{)EeCjFoD;j+iQ@Ni7OVR;kK9=GPwZYVCr~R#=(>7gFP3)l~jDG@mm-M2yd3b*q|v<{foK|t*z)Li3|*7G;7NNxKgqELuF%5*jd&=n5ptLfQq?vxp9_3g?(=LP;r4mZrbUlpls{TM#De_IX<y*YSr0Fx0i+qYK*7%4103B)`mwz*H|%rkBGMMtg=(4KHC-wHL#|s|8M}uVM_ELW@7eCV4Uqmjqj8V6oQsd7c8p`pH3X5-Do`=r+()eO~SQPoMm)}-DsEw5uZ(+qxt>qvi1LkeADQhy%H_4$AJn#M@f5ChXT-BUzDzYOJ?<eS)Fkk-3lMp13f9NS$H{S6IzGZDTQc}UA_QcDXWJWAPWyU2CDSkQeaczPeGxf@2g?zr=wDhFW77p^S34WgFWtZYW8-<IA<b1Q5^N+PSA6D<=QpQ-^fosT@Z}zRV8QXwBX629pz~iUQ7~vA@hL;+o_)MP-3#=hlSd1fV`%qF#M}ytQ=0Rr=&p|Z&rdNikG=xu0A!K*++zTw8=guUZW0C+5?!f;`1%>tmjAViO+mgvyrk2p+RR4<{keRCLQppjL5bd0n)Z;%0Je06>O1dyq=_D!&~!LL6XE9!-ol3%PHfNhYlXa4Wspbm;|X>KPU?-t9|_h-rRPjB^yQX*>3jJk*8rz16Zn(UG=jg^<|g4EPK1t3?EIdlPXV{Dp<}hOdYDB%}2F~Q^mQ-?Wdf$F~9*#vLexq2J2~|vO>bMj|~=0MCGV2GZB@e-Z0q*xI7LN&-qFktX&px5B7M=z5PgTh7?!y#LZ){bcj{!c-EZHO0{@(WbQ}tXPPtX>x%%~SX`9w5vY=W=@njsaCNm8&ig#-=&?l)24@(h9-dZawSLg$lF`@cJXk)Y)w_Bfm+0;m4l(OM&~0{#J~NrfVJetxksA}-U-TAR3FQRCQwijCxQT8e;5%7sEE!|@!D~A8-SH4T=wF=iCScaMI|-F*<DljT-pxHWgf4d2W(9Li&<k`G+YW)7`fGta&I`NIYAxTe15RDmwgXAMuQf`Rl{-Rl@Gn;v!RNb_yz&Mn3AnDVvP=eG)D5oD0N^~wg(5xLwG^y?KAWmfP*2&K>wKpd42M$7g`)cYuotI8-^bvQ?sUL(ovlkRFV^(cAK&jr-PHGKnBDYNY5V)Lrj<Re@-S9uoA`J3oM5%ld}8s$G5^WM!^hZa`SE16nF#3wnw3Q4jF75OWzh^ATfC1MapMO6wb<4&iB>(q4tZbCs;6Zvt<o;zcVT9U<4HJ3a*mhmgVgp7Tl<F2A`%B@){nzwn!WBnhs$j^yq+gaiL8tn-^c4xeCbPM$&9=xLcGr3=cdNh_ge@%ux;EZ4wX)fN^l&>ElsT-8&a&O^wvCXe&I6BI9lm-JE^fJVk+30SKth4&l(?-YerwDc1h5v^Vj$=%I7*3o-=2|^Elg)<!kblrnO>YSzIt<B9F_D^1*c-*zZ^nk8rIecJl*q)qt$0pV-f*u%;lHP+J>gZcf&W{ZAn&j+NrDOi9pPnY3LdpRq>aLO{ALVR1c*fP|BXi8JqPbkj8_T?=`L3_QrmYuMBOd}1juA0*v~uFEKsmf(QloRxZ7#7Ofhh%xz~^-~;D^4ir3MSv)FXx_WZw2LDeAU_C5Jn{0pTMz?vALS#o8V9-@wsa6yT>Pr;dmVY|ehkO~Ixmf|xckCWh)vlEf-P2S{rA0p`C+^DOAhdGyN>&Ft*uWlZ+*JCb^Y_L>tAne{;7>`f3ZG0J3r5OP5iNS<-PW^{LhSArx&WyL0RdbUFjfJ+Pd^5ud#LME3KG6QQyC`I)@EQ<{pBb%};L5H1KAyts8Go*PGwmqkB*<{*aTvVNwr-j05}ulAw#}XE8wzpaV1lg@7)8bB~B?)u#{9FV@1g?Pps6>A(X01uy{4oz^QM&#Ei7J^d;$xImXXz~e`b9rhQW`q|M_+Um_SaFrIHRl>c6T&RtfygiZO#)Ze9{nIr{w#SPd^$K(;BvcVMA41P9agkLlTNz;5fLkrE4*gxE8@nJ;a<&bnqP4<Bf(($dA|3@q<$f=vHWaJq00|@URP6KViavANC&A)Q85YPY`DOz#F?v;qJuMNF>{ghG22kBoZ3|=wA_^#Kyq_zPmMP@2UL}rppOg_Hx>X?byTID|n@%s1Z^U)O^nm-e^iy1%CAcJSjzhY2uqGa|(O3aB$0|u|c7mAhqLaqhPM#K>2;z-#C?T*)2-<zk0u9;5<!y4fvIan}OEuP&J+7Hrc{*1^E{D0oaGh_9qWMD6ep$4?Q1rMgvbCD}$mKq-{oXIwBRFkAJb-0V<rGkzK4YN4uW74-2Jc7hGA<ar-;la5^{~8GyAuPX)$74_xlJhRb)&$8zd;_HF1-J7yL|y1z)wz`SUR<|c=#lrf{K97@Chz0Of0YW2R^T0Mhr4Af>O-l6~`OQ(1jLFeusgHU13ob+F=h5Iab4zckaqusa_l`OC;XOex0v$U<3Vlg`mWfKXBF&Zuov7(N&$uK#<-5`k>_uac`ovp0QZGlXQ8a3rY8KLaERe43-B*G!`#<#RTPLm$~1;bW)w1;8gLLZ-6UajV7&p0kzk%%T1|b9zMU=l+p$*%_r-+l(m}@l^FA1xnlEp)C^`^ProVORr7C;5aS)vzwB`M$PxeOKf%B5aEeb|^ncVrG^we!sGw;$Ono_wq<RwC6p79rcB~Jq>A`o?fk^Q5A%}4!lk?(<qSRt5sspW9c?I}<dzZ_(1AA;ufJV`1i@uzVWZ6+~+w|p%ZmVIkLC{UccZ=1|B<pJpK2POUd0fjoBhYN)ki$c0hq`NuUblgDF6ga?&?n%`ZK=ZzzdJ2)b@-IF?o`0wH67yaMH!FJ%lSfkTFe_ReO2BVx>Jo?k5N3m(VnhuA-+Wmhgzg#TAVI#L0{3BhWQfU!inQcM~^R6YgkJt!Cbq7M{z$SNx?5<c6G&=&#n_*yO}?XY0z3;4>s18yTL}cJ!+ocuKTi*Nzs9X-RrlZw_woShGXE@8u@a%cnKx}jSI|YHBWd<KO7;}YN4*=y9dzB6<%$3<s|o9{|k&)P(c'),'Libraries/peggle2/rgx_golfatron.☾':strd('c$~FYU27Xh6n)pPn20{yaVBPE6ABAzVoP2unpBFkg@U3AMOs;EC9T<&VFh`SNeWF{64z}AEp6iZsgUNOkWxaR5A(-*@9gZCyhUyxdXRSK<DRqUo_j|N@_~HRXzfF{OINkqje67Wb^(h0UVr2ixj2}(_j(f_xPW4jb1u}5dILCb16*Sz#(AeO^xP>M9?kl5*PZxmJUw*1Ia4tT5Mf}{yMeKD_sB4=S3dt>^Zt#EtH9eG8u)NmeOHTw6Rzl7Q+NRVQOPW;ARq66!P`a$NBg6#%wVabxmEXWL5b5q0a~_MHiD92S=S9-fQn_7kwpbZ<*_`GPl1E{MxM)K!247A7~~S~mI{(xWr(4k_*niZUqa>6CcvaOy*KDF9C{^Bh5Gs4Y)7{b<S+6s`3E2{ZVzWs9v*(!#s&*xaU@d<$<*FI8Ne`)<Qsf^j&WKxU(2l?a;vZ9hSc7XQ$(t!NF@v}OEEGP5_u;7T){PO*Q=VakY~7HS(dLjXcp1hKrGCdQJ^rOU9m;Y7InL$tf#E9;=G!@YCI7tm5goWnen|bwnWVmbxSk0au{1VjIFhd^NGgKfteHWGex9oc00ZfH}EKO)B;p-7vl_{;<WF~$8%>25uq);120R-rIDhzjTE;rGW7v%*c=64a-7MimnE<u1q)E!Y3-ZkN{TuZsrhtLK7;IZo2Er}tfRJ25_WH0Ou}w+eZTq-FvtPpF<2u9tnuz(H*&!4$6$AI9&Bel*uWVw?;z-Uy_t{3H46+sF@qpuq#xu9c>+m50hrF8<ZsxLqC}dmH-LcPxjG_(G=T&h8zve%#PZB?8}mumL)X*RW8)bp+bj{{O=KG=Ucu+3`U-if{Ud}}%73s)MZHXs;yhX6@y*`hp)(tx&B;=HJfuc9LZ0Zg5ecJyvDR3*%qY;W@?mAihHXKMXcm3Vor&*g6eVT|p}st4e&o#<cF(U+BQI<10QbX!ZQxgOG_xyZ79_X2mu}7}6O-QD!HVUD!cF-^ek<R?P#xJk&ewrE8TRI$JEI(&$aAg8&G2NWOInF@Z?XReX}zL^DtRgR&v8|r$?xP-r7s$4e$i0!v3$MOQ4x?<Bsrb*X{8`ls6-@FTV_Qzq4@(g0Y&b2(5YTz_WF}?-+_|&#GN@jvL5nLX;#hh91X?xIqS^^<gjP*HS9+THPnVAl}flL^6URCTZ$7*oEh$?9G5g5|DvALON$x9Pg51CU7xDQ1V4OgzWIfVm4r-EzN*_=q3PP<q|bQBh<i4opDsZ~aGI(yoL<4BOz6K7zN)d37N1%&R!7`|eDyzLw;87-PD{#D)0JdBlz-<ZD<I*~YR_}M{Nm!_i=$_2kKd%P;8G0EGg?t#<+BKatQ6%6M+DKO$6FB)`xtd>EikQ2DUb^OTn7);RO{GBq-Qo>921WrYHlQJqq!0?%OFzCOZ_cKq)<UnBJWbJSxp%x+QSHUv=vb1uog+a&<S3;26b0cWltSISHF)hFU~+uiZ7i->g1tLszt%V<0AYQ#<SfSlvlKug^pw4Ym}4iz4U)K-HNlfbqhOl_+qwGt#<c5qnEQ5zMZAt$ueEKC^EN5>t8oh|Kk'),'Libraries/Compiler/op_table.☾':strd('c$~FZNlzO|6u$dc^t2SIis`X1<YdVQvqXbpz-luYjfmAU&>$2q$nK1YGzVZ35+@-c2@s^Pglx(J3{1!(vPr2qlixre=P-)oKQQlAZ`JK4F<C5?yWI8adrQ5oOxRg=F`fCDXd2GCy3@UCpQaHa8~V7R4VTJ=oFP+XBwrfH<tv0LM3yO~3g6e8CY1IQ@{<&kD9uL5foLOoQ7`8VT`P^@vsA7e0(6Znz<A4_58{dbCNiQME|O;C2J$*7ja2}lpG~n_>@jeRniJLion64qW@&`vhK95O9rV%T36jqh28MFdm{N=f&}nqESkcP{>F(`7ZRXetn^V{%TVmS@_&v{Fvez`QNkL)<6a?60H{$S^W6v#^Nf7Cl0<?>4GC?Z&(LtT`l#057UsP$P0LXVyWsIU7itrV&C75TA*c)fFrv(KSe~?9m&Dn|eWS^z={>~;U-U!J4&P))dFWJsv8pbdmJ`G|dTP=v%*5u`eVQ?D&p~V*2-$9f1TTcaL2GO#V@2Sq!Uc9WrxCrBtS)GT+6&ROc%%E2_#JM_Gr$Eb>DbV5v+F1Gmn2n_X$g+E^hr?N}(<&Ae$MWU-UU-4=-?3eUUS`kP3cBVbo59CCJBP3md;kR<g-<{*skSw79p|`q@^o`^bJF!AoS3UC2U7}o=IXNKsQT7@n`{q<1ZtNUVL`9J4jUT3*U#ZZfKA3cNnvi2t*r6Mfl}i4^lT8SMSyB?$nICIi7Qq(+4S|#bKJNc<k%`ewYp??>Y!wvRp-D-&XRsOJBS;Fhu2+-Y4_xKb5h34%Y6i5g>?5pf|PsGnYMg+Z~Md4-kZHwdk`HoGMLX*DiWk;zW+I4v+Oc^jgE1REf9>fcm!EO_Al#WWli%kE%??owh|}uk;)Os{6`3}-q5I_a7TN_))43=+w_*YK`snm#2nIxB~2SGjv7!-ECQv8KQAdw)@0sh&qb)5hUx$^Mcqwx)E=?Ju%a8lhuG%f>jHDAIirSN@c56549DY%6P;-?PCeYwVa!|$>?s*ny88rT{FHU$bh#)I*fBaxTsl#CJzufvgn$_d?iUpG1RSpuzEUT=a^_oz?-YDnY{mIa<ZhXIKS8vdVU#WM<DDdCFTu2#3UpyPjaaE?5$$xwG75k3C&jwyqQG%br4r!N>hWpuvE=iP&J;Ncy~fdOL-zG-h{p3QO!yM=MVA-osIxpGE{}N25j>p10kqx~_RKahWN(Sb)VwrWB=(xr)FiQWDju0@dQK~vUi}i&TSgWQT31|okM>n2b`?Cubqiq-rXaUK|Ea8~V@meRKF795h;)KTv2f{HLAut1qzg6^jY_9}FX@78LCE!U*b9A^<A>6;ap&t#Jw)i~+3zOww~*M5eoI~}ObfYFczdyL8-WXezlTx=2b@x9AwW|Vtd(A<<CYb4I9Qxu=YtoL1AJ~l%(mhEvVE!OZ_X-qGk3|UvG$5}6^U8*kStbkF{5IGU~!5k!tB)o_G-!2ONX0g*u%!}K9)8BT-Q)29Bh$Ii4uT9j$~`T_pz)XU5w%jS2{E`F_Z%3mbN(hOBxw2m4*P%_9;sTG5v0Gd7QS#7K}y*OJip!7ANrHy=@s8NCoN^Dl7CU6)J1}S+03!X?Rm;wTy(JbSDZ*D&a9kIR&=1q+IR=Qh*R>%kX<oKmtWQ6h=A>!-^{`UtgBPd?hxJ7KCizp-6v7wt=i8w}R=@&ge$oRkr@A$RjBQ970h&mvAFEEa(bCyt(1z3zkA-agrL0yG@PbVEw5qjiwawm&#8jRd)m)kQxT0`hZjyNIe*c8-v?xL9x3D+az9B;(VYhBsQ&7EE(wRsX;2`ibIm^Jw#5o@k_jggq^G(g3InMt27F?R&aYC&F6TkL7thz@JxN0XQ+pQGc^>XcKYBQ>Va8AJanqqRQNOe%&pL^KWCNaBRh6OYk-~TF*62TyrG;G>NsDS1j2fPPXs?2zVYC<E4SBFM<Q@UT3@m))d|t!pd7NA<HfiuqxGhRD=l7AuCv#1LI`nw(5OzMy_R8xmxh!`NJRd)eDeZ~Dr8pfykPwIJ79d<r+p~C>mR?D_jYt0>*`c9yhPc5=&as1tGoD*z=ONy<f>VHwf}7C-=*8{cg)p$_}9qXL-WC%kFzV+WR3v}0Rs-elOb9r)zz2q`=<hLft!}ndJ-;ID7x54xJ$qJmtyXc>f03)cd5QzF}~|WQq?l)&h`YVv-8y4*)f-Hm`gX!g|+?J2eqxu3$^XLkIeOZZ1bOIwHLb=%(Le|oc%BX(-|07%?m5F7u%0vyn*o+#uFIpFg9Rp!uSiu7K}$==^rJh0kZ4hF*Vt)wfFX%pwZuR`O|s@y}K=STs!`2M<zk!|0XU%Udi-zI4{iU$L8jgIlXJ1zhB#$hU4Sp?WrDzqP9J;`2L;wa`F8dZv7>l@c!X=f-l;f7q{^RoXh`5eVn@'),'Libraries/Compiler/generate_operators.☾':strd('c$}qJeNPle82_J7vE77ZrcTY>fuNUMQx$AYwGhR`1h1QW*`wDScjWd|XwwF$sKqu#M53bTRS{5&SS=_O{bT-X6Z;u@Ux6>s=b4w?x$_oZ3Yp#6*_mgam*4Z7XOHkRe6siGXT))^ckpm;&yhaIA;cbX2L=jm%%*IhP)er?9-)lbHl>t_H9ftA(tbidvZ5BH$rchSDU-^4<-Wa~o?hp`!9(5g1YZSN*?ie?U_oifEvG7_vWF{MNU5Cl;t67Jt*>rEyAJIJw0USZq1}R3h4w47+tBVnTYz>K+9I?iXv@&<LAwv_0kq$stw4JSZ5`Swv`5fh*tlV)P=*cpIG^M9z@|uT^hdWX4cA;}CtNcf9dJ$W!fQt+hy6WS9FOdVYb3V|u2C1?#<DoSEra9j={<1Wy$k1ebmG-bxp2+y7Hc~)D5o9!IUynAw&6%N2G>+JisLElN2F7-CkF>d9O;^GBaHCde3EYnUr`JEOTU9jgZW~9pqv^M#w_r=gz&R`A)Ywg(?v)jHJHw(EO@iRFU1MG6Fs`KLi0J}(WN{4s9W&dh9ykgreP%?<1b-vcz(*S$#v6|iN_Txgvk|FB4H7`wsZqc5E20uGyE!lrWe7Vp$7{Di~T@%D*u>5EJSB8l`kehW`dB~`O(DI>e(kJPDUcJ&f3kps&i`%-kUELWrx<zFB!vQ6RJ};dF-s}oL~B0_WHjB(I5mCz}uvf^&uKXTR!1a{3rgL<U}UWmaLnzhEiqEbu_A-T)yCvOsQCLixrQ?TP*k^L-EA1PmeqMk96<t>jv-J`yh)5zr`Pbixd4xOeENXeNig9todu>Ehvlcv9pMsW&u}-fe_r_YkWa_x#?6Hz7H^bmMueo!Hi%iM1td9z0Ea7fe^?m{P#w=^49Ma@)=jCC{k{k@hZ$7L(E?07bv0qk)*JUCMl(cc?#5UdyHs%&a1vQO{`FcF8*J`eVavx{{XPO?+*Y1L^ua9HQjQPRGW?qOA+|<d<G$Yoj*#z^JPev=Tu}c3(`T0^F{{KUenBl+dQAxzqgMl!I#0jGrkki^S3F1$8$Q*wzV~1w1j8=;8pPSt4FW?{Ac{trm~L3Ag`w&#?xf~u_G$1`~}>v@-rd)&|mkMqz!)Z@&j>c{?B~IAI+2o(<QK1GnoG(>v|bD4Af4;@p|rgrxfy&BxGK549&p*k_OLp?NDMffje=dZ%REG{!RY-YvhPz(z(y)M}c}H$=-xfvAj#EfJVHZ0$m{r(Cyq6WaB-4OSAu5s=UuOH-ST7m<9)kiapXlAfjKT7E?LF1caD|43iK^>P1yP%O47WVZ7#j-i5tR3`h3bfp}HYh$KP|pYv0w3ecRTO4c^H13V?2__0nGVk$7%`*}BsAe*88aD1U|JepK>QdjpO5~Vm$Z^V%5X_ZSuo)9nt!MGU0vBI1SKzZZZoJc?h(kYW_g5-_`euXH?p682tk>qHRIqeXhZ6|>0x+GAHBwVj&w$Z>{5Cte{Y#D69-{HhPA1o8T4L?_Wf?YOvP!<(L@HkVfDC7uSK}0mAu#xx(;*YZa2#c{c7G>>8!F=WvA>pN>zH=eeS6|*-3TQnje1@4!7$PZbB?wBCDV+_dN`S~9ji^*nn9%;13xG=^ED}(yL<?fM3Tlfxjy2*RhnRjKwpSS`xHb)jG~o*T>P>I(*#KTJ*>fwYN~KIRx?^fRbfZBxV&J_E@ZKizUUn-d%S8(mX%XeqfLjTQr%Eaf)sv{GvM}ngY{~h$1SQ}B_}p-HHI*;snjXHQ&IPOfeX?SU$`nRt_*%f?g0vO)$%!wvR!66sPu^PJxYIZrB>(j|Z2Hq*>ZYS)nE!V*bpBK`WlZHS^I22*rP}f}bBS7In^m~aQagj0wlb17RV0{b<c<2Xc38N@hAq3wto2~WIt|fd=ms>+*ValEvzDP891H5f|59wazfX==_$VM-ao9M&2s={6;lw<#WyS^AY05T+B2WqipIIj77&#{3j<rw-1B4S)9erv`eQs<|qSP?4`UKr!X-Z)N@_KbNskp(fBdM8M0ojDr<!^o|xye@;SxQ#ODk3Ir0Tfi4sxZnKROfdQliPK2a5lp!K2(CQB{-*ZW~fwR3p#@O&v>&_j43pT>QHk(7Ga|sSgqK#sX5VY@PjsH8|*ZL%sWAV*sUIZFpf?19O=UDT5a?hbZa-~<M24T0Uwb#48+q)h=#aPmo>mpWo+%{60TatRrrI2DzlS}%F`4zzy<#JwowInV-s3Atrdz6zAhBB+L8>MEVeK|JI45ZzNtO3P0c5N0+^b!4S*uru^8C)<3^bj6L}~!Fagd~{iqP96Jt^W#w_*(<SHd6TgrH^155$qebY7s9rg84T{RZ-iz)NqHmWI6fwPc-C{qP`9Yl>fg?+<Lvr}<$8vT0;{BRULw^}{)Myn?PH*A&47?N2$g<wHlk%9hFg@YLg)l<LT;TPc*{+O~RzjJ^9`5WQht}dthIQ~v})NzRU^B{<~nbg}3r2?CUzLM)2O9WidI0nl62Lo5<e*'),'Libraries/Compiler/gram.data.☾':strd('c$}RYYi|_S^?QHCmd4VI7e`<TSp|)jhtnzw1Y~HFcDsz$_GDRkU)fm)kgRHp!8jzi>uiFNu~`y>A+2$pgy2V7kQ}LB`;G5AKcKSYKhSgUxsP*aX4iICp56O6_q@-!=iagF{(ST2JEsN*-FH5`aDM30Mc1`*h4OH=;9K@#>(Fn9PMtdhzkeD(a^%P<{4Q7AV58|4N(uIH5`PZrn?2_*xaZCfx@X<@dxH9w33xpg@DCBdY8=L)7>w08j6)%eg?ud$0z3QeB@ME(IJ@Nf6>r3V`u(XP_u_?j&S*F`>DNZxv8$sJ=;Eb8_q`7WFKVFS!k9Z!C{du(XWw(roP9q8$gnZs5TFT!-^Fac1TeX3w&?bp>!DM8Ow9YWV$Dwk)6Wt+i}zlV`H^z52=i9(=%wY?svM-0t>r)QU~1H}`2Yj*N;TeQ+`K)(FdREm0%q)9g3TYPRv0$xKa<eRS8A*S?eU6(I{Dp&o+MiYnE3dx96ycYNYB6SyCc~`!S!q7mHeoSxZEq*kujVXjCSG$zfopjfHj2dbARKF-L<I~45)wL1pe4by@r{YY5$6s9p%tq2H*tSSwB}2xMn}wS!}$d6y+Eo0F{9oPS-gsD3?tIQ?u|#7br4LBDnL7I|_cr^$ku^`RJOEb(FM=HHK94%1JofH?>RxqJMzdI$>$j6lUcSfl(k$<aePNHw2HJK%5%U_Uo>AY(n!m{vh{CK~5r`K|_cRF!4gnCL*6b8J<-PBYV;uJm?9<JKtbK=;3NL%N!mJJc)x!a;Etu-W8cf%_zf6hQ>N5OL`!WWXv+)%MHV}CjZifnExjd!RkXH{MUkgnv0Md&8<#)n)e8Q4%I`*?lEql6Px_7nS{)ACM!|<#e8CjbXTH`BoQw%!Rmy_V;e0_^cpWWs^7>42ye@DSW#OBU(ufq{&Fj5EoZRDGcK%Jgr}hrvrT}fg4R<3EVE1Fwc(6uVS)~*G+;&m%G9^Jw(zjqDwuzuGTNj;)7mdho2nk5rp!26{&c^Hg5^6Vs>Zs3ihU29me?=?8Op}Go3D9A8v2K+&r%?}w-cD1ie-uu9Srk@1krz>H};8J$`-|X(XSTuj_~Ei&f-@$hy&79PKWgI=q2oa`-#S;blwo|D#NW|njK=M3o2z(G@65;Dxs?+NQ^N%qrk%(h+z~f49)Pg=N3?4yVq8<X9#_3?5Yc@`~m}asjG5A1Z)z%O|?6d@JBn`)=jAo#aXN@IyoD_b`l9%sw5D)oomPvgyc0vyJ^sF9)xzYJMCr+?WPb`sH!86O~Dw2i{P74`20eC#3S{PSP+8b7<=CBNw5qmY%?ii=(P$aIW?uC0_)9iaOs#aD$8)4Yiv(!E?=yatBB6KrkdlqYwk6Pvyd$gV@+KeFAjTE7XV3DL~aDLxx2ESZHCoiU1VJ@2kU`nca54bpsa({Ad8E|y7#eG4<|BXkeuO_`}PWx%e~@)2EbsDcD7fvHVuz3kP&@znL>WRsqZ5^<2Vzjc?e+N+)Exk4yCLmTjn1w|BVp%%Lq79Lxb{y$+~(a?~i#^-{HjwbMX({v$}4>GG7;Oe10gV$_ZCIQA|{s9F?fF?JzdJoHZDqj>VdmuvMk%`Ccs{52)###rf}d*S>GT^EEt6@H~O%DLmi8^LKcj!}AY#zRR$K(>@p%q)O##F<S_i#ZNwu^~c%C6or~v7ElMEr`*s{W#3W)$s`Vr+YXyhW7u80b%WGN+BCK@g>*{lkb63##3EgCPj{3HMAgc(=HBUFZ`&QyKNX^qt>%0;&+TYgtOp&3kmsrfRB>?%!<8B=L77C;3V|E@5xZUxBvZDXqC9w%2PP@U*OfTs^8ew%BRp_oSg0d#FL45Fo;2N}^C1aQimf9YBG2T}%d#v{WY1%?US{=nhTVUt>N|8SMBnY?*zDrQt@-1_@^Zv2(M}B*>b5$Rj)UhL)FHK_nDH5Zs8c8nGl)wTy?#NS6VWVWv*no&@rr#ntjFi;QT9A}!jsbS&673V+<47r4BfwJ3_-=usN*^f$k%awf(G4usU-Gsi5b@#kwmJ9&=F@+8XT<*1Htmmpz#3y(AvgTR6ov$;~~G=iog)0DqFBLmJ08wKuD&;-nd~S6_kA!N)}-L-_JO!N38Vl=}h{_(M)n8T|N)3z5&*}_91KjI@|ZrslMN2lJ<nfx|t+D6COMBHt+S?sR?Y*(WGs8=_HQyWl~}+rMI4vmou5zU0?f`mEK+dZW^9OCe8Zrykd;N$X$58!qGlx-W0<#@Z8hGQ}EnojnCovD{Fj-d@BILy&mH-kZu$L<bmJMs7Q2@3WmiXy0KI>uM$yW3dJi(N7j%2xF{a=RVsu!1h%6O@rD;@CtxWg5}oYM6>#e1^Ieydi;PZp7@@t?%voJ-GVr_15X<X-dB&BO_Ywp;1viIrsb3YaihjJ3B0$v;P&EQ1=&<w3>O)JvpAhLAF~b%TnG!5u!kS+Ym2IzWVy?;pC7KN_{pvzttj1uJ<;DC0ilQ7q9g&v!PD$=E#jn^$wqNMH0%0U>?&!URTwqHWi&giqlMQD_RnCEfqNd1ac=;jj&UtXIEk9u(1E-JipTUXriQ|WZl}Ao6UEh8k+=ZascoE!Pg<TK!6Uf;?>q*dh96X2a5};b`gN%H8XR);cjn<F5>sxc}#zwpGLwojCd$!(g+;2C&XwOc!8$Y%i5891;0I><t^-~>6O{nz_QsA<}?k(+pnEZ~NN#jq(vQZKgBv}45SiZyDoVo2Xcy7>o7PP*_<jrD^1r7@kP(uP!Hv6k@WsKK1WT#Z`La3*O{4RXWLspoDhP?h|ZF+Gk`_MLuRd&{3E??hd7N~Cl91l_MFkIhtrfH^Tu48z9f@ce!e`<-~Y(v~ztleO?0z)w?Jpgz}&s(qIdBx1c)(WzZHCf78x0gJ!7JJL6-&P;;S4mo-d>D(L>%NKA*oqA_2P?j!1ZphOy<(+y-Iccr7FJ*^Ds;6FTaV#Ygq!n9SX`LLWQ|4EJXUP9u^8ptTUP3qky+bP@5F4oR|?h<Q>dDg(u#|n4y6!NvnZp;32J?Fla?1s4Mtg1-waiQBvW=F2tyHq!aq%Vf-|ydU5-yUB63^HjPFd6Zcqlv17H%FAc~6=nES<b0&`~qO<5Bbjp8n$hGpH#x<?Ji>$gqdqrx8268+o>rq-4Em3N|Zt942O9yi_CN4yz)rQ2(g?+=k5*eCh^1Ck#w$%`|Eid)BU+^sp`lw_YEI@S*9L_%2U8i4c)J?)?fo<EYUc%gEh5LQ?q)4L;AvQ?TCB0<!Ww;iEl00ns(jtzxcUlR${31!axkiqQGFL!mNWyY!A4~Rg{UMCo$ll=t%h7pe>A&SHq4OINbYgsI@S$nt&n~0t&mPb`W)rmjVn}i)@dnH3tzh0Cr;UX|M@7Bu2q@FETH8loFO}g=d+Qt$H%2joP3=3?HD!BhjupTYMh5UC{v5`txAj@$flPo}4*Y`e7;57=NMOYW_Pm=V;2&y#7Xtq)*TtDeZCMb4>fn#T#T(vx2QL+f`ZSs0Z1Bn%IM)yi;1vd_nKUd4<d07r3opi)Iqv@v!DW#nf_X%v!uZ^8_AQ~ulh(7KmrM!%k8j8G~l#`qXjghk$3b<!`;)E)(BUb$8M>bj8unvt-UU`to2cgM%Iyp}#+j9%tdq78eSihINf0GsymJU+bPA1ZFf63Uq21=;XAIklGER)+3UoHRlK>WLqBWjfYt}IXd%1&RFu)S8wk%;j3k2W02cUrAkNDA-`5bTFezL`m1elr6TZ)Wsx=zpOO*|z<Q{{eqn^lb'),'Libraries/Compiler/ast_to_py.☾':strd('c%0Q6Yi|@s^1FY<WF$vDW^n8!xhN}^J7Rnf#R(R0=p>&rTJMfw<@N4lXB^u{h|J5_Bm``1hY%AWKEfLk@&W=ua!dF1enb56KI9_h4_sBhrsuIcYsi;d$-6y0-Sz6K>Z<DYXrn%EOw=l+df6=(gQ8Ix_v($nsQ6B;-WV@dEB|oI9iupE%$=UBH_CFv*krZh2OWeSr>6$@{+T!qw*K<w;O;&99ET9I;Z8Oxf!pv+%RW%8j})suv20?RmSx#|^v+$o{xq=r^_>HIoxXwooo~TB2JVf1qRp{v*13BSnnQ$aHF^!p8V1Z)=!f)dzCe%C1-e2k>^MztIlkwXu=6u|qHpIu0<BN!O(1Av_1wnH{JzG7yK&^w#_GrL@JB$vo>s2F(_8hLYa%)U(6arY?2Jv8Q=!e?geeU-m}t}x!ri0rI9+k8WqA7a%h_+>vFujy)$Ai^m+G~kQscN!UWJa4hFctqq8q7>Ii+f?8OrsiFs(9*5FVU|rdwqX>sMHtGcq>=52N)467kgxjw)4)zMsSs#qs9uT>_5{Qan$O6o5kjH!}}20rk%_r=T4)rlWxBo(6-^vviIw!RYtj@9cd0?H6Bs@4X#6wr}6EW&PgPty?!fIMGGFe+jf<C^u{wTZ~YY56=MbmtI1IA0C5dR~I(tQA#@stocu9Zs$$pw!oX0q4@%9&RvHl<9cK68Z?Wwa<qH>HneK>fc4Iy9NDVP&GT-9KhB@PH$H2gWK9EJGL2PCTUH0@f2%JK5~4Ho2=pHV{X9Wu=}BOJo}Qu~fL@-aAJH=)kOjI(&(S5iOjkgxpU?}y^D4avGP^`CgQ!2JYxJM=D*b|9qu1#TdXwIwx9J^vm)@ga(y!=!`ZfKAeoMcj59mYsi2gty(<k()iB#<A+m$c${dLbCLaN2_k#Z45dY7KF+0SAgepcwWB+?0-km5*b=j(mFxoxlr#B@x~)84`UY-nF6p@A$I9QvaG<km|00xDD#4gz>U?-CH%d3rzb@;C_PJ9?Xl#vOqO1iuC%eS~N%yRU#hppo*WLJN4yZizVq5GLWc>@+G`p}#{yIs~67*eyBgGdU_G0|^=I-`@ry%;b)PYAn%f(&#{R%#EF-4<%?=WQ%=q*!%kjpAmMmVMjpYp2$I<1eRhQ0ensuP_VX~Ih6-{eQ>wa|GjB-k||p-9U~gSurE%uH|@B7$?=0m8tv&TLclTneWIu5mA;8iA8`qu*y<=J)%!c{NQ4V|*#={LsI8DvBMT_4j1ut(=58G7LJU(qJK^s&jtReWud?qPe!u!U``!ghd)Ttj#VT-uGoa%fJr2G=il@N1S+l1L<Yl7^%))@ln(99VWvW(cu1}`;z6KUYNY1wGLx*i(Y#J@=2|b3E#i-*(Rdz=Wcgh2|<`n(F@urc%W$-PJZP2y?{8{-913r~egQ#~_w`+Cp<1g^TcPm4_X8mci0;5m>(to-5@f`f&77)U~q2sWOs2rc*ii=r8J;SzYgM-(m;D-d<CvZ0^*KcUp!hQQJILuGUc$y{?(#zIO3ced%wZV4!>$r8yKiZi8;iqp`|Fe3TNs28J2(;CtpO&ucV|!A@BJ&qkO*x2h`-I-N!cUaDBB%ffKn7gNxYJ<ID9T=iYY2!q%ZMPjlXeL^U_)*7&SvC=&lWs0$U0!9j~D1;l139uU!Y&)3r##8YVIwrz&AARHM9jJQN9wq2@0eca2f;*^VhG|Zb&ysh+y|4`VEodv<23#qF|_)-~#M9VEPm1M#Py)OKsWH8#bAS&C&&_UrHf+LD2&Ewwbx5?{7%jGX0VLo)f>9<gXCJB1p*Ae1Pq{0R*|@DsIgQVxZX@HhV-6yQ_bIY=bCv+i-$8Mki`f1|4d3fLD`)l`Ps_e94)o6HTeUN(`D@Ti8FEiww_xxwwF_(7zTP*a#f2*eH%;JgFJDHWlPSN`-`)3+KHI5sunxgh)T&=9lJv7EZ!!1Du|r^iB>EW~I~zjEE^+2&I%|PmFwwp_9Bb<g>qAJo|mZ_odMp8-^bU!Hp7t3WrDE3vdu!0_!CW*3tteTbV8-CgETda!|n0%SXYexV&2`uUW2?Ada=WN|N!25=0s;R+Ddv5zp10#MM69T<mhqkC~fOtxeI<dgbMEK5dtTp=TgrxGgEHWRak6yXoYpA%3+|a!Id^`K{Grn`wixU%!9&akg+;t0MgoTs7*Vnwo)h<8-Dp+Q9in|7LIkqvwAEq`L<<gA~^Nqt-|h5k#sUSlzLm0p1QvHyd@NxFv93%KdEQg`^7tcT|<+2n-4|;@85kDqA`S+@KgB;D~&z))LyAEuw79ek$fnyw9zKB39Te-nDk{UJ!V$ir+O<5KBf}H}o)Fv-o@=rYM=FI2X5yD|Ch4&lhy~(fyK$F==Uq(5Nj29|8mz7TbS$ZO`hidukA)hDA^iSh2#Lg#=@$BSS->+8h>!$TI8>3y4|>%ZKG;B&~zTBB8~jB`cB1co?N61Cs5=HbpASa+XCj$9RWCY&U@FZde9H1|iFWUvvH5`tA44lpwyX$SRV<dlnhemNZ;#gT?bo)XaEAC=tqgNF!|+cZ;KRhMv^72}A5M(d{KCwwLtHmg|)78u@JY0JR<GGG&Ktds~Z<(Ne#;r_=P?ucg+q2*ILZm^NXaZ72t+GD!*3@h3*iSdOODmaQO5fmPaqnd(X`n)Pcu8#_ZUF>@1%1v6;uy&UO9-L*rF#*VgPDqj2$LT^@>kqmO>NopWcV`)_%rtZA(!l_z<Jm5H>>jVcya;#3$DdZE$#Zj!vh9!-iEc<|Qel3=VYPFe=$5<4a%UPT|eJkw@)eI66Ce3!Tabz=|zh*d4kj6;6(IqcRO|@VC%EilHx0&Px0>ffeu<RIQjUAz6P??s|0VU_@CzdJ*D7T`W%vjy9@khzB<3zR}FR^T?En#-)s~+DGMR25dMRZROx6{VPLLe0Z={`&q>|%=4hSKmnuT4JxPZ^C>9M<sQ#&fEbfR`R5#^+E;q$TOA(wuu(B!<>9Jx2Ipr>zL&=Z5^mP@E~My4PU;{+QK;b>3c8=jByiTOPl(t@7`@TWma^W$Lc5)0h6fGmY*|nc~Hn?BqR`nZ|u=Mn&f0jQb8qdu$T4VR<ousY!XTCv2t|#BWf+YsO`IIiS#zQyyfW`W#Db8Ot2q!T!)R85D;I+?vDng)v65h8#}A69-ZM)zX6)jNTB2tN{ys)~4kW({lPW;X16?E}PFTM)<*a;B3szWTebd<BrK~@?fRv5+xr|>ju7FG#E>Z2`7h@J#h-ohiZ{=rACCSldp4nTAr7#SxH>Oxvd3Gv4#>98-?+cs34je!fg?RvWzIG8n&X!-%`A#`nb1w@y5y%^6Wq(DqDc5!h2TP!7#Ilc%DTnf!nCHU7?JYXmn03Nmgq8hOrQN9T7zvRZLu!w#gJrn4W5}eZNILGvA!YY%+O0Wb>8IIMOUnfvMtimv1-_RKjFNG)u2WBnCN+h`$7cFYvT-<q8vtA=4pjk*4DSMij2P{3J6RaRl2WPZQ^@H+eF{5{BsUov{_qP)HN}yja2rP$z)#L`$CgNA@}{jwX3?EIH20xT&2u_~)5Z>sNlhd^)<4y4<<4THQs@b8BT1(U)jlDp9}L0kX(A!-<s~QjT;~93qQO&@5>INGxqH={b8CVB{dcfL&8C1M)nW$oN4C`y!n>X_CI?C4dCI8j;}nO)Gp1{e(MJa=k!A1$~+}q9^WS#g9HsNn}I-Vc}xTXBb6afr*}(_wj{@f%xx{o2lV}ElRo1cl_G2LZxeVQm=$aI{m!IZrO=2TJmfsj$1P_A93LjuLp*A0mT!vnq)x9O5Tu;VYrQ)JH?zB!<CxvHUiMANck@#Z~(Hs(W&M~ry`Ynfd_GA!P%w+A2sOAFwxJ<OR(+}@nR~CI!%|f!dxUE%aQ~vTY8#8!uwRwYduqVpNCn7z+r4LM7Ss7>cM37uiSR&Puu`X?tX*O6N0A2Kk2?l8y;!t-&s|`O1;t}hm<^7JroteaGO%MQIs6)GUK0R-lF`E+Yi4{#m1j%dg9sMQrd&jBWsyAh1VpSNiSVivHM#5vI$$=Xk{04h~4i38+97)fl9qb25c|9&&8mB2Yt|3g(O~6r-6KdUnU!{G%`^aJ<RVw2R+<K5;wqx28M9Jun?4oVVehT(Hb63aGN$($hC_Mh+d9w3wUmuVFVSzX*o5GZA%gbV|TphNp|<XsrU`As4anb&U3Nd$%=Jo<o01M5*=w`Wq7#Nb`V^bQq?Wi95=kbrz#WmvBDu@?!)@D>9OyBA2F@Nd2Qj)1n4mcb#ArPa#RsF<?b7kArXWw(QBINw19_Vh7F@WCPOB6R;3JrvsEmY9k1@EuvIDa<U=PE^5W{-zo&2iq+%zFX7MYAVFG27XtB%WGt7MDu+48~@xm7?tlieBZRRX^T%d%*#I;PHpku5^89Zwkz<ec_nLi2om@2e<=wz<q_4deJCBC}Jo6e#le~9Z%s12UYv?}b_ci3*K8&OB$%F_{CAbv`!zhe;-o2ZxVY@Iht+$6=mpdPtJ%Ff;H*=Q_5!*vVX&(`W-I<?}s>%3cR_@cAndhj5I2(wjyU?;+(tjB~jxvtu!s?6YwS?Cu<l5(vPHj0MuZyKJ_O10|9N9SO@>iW(|(XW(r%hry81ORUug6?SW!(Qle3TLTTLP=w9D%@+M#M-=Ni^qmSfJV|U1994L{*N|*ojnGPX(KTKd9}JHY78LZPrMDFWN^Y`RCWe)0V8jEhOUK>K-AY*e%n_syLsI8_<<8{ER(f~afD=-3%#$tV*7=dagQD_^Td3u_Z4uBHa$Tfuq5)as&BIhSjY5`&JwOg#O!Z0Ai=62*TKPhO^BsZJMe<RDL^{q{EiOwFGEiM-|(M|_BsyH|F1|XwP~v+_QQ^AvTYaI`}+q?8@>SO{{TPch*J')})
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
    (ÄÊPSH(__ÄÊIMPORT__(("to_ast"),globals(),(""))),__ÄÊADDGLOBALS_CLEAN__(ÄÊPKE(),globals()),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("ast_to_py"),globals(),(""))),__ÄÊADDGLOBALS_CLEAN__(ÄÊPKE(),globals()),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(__ÄÊIMPORT__(("tree"),globals(),(""))),__ÄÊADDGLOBALS_CLEAN__(ÄÊPKE(),globals()),ÄÊPOP())[((- 1 ))]
    (ÄÊPSH(ÄÊmoon_to_py),ÄÊPSH(("has_lazy_load")),ÄÊPSH(True),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]

def ÄÊmoon_to_py(áÖï,áÖÝ,áÏè):
    ÐÌü(ÄÊdo_imps)
    return to_py(áÖï)(to_ast(áÖï,**áÖÝ),**áÏè)

(ÄÊPSH(ÄÊmoon_to_py),ÄÊPSH(("has_lazy_load")),ÄÊPSH(False),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
(ÄÊmoon_to_py_fcache:=fcache(fp=ð(CACHEDIR,("%s")%(BOOTSTRAP_HASH[slice(None,16)],)),file_only=True)(ÄÊmoon_to_py))
def moon_to_py(áÖï,áÖÝ={},áÏè={}):
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
def refresh_cached_imports():
    ÐÌü((TP_CACHE).clear)
    (reimps:=ÂÚü())
    for (k,v) in([*__ÄÊIMPORTS__]):
        if not(((v is not None) and (((v).hardcoded or ((v).name == ("Compiler")))))):continue
        if ÐÌü(((f:=(v).__file__)).is_file):
            (reimps).append(f)
        
        (__ÄÊIMPORTS__).pop(k)
    
    ËãÂ(ÐôÅ(reimps,MOD((lambda ÂîÓ:Âåß((sha((c:=ÂÞÅCAT(ÂîÓ,ÐØó)),{},{}),ÂÞÅCAT(c,moon_to_py)),Âçß(("Transpiled %s")%(ÂîÓ,)))))),(lambda x,y:(ÄÊPSH((moon_to_py).áÐñ),ÄÊPSH(x),ÄÊPSH(y),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]))

def generate_bootstrap(dest=ð(TMP,("☾.py"))):
    (ÄÊPSH(PL_FORK(compile_code,__file__,True)),((_:=ÄÊPKE(0)[0]),(Æå:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
    (pyc:=(lambda ÂîÓ:("#!/bin/python\u000ABOOTSTRAP_HASH=%s\u000A%s")%(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ,sha),repr),ÂîÓ,))(("%s\u000A%s\u000A%s\u000A%s")%(pathlib_import,ÂÞÅCAT(header_com,compile_files),ÐÌü(dump_cached_imports),ÐÌü(Æå),)))
    if dest:
        ÐØì((ÄÊPSH(dest),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),áÌî)),(dest:=ÄÊPKE(0)),ÄÊDEL(2))[2],pyc)
        (os).chmod(dest,0o775)
    
    return pyc

def generate_bootstrap_live(*áÑË,**áÑÕ):
    ÐÌü(refresh_cached_imports)
    Âçß(Åøþáüì(("Refreshed cached imports!"),("f0f")))
    (Compiler:=(ÄÊPSH(__ÄÊIMPORT__(("Compiler"),globals(),(""))),ÄÊPOP())[((- 1 ))])
    (ÄÊPSH(Compiler),ÄÊPSH(("code_file_caching")),ÄÊPSH(False),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
    Âçß(Åøþáüì(("Re-imported compiler!"),("f0f")))
    TRANSPILE_REF(moon_to_py)
    generate_bootstrap(*áÑË,**áÑÕ)
    Âçß(Åøþáüì(("Generated bootstrap!"),("f0f")))

def moon_cli():
    import traceback,readline
    (HIST_FILE:=ÂÞÅCAT(ð(TMPDIR,("☾_cli_history")),mkf))
    ÂÞÅCAT(ÂÞÅCAT(HIST_FILE,ÁÜÙ),(readline).read_history_file)
    (pfx:=Åøþáüì(("✝ "),("f0a"),rl=True))
    (ns:=ÄÕôñ(ÁØã))
    while(True):
        (áÖï:=ÂÞÅCAT(pfx,input))
        if (not áÖï ):
            Âçß(("God is good!"))
        else :
            (readline).write_history_file(HIST_FILE)
            if (áÖï == ("clear")):
                (os).system(("clear"))
            else :
                Âçß(("%s\x1B[1A%s\x1B[K")%(pfx,ÂÞÅCAT(áÖï,__highlighter__),))
                (áÕÃ:=ÂÞÅCAT(áÖï,compile_code))
                Âçß(ÂÞÅCAT(ÂÞÅCAT(áÕÃ,VEP),__highlighter__))
                (s:=False)
                try :
                    Âçß(ÄÕôñ(áÕÃ,ns,native=True,Æå=eval,ret=True,init_ns=False))
                    continue 
                except áÍÚ:pass
                try :
                    ÄÕôñ(áÕÃ,ns,native=True,Æå=exec,ret=True,init_ns=False)
                except áÍÚ as Ïã:
                    Âçß(Âøî(ÂÞÅCAT(Ïã,(traceback).format_exception),ÁØã))
                
            
        
    

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
        return ÄÕôñ(ÂÞÅCAT(áÒø[0],ÐØó),ns={("__file__"):áÒø[0],("__dir__"):(ÂÞÅCAT(áÒø[0],áÌî)).parent,("__name__"):("__main__")},Æå=(lambda x,y:exec(x,y,y)))
    elif ÂÔö(f,("C")):
        ÂÞÅCAT(ÂÞÅCAT(Âøî(áÒø,(" ")),Æå),exec)
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
        
    

__ÄÊADD_EXPORTS__(globals(),("moon_to_py",moon_to_py),("moon_to_py_debug",moon_to_py_debug),("compile_files",compile_files),("generate_bootstrap",generate_bootstrap),("transpiler_cli",transpiler_cli),("moon_cli",moon_cli),("refresh_cached_imports",refresh_cached_imports))
TRANSPILE_REF(moon_to_py)
if (__name__ == ("__main__")):
    transpiler_cli(*(áÑË[slice(1,None)]))
else :
    ÐÌü(ÄÊdo_imps)

