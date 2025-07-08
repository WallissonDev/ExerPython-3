MAX_WEIGHT = 0
MINOR_WEIGHT = 0
for i in range(1,6):
    WEIGHT = float(input(f'Write the {i} people Weight: '))
    if i == 1:
        MAX_WEIGHT = WEIGHT
        MINOR_WEIGHT = WEIGHT
    else:
        if WEIGHT > MAX_WEIGHT:
            MAX_WEIGHT = WEIGHT
        if WEIGHT < MINOR_WEIGHT:
            MINOR_WEIGHT = WEIGHT
print(f'The Less Weight is {MINOR_WEIGHT}')
print(f'The Bigger Weight is {MAX_WEIGHT}')
