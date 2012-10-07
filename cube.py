# Methods for dealing with 4x4x4 rubik's cube

class D3:
  """Element of dihedral group D_3."""
  def __init__(self, name, flip, rot):
    self.name = name
    self.flip = flip
    self.rot = rot
  def __str__(self):
    return self.name
  def __repr__(self):
    return str(self)
  def __mul__(self, other):
    if not isinstance(other, D3): raise TypeError()
    if other.flip == 0:
      return D3.elts[self.flip][(self.rot + other.rot) % 3]
    return D3.elts[1 - self.flip][(3 - self.rot + other.rot) % 3]
  def inv(self):
    if self.flip:
      return self
    return D3.elts[0][(3 - self.rot) % 3]
  def at(self, pos):
    """Formats the orientation given the position.  For corners
    it's simply the name, or blank for e.  For edges, it's * for
    rotations and flips around the axis.
    """
    bt = block_type(pos)
    if bt == 'V': # corner
      return self.name != 'e' and self.name or ''
    elif bt == 'F': # face
      return ''
    elif self.flip:
      return pos[self.rot] >= 'a' and '*' or ''
    else:
      return self.rot != 0 and '*' or ''
  def __cmp__(self, other):
    if not isinstance(other, D3): return NotImplemented
    return 3 * (self.flip - other.flip)  + (self.rot - other.rot)

D3.e0 = D3('e', 0, 0)
D3.e1 = D3('+', 0, 1)
D3.e2 = D3('-', 0, 2)
D3.F = D3('x', 1, 0)
D3.U = D3('v', 1, 1)
D3.L = D3('h', 1, 2)
D3.elts = [[D3.e0, D3.e1, D3.e2],
           [D3.F, D3.U, D3.L]]

class Cube:
  blocks = []
  index = {}
  def __init__(self):
    self.targets = [block for block in Cube.blocks]
  def __call__(self, *args):
    """Applies permutations in series."""
    cube = self
    for arg in args:
      cube = arg(cube)
    return cube

def block_type(name):
  return ' FEV'[sum([c < 'a' for c in name])]

class Block:
  def __init__(self, name, orientation, add = False):
    self.name = name
    self.orientation = orientation
    # Add self to the cube
    if add:
      Cube.index[self.name] = len(Cube.blocks)
      Cube.blocks.append(self)
  def __str__(self):
    return self.name + str(self.orientation)
  def __repr__(self):
    return str(self)
  def __cmp__(self, other):
    if not isinstance(other, Block): return NotImplemented
    val = cmp(self.name, other.name)
    if val != 0: return val
    return cmp(self.orientation, other.orientation)
  def fromOrientation(self, orient):
    # don't worry about orientation of edges
    if block_type(self.name) == 'E': return self
    return self.at(self.orientation * orient.inv())
  def at(self, orient):
    return Block(self.name, orient)
  def display(self):
    return self.name + self.orientation.at(self.name)

