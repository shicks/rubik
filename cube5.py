from d3 import *
from cube import *

Cube5 = Cube()

# Corner blocks
FUL = Block('FUL', D3.e0, Cube5)
FUR = Block('FUR', D3.e0, Cube5)
FDL = Block('FDL', D3.e0, Cube5)
FDR = Block('FDR', D3.e0, Cube5)
BUL = Block('BUL', D3.e0, Cube5)
BUR = Block('BUR', D3.e0, Cube5)
BDL = Block('BDL', D3.e0, Cube5)
BDR = Block('BDR', D3.e0, Cube5)

# Edge blocks
FUl = Block('FUl', D3.e0, Cube5) # FU
FU_ = Block('FU_', D3.e0, Cube5)
FUr = Block('FUr', D3.e0, Cube5)
FuL = Block('FuL', D3.e0, Cube5) # FL
F_L = Block('F_L', D3.e0, Cube5)
FdL = Block('FdL', D3.e0, Cube5)
FuR = Block('FuR', D3.e0, Cube5) # FR
F_R = Block('F_R', D3.e0, Cube5)
FdR = Block('FdR', D3.e0, Cube5)
FDl = Block('FDl', D3.e0, Cube5) # FD
FD_ = Block('FD_', D3.e0, Cube5)
FDr = Block('FDr', D3.e0, Cube5)
fUL = Block('fUL', D3.e0, Cube5) # UL
_UL = Block('_UL', D3.e0, Cube5)
bUL = Block('bUL', D3.e0, Cube5)
fUR = Block('fUR', D3.e0, Cube5) # UR
_UR = Block('_UR', D3.e0, Cube5)
bUR = Block('bUR', D3.e0, Cube5)
fDL = Block('fDL', D3.e0, Cube5) # DL
_DL = Block('_DL', D3.e0, Cube5)
bDL = Block('bDL', D3.e0, Cube5)
fDR = Block('fDR', D3.e0, Cube5) # DR
_DR = Block('_DR', D3.e0, Cube5)
bDR = Block('bDR', D3.e0, Cube5)
BUl = Block('BUl', D3.e0, Cube5) # BU
BU_ = Block('BU_', D3.e0, Cube5)
BUr = Block('BUr', D3.e0, Cube5)
BuL = Block('BuL', D3.e0, Cube5) # BL
B_L = Block('B_L', D3.e0, Cube5)
BdL = Block('BdL', D3.e0, Cube5)
BuR = Block('BuR', D3.e0, Cube5) # BR
B_R = Block('B_R', D3.e0, Cube5)
BdR = Block('BdR', D3.e0, Cube5)
BDl = Block('BDl', D3.e0, Cube5) # BD
BD_ = Block('BD_', D3.e0, Cube5)
BDr = Block('BDr', D3.e0, Cube5)

# Face blocks
Ful = Block('Ful', D3.e0, Cube5) # F
Fu_ = Block('Fu_', D3.e0, Cube5)
Fur = Block('Fur', D3.e0, Cube5)
Fdl = Block('Fdl', D3.e0, Cube5)
Fd_ = Block('Fd_', D3.e0, Cube5)
Fdr = Block('Fdr', D3.e0, Cube5)
F_l = Block('F_l', D3.e0, Cube5)
F__ = Block('F__', D3.e0, Cube5)
F_r = Block('F_r', D3.e0, Cube5)
Bul = Block('Bul', D3.e0, Cube5) # B
Bu_ = Block('Bu_', D3.e0, Cube5)
Bur = Block('Bur', D3.e0, Cube5)
Bdl = Block('Bdl', D3.e0, Cube5)
Bd_ = Block('Bd_', D3.e0, Cube5)
Bdr = Block('Bdr', D3.e0, Cube5)
B_l = Block('B_l', D3.e0, Cube5)
B__ = Block('B__', D3.e0, Cube5)
B_r = Block('B_r', D3.e0, Cube5)
fUl = Block('fUl', D3.e0, Cube5) # U
_Ul = Block('_Ul', D3.e0, Cube5)
bUl = Block('bUl', D3.e0, Cube5)
fU_ = Block('fU_', D3.e0, Cube5)
_U_ = Block('_U_', D3.e0, Cube5)
bU_ = Block('bU_', D3.e0, Cube5)
fUr = Block('fUr', D3.e0, Cube5)
_Ur = Block('_Ur', D3.e0, Cube5)
bUr = Block('bUr', D3.e0, Cube5)
fDl = Block('fDl', D3.e0, Cube5) # D
_Dl = Block('_Dl', D3.e0, Cube5)
bDl = Block('bDl', D3.e0, Cube5)
fD_ = Block('fD_', D3.e0, Cube5)
_D_ = Block('_D_', D3.e0, Cube5)
bD_ = Block('bD_', D3.e0, Cube5)
fDr = Block('fDr', D3.e0, Cube5)
_Dr = Block('_Dr', D3.e0, Cube5)
bDr = Block('bDr', D3.e0, Cube5)
fuL = Block('fuL', D3.e0, Cube5) # L
_uL = Block('_uL', D3.e0, Cube5)
buL = Block('buL', D3.e0, Cube5)
fdL = Block('fdL', D3.e0, Cube5)
_dL = Block('_dL', D3.e0, Cube5)
bdL = Block('bdL', D3.e0, Cube5)
f_L = Block('f_L', D3.e0, Cube5)
__L = Block('__L', D3.e0, Cube5)
b_L = Block('b_L', D3.e0, Cube5)
fuR = Block('fuR', D3.e0, Cube5) # R
_uR = Block('_uR', D3.e0, Cube5)
buR = Block('buR', D3.e0, Cube5)
fdR = Block('fdR', D3.e0, Cube5)
_dR = Block('_dR', D3.e0, Cube5)
bdR = Block('bdR', D3.e0, Cube5)
f_R = Block('f_R', D3.e0, Cube5)
__R = Block('__R', D3.e0, Cube5)
b_R = Block('b_R', D3.e0, Cube5)

