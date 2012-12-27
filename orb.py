# Defines The Orb puzzle (aka Orb-It), which has 4 circular
# channels of differently-colored beads, and can be turned
# 48 degrees through its diameter to line up different
# channels.  The top and bottom channels have 8 beads each,
# while the middle two channels have twenty.  We name the
# beads by the channel (T, t, b, B) and the half (L, R),
# and then a number where 0 is front and 3 or 9 is back.

from identity import I
from cube import *

# TODO(sdh): make this a superclass of Cubie
class Bead(Block):
  def __init__(self, *args):
    super(Bead, self).__init__(*args)
  def type(self):
    return ''
  def showOrientation(self, orientation):
    return ''
  def at(self, orient):
    return self

Orb = Cube()

# Top channel
TL0 = Bead('TL0', I.e0, Orb)
TL1 = Bead('TL1', I.e0, Orb)
TL2 = Bead('TL2', I.e0, Orb)
TL3 = Bead('TL3', I.e0, Orb)
TR3 = Bead('TR3', I.e0, Orb)
TR2 = Bead('TR2', I.e0, Orb)
TR1 = Bead('TR1', I.e0, Orb)
TR0 = Bead('TR0', I.e0, Orb)

# Top-middle channel
tl0 = Bead('tl0', I.e0, Orb)
tl1 = Bead('tl1', I.e0, Orb)
tl2 = Bead('tl2', I.e0, Orb)
tl3 = Bead('tl3', I.e0, Orb)
tl4 = Bead('tl4', I.e0, Orb)
tl5 = Bead('tl5', I.e0, Orb)
tl6 = Bead('tl6', I.e0, Orb)
tl7 = Bead('tl7', I.e0, Orb)
tl8 = Bead('tl8', I.e0, Orb)
tl9 = Bead('tl9', I.e0, Orb)
tr9 = Bead('tr9', I.e0, Orb)
tr8 = Bead('tr8', I.e0, Orb)
tr7 = Bead('tr7', I.e0, Orb)
tr6 = Bead('tr6', I.e0, Orb)
tr5 = Bead('tr5', I.e0, Orb)
tr4 = Bead('tr4', I.e0, Orb)
tr3 = Bead('tr3', I.e0, Orb)
tr2 = Bead('tr2', I.e0, Orb)
tr1 = Bead('tr1', I.e0, Orb)
tr0 = Bead('tr0', I.e0, Orb)

# Bottom-middle channel
bl0 = Bead('bl0', I.e0, Orb)
bl1 = Bead('bl1', I.e0, Orb)
bl2 = Bead('bl2', I.e0, Orb)
bl3 = Bead('bl3', I.e0, Orb)
bl4 = Bead('bl4', I.e0, Orb)
bl5 = Bead('bl5', I.e0, Orb)
bl6 = Bead('bl6', I.e0, Orb)
bl7 = Bead('bl7', I.e0, Orb)
bl8 = Bead('bl8', I.e0, Orb)
bl9 = Bead('bl9', I.e0, Orb)
br9 = Bead('br9', I.e0, Orb)
br8 = Bead('br8', I.e0, Orb)
br7 = Bead('br7', I.e0, Orb)
br6 = Bead('br6', I.e0, Orb)
br5 = Bead('br5', I.e0, Orb)
br4 = Bead('br4', I.e0, Orb)
br3 = Bead('br3', I.e0, Orb)
br2 = Bead('br2', I.e0, Orb)
br1 = Bead('br1', I.e0, Orb)
br0 = Bead('br0', I.e0, Orb)

# Bottom channel
BL0 = Bead('BL0', I.e0, Orb)
BL1 = Bead('BL1', I.e0, Orb)
BL2 = Bead('BL2', I.e0, Orb)
BL3 = Bead('BL3', I.e0, Orb)
BR3 = Bead('BR3', I.e0, Orb)
BR2 = Bead('BR2', I.e0, Orb)
BR1 = Bead('BR1', I.e0, Orb)
BR0 = Bead('BR0', I.e0, Orb)

# Must be defined after all blocks
Orb.e = Permutation(Orb).named('e')

# Fragments for building cycles
TRu = [TR0, TR1, TR2, TR3]
TRd = list(reversed(TRu))
TLd = [TL0, TL1, TL2, TL3]
TLu = list(reversed(TLd))

tru = [tr0, tr1, tr2, tr3, tr4, tr5, tr6, tr7, tr8, tr9]
trd = list(reversed(tru))
tld = [tl0, tl1, tl2, tl3, tl4, tl5, tl6, tl7, tl8, tl9]
tlu = list(reversed(tld))

bru = [br0, br1, br2, br3, br4, br5, br6, br7, br8, br9]
brd = list(reversed(bru))
bld = [bl0, bl1, bl2, bl3, bl4, bl5, bl6, bl7, bl8, bl9]
blu = list(reversed(bld))

BRu = [BR0, BR1, BR2, BR3]
BRd = list(reversed(BRu))
BLd = [BL0, BL1, BL2, BL3]
BLu = list(reversed(BLd))

# Basic Operations
UT = cycle(*(TRu + TLu)).named('UT')
DT = UT.inv().named('DT')

Ut = cycle(*(tru + tlu)).named('Ut')
Dt = Ut.inv().named('Dt')

Ub = cycle(*(bru + blu)).named('Ub')
Db = Ub.inv().named('Db')

UB = cycle(*(BRu + BLu)).named('UB')
DB = UB.inv().named('DB')

# We hold the left side fixed and rotate the right side up
# the given number of times, then rotate the beads through
# the given u/d axis on the left side (top channel if omitted)
U1 = cycle(*(TLu + tru + blu + BRu + BLd + brd + tld + TRd)).named('U1')
D1 = U1.inv().named('D1')

UT2 = cycle(*(TLu + bru + BLd + trd)).named('UT2')
DT2 = UT2.inv().named('DT2')
Ut2 = cycle(*(tlu + BRu + bld + TRd)).named('Ut2')
Dt2 = Ut2.inv().named('Dt2')

U7 = cycle(*(TLu + TRd + tld + brd + BLd + BRu + blu + tru)).named('U7')
D7 = U7.inv().named('U7')

F = swaps(TRu + tru, BRd + brd).named('F')
Ru = swaps(TLu + tlu + blu + BLu, TRu + tru + bru + BRu).named('Ru')
Rl = (F*Ru*F).named('Rl')
assert str(F * F) == '()'
assert str(Ru * Ru) == '()'
assert str(Rl * Rl) == '()'

U3 = (F * U7 * F).named('U3')
D3 = U3.inv().named('D3')

UT4 = (F * UT * F).named('UT4')
DT4 = UT4.inv().named('DT4')
Ut4 = (F * Ut * F).named('Ut4')
Dt4 = Ut4.inv().named('Dt4')
Ub4 = (F * Ub * F).named('Ub4')
Db4 = Ub4.inv().named('Db4')
UB4 = (F * UB * F).named('UB4')
DB4 = UB4.inv().named('DB4')

U5 = (F * U1 * F).named('U5')
D5 = U5.inv().named('D5')

UT6 = (F * UT2 * F).named('UT6')
DT6 = UT6.inv().named('DT6')
Ut6 = (F * Ut2 * F).named('Ut6')
Dt6 = Ut6.inv().named('Dt6')