# TODO(sdh): parametrize by the Cube, so that we can have diff kinds
# Permutations
class Permutation:
  def __init__(self, targets=None, components=None):
    self.targets = [target for target in (targets or Cube.blocks)]
    if Permutation.DEBUG:
      print targets
      print self.targets
      print (targets or Cube.blocks)
    self.components = components
    self.label = self.strng = self.power = self.base = None
  def named(self, label):
    # TODO: Make a copy
    self.label = label
    # Link inverses if applicable
    if self.power and self.power == -1 and not self.base.power:
      self.base.power = -1
      self.base.base = self
    return self
  def __str__(self):
    if self.strng:
      return self.strng
    found = {}
    cycles = []
    for i,t in enumerate(self.targets):
      if t.name in found: continue
      i2 = Cube.index[t.name]
      if t == Cube.blocks[i]: continue # unchanged, so skip
      if i == i2:
        cycles.append('(%s)%s' % (t.name, t.orientation.at(t.name)))
        continue
      t2 = t
      t = Cube.blocks[i]
      cycle = [t.name]
      found[t.name] = True
      while t2.name not in found:
        found[t2.name] = True
        t = t2.fromOrientation(t.orientation)
        cycle.append(t.display())
        t2 = self.targets[Cube.index[t2.name]]
      orient = t2.fromOrientation(t.orientation).orientation
      #orient = t2.orientation * t.orientation.inv()
      cycles.append('(%s)%s' % (' '.join(cycle), orient.at(t.name)))
    if cycles:
      self.strng = ' '.join(cycles)
    else:
      self.strng = '()'
    return self.strng
  def __repr__(self):
    return str(self)
  def addComponents(self, components):
    if self.components and not self.label:
      components.extend(self.components)
    else:
      components.append(self)
  def rewriteComponents(self, components):
    r = []
    for c in components:
      if str(c) == '()': continue
      cinv = str(c.inv())
      if r:
        top = r[len(r)-1]
        if str(top) == cinv:
          r.pop()
          continue
        if str(top) == str(c):
          r.pop()
          r.append(top ** 2)
          continue
        if top.power and abs(top.power) != 1:
          if str(top.base) == cinv:
            r.pop()
            r.append(top.base ** (top.power - 1))
            continue
          elif str(top.base) == str(c):
            r.pop()
            r.append(top.base ** (top.power + 1))
            continue
      r.append(c)
    return r
  def __pow__(self, num):
    if num == 0:
      return Permutation.e
    elif num == 1:
      return self
    elif self.power and (self.power * num > 0 or not self.label):
      return (self.base ** (self.power * num)).simplify()
    p = self
    if num < 0:
      p = p.inv()
    targets = Cube.blocks # would be nice to use Permutation.e but doesn't work?
    if Permutation.DEBUG: print targets
    for i in range(abs(num)):
      targets = p.internalMult(targets)
      if Permutation.DEBUG: print targets
    p = Permutation(targets, [p] * abs(num)).named('%s^%d' % (self.name(), num))
    p.base = self
    p.power = num
    return p.simplify()
  def simplify(self):
    if str(self) == '()':
      return Permutation.e
    return self
  def internalMult(self, otherTargets):
    targets = []
    for target in otherTargets:
      result = self.targets[Cube.index[target.name]]
      targets.append(result.at(result.orientation * target.orientation))
    return targets
  def __mul__(self, other):
    if not isinstance(other, Permutation): return NotImplemented
    targets = self.internalMult(other.targets)
    components = []
    other.addComponents(components) # read left-to-right
    self.addComponents(components)
    return Permutation(targets, self.rewriteComponents(components)).simplify()
  def inv(self):
    if self.power:
      return self.base ** -self.power
    targets = [None] * len(Cube.blocks)
    for i, t2 in enumerate(self.targets):
      i2 = Cube.index[t2.name]
      t = Cube.blocks[i]
      targets[i2] = t.at(t.orientation * t2.orientation.inv())
    if self.components:
      components = [c.inv() for c in self.components]
      components.reverse()
    else:
      components = None
    p = Permutation(targets, components)
    if self.label:
      p = p.named(self.label + "^-1")
    p.base = self
    p.power = -1
    return p.simplify()
  def __call__(self, block): # TODO: make this work for whole cubes too
    return (self.targets[Cube.index[block.name]]
            .fromOrientation(block.orientation))
  def name(self):
    if self.label:
      return self.label
    if not self.components:
      return '?'
    return ' '.join([c.name() for c in self.components])
  def filter(self, bt):
    targets = self.targets
    for i, t in enumerate(Cube.blocks):
      if block_type(t.name) not in bt:
        targets[i] = t
    return Permutation(targets)    

Permutation.DEBUG = False

def cycle(*blocks):
  targets = [target for target in Cube.blocks]
  last = blocks[0]
  blocks = list(blocks[1:]) + [last]
  for block in blocks:
    next = block.at(block.orientation * last.orientation.inv())
    targets[Cube.index[last.name]] = next
    last = block
  return Permutation(targets)

# Corner blocks
FUL = Block('FUL', D3.e0, True)
FUR = Block('FUR', D3.e0, True)
FDL = Block('FDL', D3.e0, True)
FDR = Block('FDR', D3.e0, True)
BUL = Block('BUL', D3.e0, True)
BUR = Block('BUR', D3.e0, True)
BDL = Block('BDL', D3.e0, True)
BDR = Block('BDR', D3.e0, True)