# Must be defined after all blocks
Cube5.e = Permutation(Cube5).named('e')

# Operations
Bff = (cycle(FUL, FUR.at(D3.F), FDR, FDL.at(D3.F))
       * cycle(FUl, FuR.at(D3.F), FDr, FdL.at(D3.F))
       * cycle(FU_, F_R.at(D3.F), FD_, F_L.at(D3.F))
       * cycle(FUr, FdR.at(D3.F), FDl, FuL.at(D3.F))
       * cycle(Ful, Fur, Fdr, Fdl)
       * cycle(Fu_, F_r, Fd_, F_l)).named('Bff')
Bf = (cycle(fUL, fUR.at(D3.F), fDR, fDL.at(D3.F))
      * cycle(fUl, fuR, fDr, fdL)
      * cycle(fU_, f_R, fD_, f_L)
      * cycle(fUr, fdR, fDl, fuL)).named('Bf')
Bm = (cycle(_UL, _UR.at(D3.F), _DR, _DL.at(D3.F))
      * cycle(_Ul, _uR, _Dr, _dL)
      * cycle(_U_, __R, _D_, __L)
      * cycle(_Ur, _dR, _Dl, _uL)).named('Bm')
Bb = (cycle(bUL, bUR.at(D3.F), bDR, bDL.at(D3.F))
      * cycle(bUl, buR, bDr, bdL)
      * cycle(bU_, b_R, bD_, b_L)
      * cycle(bUr, bdR, bDl, buL)).named('Bb')
Bbb = (cycle(BUL, BUR.at(D3.F), BDR, BDL.at(D3.F))
       * cycle(BUl, BuR.at(D3.F), BDr, BdL.at(D3.F))
       * cycle(BU_, B_R.at(D3.F), BD_, B_L.at(D3.F))
       * cycle(BUr, BdR.at(D3.F), BDl, BuL.at(D3.F))
       * cycle(Bul, Bur, Bdr, Bdl)
       * cycle(Bu_, B_r, Bd_, B_l)).named('Bbb')
Fff = Bff.inv().named('Fff')
Ff = Bf.inv().named('Ff')
Fm = Bm.inv().named('Fm')
Fb = Bb.inv().named('Fb')
Fbb = Bbb.inv().named('Fbb')

Urr = (cycle(FUR, BUR.at(D3.L), BDR, FDR.at(D3.L))
       * cycle(fUR, BuR.at(D3.L), bDR, FdR.at(D3.L))
       * cycle(_UR, B_R.at(D3.L), _DR, F_R.at(D3.L))
       * cycle(bUR, BdR.at(D3.L), fDR, FuR.at(D3.L))
       * cycle(fuR, buR, bdR, fdR)
       * cycle(f_R, _uR, b_R, _dR)).named('Urr')
Ur = (cycle(FUr, BUr.at(D3.L), BDr, FDr.at(D3.L))
      * cycle(fUr, Bur, bDr, Fdr)
      * cycle(_Ur, B_r, _Dr, F_r)
      * cycle(bUr, Bdr, fDr, Fur)).named('Ur')
