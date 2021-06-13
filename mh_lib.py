import numpy as np
import pandas as pd
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