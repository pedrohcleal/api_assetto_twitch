from pyaccsharedmemory import accSharedMemory
from pprint import pprint

asm = accSharedMemory()
sm = asm.read_shared_memory()

pprint(sm)
# if sm is not None:
#     print(f"Fuel: {sm.Physics.fuel}")
#     print(f"RPM: {sm.Physics.rpm}")
#     print(f"Speed (km/h): {sm.Physics.speed_kmh}")

asm.close()