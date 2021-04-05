# -*- coding: utf-8 -*-
from gocam.gocam import *
from types import ModuleType

import json
from jsonasobj import as_json
from rdflib import Graph

from linkml.generators.jsonldcontextgen import ContextGenerator
from linkml.generators.pythongen import PythonGenerator
from linkml.generators.shexgen import ShExGenerator
from linkml.generators.yumlgen import YumlGenerator
from linkml.utils.yamlutils import DupCheckYamlLoader
from linkml.dumpers.json_dumper import dumps
import os
from tests import JSONLD_DIR, TARGET_DIR

"""Test the module can be imported."""

import unittest

# from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7012280/figure/F3/

WNT_SIGNALING = 'GO:0060070' ## canonical Wnt signaling pathway
RECEPTOR_LIGAND = 'GO:0048018' ## receptor ligand activity
RECEPTOR_ACTIVITY = 'GO:0042813' ## Wnt-activated receptor activity
EXTRACELLULAR = 'GO:0005615' ## extracellular space
PM = 'GO:0005886' ## plasma membrane
WNT3 = 'UniprotKB:P56703'
FZD1 = 'UniprotKB:Q9UP38'

ttl_out = os.path.join(TARGET_DIR, 'sample.ttl')
json_out = os.path.join(TARGET_DIR, 'sample.jsonld')
cntxt_file =  os.path.join(JSONLD_DIR, 'gocam.context.jsonld')
f = open(cntxt_file)
#cntxt = json.load(f)
cntxt = f.read()

def id(s):
    return f'model:a5g4ccd08-{s}'

counter = 0
def gen_evidence(eco: str, ref: str = 'PMID:1234') -> Evidence:
    global  counter
    counter += 1
    return Evidence(id=id(f'e{counter}'),
                    evidence_type=eco, reference=ref)

class TestCreate(unittest.TestCase):
    """A test case for create tests."""

    def test_create(self):
        m = Model(id=id('m1'),
                  title='test title',
                  contributor=['orcid:123', 'orcid:234'],
                  state=ModelStateEnum.production)
        print(f'Model = {m.id}')
        p1 = BiologicalProcess(id=id('p1'), type=WNT_SIGNALING)
        c1 = AnatomicalEntity(id=id('c1'), type=EXTRACELLULAR,
                              category=AnatomicalEntityCategory.CellularAnatomicalEntity)
        c2 = AnatomicalEntity(id=id('c2'), type=PM,
                              category=AnatomicalEntityCategory.CellularAnatomicalEntity)
        g1 = InformationBiomacromolecule(id=id('g1'), type=WNT3,
                                         category=InformationBiomacromoleculeCategory.GeneOrReferenceProtein)
        g2 = InformationBiomacromolecule(id=id('g2'), type=FZD1,
                                         category=InformationBiomacromoleculeCategory.GeneOrReferenceProtein)
        a2 = MolecularActivity(id=id('a2'), type=RECEPTOR_ACTIVITY,
                               enabled_by=EnabledByAssociation( has_evidence=gen_evidence('ECO:nnn'),
                                                               object=g2.id),
                               occurs_in=OccursInAssociation(
                                   has_evidence=gen_evidence('ECO:nnn'),
                                   object=c2.id),
                               part_of=ProcessPartOfAssociation(
                                   has_evidence=gen_evidence('ECO:nnn'),
                                   object=p1.id))
        a1 = MolecularActivity(id=id('a1'), type=RECEPTOR_LIGAND,
                               enabled_by=EnabledByAssociation(
                                   has_evidence=gen_evidence('ECO:nnn'),
                                   object=g1.id),
                               occurs_in=OccursInAssociation(
                                   has_evidence=gen_evidence('ECO:nnn'),
                                   object=c1.id),
                               causes=CausesAssociation(has_evidence=gen_evidence('ECO:nnn'),
                                                        predicate='regulates',
                                                        object=id('a2')))

        m.molecular_activity_set = [a1, a2]
        m.information_biomacromolecule_set = [g1, g2]
        jsonld = dumps(m, cntxt)
        print(jsonld)
        with open(json_out, 'w') as io:
            io.write(jsonld)
        #print(cntxt)
        g = Graph()
        g.parse(data=jsonld, format="json-ld")
        print(f'Writing to {ttl_out}')
        g.serialize(destination=ttl_out, format='turtle')
        ttl = g.serialize(format="turtle").decode()
        print(ttl)
        print(f'P1={p1.id} // {p1}')
