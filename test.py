from tist import utils

for value in (1, 2, 3, 4):
    print(utils.ti_priority_to_tw(value))

for value in (None, "L", "M", "H"):
    print(utils.tw_priority_to_ti(value))
