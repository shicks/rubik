# Defines the dihedral group

import base

class D3:
  """Element of dihedral group D_3."""
  def __init__(self, name, flip, rot, cname):
    self.name = name
    self.flip = flip
    self.rot = rot
    self.cname = cname
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
  def __cmp__(self, other):
    if not isinstance(other, D3): return NotImplemented
    return (base.ComparisonChain()
            .compare(self.flip, other.flip)
            .compare(self.rot, other.rot)
            .end())

D3.e0 = D3('e', 0, 0, '')
D3.e1 = D3('+', 0, 1, '+')
D3.e2 = D3('-', 0, 2, '-')
D3.F = D3('F', 1, 0, 'x')
D3.U = D3('U', 1, 1, 'v')
D3.L = D3('L', 1, 2, 'h')
D3.elts = [[D3.e0, D3.e1, D3.e2],
           [D3.F, D3.U, D3.L]]
