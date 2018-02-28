from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import *
import random
import numpy as np


def bell_p(a,b):
	p = Program()
	p.inst(H(a))
	p.inst(CNOT(a,b))
	return p

def simulation(qvm):
	a,b = random.sample(range(10), 2)
	assert a != b
	p = bell_p(a,b)
	wave = qvm.wavefunction(p)
	p.measure(a, a)
	p.measure(b, b)

	result = qvm.run(p, range(1 + max(a, b)))
	
	print("a: %s, b: %s"%(a, b))
	print("wave: ", wave)
	print("result: ", result)

if __name__ == '__main__':
	qvm = QVMConnection()
	for _ in range(10):
		simulation(qvm)
