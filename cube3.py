from d3 import *
from cube import *

Cube3 = Cube()

# Corner blocks
FUL = Block('FUL', D3.e0, Cube3)
FUR = Block('FUR', D3.e0, Cube3)
FDL = Block('FDL', D3.e0, Cube3)
FDR = Block('FDR', D3.e0, Cube3)
BUL = Block('BUL', D3.e0, Cube3)
BUR = Block('BUR', D3.e0, Cube3)
BDL = Block('BDL', D3.e0, Cube3)
BDR = Block('BDR', D3.e0, Cube3)

# Edge blocks
FU_ = Block('FU_', D3.e0, Cube3)
F_L = Block('F_L', D3.e0, Cube3)
F_R = Block('F_R', D3.e0, Cube3)
FD_ = Block('FD_', D3.e0, Cube3)
_UL = Block('_UL', D3.e0, Cube3)
_UR = Block('_UR', D3.e0, Cube3)
_DL = Block('_DL', D3.e0, Cube3)
_DR = Block('_DR', D3.e0, Cube3)
BU_ = Block('BU_', D3.e0, Cube3)
B_L = Block('B_L', D3.e0, Cube3)
B_R = Block('B_R', D3.e0, Cube3)
BD_ = Block('BD_', D3.e0, Cube3)

# Face blocks
F__ = Block('F__', D3.e0, Cube3)
B__ = Block('B__', D3.e0, Cube3)
_U_ = Block('_U_', D3.e0, Cube3)
_D_ = Block('_D_', D3.e0, Cube3)
__L = Block('__L', D3.e0, Cube3)
__R = Block('__R', D3.e0, Cube3)

# Must be defined after all blocks
Cube3.e = Permutation(Cube3).named('e')

# Operations
Bf = (cycle(FUL, FUR.at(D3.F), FDR, FDL.at(D3.F))
      * cycle(FU_, F_R.at(D3.F), FD_, F_L.at(D3.F))).named('Bf')
Bm = (cycle(_UL, _UR.at(D3.F), _DR, _DL.at(D3.F))
      * cycle(_U_, __R, _D_, __L)).named('Bm')
Bb = (cycle(BUL, BUR.at(D3.F), BDR, BDL.at(D3.F))
      * cycle(BU_, B_R.at(D3.F), BD_, B_L.at(D3.F))).named('Bb')
Ff = Bf.inv().named('Ff')
Fm = Bm.inv().named('Fm')
Fb = Bb.inv().named('Fb')

Ur = (cycle(FUR, BUR.at(D3.L), BDR, FDR.at(D3.L))
      * cycle(_UR, B_R.at(D3.L), _DR, F_R.at(D3.L))).named('Ur')
Um = (cycle(FU_, BU_.at(D3.L), BD_, FD_.at(D3.L))
      * cycle(_U_, B__, _D_, F__)).named('Um')
Ul = (cycle(FUL, BUL.at(D3.L), BDL, FDL.at(D3.L))
      * cycle(_UL, B_L.at(D3.L), _DL, F_L.at(D3.L))).named('Ul')
Dr = Ur.inv().named('Dr')
Dm = Um.inv().named('Dm')
Dl = Ul.inv().named('Dl')

Ru = (cycle(FUL, FUR.at(D3.U), BUR, BUL.at(D3.U))
      * cycle(FU_, _UR.at(D3.U), BU_, _UL.at(D3.U))).named('Ru')
Rm = (cycle(F_L, F_R.at(D3.U), B_R, B_L.at(D3.U))
      * cycle(F__, __R, B__, __L)).named('Rm')
Rd = (cycle(FDL, FDR.at(D3.U), BDR, BDL.at(D3.U))
      * cycle(FD_, _DR.at(D3.U), BD_, _DL.at(D3.U))).named('Rd')
Lu = Ru.inv().named('Lu')
Lm = Rm.inv().named('Lm')
Ld = Rd.inv().named('Ld')

OF = (Ff*Fm*Fb).named('OF')
OU = (Ru*Rm*Rd).named('OU')
OR = (Dr*Dm*Dl).named('OR')
OB = (OF.inv()).named('OB')
OD = (OU.inv()).named('OD')
OL = (OR.inv()).named('OL')

# Quick check that all the basic permutations are likely correct.
assert str(OD*OL*OU*OF) == '()'

# Additional permutations

seven = cat(Dr, Rd, Ur, Rd, Bf, Ld, Ff)
sevenI = seven.inv()

c1r = cat(Dr, Rd, Ur, Ld)
c1l = cat(Dr, Ld, Ur, Rd) # this is useful for swapping corners
c2r = cat(Bf, Rd, Ff, Ld)
c2l = cat(Bf, Ld, Ff, Rd)

Um1R = cat(Um, Ru, Dm, Ru**2, Um, Ru, Dm)
Um1L = cat(Um, Lu, Dm, Lu**2, Um, Lu, Dm)
Um2R = cat(Um, Ru, Dm, Ru, Um, Ru**2, Dm)
Um2L = cat(Um, Lu, Dm, Lu, Um, Lu**2, Dm)
Um3R = cat(Um, Ru**2, Dm, Ru, Um, Ru, Dm)
Um3L = cat(Um, Lu**2, Dm, Lu, Um, Lu, Dm)
