#!/usr/bin/env python

import unittest
import os
import sys
import subprocess
import glob

TOPDIR = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))

class Tests(unittest.TestCase):
    def run_modeller_script(self, script_dir, script_name, model_name, resrng):
        """Run a Modeller script and test the output model"""
        os.chdir(os.path.join(TOPDIR, 'scripts', 'MODELLER', script_dir))
        # Run script
        p = subprocess.check_call(["python", script_name, "--test"])
        # Make sure PDB was produced with the requested residue range
        with open('%s.B99990001.pdb' % model_name) as fh:
            pdb_lines = [x for x in fh.readlines() if x.startswith('ATOM')]
        rng = (int(pdb_lines[0][22:26]), int(pdb_lines[-1][22:26]))
        self.assertEqual(rng, resrng)

    def test_npr2_1(self):
        """Test generation of Npr2 model, first domain"""
        self.run_modeller_script('Npr2', 'all_sjkim_final1.py',
                                 'Npr2', (9, 127))

    def test_npr2_2(self):
        """Test generation of Npr2 model, second domain"""
        self.run_modeller_script('Npr2', 'all_sjkim_final2.py',
                                 'Npr2', (257, 327))

    def test_npr2_3(self):
        """Test generation of Npr2 model, third domain"""
        self.run_modeller_script('Npr2', 'all_sjkim_final3.py',
                                 'Npr2', (563, 610))

    def test_npr3_1(self):
        """Test generation of Npr3 model, first domain"""
        self.run_modeller_script('Npr3', 'all_sjkim_final1.py',
                                 'Npr3', (322, 438))

    def test_npr3_2(self):
        """Test generation of Npr3 model, second domain"""
        self.run_modeller_script('Npr3', 'all_sjkim_final2.py',
                                 'Npr3', (531, 577))

    def test_npr3_3(self):
        """Test generation of Npr3 model, third domain"""
        self.run_modeller_script('Npr3', 'all_sjkim_final3.py',
                                 'Npr3', (1, 31))

    def test_npr3_4(self):
        """Test generation of Npr3 model, fourth domain"""
        self.run_modeller_script('Npr3', 'all_sjkim_final4.py',
                                 'Npr3', (950, 988))

    def test_npr3_5(self):
        """Test generation of Npr3 model, fifth domain"""
        self.run_modeller_script('Npr3', 'all_sjkim_final5.py',
                                 'Npr3', (1083, 1140))

    def test_sea1_1(self):
        """Test generation of SEA1 model, first domain"""
        self.run_modeller_script('SEA1', 'all_sjkim_final1.py',
                                 'SEA1', (101, 275))

    def test_sea1_2(self):
        """Test generation of SEA1 model, second domain"""
        self.run_modeller_script('SEA1', 'all_sjkim_final2.py',
                                 'SEA1', (279, 473))

    def test_sea1_3(self):
        """Test generation of SEA1 model, third domain"""
        self.run_modeller_script('SEA1', 'all_sjkim_final3.py',
                                 'SEA1', (1178, 1273))

    def test_sea2_1(self):
        """Test generation of SEA2 model, first domain"""
        self.run_modeller_script('SEA2', 'all_sjkim_final1.py',
                                 'SEA2', (127, 520))

    def test_sea2_2(self):
        """Test generation of SEA2 model, second domain"""
        self.run_modeller_script('SEA2', 'all_sjkim_final2.py',
                                 'SEA2', (1280, 1341))

    def test_sea3_1(self):
        """Test generation of SEA3 model, first domain"""
        self.run_modeller_script('SEA3', 'all_sjkim_final1.py',
                                 'SEA3', (54, 424))

    def test_sea3_2(self):
        """Test generation of SEA3 model, second domain"""
        self.run_modeller_script('SEA3', 'all_sjkim_final2.py',
                                 'SEA3', (430, 536))

    def test_sea3_3(self):
        """Test generation of SEA3 model, third domain"""
        self.run_modeller_script('SEA3', 'all_sjkim_final3.py',
                                 'SEA3', (1092, 1139))

    def test_sea4_1(self):
        """Test generation of SEA4 model, first domain"""
        self.run_modeller_script('SEA4', 'all_sjkim_final1.py',
                                 'SEA4', (45, 426))

    def test_sea4_2(self):
        """Test generation of SEA4 model, second domain"""
        self.run_modeller_script('SEA4', 'all_sjkim_final2.py',
                                 'SEA4', (659, 835))

    def test_sea4_3(self):
        """Test generation of SEA4 model, third domain"""
        self.run_modeller_script('SEA4', 'all_sjkim_final3.py',
                                 'SEA4', (942, 1032))

if __name__ == '__main__':
    unittest.main()
