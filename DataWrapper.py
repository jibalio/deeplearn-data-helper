"""
CUSTOM HELPER FUNCTION TO MAKE BATCH FETCHING EZIER
"""
import itertools
from itertools import cycle, islice
class CycleDataWrapper():
    
    def __init__(self, X_train, y_train, batch_size):
        self.generatorX = cycle(X_train)
        self.generatory = cycle(y_train)
        self.data_size = len(X_train)
        self.remaining = self.data_size
        self.batch_size = batch_size
    
    def get(self):
        if self.remaining-self.batch_size < 0:
            return next(islice(self.generatorX, self.remaining-1, self.remaining)), next(islice(self.generatory, self.remaining-1, self.remaining))
            print("Epoch complete!")
            remaining = self.data_size
        else:
            return next(islice(self.generatorX, self.remaining-1, self.remaining)), next(islice(self.generatory, self.remaining-1, self.remaining))
            
            
          
# usage
# data_train = DataWrapper(X_train, y_train, 256)