Um = (cycle(FU_, BU_.at(D3.L), BD_, FD_.at(D3.L))
      * cycle(fU_, Bu_, bD_, Fd_)
      * cycle(_U_, B__, _D_, F__)
      * cycle(bU_, Bd_, fD_, Fu_)).named('Um')
Ul = (cycle(FUl, BUl.at(D3.L), BDl, FDl.at(D3.L))
      * cycle(fUl, Bul, bDl, Fdl)
      * cycle(_Ul, B_l, _Dl, F_l)
      * cycle(bUl, Bdl, fDl, Ful)).named('Ul')
Ull = (cycle(FUL, BUL.at(D3.L), BDL, FDL.at(D3.L))
       * cycle(fUL, BuL.at(D3.L), bDL, FdL.at(D3.L))
       * cycle(_UL, B_L.at(D3.L), _DL, F_L.at(D3.L))
       * cycle(bUL, BdL.at(D3.L), fDL, FuL.at(D3.L))
       * cycle(fuL, buL, bdL, fdL)
       * cycle(f_L, _uL, b_L, _dL)).named('Ull')
Drr = Urr.inv().named('Drr')
Dr = Ur.inv().named('Dr')
Dm = Um.inv().named('Dm')
Dl = Ul.inv().named('Dl')
Dll = Ull.inv().named('Dll')

Ruu = (cycle(FUL, FUR.at(D3.U), BUR, BUL.at(D3.U))
       * cycle(FUl, fUR.at(D3.U), BUr, bUL.at(D3.U))
       * cycle(FU_, _UR.at(D3.U), BU_, _UL.at(D3.U))
       * cycle(FUr, bUR.at(D3.U), BUl, fUL.at(D3.U))
       * cycle(fUl, fUr, bUr, bUl)
       * cycle(fU_, _Ur, bU_, _Ul)).named('Ruu')
Ru = (cycle(FuL, FuR.at(D3.U), BuR, BuL.at(D3.U))
      * cycle(Ful, fuR, Bur, buL)
      * cycle(Fu_, _uR, Bu_, _uL)
      * cycle(Fur, buR, Bul, fuL)).named('Ru')
Rm = (cycle(F_L, F_R.at(D3.U), B_R, B_L.at(D3.U))
      * cycle(F_l, f_R, B_r, b_L)
      * cycle(F__, __R, B__, __L)
      * cycle(F_r, b_R, B_l, f_L)).named('Rm')
Rd = (cycle(FdL, FdR.at(D3.U), BdR, BdL.at(D3.U))
      * cycle(Fdl, fdR, Bdr, bdL)
      * cycle(Fd_, _dR, Bd_, _dL)
      * cycle(Fdr, bdR, Bdl, fdL)).named('Rd')
Rdd = (cycle(FDL, FDR.at(D3.U), BDR, BDL.at(D3.U))
       * cycle(FDl, fDR.at(D3.U), BDr, bDL.at(D3.U))
       * cycle(FD_, _DR.at(D3.U), BD_, _DL.at(D3.U))
       * cycle(FDr, bDR.at(D3.U), BDl, fDL.at(D3.U))
       * cycle(fD_, _Dr, bD_, _Dl)
       * cycle(fDl, fDr, bDr, bDl)).named('Rdd')
Luu = Ruu.inv().named('Luu')
Lu = Ru.inv().named('Lu')
Lm = Rm.inv().named('Lm')
Ld = Rd.inv().named('Ld')
Ldd = Rdd.inv().named('Ldd')

OF = (Fff*Ff*Fm*Fb*Fbb).named('OF')
OU = (Ruu*Ru*Rm*Rd*Rdd).named('OU')
OR = (Drr*Dr*Dm*Dl*Dll).named('OR')
OB = (OF.inv()).named('OB')
OD = (OU.inv()).named('OD')
OL = (OR.inv()).named('OL')

# Quick check that all the basic permutations are likely correct.
assert str(OD*OL*OU*OF) == '()'

# Additional permutations

seven = cat(Drr, Rdd, Urr, Rdd, Bff, Ldd, Fff)
sevenI = seven.inv()
Ur1R = cat(Ur, Ruu, Dr, Ruu**2, Ur, Ruu, Dr)
Ur1L = cat(Ur, Luu, Dr, Luu**2, Ur, Luu, Dr)
Um1R = cat(Um, Ruu, Dm, Ruu**2, Um, Ruu, Dm)
Um1L = cat(Um, Luu, Dm, Luu**2, Um, Luu, Dm)
Ul1R = cat(Ul, Ruu, Dl, Ruu**2, Ul, Ruu, Dl)
Ul1L = cat(Ul, Luu, Dl, Luu**2, Ul, Luu, Dl)

