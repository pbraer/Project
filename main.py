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
PopulationIn2020 = float(144500000)
Year = int(input())
print(PopulationIn2020 + (2020 - Year) * (DeadDaily + EmigratedDaily - BornDaily - NewcomerDaily))
