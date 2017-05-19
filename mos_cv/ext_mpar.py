# -*- coding: utf-8 -*-

#PTS16のCV測定結果から、関連するモデルパラメータを計算する

#ファイル名先頭 TEG種類 仕様書TEG番号
#01 p120x18x6   12
#02 p6x120x14   14
#03 PN_B        16
#04 PN_SIDE     17
#05 p120x1.8x34 13
#06 p0.6x120x40 15
#07 p120x120x1  11
#08 n120x18x6   3
#09 n6x120x14   5
#10 NP_B        7
#11 NP_SIDE     8
#12 n120x1.8x34 4
#13 n0.6x120x40 6
#14 n120x120x1  2
#15 POLY-Metal  10
#16 Nwell-Psub  9
#17 OPEN        1

import sys

import numpy as np

args = sys.argv

if (args[1] == 'pmos'):
    type = 'pmos'
elif (args[1] == 'nmos'):
    type = 'nmos'
else:
    print 'Usage: python %s pmos|nmos' % args[0]
    quit()

epsOx   = 3.453133e-11     # BSIM3のソースコードの値

# load open cv
cv = np.loadtxt('../AC-data/17_CSRS_100k.csv', delimiter=',')
openc_csrs_100k = cv[:,1]
cv = np.loadtxt('../AC-data/17_CPRP_100k.csv', delimiter=',')
openc_cprp_100k = cv[:,1]
cv = np.loadtxt('../AC-data/17_CSRS_1000k.csv', delimiter=',')
openc_csrs_1000k = cv[:,1]
cv = np.loadtxt('../AC-data/17_CPRP_1000k.csv', delimiter=',')
openc_cprp_1000k = cv[:,1]

params = {}

# extract TOX
# Vg=-5.0V(蓄積)のCggから計算
if type == 'nmos':
    cv = np.loadtxt('../AC-data/14_CSRS_100k.csv', delimiter=',')
    c_raw = cv[:, 1]
    c = c_raw - openc_csrs_100k
    Cgg_acc = c[150]
elif type == 'pmos':
    cv = np.loadtxt('../AC-data/07_CSRS_100k.csv', delimiter=',')
    c_raw = cv[:, 1]
    c = c_raw - openc_csrs_100k
    Cgg_acc = c[50]

params['TOX'] = epsOx * 120e-6 * 120e-6 / Cgg_acc

# extract CGSO, CGDO
# Vg=+5.0(強反転)のCggから計算
if type == 'nmos':
    # L=6.0u, M=14
    cv = np.loadtxt('../AC-data/09_CSRS_100k.csv', delimiter=',')
    c_raw = cv[:, 1]
    c = c_raw - openc_csrs_100k
    Cgg_inv_L60 = c[50] / 14

    # L=0.6u, M=40
    cv = np.loadtxt('../AC-data/13_CSRS_100k.csv', delimiter=',')
    c_raw = cv[:, 1]
    c = c_raw - openc_csrs_100k
    Cgg_inv_L06 = c[50] / 40

if type == 'pmos':
    # L=6.0u, M=14
    cv = np.loadtxt('../AC-data/02_CSRS_100k.csv', delimiter=',')
    c_raw = cv[:, 1]
    c = c_raw - openc_csrs_100k
    Cgg_inv_L60 = c[50] / 14

    # L=0.6u, M=40
    cv = np.loadtxt('../AC-data/06_CSRS_100k.csv', delimiter=',')
    c_raw = cv[:, 1]
    c = c_raw - openc_csrs_100k
    Cgg_inv_L06 = c[150] / 40

params['CGDO'] = (Cgg_inv_L06 - (Cgg_inv_L60 - Cgg_inv_L06) / (6.0e-6 - 0.6e-6) * 0.6e-6 ) / 120e-6 / 2.0
params['CGSO'] = params['CGDO']
params['CF'] = 0.  # CFとCGDOは並列関係。CFはパラメータが設定されていないと自動的に計算された値が入ってしまうのでゼロを設定

'''
結果がマイナスになってしまうので省略
# extract CGB0
# Vg=+5.0(強反転)のCggから計算
if type == 'nmos':
    # W=18u, M=6
    cv = np.loadtxt('../AC-data/08_CSRS_100k.csv', delimiter=',')
    c_raw = cv[:, 1]
    c = c_raw - openc_csrs_100k
    Cgg_inv_W180 = c[50] / 6

    # W=1.8u, M=34
    cv = np.loadtxt('../AC-data/12_CSRS_100k.csv', delimiter=',')
    c_raw = cv[:, 1]
    c = c_raw - openc_csrs_100k
    Cgg_inv_W018 = c[50] / 34

if type == 'pmos':
    pass
print Cgg_inv_W018
print Cgg_inv_W180
CGB0 = (Cgg_inv_W018 - (Cgg_inv_W180 - Cgg_inv_W018) / (18.e-6 - 1.8e-6) * 1.8e-6 ) / 120e-6
print('paramcap_%s={\'CGB0\', %e}' % (type, CGB0))
'''

# extract CJ CJSW
# とりあえずゼロバイアス単位容量CJ, CJSWのみ実装
# CVカーブがあるので、フィッティングすればMJ等も抽出できる。
if type == 'nmos':
    cv = np.loadtxt('../AC-data/10_CSRS_100k.csv', delimiter=',')
    c_raw = cv[:,1]
    c  = c_raw - openc_csrs_100k
    Cb = c[100]
    cv = np.loadtxt('../AC-data/11_CSRS_100k.csv', delimiter=',')
    c_raw = cv[:,1]
    c  = c_raw - openc_csrs_100k
    Cs = c[100]
elif type == 'pmos':
    cv = np.loadtxt('../AC-data/03_CSRS_100k.csv', delimiter=',')
    c_raw = cv[:,1]
    c  = c_raw - openc_csrs_100k
    Cb = c[100]
    cv = np.loadtxt('../AC-data/04_CSRS_100k.csv', delimiter=',')
    c_raw = cv[:,1]
    c  = c_raw - openc_csrs_100k
    Cs = c[100]

Ab = 120e-6 * 120e-6
As = 120e-6 * 1.8e-6 * 40
Pb = 120e-6 * 4
Ps = (120e-6 + 1.8e-6) * 2 * 40

params['CJ'] = (Cb/Pb-Cs/Ps)/(Ab/Pb - As/Ps)
params['CJSW'] = (Cb/Ab - Cs/As) / (Pb/Ab - Ps/As)

for param, value in params.items():
    if (param == 'TOX'):
        print '*',
    print ('+ %-8s= %-12G' % (param, value))

