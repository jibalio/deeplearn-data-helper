## Custom Helper Classes for Deep Learning

### class DataWrapper:

A class that wraps the training set into a circular generator.

**Usage**: `DataWrapper(feature_space, labels, batch_size)`

- `feature_space`: the features of the dataset to be wrapped.
- `labels`: the labels of the respective features (may or may not be one-hot encoded)
- `batch_size`: the batch size

```python
from DataWrapper import DataWrapper
data_train = DataWrapper(X_train, y_train, 256)
```