# Edge blocks
FUl = Block('FUl', D3.e0, True)
FUr = Block('FUr', D3.e0, True)
FuL = Block('FuL', D3.e0, True)
FdL = Block('FdL', D3.e0, True)
FuR = Block('FuR', D3.e0, True)
FdR = Block('FdR', D3.e0, True)
FDl = Block('FDl', D3.e0, True)
FDr = Block('FDr', D3.e0, True)
fUL = Block('fUL', D3.e0, True)
fUR = Block('fUR', D3.e0, True)
fDL = Block('fDL', D3.e0, True)
fDR = Block('fDR', D3.e0, True)
bUL = Block('bUL', D3.e0, True)
bUR = Block('bUR', D3.e0, True)
bDL = Block('bDL', D3.e0, True)
bDR = Block('bDR', D3.e0, True)
BUl = Block('BUl', D3.e0, True)
BUr = Block('BUr', D3.e0, True)
BuL = Block('BuL', D3.e0, True)
BdL = Block('BdL', D3.e0, True)
BuR = Block('BuR', D3.e0, True)
BdR = Block('BdR', D3.e0, True)
BDl = Block('BDl', D3.e0, True)
BDr = Block('BDr', D3.e0, True)

# Face blocks
Ful = Block('Ful', D3.e0, True)
Fur = Block('Fur', D3.e0, True)
Fdl = Block('Fdl', D3.e0, True)
Fdr = Block('Fdr', D3.e0, True)
fUl = Block('fUl', D3.e0, True)
fUr = Block('fUr', D3.e0, True)
fDl = Block('fDl', D3.e0, True)
fDr = Block('fDr', D3.e0, True)
fuL = Block('fuL', D3.e0, True)
fuR = Block('fuR', D3.e0, True)
fdL = Block('fdL', D3.e0, True)
fdR = Block('fdR', D3.e0, True)
bUl = Block('bUl', D3.e0, True)
bUr = Block('bUr', D3.e0, True)
bDl = Block('bDl', D3.e0, True)
bDr = Block('bDr', D3.e0, True)
buL = Block('buL', D3.e0, True)
buR = Block('buR', D3.e0, True)
bdL = Block('bdL', D3.e0, True)
bdR = Block('bdR', D3.e0, True)
Bul = Block('Bul', D3.e0, True)
Bur = Block('Bur', D3.e0, True)
Bdl = Block('Bdl', D3.e0, True)
Bdr = Block('Bdr', D3.e0, True)

# Must be defined after all blocks
Permutation.e = Permutation().named('e')

# Operations
Bff = (cycle(FUL, FUR.at(D3.F), FDR, FDL.at(D3.F))
       * cycle(FUl, FuR.at(D3.F), FDr, FdL.at(D3.F))
       * cycle(FUr, FdR.at(D3.F), FDl, FuL.at(D3.F))
       * cycle(Ful, Fur, Fdr, Fdl)).named('Bff')
Bf = (cycle(fUL, fUR.at(D3.F), fDL.at(D3.F))
      * cycle(fUl, fuR, fDr, fdL)
      * cycle(fUr, fdR, fDl, fuL)).named('Bf')
Bb = (cycle(bUL, bUR.at(D3.F), bDR, bDL.at(D3.F))
      * cycle(bUl, buR, bDr, bdL)
      * cycle(bUr, bdR, bDl, buL)).named('Bb')
Bbb = (cycle(BUL, BUR.at(D3.F), BDR, BDL.at(D3.F))
       * cycle(BUl, BuR.at(D3.F), BDr, BdL.at(D3.F))
       * cycle(BUr, BdR.at(D3.F), BDl, BuL.at(D3.F))
       * cycle(Bul, Bur, Bdr, Bdl)).named('Bff')
Fff = Bff.inv().named('Fff')
Ff = Bf.inv().named('Ff')
Fb = Bb.inv().named('Fb')
Fbb = Bbb.inv().named('Fbb')

Urr = (cycle(FUR, BUR.at(D3.L), BDR, FDR.at(D3.L))
       * cycle(fUR, BuR.at(D3.L), bDR, FdR.at(D3.L))
       * cycle(bUR, BdR.at(D3.L), fDR, FuR.at(D3.L))
       * cycle(fuR, buR, bdR, fdR)).named('Urr')
Ur = (cycle(FUr, BUr.at(D3.L), BDr, FDr.at(D3.L))
      * cycle(fUr, Bur, bDr, Fdr)
      * cycle(bUr, Bdr, fDr, Fur)).named('Ur')
