
from floris.tools.floris_interface import FlorisInterface


def calculate_wake(input_dict):
    fi = FlorisInterface(input_dict=input_dict)
    fi.calculate_wake()
    turbines = fi.floris.farm.turbines

    cts = [t.Ct for t in turbines]
    powers = [t.power for t in turbines]
    ave_vels = [t.average_velocity for t in turbines]
    ais = [t.aI for t in turbines]

    return cts, powers, ave_vels, ais
