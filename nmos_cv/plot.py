# -*- coding: utf-8 -*-

#PTS16のCV測定結果から、プロットを作成する

import matplotlib.pyplot as plt
import numpy as np

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

for num_prefix in ('01','02','03','04','05','07','06','08','09','10','11','12','13','14','15','16'):
    fig = plt.figure()
    for model in ('CSRS','CPRP'):
        if model == 'CSRS':
            fig.add_subplot(2, 1, 1)
        else:
            fig.add_subplot(2, 1, 2)
        for freq in ('100k','1000k'):
            filebase = num_prefix + '_' + model + '_' + freq
            m = np.loadtxt('../AC-data/' + filebase + '.csv', delimiter=',')
            n = np.loadtxt('../AC-data/17_' + model + '_' + freq + '.csv', delimiter=',')
            v = m[:,0]
            c = m[:,1] - n[:,1]
            plt.plot(v,c*1e12,label=freq)
            plt.title(num_prefix + '_' + model)
            plt.legend(loc="best")
            plt.xlabel("Volt[V]")
            plt.ylabel("Cap[pF]")
            if num_prefix in ('03','04','10','11','16'):
                plt.ylim(0,16)
            elif num_prefix == '08':
                plt.ylim(0,35)

        plt.grid()
    plt.tight_layout()
    fig.show()
    plt.savefig(num_prefix + ".png")
    plt.close(fig)