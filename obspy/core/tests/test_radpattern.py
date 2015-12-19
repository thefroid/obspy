# -*- coding: utf-8 -*-
"""
The obspy.imaging.radiation_pattern test suite.
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import *  # NOQA

import unittest

import matplotlib.pyplot as plt
from obspy.core.event import plot_3drpattern
from mpl_toolkits.mplot3d import Axes3D


class RadPatternTestCase(unittest.TestCase):
    """
    Test cases for radiation_pattern.
    """

    def test_farfield(self):
        """
        Tests to plot P/S wave farfield radiation pattern
        """
        mt = [0.91, -0.89, -0.02, 1.78, -1.55, 0.47]
        #mt = [0.0, 1, -1, 0, -1, 0.]
        plot_3drpattern(mt,kind='vtk')

def suite():
    return unittest.makeSuite(RadPatternTestCase, 'test')

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
