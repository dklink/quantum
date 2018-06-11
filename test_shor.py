#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 23:29:32 2018

@author: dklink

Testing modules in shor.py
"""

import shor
import numpy as np

from pyquil.api import QVMConnection

def test_initialization():
    r1 = [0, 1, 2]
    r2 = [3, 4, 5]
    circuit = shor.initialization(r1, r2)
    
    qvm = QVMConnection()
    
    #confirm hadamard transform does expected
    qvm.wavefunction(circuit)[0].real == 1/np.sqrt(2**len(r1))

