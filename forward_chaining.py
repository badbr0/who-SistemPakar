# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:42:21 2021

@author: VAIO
"""

global facts   #deklarasi fungsi variable yang dapat dipanggil dari manapun
global is_changed
is_changed = True
facts = [["vertebrate","duck"],["flying","duck"],["mammal","cat"]]  #isi/anggota variable facts

def assert_fact(fact):   #baris code assert_fact yang akan digunakan berkali^2
    global facts
    global is_changed
    if not fact in facts:  #bila kondisi tidak terpenuhi
        facts += [fact]
        is_changed = True

while is_changed:       #jika suatu kondisi terpenuhi
    is_changed = False
    for A1 in facts:
        if A1[0] == "mammal":
            assert_fact(["vertebrate",A1[1]])
            if A1[0] == "vertebrate":
                assert_fact(["animal",A1[1]])
                if A1[0] == "vertebrate" and ["flying",A1[1]] in facts:
                    assert_fact(["bird",A1[1]])

print(facts) #mencetak hasil