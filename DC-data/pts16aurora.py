# -*- coding: utf-8 -*-
'''
PTS16のTEG測定結果のcsvを、synopsys社Aurora形式に変換する。

csvファイルは、MakeLSI/Measure/16PTS/DC-data/以下のxlsxから作成。
TEGの作者は高橋誓さん。
データ取得は秋田純一先生。

TegName    L      W    M
n1,p6      0.6u   15u  1
n2,p7      1.8u   15u  1
n3,p8       15u   15u  1
n4,p9       15u    3u  5
n5,p10      15u  1.8u  8

 |  15u x 1    n1   n2   n3
 W   3u x 5              n4
 | 1.8u x 8              n5
             0.6u  1.8u  15u
              --- L --->

 |  15u x 1    SW    MW   LW
 W   3u x 5               LM
 | 1.8u x 8               LN
             0.6u  1.8u  15u
              --- L --->
'''

'''
*** IdVg
                  TegName
Vgs   Vbs    Vds  n1 n2 n3 n4 n5  MeasNum
      0.0   0.05  *  *  *  *  *  {1n, 2n, 3n}
     -0.5         *  *  *  *  *  "
     -1.0         *  *  *  *  *  "
     -1.5         *  *  *  *  *  "
     -2.0         *  *  *  *  *  "
     -2.5         *  *  *  *  *  "
     -3.0         *  *  *  *  *  "
     -5.0   0.0   *  *  *        4n
            0.5   *  *  *        "
            1.0   *  *  *        "
            1.5   *  *  *        "
            2.0   *  *  *        "
            2.5   *  *  *        "
            3.5   *  *  *        "
            4.0   *  *  *        "
            4.5   *  *  *        "
            5.0   *  *  *        "
      0.0   5.0   *  *  *        5n
     -0.5         *  *  *        "
     -1.0         *  *  *        "
     -1.5         *  *  *        "
     -2.0         *  *  *        "
     -2.5         *  *  *        "
     -3.0         *  *  *        "


*** IdVd
                 TegName
Vds   Vgs   Vbs  n1 n2 n3 n4 n5  MeasNum
      2.5   0.0   *  *  *        6n       <-- {7n, 8n}と重複するのでcsvから削除
           -0.5   *  *  *
           -1.0   *  *  *
           -1.5   *  *  *
           -2.0   *  *  *
           -2.5      *                    <-- ？何故かn2だけ
           -3.0      *
      0.0   0.0   *  *  *  *  *  {7n, 8n}
      0.5         *  *  *  *  *
      1.0         *  *  *  *  *
      1.5         *  *  *  *  *
      2.0         *  *  *  *  *
      2.5         *  *  *  *  *
      3.0         *  *  *  *  *
      3.5         *  *  *  *  *
      4.0         *  *  *  *  *
      4.5         *  *  *  *  *
      5.0         *  *  *  *  *
      0.0   -5.0  *  *  *        9n
      1.0         *  *  *
      2.0         *  *  *
      3.0         *  *  *
      4.0         *  *  *
      5.0         *  *  *
'''

import re
import sys

import numpy as np

args = sys.argv
if len(args) == 2:
    Vstep = float(args[1])
else:
    Vstep = 0.01
# Teg Name to CSV file list Map
# 2n-n3.csv == 1n-n3.csv == 3n-n3.csv
CSV_IdVg = {
    'n1': ('2n-n1-170327.csv','4n-n1.csv','5n-n1.csv'),
    'n2': ('2n-n2-170327.csv','4n-n2.csv','5n-n2.csv'),
    'n3': ('2n-n3.csv',       '4n-n3.csv','5n-n3.csv'),
    'n4': ('3n-n4.csv',),
    'n5': ('3n-n5.csv',),
    'p1': ('2p-p1.csv', '4p-p1.csv', '5p-p1.csv'),
    'p2': ('2p-p2.csv', '4p-p2.csv', '5p-p2.csv'),
    'p3': ('2p-p3.csv', '4p-p3.csv', '5p-p3.csv'),
    'p4': ('3p-p4.csv',),
    'p5': ('3p-p5.csv',),
}

CSV_IdVd = {
    'n1': ('7n-n1.csv','6n-n1.csv'),
    'n2': ('7n-n2.csv','6n-n2.csv'),
    'n3': ('7n-n3.csv','6n-n3.csv'),
    'n4': ('8n-n4.csv',),
    'n5': ('8n-n5.csv',),
    'p1': ('7p-p1.csv', '6p-p1.csv'),
    'p2': ('7p-p2.csv', '6p-p2.csv'),
    'p3': ('7p-p3.csv', '6p-p3.csv'),
    'p4': ('8p-p4.csv',),
    'p5': ('8p-p5.csv',),
}

