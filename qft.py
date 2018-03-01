from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import *

from math import pi
import random
import numpy as np


def qft(program, qubits):
	assert len(qubits) == len(set(qubits)) # make sure qubits are all distinct
	count, l = 0, len(qubits)

	while count < l:
		program.inst(H(count))
		temp = count + 1
		denom = 2
		while temp < l:
			program.inst(CPHASE(pi/denom, temp, count))
			temp += 1
			denom *= 2
		count += 1

	start, end = 0, l-1
	while start < end:
		program.inst(SWAP(qubits[start], qubits[end]))
		start += 1
		end -= 1

def simulation(qvm):
	p = Program()
	p.inst(I(0), H(1), I(2))
	wave = qvm.wavefunction(p)
	print("Before QFT : ", wave)


	qft(p, [0,1,2])
	wave = qvm.wavefunction(p)
	print("After QFT : ", wave)


if __name__ == '__main__':
	qvm = QVMConnection()
	for _ in range(1):
		simulation(qvm)
