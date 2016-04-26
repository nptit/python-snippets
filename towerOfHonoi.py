def solve(N, Src, Aux, Dst):
    if N == 0:
        exit
    else:
        solve(N-1, Src, Dst, Aux)
        print "Move disk {} from {} to {}".format(N, Src, Dst)
        solve(N-1, Aux, Src, Dst)


print "\n0 disks:"
solve(0, 'Src', 'Aux', 'Dst')

print "\n1 disks:"
solve(1, 'Src', 'Aux', 'Dst')

print "\ntwo disks:"
solve(2, 'Src', 'Aux', 'Dst')

print "\nthree disks:"
solve(3, 'Src', 'Aux', 'Dst')



