from collections import namedtuple

Tensor = namedtuple('Tensor', field_names=['value', 'shape', 'dtype', 'argname'])
Script = namedtuple('Script', field_names=['script', 'device', 'tag'])
Model = namedtuple('Model', field_names=['data', 'device', 'backend', 'tag'])
