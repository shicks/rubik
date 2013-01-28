from d3 import *
from cube import *

Flower = Cube()

class FlowerBlock(Block):
  def __init__(self, name, cube = Flower):
    super(FlowerBlock, self).__init__(name, D3.e0, cube)
  def type(self):
    return ' FEV'[len(self.name)]
  def showOrientation(self, orientation):
    return ''
  def at(self, orient):
    return self

# Center blocks
F = FlowerBlock('F')
B = FlowerBlock('B')
U = FlowerBlock('U')
D = FlowerBlock('D')
L = FlowerBlock('L')
R = FlowerBlock('R')
# Edge blocks
FU = FlowerBlock('FU')
FD = FlowerBlock('FD')
FL = FlowerBlock('FL')
FR = FlowerBlock('FR')
BU = FlowerBlock('BU')
BD = FlowerBlock('BD')
BL = FlowerBlock('BL')
BR = FlowerBlock('BR')
UL = FlowerBlock('UL')
UR = FlowerBlock('UR')
DL = FlowerBlock('DL')
DR = FlowerBlock('DR')

# Corner blocks
Ful = FlowerBlock('Ful')
Fur = FlowerBlock('Fur')
Fdl = FlowerBlock('Fdl')
Fdr = FlowerBlock('Fdr')
Bul = FlowerBlock('Bul')
Bur = FlowerBlock('Bur')
Bdl = FlowerBlock('Bdl')
Bdr = FlowerBlock('Bdr')

fUl = FlowerBlock('fUl')
fUr = FlowerBlock('fUr')
bUl = FlowerBlock('bUl')
bUr = FlowerBlock('bUr')
fDl = FlowerBlock('fDl')
fDr = FlowerBlock('fDr')
bDl = FlowerBlock('bDl')
bDr = FlowerBlock('bDr')

fuL = FlowerBlock('fuL')
fdL = FlowerBlock('fdL')
buL = FlowerBlock('buL')
bdL = FlowerBlock('bdL')
fuR = FlowerBlock('fuR')
fdR = FlowerBlock('fdR')
buR = FlowerBlock('buR')
bdR = FlowerBlock('bdR')

# Must be defined after all blocks
Flower.e = Permutation(Flower).named('e')

# Full-cube rotations
OF = (cycle(U, L, D, R)
      * cycle(Fdl, Fdr, Fur, Ful) * cycle(Bdl, Bdr, Bur, Bul)
      * cycle(fUl, fdL, fDr, fuR) * cycle(fUr, fuL, fDl, fdR)
      * cycle(bUl, bdL, bDr, buR) * cycle(bUr, buL, bDl, bdR)
      * cycle(FL, FD.at(D3.F), FR, FU.at(D3.F))
      * cycle(BL, BD.at(D3.F), BR, BU.at(D3.F))
      * cycle(UR, UL.at(D3.F), DL, DR.at(D3.F))).named('OF')
OB = OF.inv().named('OB')
OU = (cycle(F, R, B, L)
      * cycle(fUl, fUr, bUr, bUl) * cycle(fDl, fDr, bDr, bDl)
      * cycle(Ful, fuR, Bur, buL) * cycle(Fur, buR, Bul, fuL)
      * cycle(Fdl, fdR, Bdr, bdL) * cycle(Fdr, bdR, Bdl, fdL)
      * cycle(FU, UR.at(D3.U), BU, UL.at(D3.U))
      * cycle(FD, DR.at(D3.U), BD, DL.at(D3.U))
      * cycle(FL, FR.at(D3.F), BR, BL.at(D3.F))).named('OU')
OD = OU.inv().named('OD')
OL = (OD * OF * OU).named('OL')
OR = OL.inv().named('OR')

# Operations
# We number the corners in binary:
#  0 = 000 = FUL
#  1 = 001 = FUR
#  2 = 010 = FDL
#  ...
#  7 = 111 = BDR

R0 = (cycle(F, U, L) * cycle(Ful, fUl, fuL)
      * cycle(Fdl, fUr, buL) * cycle(Fur, bUl, fdL)
      * cycle(FL, FU.at(D3.e1), UL.at(D3.e2))).named('R0')
L0 = R0.inv().named('L0') # left-hand rotation about FUL

R1 = (OU * R0 * OD).named('R1')
L1 = R1.inv().named('L1')

R2 = (OR * R0 * OL).named('R2')
L2 = R2.inv().named('L2')

R3 = (OR * R1 * OL).named('R3')
L3 = R3.inv().named('L3')

R4 = (OL * R0 * OR).named('R4')
L4 = R4.inv().named('L4')

R5 = (OL * R1 * OR).named('R5')
L5 = R5.inv().named('L5')

R6 = (OR * R2 * OL).named('R6')
L6 = R6.inv().named('L6')

R7 = (OR * R3 * OL).named('R7')
L7 = R7.inv().named('L7')

# Quick check that all the basic permutations are likely correct.
assert str(R1*R1*R1) == '()'
assert str(OD*OL*OU*OF) == '()'

# Additional permutations

rotate_petals1 = cat(R0,L5,L0,R5)
rotate_petals2 = cat(L0,R3,R0,L3)
swap_petals = cat(rotate_petals1, rotate_petals2)
swap_faces = cat(R0,L5,L0,R5, L2,R7,R2,L7, L5,R0,R5,L0, R7,L2,L7,R2)
