# Cluster identifiers deemed to be equivalent.

The `clustering` module implements the [union-find](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) data structure
which can be used to cluster together equivalent items. These items are often identifiers that reference real-world
entities in some domain.

## Usage

```
$ # source a virtual environment (example uses [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/))
$ workon clustering
(clustering) $ # install clustering module
(clustering) $ pip install -e git+https://github.com/christiemj09/clustering.git@b0da608fa2482e1828dcfa09ce7cff6362b751e4#egg=clustering
(clustering) $ python
Python 3.6.5
...
>>> from clustering import UnionFind
>>> items = [1, 2, 3]
>>> uf = UnionFind(items)
>>> uf.union(1, 2)
>>> uf.find(1)
2
>>> uf.find(2)
2
>>> uf.find(3)
3
```

## Example

To run some example code demonstrating how to use this module in a more applied setting, clone this repository and run the script `clustering-demo`
from the repository root. Example files are contained in the `example` directory.
