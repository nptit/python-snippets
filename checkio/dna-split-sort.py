golf=lambda t,n:''.join(sorted(map(''.join,zip(*[iter(t)]*n)),key=lambda s:len([1for i,x in enumerate(s)for y in s[i+1:]if x>y])))
