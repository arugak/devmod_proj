# -*- coding: utf-8 -*-

from BSIM3v3Param import *
from MOSp35Data import *

class MOSp35Proj(MOSp35Data):
    def __init__(self, param0):
        super(MOSp35Proj, self).__init__(param0)

    def step10(self):
        targets=['VTH0', 'U0', 'UA', 'UB']
        fit = MOS_IV_Fit(self.param, targets, 'Step 1')
        fit.setDataSource(self.IdVg_LW_lin_b0)

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
        fit.setDataSource(self.IdVg_LW_lin_ba.copy())

        fit.dataSrc.setSubVth(True)
        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)

        return result, err

    def step40(self):
        targets = ['K3', 'W0', 'WINT', 'U0']
        fit = MOS_IV_Fit(self.param, targets, 'Step 4')
        fit.setDataSource(1. * self.IdVg_LW_lin_b0+
                          0*6. * self.IdVg_LM_lin_b0+
                          13 * self.IdVg_LN_lin_b0)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)

        self.acceptParam(result, targets)

        return result, err

    def step50(self):
        targets = ['K3B', 'DWB']
        fit = MOS_IV_Fit(self.param, targets, 'Step 5')
        fit.setDataSource(1   * self.IdVg_LW_lin_ba+
                          0*6 * self.IdVg_LM_lin_ba+
                          13  * self.IdVg_LN_lin_ba)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)

        return result, err


    def step70(self):
        #targets = ['LINT', 'RDSW', 'PRWG', 'DVT0', 'DVT1', 'NLX', 'U0']
        targets = ['LINT', 'RDSW', 'PRWG', 'NLX', 'U0']
        fit = MOS_IV_Fit(self.param, targets, 'Step 7-0')
        fit.setDataSource(        self.IdVg_LW_lin_b0 +
                           0.12 * self.IdVg_MW_lin_b0 +
                           0 * 0.06 * self.IdVg_SW_lin_b0_2)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)

        return result, err


    def step71(self):
        #targets = ['LINT', 'RDSW', 'PRWG', 'DVT0', 'DVT1', 'NLX', 'U0']
        targets = ['LINT', 'RDSW', 'PRWG', 'DVT0', 'DVT1', 'U0']
        fit = MOS_IV_Fit(self.param, targets, 'Step 7-1')
        fit.setDataSource(        self.IdVg_LW_lin_b0 +
                           0.12 * self.IdVg_MW_lin_b0 +
                           0 * self.IdVg_SW_lin_b0 +
                           10*0.06 * self.IdVg_SW_lin_b0_2 +
                           0 * self.IdVg_LW_lin_b0_2 +
                           0 * self.IdVg_MW_lin_b0_2
                                  )

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)

        return result, err

    def step72(self):
        targets = ['LINT', 'RDSW', 'PRWB', 'DVT1', 'DVT2', 'NLX']
        #targets = ['LINT', 'RDSW', 'PRWB', 'DVT0', 'DVT1', 'DVT2', 'NLX']
        fit = MOS_IV_Fit(self.param, targets, 'Step 7-2')
        fit.setDataSource(       self.IdVg_LW_lin_ba +
                          0.12 * self.IdVg_MW_lin_ba +
                          0*0.06 * self.IdVg_SW_lin_ba +
                          0*0.06 * self.IdVg_SW_lin_b0_2)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)

        return result, err


    def skip_step80(self):
        targets = [
            'U0', 'K1', 'K2', 'UA', 'UB', 'UC', 'VTH0',
            'K3', 'K3B', 'WINT', 'DWG', 'DWB',
            'LINT', 'RDSW', 'PRWB', 'DVT0', 'DVT1', 'DVT2', 'NLX'
        ]
        fit = MOS_IV_Fit(self.param, targets, 'Step 8')
        fit.setDataSource(       self.IdVg_LW_lin_ba +
                          0.12 * self.IdVg_MW_lin_ba +
                          0 * 0.06 * self.IdVg_SW_lin_ba +
                          0.06 * self.IdVg_SW_lin_b0_2 +
                          0 * 6   * self.IdVg_LM_lin_ba +
                          13 * self.IdVg_LN_lin_ba)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)
        return result, err

    def step130(self):
        #targets = ['A0', 'AGS', 'VSAT', 'DSUB', 'ETA0', 'A1', 'A2', 'PCLM']
        targets = ['A0', 'AGS', 'VSAT']
        fit = MOS_IV_Fit(self.param, targets, 'Step 13-0')
        fit.setDataSource( 0*0.04 * self.IdVd_SW_b0+
                           0.12 * self.IdVd_MW_b0+
                           1.0  * self.IdVd_LW_b0)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)
        return result, err


    def step132(self):
        targets = ['A0', 'KETA', 'DSUB', 'ETA0', 'ETAB']
        fit = MOS_IV_Fit(self.param, targets, 'Step 13-2')
        fit.setDataSource( 0*0.04 * self.IdVg_SW_sat_ba+
                           0.12 * self.IdVg_MW_sat_ba+
                           1.0  * self.IdVg_LW_sat_ba)

        result,err = fit.doFit()
        fit.visualize(result, timeout=0.0)
        self.acceptParam(result, targets)
        return result, err

    def step134(self):
        targets = ['A0', 'AGS', 'VSAT', 'A1', 'A2']
        fit = MOS_IV_Fit(self.param, targets, 'Step 13-4')
        fit.setDataSource( 0*0.05 * self.IdVd_SW_b0+
                           0*0.1 * self.IdVd_MW_b0+
                           0*1.0 * self.IdVd_LW_b0)

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
            if k == 'TEMP':
                s += '*'
            s += '+ %-8s= %-12G\n' % (k, v)
            i += 1

        f = open('pyeda.l', 'w')
        f.write(s)
        f.close() # ????????
        return result, err

param0['TEMP']=25.
param0['TNOM']=25.

proj = MOSp35Proj(param0)
proj.run(71, 71)

