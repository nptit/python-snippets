def flat_list(a):
 l = []; f = lambda l, i: l.extend(flat_list(i)) if isinstance(i, list) else l.append(i)
 for i in a: f(l, i)
 return l

print flat_list([1,2,['a'], 3])
