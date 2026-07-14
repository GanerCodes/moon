#!/bin/python -Su
BOOTSTRAP_HASH='30n9ZOyYwO7jowJOq7lmOXrvOwJicmyL2_mJkoqlVJ4'
from pathlib import Path as áÌî
from os import environ as env
moon_dir=env.get('MOON_BASE_DIR')
moon_dir=áÌî(moon_dir)if moon_dir else áÌî(__file__).parent
__dir__=(__file__:=áÌî(moon_dir/'Builtins/base.☾')).parent
(moon_platform:=env.get('MOON_PLATFORM','NATIVE'))
import os,sys,inspect,traceback,threading,errno,struct
from threading import get_ident as áÐèþÂÐðþáÐØ
from sys import stdin as ÂÐðþáÐâ,stdout as áÐãþáÐéþáÐè,stderr as áÐÙþÂÐüþÂÐü,argv as áÑË
from sys import exit,setrecursionlimit,path as syspath,getsizeof as áÐçþÂÑÉ
from math import*
from site import getsitepackages
from json import dumps as jdumps__,loads as jloads__
from zlib import compress as zibe,decompress as zibd
from cmath import*
from types import UnionType
from random import shuffle,choice,uniform,randint
from pickle import dumps as pdump,loads as pload
from base64 import urlsafe_b64encode,urlsafe_b64decode,b85encode as b85e,b85decode as b85d
from hashlib import sha256 as _sha256
from tempfile import gettempdir
from builtins import setattr as setattr_
from operator import setitem as setitem_,__gt__,__lt__,__ge__,__le__,rshift,lshift,getitem,delitem
from functools import reduce,partial as MOD,cache as cache_
from itertools import chain,filterfalse,product,accumulate,zip_longest
syspath.extend(getsitepackages())
setrecursionlimit(2**18)
del(getsitepackages,factorial,e,pi,tau,sqrt,cbrt,pow)
(setattr:=lambda x,y,z:setattr_(x,y,z)or z)
(setitem:=lambda x,y,z:setitem_(x,y,z)or z)
(ÄÊSTK:={})
def ÄÊPSH(x):
	if(t:=áÐèþÂÐðþáÐØ())in ÄÊSTK:ÄÊSTK[t].append(x)
	else:ÄÊSTK[t]=[x]
	return x
def ÄÊPKE(x=0):return ÄÊSTK[áÐèþÂÐðþáÐØ()][~x]
def ÄÊPOP(x=0):return ÄÊSTK[áÐèþÂÐðþáÐØ()].pop(~x)
def ÄÊDEL(x):del ÄÊSTK[áÐèþÂÐðþáÐØ()][-x:]
(ÂÞÅCAT:=lambda x,y:y(x)if callable(y)else ÁÜÙ(x)+y if isinstance(y,ÁÜÙ)and not isinstance(x,int)else x*y)
def ÄÊCUR(áÍÊ,áÍÅ,*áÎç):
	def Ëðá(*áÌú):
		if len(áÌú)<len(áÍÊ):return lambda*áÑË,**áÑÕ:Ëðá(*áÌú,*áÑË)
		(ÄÊPSH(([*áÎç],{**áÍÅ})),((áÖÒ:=ÄÊPKE(0)[0]),(áÖÝ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
		for(k,v)in zip(áÍÊ,áÌú):(ÄÊPSH(áÖÒ if isinstance(k,int)else áÖÝ),ÄÊPSH(k),ÄÊPSH(v),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		return áÖÒ[0](*áÖÒ[slice(1,None)],*áÌú[slice(len(áÍÊ),None)],**áÖÝ)
	return Ëðá()
(ÄÊPSH(sys.modules),ÄÊPSH('__main__'),ÄÊPSH(sys.modules[__name__]),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
(ÄÊPSH((Exception,object,dict,bool,list,tuple,set,str,int,float,bytes)),((áÍÚ:=ÄÊPKE(0)[0]),(áÍä:=ÄÊPKE(0)[1]),(áÍÙ:=ÄÊPKE(0)[2]),(áÍÖ:=ÄÊPKE(0)[3]),(áÍá:=ÄÊPKE(0)[4]),(áÍé:=ÄÊPKE(0)[5]),(áÍè:=ÄÊPKE(0)[6]),(ÁÜÙ:=ÄÊPKE(0)[7]),(áÍÞ:=ÄÊPKE(0)[8]),(áÍÛ:=ÄÊPKE(0)[9]),(áÍî:=ÄÊPKE(0)[10])),ÄÊDEL(1))[1]
(áÍÚþáÍÚ:=(Exception,BaseExceptionGroup,GeneratorExit))
(ÁØã:='')
(ÄÊPSH((1/2,1/3,1/4,1/5,1/6,1/7,1/8,1/9,1/10,2/3,2/5,2/7,2/9,3/4,3/5,3/7,3/8,3/10,4/5,4/7,4/9,5/6,5/7,5/8,5/9,6/7,7/8,7/9,7/10,8/9,9/10,0,1/100)),((ÃÆ:=ÄÊPKE(0)[0]),(ÂÑõ:=ÄÊPKE(0)[1]),(ÃÅ:=ÄÊPKE(0)[2]),(ÂÑø:=ÄÊPKE(0)[3]),(ÂÑü:=ÄÊPKE(0)[4]),(ÂÑò:=ÄÊPKE(0)[5]),(ÂÑÿ:=ÄÊPKE(0)[6]),(ÂÑó:=ÄÊPKE(0)[7]),(ÂÑô:=ÄÊPKE(0)[8]),(ÂÑö:=ÄÊPKE(0)[9]),(ÂÑù:=ÄÊPKE(0)[10]),(ÄÝóú:=ÄÊPKE(0)[11]),(ÄÝôÀ:=ÄÊPKE(0)[12]),(ÃÇ:=ÄÊPKE(0)[13]),(ÂÑú:=ÄÊPKE(0)[14]),(ÄÝóû:=ÄÊPKE(0)[15]),(ÂÒÀ:=ÄÊPKE(0)[16]),(ÄÝôÏ:=ÄÊPKE(0)[17]),(ÂÑû:=ÄÊPKE(0)[18]),(ÄÝóü:=ÄÊPKE(0)[19]),(ÄÝôË:=ÄÊPKE(0)[20]),(ÂÑý:=ÄÊPKE(0)[21]),(ÄÝóý:=ÄÊPKE(0)[22]),(ÂÒÁ:=ÄÊPKE(0)[23]),(ÄÝôÂ:=ÄÊPKE(0)[24]),(ÄÝóÿ:=ÄÊPKE(0)[25]),(ÂÒÂ:=ÄÊPKE(0)[26]),(ÄÝôÃ:=ÄÊPKE(0)[27]),(ÄÝôÐ:=ÄÊPKE(0)[28]),(ÄÝôÄ:=ÄÊPKE(0)[29]),(ÄÝôÑ:=ÄÊPKE(0)[30]),(ÂÒî:=ÄÊPKE(0)[31]),(ÄÝôÒ:=ÄÊPKE(0)[32])),ÄÊDEL(1))[1]
(ÄÊPSH((3.141592653589793,2.718281828459045)),((Ïî:=ÄÊPKE(0)[0]),(ÂÐæ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH((inf,complex(0,1),ÂÞÅCAT(2,Ïî),ÂÞÅCAT(ÃÆ,Ïî),ÂÞÅCAT(ÃÅ,Ïî),ÂÞÅCAT(ÂÑÿ,Ïî))),((ÂÕË:=ÄÊPKE(0)[0]),(Ãù:=ÄÊPKE(0)[1]),(Ïò:=ÄÊPKE(0)[2]),(ÄÝøà:=ÄÊPKE(0)[3]),(ÄÝøá:=ÄÊPKE(0)[4]),(ÄÝøâ:=ÄÊPKE(0)[5])),ÄÊDEL(1))[1]
(ÄÊPSH((-ÂÕË,-Ãù,-Ïò,-Ïî,-ÄÝøà,-ÄÝøá,-ÄÝøâ,-ÂÐæ)),((ÄÝîá:=ÄÊPKE(0)[0]),(ÄÝîâ:=ÄÊPKE(0)[1]),(ÄÝîä:=ÄÊPKE(0)[2]),(ÄÝîå:=ÄÊPKE(0)[3]),(ÄÝîæ:=ÄÊPKE(0)[4]),(ÄÝîç:=ÄÊPKE(0)[5]),(ÄÝîè:=ÄÊPKE(0)[6]),(ÄÝîã:=ÄÊPKE(0)[7])),ÄÊDEL(1))[1]
(ÂÒå:=2**3**4)
(ÄÊPSH((lambda*áÑË,**áÑÕ:áÑË[0],lambda*áÑË,**áÑÕ:áÑË[-1])),((Âåß:=ÄÊPKE(0)[0]),(ÂåÔ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
class Named:(ÄÊPSH((lambda áÑÞ,s:ÂåÔ((ÄÊPSH(s),ÄÊPSH(áÑÞ),ÄÊPSH('s'),setattr(ÄÊPKE(1),ÄÊPKE(0),ÄÊPKE(2)),ÄÊDEL(3))[3],None),lambda áÑÞ:áÑÞ.s)),((__init__:=ÄÊPKE(0)[0]),(__repr__:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÂÞÅ:=(NULL:=Named('␀')))
(ÄÊPSH((Named('\U000f0b88'),Named('\U000f18e9'),Named('⬤'))),((ÄÔýò:=ÄÊPKE(0)[0]),(ÄÕøü:=ÄÊPKE(0)[1]),(ÂýÃ:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
class ÂÐô:None
(ÂÑÅ:=áÍÞ)
(ÂÐý:=áÍÛ|ÂÑÅ)
(ÂÐá:=complex)
(ÂÁÍ:=lambda Æå,*áÑË,**áÑÕ:lambda*áÑË,**áÑÕ:Æå(áÑË[1],áÑË[0],*áÑË[slice(2,None)],**áÑÕ)if ãÊú(áÑË)>=2 else Æå(*áÑË,**áÑÕ))
(ËßØ:=lambda Æå,*áÑË,**áÑÕ:lambda*áÑË,**áÑÕ:Æå(áÑË[0],*áÑË,**áÑÕ))
(ÂÖë:=lambda Æå,*áÑË,**áÑÕ:lambda*áÑË,**áÑÕ:Æå(*áÑË[0],**áÑÕ))
(ãÊú:=len)
(ÄÕÍÔ:=lambda*áÑË,áØÁ=ÂÞÅ,**áÑÕ:(áÑË[0]if áØÁ is ÂÞÅ else áØÁ)if áÑË else(lambda*áÑË,**áÑÕ:áÑË[0]if áÑË else ÄÕÍÔ)if áØÁ is ÂÞÅ else lambda*áÑË,**áÑÕ:áØÁ)
(CUR:=lambda Æå,*áÖÒ,**áÖÝ:Æå(*áÖÒ,**áÖÝ)if ãÊú(áÖÒ)>=2 else lambda*áÖÓ,**áÖÞ:CUR(Æå,*áÖÒ,*áÖÓ,**áÖÝ|áÖÞ))
(CURR:=lambda Æå,*áÖÒ,**áÖÝ:Æå(*áÖÒ,**áÖÝ)if ãÊú(áÖÒ)>=2 else lambda*áÖÓ,**áÖÞ:CUR(Æå,áÖÓ[0],*áÖÒ,*áÖÓ[slice(1,None)],**áÖÝ|áÖÞ))
(ÁØò:=(ÁÙÇ:=lambda Æå:lambda áØÆ,*áÖÒ,**áÖÝ:[áÑÿ for v in áØÆ if(áÑÿ:=Æå(v,*áÖÒ,**áÖÝ))is not ÄÔýò]))
(ÁØòþë:=(ÁÙÇþë:=lambda Æå:lambda áØÆ,*áÖÒ,**áÖÝ:[áÑÿ for(ÄÝõÌ,v)in ÂÓÏ(áØÆ)if(áÑÿ:=Æå(v,ÄÝõÌ,áØÆ,*áÖÒ,**áÖÝ))is not ÄÔýò]))
(ÁØÿþÁÙÄ:=lambda Æå:Æå)
(ÁØòþÁÙÄ:=lambda Æå:lambda áØÆ,áØÇ,*áÖÒ,**áÖÝ:[áÑÿ for v in áØÆ if(áÑÿ:=Æå(v,áØÇ,*áÖÒ,**áÖÝ))is not ÄÔýò])
(ÁØÿþÁÙÇ:=lambda Æå:lambda áØÆ,áØÇ,*áÖÒ,**áÖÝ:[áÑÿ for v in áØÇ if(áÑÿ:=Æå(áØÆ,v,*áÖÒ,**áÖÝ))is not ÄÔýò])
(ÁØòþÁÙÄþë:=lambda Æå:lambda áØÆ,áØÇ,*áÖÒ,**áÖÝ:[áÑÿ for(ÄÝõÌ,v)in ÂÓÏ(áØÆ)if(áÑÿ:=Æå(v,áØÇ,ÄÝõÌ,áØÆ,*áÖÒ,**áÖÝ))is not ÄÔýò])
(ÁØÿþÁÙÇþë:=lambda Æå:lambda áØÆ,áØÇ,*áÖÒ,**áÖÝ:[áÑÿ for(ÄÝõÌ,v)in ÂÓÏ(áØÇ)if(áÑÿ:=Æå(áØÆ,v,ÄÝõÌ,áØÇ,*áÖÒ,**áÖÝ))is not ÄÔýò])
(ÁØòþÁÙÇ:=lambda Æå:lambda áØÆ,áØÇ,*áÖÒ,**áÖÝ:[áÑÿ for(x,y)in ÄÕåØ(áØÆ,áØÇ)if(áÑÿ:=Æå(x,y,*áÖÒ,**áÖÝ))is not ÄÔýò])
(ÁØòþÁÙÇþë:=lambda Æå:lambda áØÆ,áØÇ,*áÖÒ,**áÖÝ:[áÑÿ for(ÄÝõÌ,(x,y))in ÂÓÏ(ÄÕåØ(áØÆ,áØÇ))if(áÑÿ:=Æå(x,y,ÄÝõÌ,áØÆ,áØÇ,*áÖÒ,**áÖÝ))is not ÄÔýò])
(ÄÊPSH((lambda x,y:(False if y else x)if x else y,lambda x,y:(y if y else False)if x else x if y else True)),((ÄÝøø:=ÄÊPKE(0)[0]),(ÄÝøú:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÂÕÕ:=(Âùè:=lambda x,y:x or y))
(ÄÝøù:=(ÄÝùÀ:=lambda x,y:not(x or y)))
(ÂÕÔ:=(Âùç:=lambda x,y:x and y))
(ÄÝøå:=(ÄÝùÁ:=lambda x,y:(False if y else x)if x else y if y else True))
(ÄÊPSH((__lt__,__gt__,__le__,__ge__)),((ÿ:=ÄÊPKE(0)[0]),(ÁÁ:=ÄÊPKE(0)[1]),(ÂÖÔ:=ÄÊPKE(0)[2]),(ÂÖÕ:=ÄÊPKE(0)[3])),ÄÊDEL(1))[1]
(ÄÊPSH((lambda x,y:gcd(x,y)==x,lambda x,y:gcd(x,y)!=x)),((ÂÕÐ:=ÄÊPKE(0)[0]),(ÂÕÑ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH((lambda x,y:x in y,lambda x,y:x not in y)),((ÂÔó:=ÄÊPKE(0)[0]),(ÂÔô:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH((lambda x,y:y in x,lambda x,y:y not in x)),((ÂÔö:=ÄÊPKE(0)[0]),(ÂÔø:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH((lambda x,y:{*x}.issubset({*y}),lambda x,y:{*y}.issubset({*x}))),((ÂÖó:=ÄÊPKE(0)[0]),(ÂÖô:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH((lambda x,y:not ÂÖó(x,y),lambda x,y:not ÂÖô(x,y))),((ÂÖõ:=ÄÊPKE(0)[0]),(ÂÖö:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH((lambda x,y:((Ïß:={*x}).issubset((Ïà:={*y}))and Ïß)!=Ïà,lambda x,y:((Ïß:={*y}).issubset((Ïà:={*x}))and Ïß)!=Ïà)),((ÂÖü:=ÄÊPKE(0)[0]),(ÂÖý:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH((lambda x,y:not ÂÖü(x,y),lambda x,y:not ÂÖý(x,y))),((ÄÝøÄ:=ÄÊPKE(0)[0]),(ÄÝøÅ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÝöú:=lambda x,y:ÂÕÃ(ÂÕØ(x,y),ÂÕÖ(x,y)))
(ÂÕØ:=lambda x,y:{*x}|{*y}if ÁØö(x,áÍè)else[*x,*[z for z in y if z not in x]])
(ÂÕÖ:=lambda x,y:{*x}&{*y}if ÁØö(x,áÍè)else[z for z in x if z in y])
(ÄÝöù:=lambda x,y:not ÂÕÖ(x,y))
(ÂÕÃ:=lambda x,y:x-{*y}if ÁØö(x,áÍè)else[z for z in x if z not in y])
(ÂøÚ:=lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:Áÿú(product(*([áØÆ]*áØÁ if áØÇ is ÂÞÅ and áØÁ is not ÂÞÅ else([áØÆ,áØÇ]if áØÇ is not ÂÞÅ else áØÆ)*(áØÁ if áØÁ is not ÂÞÅ else 1))),áÍá))
(ÂØÑ:=lambda*áÑË,áØÁ=1:(Æå:=lambda*áÑË,n=1,r=[]:(lambda ÂîÓ:Áÿú(ÂîÓ[0],lambda x:Æå(*ÂîÓ[slice(1,None)],r=r+[x])if ãÊú(ÂîÓ)>1 else r+[x]))(áÑË*n))(*áÑË,n=áØÁ))
(ÄÊPSH((lambda x,y:x%y,lambda x,y:x//y)),((æ:=ÄÊPKE(0)[0]),(ÃËÕ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH((lambda x,y:x is y,lambda x,y:x is not y)),((ÂÕó:=ÄÊPKE(0)[0]),(ÂÕõ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH((lambda x:~x,lambda x,y:x@y)),((ÂÄ:=ÄÊPKE(0)[0]),(ÁÃ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄÊPSH((lambda x,y:x|y,lambda x,y:x&y,lambda x,y:x^y)),((ÂÂ:=ÄÊPKE(0)[0]),(ç:=ÄÊPKE(0)[1]),(Áâ:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
(ÄÊPSH((lambda x,y:x**y,lambda x:not x,lambda áØÆ,áØÁ=ÂÞÅ:lambda x:MOD(î,áØÁ=áØÁ)(áØÆ))),((ÂÙû:=ÄÊPKE(0)[0]),(Âó:=ÄÊPKE(0)[1]),(Âö:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
(ÂÀÇ:=lambda áØÆ:ÄÝöì(ÂÀÇ(ÄÝöì(áØÆ)))if ÁØö(áØÆ,áÍÞ)else áØÆ[slice(None,None,-1)]if ÁØö(áØÆ,áÍî|ÁÜÙ|áÍá|áÍé)else áØÆ.__reversed__()if hasattr(áØÆ,'__reversed__')else[*áØÆ][slice(None,None,-1)])
(ÄÝöí:=lambda áØÆ=ÂÞÅ,áØÁ=ÂÞÅ:chr(áØÆ)if ÁØö(áØÆ,áÍÞ)else ord(áØÆ)if ÁØö(áØÆ,ÁÜÙ)and(ãÊú(áØÆ)==1 and áØÁ is not áÍá)else MOD(Áëý,áØÁ=ÁØö(áØÆ[0],áÍÞ))(Áÿú(áØÆ,ÄÝöí),Âøî))
(ÂÛê:=lambda áØÆ,áØÁ=ÂÞÅ:MOD(ÂÛê,áØÁ=ÂÔö(áØÆ,'\u205f')*'\u205f'+'\u2009')(áØÆ)if áØÁ is ÂÞÅ else MOD(Áëý,áØÁ=ãÊú(áØÁ)>1)(áØÆ.split(áØÁ[0]),MOD(ÁØò(lambda ÂîÓ:MOD(ÂÛê,áØÁ=áØÁ[slice(1,None)])(ÂîÓ)))))
(Âäû:=lambda áØÆ,áØÁ=ÂÞÅ:ÄÝõé(Áÿú(ÄÝõé(áØÆ),MOD(Âäû,áØÁ=áØÁ)))if MOD(ÁØö,áØÁ=ÂÕó)(áØÆ,ÂÐá)else áÍÞ(round(áØÆ))if áØÁ is ÂÞÅ else round(áØÆ,áØÁ))
(ÄÊPSH((floor,ceil)),((Âüð:=ÄÊPKE(0)[0]),(Âüï:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÂÛÅ:=lambda áØÆ,áØÁ=ÂÞÅ:MOD(ÄÕåØ,áØÁ=áØÁ)(áØÆ))
(Âüá:=ÁÜÙ.strip)
def ÂÖÑ(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
	if áØÁ is ÂÞÅ:return áØÆ==áØÇ
	if áÓó(áØÁ):return áØÁ(áØÆ)==áØÁ(áØÇ)
	if áÓö(áØÁ):(ÄÊPSH(áØÁ),ÄÊPSH(ãÊú(ÄÊPKE(0))),(áØÁ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	return x%áØÁ==y%áØÁ
(ÂÖÐ:=lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:not MOD(ÂÖÑ,áØÁ=áØÁ)(áØÆ,áØÇ))
(ÂØú:=lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:áØÆ*áØÇ if áØÁ is ÂÞÅ else áØÆ*áØÇ%MOD(Áëý,áØÁ=áÓö)(áØÁ,ãÊú))
(ÄÃ:=lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:áØÆ/áØÇ if áØÁ is ÂÞÅ else áØÆ/áØÇ%MOD(Áëý,áØÁ=áÓö)(áØÁ,ãÊú))
(ÃËÕ:=lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:áØÆ//áØÇ if áØÁ is ÂÞÅ else MOD(ÂÙû,áØÁ=-MOD(Áëý,áØÁ=áÓö)(áØÁ,ãÊú))(áØÆ,áØÇ))
(ÂÙû:=lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:áØÆ**áØÇ if áØÁ is ÂÞÅ else pow(áØÆ,áØÇ,MOD(Áëý,áØÁ=áÓö)(áØÁ,ãÊú)))
def ì(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):(v:=+áØÆ if áØÇ is ÂÞÅ else áØÆ+áØÇ);return v if áØÁ is ÂÞÅ else v%MOD(Áëý,áØÁ=áÓö)(áØÁ,ãÊú)
def î(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):(v:=-áØÆ if áØÇ is ÂÞÅ else áØÆ-áØÇ);return v if áØÁ is ÂÞÅ else v%MOD(Áëý,áØÁ=áÓö)(áØÁ,ãÊú)
(ÂÕÀ:=lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:[MOD(î,áØÁ=áØÁ)(áØÆ),MOD(ì,áØÁ=áØÁ)(áØÆ)]if áØÇ is ÂÞÅ else[MOD(î,áØÁ=áØÁ)(áØÆ,áØÇ),MOD(ì,áØÁ=áØÁ)(áØÆ,áØÇ)])
(Âù:=lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:[MOD(ì,áØÁ=áØÁ)(áØÆ),MOD(î,áØÁ=áØÁ)(áØÆ)]if áØÇ is ÂÞÅ else[MOD(ì,áØÁ=áØÁ)(áØÆ,áØÇ),MOD(î,áØÁ=áØÁ)(áØÆ,áØÇ)])
def ÂØô(áÍÒ,áØÁ=True):
	for áØÁ in áÍÒ:
		if not not áØÁ:continue
		break
	return áØÁ
def ÂØõ(áÍÒ,áØÁ=False):
	for áØÁ in áÍÒ:
		if not áØÁ:continue
		break
	return áØÁ
def ÄÝõÓ(áÍÒ,áØÁ=False):
	if not ãÊú(áÍÒ):return áØÁ
	(r:=True)
	for áØÁ in áÍÒ:
		if áØÁ:(r:=áØÁ)
		else:return r
	return not r
def ÄÝõÔ(áÍÒ,áØÁ=True):
	if not ãÊú(áÍÒ):return áØÁ
	(r:=False)
	for áØÁ in áÍÒ:
		if áØÁ:return r
		else:(r:=áØÁ)
	return not r
def ÐÌü(Æå,*áÑË,**áÑÕ):
	if áÓó(Æå):return Æå(*áÑË,**áÑÕ)
	if áÓö(Æå):
		for x in Æå:None
		return Æå
	ÄÊPOP(0)if ÄÊPSH(False)else ÂùÆ(ÄÊPOP(0),'%s is not iterable or callable.'%(Æå,))
class Ticker:(__slots__:=('i',));(__init__:=lambda áÑÞ,i:ÂåÔ((ÄÊPSH(áÑÞ),ÄÊPSH('i'),ÄÊPSH(i),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3],None));(__call__:=lambda áÑÞ,*áÑË,**áÑÕ:ÂåÔ((ÄÊPSH(áÑÞ),ÄÊPSH('i'),ÄÊPSH(getattr(ÄÊPKE(1),ÄÊPKE(0))),ÄÊPSH(ÄÊPKE(0)-1),setattr(ÄÊPKE(3),ÄÊPKE(2),ÄÊPKE(0)),ÄÊDEL(4))[4],áÑÞ));(__bool__:=lambda áÑÞ:not áÑÞ.i);(__repr__:=lambda áÑÞ:'Ticker[i=%s]'%(áÑÞ.i,))
class TimerState:(__init__:=lambda áÑÞ,áÓË:ÂåÔ((ÄÊPSH(áÑÞ),ÄÊPSH('áÓË'),ÄÊPSH(áÓË),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3],None));(__bool__:=lambda áÑÞ:áÑÞ.áÓË.s);(__call__:=lambda áÑÞ:áÑÞ.áÓË.r if áÑÞ else ÐÌü(áÑÞ.áÓË.r.copy));(__repr__:=lambda áÑÞ:'Timer[%s; %ss; %s; %s Remaining loops]=%s'%('ID'[áÑÞ.áÓË.y>=0],ÂüÌ(áÑÞ.áÓË.y),'Running'if áÑÞ else'Completed',áÑÞ.áÓË.n,áÑÞ.áÓË.r))
(tmp:={'ᴍ':'Áÿú','ꟿ':'ËãÂ','ſ':'ÆÑ','Ϝ':'ÐÌ','\U000f0233':'ÄÔÔè','\U000f0232':'ÄÔÔç','\ueb86':'ÐÌÛ','\U000f04bc':'ÄÔàÑ','\U000f04bd':'ÄÔàÒ','ᙎ':'Ááæ','ᙡ':'Ááú','ᗢ':'Áßô','ᙧ':'ÁâÁ','⊚':'ÂØÍ','⊜':'ÂØÏ','🟕':'ãéÜ','🟖':'ãéÝ','⊛':'ÂØÎ','⍟':'ÂÛÜ','○':'Âåæ','⍜':'ÂÛÙ','\U000f0b2b':'ÄÔüÑ','\U000f0b29':'ÄÔüÏ','\uf071':'ÐâÄ','\U000f0536':'ÄÔâÑ','\uea6c':'ÐÇò','\U000f147c':'ÄÕåØ','\U000f7e45':'ÄÝöÔ','\U000f7e62':'ÄÝöò','\U000f7e63':'ÄÝöó','⪡':'Âúù','⪢':'Âúú','\U000f0e35':'ÄÕÊÂ','\U000f0e37':'ÄÕÊÄ','⤉':'ÂóÍ','⤈':'ÂóÌ','⟷':'Âîí','\U000f7e4c':'ÄÝöÜ','\U000f7e4d':'ÄÝöÝ','\U000f7e4e':'ÄÝöÞ','\U000f7e51':'ÄÝöá','\U000f7e39':'ÄÝöÈ','\U000f7e3a':'ÄÝöÉ','\U000f7e38':'ÄÝöÇ','\U000f7e3b':'ÄÝöÊ','⨝':'Âøî','⟕':'ÂîÊ','⟖':'ÂîË','⟗':'ÂîÌ','⫰':'ÂüÌ','⫯':'ÂüË','\U000f7e52':'ÄÝöâ','\U000f7e53':'ÄÝöã','\U000f7e54':'ÄÝöä','\U000f7e55':'ÄÝöå','\U000f7e56':'ÄÝöæ','\U000f7e13':'ÄÝõà','\U000f7e3c':'ÄÝöË','\U000f7e14':'ÄÝõá','\ue270':'ÏäÒ','\U000f114f':'ÄÕØÃ','\uf074':'ÐâÇ'})
(ENC:='ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýÿ')
(RCD:=CURR(lambda ÂîÓ,ÂîÒ:ÂÖõ(ÂîÓ,ÂîÒ),'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'+'_'))
(SPE:=CURR(lambda ÂîÓ,ÂîÒ:ÂÖó(ÂîÓ,ÂîÒ),ENC+'þ'))
(enc:=MOD(lambda ÂîÓ:Âøî(ÁØò(lambda ÂîÓ:ÄÝöì(ÄÝöí(ÂîÓ),ãÊú(ENC),C=ENC))(ÂîÓ),'þ')))
(dec:=MOD(lambda ÂîÓ:Âøî(ÁØò(lambda ÂîÓ:ÄÝöí(ÄÝöì(ÂîÓ,ãÊú(ENC),C=ENC)))(ÄÝöÞ(ÂîÓ,'þ')))))
(PEV:=MOD(lambda ÂîÓ:Âøî(MOD(ÄÔÔç,áØÁ=enc)(áÇù(ÂîÓ,RCD),RCD))))
(VEP:=MOD(lambda ÂîÓ:Âøî(MOD(ÄÔÔç,áØÁ=MOD(lambda ÂîÓ:MOD(Áëý,áØÁ=SPE)(ÂîÓ,ÄÔâÑ(dec,lambda x:'⸮%s?'%(x,)))))(áÇù(ÂîÓ,SPE),SPE))))
def OPWRAP_(*áÖê):
	def R(Æå):
		for x in áÖê:(ÄÊPSH(globals()),ÄÊPSH(tmp[x]if x in tmp else PEV(x)),ÄÊPSH(MOD(Æå,x)),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
	return R
(ÄÊPSH((callable,lambda x:hasattr(x,'__iter__'))),((áÓó:=ÄÊPKE(0)[0]),(áÓö:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
def áÓõ(x):
	try:return hash(x)
	except áÍÚ:pass
	return False
(áÍÇ:=lambda x,y='utf-8',*áÑË,**áÑÕ:x.encode(y,*áÑË,**áÑÕ)if ÁØö(x,ÁÜÙ)else x.decode(y,*áÑË,**áÑÕ))
class ÃÆë(áÍÞ):(__new__:=lambda ÂÑÎ:áÍÞ.__new__(ÂÑÎ,1));(__call__:=lambda*áÑË,**áÑÕ:ÃÆë);(__repr__:=lambda áÑÞ:'ⴳ')
class ÃÆì(áÍÞ):(__new__:=lambda ÂÑÎ:áÍÞ.__new__(ÂÑÎ,0));(__call__:=lambda*áÑË,**áÑÕ:ÃÆì);(__repr__:=lambda áÑÞ:'ⴴ')
(ÃÆë:=ÃÆë())
(ÃÆì:=ÃÆì())
def ÂùÆ(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
	if ÂÞÅ is áØÇ and ÁØö(áØÆ,áÍÚþáÍÚ):(ÄÊPSH((False,áØÆ)),((áØÆ:=ÄÊPKE(0)[0]),(áØÇ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	elif áØÆ:return áØÆ
	(E:=ÂÞÅ is not áØÇ and ÁØö(áØÇ,áÍÚþáÍÚ));(áØÅ:='MOON_WARNING_IS_ERR'in env);(áÖð:=áØÅ or'MOON_DEPRECATION_IS_ERR'in env)
	if áØÁ is ÄÔáô:(ÄÊPSH((áÖð,'Deprecation %s'%('Error'if áÖð else'Warning',))),((áÓÔ:=ÄÊPKE(0)[0]),(áÓà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	elif áØÁ is ÂÄ:(ÄÊPSH((áØÅ,'Warning%s'%(' [as Error]'if áØÅ else ÁØã,))),((áÓÔ:=ÄÊPKE(0)[0]),(áÓà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	else:(ÄÊPSH((True,'Assertion failed')),((áÓÔ:=ÄÊPKE(0)[0]),(áÓà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	(ÄÊPSH(áÓà),ÄÊPSH(ÄÊPKE(0)+' ⟨%s⟩%s'%(áØÆ,' '+('%s(%s)'%(ÁØö(áØÇ).__name__,Âøî(getattr(áØÇ,'args',ÂÚü()),','))if E else ÂÞÅCAT(áØÇ,ÁÜÙ))if áØÇ is not ÂÞÅ else ÁØã)),(áÓà:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	try:Âçß(termclr(áÓà,'f22'if áÓÔ else'ff2'))
	except áÍÚ as Ðáü:Âçß(áÓà)
	if áÓÔ:
		if E:raise áØÇ
		raise ÂÞÅCAT(áÓà,AssertionError)
	return áØÆ
@OPWRAP_(*'\uf071\U000f0536\uea6c')
def _(áÑã,Æå=ÂÞÅ,Ëðá=ÂÞÅ,áØÁ=áÍÚ):
	(ÄÊPSH((áØÁ,ÂÕÃ([Æå,Ëðá],[ÂÞÅ]))),((áÍÎ:=ÄÊPKE(0)[0]),(v:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	if ãÊú(v)==1:
		(Æå:=v[0])
		if áÑã=='\uf071':raise Æå
	elif ãÊú(v)==2:
		if áÑã=='\uf071'and ÄÝøÇ(Æå,áÓó):
			if Æå:return Æå
			raise Ëðá
	def r(*áÑË,**áÑÕ):
		try:return Æå(*áÑË,**áÑÕ)
		except áÍÎ as Ïã:
			if ãÊú(v)==1:
				if áÑã=='\U000f0536':return áÑË[0]if áÑË else None
				if áÑã=='\uea6c':return Ïã
			if áÑã=='\uf071':return Ëðá
			if áÑã=='\U000f0536':return Ëðá(*áÑË,**áÑÕ)
			if áÑã=='\uea6c':return Ëðá(Ïã)
	return r
def Âáõ(*áÑË,áÌÄ=None):
	(ÄÊPSH(áÑË),(*(áÑË:=ÄÊPKE(0)[slice(0,-1,None)]),(Æå:=ÄÊPKE(0)[-1])),ÄÊDEL(1))[1]
	if not áÌÄ:(áÌÄ:=ÂÚü())
	if not áÑË:return Æå(*áÌÄ)
	with áÑË[0]as áÌß:return áÌÄ.append(áÌß)or Âáõ(*áÑË[slice(1,None)],Æå,áÌÄ=áÌÄ)
def Âçß(*áÑË,ÂìÆ=False,áÖý=' ',áØÁ='\n'):
	(Æå:=áÐÙþÂÐüþÂÐü if ÂìÆ else áÐãþáÐéþáÐè).write(Âøî(áÑË,ÁÜÙ(áÖý))+ÁÜÙ(áØÁ));Æå.flush()
	if áÑË:return áÑË[0]
def ÁØö(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ,TYPELIKE={áÓó,áÓõ,áÓö},TYPEE=áÍé|áÍá|type|UnionType):
	if áØÇ is ÂÞÅ:return type(áØÆ)
	if áØÇ in TYPELIKE:return áØÇ(áØÆ)
	if áØÁ is ÂÞÅ:
		if áØÇ is ÂÐô:return ÁØö(áØÆ,áÍÖ|áÍÞ)and áØÆ>=0
		elif áØÇ is ÂÑÅ:return ÁØö(áØÆ,ÂÐô|áÍÞ)
		elif áØÇ is ÂÐý:return ÁØö(áØÆ,ÂÑÅ|ÂÐý)
		elif áØÇ is ÂÐá:return ÁØö(áØÆ,ÂÐý|complex)
	return isinstance(áØÆ,áØÇ if isinstance(áØÇ,TYPEE)else type(áØÇ))
(ÄÊPSH((lambda áØÆ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:MOD(ÁØö,áØÁ=áØÁ)(áØÇ,áØÆ),lambda áØÆ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:not MOD(ÁØö,áØÁ=áØÁ)(áØÆ,áØÇ),lambda áØÆ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:not MOD(ÁØö,áØÁ=áØÁ)(áØÇ,áØÆ))),((ÁØñ:=ÄÊPKE(0)[0]),(ÄÝøÇ:=ÄÊPKE(0)[1]),(ÄÝøÆ:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
(Âõ:=lambda áØÁ:ÁØò(lambda ÂîÓ:ÄóÌÁ(ÂÞÅCAT(Ïò,áØÁ**-1)*(ÂîÓ+ÃÆ*(áØÁ<0)))+ÂÞÅCAT(Ãù,ÄóÌÀ(ÂÞÅCAT(Ïò,áØÁ**-1)*(ÂîÓ+ÃÆ*(áØÁ<0)))))(ÂÿÇ(ÂüÌ(áØÁ))))
(ÂÕÇ:=lambda áØÆ=ÂÞÅ,áØÁ=2:áØÆ**áØÁ**-1)
(ÚÑ:=lambda áØÆ,áØÁ=2:ÁØò(lambda ÂîÓ:ÂîÓ*áØÆ**áØÁ**-1)(MOD(Âõ,áØÁ=ÂüÌ(áØÁ))))
(ÐàÒ:=lambda áØÆ,*áÑË,**áÑÕ:lambda*áÑË,**áÑÕ:áØÆ(*ÄÔÙù(áÑË),**áÑÕ))
(ÂÕì:=lambda áØÆ,*áÑË,**áÑÕ:lambda*áÑË,**áÑÕ:áØÆ(*ÂÀÇ(áÑË),**áÑÕ))
(ë:=lambda x,y:x*y)
(ð:=lambda x,y:x/y)
(ÄÔáô:=áÍä())
(ÄÊPSH((gcd,lcm,log,sin,cos,tan)),((ÄóÌÐ:=ÄÊPKE(0)[0]),(ÄóÌÑ:=ÄÊPKE(0)[1]),(ÄóÍÀ:=ÄÊPKE(0)[2]),(ÄóÌÀ:=ÄÊPKE(0)[3]),(ÄóÌÁ:=ÄÊPKE(0)[4]),(ÄóÌÂ:=ÄÊPKE(0)[5])),ÄÊDEL(1))[1]
class Holder:
	(__slots__:=('x',))
	def __init__(áÑÞ,x=ÂÞÅ):(ÄÊPSH(áÑÞ),ÄÊPSH('x'),ÄÊPSH(x),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
	def __pos__(áÑÞ):return Âåß(áÑÞ.x,ÄÊPOP(0)if ÄÊPSH(áÑÞ.x is not ÂÞÅ)else ÂùÆ(ÄÊPOP(0),'Holder value unset!'))
	def __call__(áÑÞ,x=ÂÞÅ):(ÄÊPSH(áÑÞ),ÄÊPSH('x'),ÄÊPSH(x),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
	def __bool__(áÑÞ):return áÑÞ.x is not ÂÞÅ
def proxy_chained_calls_pure(Æå,n=1):
	def j(*áÔå,_PAIRS=None,**áÔï):
		if _PAIRS is None:(_PAIRS:=ÂÚü())
		(_PAIRS:=[*_PAIRS,(áÔå,áÔï)])
		if ãÊú(_PAIRS)==n:
			(G:=Æå(*_PAIRS[0][0],**_PAIRS[0][1]))
			for(A,K)in _PAIRS[slice(1,None)]:(G:=G(*A,**K))
			return G
		return lambda*áÑË,**áÑÕ:j(*áÑË,_PAIRS=_PAIRS,**áÑÕ)
	return j
__dir__=(__file__:=áÌî(moon_dir/'Builtins/system.☾')).parent
from time import time,sleep
def PL_MEM_USAGE():
	try:import psutil;(áÖý:=ÐÌü(psutil.Process));return ÐÌü(áÖý.memory_info).rss
	except áÍÚ:pass
	ÄÊPOP(0)if ÄÊPSH(False)else MOD(ÂùÆ,áØÁ=ÂÄ)(ÄÊPOP(0),'Failed to get memory! Do you have psutil installed?');return 0
def PL_CPU_COUNT():import multiprocessing;return ÐÌü(multiprocessing.cpu_count)
def PL_THREAD(Æå,*áÑË,**áÑÕ):from threading import Thread as T;(atom:=[]);ÐÌü((t:=T(target=lambda:ÂÞÅCAT(Æå(*áÑË,**áÑÕ),atom.append))).start);return lambda*áÑË,**áÑÕ:ÂåÔ(ÐÌü(t.join),atom[0])
def PL_WAIT_PID(p):
	try:os.kill(p,0)
	except áÍÚ as Ðáü:return
	os.waitpid(p,0)
def PL_CHECK_PID(p):return not os.waitpid(p,os.WNOHANG)[0]
def PL_FORK(Æå,*áÑË,**áÑÕ):
	if env.get('MOON_NO_FORK'):return ÂÞÅCAT(ÂÞÅCAT(Æå(*áÑË,**áÑÕ),pdump),pload)
	from multiprocessing import shared_memory;(áÓà:=shared_memory.SharedMemory(create=True,size=2**20));(áÑÅ:=MOD(lambda ÂîÓ:ÂîÓ[slice(4,4+struct.unpack('I',ÂîÓ[slice(None,4)])[0])]));(p:=ÐÌü(os.fork))
	if p:return p,lambda*áÑË,**áÑÕ:Âåß(ÂåÔ(ÂÞÅCAT(p,PL_WAIT_PID),ÂÞÅCAT(áÑÅ(áÓà.buf),pload)),ÂåÔ(ÐÌü(áÓà.close),ÐÌü(áÓà.unlink)))
	(v:=ÂÞÅCAT(Æå(*áÑË,**áÑÕ),pdump));(ÄÊPSH(áÓà.buf),ÄÊPSH(slice(None,4)),ÄÊPSH(struct.pack('I',ãÊú(v))),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3];(ÄÊPSH(áÓà.buf),ÄÊPSH(slice(4,4+ãÊú(v))),ÄÊPSH(v),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3];ÂÞÅCAT(0,os._exit)
def PL_SLEEP(x):sleep(x)
def PL_TIME():return ÐÌü(time)
def PL_TEXT_COPY(x):
	try:from clipboard import copy;return copy(x)
	except áÍÚ:pass
	ÄÊPOP(0)if ÄÊPSH(False)else MOD(ÂùÆ,áØÁ=ÂÄ)(ÄÊPOP(0),'Failed to copy! Do you have clipboard installed?')
def PL_TEXT_PASTE():
	try:from clipboard import paste;return paste()
	except áÍÚ:pass
	ÄÊPOP(0)if ÄÊPSH(False)else MOD(ÂùÆ,áØÁ=ÂÄ)(ÄÊPOP(0),'Failed to paste! Do you have clipboard installed?')
def PL_URANDOM(n):return os.urandom(n)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ops_A.☾')).parent
def _map_d(x,y,n=1):
	(mapwd:=lambda x,y:[áÑÿ for z in x if(áÑÿ:=y(z))is not ÄÔýò])
	def _get_d(x):
		if not áÓö(x):return{0}
		if ÁØö(x,ÁÜÙ):return{1}
		return{*ÁØò(lambda ÂîÓ:ÂîÓ+1)(ÄÔÒØ([_get_d(z)for z in x]))}
	def _map_m_d(x,y,n):
		if ÁØö(x,ÁÜÙ):return y(x)if n==1 else x if n else mapwd(x,y)
		if ÂÔö((d:=_get_d(x)),0):return x if n else y(x)
		(x:=mapwd(x,lambda x:_map_m_d(x,y,n)));return y(x)if n in d else x
	def _map_p_d(x,y,i):
		if not i:return y(x)
		if ÁØö(x,ÁÜÙ):return mapwd(x,y)
		if áÓö(x):return mapwd(x,lambda x:_map_p_d(x,y,i-1))
		return y(x)
	return _map_m_d(x,y,-1-n)if n<0 else _map_p_d(x,y,ÂÒå if n is ÂÕË else n)
@OPWRAP_(*'ᴍꟿ')
def _(áÑã,áØÆ=ÂÞÅ,Æå=ÂÞÅ,áØÁ=1):
	(áÖß:=_map_d if áÑã=='ᴍ'else lambda x,y,z:_map_d(x,lambda x:y(*(x if áÓö(x)else[x])),z))
	if ÄÝøÇ(áØÁ,áÍÞ):
		if áØÁ is ë:return ÁØö(áØÆ)(áÖß(áØÆ.items(),Æå,1))
		elif áØÁ is î:return ÁØö(áØÆ)(ÄÕåØ(áÖß(áØÆ.items(),Æå,1),áØÆ.values()))
		elif áØÁ is ì:return ÁØö(áØÆ)(ÄÕåØ(áØÆ.keys(),áÖß(áØÆ.items(),Æå,1)))
	return _map_d(áØÆ,(lambda x:Æå(*(x if áÓö(x)else[x])))if áÑã=='ꟿ'else Æå,áØÁ)
def ÐôÅ(áØÆ=ÂÞÅ,áØÇ=ÐÌü,áØÁ=ÐÌü(PL_CPU_COUNT),m='f'):
	if m=='f':
		if env.get('MOON_NO_FORK'):return ÁØò(lambda ÂîÓ:ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ,áØÇ),pdump),pload))(áØÆ)
		(ÄÊPSH(MOD(ÂÚü,áØÁ=2)()),((P:=ÄÊPKE(0)[0]),(G:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
		for Æå in ÁØò(lambda ÂîÓ:lambda*áÑË,**áÑÕ:PL_FORK(áØÇ,ÂîÓ))(áØÆ):
			while ãÊú((ÄÊPSH(P),ÄÊPSH(ÄÔÔç(ÄÊPKE(0),PL_CHECK_PID)),(P:=ÄÊPKE(0)),ÄÊDEL(2))[2])>=áØÁ:PL_SLEEP(ÄÝôÒ)
			ÁØòþÁÙÇ(lambda ÂîÓ,ÂîÒ:ÂÕÅ(ÂîÓ.append,ÂîÒ))((P,G),ÐÌü(Æå))
		return Áÿú(G,ÐÌü)
	elif m=='t':
		(O:=MOD(ÂÚü,áØÁ=ãÊú(áØÆ))());(Q:=ÁØòþë(lambda ÂîÓ,ÄÝõÌ,ÄÝõË:lambda*áÑË,**áÑÕ:(ÄÊPSH(O),ÄÊPSH(ÄÝõÌ),ÄÊPSH(ÂÞÅCAT(ÂîÓ,áØÇ)),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3])(áØÆ))
		def Æå():
			while Q:
				try:(Ëðà:=ÂÞÅCAT(0,Q.pop))
				except áÍÚ as Ðáü:continue
				ÐÌü(Ëðà)
		Áÿú(ÁØò(lambda ÂîÓ:ÂÞÅCAT(Æå,PL_THREAD))(ÂÿÇ(áØÁ)),ÐÌü);return O
	ÄÊPOP(0)if ÄÊPSH(False)else ÂùÆ(ÄÊPOP(0),'%s is an invalid mode for \uf4bc!'%(m,))
@OPWRAP_(*'\U000f04bc\U000f04bd')
def _(áÑã,áØÆ=ÂÞÅ,Æå=ÄÕÍÔ,ÁÜñ=False):(áØÆ:=[*áØÆ]);(áÖê:=[(áÑÿ,i)for(i,v)in ÂÓÏ(áØÆ)if(áÑÿ:=Æå(v))is not ÄÔýò]);áÖê.sort(reverse=áÑã=='\U000f04bd');return Áÿú(áÖê,(lambda x:x[1])if ÁÜñ else lambda x:áØÆ[x[1]])
@OPWRAP_(*'\U000f0233\U000f0232')
def _(áÑã,áØÆ=ÂÞÅ,Æå=ÂÞÅ,áØÁ=ÂÞÅ,ÁÜñ=False):
	ÄÊPOP(0)if ÄÊPSH(not ÁÜñ or áØÁ is ÂÞÅ)else ÂùÆ(ÄÊPOP(0),'"%sˣᔨ" is invalid'%(áÑã,));(Æå:=ÄÕÍÔ if Æå is ÂÞÅ else Æå if áÓó(Æå)else ÄÊCUR((2,),{},ÂÖÑ,Æå,ÂýÃ))
	if áÑã=='\U000f0233':(Æå:=CUR(lambda ÂîÓ,ÂîÒ:not ÂîÓ(ÂîÒ),Æå))
	if ÁÜñ:return[i for(i,z)in ÂÓÏ(áØÆ)if(áÑÿ:=Æå(z))and áÑÿ is not ÄÔýò]
	if áØÁ is ÂÞÅ:return[z for z in áØÆ if(áÑÿ:=Æå(z))and áÑÿ is not ÄÔýò]
	if áØÁ==ë:return[áÑÿ for z in áØÆ if(áÑÿ:=Æå(z))and áÑÿ is not ÄÔýò]
	if not áÓó(áØÁ):(áØÁ:=MOD(ÄÕÍÔ,áØÁ=áØÁ))
	return[áØÁ(z)if áÑÿ else z for z in áØÆ if(áÑÿ:=Æå(z))is not ÄÔýò]
@OPWRAP_(*'ᙎᙡᗢᙧ')
def _(áÑã,áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ,ÁÜñ=False):
	if ÁÜñ:(ÄÊPSH(áØÆ),ÄÊPSH(ÂÿÇ(ÄÊPKE(0))),(áØÆ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	(chnk:=1)
	if áÓö(áØÇ)and ãÊú(áØÇ)>2:(ÄÊPSH(áØÇ),(*(áØÇ:=ÄÊPKE(0)[slice(0,-1,None)]),(chnk:=ÄÊPKE(0)[-1])),ÄÊDEL(1))[1]
	if áØÇ is not ÂÞÅ:(ÄÊPSH([áØÇ,áØÇ]if ÁØö(áØÇ,áÍÞ)else áØÇ),((áÝÍ:=ÄÊPKE(0)[0]),(áÝÎ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	elif áÑã in'ᙎᙡ':(ÄÊPSH([1,1]),((áÝÍ:=ÄÊPKE(0)[0]),(áÝÎ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	elif áÑã in'ᗢᙧ':(ÄÊPSH([1,1]if áØÁ is ÂÞÅ else[0,áØÁ]),((áÝÍ:=ÄÊPKE(0)[0]),(áÝÎ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	(áÝÏ:=áÑã in'ᙡᙧ');(áÝÐ:=(None if áØÁ is ÂÞÅ else áØÁ)if áÑã in'ᙎᙡ'else ÂÞÅ);(áÝÑ:=(chnk if áØÁ is ÂÞÅ else áØÁ+1)if áÑã in'ᗢᙧ'else chnk);(ÄÊPSH((áØÆ,áÝÍ,áÝÎ,áÝÏ,áÝÐ,áÝÑ)),((áÖê:=ÄÊPKE(0)[0]),(l:=ÄÊPKE(0)[1]),(r:=ÄÊPKE(0)[2]),(m:=ÄÊPKE(0)[3]),(áØÁ:=ÄÊPKE(0)[4]),(ÏÁ:=ÄÊPKE(0)[5])),ÄÊDEL(1))[1]
	if ÁØö(l,áÍÛ):(l:=áÍÞ(l))
	if ÁØö(r,áÍÛ):(r:=áÍÞ(r))
	if ÁØö(ÏÁ,áÍÛ):(ÏÁ:=áÍÞ(ÏÁ))
	(c:=ãÊú((áÖê:=[*áÖê])))
	if áØÁ is ÂÞÅ:return Áÿú(ÂÿÇ(áÖê)[slice(l,c-r,ÏÁ)],lambda x:áÖê[slice(x-l,x)]+MOD(Âêà,áØÁ=áÍÖ(m))(áÖê[x])+áÖê[slice(x+1,x+r+1)])
	(V:=MOD(Âêà,áØÁ=l)(áØÁ)+áÖê+MOD(Âêà,áØÁ=r)(áØÁ));(r:=Áÿú(ÂÿÇ(áÖê)[slice(None,None,ÏÁ)],lambda x:V[slice(x,x+l)]+MOD(Âêà,áØÁ=áÍÖ(m))(V[x+l])+V[slice(x+l+1,x+l+r+1)]))
	if áØÁ is ÄÔýò:return MOD(Áÿú,áØÁ=2)(r,ÄÕÍÔ)
	return r
def ÐÌÛ(áØÆ,Æå=áÍÖ,áØÁ=ÂÞÅ,ÁÜñ=False):
	if not áÓó(Æå):(ÄÊPSH(Æå),ÄÊPSH(CUR(lambda ÂîÓ,ÂîÒ:ÂîÓ==ÂîÒ,ÄÊPKE(0))),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	if áØÁ is not ÂÞÅ:
		(X:=MOD(ÐÌÛ,ÁÜñ=ÁÜñ)(áØÆ,Æå))
		if áØÁ is ë:return ÄÔàÑ(X.items())
		if áØÁ is ì:return Áÿú(ÄÔàÑ(X.items()),lambda x:x[1])
		if áØÁ is áÍÖ:return[X.get(False,ÂÚü()),X.get(True,ÂÚü())]
		ÄÊPOP(0)if ÄÊPSH(False)else ÂùÆ(ÄÊPOP(0),'Invalid modifier for \ueb86!')
	(r:={})
	for(i,z)in ÂÓÏ(áØÆ):
		if(áÑÿ:=Æå(z))is ÄÔýò:continue
		if ÁÜñ:(z:=i)
		if áÑÿ in r:r[áÑÿ].append(z)
		else:(ÄÊPSH(r),ÄÊPSH(áÑÿ),ÄÊPSH([z]),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
	return r
def ÁÞç(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
	if áØÇ is ÂÞÅ:(ÄÊPSH((áØÇ,áØÆ)),((áØÆ:=ÄÊPKE(0)[0]),(áØÇ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	ÄÊPOP(0)if ÄÊPSH(áØÇ is not ÂÞÅ)else ÂùÆ(ÄÊPOP(0),'ᖘ needs right side')
	def Æå(áØÆ):
		(áØÆ:=ÄÔÙù(áØÆ)if(is_str:=ÁØö(áØÆ,ÁÜÙ))else ÐÌü(áØÆ.copy)if ÁØö(áØÆ,áÍÙ)else[*áØÆ]);(ÄÊPSH((MOD(Áëý,áØÁ=áÓó)(áØÁ,MOD(lambda ÂîÓ:ÂîÓ(áØÆ))),[])),((ids:=ÄÊPKE(0)[0]),(TD:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
		if(ÄÝøÆ(ÁÜÙ,ÄÊPSH(ids))and ÁØö(ÄÊPOP(0),ÄÊPSH(áÓö)))and(ÄÊDEL(1)or True)or(ÄÊDEL(1)or False):ÁØòþÁÙÇ(lambda ÂîÓ,ÂîÒ:TD.append(ÂîÓ)if ÂîÒ is ÄÔýò else(ÄÊPSH(áØÆ),ÄÊPSH(ÂîÓ),ÄÊPSH(ÂîÒ),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3])(ids,(V:=áØÇ(ÄÝöÊ(áØÆ,ids))))
		else:ÁØÿþÁÙÇ(lambda ÂîÓ,ÂîÒ:TD.append(ÂîÓ)if ÂîÒ is ÄÔýò else(ÄÊPSH(áØÆ),ÄÊPSH(ÂîÓ),ÄÊPSH(ÂîÒ),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3])(ids,(V:=Âêà(áØÇ(áØÆ[ids]))))
		for x in ÄÔàÒ(TD):del áØÆ[x]
		return Âøî(áØÆ,ÁØã)if is_str else áØÆ
	return Æå if áØÆ is ÂÞÅ else Æå(áØÆ)
(ÆÑ:=lambda áØÆ,áØÇ,áØÁ=ÂÞÅ:reduce(áØÇ,áØÆ,*(()if áØÁ is ÂÞÅ else(áØÁ,))))
(ÐÌ:=lambda áØÆ,áØÇ,áØÁ=ÂÞÅ:[*accumulate(áØÆ,áØÇ,initial=None if áØÁ is ÂÞÅ else áØÁ)])
(ÂøÑ:=lambda áØÆ,áØÁ=ÂÞÅ:(ÁØã if ÁØö(áØÆ,ÁÜÙ)else 0)if((ÄÊDEL(1),False)[1]if ÄÊPSH(áØÆ)else ÄÊPOP(0)if áØÁ is not ÂÞÅ else(ÄÊDEL(1),True)[1])else MOD(ÆÑ,áØÁ=áØÁ)(áØÆ,ì))
(ÂøÐ:=lambda áØÆ,áØÁ=ÂÞÅ:1 if((ÄÊDEL(1),False)[1]if ÄÊPSH(áØÆ)else ÄÊPOP(0)if áØÁ is not ÂÞÅ else(ÄÊDEL(1),True)[1])else MOD(ÆÑ,áØÁ=áØÁ)(áØÆ,ÂØú))
(ÄÕéý:=lambda áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:(lambda Æå:Æå(*ÂÕÃ([áØÆ,áØÇ],[ÂÞÅ])))if áØÁ is ÂÞÅ else áØÁ(*ÂÕÃ([áØÆ,áØÇ],[ÂÞÅ])))
(ÂÔð:=lambda áØÁ=ÂÞÅ:{*''}if áØÁ is ÂÞÅ else ÁØò(lambda ÂîÓ:{*''})(ÂÿÇ(áØÁ)))
(ÂÚü:=lambda áØÁ=ÂÞÅ:[]if áØÁ is ÂÞÅ else ÁØò(lambda ÂîÓ:[])(ÂÿÇ(áØÁ))if áØÁ>0 else ÂØÍ(Âêà,-áØÁ)([]))
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ops_B.☾')).parent
(ÃÆí:=lambda áØÆ,áØÁ=ÂÞÅ:(GET_CASE(áØÆ)if ÁØö(áØÆ,ÁÜÙ)else 1 if áØÆ>0 else-1 if áØÆ<0 else None)or(0 if áØÁ is ÂÞÅ else áØÁ))
(ÄÕÇè:=lambda áØÆ,áØÁ=ÂÞÅ:ÂåÔ(ÄÊPOP(0)if ÄÊPSH(ÁØö(áØÆ,ÂÐá)and áØÁ is ÂÞÅ)else ÂùÆ(ÄÊPOP(0),'\U000f0931'),áØÆ+1))
(ÄÕÇæ:=lambda áØÆ,áØÁ=ÂÞÅ:ÂåÔ(ÄÊPOP(0)if ÄÊPSH(ÁØö(áØÆ,ÂÐá)and áØÁ is ÂÞÅ)else ÂùÆ(ÄÊPOP(0),'\U000f0931'),áØÆ-1))
def ÃÇÆ(áØÆ,áØÇ=ÄÕÍÔ,áØÁ=ÂÞÅ):
	(áØÇ:=ÄÕÍÔ if áØÇ is ÂÞÅ else áØÇ if áÓó(áØÇ)else ÄÊCUR((2,),{},ÂÖÑ,áØÇ,ÂýÃ));ÄÊPOP(0)if ÄÊPSH(áÓó(áØÇ))else ÂùÆ(ÄÊPOP(0),"𝚡 isn't iterable!");ÄÊPOP(0)if ÄÊPSH(áØÁ is ÂÞÅ)else ÂùÆ(ÄÊPOP(0),'\U000f0931');(n:=0)
	for x in áØÆ:
		if not áØÇ(x):continue
		(ÄÊPSH(n),ÄÊPSH(ÄÕÇè(ÄÊPKE(0))),(n:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	return n
def ÁãÁ(áØÆ,áØÇ=ÄÕÍÔ,ÁÜñ=False):
	(ÄÊPSH(([],[])),((s:=ÄÊPKE(0)[0]),(r:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	for(i,z)in ÂÓÏ(áØÆ):
		if not((v:=áØÇ(z))not in s and v is not ÄÔýò):continue
		s.append(v);r.append(i if ÁÜñ else z)
	return r
def Âêà(*áÑË,áØÁ=ÂÞÅ):
	if áØÁ is ÂÞÅ:return[*áÑË]
	if áØÁ is áÍé:return áÍé(áÑË)
	return[*áÑË]*áØÁ if áØÁ>=0 else ÂØÍ(Âêà,ÂüÌ(áØÁ))(*áÑË)
def ÄÔéÄ(áØÆ,áØÇ,áØÁ=ÂÞÅ):(R:=MOD(lambda ÂîÓ:[ÁØã]if ÂîÓ is ÂÞÅ else[ÂîÓ]if ÁØö(ÂîÓ,ÁÜÙ)else Áÿú(ÂîÓ,ÁÜÙ)));(Æå:=MOD(lambda ÂîÓ:MOD(ÆÑ,áØÁ=ÂîÓ)((lambda ÂîÓ,ÂîÒ:MOD(ÄÕåØ,áØÁ=ÄÝöÉ(ÂîÒ))(ÂîÓ,ÂîÒ))(R(áØÆ),R(áØÇ)),lambda x,y:x.replace(*y))));return Æå if áØÁ is ÂÞÅ else Æå(áØÁ)
(ÂÓÏ:=lambda áØÆ,áØÁ=ÂÞÅ:Áÿú(ÂÿÇ(áØÆ),lambda x:(x,áØÆ[x]))if áØÁ is ÂÞÅ else ÄÕåØ(Áÿú(ÂÿÇ(áØÆ),MOD(Âêà,áØÁ=áÍé)),áØÆ)if ÂüÌ(áØÁ)==1 else MOD(Áëý,áØÁ=áØÁ>0)(ËãÂ(ÂÓÏ(áØÆ),lambda x,y:ÁØò(lambda ÂîÓ:((x,*ÂîÓ[0]),ÂîÓ[1]))(MOD(ÂÓÏ,áØÁ=áØÁ-ÃÆí(áØÁ))(y))),ÄÔÙù))
(ÂÿÇ:=lambda áØÆ,áØÁ=ÂÞÅ:ÄÝöÈ(MOD(Áëý,áØÁ=áÓö)(áØÆ,ãÊú))if áØÁ is ÂÞÅ else MOD(Áÿú,áØÁ=ÂüÌ(áØÁ)if áØÁ<0 else 1)(MOD(ÂÓÏ,áØÁ=áØÁ)(MOD(Áëý,áØÁ=Âåæ(Âó,áÓö))(áØÆ,Âåæ(MOD(ÂØÑ,áØÁ=ÂüÌ(áØÁ)),ÂÿÇ))),MOD(lambda ÂîÓ:ÂîÓ[0])))
@OPWRAP_(*'⤉⤈⟷')
def _(áÑã,áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ,ÁÜñ=False):
	if áÑã=='⟷':return MOD(ÂóÌ,áØÁ=áØÁ,ÁÜñ=ÁÜñ)(áØÆ,áØÇ),MOD(ÂóÍ,áØÁ=áØÁ,ÁÜñ=ÁÜñ)(áØÆ,áØÇ)
	(áÍÛ:=ÿ if áÑã=='⤉'else ÁÁ)
	if áØÇ is ÂÞÅ:(ÄÊPSH((áØÆ,ÄÕÍÔ)),((v:=ÄÊPKE(0)[0]),(Æå:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	elif áÓó(áØÇ):(ÄÊPSH((áØÆ,áØÇ)),((v:=ÄÊPKE(0)[0]),(Æå:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	else:(ÄÊPSH(([áØÆ,áØÇ],ÄÕÍÔ)),((v:=ÄÊPKE(0)[0]),(Æå:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	(áÐð:=(áÑÈ:=(áÐø:=ÂÞÅ)))
	for(áÖõ,áÖî)in ÂÓÏ(v):
		if not(áØÆ:=Æå(áÖî))is not ÄÔýò:continue
		if(ÄÊDEL(1),False)[1]if ÄÊPSH(áÑÈ is ÂÞÅ)else ÄÊPOP(0)if áÍÛ(áÑÈ,áØÆ)else(ÄÊDEL(1),True)[1]:continue
		(ÄÊPSH((áÖî,áØÆ,áÖõ)),((áÐð:=ÄÊPKE(0)[0]),(áÑÈ:=ÄÊPKE(0)[1]),(áÐø:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
	return(áÐø if ÁÜñ else áÐð)if áÐð is not ÂÞÅ else áØÁ if áØÁ is not ÂÞÅ else ÐâÄ(ValueError)
(ÄÝöÓ:=lambda áØÆ,áØÇ,áØÁ=ÂÞÅ:(lambda x:ÂóÌ(ÂóÍ(áØÆ,x),áØÇ))if áØÁ is ÂÞÅ else ÂóÌ(ÂóÍ(áØÆ,áØÁ),áØÇ))
def ÄÔÞÔ(áØÆ,Æå=áÍÖ,áØÁ=None,ÁÜñ=False):
	if Æå is ÂÞÅ:(Æå:=áÍÖ)
	elif ÄÝøÇ(Æå,áÓó):(ÄÊPSH(Æå),ÄÊPSH(CUR(lambda ÂîÓ,ÂîÒ:ÂîÓ==ÂîÒ,ÄÊPKE(0))),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	for(i,x)in enumerate(áØÆ):
		if Æå(x):return i if ÁÜñ else x
	return áØÁ
@OPWRAP_(*'\U000f7e53\U000f7e54\U000f7e55\U000f7e56')
def _(áÑã,áØÆ,Æå=áÍÖ,áØÁ=ÂÞÅ,ÁÜñ=False):
	if(ÁØö(áØÆ,ÄÊPSH(ÁÜÙ))and ÁØñ(ÄÊPOP(0),ÄÊPSH(Æå)))and(ÄÊDEL(1)or True)or(ÄÊDEL(1)or False):(Æå:=CUR(lambda ÂîÓ,ÂîÒ:ÂîÓ!=ÂîÒ,Æå))
	(áÖõ:=MOD(ÄÔÞÔ,ÁÜñ=ÄÕøü)(áØÆ,Æå))
	if ÄÝõÒ(áÖõ):
		if áØÁ is not ÂÞÅ:return áØÁ
		return ÁØã if not ÁÜñ and ÁØö(áØÆ,ÁÜÙ)else ÂÚü()
	if ÁÜñ:(ÄÊPSH(áØÆ),ÄÊPSH(ÂÿÇ(ÄÊPKE(0))),(áØÆ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	if áÑã=='\U000f7e53':return áØÆ[slice(None,áÖõ+1)]
	if áÑã=='\U000f7e54':return áØÆ[slice(áÖõ,None)]
	if áÑã=='\U000f7e55':return áØÆ[slice(None,áÖõ)]
	if áÑã=='\U000f7e56':return áØÆ[slice(1+áÖõ,None)]
@OPWRAP_(*'\U000f0e35\U000f0e37')
def _(áÑã,áØÆ,áØÇ,áØÁ=ÂÞÅ):
	if((ÁØö(áØÆ,ÄÊPSH(áÍÞ))and ÁØñ(ÄÊPOP(0),ÄÊPSH(áØÇ)))and(ÄÊDEL(1)or True)or(ÄÊDEL(1)or False))and áØÁ is ÂÞÅ:
		if áÑã=='\U000f0e35':return MOD(ÄÝöì,áØÁ=ÂÞÅCAT(áØÇ,Ãù))(áØÆ)
		(ÄÊPSH(áØÆ),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),ÁÜÙ)),(áØÆ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
		if áØÁ is ÂÞÅ:(áØÁ:=' ')
	if not áÓö(áØÆ):(ÄÊPSH(áØÆ),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),ÁÜÙ)),(áØÆ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	if(l:=áØÇ-ãÊú(áØÆ))>0:
		(r:=[áØÁ if áØÁ is not ÂÞÅ else' 'if ÁØö(áØÆ,ÁÜÙ)else False]*l)
		if áÑã=='\U000f0e35':(r:=ÄÔÙù(r,áØÆ))
		else:(r:=ÄÔÙù(áØÆ,r))
	else:(r:=áØÆ)
	return Âøî(r)if ÁØö(áØÆ,ÁÜÙ)else r
@OPWRAP_(*'\U000f7e39\U000f7e3a\U000f7e38\U000f7e3b')
def _(áÑã,áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ,ÁÜñ=False):
	ÄÊPOP(0)if ÄÊPSH(áØÆ is not ÂÞÅ or ÂÞÅ is not áØÇ)else ÂùÆ(ÄÊPOP(0),'Range missing both values!')
	if(áÑÃ:=áØÁ is ÂÞÅ):(áØÁ:=1)
	(v:=áØÇ if áØÆ is ÂÞÅ else áØÆ if áØÇ is ÂÞÅ else ÂÞÅ)
	if(áØÆ is not ÂÞÅ and ÂÞÅ is not áØÇ)and((ÁØö(áØÆ,ÄÊPSH(áÍÞ))and ÁØñ(ÄÊPOP(0),ÄÊPSH(áØÇ)))and(ÄÊDEL(1)or True)or(ÄÊDEL(1)or False))if v is ÂÞÅ else ÁØö(v,áÍÞ):
		if v is not ÂÞÅ:(ÄÊPSH((0,v)),((áØÆ:=ÄÊPKE(0)[0]),(áØÇ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
		(ÏÁ:=-1 if áØÇ<áØÆ else 1)
		if áÑÃ and ÏÁ==-1:(áØÁ:=-1)
		if áÑã=='\U000f7e39':return[*range(áØÆ,áØÇ,áØÁ)]
		if áÑã=='\U000f7e3a':return[*range(áØÆ+ÏÁ,áØÇ+ÏÁ,áØÁ)]
		if áÑã=='\U000f7e38':return[*range(áØÆ+ÏÁ,áØÇ,áØÁ)]
		if áÑã=='\U000f7e3b':return[*range(áØÆ,áØÇ+ÏÁ,áØÁ)]
	if v is not ÂÞÅ:
		ÂùÆ(ÁØö(v,áÓö));(v:=[*v])
		if áÑã=='\U000f7e38':return v[0],v[slice(1,-1,áØÁ)],v[-1]
		if áÑÃ:(áØÁ:=0)
		if áÑã=='\U000f7e39':return v[0+áØÁ]
		if áÑã=='\U000f7e3a':return v[-1-áØÁ]
		if áÑã=='\U000f7e3b':return v[0+áØÁ],v[-1-áØÁ]
	if ÁØö(áØÆ,slice):(áØÆ:=[*range(áØÆ.start,áØÆ.stop,áØÆ.step)])
	if ÁÜñ:
		if áÓö(áØÆ):(ÄÊPSH(áØÆ),ÄÊPSH(ÂÿÇ(ÄÊPKE(0))),(áØÆ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
		elif áÓö(áØÇ):(ÄÊPSH(áØÇ),ÄÊPSH(ÂÿÇ(ÄÊPKE(0))),(áØÇ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	if áÓö(áØÆ)and áÓö(áØÇ):return[áØÆ[h%ãÊú(áØÆ)]for h in áØÇ[slice(None,None,áØÁ)]]
	if áÓö(áØÆ)and ÁØö(áØÇ,slice):return áØÆ[áØÇ]
	if áÓö(áØÆ)and ÁØö(áØÇ,áÍÞ):
		if áÑã=='\U000f7e39':return áØÆ[slice(None,áØÇ,áØÁ)]
		if áÑã=='\U000f7e3a':return áØÆ[slice(1,áØÇ+1,áØÁ)]
		if áÑã=='\U000f7e38':return áØÆ[slice(1,áØÇ,áØÁ)]
		if áÑã=='\U000f7e3b':return áØÆ[slice(None,áØÇ+1,áØÁ)]
	if ÁØö(áØÆ,áÍÞ)and áÓö(áØÇ):
		if áÑã=='\U000f7e39':return áØÇ[slice(áØÆ,-1,áØÁ)]
		if áÑã=='\U000f7e3a':return áØÇ[slice(áØÆ+1,None,áØÁ)]
		if áÑã=='\U000f7e38':return áØÇ[slice(áØÆ+1,-1,áØÁ)]
		if áÑã=='\U000f7e3b':return áØÇ[slice(áØÆ,None,áØÁ)]
	ÄÊPOP(0)if ÄÊPSH(False)else ÂùÆ(ÄÊPOP(0),'Invalid argument types! %s %s'%(ÁØö(áØÆ),ÁØö(áØÇ)))
def áÇù(x,y=ÂÞÅ,áØÁ=ÂÒå,ÁÜñ=False):
	if not x:return[]
	if ÁØö(x,áÍÞ):(ÄÊPSH(x),ÄÊPSH(ÂÿÇ(ÄÊPKE(0))),(x:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	if y is ÂÞÅ:(y:=ÄÕÍÔ)
	if ÁÜñ:return MOD(áÇù,áØÁ=áØÁ)(ÂÿÇ(x),(lambda i:y(x[i]))if áÓó(y)else y)
	elif ÁØö(y,áÍÞ):return[x[slice(None,y)],x[slice(y,None)]]
	elif not áÓó(y):
		ÂùÆ(áÓö(y));(y:={*MOD(ÄÔÔç,áØÁ=MOD(lambda ÂîÓ:ÂÁÍ(ì)(ÂîÓ,ãÊú(x))))(y,MOD(lambda ÂîÓ:ÂîÓ<0))});(ÄÊPSH(([],[])),((R:=ÄÊPKE(0)[0]),(áÍÌ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
		for(áÑî,áÑü)in ÂÓÏ(x):
			if áÑî in y:áÍÌ.append(R);(R:=[])
			R.append(áÑü)
		if R:áÍÌ.append(R)
		return áÍÌ
	(ÄÊPSH((y((áÝÌ:=x[0])),[áÝÌ]if áÝÌ is not ÄÔýò else ÂÚü(),[])),((áÍç:=ÄÊPKE(0)[0]),(R:=ÄÊPKE(0)[1]),(áÍÌ:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
	for(áÑî,áÑü)in ÂÓÏ(x)[slice(1,None)]:
		if(r:=y(áÑü))!=áÍç:
			áÍÌ.append(R);(ÄÊPSH((r,[])),((áÍç:=ÄÊPKE(0)[0]),(R:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
			if not(ÄÊPSH(áØÁ),ÄÊPSH(ÄÊPKE(0)-1),(áØÁ:=ÄÊPKE(0)),ÄÊDEL(2))[2]:áÍÌ.append(x[slice(áÑî+(r is ÄÔýò),None)]);break
		if r is not ÄÔýò:R.append(áÑü)
	if R:áÍÌ.append(R)
	(áÍÌ:=ÄÔÔè(áÍÌ,MOD(lambda ÂîÓ:ÂîÓ==[])))
	if ÁØö(x,ÁÜÙ):(áÍÌ:=MOD(ÄÔÔç,áØÁ=MOD(lambda ÂîÓ:Âøî(ÂîÓ,ÁØã)))(áÍÌ,MOD(lambda ÂîÓ:ÄÝøÇ(ÂîÓ,ÁÜÙ))))
	return áÍÌ
@OPWRAP_(*'⨝⟕⟖⟗')
def _(áÑã,áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ,LR_def=None,bound_mode=ÂÞÅ):
	ÄÊPOP(0)if ÄÊPSH(áØÆ is not ÂÞÅ or ÂÞÅ is not áØÇ)else ÂùÆ(ÄÊPOP(0),'Join missing both values!')
	if áØÁ is not ÂÞÅ:(bound_mode:=áØÁ)
	if bound_mode is ÂÞÅ:(bound_mode:=áÑã=='⟗'and 1 or 0)
	if áØÆ is ÂÞÅ:(ÄÊPSH((áØÇ,áØÆ)),((áØÆ:=ÄÊPKE(0)[0]),(áØÇ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	if áØÇ is ÂÞÅ:ÄÊPOP(0)if ÄÊPSH(áÓö(áØÆ))else ÂùÆ(ÄÊPOP(0),'Single-arg %s needs an iterable'%(áÑã,));return'\n'*(áÑã in'⟕⟗')+ÁØã.join(Áÿú(áØÆ,ÁÜÙ))+ÂÔö('⟗⟖',áÑã)*'\n'
	(Y:=áØÇ)
	if not áÓó(áØÇ):(ÄÊPSH(áØÇ),ÄÊPSH((lambda ÂîÓ:lambda*áÑË:ÂîÓ)(ÄÊPKE(0))),(áØÇ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	(ÄÊPSH(([*áØÆ],[])),((áØÆ:=ÄÊPKE(0)[0]),(R:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	if ãÊú(áØÆ)==0 and(áÑã!='⨝'or bound_mode>0):
		if(v:=áØÇ(LR_def,LR_def))is ÄÔýò:(R:=[])
		if áÑã in'⟕⟖'or bound_mode==1:(R:=[v])
		else:(R:=[v,v])
	else:
		if áÑã in'⟕⟗'and ÄÔýò is not(áÑÿ:=áØÇ(LR_def,áØÆ[0])):R.append(áÑÿ)
		for i in ÄÝöÇ(ãÊú(áØÆ)):R.extend([áØÆ[i-1]]if(áÑÿ:=áØÇ(áØÆ[i-1],áØÆ[i]))is ÄÔýò else[áØÆ[i-1],áÑÿ])
		if ãÊú(áØÆ):R.append(áØÆ[-1])
		if áÑã in'⟖⟗'and ÄÔýò is not(áÑÿ:=áØÇ(áØÆ[-1],LR_def)):R.append(áÑÿ)
	return ÁØã.join(Áÿú(R,ÁÜÙ))if ÁØö(Y,ÁÜÙ)else R
@OPWRAP_(*'\U000f7e4c\U000f7e4d\U000f7e4e\U000f7e51')
def _(áÑã,áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=-1):
	if ÁØö(áØÁ,áÍé):(ÄÊPSH(ÂÀÇ(áØÁ)if áØÁ[0]==áÍá else áØÁ),((n:=ÄÊPKE(0)[0]),(L:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	else:(ÄÊPSH([-1,True]if áØÁ==áÍá else[áØÁ,False]),((n:=ÄÊPKE(0)[0]),(L:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	if(not L and ÁØö(áØÆ,ÁÜÙ))and(áØÇ is ÂÞÅ or ÁØö(áØÇ,ÁÜÙ)):
		(áÏÞ:=()if áØÇ is ÂÞÅ else(áØÇ,))
		if áÑã in'\U000f7e4e\U000f7e51':(r:=áØÆ.split(*áÏÞ,maxsplit=n));return ÄÔÔç(r)if áÑã=='\U000f7e4e'else r
	if áØÇ is ÂÞÅ:(áØÇ:=Âó)
	if not((YS:=ÁØö(áØÇ,ÁÜÙ))and L):(ÄÊPSH((Áÿú(Ááú(áØÆ,[0,ãÊú(áØÇ)-1]),MOD(lambda ÂîÓ:Âøî(ÄÔÔç(ÂîÓ)))),CUR(lambda ÂîÓ,ÂîÒ:ÂîÓ==ÂîÒ,áØÇ),ãÊú(áØÇ),ãÊú(áØÇ)-1)),((áØÆ:=ÄÊPKE(0)[0]),(áØÇ:=ÄÊPKE(0)[1]),(Y:=ÄÊPKE(0)[2]),(ÏÁ:=ÄÊPKE(0)[3])),ÄÊDEL(1))[1]
	else:(ÄÊPSH(([*áØÆ],áØÇ if áÓó(áØÇ)else CUR(lambda ÂîÓ,ÂîÒ:ÂîÓ==ÂîÒ,áØÇ),0)),((áØÆ:=ÄÊPKE(0)[0]),(áØÇ:=ÄÊPKE(0)[1]),(ÏÁ:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
	(ÄÊPSH(([],[],-1,0)),((r:=ÄÊPKE(0)[0]),(b:=ÄÊPKE(0)[1]),(Ïç:=ÄÊPKE(0)[2]),(Ïñ:=ÄÊPKE(0)[3])),ÄÊDEL(1))[1];(last_v:=False)
	while(ÄÊPSH(Ïç),ÄÊPSH(ÄÊPKE(0)+1),(Ïç:=ÄÊPKE(0)),ÄÊDEL(2))[2]<ãÊú(áØÆ)and Ïñ<(ÂÕË if n==-1 else n):
		(áÐÏ:=áØÆ[Ïç])
		if(áÑÿ:=áØÇ(áÐÏ)):
			if b or áÑã!='\U000f7e4e':
				if áÑã=='\U000f7e4e':r.append(b)
				elif áÑã in'\U000f7e4c\U000f7e51'or áÑã=='\U000f7e4d'and not last_v:r.extend([b]if áÑÿ is ÄÔýò else[b,áÐÏ]);(last_v:=True)
			(b:=[]);(ÄÊPSH(Ïç),ÄÊPSH(ÄÊPKE(0)+ÏÁ),(Ïç:=ÄÊPKE(0)),ÄÊDEL(2))[2];(ÄÊPSH(Ïñ),ÄÊPSH(ÄÊPKE(0)+1),(Ïñ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
		elif áÑÿ is not ÄÔýò:b.append(áÐÏ);(last_v:=False)
	if b or áÑã!='\U000f7e4e':b.extend(áØÆ[slice(Ïç,None)]);r.append(b)
	elif áØÆ[slice(Ïç,None)]:r.append(áØÆ[slice(Ïç,None)])
	return ÁØò(lambda ÂîÓ:Âøî(ÁØò(lambda ÂîÓ:ÂîÓ[0])(ÂîÓ))if ÁØö(ÂîÓ,áÍá)else ÂîÓ)(r)if YS else r
@OPWRAP_(*'⫰⫯\U000f7e52')
def _(áÑã,áØÆ,áØÁ=ÂÞÅ,ÁÜñ=ÂÞÅ):
	if ÁÜñ is not ÂÞÅ:ÂùÆ(ÁØö(áØÆ,ÁÜÙ)and áÑã!='\U000f7e52');return MOD(ÄÔÔç,ÁÜñ=ÄÕøü)(áØÆ,CURR(lambda ÂîÓ,ÂîÒ:ÃÆí(ÂîÓ)==ÂîÒ,áÑã=='⫰'or-1))
	if áÑã=='⫰':(v:=TO_UPPERCASE(áØÆ)if ÁØö(áØÆ,ÁÜÙ)else+abs(áØÆ))
	elif áÑã=='⫯':(v:=TO_LOWERCASE(áØÆ)if ÁØö(áØÆ,ÁÜÙ)else-abs(áØÆ))
	elif áÑã=='\U000f7e52':
		if áØÁ is not ÂÞÅ and ÁØö(áØÁ,ÂÑÅ):return((ÂüÌ if v==1 else ÂüË)if(v:=ÃÆí(áØÁ))else ÄÝöâ)(áØÆ,áØÁ=ÂÞÅ,ÁÜñ=ÁÜñ)
		(v:=REVERSE_CASE(áØÆ)if ÁØö(áØÆ,ÁÜÙ)else-áØÆ)
	if áØÁ is ÂÞÅ:return v
	ÂùÆ(áÓó(áØÁ));(áØÁ:=áØÁ(v))
	if ÄÝøÇ(áØÆ,ÁÜÙ):
		if áÑã=='⫰':return-áØÁ if áØÆ<0 else áØÁ
		elif áÑã=='⫯':return-áØÁ if áØÆ>0 else áØÁ
		elif áÑã=='\U000f7e52':return áØÁ if not áØÆ else-áØÁ
	return Âøî(ËãÂ(ÂÛÅ([áØÆ,v,áØÁ]),lambda x,y,z:MOD(Áëý,áØÁ=ÃÆí(x)!=ÃÆí(y))(z,MOD(ÄÝöâ,áØÁ=ÃÆí(x)))))
def ÄÝöì(áØÆ=ÂÞÅ,áØÁ=ÂÞÅ,C=ÂÞÅ):
	(nc:=C is ÂÞÅ)
	if nc:(C:=num+ABC+abc)
	elif áØÁ is ÂÞÅ:(áØÁ:=ãÊú(C))
	if áØÁ is ÂÞÅ:
		if ÄÝøÇ(áØÆ,ÁÜÙ):
			if áØÆ!=Âäû(áØÆ):return ÁÜÙ(áØÆ)
		elif'.'in áØÆ:return áÍÛ(áØÆ)
		(áØÇ:=10)
	elif ÁØö(áØÁ,áÓö):(ÄÊPSH([áØÁ[0],ÂÞÅ]if ãÊú(áØÁ)==1 else áØÁ),((áØÇ:=ÄÊPKE(0)[0]),(áØÁ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	elif ÁØö(áØÁ,ÂÐý):(ÄÊPSH((Âüð(áØÁ),ÂÞÅ)),((áØÇ:=ÄÊPKE(0)[0]),(áØÁ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	else:(ÄÊPSH(MOD(ÁÞç,áØÁ=0)(Áÿú(ÄÝõé(áØÁ),Âüð),MOD(lambda ÂîÓ:ÂîÓ or 10))),((áØÇ:=ÄÊPKE(0)[0]),(áØÁ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	if MOD(ÁØö,áØÁ=ÂÕó)(áØÆ,áÍÛ):(ÄÊPSH(áØÆ),ÄÊPSH(Âäû(ÄÊPKE(0))),(áØÆ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	elif ÁØö(áØÆ,ÁÜÙ):
		if áØÆ and áØÆ[0]=='-':(ÄÊPSH((áØÆ[slice(1,None)],-1)),((áØÆ:=ÄÊPKE(0)[0]),(p:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
		else:(p:=1)
		if nc and áØÇ<=36:(ÄÊPSH(áØÆ),ÄÊPSH(ÂüÌ(ÄÊPKE(0))),(áØÆ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
		(áØÆ:=MOD(ÆÑ,áØÁ=0)(ÁØò(lambda ÂîÓ:MOD(ÄÔÞÔ,ÁÜñ=ÄÕøü)(C,ÂîÓ))(áØÆ),CUR(lambda ÂîÓ,ÂîÒ:ÂîÓ*áØÇ+ÂîÒ))*p)
		if áØÁ is ÂÞÅ:return áØÆ
	if áØÁ is ÂÞÅ:(áØÁ:=1)
	(ÂÐôþáÏß:=CUR(lambda ÂîÓ,ÂîÒ:Âøî(ÂÀÇ(ÁØò(lambda ÂîÓ:ÂîÒ[ÂîÓ%ãÊú(ÂîÒ)])(ÂÛÜ(MOD(lambda ÂîÓ:ÂîÓ//ãÊú(ÂîÒ)),Âó)(ÂîÓ))))));(ÂÑÅþáÏß:=CUR(lambda ÂîÓ,ÂîÒ,*áÏÞ:(ÂîÓ<0)*'-'+MOD(ÄÕÊÂ,áØÁ=ÂîÒ[0])(ÂÐôþáÏß(ÂüÌ(ÂîÓ),ÂîÒ),áÏÞ[0])));return ÂÑÅþáÏß(áØÆ,ÄÝöÈ(C,áØÇ),áØÁ)
(ÄÔóÅ:=lambda áØÆ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:phase(áØÆ+ÂÞÅCAT(áØÇ,Ãù))if áØÇ is not ÂÞÅ else phase(áØÆ)if ÁØö(áØÆ,ÂÐá)else phase(ÄÝõé(áØÆ)))
(Âõì:=lambda áØÆ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ:rect(áØÆ,áØÇ)if áØÇ is not ÂÞÅ else rect(*áØÆ)if ÁØö(áØÆ,áÓö)else polar(áØÆ)if s is ÂÞÅ else ÂÞÅCAT(áØÆ,ÂÐæ**ÂÞÅCAT(áØÁ,Ãù)))
@OPWRAP_(*'\U000f7e13\U000f7e3c\U000f7e14')
def _(áÑã,áØÆ,áØÁ=ÂÞÅ,ÁÜñ=ÂÞÅ):
	if áØÆ is ë:ÄÊPOP(0)if ÄÊPSH(ÁÜñ is ÂÞÅ and áØÁ is ÂÞÅ)else ÂùÆ(ÄÊPOP(0),'no');return SUBSCRIPT if áÑã=='\U000f7e13'else SUPSCRIPT if áÑã=='\U000f7e14'else(ÄÝõà(ë),ÄÝõá(ë))
	(áØÆ:=ÁÜÙ(áØÆ))
	if ÁÜñ is not ÂÞÅ:
		if áÑã=='\U000f7e3c':ÄÊPOP(0)if ÄÊPSH(áØÁ is ÂÞÅ)else ÂùÆ(ÄÊPOP(0),'\U000f0931');ÄÊPOP(0)if ÄÊPSH(ÁØö(ÁÜñ,áÓó))else ÂùÆ(ÄÊPOP(0),'\U000f0931');return under_script(áØÆ,ÁÜñ)
		ÄÊPOP(0)if ÄÊPSH(False)else ÂùÆ(ÄÊPOP(0),'\U000f0931')
	if áØÁ is ÂÞÅ:(áØÁ:=1)
	if áØÁ>0:(Æå:=subscript if áÑã=='\U000f7e13'else supscript if áÑã=='\U000f7e14'else nrmscript);return ÂÕÅ(ÂØÍ(Æå,áØÁ),áØÆ)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ops_C.☾')).parent
@OPWRAP_(*'\U000f147c\U000f7e45')
def _(áÑã,áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
	(áÖÒ:=áØÆ if áØÇ is ÂÞÅ else(áØÆ,áØÇ))
	if not ãÊú(áÖÒ):return ÂÚü()
	(ÄÊPSH(MOD(ÐÌÛ,áØÁ=áÍÖ,ÁÜñ=ÄÕøü)(áÖÒ,áÓö)),((N:=ÄÊPKE(0)[0]),(I:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1];(ÄÊPSH(Âîí(Áÿú(ÄÝöÊ(áÖÒ,I),ãÊú))),((l:=ÄÊPKE(0)[0]),(h:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	if N:(ÄÊPSH(áÖÒ),ÄÊPSH(MOD(ÁÞç,áØÁ=N)(ÄÊPKE(0),MOD(ÁØò(lambda ÂîÓ:MOD(Âêà,áØÁ=h)(ÂîÓ))))),(áÖÒ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	if áØÁ is ÂÞÅ:
		if áÑã=='\U000f7e45':(áÖÒ:=ÁØòþÁÙÄ(lambda ÂîÓ,ÂîÒ:ÂîÓ[slice(ãÊú(ÂîÓ)-ÂîÒ,None)])(áÖÒ,l))
	else:(ÄÊPSH(áÖÒ),ÄÊPSH(Áÿú(ÄÊPKE(0),Âåæ(MOD(lambda ÂîÓ:MOD(ÄÕÊÄ,áØÁ=ÂîÓ[-1]if áØÁ is ÄÕøü else áØÁ)(ÂîÓ,h))if áÑã=='\U000f147c'else MOD(lambda ÂîÓ:MOD(ÄÕÊÂ,áØÁ=ÂîÓ[0]if áØÁ is ÄÕøü else áØÁ)(ÂîÓ,h)),áÍá))),(áÖÒ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	(r:=[*zip(*áÖÒ)]);return Áÿú(r,ÄÊCUR((1,),{},ÄÔÔè,ÂýÃ,ÄÔýò))if áØÁ is ÄÔýò else r
@OPWRAP_(*'\U000f7e62\U000f7e63')
def _(áÑã,áØÆ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
	if ÂÞÅ is áØÇ:(áØÇ:=2)
	if(ÄÝøÆ(ÁÜÙ,ÄÊPSH(áØÆ))and ÄÝøÇ(ÄÊPOP(0),ÄÊPSH(áÍá)))and(ÄÊDEL(1)or True)or(ÄÊDEL(1)or False):(ÄÊPSH(áØÆ),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),áÍá)),(áØÆ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	if ÁØñ(ÁÜÙ,áØÆ)and((ÂÞÅ is not ÄÊPSH(áØÁ)and ÄÊPOP(0)is not ÄÊPSH(ÄÔýò))and(ÄÊDEL(1)or True)or(ÄÊDEL(1)or False)):(ÄÊPSH(áØÁ),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),ÁÜÙ)),(áØÁ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	(áØÅ:=Âüð(ÄÝõè(áØÇ))or 2);(ÏÁ:=(lambda ÂîÓ:ÂîÓ if ÂîÓ>0 else áØÅ+ÂîÓ)(Âüð(ÄÝõç(áØÇ))));(ÄÊPSH((ãÊú(áØÆ),ÂÚü())),((áÖù:=ÄÊPKE(0)[0]),(áÖä:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	if áÑã=='\U000f7e62':
		(i:=0)
		while i<áÖù:
			if(e:=i+áØÅ>áÖù)and áØÁ is ÂÞÅ:return áÖä
			(áØÀ:=áØÆ[slice(i,i+áØÅ)])
			if e and áØÁ is not ÄÔýò:
				if ÁØö(áØÆ,ÁÜÙ):(ÄÊPSH(áØÀ),ÄÊPSH(ÄÊPKE(0)+(ÂüË(ãÊú(áØÀ))+áØÅ)*áØÁ),(áØÀ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
				else:(ÄÊPSH(áØÀ),ÄÊPSH(ÄÊPKE(0)+(ÂüË(ãÊú(áØÀ))+áØÅ)*[áØÁ]),(áØÀ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
			(ÄÊPSH(áÖä),ÄÊPSH(ÄÊPKE(0)+[áØÀ]),(áÖä:=ÄÊPKE(0)),ÄÊDEL(2))[2];(ÄÊPSH(i),ÄÊPSH(ÄÊPKE(0)+ÏÁ),(i:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	else:
		(i:=áÖù)
		while i>0:
			if(s:=i-áØÅ<0)and áØÁ is ÂÞÅ:return áÖä
			(áØÀ:=áØÆ[slice(ÂóÍ(i-áØÅ,0),i)])
			if s and áØÁ is not ÄÔýò:
				if ÁØö(áØÆ,ÁÜÙ):(ÄÊPSH(áØÀ),ÄÊPSH(ÂÁÍ(ì)(ÄÊPKE(0),(ÂüË(ãÊú(áØÀ))+áØÅ)*áØÁ)),(áØÀ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
				else:(ÄÊPSH(áØÀ),ÄÊPSH(ÂÁÍ(ì)(ÄÊPKE(0),(ÂüË(ãÊú(áØÀ))+áØÅ)*[áØÁ])),(áØÀ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
			(ÄÊPSH(áÖä),ÄÊPSH(ÂÁÍ(ì)(ÄÊPKE(0),[áØÀ])),(áÖä:=ÄÊPKE(0)),ÄÊDEL(2))[2];(ÄÊPSH(i),ÄÊPSH(ÄÊPKE(0)-ÏÁ),(i:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	return áÖä
def ÁÛÛ(áØÆ,áØÁ=ÂÞÅ):
	def Æå(áØÁ):
		if ÄÝøÇ(áØÁ,áÓö)or ÁØñ(ÁÜÙ,áØÁ):(ÄÊPSH(áØÁ),ÄÊPSH(Âêà(ÄÊPKE(0))),(áØÁ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
		(áÓÕ:=MOD(ÁÛÛ,áØÁ=áØÁ[slice(1,None)])if ãÊú(áØÁ)>1 else ÄÕÍÔ);(áÓÙ:=lambda x,y:áÓÕ(x[y%ãÊú(x)])if ÁØö(y,ÂÑÅ)else áÓÕ(x[y])if ÁØö(y,ÁÜÙ)or((ÄÝøÆ(áÓö,ÄÊPSH(y))and ÄÝøÇ(ÄÊPOP(0),ÄÊPSH(slice)))and(ÄÊDEL(1)or True)or(ÄÊDEL(1)or False))else MOD(Áëý,áØÁ=áÓÕ is not ÄÕÍÔ)(ÄÝöÊ(x,y),MOD(lambda ÂîÓ:Áÿú(ÂîÓ,áÓÕ))));return áÓÙ(áØÆ,áØÁ[0])
	return Æå if áØÁ is ÂÞÅ else Æå(áØÁ)
def ÁÝÖ(áØÆ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
	ÄÊPOP(0)if ÄÊPSH(ÁØö(áØÆ,áÓö))else ÂùÆ(ÄÊPOP(0),'%s\U000f7e75𝗜'%(áØÆ,));ÄÊPOP(0)if ÄÊPSH(áØÁ is not ÂÞÅ)else ÂùÆ(ÄÊPOP(0),'ᕋ requires modifier');(áØÆ:=ÄÔÙù(áØÆ)if(is_str:=ÁØö(áØÆ,ÁÜÙ))else ÐÌü(áØÆ.copy));(áØÇ:=MOD(Áëý,áØÁ=ÄÝøÇ(áØÇ,áÓö))(áØÇ,Âêà)if áØÇ is not ÂÞÅ else ÂÚü());(áØÁ:=slice((ÄÊPSH(áØÁ),ÄÊPSH(ÄÊPKE(0)%ãÊú(áØÆ)),(áØÁ:=ÄÊPKE(0)),ÄÊDEL(2))[2],áØÁ+1)if ÁØö(áØÁ,áÍÞ)else áØÁ)
	if ÁØö(áØÁ,slice):(ÄÊPSH(áØÆ),ÄÊPSH(áØÁ),ÄÊPSH(áØÇ),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
	elif ÁØö(áØÁ,áÓö):
		for(i,(z,n))in ÂÓÏ(ÁØò(lambda ÂîÓ:ãÊú([ÂîÓ[0],ÂîÓ]))(áÇù(ÄÔàÒ(ÁØò(lambda ÂîÓ:ÂîÓ%ãÊú(áØÆ))(áØÁ))))):
			if áØÇ is ÂÞÅ or i>=ãÊú(áØÇ):del áØÆ[z]
			else:(ÄÊPSH(áØÆ),ÄÊPSH(slice(z,z+1)),ÄÊPSH(MOD(Âêà,áØÁ=n)(áØÇ[i])),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
	else:ÄÊPOP(0)if ÄÊPSH(False)else ÂùÆ(ÄÊPOP(0),'Modifier \U000f7e75 slice|𝑖|𝗜')
	return Âøî(áØÆ,ÁØã)if is_str else áØÆ
(ÂÕÅ:=lambda áØÆ,áØÇ,áØÁ=1:áØÆ(*MOD(Âêà,áØÁ=áØÁ)(áØÇ)))
def Áëý(áØÆ,áØÇ,áØÁ=ÂÞÅ):
	(v:=áØÆ if áØÁ is ÂÞÅ else áØÁ(áØÆ)if áÓó(áØÁ)else áØÁ)
	if áÓó(áØÇ):return áØÇ(áØÆ)if v else áØÆ
	if áÓö(áØÇ):
		if ãÊú(áØÇ)==1:return áØÇ[0](áØÆ)if v else v
		if ãÊú(áØÇ)==2:return áØÇ[áÍÖ(v)](áØÆ)
	ÄÊPOP(0)if ÄÊPSH(False)else ÂùÆ(ÄÊPOP(0),'Unsupport type of 𝚢 in ᣆ: %s'%(ÁØö(áØÇ),))
@OPWRAP_(*'○⍜\U000f0b2b\U000f0b29')
def _(áÑã,áÍÛ,áÍÜ,áØÁ=1):
	if áÑã in'\U000f0b29\U000f0b2b':
		ÄÊPOP(0)if ÄÊPSH((ÄÊDEL(1),False)[1]if ÄÊPSH(áØÁ==ì)else ÄÊPOP(0)if î==áØÁ else(ÄÊDEL(1),True)[1])else ÂùÆ(ÄÊPOP(0),'\U000f0931 generalize')
		if not áØÁ or ÁØö(áÍÜ,áÓö):
			def Æå(*áÑË):
				if áØÁ==0:(áÖÒ:=[Áÿú(MOD(Áëý,áØÁ=ÁØö(áÍÜ,áÓó))(áÍÜ,Âêà),ÐÌü),áÑË])
				else:
					(áÖû:=ãÊú(áÍÜ)*(S:=ÂüÌ(áØÁ)))
					if áØÁ<0:(ÄÊPSH(áÑË),ÄÊPSH(Âúú(ÄÊPKE(0),ãÊú(áÑË)-áÖû)),(áÑË:=ÄÊPKE(0)),ÄÊDEL(2))[2]
					if áÑã=='\U000f0b2b':(ÄÊPSH(MOD(ÄÕÊÄ,áØÁ=[])(áÇù(áÑË,áÖû),2)),((Ïß:=ÄÊPKE(0)[0]),(Ïà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
					elif áÑã=='\U000f0b29':(ÄÊPSH(MOD(ÄÕÊÂ,áØÁ=[])(áÇù(áÑË,ÂóÍ(ãÊú(áÑË)-áÖû,0)),2)),((Ïà:=ÄÊPKE(0)[0]),(Ïß:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
					(áÖÒ:=[ÁØò(lambda ÂîÓ:ÂîÓ[1](*ÂîÓ[0]))((ÄÕåØ if áØÁ<0 else ÄÝöÔ)[[]](MOD(Ááú,áØÁ=ÄÔýò)(Ïß,[0,S-1,S]),áÍÜ)),Ïà])
				return ÄÔÙù(MOD(Áëý,áØÁ=áÑã=='\U000f0b29')(áÖÒ,ÂÀÇ))
		else:
			def Æå(*áÑË):
				(áÖí:=ãÊú(áÑË)//((S:=ÂüÌ(áØÁ))or 1)*S);(ÄÊPSH(áÇù(ÂÿÇ(áÑË),áÖí if áÑã=='\U000f0b2b'else ãÊú(áÑË)-áÖí)),((Ïß:=ÄÊPKE(0)[0]),(Ïà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
				if Ïß and áØÁ<0:(ÄÊPSH((ÁØò(lambda ÂîÓ:ÂîÓ+ãÊú(Ïà))(Ïß),ÂÿÇ(Ïà))),((Ïß:=ÄÊPKE(0)[0]),(Ïà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
				(ÄÊPSH((ÄÝöÊ(áÑË,Ïß),ÄÝöÊ(áÑË,Ïà))),((Ïß:=ÄÊPKE(0)[0]),(Ïà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
				if áÑã=='\U000f0b2b':return*ËãÂ(MOD(ÁâÁ,áØÁ=ÂóÍ(S-1,0))(Ïß),áÍÜ),*Ïà
				elif áÑã=='\U000f0b29':return*Ïß,*ËãÂ(MOD(ÁâÁ,áØÁ=ÂóÍ(S-1,0))(Ïà),áÍÜ)
	elif ÁØö(áÍÜ,áÓó):
		def Æå(*áÑË):
			(ÄÊPSH(((L:=ãÊú(áÑË))//(S:=ÂüÌ(áØÁ)),L%S)),((n:=ÄÊPKE(0)[0]),(m:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1];ÄÊPOP(0)if ÄÊPSH(n!=0)else ÂùÆ(ÄÊPOP(0),'\U000f0931 generalize');(áÖÒ:=(MOD(ÄÕÊÄ,áØÁ=ÂýÃ)if áÑã=='○'else MOD(ÄÕÊÂ,áØÁ=ÂýÃ))(áÑË,L+(n-m)%n));(v:=MOD(ÁâÁ,áØÁ=n-1)(áÖÒ))
			if m!=0:
				(ÄÊPSH([-1,0]if áÑã=='○'else[0,-1]),((Ïß:=ÄÊPKE(0)[0]),(Ïà:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
				if ÄÝøø(áÑã=='⍜',áØÁ<0):(ÄÊPSH(v),ÄÊPSH(Ïß),ÄÊPSH(ÄÔÙù(ÂÀÇ(áÇù(v[Ïß],MOD(lambda ÂîÓ:ÂîÓ is ÂýÃ))))),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
				(ÄÊPSH(v),ÄÊPSH(Ïß),ÄÊPSH(ÁØòþÁÙÇ(lambda ÂîÓ,ÂîÒ:ÂîÓ if ÂîÓ is not ÂýÃ else ÂîÒ)(v[Ïß],v[Ïà])),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
			return ËãÂ(v,áÍÜ)
	elif ÁØö(áÍÜ,áÓö):
		def Æå(*áÑË):ÄÊPOP(0)if ÄÊPSH(ãÊú(áÑË)>=ãÊú(áÍÜ)*(S:=ÂüÌ(áØÁ)))else ÂùÆ(ÄÊPOP(0),'\U000f0931 generalize');ÄÊPOP(0)if ÄÊPSH(áØÁ>0)else ÂùÆ(ÄÊPOP(0),'\U000f0931 generalize');ÄÊPOP(0)if ÄÊPSH(áÑã!='⍜')else ÂùÆ(ÄÊPOP(0),'\U000f0931 generalize');(ÄÊPSH(áÇù(áÑË,ãÊú(áÍÜ)*(S:=ÂüÌ(áØÁ)))),((l:=ÄÊPKE(0)[0]),(r:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1];(áÖÒ:=ÁØòþÁÙÄ(lambda ÂîÓ,ÂîÒ:ÄÔÙù(ÂîÓ,ÂîÒ))(MOD(ÁâÁ,áØÁ=S-1)(l),r));return ËãÂ(ÄÕåØ(áÖÒ,áÍÜ),lambda x,y:y(*x))
	return lambda*áÑË,**áÑÕ:áÍÛ(*Æå(*áÑË),**áÑÕ)
@OPWRAP_(*'⊚⊜🟕🟖⊛⍟')
def _(áÑã,Æå=ÂÞÅ,áÍÜ=ÂÞÅ,áØÁ=ÂÕË):
	if not áÓó(Æå):(ÄÊPSH((áÍÜ,Æå)),((Æå:=ÄÊPKE(0)[0]),(áÍÜ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	if áÍÜ is ÂÞÅ:(áÍÜ:=ÄÕÍÔ)
	elif ÁØö(áÍÜ,áÍÞ)and áÑã in'⊚⊛⍟':(áÍÜ:=Ticker(áÍÜ+1))
	def r(*áÑË,**áÑÕ):
		(ÄÊPSH((ÂüÌ(áØÁ),áÑË[0]if áÑË else None,áÍÜ(*áÑË,**áÑÕ))),((n:=ÄÊPKE(0)[0]),(f:=ÄÊPKE(0)[1]),(g:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
		if áÑã=='⊚':
			if g:return f
			while 0<(ÄÊPSH(n),ÄÊPSH(ÄÊPKE(0)-1),(n:=ÄÊPKE(0)),ÄÊDEL(2))[2]:
				if áÍÜ((f:=Æå(f))):return f
		elif áÑã=='⊜':
			while 0<(ÄÊPSH(n),ÄÊPSH(ÄÊPKE(0)-1),(n:=ÄÊPKE(0)),ÄÊDEL(2))[2]:
				if g==(g:=áÍÜ((nf:=Æå(f)))):return f
				(f:=nf)
		elif áÑã in'⊛⍟':
			(rf:=[f])
			if g:return rf if áÑã=='⊛'else[]
			while 0<(ÄÊPSH(n),ÄÊPSH(ÄÊPKE(0)-1),(n:=ÄÊPKE(0)),ÄÊDEL(2))[2]:
				(g:=áÍÜ((f:=Æå(f))))
				if not g or áÑã=='⊛':rf.append(f)
				if g:return rf
			if áØÁ<0:return rf
		elif áÑã in'🟕🟖':
			(ÄÊPSH(([f],[g])),((rf:=ÄÊPKE(0)[0]),(rg:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
			while 0<(ÄÊPSH(n),ÄÊPSH(ÄÊPKE(0)-1),(n:=ÄÊPKE(0)),ÄÊDEL(2))[2]:
				if(g:=áÍÜ((f:=Æå(f))))in rg:
					if áÑã=='🟖':return rf
					return ÄÝöÊ(MOD(ÄÔÞÔ,ÁÜñ=ÄÕøü)(rg,lambda x:x==g),rf)
				rf.append(f);rg.append(g)
	return r
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ℵ.☾')).parent
class aleph_wrapper:(__slots__:=('x',));(__init__:=lambda áÑÞ,y:Âåß(None,(ÄÊPSH(áÑÞ),ÄÊPSH('x'),ÄÊPSH(y),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]));(__repr__:=lambda áÑÞ:áÑÞ.x);(__call__:=lambda áÑÞ,*áÑË,**áÑÕ:áÑÞ.x(*áÑË,**áÑÕ))
class ÂÑÖ(áÍÙ):
	(áÌüþáÍã:='ℵ')
	def __getitem__(áÑÞ,x):
		if x in áÑÞ:return áÍÙ.__getitem__(áÑÞ,x)
		if áÑÞ.hasdef():return áÑÞ.getdef(x)
		ÐâÄ(KeyError('%s ∉ %s, and I have no default value!'%(x,áÑÞ)))
	def __contains__(áÑÞ,x):return super().__contains__(x)
	def __init__(áÑÞ,*áÑË,áØÁ=ÂÞÅ,**áÑÕ):
		super().__init__(*áÑË,**áÑÕ)
		if áØÁ is not ÂÞÅ:áÑÞ.setdef(áØÁ)
	(__repr__:=lambda áÑÞ:'%s%s(%s)'%(áÑÞ.__class__.áÌüþáÍã,'[%s]'%(h[0]or'ᐦ',)if 0 in(h:=áÑÞ.__dict__)else ÁØã,Âøî(ËãÂ(ÐÌü(áÑÞ.items),lambda x,y:'%s=%s'%(x,y)),', ')));(__json__:=lambda áÑÞ,cb,*áÏÞ,**áÏè:MOD(ËãÂ,áØÁ=ì)(áÍÙ(áÑÞ),lambda x,y:cb(y,*áÏÞ,**áÏè)));(__iter__:=lambda áÑÞ:iter(áÑÞ.items()));(__call__:=lambda áÑÞ,*áÑË,**áÑÕ:ÂåÔ(áÍÙ.update(áÑÞ,*áÑË,**áÑÕ),áÑÞ));(__bool__:=lambda áÑÞ:ãÊú(áÑÞ)>0);(__or__:=lambda áÑÞ,x:áÑÞ.copy()(x));(__ror__:=lambda áÑÞ,x:ÂÞÅCAT(x,ÂÑÖ())|áÑÞ)
	def __and__(áÑÞ,y):
		(r:=ÂÑÖ())
		if áÑÞ.hasdef():r.setdef(áÑÞ.getdef())
		if ÁØö(y,áÍè|áÍá|áÍé|ÁÜÙ):
			for k in{*y}:
				if not k in áÑÞ:continue
				(ÄÊPSH(r),ÄÊPSH(k),ÄÊPSH(áÑÞ[k]),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		else:
			for(k,v)in y.items():
				if not k in áÑÞ:continue
				(ÄÊPSH(r),ÄÊPSH(k),ÄÊPSH(v),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		return r
	def __rand__(áÑÞ,y):
		if ÁØö(y,áÍè|áÍá|áÍé|ÁÜÙ):return áÑÞ&y
		if ÁØö(y,áÍÙ):return ÂÞÅCAT(y,ÂÑÖ())&áÑÞ
		return NotImplemented
	def __sub__(áÑÞ,y):
		(r:=ÂÑÖ())
		if áÑÞ.hasdef():r.setdef(áÑÞ.getdef())
		ÂùÆ(áÓö(y))
		for(k,v)in áÑÞ:
			if not k not in y:continue
			(ÄÊPSH(r),ÄÊPSH(k),ÄÊPSH(v),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		return r
	def __rsub__(áÑÞ,y):
		if ÁØö(y,áÍÙ):return ÂÞÅCAT(y,ÂÑÖ())-áÑÞ
		return NotImplemented
	(__setattr__:=áÍÙ.__setitem__);(__getattr__:=__getitem__)
	def __getstate__(áÑÞ):
		if áÑÞ.hasdef():return áÍÙ(áÑÞ),áÑÞ.getdef()
		else:return áÍÙ(áÑÞ),
	def __setstate__(áÑÞ,s):
		áÑÞ.__init__(s[0])
		if ãÊú(s)>1:áÑÞ.setdef(s[1])
	def __pow__(áÑÞ,x):
		if x is î:return[*ÐÌü(áÑÞ.keys)]
		if x is ì:return[*ÐÌü(áÑÞ.values)]
		if x is ë:return[*ÐÌü(áÑÞ.items)]
		if x is ÂÕì:return MOD(Áÿú,áØÁ=ë)(áÑÞ,ÂÀÇ)
		if x is Áâ:return MOD(Áëý,áØÁ=ÄÝøÇ((v:=ÐÌü(áÑÞ.getdef)),(C:=aleph_wrapper)))(ÐÌü(áÑÞ.copy),lambda x:x.setdef(C(v)))
		ÂùÆ(False)
	(hasdef:=lambda áÑÞ:0 in áÑÞ.__dict__);(setdef:=lambda áÑÞ,x:ÂåÔ((ÄÊPSH(áÑÞ.__dict__),ÄÊPSH(0),ÄÊPSH(x),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3],áÑÞ))
	def getdef(áÑÞ,k=ÂÞÅ):
		(d:=áÑÞ.__dict__[0])
		if ÁØö(d,aleph_wrapper):(ÄÊPSH(d),ÄÊPSH(ÐÌü(ÄÊPKE(0))),(d:=ÄÊPKE(0)),ÄÊDEL(2))[2];(ÄÊPSH(áÑÞ),ÄÊPSH(k),ÄÊPSH(d),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		return d
	def copy(áÑÞ):
		(r:=type(áÑÞ)(super().copy()))
		if áÑÞ.hasdef():r.setdef(áÑÞ.getdef())
		return r
class ÂÑØ(ÂÑÖ):(áÌüþáÍã:='ℶ');(__iter__:=lambda áÑÞ:iter(áÑÞ.values()))
class áÍáþáÍá(áÍá):None
__dir__=(__file__:=áÌî(moon_dir/'Builtins/?.☾')).parent
class qproxy:
	(__slots__:=('v','a'))
	def __init__(áÑÞ,v,a=None):(ÄÊPSH(áÑÞ),ÄÊPSH('v'),ÄÊPSH(áÑÞ),ÄÊPSH('a'),ÄÊPSH((v,a)),(setattr(ÄÊPKE(4),ÄÊPKE(3),ÄÊPKE(0)[0]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)[1])),ÄÊDEL(5))[5]
	def __call__(áÑÞ,*áÑË,**áÑÕ):return áÑÞ.v(*áÑË,**áÑÕ)if áÓó(áÑÞ.v)else áÑÞ.a
	def __getattr__(áÑÞ,x):return getattr(áÑÞ.v,x)if getattr(áÑÞ.v,'__contains__')(x)else áÑÞ.a
	def __getitem__(áÑÞ,x):
		(v:=áÑÞ.v)
		if ÁØö(v,áÍÙ):
			if x in v:return v[x]
		elif ÁØö(v,áÍá|áÍé|ÁÜÙ):
			try:return v[x]
			except áÍÚ:pass
		elif hasattr(v,'__getitem__'):
			try:return v[x]
			except áÍÚ:pass
		return áÑÞ.a
def ÁÂ(áØÆ,áØÁ=ÂÞÅ):return qproxy(áØÆ,áØÁ if áØÁ is not ÂÞÅ else None)
def ÂÛí(áØÆ,áØÁ=ÂÞÅ):return(áØÁ if áØÁ is not ÂÞÅ else False)if áØÆ is None else True
def ÄÝõÒ(áØÆ,áØÁ=ÂÞÅ):return True if áØÆ is None else áØÁ if áØÁ is not ÂÞÅ else False
__dir__=(__file__:=áÌî(moon_dir/'Builtins/crypto.☾')).parent
class Cmap(ÂÑÖ):
	def __init__(áÑÞ,d,*áÑË,**áÑÕ):super().__init__(*áÑË,**áÑÕ);(ÄÊPSH(áÑÞ.__dict__),ÄÊPSH(1),ÄÊPSH(d),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
	(__call__:=lambda áÑÞ,*áÑË,**áÑÕ:áÑÞ[áÑÞ.__dict__[1]](*áÑË,**áÑÕ));(__pow__:=lambda x,y:x[y])
def SR_bytes(x=None,y=None):
	if(x is ÄÊPSH(None)and ÄÊPOP(0)is ÄÊPSH(y))and(ÄÊDEL(1)or True)or(ÄÊDEL(1)or False):return PL_URANDOM(1)[0]
	if y is None:return PL_URANDOM(x)
	if x is None:(x:=0)
	return SR_bytes(SR_int(x,y))
def SR_int(x=None,y=None):
	if x is None:ÂùÆ(y is None);return ÐÌü(SR_bytes)
	if y is None:(ÄÊPSH((0,x)),((x:=ÄÊPKE(0)[0]),(y:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	if x>y:(ÄÊPSH((y,x)),((x:=ÄÊPKE(0)[0]),(y:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	(r:=y-x);(l:=ÐÌü(r.bit_length))
	while(s:=áÍÞ.from_bytes(SR_bytes(Âüï(l/8)))&2**l-1)>r:None
	return x+s
def SR_float(x=None,y=None):
	if x is None:ÂùÆ(y is None);(ÄÊPSH((0,1)),((x:=ÄÊPKE(0)[0]),(y:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	else:
		if y is None:(ÄÊPSH((0,x)),((x:=ÄÊPKE(0)[0]),(y:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
		if x>y:(ÄÊPSH((y,x)),((x:=ÄÊPKE(0)[0]),(y:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	return x+SR_int(2**64-1)*((y-x)/(2**64-1))
def SR_choice(x):return x[SR_int(ãÊú(x)-1)]
def SR_shuffle(x,n=None):
	if n is None:(n:=ãÊú(x))
	elif(ÄÊPSH(n),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),áÍÞ)),(n:=ÄÊPKE(0)),ÄÊDEL(2))[2]>ãÊú(x):ÄÊPOP(0)if ÄÊPSH(False)else ÂùÆ(ÄÊPOP(0),'Cannot shuffle (%s > %s)'%(n,ãÊú(x)))
	(ÄÊPSH(([*x],ÂÚü())),((X:=ÄÊPKE(0)[0]),(Y:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	for _ in ÂÿÇ(n):Y.append(X.pop(SR_int(ãÊú(X)-1)))
	return Y
def SR_str(n=24,chars=None):return Âøî(ÁØò(lambda ÂîÓ:SR_choice(abcABC123 if chars is None else chars))(ÂÿÇ(n)),ÁØã)
@OPWRAP_(*'\ue270\U000f114f\uf074')
def _(áÑã,áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ):
	def Æå():
		if áÑã=='\uf074':
			ÂùÆ(áÓö(áØÆ)or áÓö(áØÇ));(ÄÊPSH((áØÆ,áØÇ)if áÓö(áØÆ)else(áØÇ,áØÆ)),((áÏË:=ÄÊPKE(0)[0]),(n:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
			if n is ÂÞÅ:return SR_shuffle(áÏË)
			return ÁØò(lambda ÂîÓ:SR_choice(áÏË))(ÂÿÇ(n))
		if(áØÆ is ÄÊPSH(ÂÞÅ)and ÄÊPOP(0)is ÄÊPSH(áØÇ))and(ÄÊDEL(1)or True)or(ÄÊDEL(1)or False):return SR_float(*(ÂÕÀ(1)if áÑã=='\ue270'else ÂÿÇ(1)))
		(Æå:=SR_float if áÑã=='\ue270'else SR_int)
		if(áØÆ is not ÄÊPSH(ÂÞÅ)and ÄÊPOP(0)is not ÄÊPSH(áØÇ))and(ÄÊDEL(1)or True)or(ÄÊDEL(1)or False):return Æå(áØÆ,áØÇ)
		if áÓö((áÑÿ:=áØÇ if áØÆ is ÂÞÅ else áØÆ)):return Æå(*áÑÿ)
		else:return Æå(0,áÑÿ)
		ÂùÆ(False)
	return ÐÌü(Æå)if áØÁ is ÂÞÅ else ËãÂ(MOD(ÂÚü,áØÁ=áØÁ)(),Æå)
(ÄïÉð:=(sha:=Cmap(ÁÁ,{ÁÁ:lambda*áÑË,**áÑÕ:ÂÞÅCAT(_sha256(áÍÇ(ÁÜÙ(áÑË)+ÁÜÙ(áÑÕ))).digest(),ÄïÊÀ),áÍî:lambda x:_sha256(MOD(Áëý,áØÁ=ÄÊCUR((1,),{},ÄÝøÇ,ÂýÃ,áÍî))(x,áÍÇ)).digest()})))
(ÄÊPSH((MOD(lambda ÂîÓ:ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ,áÍÇ),zibe),b85e),áÍÇ)),MOD(lambda ÂîÓ:ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ,áÍÇ),b85d),zibd),áÍÇ)))),((stre:=ÄÊPKE(0)[0]),(strd:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ÄïÉö:=(ÄïÉù:=(áÐÞ:=Cmap(ÁÁ,{ÁÁ:ÄÊCUR((1,),{'ensure_ascii':False,'indent':None,'separators':',:'},jdumps__,ÂýÃ),ÿ:jloads__}))))
(ÄïÊÀ:=Cmap(ÁÁ,{ÁÁ:lambda x:áÍÇ(urlsafe_b64encode(MOD(Áëý,áØÁ=ÄÊCUR((1,),{},ÄÝøÇ,ÂýÃ,áÍî))(x,áÍÇ))).rstrip('='),ÿ:lambda x:urlsafe_b64decode(áÍÇ(MOD(Áëý,áØÁ=ÄÊCUR((1,),{},ÁØö,ÂýÃ,áÍî))(x,áÍÇ)+'='*(4-ãÊú(x)%4)))}))
try:from Crypto.Cipher import AES;from Crypto.Util.Padding import pad,unpad
except áÍÚ as Ðáü:ÄÊPOP(0)if ÄÊPSH(False)else MOD(ÂùÆ,áØÁ=ÂÄ)(ÄÊPOP(0),'Failed to import AES libraries! Do you have pycryptodome installed?')
def AES_ENC_SIV(áÖú,k):return ÂøÑ(AES.new(k,AES.MODE_SIV).encrypt_and_digest(áÖú))
def AES_DEC_SIV(m,k):return AES.new(k,AES.MODE_SIV).decrypt_and_verify(*áÇù(m,-16))
def ENC_BYTES(áÖú,k,áÕÎ=True):
	if áÕÎ:(áÖú:=SR_bytes(8)+áÖú)
	(n:=(16-(ãÊú(áÖú)+1)%16)%16);return AES_ENC_SIV(ÂÞÅCAT([n+1+(8 if áÕÎ else 0),*ÂÞÅCAT([0],n),*áÖú],áÍî),(lambda ÂîÓ:ÂîÓ+ÂÞÅCAT(ÂîÓ,ÄïÉð[áÍî]))(ÂÞÅCAT(k,ÄïÉð[áÍî])))
def DEC_BYTES(m,k):return(lambda ÂîÓ:ÂîÓ[slice(ÂîÓ[0],None)])(AES_DEC_SIV(m,(lambda ÂîÓ:ÂîÓ+ÂÞÅCAT(ÂîÓ,ÄïÉð[áÍî]))(ÂÞÅCAT(k,ÄïÉð[áÍî]))))
class ÄïÉï:(__getitem__:=lambda x,y:Cmap(ÁÁ,{ÁÁ:lambda x:ENC_BYTES(ÂÞÅCAT(ÂÞÅCAT(x,ÄïÉù[ÁÁ]),áÍÇ),y,True),Âúú:lambda x:ENC_BYTES(ÂÞÅCAT(ÂÞÅCAT(x,ÄïÉù[ÁÁ]),áÍÇ),y,False),ÿ:lambda x:ÂÞÅCAT(ÂÞÅCAT(DEC_BYTES(x,y),áÍÇ),ÄïÉù[ÿ])}));(__getattr__:=__getitem__)
(ÄïÉï:=ÐÌü(ÄïÉï))
__dir__=(__file__:=áÌî(moon_dir/'Builtins/\uea7b.☾')).parent
(TMPDIR:=ÂÞÅCAT(env.get('MOON_TMPDIR',ð(ÂÞÅCAT('/dev/shm',áÌî),'☾_tmp')),áÌî))
(CACHEDIR:=ÂÞÅCAT(env.get('MOON_CACHEDIR',ð(TMPDIR,'cache')),áÌî))
(mkd:=lambda f,e=True,p=True:ÂåÔ((p:=ÂÞÅCAT(f,áÌî)).mkdir(exist_ok=e,parents=p),p))
(mkf:=lambda f,e=True:ÂåÔ(ÂåÔ(mkd((p:=ÂÞÅCAT(f,áÌî)).parent),p).touch(exist_ok=e),p))
(tmpf:=lambda b=ÁØã,f=ÂÞÅ,n=14:mkf(ð((lambda ÂîÓ:MOD(Áëý,áØÁ=b)(ÂîÓ,ÄÊCUR((1,),{},ð,ÂýÃ,b)))(TMPDIR),ÂÞÅCAT(n,SR_str)if f is ÂÞÅ else f)))
(tmpd:=lambda b=ÁØã,f=ÂÞÅ,n=14:mkd(ð((lambda ÂîÓ:MOD(Áëý,áØÁ=b)(ÂîÓ,ÄÊCUR((1,),{},ð,ÂýÃ,b)))(TMPDIR),ÂÞÅCAT(n,SR_str)if f is ÂÞÅ else f)))
class suppar2:(__init__:=lambda áÑÞ,Æå:ÂåÔ((ÄÊPSH(Æå),ÄÊPSH(áÑÞ),ÄÊPSH('Æå'),setattr(ÄÊPKE(1),ÄÊPKE(0),ÄÊPKE(2)),ÄÊDEL(3))[3],None));(__call__:=lambda áÑÞ,*áÑË,**áÑÕ:áÑÞ.Æå(*áÑË,**áÑÕ));(__getitem__:=(__getattr__:=lambda áÑÞ,x,*áÑË,**áÑÕ:lambda*áÑË,**áÑÕ:áÑÞ.Æå(*áÑË,x,**áÑÕ)))
(ÐâÒ:=lambda x=ÂÞÅ:ÐÌü(PL_TEXT_PASTE)if x is ÂÞÅ else ÂåÔ(ÂÞÅCAT(ÂÞÅCAT(x,ÁÜÙ),PL_TEXT_COPY),x))
(ÐÈÃ:=suppar2(lambda f,o=ÁØã:áÌî(f).open(o)))
(ÐØó:=suppar2(lambda f,o=ÁØã:Âáõ((y:=ÐÈÃ['r'+o](f)),lambda x:ÐÌü(x.read))))
(ÐØì:=suppar2(lambda f,áÏû,o=ÁØã:Âáõ((y:=ÐÈÃ['w'+o](f)),lambda x:ÂåÔ(x.write(áÏû),y))))
(pwd:=lambda*áÑË,**áÑÕ:áÌî(ÐÌü(os.getcwd)))
class cd:
	(ÄÊPSH(MOD(ÂÚü,áØÁ=2)()),((s:=ÄÊPKE(0)[0]),(c:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	def __init__(áÑÞ,d=None):(ÄÊPSH(áÑÞ),ÄÊPSH('d'),ÄÊPSH(d),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
	def __enter__(áÑÞ):
		(x:=áÑÞ.d);cd.s.append((ãÊú(cd.c),(x:=ÐÌü(pwd))))
		if x is not None:os.chdir(áÌî(x))
		return ÐÌü(pwd)
	def __exit__(áÑÞ,*áÑË):(ÄÊPSH(cd.s.pop(-1)),((i:=ÄÊPKE(0)[0]),(d:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1];(ÄÊPSH(cd),ÄÊPSH('c'),ÄÊPSH(cd.c[slice(None,i)]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3];os.chdir(d);return ÐÌü(pwd)
	def __call__(áÑÞ,d=None):
		if d is ÁÃ:return cd(áÌî(inspect.stack()[1].filename).parent)
		if d is None:os.chdir(cd.c.pop(-1));return ÐÌü(pwd)
		cd.c.append(ÐÌü(pwd));os.chdir(d);return ÐÌü(pwd)
	def __getitem__(áÑÞ,d):return áÑÞ.__class__(d)
(cd:=ÐÌü(cd))
__dir__=(__file__:=áÌî(moon_dir/'Builtins/🌈.☾')).parent
def h2r(c=ÁØã):
	if ÁØö(c,áÍÞ):(ÄÊPSH(c),ÄÊPSH(MOD(ÄÝöì,áØÁ=16)(ÄÊPKE(0))),(c:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	(c:=c.strip().lstrip('#'))
	if c.startswith('0x'):(ÄÊPSH(c),ÄÊPSH(ÄÊPKE(0)[slice(2,None)]),(c:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	(ÄÊPSH((ÄÊCUR((1,),{},áÍÞ,ÂýÃ,16),ãÊú(c))),((ÂÐí:=ÄÊPKE(0)[0]),(n:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	if n==0:return 0,0,0,255
	if n==1:return ÂÐí(ÂÞÅCAT(c[0],2)),ÂÐí(ÂÞÅCAT(c[0],2)),ÂÐí(ÂÞÅCAT(c[0],2)),255
	if n==2:return ÂÐí(ÂÞÅCAT(c[0],2)),ÂÐí(ÂÞÅCAT(c[0],2)),ÂÐí(ÂÞÅCAT(c[0],2)),ÂÐí(ÂÞÅCAT(c[1],2))
	if n==3:return ÂÐí(ÂÞÅCAT(c[0],2)),ÂÐí(ÂÞÅCAT(c[1],2)),ÂÐí(ÂÞÅCAT(c[2],2)),255
	if n==4:return ÂÐí(ÂÞÅCAT(c[0],2)),ÂÐí(ÂÞÅCAT(c[1],2)),ÂÐí(ÂÞÅCAT(c[2],2)),ÂÐí(ÂÞÅCAT(c[3],2))
	if n==5:return ÂÐí(ÂÞÅCAT(c[0],2)),ÂÐí(ÂÞÅCAT(c[1],2)),ÂÐí(ÂÞÅCAT(c[2],2)),ÂÐí(c[slice(3,5)])
	if n==6:return ÂÐí(c[slice(0,2)]),ÂÐí(c[slice(2,4)]),ÂÐí(c[slice(4,6)]),255
	if n==7:return ÂÐí(c[slice(0,2)]),ÂÐí(c[slice(2,4)]),ÂÐí(c[slice(4,6)]),ÂÐí(ÂÞÅCAT(c[6],2))
	if n==8:return ÂÐí(c[slice(0,2)]),ÂÐí(c[slice(2,4)]),ÂÐí(c[slice(4,6)]),ÂÐí(c[slice(6,8)])
(r2hl:=lambda x:'#%s'%(Âøî(Áÿú(x,MOD(ÄÝöì,áØÁ=16+ÂÞÅCAT(2,Ãù)))),))
(h2hl:=Âåæ(r2hl,h2r))
def rgb2hsv(r,g,b):(ÄÊPSH(Âîí([r,g,b])),((m:=ÄÊPKE(0)[0]),(v:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1];(s:=(ÏÁ:=v-m)/v if v else 0);(h:=((g-b)/ÏÁ%6 if v==r else(b-r)/ÏÁ+2 if v==g else(r-g)/ÏÁ+4)*60%360 if v else 0);return h/360,s,v
def hsv2rgb(h,s,v):(ÄÊPSH(h),ÄÊPSH(ÄÊPKE(0)*360%360),(h:=ÄÊPKE(0)),ÄÊDEL(2))[2];(ÄÊPSH((s,v)),ÄÊPSH(Áÿú(ÄÊPKE(0),ÄÝöÓ(0,1))),((s:=ÄÊPKE(0)[0]),(v:=ÄÊPKE(0)[1])),ÄÊDEL(2))[2];(x:=(c:=v*s)*(1-ÂüÌ(h/60%2-1)));return ÁØòþÁÙÄ(lambda ÂîÓ,ÂîÒ:ÂîÓ+ÂîÒ)([c,x,0]if h<=60 else[x,c,0]if h<=120 else[0,c,x]if h<=180 else[0,x,c]if h<=240 else[x,0,c]if h<=300 else[c,0,x],v-c)
(TERM_RESET_B:='\x1b[49m')
(TERM_RESET_F:='\x1b[39m')
(TERM_RESET:='\x1b[0m')
(styd:=ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(ð(moon_dir,'Builtins/Data/style.json'),ÐØó),áÐÞ[ÿ]),ÂÑÖ()))
def termclr(t,fg=None,bg=None,rst=True,rl=False):(rlw:=lambda x:'\x01%s\x02'%(x,)if rl else x);(mkc:=lambda x,y,z,w,v:ÂÞÅCAT('\x1b[%s;2;%s;%s;%sm'%(x,y,z,w),rlw));(R:=Âøî([mkc(n,*h2r(c))for(c,n)in ÄÕåØ([fg,bg],[38,48])if c is not None]));return'%s%s%s'%(R,t,rlw(ÁØã if fg is None and bg is None else TERM_RESET_B if fg is None else TERM_RESET_F if bg is None else TERM_RESET)if rst else ÁØã)
@cache_
def sty(s,bg=0,def_='bec'):
	for(k,v)in styd:
		if not(s in k and ÂÔö(v,'fg')):continue
		return termclr(s,v['fg'],bg)
	return termclr(s,def_,bg)
(__highlighter__:=lambda l,b=None,clr='bec':Âøî(Áÿú(ÂÞÅCAT(ÂÞÅCAT(l,ÁÜÙ),VEP),ÄÊCUR((1,),{},sty,ÂýÃ,b,clr))))
def highlight_tester():
	while(l:=ÐÌü(ÂÐðþáÐâ.readline)):Âçß(ÂÞÅCAT(ÂÞÅCAT('\n',l.rstrip),__highlighter__))
__dir__=(__file__:=áÌî(moon_dir/'Builtins/\uea8c.☾')).parent
(áÍù:=áÓö)
def adjust_depth(áØÆ,áØÁ,áÍù=áÓö):
	if áØÁ is ÂÞÅ:return 1
	if áØÁ>=0:return áØÁ
	(ÄÊPSH((áØÆ,0)),((áØÆ:=ÄÊPKE(0)[0]),(k:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	while(ÄÊPSH(k),ÄÊPSH(ÄÊPKE(0)+1),(k:=ÄÊPKE(0)),ÄÊDEL(2))[2]if áÍù(áØÆ)else None:
		if ÁØö(áØÆ,ÁÜÙ):break
		if ÁØö(áØÆ,ÁÜÙ)or not ãÊú(áØÆ):break
		(ÄÊPSH(áØÆ),ÄÊPSH(ÄÊPKE(0)[0]),(áØÆ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	return ÂóÍ(áØÁ+k-1,0)
def flatten(áØÆ,áØÁ=ÂÞÅ,áÖÞ=None,áÍù=áÓö):
	(áØÁ:=adjust_depth(áØÆ,áØÁ))
	if áÖÞ is None:(áÖÞ:=ÂÚü())
	if(áØÁ<=0 or not áÍù(áØÆ))or ÁØñ(ÁÜÙ,áØÆ):return ÂåÔ((áÖÞ.extend if áÍù(áØÆ)else áÖÞ.append)(áØÆ),áÖÞ)
	for x in áØÆ:flatten(x,áØÁ-1,áÖÞ,áÍù=áÍù)
	return áÖÞ
def chain_structure(áØÆ,áØÁ=ÂÞÅ,áÍù=áÓö):
	(áØÁ:=adjust_depth(áØÆ,áØÁ))
	if(áØÁ<=0 or not áÍù(áØÆ))or ÁØö(áØÆ,ÁÜÙ):return MOD(Âêà,áØÁ=ãÊú(áØÆ))(None)if áÍù(áØÆ)else None
	return ÁØò(lambda ÂîÓ:chain_structure(ÂîÓ,áØÁ-1,áÍù=áÍù))(áØÆ)
def deflatten(áØÆ,áÖÛ,áÍù=áÓö):
	if áÖÛ is None:return áØÆ.pop(0)if áØÆ else ÄÔýò
	return ÁØò(lambda ÂîÓ:deflatten(áØÆ,ÂîÓ,áÍù=áÍù))(áÖÛ)
def flatten_under(áØÆ,Æå,áØÁ=ÂÞÅ,ÁÜñ=ÂÞÅ,áÍù=áÓö):
	(áØÁ:=adjust_depth(áØÆ,áØÁ))
	if ÁÜñ is ÂÞÅ:(ÁÜñ:=flatten(áØÆ,áØÁ,áÍù=áÍù))
	return deflatten(Æå(ÁÜñ),chain_structure(áØÆ,áØÁ,áÍù=áÍù))
def ÄÔÙù(áØÆ=ÂÞÅ,áØÇ=ÂÞÅ,áØÁ=ÂÞÅ,ÁÜñ=ÂÞÅ):
	if((áØÆ is not ÄÊPSH(ÂÞÅ)and ÄÊPOP(0)is not ÄÊPSH(áØÇ))and(ÄÊDEL(1)or True)or(ÄÊDEL(1)or False))and((ÁØö(áØÆ,ÄÊPSH(áÍÞ))and ÁØñ(ÄÊPOP(0),ÄÊPSH(áØÇ)))and(ÄÊDEL(1)or True)or(ÄÊDEL(1)or False)):ÄÊPOP(0)if ÄÊPSH(ÁÜñ is ÂÞÅ)else ÂùÆ(ÄÊPOP(0),'\U000f0931');return ÄÝöì('%s%s'%(ÄÝöì(ÂüÌ(áØÆ)),ÄÝöì(ÂüÌ(áØÇ))))*(ÂÞÅCAT(ÃÆí(ÄÊCUR((2,),{},ÂØú,ÃÆí(áØÆ),ÂýÃ)),áØÇ)or 1)
	if áØÇ is not ÂÞÅ:(áØÆ:=[áØÆ,áØÇ])
	if ÁÜñ is not ÂÞÅ:
		if áÍù(ÁÜñ):return flatten_under(áØÆ,ÄÕÍÔ,áØÁ,[*ÁÜñ])
		return flatten_under(áØÆ,ÁÜñ,áØÁ)
	return flatten(áØÆ,áØÁ,áÍù=áÓö)
(ÄÝõÞ:=lambda áØÆ,áØÁ=ÂÕË:ÂÚü()if ÄÝøÇ(áØÆ,áÓö)else ÁØò(lambda ÂîÓ:ãÊú(ÂîÓ)if ÁØö(ÂîÓ,áÓö)else ÄÔýò)(ÂÕÅ(MOD(ÂØÎ,áØÁ=-áØÁ)(MOD(lambda ÂîÓ:ÂîÓ[0]if ãÊú(ÂîÓ)else 0),MOD(lambda ÂîÓ:ÄÝøÇ(ÂîÓ,áÓö)or ÁØö(ÂîÓ,ÁÜÙ))),áØÆ)))
(ÄÝõß:=lambda áØÆ,áØÁ=ÂÕË:ãÊú(MOD(ÄÝõÞ,áØÁ=áØÁ)(áØÆ)))
(ÐÈÔ:=lambda áØÆ,áØÇ,áØÁ=ÂÞÅ:MOD(ÆÑ,áØÁ=áØÆ)(ÂÀÇ(áØÇ),lambda x,y:MOD(ÁâÁ,áØÁ=y-1)(x)))
(ÄÔÒØ:=lambda áØÆ,áØÁ=ÂÕË:MOD(ÄÔÙù,áØÁ=MOD(ÄÝõß,áØÁ=áØÁ)(áØÆ)-1)(áØÆ))
@OPWRAP_(*'⪡⪢')
def _(áÑã,áØÆ=ÂÞÅ,áØÇ=1,áØÁ=ÂÞÅ):
	if ÁØö(áØÆ,ÂÑÅ):return áØÆ>>áØÇ if áÑã=='⪢'else áØÆ<<áØÇ
	if(ÁØö(áØÆ,ÄÊPSH(ÁÜÙ|áÍá|áÍé))and ÁØñ(ÄÊPOP(0),ÄÊPSH(áØÇ)))and(ÄÊDEL(1)or True)or(ÄÊDEL(1)or False):ÄÊPOP(0)if ÄÊPSH(áØÁ is ÂÞÅ)else ÂùÆ(ÄÊPOP(0),'\U000f0931 idk what this should do');return áØÆ+áØÇ if áÑã=='⪢'else áØÇ+áØÆ
	ÂùÆ(ÁØö(áØÇ,ÂÑÅ))
	if áÑã=='⪡':(ÄÊPSH(áØÇ),ÄÊPSH(ÄÝöâ(ÄÊPKE(0))),(áØÇ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	if áØÁ is ÂÞÅ:return áØÆ and áØÆ[slice((i:=-áØÇ%ãÊú(áØÆ)),None)]+áØÆ[slice(None,i)]
	return ÐÈÔ(MOD(ÄÔÒØ,áØÁ=áØÁ)(áØÆ),Âúú(MOD(ÄÝõÞ,áØÁ=áØÁ)(áØÆ),áØÇ))
__dir__=(__file__:=áÌî(moon_dir/'Builtins/Ń.☾')).parent
from collections import deque as áÐòþáÑÁ
class ÅÒ:
	(__slots__:=('t','c','e'));(MCH:=lambda Æå:CURR(lambda ÂîÓ,ÂîÒ:ÂîÓ.t in ÂîÒ,frozenset(Æå))if ÁØö(Æå,áÍé|áÍá)else CURR(lambda ÂîÓ,ÂîÒ:ÂîÓ.t==ÂîÒ,Æå)if ÁØö(Æå,ÁÜÙ)else Æå)
	def __init__(ÄÕÒü,t,*c,e=ÂÞÅ):
		(ÄÊPSH(ÄÕÒü),ÄÊPSH('t'),ÄÊPSH(ÄÕÒü),ÄÊPSH('c'),ÄÊPSH(ÄÕÒü),ÄÊPSH('e'),ÄÊPSH((t,[*c]if c else[],MOD(ÂÑÖ,áØÁ=None)()if e is ÂÞÅ else e)),(setattr(ÄÊPKE(6),ÄÊPKE(5),ÄÊPKE(0)[0]),setattr(ÄÊPKE(4),ÄÊPKE(3),ÄÊPKE(0)[1]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)[2])),ÄÊDEL(7))[7]
		for z in ÄÕÒü.c:
			if not ÄÝøÇ(z,ÅÒ):continue
			ÄÊPOP(0)if ÄÊPSH(False)else ÂùÆ(ÄÊPOP(0),'Cannot construct Ń(%s,%s), ⟨%s⟩ \U0010029e Ń'%(t,Âøî(Áÿú(c,ÁÜÙ),', '),z))
	(__contains__:=lambda ÄÕÒü,x:x in ÄÕÒü.e if ÁØö(x,ÁÜÙ)else x in ÄÕÒü.c);(__repr__:=lambda ÄÕÒü:'Ń(%s│%s)⟨%s⟩'%(ÄÕÒü.t or'∅',ÄÕÒü.e or'∅',Âøî(ÄÕÒü,', ')));(__setitem__:=lambda ÄÕÒü,x,y:(ÄÊPSH(ÄÕÒü.c),ÄÊPSH(x),ÄÊPSH(y),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]);(__and__:=lambda ÄÕÒü,x:ÄÕÒü.t==x.t);(__len__:=lambda ÄÕÒü:ãÊú(ÄÕÒü.c));(__iter__:=lambda ÄÕÒü:iter(ÄÕÒü.c))
	def __getitem__(ÄÕÒü,i):return ÄÕÒü.c[i]
	def __delitem__(ÄÕÒü,i):del ÄÕÒü.c[i]
	def set(ÄÕÒü,t=None,c=None,e=None):
		if t is not None:(ÄÊPSH(ÄÕÒü),ÄÊPSH('t'),ÄÊPSH(t),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		if c is not None:(ÄÊPSH(ÄÕÒü),ÄÊPSH('c'),ÄÊPSH(c),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		if e is not None:(ÄÊPSH(ÄÕÒü),ÄÊPSH('e'),ÄÊPSH(e),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		return ÄÕÒü
	def from_(ÄÕÒü,R):(ÄÊPSH(ÄÕÒü),ÄÊPSH('t'),ÄÊPSH(R.t),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3];(ÄÊPSH(ÄÕÒü),ÄÊPSH('c'),ÄÊPSH(R.c),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3];(ÄÊPSH(ÄÕÒü),ÄÊPSH('e'),ÄÊPSH(R.e),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3];return ÄÕÒü
	(cp:=(copy:=lambda ÄÕÒü,t=None,c=None,e=ÂÞÅ:ÅÒ(ÄÕÒü.t if t is None else t,*(ÄÕÒü.c if c is None else c),e=ÄÕÒü.e.copy()if e is ÂÞÅ else e)));(cpr:=(rcopy:=lambda ÄÕÒü:ÅÒ(ÄÕÒü.t,*Áÿú(ÄÕÒü.c,ÅÒ.cpr),e=ÄÕÒü.e.copy())))
	def part(ÄÕÒü):(ÄÊPSH(ÄÕÒü),ÄÊPSH('c'),ÄÊPSH(ÂÕÃ(ÄÕÒü.c,ÄÕÒü.e**ì)),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3];return ÄÕÒü,ÄÕÒü.e
	def frp(ÄÕÒü,Æå,r,pre=False,not_T=True):
		if r is None:return lambda x:ÄÕÒü.frp(Æå,x,pre,not_T)
		(ÄÊPSH(Æå),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),ÅÒ.MCH)),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
		if not_T:(Æå:=lambda ÄÕÒü,Æå=Æå:not ÄÕÒü.e.T and Æå(ÄÕÒü))
		if pre:
			if not ãÊú(ÄÕÒü):return r(ÄÕÒü)if Æå(ÄÕÒü)else ÄÕÒü
			(ÄÊPSH((áÐòþáÑÁ([ÄÕÒü]),áÐòþáÑÁ())),((áÖå:=ÄÊPKE(0)[0]),(áÖæ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1];(ÄÊPSH((áÖå.popleft,áÖå.extend,áÖæ.appendleft)),((pl:=ÄÊPKE(0)[0]),(ex:=ÄÊPKE(0)[1]),(al:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
			while áÖå:(C:=pl());ex([c for c in C if c.c]);al(C)
			for C in áÖæ:
				for(i,c)in enumerate(C):
					if not Æå(c):continue
					(ÄÊPSH(C),ÄÊPSH(i),ÄÊPSH(r(c)),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
			return r(ÄÕÒü)if Æå(ÄÕÒü)else ÄÕÒü
		else:
			def áÏï(ÄÕÒü):
				if Æå(ÄÕÒü):return r(ÄÕÒü)
				for(i,y)in enumerate(ÄÕÒü):(ÄÊPSH(ÄÕÒü),ÄÊPSH(i),ÄÊPSH(áÏï(y)),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
				return ÄÕÒü
			return áÏï(ÄÕÒü)
	def ftrp(ÄÕÒü,fs,Æå,pre=False,not_T=True,**áÏè):
		if Æå is None:return lambda x:ÄÕÒü.ftrp(fs,x,pre,not_T,**áÏè)
		(ÄÊPSH(Æå),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),ÅÒ.MCH)),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2];return ÄÕÒü if not_T and ÄÕÒü.e.T else ÄÕÒü.frp((lambda x:x.t==fs)if ÁØö(fs,ÁÜÙ)else lambda x:x.t in fs,Æå,pre,not_T,**áÏè)
	def ftrpm(ÄÕÒü,*áÑË,not_T=True):
		(M:={})
		for(k,v)in áÑË:
			if ÁØö(k,áÍé|áÍá):
				for Ïè in k:(ÄÊPSH(M),ÄÊPSH(Ïè),ÄÊPSH(v),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
			else:(ÄÊPSH(M),ÄÊPSH(k),ÄÊPSH(v),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		(ÄÊPSH((áÐòþáÑÁ([ÄÕÒü]),áÐòþáÑÁ())),((áÖå:=ÄÊPKE(0)[0]),(áÖæ:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1];(ÄÊPSH((áÖå.popleft,áÖå.extend,áÖæ.appendleft)),((pl:=ÄÊPKE(0)[0]),(ex:=ÄÊPKE(0)[1]),(al:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
		while áÖå:(C:=pl());ex([c for c in C if c.c]);al(C)
		áÖæ.append((holder:=ÅÒ(ÁØã,ÄÕÒü)))
		for C in áÖæ:
			for(i,c)in enumerate(C):
				if not(((ÄÊDEL(1),False)[1]if c.e.T else ÄÊPOP(0))if ÄÊPSH(not_T)else(ÄÊDEL(1),True)[1]):continue
				if c.t in M:(ÄÊPSH(C),ÄÊPSH(i),ÄÊPSH(M[c.t](c)),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		return ÄÕÒü.from_(holder[0])
	def gets(ÄÕÒü,Æå,not_T=True):(ÄÊPSH(Æå),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),ÅÒ.MCH)),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2];return[c for c in ÄÕÒü if(((ÄÊDEL(1),False)[1]if c.e.T else ÄÊPOP(0))if ÄÊPSH(not_T)else(ÄÊDEL(1),True)[1])and Æå(c)]
	def find(ÄÕÒü,Æå,pre=True,not_T=True,R=None):
		(ÄÊPSH(Æå),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),ÅÒ.MCH)),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
		if R is None:(R:=ÂÚü())
		if not_T and ÄÕÒü.e.T:return R
		if pre:
			for c in ÄÕÒü:c.find(Æå,True,not_T,R)
		if(do:=Æå(ÄÕÒü)):R.append(ÄÕÒü)
		if do and not pre:
			for c in ÄÕÒü:c.find(Æå,False,not_T,R)
		return R
	def rm(ÄÕÒü,Æå,not_T=True):
		(ÄÊPSH(Æå),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),ÅÒ.MCH)),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
		for(i,x)in ÂÓÏ(ÄÕÒü)[slice(None,None,-1)]:
			if not(((ÄÊDEL(1),False)[1]if x.e.T else ÄÊPOP(0))if ÄÊPSH(not_T)else(ÄÊDEL(1),True)[1]):continue
			if Æå(x):del ÄÕÒü[i]
			else:ÄÕÒü[i].rm(Æå,not_T)
		return ÄÕÒü
	def sep(ÄÕÒü,*áÑË,**áÑÕ):(M:=ÄÕÒü.find(*áÑË,**áÑÕ));ÄÕÒü.rm(CURR(lambda ÂîÓ,ÂîÒ:ÂÞÅCAT(ÂîÓ,id)in ÂîÒ,frozenset(Áÿú(M,id))));return M
	def flat(ÄÕÒü,Æå,áÑÂ=True):
		(ÄÊPSH(Æå),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),ÅÒ.MCH)),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2];(C:=[])
		for c in ÄÕÒü:(C.append if c.e.T or not Æå((c:=c.flat(Æå)if áÑÂ else c))else C.extend)(c)
		(ÄÊPSH(ÄÕÒü),ÄÊPSH('c'),ÄÊPSH(C),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3];return ÄÕÒü
	def __pos__(ÄÕÒü):
		(áØÀ:='')
		if ÄÕÒü.e.T:return ÄÕÒü.t
		(áÖã:=áÐòþáÑÁ(ÄÕÒü.c))
		while áÖã:
			(v:=áÖã.popleft())
			if v.e.T:(ÄÊPSH(áØÀ),ÄÊPSH(ÄÊPKE(0)+v.t),(áØÀ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
			else:áÖã.extendleft(reversed(v.c))
		return áØÀ
	def lchar(ÄÕÒü):
		if ÄÕÒü.e.T and ÄÕÒü.t:return ÄÕÒü.t[0]
		for c in ÄÕÒü.c:
			if not(x:=c.lchar()):continue
			return x
		return''
	def rchar(ÄÕÒü):
		if ÄÕÒü.e.T and ÄÕÒü.t:return ÄÕÒü.t[-1]
		for c in ÄÕÒü.c[slice(None,None,-1)]:
			if not(x:=c.rchar()):continue
			return x
		return''
	def farnodes(ÄÕÒü,Æå=MOD(lambda ÂîÓ:not ÂîÓ.e.T)):
		(ÄÊPSH(Æå),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),ÅÒ.MCH)),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2];(Ïß:=(Ïà:=ÄÕÒü))
		while Æå(Ïß)and ãÊú(Ïß):(Ïß:=Ïß[0])
		while Æå(Ïà)and ãÊú(Ïà):(Ïà:=Ïà[-1])
		return Ïß,Ïà
	def first_l(ÄÕÒü,Æå):
		(ÄÊPSH(Æå),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),ÅÒ.MCH)),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
		if Æå(ÄÕÒü):return ÄÕÒü
		for áÎÚ in ÄÕÒü:
			if not(l:=áÎÚ.first_l(Æå))is not None:continue
			return l
	def first_r(ÄÕÒü,Æå):
		(ÄÊPSH(Æå),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),ÅÒ.MCH)),(Æå:=ÄÊPKE(0)),ÄÊDEL(2))[2]
		if Æå(ÄÕÒü):return ÄÕÒü
		for áÎÚ in ÄÕÒü[slice(None,None,-1)]:
			if not(r:=áÎÚ.first_r(Æå))is not None:continue
			return r
	(first_sides:=lambda ÄÕÒü,Æå:(ÄÕÒü.first_l(Æå),ÄÕÒü.first_r(Æå)));(filter:=lambda ÄÕÒü,Æå,*áÑË,**áÑÕ:ÄÕÒü.rm(Âåæ(Âó,Æå),*áÑË,**áÑÕ))
	@property
	def ÄÔÕý(áÑÞ):return+áÑÞ
	def P(ÄÕÒü,fs=True):
		if not hasattr(ÅÒ,'txt_format_imported'):(ÄÊPSH(ÅÒ),ÄÊPSH('txt_format_imported'),ÄÊPSH(True),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3];(ÄÊPSH(__ÄÊIMPORT__('text_format',globals(),'')),ÄÊPOP(0))[-1]
		(ÄÊPSH(ËãÂ(ÂÛê('∅\u2009f00\u205f→\u200900f\u205f\U000f0141\u2009ff0\u205f\U000f0142\u2009ff0'),Åøþáüì)),((NA:=ÄÊPKE(0)[0]),(AR:=ÄÊPKE(0)[1]),(yl:=ÄÊPKE(0)[2]),(yr:=ÄÊPKE(0)[3])),ÄÊDEL(1))[1]
		if ÄÝøÇ(ÄÕÒü,ÅÒ):return Åøþáüì(ÁÜÙ(ÄÕÒü),'f00')
		def format_e(e):
			if not e:return ÁØã
			(r:=ËãÂ(e,lambda x,y:ÄÔýò if x in{*'Tpρ'}else'%s%s%s'%(x,AR,y.t)if ÁØö(y,ÅÒ)else'%s=%s'%(x,y)));return MOD(Áëý,áØÁ=r)((Åøþáüì((lambda ÂîÓ:Âøî(ËãÂ(ÄÕåØ(Áÿú(ÂÿÇ(ÂîÓ),ÁÛÛ([ÄÝõà,ÄÝõá])),ÂîÓ),ÂÕÅ))if ãÊú(ÂîÓ)==4 else ÄÝõà(Âøî(ÂîÓ,'…')))(e.p),'ff0')if'p'in e else ÁØã)+(Åøþáüì((lambda ÂîÓ:Âøî(ËãÂ(ÄÕåØ(Áÿú(ÂÿÇ(ÂîÓ),ÁÛÛ([ÄÝõà,ÄÝõá])),ÂîÓ),ÂÕÅ))if ãÊú(ÂîÓ)==4 else ÄÝõà(Âøî(ÂîÓ,'…')))(getattr(e,'ρ')),'0ff')if'ρ'in e else ÁØã),MOD(lambda ÂîÓ:stackr(ÂîÓ,Âøî(r,'\n'))))
		(áØÀ:=box((ÂÞÅCAT(False,ÄÕÒü.t.P)if ÁØö(ÄÕÒü.t,ÅÒ)else stackr(Åøþáüì(ÄÕÒü.t,'f55'),ÂÞÅCAT(ÄÕÒü.e,format_e))if ÁØö(ÄÕÒü,ÅÒ)else ÁÜÙ(ÄÕÒü.t))or NA,fg='0f0'if ÁØö(ÄÕÒü,ÅÒ)and ÄÕÒü.e.T else'00007f'))
		if ãÊú(ÄÕÒü):(ÄÊPSH(Áÿú('─╰├┬│',ÄÊCUR((1,),{'fg':'11a'},Åøþáüì,ÂýÃ))),((ÂâÑ:=ÄÊPKE(0)[0]),(ÂäÇ:=ÄÊPKE(0)[1]),(Ââî:=ÄÊPKE(0)[2]),(ÂãÀ:=ÄÊPKE(0)[3]),(ÂâÓ:=ÄÊPKE(0)[4])),ÄÊDEL(1))[1];(áØÀ:=stackr(áØÀ,Âøî(ËãÂ(ÂÓÏ(ÄÕÒü),lambda x,y:Âøî(ËãÂ(ÂÓÏ(ÂÞÅCAT(ÂÞÅCAT(False,y.P),lines)),CUR(lambda ÂîÓ,ÂîÒ:ÂÁÍ(ì)(ÂîÒ,ÂâÑ if((ÄÊDEL(1),False)[1]if ÄÊPSH(ÂîÓ)else ÄÊPOP(0)if ãÊú(ÄÕÒü)!=1 else(ÄÊDEL(1),True)[1])else ÂîÓ and' 'or ÂäÇ if x==ãÊú(ÄÕÒü)-1 else x and Ââî or ÂãÀ if((ÄÊDEL(1),False)[1]if ÄÊPSH(ÂîÓ)else ÄÊPOP(0)if ãÊú(ÄÕÒü)==0 else(ÄÊDEL(1),True)[1])else ÂâÓ))),'\n')),'\n')))
		return ÂåÔ(Âçß(áØÀ),ÄÕÒü)if fs else áØÀ
__dir__=(__file__:=áÌî(moon_dir/'Builtins/cache.☾')).parent
class Cacher:
	def __init__(áÑÞ,Æå,áÕÈ,áÕÅ,áÕÄ):(ÄÊPSH(áÑÞ),ÄÊPSH('Æå'),ÄÊPSH(áÑÞ),ÄÊPSH('áÕÈ'),ÄÊPSH(áÑÞ),ÄÊPSH('áÕÅ'),ÄÊPSH(áÑÞ),ÄÊPSH('áÕÄ'),ÄÊPSH(áÑÞ),ÄÊPSH('áÍò'),ÄÊPSH((Æå,áÕÈ,áÕÅ,áÕÄ,{})),(setattr(ÄÊPKE(10),ÄÊPKE(9),ÄÊPKE(0)[0]),setattr(ÄÊPKE(8),ÄÊPKE(7),ÄÊPKE(0)[1]),setattr(ÄÊPKE(6),ÄÊPKE(5),ÄÊPKE(0)[2]),setattr(ÄÊPKE(4),ÄÊPKE(3),ÄÊPKE(0)[3]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)[4])),ÄÊDEL(11))[11]
	def __call__(áÑÞ,*áÑË,**áÑÕ):
		(áÖñ:=áÑÞ.áÕÈ(getattr(áÑÞ.Æå,'__name__',''),*áÑË,**áÑÕ))
		if(v:=áÑÞ.chk_cache(áÖñ))is not ÂÞÅ:return áÑÞ.áÕÄ(v)
		(v:=áÑÞ.Æå(*áÑË,**áÑÕ));áÑÞ.add_cache(áÖñ,áÑÞ.áÕÅ(v));return v
	def chk_cache(áÑÞ,x):return áÑÞ.áÍò.get(x,ÂÞÅ)
	def add_cache(áÑÞ,x,y):return(ÄÊPSH(áÑÞ.áÍò),ÄÊPSH(x),ÄÊPSH(y),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
class FileCacher(Cacher):
	def __init__(áÑÞ,Æå,áÕÈ,áÕÅ,áÕÄ,fp=ÁØã,file_only=True):super().__init__(Æå,áÕÈ,áÕÅ,áÕÄ);(ÄÊPSH(áÑÞ),ÄÊPSH('áÖòþáÖü'),ÄÊPSH(áÑÞ),ÄÊPSH('áÖòþáÖý'),ÄÊPSH((file_only,mkd(fp if ÁØö(fp,áÌî)and ÐÌü(fp.is_absolute)else ð(CACHEDIR,fp)))),(setattr(ÄÊPKE(4),ÄÊPKE(3),ÄÊPKE(0)[0]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)[1])),ÄÊDEL(5))[5]
	def __call__(áÑÞ,*áÑË,**áÑÕ):
		(log:='MOON_LOG_FCACHE'in env);(áÖñ:=áÑÞ.áÕÈ((fname:=getattr(áÑÞ.Æå,'__name__','')),*áÑË,**áÑÕ))
		if(v:=áÑÞ.chk_cache(áÖñ))is not ÂÞÅ:
			if log:Âçß('Cache hit (%s)!\n𝔸=%s\n𝕂=%s\n⇒%s'%(fname or None,ÁÜÙ(áÑË),ÁÜÙ(áÑÕ),ÁÜÙ(v)))
			return áÑÞ.áÕÄ(v)
		(v:=áÑÞ.Æå(*áÑË,**áÑÕ));áÑÞ.add_cache(áÖñ,áÑÞ.áÕÅ(v))
		if log:Âçß('Cache fail (%s)!\n𝔸=%s\n𝕂=%s\n⇒%s'%(fname or None,ÁÜÙ(áÑË),ÁÜÙ(áÑÕ),ÁÜÙ(v)))
		return v
	def chk_cache(áÑÞ,x):
		if not áÑÞ.áÖòþáÖü and x in áÑÞ.áÍò:return áÑÞ.áÍò[x]
		if ÐÌü((f:=ð(áÑÞ.áÖòþáÖý,x)).exists):(v:=ÐØó.b(f));return v if áÑÞ.áÖòþáÖü else(ÄÊPSH(áÑÞ.áÍò),ÄÊPSH(x),ÄÊPSH(v),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		return ÂÞÅ
	def add_cache(áÑÞ,x,y):ÐØì.b(ð(áÑÞ.áÖòþáÖý,x),y if áÑÞ.áÖòþáÖü else(ÄÊPSH(áÑÞ.áÍò),ÄÊPSH(x),ÄÊPSH(y),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3])
(mkmk_cache:=lambda ÆÚ:lambda áÕÈ=ÄïÉð,áÕÅ=pdump,áÕÄ=pload,*áÔå,**áÔï:lambda Æå:ÆÚ(Æå,áÕÈ,áÕÅ,áÕÄ,*áÔå,**áÔï))
(ÄÊPSH(Áÿú([Cacher,FileCacher],mkmk_cache)),((cache:=ÄÊPKE(0)[0]),(fcache:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ugex.☾')).parent
class winder:
	def __init__(áÑÞ,áÖï,áÖõ=-1):(ÄÊPSH(áÑÞ),ÄÊPSH('áÖï'),ÄÊPSH(áÑÞ),ÄÊPSH('áÖõ'),ÄÊPSH(áÑÞ),ÄÊPSH('áÖà'),ÄÊPSH((áÖï,áÖõ,ÂÚü())),(setattr(ÄÊPKE(6),ÄÊPKE(5),ÄÊPKE(0)[0]),setattr(ÄÊPKE(4),ÄÊPKE(3),ÄÊPKE(0)[1]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)[2])),ÄÊDEL(7))[7]
	(__bool__:=lambda áÑÞ:áÑÞ.áÖõ+1<ãÊú(áÑÞ.áÖï));(__repr__:=lambda áÑÞ:'[%s│%s]⟨%s⟩'%(ÂîË(áÑÞ.áÖï[slice(None,áÑÞ.áÖõ+1)],' '),ÂîÊ(áÑÞ.áÖï[slice(áÑÞ.áÖõ+1,None)],' '),Âøî(áÑÞ.áÖà,' ')));(peek:=lambda áÑÞ:áÑÞ.áÖï[áÑÞ.áÖõ+1]);(next:=lambda áÑÞ:áÑÞ.áÖï[(ÄÊPSH(áÑÞ),ÄÊPSH('áÖõ'),ÄÊPSH(getattr(ÄÊPKE(1),ÄÊPKE(0))),ÄÊPSH(ÄÊPKE(0)+1),setattr(ÄÊPKE(3),ÄÊPKE(2),ÄÊPKE(0)),ÄÊDEL(4))[4]]);(note:=lambda áÑÞ:ÂåÔ(áÑÞ.áÖà.append(áÑÞ.áÖõ),áÑÞ));(eton:=lambda áÑÞ:ÂåÔ(ÐÌü(áÑÞ.áÖà.pop),áÑÞ));(wind:=lambda áÑÞ:ÂåÔ((ÄÊPSH(áÑÞ),ÄÊPSH('áÖõ'),ÄÊPSH(ÐÌü(áÑÞ.áÖà.pop)),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3],áÑÞ))
(ARROW_TARG:=ÂÚü())
def ÄÝöç(áØÆ,áØÁ=ÂÞÅ):
	(áÖí:=ARROW_TARG[-1])
	if áØÁ is ÂÞÅ:áÖí.append(áØÆ);return áØÆ
	if áØÁ==ÂÕË:áÖí.extend(áØÆ);return áØÆ
	áÖí.extend((h:=MOD(Âêà,áØÁ=áØÁ)(áØÆ)));return h
def ÄÝöè(áØÁ=ÂÞÅ):
	(áÖí:=ARROW_TARG[-1])
	if áØÁ is ÂÞÅ:return áÖí.pop(-1)
	if áØÁ==ÂÕË:(r:=áÖí[slice(None,None)]);del áÖí[slice(None,None)];return r
	if(ÄÊPSH(áØÁ),ÄÊPSH(ÄÊPKE(0)*-1),(áØÁ:=ÄÊPKE(0)),ÄÊDEL(2))[2]==0:return ÂÚü()
	(r:=áÖí[slice(áØÁ,None)]);del áÖí[slice(áØÁ,None)];return r
def ÂÛÒ(áØÁ=ÂÞÅ):
	(áÖí:=ARROW_TARG[-1])
	if áØÁ is ÂÞÅ:return áÖí[-1]
	if áØÁ==ÂÕË:return áÖí[slice(None,None)]
	if(ÄÊPSH(áØÁ),ÄÊPSH(ÄÊPKE(0)*-1),(áØÁ:=ÄÊPKE(0)),ÄÊDEL(2))[2]==0:return ÂÚü()
	return áÖí[slice(áØÁ,None)]
(UGX_CREATE:=lambda x,d=False:MOD(lambda ÂîÓ:d if(y:=UGX_RUN(winder([*ÂîÓ]),x))is ÂÞÅ else y[0]))
def UGX_SCAN(áÖÿ,Æå,áÓà):
	if not áÖÿ:return ÂÚü()if'*'==áÓà or áÓà=='?'else ÂÞÅ
	(áÍí:=Æå((p:=ÐÌü(áÖÿ.peek))))
	if áÓà=='¬':return ÂÞÅ if áÍí else ÂÚü()
	if áÓà=='⮞':return ÂÚü()if áÍí else ÂÞÅ
	if not áÍí:return ÂÞÅ if áÓà in'+'else ÂÚü()
	(V:=ÂÚü()if ÐÌü(áÖÿ.next)is ÄÔýò or ÄÔýò is áÍí else Âêà(p))
	if áÓà in'?':return V
	while áÖÿ:
		if not(v:=Æå((p:=ÐÌü(áÖÿ.peek)))):break
		if v is ÄÔýò or ÄÔýò is ÐÌü(áÖÿ.next):continue
		V.append(p)
	return V
def UGX_RUN(áÖÿ,áØÃ):
	(ÄÊPSH(áØÃ),((áÓç:=ÄÊPKE(0)[0]),*(áÒø:=ÄÊPKE(0)[slice(1,None,None)])),ÄÊDEL(1))[1]
	if ÁØö(áÓç,áÓó):return UGX_SCAN(áÖÿ,áÓç,áÒø[0])
	elif áÓç in'BP':
		(ÄÊPSH(áÒø),((áÓæ:=ÄÊPKE(0)[0]),(áÓà:=ÄÊPKE(0)[1]),(áÓå:=ÄÊPKE(0)[2]),(áÓÕ:=ÄÊPKE(0)[3])),ÄÊDEL(1))[1];ARROW_TARG.append(áÓæ);ÂåÔ(ÐÌü(áÖÿ.note),(V:=(r:=UGX_RUN(áÖÿ,áÓÕ))))
		if áÓà=='⮞':ÂåÔ(ÐÌü(áÖÿ.wind),(V:=ÂÞÅ if r is ÂÞÅ else ÂÚü()))
		elif áÓà=='¬':ÂåÔ(ÐÌü(áÖÿ.wind),(V:=ÂÚü()if r is ÂÞÅ else ÂÞÅ))
		elif áÓà=='?':ÂåÔ(ÐÌü(áÖÿ.wind),(V:=ÂÚü()if r is ÂÞÅ else ÂÞÅ))
		elif r is ÂÞÅ:ÂåÔ(ÐÌü(áÖÿ.wind),(V:=ÂÚü()if áÓà=='∗'else ÂÞÅ))
		elif áÓà not in'?':
			while áÖÿ:
				ÂåÔ(ÐÌü(áÖÿ.note),(r:=UGX_RUN(áÖÿ,áÓÕ)))
				if r is ÂÞÅ:ÐÌü(áÖÿ.wind);break
				ÂåÔ(ÐÌü(áÖÿ.eton),V.extend(r))
			ÐÌü(áÖÿ.eton)
		if áÓå is ÄÔýò:(V:=ÂÚü())
		if V is not ÂÞÅ and áÓó(áÓå):(V:=áÓå(V))
		ARROW_TARG.pop(-1)
		if V is ÂÞÅ:return V
		return MOD(Áëý,áØÁ=áÓç=='B')(V,Âêà)
	elif áÓç in'∧∨':
		if áÓç=='∧':
			ÂåÔ(ÐÌü(áÖÿ.note),(V:=ÂÚü()))
			for U in áÒø:
				if(r:=UGX_RUN(áÖÿ,U))is ÂÞÅ:return ÂåÔ(ÐÌü(áÖÿ.wind),ÂÞÅ)
				V.extend(r)
			return ÂåÔ(ÐÌü(áÖÿ.eton),V)
		elif áÓç=='∨':
			for U in áÒø:
				ÐÌü(áÖÿ.note)
				if(r:=UGX_RUN(áÖÿ,U))is not ÂÞÅ:return ÂåÔ(ÐÌü(áÖÿ.eton),r)
				ÐÌü(áÖÿ.wind)
			return ÂÞÅ
__dir__=(__file__:=áÌî(moon_dir/'Builtins/subproca.☾')).parent
def ÄÊSUBPROCA(cmd,áÏÃ=ÁØã):
	from subprocess import Popen as áÐä,DEVNULL as NULL,PIPE,STDOUT;ÄÊPOP(0)if ÄÊPSH(not('M'in áÏÃ and ÂÕÖ(áÏÃ,'OEoe')))else ÂùÆ(ÄÊPOP(0),'Cannot use stdout/err and MERGE at once');ÄÊPOP(0)if ÄÊPSH(not((('o'in ÄÊPSH(áÏÃ)and ÂÔö(ÄÊPOP(0),ÄÊPSH('O')))and(ÄÊDEL(1)or True)or(ÄÊDEL(1)or False))or(('e'in ÄÊPSH(áÏÃ)and ÂÔö(ÄÊPOP(0),ÄÊPSH('E')))and(ÄÊDEL(1)or True)or(ÄÊDEL(1)or False))))else ÂùÆ(ÄÊPOP(0),'Cannot suppress and ignore stdout/err');(K:=ÐÌü(ÂÑÖ()));(ÄÊPSH(ÁØò(lambda ÂîÓ:ÂîÓ in áÏÃ)((vs:='toeBPSD'))),((áÐÍ:=ÄÊPKE(0)[0]),(áÐÈ:=ÄÊPKE(0)[1]),(áÏý:=ÄÊPKE(0)[2]),(áÏß:=ÄÊPKE(0)[3]),(áÏí:=ÄÊPKE(0)[4]),(áÏð:=ÄÊPKE(0)[5]),(áÏá:=ÄÊPKE(0)[6])),ÄÊDEL(1))[1];(ÄÊPSH(áÏÃ),ÄÊPSH(ÂÕÃ(ÄÊPKE(0),vs)or{'R'}),(áÏÃ:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	if áÏð:(ÄÊPSH(K),ÄÊPSH('shell'),ÄÊPSH(True),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
	if'M'in áÏÃ:(ÄÊPSH(K),ÄÊPSH('stdout'),ÄÊPSH(K),ÄÊPSH('stderr'),ÄÊPSH((PIPE,STDOUT)),(setattr(ÄÊPKE(4),ÄÊPKE(3),ÄÊPKE(0)[0]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)[1])),ÄÊDEL(5))[5]
	else:
		if not áÐÈ:(ÄÊPSH(K),ÄÊPSH('stdout'),ÄÊPSH(PIPE if'O'in áÏÃ else NULL),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		if not áÏý:(ÄÊPSH(K),ÄÊPSH('stderr'),ÄÊPSH(PIPE if'E'in áÏÃ else NULL),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
	(ÄÊPSH(K),ÄÊPSH('bufsize'),ÄÊPSH(ÂÞÅCAT(2**6,2**10)),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
	def p_stream(x):
		(t:=ÐÌü(getattr(p,x).read))
		if áÏß:return t
		(t:=t.decode('UTF8'));return t if áÐÍ else t.removesuffix('\n')
	def extract(p):
		(r:=ÐÌü(ÂÑØ()))
		if ÂÔö(áÏÃ,(v:='R')):(ÄÊPSH(r),ÄÊPSH(v),ÄÊPSH(p.returncode),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		if ÂÔö(áÏÃ,(v:='M')):(ÄÊPSH(r),ÄÊPSH(v),ÄÊPSH(p_stream('stdout')),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		else:
			if ÂÔö(áÏÃ,(v:='O')):(ÄÊPSH(r),ÄÊPSH(v),ÄÊPSH(p_stream('stdout')),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
			if ÂÔö(áÏÃ,(v:='E')):(ÄÊPSH(r),ÄÊPSH(v),ÄÊPSH(p_stream('stderr')),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		return r[ÐÌü(áÏÃ.pop)]if ãÊú(áÏÃ)==1 else r
	class Popen_Proxy:(__slots__:=('p',));(__init__:=lambda áÑÞ,p:ÂåÔ((ÄÊPSH(áÑÞ),ÄÊPSH('p'),ÄÊPSH(p),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3],None));(__call__:=lambda áÑÞ:ÂåÔ(ÐÌü(áÑÞ.p.wait),extract(p)));(__getitem__:=lambda áÑÞ,*áÑË:ÐÌü(áÑÞ).__getitem__(*áÑË));(__getattr__:=lambda áÑÞ,*áÑË:ÐÌü(áÑÞ).__getattr__(*áÑË));(__iter__:=lambda áÑÞ,*áÑË:ÐÌü(áÑÞ).__iter__(*áÑË))
	if áÏá:Âçß('Running: "%s"'%(termclr(cmd,'3d3'),))
	(p:=áÐä(ÂÛê(cmd),**K));return MOD(Áëý,áØÁ=not áÏí)(ÂÞÅCAT(p,Popen_Proxy),ÐÌü)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/extra_globals.☾')).parent
(FRAC_CONV:={**dict(ÄÕåØ(ÂÛê('12\u200913\u200914\u200915\u200916\u200917\u200918\u200919\u2009110\u200923\u200925\u200927\u200929\u200934\u200935\u200937\u200938\u2009310\u200945\u200947\u200949\u200956\u200957\u200958\u200959\u200967\u200978\u200979\u2009710\u200989\u2009910\u200903\u20091100'),'½⅓¼⅕⅙⅐⅛⅑⅒⅔⅖\U000f7db2\U000f7db7¾⅗\U000f7db3⅜\U000f7dc6⅘\U000f7db4\U000f7dc2⅚\U000f7db5⅝\U000f7db9\U000f7db6⅞\U000f7dba\U000f7dc7\U000f7dbb\U000f7dc8↉\U000f7dc9'))})
(TOFRAC:=lambda x:FRAC_CONV.get(x,x))
class UPSIDEDOWNSYNDROME:(NRM:='0123456789abcdefoxABCDEFOXîĵ\U000f7e88ℇτπ\U000f7e8d\U000f7e8f∞');(USD:='\U000f7c3d\U000f7c3e\U000f7c3f\U000f7c40\U000f7c41\U000f7c42\U000f7c43\U000f7c44\U000f7c45\U000f7c46\U000f7c47\U000f7c48\U000f7c49\U000f7c4a\U000f7c4b\U000f7c4c\U000f7c4d\U000f7c4e\U000f7c4f\U000f7c50\U000f7c51\U000f7c52\U000f7c53\U000f7c54\U000f7c55\U000f7c56\U000f7c6a\U000f7c7d\U000f7c7e\U000f7c6b\U000f7c6c\U000f7c6d\U000f7c6e\U000f7c70\U000f7c69');(MAP:={**dict(ÄÕåØ(NRM,USD))}|{**dict(ÄÕåØ(USD,NRM))});(flip:=lambda x,m=MAP:Âøî(ÁØò(lambda ÂîÓ:m.get(ÂîÓ,ÂîÓ))(x),ÁØã))
class SCRIPT:(SCRIPT_FILE_LOC:=ð(moon_dir,'Builtins/Data/script.map'));(ÄÊPSH(ÄÝöÞ(ÐØó(SCRIPT_FILE_LOC).strip('\n'),'\n')),((CHAR_NRM:=ÄÊPKE(0)[0]),(CHAR_SUP:=ÄÊPKE(0)[1]),(CHAR_SUB:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1];(SUP:=ÁÜÙ.maketrans(CHAR_NRM,CHAR_SUP));(SUB:=ÁÜÙ.maketrans(CHAR_NRM,CHAR_SUB));(NRM:=ÁÜÙ.maketrans(CHAR_SUP+CHAR_SUB,ÂÞÅCAT(2,CHAR_NRM)));(ÄÊPSH(Áÿú([SUP,SUB,NRM],lambda áÖæ:lambda x:x.translate(áÖæ))),((sup:=ÄÊPKE(0)[0]),(sub:=ÄÊPKE(0)[1]),(nrm:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
(ÄÊPSH((SCRIPT.sup,SCRIPT.sub,SCRIPT.nrm)),((supscript:=ÄÊPKE(0)[0]),(subscript:=ÄÊPKE(0)[1]),(nrmscript:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
(ÄÊPSH((SCRIPT.CHAR_SUP,SCRIPT.CHAR_SUB)),((SUPSCRIPT:=ÄÊPKE(0)[0]),(SUBSCRIPT:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(ALPHABETS:=Áÿú(ÄÝöÞ(Âüá('\n    abcdefghijklmnopqrstuvwxyz\u2009ABCDEFGHIJKLMNOPQRSTUVWXYZ\u20090123456789\n    𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫\u2009𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ\u2009𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡\n    𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳\u2009𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙\u2009𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗\n    𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧\u2009𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍\u2009◌◌◌◌◌◌◌◌◌◌\n    𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇\u2009𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭\u2009𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵\n    𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣\u2009𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉\u2009𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿\n    ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ\u2009ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ\u2009◌\U000f0ca1\U000f0ca3\U000f0ca5\U000f0ca7\U000f0ca9\U000f0cab\U000f0cad\U000f0caf\U000f0cb1\n    ⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵\u2009🄐🄑🄒🄓🄔🄕🄖🄗🄘🄙🄚🄛🄜🄝🄞🄟🄠🄡🄢🄣🄤🄥🄦🄧🄨🄩\u2009◌⑴⑵⑶⑷⑸⑹⑺⑻⑼\n    \U000f0aee\U000f0aef\U000f0af0\U000f0af1\U000f0af2\U000f0af3\U000f0af4\U000f0af5\U000f0af6\U000f0af7\U000f0af8\U000f0af9\U000f0afa\U000f0afb\U000f0afc\U000f0afd\U000f0afe\U000f0aff\U000f0b00\U000f0b01\U000f0b02\U000f0b03\U000f0b04\U000f0b05\U000f0b06\U000f0b07\u2009\U000f0aee\U000f0aef\U000f0af0\U000f0af1\U000f0af2\U000f0af3\U000f0af4\U000f0af5\U000f0af6\U000f0af7\U000f0af8\U000f0af9\U000f0afa\U000f0afb\U000f0afc\U000f0afd\U000f0afe\U000f0aff\U000f0b00\U000f0b01\U000f0b02\U000f0b03\U000f0b04\U000f0b05\U000f0b06\U000f0b07\u2009\U000f0b39\U000f0b3a\U000f0b3b\U000f0b3c\U000f0b3d\U000f0b3e\U000f0b3f\U000f0b40\U000f0b41\U000f0b42\n    𜳖𜳗𜳘𜳙𜳚𜳛𜳜𜳝𜳞𜳟𜳠𜳡𜳢𜳣𜳤𜳥𜳦𜳧𜳨𜳩𜳪𜳫𜳬𜳭𜳮𜳯\u2009𜳖𜳗𜳘𜳙𜳚𜳛𜳜𜳝𜳞𜳟𜳠𜳡𜳢𜳣𜳤𜳥𜳦𜳧𜳨𜳩𜳪𜳫𜳬𜳭𜳮𜳯\u2009𜳰𜳱𜳲𜳳𜳴𜳵𜳶𜳷𜳸𜳹\n    𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓\u2009𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹\u2009𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫\n    ɒც𝼝𝼥⋿ꬵꬶҕї𝼚𝼐ꬷӍꬼϙƿ𝼛Ʀ𝼞ŧꭒѵꭐꭘꭚƶ\u2009ѦƁƇƊᗴҒႺⴼΙɈⴿꝈⱮͶⴲƤꝖⴽႽƬŲѴϢҲⵖΖ\u2009◌◌◌◌◌◌◌◌◌◌\n    𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻\u2009𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡\u2009◌◌◌◌◌◌◌◌◌◌\n    𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏\u2009𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵\u2009◌◌◌◌◌◌◌◌◌◌\n    𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃\u2009𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩\u2009◌◌◌◌◌◌◌◌◌◌\n    𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛\u2009𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁\u2009◌◌◌◌◌◌◌◌◌◌\n    𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷\u2009𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ\u2009◌◌◌◌◌◌◌◌◌◌\n    𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟\u2009𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅\u2009◌◌◌◌◌◌◌◌◌◌\n    𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯\u2009𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕\u2009◌◌◌◌◌◌◌◌◌◌\n'),'\n'),Âåæ(ÂÛê,Âüá)))
(LOWERCASE:=Âøî(Áÿú(ALPHABETS,MOD(ÁÛÛ,áØÁ=0))))
(UPPERCASE:=Âøî(Áÿú(ALPHABETS,MOD(ÁÛÛ,áØÁ=1))))
(LETTERS:=LOWERCASE+UPPERCASE)
(TERLETS:=UPPERCASE+LOWERCASE)
(ÄÊPSH(ALPHABETS[0][slice(None,3)]),((abc:=ÄÊPKE(0)[0]),(ABC:=ÄÊPKE(0)[1]),(num:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
(ÄÊPSH((abc+ABC,abc+num,ABC+num,abc+ABC+num)),((abcABC:=ÄÊPKE(0)[0]),(abc123:=ÄÊPKE(0)[1]),(ABC123:=ÄÊPKE(0)[2]),(abcABC123:=ÄÊPKE(0)[3])),ÄÊDEL(1))[1]
(TO_LOWERCASE:=CUR(lambda ÂîÓ,ÂîÒ:under_script(ÂîÒ,ÂîÓ),(lambda ÂîÓ:lambda x:x.translate(ÂîÓ))(ÁÜÙ.maketrans(UPPERCASE,LOWERCASE))))
(TO_UPPERCASE:=CUR(lambda ÂîÓ,ÂîÒ:under_script(ÂîÒ,ÂîÓ),(lambda ÂîÓ:lambda x:x.translate(ÂîÓ))(ÁÜÙ.maketrans(LOWERCASE,UPPERCASE))))
(REVERSE_CASE:=CUR(lambda ÂîÓ,ÂîÒ:under_script(ÂîÒ,ÂîÓ),(lambda ÂîÓ:lambda x:x.translate(ÂîÓ))(ÁÜÙ.maketrans(LETTERS,TERLETS))))
(GET_CASE:=lambda x:(TO_UPPERCASE(x)==x)-(x==TO_LOWERCASE(x)))
def under_script(áØÆ,Æå,áÕÉ=ÂÞÅ):(áÓÕ:=MOD(lambda ÂîÓ:supscript if ÂîÓ in SUPSCRIPT else subscript if ÂîÓ in SUBSCRIPT else None));return Âøî(ËãÂ(ÄÕåØ(ÁØò(lambda ÂîÓ:MOD(ÆÑ,áØÁ=ÄÕÍÔ)(Áÿú(ÂÕÅ(ÂÛÜ(nrmscript,Âåæ(Âó,áÓÕ)),ÂîÓ),áÓÕ),Âåæ))(áØÆ if áÕÉ is ÂÞÅ else áÕÉ),Æå(ÂÕÅ(ÂØÏ(nrmscript),áØÆ))),ÂÕÅ))
__dir__=(__file__:=áÌî(moon_dir/'Builtins/ℍ.☾')).parent
class ÂÐì:
	(__slots__:=('r','i','j','k'))
	def __init__(áÑÞ,r=0,i=0,j=0,k=0):(ÄÊPSH(áÑÞ),ÄÊPSH('r'),ÄÊPSH(áÑÞ),ÄÊPSH('i'),ÄÊPSH(áÑÞ),ÄÊPSH('j'),ÄÊPSH(áÑÞ),ÄÊPSH('k'),ÄÊPSH(r if MOD(ÁØö,áØÁ=ÂÕó)(r,ÂÐì)else(ÄÝõè(r),i or ÄÝõç(r),j,k)),(setattr(ÄÊPKE(8),ÄÊPKE(7),ÄÊPKE(0)[0]),setattr(ÄÊPKE(6),ÄÊPKE(5),ÄÊPKE(0)[1]),setattr(ÄÊPKE(4),ÄÊPKE(3),ÄÊPKE(0)[2]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)[3])),ÄÊDEL(9))[9]
	(__abs__:=lambda áÑÞ:ÂÕÇ(áÑÞ.r**2+áÑÞ.i**2+áÑÞ.j**2+áÑÞ.k**2));(__truediv__:=lambda áÑÞ,x:ÂåÔ((x:=ÂÐì(x)),áÑÞ*ÂÐì(x.r/(a:=ÂüÌ(x)),-(x.i/a),-(x.j/a),-(x.k/a))));(__rtruediv__:=lambda áÑÞ,x:ÂåÔ((x:=ÂÐì(x)),x*ÂÐì(áÑÞ.r/(a:=ÂüÌ(áÑÞ)),-(áÑÞ.i/a),-(áÑÞ.j/a),-(áÑÞ.k/a))));(__mod__:=lambda áÑÞ,x:ÂÐì(áÑÞ.r%x,áÑÞ.i%x,áÑÞ.j%x,áÑÞ.k%x));(__floordiv__:=lambda áÑÞ,x:ÂÐì(áÑÞ.r//x,áÑÞ.i//x,áÑÞ.j//x,áÑÞ.k//x));(__neg__:=lambda áÑÞ:0-áÑÞ);(__pos__:=lambda áÑÞ:0+áÑÞ);(__bool__:=lambda áÑÞ:((áÑÞ.r or áÑÞ.i)or áÑÞ.j)or áÑÞ.k);(__hash__:=lambda áÑÞ:hash(áÍé(áÑÞ)));(__inverse__:=lambda áÑÞ:áÑÞ**-1);(__bool__:=lambda áÑÞ:áÍÖ(((áÑÞ.r or áÑÞ.i)or áÑÞ.j)or áÑÞ.k));(__repr__:=lambda áÑÞ:Âøî(ÁØòþÁÙÇ(lambda ÂîÓ,ÂîÒ:'-+'[ÂîÓ>=0]+ÁÜÙ(MOD(Âäû,áØÁ=5)(ÂüÌ(ÂîÓ)))+ÂîÒ)(áÑÞ,ÄÔÙù([ÁØã],'îĵ\U000f7e88'))));(__iter__:=lambda áÑÞ:iter((áÑÞ.r,áÑÞ.i,áÑÞ.j,áÑÞ.k)));(__len__:=lambda áÑÞ:4);(conj:=lambda áÑÞ:ÂÐì(áÑÞ.r,-áÑÞ.i,-áÑÞ.j,-áÑÞ.k));(copy:=lambda áÑÞ:ÂÐì(*áÑÞ));(vec:=lambda áÑÞ:[áÑÞ.i,áÑÞ.j,áÑÞ.k]);(norm:=lambda áÑÞ:áÑÞ/(ÂüÌ(áÑÞ)or 1));(rotmat:=lambda áÑÞ:[[1-2*(áÑÞ.j*áÑÞ.j+áÑÞ.k*áÑÞ.k),2*(áÑÞ.i*áÑÞ.j-áÑÞ.k*áÑÞ.r),2*(áÑÞ.i*áÑÞ.k+áÑÞ.j*áÑÞ.r)],[2*(áÑÞ.i*áÑÞ.j+áÑÞ.k*áÑÞ.r),1-2*(áÑÞ.i*áÑÞ.i+áÑÞ.k*áÑÞ.k),2*(áÑÞ.j*áÑÞ.k-áÑÞ.i*áÑÞ.r)],[2*(áÑÞ.i*áÑÞ.k-áÑÞ.j*áÑÞ.r),2*(áÑÞ.j*áÑÞ.k+áÑÞ.i*áÑÞ.r),1-2*(áÑÞ.i*áÑÞ.i+áÑÞ.j*áÑÞ.j)]])
	def __eq__(áÑÞ,x):
		if ÁØö(x,ÂÐá):return((áÑÞ.j==0 and áÑÞ.k==0)and áÑÞ.r==ÄÝõè(x))and áÑÞ.i==ÄÝõç(x)
		if MOD(ÁØö,áØÁ=ÂÕó)(x,ÂÐì):return((áÑÞ.r==x.r and áÑÞ.i==x.i)and áÑÞ.j==x.j)and áÑÞ.k==x.k
	def __lt__(áÑÞ,x):
		if ÁØö(x,ÂÐá):return áÑÞ.r**2+áÑÞ.i**2+áÑÞ.j**2+áÑÞ.k**2<ÄÝõè(x)**2+ÄÝõç(x)**2
		if MOD(ÁØö,áØÁ=ÂÕó)(x,ÂÐì):return áÑÞ.r**2+áÑÞ.i**2+áÑÞ.j**2+áÑÞ.k**2<x.r**2+x.i**2+x.j**2+x.k**2
	def __le__(áÑÞ,x):
		if ÁØö(x,ÂÐá):return áÑÞ.r**2+áÑÞ.i**2+áÑÞ.j**2+áÑÞ.k**2<=ÄÝõè(x)**2+ÄÝõç(x)**2
		if MOD(ÁØö,áØÁ=ÂÕó)(x,ÂÐì):return áÑÞ.r**2+áÑÞ.i**2+áÑÞ.j**2+áÑÞ.k**2<=x.r**2+x.i**2+x.j**2+x.k**2
	def __gt__(áÑÞ,x):
		if ÁØö(x,ÂÐá):return áÑÞ.r**2+áÑÞ.i**2+áÑÞ.j**2+áÑÞ.k**2>ÄÝõè(x)**2+ÄÝõç(x)**2
		if MOD(ÁØö,áØÁ=ÂÕó)(x,ÂÐì):return áÑÞ.r**2+áÑÞ.i**2+áÑÞ.j**2+áÑÞ.k**2>x.r**2+x.i**2+x.j**2+x.k**2
	def __ge__(áÑÞ,x):
		if ÁØö(x,ÂÐá):return áÑÞ.r**2+áÑÞ.i**2+áÑÞ.j**2+áÑÞ.k**2>=ÄÝõè(x)**2+ÄÝõç(x)**2
		if MOD(ÁØö,áØÁ=ÂÕó)(x,ÂÐì):return áÑÞ.r**2+áÑÞ.i**2+áÑÞ.j**2+áÑÞ.k**2>=x.r**2+x.i**2+x.j**2+x.k**2
	def __add__(áÑÞ,x):
		if ÁØö(x,ÂÐá):return ÂÐì(áÑÞ.r+ÄÝõè(x),áÑÞ.i+ÄÝõç(x),áÑÞ.j,áÑÞ.k)
		if MOD(ÁØö,áØÁ=ÂÕó)(x,ÂÐì):return ÂÐì(áÑÞ.r+x.r,áÑÞ.i+x.i,áÑÞ.j+x.j,áÑÞ.k+x.k)
	def __radd__(áÑÞ,x):
		if ÁØö(x,ÂÐá):return ÂÐì(áÑÞ.r+ÄÝõè(x),áÑÞ.i+ÄÝõç(x),áÑÞ.j,áÑÞ.k)
		if MOD(ÁØö,áØÁ=ÂÕó)(x,ÂÐì):return ÂÐì(áÑÞ.r+x.r,áÑÞ.i+x.i,áÑÞ.j+x.j,áÑÞ.k+x.k)
	def __sub__(áÑÞ,x):
		if ÁØö(x,ÂÐá):return ÂÐì(áÑÞ.r-ÄÝõè(x),áÑÞ.i-ÄÝõç(x),áÑÞ.j,áÑÞ.k)
		if MOD(ÁØö,áØÁ=ÂÕó)(x,ÂÐì):return ÂÐì(áÑÞ.r-x.r,áÑÞ.i-x.i,áÑÞ.j-x.j,áÑÞ.k-x.k)
	def __rsub__(áÑÞ,x):
		if ÁØö(x,ÂÐá):return ÂÐì(ÄÝõè(x)-áÑÞ.r,ÄÝõç(x)-áÑÞ.i,-áÑÞ.j,-áÑÞ.k)
		if MOD(ÁØö,áØÁ=ÂÕó)(x,ÂÐì):return ÂÐì(x.r-áÑÞ.r,x.i-áÑÞ.i,x.j-áÑÞ.j,x.k-áÑÞ.k)
	def __mul__(áÑÞ,x):
		if ÁØö(x,ÂÐá):return áÑÞ*ÂÐì(x)
		if MOD(ÁØö,áØÁ=ÂÕó)(x,ÂÐì):return ÂÐì(áÑÞ.r*x.r-áÑÞ.i*x.i-áÑÞ.j*x.j-áÑÞ.k*x.k,áÑÞ.r*x.i+áÑÞ.i*x.r+áÑÞ.j*x.k-áÑÞ.k*x.j,áÑÞ.r*x.j-áÑÞ.i*x.k+áÑÞ.j*x.r+áÑÞ.k*x.i,áÑÞ.r*x.k+áÑÞ.i*x.j-áÑÞ.j*x.i+áÑÞ.k*x.r)
	def __rmul__(áÑÞ,x):
		if ÁØö(x,ÂÐá):return ÂÐì(x)*áÑÞ
		if MOD(ÁØö,áØÁ=ÂÕó)(x,ÂÐì):return ÂÐì(áÑÞ.r*x.r-áÑÞ.i*x.i-áÑÞ.j*x.j-áÑÞ.k*x.k,áÑÞ.r*x.i+áÑÞ.i*x.r+áÑÞ.j*x.k-áÑÞ.k*x.j,áÑÞ.r*x.j-áÑÞ.i*x.k+áÑÞ.j*x.r+áÑÞ.k*x.i,áÑÞ.r*x.k+áÑÞ.i*x.j-áÑÞ.j*x.i+áÑÞ.k*x.r)
	def __pow__(áÑÞ,x):
		if ÁØö(x,ÂÑÅ):return áÑÞ*áÑÞ**(x-1)if x>0 else 1/áÑÞ**-x if x<0 else 1
		return(x*áÑÞ.log()).exp()
	def log(áÑÞ):
		if(v:=ÂÕÇ(áÑÞ.i**2+áÑÞ.j**2+áÑÞ.k**2)):return ÂÐì(log(ÂüÌ(áÑÞ)),áÑÞ.i*acos(ÂÞÅCAT(ÂüÌ(ÄÊCUR((2,),{},ÄÃ,áÑÞ.r,ÂýÃ)),áÑÞ))/v,áÑÞ.j*acos(ÂÞÅCAT(ÂüÌ(ÄÊCUR((2,),{},ÄÃ,áÑÞ.r,ÂýÃ)),áÑÞ))/v,áÑÞ.k*acos(ÂÞÅCAT(ÂüÌ(ÄÊCUR((2,),{},ÄÃ,áÑÞ.r,ÂýÃ)),áÑÞ))/v)
		return log(áÑÞ.r)
	def exp(áÑÞ):
		if(v:=ÂÕÇ(áÑÞ.i**2+áÑÞ.j**2+áÑÞ.k**2)):return ÄóÌÊ(áÑÞ.r)*ÂÐì(ÄóÌÁ(v),áÑÞ.i*(w:=ÄóÌÀ(v)/v),áÑÞ.j*2,áÑÞ.k*w)
		return ÄóÌÊ(áÑÞ.r)
	def __getitem__(áÑÞ,x):
		if x==0:return áÑÞ.r
		if x==1 or x==Ãù:return áÑÞ.i
		if x==2 or x==ÅÄ:return áÑÞ.j
		if x==3 or x==ÄÝøÛ:return áÑÞ.k
	def __setitem__(áÑÞ,x,v):
		if x==0:return(ÄÊPSH(áÑÞ),ÄÊPSH('r'),ÄÊPSH(v),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		if x==1 or x==Ãù:return(ÄÊPSH(áÑÞ),ÄÊPSH('i'),ÄÊPSH(v),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		if x==2 or x==ÅÄ:return(ÄÊPSH(áÑÞ),ÄÊPSH('j'),ÄÊPSH(v),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		if x==3 or x==ÄÝøÛ:return(ÄÊPSH(áÑÞ),ÄÊPSH('k'),ÄÊPSH(v),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
(ÄÝõè:=lambda x:x.r if MOD(ÁØö,áØÁ=ÂÕó)(x,ÂÐì)else x.real if MOD(ÁØö,áØÁ=ÂÕó)(x,ÂÐá)else x)
(ÄÝõç:=lambda x:x.i if MOD(ÁØö,áØÁ=ÂÕó)(x,ÂÐì)else x.imag if MOD(ÁØö,áØÁ=ÂÕó)(x,ÂÐá)else 0)
(ÄÝõé:=lambda x:ÂÐá(*x)if ÁØö(x,áÍá|áÍé)else(ÄÝõè(x),ÄÝõç(x)))
(ÄÝõæ:=lambda x:x.j if MOD(ÁØö,áØÁ=ÂÕó)(x,ÂÐì)else 0)
(ÄÝõå:=lambda x:x.k if MOD(ÁØö,áØÁ=ÂÕó)(x,ÂÐì)else 0)
(ÄÝõä:=lambda x:(ÄÝõè(x),ÄÝõæ(x)))
(ÄÝõã:=lambda x:(ÄÝõè(x),ÄÝõå(x)))
(ÄÝöÌ:=lambda x:(ÄÝõç(x),ÄÝõæ(x),ÄÝõå(x)))
(ÄÝõâ:=lambda x:ÂÐì(*x)if ÁØö(x,áÍá|áÍé)else(ÄÝõè(x),ÄÝõç(x),ÄÝõæ(x),ÄÝõå(x)))
(ÄÊPSH((ÂÐì(0,0,1,0),ÂÐì(0,0,0,1),ÂÐì(0,0,-1,0),ÂÐì(0,0,0,-1))),((ÅÄ:=ÄÊPKE(0)[0]),(ÄÝøÛ:=ÄÊPKE(0)[1]),(ÄÝîõ:=ÄÊPKE(0)[2]),(ÄÝîö:=ÄÊPKE(0)[3])),ÄÊDEL(1))[1]
__dir__=(__file__:=áÌî(moon_dir/'Builtins/!.☾')).parent
def ÏÀ(z):
	if ÄÝõè(z)<ÃÆ:return ÂÞÅCAT(Ïò,Ãù)/((ÂÐæ**ÂÞÅCAT(ÂÞÅCAT(Ãù,Ïî),z)-ÂÐæ**ÂÞÅCAT(ÂÞÅCAT(ÄÝîâ,Ïî),z))*ÏÀ(1-z))
	(p:=[1.000000000190015,76.18009172947146,-86.50532032941676,24.01409824083091,-1.2317395724501554,.0012086509738661786,-5.395239384953128e-06]);return MOD(ÂøÑ,áØÁ=p[0])(ÁÙÇ(lambda ÂîÒ:p[ÂîÒ]/(z+ÂîÒ))(ÄÝöÊ(1,6)))*ÂÐæ**(-5.5-z)*(5.5+z)**(ÃÆ+z)*ÂÕÇ(Ïò)/z
def â(áØÆ,áØÁ=ÂÞÅ):
	if áØÁ is ÂÞÅ:
		if ÁØö(áØÆ,ÂÑÅ):return nan if áØÆ<0 else MOD(ÂøÐ,áØÁ=1)(ÄÝöÉ(0,áÍÞ(áØÆ)))
		return áØÆ*ÏÀ(áØÆ)
	if ÁØö(áØÁ,áÍÞ):return MOD(ÂøÐ,áØÁ=1)(ÁØò(lambda ÂîÓ:ÂîÓ+áØÆ)(ÂÿÇ(áØÁ)))
	if ÁØö(áØÁ,ÂÐá):
		if áØÆ==0:return 1
		if(d:=ÂÞÅCAT(ÄÝõç(Âüð),áØÁ))>=0 and áØÆ>0:return ÂÕË
		if d<=0 and áØÆ<0:return nan
		(ÄÊPSH((1,áØÆ)),((t:=ÄÊPKE(0)[0]),(c:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
		while ÃÆí(c)==ÃÆí(áØÆ):(ÄÊPSH(t),ÄÊPSH(ÄÊPKE(0)*c),(t:=ÄÊPKE(0)),ÄÊDEL(2))[2];(ÄÊPSH(c),ÄÊPSH(ÄÊPKE(0)+d),(c:=ÄÊPKE(0)),ÄÊDEL(2))[2]
		return t
	if ÁØö(áØÁ,áÓö):return MOD(ÂøÐ,áØÁ=1)(ÁØò(lambda ÂîÓ:ÂîÓ*áØÁ[-1]+áØÆ)(ÂÿÇ(áØÁ[0])))
	ÄÊPOP(0)if ÄÊPSH(False)else ÂùÆ(ÄÊPOP(0),'what do you meeeeaaaaaannnnnn!?!?!?')
__dir__=(__file__:=áÌî(moon_dir/'Builtins/⫚.☾')).parent
@OPWRAP_(*'\U000f7e98\U000f7e99\U000f7e9a\U000f7e9b')
def _(áÑã,áØÆ,áØÁ=ÂÞÅ):
	ÄÊPOP(0)if ÄÊPSH(áØÁ is ÂÞÅ)else ÂùÆ(ÄÊPOP(0),'\U000f0931');ÄÊPOP(0)if ÄÊPSH(ÁØö(áÑã,áÍá|áÍé|ÁÜÙ))else ÂùÆ(ÄÊPOP(0),'\U000f0931')
	if not áØÆ:return ÂÚü()
	if áÑã=='\U000f7e98':return ÁØòþë(lambda ÂîÓ,ÄÝõÌ,ÄÝõË:ÁØòþë(lambda ÂîÓ,ÄÝõÌ,ÄÝõË:áØÆ[ÄÝõÌ]if ÂîÓ else ÄÔýò)(ÂîÓ))(MOD(ÂÿÇ,áØÁ=ãÊú(áØÆ))(2))
	if áÑã=='\U000f7e99':return ÁãÁ(MOD(ÄÝøî,áØÁ=áØÁ)(áØÆ),ÄÔàÑ)
	if áÑã=='\U000f7e9a':
		(R:=ÂÚü())
		for x in ÂÿÇ(â(ãÊú(áØÆ))):
			(ÄÊPSH((ÂÚü(),0)),((D:=ÄÊPKE(0)[0]),(i:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
			while x:(ÄÊPSH(divmod(x,(ÄÊPSH(i),ÄÊPSH(ÄÕÇè(ÄÊPKE(0))),(i:=ÄÊPKE(0)),ÄÊDEL(2))[2])),((x:=ÄÊPKE(0)[0]),(r:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1];D.append(r)
			(áÑÈ:=[*áØÆ]);R.append(Áÿú(MOD(ÄÕÊÂ,áØÁ=0)(ÂÀÇ(D),ãÊú(áØÆ)),áÑÈ.pop))
		return R
	if áÑã=='\U000f7e9b':return ÆÑ(ÁØòþë(lambda ÂîÓ,ÄÝõÌ,ÄÝõË:MOD(ÂøÚ,áØÁ=ÄÝõÌ)(áØÆ))(ÄÝöÊ(ãÊú(áØÆ))),ÂÕØ)
def Âûô(x,y):
	if ÁØö(x,áÍÞ)and ÁØö(y,áÍÞ):return MOD(â,áØÁ=-y)(x)//â(y)
	if ÄÝøÇ(x,áÓö)and ÁØö(y,áÍÞ):return MOD(â,áØÁ=-y)(x)/â(y)
	if ÁØö(x,ÂÐá)and ÁØö(y,ÂÐá):return â(x)/(â(y)*â(x-y))
	if ÁØö(x,áÓö)and ÁØö(y,ÂÐá):
		ÄÊPOP(0)if ÄÊPSH(ÁØö(y,áÍÞ)and y>=0)else ÂùÆ(ÄÊPOP(0),"can't choose %s things from a list"%(y,))
		if ãÊú(x)<y:return ÂÚü()
		if not y:return MOD(ÂÚü,áØÁ=-1)()
		return Âûô(x[slice(None,-1)],y)+ÁØò(lambda ÂîÓ:ÂîÓ+[x[-1]])(Âûô(x[slice(None,-1)],y-1))
	if ÁØö(x,ÂÐá)and ÁØö(y,áÓö):return â(x)//ÂøÐ(Áÿú(y+[x-ÂøÑ(y)],â))if ÁØö(x,áÍÞ)and ÂØô(ÁØò(lambda ÂîÓ:ÁØö(ÂîÓ,áÍÞ))(y))else ð(â(x),ÂøÐ(Áÿú(y+[x-ÂøÑ(y)],â)))
	if ÁØö(x,áÓö)and ÁØö(y,áÓö):
		ÄÊPOP(0)if ÄÊPSH(ÂØô(ÁØò(lambda ÂîÓ:ÁØö(ÂîÓ,áÍÞ)and ÂîÓ>=0)(y)))else ÂùÆ(ÄÊPOP(0),"can't choose groups %s from a list"%(y,))
		if ãÊú(x)<ÂøÑ(y):return ÂÚü()
		if ÄÝõÔ(y):return[MOD(ÂÚü,áØÁ=ãÊú(y))()]
		return Âûô(x[slice(None,-1)],y)+ÂøÑ(ÁØò(lambda ÂîÓ:ÁÙÇ(lambda ÂîÒ:ÁÙÇ(lambda ÂîÒ:ÂîÒ[1]+(ÂîÒ[0]==ÂîÓ)*[x[-1]])(ÂÓÏ(ÂîÒ)))(Âûô(x[slice(None,-1)],ÁÙÇ(lambda ÂîÒ:ÂîÒ[1]-(ÂîÒ[0]==ÂîÓ))(ÂÓÏ(y)))))(ÄÔÔç(ÂÿÇ(y),lambda x:y[x])))
__dir__=(__file__:=áÌî(moon_dir/'Builtins/¶.☾')).parent
def smolfactor(n,k=1):
	if k>n:return 0
	if k<1:return 1
	if k==1 and ÂÕÐ(2,n):return 2
	for p in ÄÝöÉ(k,n):
		if not ÂÕÐ(p,n):continue
		return p
	return n
def firstÂÐôbool(c,r=2):
	if c(1):return 1
	(ub:=1)
	while not c(ub):(ÄÊPSH(ub),ÄÊPSH(ÄÊPKE(0)*r),(ub:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	(lb:=ub//r)
	while ub-lb>1:
		(m:=(ub+lb)//2)
		if c(m):(ub:=m)
		else:(lb:=m)
	return ub
class Âÿ:
	@cache_
	def __contains__(áÑÞ,n):
		if n<=1:return False
		if ÂÕÐ(2,n):return n==2
		if n<10000:
			for k in MOD(ÄÝöÊ,áØÁ=2)(3,Âüï(ÂÕÇ(n))):
				if not ÂÕÐ(k,n):continue
				return False
			return True
		for k in MOD(ÄÝöÊ,áØÁ=2)(3,100):
			if not ÂÕÐ(k,n):continue
			return False
		if(a:=pow(2,(n-1)//2**(s:=MOD(Âÿ,áØÁ=2)(n-1)),n))!=1:
			for r in ÂÿÇ(s):
				if a==n-1:break
				(ÄÊPSH(a),ÄÊPSH(ÄÊPKE(0)**2%n),(a:=ÄÊPKE(0)),ÄÊDEL(2))[2]
			else:return False
		if firstÂÐôbool(MOD(lambda ÂîÓ:ÂîÓ**2>=n))**2==n:return False
		(D:=5)
		while Âëì(D,n)!=-1:(ÄÊPSH(D),ÄÊPSH(ÃÆí(ÄÊPKE(0))*-2-D),(D:=ÄÊPKE(0)),ÄÊDEL(2))[2]
		(s:=MOD(Âÿ,áØÁ=2)(n+1));(d:=(n+1)//2**s);(B:=bin(d)[slice(3,None)]);(ÄÊPSH((1,(1-D)//4)),((P:=ÄÊPKE(0)[0]),(Q:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1];(ÄÊPSH((1,P,Q)),((U:=ÄÊPKE(0)[0]),(V:=ÄÊPKE(0)[1]),(Qk:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
		for b in B:
			(ÄÊPSH((U*V%n,(V**2-ÂÞÅCAT(2,Qk))%n,pow(Qk,2,n))),((U:=ÄÊPKE(0)[0]),(V:=ÄÊPKE(0)[1]),(Qk:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
			if b=='1':(ÄÊPSH(((áÐÍ if ÂÕÐ(2,(áÐÍ:=P*U+V))else áÐÍ+n)//2%n,(áÐÍ if ÂÕÐ(2,(áÐÍ:=D*U+P*V))else áÐÍ+n)//2%n,Qk*Q%n)),((U:=ÄÊPKE(0)[0]),(V:=ÄÊPKE(0)[1]),(Qk:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
		if U:
			for r in ÂÿÇ(s):
				if not V:break
				(ÄÊPSH((U*V%n,(V**2-ÂÞÅCAT(2,Qk))%n,pow(Qk,2,n))),((U:=ÄÊPKE(0)[0]),(V:=ÄÊPKE(0)[1]),(Qk:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1]
			else:return False
		if n<2**64:return True
		ÄÊPOP(0)if ÄÊPSH(n<2**1500)else ÂùÆ(ÄÊPOP(0),'\U000f0931 implement APRCL for n<2¹⁵⁰⁰');ÄÊPOP(0)if ÄÊPSH(False)else ÂùÆ(ÄÊPOP(0),'\U000f0931 implement ECPP for n>2¹⁵⁰⁰')
	(__getitem__:=lambda áÑÞ,t,*áÑË,**áÑÕ:lambda*áÑË,**áÑÕ:áÑÞ.__call__(*áÑË,s=t))
	def __call__(áÑÞ,x,áØÁ=ÂÞÅ):
		if x is ÂÕË:return'\U000f0931 ∞ primes'
		if áØÁ is ÂÞÅ:
			if x<=1:return[2]*x
			(ÄÊPSH(([2],3)),((t:=ÄÊPKE(0)[0]),(p:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
			while ãÊú(t)<x:
				if p in Âÿ:t.append(p)
				(ÄÊPSH(p),ÄÊPSH(ÄÊPKE(0)+2),(p:=ÄÊPKE(0)),ÄÊDEL(2))[2]
			return t
		if ÁØö(áØÁ,ÂÑÅ):
			(t:=0)
			while ÂÕÐ(áØÁ,x):(ÄÊPSH(t),ÄÊPSH(ÄÊPKE(0)+1),(t:=ÄÊPKE(0)),ÄÊDEL(2))[2];(ÄÊPSH(x),ÄÊPSH(ÄÊPKE(0)//áØÁ),(x:=ÄÊPKE(0)),ÄÊDEL(2))[2]
			return t
		if áØÁ is ÿ:return ÄÔÔç(ÄÝöÈ(2,x),MOD(lambda ÂîÓ:ÂîÓ in Âÿ))
		if áØÁ is ì:
			if(r:=Âäû(ÂÕÇ(x)))**2==x:return(f:=ÄÔÔè(ÄÝöÈ(1,r),MOD(lambda ÂîÒ:x%ÂîÒ)))+[r]+ÁØò(lambda ÂîÓ:ÂÁÍ(ÃËÕ)(ÂîÓ,x))(ÂÀÇ(f))
			return(f:=ÄÔÔè(ÄÝöÊ(1,r),MOD(lambda ÂîÒ:x%ÂîÒ)))+ÁØò(lambda ÂîÓ:ÂÁÍ(ÃËÕ)(ÂîÓ,x))(ÂÀÇ(f))
		if áØÁ is ÂÕÐ:return[*ÐÌÛ(MOD(Âÿ,áØÁ=ë)(x),ÄÕÍÔ)]
		if áØÁ is ë:
			(ÄÊPSH(x),ÄÊPSH(ÂüÌ(ÄÊPKE(0))),(x:=ÄÊPKE(0)),ÄÊDEL(2))[2]
			if x==1:return ÂÚü()
			(t:=ÂÚü())
			while ÂÕÐ(2,x):(ÄÊPSH(t),ÄÊPSH(ÄÊPKE(0)+[2]),(t:=ÄÊPKE(0)),ÄÊDEL(2))[2];(ÄÊPSH(x),ÄÊPSH(ÄÊPKE(0)//2),(x:=ÄÊPKE(0)),ÄÊDEL(2))[2]
			for k in MOD(ÄÝöÊ,áØÁ=2)(3,100):
				while ÂÕÐ(k,x):(ÄÊPSH(t),ÄÊPSH(ÄÊPKE(0)+[k]),(t:=ÄÊPKE(0)),ÄÊDEL(2))[2];(ÄÊPSH(x),ÄÊPSH(ÄÊPKE(0)//k),(x:=ÄÊPKE(0)),ÄÊDEL(2))[2]
			if x==1:return t
			if x in Âÿ:return t+[x]
			if(ÄÊPSH(firstÂÐôbool(MOD(lambda ÂîÓ:ÂîÓ**2>=x))),(r:=ÄÊPKE(0)),ÄÊDEL(1))[1]**2==x:return ÄÔàÑ(t+MOD(Âÿ,áØÁ=ë)(r)*2)
			(p:=MOD(Âÿ,áØÁ=ÿ)(25));(ÄÊPSH(MOD(ÂÚü,áØÁ=3)()),((ass:=ÄÊPKE(0)[0]),(bs:=ÄÊPKE(0)[1]),(vs:=ÄÊPKE(0)[2])),ÄÊDEL(1))[1];(a:=r)
			while a<=x//2:
				(b:=a**2%x);(v:=ÁØò(lambda ÂîÓ:MOD(Âÿ,áØÁ=ÂîÓ)(b))(p));(B:=ÂøÐ(ËãÂ(ÄÕåØ(p,v),ÂÙû)));(xx:=b//B)
				if(ÄÊPSH(firstÂÐôbool(MOD(lambda ÂîÓ:ÂîÓ**2>=xx))),(pp:=ÄÊPKE(0)),ÄÊDEL(1))[1]**2!=xx:(ÄÊPSH(a),ÄÊPSH(ÄÊPKE(0)+1),(a:=ÄÊPKE(0)),ÄÊDEL(2))[2];continue
				(ÄÊPSH(ass),ÄÊPSH(ÄÊPKE(0)+[a]),(ass:=ÄÊPKE(0)),ÄÊDEL(2))[2];(ÄÊPSH(bs),ÄÊPSH(ÄÊPKE(0)+[b]),(bs:=ÄÊPKE(0)),ÄÊDEL(2))[2];(ÄÊPSH(vs),ÄÊPSH(ÄÊPKE(0)+[v]),(vs:=ÄÊPKE(0)),ÄÊDEL(2))[2];(g:=ÄÔÔè(MOD(ÂøÚ,áØÁ=ãÊú(vs))(ÂÿÇ(2)),Âåæ(ÂØõ,MOD(lambda ÂîÓ:Áÿú(ÂÛÅ(vs),lambda x:ÂøÑ(ËãÂ(ÄÕåØ(x,ÂîÓ),ÂØú))%2)))))
				if ãÊú(g)>1:
					(y:=ÂøÐ(ËãÂ(ÄÕåØ(ass,g[1]),ÂÙû)));(z:=firstÂÐôbool(MOD(lambda ÂîÓ:ÂîÓ**2>=ÂøÐ(ËãÂ(ÄÕåØ(bs,g[1]),ÂÙû)))))
					if(f:=ÄóÌÐ(y-z,x))in[1,x]:(vs:=vs[slice(None,-1)])
					else:return ÄÔàÑ(t+MOD(Âÿ,áØÁ=ë)(f)+MOD(Âÿ,áØÁ=ë)(x//f))
				(ÄÊPSH(a),ÄÊPSH(ÄÊPKE(0)+1),(a:=ÄÊPKE(0)),ÄÊDEL(2))[2]
			ÄÊPOP(0)if ÄÊPSH(False)else ÂùÆ(ÄÊPOP(0),"Dixon's alg failed and I don't feel like doing the \U000f0931 big boi next step yet.")
		if áØÁ is ÂØÑ:return MOD(ÂÑÖ,áØÁ=0)()(MOD(ËãÂ,áØÁ=ì)(ÐÌÛ(MOD(Âÿ,áØÁ=ë)(x),ÄÕÍÔ),CUR(lambda ÂîÓ,ÂîÒ:ãÊú(ÂîÒ))))
		if áØÁ is ÂøÚ:return MOD(ËãÂ,áØÁ=ì)(MOD(Âÿ,áØÁ=ÂØÑ)(x),CUR(lambda ÂîÓ,ÂîÒ:MOD(Âêà,áØÁ=ÂîÒ)(ÂîÓ)))
		if áØÁ is ÄóÌÐ:return MOD(ÐÌ,áØÁ=n)(MOD(Âÿ,áØÁ=ÂÕÐ)(x),CUR(lambda ÂîÓ,ÂîÒ:ÂîÓ*(ÂîÒ-1)//ÂîÒ))
		if áØÁ is æ:
			(t:=(-1)**ÂÕÐ(2,x))
			if t<0:(ÄÊPSH(x),ÄÊPSH(ÄÊPKE(0)//2),(x:=ÄÊPKE(0)),ÄÊDEL(2))[2]
			if ÂÕÐ(2,x):return 0
			(p:=3)
			while p<=x:
				if ÂÕÐ(p,x):
					if ÂÕÐ(p**2,x):return 0
					(ÄÊPSH(x),ÄÊPSH(ÄÊPKE(0)//p),(x:=ÄÊPKE(0)),ÄÊDEL(2))[2];(t:=-t)
				(ÄÊPSH(p),ÄÊPSH(ÄÊPKE(0)+2),(p:=ÄÊPKE(0)),ÄÊDEL(2))[2]
			return t
		if áØÁ is ÄóÍÀ:
			if ÂÕÐ(2,x):
				while ÂÕÐ(2,x):(ÄÊPSH(x),ÄÊPSH(ÄÊPKE(0)//2),(x:=ÄÊPKE(0)),ÄÊDEL(2))[2]
				return x==1 and ÄóÍÀ(2)
			(p:=3)
			while p<Âüï(ÂÕÇ(x)):
				if ÂÕÐ(p,x):
					while ÂÕÐ(p,x):(ÄÊPSH(x),ÄÊPSH(ÄÊPKE(0)//p),(x:=ÄÊPKE(0)),ÄÊDEL(2))[2]
					return x==1 and ÄóÍÀ(p)
				(ÄÊPSH(p),ÄÊPSH(ÄÊPKE(0)+2),(p:=ÄÊPKE(0)),ÄÊDEL(2))[2]
			return ÄóÍÀ(x)
(Âÿ:=ÐÌü(Âÿ))
def Âëì(x,y,áØÁ=ÂÞÅ):
	if y==0:return áÍÞ(ÂüÌ(x)==1)
	if x==0:return áÍÞ(y in Âù(1))
	if ÄóÌÐ(x,y)>1:return 0
	if x==1:return 1
	(t:=(-1)**(0>x and 0>y))
	if(r:=MOD(Âÿ,áØÁ=2)(y))%2 and x%8 in[3,5]:(t:=-t)
	(ÄÊPSH(y),ÄÊPSH(ÂüÌ(ÄÊPKE(0))//2**r),(y:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	if y==1:return t
	(ÄÊPSH(x),ÄÊPSH(ÄÊPKE(0)%y),(x:=ÄÊPKE(0)),ÄÊDEL(2))[2];return t*Âëì(y,x)*(-1)**((x//2**MOD(Âÿ,áØÁ=2)(x)-1)*(y-1)//4)
__dir__=(__file__:=áÌî(moon_dir/'Builtins/meta.☾')).parent
(IMPSIMPS:=(('ℍ','ℍ\U000f7e19\U000f7e18\U000f7e1b\U000f7e1a\U000f7e17\U000f7e16\U000f7e1c\U000f7e3d\U000f7e15ĵ\U000f7e88\U000f7c7d\U000f7c7e'),('⫚','⫚'),('¶','¶✿')))
(ÄÊPSH((ÐÌü(ÂÑÖ()),{})),((__ÄÊIMPORTS__:=ÄÊPKE(0)[0]),(TP_CACHE:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
(TRANSPILE_REF:=ÐÌü(Holder))
def EXEC_NATIVE(áÖï,*áÑË,**áÑÕ):
	try:exec(áÖï,*áÑË,**áÑÕ)
	except áÍÚ as Ïã:Âçß('Exec failed! Writing to %s'%((o:=ÂÞÅCAT('/tmp/%s'%(Âøî(ÐâÇ(abc,NULL)),),áÌî)),));MOD(ÄÕéý,áØÁ=ÐØì)(o,áÖï);raise Ïã
(dump_cached_imports:=lambda*áÑË,**áÑÕ:'TP_CACHE.update({%s})'%((lambda ÂîÓ:Âøî(ÂîÓ,','))(ÁØò(lambda ÂîÓ:'%s:strd(%s)'%(ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(moon_dir,ÂîÓ[0].relative_to),ÁÜÙ),repr),ÂÞÅCAT(ÂÞÅCAT(ÂîÓ[1].native_code,stre),repr)))(ÄÔÔç(__ÄÊIMPORTS__,MOD(lambda ÂîÓ:ÂîÓ[0].is_relative_to(moon_dir))))),))
@cache_
def moon_to_py_cached(áÖï):ÄÊPOP(0)if ÄÊPSH(TRANSPILE_REF)else ÂùÆ(ÄÊPOP(0),'Cannot transpile without transpiler!');return ÂÞÅCAT(áÖï,+TRANSPILE_REF)
def ÄÕôñ(áÖï,ns=None,get_code=False,include_builtins=True,native=False,Æå=EXEC_NATIVE,ret=False,init_ns=True,code_ref=True,custom_errors=True,show_error_áÑÕ={}):
	if env.get('MOON_DISABLE_CUSTOM_ERRORS'):(custom_errors:=False)
	(áÕÃ:=áÖï)
	if not native:(áÖï:=moon_to_py_cached(áÖï))
	if get_code:return áÖï
	if init_ns:(ns:=ÐÌü(BOOTSTRAP_GLOBALS.copy)|({}if ÄÝõÒ(ns)else ns))
	if code_ref and not native:(ÄÊPSH(ns),ÄÊPSH('__moon_code__'),ÄÊPSH(áÕÃ),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
	try:(r:=Æå(áÖï,ns))
	except áÍÚþáÍÚ as Ïã:
		if not custom_errors:raise Ïã
		(ÄÊPSH(__ÄÊIMPORT__('errors',globals(),'')),ÄÊPOP(0))[-1];return show_error(Ïã,**show_error_áÑÕ)
	return r if ret else ns
class Module(ÁØö(ÐÌü(ÂÑÖ()))):
	def __init__(áÑÞ,name,ns,code=None,native_code=None,hardcoded=False):super().__init__(ns);(ÄÊPSH(áÑÞ),ÄÊPSH('name'),ÄÊPSH(áÑÞ),ÄÊPSH('code'),ÄÊPSH(áÑÞ),ÄÊPSH('native_code'),ÄÊPSH(áÑÞ),ÄÊPSH('hardcoded'),ÄÊPSH((name,code,native_code,hardcoded)),(setattr(ÄÊPKE(8),ÄÊPKE(7),ÄÊPKE(0)[0]),setattr(ÄÊPKE(6),ÄÊPKE(5),ÄÊPKE(0)[1]),setattr(ÄÊPKE(4),ÄÊPKE(3),ÄÊPKE(0)[2]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)[3])),ÄÊDEL(9))[9]
	def __repr__(áÑÞ):return'Module[%s,%s]'%(áÑÞ.name,'✗✓'[áÑÞ.hardcoded])
def IMPORT_find_file(p,g_dir=None,w_dir=None,flags=ÁØã):
	(ÄÊPSH(((ÄÊPSH(p),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),áÌî)),(p:=ÄÊPKE(0)),ÄÊDEL(2))[2].name,None,None,ÂÚü())),((name:=ÄÊPKE(0)[0]),(F:=ÄÊPKE(0)[1]),(native:=ÄÊPKE(0)[2]),(failed:=ÄÊPKE(0)[3])),ÄÊDEL(1))[1];(dirs:=ÄÔÔè((p.parent if ÐÌü(p.is_absolute)else None,g_dir,ÐÌü(pwd)if w_dir is None else w_dir,ð(moon_dir,'Libraries')),None));(sufs:=(p,'%s.py'%(p,),'%s.☾'%(p,),ð(p,'main.py'),ð(p,'main.☾'),ð(p,p.name)))
	for F in ËãÂ(ÂøÚ(dirs,sufs),ð):
		(ÄÊPSH(F),ÄÊPSH(ÐÌü(ÄÊPKE(0).resolve)),(F:=ÄÊPKE(0)),ÄÊDEL(2))[2]
		if('↺'not in flags and ÂÞÅCAT(moon_dir,F.is_relative_to))and(h:=ÂÞÅCAT(ÂÞÅCAT(moon_dir,F.relative_to),ÁÜÙ))in TP_CACHE:(native:=h);break
		if ÐÌü(F.is_file):break
		failed.append(F);(F:=None)
	return name,F,native,failed
def __ÄÊIMPORT__(p,áÒÿ,flags=ÁØã):
	if'Ń'in p:return
	(ÄÊPSH(MOD(Áëý,áØÁ=ÄÊCUR((1,),{},ÄÝøÇ,ÂýÃ,áÍé))(p,ÄÊCUR((1,),{},IMPORT_find_file,ÂýÃ,áÒÿ.get('__dir__'),ÐÌü(pwd),flags))),((name:=ÄÊPKE(0)[0]),(F:=ÄÊPKE(0)[1]),(native:=ÄÊPKE(0)[2]),(failed:=ÄÊPKE(0)[3])),ÄÊDEL(1))[1]
	if'MOON_LOG_IMPORTS'in env:Âçß('⨡%s %s = "%s" : %s (native=%s) (→ %s)'%(ÄÝõá(flags),p,name,F,native,áÒÿ['__file__']));Âçß('\nmoon_dir=%s\n__þIMPORTS__:\n%s'%(moon_dir,ÂîË(ÁØò(lambda ÂîÓ:'\t'+Âøî(ÂîÓ,' → '))(__ÄÊIMPORTS__),'\n')))
	ÄÊPOP(0)if ÄÊPSH(F is not None)else ÂùÆ(ÄÊPOP(0),'Unable to find module "%s"! Paths checked:%s'%(name,ÂîÊ(failed,'\n')))
	if'↺'in flags or F not in __ÄÊIMPORTS__:
		(ÄÊPSH(__ÄÊIMPORTS__),ÄÊPSH(F),ÄÊPSH(None),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		try:
			(ns:={'__name__':name,'__file__':F,'__dir__':F.parent,'__path__':ÂÞÅCAT(F.parent,ÁÜÙ),'__EXPORTS__':{},'__þIMPORTS__':__ÄÊIMPORTS__,'TP_CACHE':TP_CACHE,'TRANSPILE_REF':TRANSPILE_REF});(áÑÕ:=ÂÞÅCAT({'code':ÂÞÅCAT(F,ÐØó)},ÂÑÖ()))
			if F.suffix=='.py':(ÄÊPSH(áÑÕ),ÄÊPSH('native_code'),ÄÊPSH(áÑÕ.code),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3];(ÄÊPSH(ns),ÄÊPSH('__moon_code__'),ÄÊPSH(ÂÞÅCAT(F.with_suffix('.☾'),ÐØó)),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
			else:(ÄÊPSH(ns),ÄÊPSH('__moon_code__'),ÄÊPSH(áÑÕ.code),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3];(ÄÊPSH(áÑÕ),ÄÊPSH('native_code'),ÄÊPSH(ÄÕôñ(áÑÕ.code,get_code=True)if native is None else TP_CACHE[native]),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
			(ns:=ÄÕôñ(áÑÕ.native_code,ns=ns,native=True));(ÄÊPSH(__ÄÊIMPORTS__),ÄÊPSH(F),ÄÊPSH(Module(name,ns,hardcoded=native is not None,**áÑÕ)),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
			if name not in sys.modules:(ÄÊPSH(sys.modules),ÄÊPSH(name),ÄÊPSH(__ÄÊIMPORTS__[F]),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
		except áÍÚ as Ïã:__ÄÊIMPORTS__.pop(F,None);Âçß('Error importing "%s"!'%(F,));raise Ïã
	(mod:=__ÄÊIMPORTS__[F])
	if(k:='__EXPORTS__')in mod:ÂÞÅCAT(mod[k],áÒÿ.update)
	else:ÄÊPOP(0)if ÄÊPSH(False)else MOD(ÂùÆ,áØÁ=ÂÄ)(ÄÊPOP(0),'%s has no "%s" symbol! This is strange!'%(mod,k))
	return mod
def __ÄÊADD_EXPORTS__(áÒÿ,*áÑË):(E:=áÒÿ.setdefault('__EXPORTS__',{}));E.update({**dict(áÑË)});return E
def __ÄÊADDGLOBALS_CLEAN__(M,áÒÿ):áÒÿ.update(MOD(ËãÂ,áØÁ=ë)(ÂÞÅCAT(M,áÍÙ),lambda x,y:ÄÔýò if x.startswith('_')else(x,y)))
(__ÄÊGET_GLOB_MODNAME__:=lambda*áÑË,**áÑÕ:áÑË)
(__ÄÊSET_GLOB_MODNAME__:=lambda*áÑË,**áÑÕ:áÑË)
def show_imports():(ÄÊPSH(__ÄÊIMPORT__('text_format',globals(),'')),ÄÊPOP(0))[-1];(show_table:=lambda x,y:Âøî(Áÿú(ÂÛÅ(ÁØò(lambda ÂîÓ:ÂåÔ((m:=ÂóÍ(Áÿú(ÂîÓ,áüíþËðâ))),Áÿú(ÂîÓ,ÄÊCUR((1,),{},padc,ÂýÃ,m))))(ÂÛÅ(MOD(Áÿú,áØÁ=2)([x]+y,ÁÜÙ)))),ÄÊCUR((1,),{},Âøî,ÂýÃ,'│')),'\n'));Âçß(show_table(ÂÛê('Static\u2009Name\u2009Path'),ËãÂ(__ÄÊIMPORTS__,lambda x,y:('✗✓'[y.hardcoded],y.name,x))))
(BOOTSTRAP_GLOBALS:=globals().copy())
TP_CACHE.update({'Libraries/peggle3/rgx_golfatron.☾':strd('c$}?S|8E?{7609T#j<Lonajko9aTuDZqpE(HiD8UF%r`Dx?11uIhWk+9(!k4%UB{NUnmJ`N$m)lmIe@tl>~%ZKu{&(hxt$VOZwiMFFSj?c3jH+;M?1odGp?9KJU$E#!P-9|04I>0UO4nwO;HMqSb<TAIQD7ye{uB_#F2NkMlvF$*b~1`7J91ws4*dCkej$yZne1oO6)`zdyIk<PMC!E5OKy@@nu(mL{BWwi>MF8wnU^Oqu8N>&cWcKk>QP+UE3`>m_{;n*R(F!`EH8C$5kM(F?%r$MU+!^#gCudGHzZJ$A)Qv#B>oJvBtPnAV;*n0S>j=94GWjXcG+@8u2lVhrJM+rd7dBe&&O?VzU`F>0?}Z`Ka;`EfR8SGekIeaz7dbhG9Olh@>X=P&-wj2GtjmGUv?Vv<Y;(`2N2zqG=ZbSpeAmX8ZuJuk1k%uaG1p6rxvm~hG8IfA-3m|V^VX|$ea8{<i&*ODB0s9n^*+QC*!J#BLv6!GCRi~K`gg$3Wt=gBC0Bhg)FKp{M+pXUrMm*sEr33G;MgxZ<`XHKswv;Sg-ywLEa{A)W@-vYjN<yVY%IA>cegl<=UB)>Pl@og>?SsB;sg`f<xF3`F3=gmulVPd$iTnLMfP+;*HPO$>qGkqG^q=PHUsQOv%QLfwoAXy#AVLL#NAWLrp98C52T(1X=g499EnFtQ0)UbTqQlmx7gf#4M;bPQ?Y&ADE%y}^68sV$*2l*fEq5!uMW5W68qpzL<{oIugG#-0itL4eZYV?^`FEF+!u&m(kf5`9TP4xAte8;YuAOrX12Yha>giG7rk@w_7C{1DO_$kK!u(7c4{0sDV`K@2f|M>Qw{@6az@xcaGyBUCJ?#e5L(w#O_KULXN?{pI<8Xn4MR@&12n2#R)@{G^*GGP5Qb2zldk6>u_zI->$M?g;tcDMj*uAA~Wtu!rmoV8fw_<~ACzFtJocLKY>C^+d<VWj3~@;$(>;9d}T22>d9#c5BI^4xha?)}QPj=0;b=JFsTaI@g_G}EBUbYr>D$P^Hku<^R}qo4?B+09zhhDDEN!&)K~&1%eaFGQC20GL;Q`&xA7!piB@6$smZ!ABVH%g3<HL5P_8EqFy67c~F)?ml*C>{sdb0NWc#1z(@bT}E8~7C3KKS%IX?G>t^kU6XtArrbA!_kk07bsSrF6id)+dXVqP8}gB|OK-ZDaw64t@=N%pW!CjZ!w<=FYywGfjHzA+@fhMfHaT%@qI(*cskK};AXp_QR5N2IyhTtVm0l!F4D&QF-me31Wb}!3=Lg%t8BZTnF9Hhzl6x(l47#o!x=hNYJrjv0&LjEM5a%*yA*dS`+7vN!o9MuGl2P_Ic?d+{RC-+(A>AAfW5~0Gjcl8;#{9QvsT7}atGH*}g0J`GUGi<KRcwQ)28PuD^cJ}z$%a|Fo=m1ue^5XQOg8#~N<*9dG%Zr<8$?%4Ozf=eq?#)WRTWUF8jB5?t=kc>>b7~7cFY}s?IwQxTi!17)R5FI6>QKB>gxvKaCR1vyyono<QZoF$B=nNI2jJQ31Clhwj*FAo>Aw+LC1S8@N9)g_u(C%6%0DavsI~3+3`#YpXExmjpKZhL{K!N?j_Kg70K{ySw%vuoCFO{vuK(pNrU(>Wg232D4_dcIfl)<-clAOHm>hClV|QTcKVBuhm0xgA^9hss+J%p=#{FR^q#9aFahR{b>=gt)7T6dD+An>O9q)+z?q$<40^;(V9muDm-`|FM~Pe(j?LMcfz{9Fq?dICZ?QTbO%N<BlvRMyu8`j9spc8gV)lIV+ejlvRbfq6J~-HyxGw?jOC4J<Nq1Ax*^zI{n@U+U>p>IzA_mVkEv}YZ1l*^PkmEp~0UUbeq~+Cg_AO>Mi^ZDgB2<+ELW5o>QuwEQ1w)tQLtGw5aSq4a439&wOI4Vm-ch1{&B{Vuk-K6|t)-R>75;7>nZMPk)kz!T5o(*Lul(zpXP*L)Wx-$41s~4bg2L8CU+*TH&MwmVnS9Rqd^{c}X|I8vN8de~xQ(?b^@!Y}wP_h9!h<twq2p$izLn5wsZ~(W2cEM4b<-U+SSzo{g<QKz0OmB2d)mahdq+O0oHxrSRS<Mya-kMZ8^G2l@^QNnEM`vvl&O32sq#s`OhWMX>!&`~`Dir>_IN1oHw@=xJyX){8&|(<D#!|vIDu?2f7R!0x|7lKnI9=UZf=VMuX3EZFy<%KxsFB{-D}74qAuW|CIOWJ4<3?F9ayVPbI37LUnrm(vPH=w<}>ajjCTAtc5V55f0~cW6Cbb&&UZi-_=^QbiF4Y{Y(<O8(bbzK$LbWdjH*!w-8mT^(Rz_AK1HIKFtw&o6EA=`#Xqjsc{Yj~Xz%DL+j&-2HM`-=cf@(>;ZjZ>G2j_pu1(ctF2P}BE|wMe^Z$6bU-Qsb=!3PhW2k$81~A9+dKwFDMW4jedUekJr|JxmrPT;13b5;xio<RZ+{(e=2&IqIb(3*h<$SG$R3-}Ag^t2Ctf5*%H^t!NTJWt|L|mn<<u*SYkjlEdc&L3=6E21nGRLob@(X4Z!_4t3ty7T3yA<qH5ou<VrHmD3%<uZ#`I&mhy^Pb{SUjEPKkaVJe9VS7lNpS;sa-iMSL=h8PlqR`F1G5liHPjUTNNo?JG?ml7}Du;_Ift#$J0DZX@A|5*Uc4YzZ-WiC5^Xh#xJ9Ab;f=zubYfL$!nLvE$6_EbgL}T`*Ig~8J3q*iX--?+g;y`ngcpFdeP}FfKI9j|8@>Lkk8(4h{oIaMjV{WHnU?s<HpTtt_&p6^V6>2sGe2NqMX~C2p~li;keVw%hAef=g(bOy%<GoeVDDmaE2W#Ebv9;Ck)3T6Gdq}N}@<rnJ5~?fKOzL4aD$3{<BIa_3x!yGbeViH}_vLTwhx'),'Libraries/text_format.☾':strd('c$~#MX>S`xmf!U&8VwkzRw^EnvL>+-X4Y5Mi}kDn+lvHX2!bM8A`>23l3KN9Jb*2mwlj8Y*^(S9c05sh<gla3*s<g@22wv@ena{f4B$Vo@4c$(u0E(EyNeOftnNBqy?R%@_o~$E%vxhZ7W~zlQ|(UAnyPf%oK@~x9ha)vkpusF;Dgekf7?5jXEwFkjx*$X6?dv<i52mw_#C^7d3b*=LG=Ql2H=i6>3Rm>Byj41z_Dq=2_j(eV`H!y=Fm`m!f3Sec`IC!gj{teB&O^=J`59H7U%h}d|7hB$yo;=cU)&@rQMvWH(aClNA+I*SZCS|hdIVDXD76m^r*0<<MyUIEvqB(bQ>v%YVvFgQ3ZDZuEBr}r~QAObBG~Z#rKtRrRD-r8|CJBwQPwq;!a}7n3xlH#3Ezjy!b(^jOA%iiD75Q;d*Rh7}F!1`UJeriO1qH6DP$r@qh&r&WTmA0A0l`@n`Xr$!`ZoP|r10!vW@kSaTe=(REqYfj=haa~$h!E1SvfQf(3|hb0z{e?x4d-l~?|Zl%<9|EmiNhsMvv-LbqRFguE(`=OWJ`{8sZGrF(9em5rHs;|A3dn<TNyd2LQFO2Le?sl5T3m<x!EIhfQZO++pJ&?d!xf9G~Gl0IM>kRMwont#Y*ilZs0iz4zrO}Hzy=L?{IF>iK$4aGIeX`bor{{J`C4$ihV*f;)?ngUAmu98W!A_kf5+d3xPK!V9`_Chcjc|wm@lTwjsXIN+BXr}$n_C=s^Fo{=oT}|!r{0VL(@ggGY<@I@^57M^je5mp|Iu!_oXuLVTfoYq^%@Agf8s9Ei$sNB0RAXFU%@B<ds5sG%glow);rd$;<cv;JULzNRHJkM{_y^|kdXwgQVT3|Q7nrmC|1|R$$Zv9aeFBR@TTbR+jC3{UU#YirlUvPYd6}RZYc4d2C2uM7GH=pu>#A?6*<aLW)G~12Sm+EqMF=MG~~k?NQ6W=r^q|GS_79E0@Qy)tWj^dAjK(*1!BvUo)q`Q3%yPy?!Z#F+^N)P)ks&RcAN+akayCmSvVu=Bd+eTII9W6Xp>m6j?3NRTSqIPQei?6q{eOaLIdORdOoMg7UvI{1|ZByV9n`RE2rWL4t*+~ut+5t1BDc0b!!;J$<kO$D^ka<mqlOUSa;MI#cPifC8I<hVm%;(iTmuB=Jbj<3s{hLpk|aCjhL2m&*8HUmn+qJZAi5NHne_HBT1}7)IBblWXik&jmjvrxG0bu%!!BMQ!NJ>Q{I(%HIPG@joM>JirU7g!8b~+Vtv((v%Z-Ja96~g|0Vz7OX-NLlam$=A)v)x2#VA#M=ua9!J_zDE6bcFku-6RX0^uRv{(XRUv!*8236dW>KM?8H@7BP!0DN8X|Vcg!=kZEm?a4nsq!2)*obWyLWdz?wg8if$$SWB7cXSIci$~Kd^}N|$rQEofyP(vh=q|iVGG>RZSLseUZgObm^AIxh=W9V3yq$~l?R4S+kjnv0B1}V=OWx)5~mWRAVz4rrj$_;gtlQM3RhjTMdA)J@s79_VUyZ-4G<~BH@XplCB12t=y#;EGO{_`WRc~Kg2jSO&;l?4<;a}g3?ZY_t41$MF`X9|w3rqqCV_!PhjqAVr>NT*aanis95zdYGWsx9@URYt<F-2+<D_&%ckOQ4+O)$6n9c(-ZZu*fF=FExGLh~fv1d8?a+}Zh=36EJT2lhbhD$U6z`!Ts412c>A5Qd-Zz!%PS`cVxt|@PPfZz`g5PjvFEP-h{9oTBn(!jLs3XKgcvw(WaLnmYt?2MgRo3##4H$D<Rt!C(748MwO%T&3_2)Q#7$Fs6HmnVCOA6Lcmd?47$kf0az-qC{z_fA4`cv|&Y@_QI;!ZiBd53mdxUWcpZNPV`be69Tl4q=D@6*9zz=&E78leZMeM93sDkb#jz^^!O#V*}_9PHICj6(Pyhk>ErZXvSa?BKoxm3LFwiARQ1VVP#UVLM~ij1q`DQ$PO##gpdHXA{;2S?C_i4M0yOIE1QCF49^g{K^4it!|wsDl|M-QRH|ZXPuLM`+K#S&?vq#RKm7D+{qeIbZ5@OPA1qy6EnYKuagW#FN1+T0(P5#IKk0uMDFWFrmY4pDT1AW&GgiH81wd)ojI`YY-K0R=BW_X*ZY>G71|q6FjWkqXzU$(9R!gqH*$I2M+p02@0MsjVYiF!>2V?~d*D%iZx)p<+4t*w#K7+PoDp7KcNnf|(${AV`CuLz#y-KpU+bdT-?ofz+ReTrnmbKcHdxA<UMIp!|Gu2c{paR2LxVWgb7-q81y-17P3bN#21YX8K3ldTq;5dVHHfBju2ELP~e~KVV$|B^sXA(9rdx3OA2Qt*bbd0g6P#~(BQm`hg+^SlJhMLXhKs3EZXGswhKg_Z@^cHJShG3921T?i-Ig2PK#YOF7=K+m57Hoy!sKtG9(?o!Qh@q`EB`EJ3j&X_@j<>y%1_Qn^cp{^j(cKfUg^kxI^Kv<32HiohjF|(+55M}bU8HYp#2qx3auAuxjAIO55KB@lH%k#rOqy&?GC8Z*g-Qequ+mteCIsa!08Iijk4VZ7*+{9Y6irh>5?Dmdk{r1e*Tr`*%D=ecU;N6yc*{TWiGT67fANlg@vib{7cc_{8hSXnmG9f?E)I)I+a*zG47ZUXCW{wrT2NREbth~k8+}?jR?Qpe@j+f0U=3JEaA@}6ZJ!P$lqm4{{EJ(g|C%wskuusuHvr8QV^azy$#F?O!^`J?AoN)a1vCqmoO!rO$v7R6_(S+fnYdZGyjC%iavCCqne5c7GLEDHN;fdwfvMC2?HC9nnRrq=5sEM?3?ns`e)N~tfF}OZBOn71%wL3>bzliF&tJUnFV6XkxBbN%{^D~Rqoah1C^?kMu~h{MHBX7OC#8+d-&PV3X)bz@D~RS)q;Fy-sRA+Q8#x=EvS>2v=b7peszwe}BPUgZ9a7FqTr<7UVWCp5{ry4P{~)Xe2Ns!VU?Gh`pB)P5eDMEnu2>L*lLYIh<Ul{nU)x0ezu8I}biP+j`clU%Cn-$HSqdCiWK6+<EWcL>mR&3aSQYvE=Ep&!lanHG+H?=fIC;`8s$QN9fo76+v$iF>iANeru4qECAW`dm4bNqWC=8s+*Dxo~_4kbYcA}XBQu#vUNC#x>UP5IsYw-w^74qf0k-m+lvnc0r)d@x*KMJ#WMDVsXgUKW?TW?!6^w5gZIVE!n?rEHgAVlvwh1sIxIAQuV#gq;>22j<MYzY{H-Cl?Xfr3WIlAz@WOO6WUbaE0fpR={=Ea4sEQf<=C3J6<m!NN2jKN>a9ENa9OTUfxo#4#OtK}_fKJRVK@>qPIMY(I!+0wlRlQJa9Wl#`MS^Ce|@@8J(Nm1cDNqUm@&vvCfyxdEr_g;^ux1^|PoNKXyV6=gn2W_S}h4I?2Qv$1SeEy+yx!km?VF6NnEfpX`ci*k0mC}ZE5PI)T*6jFIh)%=?oK9y&?f@7lSf>O7s#35QrFbt7h)i{F)&SOZMQ;EZjXj`uX-t{sVo6<h#6^B>(6p7t1ol1d5R#jS(MKc}IqX24bO%FJjRU~QVv%H(vM;jbdLHW#B(u$cLsJaq>`Y1PX79Oae@x0ICXZpAnfb7UaUpy(neA6lMMB3>EaVb1S*@R|l?=Wojea)PPV^Edmb9h&J+m?!Wv^!>!Dn`UmoVH0jEnUA2r7K{kVug0wn}C<*>JaPJ+B2m}yXu-cSIuWLnK7`90WQe*d{xe9>=X9Hq&>#$-PuvwN%eizl6v)CBQk?F-IcuBQ3tTSfEJ8G8;b%PFC?itTj3QIKrN%&U;-g4P|=5V!M+gO-zb`V*vK!2z(KJ|$)d#F5P0qtlQ}xNg3$!4@W<g{R;^ch;Q>$~yvP7DWyBJ+-^<Jpi0B!4di)6A`||y<ES}5afh=Ci;-M^ll*O7Xo=D&3Av);z@}oF`;Lgg{r@HkSeqX^h+3AvOf2P}?>xT2P;e~E^AqSq+?Q^=}rEHkf4X5<WynZ>YUoPvHD`*7B>zEgJIr-M-5!)wN|A4Ej0AK2t75(y+d|A~st6|M;{c=aY+|@5%>z8lz%Pr{;elCmKvRGDLqAXTq@vSVrQPGw<Jd?$BS*)Uf{W5>opFiQ>zy0cm)pP#Um7ibu{e_>O`~4-qzwGzt{r+{of7$O}@%xK@|LUvtwFmI5|NN8R{|sIp`u!WP*4NMY{cG^`BfQS}{m<d`k>CFUiYM@_`Td(vJcY)yP(Fk596X=={e*w|tbgvNSpECySL;tdh36tXmtL*^?OS-hgXcax-@~&C&tKvB0iJvR_~P;vcy7RR8J<h<EW@(`&zHX}&O>n(o&|X5=8W?vC-eeA-ov;y>GzBKkzmyH?GM7%O16<yW`oFc6OYq0LZR<FF)>28f+69BBHo^QgRWY=vETp8nk^l~eTRRa;vgQ1`-f0>BvO~7WKy)>2-QXV?ZUb}N8XQAj;1-BLBxienL2lv7Z=2HM!I*EQI7PumDYHT8XfI0FFR>2wDg89h!?2`T%X2L*=bHOre!F9v`oZa5MQeDYjB!U?}biK3aDkFh=kQffCLQ%uNbr>?}dUr?{;Nyc}zw3YZwRw$;o4wQ|ir5xycM95YuyZmP)O1(=C-^=O;8yg@VaUpD9qVTiy7~zp-FDg=2VvoyV;yGm)_=YB{F;$%#zHPMnIUY2qhGY10JP&S(ldN4E(E;e0do$bzm{QFB0|l(E+bj#V4tZQKH+@{T$iL0V18`r13X^3sM9<6CqXZjMpMcj<z3jGXeAJ{$MmJf7x>vFvXn8PFV;&K?3IYL1K`b9n5?D!5rhW_{3NHd)X&TUgM(Lp;8W^zM$j=fn3M*#KEk;$MmE@^+C;&oP)65sf>uDa!%dM<y5)vEFl=UFK|UiC~X@<q}u6u*ALF=EvTRkX;ZDw_$yvI_FVB<&1b7y2>fHo1<~842YokTKr|uIvM*|b=R>G`&iyH06=(zru<P%Uda<3Nw$xXKEXw1t{rDdQb}(#a-|Y(4tw_RFCF;cy~9V29W9mEWTQP^ZUBpcX!3fY&1H!-iCbcJ>U~$6+-_T6I%BrH)@gHDVhskRHpgH5!c2|L@mGCS=&Pc>I`q|1UtRhlxbo!FRwtlXGv4-W4nOz~fsoDNht}f4I$ZgN7xXz5_#IrNw|Vf2^>}z;bNtmSf_O@<30`#FOi($aYURylo6C~0)Ug^Ms$Yo)7+nDou%MByq>?NZ2lTZ+VuSv`wrJd9$Kx2Y2bFd#B|<$6BW*`awi=%zmG%Z|hB{#51**sDT4B%aD&d%DcberMQ#z*QUMetUC|GR6b|)uogemuA+!~_oGcNp554n#!eAEfErRFR_L~VRyY)o@l-EyN`wcvZ)?O44TxAEVu1<3YVVC&G;%<SpaT&q#;_N-p5-kP*#+tXN|d!uU2lv_Qk-NLGlH9p;$Bs{V?&PKvp#VVa&rb7puAH);p{;2JLf5$&}&MkLc3`on}cD-8eR^_sSVdKFtjO({NtP-1T6h{3r|LErjMxSa7bV?u9u5K8Vfxcy&bR2&w_*2CnWWzYGV2a5ch58&YGMnWpWw2Q%E2T?i+g;M9!cL9p26oD9+zBiUF3sCsSL6?IrChe14M%OVn$EVnm{Z|d&!DsStKyzI#EG9zEJ5WdqjMHDN+#pY1D(Kmm=|Bk>;1}OE00%r@IL?`|8L0fgTMl?Y{od<8t9f7W+8|I0pf0TaXNKXHJO6>7SqaVdKmSOFFt!_Nc&_U?IFfBY2Txym75fsOt0nA@+26d%{TK;Jh7~r+i0{A0SKpRZpZacJaz2o0M#9MD|;i}s`s{G^X#^uL-!bbV{eg@ApDQoE*3OZtzM_Pl!cgMaXy?1hGIdp;!vG&lmFYN9V&U9wp41C>#b5L_y;x>7RUDv82mp6%cln'),'Libraries/peggle3/main.☾':strd('c%02VX_FkqmEY%Al-t2Nv!@u(Aqj7@y?7XngaaMpnIS|(d$yz0T|H{k*H+a?tpyQ67Q!4}WJw6yAS}#{wGv)z7BH+Ms0hCA57-YoKVZWVyFXyxk(rfs^)wP6wgWWPdA#@X<-0ShMW^MpPWiRE=z0B<ZO^I3Z^pljUv#Vd@JcPd7{3z#BEBZ&jDY7C);1my%_ctm=;+$<_048eh)U#-qh@Cq^u4Ge-R<7+q}L0DbVa2irF3cD@ij3oWkZPjodrkAEdcjsd^vtU!97l}9zA|g5ati!FI{N+Rs2jnz5suIEk*ond_}-#))@nwZb!t=K*uLy>|&3UelPT~?e+NAVvOkhI)S?YkgscC$A$x63Mn@0o579`h=pL(a&Fs?U`akK<jHdq=Od6AF(7)b#9#Ciigi;>sKp4~ViTs@Tt$`hltaWkD>boZ5+G{(9fy~iOa$Qn9KSAWGY))AbFH4xWWk_8-Hv0>(`1)%OJ^7$**D@(<4f3eHU30{SMc!@_|Z-<Fzcgs4Oh*6&HzTPCsS2(txo$yG`!_jHHrk1ktQ`k&ULy$7&XIg+YbfqnBnq;_;!4?27j)>as+>sb3TaI2;~d+2nGX2g!t$x$XR243)+HI)54Y##e=Iy#Dc^I!>XRs4IPq+DR^K}u9-gPD=EiTqAK|cq9uAbVs6w3d)<~V5Rtnmfkf;JQhkdqk+Fq~3jN57qCn_HEGnq*xR5-~TgzI4Wi9ctvgEU1y$QPf$9oj4Lb;k!c2ZLXk@ErS13tVdQ)2W@m<%%UM*Qr`@}{ARAm1wwQ9GRinhZ%6J${Ow%kfL`7b1~u*x}Z2boO2eD&AS<;~(OG=f8RT<SMg{I`mF_4cYZx{9Ezx@yGG;nfMnXz9ofd*Xju)4}l2>6-&6kh9q48&A-iB{jXUC6(g_RV)cAUG`MjKl+;1awBcd*+Ie_%W*t%a$#{O5beGNUi>$?#A%sO;iZ9mc#fD%45%8&;t{@iWL~g{N#J9BFUpOFj+rMZ_BFR|inw`IQ7WePhCfW?O9_36Y81|i3r_*)1{n0RpoI{6xG$Y_UaFRs;8gMbt1QGx$Xo)ItVP}4RemOcj@=-Z=24Q!5;J2ODDKBt#x`XHk&FI0BG0^MKn5D(spfCz{T9Gqq1^!~QHEjFVWAV`cx^~&Yjt3src%5qapn>o79^~$WII<YT`cBWcVbHwDg3&r+e_4kwgYIykrXT@;Frl;R1O{i@i_9~kDJI~k7qw31DCoA`kqhLf22~%mNEtk8fKzWV^yR=Gcn|l6ttS);9_1ADR|gOdJ!ty7|KtOfozQQ)EpKGnX_H}PUSrGPPk<B?p%!Q3I^}!q^n5jy)>3swUI5}t9ZvN>-gSwARp+lae)Ei*@BqKU|F60v3Gnoin_{7JayaZcQQ(EAq=Ij66+C*8-wgb1e=HEfnjUp}*lk<8+Ux|rFD${Vwo)TKq_f!_bfbjif&mDn>GgW~K@hc}-9VM=bx+#%%+kB~BM4#J-Jsb7qjY>H`aTRD`P<t)e`)T%up;jxBXY(I`xQ0~{o!!X9QC{iV_c_R2LpCudE;nB2XLYi4k^+lBgPKVWu0&Lh9iG~^c+h?y4g6JM-Tin7NKKaOKvb)o>tEbLuaMudjmgU7lne-B<4X-P9xty0PnctdM30<92t$W-55?td9vJyaVolD1Q>y39oxRdn=RRnjbgKDy<j?O18dyaZ+Svqu|J6Xz%1EXCayX+cx<yran_onJ+}fjhwD>OYmxwoC(pU~U-f(6J4eCi%Esn;^XTf)d<?p>e)#cR&jR*rt{z>>^(+<ysYrMWEPx1I6nyVw&##krR%BxUD+a^J(Y=mzyg}O$A$SQ#lU5Mk>#jy<@l;?o7(&D{Km~>U-ibQ*{{W?%yO(SAW7x`WqOk=U=j%SbBsu4`+hSR@20R1oLKOy!WjB5+ej)x`_);c8rKUYkB#XEx%}_0@f!`mV25SdA3}h}~GTUcZV#GL19s?52ZshmBd5Fea6>N_IO0qWrZG)17f?ZHOjUXT6B_!+VHl0Qs!G1w>VH@GZhy*Um4oTy^tV{&pH`Wsq7P&#~Nyz*wvKE0AZDZz-4FUW~AqQ^AbLY?iB7_YaLRi=7q29|Ph+zt1XqI!%Of%3A+t6D_>ho@E9sVf--#P*htt0rfj!)}pXzR^m%STtqe|#Q)CKlX<d2ZfZ-+07sUf||KN0t#ePlJSp2SVQul|kV`3#a$nf!A*$z0E!}b_YIMo9pr0?x63DOfq%>W`0rAwTs_ywnl{zRv(@N0jbtL(7B>`nT*`a@f$Tto!^1DUjrZv6x1u`Hq=mv+EwSAHv;$7)*&(hG`X?~jR`0tOI(YFo_xo!*?c#+?p`W6_cz8JO|>8%op*z*%S$DnID&E|+gn&_*WfW*rf&k6Z2GIUp8Gji*nRzKMP|lW=!kH&&mYD&%|3GuEA)JA({e;vh9-2-5oFe`KZ>SWy#XN4{|;j%US}F^ChN`e28C2JXsei@!axJYqpO4`$nkQHk_&Lx;`dTLToYNKnut{xDX8LDYzOdYaYf~SKDzYB-J74}SWga94dnfyLF_csOx$DBaBqJ89(py##!s|euGH+Eym3s(&uVpEJ~E?7mJF?orkt)uRcJ*3uz;G#faxWBg&)$M7vqoOH}yv4!RI7jSmjLCC9Ex~URVb20eJnd-~IZ1%JuU=ZGO_c+=#MeCU`(}CX@nbYh9hQTSZxIt}<&#j9QX6;6P@N)Flf<Z3`#KWjTYhdt;ZYaF-PH!rdwr?;@+B5n=olC{S_=ShP)3L30y1odWJdySLx?>ekoqlew7+y3HEKLrILB2HWgJ9AZ$bGcHzbS1WHRPOAq*=^>@vBvAt?r>CpB$J!Zo3fU}MXT|C1QNfCKfBt?BpI`|qNI^kOm^%<rqK_9zc!8ObGwUo!v^+^O(4^HwF;eZ_Sjn-_X%%P%Y8-!|31eyNNv>wBrlVH=#UN9QPo@E*K8r7Lh0+T1VfI_`1vB?Td^LVqs4&T?R-O13S1`}V&nbq|v<_OWt_#~xJq=EvJJ3^A1d|RTz%vNd)97xYnL}TZ(jkZ@hl8j)*zxmz@U#^WU4+HK@<ihA+@fk{%3i5(gU>up+rBdKii;BS$drU2ji;TAOlT?#{B}oK@>k;LT_s*5FR#Sc_h3<qO)QtwFet^OT<A!ISfQh)sNC?YNOjgZZAY%ST_DQcf}*Zk+dV|1X)dNJ^|T(yq5QCQ?1-&{ow}&(-?wk6)5bI!z8pGq2(l4XxxN;E5MR{M;1~lzE}Od|@`HY>2T5_|uQy)(GqiM2QFW`zs(cQQAwS;OY#v@;KH6MaUU>wPnkUb39s;{?+7F^8<|8@<Ik@`pV~4rCz|WX<)&UWJSzA4P_{b`@RZtEbe{fn_$47d*Ffl1QoJk~|k7EVNF;Cc2n0X<OEK>r8CzpRp74;H5|GhNlKgnsRnT%v-Sdvz8T4`FM)q#nqG}fq2xaF*1I_I3~M&GGSFlZS(4MT*L>T8Tt3z{j%*q{pg3hi0g9S*jf-Ah-T`@*B$hpB%1zvo~0tj^_2l}o%G|5;1V5=f8AMAwcWrsiWC%ZFE`^L+?~7v>lDA>)wQ6kewiOxHfO&9lc4x)%8NV^SN|Y>sH7%+i%e{@I$D=)fXs4pR;tu5l5(>(Q_Yj(g>?^=w{Cf3DP&YV$WNtYLzZs{EEZgxj`5FaoLb>GfKDa;7f#WXUj$Ch&v_T9<dj7S!KPKLW><i`Yefq{;?_$E1_Lm!gy@Y@0cF;Ft}fOC7f5dE}OFM?*)}3t*ABje_H3`DIDr)smzzn=XE{q)<e)dVj<&<EoWgnZW5P=T*RfvM7xTS0YkjPAWqy1y>$TQz2~+Xx7lfFmz8xhmI{NI(6xk@tT$8=&Vs4S7fJQ(aQMAYw@SaJUcT^=KP(LsX?V2DwP@&uX-h|&a4hp5k`YX1>~GUfMgpr9C&@4kWQLV2aPmpT~1emT5h*p$56WObqDGoM}I*dKyVe|^voqvt|2$+tjiDideDhx&mZvPDm}7)JkjiU-Jbfg%3o-Z<wOfyOWM$<42CiGiD@T(DckO}^g|eVLG-O!`*riwvQv?keP`vsKDp&m5M#VTN^FI&u6m&q>H;-}fV6f;i;5x|;&|(R*F|XoAgO)(4{9C-k^NE6@8fY#yOOdfXS&fTM<b)7l9r1bk;{Tw&F)~d6Df1Tbe4?JPjYUY84_QKZ?FKX<Hw53Kp}eeKDeN=eda_Hfftra?9p^UN+a{b0*o(lD4+b|D3@eNZ!dk3u38@Dx@Nb#Z5Q2bRtsbvPq{GXgqn77U(E@WyasLoyj+7y^7xb3c9*pZkI+ECNE^*1I=!PQ*(2T6hR=dS@<GRoY~3cKLEYX94~?0GsF;nU96>fYvj;GGtga~}#Y1WPOEfSjRXeiz7jf(fdzB;-WW#NRJOl&$wi6BcUO}aBO@-TuALZ5d-g~z2ckCdp#UcH3B|KzFU>4zit33_mT+jJVJ>{<MlvX0eb}DS7!M6D$a9{yTDPh{p(Ktm-qCJd)ZeM@fmhRFb-iP8=ZC(|D(8~c04Wh{C<@mSxQ)OtqIo0LH9Ce}B=ir#GP_f@_G!P4H@8Z6F`xg&X06n(cgq8#I3kMdkWh)h=noQHWtDyV>aq6rrm5ee8WrdqYN)weY7SfGVcoT~R)Pb?vV2j0l;6k5&>%LIdz<IJ6N?4xwy-WtJ@^R@R*WAJ-<z*KPXsbN^prwIp)(e}LdVrDe3Bh$z*GSIrZc~IM3sadKbr>DB{ZVqQuS655@^+`-rgL#1YUknR!r-Ik4j^DuH|PEWDqsy6JX$U%q<_By5|E({Ytm@T<tDogZxtqAdzccG+EZ&_w@u-?5Q`KNk=8l)I}2qd0zb)t1>U7K8cgJpJLM-(N&Q?*ir<@#n8oRd;k)tryl^t|!b3j8eT;z8r2UN}o_6@8+bP>LnyQnz^+vRnJI=B{xcn%eOq5flC#ghh!pTL^r+`%)_eaX4Pq~?s8LL0MyLL)gb_#qKbQbRO-O}}S{<z>S$wH}7w)@lgmnN_$V=BvXSXG6cqk`uv@s~1Hrm$|RUnAEo-A1xI$wnn6F~TbDw7i(81k<d%I+56^s3`4BZPhmr_HWBT<!G2%jPKSe6=R%2K+_2S|Hxq}(bGrG`O~h6Qz!vU-Txx*3z1V`pV{40MrV~NE_0dUTc|@!6I|)K*i7LltIDLK%50(EO?6-;-a4nCBj0;E{<)W0zT%{_{;e1C*V8q8>jDekSlsppet>revD{6ELHbB%1!YOyXW>g|CaO%TxP|JpXAJA=(A8Ydkh%;#TYX4f-QkNPkOqZQyxrxBwd`G5S8Sx3mayr^siu8&7dO?kADa%Qnhs#op;XfYB`Mcr#+ci9r3^~$>lHR<7-r7<kxR>YE*+mLO-v3dmDRv|ml22rR@?9b=5p%2l@lNiKenrc%i=gRw}yQjj|Y?$zt?XL)!9L2o^&^)H3VSuvsX!joQM%u4$F4KA`GqpXyfuMTtBU3$)5t>du902ZD&-Q!DJHwUu(##rlx|LE7Y&sG?kUYwb@OL-8;|j-nq1U{o~#1U+!M|H!P+Hg|iBAnkT|I3j9uYT;Z`^h%Xv7{eSGy`0Zf0Goq(33g~ZuArR9Y?sRA(KHKvMsv5V~O6q&;<&eQEIx_MoCQPOo&F%n9T!sosvvOl<wp<wGC3378LVF5N3z|oZ`eBI)*UYVDCGAXJmr^@Smhi@_ySLvUd-(KMw@Nozx@)DPsP`y?e^04zRA(Pzgb2M5cnLychFuw;*WDHuMdKg%VfXTDTTj71bF#_}ye`eY{L}~Z)CaOtAF!q_Wv1?){|x5sp8wpM1mE-wC7-D&Fg&eSxCuf&#QQK;qn+4&{ngoO{i|DGhrl#E{oVh*^)8@da(F$?Psa0qi&r)f^XyYFK_fMmGL05Me0K}h2vfGIdhD6ZDA6Fev=kgEXZ6Sv#Ulw^X7oANzWgC)W`y?rRJ!^wzNzBGnIEFNAZNAU;w$m)C>V~<He08>?!a$1TVAghHb*;wk8<#3{4>5<qF$#GhYQZa^gHB#f~-JeMQ2s;ev<A^g0%VEOSZY_<zC)%NJWt9W$1*Zhh3Xq>wK~q_<e5_(pW0J@$`4%U!i`z7JsM>$?o~*$rZt0%joED6?G}`ee&w>k;gId*5+p64-bf0^UYC*oU!%B^xUR7^W{TnH$5RcBjS|nY3s1q>ZBLelNRIxG?oG3BX#qG3{(ZxdDP~nOg_9oKWup;-@YCd)kWn$K~r&=V|=}5)bk*d#rhZ~qL*JohC!Z{^l+oAQoW=DU-{ti)-iG5w|828^QT4C(1Lfp%Zl;Cd?1>u&oA<AhLwVg3`^7BZePhA8y94TsVfO$Xm$h4SlN{XouKn=SUd}$@;^Q$a8<d|0(j@ro&YgK%R;}YTV@M788xv1|4zVu{o}j9&R?n%5c8_{T>JGe?;3la5tHbVNf*^mCT_^H)9vuy?9Z&<PGyU(-l8_0^x8#=l&NvkRZwFSl^+EAcLx4HQOO<6>3ej6byqYEnlBfmFzEX#s;sPgkVy;4ac?rCMRtsAWm%`X!73!@TebQ(Ak}cFHSG1kOZZK1I0dJWp5nc<e_12NkcmG~(X!v$-Ojv!oA!#yxPmI0E(2I5U0>=nmRlL@7CQ#|jB9m!{d5tW1vfb`P4>{-IWh-(BsXR;N!n`-WTT0Pz<l|G-$zMxs8dGvNsY0(sFZsh*?M7lu{d7XC$V&py|9(q8nf?o6p6`~I9B)zC*YBfVd+r1$H3sb^mTE|nREa=n9k>v--=6ZFa}burCvL`E(KeIOz=nd!#-A_9{N;>h;^BUeuZZtPit>+>Z5ABcRs}X<)YeKaI0h^tG(O-7%d+y*AU;sD7`*6$X`1XsrUurgT4T}1(Mi_f>9Eyakd5~$x3aFY_rWAW8@R_uRf{Yq9TzdKqgJjOyZD8Pvd~c{FIfs*r<OaOKzoLT7jmz@s@>ejc5>ocs|h(XC?CWEb?_s8c7xtn#smEj7MFVn(OquNZ5)zHvUD|516Lzpj|S~t^p+Bo!WsULT2;9cav;Dzzx=hF^RASK<^|xk^DvsE{E?jrFBY0?Z8&s-q@R--s=>#79nGj-ZHN6a&2FRCh7e17`$_gPmD@=qOo>CwxH;mj1EQ(M$-+Q#)4#eb#cX#10|7Tc3Y|Ab@rDTUu@aZiEcCdK2ee$S;@czm!z(p>90>%rTFA{<y%SJl=i3IZeS_nT$KKWl$U?TZu#KB=IZ14Q+6B8rm%mzPUWx_S3M+cNt2xUKgZuJo&'),'Libraries/peggle3/gram_tools.☾':strd('c%0o@>u(g-760zPVmcDiz2;)=+Nmn7I;|*B6*VaqI8vp}cC=oPmlgZc%(z+7hhpQH3a1IU1{ve<Xa!Ab#G^F`qL_TRAN!$yL;NqKe?ZT<uetMB<438~tS~!s=H7G9`~2>mC6g78@I`)Q^4!me@8i|!cP7uAo$`G`+<wq(wu1?mvSzzCU2jK(GUB?FQYPk{nIt7jtAreL$_}M9Ix?JB*c|xHUVFA4hrRBeIqt$R4hFG5+Y3AO_yFt(nWSU<9{(eM%3sNErbt)$=i;&pW3TfS{#8dlS>S8@CNuN4U=c#nEGnMh|MOF@Y_(K_0g_*eUPgMtJoRi`%n>W4=o5+;ESsXgRa2^-JoPpyQ)E7Z<37Q0q+Rb!&(xg(8wJuezRX7D#r4WNXHF6!!54g+0d0-XdvaMy_(yz&<mXT(31HljnPAp|;g9$x(Rwhk>ISWhIPfv#ikE0=h`<2{wSdVytod9@yusjZ10;|v@Dm2{T-bH=JV7^87x`!W1;1=2gV@$o9Pt-^g?~v>g6WT<f-%K6I?Fr{+EL)7hZhNAgfS8=@KyeT=mp0Dh{Zkx;~w-$;?me?EKos=RKdsG!a}$CM<<R?5o<9z)~`nGRwE$4=yd}&PHXT-Sro+eI1Y&pnsLPjF3ZVf$qJ(hit#p5ByZyQhu;;)TgB_U;{S1m5%4DczsA=N<Ny6>OGb^Fn5IRVQf7@wJX(|#^o`i0H#-YVeURV=f1EPS4Zf{R0}&!sb6Q;|rFjw{`?L&6j{{{(HRq_KmSy?JW$W=_4I%!62JAFIp=6;%nY2+F+8W8^*P8OBXsm}dDb9EV?J#2udSI(dj<&63v)2!x!?$LWQ4|Y`^)Q)L7U8I$j1S{CVe=c$@SDi;`=9zX@z7rV+irCOKdg6~K_pdpoc5_C-i87_&%cH$ZdE%q963ZFuS{%XFs3hs9RUp0m}~?|*C9z~fF-Eoc`z<lo~ss5V_1C!zK~|hbcxr`y)B$NN<{1XJJ@ZLXoMzO>YteCY|r?|`eM1FgKb*{n;Jlcf~>^kL~yxMN!g^#bP>dYhk=yV`<R-YQAs+e;m18cY-CdIamqb+5_Bm=sEE<`p)Uw%c@>qAu(CvnQt!mOXLB0k*Gh$`Awn(GQ;<a{YYmAChau5mTutrBv+{X1>=S;8FY!%gWYDb&c;4r$WPfF#naQzqVp+|45m3PjHcX{}8Ds<*R5HfY79#_2l{9!&l4=-4U=0P}SHT#o5<Wfkgw!uUYULw_g9<pm;Mddw)cKL;45<F(>c&K((|B>+c#GmDge480O@(s->-J)Q%KIto$O0;(Dh`9dmwUEWyB*AA!;AGj;yMN`nJ|;tl2t>fzrg>-?^?STREYHHeq%*onk9a}sMHa`eWBu6kShs}SeGI*9?K?avxo)Ql1Q%B-C?;dl*6YwZlv4WwIq~eawBsqyo7*N(uPPWKm)X9;~x^hs0fP!y1EqyorATAH1y46Sy9yKctf$KkSEx?AX4n6fpPlCcv2cq5^<0J-k@|Gf<?ww7~na8-|t1OxYg@M|JS99L={;0wUOEFb=$p0z3oJX^#1u)JJ22DPBp4o2u0iiJaB$k7$w7kFtW;D5)-n$GL*C^P+;2uJvbdGCOKMcAW|df&UJ#Y9tTET72FEZXCx9xZy*&K2t}ZB6~Nofw3IS?Lw8XDY=&izIks6r`4&hL4Z+yQoPn&<heKlaXF3e(7n~Hi*uozSL2dXE!Sn$w$l)aGuoI?(E~)M^-LQcBn&zMHwS&l?u1Bp#cG(1;LzeGz*E8D+qu7sHGf+AUDvH=^Key_N+G~r%1M;V$cVrLaKIM0_M{&91vsA=kFgmSB$d5d!Q}50=f{`YRcpa8M``F+j_reV;Q;+W!Z+-t8LAE#CKiuz)-9SHShV_mg_N}^$ne-19vW|y6Kz8$azL}gwb|{h6c!^&#9bU{*&}SKn=7M?hkdlyz*nL1!2hEbWN-eC#E>;Y9`hqWN9s^bDKPJ_S5G}BqaF3vqE~-rxlZWB@^fL@Py<Z2?2$^=XuG>w=h7Dr9oBSmy1~kP~-F`|6)T}`tc?I7$`Q>5l$aEvqh!jceNEU#>Wld1KMWUppOrff4{D!tlnG(~NAOz<tUU82^u0_>&x5jBC?MQ69BE>0!6biT(*8u_Dt&B5B<FLp*=L|4F)ff}3Y2BA=HMFG7=Ad9Y0S*dG7l5PGj(V;;6NElySvG4^R$1p?5sIOt4;I$*6*AmYdBh?iAq-ZERMGCv45`-F`3+(@#~B@UB$7LQR+Md9)y!$GF7*=2iBf;o&6ivm#bfn;KL9BR2_dwsSqkYWw3R#%iFsX|hwXL(yeIx;3D!U3&-tIpE(_6o>o%?mhe57g_+=bd2*t8_6?P8jsq_xp;;01@tBb@hGs=GRJ7yP44DM}yNta3mDMX8i=BA^$zTDBw<A7DZ>8a)cISkJn$8&za^Wn=Q=iZ$>a&+gzFW;Lhl}g8*T|dCqn)j1E&+F6yu^`C&*QKZtw)!#LfDAi-_#8M=_(G0jzeQHxKhXuIbkr5O3-yyw0wQ|qyyhO^o0P%Yns65h;HD7vyts_D?Oo<i_&w|0U4=+PkOA~dWym<JN9Th`?V2F%VqqXHr%Urk9G07)E|J(X1aYPwvxZld?<#@Ow@)^1!{54#uTInBlGAlOJd=gB#sV+jIs`lcJDe6h9=G=eusXLLR<L<=NSn-@v#V2*LLSPLMCIdhQKZUknx*zFu-yTbDHkXsI&3YMG!`nbw}c|<h0v5GHC<&0!VkEEFTH#0MjqsrN)w4rK#5#r>oA@U>lX@xHa7!D!i;a9ENx-V>^!&x<3#=t^5gIAJXkzJ$LJ{1)DR@)k_tPn#CIyTmGZ@4@2I2WT$MKy)hLZihn;1K8if&^#INwd7Jr)5FjJVoWZg)4#4(U=WJLbB;P}at{;6N$4-C%vKCypMAP2g70#NX!qbpxM;$7-j04_`4s}Y~@EmyuQ+fo#e)>YvrDB_K}E8G93p*&QShl;YsZwd;&tk;w^MOib_Y$++kT7@U}E-NHw$7jZg=h*`nmt`q9N|kPxsSBhfaqZeMu1Cujpk~M$ZGRd3(g*SypA6lTxNPVnoM)ZPxy-u3XX*glW$FTH+2c!>WhrW75C^br72?Oe9)^!9?9Ga2rEo!>W;&M4KO8mw1FXmL$|3j+(il6D_{OxX{t8Q1O=NR=+AVpt`(pj<V(V{gF<p!_L%jeIRp#og7@G6T^8ql&n&OFKg)0?QDXY$8-YTcS!~*{-zk}$Z*9pFPzVXeo75Mkhd;h-j^(**$27k}x_4ccsg@p^QIzWgDPY;&%1dpwE;J8x)*iD*R5U4(MY*I<ApCV`L9XUK78Tk(hbtXs'),'Libraries/Compiler/gram.data.☾':strd('c$}RYYj0CW_WS;dyKE!fn?ME8BD6)8d8A!cg@S<HcGqjJoWu=LY{#{o0#dYc34}mP*1<qf9+);@=x%^ODGBK=NU6lv{l@p)e(xgX59~Q}=5glUYm+p}*z-7Z&Y3gkH8b}8pU(eud4Erj|Nf^(j~qL3-1psq+;DFuS9ZPa?zTT3+kbc)eE)4^=gyt`>2tW~2P<_yS8(tz;ru<QKJPek)IWTr$3NtM+!0h)ZNRg!fPaYqmf|oTi@{im!+0!&F*jIoLSTnJJYhiI%ug-&<zlwag8K9RWB&1@?;kX9I9RUq`$MPu70~e$J^n|Z^c*)py}2R3FIV6|2M&GYA3XGN2oSL$a0t)_qR)J0umCUvrA*%MINZU9M4uclSMrsz6HMH9-pt>4#>V@G^LZF|gWJ#Ca-}3d3Yp5_7g-qU&w8Q*fwF~)s3SM;jv|KL2MfTA*U7Mz`$|Q`=KgmKs)NM}HlRLIOpr|ebhM)jCjlnW->do$P(RTtpDp`+nOx2%B>t&P-w+K*4qGunpR`z@j1{@)>3@pK#?tsx1nS<im%h9%GY9t<#eOQA=@-x-e;;;L)HCIQg2XlT)tmX+Gp!(^1yeyvpm`Hj0R{5Jp<sLp{yB4+K*9+wf9v;yY6%g8UKBq&BUjna>iLR6I{V0QD|(S-{4?u<UaH_mJFa1Z!z|urFdC#zMCR&oT~IuSa2iBwFWchr7|r+Si}=@~LjL1fw3g8VCVm-HPUP>cEKg~ci9xkBf<Z>{^0!>Lr%M@BciQVQl8#<Fihe;frJvCwdS}K$eJ!M=)KJ(l`4~{>nzgw$`%0V82plJPcuTJR8~S#*Cn9bPx5nie-Xr`aTJL*|8W^vp{&2)mZqDW;x_i;T7#i(Gs7y*)xS~db!nB>RF1A`R3f^)C1n(&~Sk$3H%;-)9UtS0r%`~-yr-fPbP-@yCdklCyXxx*)QWs|*sdXpfNhe7kn4XfOknDyX5%{Z@mRhHzTD0KJ0H!6Na-|zfbGO>fg7I1HC&w(B?q+Fvd>;X7+_uQ(rOhG=nwM=<wPgzxe(pJ-u#qt%%G$C&SjpzO6WPwxpTl^aEudhF;#d+SdpK8yHzMjN|8i~R&HVLq#>WVdp)dSGDQ~wkd4@v*D8;U$#l+hQGv&Hc{}7@KA+p^CcW$?zL4a=MD^vjY5g+1;2b0rdIZ^yvzY57op<i%w{VJ3>(Wam&v|v(cf|+82SrT#W@mE(vxq^xr<f>IfjGq<m^auOBI3@r*6kH4yT*Ay;{4BuNV%A)pOKIq|Zwm_cD<tvYQp2*HnYmCrij}28To_i06+z6SLoAM87MqU5L;7tYrPRx?Z_$my+qxkgfYMZ*X=uZ7<JgL1Hr&G9FfgK7pPnNrd7XNH83>Y>Cabi9wt_8=x$!!4&N>1K;a*hH-PI|jw2JAPN?utwRCDUlIrZ=yff{2<h*eEPuQN_Clz_CKXcMcqAy)sj#OiUx6dwt_cP*t>C#hL*5lKyIeC6C=UzTO~azY4FVC?v?!@+bwvOA{S^h@op)zG+hpLA$4&eS>%g%4*|T7_eS`QmVirf1LS>d3$u|BS+!%jA3MAXpg5_hw5z0J5fZ=@HC!Qiv_jHaodBcnShHWo;EuMKjf%>IlH$EO#6~!RnIsrEKe*VFM-4T-@zDEc&?0heiQ6mX{x!07U9GGY6AIZW#_rdcOrH7QJWj^umBZ@5z?wDXQ~TnNA5E#1=S{b{;GYr_Rf|6U8}S&3<k)ThN%aC{Bu_{n{exkblYtZ3AO~*uS=D_S>>H3z==a3tq^^1ogLvlQ_n-O1P?Rr-(`iluQ>q6$r%Y&xN3$g`tTSS&leRxu;JJmWQ&XazdO|(06>|A2R1Ux)CtJRE!^sIR=G~L{Us!k^+@HihE&fVmelk&xDIrS8i0Xlr3i~j=H`|fu=p#SbEZc@(q*)D0iXUgYq4ee?fTw<q?#}X}n$81mltv8fhjMN^F9=U&ra<)L4=OjW?y`Y=N9s!Gt;%E;uASXX~iF@CGt#UAl0N*|pgiPj3W$Qg}$Py$c66*UGwKOjfFrM~@%vW8)ir7Bi)RvOh?NLKj=mU~Y6u$iq4n@*`}q0yD@CWYrBp^Vo~GgOXs<^OBr{Eaw21F3`0j%~|{v9Ap^>f)wS^1l!4WiK_eTeQSNkK`3Pi4Qudyb#vmnt~}VzkTIRaGj19$FZGExltq(rwbDGib@eOdkzRd1D)2@H7-};)oY6m6VU}i8#I~OJD;bT^+5>q_s;AGXOCH)2mT?HLL}+F55f<WuWr>V&CzBYxR0?WX^#?{OW#s4Pd8-S~*hrn`89*^l2ouET4;BhCnNgT&u4O_jl?vS{jH%tGEryPuc|NGk!ar@bbw2E-5vtSObOeSW)uA1oOfqsPYo1rmsxz+J@&UtTAM!R}{?&cK>P|P+dmx?Kxhvf@ni@U=wH<q~dgfEC{vosDv;8|hNOyUoE;iF$!Wr#8_^xPmddX3$@ZK)Z&8E7jXGc0I`;sOs6tV+06C2A*|8Y|r%a13Z)Y2(zLwSLWK+hE@*Qs|0RL{%qNhmi=_c)Y`Sos>tKd^F*_|^c7d($V@z?xAASPy)E#h1hf`NAk8CN)-~7O66=m_vy)I-!#2@`%i!%_9idIaqbV+?rWhV3Yv;N5nYswFGdQ=`(Gov#ZEfw~(PoXFIGmcaiitjEL34ow@;1&u$6?8aaP}?9x2);jw0<m}Eeu5Kt)sB<bKG?cpugyevxJO_(8kM1~{_<gjMuWXjp;*_cZ*dx&v{u6cCS7)vo2RW>>^M@!KPpwER1B1p1p8~H7R$l6omSHO(qtvkOeR1-V}<6_zkVXQaPuYHc!W$q$qM5H3}@e84Vh2~v^*>m9c;;ScxJ^!oSN_(Rz$U-1n#<LJC0*@%~!N*b}xYXDiTzR-Xxcu$f%V6<#F#9N&s0LTSz*n9^Y=p1_&OK<{4H|cX2hdyqnh$q?>%RDAzOe|E#t$3ItJCYXmG#>9>r)rjr>g6<o9nf!>r)f!wI9}Nv+K1R0P!5m@W(3Ti;%KyB}>Kp>>Z=0<Ry0>Owm``^=QSk;GlUaXkJEp_!7L#@*<Q6U>cz6KUc5)T)iGN?gx$U$mgS}qP?MAf%F{m^!Q(0O<V7^EWYZ;Pp+ULbq(L0vKe-AqF#Kk&L2xu8|qdDipK}obQv`ocXggA>|1D?*n=ucA4M<Z4&_HEt5E)J)&++aW*c(u3hp0l9`4*Mz=LmJeF^0SZXM1w#P3+dtvosIg;ynU@9@0u;VtogY=kPhDQP-ewy{}JoMYKq&KAXAK_8LL7b|Cdbt&Ug;)cd!@{HItj&5@Nfoy@&68q$9u&8W_f@n)KMKdQ;c9XwtW6iF9AosjZwbZxc4rPdXSyqBneXbHDxwx2|3%g{##%HebG)9S8X<0jTu*VT}8_Un1hw-WBg}0)VfD)_Ckjg1lC_EYO(4;R|yaS#CTnMt0?&9&%lEjwrNk0?C$g<weVQe(_lAm@+Cn{1kqPV$K(2;BwKWS28dkX?O0Hq=TsB~+K);ZD6)3r6393PvzEK}?DY~Wo|W0kIU3*8=H)(WBRk<3}o(}ESAqTQ+qZ<>C%(rJ_L4w2upN%GxWB)`WdFVA1vQza~8S)G<<%R(jFdSfDqh||)t<}MB=yt---80ZA8C|mB!6tkg|5aUB5f@tUWoywHBS42vo6J(>QoVs;{;t==3{(zXY@PKvk;6MqR3Xv^wLu$a-7B7GXKO|eZT!Q~LMFu~nmU@-uB2I3q+~(=;)8v=C$(lw}djC;qCNMMECf;@qW!tkkkI`tN_fc7nT#iB;b#e4bj|_BH!g_BBBDxvM5BKZ6G;uiD*#+@^Z86Owv6+-9&?ML&(X0&TyUgft$xuT`u3#%FyVmb_a)x>jfeD^L72JFwS&yEm<od5Xq)O6}%SoE)<?QDUU4k(xjA{8!*kwHwT$$i3W{Sn!*?kE`-ecGigTRiBfzt3uQLjSs?Xf3v10-h@Go@@n&k)<fRz6V442qK#tY}|CK8;S?Q;YPxq`VQr&T?gFUjo#fb4Tdoe%PTddzFMDzvxhdf(L_9uoyD?`)|bw8GB2t^eIl=D#gSGcN8K8WP`Jz!5Ka{!w1)==Y-yXj7+!rjmgdPJgak!g+k~X)v++`i74pk(;J-FHZe_wP%&Hm^h^F$Ga+-tUlyCAzw=Tj6>O)QOejS3{a4Q$b>B1^Q{WNc6Cm)555AsEoqRnB1Ft7dcj$+x+dR+v&Hn*kJEFk'),'Libraries/Compiler/generate_operators.☾':strd('c$}qJeNPle82_J7vE77ZMyK@dz?fWeO;NBl)j|*xlk>Vc?iRfExFffxLX8ces70G10-++v)gt&(#Fv6n(Ld(DHnE?fd<DKhpJ!fn=gvK>_Q<fa^ZLB}p5HvPgkR+2oyWc)j)S$sM>{*Zx*dlQd%*4M%e&1sWqtW#Pde`r%7|@KN|~6`(MckdCJFi2idvMW8c0W{bLjAq_IQG?!E)JL$#GytalkF5%f*t1QyWN6{#!4eAokA2+AS#aP!^!vhO!8y0_7Jdcc3gmxeH|($_kYGP#!}04azE%M^HAPtU-Bf<Ko3qRxiHQ=)wP2Hf<DJGVIReOVG_n`5eCw8b-E<e`xgJUj#=%^K-sR_y~W^H_6eCHdST3!e{wNB1Q?n%J1+|Y@g*%_$&T^kbJtoC!4ll@+!Z9hMDKT^J}_tHBR8CTdhwlm_H7y>uyS|J(hTR#;;RruhrDDkFqF>f~kbql%4X<#7ccV(&z_|cM%e0l$|@zV9QyQZj^8F3oN#8A2_BIJC#Q-flgo#CJdfE-QPdtNXwjyFrq}j25N!t=y@2_pDX10O6h)Koh5!3gucX=;t4cEwT`HftkI@2&Gj0uE^X?jZr*d>G7CN?VWu*!F!fD2Z;~=;c`6o@Gpt0y0xeeN5i?>%(0+>l%wOn9XrMq27A!3G1KFwkF$rVvc7HloNWhW_Lbk6ACwA5@Jv(_i5{d2KzI|6!7T2NQ>{yl+x_xEEXdW3;m8!ubmsI7-%J;IC{2G>qMPLH-rqo({P$$~(8K2<S_)F58NoP*Ev?1&ES_A2l=Q=uIoZcJ=o+%c}ZlUbac!LE$G7wK3|NMk=u&cebyB&;gAAkrYe33r{3n!8(bU$ptzA6@67T#_2g0R?+m1V4i`P;<oI$zR84jn4J_Yr!}vZV*mml5=YAP?NDGhAX7au8az>&i#c%jYt#j7$vSNgbK+HVv^vXfl!#n$Z-c)KE`h8Xiv(Y%h7mmnK9DrRehiRovHERQLrz<paL~5Fp&yhmq-)LLzN4E;L2lFYqZu_$~f80q@fgEib7EU=~D!Ud|ip@9{zd7aj|I>|kp*Q43FldKY~oqUG-Z$5r@c9cH`gnk!g}#wuXxH;>=^@%QMPEu|fcL0C_Kk0%Lomd}_Y5W^Si&_lB7HAQRe<mLL}QvDzKl;4^u_V*M)Urk_sN7nT+a1^MW2IJM#^Ijq32T7fA;TW2NzZDIhTiT$+W&(HOLEja6(*0Zf$y?lrWU~K&PmcoiMv%P=qhflS5&@O?Fag@?2tao;R}hW&`JyKO|0wbS+uQ`sfI%9ZAIkU0{(y+23N5B$f(ZyQ4H+gOlG2kZe1<;~07HK*_`C~yog9p`+QITFVG==v96slVPz9hlL)BWl#18P3G~%Z^T!<;ac;}bxkXykhv>&!FRkcS`DhF$8KSCf?fQD)%22@RpTpaMk0#o3O>vcF*s3Y<ltxhB$18J0TKLNrhT;j7jOIqN|dXnU55jid3o?Qok=vC>KGQA$zOapTTIgRG;`oz5uOcS=Pf3Elhd(YrOnNtwK<4m!lSV!OrJfbOu4aJ8Lf0QL7EXJB4Z)-^j<}-(g6<#aqyIhC*s<WFL0j&pl&mc?c3{`t0%9OAHMpFV9(m6vaL=+aZ9p(bSk_d|g6f04J7_NZ0;)!jwxW^`@Ux@9Mhw`pXgC<S10=Ih8c|H@s3I=;_IbAN7h(>ix&4+3<s74H&Hv`U_CC*E3`E;pZfglYcZR&H&LDE!C_dwPpGN~-IdMsOXz9~ZLcL=U9uFj%zh2GFZSERR~)j!WxZIO^d>l9xP*jtdb;ygL<)y~@RWcc8njm=+cN5jg0KCL(W`A=2Dab+0)SEcUwi7;VI;ivhGDg4Uzy_@C~ImtG2Z=al+f`PWuF;t9ToDnVR2Ui;0VbhjXrPM~SVU>JnFEj!w=F4iO3t7vM4GshK;$J;O_xCArmJb826?2X9>#!qL%uUR5TE<y`oKTK21c3x7xLcV_V?>w$ySTN5$9;WTsv=FTsn3WlDO|PQvijWIYiS~30`PivG^Loq&mO56Sn^7zF2mvJ_`5qLGx-uDN6Exkxx^qX0R|PO%8_yi)$v`x;C7u}IFsS@9w@>s3C`zU(^)F81sy@&XY@3QHiZX~6>84M<ZF1-7B}XJIZ>^#gw|#k^n`)ty+A<hMh`EFBV!$1ZCG939)5w}B{t#Ki0{kzc>+Uc`}PXH-@|wOmZ37{6sx*B7mDRtY*s~wIyD$}`77+|Q`mWAtX4Ah%|u-(6tbFA3@j|RFz*^8`~lz6=GZ0Clh^)<IorS|f*mt}U2il>rI-jqA%Tf+rjka5Hysz_5-nziC-7D-I@w~zdmCK}6(1V4b)Zq51XZPAF+YPcPi-TG5@|Q9(-37UE3d+*k({va*jaWaPR^oz&ww3{!5yp7Lu)j80(65`v4k#}!6OJJ$V5nG7-%n*HJFZ2HT5+RuYt4tDP<uaH(&wz*|D{)&1pY@pB|4n4l%zs!tyqga@%!zz-D#3<h<Ja04LP8fiV99N|o#y'),'Libraries/Compiler/operator.☾':strd('c$}?PTTdHD6n^)w*zVIzGa)!pRmqYoaZ8Iruw@gf%C%M|ULp&#YuQWWDvD$X5N>I>7(xUX$b~imT+=v#(m*Aq@A(bvV;`zW{sTQTJA1K#hc-1jnq}r(zH{bW2GLPE6^?#`6oq|t-VBE#J&J;mY^Zrd>DRM^2}8!@PFn9vq;m)pB+D3M!sS9?)QoWqq05qA!Z_|j7pl9XYHBuNsEVFptDepM3$1#lKM<rNv_!|+T6z$zpg~>Nlw>Lkf~`ZTw2{(sSK1Rs;)<Tpvq_n$nx)J14aPondnjk<gSkNP-scFE9MCd@xklg764MMSzRx$efJ`ixPTf|KpLFY*isKmH2kB5aszgI|=0|CfKBd1QI!&L`5k!Z<(ys`m6N7!pganLbx)4Ct8f%Ud@ztmuGnN%Pb^#jZ!w6lZJE-keL>QsRus#L;W4hg7(6Ta5xU#o&#{QVLk&qa=8ER*Ww&@X}o1kwvh+LRbN|QvWu$0h}60%iEUrGKiIbM(MDTWHX!Q|e3LU)+?Bl>`RA#ei}=A!M!99=?~T?Rntyx!RniSmf9(ASU~=K4!>^3W_ynp@A!;dOKJ_tUqlf30quRL%7luzgzm+1z^eakexka~*IcAU#WG=zHYV9r{`cg#$r5F8Kfww-?LDWBxc!^&^yLZd$t-tLdDI@|X*EM(c#Z!$mqz--8Z>?0;~Rikm`Qk9X6Mf<Xz%AJ?8t08Ii&D}G2msmfT=bb}eK(;{s1RN&^}K9+!v`MSk}Q=kt~jHj$fJUx>mcT~eEA;n1ar9qy=oKQBga8(ZhLOd?iKBiON?6u2^G?>Iq89l>963L{}r$XhcZZtAP3!LGHnp3lel~k-GO0-BIyH@F5kh^*St~Lk}#@tXSuoUS#J2zM8ij$jG!LS%vHA9-MngJ<HGCZ|37CeDqk-l;h+w}rNSU!`zK{96x5D6<%r`0kG)|nfCOUfInmP9ctgv2W?WNVe-<yxh%&vKS+u9xin!u*-DHQV0tIbwCEg?RvFGs#x{2-CaIfRAx7+1(8;bX?CeKJQ@}pLJP0{_n0j&V!v97J#~A3ypi`9+fsd+IPkr?GQkSwS)!;N|C!z04Yt>9uD{<_@(+;9U!Yl(Ezqe228P%4&2r?XyHRDXLW{%P(bYe2i(sXN=cU_KPGqMnB-I=WvGLe+>H)&Rq(;5-~DVB^QFC`3tfX|e=Y8_FsDc_#|vIA(8rB=An-FzEA<#_uh?yb>jHGzs=IamfFKB^SV!T#ehFgS8kI!{T@YP@AwR<vK8Fj+gUvW=oJ`vo{CtvqLYSDBJ|EJcAHcwyqKAz!k}gZo_k9-)!i(eM2@bdf9yPOy{?AA;t95g-Sld6C1eyYxmj54M8f!kE3TzPo{RlJz^hmZwnbOtS!~3&%mlWv+ofFqsgukDVm~<Rw(}4Oz4xiUXovX3%v-<K|<JW!lu;h8*d1XlanQ@=>(4^WAV-bd-Q?5K{?@*r5F*@(b_pE9RWnrAbFV6=ej3n?b#B}k=SU>eRk9XQx=_HIe^Z2X**o3+5ayPUEIOA0j2)beC<%aaSEtdVxZ9qg|!{>G5!dIJHaiWMkJ~SL&jn|KJ1~H~XPvlbthCaVw{!S4$9<&w$3*4pBrE~|Kmk}6e_MM~e>W}=+QKU}F@0E(wN%^@{Z%agphCAAVEElV9%xcwKT`*Ulm`j_dvs<-Fd7`%W{FS-$f|mb$TiZXJFh?JL82wOy&qqLy&52TNfA2NW5zsNvHqZ{xE>Ich7oZBzE4cqllAU!TeXmDa+LX3XcQ0<bn@A6-IhLEPT{n~)-?m4CNdCJpRjaHlLajx6+U-qq{IyvgF~<+hhc9cDaY!sK($>{&bJX?<%O`)B2g@g$O!QVbC|;?Xh;FluR(oTEZ9xA018WG3vH'),'Libraries/Compiler/node_types.☾':strd('c$}?Q-A)@v6u$RUtoCXq-BJwgjU`_=K%1%#wn!pHO3`Y8g<7?-yI$Irs!9#zuPH=;F);`V#x=nLA+@Sn5+&hcq~7!`c!41G1$t(7X8*iv?538i*_}D_oxgAAoIzxPJjvd>gH)A1eR?;W8N08l2+1XVW+tx>elTNb1=TDT^JN(;Gx_3#mM<f$AX&y3D{Olvi~2EsgwXp^T*7!fh9Xf--7?kbqEXPy{{yaA(hbcl8ev$raB6t?lXT{GDt%8KN{^&QVH-pHYy_0Jn<7<D=d45$*0xBCEP%$hFRC(C@%K7a5}VSeB{EN*lLK^%)X4_<Nhv3h{JGVi0<p4Qf)@#%K<11rB|ipbx^l}Ft>Q#Xf*(R;i8K>Q80%!6?2tDgy-r?<5$C3ny&vna-Ii*=Dji#VJOOKP-#13i)Tzyg?zkZ5h#N&7lRdJ7z#xpJ_ayO3H!&LkVU@hHEx~=$`ML5J_CgN)V-U8j^k?YioH5I%AN7y3g;<QLS|h)LA9<}XF{Mc&Ai~|m?aV_|Hnqtw4G}D+pKoN2JSDpj?s?KA$7rHxDR(o&NZ`TrIjJOIsFFqIAiUzftiqy-IToji9i<Zlp4LbM5@5fwY*2PEfn9ROlFR7;zQ6*^Z<8m!`S>^|$nZ!S#W9_5H8Bmp1+9z>0(0_rZoLv*rnZ5R*291PeDUmhe`6c|PvO5TJ4RQ?X{gZ^vK};=&u{zY2b}pm-~6C6U-8X<=*+MB=0E!HL9vqkZJq}L!xYw$g`+|Q0jgcCZF}R=h=|K!7s;e@O_#e?g3VMJDIp?!JP;!oK;8g=j9p88{Og?+kPjYa=j#yIoa)STc)lddXu#w5LWJKvkQn(Kr+Gj!(5@jnUyj8ThD)jCl0JE}=vQBBhF{9{p%vjni%0x8g4@6F^;VGMp*h|pmmSWh8&l59h3p(#kemQ#Y)@zB3IRvC_;ZeS$j3%!b8IxTP?DYRz{NTe7;M}mFFmFRX&0ne8Uhe{o&q&b$!ls|jXY*i8+tH?P+Y;vx8Es@xPQ=s^_u*^>ju!yvbng-b*_ZibIjL-kIim;E1O1`Z#9l_+Dn{tD>P1f0lNhDVK<miPYYq7L9iwt>s=*OH)g{?D*;P;ilk<Shf+|jjo96Q7ACcP7--~I(hca<N{wPhoRRGm4Qm1zOPylDS!y4TPWfoD38&EzwjTs+7XjMp#&#+Y7LYdb_W}wZK`7`B2RZ762UjcKcQR0TzZalItphefH)Ngqkk3u(EUjUwYOjQW<DDA5U8g52bh|u@Qm!nG7H6Tg6Mb*67`j~`^p%FGcwUPo?;GuV1s7;_!9o$6k+j(<Nl;42D9j`5D(AU!{PcI&k-=kpUVzxOJcsT)3^gp8R3s;4%<6@pDyJ)S<LZ<?sq(|T)A@eAzje`Gb9?|*A3z&%uJ^0+;Z;lUuo1|AGvZ4+?uMs-Z8FPB8eA~TVT|1kXlZoxf5s?@`qm!ob8_kg+hW}X@pf3JZpRe~aOMGsk9(69EXSc8LGecG7Re@)Q?D*6YM%1JVp_z0HJ>wm>FI2%56-aRoExjJlmiyOh#JsD`COrD>?P4C8vLeAdq&xmvG?_Q|Je%sf26Zz-J}J{xoi(`L3oV2kNuuDZ4lEth+iA1>(jj|GG2|~>(69yD0Sbt?SZ*{?6O{kh-9+wY6rjR8ZkF&g6b!M^Zv+*BE2!&M~Owds134+!|u-Zox#34w{5fQS@^cLO5<@p0*>CVTM=-pwAfyfm!iXqbg(0OJrrG>E9;k(xbLRMK8-tvB(k>oBF%SNG5+B$aj7*vE{KtT4K46t^g%i;yWjdITe98Drc*;BcQWbWkufImFLP=Azy'),'Libraries/Compiler/tree.☾':strd('c$|$?O>fgc5WV|XEII8|OO&KH3m*arA0llc+FKM^X}tkU#<uLO6d$P&ha!P!K`IC#Rj5}EAUGfdhy7#BuGd~CQK6P1ZDw}f%)EKCR6ds{lfC=Y_toja&Sd;(-}fnP#Yw<@QKUR?0ec)J2lFVWz-X%l0Ia;;9}Mn|#<%;UJ^#*V*x$uKjrVX!JB=V<+B%+~6{eKlBwYe9a{|5~=y@kk<u5<X{U?d=b8)m-(8|i>3wg=5<b`}AUxMop{6Y+RCeP&$s-1ZLDBl~O@oNvc;gK2$+M;nqeHj-=Sxjo1KJaKA{X(9}Z)@mrB8c)@baHKQ+AN7Eq%hWC4TNU2(=cG{F_!k7>I%P78qJ>`1apGcFY?U2f=cbIIRvl;0EFl-?L5jk-Or9VfaB0$F1TOabG<5&0(mVzxpm^|Mx&`k7zcG_%PWdnG6MzrTTz1ijjmJq$BJOd3OoB%0&&L0v@`n`d5a_?G-Lvh=`!|Go?`{YG>^hVPP=S3i8;(*ZOT-BmM8LOW5~BW5&}_h)K=ko)oB_chAB$GbrjJYuHxR&M2M{L(<H@TZaGM^WLbEsQkL;U?=CJDHz~AIU2kVR*igi=e2Ypp8h|#(^-WtP<z=MV{$@i;6jY}pVNNtRr8=}t#o~;!97h=jJlDx_!!fmH!Ysd<38UGHsXH?-!C*L|T~LO4s8OA3W0F-}mN8qll>#@9jI!z;?cXhIE>btzsTsMZv4<mP%9pM9dbJ#Y<y_2#$m&O}XHfCjwZ~4Qt!->;+qR|l8^=Zdr%zP;EBT=osOrc@tmr{sgbnr7BsqTpev2kL'),'Libraries/Compiler/tree_txt.☾':strd('c$|$?TWb?R6n@XI824$Wt|75c23AOuP=l!{Z3Q8QWz(HBOShY_J3(Jti%78wX)EFli`0shqIjW*KAnH!FY(MJ*`$r&JS?+kzB%VR=X_@<Y{Smt@(t>`a#vkgtS_y&E~S=;Ik%X-7Is@+m{4X@%VLb#8dxls=WF%3Vr|(i)hfkXctv@-S)sYHOUzc*`XX9cgVHM`PZ(=veBLH8zZVCByNQV1Ao6)6q>BR>z%N$F5L`i<Ad#NMNYoW1h)4>^a)Xg8=As`*WO%6T>O+Uw;Tpf1?KN^u`=T-5B$r8EW=Ux;EI4UOh({wF!ZY|hVb3>BlI2Q`;#D-L(Cuza5dH*SAo1})Yg{ClmCRZs{g%7d7l|xvnoi0(3?hzT?MG6`3T8K&iXR%E!{$Yfo&TaYq(}oBw%`=@n52o@J$Pzdk5f{#ss)D*$&9Lq1q&FP1a?@~>-Bi#OStmhNWx&1%b&0Cm@d@I6gJ@me%m^fWc(Vw!+`0tZP<r5ux}&i6?}12@y@V##+xlcH1sxFzDKmFV2(ygvB=%~xofhpSODYn0CuHQ6Y?GGz)y2cf^>74eXARB)?`6jYJgmFNR=@jCOm~sW-EnKO>Gz3n6}Rzb=DFVOMlVx8JyA%&KR;TsyR!z@Pvp*V|CTQahp%Kxv}=nVtZ$ssrt{4g_=6g_uW?5U0qMkPa92y7Ypq1u(0O1Ffk{BI1Z8W-H;g&FY-xxtR<=ut#IA#aL?B*Fyr_Tj!>Rka0Kt^?fE-yX{l0NsbBzW&XV)>7CynC;54L=tr<%<1I2FrdGtX7rsAZ<a4r>8vA<Cj9}h}$&}WR=Xvyd>Z<=gNLQKy)hB%g<R2B4NXVWP{Q&Rl_$0Kd)QBY3)dFdQjJ~Y=IdH50rR8OhNSZ&||5<4+3u9oI59FD3uYDQbcJ*u0Lj8!4+Tna@w(N#z0n;OycO5EoxlcDVp#l|Cij6Jb|PjNC$2V;Q|K0VK2nraGFf*<KfE_!AD0{B~P9s'),'Libraries/Compiler/expr.☾':strd('c%0o@TXPi06@J&R7*7>dJ<3G2THfTW%OHr8vW!#+o|LVvWp`w6G3;(;M=^f0v5}D-Sx74pg>VsO!6A^8FOUF6xGMeb|6o1liJy>jx=&B{%=Abrz@#c$g=V*>`}Db=?{vfXC;YRS+262Q4Zr>Notf$5Cu%ju+&Bt?T6{KkJ^$UXbE+QpnCCOs^*qm)lMfv^^48S!;X_liwaKZYhmOHALGA6MtYj?md@(vb1Eby?W50C99nY(dG=q7k8MHgipw{W)$_>88pLi1^4t$v6D;f703nwaigSk=_#yY8?aU6<LL**(laOCI|8~1QddIR8#@pF8YZ%kBJ#~Xw3b=Yzn<%Bmk_$B@%zpog7l;0f2H~EMA<A8qzYrX~X>Ss<h>kcsU58j`!j|z^y;P(a3Fo4{Q#r~-J*$Z2ZfQ|ddI_<!NjlI@9Q*&XW^IFAW?z5|xub>@+uotLz@X=q{T<Awtt$=F<3K(P+u&1Cu@W=a<Hznv0;-LAq`L|YqeBgSS|5XS!m6z%GP~yyYA}4lQZ8k-|il5fJ!(yj`?Ce~>1>ERYDHR|~8+=nfJ|_2qu$npSB3JG#K1#lHqo3OY@e_n5>r0PckadhE_ow^IuGqydy$TUVl0S)Qju)6_>HGc5H%s!(NYj`SmaDJcMAru|D1zkb)tDy5`cDt8<XFc%WuN_@D_gnQ@ESy0=l|5A9nMWkryMblN)Y}g&FDJC+{weDs9AKO<thtn=k}2dZSYG*ILul(!cU{qj$7@8z{$PcrvRI20mPR37eJ_cNcIzl&>nD(f5(?;JV{vI|45Qv;8>Vu2J(Q)p?3Z?;F3U>zejx0nCJ`Fa~kz_yAwNSI?dMn2TrGp-vZ}%3#C%Ie4r<vuesg<r8zGvyCprzxi_Q|g}SBo97tQGB)H@+q9$i7fhNxLHHNkBPZ!|d5}>korjKALz00?y_CKmH<X9GL2df_;1-H|!?L6$)LRd5^U(3~*S}O=5+`6MlidT14CG`~=gBZs=;mLH8>=L#RE@md}%ILtxXp}HI*dL?!c4IWCh;<0{E~!-lCNYnVjxvoj#{#Hh6=^GF2TV-N{r7#>gYx2-<;6(8!c<~;GA5SffA@m86$fV$=P%O~_&Tn?nqGepy#8QS`%)Cd3sGAtacM+==|&XP<Dk~4hoN#XX>Ff$nSs_S`(tKLU@z7;id0b`;(Tq8?;mH1!!C8BuynvHtR8mM2s=-|RReZn!v<L0u?qhE%bmrwoohEz$x7>_&o46N>RM+h0$V$a7kBQR-;=-~M?lu$TT8a31+KZt|18`b$!4hg8FrNt6RTzRXYP;d;Ds1LEwcY(n>!ZZY58<oJ%?hj&lmYq@m!|oC+aDHbBY<lJ1hLU1v0Ggt)T$4VDlto!5nc!_ek8Sx0?>qqa>Zo6jN|UdVHY9x00lOnLlA3eMT%bLNHLM=wYq-C8_GBc&=e{BLi>rq{WURO1t$aPKD>X-^@j(4no3dwwNmw$6Tp6=1Nt9t*s%Ow{!e^{vBEiz5%zg1#^G=My5h?K+^jUX1;8SNTGh;a8X3*tmU_HJreEn6)D5INBt|NWzoX=$?|F*3W_SinD%(l#Z!V>;VV{DyTZS)qS_U{z89*M?ny@lV4=3^IYkxm91Co+Bfgv<1OtBMNCqv0PC;%zT|kB0J5l*~Djf)~74EqSygwCNJrwZmZ+wd>+%}AH{$DNd{(G%3C{UDzBFbHm7$8tQ64AHQ)8}6v;yflk*q0fxl)S*^MvR*X8e&bRM{I;1n!r_q41uEMG^RC(bWcPJs3_ba{em#DS|pL^8_FSR*yI$<tA<4_O2@eQDN^lNz1t1iO|pHyb13lpoc(s)quc4SH0gq7VYdjgEJ=L6Whh>Iuk#BC!)%f*>|t_+2gUi6KcdL<Tf#&HUoXqTfi71D>`G+?bQyji4pN6eez_WSO($A$&}unp4Wl9JMbRDuUuc9y7UI!x#3A%xbsp<PVXCdX#?Mb4I$?H}z)UZw1!ubvvXJJ$Y8CMZ_1asQpKqOIDLoP^G)SQ#bD?Nu{vwi-d@H&SN5!-eKQIm7(P{z4WGfC~KkHIoC8tOfll4Ez(O9e93qaE)i6cKHKym@d>|Fd1)Zm(psRii*5u-x|am!Ha6=;-)ydvjfwMaI_s4CIva!LzY=rIDyaXorBh-=Y%J&}}h_$+rCueuL=qw%s%rv#KXQY@ujlp>7e6TB*i@7dgF82a{3tIzMUQCOUO2LfKzk0J#?<(`<GEnB|8R>c6`9~Bl=b^~tG{+!`#CeK-c5-4jFaaYLEUb;D!=Rly%ZCi!ZX7y$HB8Z@z2^6IIg!DlWY%a$Q3ZgQK%##kboXm_pr_{UjS%j&#ZJ1hxL(Y`k)}CfPI+d{?ho_RrzC10-tB_gl4P5fQJ0!&IEJvwylS$k|`_f)}7PwQgxA<dJghZ@m{*534Ps%{gc~*F`T|X5DPTY|d*y(hGs2+oV9_URtVOTlPdmYp+9+CVN;V<Ll5L6#VeiQ=t@)S|EiBz!^{Lc1>b5);oxBk+u>JliNE_SS;nq{5)P1}Mp8bx;!2{377Fv&||S*8yQK9k2O3S>5Ho?)K%fD<Wx0K6$4$r_D?C_*86*?a0Yjbp?4IO?LKUf2Xj72T`IDG8LQWfx067x}G;ish6ub<tUo7oDp&YrSsJa1%goUXIFkTLy}8@F92UW7lQfC9}!t_iN9tZmhXk0-y7*@#xw{0*Na!vNr*l6l;`GHKj=~Yr$Rb9G%`$8rM`(=RkcvpagIyr2ut=>G`_JLNbDLJE1E?=qq||(sPRqwT~9jFUh?OO~{>;NTsSejWSP~8|gUGuS^7`&-{yGY*NEtd4N*(%f_j5vAV57;yrs>h4AJk{|ryJ$jIW9A!lkKBT4-{+7%mXTBI|1rN7R<GL-|k&X+uSFM6DwWCLXc!s46!LD7Fz(4Gyd&mB9ctU}!8H%aW4@8}L<M<)~GDt};2jH~=>EAn0Cw}-x$6{kE6|Fk&enY0}2K)zJ&hng+C69i^#DHcBx)15{lrNY&>hgdysTTL1=4-xtp<>aT5wwGuoJud+eM!K}@ZYbgRf2c>hDB(eo7<Lcaf0!G7?~Q@GvqmLpqIT=<`mj>U+NbAr^#s}Z)5(*^6{`B9xPm}g^qt<bs~7)8mvLxm`f{5v=Ll;Cy*g}#xUJJQ`bJ_HBjpxfXNJJ?qDY7kR}6fYouKcd@D7OXh-B6TiT?|n*Q*!'),'Libraries/Compiler/lambdas.☾':strd('c%02zTW=Fb6n^JdY*#{>p<84p?Moy}r9ewnE>WQEgJoGJ*%S+tL~B!M5mJ&CNLwyWV$yJRD55mw(f}<9P~c&HN%9Mj@&|g(oSE6#^==%T2sP5O>-Cv)n{UqfW(*TQil2KA?qS6uK7GEg_dwsFVv#Y|KRFV(-20|7e7IDpGVU?g<(zvYxMSC@&-NbpWXIlv#hrV1@7NDRq^2)+vy3%}d-CmpUU<v%jD6r_9nK3|2K+&1B=84^gJY#y@x+mG^{5|IQN?93CI00-TO9Z+4?4`e%Xby{_L`H+Im}(TJ`KK*5dJY8g;C(?H(lZ5z5}~RU|ziR#4Rx^#&TjDZdW*ij~B(?5cZoJlfSH-onARR>5})xIQOc4tz7eunMk#6c+7^685Q-e-FsO#MBQDGe#(DXe@~7j$ApI8+^9bVvrcJf03v7P)y1BiC7;iLCpf4)<bd<n#GmB!Iq-O8^rvd2-0$N&ah{OEY(b4=?(*d5a{Zsx#plo9dLGFpjOh<QQGRcMh9A&(dgA3l7CMMN*<qOc$w0(y@w0etiALg+YRz}@Ypu$P#jjL-r9nq#a;n4ZS87SA?bGtF*HKM8CXE@2$iO5MJ|?09p))P!)8O<_+~Y7}rFqj0@q;mJ3_kehR}!Yij<=t0FAr7ypvE#CdTH6J`c8`}8@HQiEL<Q_yms4oJ+nMH0a$$r*Q*WU)fA$2!!{g|ie4jP3vUjVTm5}INbB*NgzOvd7TH$xfVtAhh(9#II&<~y;JrDfLU0Fu?RWrXTM2EEZBSei^TpD@K=Iq7#sO46DSpr4^fZ=eVkX6c{Cs)bfL|^a_p2{lF4u@LzTLNg5jSeQF=z?n&J;YtH5hl^cgQNI#p8a}7qcTvj;{c%vU5W`6~E~0bn#g4fe#J%_)@L|Pg<H0zsdfl5P~{ArsX2vWD6F4vK(Kio_aj!$(`E9#28q8%vhy#?C?Ozk#jTMLpOU(lKO_Yn=*pY9o8D>%0)7~^UFTQvL5$No%TScA)esvrTD=E>oiwteokY6r>z#OXVMuOmIV!bR)s`myDX<jWyfMR+JPt@_1e|osEa?+@p+#sBc9Tw(HV6Q9Zzv@p+omj<+|NlNOZ3irHHw(vPt-dpAQAceOZr6wOY_wJ!)B{VOdQB*iCU}=Z-^6^06}-K8TG;F~cw(W~dtRuI2jFa(xE)nkHayy@2cAm9Zvuy5;)pa{U@f$d(7!>(#{<qpn&zwMy%{sReCU43?ZWv^#-KL(GR0mMPZf^Kp|NVWJUv-(}>dBJaELeGt|CVcJ3u+Zmy0Oxz2x1Rh!iMm3M~;VTb^#HOxR$<q^ZYVHgN*jejOT$$hm6G4KBsWv8pBoj++SOMcH%%r3$wf@O;&&iENM%HRls)&LNhiWtwFZ=s&A26k0_`-;GDgP{mQ(ECtvcjp5sMTi`YF|ecs)bD+-#7H^ye>P^U0NG*4wPQ&+a+2TZcNv_rOVphw5qbWWRfN*lAy`mTHRW8`BnrPu~v+d(u~tX3=WIIZJ8w1{VkzvTqt7WuAD1rCA71;xHL*Suvk117nClJY473*MpqXXU+WRtx3z>{MTN7;!W70hWNU`WwuU3oIc4s&Uf*^*kEjSkofYGl&XxM;q4bo_uP3GRYorv*>}5&Ar^Pw(O5P{h?e@X77Pe;f8mTkZX};cLcba6GqY)A8MxL5Rh$`NeJ`8(Nx80Ux30Q9ri`IpYpe}r*>%t{m7ZHAmscEVdO{@Eyx;NHjxKiYb61^Q$aVJIP?<|#-wdd3%=_#;b6OA#`yRt^9??Y5V;#dt(cTyf#Aq|<XyXxVpYaNV8y7~{qt!Ai|GehbUn24HqGtJrX5l3urJA{r=k!U^MO2*vo-c4pe5gH^d(pIJIf!)UzNgE7CSVBK!ETq@!FmGbk?75LtKh+Ynzwp$;!^zw~Jmh;aKxqzrD#m?CWiX~rw6@wA@gRl8JdCrL#1?EXH)#bmBut;O<-C`3<N`RW*2x8R|54wK`E`gAkGLe7387s=Ua$@h5qHzTZ2M8OPkWY_x>+&0ZVRCHnK;YnFO=~<EkR+IL$N(!w<m*+ZY<#$GIfM-wKX*pvD8U`NJq?3O{z7_(Aq|{KM<(H*R*Es`Ds&?YBW5AfhY}^vOJ)+2PW6H*Lv!8UMx__w~socH+EXh)((S$MVL)hWgS*iW$n-9Q9YI2hXo!>B3kAxwzFtNMN76LN$tq?17o}SmbO_Waw<HiML*4@Csw<Yd}^mAlxUTt`k|q&R;5%g^ln*}L45+pSe|%}C#kG#U%+QwUdWS;0yIHe<P3>SPACzuTHqjqOlq5}k8rS4&=HPV;4$h39>_GN1qgYPfkhUnN~=AmD3p{+)m2g^b{i3baq*{^Gjsr_MiowQFGXZdi9Ey;o;U>F!Adm9YG=qQS#dLF6{Q(T&SeUM+?`+cxq3ch8BsGQ@lL@-HLtULZ6ubc!A`@mCwT+z5_G|5r%i$H#B1ZWs+pa6uU%}0P3WEGTov7@^Kn=qp<WV83SXYW*8gyAKn-aHQ=F%elf;O(u)seN0IM$|ovju@Qv(@MKF?guhQUCL9~V6M8V3}Q6h{IdN*$JIO^8(q?1?etgmb6pk-Oe@>tC*}K6cd+Bkq?HI5*txh^7{Z>?R};kDjOYZQgD|PE5O#-*>sKydQ2Wt&DQ|O#pwpn1BqN{O<b`-yW}3@xMQ)qZqBRA#RF>2ez+^N5lq}pocM<h1G?}O}K8sbsMfbaNUJ#9<F<EJ%H;kxE{Im3rFjOQp46i)n#bU6Lr)^RQcFQrQBam#8iiQRryP?>C%c(rwIjUwEqF&6YNa'),'Libraries/Compiler/rewriters.☾':strd('c%0QeYi|_Cmf!gmo%z&lI><J=_c6M&8)AI3XcIs{w0GsTTH|qJMvP}hGh;JowJRVbJOU;dV@xms!a5-#5Ap;;0#Zu4ANT%*EAeqZtRk^LV9z=A=&I`Ko*qNAS}Vi!bl2n5sq;RkIzBte&hFj+4}KKk)vh=8?%8)BihRG+sLs#KR=cGjoNKgZs*SE6gnp?M1VPB#?%28Wwb%E&y5sfz(ZuVMJ9a}a8tfk@{ZXw`5YpW}d*N;{<@+ytV_pzUZ}HpJPA{spn!R$x=aYHt7W<KX7P5EPMp@qLm;E<i`%^TrZ*s?hNgn`v6+rUYP4*dEE?1_e5vmcmwY$}fLwNl3^c`%F*$xMX`+O#`AfLSjx9^IdLE!fTuhsF`3HCnw(WhHmu*)TOHKMPN*<<=%6W<%+`<AhmC3Z2SuQUAX0)Aa)YZbuAWp<vel&RBQKJ;1swd(VpL6|=iZ+%((yd=JF$Z!7mwl9Veqn-%@0fTxj8k{vc0IUID_H2C6>%>Po^<Erx+l^|k>l5_L?8l(I#e+Zmy}}-`hvmw@`lVm4uRJIPWxROr3GM(~Ts|T1+%E<H7ErHOl3}(T>~-2cAp08o)aN5SJ$8n76Z?9gvk>!s2v1~#fPeLap0DmtjZO#KdS1QhsbPWAW}`nZM>sAFpZr9418pF=CSnUU5l|H1<vjbkTuG=LrwIjSjr(KMg6?-tzV43&c*7W<154uxP%9M=Xm|Zm$p*y)hq?%sg5RUbC2ik_V*78yf}h=c^q8o-8~0%M<`s92i%xJkmRyc%5N`*Fx0?_fKRR)5q0{uVErdDzT4ida7?&hVH~8aQMM_h0rQ3Rm$N-!M)4`S$L;@NK%og=9MPq^raL+k;6{fCVlOP2AZ|vF0NB@NVg!ouv$16a+YwT*^OYYrPYqgIeq6^_yAXlN;!Y>Wjn?|IDYFQk62HO+Pp#4Sm5lwKB-Lp~Tz%(FunYunNmN}?P7Mc~N(>uVCJ?t(>mgHFB{CM~Xii_nGPf}Y2nP@IyPe?ZiylQh+tcnz%(N3_t-ipJ8x`(huSJs0+f>w=PLc+xcPVUvE39dF23t4?3qD_tNOVJ-HRbD|tC<|JY3LzYUrktSH1p(WHebdil4r=lrqUk4cF~K$>_RH)iq0v@@un(kOKgd<h=b+?+7;x$9YM!hCpHJXK$13}%FgkE_FGI2TQdKJKj1X(R8;<ac%LblMm5K&07RD6)bJF!*%F;&(O$d=faD<ze`v5IBI^Y5=4x7>V1e_s-QQ*>$V%deTdEdZhdN7S+iC)B>3DzT`A%Z-?9<p~day%JmJ;C((ug|{se}3{mXMg(PaAh&@j?^0sFJ6qBy@hI{an!59zuuph{eM{)9UUJ(%)i3LfP{jZe;wj#Y17-4yH7B%+#M+=<Ywv64Wq^6p6BSAR=ZbkHPLZ!See-hMj73rQ5mM(KqFZECN+}ShR6|Qvh*qfYhevt1l(-B<=C`C6>w>t8m^}(bQwPDku)&tv$UN=G${UveG^^iURP>_^a=+`#Jf2rp_)_&CCkh=9_AVYaxZ5WYH`Far0oQtT7YqdJ>bf771mL)toAtAwkJSY2K@6Eli4#3J)Z*vZk{%jFclAi&TN7wkj&C;)N8RnMpg+Z1j~hhzoy#FzS?hgo1JApz$1JxChy8kIl;bQm&&*(x>EgH?Fo%y=$WJ!shy~yO-xF4fiK!bw7A$BRt)Is_u}R(HL@3GbU;VD-du<sqC|~VZMSKxK*wy#B1`O-S}8F64;%!&jcTvg*_^jw@9-91(j9CglHCfrnNw3}$j`T<r>Bp(SR?J13}lw8f=eW~Z0K7OY62m-9tR3lKekU(zyP~0>->e*bqL^gd-J_t7hIY;)WOyu3U!&L?tdbBf0WpwTEp?2B~9~q$P&AnXxx4|y)s>zDyEoe9CnIP)c}!I3Y?NwYX!qZhvMq2)-uJ8Ha{lYz-4`3_}%;t$!MKV)ogu=3Yma#wxrO|T&EoYI9-iGRonrm>^?nqhOfH7?!T~T7u-QYvaq7;pr4;SeX#cPEi#2TmdLJzAwMoj)Bh^9Be+YYK)(xp`Rx(&J`RYt|Gp&b)J;J4-^b4WeCyf0YnKPY1}$B{NgyoP_>j*F9S}<atZ|acgiHcp2Oc$Qs0EzSP^HdS+n|=?TD{uv`-&AS%5xDm(t)vZMHr?R*{YNrqz-&Rz8h?fY>X>kz~@W&d;_0H@Okpf^|j;hc?*^?_1o}w;n;XMHX4p?4}Twyp$8%Cl>_6z^6WVHYFC48^VP#~uTyPyxn+OVoa4r4@cA4*FxL&3>&89!d<CDc;REyD_!d6jX|TZaEAafv*9aE{4@bwwxBt!G{^qy8`+aq$2AJSzGIRw=Fw1e=knZ_=>`t!lh<_!oMAD!y+`;4U=(cGkNoi4Ul8LvLhzs}h;(MhC2ppF_Y~EC#M6PIjoqdn7aNc<AHvnrNq!A(;%(EEwA+TXY%$Nb&UMFox!_BC7v>kWL6(ywN`F8IpHU~jP&!64<XhUAt=iBnKyD%dzo5^Lbd$cPq(YI<==d}mX+(NIbbvJ&)$og;5Tfc?VjM+EF^&4@wR&B>6MW3e1L7RHsCk5PzaC)$(XTa^+ltq0?Z0qU7l-BSs^n8aHHL4w|c3hL_oUFkq4L*ImK)3{I!v-o3bZ4M-Nx2xxsi3<KH_6RBBRo)el|AI#@U<-r30240-2_n%iK(eyFzOFbEK5_!FL8z3;Vd19Cn0=&%5LiFHVD$|=@&AjREo)Wg4b;IJPStCR@dwX0cH}*DuBCw5LoLdwkyM~LtlXn;y~$hf<0hg;AUQBr_7<3%l=kz<?*B#M$nuqN{JofHB7Y?h!k@y43Xy{;rJa&S0`}}xv@ell<dti9j>hCYT`vT%azf@=R&vBuZOjOT+b6g8W%Fhh9v>Sz%I26xXRLdOGlw=#qviN*bNf*AF#J4b{z1VJOFgd75tJ8T~l-Q61UCUir#OCt9AKupp?LIFa~u*K{c2N{vxsJl>b>zE(ZpkzV#JKOCsT!ojI+Mn@90zKS7y_*K*ehz5#w@fZB^lu?-nUOTd-j-_%VGzF_2v=up&bb>^#$QV_Bv0?HSXxi+IMh49U`{FZ2|>A+NIPr2{Sh54Dd(=}Z9W;}=YGxgH@mNkVDEI*JlCvmL|Tz$dr2551ASu)~XBEp$#6u!B4|E`^rJNNw4?*0F~d*{AAZ%l%)YSh~<jcuA>WCXNZU9m7e8QtU<5WWQnu50X?oOd+PT10Wby$O`)(TalT`3%wX^xRu!cZs6RsYZ<WsOF@|z3#=GX0>xPWq8)RQNP`Zs=d~{Rwj|e3Q~cBei8_Gs11s(J$C|^LXgbNp^W%aU?%tV*qRKm4M-;Lc`e$rS59Jv^+de>^Xny^;}g+E(R6%zc<rN>hf*nYEFf9f&F5Gc_P+)FVRS=qtBfc-R>qx(exfFnxPZs07^g(WIz@8GN|adR;b4qey$ouH8p<)$BNKySf=!@M_b0P6BO`nYE7Tf}AYQe&>HkN1?UgGzBpaZO!X04PDo(n;3X!Hsbd0Ytax8GX-~xH7P8UHmjb{Id7TkDD@uMdQGyQ<l0n)gXw{@fJm+SAZYheqH2$8QKAVRYv_Qj-QN+j^`WS%(J^FBs!clDN)_A$UIM)|l|unlR~&zIIG(L^8?hbF@@c1q5}J%qVVYoQ(Ws-3ymQAjr1>XipLk_x9+PQ&L+D!DSoQP1?`N@-h3Td)uMHDeZQ5>muTKf~Chz?($Cc;HhIa9^61CkiFv`7VEn^q__Rlz^zt&UV53GJK#3M@5PtnF*69Cv;+*uc0aE^bz){1kecYW18hzW_;33*^GRDqs}3$9vzv;%4Jjc30P?(u6BG!N*Nc`_v&4eJjCKw5-gd!Z*`}CjvT5tVu4#-v@Rl|`Q2^pRvYbdQxYy}godRT_Pi5n-o>P6+(`Akcq*^2VYjE;5g5oC8`uMG<_~wtibrSx(G<12;}<fjO{wq{+g-e!L_THs+qaQv0}hNd5O67P?k47@J!)QE4YA0giwNim5zmkb&3!LAm&t8pE&}65JRdh*#k5qIOuqUCmR^WhlJpv!;f|>Rlq7a)I%`i)rIKIHmO5LD_EWscw5*-Vs%a<|uEPm0v$tPdy?4n9hH>!(WY?&ZD>fp~%_DVM8fSodAcK`WydcT(4Co_L2NzF0J$A;#B#yAvoev5Pg<#dBYi4AA?WnyQhJ1E8nkhVK{xeN#Ir>Q149m)Iai-P6*ck=dwnB1Sl1a*Ktt85ie$xF<LrD#o$SKKn%V%A}K4LDez}P4xa>u@8<Hc~E28_<_kbDer=OUG*An#sbE`M@{8N9EkGkp7LBorx&6IOK65J-7fbFtc}&w4`Ud6>)a4z?D+IsvBO#OMJrzLdE88Db=%$f89Q@9-lS#1Fza)``c+w^~jeKPYhv-3mR(4f-Ui&9|dg8*@DMW?F=I;>Kc@9h)H^cv0#K`#vc?0L1<0BPD1><(OWbAWNlOqMCc&X3^OT3Zx*7QhZ%HqqtlxwCxS;6?UuhaZ!BXLcd|>B^E3<oXV?31MW9j4FZ8_#Fc^9B)*w!04^+$_!Zt5?`k@IChGg?azEYi(<16ht}BznfL1H58a5e+7*z?iDV|Yt#~tmOgEYdPKenA&wwFFeVo;>3oXF&I%y$AWifSH<5V<_c&s0I@0tqUbVkicY<RYJXf2erd-HhQ_66fB$_{lAh@(+!TbCs;*xy{1hX{BA(#lp4Y3Z9lmtK{`-2_u}QRVZ0R&N2vWVb7`vHhnJxI$<8+420-riA%=Mw<UK1GVGkJGI(J29y<s26>pFno|C>#fNt4zZq2@P0%2HcCHzBYeB7hnN##RQlV(v^SgTCrc2;9=5T|F93_jlwS4w6Xixw<GP1`-x!qj)YQ(LH~y(NQJfmI8|j>woy)#PUI$n$aiOPO3>AV{iW=33RE72eVkH)dsOkP|KTtEu3sKV#e)A8<^H4=k{G=bK#1cfk48Rlh38;x@5$%8JugueF=WH2ihgp56ap<HZ0cPRHgF@t`vmGaCFw2EAkjjq{e7KBBg%Wex<sI38|uNnd!K+4&g5Y%sL<Lbu+WvzgIhRAfqqlxVp2r4$XO!54Uchh-0i{0`}72+g7AN|UsDwL90e(zZnpbljFYG;w35-PR3GQs5wsfW@70woj2L={_4bTeEmz$3A9~xsEl;H=kKC^6^G+K@VwU1-s;y9c)wwltUQ?c__Tp;{BAfsr3&0*(xAbLR=u`qe?6h%ar-R!bSB%hIt4|&01Ak1wJ8W!&DecGd133%T$PX=QLn6&MExeRY|&OLAnpwwY-7<dVe#+BK;*cH7EF!WcRFc$74yH@?2tT6)UEn3V-PM>m%CumZTzRPSMx)E!~j=i1~Afn3A#;^20OxdE{J(KV2x0N|yV~#rm~jf?5=iFF3i5j^~)sk<_S*x^u$|WxPypIglb@1$^w4km{Yk;_twC03#>FQZV&LFKkeC0%>M94s017d!E(DUjsqhs3h2V1XoG0%jwgix|ThMwE^$Kv?o&aen}KMJX&u1M{R1v(r#X04t`=?#^U?l%bsmg22zP=w3}`+%y!bc^9e{4hq)O_P>={5h^Rb&V*?gO_<r(0p0A_~JN4pebxA0`#fIYeyKz%&Bu5b+S^%Kl6M=3m&D5g9h1OF<syPiWX|zH%g-|GC`m69+$~by^Qk~IDCwDUt4lG+jsPwsD+d*FI1qe7aEM`2&d^8pm5-sfiCh%MBcI$I8{%gm6H|5#sr!A%PlyJIonnV%HnU!bvADn^DS@^vB^vq@WT7u6x_?#co`{PKzR<1Zh?EKL63B9}q8mF8&SD4VB(sYIH;qhc1AK1AdEk~F1(*4EhKzfNw?3D980_WMc!@WMkh6j+Ux!N?5X_lFynl}&}?y7H~2Bz3{=s#O9-%TnLG(F5m3i&egN)$4u&d~kErYAE%4yx>cTwp9*yAW!iT8CCMW<?tw`%@6mVMZ%`koD?{i8uFI%oxf81Ck@vdumiPUE+co2BCO>gdBt|_)omG#Xr)iwliKta;h*jy578@1}44k46h>kzb{wXVmdMH$#QbgPG{13H|oR(BkFaxTmh_Pq9v=6LhOY&W^u`r84N^G!kyPB)k6aOkyS;u!ahyc((-)YcjdIJC!7WM(I-1sc2k~S<HL#clNu60+7)J#0uwn^aZ|5IxMLNaeCVqsTdJ2Y@vdu$7ua#f0?BD{d$MXdSjl!A)$6}|_If-g1WW7#_5O^cV8V{aD8Z*oVN0jD41{&8M&eOtL4m+N?M`677mb7mxIXy3D!!MB94YSUWo11(%ULsu&N9q6+wN7SjVR%9`uwzY;sC~aXj&&ZaV;H>Qj?|eM!HE{a1+5`$3ZkOnqlJc5g)>KA7@V#xFQW;kp)+eBFtk;ZpUJ>iC}Y!S@)&i!GR|I!3kX98gFw;FujL@w9y*XO0f`xf$j44JM-D6fuQe@BE6=y%5CtJ;uR<qaZU&Na#n)DD8|E=sj(ef@I-9px)@EK6fq$EKw&da*C6Db@doJ)OzNXCMCK*e{jj2}cNpP*ZL2rCai`~xhOX_%JWeG#=j>$mwh9kLjPYx4KjOw4@ob3@rs)<Mx<pUTX1U!U%~qDAlo-gV9p0LvyCpK5xXKs@&|UJLx5;!Kg>ZjDR+&Yo8xEFrk-j5sh*pgl+4Vl9g}Jz&iU8Ab(rT|epbT2raK3*?M0Ze0UDNjTJcvZC`G6F(=7Q6jUXk&Z#Pq$IRpOXAXea~p7TCRtHgTp-^ACw5OzQBsW>93ti8BJc3v>Ml%sJ4^c-88p{Tm|`g@4j&!46N?9=l&Wp{A3`TW)}aY3n-MzVhW;4Tup;aQ;Bxa86KF^u{ZQrp?HF_N!ZQ9Y9=hQy^icQ?1ckPli7AB1u#WYr)<%(~dzrl!uzU#R>B{mLi7H@zqb-D>k{oCpH$-_szhWc+~uLup;MRpYXWpVe`x-l^-I+vIY8NM@z1p7(cE-OP)zDxmLVDqa(!RIe!p=lwRFi!q+n=@4ix-S>kU9&2VC2Y3twI!A+hC29lwZvN@9^J`ggqLehK-5ud!1qZT&PLa>trj#A~WdHk7SSQWt5)6*YQal@1&rmBXYc2v$9Jnt-vra7`tC;O$OJlZVHwX%QhR%bxP1P7!(k1e0~Xc~yixo(<PVeoXd!D6-3wF?gLfY+qsfY<h-2NU@+B0=zZ_=_U;Sia~SmJJ=Xs-I=hqXWr!t4GWA423KrU<y2uGsGopF;iT7Vs{u})k!IYlObp~gpL}rj$}aolp^tx=QPzUPGi1e9tqfBD}J)=d<0eUHI`fsz`Zotv>L0M0^8dATWNz{n>-NV>*XWRh`V>ZF^OA6B5||jh+#^PdNiU#BLWwX2ij)17Hz+I`-Loe|BGHUH#0cVr3xzyA5!?Sf{U^%=v*g6j8{-lb(JEWBD|RX9|@GqI=q{K#h`<Wa?OYue-oJg#wK}4(tO#QeRN)wD^MU#Sw<OCk7v{ad)CZ@D8c4P^_n?tEA28xO*<zqRgl2|a31bG9#~o*_k|W1ULT1)j3)ntGIhVTeI!tG>oEoKrBFZ{VqqiD>y?Eol~|`+{ufo)qeu'),'Libraries/Compiler/to_ast.☾':strd('c$~di-EQ2*6~5O~FncvrSwV8{1T0cnQrw`jWmqy0KotfQmy#CRU9v;2y+Tnywq(V&>Qw($(x|m;IPqWHq$m=(jgyN3a+_z!K7oP0K+l;Ol0z=JyH<b-+9h{5bIzIb_nk8&e1qS;Jo8&ZDc*f>@$&SQSxN~hG50#FhAs<ArnOY_7VKI;OpBCCrfFJo_SnS4g{kTDV^cG9d}?y+608&Cem6;mwMC{SMyD^ss5wW-uZ<DIH0K9MA@3z-*M};0Xy@@RAckv3%lJ*1PcBYRAo+d%ly6x4gdg!6<qKEFE}Dej<bUPQfXSQV``hicJ8zB;zbPTvWc+C3J@MfFv-c#&6Mn#Vt@l9;*EA(7>UedHA6}8f4nHI&xmbqVXZ!(B!)ZwVgY=Nw2-~-x{Ini8tm@;fU^L5`2?KcK_rU<CWf*iNTequ?KFH#<3|XC4#a%Q)kJ>><Ks$&0AN+f9{Z3uKQrEAo>o#l9VA*3~8P{5i9&=o}*sRq+l+al&3$<F6g(d3SEO1$QSp0w`*QpRQWUi}b4Gsd;zwjsK=zsx#J$R3nNn)#Bax%B>U2}n%9W1*+Ss8n1F$68eHUob|&muLuzEH6ZP|ZueHwu@>e4oVrEQjZY=asX<5GjQvQ~L>1PWem1Z-8h1GfPi6?+yN(zm8lN*NtDjLdb|^T7Uc#TI`T-<K;D9hrsxKYj_OJqgY$Y{SWv(z8}#bB?G6xBu&7f5J#-Q4ec;warmB7qQdP+ayzVcFflnr-i7FUcixhe1lb`GZwLIfscfV6DxJBx5H$T>Hi-Qm7!fsjw4AUPDkb0mo2k)}c}=hp69-}uAaMD2%HPqa6;*3u^8D2c<;3euDRp(x=yX2mZ1@L@@A0pNyl{=_g9T=p?W|NAONI<R$eNO%_zKyop%DT3<E3Ui+=F#@_7kq;TV1TWm56uDKcx(Fh}B7s7e{UZK4DZFhD?N*1f|!+gd7Ti&zyvNccUf??Mj6%)I4V;$l1Mu8|p)%$a_wRwgC*vI+;Tex4(s$jCT^*Tbm26O`LLmpa~z_<DUsx_xKm;dZexoNKPc)1SdaDhY;vL2$>dtFr1esVg;j2VL4tU(FfO|Cs!AVZi;f*ko%-7*J#5=Ffm=oO{AyrgHdpHrN|PBS}>c51_52IIUy?zA&f!Yk*#p3+NeNY6f@d)AJU5J<k=(2keXeb1iTZ4{J4u0FeL4Ipc1B%La?~LTn$!aP2w{bpadX<MuYQa>=_!E?`*+VzY%!8v(?_*!GG<?Ui@QEf3g=nIbMT-kHzi&>6_z&n<!Ps{^ET5H03Er{1a1J={Z;<+Ddv;x~S`t|3|STaJTpN3~%vWN$(@jQy+YBkNc<bb_@2Hi77BwG7xIUG=&{h4b~BGIgW^8nugt|K#qFE@A7{~Q*gpa^e7c^aw&kaPusWGR1CeXRX*nb65HSYp-4@#+R00y($5B?NI=d31)BT(l@*URn)L<nOEsR*`HfDfP*E8@d48;==?fI<Uy|gE1bSuW{_nS^cj2=IpFhLrUi-@j?Jpm;H@DlHyX_aZ+J8G~Kfa^1cFAkFnSEk$M-v&-7?e~wvBDHozsiAX96!l|wHQC*YpL;b1t6aAMT>n3YxHdQKwTfDQj6!WLe7_w_b{Fzg#qVubU0Jc8!J^#>ZMUoURo`Yh(~-wiTE@r2$k%@cU`?G6x{xkstjT9`;uw=%1|YuzA@Jv@&RmU=@%7kna#hQ0&+Jl0a|Vn)jMSSzT2pff&hHUUzkc)R%Db8nuth7AFQeksNO;{Y!xzl-kaG#;Sbb|^zK9@IhN0rD9$lZ`j$+|{S`O?`hnS#B?L&{ES0`H83K{s44E4?S;LU@aw^Ac=@m2R#0XLlotaSVW-C$}Dy5QebQ^6%lrxD;IwG_>kVKo5fs-^<4UQg(@RAi#m)%5#*7IaIfsicbn@R6Hv{<vlUIn<2C9L~0Noy4^!hi)OmsfGA=Zm7Kg{LIUYx*>_*^(PVA=FV;d(awq4LnE5DXj}(4GOFn)RveJ)%!{(nrYQw9(CMp=r-W79byYzP~7MESS!!NM7KuWmd~^bHPUQRW0Qxb<E75ZB88=LVtadSd~6oYpeB<P@CtHzSC0?Q$-Y`SVtibcnwmITGEE|%;W0z*2k$Zu)UiaqFuLS<GQ}yqhiI3sPEDO%wAf#ZOxTIkLa<NxtG>@edPL7VQ7+JqMC376rn5<6Qp)>bAI&88DXmiHTH#XA8&#T)OQFaADpOTq`|Ci#>iN`JwgDu%bitv^8a7+aogqWrt+_?f6cK3#)y7hn=XS8vRR|C^H&)M7yp9)CufwV8RfgQwMo~qdV+vKjJ9<0f%muZo<B}0k-C{$6?P58y*IA@aC5e>Oa;{Y*veszGek?(rtdJT;li&|cJ6Lw?aI~C<vKp)*9A?lif;x#|n|vo#9mg`ZtkuypFpKLhP>K<zZ{&V~$Q@-%tA)A%`YIn}_f>D!{vZ1~P-5??>))g6nfJGKtJ~)KMzN0bDS)+*I$on^VF1Or*12#05S<gO-2wcCZ|FHQp4duUP>Mg;l83;F<~oxZN*%jkZldewe5-x?sFagsr5Ld%Wb$OkxlYg1z<%So_ff+yI7Qf5?|zEVMb3ON&3qk`l$J5=sh?5O6AgWI9Am0_Sx!o)GVT0LasK)KXIkwWp9bpY6Gf<)cZO52rz*@oM<+Nu$vNN)Rs-tTwOU_6GuI=?qc$8m>Y1zOFJGA+AJbVvBA12w=b0na$GCEvKgskMN%<sCxl+h3-f&T;%A9637nPkRW2=yGx+3<H+v@Td&s&4$0)@=?xEC_ZNPBa9|2BN?h@K&^q0O^JGms5PjMEN<TllhVhi~O6KG6#TTG8Qp4DnIR*5T;u`SF<3u63OL;hANgw-)2;eCkBcZ8@$V%6BTC8g_v1WghkOs%MfhD0d-QUxPLuU-^WdF*Y;%j{e$(+10=m6qC0=QJbwO4GhF@(dp!e`0jg#Qlh`^mM>UKmb?P>{{b~@P^k'),'Libraries/Compiler/ast_to_py.☾':strd('c%0Q6Yi|@s^1FY<WF<%4W^n8!chRj_?uhX{6en1~p_6>hXuUfQE3bDaJ40+=LS$aXCLzIKJ3Ir#A-o|WFCY*kw{&0cH^d+BLoQPOz*Y5YdLFy8hWm1h*zM`*u2)x8S5>#in~h0pf4y36RNP7_C|T7>uh9&ws_)br&B;=&`VY6#HIAbu+?lCHv!X^!Ox3D>&_&o0c6@mEpNZpO>o2bl@7%S=aR|vZ-Kl0ZaGQRP+HchwW2Kr;s7-P?N~tYIZ{M-wPeVIj-9EJ285kPe{szqB;9eUfea0ke^WL4q&`U=M*=+S&l#T-KE9^sdvQT7)*dkjY6gy6^TaNF!W$gTv9Ua)dhd}E*y9p$%UpT!!yRfIZ-(5d=Y5l?{@bE{#z@JvGz|$Lzx|>6M5+JqxpyEtSRZ^kN-GnJkH`w2-BZRw$;Bltv)++Gy>z8xiz+=U&;j6hv&@MOXLA5S$AG-=2V@<a-5k)svn{djtdMlJ`Phnbh93eb715LNaAJ(q$wqRs_79PeMO(f#0SsYcam3%*mrv;9mXOF|2pgF_2IKPb0s`XN>HWLNW@Qm4non-TD38ugQes}kqZ@&2Ad+%-Awsq^KO>6fyZ{EEA!O<S}{Y#(;Bl%HkZL&fkKKvLEyz~-M{^4P0_Vi$L0p+u;$eW)-bE{|~pGDEU49ypKbN)IsIlt@k*PvOdSEAi(x1m*U1iW`1CCJxnenE6w;&I_9zVUhU7;jqel54AGn$j*Z_{Kn?NOEkJ9fbbFpqfY796JW=FR<h61JKA5>?8Iu2xO6+VyD>>TV^Zl3_Hut0nZoMMUdGgb{SOlGq%b;XII%5>>9hyZm^r|7Q4;vu)FLY`;vXd?z6AiH|$&X9ecnYvPbL(_Lx0kPjg7cu7Mqe;=o^b?INUBnjEW?P^5R+X`BC?D!|VQ`<6sHffG_1D{p^wpg+F_7J=lPoZxBq@L)EyuanR~790-yQ37)7<wEiGojYQ15WoX=mw?F5u=|OZM?fgwvD-v8?np!+_*D?;BSb^(fg=7;s$XiffVbj4JKj4aBtSBlf|jaLpQ=$IexzV{aBn*b@C^W1f`8X+So<^VU=f7HUDh%7P{D*{rTj|(-8(qEQJ^WK`LKhaTu;;>SZ}JCMF5|%MU<hfW=<EtG#}jU_J5zF-DKL9Y{sZXF#JnU>&-Z>Uv~VU$z3uiHW7r{l7f^qAm9W3zQ3>UHv{{-eZ(bs;_IQvCH=n@K0|t&mu;}ShsK&{jiEqkb)3jYux#ty9>g%+w;lffPGG|C{44xBkKeDn%D;EOVjiFr{ip^fIRiRQvm;>kN<2l*&8j_9BrjV%U;!3PHni<2s86k0cYQJ~b}uk4Lh?4X-#uUhV>4((PuO8JB2JyKpNczfxziqaFsI}PjyHo0E`u9+Y=eFk;Xf^OS@5ZjTSUL3y)NzDBVOP~Y)O`S&HK}41y->Lr2lg9lX>{RfE;KTICK)05tZXCuDF~v(l=`BHu!R53Vui+^i_CFwSFU`6gTIS;2Y1ANjpVF3F+tSrUc&`=(Ss4c(lIo!%yE{`1gg&#tMNnTg~`s>3U>fU&=sa``iVTx>#@I^9j38!%vj25-dImfP0}{!a?w76k@-|H3BT3WY>WTg4<<}v;aQT*6(b-+~G5YXAao}tTpi*drZ=3g6WIwi$bx5cSD`MB~<r@!M%aDh$O04k~c|#G5|q?gpvF8tJNFI<q;y;{fK=-lsIjPwWlN*DkZo8OAff^#JQ1yq}ESc_4J2Lu3K|#QE8S|#ePt+0KRQ*Xz806lD5o#<iDro?<Mss#c&EFWE<9R`)&YH?4%A%^O6{7_J_?r8KmwQ93opFNZm4;V2;y?T9iSDULD{yC%`He?H;k@+{ekLQeQ0wL#}NsA51{UV82{k#DM3YrySS<9Iw<YO=7rcn6@z$<Uz{CgqlmYy$oTD-esgnKM>}Z=6Dv5!E6iMou&0o4U%T1)d!4-D_sbsoMlg(d<>D3ymRDpzg#@|eZuRd(HR?tABeE6GJpz)N8d|u5JCd$WdqjI11?*Y4J0PvU=(st#L>%#z^H`0+bVCaQY}NUYWI{C;}In=B$2ufb9x;xAWp1B!p*lfR+1~{X!sZ^N{_MazQWfBZL1Un&1bi*P83w^@DXR+nG)%sptU9`@g2@>%vv@?M|)*f8v3+T5=NeZgwc+qu#!cB8AGI#qlfslYS|_IHfH3s&Cb~YWxsy^@RMxew6`wyBPcVPm!6t|bp1r8G&;cf+TccT0;6aC2S|4gZv-i<`$z4OCW4|=J)pg@%?{p<s+}Y1k8qb0+k<dfkr#?C$U;z6k|QwAF^FH~3dMJsZ0Wou99B#|w7rCOXNxEsv!9AN6Yp~?p$vaEig&dWyyqmItMYdh6@;oF@`jmn7#3eB#uO#f6zAhsafPk0`-P$jKN<oMIVLSfk{Sj1C?5g@Sd@npq8dqi8=fA-so@(J>}R~xNReQS-qZ#vRa?Nqs9$9gM$OX*%f-07$_`BUSl6T?0;Guz+r!8+8Dwp>wrE;&pk161k-aU;Se1(b63m^j^>X?wh<rl+CG)wpduzAf&!r?O9Yv0j>V!whh_Sxm(px-V(Q@aOEJLMG_#@!}+RO90W%gtg_mD$umK`%U4@>Sn(M=~WH=Xn?SZJE>TFHng!6#5*$JtHUcRSwfVq~<{dg1>Jt@rDxr6j^5zA!(;Qi7%3rcRj^Ovm3pmWw5$TABG$@+@EHXIPM5iG}TcU8J2KvrF6vWt7Lw9D6TEdQqY6P|dNUqex5Cccjo;)t(fCLW`2Bh}2M{u*LOW)RqKQOOWs!0d(Eqwn(0rg1V)AB1H!jtF~-KV>eH;V4Po%CEP~&DdaI0o96RWaA$6?-JzO6=EbGiN!bC}j3??DZWW|4)@jTs>Tc7WSNQVr3g2y$0%g^_+?O4ntnve)3|i9?SfJ+&J4<!_LwgzHoQd{AP>@EPolbD)aTQM#I}&e?sR!|$QwC9HS411lusm&SEL75wlIhiSl`^JU9jK8=aXaMm|CG^Kv1JtxraY%s4Mf#NVSEntL|T&GE6v@9m2qe-v%^Fj<l34*aUv?tLgi_xF8K`)?oGABu*BW3OWdNsZL343jurpycS_CYvsKeYcKd1{=x$B@hRpKfY<9vQ%Vy&qIHNFian^ksBtJ0)nz4MUBTOU4L2fj=0xRJr(>mTTBaUKQ`b0Q={4=Z*W-L*3SNcQCv`?OW$g;X=j(U0G`%*X=k4t0;+eil@kouF5R54rXr7<`ko19OZEZqT(?WKk6LWCbo2G08YY(}~qHQ1OWr}kBAE(s+jO81b1yl8R8P9+={7Aob*y%=i5ztuXC?n}MSn<;rgxmzuL1Lu}DIOVD;P<#|dNwOfCGZ1cxAXHURN!2Kg=tO(*mK&4a#>E>eO{k*~gQ#o)rV8&_We3A@EyVLIQVHB<z2oX+v^-;SN)=hDwHwYt<aI<89aJ!JRXQe9E@65?#hpi+T4td&kJ)63TFAz$oN=UCo&p{8bC+%e5LCis-ZRIpMkEHAi;SrxgfH;ub>#{diKUVrY>}4Z07ew9zN)427<rc5A{&zj$2UdF!qbB2X{5CokAz4I{Gv|63D5_c@pMXEV2I?SLL4o!<5&t@P_a-avF-Z#d!6d^R5jRVwKOp8i1h^JW35e=^sY3nVa7pqSnvV5^2w9s3_gCIJ-&7Y?}A0SF%?Ky9qlc7o?EYw2<6e@T7sl)u&D833f4}R3dMF&OJs(io6ichPLQRDQ$_MP8zDOi0`2u09>@i7cElBaTAU3EcqzzK$wU?Upji%2&EiFovRM%ct0AzG7^6rkL67$(>M5W!1CdTsib|BN3oHqG4I*2f^tsbz*9&B1Heh%G)W`u|S{g8nQ^jKtR-cObYOCaHFwv_Q143_NApUdkW@=dW{3nf(HBPJlnW~yp7%7r&zu@t^m@*krJlly=`;077UQ5MGq~VQG`2?*N*<`X{I$~lN-C!*v#S?Jmt99RP2B2e+LTg6w1}u2v)2&bAr47Fz0_lq6azl#{wc5;3-OtRtu)-GENpxa*f-M;(&`406B?(x<1Y+qb^yR$h9kFS=9LB9AZBxMh;bfh)(s7YhUMEX#Uc=E7nwDi&wS|s1J<@iM<<%ORdOu7JDSN6;D{HS|sGu)6X*t*x&Ofhc$m16b0mSt@KK^*i6X(vB(jJap8Bp15c=M)}^wMP&yZk5aFY(ol*3dzR_+>$`SEuQ|Rc+MCknM$+13C2Xpbr`s*jZDZh6+V-GjWI-WTGy5u#BjK9&Rd$>x3giBRF7G3d+OK*#j3zM@JLfrj3<y?IA<5SK!+OUfkvwL4|NyUQgp&ltRJToh*5Z-QBNie#85YOCX*zLTq=k;!PI0%9@WvsD@ZM9$~dz1lOfpb4zu{4KIW0Do<mg$nPKS@&0uXwBSI&STWRnb{OK!TW!@Fb;C`$LCJ+jB!x@tnqf0-;GukB*Jw<rc$J?KYD*COlqwa+YxpVrREvFu(EEhExMmFCnK1yV+Q}+p{Gw`@z4C3vs2k?Qj9j65z!tasL=BNwDsP+Aw(=4pIMBk;dljfzRmtF4V*&0Yh0OdZP{dTB6+-WF75^S0a^Fg<Zt^a-tlYgza;P|=Hh4BDli9K7fZb9zq8`Fk2T-^`;&|G8$HOK*(X4&iCT~>UN5;OO5xI-Z!`gc`T1n7!-J)=?^#<5Xy)@}M@06Op>}<LoJjfx^UNs=tg7CEPF(EB3J@@FcJ$PXr|3#6cT#<zxqA4AliO2jqmsp|HHmsW3<JDTtQLmhRjhgE_V<o>@RzSU(awIX)I>ukO0I!AGZjjP#<&c$pJGj{`UjS`gUHWgUoWZ~0Ut{fd9Af?fmR``Dt(({n+f0t{HPGHWIGnTL3z+^dJ$@On'),'Libraries/Compiler/main.☾':strd('c$~!=?QY!0@xPvexxm1#OPwVdX@G;zh9sY3A+aS$auUE12#VahBg`WSk|&>P7>M22P0|!e9XoZ>IH_SIZQ3+#&>(fwIQhXh(Gvvd3v_08xm@yi`m)d-ER)=i+1Z)d`CQ_JF0;Cx&n(Aw`d-j$wb$bzqf=!4!b+<>xZ;xR@A!UpY1PbbW}jrY7U$PV@n(tHmYKbm-Ov6(&7^Nr_)U>Mvt1TjPB>__vm4O)WA+0)Kg@nbh;I)zUE2UKUuEx`{BfrR5Z=kYC%B;OAdO>5bLajK4SGy8-7x`lGiFKXZ!vhqv4b!SEZ2)+^uo~dQ!hvwl$zNa*@Nuc>=Pmon=takW-&#e9ocE$_ckqW5QTBtYLiAc4hM#8Hbk?r0-uJR7{`*=hBGrW^L$L0<lQXT^5QViN92neZR~CKSW2*CZtlYJ@<nT5eyw8xjYSh3n{q5s*i*yn8mf!=3B%r;540KCF$+>jGRY;<`02rWUo@z>(s`MhdOP4!*F0&s-j38tLo3<_BIOKyn0=7_%{&gz-)6rykBgUkt-OD%!%k9*!ytK=0MX7N$$^|VE|VMQGc1>F4tqonO#0zf3!riF6<^`7@?`~~1+=jTtbNV~x`~b`W;jo4@dEj!R&Pxi@B_Nbe({YzAkH7NPszgat0eVOp8<`QE;e+c=?LO+<6FV0{67M6dM~?^ecx)st^kpIyt~=6_?%vB53Dq1tgWG|5vGJ1bQQQE?6+6e&Vz8^+tP)V<<)h|0u&?G>-p^D2?09{eUN{%=ZBlHZ9?IE;Bhed^yL*YL+NEgrj1#H(v4#053}E7U&EQ^Pqh!2JioTyDDUwh^!<|W5I8M1NQpY{awcs$QA{fvDzR->vM*nPRSPo9Ma$IIpdJX;eh@bmn%0&bCqj>wmycOGi~~bpHpS%`Y3zomZGiAf%sA%?QK!wmomjs8i*3sfZMQ&O0xXNu?ktacBdZtsT{{H@bug|^2A;A}YIVbSV5dg~axol4pwZ$J;#eFxSfzOm3Aw@{GjAu260aJx=;9J#CM>nnG!}qf?2tJ*0A6Q{*BLqQZ099%60kVAQOHZNY_2T$;{iV2&Hg0CNJ^<DU{n{vvPhS84_7V#kcu~iIW_e(JLl^3DYjl&)9RwP!dh+dB;BYD=6!K~@q7pU6w+`6mtE^vf`)Kmd3k+peRY1tIzPX5{&M1b4kH)CfSI#DryC}BB+8qr8k;hq+t;p3TEm-mYDvEZO4_dH3fS$yAPyKy{a{1qd)e2Nj-6@ea(`n?b0{7-1#SBp2S`1ksMjT9o*qTlVQk-Y0`kZ^FJ*&6h^<1pUT6dbbZG&a9$r+CZ<77W4ygS+X>+b;x3kaM1vaK1_JqaPH83A<c!|M}ZH-kWV>Ukbf#s<Jbs~Gf16CMcp4os70lw5eyP@r7mSRJV4IN(;Hd7c)4euaK4cu-CcL{|wo;{Wr1panD{TBR3>2X@<Q(9JAxs$E7=6Rlgak+mf#*5=6*Q8A}erEP4dpr9s*DTs6TH}2<nRRc4=bkSWGv7|VEe0Hf$v3i(vk$2mGql5EDYIhtfyZMeUzr0JNPz!#Zr?G)o-Qn(754p$><L1=pWSG?VH$e_TIKr_wf@QHsJYuj*>@NE-pKoM4NMxZjb`Q>Xo7xv@VkHGc{n6Er1K<jyLclcKQ+ktq}4{~<v^_kkH^_p=>L3^-O7VBl-R{ftAxy&)V$UJIyYK)WUia~F+>JG0j>zI$js3z{CY3&y4#vb63j~DZKGgY`HM4F#9PsJ+6M{YKs*+!A#CKZC>5^iM;MI(>JP!!F2N8=Q<{6wlx3qO)#T0WU)gPKAnf3r%_S!dCtzV3uIC!t;SdymlG?s+c&TyKgTOKJqB9NU8Y+g=Z!uT>73j1nNS3RCe&~Tm<AaWl0dJ|!{?~+vhe4GJ&(v(RgiR~5lVnO`CO9Jd;(bmS7*CtS0Q3^zC%(jcu7>}AR4^bEGT^~afUy~dX_CfvgxcBnt}uTaL}SbLJ@)`qDvm8|PB?`<768{%W~mj3%OIu|sT;rz^=A`ZU1|!cX=_G}T#Z3$EH+|AAU`s<@w9)I-6i=0ZQGXwI$*P50x?g25W4U^6F&d^a{zdhZ-7WIBM5_5TT4u!=v&FK+x14Eo<v?JpMpkAOCtz%lYh3vH~1zc!(J@IwF<Z5GUzJ1>PU;iyU?_^vc0H1-^sp0#e{=(vs{?uIWWm{G75;copE#<&pvZv(+f^W-cPR$g_SJ3pY1#&Bn-_2!-tv`Q)#(P6D<@KdojQIM0n-=m1b9qe4JU*^wgA*f;${U+&KilS<Ei_xRYUO!MPBl;^aURr(EeMDKq;@9Hz_|22v@w{6OGQ5jZOWB%}+p7fYsts0-8wN-MKf(v*t5e8jHYRmKGw%vrYwf2V4<RG^9N9J4WN3XS4SLNx3!D`tX{mLz#h%F$UVKwZOA;`q#tX=%**ip67_a%WE4CB6VS^u~k`zj7K5l^NK%{oNjcaScADtiWDaOim#jYHhixeeeDV*DPh#_DlSUnYcq?qOu$aw&~iby*DOxbB+>|+(v~FKErq)#MyQ75#p9ZJpe|<lq19=z!*K<j@UtHqfa_QTrlH&04&7tBVON1NBhtmHB*id4>pPpA{S!#5w0(MjDrY-nsJ0!#Ecui107mz&QZ#ROb72@D(dpbPltn+JKi@Mlk&|^g^5}pz0o~!ILOKZE;y|h*H)HZ>R79tbA&jwS;-gbeu}7#Nykz5iJVDM3WTd$j8uz)c~~OBPH?0sZPtW6JQoGPFv*6o8~+e78)>LvA{3&<iaMRMTiIh?)%qU79nyF~F5(v9+cP|^(w*t@_@&4cJHAK2i-~O~FDH7os6fWP9&pJx7YDLU+qt50cb;w7fosIRma>zBWANU6FJOiHdwywc-8u)nDdhxJu^#w){|7|L>U#+oDiQo$>1wWYUFe~ps-zalm&T-<?dITk@Sqp@qV5PVDHCt!;|GQ$7J3sv2H2Yv*&yL=_`U2KtRCV8fk(27*Et~IAYKp+(@Of1XH%7|2Z^3awk*L1w1}3TQRaZiaS)HofF>6W&sL%QM<8XQ{D0^ycR^I-BW7L&ss^piS*RoZLg->LpcjTb1u!1v0Jzw%Bq$1oh=@ezNWs8*V3LGJyKRt$<D&+t&#GXEpKK>c3>*k?$0Yn}#a25|JYpTqE?l0SmoG2!K(#v>uaaA^nI6Qiy*?NY2#55@k6(4DU13i!wc+EWgu0$&D4&+fTKYuHIKSLkp}Q<y6b^)PxJDX+*cOX{xFTuFiw4Pfy#R(p`>Gb;Z(^=2--9}K0`VX*1D;J6+KQJ)*p}^^FikW;0G(PvqTiALjKbIw3bc*rO-i&CsjJ;_+XqseS38T=#rgH6mpcc<ZI>M2yV;{jQpK~~1)E`{NtD{AO%bkI0;CrPyb@99F(q%gf|tf&tk#EnD+XTe<2kNWoyN(gX~^p4US!*wp&h$R0mxuHjM7QD&U~i=>uQ(W_Ke9!URvD}H+z7UHH=)e!96b}soiU96{ni|jpM2e67>E)`zy}Twh5U0C40h8%G#xcmDT0NdC(sKd*}7Hx-512@SL88ISIUkvDfngZeK!n7WI7@(cOSKedb&Vhbf2Wvef3F5%39-lY&>X7IH-m?Q@X<_<!63I|Q!L(D&7L_kbmAYb7y>x}1%ev!!Y_H?u!ye;|2YwN%n7-IJ4*3vNq=KR|QN+d;w|G4A%DBXuWxoV#xP5W1n06iL#tt6$1GTuSU7Yl$4DVVvS=UCd&hHctKY;O^s{o3EcyuQ%Xz=k?F?!SGuh1_pRK22RVHr$Y(G3r@>7;KG?Cb>VSZn=CzJKH1nDriL5xvS~aF6s+kUOQ(Sv+O*|i3dfEw3mwcs>syQ$2f{c75_Cpi>=JKJ1h#lz5V*??XWC~$UL#7h3FH+o?E}U}6o*@$%TsE0535Kh5eYb*2|9)j3sPeX;w;oa`ShJPZy961oi`sDi!Uv~M7N+-zjoLfa1apl6h70Aaf&-u;P?Z1PRnr}FcTb}X@r6*Ql~-tkQqNS0(KRB6$R!$|NQ!`LqJmVn|n<T!hE6tqh>DF&xCWa*USau6gdAPWWm($X+Cp7m2=XtEPlXz=)i?ofJ=(;oy4&t2HS}ZER?I!t{UyKV)UhemB$wqqQa55EYIBrp6I)9bZLI+02;@gi0-~T2w{ID5H6tn<9*O1ZPAF(;7>S_(;Tr<B>;|4UN%y=c1t<>d)a+GL0>I2!_LH;ysI;7a<j6*J$I?L$_V7X{FpwQG38EZGYTVG0mz;HGF_?#0aI??cm@`mGmfh*)0Ptk5RMOvpbUYQEIz2W)ds)$)77oqgsWLv-=wHlQ}VKAreCW;>hRzLDf|H}ZsQezE;R}Q$y#1@eRHCo9=mZ{9Z|YQ%jNJ}(#30_@=mpOIYo$rkT+8lR8b7IDr;9_I#z`hJQRHz5bh>%QPyQ}mwn2%JYc7}QGYu01l8457eqCu`M$6%2`i>7xUi1-iONORLl1Ev)#W4bgs)*JEXuABR}@3AnP2dM)_NGS3@R`A@Cp1zE1!Y!we1D?ab5W1dbwEh&9O>sZd0AMnq2ftF{hq9LXV+-j<msz3fa(sQ1{|%CkkU+npbgJbJwMIdb7G>U9FZ!2^<K_Fu1S8%cU4X)q{0PU@OXxU+dxSpt{t<U1h3yZ?N&Q*S2qb>JdV#{8Tvc0UR$iK!!p`iRR+dutO8jdQW~Atz1Uq>{!->jCdkJWRglfwb7g=ipF?rWp4s45$Ty^M4NULvB0Hc^JMhbSw7dn_;*s!m;W|FV_z}Gx~3+6RN~?r*^i*@coOHc>~m5{eDG|De$h+I<CLlCj#0BN)uJsanak5HlEag;F4fi8E~|~N!S5!DH70{xr~_G-Br0oJb3#IV@<N+Ow$S7?!tpiab-x<`P7&tvj5%x0Z4`dPs8wK4zJIHlN4lBf_Cp*@X-)Yh!a2M|cwLP8(j0-Uls5;tnZ<AA$#5M=>7E%vd5KBZP{e&J?(vg^w&V?zu1S?^P?(~zoQEi_%%44LbzYS>Hi%wQQ5Q`b+MN@5|4LSWO#K$L-Xpv#y<fD@;y$~$u+ymC-$C<OWpJa8=`gY!w>Ql4x59|`X+Bc95TqA?&~M6}1mTYtUV^&BS<V&YHJYj`KBe)mP8m=A7g^w&3j')})
__dir__=(__file__:=áÌî(moon_dir/'Libraries/Compiler/main.☾')).parent
(code_file_caching:=True)
(TMP:=mkd(ð(TMPDIR,ÂÞÅCAT(ÂÞÅCAT(__file__,ÐØó),sha))))
(header_com:=ÁØÿþÁÙÇ(lambda ÂîÓ,ÂîÒ:ÐÌü(ð(ÂîÓ,'%s.☾'%(ÂîÒ,)).resolve))(ð(moon_dir,'Builtins'),ÄÝöÞ(ÐØó(ð(moon_dir,'Builtins/builtins')))))
(pathlib_import:='from pathlib import Path as %s\nfrom os import environ as %s\nmoon_dir = env.get("MOON_BASE_DIR")\nmoon_dir = %s(moon_dir) if moon_dir else %s(__file__).parent'%(ÂÞÅCAT('𝐩',PEV),ÂÞÅCAT('env',PEV),ÂÞÅCAT('𝐩',PEV),ÂÞÅCAT('𝐩',PEV)))
(to_py:=lambda áÖï,*áÑË,**áÑÕ:lambda*áÑË,**áÑÕ:ast_to_py(*áÑË,áÖï=áÖï,**áÑÕ))
def moon_to_py_debug(áÖï,show_ast=True,show_out=True,show_out_no_rename=False,show_preast=False,show_in=False,**áÑÕ):
	if show_in:Âçß(BOX(title('IN',ÂÞÅCAT(áÖï,show_code))))
	(ÄÕÒü:=to_ast(áÖï,dbg_show_gram_tree=show_preast,**áÑÕ))
	if show_ast:(ÄÊPSH(__ÄÊIMPORT__('peggle3/gram_tools',globals(),'')),ÄÊPOP(0))[-1];áÍñþáÍñ(ÄÕÒü,'AST')
	(áÕÃ:=to_py(áÖï)(ÐÌü(ÄÕÒü.cpr)))
	if show_out_no_rename:Âçß(BOX(title('OUT',show_code(áÕÃ))))
	if show_out:Âçß(BOX(title('OUT',show_code(to_py(áÖï)(ÐÌü(ÄÕÒü.cpr),no_rename_vars=True)))))
	return áÕÃ
def ÄÊdo_imps():
	if ÄÊmoon_to_py.has_lazy_load:return
	(ÄÊPSH(__ÄÊIMPORT__('peggle3/rgx_golfatron',globals(),'')),ÄÊPOP(0))[-1];(ÄÊPSH(__ÄÊIMPORT__('text_format',globals(),'')),ÄÊPOP(0))[-1];(ÄÊPSH(__ÄÊIMPORT__('Compiler/to_ast',globals(),'')),ÄÊPOP(0))[-1];(ÄÊPSH(__ÄÊIMPORT__('Compiler/ast_to_py',globals(),'')),ÄÊPOP(0))[-1];(ÄÊPSH(ÄÊmoon_to_py),ÄÊPSH('has_lazy_load'),ÄÊPSH(True),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
def ÄÊmoon_to_py(áÖï,áÖÝ,áÏè):ÐÌü(ÄÊdo_imps);return to_py(áÖï)(to_ast(áÖï,**áÖÝ),**áÏè)
(ÄÊPSH(ÄÊmoon_to_py),ÄÊPSH('has_lazy_load'),ÄÊPSH(False),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
(ÄÊmoon_to_py_fcache:=fcache(fp=ð(CACHEDIR,'compiled_%s'%(BOOTSTRAP_HASH[slice(None,16)],)))(ÄÊmoon_to_py))
def moon_to_py(áÖï,áÖÝ={},áÏè={}):
	if(h:=sha(áÖï,áÖÝ,áÏè))in(c:=moon_to_py.áÐñ):return c[h]
	return(ÄÊPSH(c),ÄÊPSH(h),ÄÊPSH((ÄÊmoon_to_py_fcache if code_file_caching else ÄÊmoon_to_py)(áÖï,áÖÝ,áÏè)),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
(ÄÊPSH(moon_to_py),ÄÊPSH('áÐñ'),ÄÊPSH({}),setattr(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3]
def compile_code(áÖï,áÖý=None,Æå=moon_to_py,log=False):
	if áÖý is True:(ÄÊPSH((ÂÞÅCAT(áÖï,ÐØó),áÖï)),((áÖï:=ÄÊPKE(0)[0]),(áÖý:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	(áÕÃ:=ÂÞÅCAT(áÖï,Æå))
	if áÖý is not None:(áÕÃ:='#%s (%s ⟶ %s)\n__dir__=(__file__:=%s(moon_dir/%s)).parent\n%s'%(áÖý.name,ãÊú(áÖï),ãÊú(áÕÃ),ÂÞÅCAT('𝐩',PEV),ÂÞÅCAT(ÂÞÅCAT(ÂÞÅCAT(moon_dir,áÖý.relative_to),ÁÜÙ),repr),áÕÃ))
	if log:Âçß('Compiled %s %s → %s'%(MOD(ÄÕéý,áØÁ=dotrim)(ÂÞÅCAT(áÖý,ÁÜÙ),35),MOD(ÄÕéý,áØÁ=dotrim)(MOD(ÄÔéÄ,áØÁ=áÖï)('\n','𝗻'),35),MOD(ÄÕéý,áØÁ=dotrim)(MOD(ÄÔéÄ,áØÁ=áÕÃ)('\n','𝗻'),35)))
	return áÕÃ
(compile_files:=MOD(lambda ÂîÓ:Âøî(ÐôÅ(ÂîÓ,ÄÊCUR((1,),{'log':True},compile_code,ÂýÃ,True)),'\n')))
def minify_py(áÖï):
	try:
		try:import python_minifier
		except áÍÚ as Ðáü:ÄÊPOP(0)if ÄÊPSH(False)else ÂùÆ(ÄÊPOP(0),'Failed to import python_minifier, did you install it with pip?')
		try:return python_minifier.minify(áÖï,hoist_literals=False)
		except áÍÚ as Ðáü:ÄÊPOP(0)if ÄÊPSH(False)else ÂùÆ(ÄÊPOP(0),'Failed to run python_minifier!')
	except áÍÚ:pass
	import ast
	try:
		try:return ast.unparse(ast.parse(áÖï))
		except áÍÚ as Ðáü:ÄÊPOP(0)if ÄÊPSH(False)else ÂùÆ(ÄÊPOP(0),'Failed to run python AST on code, bootstrap is likely invalid!')
	except áÍÚ:pass
	return áÖï
def generate_bootstrap(dest=ð(TMP,'moon.py'),minify=True):
	(write_exe:=lambda x,y:ÂåÔ(ÂåÔ(ÐØì(x,y),os.chmod(x,509)),x));(file_canon:=__file__.with_suffix('.☾'));(Æå:=(lambda ÂîÓ:lambda:ÂîÓ)(compile_code(file_canon,True,log=True)));(ÄÊPSH(dest),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),áÌî)),(dest:=ÄÊPKE(0)),ÄÊDEL(2))[2];(pyc:=(lambda ÂîÓ:'#!/bin/python -Su\nBOOTSTRAP_HASH=%s\n%s'%(ÂÞÅCAT(ÂÞÅCAT(ÂîÓ,sha),repr),ÂîÓ))('%s\n%s\n%s\n%s'%(pathlib_import,ÂÞÅCAT(header_com,compile_files),ÐÌü(dump_cached_imports),ÐÌü(Æå))))
	if minify:
		if dest:Âçß('Wrote unminified code to %s'%(write_exe((f:=ÐÌü(tmpf)),pyc),))
		(ÄÊPSH(pyc),ÄÊPSH(ÂÞÅCAT(ÄÊPKE(0),minify_py)),(pyc:=ÄÊPKE(0)),ÄÊDEL(2))[2]
	if dest:write_exe(dest,pyc)
	return pyc
def force_reimport_compiler():ÐÌü(__ÄÊIMPORTS__.clear);ÐÌü(TP_CACHE.clear);Âçß('Importing peggle3/rgx_golfatron');(ÄÊPSH(__ÄÊIMPORT__('peggle3/rgx_golfatron',globals(),'↺')),ÄÊPOP(0))[-1];Âçß('Importing text_format');(ÄÊPSH(__ÄÊIMPORT__('text_format',globals(),'↺')),ÄÊPOP(0))[-1];Âçß('Importing peggle3');(ÄÊPSH(__ÄÊIMPORT__('peggle3',globals(),'↺')),ÄÊPOP(0))[-1];Âçß('Importing peggle3/gram_tools');(ÄÊPSH(__ÄÊIMPORT__('peggle3/gram_tools',globals(),'↺')),ÄÊPOP(0))[-1];Âçß('Importing Compiler/gram.data');(ÄÊPSH(__ÄÊIMPORT__('Compiler/gram.data',globals(),'↺')),ÄÊPOP(0))[-1];Âçß('Importing Compiler/generate_operators');(ÄÊPSH(__ÄÊIMPORT__('Compiler/generate_operators',globals(),'↺')),ÄÊPOP(0))[-1];Âçß('Importing Compiler/operator');(ÄÊPSH(__ÄÊIMPORT__('Compiler/operator',globals(),'↺')),ÄÊPOP(0))[-1];Âçß('Importing Compiler/node_types');(ÄÊPSH(__ÄÊIMPORT__('Compiler/node_types',globals(),'↺')),ÄÊPOP(0))[-1];Âçß('Importing Compiler/tree');(ÄÊPSH(__ÄÊIMPORT__('Compiler/tree',globals(),'↺')),ÄÊPOP(0))[-1];Âçß('Importing Compiler/tree_txt');(ÄÊPSH(__ÄÊIMPORT__('Compiler/tree_txt',globals(),'↺')),ÄÊPOP(0))[-1];Âçß('Importing Compiler/expr');(ÄÊPSH(__ÄÊIMPORT__('Compiler/expr',globals(),'↺')),ÄÊPOP(0))[-1];Âçß('Importing Compiler/lambdas');(ÄÊPSH(__ÄÊIMPORT__('Compiler/lambdas',globals(),'↺')),ÄÊPOP(0))[-1];Âçß('Importing Compiler/rewriters');(ÄÊPSH(__ÄÊIMPORT__('Compiler/rewriters',globals(),'↺')),ÄÊPOP(0))[-1];Âçß('Importing Compiler/to_ast');(ÄÊPSH(__ÄÊIMPORT__('Compiler/to_ast',globals(),'↺')),ÄÊPOP(0))[-1];Âçß('Importing Compiler/ast_to_py');(ÄÊPSH(__ÄÊIMPORT__('Compiler/ast_to_py',globals(),'↺')),ÄÊPOP(0))[-1];Âçß('Importing Compiler');(c:=(ÄÊPSH(__ÄÊIMPORT__('Compiler',globals(),'↺')),ÄÊPOP(0))[-1]);TRANSPILE_REF(c.ÄÊmoon_to_py);ÐÌü(show_imports);return c
def generate_bootstrap_live(*áÑË,**áÑÕ):ÐÌü(force_reimport_compiler).generate_bootstrap(áÑË[0]if áÑË else'bootstrap.py',**áÑÕ);Âçß(Åøþáüì('Generated bootstrap!','f0f'))
def moon_cli(extract=False,ia=True,rl=True):
	import traceback
	if ia and rl:import readline;(HIST_FILE:=ÂÞÅCAT(ð(TMPDIR,'☾_cli_history'),mkf));ÂÞÅCAT(ÂÞÅCAT(HIST_FILE,ÁÜÙ),readline.read_history_file)
	(pfx:=Åøþáüì('✝ ','f0a',rl=rl));(ns:=ÄÕôñ(ÁØã))
	def Æå(input):
		(áÖï:=(ÄÊPSH(ns),ÄÊPSH('__moon_code__'),ÄÊPSH(input(*([pfx]if ia else ÂÚü()))),setitem(ÄÊPKE(2),ÄÊPKE(1),ÄÊPKE(0)),ÄÊDEL(3))[3])
		if not áÖï:return Âçß('God is good!')
		if rl:readline.write_history_file(HIST_FILE)
		if áÖï=='clr':return os.system('clear')
		if ia and rl:Âçß('%s\x1b[1A%s\x1b[K'%(pfx,ÂÞÅCAT(áÖï,__highlighter__)))
		else:Âçß(ÂÞÅCAT(áÖï,__highlighter__))
		(áÕÃ:=ÂÞÅCAT(áÖï,compile_code));Âçß(ÂÞÅCAT(ÂÞÅCAT(áÕÃ,VEP),__highlighter__));(ÄÊPSH((False,{'return_err':True})),((s:=ÄÊPKE(0)[0]),(errp:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
		try:return Âçß(ÄÕôñ(áÕÃ,ns,native=True,Æå=eval,ret=True,init_ns=False,show_error_áÑÕ=errp))
		except áÍÚ:pass
		try:return ÄÕôñ(áÕÃ,ns,native=True,Æå=EXEC_NATIVE,ret=True,init_ns=False,show_error_áÑÕ=errp)
		except áÍÚ as Ïã:Âçß(Âøî(ÂÞÅCAT(Ïã,traceback.format_exception),ÁØã))
	if extract:return Æå
	while True:
		try:Æå(input)
		except KeyboardInterrupt as Ðáü:Âçß(ÁØã);ÂÞÅCAT(0,exit)
def try_update_git(tag=None):
	ÂÞÅCAT(moon_dir,cd)
	if ÂÛí(tag):Áëý(ÄÊSUBPROCA('git\u2009fetch\u2009--tags\u2009origin','oeD'),exit);Áëý(ÄÊSUBPROCA('git\u2009checkout\u2009--detach\u2009tags/%s'%(tag,),'oeD'),exit)
	else:Áëý(ÄÊSUBPROCA('git\u2009checkout\u2009master','oeD'),exit);Áëý(ÄÊSUBPROCA('git\u2009pull\u2009origin\u2009master','oeD'),exit)
	(lambda ÂîÓ:os.execv(ÂîÓ,Âêà(ÂîÓ)))(ÂÞÅCAT(ð(moon_dir,'install'),ÁÜÙ))
def transpiler_cli(*áÒø):
	(show_docs:=lambda*áÑË,**áÑÕ:Âçß('Usage:\n  <file_path> <𝔸₀?> <𝔸₁?> …\n     Run ☾ file\n  -o <file_in> <file_out?stdout>\n     Compile file but do not run\n  --get-dir\n     Output ☾ directory\n  --update <tag?>\n     Updates ☾ from git and then installs\n     (Without providing tag it pulls most recent version)\n  ∅                  ∣ CLI mode\n  -h                 ∣ Show this\n  -c <code_to_run>   ∣ Eval mode, output return value + newline\n  -\U000f7c49 <code_to_run>   ∣ Eval mode, output return value\n  -. <code_to_run>   ∣ Eval mode, no return output\n  -C <code_to_run>   ∣ Exec mode, no return output\n  -B <boostrap_dest> ∣ Bootstrap to file\n  -e <str_to_encode> ∣ Escape var name\n  -d <str_to_decode> ∣ Unescape var name'));(ÄÊPSH(([*áÒø],ÂÔð())),((áÒø:=ÄÊPKE(0)[0]),(f:=ÄÊPKE(0)[1])),ÄÊDEL(1))[1]
	while áÒø and(áÓÓ:=áÒø[0])[0]=='-':
		if not ÂåÔ((ÄÊPSH(f),ÄÊPSH(ÂÕØ(ÄÊPKE(0),(lambda ÂîÓ:[ÂîÓ[slice(1,None)]]if ÂîÓ[0]=='-'else ÂîÓ)(ÂÞÅCAT(0,áÒø.pop)[slice(1,None)]))),(f:=ÄÊPKE(0)),ÄÊDEL(2))[2],áÓÓ!=2*'-'):continue
		None
	if'R'in f:ÐÌü(ÄÊdo_imps);ÐÌü(force_reimport_compiler)
	(Æå:=moon_to_py if not ÂÕÖ('aA',f)else ÂåÔ(ÐÌü(ÄÊdo_imps),lambda*áÑË,**áÑÕ:moon_to_py_debug(*áÑË,**áÑÕ,show_preast=ÂÔö(f,'A'))))
	if(ÄÊDEL(1),False)[1]if ÄÊPSH(f)else ÄÊPOP(0)if áÒø else(ÄÊDEL(1),True)[1]:ÂåÔ(ÐÌü(ÄÊdo_imps),ÐÌü(moon_cli))
	elif(ÄÊDEL(1),False)[1]if ÄÊPSH(f)else ÄÊPOP(0)if not ãÊú(áÒø)else(ÄÊDEL(1),True)[1]:ÂÞÅCAT(0,áÑË.pop);return ÄÕôñ(ÂÞÅCAT(áÒø[0],ÐØó),ns={'__file__':áÒø[0],'__dir__':ÂÞÅCAT(áÒø[0],áÌî).parent,'__name__':'__main__'},Æå=lambda x,y:EXEC_NATIVE(x,y,y))
	elif ÂÔö(f,'h'):ÐÌü(show_docs)
	elif ÂÔö(f,'get-dir'):Âçß(moon_dir)
	elif ÂÔö(f,'update'):try_update_git(*áÒø)
	elif ÂÔö(f,'.'):ÂÞÅCAT(ÂÞÅCAT(Âøî(áÒø,' '),Æå),eval)
	elif ÂÔö(f,'c'):(lambda ÂîÓ:MOD(Áëý,áØÁ=ÂÛí)(ÂîÓ,Âçß))(ÂÞÅCAT(ÂÞÅCAT(Âøî(áÒø,' '),Æå),eval))
	elif ÂÔö(f,'\U000f7c49'):(lambda ÂîÓ:MOD(Áëý,áØÁ=ÂÛí)(ÂîÓ,MOD(Âçß,áØÁ=ÁØã)))(ÂÞÅCAT(ÂÞÅCAT(Âøî(áÒø,' '),Æå),eval))
	elif ÂÔö(f,'C'):ÂÞÅCAT(ÂÞÅCAT(Âøî(áÒø,' '),Æå),EXEC_NATIVE)
	else:
		ÐÌü(ÄÊdo_imps)
		if ÂÔö(f,'D'):
			(x:=ÂÚü())
			while True:
				try:ÂÞÅCAT(ÐÌü(input),x.append)
				except EOFError as Ðáü:break
			Âçß(Âøî(Áÿú(x,Âåæ(__highlighter__,VEP)),'\n'))
		elif ÂÔö(f,'d'):Âçß(ÂÞÅCAT(Âøî(Áÿú(áÒø,VEP),' '),__highlighter__))
		elif ÂÔö(f,'e'):Âçß(Âøî(Áÿú(áÒø,PEV),' '))
		elif ÂÔö(f,'B'):ÂÞÅCAT(ÂÞÅCAT(áÒø[0],áÌî),generate_bootstrap_live)
		elif ÂÔö(f,'b'):ÂÞÅCAT(ÂÞÅCAT(áÒø[0],áÌî),generate_bootstrap)
		elif ÂÔö(f,'o'):ÐôÅ(Ááú(áÒø,[0,1,2]),lambda x:ÂÞÅCAT(compile_code(ÂÞÅCAT(x[0],ÐØó),Æå=Æå),ÄÊCUR((2,),{},ÐØì,x[1],ÂýÃ)if x[1]else Âçß))
		else:ÂåÔ(Âçß('Invalid mode(s): %s'%(f,)),ÐÌü(show_docs))
__ÄÊADD_EXPORTS__(globals(),('minify_py',minify_py),('moon_to_py',moon_to_py),('moon_to_py_debug',moon_to_py_debug),('compile_files',compile_files),('generate_bootstrap',generate_bootstrap),('transpiler_cli',transpiler_cli),('moon_cli',moon_cli))
TRANSPILE_REF(moon_to_py)
if __name__=='__main__':transpiler_cli(*áÑË[slice(1,None)])
else:ÐÌü(ÄÊdo_imps)