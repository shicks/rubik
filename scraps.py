class F4:
  """Element of F_4."""
  def __init__(self, name, value):
    self.name = name
    self.value = value
  def __str__(self):
    return self.name
  def __repr__(self):
    return str(self)
  def __mul__(self, other):
    if not isinstance(other, F4): return NotImplemented
    return F4.elts[(self.value + other.value) % 4]
  def inv(self):
    return F4.elts[(4 - self.value) % 4]
  def __cmp__(self, other):
    if not isinstance(other, F4): return NotImplemented
    return self.value - other.value

F4.e0 = F4('', 0)
F4.e1 = F4('.', 1)
F4.e2 = F4(':', 2)
F4.e3 = F4(',', 3)
F4.elts = [F4.e0, F4.e1, F4.e2, F4.e3]

class F2:
  """Element of F_2."""
  def __init__(self, name, value):
    self.name = name
    self.value = value
  def __str__(self):
    return self.name
  def __repr__(self):
    return str(self)
  def __mul__(self, other):
    if not isinstance(other, F2): raise TypeError()
    return F2.elts[(self.value + other.value) % 2]
  def inv(self):
    return self
  def __cmp__(self, other):
    if not isinstance(other, F2): return NotImplemented
    return self.value - other.value

F2.e0 = F2('', 0)
F2.e1 = F2('*', 1)
F2.elts = [F2.e0, F2.e1]


class O3:
  """90-degree subgroup of O_3."""
  def __init__(self, value):
    self.value = value
  def __str__(self):
    s = ''
    for i in self.value:
      s += (i < 0 and '-' or '') + (chr(119 + abs(i)))
    return s
  def at(self, pos):
    """Formats the orientation given the position."""
    for i, c in enumerate(pos):
      if ord(c) >= ord('a'):
        return self % (i + 1) and '*' or ''
    return '?'
  def __repr__(self):
    return str(self)
  def __mul__(self, other):
    if not isinstance(other, O3): raise TypeError()
    x = [(i/abs(i)) * self.value[abs(i) - 1] for i in other.value]
    return O3(x)
  def inv(self):
    x = [0, 0, 0]
    for i, d in enumerate(self.value):
      x[abs(d) - 1] = (i + 1) * (d/abs(d))
    return O3(x)
  def __mod__(self, other):
    """Other is an axis (1, 2, or 3).  Returns true if this rotation
    is a flip through the other axes."""
    for i, d in enumerate(self.value):
      i = i + 1
      d = abs(d)
      if i == other or d == other: continue
      return i != d
  def __cmp__(self, other):
    if not isinstance(other, O3): return NotImplemented
    # arbitrary but consistent ordering
    return (225 * (self.value[0] - other.value[0])
            + 15 * (self.value[1] - other.value[1])
            + (self.value[2] - other.value[2]))

O3.e = O3([1, 2, 3])
O3.x = O3([1, 3, -2])
O3.y = O3([-3, 2, 1])
O3.z = O3([2, -1, 3])
O3.x2 = O3.x * O3.x
O3.y2 = O3.y * O3.y
O3.z2 = O3.z * O3.z
O3.xi = O3.x.inv()
O3.yi = O3.y.inv()
O3.zi = O3.z.inv()

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
