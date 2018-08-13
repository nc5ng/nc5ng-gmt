"""
Meta Types are used for behind the scenes constructor magic.

Including the cheese-ball caching database behind ``DataPoint``

``DataPointType`` Metaclass
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: nc5ng.types.meta.DataPointType
  :members:

FileBacked Metaclasses
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: nc5ng.types.meta.FileBackedMetaBase
  :members:


.. autoclass:: nc5ng.types.meta.SingletonFileBackedMeta
  :members:

"""

from ._file_meta import FileBackedMetaBase, SingletonFileBackedMeta
from ._datapoint_meta import DataPointType
