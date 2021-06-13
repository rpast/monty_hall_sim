import mh_lib
import numpy as np
import pandas as pd
import array as ar

############################################
## Simulate n trials with decision switch ##
p_change = ar.array('B',[])
n = 100_000

for _ in range(0, n):
    # Set initial state
    sim = mh_lib.Preset()
    # Make first choice
    sim.choose()
    # Reveal empty gate = update gates state
    sim.update_state()
    # Make a new decision basing on update probability distr
    sim.choose(1)
    # Collect results for further analysis
    p_change.append(sim.result)

## Check P distribution
p_change_series = pd.Series(p_change)
print("MH simulation - path with decision switch")
print(p_change_series.value_counts(normalize = True),"\n")


###############################################
## Simulate n trials without decision switch ##
p_no_change = ar.array('B',[])
n = 100_000

for _ in range(0, n):
    # Set initial state
    sim = mh_lib.Preset()
    # Make first choice
    sim.choose()
    # Reveal empty gate = update gates state
    sim.update_state()
    
    p_no_change.append(sim.result)

## Check P distribution
p_no_change_series = pd.Series(p_no_change)
print("MH simulation - path wo decision switch")
print(p_no_change_series.value_counts(normalize=True))