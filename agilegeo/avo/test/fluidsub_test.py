import unittest
import agilegeo.avo as avo
import numpy as np

class FluidsubTest( unittest.TestCase ):
    """
    Tests fluid sub calculations against Smith et al 2003.
    https://dl.dropboxusercontent.com/u/14965965/Smith_etal_2003.pdf
    """
    
    def test_avseth(self):    # Test is failing

        vp_gas = 2429.0
        vs_gas = 1462.4
        rho_gas = 2080.

        vp_brine = 2850.5
        vs_shale = 1416.1
        rho_shale = 2210.

        # Base case: gas
        # Subbing with: brine

        phi = 0.19           # Don't know this... just guessing...
        rhof1 = 250.         # gas
        rhof2 = 1040.        # brine
        kmin = 9000000000.   # Don't know this... just guessing...
        kf1 = 207000000.     # gas
        kf2 = 50000000000.   # brine

        self.assertAlmostEqual( avo.avseth_fluidsub(vp=vp_gas, vs=vs_gas, rho=rho_gas, phi=phi, rhof1=rhof1, rhof2=rhof2, kmin=kmin, kf1=kf1, kf2=kf2)[0], vp_brine,  places=0 )        
        self.assertAlmostEqual( avo.avseth_fluidsub(vp=vp_gas, vs=vs_gas, rho=rho_gas, phi=phi, rhof1=rhof1, rhof2=rhof2, kmin=kmin, kf1=kf1, kf2=kf2)[1], vs_brine,  places=0 )        
        self.assertAlmostEqual( avo.avseth_fluidsub(vp=vp_gas, vs=vs_gas, rho=rho_gas, phi=phi, rhof1=rhof1, rhof2=rhof2, kmin=kmin, kf1=kf1, kf2=kf2)[2], rho_brine, places=0 )        

    def test_smith(self):

        # Base case: gas
        # Subbing with: brine


        # INPUTS

        vp_gas = 2429.0
        vs_gas = 1462.4
        rho_gas = 2080.      # RHOB for rock in brine case

        phi = 0.30           # Don't know this... just guessing
        rhohc = 250.         # gas
        rhow = 1040.         # brine
        sw = 0.3             # Don't know this... just guessing
        swnew = 0.           # Don't know this... seems likely
        khc = 207000000.     # gas
        kw = 2950000000.     # brine
        kclay = 25000000000.
        kqtz = 37000000000.  
        vclay = 0.0


        # EXPECTED OUTPUT

        vp_brine = 2850.5
        vs_brine = 1416.1
        rho_brine = 2210.    # RHOB for rock in brine case

        self.assertAlmostEqual( avo.smith_fluidsub(vp=vp_gas, vs=vs_gas, rho=rho_gas, phi=phi, rhohc=rhohc, rhow=rhow, sw=sw, swnew=swnew, khc=khc, kw=kw, kclay=kclay, kqtz=kqtz, vclay=vclay)[0], vp_brine,  places=0 )        
        self.assertAlmostEqual( avo.smith_fluidsub(vp=vp_gas, vs=vs_gas, rho=rho_gas, phi=phi, rhohc=rhohc, rhow=rhow, sw=sw, swnew=swnew, khc=khc, kw=kw, kclay=kclay, kqtz=kqtz, vclay=vclay)[1], vs_brine,  places=0 )        
        self.assertAlmostEqual( avo.smith_fluidsub(vp=vp_gas, vs=vs_gas, rho=rho_gas, phi=phi, rhohc=rhohc, rhow=rhow, sw=sw, swnew=swnew, khc=khc, kw=kw, kclay=kclay, kqtz=kqtz, vclay=vclay)[2], rho_brine, places=0 )        
        
if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(ModuliTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