Ul = (cycle(FUl, BUl.at(D3.L), BDl, FDl.at(D3.L))
      * cycle(fUl, Bul, bDl, Fdl)
      * cycle(bUl, Bdl, fDl, Ful)).named('Ul')
Ull = (cycle(FUL, BUL.at(D3.L), BDL, FDL.at(D3.L))
       * cycle(fUL, BuL.at(D3.L), bDL, FdL.at(D3.L))
       * cycle(bUL, BdL.at(D3.L), fDL, FuL.at(D3.L))
       * cycle(fuL, buL, bdL, fdL)).named('Ull')
Drr = Urr.inv().named('Drr')
Dr = Ur.inv().named('Dr')
Dl = Ul.inv().named('Dl')
Dll = Ull.inv().named('Dll')

Ruu = (cycle(FUL, FUR.at(D3.U), BUR, BUL.at(D3.U))
       * cycle(FUl, fUR.at(D3.U), BUr, bUL.at(D3.U))
       * cycle(FUr, bUR.at(D3.U), BUl, fUL.at(D3.U))
       * cycle(fUl, fUr, bUr, bUl)).named('Ruu')
Ru = (cycle(FuL, FuR.at(D3.U), BuR, BuL.at(D3.U))
      * cycle(Ful, fuR, Bur, buL)
      * cycle(Fur, buR, Bul, fuL)).named('Ru')
Rd = (cycle(FdL, FdR.at(D3.U), BdR, BdL.at(D3.U))
      * cycle(Fdl, fdR, Bdr, bdL)
      * cycle(Fdr, bdR, Bdl, fdL)).named('Rd')
Rdd = (cycle(FDL, FDR.at(D3.U), BDR, BDL.at(D3.U))
       * cycle(FDl, fDR.at(D3.U), BDr, bDL.at(D3.U))
       * cycle(FDr, bDR.at(D3.U), BDl, fDL.at(D3.U))
       * cycle(fDl, fDr, bDr, bDl)).named('Rdd')
Luu = Ruu.inv().named('Luu')
Lu = Ru.inv().named('Lu')
Ld = Rd.inv().named('Ld')
Ldd = Rdd.inv().named('Ldd')

OF = (Fff*Ff*Fb*Fbb).named('OF')
OU = (Ruu*Ru*Rd*Rdd).named('OU')
OR = (Drr*Dr*Dl*Dll).named('OR')
OB = (OF.inv()).named('OB')
OD = (OU.inv()).named('OD')
OL = (OR.inv()).named('OL')

# Utility functions

def cat(*args):
  """Performs left-multiplication."""
  perm = Permutation.e
  for arg in args:
    perm = arg * perm
  return perm

def comm(a, b):
  return cat(a, b, a.inv(), b.inv())

# Additional permutations

seven = cat(Drr, Rdd, Urr, Rdd, Bff, Ldd, Fff)
sevenI = seven.inv()
Ur1R = cat(Ur, Ruu, Dr, Ruu**2, Ur, Ruu, Dr)
Ur1L = cat(Ur, Luu, Dr, Luu**2, Ur, Luu, Dr)
Ul1R = cat(Ul, Ruu, Dl, Ruu**2, Ul, Ruu, Dl)
Ul1L = cat(Ul, Luu, Dl, Luu**2, Ul, Luu, Dl)

Ur2R = cat(Ur, Ruu, Dr, Ruu, Ur, Ruu**2, Dr)
Ur2L = cat(Ur, Luu, Dr, Luu, Ur, Luu**2, Dr)
Ul2R = cat(Ul, Ruu, Dl, Ruu, Ul, Ruu**2, Dl)
Ul2L = cat(Ul, Luu, Dl, Luu, Ul, Luu**2, Dl)

Ur3R = cat(Ur, Ruu**2, Dr, Ruu, Ur, Ruu, Dr)
Ur3L = cat(Ur, Luu**2, Dr, Luu, Ur, Luu, Dr)
Ul3R = cat(Ul, Ruu**2, Dl, Ruu, Ul, Ruu, Dl)
Ul3L = cat(Ul, Luu**2, Dl, Luu, Ul, Luu, Dl)
