#!# This example shows the computation of the DC bias and sensitivity in a voltage divider.

####################################################################################################

import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()

####################################################################################################

from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

####################################################################################################

#cm# voltage-divider.m4

circuit = Circuit('Voltage Divider')

circuit.V('input', 'in', circuit.gnd, u_V(10))
circuit.R(1, 'in', 'out', u_kΩ(9))
circuit.R(2, 'out', circuit.gnd, u_kΩ(1))

####################################################################################################

simulator = circuit.simulator(temperature=25, nominal_temperature=25)

analysis = simulator.operating_point()
for node in (analysis['in'], analysis.out): # .in is invalid !
    print('Node {}: {} V'.format(str(node), float(node)))
#o#

analysis = simulator.dc_sensitivity('v(out)')
for element in analysis.elements.values():
    print(element, float(element))
#o#
