#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 14:47:52 2018

@author: dklink
"""

"""
Code to run shor's algorithm.  Uses Rigetti forest API to simulate the quantum
operations (QFT for example).
"""

import pyquil.quil as pq
from pyquil.gates import H
import math
import fourier
import numpy as np

def factor():
    """uses shor's algorithm to find the prime factors of x"""
    x = 21 #hardcoded for now
    
    #step 0: do a bit of preprocessing to set up registers
    n = x.bit_length() #5
    s = 0
    while (2**s < n**2):
        s += 1
    q = 2**s #n^2 <= q <= 2n^2, and q = 2^s (in this case, s=4)
             #this is the number of qubits in the first/second registers
    r1 = [i for i in range(q)] #first register
    r2 = [i + q for i in range(q)] #second register

    circuit = pq.Program()
    #step 1: initialize first register
    circuit += initialization(r1, r2)
    
    #step 2: computation of x^a in second register 
    circuit += computation(r1, r2)
    
    #step 3: Fourier Transform
    circuit += fourier.qft(r1, r2)
    
    #step 4: Observation
    circuit += measurement(r1, r2)
    
    #step 5: Post-processing
    #a bit of classical work to extract the factor
    
    return

def initialization(r1, r2):
    """program to initialize qubits"""
    return pq.Program().inst([H(qubit) for qubit in r1])

def computation(r1, r2):
    """computes the modular exponentiation from the first register onto the second register"""
    return
    
def measurement(r1, r2):
    """observes register 1 to collapse the superposition into periodic form"""
    return