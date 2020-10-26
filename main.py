import math
# Statistics for 2019
Dead = float(1800700)
Born = float(1461000)
Emigrated = float(10000000)
Newcomer = float(12000000)
# Daily
DeadDaily = Dead / 365
BornDaily = Born / 365
EmigratedDaily = Emigrated / 365
NewcomerDaily = Newcomer / 365
# Calculation
PopulationIn2015 = float(146300000)
Year = int(input())
print(round(PopulationIn2015 + (2015 - Year) * (DeadDaily + EmigratedDaily - BornDaily - NewcomerDaily)))
