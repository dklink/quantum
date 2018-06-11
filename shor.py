#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 14:47:52 2018

@author: dklink
"""

"""
Code to run shor's algorithm.  Uses Rigetti forest API to simulate the quantum
operations (QFT for example).

This attempts to follow the circuit laid out in https://arxiv.org/pdf/quant-ph/0205095.pdf
"""

import pyquil.quil as pq
from pyquil.gates import H
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
    r1 = [i for i in range(2*q)] #first register
    r2 = [i + len(r1) for i in range(q)] #second register

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

def q_add(a, r2):
    """The quantum addition takes as input a number a, and n  qubits containing
    the quantum Fourier transform of an other number b.
    After, r2 contains the quantum
    Fourier transform of (a + b)mod 2n"""
    A_i = np.array([[1, 0],
                    [0, np.exp(2*np.pi*(a>>a.bit_length))]])
    p = pq.Program().defgate("A_i", A_i)
    p.inst([("A_i", qubit) for qubit in r2])
    
    return p
    
    
def measurement(r1, r2):
    """observes register 1 to collapse the superposition into periodic form"""
    return