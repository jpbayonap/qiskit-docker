
"""
Since the GHZ state requires a general manipulation of 
a photonic beam it is impossible to construct a general
cluster state using the IBM platform. On the other hand,
we can create a simple cluster GHZ state using the QisKit tools
by letting |H>= |0>, |V>=|1>  |a> =|0> and |c>=|1>.
Hence the state to create becomes:

|GHZ> = 1/2 (|000> - |110> + |011> + |101> )  (1)

The following circuit generates the state (1)
"""

import numpy as np
from qiskit import ClassicalRegister, QuantumRegister,QuantumCircuit,execute,Aer
from qiskit.tools.visualization import circuit_drawer,plot_histogram
from numpy import pi



qreg_q = QuantumRegister(3, 'q')
creg_c = ClassicalRegister(3, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[0])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.h(qreg_q[1])
circuit.cx(qreg_q[1], qreg_q[2])
circuit.cx(qreg_q[0], qreg_q[2])