Ur2R = cat(Ur, Ruu, Dr, Ruu, Ur, Ruu**2, Dr)
Ur2L = cat(Ur, Luu, Dr, Luu, Ur, Luu**2, Dr)
Um2R = cat(Um, Ruu, Dm, Ruu, Um, Ruu**2, Dm)
Um2L = cat(Um, Luu, Dm, Luu, Um, Luu**2, Dm)
Ul2R = cat(Ul, Ruu, Dl, Ruu, Ul, Ruu**2, Dl)
Ul2L = cat(Ul, Luu, Dl, Luu, Ul, Luu**2, Dl)

Ur3R = cat(Ur, Ruu**2, Dr, Ruu, Ur, Ruu, Dr)
Ur3L = cat(Ur, Luu**2, Dr, Luu, Ur, Luu, Dr)
Um3R = cat(Um, Ruu**2, Dm, Ruu, Um, Ruu, Dm)
Um3L = cat(Um, Luu**2, Dm, Luu, Um, Luu, Dm)
Ul3R = cat(Ul, Ruu**2, Dl, Ruu, Ul, Ruu, Dl)
Ul3L = cat(Ul, Luu**2, Dl, Luu, Ul, Luu, Dl)

# First attempt at moving middles/edges
Mfr = cat(Um, Ruu, Dm, Luu, Fff, Um, Luu, Dm, Ruu, Bff)
Mbr = cat(Um, Ruu, Dm, Luu, Bff, Um, Luu, Dm, Ruu, Fff)
Mfl = cat(Um, Luu, Dm, Ruu, Fff, Um, Ruu, Dm, Luu, Bff)
Mbl = cat(Um, Luu, Dm, Ruu, Bff, Um, Ruu, Dm, Luu, Fff)

face = lambda b:b.type() == 'F' and '_' not in b.name
FACE = lambda b:b.type() == 'F' and '_' in b.name
edge = lambda b:b.type() == 'E' and '_' not in b.name
EDGE = lambda b:b.type() == 'E' and '_' in b.name

# Attempt to move middle faces
#MrR = cat(Ur, Ruu, Dm, Luu, Dr, Ruu, Um, Luu)
#MrL = cat(Ur, Luu, Dm, Ruu, Dr, Luu, Um, Ruu)
#MlR = cat(Ul, Ruu, Dm, Luu, Dl, Ruu, Um, Luu)
#MlL = cat(Ul, Luu, Dm, Ruu, Dl, Luu, Um, Ruu)

# This move puts F_l into bU_ (and messes up F a bit)
#M1 = cat(Dm, Luu, Ur, Ruu, Um, Luu, Dr, Ruu**2, Ul, Luu, Dm, Ruu, Dl, Luu, Um)

# Move middles last:
# (Fu_ F_r _Ur)
M1 = cat(Ur, Ruu, Um, Luu, Dr, Ruu, Dm, Luu
# (Fur bUr Ful)
R1 = cat(Ur, Ruu, Ul, Luu, Dr, Ruu, Dl, Luu)

#####
# How to permute edges more easily (no worry of faces)
# Um1r flips _UR and BU_, then M1:

# does some flips... :-/ also not localized to one face yet
#R1 = cat(Ruu, Ur, Ruu**2, Ul, Ruu**2, Dl, Ruu**2, Dr, Ruu)

# This one is long and messy, but does a pair of opposite swaps
# (FUr BUl) (fUL, bUR)
Rswap = cat(Ff, Drr**2, Rdd, Dr, Rdd**2, Ul, Rdd**2, Ur, Rdd**2, Dl, Rdd, Urr**2, Bf)


### Principle: find a move that does even close to what we want
### then move what we need into place (flips are okay if the pre/post
### moves flip, too)
Mtri = cat(Fbb**2, Ruu, Dm, Ruu**2, Um, Ruu, Fbb**2) # no flips!!!
Ltri = cat(Ur, Ruu, Dl, Ruu**2, Dr, Ruu**2, Ur, Ruu**2, Ul, Ruu, Dr)
Rtri = cat(Ul, Ruu, Dr, Ruu**2, Dl, Ruu**2, Ul, Ruu**2, Ur, Ruu, Dl)
