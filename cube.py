# Methods for dealing with cubes in general

import base

class Cube:
  def __init__(self):
    self.blocks = []
    self.index = {}
    #self.targets = [block for block in Cube.blocks]
  #def __call__(self, *args):
  #  """Applies permutations in series."""
  #  cube = self
  #  for arg in args:
  #    cube = arg(cube)
  #  return cube

class Block:
  def __init__(self, name, orientation, cube = None):
    self.cube = cube
    self.name = name
    self.orientation = orientation
    # Add self to the cube
    if cube:
      cube.index[self.name] = len(cube.blocks)
      cube.blocks.append(self)
  def __str__(self):
    return self.name + str(self.orientation)
  def __repr__(self):
    return str(self)
  def __cmp__(self, other):
    if not isinstance(other, Block): return NotImplemented
    return (base.ComparisonChain()
            .compare(self.cube, other.cube)
            .compare(self.name, other.name)
            .compare(self.orientation, other.orientation)
            .end())
  def fromOrientation(self, orient):
    # don't worry about orientation of edges
    if self.type() == 'E': return self
    return self.at(self.orientation * orient.inv())
  def at(self, orient):
    block = Block(self.name, orient)
    block.cube = self.cube
    return block
  def showOrientation(self, orientation):
    """
    Formats the orientation given the block type (and possibly its position).
    The default implementation (for cubes) is to show a different
    representation of D3 depending on whether it's a corner, edge, or face.
    For corners it's simply the name, or blank for e.  For edges, it's * for
    rotations and flips around the axis.
    """
    bt = self.type()
    if bt == 'V': # corner
      return orientation.cname
    elif bt == 'F': # face
      return ''
    elif orientation.flip:
      return self.name[orientation.rot] not in 'FBUDLR' and '*' or ''
    else:
      return orientation.rot != 0 and '*' or ''
  def display(self):
    return self.displayName() + self.displayOrientation()
  def displayName(self):
    return self.name
  def displayOrientation(self, relativeTo=None):
    if relativeTo is None:
      return self.showOrientation(self.orientation)
    orient = self.fromOrientation(relativeTo.orientation).orientation
    return relativeTo.showOrientation(orient)
  def type(self):
    """
    Returns the type of block.  The default implementation (for cube-style
    puzzles) uses F for face blocks, E for edges, and V for vertices, but
    this can be overridden, or not used at all (i.e. return '').
    """
    return ' FEV'[sum([c in 'FBUDLR' for c in self.name])]

# TODO(sdh): represent permutations as sparse.

# Permutations
class Permutation:
  def __init__(self, cube, targets=None, components=None):
    self.cube = cube
    self.targets = [target for target in (targets or cube.blocks)]
    if Permutation.DEBUG:
      print targets
      print self.targets
      print (targets or cube.blocks)
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
      i2 = self.cube.index[t.name]
      if t == self.cube.blocks[i]: continue # unchanged, so skip
      if i == i2:
        cycles.append('(%s)%s' % (t.displayName(), t.displayOrientation()))
        continue
      t2 = t
      t = self.cube.blocks[i]
      cycle = [t.name]
      found[t.name] = True
      while t2.name not in found:
        found[t2.name] = True
        t = t2.fromOrientation(t.orientation)
        cycle.append(t.display())
        t2 = self.targets[self.cube.index[t2.name]]
      orient = t2.fromOrientation(t.orientation).orientation
      #orient = t2.orientation * t.orientation.inv()
      cycles.append('(%s)%s' % (' '.join(cycle), t2.displayOrientation(t)))
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
      return self.identity() # Permutation.e
    elif num == 1:
      return self
    elif self.power and (self.power * num > 0 or not self.label):
      return (self.base ** (self.power * num)).simplify()
    p = self
    if num < 0:
      p = p.inv()
    targets = self.cube.blocks # Permutation.e doesn't work?
    if Permutation.DEBUG: print targets
    for i in range(abs(num)):
      targets = p.internalMult(targets)
      if Permutation.DEBUG: print targets
    p = Permutation(self.cube, targets, [p] * abs(num))
    p = p.named('%s^%d' % (self.name(), num))
    p.base = self
    p.power = num
    return p.simplify()
  def simplify(self):
    if str(self) == '()':
      return self.identity() # Permutation.e
    return self
  def internalMult(self, otherTargets):
    targets = []
    for target in otherTargets:
      result = self.targets[self.cube.index[target.name]]
      targets.append(result.at(result.orientation * target.orientation))
    return targets
  def __mul__(self, other):
    if other is None: return self
    if not isinstance(other, Permutation): return NotImplemented
    targets = self.internalMult(other.targets)
    components = []
    other.addComponents(components) # read left-to-right
    self.addComponents(components)
    return Permutation(self.cube, targets, self.rewriteComponents(components)
                       ).simplify()
  def inv(self):
    if self.power:
      return self.base ** -self.power
    targets = [None] * len(self.cube.blocks)
    for i, t2 in enumerate(self.targets):
      i2 = self.cube.index[t2.name]
      t = self.cube.blocks[i]
      targets[i2] = t.at(t.orientation * t2.orientation.inv())
    if self.components:
      components = [c.inv() for c in self.components]
      components.reverse()
    else:
      components = None
    p = Permutation(self.cube, targets, components)
    if self.label:
      p = p.named(self.label + "^-1")
    p.base = self
    p.power = -1
    return p.simplify()
  def __call__(self, block): # TODO: make this work for whole cubes too
    return (self.targets[self.cube.index[block.name]]
            .fromOrientation(block.orientation))
  def name(self):
    if self.label:
      return self.label
    if not self.components:
      return '?'
    return ' '.join([c.name() for c in self.components])
  def filter(self, bt):
    targets = self.targets
    for i, t in enumerate(self.cube.blocks):
      if t.type() not in bt:
        targets[i] = t
    return Permutation(self.cube, targets)
  def identity(self):
    return Permutation(self.cube).named('e')

Permutation.DEBUG = False

def cycle(*blocks):
  cube = blocks[0].cube
  targets = [target for target in cube.blocks]
  last = blocks[0]
  blocks = list(blocks[1:]) + [last]
  for block in blocks:
    next = block.at(block.orientation * last.orientation.inv())
    targets[cube.index[last.name]] = next
    last = block
  return Permutation(cube, targets)

# Utility functions

def cat(*args):
  """Performs left-multiplication."""
  perm = None
  for arg in args:
    perm = arg * perm
  return perm

def comm(a, b):
  return cat(a, b, a.inv(), b.inv())
