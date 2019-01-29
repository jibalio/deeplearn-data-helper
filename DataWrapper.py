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


class DataWrapper():
    # does not use an iterator
    def __init__(self, X_train, y_train, batch_size):

        self._current_instance_idx = 0
        self.batch_size = 128
        self.data_size = X_train.shape[0]
        self.total_batches = self.data_size // batch_size 
        self.X_train = X_train
        self.y_train = y_train
        
    def fetch_next():
        batch_X =  X_train[self._current_instance_idx:self._current_instance_idx+self.batch_size]
        batch_y = y_train[self._current_instance_idx:self._current_instance_idx+self.batch_size]
        self._current_instance_idx+=self.batch_size
        if self._current_instance_idx>self.data_size:
            self._current_instance_idx=0
        return batch_X, batch_y