# -*- coding: utf-8 -*-

from BSIM3v3Param import *
from MOSp35Data import *


class MOSp35Proj(MOSp35Data):
    def __init__(self, param0):
        super(MOSp35Proj, self).__init__(param0)

    def step10(self):
        targets = ['U0', 'VTH0', 'UA', 'UB', 'NFACTOR', 'VOFF']
        fit = MOS_IV_Fit(self.param, targets, 'Step 1-0')
        fit.setDataSource(self.IdVg_LW_lin_b0)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)

        self.acceptParam(result, targets)

        return result, err

    def step12(self):
        targets = ['NFACTOR', 'VOFF']
        fit = MOS_IV_Fit(self.param, targets, 'Step 1-2')
        fit.setDataSource(1 * self.IdVg_LW_lin_b0.copy())

        fit.dataSrc.setSubVth(True)
        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)

        return result, err

    def step20(self):
        targets=['K1', 'K2', 'UC']
        fit = MOS_IV_Fit(self.param, targets, 'Step 2')
        fit.setDataSource(self.IdVg_LW_lin_ba.copy())

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)

        self.acceptParam(result, targets)

        return result, err

    def step30(self):
        targets = ['NFACTOR', 'VOFF']
        fit = MOS_IV_Fit(self.param, targets, 'Step 3')
        fit.setDataSource(0 * self.IdVg_LW_lin_ba.copy())

        fit.dataSrc.setSubVth(True)
        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)

        return result, err


    def step40(self):
        #targets = ['K3', 'WVTH0', 'W0', 'WINT', 'U0', 'WR', 'DWG']
        targets = ['K3', 'W0', 'WINT', 'VTH0', 'U0', 'WU0', 'DWG']
        #targets = ['WINT', 'VTH0', 'WVTH0']
        fit = MOS_IV_Fit(self.param, targets, 'Step 4-0')
        fit.setDataSource(1. * self.IdVg_LW_lin_b0+
                          6. * self.IdVg_LM_lin_b0+
                          0 * 12. * self.IdVg_LN_lin_b0)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)

        self.acceptParam(result, targets)

        return result, err

    def step42(self):
        #targets = ['WINT', 'U0', 'WU0', 'VTH0', 'WVTH0', 'WR']
        targets = ['K3', 'W0', 'WINT', 'VTH0', 'WVTH0', 'U0', 'WU0', 'WR', 'DWG' ]
        fit = MOS_IV_Fit(self.param, targets, 'Step 4-2')
        fit.setDataSource(1. * self.IdVg_LW_lin_b0+
                          6. * self.IdVg_LM_lin_b0+
                          12. * self.IdVg_LN_lin_b0)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)

        self.acceptParam(result, targets)

        return result, err

    def step50(self):
        targets = ['K3B', 'DWB']
        fit = MOS_IV_Fit(self.param, targets, 'Step 5')
        fit.setDataSource(1. * self.IdVg_LW_lin_ba+
                          6. * self.IdVg_LM_lin_ba+
                          12. * self.IdVg_LN_lin_ba)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)

        return result, err


    def step70(self):
        #targets = ['LINT', 'RDSW', 'PRWG', 'DVT0', 'DVT1', 'NLX', 'U0', 'VTH0']
        targets = ['LINT', 'NLX', 'DVT0', 'DVT1', 'RDSW', 'U0', 'VTH0']
        fit = MOS_IV_Fit(self.param, targets, 'Step 7-0')
        fit.setDataSource(        self.IdVg_LW_lin_b0 +
                           0.12 * self.IdVg_MW_lin_b0 +
                           0 * 0.06 * self.IdVg_SW_lin_b0)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)

        return result, err

    def step72(self):
        targets = ['LINT', 'NLX', 'DVT0', 'DVT1', 'RDSW', 'U0', 'VTH0']
        fit = MOS_IV_Fit(self.param, targets, 'Step 7-2')
        fit.setDataSource(       self.IdVg_LW_lin_b0 +
                          0.12 * self.IdVg_MW_lin_b0 +
                          0.06 * self.IdVg_SW_lin_b0)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)

        return result, err

    def step74(self):
        targets = ['LINT', 'NLX', 'DVT0', 'DVT1', 'RDSW', 'PRWB', 'DVT2', 'U0', 'VTH0', 'LVTH0']
        fit = MOS_IV_Fit(self.param, targets, 'Step 7-4')
        fit.setDataSource(       self.IdVg_LW_lin_ba +
                          0.12 * self.IdVg_MW_lin_ba +
                          0.06 * self.IdVg_SW_lin_ba)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)

        return result, err


    def step80(self):
        targets = [
            'U0', 'WU0', 'VTH0', 'WVTH0', 'LVTH0', 'K1', 'K2', 'UA', 'UB', 'UC',
            'K3', 'K3B', 'W0', 'WR', 'WINT', 'DWG', 'DWB',
            'LINT', 'RDSW', 'PRWB', 'DVT0', 'DVT1', 'DVT2', 'NLX'
        ]
        fit = MOS_IV_Fit(self.param, targets, 'Step 8')
        fit.setDataSource(       self.IdVg_LW_lin_ba +
                          0.12 * self.IdVg_MW_lin_ba +
                          0.06 * self.IdVg_SW_lin_ba +
                          6   * self.IdVg_LM_lin_ba +
                          12 * self.IdVg_LN_lin_ba)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)
        return result, err


    def skip_step120(self):
        targets = ['A0', 'AGS', 'KETA']
        fit = MOS_IV_Fit(self.param, targets, 'Step 12')
        fit.setDataSource(self.IdVg_LW_sat_ba)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)
        return result, err


    def step130(self):
        targets = ['A0', 'AGS', 'VSAT']
        #targets = ['A0', 'AGS', 'VSAT', 'A1', 'A2', 'DELTA']
        #targets = ['A0', 'AGS', 'VSAT', 'DSUB', 'ETA0', 'A1', 'A2', 'PCLM']
        fit = MOS_IV_Fit(self.param, targets, 'Step 13-0')
        fit.setDataSource( 0.06 * self.IdVd_SW_b0+
                           0.12 * self.IdVd_MW_b0+
                           1.0  * self.IdVd_LW_b0)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)
        return result, err

    # PCLM
    def step131(self):
        targets = ['A0', 'LA0', 'AGS', 'VSAT', 'PCLM']
        fit = MOS_IV_Fit(self.param, targets, 'Step 13-1')
        fit.setDataSource( 0.06 * self.IdVd_SW_b0+
                           0.12 * self.IdVd_MW_b0+
                           1.00 * self.IdVd_LW_b0)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)
        return result, err


    def step134(self):
        targets = ['KETA', 'DSUB', 'ETA0', 'ETAB']
        fit = MOS_IV_Fit(self.param, targets, 'Step 13-4')
        fit.setDataSource( 0.06 * self.IdVg_SW_sat_ba+
                           0.12 * self.IdVg_MW_sat_ba+
                           1.0  * self.IdVg_LW_sat_ba)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)
        return result, err

    #PCLM
    def step135(self):
        targets = ['ETA0', 'DSUB', 'ETAB', 'KETA', 'PCLM']
        fit = MOS_IV_Fit(self.param, targets, 'Step 13-5')
        fit.setDataSource( 0    * self.IdVd_LW_g25_ba +
                           0.12 * self.IdVd_MW_g25_ba +
                           0.06 * self.IdVd_SW_g25_ba
        )

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)
        return result, err

    def step136(self):
        targets = ['A0', 'LA0', 'AGS', 'VSAT']
        fit = MOS_IV_Fit(self.param, targets, 'Step 13-6')
        fit.setDataSource( 0.06 * self.IdVd_SW_b0+
                           0.12 * self.IdVd_MW_b0+
                           1.0  * self.IdVd_LW_b0+
                           0    * self.IdVd_LW_g25_ba +
                           0    * self.IdVd_MW_g25_ba +
                           0    * self.IdVd_SW_g25_ba)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)
        return result, err


    def step140(self):
        targets = ['B0', 'B1']
        fit = MOS_IV_Fit(self.param, targets, 'Step 14')
        fit.setDataSource(1.0 *self.IdVd_LW_b0+
                          6.0 *self.IdVd_LM_b0+
                          13. *self.IdVd_LN_b0)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)
        return result, err



    def step300(self):
        targets = ['VTH0'] # dummy
        fit = MOS_IV_Fit(self.param, targets, 'Step 300')
        fit.setDataSource(
            0 * self.IdVg_LW_lin_ba +
            0 * self.IdVg_MW_lin_ba +
            0 * self.IdVg_SW_lin_ba +
            0 * self.IdVg_LM_lin_ba +
            0 * self.IdVg_LN_lin_ba +
            0 * self.IdVg_LW_sat_ba +
            0 * self.IdVg_MW_sat_ba +
            0 * self.IdVg_SW_sat_ba +
            0 * self.IdVd_SW_b0 +
            0 * self.IdVd_MW_b0 +
            0 * self.IdVd_LW_b0 +
            0 * self.IdVd_LM_b0 +
            0 * self.IdVd_LN_b0 +
            0 * self.IdVd_SW_g25_ba +
            0 * self.IdVd_MW_g25_ba +
            0 * self.IdVd_LW_g25_ba
        )

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)

        return result, err

    def step310(self):
        targets = ['VTH0']  # dummy
        fit = MOS_IV_Fit(self.param, targets, 'Step 310')
        fit.setDataSource(
            0 * self.IdVg_LW_lin_ba +
            0 * self.IdVg_MW_lin_ba +
            0 * self.IdVg_SW_lin_ba +
            0 * self.IdVg_LM_lin_ba +
            0 * self.IdVg_LN_lin_ba +
            0 * self.IdVg_LW_sat_ba +
            0 * self.IdVg_MW_sat_ba +
            0 * self.IdVg_SW_sat_ba)

        fit.dataSrc.setSubVth(True)
        result, err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)

        i = 0
        s = ''
        keys = self.param.keys()
        keys.sort()
        for k in keys:
            v = self.param[k]
            if isinstance(v, tuple):
                v = v[0]
            if k == 'TEMP':
                s += '*'
            if k == 'VTH0' or k == 'LVTH0' or k == 'WVTH0' or k == 'PVTH0':
                v = -1.0 * v
            s += '+ %-8s= %-12G\n' % (k, v)
            i += 1

        f = open('pyeda.l', 'w')
        f.write(s)
        f.close() # ????????
        return result, err

param0['TEMP']=25.
param0['TNOM']=25.

proj = MOSp35Proj(param0)
1
