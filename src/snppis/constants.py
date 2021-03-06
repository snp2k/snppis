# -*- coding: utf-8 -*-

"""Constants for :mod:`snppis`."""

import os
from typing import Tuple

HERE = os.path.abspath(os.path.dirname(__file__))

RESOURCES = os.path.join(HERE, 'resources')
os.makedirs(RESOURCES, exist_ok=True)

MAPPINGS = os.path.join(RESOURCES, 'mappings')
os.makedirs(MAPPINGS, exist_ok=True)

MYVARIANT_CACHE = os.path.join(RESOURCES, 'myvariant')
os.makedirs(MYVARIANT_CACHE, exist_ok=True)

DATABASES = [
    'kegg',
    'wikipathways',
    'reactome',
]

#: The database, identifier, and name of a pahtway
PathwayTuple = Tuple[str, str, str]
