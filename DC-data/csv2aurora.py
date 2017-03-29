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
Vgs   Vbs    Vds  n1 n2 n3 n4 n5
      0.0   0.05  *  *  *  *  *
     -0.5         *  *  *  *  *
     -1.0         *  *  *  *  *
     -1.5         *  *  *  *  *
     -2.0         *  *  *  *  *
     -2.5         *  *  *  *  *
     -3.0         *  *  *  *  *
     -5.0   0.0   *  *  *
            0.5   *  *  *
            1.0   *  *  *
            1.5   *  *  *
            2.0   *  *  *
            2.5   *  *  *
            3.5   *  *  *
            4.0   *  *  *
            4.5   *  *  *
            5.0   *  *  *
      0.0   5.0   *  *  *
     -0.5         *  *  *
     -1.0         *  *  *
     -1.5         *  *  *
     -2.0         *  *  *
     -2.5         *  *  *
     -3.0         *  *  *

*** IdVd
Vds   Vg    Vb    TegName
      0.0   0.0   1  2  3  4  5
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
      0.0   -5.0  *  *  *
      1.0         *  *  *
      2.0         *  *  *
      3.0         *  *  *
      4.0         *  *  *
      5.0         *  *  *
'''

import numpy as np

# Teg Name to CSV file list Map
CSV_IdVg = {'n1': ('2n-n1-170327.csv',),
            'n2': ('2n-n2-170327.csv',),
            'n3': ('2n-n3.csv',),
            'n4': ('3n-n4.csv',),
            'n5': ('3n-n5.csv',),
            }

# Teg Name to Device Properties Map
DevSize = {'n1': {'L':0.6e-6, 'W':15.e-6, 'M':1.},
           'n2': {'L':1.8e-6, 'W':15.e-6, 'M':1.},
           'n3': {'L':15.e-6, 'W':15.e-6, 'M':1.},
           'n4': {'L':15.e-6, 'W':3.0e-6, 'M':5.},
           'n5': {'L':15.e-6, 'W':1.8e-6, 'M':8.},
           }

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
        src_avg = (src[:,2]+src[:,3])/2./DevSize[TegName]['M']
        for col in range(src_avg.shape[0]):
            print("%e   %e   %e   %e" % (src[col,0], src[col,1], 0.05, src_avg[col]))
    print ("")
