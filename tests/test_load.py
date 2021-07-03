# -*- coding: utf-8 -*-
from gocam.gocam import *
from rdflib import Graph
import json

from hbreader import hbread
from linkml_runtime.loaders import yaml_loader, json_loader, rdf_loader
from linkml_runtime.dumpers import json_dumper, yaml_dumper, rdf_dumper

import os
from tests import JSONLD_DIR, RESOURCE_DIR

"""Test the module can be imported."""

import unittest

json_in = os.path.join(RESOURCE_DIR, 'sample.json')
a1json = os.path.join(RESOURCE_DIR, 'activity1.json')

class TestLoad(unittest.TestCase):
    """A test case for loading."""

    def test_load(self):
        a = {
            "id": 'activity-instance:001',
            "type": "GO:0048018",
            "occurs_in": {
                "object": "gomodel:a5g4ccd08-c1"
            }
        }
        a = json_loader.loads(a, MolecularActivity)
        #print(a)