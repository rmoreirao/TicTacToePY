import itertools

def count_each_item(xs):
  d = {}
  for x in xs:
    if x not in d:
      d[x] = 0
    d[x] += 1
  return d

def flatten(xs):
  return list(itertools.chain(*xs))

def memoize(f):
  d = {}
  def g(*a):
    if a not in d:
      d[a] = f(*a)
    return d[a]
  return g
