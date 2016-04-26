import re

def checkio(text):
    "Convert Euro style currency in dollars to US/UK style"
    eu = re.compile(r'''
                    (\$(\d+\.)+\d+\,\d{2})\b
                    |(\$(\d+\.)+\d{3})\b
                    |(\$\d+\.\d{3})\b
                    |(\$\d+\,\d{2})\b
                    ''', re.VERBOSE
                    )
    spans = [m.span() for m in re.finditer(eu, text)]
    print [text[s:e] for s,e in spans]
    inspan = lambda i: any([start <= i < end for start, end in spans])

    d = {',':'.', '.':','}
    return ''.join([d[c] if c in d and inspan(i) else c for i, c in enumerate(text)])


import re

def checkio(text):
    reform = lambda match: match.group(0).translate(str.maketrans(',.', '.,'))
    return re.sub('\$\d{1,3}(\.\d{3})*(,\d{2}){,1}(?!\d)', reform, text)
    # \$            letter '$'
    # \d{1,3}       [0-9] of length {1, 3}
    # (\.\d{3})*    repetation of \.[0-9]{3}, if exists
    # (,\d{2}){,1}  ,[0-9]{2}, if exists
    # (?!\d)        no [0-9] after pattern


import re
def checkio(text):
    return re.sub(r"(\$\d{1,3}(\.\d{3})*(,\d{1,2}(?!\d)){,1})", lambda nl: nl.group(0).translate(str.maketrans('.,', ',.')), text)


#Euro Style = $12.345,67, US Style = $12,345.67

if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert checkio("$1.234.567,89") == "$1,234,567.89" , "1st Example"
    #assert checkio("$0,89") == "$0.89" , "2nd Example"
    # print checkio("Euro Style = $12.345,67, US Style = $12,345.67")
    # print checkio("Us Style = $12,345.67, Euro Style = $12.345,67")
    print checkio("$5.34")

    print checkio("$222.100.455,34")
    print checkio(("$222.100.455"))

    print checkio("$5,34")
    print checkio("$5,34, $1.234, $5.678 and $9")
    exit()
    print checkio("Euro Style = $12.345,67, US Style = $12,345.67")
    print "Euro Style = $12,345.67, US Style = $12,345.67" , "European and US"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
                   "Us Style = $12,345.67, Euro Style = $12,345.67" , "US and European"
    assert checkio("$1.234, $5.678 and $9") == \
                   "$1,234, $5,678 and $9", "Dollars without cents"
