
from floris.tools.floris_interface import FlorisInterface
import time

def calculate_wake(input_dict):
    fi = FlorisInterface(input_dict=input_dict)

    start = time.perf_counter()
    fi.calculate_wake()
    end = time.perf_counter()

    computation_time = end - start

    return computation_time