Vconst = {
    '2n-n1-170327.csv': ('Vd', 0.05),
    '2n-n2-170327.csv': ('Vd', 0.05),
    '2n-n3.csv': ('Vd', 0.05),
    '3n-n4.csv': ('Vd', 0.05),
    '3n-n5.csv': ('Vd', 0.05),
    '4n-n1.csv': ('Vb', -5.0),
    '4n-n2.csv': ('Vb', -5.0),
    '4n-n3.csv': ('Vb', -5.0),
    '5n-n1.csv': ('Vd', 5.0),
    '5n-n2.csv': ('Vd', 5.0),
    '5n-n3.csv': ('Vd', 5.0),
    '6n-n1.csv': ('Vg', 2.5),
    '6n-n2.csv': ('Vg', 2.5),
    '6n-n3.csv': ('Vg', 2.5),
    '7n-n1.csv': ('Vb', 0.0),
    '7n-n2.csv': ('Vb', 0.0),
    '7n-n3.csv': ('Vb', 0.0),
    '8n-n4.csv': ('Vb', 0.0),
    '8n-n5.csv': ('Vb', 0.0),
    '2p-p1.csv': ('Vd', 0.05),
    '2p-p2.csv': ('Vd', 0.05),
    '2p-p3.csv': ('Vd', 0.05),
    '3p-p4.csv': ('Vd', 0.05),
    '3p-p5.csv': ('Vd', 0.05),
    '4p-p1.csv': ('Vb', -5.0),
    '4p-p2.csv': ('Vb', -5.0),
    '4p-p3.csv': ('Vb', -5.0),
    '5p-p1.csv': ('Vd', 5.0),
    '5p-p2.csv': ('Vd', 5.0),
    '5p-p3.csv': ('Vd', 5.0),
    '6p-p1.csv': ('Vg', 2.5),
    '6p-p2.csv': ('Vg', 2.5),
    '6p-p3.csv': ('Vg', 2.5),
    '7p-p1.csv': ('Vb', 0.0),
    '7p-p2.csv': ('Vb', 0.0),
    '7p-p3.csv': ('Vb', 0.0),
    '8p-p4.csv': ('Vb', 0.0),
    '8p-p5.csv': ('Vb', 0.0),
}


# Teg Name to Device Properties Map
DevSize = {'n1': {'L':0.6e-6, 'W':15.e-6, 'M':1.},
           'n2': {'L':1.8e-6, 'W':15.e-6, 'M':1.},
           'n3': {'L':15.e-6, 'W':15.e-6, 'M':1.},
           'n4': {'L':15.e-6, 'W':3.0e-6, 'M':5.},
           'n5': {'L':15.e-6, 'W':1.8e-6, 'M':8.},
           'p1': {'L':0.6e-6, 'W':15.e-6, 'M':1.},
           'p2': {'L':1.8e-6, 'W':15.e-6, 'M':1.},
           'p3': {'L':15.e-6, 'W':15.e-6, 'M':1.},
           'p4': {'L':15.e-6, 'W':3.0e-6, 'M':5.},
           'p5': {'L':15.e-6, 'W':1.8e-6, 'M':8.},
           }

# IdVg curve
for TegName, FileList in CSV_IdVg.items():
    print('$ Aurora File: n/a        Date:   Misc: ')
    print('$ Atem File: %s.gtr' % (TegName))
    print('VARIABLE W = %e' % (DevSize[TegName]['W']))
    print('VARIABLE L = %e' % (DevSize[TegName]['L']))
    print('VARIABLE T = 25')
    print('VARIABLE REGION = 0')
    print('')
    print('TABLE VGS  VBS  VDS  ID')

    for file in FileList:
        src = np.loadtxt(file, delimiter=',', skiprows=1)
        const, volt = Vconst[file]

        if re.match(r".p", file): # pmos
            type = -1
        else:
            type = 1

        vgs = src[:,0] * type
        if const == 'Vd':
            vbs = src[:, 1] * type
            vds = [volt] * len(vgs)
        elif const == 'Vb':
            vbs = [volt] * len(vgs)
            vds = src[:, 1] * type
        #id = src[:, 3]/ DevSize[TegName]['M']
        id = (src[:,2]+src[:,3])/2./DevSize[TegName]['M'] * type
        for col in range(vgs.shape[0]):
            if round(vgs[col]*1e3) % round(Vstep*1e3) == 0:
                print("%e   %e   %e   %e" % (vgs[col], vbs[col], vds[col], id[col]))
    print ("")

# IdVd curve
for TegName, FileList in CSV_IdVd.items():
    print('$ Aurora File: n/a        Date:   Misc: ')
    print('$ Atem File: %s.drr' % (TegName))
    print('VARIABLE W = %e' % (DevSize[TegName]['W']))
    print('VARIABLE L = %e' % (DevSize[TegName]['L']))
    print('VARIABLE T = 25')
    print('VARIABLE REGION = 1')
    print('')
    print('TABLE VDS  VGS  VBS  ID')

    for file in FileList:
        src = np.loadtxt(file, delimiter=',', skiprows=1)
        const, volt = Vconst[file]

        if re.match(r".p", file): # pmos
            type = -1
        else:
            type = 1

        vds = src[:,0] * type
        if const == 'Vg':
            vgs = [volt] * len(vds)
            vbs = src[:,1] * type
        elif const == 'Vb':
            vgs = src[:,1] * type
            vbs = [volt] * len(vds)
        #id = src[:, 3] / DevSize[TegName]['M']
        id = (src[:,2]+src[:,3])/2./DevSize[TegName]['M'] * type
        for col in range(vds.shape[0]):
            if round(vds[col]*1e3) % round(Vstep*1e3) == 0:
                print("%e   %e   %e   %e" % (vds[col], vgs[col], vbs[col], id[col]))
    print ("")
