"""
Test DataAdapter interface.
"""
import os, unittest
import opensim as osim

test_dir = os.path.join(os.path.dirname(os.path.abspath(osim.__file__)),
                        'tests')

class TestDataAdapter(unittest.TestCase):
    def test_TRCFileAdapter(self):
        adapter = osim.TRCFileAdapter()
        table = adapter.read(os.path.join(test_dir, 
                             'futureOrientationInverseKinematics.trc'))
        assert table.getNumRows()    == 1202
        assert table.getNumColumns() == 2

        table = adapter.read(os.path.join(test_dir, 'TRCFileWithNANs.trc'))
        assert table.getNumRows()    == 5
        assert table.getNumColumns() == 14

    def test_STOFileAdapter(self):
        adapter = osim.STOFileAdapter()
        table = adapter.read(os.path.join(test_dir, 'subject02_grf_HiFreq.mot'))
        assert table.getNumRows()    == 439
        assert table.getNumColumns() == 18

        table = adapter.read(os.path.join(test_dir, 
                                          'std_subject01_walk1_ik.mot'))
        assert table.getNumRows()    == 73
        assert table.getNumColumns() == 23

    def test_C3DFileAdapter(self):
        try:
            adapter = osim.C3DFileAdapter()
        except AttributeError:
            # C3D support not available. OpenSim was not compiled with BTK.
            return
        tables = adapter.read(os.path.join(test_dir, 'walking2.c3d'))
        markers = tables['markers']
        forces = tables['forces']
        
        assert markers.getNumRows()    == 1249
        assert markers.getNumColumns() == 44
        assert forces.getNumRows()     == 9992
        assert forces.getNumColumns()  == 6

        tables = adapter.read(os.path.join(test_dir, 'walking5.c3d'))
        markers = tables['markers']
        forces = tables['forces']
        assert markers.getNumRows()    == 1103
        assert markers.getNumColumns() == 40
        assert forces.getNumRows()     == 8824
        assert forces.getNumColumns()  == 6
