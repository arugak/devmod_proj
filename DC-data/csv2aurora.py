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
      2.5   0.0   *  *  *        6n
           -0.5   *  *  *
           -1.0   *  *  *
           -1.5   *  *  *
           -2.0   *  *  *
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

import numpy as np

# Teg Name to CSV file list Map
# 2n-n3.csv == 1n-n3.csv == 3n-n3.csv
CSV_IdVg = {
    'n1': ('2n-n1-170327.csv','5n-n1.csv'),
    'n2': ('2n-n2-170327.csv','5n-n2.csv'),
    'n3': ('2n-n3.csv','5n-n3.csv'),
    'n4': ('3n-n4.csv',),
    'n5': ('3n-n5.csv',),
}

CSV_IdVd = {
    'n1': ('7n-n1.csv',),
    'n2': ('7n-n2.csv',),
    'n3': ('7n-n3.csv',),
    'n4': ('8n-n4.csv',),
    'n5': ('8n-n5.csv',),}

Vconst = {
    # Vds for IdVg curve
    '2n-n1-170327.csv': 0.05,
    '2n-n2-170327.csv': 0.05,
    '2n-n3.csv': 0.05,
    '3n-n4.csv': 0.05,
    '3n-n5.csv': 0.05,
    '5n-n1.csv': 5.0,
    '5n-n2.csv': 5.0,
    '5n-n3.csv': 5.0,
}

# Teg Name to Device Properties Map
DevSize = {'n1': {'L':0.6e-6, 'W':15.e-6, 'M':1.},
           'n2': {'L':1.8e-6, 'W':15.e-6, 'M':1.},
           'n3': {'L':15.e-6, 'W':15.e-6, 'M':1.},
           'n4': {'L':15.e-6, 'W':3.0e-6, 'M':5.},
           'n5': {'L':15.e-6, 'W':1.8e-6, 'M':8.},
           }

Vstep = 0.01

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
        vgs = src[:,0]
        vbs = src[:,1]
        id = (src[:,2]+src[:,3])/2./DevSize[TegName]['M']
        for col in range(vgs.shape[0]):
            if round(vgs[col]*1e3) % round(Vstep*1e3) == 0:
                print("%e   %e   %e   %e" % (vgs[col], vbs[col], Vconst[file], id[col]))
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
        vds = src[:,0]
        vgs = src[:,1]
        id = (src[:,2]+src[:,3])/2./DevSize[TegName]['M']
        for col in range(vds.shape[0]):
            if round(vds[col]*1e3) % round(Vstep*1e3) == 0:
                print("%e   %e   %e   %e" % (vds[col], vgs[col], 0., id[col]))
    print ("")
