# Defines the identity group.

class I:
  """Element of identity group."""
  def __str__(self):
    return ''
  def __repr__(self):
    return ''
  def at(self, pos):
    return ''
  def __mul__(self, other):
    if not isinstance(other, I): return NotImplemented
    return I.e0
  def inv(self):
    return self
  def __cmp__(self, other):
    if not isinstance(other, I): return NotImplemented
    return 0
I.e0 = I()
