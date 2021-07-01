
from dataclasses import dataclass
from dataclasses import field
from typing import List

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import Text
from sqlalchemy import Integer
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship

mapper_registry = registry()
metadata = MetaData()

from gocam import *


tbl_activity_to_activity_causal_association = Table('activity_to_activity_causal_association', metadata, 
    Column('has_evidence', Text, ForeignKey('evidence.id'), primary_key=True),
    Column('predicate', Text, primary_key=True),
    Column('subject', Text, ForeignKey('molecular_activity.id'), primary_key=True),
    Column('object', Text, ForeignKey('molecular_activity.id'), primary_key=True),
)
tbl_activity_to_process_causal_association = Table('activity_to_process_causal_association', metadata, 
    Column('has_evidence', Text, ForeignKey('evidence.id'), primary_key=True),
    Column('predicate', Text, primary_key=True),
    Column('subject', Text, ForeignKey('molecular_activity.id'), primary_key=True),
    Column('object', Text, ForeignKey('biological_process.id'), primary_key=True),
)
tbl_anatomical_entity = Table('anatomical_entity', metadata, 
    Column('id', Text, primary_key=True),
    Column('type', Text, ForeignKey('ontology_class.id')),
    Column('type_inferences', Text),
    Column('part_of', Text),
    Column('category', Text),
)
tbl_anatomical_part_of_association = Table('anatomical_part_of_association', metadata, 
    Column('has_evidence', Text, ForeignKey('evidence.id'), primary_key=True),
    Column('subject', Text, primary_key=True),
    Column('predicate', Text, primary_key=True),
    Column('object', Text, ForeignKey('anatomical_entity.id'), primary_key=True),
)
tbl_biological_process = Table('biological_process', metadata, 
    Column('id', Text, primary_key=True),
    Column('type', Text, ForeignKey('ontology_class.id')),
    Column('type_inferences', Text),
    Column('occurs_in', Text),
    Column('has_activity_causal_associations', Text),
    Column('has_process_causal_associations', Text),
    Column('happens_during', Text),
)
tbl_chemical_entity = Table('chemical_entity', metadata, 
    Column('id', Text, primary_key=True),
    Column('type', Text, ForeignKey('ontology_class.id')),
    Column('type_inferences', Text),
    Column('model_id', Text, ForeignKey('model.id')),
)
tbl_enabled_by_association = Table('enabled_by_association', metadata, 
    Column('has_evidence', Text, ForeignKey('evidence.id'), primary_key=True),
    Column('subject', Text, primary_key=True),
    Column('predicate', Text, primary_key=True),
    Column('object', Text, ForeignKey('information_biomacromolecule.id'), primary_key=True),
)
tbl_evidence = Table('evidence', metadata, 
    Column('id', Text, primary_key=True),
    Column('date', Text),
    Column('evidence_type', Text, ForeignKey('ontology_class.id')),
)
tbl_happens_during_association = Table('happens_during_association', metadata, 
    Column('has_evidence', Text, ForeignKey('evidence.id'), primary_key=True),
    Column('subject', Text, primary_key=True),
    Column('predicate', Text, primary_key=True),
    Column('object', Text, primary_key=True),
)
tbl_has_input_association = Table('has_input_association', metadata, 
    Column('has_evidence', Text, ForeignKey('evidence.id'), primary_key=True),
    Column('subject', Text, primary_key=True),
    Column('predicate', Text, primary_key=True),
    Column('object', Text, primary_key=True),
)
tbl_information_biomacromolecule = Table('information_biomacromolecule', metadata, 
    Column('id', Text, primary_key=True),
    Column('type', Text, ForeignKey('ontology_class.id')),
    Column('type_inferences', Text),
    Column('has_part', Text),
    Column('category', Text),
)
tbl_macromolecule_has_part_association = Table('macromolecule_has_part_association', metadata, 
    Column('has_evidence', Text, ForeignKey('evidence.id'), primary_key=True),
    Column('subject', Text, primary_key=True),
    Column('predicate', Text, primary_key=True),
    Column('object', Text, primary_key=True),
)
tbl_model = Table('model', metadata, 
    Column('id', Text, primary_key=True),
    Column('title', Text),
    Column('date', Text),
    Column('state', Text),
    Column('provided_by', Text),
    Column('molecular_activity_set', Text),
    Column('biological_process_set', Text),
    Column('information_biomacromolecule_set', Text),
    Column('ontology_class_set', Text),
)
tbl_molecular_activity = Table('molecular_activity', metadata, 
    Column('id', Text, primary_key=True),
    Column('type', Text, ForeignKey('ontology_class.id')),
    Column('type_inferences', Text),
    Column('has_activity_causal_associations', Text),
    Column('has_process_causal_associations', Text),
    Column('happens_during', Text),
    Column('part_of', Text),
    Column('enabled_by', Text),
    Column('has_input', Text),
    Column('occurs_in', Text),
)
tbl_occurs_in_association = Table('occurs_in_association', metadata, 
    Column('has_evidence', Text, ForeignKey('evidence.id'), primary_key=True),
    Column('subject', Text, primary_key=True),
    Column('predicate', Text, primary_key=True),
    Column('object', Text, ForeignKey('anatomical_entity.id'), primary_key=True),
)
tbl_ontology_class = Table('ontology_class', metadata, 
    Column('id', Text, primary_key=True),
    Column('name', Text),
    Column('category', Text),
)
tbl_process_part_of_association = Table('process_part_of_association', metadata, 
    Column('has_evidence', Text, ForeignKey('evidence.id'), primary_key=True),
    Column('subject', Text, primary_key=True),
    Column('predicate', Text, primary_key=True),
    Column('object', Text, primary_key=True),
)
tbl_process_to_activity_causal_association = Table('process_to_activity_causal_association', metadata, 
    Column('has_evidence', Text, ForeignKey('evidence.id'), primary_key=True),
    Column('predicate', Text, primary_key=True),
    Column('subject', Text, ForeignKey('biological_process.id'), primary_key=True),
    Column('object', Text, ForeignKey('molecular_activity.id'), primary_key=True),
)
tbl_process_to_process_causal_association = Table('process_to_process_causal_association', metadata, 
    Column('has_evidence', Text, ForeignKey('evidence.id'), primary_key=True),
    Column('predicate', Text, primary_key=True),
    Column('subject', Text, ForeignKey('biological_process.id'), primary_key=True),
    Column('object', Text, ForeignKey('biological_process.id'), primary_key=True),
)
tbl_publication = Table('publication', metadata, 
    Column('id', Text, primary_key=True),
    Column('evidence_id', Text, ForeignKey('evidence.id')),
)
tbl_evidence_contributor = Table('evidence_contributor', metadata, 
    Column('backref_id', Text, ForeignKey('evidence.id'), primary_key=True),
    Column('contributor', Text, primary_key=True),
)
tbl_evidence_with_object = Table('evidence_with_object', metadata, 
    Column('backref_id', Text, ForeignKey('evidence.id'), primary_key=True),
    Column('with_object', Text, primary_key=True),
)
tbl_model_contributor = Table('model_contributor', metadata, 
    Column('backref_id', Text, ForeignKey('model.id'), primary_key=True),
    Column('contributor', Text, primary_key=True),
)
mapper_registry.map_imperatively(ActivityToActivityCausalAssociation, tbl_activity_to_activity_causal_association, properties={
})
mapper_registry.map_imperatively(ActivityToProcessCausalAssociation, tbl_activity_to_process_causal_association, properties={
})
mapper_registry.map_imperatively(AnatomicalEntity, tbl_anatomical_entity, properties={
})
mapper_registry.map_imperatively(AnatomicalPartOfAssociation, tbl_anatomical_part_of_association, properties={
})
mapper_registry.map_imperatively(BiologicalProcess, tbl_biological_process, properties={
})
mapper_registry.map_imperatively(ChemicalEntity, tbl_chemical_entity, properties={
})
mapper_registry.map_imperatively(EnabledByAssociation, tbl_enabled_by_association, properties={
})
mapper_registry.map_imperatively(Evidence, tbl_evidence, properties={

    'reference': 
        relationship(publication, 
                      foreign_keys=tbl_publication.columns["evidence_id"],
                      backref='Evidence'),

})
mapper_registry.map_imperatively(HappensDuringAssociation, tbl_happens_during_association, properties={
})
mapper_registry.map_imperatively(HasInputAssociation, tbl_has_input_association, properties={
})
mapper_registry.map_imperatively(InformationBiomacromolecule, tbl_information_biomacromolecule, properties={
})
mapper_registry.map_imperatively(MacromoleculeHasPartAssociation, tbl_macromolecule_has_part_association, properties={
})
mapper_registry.map_imperatively(Model, tbl_model, properties={

    'chemical_entity_set': 
        relationship(chemical entity, 
                      foreign_keys=tbl_chemical_entity.columns["model_id"],
                      backref='Model'),

})
mapper_registry.map_imperatively(MolecularActivity, tbl_molecular_activity, properties={
})
mapper_registry.map_imperatively(OccursInAssociation, tbl_occurs_in_association, properties={
})
mapper_registry.map_imperatively(OntologyClass, tbl_ontology_class, properties={
})
mapper_registry.map_imperatively(ProcessPartOfAssociation, tbl_process_part_of_association, properties={
})
mapper_registry.map_imperatively(ProcessToActivityCausalAssociation, tbl_process_to_activity_causal_association, properties={
})
mapper_registry.map_imperatively(ProcessToProcessCausalAssociation, tbl_process_to_process_causal_association, properties={
})
mapper_registry.map_imperatively(Publication, tbl_publication, properties={
})
