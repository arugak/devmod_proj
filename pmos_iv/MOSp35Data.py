from pyEDA.Compact.MOSParamFit import *


class MOSp35Data(MOS_FitProject):
    def __init__(self, param0):
        super(MOSp35Data, self).__init__(param0)

        print 'loading data files...'
        self.loadAuroraFile('../DC-data/aurora_100mv.dat')
        print self.datasets.keys()
        print 'done.'


        # Idvg, short/wide, linear region, zero Vb
        dsrc = MOS_IV_FitData('Idvg, short/wide, linear region, zero Vb')
        ds = self.datasets['p1.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':0.05}, 'Id'))
        self.IdVg_SW_lin_b0 = dsrc
        self.IdVg_SW_lin_b0.curr_min = 5e-8

        # Idvg, mid/wide, linear region, zero Vb
        dsrc = MOS_IV_FitData('Idvg, mid/wide, linear region, zero Vb')
        ds = self.datasets['p2.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':0.05}, 'Id'))
        self.IdVg_MW_lin_b0 = dsrc
        self.IdVg_MW_lin_b0.curr_min = 5e-8

        # Idvg, long/wide, linear region, zero Vb
        dsrc = MOS_IV_FitData('Idvg, long/wide, linear region, zero Vb')
        ds = self.datasets['p3.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':0.05}, 'Id'))
        self.IdVg_LW_lin_b0 = dsrc
        self.IdVg_LW_lin_b0.curr_min = 5e-8

        # Idvg, long/mid, linear region, zero Vb
        dsrc = MOS_IV_FitData('Idvg, long/mid, linear region, zero Vb')
        ds = self.datasets['p4.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':0.05}, 'Id'))
        self.IdVg_LM_lin_b0 = dsrc
        self.IdVg_LM_lin_b0.curr_min = 5e-8

        # Idvg, long/narrow, linear region, zero Vb
        dsrc = MOS_IV_FitData('Idvg, long/narrow, linear region, zero Vb')
        ds = self.datasets['p5.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':0.05}, 'Id'))
        self.IdVg_LN_lin_b0 = dsrc
        self.IdVg_LN_lin_b0.curr_min = 5e-8

        #---
        # IdVg, short/wide, linear region, all Vb
        dsrc = MOS_IV_FitData('IdVg, short/wide, linear region, all Vb')
        ds = self.datasets['p1.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs': 0.0, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-0.5, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.0, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.5, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.0, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.5, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.0, 'Vds': 0.05}, 'Id'))
        self.IdVg_SW_lin_ba = dsrc
        self.IdVg_SW_lin_ba.curr_min = 1e-8

        # IdVg, mid/wide, linear region, all Vb
        dsrc = MOS_IV_FitData('IdVg, mid/wide, linear region, all Vb')
        ds = self.datasets['p2.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs': 0.0, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-0.5, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.0, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.5, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.0, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.5, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.0, 'Vds': 0.05}, 'Id'))
        self.IdVg_MW_lin_ba = dsrc
        self.IdVg_MW_lin_ba.curr_min = 5e-8

        # ---
        # IdVg, long/wide, linear region, all Vb
        dsrc = MOS_IV_FitData('IdVg, long/wide, linear region, all Vb')
        ds = self.datasets['p3.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs': 0.0, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-0.5, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.0, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.5, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.0, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.5, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.0, 'Vds': 0.05}, 'Id'))
        self.IdVg_LW_lin_ba = dsrc
        self.IdVg_LW_lin_ba.curr_min = 5e-8

        # IdVg, long/mid, linear region, all Vb
        dsrc = MOS_IV_FitData('IdVg, long/mid, linear region, all Vb')
        ds = self.datasets['p4.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs': 0.0, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-0.5, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.0, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.5, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.0, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.5, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.0, 'Vds': 0.05}, 'Id'))
        self.IdVg_LM_lin_ba = dsrc
        self.IdVg_LM_lin_ba.curr_min = 5e-8

        # IdVg, long/narrow, linear region, all Vb
        dsrc = MOS_IV_FitData('IdVg, long/narrow, linear region, all Vb')
        ds = self.datasets['p5.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs': 0.0, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-0.5, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.0, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.5, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.0, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.5, 'Vds': 0.05}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.0, 'Vds': 0.05}, 'Id'))
        self.IdVg_LN_lin_ba = dsrc
        self.IdVg_LN_lin_ba.curr_min = 5e-8

        # ---
        # Idvg, short/wide, Vd=all, Vb=-5.0
        dsrc = MOS_IV_FitData('Idvg, short/wide, Vd=all, Vb=-5.0')
        ds = self.datasets['p1.gtr']
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
        ds = self.datasets['p2.gtr']
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
        ds = self.datasets['p3.gtr']
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
        ds = self.datasets['p1.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':5.0}, 'Id'))
        self.IdVg_SW_sat_b0 = dsrc
        self.IdVg_SW_sat_b0.curr_min = 5e-8

        # Idvg, mid/wide, saturation region, zero Vb
        dsrc = MOS_IV_FitData('Idvg, mid/wide, saturation region, zero Vb')
        ds = self.datasets['p2.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':5.0}, 'Id'))
        self.IdVg_MW_sat_b0 = dsrc
        self.IdVg_MW_sat_b0.curr_min = 5e-8

        # Idvg, long/wide, saturation region, zero Vb
        dsrc = MOS_IV_FitData('Idvg, long/wide, saturation region, zero Vb')
        ds = self.datasets['p3.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':5.0}, 'Id'))
        self.IdVg_LW_sat_b0 = dsrc
        self.IdVg_LW_sat_b0.curr_min = 5e-8

        #---
        # IdVg, short/wide, saturation region, all Vb
        dsrc = MOS_IV_FitData('IdVg, short/wide, saturation region, all Vb')
        ds = self.datasets['p1.gtr']
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
        ds = self.datasets['p2.gtr']
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
        ds = self.datasets['p3.gtr']
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
        ds = self.datasets['p1.drr']
        #dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.0}, 'Id'))
        #dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.5}, 'Id'))
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
        ds = self.datasets['p2.drr']
        #dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.0}, 'Id'))
        #dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.5}, 'Id'))
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
        ds = self.datasets['p3.drr']
        #dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.0}, 'Id'))
        #dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.5}, 'Id'))
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
        ds = self.datasets['p4.drr']
        #dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.0}, 'Id'))
        #dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.5}, 'Id'))
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
        ds = self.datasets['p5.drr']
        #dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.0}, 'Id'))
        #dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.5}, 'Id'))
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
        # IdVd, short/wide , zero Vb
        dsrc = MOS_IV_FitData('IdVd, short/wide , all Vb, Vg=2.5')
        ds = self.datasets['p1.drr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs': 0.0,     'Vgs':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':-0.5,     'Vgs':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':-1.0,     'Vgs':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':-1.5,     'Vgs':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':-2.0,     'Vgs':2.5}, 'Id'))
        self.IdVd_SW_g25_ba = dsrc

        # IdVd, mid/wide , zero Vb
        dsrc = MOS_IV_FitData('IdVd, mid/wide , all Vb, Vg=2.5')
        ds = self.datasets['p2.drr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs': 0.0,     'Vgs':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':-0.5,     'Vgs':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':-1.0,     'Vgs':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':-1.5,     'Vgs':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':-2.0,     'Vgs':2.5}, 'Id'))
        self.IdVd_MW_g25_ba = dsrc

        # IdVd, long/wide , zero Vb
        dsrc = MOS_IV_FitData('IdVd, long/wide , all Vb, Vg=2.5')
        ds = self.datasets['p3.drr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs': 0.0,     'Vgs':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':-0.5,     'Vgs':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':-1.0,     'Vgs':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':-1.5,     'Vgs':2.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':-2.0,     'Vgs':2.5}, 'Id'))
        self.IdVd_LW_g25_ba = dsrc
