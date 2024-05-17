import numpy as np
from qiskit import ClassicalRegister, QuantumRegister,QuantumCircuit,execute,Aer
from qiskit.tools.visualization import circuit_drawer,plot_histogram
from numpy import pi


qreg_q = QuantumRegister(3, 'q')
creg_c = ClassicalRegister(3, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.x(qreg_q[0])
circuit.u(-0.615, 0, 0, qreg_q[1])
circuit.u(-pi/4, 0, 0, qreg_q[2])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.u(0.615, 0, 0, qreg_q[1])
circuit.cx(qreg_q[1], qreg_q[0])
circuit.cx(qreg_q[1], qreg_q[2])
circuit.u(pi/4, 0, 0, qreg_q[2])
circuit.cx(qreg_q[2], qreg_q[1])

