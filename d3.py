# Defines the dihedral group

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
      return pos[self.rot] not in 'FBUDLR' and '*' or ''
    else:
      return self.rot != 0 and '*' or ''
  def __cmp__(self, other):
    if not isinstance(other, D3): return NotImplemented
    return 3 * (self.flip - other.flip)  + (self.rot - other.rot)

# TODO(sdh): figure out how to not duplicate this...
def block_type(name):
  return ' FEV'[sum([c in 'FBUDLR' for c in name])]

D3.e0 = D3('e', 0, 0)
D3.e1 = D3('+', 0, 1)
D3.e2 = D3('-', 0, 2)
D3.F = D3('x', 1, 0)
D3.U = D3('v', 1, 1)
D3.L = D3('h', 1, 2)
D3.elts = [[D3.e0, D3.e1, D3.e2],
           [D3.F, D3.U, D3.L]]
