
#! /usr/bin/env python

import sys

if len(sys.argv) != 2:
	print 'Error, write filename'
	exit()

mappings={
        'AAA' : 'a',
        'AAC' : 'b',
        'AAG' : 'c',
        'AAT' : 'd',
        'ACA' : 'e',
        'ACC' : 'f',
        'ACG' : 'g',
        'ACT' : 'h',
        'AGA' : 'i',
        'AGC' : 'j',
        'AGG' : 'k',
        'AGT' : 'l',
        'ATA' : 'm',
        'ATC' : 'n',
        'ATG' : 'o',
        'ATT' : 'p',
        'CAA' : 'q',
        'CAC' : 'r',
        'CAG' : 's',
        'CAT' : 't',
        'CCA' : 'u',
        'CCC' : 'v',
        'CCG' : 'w',
        'CCT' : 'x',
        'CGA' : 'y',
        'CGC' : 'z',
        'CGG' : 'A',
        'CGT' : 'B',
        'CTA' : 'C',
        'CTC' : 'D',
        'CTG' : 'E',
        'CTT' : 'F',
        'GAA' : 'G',
        'GAC' : 'H',
        'GAG' : 'I',
        'GAT' : 'J',
        'GCA' : 'K',
        'GCC' : 'L',
        'GCG' : 'M',
        'GCT' : 'N',
        'GGA' : 'O',
        'GGC' : 'P',
        'GGG' : 'Q',
        'GGT' : 'R',
        'GTA' : 'S',
        'GTC' : 'T',
        'GTG' : 'U',
        'GTT' : 'V',
        'TAA' : 'W',
        'TAC' : 'X',
        'TAG' : 'Y',
        'TAT' : 'Z',
        'TCA' : '1',
        'TCC' : '2',
        'TCG' : '3',
        'TCT' : '4',
        'TGA' : '5',
        'TGC' : '6',
        'TGG' : '7',
        'TGT' : '8',
        'TTA' : '9',
        'TTC' : '0',
        'TTG' : ' ',
        'TTT' : '.',
        }

c = open(sys.argv[1]).read().strip()

flag = []
for x in range(0,len(c),3):
	piece = c[x:x+3]
	flag.append(mappings[piece])

print ''.join(flag)
