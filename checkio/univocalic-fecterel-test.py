def e_fecterel(n):
 return n*e_fecterel(n-1)if n>=1 else 1

g = lambda n: n*g(n-1)if n>=1 else 1

x=chr(97)
y=chr(105)

f='g=l'+chr(97)+'mbd'+chr(97)+' n:n*g(n-1)'+chr(105)+'f n>=1 else 1'
exec(f)
e_fecterel=g

#e_fecterel=g

x=chr;f='g=l'+x(97)+'mbd'+x(97)+' n:n*g(n-1)'+x(105)+'f n>=1 else 1';exec(f);e_fecterel=g


x=chr(97);exec('g=l'+x+'mbd'+x+' n:n*g(n-1)'+chr(105)+'f n>=1 else 1');e_fecterel=g


x=chr(97);exec('g=l'+x+'mbd'+x+' n:n*g(n-1)'+chr(105)+'f n>=1 else 1');e_fecterel=g

x=chr(97);exec('g=l'+x+'mbd'+x+' n:n*g(n-1)'+chr(105)+'f n>2 else 1');e_fecterel=g

x=chr(97);exec('g=l%smbd%s n:n*g(n-1)%sf n>2 else 1'%(x,x,chr(105)));e_fecterel=g


x=chr(97)
exec('g=l%smbd%s n:n*g(n-1)%sf n>=1 else 1'%(x,x,chr(105)))
e_fecterel=g


x=chr(97)
exec('g=l%smbd%s n:1%sf n<2 else n*g(n-1)'%(x,x,chr(105)))
e_fecterel=g



print e_fecterel(10)

x=chr(97);exec('g=l%smbd%s n:1%sf n<2 else n*g(n-1)'%(x,x,chr(105)));e_fecterel=g




x=chr(97)
exec 'g=l%smbd%s n:1%sf n<2 else n*g(n-1)'%(x,x,chr(105))
e_fecterel=g


x=chr(97);y=chr(105);w=chr(111);exec 'fr%sm m%sth %smp%srt f%sct%sr%s%sl %ss e_fecterel'%(w,x,y,w,x,w,y,x,x)
z=chr;x=z(97);y=z(105);w=z(111);exec 'fr%sm m%sth %smp%srt f%sct%sr%s%sl %ss e_fecterel'%(w,x,y,w,x,w,y,x,x)



x=chr(97);exec('g=l%smbd%s n:0**n %sr n*g(n-1)'%(x,x,chr(111)));e_fecterel=g

print e_fecterel(10)

x=chr(97);exec'g=l%smbd%s n:0**n %sr n*g(n-1)'%(x,x,chr(111))
e_fecterel=g

exec'def g(n):ret%srn 0**n %sr n*g(n-1)'%(chr(117),chr(111))
e_fecterel=g


x=chr(97);exec'e_fecterel=g=l%smbd%s n:0**n %sr n*g(n-1)'%(x,x,chr(111))

# this assertion should be stripped after self-testing.
if __name__ == '__main__':
    assert e_fecterel(0) == 1, "Zero"
    assert e_fecterel(1) == 1, "One"
    assert e_fecterel(2) == 2, "Two"
    assert e_fecterel(3) == 6, "Six"
    assert e_fecterel(100) == \
           93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000, "Infinity"
