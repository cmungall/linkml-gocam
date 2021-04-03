# Auto generated from gocam.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-03 12:39
# Schema: gocam
#
# id: https://w3id.org/gocam
# description: GO CAM
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from biolinkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from .types import String, Uriorcurie
from biolinkml.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
GOCAM = CurieNamespace('gocam', 'https://w3id.org/gocam/')
GOSHAPES = CurieNamespace('goshapes', 'http://purl.obolibrary.org/obo/go/shapes/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = GOCAM


# Types
class ChemicalFormulaValue(str):
    """ A chemical formula """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "chemical formula value"
    type_model_uri = GOCAM.ChemicalFormulaValue


class CategoryType(Uriorcurie):
    """ A primitive type in which the value denotes a class within the biolink model. The value must be a URI or a CURIE. In a Neo4j representation, the value should be the CURIE for the biolink class, for example biolink:Gene. For an RDF representation, the value should be a URI such as https://w3id.org/biolink/vocab/Gene """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "category type"
    type_model_uri = GOCAM.CategoryType


class IriType(Uriorcurie):
    """ An IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = GOCAM.IriType


class LabelType(String):
    """ A string that provides a human-readable name for an entity """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "label type"
    type_model_uri = GOCAM.LabelType


class PredicateType(Uriorcurie):
    """ A CURIE from the biolink related_to hierarchy. For example, biolink:related_to, biolink:causes, biolink:treats. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "predicate type"
    type_model_uri = GOCAM.PredicateType


class NarrativeText(String):
    """ A string that provides a human-readable description of something """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "narrative text"
    type_model_uri = GOCAM.NarrativeText


class SymbolType(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "symbol type"
    type_model_uri = GOCAM.SymbolType


# Class references
class ElementId(extended_str):
    pass


class MolecularActivityId(ElementId):
    pass


class BiologicalProcessId(ElementId):
    pass


class CellularComponentId(ElementId):
    pass


class OntologyClassId(extended_str):
    pass


@dataclass
class Element(YAMLRoot):
    """
    An OWL individual representing a particular element in a context. Here element is generic and encompasses causal
    entities as well as processes, activities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Element
    class_class_curie: ClassVar[str] = "gocam:Element"
    class_name: ClassVar[str] = "element"
    class_model_uri: ClassVar[URIRef] = GOCAM.Element

    id: Union[str, ElementId] = None
    type: Optional[Union[str, OntologyClassId]] = None
    type_inferences: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ElementId):
            self.id = ElementId(self.id)

        if self.type is not None and not isinstance(self.type, OntologyClassId):
            self.type = OntologyClassId(self.type)

        if self.type_inferences is None:
            self.type_inferences = []
        if not isinstance(self.type_inferences, list):
            self.type_inferences = [self.type_inferences]
        self.type_inferences = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.type_inferences]

        super().__post_init__(**kwargs)


@dataclass
class MolecularActivity(Element):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.MolecularActivity
    class_class_curie: ClassVar[str] = "gocam:MolecularActivity"
    class_name: ClassVar[str] = "molecular activity"
    class_model_uri: ClassVar[URIRef] = GOCAM.MolecularActivity

    id: Union[str, MolecularActivityId] = None
    causes: Optional[Union[dict, "CausesAssociation"]] = None
    happens_during: Optional[Union[dict, "HappensDuringAssociation"]] = None
    part_of: Optional[Union[dict, "PartOfAssociation"]] = None
    enabled_by: Optional[Union[dict, "EnabledByAssociation"]] = None
    has_input: Optional[Union[dict, "HasInputAssociation"]] = None
    occurs_in: Optional[Union[dict, "OccursInAssociation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MolecularActivityId):
            self.id = MolecularActivityId(self.id)

        if self.causes is not None and not isinstance(self.causes, CausesAssociation):
            self.causes = CausesAssociation(**self.causes)

        if self.happens_during is not None and not isinstance(self.happens_during, HappensDuringAssociation):
            self.happens_during = HappensDuringAssociation(**self.happens_during)

        if self.part_of is not None and not isinstance(self.part_of, PartOfAssociation):
            self.part_of = PartOfAssociation(**self.part_of)

        if self.enabled_by is not None and not isinstance(self.enabled_by, EnabledByAssociation):
            self.enabled_by = EnabledByAssociation(**self.enabled_by)

        if self.has_input is not None and not isinstance(self.has_input, HasInputAssociation):
            self.has_input = HasInputAssociation(**self.has_input)

        if self.occurs_in is not None and not isinstance(self.occurs_in, OccursInAssociation):
            self.occurs_in = OccursInAssociation(**self.occurs_in)

        super().__post_init__(**kwargs)


@dataclass
class BiologicalProcess(Element):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.BiologicalProcess
    class_class_curie: ClassVar[str] = "gocam:BiologicalProcess"
    class_name: ClassVar[str] = "biological process"
    class_model_uri: ClassVar[URIRef] = GOCAM.BiologicalProcess

    id: Union[str, BiologicalProcessId] = None
    occurs_in: Optional[Union[dict, "OccursInAssociation"]] = None
    causes: Optional[Union[dict, "CausesAssociation"]] = None
    happens_during: Optional[Union[dict, "HappensDuringAssociation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BiologicalProcessId):
            self.id = BiologicalProcessId(self.id)

        if self.occurs_in is not None and not isinstance(self.occurs_in, OccursInAssociation):
            self.occurs_in = OccursInAssociation(**self.occurs_in)

        if self.causes is not None and not isinstance(self.causes, CausesAssociation):
            self.causes = CausesAssociation(**self.causes)

        if self.happens_during is not None and not isinstance(self.happens_during, HappensDuringAssociation):
            self.happens_during = HappensDuringAssociation(**self.happens_during)

        super().__post_init__(**kwargs)


@dataclass
class CellularComponent(Element):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.CellularComponent
    class_class_curie: ClassVar[str] = "gocam:CellularComponent"
    class_name: ClassVar[str] = "cellular component"
    class_model_uri: ClassVar[URIRef] = GOCAM.CellularComponent

    id: Union[str, CellularComponentId] = None
    part_of: Optional[Union[dict, "PartOfAssociation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CellularComponentId):
            self.id = CellularComponentId(self.id)

        if self.part_of is not None and not isinstance(self.part_of, PartOfAssociation):
            self.part_of = PartOfAssociation(**self.part_of)

        super().__post_init__(**kwargs)


@dataclass
class Association(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Association
    class_class_curie: ClassVar[str] = "gocam:Association"
    class_name: ClassVar[str] = "association"
    class_model_uri: ClassVar[URIRef] = GOCAM.Association

    subject: Union[str, ElementId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, ElementId] = None
    has_evidence: Optional[Union[dict, "Evidence"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ElementId):
            self.subject = ElementId(self.subject)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ElementId):
            self.object = ElementId(self.object)

        if self.has_evidence is not None and not isinstance(self.has_evidence, Evidence):
            self.has_evidence = Evidence(**self.has_evidence)

        super().__post_init__(**kwargs)


@dataclass
class OccursInAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.OccursInAssociation
    class_class_curie: ClassVar[str] = "gocam:OccursInAssociation"
    class_name: ClassVar[str] = "occurs in association"
    class_model_uri: ClassVar[URIRef] = GOCAM.OccursInAssociation

    subject: Union[str, ElementId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, ElementId] = None

@dataclass
class CausesAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.CausesAssociation
    class_class_curie: ClassVar[str] = "gocam:CausesAssociation"
    class_name: ClassVar[str] = "causes association"
    class_model_uri: ClassVar[URIRef] = GOCAM.CausesAssociation

    subject: Union[str, ElementId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, ElementId] = None

@dataclass
class PartOfAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.PartOfAssociation
    class_class_curie: ClassVar[str] = "gocam:PartOfAssociation"
    class_name: ClassVar[str] = "part of association"
    class_model_uri: ClassVar[URIRef] = GOCAM.PartOfAssociation

    subject: Union[str, ElementId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, ElementId] = None

@dataclass
class EnabledByAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.EnabledByAssociation
    class_class_curie: ClassVar[str] = "gocam:EnabledByAssociation"
    class_name: ClassVar[str] = "enabled by association"
    class_model_uri: ClassVar[URIRef] = GOCAM.EnabledByAssociation

    subject: Union[str, ElementId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, ElementId] = None

@dataclass
class HappensDuringAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.HappensDuringAssociation
    class_class_curie: ClassVar[str] = "gocam:HappensDuringAssociation"
    class_name: ClassVar[str] = "happens during association"
    class_model_uri: ClassVar[URIRef] = GOCAM.HappensDuringAssociation

    subject: Union[str, ElementId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, ElementId] = None

@dataclass
class HasPartAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.HasPartAssociation
    class_class_curie: ClassVar[str] = "gocam:HasPartAssociation"
    class_name: ClassVar[str] = "has part association"
    class_model_uri: ClassVar[URIRef] = GOCAM.HasPartAssociation

    subject: Union[str, ElementId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, ElementId] = None

@dataclass
class HasInputAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.HasInputAssociation
    class_class_curie: ClassVar[str] = "gocam:HasInputAssociation"
    class_name: ClassVar[str] = "has input association"
    class_model_uri: ClassVar[URIRef] = GOCAM.HasInputAssociation

    subject: Union[str, ElementId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, ElementId] = None

@dataclass
class OntologyClass(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.OntologyClass
    class_class_curie: ClassVar[str] = "gocam:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = GOCAM.OntologyClass

    id: Union[str, OntologyClassId] = None
    name: Optional[Union[str, LabelType]] = None
    category: Optional[Union[str, CategoryType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.category is not None and not isinstance(self.category, CategoryType):
            self.category = CategoryType(self.category)

        super().__post_init__(**kwargs)


@dataclass
class Evidence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Evidence
    class_class_curie: ClassVar[str] = "gocam:Evidence"
    class_name: ClassVar[str] = "evidence"
    class_model_uri: ClassVar[URIRef] = GOCAM.Evidence

    contributor: Optional[str] = None
    date: Optional[str] = None
    evidence_type: Optional[Union[str, OntologyClassId]] = None
    reference: Optional[str] = None
    with: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.contributor is not None and not isinstance(self.contributor, str):
            self.contributor = str(self.contributor)

        if self.date is not None and not isinstance(self.date, str):
            self.date = str(self.date)

        if self.evidence_type is not None and not isinstance(self.evidence_type, OntologyClassId):
            self.evidence_type = OntologyClassId(self.evidence_type)

        if self.reference is not None and not isinstance(self.reference, str):
            self.reference = str(self.reference)

        if self.with is not None and not isinstance(self.with, str):
            self.with = str(self.with)

        super().__post_init__(**kwargs)


class Occurent(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Occurent
    class_class_curie: ClassVar[str] = "gocam:Occurent"
    class_name: ClassVar[str] = "occurent"
    class_model_uri: ClassVar[URIRef] = GOCAM.Occurent


class Continuant(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Continuant
    class_class_curie: ClassVar[str] = "gocam:Continuant"
    class_name: ClassVar[str] = "continuant"
    class_model_uri: ClassVar[URIRef] = GOCAM.Continuant


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=GOCAM.id, name="id", curie=GOCAM.curie('id'),
                   model_uri=GOCAM.id, domain=None, range=URIRef)

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=GOCAM.name, domain=None, range=Optional[Union[str, LabelType]])

slots.type = Slot(uri=GOCAM.type, name="type", curie=GOCAM.curie('type'),
                   model_uri=GOCAM.type, domain=None, range=Optional[Union[str, OntologyClassId]])

slots.category = Slot(uri=GOCAM.category, name="category", curie=GOCAM.curie('category'),
                   model_uri=GOCAM.category, domain=None, range=Optional[Union[str, CategoryType]])

slots.with = Slot(uri=GOCAM.with, name="with", curie=GOCAM.curie('with'),
                   model_uri=GOCAM.with, domain=None, range=Optional[str])

slots.reference = Slot(uri=GOCAM.reference, name="reference", curie=GOCAM.curie('reference'),
                   model_uri=GOCAM.reference, domain=None, range=Optional[str])

slots.contributor = Slot(uri=GOCAM.contributor, name="contributor", curie=GOCAM.curie('contributor'),
                   model_uri=GOCAM.contributor, domain=None, range=Optional[str])

slots.date = Slot(uri=GOCAM.date, name="date", curie=GOCAM.curie('date'),
                   model_uri=GOCAM.date, domain=None, range=Optional[str])

slots.evidence_type = Slot(uri=GOCAM.evidence_type, name="evidence type", curie=GOCAM.curie('evidence_type'),
                   model_uri=GOCAM.evidence_type, domain=None, range=Optional[Union[str, OntologyClassId]])

slots.type_inferences = Slot(uri=GOCAM.type_inferences, name="type inferences", curie=GOCAM.curie('type_inferences'),
                   model_uri=GOCAM.type_inferences, domain=None, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.related_to = Slot(uri=GOCAM.related_to, name="related to", curie=GOCAM.curie('related_to'),
                   model_uri=GOCAM.related_to, domain=None, range=Optional[Union[dict, Association]])

slots.occurs_in = Slot(uri=GOCAM.occurs_in, name="occurs in", curie=GOCAM.curie('occurs_in'),
                   model_uri=GOCAM.occurs_in, domain=None, range=Optional[Union[dict, OccursInAssociation]])

slots.causes = Slot(uri=GOCAM.causes, name="causes", curie=GOCAM.curie('causes'),
                   model_uri=GOCAM.causes, domain=None, range=Optional[Union[dict, CausesAssociation]])

slots.happens_during = Slot(uri=GOCAM.happens_during, name="happens during", curie=GOCAM.curie('happens_during'),
                   model_uri=GOCAM.happens_during, domain=None, range=Optional[Union[dict, HappensDuringAssociation]])

slots.part_of = Slot(uri=GOCAM.part_of, name="part of", curie=GOCAM.curie('part_of'),
                   model_uri=GOCAM.part_of, domain=None, range=Optional[Union[dict, PartOfAssociation]])

slots.enabled_by = Slot(uri=GOCAM.enabled_by, name="enabled by", curie=GOCAM.curie('enabled_by'),
                   model_uri=GOCAM.enabled_by, domain=None, range=Optional[Union[dict, EnabledByAssociation]])

slots.has_input = Slot(uri=GOCAM.has_input, name="has input", curie=GOCAM.curie('has_input'),
                   model_uri=GOCAM.has_input, domain=None, range=Optional[Union[dict, HasInputAssociation]])

slots.has_evidence = Slot(uri=GOCAM.has_evidence, name="has evidence", curie=GOCAM.curie('has_evidence'),
                   model_uri=GOCAM.has_evidence, domain=None, range=Optional[Union[dict, Evidence]])

slots.association_slot = Slot(uri=GOCAM.association_slot, name="association slot", curie=GOCAM.curie('association_slot'),
                   model_uri=GOCAM.association_slot, domain=Association, range=Optional[str])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=GOCAM.subject, domain=Association, range=Union[str, ElementId])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=GOCAM.object, domain=Association, range=Union[str, ElementId])

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=GOCAM.predicate, domain=Association, range=Union[str, PredicateType])
