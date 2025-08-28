### Computational Guided Inquiry for Modeling Earth's Climate (Neshyba, 2025)
#
# Cambio Comparisons
# This code takes as input a user-generated emission scenario and runs four versions of Cambio:
#
# - Cambio 1.0 has the five basic equations of motion, with $CO_2$ fertilization but no other feedbacks
# - Cambio 2.0 adds in Henry's Law feedbacks
# - Cambio 3.0 adds in ice-albedo feedback
# - Cambio 4.0 adds in terrestrial sequestion feedback that reduces $CO_2$ fertilization
#
# The code then runs the four simulations, and compares the output of a selected two of them.

import numpy as np
import matplotlib.pyplot as plt
import meclib.cl as cl

# Loading an emission scenario
filename = "Peaks_in_2040.pkl"
time, eps, epsdictionary_from_file = cl.LoadMyScenario(filename, verbose=True)


# Creating climate parameters consistent with this emission scenario
ClimateParams = cl.CreateClimateParams(epsdictionary_from_file)

# Running Cambio
CS_Cambio1_list = cl.run_Cambio(
    cl.PropagateClimateState_Cambio1, ClimateParams, time, eps
)
CS_Cambio2_list = cl.run_Cambio(
    cl.PropagateClimateState_Cambio2, ClimateParams, time, eps
)
CS_Cambio3_list = cl.run_Cambio(
    cl.PropagateClimateState_Cambio3, ClimateParams, time, eps
)
CS_Cambio4_list = cl.run_Cambio(
    cl.PropagateClimateState_Cambio4, ClimateParams, time, eps
)

# Reporting the starting and ending state of the Cambio1.0 run
print("Starting state:")
print(CS_Cambio1_list[0])
print("Ending state:")
print(CS_Cambio1_list[-1])

# Decide on what graphics we want
items_to_plot = [
    ["C_atm", "C_ocean"],
    ["F_ha", "F_ocean_net", "F_land_net"],
    "T_anomaly",
    "OceanSurfacepH",
]

# Graph results from a single run 
cl.CS_list_plots(CS_Cambio1_list, "Cambio1.0", items_to_plot)

# Graph comparisons between two runs
cl.CS_list_compare(
    [CS_Cambio1_list, CS_Cambio4_list],
    ["Cambio1.0", "Cambio4.0"],
    items_to_plot,
)
