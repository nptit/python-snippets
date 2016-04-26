# coding = utf8
# -*- coding: utf-8 -*-
# encoding: utf-8


s = u"préfèrent"
print type(s)
print s.encode('utf-8')

import unicodedata

print ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
