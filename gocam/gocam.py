# Auto generated from gocam.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-06-25 16:20
# Schema: gocam
#
# id: https://w3id.org/gocam
# description: GO CAM LinkML schema (experimental) The central class in this datamodel is a [Model](Model.md). A
#              model consists of a set of [MolecularActivity](MolecularActivity.md) objects, from which hangs
#              various elements connected by different kinds of [Association](Association.md) See: *
#              [https://github.com/cmungall/linkml-gocam](https://github.com/cmungall/linkml-gocam) *
#              [https://cmungall.github.io/linkml-gocam/](https://cmungall.github.io/linkml-gocam/)
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
DOI = CurieNamespace('DOI', 'http://dx.doi.org/')
ECO = CurieNamespace('ECO', 'http://purl.obolibrary.org/obo/ECO_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
DCE = CurieNamespace('dce', 'http://purl.org/dc/elements/1.1/')
GOCAM = CurieNamespace('gocam', 'https://w3id.org/gocam/')
GOMODEL = CurieNamespace('gomodel', 'http://model.geneontology.org/')
GOSHAPES = CurieNamespace('goshapes', 'http://purl.obolibrary.org/obo/go/shapes/')
LEGO = CurieNamespace('lego', 'http://geneontology.org/lego/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
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
    """ A RO identifier """
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


class ModelId(ElementId):
    pass


class DomainElementId(ElementId):
    pass


class MolecularActivityId(DomainElementId):
    pass


class BiologicalProcessId(DomainElementId):
    pass


class AnatomicalEntityId(DomainElementId):
    pass


class ChemicalEntityId(DomainElementId):
    pass


class InformationBiomacromoleculeId(ChemicalEntityId):
    pass


class OntologyClassId(extended_str):
    pass


class InformationElementId(ElementId):
    pass


class PublicationId(InformationElementId):
    pass


class EvidenceId(InformationElementId):
    pass


class DomainElementMixinId(extended_str):
    pass


class ActivityOrProcessId(DomainElementMixinId):
    pass


class ProcessOrPhaseId(DomainElementMixinId):
    pass


class ContinuantId(DomainElementMixinId):
    pass


@dataclass
class Element(YAMLRoot):
    """
    Base class for any biological entity or activity or process in a GO-CAM model
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Element
    class_class_curie: ClassVar[str] = "gocam:Element"
    class_name: ClassVar[str] = "element"
    class_model_uri: ClassVar[URIRef] = GOCAM.Element

    id: Union[str, ElementId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ElementId):
            self.id = ElementId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Model(Element):
    """
    A collection of GO-CAM elements and associated metadata. A model combines multiple simple GO annotations into an
    integrated, semantically precise and computable model of biological function.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Model
    class_class_curie: ClassVar[str] = "gocam:Model"
    class_name: ClassVar[str] = "model"
    class_model_uri: ClassVar[URIRef] = GOCAM.Model

    id: Union[str, ModelId] = None
    title: Optional[str] = None
    contributor: Optional[Union[str, List[str]]] = empty_list()
    date: Optional[str] = None
    state: Optional[Union[str, "ModelStateEnum"]] = None
    provided_by: Optional[str] = None
    molecular_activity_set: Optional[Union[Dict[Union[str, MolecularActivityId], Union[dict, "MolecularActivity"]], List[Union[dict, "MolecularActivity"]]]] = empty_dict()
    biological_process_set: Optional[Union[Dict[Union[str, BiologicalProcessId], Union[dict, "BiologicalProcess"]], List[Union[dict, "BiologicalProcess"]]]] = empty_dict()
    information_biomacromolecule_set: Optional[Union[Dict[Union[str, InformationBiomacromoleculeId], Union[dict, "InformationBiomacromolecule"]], List[Union[dict, "InformationBiomacromolecule"]]]] = empty_dict()
    chemical_entity_set: Optional[Union[Dict[Union[str, ChemicalEntityId], Union[dict, "ChemicalEntity"]], List[Union[dict, "ChemicalEntity"]]]] = empty_dict()
    ontology_class_set: Optional[Union[Dict[Union[str, OntologyClassId], Union[dict, "OntologyClass"]], List[Union[dict, "OntologyClass"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModelId):
            self.id = ModelId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.contributor, list):
            self.contributor = [self.contributor] if self.contributor is not None else []
        self.contributor = [v if isinstance(v, str) else str(v) for v in self.contributor]

        if self.date is not None and not isinstance(self.date, str):
            self.date = str(self.date)

        if self.state is not None and not isinstance(self.state, ModelStateEnum):
            self.state = ModelStateEnum(self.state)

        if self.provided_by is not None and not isinstance(self.provided_by, str):
            self.provided_by = str(self.provided_by)

        self._normalize_inlined_as_dict(slot_name="molecular_activity_set", slot_type=MolecularActivity, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="biological_process_set", slot_type=BiologicalProcess, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="information_biomacromolecule_set", slot_type=InformationBiomacromolecule, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="chemical_entity_set", slot_type=ChemicalEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="ontology_class_set", slot_type=OntologyClass, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class DomainElement(Element):
    """
    An element that is part of a GO-CAM model
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.DomainElement
    class_class_curie: ClassVar[str] = "gocam:DomainElement"
    class_name: ClassVar[str] = "domain element"
    class_model_uri: ClassVar[URIRef] = GOCAM.DomainElement

    id: Union[str, DomainElementId] = None
    type: Union[str, OntologyClassId] = None
    type_inferences: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DomainElementId):
            self.id = DomainElementId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, OntologyClassId):
            self.type = OntologyClassId(self.type)

        if not isinstance(self.type_inferences, list):
            self.type_inferences = [self.type_inferences] if self.type_inferences is not None else []
        self.type_inferences = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.type_inferences]

        super().__post_init__(**kwargs)


@dataclass
class MolecularActivity(DomainElement):
    """
    An instance of a GO molecular function
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.MolecularActivity
    class_class_curie: ClassVar[str] = "gocam:MolecularActivity"
    class_name: ClassVar[str] = "molecular activity"
    class_model_uri: ClassVar[URIRef] = GOCAM.MolecularActivity

    id: Union[str, MolecularActivityId] = None
    type: Union[str, OntologyClassId] = None
    influences: Optional[Union[dict, "CausalAssociation"]] = None
    happens_during: Optional[Union[dict, "HappensDuringAssociation"]] = None
    part_of: Optional[Union[dict, "ProcessPartOfAssociation"]] = None
    enabled_by: Optional[Union[dict, "EnabledByAssociation"]] = None
    has_input: Optional[Union[dict, "HasInputAssociation"]] = None
    occurs_in: Optional[Union[dict, "OccursInAssociation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularActivityId):
            self.id = MolecularActivityId(self.id)

        if self.influences is not None and not isinstance(self.influences, CausalAssociation):
            self.influences = CausalAssociation(**self.influences)

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
class BiologicalProcess(DomainElement):
    """
    An instance of a GO biological process
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.BiologicalProcess
    class_class_curie: ClassVar[str] = "gocam:BiologicalProcess"
    class_name: ClassVar[str] = "biological process"
    class_model_uri: ClassVar[URIRef] = GOCAM.BiologicalProcess

    id: Union[str, BiologicalProcessId] = None
    type: Union[str, OntologyClassId] = None
    occurs_in: Optional[Union[dict, "OccursInAssociation"]] = None
    influences: Optional[Union[dict, "CausalAssociation"]] = None
    happens_during: Optional[Union[dict, "HappensDuringAssociation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiologicalProcessId):
            self.id = BiologicalProcessId(self.id)

        if self.occurs_in is not None and not isinstance(self.occurs_in, OccursInAssociation):
            self.occurs_in = OccursInAssociation(**self.occurs_in)

        if self.influences is not None and not isinstance(self.influences, CausalAssociation):
            self.influences = CausalAssociation(**self.influences)

        if self.happens_during is not None and not isinstance(self.happens_during, HappensDuringAssociation):
            self.happens_during = HappensDuringAssociation(**self.happens_during)

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalEntity(DomainElement):
    """
    An instance of a GO cellular anatomical entity, a cell type, or gross anatomical structure
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.AnatomicalEntity
    class_class_curie: ClassVar[str] = "gocam:AnatomicalEntity"
    class_name: ClassVar[str] = "anatomical entity"
    class_model_uri: ClassVar[URIRef] = GOCAM.AnatomicalEntity

    id: Union[str, AnatomicalEntityId] = None
    type: Union[str, OntologyClassId] = None
    category: Union[str, "AnatomicalEntityCategory"] = None
    part_of: Optional[Union[dict, "AnatomicalPartOfAssociation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, AnatomicalEntityCategory):
            self.category = AnatomicalEntityCategory(self.category)

        if self.part_of is not None and not isinstance(self.part_of, AnatomicalPartOfAssociation):
            self.part_of = AnatomicalPartOfAssociation(**self.part_of)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalEntity(DomainElement):
    """
    An instance of a chemical entity, as defined in CHEBI, including macromolecules defined in NEO
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ChemicalEntity
    class_class_curie: ClassVar[str] = "gocam:ChemicalEntity"
    class_name: ClassVar[str] = "chemical entity"
    class_model_uri: ClassVar[URIRef] = GOCAM.ChemicalEntity

    id: Union[str, ChemicalEntityId] = None
    type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityId):
            self.id = ChemicalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class InformationBiomacromolecule(ChemicalEntity):
    """
    This class groups gene, gene product (protein on ncRNA), or a macromolecular complex that is capable of carrying
    out a molecular activity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.InformationBiomacromolecule
    class_class_curie: ClassVar[str] = "gocam:InformationBiomacromolecule"
    class_name: ClassVar[str] = "information biomacromolecule"
    class_model_uri: ClassVar[URIRef] = GOCAM.InformationBiomacromolecule

    id: Union[str, InformationBiomacromoleculeId] = None
    type: Union[str, OntologyClassId] = None
    category: Union[str, "InformationBiomacromoleculeCategory"] = None
    has_part: Optional[Union[dict, "MacromoleculeHasPartAssociation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationBiomacromoleculeId):
            self.id = InformationBiomacromoleculeId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, InformationBiomacromoleculeCategory):
            self.category = InformationBiomacromoleculeCategory(self.category)

        if self.has_part is not None and not isinstance(self.has_part, MacromoleculeHasPartAssociation):
            self.has_part = MacromoleculeHasPartAssociation(**self.has_part)

        super().__post_init__(**kwargs)


@dataclass
class Association(YAMLRoot):
    """
    An association between a domain element (e.g. a MolecularActivity) and another domain element (e.g. another
    MolecularActivity) with evidence and provenance attached
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF.Statement
    class_class_curie: ClassVar[str] = "rdf:Statement"
    class_name: ClassVar[str] = "association"
    class_model_uri: ClassVar[URIRef] = GOCAM.Association

    object: Union[str, ElementId] = None
    has_evidence: Optional[Union[dict, "Evidence"]] = None
    subject: Optional[Union[str, DomainElementId]] = None
    predicate: Optional[Union[str, PredicateType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ElementId):
            self.object = ElementId(self.object)

        if self.has_evidence is not None and not isinstance(self.has_evidence, Evidence):
            self.has_evidence = Evidence(self.has_evidence)

        if self.subject is not None and not isinstance(self.subject, DomainElementId):
            self.subject = DomainElementId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class OccursInAssociation(Association):
    """
    An association owned by a MA or BP that connect to an AE object in which the activity/process is carried out
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.OccursInAssociation
    class_class_curie: ClassVar[str] = "gocam:OccursInAssociation"
    class_name: ClassVar[str] = "occurs in association"
    class_model_uri: ClassVar[URIRef] = GOCAM.OccursInAssociation

    object: Union[str, AnatomicalEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class CausalAssociation(Association):
    """
    An association owned by an upstream MA or BP that connects to a downstream MA or BP. The nature of the causal
    relationship is indicated with the predicate.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.CausalAssociation
    class_class_curie: ClassVar[str] = "gocam:CausalAssociation"
    class_name: ClassVar[str] = "causal association"
    class_model_uri: ClassVar[URIRef] = GOCAM.CausalAssociation

    object: Union[str, ActivityOrProcessId] = None
    predicate: Optional[Union[str, PredicateType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ActivityOrProcessId):
            self.object = ActivityOrProcessId(self.object)

        if self.predicate is not None and not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class HasPartAssociation(Association):
    """
    General grouping for associations that Link an entity to its parts by a HasPartAssociation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.HasPartAssociation
    class_class_curie: ClassVar[str] = "gocam:HasPartAssociation"
    class_name: ClassVar[str] = "has part association"
    class_model_uri: ClassVar[URIRef] = GOCAM.HasPartAssociation

    object: Union[str, ElementId] = None

@dataclass
class MacromoleculeHasPartAssociation(HasPartAssociation):
    """
    Connects a macromolecule (such as a protein complex) to its parts (gene products or chemical entities)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.MacromoleculeHasPartAssociation
    class_class_curie: ClassVar[str] = "gocam:MacromoleculeHasPartAssociation"
    class_name: ClassVar[str] = "macromolecule has part association"
    class_model_uri: ClassVar[URIRef] = GOCAM.MacromoleculeHasPartAssociation

    object: Union[str, ContinuantId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ContinuantId):
            self.object = ContinuantId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class PartOfAssociation(Association):
    """
    General grouping for associations that Link an entity to its wholes by a PartOfAssociation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.PartOfAssociation
    class_class_curie: ClassVar[str] = "gocam:PartOfAssociation"
    class_name: ClassVar[str] = "part of association"
    class_model_uri: ClassVar[URIRef] = GOCAM.PartOfAssociation

    object: Union[str, ElementId] = None

@dataclass
class AnatomicalPartOfAssociation(PartOfAssociation):
    """
    Connects an anatomical entity (such as a component, cell, or gross anatomical entity) to its parent parts
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.AnatomicalPartOfAssociation
    class_class_curie: ClassVar[str] = "gocam:AnatomicalPartOfAssociation"
    class_name: ClassVar[str] = "anatomical part of association"
    class_model_uri: ClassVar[URIRef] = GOCAM.AnatomicalPartOfAssociation

    object: Union[str, AnatomicalEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ProcessPartOfAssociation(PartOfAssociation):
    """
    Connects a MA or BP to its parent parts
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ProcessPartOfAssociation
    class_class_curie: ClassVar[str] = "gocam:ProcessPartOfAssociation"
    class_name: ClassVar[str] = "process part of association"
    class_model_uri: ClassVar[URIRef] = GOCAM.ProcessPartOfAssociation

    object: Union[str, ActivityOrProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ActivityOrProcessId):
            self.object = ActivityOrProcessId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class EnabledByAssociation(Association):
    """
    Connects an MA to the information biomacromolecule that executes the activity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.EnabledByAssociation
    class_class_curie: ClassVar[str] = "gocam:EnabledByAssociation"
    class_name: ClassVar[str] = "enabled by association"
    class_model_uri: ClassVar[URIRef] = GOCAM.EnabledByAssociation

    object: Union[str, InformationBiomacromoleculeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, InformationBiomacromoleculeId):
            self.object = InformationBiomacromoleculeId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class HappensDuringAssociation(Association):
    """
    Connects an MF to a process or phase in which the process occurs
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.HappensDuringAssociation
    class_class_curie: ClassVar[str] = "gocam:HappensDuringAssociation"
    class_name: ClassVar[str] = "happens during association"
    class_model_uri: ClassVar[URIRef] = GOCAM.HappensDuringAssociation

    object: Union[str, ActivityOrProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ActivityOrProcessId):
            self.object = ActivityOrProcessId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class HasInputAssociation(Association):
    """
    Connects an MF or BP to its input entity, which may be a chemical entity, an information biomacromolecule, or a
    larger structure
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.HasInputAssociation
    class_class_curie: ClassVar[str] = "gocam:HasInputAssociation"
    class_name: ClassVar[str] = "has input association"
    class_model_uri: ClassVar[URIRef] = GOCAM.HasInputAssociation

    object: Union[str, ContinuantId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ContinuantId):
            self.object = ContinuantId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class OntologyClass(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.OntologyClass
    class_class_curie: ClassVar[str] = "gocam:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = GOCAM.OntologyClass

    id: Union[str, OntologyClassId] = None
    category: Union[str, CategoryType] = None
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, CategoryType):
            self.category = CategoryType(self.category)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        super().__post_init__(**kwargs)


@dataclass
class InformationElement(Element):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.InformationElement
    class_class_curie: ClassVar[str] = "gocam:InformationElement"
    class_name: ClassVar[str] = "information element"
    class_model_uri: ClassVar[URIRef] = GOCAM.InformationElement

    id: Union[str, InformationElementId] = None

@dataclass
class Publication(InformationElement):
    """
    A published entity such as a paper in pubmed
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Publication
    class_class_curie: ClassVar[str] = "gocam:Publication"
    class_name: ClassVar[str] = "publication"
    class_model_uri: ClassVar[URIRef] = GOCAM.Publication

    id: Union[str, PublicationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Evidence(InformationElement):
    """
    An instance of a piece of evidence. Evidence attributes such as type, reference, hang off of here
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Evidence
    class_class_curie: ClassVar[str] = "gocam:Evidence"
    class_name: ClassVar[str] = "evidence"
    class_model_uri: ClassVar[URIRef] = GOCAM.Evidence

    id: Union[str, EvidenceId] = None
    evidence_type: Union[str, OntologyClassId] = None
    contributor: Optional[Union[str, List[str]]] = empty_list()
    date: Optional[str] = None
    reference: Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]] = empty_list()
    with_object: Optional[Union[Union[str, ElementId], List[Union[str, ElementId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvidenceId):
            self.id = EvidenceId(self.id)

        if self._is_empty(self.evidence_type):
            self.MissingRequiredField("evidence_type")
        if not isinstance(self.evidence_type, OntologyClassId):
            self.evidence_type = OntologyClassId(self.evidence_type)

        if not isinstance(self.contributor, list):
            self.contributor = [self.contributor] if self.contributor is not None else []
        self.contributor = [v if isinstance(v, str) else str(v) for v in self.contributor]

        if self.date is not None and not isinstance(self.date, str):
            self.date = str(self.date)

        if not isinstance(self.reference, list):
            self.reference = [self.reference] if self.reference is not None else []
        self.reference = [v if isinstance(v, PublicationId) else PublicationId(v) for v in self.reference]

        if not isinstance(self.with_object, list):
            self.with_object = [self.with_object] if self.with_object is not None else []
        self.with_object = [v if isinstance(v, ElementId) else ElementId(v) for v in self.with_object]

        super().__post_init__(**kwargs)


@dataclass
class DomainElementMixin(YAMLRoot):
    """
    Grouping for mixins that apply to GO-CAM elements. These mixins allow us to group together elements that are alike
    in some fashion
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.DomainElementMixin
    class_class_curie: ClassVar[str] = "gocam:DomainElementMixin"
    class_name: ClassVar[str] = "domain element mixin"
    class_model_uri: ClassVar[URIRef] = GOCAM.DomainElementMixin

    id: Union[str, DomainElementMixinId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DomainElementMixinId):
            self.id = DomainElementMixinId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ActivityOrProcess(DomainElementMixin):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ActivityOrProcess
    class_class_curie: ClassVar[str] = "gocam:ActivityOrProcess"
    class_name: ClassVar[str] = "activity or process"
    class_model_uri: ClassVar[URIRef] = GOCAM.ActivityOrProcess

    id: Union[str, ActivityOrProcessId] = None

@dataclass
class ProcessOrPhase(DomainElementMixin):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ProcessOrPhase
    class_class_curie: ClassVar[str] = "gocam:ProcessOrPhase"
    class_name: ClassVar[str] = "process or phase"
    class_model_uri: ClassVar[URIRef] = GOCAM.ProcessOrPhase

    id: Union[str, ProcessOrPhaseId] = None

@dataclass
class Continuant(DomainElementMixin):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Continuant
    class_class_curie: ClassVar[str] = "gocam:Continuant"
    class_name: ClassVar[str] = "continuant"
    class_model_uri: ClassVar[URIRef] = GOCAM.Continuant

    id: Union[str, ContinuantId] = None

# Enumerations
class ModelStateEnum(EnumDefinitionImpl):

    production = PermissibleValue(text="production")
    development = PermissibleValue(text="development")

    _defn = EnumDefinition(
        name="ModelStateEnum",
    )

class AnatomicalEntityCategory(EnumDefinitionImpl):

    CellularAnatomicalEntity = PermissibleValue(text="CellularAnatomicalEntity")
    Cell = PermissibleValue(text="Cell")
    GrossAnatomicalStructure = PermissibleValue(text="GrossAnatomicalStructure")
    Organism = PermissibleValue(text="Organism")

    _defn = EnumDefinition(
        name="AnatomicalEntityCategory",
    )

class InformationBiomacromoleculeCategory(EnumDefinitionImpl):

    GeneOrReferenceProtein = PermissibleValue(text="GeneOrReferenceProtein",
                                                                   meaning=GOCAM["biolink.GeneOrGeneProduct"])
    ProteinIsoform = PermissibleValue(text="ProteinIsoform")
    MacromolecularComplex = PermissibleValue(text="MacromolecularComplex")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="InformationBiomacromoleculeCategory",
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

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=GOCAM.type, domain=None, range=Union[str, OntologyClassId])

slots.category = Slot(uri=GOCAM.category, name="category", curie=GOCAM.curie('category'),
                   model_uri=GOCAM.category, domain=None, range=Union[str, CategoryType])

slots.with_object = Slot(uri=LEGO.evidence, name="with object", curie=LEGO.curie('evidence'),
                   model_uri=GOCAM.with_object, domain=None, range=Optional[Union[Union[str, ElementId], List[Union[str, ElementId]]]])

slots.reference = Slot(uri=DCE.source, name="reference", curie=DCE.curie('source'),
                   model_uri=GOCAM.reference, domain=None, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.provided_by = Slot(uri=PAV.providedBy, name="provided by", curie=PAV.curie('providedBy'),
                   model_uri=GOCAM.provided_by, domain=None, range=Optional[str])

slots.contributor = Slot(uri=DCE.contributor, name="contributor", curie=DCE.curie('contributor'),
                   model_uri=GOCAM.contributor, domain=None, range=Optional[Union[str, List[str]]])

slots.date = Slot(uri=DCE.date, name="date", curie=DCE.curie('date'),
                   model_uri=GOCAM.date, domain=None, range=Optional[str])

slots.evidence_type = Slot(uri=GOCAM.evidence_type, name="evidence type", curie=GOCAM.curie('evidence_type'),
                   model_uri=GOCAM.evidence_type, domain=None, range=Union[str, OntologyClassId],
                   pattern=re.compile(r'^ECO:\d+$'))

slots.type_inferences = Slot(uri=GOCAM.type_inferences, name="type inferences", curie=GOCAM.curie('type_inferences'),
                   model_uri=GOCAM.type_inferences, domain=None, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.related_to = Slot(uri=GOCAM.related_to, name="related to", curie=GOCAM.curie('related_to'),
                   model_uri=GOCAM.related_to, domain=None, range=Optional[Union[dict, Association]])

slots.occurs_in = Slot(uri=GOCAM.occurs_in, name="occurs in", curie=GOCAM.curie('occurs_in'),
                   model_uri=GOCAM.occurs_in, domain=None, range=Optional[Union[dict, OccursInAssociation]])

slots.influences = Slot(uri=GOCAM.influences, name="influences", curie=GOCAM.curie('influences'),
                   model_uri=GOCAM.influences, domain=None, range=Optional[Union[dict, CausalAssociation]])

slots.happens_during = Slot(uri=GOCAM.happens_during, name="happens during", curie=GOCAM.curie('happens_during'),
                   model_uri=GOCAM.happens_during, domain=None, range=Optional[Union[dict, HappensDuringAssociation]])

slots.part_of = Slot(uri=GOCAM.part_of, name="part of", curie=GOCAM.curie('part_of'),
                   model_uri=GOCAM.part_of, domain=None, range=Optional[Union[dict, PartOfAssociation]])

slots.has_part = Slot(uri=GOCAM.has_part, name="has part", curie=GOCAM.curie('has_part'),
                   model_uri=GOCAM.has_part, domain=None, range=Optional[Union[dict, HasPartAssociation]])

slots.enabled_by = Slot(uri=GOCAM.enabled_by, name="enabled by", curie=GOCAM.curie('enabled_by'),
                   model_uri=GOCAM.enabled_by, domain=MolecularActivity, range=Optional[Union[dict, "EnabledByAssociation"]])

slots.has_input = Slot(uri=GOCAM.has_input, name="has input", curie=GOCAM.curie('has_input'),
                   model_uri=GOCAM.has_input, domain=None, range=Optional[Union[dict, HasInputAssociation]])

slots.has_evidence = Slot(uri=GOCAM.has_evidence, name="has evidence", curie=GOCAM.curie('has_evidence'),
                   model_uri=GOCAM.has_evidence, domain=Association, range=Optional[Union[dict, "Evidence"]])

slots.association_slot = Slot(uri=GOCAM.association_slot, name="association slot", curie=GOCAM.curie('association_slot'),
                   model_uri=GOCAM.association_slot, domain=Association, range=Optional[str])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=GOCAM.subject, domain=Association, range=Optional[Union[str, DomainElementId]])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=GOCAM.object, domain=Association, range=Union[str, ElementId])

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=GOCAM.predicate, domain=Association, range=Optional[Union[str, PredicateType]])

slots.model_property = Slot(uri=GOCAM.model_property, name="model property", curie=GOCAM.curie('model_property'),
                   model_uri=GOCAM.model_property, domain=None, range=Optional[str])

slots.title = Slot(uri=DCE.title, name="title", curie=DCE.curie('title'),
                   model_uri=GOCAM.title, domain=None, range=Optional[str])

slots.state = Slot(uri=LEGO.modelstate, name="state", curie=LEGO.curie('modelstate'),
                   model_uri=GOCAM.state, domain=None, range=Optional[Union[str, "ModelStateEnum"]])

slots.domain_element_set = Slot(uri=GOCAM.domain_element_set, name="domain element set", curie=GOCAM.curie('domain_element_set'),
                   model_uri=GOCAM.domain_element_set, domain=None, range=Optional[Union[Dict[Union[str, DomainElementId], Union[dict, DomainElement]], List[Union[dict, DomainElement]]]])

slots.molecular_activity_set = Slot(uri=GOCAM.molecular_activity_set, name="molecular activity set", curie=GOCAM.curie('molecular_activity_set'),
                   model_uri=GOCAM.molecular_activity_set, domain=None, range=Optional[Union[Dict[Union[str, MolecularActivityId], Union[dict, MolecularActivity]], List[Union[dict, MolecularActivity]]]])

slots.biological_process_set = Slot(uri=GOCAM.biological_process_set, name="biological process set", curie=GOCAM.curie('biological_process_set'),
                   model_uri=GOCAM.biological_process_set, domain=None, range=Optional[Union[Dict[Union[str, BiologicalProcessId], Union[dict, BiologicalProcess]], List[Union[dict, BiologicalProcess]]]])

slots.information_biomacromolecule_set = Slot(uri=GOCAM.information_biomacromolecule_set, name="information biomacromolecule set", curie=GOCAM.curie('information_biomacromolecule_set'),
                   model_uri=GOCAM.information_biomacromolecule_set, domain=None, range=Optional[Union[Dict[Union[str, InformationBiomacromoleculeId], Union[dict, InformationBiomacromolecule]], List[Union[dict, InformationBiomacromolecule]]]])

slots.chemical_entity_set = Slot(uri=GOCAM.chemical_entity_set, name="chemical entity set", curie=GOCAM.curie('chemical_entity_set'),
                   model_uri=GOCAM.chemical_entity_set, domain=None, range=Optional[Union[Dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], List[Union[dict, ChemicalEntity]]]])

slots.ontology_class_set = Slot(uri=GOCAM.ontology_class_set, name="ontology class set", curie=GOCAM.curie('ontology_class_set'),
                   model_uri=GOCAM.ontology_class_set, domain=None, range=Optional[Union[Dict[Union[str, OntologyClassId], Union[dict, OntologyClass]], List[Union[dict, OntologyClass]]]])

slots.molecular_activity_part_of = Slot(uri=GOCAM.part_of, name="molecular activity_part of", curie=GOCAM.curie('part_of'),
                   model_uri=GOCAM.molecular_activity_part_of, domain=MolecularActivity, range=Optional[Union[dict, "ProcessPartOfAssociation"]])

slots.anatomical_entity_category = Slot(uri=GOCAM.category, name="anatomical entity_category", curie=GOCAM.curie('category'),
                   model_uri=GOCAM.anatomical_entity_category, domain=AnatomicalEntity, range=Union[str, "AnatomicalEntityCategory"])

slots.anatomical_entity_part_of = Slot(uri=GOCAM.part_of, name="anatomical entity_part of", curie=GOCAM.curie('part_of'),
                   model_uri=GOCAM.anatomical_entity_part_of, domain=AnatomicalEntity, range=Optional[Union[dict, "AnatomicalPartOfAssociation"]])

slots.information_biomacromolecule_category = Slot(uri=GOCAM.category, name="information biomacromolecule_category", curie=GOCAM.curie('category'),
                   model_uri=GOCAM.information_biomacromolecule_category, domain=InformationBiomacromolecule, range=Union[str, "InformationBiomacromoleculeCategory"])

slots.information_biomacromolecule_has_part = Slot(uri=GOCAM.has_part, name="information biomacromolecule_has part", curie=GOCAM.curie('has_part'),
                   model_uri=GOCAM.information_biomacromolecule_has_part, domain=InformationBiomacromolecule, range=Optional[Union[dict, "MacromoleculeHasPartAssociation"]])

slots.occurs_in_association_object = Slot(uri=GOCAM.object, name="occurs in association_object", curie=GOCAM.curie('object'),
                   model_uri=GOCAM.occurs_in_association_object, domain=OccursInAssociation, range=Union[str, AnatomicalEntityId])

slots.causal_association_object = Slot(uri=GOCAM.object, name="causal association_object", curie=GOCAM.curie('object'),
                   model_uri=GOCAM.causal_association_object, domain=CausalAssociation, range=Union[str, ActivityOrProcessId])

slots.causal_association_predicate = Slot(uri=GOCAM.predicate, name="causal association_predicate", curie=GOCAM.curie('predicate'),
                   model_uri=GOCAM.causal_association_predicate, domain=CausalAssociation, range=Optional[Union[str, PredicateType]])

slots.macromolecule_has_part_association_object = Slot(uri=GOCAM.object, name="macromolecule has part association_object", curie=GOCAM.curie('object'),
                   model_uri=GOCAM.macromolecule_has_part_association_object, domain=MacromoleculeHasPartAssociation, range=Union[str, ContinuantId])

slots.anatomical_part_of_association_object = Slot(uri=GOCAM.object, name="anatomical part of association_object", curie=GOCAM.curie('object'),
                   model_uri=GOCAM.anatomical_part_of_association_object, domain=AnatomicalPartOfAssociation, range=Union[str, AnatomicalEntityId])

slots.process_part_of_association_object = Slot(uri=GOCAM.object, name="process part of association_object", curie=GOCAM.curie('object'),
                   model_uri=GOCAM.process_part_of_association_object, domain=ProcessPartOfAssociation, range=Union[str, ActivityOrProcessId])

slots.enabled_by_association_object = Slot(uri=GOCAM.object, name="enabled by association_object", curie=GOCAM.curie('object'),
                   model_uri=GOCAM.enabled_by_association_object, domain=EnabledByAssociation, range=Union[str, InformationBiomacromoleculeId])

slots.happens_during_association_object = Slot(uri=GOCAM.object, name="happens during association_object", curie=GOCAM.curie('object'),
                   model_uri=GOCAM.happens_during_association_object, domain=HappensDuringAssociation, range=Union[str, ActivityOrProcessId])

slots.has_input_association_object = Slot(uri=GOCAM.object, name="has input association_object", curie=GOCAM.curie('object'),
                   model_uri=GOCAM.has_input_association_object, domain=HasInputAssociation, range=Union[str, ContinuantId])
