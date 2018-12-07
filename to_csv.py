# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 00:38:08 2018

@author: macchini
"""

import numpy as np


markers_clean = [x for x in markers if x is not None]

markers_clean = np.array(markers_clean)

np.savetxt("markers.csv", markers_clean, delimiter=",")