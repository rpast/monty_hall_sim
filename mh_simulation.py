import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import array as ar


class Preset:
    '''
    Monty Hall problem simulation class.
    '''

    gates = np.array([[0,0,1],[0,1,0],[1,0,0]])
    
    def __init__(self):
        self.result = None # Current chosen gate
        self.state = Preset.gates[np.random.randint(0,2)]
        
    def __repr__(self):
        return f'***\nCurrent gates state is: {self.state}\nMy current choice is: {self.result}\n'
    
    def choose(self, step=0):
        '''
        Choose between available gates
        :step: 0 = first choice, 1 = second choice
        '''
        self.step = step
        
        # First choice range 0,1,2 p(car) = 0.33%
        if self.step == 0: 
            self.result = self.state[np.random.randint(0,3)]
        
        elif self.step == 1:
            if len(self.state) < 3:
                if self.result == 1:
                    self.result = 0
                elif self.result == 0:
                    self.result = 1
            else:
                print('Gates state has to be updated first!')
                
        else:
            print('Use 0 for first step and 1 for second step!')
                    

    def update_state(self):
        '''
        Remove one goat gate from the state
        '''
        goat_slice = np.where(self.state == 0)
        self.state = np.delete(self.state, goat_slice[0][0], axis=None)


def sim_mh(scenario, n = 1000):
    '''
    Simulate n Monty Hall Trials and return pandas series with p distribution
    :scenario: int 0 = without switch, 1 = with switch
    :n: int
    :return: pd.series
    '''

    outcomes = ar.array('B',[])
    loop = 0

    if scenario == 0:
        name = 'no_switch'
    elif scenario == 1:
        name = 'with_switch'

    while loop < n+1:
        # Set initial state
        sim = Preset()
        # Make first choice
        sim.choose()
        # Reveal empty gate = update gates state
        sim.update_state()

        if scenario == 0:
            outcomes.append(sim.result)
            loop += 1
        elif scenario == 1:
            # Make a new decision basing on update probability distr
            sim.choose(1)
            # Collect results for further analysis
            outcomes.append(sim.result)
            loop += 1

    ## Check P distribution
    p_series = pd.Series(outcomes, name=name)

    p_series = (p_series
                .value_counts(normalize=True)
                .sort_index()
                )

    return p_series

if __name__ == '__main__':
    # Set number of trials
    n = 100_000

    # simulate trials
    no_switch = sim_mh(0, n)
    w_switch = sim_mh(1, n)

    # Construct pd.DataFrame
    mh_df = pd.merge(no_switch, 
                    w_switch, 
                    left_index=True, 
                    right_index=True)

    # Visualise results
    plt.style.use('fivethirtyeight')
    y = np.arange(0.0, 1.1, 0.1)
    title = f'Monty Hall problem P distr n={n} trials'

    fig, ax = plt.subplots()
    mh_plot = mh_df.T.plot(kind='bar',  
            ax=ax, 
            figsize=[12,8],
            title=title,
            yticks=y,
            grid=False,
            )
    mh_plot.set_ylabel('probability')

    plt.savefig('distr_plot.png',
                dpi=150,
                bbox_inches = 'tight')