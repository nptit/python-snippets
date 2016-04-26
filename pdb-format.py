__author__ = 'qxu'

'''
field id	definition	length	format	range	string slicing (Python)
1	"ATOM " or "HETATM"	6	%-6s	01-06	[0:6]
2	atom serial number	5	%5d	07-11	[6:11]
3	atom name	4	%4s	13-16	[12:16]
4	alternate location indicator	1	%1s	17	[16:17]
5	residue name	3	%3s	18-20	[17:20]
6	chain identifier	1	%1s	22	[21:22]
7	residue sequence number	4	%4d	23-26	[22:26]
8	code for insertion of residues	1	%1s	27	[26:27]
9	orthogonal coordinates for X (in Angstroms)	8	%8.3f	31-38	[30:38]
10	orthogonal coordinates for Y (in Angstroms)	8	%8.3f	39-46	[38:46]
11	orthogonal coordinates for Z (in Angstroms)	8	%8.3f	47-54	[46:54]
12	occupancy	6	%6.3f	55-60	[54:60]
13	temperature factor	6	%6.3f	61-66	[60:66]
14	element symbol	2	%2s	77-78	[76:78]
15	charge on the atom	2	%2s	79-80	[78:80]


Formated string for ATOM lines in PDB files (copy and paste this line into your Python code):

"%-6s%5d %4s%1s%3s %1s%4d%1s   %8.3f%8.3f%8.3f%6.2f%6.2f          %2s%2s"
'''