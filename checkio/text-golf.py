f=lambda m,i,j:sum([m[x][y]==' ' for x in range(i-1,i+2) for y in range(j-1,j+2) if m[i][j]==' '])
golf=lambda t: [(i+1,j+1, c, l) for i, l in enumerate(t[1:-1]) for j,c in enumerate(l[1:-1]) if f(t,i+1,j+1)==1]


golf=lambda t: [(i+1,j+1, c, l) for i, l in enumerate(t[1:-1]) for j,c in enumerate(l[1:-1]) if c==' ' and f(t,i+1,j+1)==1]

f=lambda m,i,j:sum([m[x][y:y+1]==list(' ') for x in range(i-1,i+2) for y in range(j-1,j+2)])



f=lambda m,i,j:sum([m[x][y:y+1]==list(' ') for x in range(i-1,i+2) for y in range(j-1,j+2)])
golf=lambda t:len([1for i, l in enumerate(t[1:-1]) for j,c in enumerate(l[1:-1]) if f(t,i+1,j+1)==1])


def golf(t):
 r = 0
 for i,l in enumerate(t[1:-1]):
  for j,c in enumerate(l[1:-1]):
   if c==' ':
    #p= [t[x][y:y+1] for x in range(i,i+3) for y in range(j,j+3)]
    z= [t[x][y]==' ' for x in range(i,i+3) for y in range(j,j+3) if t[x][y:y+1]!='']
    #print l, c, i+1, j+1, t[i+1][j+1], p,z
    if sum(z)==1 and len(z)==9:
     #print l, c, i+1, j+1, t[i+1][j+1], p,z
     r+=1
 return r

# this code passed the test
def golf(t):
 r = 0
 for i,l in enumerate(t[1:-1]):
  for j,c in enumerate(l[1:-1]):
   if c==' ':
    z= [t[x][y]==' ' for x in range(i,i+3) for y in range(j,j+3) if t[x][y:y+1]!='']
    if sum(z)==1 and len(z)==9:
     r+=1
 return r

#122 points, 177th
def golf(t):
 r=0
 for i,l in enumerate(t[1:-1]):
  for j,c in enumerate(l[1:-1]):
   if c==' ':
    z=[t[x][y]==' 'for x in range(i,i+3)for y in range(j,j+3)if t[x][y:y+1]!='']
    if sum(z)==1and len(z)==9:
     r+=1
 return r

##168th
def golf(t):
 r=0
 for i,l in enumerate(t[1:-1]):
  for j,c in enumerate(l[1:-1]):
   if c==' ':
    z=[t[x][y]==' 'for x in range(i,i+3)for y in range(j,j+3)if t[x][y:y+1]!='']
    if sum(z)==1and len(z)==9:r+=1
 return r


##162th
def golf(t):
 r=0;e=enumerate;u=range
 for i,l in e(t[1:-1]):
  for j,c in e(l[1:-1]):
   if c==' ':
    z=[t[x][y]==' 'for x in u(i,i+3)for y in u(j,j+3)if t[x][y:y+1]!='']
    if sum(z)==1and len(z)==9:r+=1
 return r


##162th
def golf(t):
 r=0;e=enumerate;u=range
 for i,l in e(t[1:-1]):
  for j,c in e(l[1:-1]):
   if c==' ':
    z=[t[x][y]==' 'for x in u(i,i+3)for y in u(j,j+3)if t[x][y:y+1]!='']
    if sum(z)==1and len(z)==9:r+=1
 return r

##127th
def golf(t):
 r=0;e=enumerate;u=range
 for i,l in e(t[1:-1]):
  for j,c in e(l[1:-1]):
   if c==' ':
    z=[t[x][y:y+1]in[' ','']for x in u(i,i+3)for y in u(j,j+3)]
    if sum(z)==1:r+=1
 return r

##113th
def golf(t):
 r=0;e=enumerate;u=range
 for i,l in e(t[1:-1]):
  for j,c in e(l[1:-1]):
   if c==' ':
    if sum(t[x][y:y+1] in [' ','']for x in u(i,i+3)for y in u(j,j+3))==1:r+=1
 return r

###111th
def golf(t):
 r=0;e=enumerate;u=range
 for i,l in e(t[1:-1]):
  for j,c in e(l[1:-1]):
   if c==' ':
    if sum(t[x][y:y+1]in[' ','']for x in u(i,i+3)for y in u(j,j+3))==1:r+=1
 return r


###98th place
def golf(t):
 r=0;e=enumerate;u=range
 for i,l in e(t[1:-1]):
  for j,c in e(l[1:-1]):
   if c==' 'and sum(t[x][y:y+1]in[' ','']for x in u(i,i+3)for y in u(j,j+3))==1:r+=1
 return r

##73rd place @checkio
def golf(t):r=0;e=enumerate;u=range;return sum(1for i,l in e(t[1:-1])for j,c in e(l[1:-1])if c==' 'and sum(t[x][y:y+1]in[' ','']for x in u(i,i+3)for y in u(j,j+3))==1)


##61rd place @checkio
def golf(t):e=enumerate;u=range;return sum(1for i,l in e(t[1:-1])for j,c in e(l[1:-1])if c==' 'and sum(t[x][y:y+1]in[' ','']for x in u(i,i+3)for y in u(j,j+3))==1)

##51th place
e=enumerate;u=range;golf=lambda t:sum(1for i,l in e(t[1:-1])for j,c in e(l[1:-1])if c==' 'and sum(t[x][y:y+1]in[' ','']for x in u(i,i+3)for y in u(j,j+3))==1)

##51th place
e=enumerate;u=range;golf=lambda t:sum(1for i,l in e(t[1:-1])for j,c in e(l[1:-1])if c==' 'and sum(t[x][y:y+1]in[' ','']for x in u(i,i+3)for y in u(j,j+3))==1)



print golf([
"Lorem ipsum dolor",
"sit amet,",
"consectetuer",
"adipiscing elit.",
"Aenean commodo",
"ligula eget dolor.",
"Aenean massa. Cum",
"sociis natoque",
"penatibus et magnis",
"dis parturient",
"montes, nascetur",
"ridiculus mus. Donec",
"quam felis,",
"ultricies nec,",
"pellentesque eu,",
"pretium quis, sem.",
"Nulla consequat",
"massa quis enim.",
"Donec pede justo,",
"fringilla vel,"]) ==11


t=["How are you doing?","I'm fine. OK.","Lorem Ipsum?","Of course!!!","1234567890","0        0","1234567890","Fine! good buy!"]

print golf(t) #== 3

