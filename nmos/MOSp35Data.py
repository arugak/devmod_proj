from pyEDA.Compact.AuroraData import *
from pyEDA.Compact.MOSParamFit import *


class MOSp35Data(MOS_FitProject):
    def __init__(self, param0):
        super(MOSp35Data, self).__init__(param0)

        print 'loading data files...'
        self.loadAuroraFile('../DC-data/aurora_100mv.dat')
        #self.loadAuroraFile('../DC-data/aurora_1mv_avg.dat')
        print self.datasets.keys()
        print 'done.'


        # Idvg, short/wide, linear region, zero Vb
        dsrc = MOS_IV_FitData('Idvg, short/wide, linear region, zero Vb')
        ds = self.datasets['n1.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':0.05}, 'Id'))
        self.IdVg_SW_lin_b0 = dsrc
        self.IdVg_SW_lin_b0.curr_min = 5e-8

        # Idvg, mid/wide, linear region, zero Vb
        dsrc = MOS_IV_FitData('Idvg, mid/wide, linear region, zero Vb')
        ds = self.datasets['n2.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':0.05}, 'Id'))
        self.IdVg_MW_lin_b0 = dsrc
        self.IdVg_MW_lin_b0.curr_min = 5e-8

        # Idvg, long/wide, linear region, zero Vb
        dsrc = MOS_IV_FitData('Idvg, long/wide, linear region, zero Vb')
        ds = self.datasets['n3.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':0.05}, 'Id'))
        self.IdVg_LW_lin_b0 = dsrc
        self.IdVg_LW_lin_b0.curr_min = 5e-8

        # Idvg, long/mid, linear region, zero Vb
        dsrc = MOS_IV_FitData('Idvg, long/mid, linear region, zero Vb')
        ds = self.datasets['n4.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':0.05}, 'Id'))
        self.IdVg_LM_lin_b0 = dsrc
        self.IdVg_LM_lin_b0.curr_min = 5e-8

        # Idvg, long/narrow, linear region, zero Vb
        dsrc = MOS_IV_FitData('Idvg, long/narrow, linear region, zero Vb')
        ds = self.datasets['n5.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':0.05}, 'Id'))
        self.IdVg_LN_lin_b0 = dsrc
        self.IdVg_LN_lin_b0.curr_min = 5e-8

        #---
        # IdVg, short/wide, linear region, all Vb
        dsrc = MOS_IV_FitData('IdVg, short/wide, linear region, all Vb')
        ds = self.datasets['n1.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs': 0.0, 'Vds': 0.05}, 'Id'), wMult=1.00)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-0.5, 'Vds': 0.05}, 'Id'), wMult=1.03)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.0, 'Vds': 0.05}, 'Id'), wMult=1.06)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.5, 'Vds': 0.05}, 'Id'), wMult=1.09)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.0, 'Vds': 0.05}, 'Id'), wMult=1.11)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.5, 'Vds': 0.05}, 'Id'), wMult=1.11)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.0, 'Vds': 0.05}, 'Id'), wMult=1.13)
        self.IdVg_SW_lin_ba = dsrc
        self.IdVg_SW_lin_ba.curr_min = 1e-8

        # IdVg, mid/wide, linear region, all Vb
        dsrc = MOS_IV_FitData('IdVg, mid/wide, linear region, all Vb')
        ds = self.datasets['n2.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs': 0.0, 'Vds': 0.05}, 'Id'), wMult=1.00)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-0.5, 'Vds': 0.05}, 'Id'), wMult=1.05)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.0, 'Vds': 0.05}, 'Id'), wMult=1.10)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.5, 'Vds': 0.05}, 'Id'), wMult=1.14)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.0, 'Vds': 0.05}, 'Id'), wMult=1.18)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.5, 'Vds': 0.05}, 'Id'), wMult=1.20)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.0, 'Vds': 0.05}, 'Id'), wMult=1.24)
        self.IdVg_MW_lin_ba = dsrc
        self.IdVg_MW_lin_ba.curr_min = 5e-8

        # ---
        # IdVg, long/wide, linear region, all Vb
        dsrc = MOS_IV_FitData('IdVg, long/wide, linear region, all Vb')
        ds = self.datasets['n3.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs': 0.0, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-0.5, 'Vds': 0.05}, 'Id'), wMult=1.06)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.0, 'Vds': 0.05}, 'Id'), wMult=1.12)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.5, 'Vds': 0.05}, 'Id'), wMult=1.17)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.0, 'Vds': 0.05}, 'Id'), wMult=1.22)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.5, 'Vds': 0.05}, 'Id'), wMult=1.25)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.0, 'Vds': 0.05}, 'Id'), wMult=1.30)
        self.IdVg_LW_lin_ba = dsrc
        self.IdVg_LW_lin_ba.curr_min = 5e-8

        # IdVg, long/mid, linear region, all Vb
        dsrc = MOS_IV_FitData('IdVg, long/mid, linear region, all Vb')
        ds = self.datasets['n4.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs': 0.0, 'Vds': 0.05}, 'Id'), wMult=1.00)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-0.5, 'Vds': 0.05}, 'Id'), wMult=1.07)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.0, 'Vds': 0.05}, 'Id'), wMult=1.13)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.5, 'Vds': 0.05}, 'Id'), wMult=1.19)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.0, 'Vds': 0.05}, 'Id'), wMult=1.25)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.5, 'Vds': 0.05}, 'Id'), wMult=1.28)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.0, 'Vds': 0.05}, 'Id'), wMult=1.33)
        self.IdVg_LM_lin_ba = dsrc
        self.IdVg_LM_lin_ba.curr_min = 5e-8

        # IdVg, long/narrow, linear region, all Vb
        dsrc = MOS_IV_FitData('IdVg, long/narrow, linear region, all Vb')
        ds = self.datasets['n5.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs': 0.0, 'Vds': 0.05}, 'Id'), wMult=1.00)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-0.5, 'Vds': 0.05}, 'Id'), wMult=1.07)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.0, 'Vds': 0.05}, 'Id'), wMult=1.14)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.5, 'Vds': 0.05}, 'Id'), wMult=1.20)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.0, 'Vds': 0.05}, 'Id'), wMult=1.27)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.5, 'Vds': 0.05}, 'Id'), wMult=1.30)
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.0, 'Vds': 0.05}, 'Id'), wMult=1.36)
        self.IdVg_LN_lin_ba = dsrc
        self.IdVg_LN_lin_ba.curr_min = 5e-8

        # ---
        # Idvg, short/wide, Vd=all, Vb=-5.0
        dsrc = MOS_IV_FitData('Idvg, short/wide, Vd=all, Vb=-5.0')
        ds = self.datasets['n1.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':0.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':0.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':1.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':2.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':3.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':3.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':4.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':4.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':5.0}, 'Id'))
        self.IdVg_SW_da_b5 = dsrc
        self.IdVg_SW_da_b5.curr_min = 5e-8

        # Idvg, mid/wide, Vd=all, Vb=-3.0
        dsrc = MOS_IV_FitData('Idvg, mid/wide, Vd=all, Vb=-5.0')
        ds = self.datasets['n2.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':0.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':0.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':1.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':2.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':3.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':3.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':4.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':4.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':5.0}, 'Id'))
        self.IdVg_MW_da_b5 = dsrc
        self.IdVg_MW_da_b5.curr_min = 5e-8

        # Idvg, long/wide, Vd=all, Vb=-3.0
        dsrc = MOS_IV_FitData('Idvg, long/wide, Vd=all, Vb=-5.0')
        ds = self.datasets['n3.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':0.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':0.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':1.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':2.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':3.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':3.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':4.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':4.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-5.,    'Vds':5.0}, 'Id'))
        self.IdVg_LW_da_b5 = dsrc
        self.IdVg_LW_da_b5.curr_min = 5e-8

        # ---
        # Idvg, short/wide, saturation region, zero Vb
        dsrc = MOS_IV_FitData('Idvg, short/wide, saturation region, zero Vb')
        ds = self.datasets['n1.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':5.0}, 'Id'))
        self.IdVg_SW_sat_b0 = dsrc
        self.IdVg_SW_sat_b0.curr_min = 5e-8

        # Idvg, mid/wide, saturation region, zero Vb
        dsrc = MOS_IV_FitData('Idvg, mid/wide, saturation region, zero Vb')
        ds = self.datasets['n2.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':5.0}, 'Id'))
        self.IdVg_MW_sat_b0 = dsrc
        self.IdVg_MW_sat_b0.curr_min = 5e-8

        # Idvg, long/wide, saturation region, zero Vb
        dsrc = MOS_IV_FitData('Idvg, long/wide, saturation region, zero Vb')
        ds = self.datasets['n3.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':5.0}, 'Id'))
        self.IdVg_LW_sat_b0 = dsrc
        self.IdVg_LW_sat_b0.curr_min = 5e-8

        # ---


        '''
        #---
        # IdVg, long/wide , Vd=1, all Vb
        dsrc = MOS_IV_FitData('IdVg, long/wide , Vd=1, all Vb')
        ds = self.datasets['n15x15.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,     'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.1,   'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.2,   'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.3,   'Vds':1.0}, 'Id'))
        self.IdVg_LW_d1_ba = dsrc

        # IdVg, mid/wide, Vd=1, all Vb
        dsrc = MOS_IV_FitData('IdVg, mid/wide, Vd=1, all Vb')
        ds = self.datasets['n15x1p8.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,     'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.1,   'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.2,   'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.3,   'Vds':1.0}, 'Id'))
        self.IdVg_MW_d1_ba = dsrc

        # IdVg, short/wide, Vd=1, all Vb
        dsrc = MOS_IV_FitData('IdVg, short/wide, Vd=1, all Vb')
        ds = self.datasets['n15x0p6.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,     'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.1,   'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.2,   'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.3,   'Vds':1.0}, 'Id'))
        self.IdVg_SW_d1_ba = dsrc

        '''
        #---
        # IdVg, short/wide, saturation region, all Vb
        dsrc = MOS_IV_FitData('IdVg, short/wide, saturation region, all Vb')
        ds = self.datasets['n1.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs': 0.,    'Vds':5.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-0.5,   'Vds':5.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.0,   'Vds':5.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.5,   'Vds':5.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.0,   'Vds':5.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.5,   'Vds':5.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.0,   'Vds':5.0}, 'Id'))
        self.IdVg_SW_sat_ba = dsrc
        self.IdVg_SW_sat_ba.curr_min = 5e-8

        # IdVg, mid/wide, saturation region, all Vb
        dsrc = MOS_IV_FitData('IdVg, mid/wide, saturation region, all Vb')
        ds = self.datasets['n2.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs': 0.,    'Vds':5.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-0.5,   'Vds':5.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.0,   'Vds':5.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.5,   'Vds':5.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.0,   'Vds':5.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.5,   'Vds':5.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.0,   'Vds':5.0}, 'Id'))
        self.IdVg_MW_sat_ba = dsrc
        self.IdVg_MW_sat_ba.curr_min = 5e-8

        # IdVg, long/wide , saturation region, all Vb
        dsrc = MOS_IV_FitData('IdVg, long/wide , saturation region, all Vb')
        ds = self.datasets['n3.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs': 0.,    'Vds':5.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-0.5,   'Vds':5.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.0,   'Vds':5.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.5,   'Vds':5.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.0,   'Vds':5.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.5,   'Vds':5.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.0,   'Vds':5.0}, 'Id'))
        self.IdVg_LW_sat_ba = dsrc
        self.IdVg_LW_sat_ba.curr_min = 5e-8

        #---
        # IdVd, short/wide , zero Vb
        dsrc = MOS_IV_FitData('IdVd, short/wide , zero Vb')
        ds = self.datasets['n1.drr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':1.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':2.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':3.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':3.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':4.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':4.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':5.0}, 'Id'))
        self.IdVd_SW_b0 = dsrc

        # IdVd, mid/wide , zero Vb
        dsrc = MOS_IV_FitData('IdVd, mid/wide , zero Vb')
        ds = self.datasets['n2.drr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':1.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':2.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':3.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':3.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':4.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':4.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':5.0}, 'Id'))
        self.IdVd_MW_b0 = dsrc

        # IdVd, long/wide , zero Vb
        dsrc = MOS_IV_FitData('IdVd, long/wide , zero Vb')
        ds = self.datasets['n3.drr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':1.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':2.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':3.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':3.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':4.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':4.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':5.0}, 'Id'))
        self.IdVd_LW_b0 = dsrc

        # IdVd, long/mid, zero Vb
        dsrc = MOS_IV_FitData('IdVd, long/mid, zero Vb')
        ds = self.datasets['n4.drr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':1.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':2.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':3.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':3.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':4.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':4.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':5.0}, 'Id'))
        self.IdVd_LM_b0 = dsrc

        # IdVd, long/narrow, zero Vb
        dsrc = MOS_IV_FitData('IdVd, long/narrow, zero Vb')
        ds = self.datasets['n5.drr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':1.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':2.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':3.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':3.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':4.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':4.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':5.0}, 'Id'))
        self.IdVd_LN_b0 = dsrc

        #---
        # IdVd, short/wide , Vgs=5.0V, Vbs=0.0V
        dsrc = MOS_IV_FitData('IdVd, short/wide , Vgs=5.0V, Vbs=0.0V')
        ds = self.datasets['n1.drr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':5.0}, 'Id'))
        self.IdVd_SW_d5_b0 = dsrc

        # IdVd, mid/wide , Vgs=5.0V, Vbs=0.0V
        dsrc = MOS_IV_FitData('IdVd, mid/wide , Vgs=5.0V, Vbs=0.0V')
        ds = self.datasets['n2.drr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':5.0}, 'Id'))
        self.IdVd_MW_d5_b0 = dsrc

        # IdVd, long/wide , Vgs=5.0V, Vbs=0.0V
        dsrc = MOS_IV_FitData('IdVd, long/wide , Vgs=5.0V, Vbs=0.0V')
        ds = self.datasets['n3.drr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':5.0}, 'Id'))
        self.IdVd_LW_d5_b0 = dsrc
