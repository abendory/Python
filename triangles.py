#!/usr/env Python
# -*- coding: utf-8 -*-


import math

AB = 4
BC = 10
AC = math.sqrt(AB**2 + BC**2)
MC = BM = AC / 2

MBC = math.acos((BM**2 + BC**2 - MC**2) / (2*BM*BC))

print str(int(round(MBC*(180/math.pi))))
