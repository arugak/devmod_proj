# -*- coding: utf-8 -*-

from BSIM3v3Param import *
from MOSp35Data import *


class MOSp35Proj(MOSp35Data):
    def __init__(self, param0):
        super(MOSp35Proj, self).__init__(param0)

    def step10(self):
        targets = ['U0', 'VTH0', 'K1', 'K2', 'UA', 'UB', 'UC']
        fit = MOS_IV_Fit(self.param, targets, 'Step 1')
        fit.setDataSource(self.IdVg_LW_lin_ba)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)

        self.acceptParam(result, targets)

        return result, err


    def step30(self):
        #targets = ['NFACTOR', 'VOFF']
        targets = ['VOFF']
        fit = MOS_IV_Fit(self.param, targets, 'Step 3')
        fit.setDataSource(1* self.IdVg_LW_lin_b0.copy() +
                          0* self.IdVg_LW_lin_ba.copy())

        fit.dataSrc.setSubVth(True)
        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)

        return result, err

    def step40(self):
        targets = ['K3', 'K3B', 'WINT', 'DWG', 'DWB', 'U0']
        fit = MOS_IV_Fit(self.param, targets, 'Step 4')
        fit.setDataSource(1   * self.IdVg_LW_lin_ba+
                          5   * self.IdVg_LM_lin_ba+
                          8.3 * self.IdVg_LN_lin_ba)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)

        self.acceptParam(result, targets)

        return result, err

    def step70(self):
        targets = ['LINT', 'RDSW', 'PRWG', 'DVT0', 'DVT1', 'NLX', 'U0']
        fit = MOS_IV_Fit(self.param, targets, 'Step 7-0')
        fit.setDataSource(       self.IdVg_LW_lin_b0 +
                           0.12* self.IdVg_MW_lin_b0 +
                           0.06* self.IdVg_SW_lin_b0)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)

        return result, err

    def step72(self):
        targets = ['LINT', 'RDSW', 'PRWB', 'DVT0', 'DVT1', 'DVT2', 'NLX']
        fit = MOS_IV_Fit(self.param, targets, 'Step 7-2')
        fit.setDataSource(      self.IdVg_LW_lin_ba +
                          0.12* self.IdVg_MW_lin_ba +
                          0.06* self.IdVg_SW_lin_ba)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)

        return result, err



    def step80(self):
        targets = [
            'U0', 'K1', 'K2', 'UA', 'UB', 'UC', 'VTH0',
            'K3', 'K3B', 'WINT', 'DWG', 'DWB',
            'LINT', 'RDSW', 'PRWG', 'PRWB', 'DVT0', 'DVT1', 'DVT2', 'NLX'
        ]
        fit = MOS_IV_Fit(self.param, targets, 'Step 8')
        fit.setDataSource(       self.IdVg_LW_lin_ba +
                          0.12 * self.IdVg_MW_lin_ba +
                          0.06 * self.IdVg_SW_lin_ba +
                          5.   * self.IdVg_LM_lin_ba +
                          8.3  * self.IdVg_LN_lin_ba)

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
        #targets = ['A0', 'AGS', 'VSAT']
        targets = ['A0', 'AGS', 'VSAT', 'A1', 'A2', 'DELTA']
        fit = MOS_IV_Fit(self.param, targets, 'Step 13')
        fit.setDataSource( 0.1 * self.IdVd_SW_b0+
                           0.2 * self.IdVd_MW_b0+
                           1.0 * self.IdVd_LW_b0)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)
        return result, err

    def step132(self):
        #targets = ['A0', 'AGS', 'VSAT']
        targets = ['A0', 'AGS', 'VSAT', 'A1', 'A2', 'PCLM']
        fit = MOS_IV_Fit(self.param, targets, 'Step 13-2')
        fit.setDataSource( 0.1 * self.IdVd_SW_b0+
                           0.2 * self.IdVd_MW_b0+
                           1.0 * self.IdVd_LW_b0)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)
        return result, err

    def step140(self):
        targets = ['B0', 'B1']
        fit = MOS_IV_Fit(self.param, targets, 'Step 14')
        fit.setDataSource(1.0 *self.IdVd_LW_b0+
                          5.0 *self.IdVd_LM_b0+
                          8.3 *self.IdVd_LN_b0)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)
        return result, err


    def step170(self):
        targets = ['ETA0', 'DSUB']
        fit = MOS_IV_Fit(self.param, targets, 'Step 17')
        fit.setDataSource(     self.IdVg_LW_sat_b0+ 
                          0.2 *self.IdVg_MW_sat_b0+
                          0.1 *self.IdVg_SW_sat_b0)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)
        return result, err


    def step180(self):
        targets = ['ETAB', 'KETA']
        fit = MOS_IV_Fit(self.param, targets, 'Step 18')
        fit.setDataSource(     self.IdVg_LW_sat_ba+
                          0.2 *self.IdVg_MW_sat_ba+
                          0.1*self.IdVg_SW_sat_ba)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)
        return result, err


    def step200(self):
        targets = ['CDSCD']
        fit = MOS_IV_Fit(self.param, targets, 'Step 20')
        fit.setDataSource(      self.IdVg_LW_sat_b0.copy()+
                          0.2 * self.IdVg_MW_sat_b0.copy()+
                          0.1 * self.IdVg_SW_sat_b0.copy())

        fit.dataSrc.setSubVth(True)
        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)

        return result, err

    def step205(self):
        targets = ['CDSCB']
        fit = MOS_IV_Fit(self.param, targets, 'Step 20-5')
        fit.setDataSource(0*     self.IdVg_LW_sat_ba.copy()+
                          0*0.2 *self.IdVg_MW_sat_ba.copy()+
                          0*0.1 *self.IdVg_SW_sat_ba.copy())

        fit.dataSrc.setSubVth(True)
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

        i = 0
        s = ''
        keys = self.param.keys()
        keys.sort()
        for k in keys:
            v = self.param[k]
            if isinstance(v, tuple):
                v = v[0]
            s += '+ %-8s= %-12G\n' % (k, v)
            i += 1

        f = open('pyeda.l', 'w')
        f.write(s)
        f.close() # ????????
        return result, err

param0['TEMP']=25.
param0['TNOM']=25.

proj = MOSp35Proj(param0)
proj.run(300,300)

