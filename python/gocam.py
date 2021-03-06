# Auto generated from gocam.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-03 16:56
# Schema: gocam
#
# id: https://w3id.org/gocam
# description: GO CAM experimental LinkML schema
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


class AnatomicalEntityId(ElementId):
    pass


class InformationMacromoleculeId(ElementId):
    pass


class OntologyClassId(extended_str):
    pass


@dataclass
class Element(YAMLRoot):
    """
    Base class for any biological entity or occurrent in a GO-CAM model
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
    part_of: Optional[Union[dict, "ProcessPartOfAssociation"]] = None
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

        if self.part_of is not None and not isinstance(self.part_of, ProcessPartOfAssociation):
            self.part_of = ProcessPartOfAssociation(**self.part_of)

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
class AnatomicalEntity(Element):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.AnatomicalEntity
    class_class_curie: ClassVar[str] = "gocam:AnatomicalEntity"
    class_name: ClassVar[str] = "anatomical entity"
    class_model_uri: ClassVar[URIRef] = GOCAM.AnatomicalEntity

    id: Union[str, AnatomicalEntityId] = None
    part_of: Optional[Union[dict, "EntityPartOfAssociation"]] = None
    category: Optional[Union[str, "AnatomicalEntityCategory"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)

        if self.part_of is not None and not isinstance(self.part_of, EntityPartOfAssociation):
            self.part_of = EntityPartOfAssociation(**self.part_of)

        if self.category is not None and not isinstance(self.category, AnatomicalEntityCategory):
            self.category = AnatomicalEntityCategory(self.category)

        super().__post_init__(**kwargs)


@dataclass
class InformationMacromolecule(Element):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.InformationMacromolecule
    class_class_curie: ClassVar[str] = "gocam:InformationMacromolecule"
    class_name: ClassVar[str] = "information macromolecule"
    class_model_uri: ClassVar[URIRef] = GOCAM.InformationMacromolecule

    id: Union[str, InformationMacromoleculeId] = None
    part_of: Optional[Union[dict, "PartOfAssociation"]] = None
    category: Optional[Union[str, "AnatomicalEntityCategory"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, InformationMacromoleculeId):
            self.id = InformationMacromoleculeId(self.id)

        if self.part_of is not None and not isinstance(self.part_of, PartOfAssociation):
            self.part_of = PartOfAssociation(**self.part_of)

        if self.category is not None and not isinstance(self.category, AnatomicalEntityCategory):
            self.category = AnatomicalEntityCategory(self.category)

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
    object: Union[str, AnatomicalEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class CausesAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.CausesAssociation
    class_class_curie: ClassVar[str] = "gocam:CausesAssociation"
    class_name: ClassVar[str] = "causes association"
    class_model_uri: ClassVar[URIRef] = GOCAM.CausesAssociation

    subject: Union[str, ElementId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[dict, "Occurrent"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, Occurrent):
            self.object = Occurrent()

        super().__post_init__(**kwargs)


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
class EntityPartOfAssociation(PartOfAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.EntityPartOfAssociation
    class_class_curie: ClassVar[str] = "gocam:EntityPartOfAssociation"
    class_name: ClassVar[str] = "entity part of association"
    class_model_uri: ClassVar[URIRef] = GOCAM.EntityPartOfAssociation

    subject: Union[str, ElementId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[dict, "Continuant"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, Continuant):
            self.object = Continuant()

        super().__post_init__(**kwargs)


@dataclass
class ProcessPartOfAssociation(PartOfAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ProcessPartOfAssociation
    class_class_curie: ClassVar[str] = "gocam:ProcessPartOfAssociation"
    class_name: ClassVar[str] = "process part of association"
    class_model_uri: ClassVar[URIRef] = GOCAM.ProcessPartOfAssociation

    subject: Union[str, ElementId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[dict, "Occurrent"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, Occurrent):
            self.object = Occurrent()

        super().__post_init__(**kwargs)


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


class Occurrent(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Occurrent
    class_class_curie: ClassVar[str] = "gocam:Occurrent"
    class_name: ClassVar[str] = "occurrent"
    class_model_uri: ClassVar[URIRef] = GOCAM.Occurrent


class Continuant(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Continuant
    class_class_curie: ClassVar[str] = "gocam:Continuant"
    class_name: ClassVar[str] = "continuant"
    class_model_uri: ClassVar[URIRef] = GOCAM.Continuant


# Enumerations
class AnatomicalEntityCategory(EnumDefinitionImpl):

    CellularAnatomicalEntity = PermissibleValue(text="CellularAnatomicalEntity")
    Cell = PermissibleValue(text="Cell")
    GrossAnatomicalStructure = PermissibleValue(text="GrossAnatomicalStructure")
    Organism = PermissibleValue(text="Organism")

    _defn = EnumDefinition(
        name="AnatomicalEntityCategory",
    )

class CausalPredicateEnum(EnumDefinitionImpl):

    regulates = PermissibleValue(text="regulates",
                                         meaning=RO["0002211"])

    _defn = EnumDefinition(
        name="CausalPredicateEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "causally upstream of, positive effect",
                PermissibleValue(text="causally upstream of, positive effect",
                                 meaning=RO["0002304"]) )
        setattr(cls, "causally upstream of, negative effect",
                PermissibleValue(text="causally upstream of, negative effect",
                                 meaning=RO["0002305"]) )
        setattr(cls, "causally upstream of",
                PermissibleValue(text="causally upstream of",
                                 meaning=RO["0002411"]) )
        setattr(cls, "immediately causally upstream of",
                PermissibleValue(text="immediately causally upstream of",
                                 meaning=RO["0002412"]) )
        setattr(cls, "causally upstream of or within",
                PermissibleValue(text="causally upstream of or within",
                                 meaning=RO["0002418"]) )
        setattr(cls, "causally upstream of or within, negative effect",
                PermissibleValue(text="causally upstream of or within, negative effect",
                                 meaning=RO["0004046"]) )
        setattr(cls, "causally upstream of or within, positive effect",
                PermissibleValue(text="causally upstream of or within, positive effect",
                                 meaning=RO["0004047"]) )
        setattr(cls, "negatively regulates",
                PermissibleValue(text="negatively regulates",
                                 meaning=RO["0002212"]) )
        setattr(cls, "positively regulates",
                PermissibleValue(text="positively regulates",
                                 meaning=RO["0002213"]) )

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

slots.molecular_activity_part_of = Slot(uri=GOCAM.part_of, name="molecular activity_part of", curie=GOCAM.curie('part_of'),
                   model_uri=GOCAM.molecular_activity_part_of, domain=MolecularActivity, range=Optional[Union[dict, "ProcessPartOfAssociation"]])

slots.anatomical_entity_category = Slot(uri=GOCAM.category, name="anatomical entity_category", curie=GOCAM.curie('category'),
                   model_uri=GOCAM.anatomical_entity_category, domain=AnatomicalEntity, range=Optional[Union[str, "AnatomicalEntityCategory"]])

slots.anatomical_entity_part_of = Slot(uri=GOCAM.part_of, name="anatomical entity_part of", curie=GOCAM.curie('part_of'),
                   model_uri=GOCAM.anatomical_entity_part_of, domain=AnatomicalEntity, range=Optional[Union[dict, "EntityPartOfAssociation"]])

slots.information_macromolecule_category = Slot(uri=GOCAM.category, name="information macromolecule_category", curie=GOCAM.curie('category'),
                   model_uri=GOCAM.information_macromolecule_category, domain=InformationMacromolecule, range=Optional[Union[str, "AnatomicalEntityCategory"]])

slots.occurs_in_association_object = Slot(uri=GOCAM.object, name="occurs in association_object", curie=GOCAM.curie('object'),
                   model_uri=GOCAM.occurs_in_association_object, domain=OccursInAssociation, range=Union[str, AnatomicalEntityId])

slots.causes_association_object = Slot(uri=GOCAM.object, name="causes association_object", curie=GOCAM.curie('object'),
                   model_uri=GOCAM.causes_association_object, domain=CausesAssociation, range=Union[dict, "Occurrent"])

slots.entity_part_of_association_object = Slot(uri=GOCAM.object, name="entity part of association_object", curie=GOCAM.curie('object'),
                   model_uri=GOCAM.entity_part_of_association_object, domain=EntityPartOfAssociation, range=Union[dict, "Continuant"])

slots.process_part_of_association_object = Slot(uri=GOCAM.object, name="process part of association_object", curie=GOCAM.curie('object'),
                   model_uri=GOCAM.process_part_of_association_object, domain=ProcessPartOfAssociation, range=Union[dict, "Occurrent"])
