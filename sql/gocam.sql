
CREATE TABLE "ActivityOrProcess" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Continuant" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "DomainElementMixin" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Element" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "InformationElement" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "OntologyClass" (
	id TEXT NOT NULL, 
	name TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "ProcessOrPhase" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Publication" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "AnatomicalEntity" (
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	type_inferences TEXT, 
	part_of TEXT, 
	category VARCHAR(24) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type) REFERENCES "OntologyClass" (id), 
	FOREIGN KEY(type_inferences) REFERENCES "OntologyClass" (id)
);

CREATE TABLE "BiologicalProcess" (
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	type_inferences TEXT, 
	occurs_in TEXT, 
	influences TEXT, 
	happens_during TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type) REFERENCES "OntologyClass" (id), 
	FOREIGN KEY(type_inferences) REFERENCES "OntologyClass" (id)
);

CREATE TABLE "ChemicalEntity" (
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	type_inferences TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type) REFERENCES "OntologyClass" (id), 
	FOREIGN KEY(type_inferences) REFERENCES "OntologyClass" (id)
);

CREATE TABLE "DomainElement" (
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	type_inferences TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type) REFERENCES "OntologyClass" (id), 
	FOREIGN KEY(type_inferences) REFERENCES "OntologyClass" (id)
);

CREATE TABLE "Evidence" (
	id TEXT NOT NULL, 
	contributor TEXT, 
	date TEXT, 
	evidence_type TEXT NOT NULL, 
	reference TEXT, 
	with_object TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(evidence_type) REFERENCES "OntologyClass" (id), 
	FOREIGN KEY(reference) REFERENCES "Publication" (id), 
	FOREIGN KEY(with_object) REFERENCES "Element" (id)
);

CREATE TABLE "InformationBiomacromolecule" (
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	type_inferences TEXT, 
	has_part TEXT, 
	category VARCHAR(22) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type) REFERENCES "OntologyClass" (id), 
	FOREIGN KEY(type_inferences) REFERENCES "OntologyClass" (id)
);

CREATE TABLE "MolecularActivity" (
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	type_inferences TEXT, 
	influences TEXT, 
	happens_during TEXT, 
	part_of TEXT, 
	enabled_by TEXT, 
	has_input TEXT, 
	occurs_in TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type) REFERENCES "OntologyClass" (id), 
	FOREIGN KEY(type_inferences) REFERENCES "OntologyClass" (id)
);

CREATE TABLE "AnatomicalEntity_to_type_inferences" (
	type_inferences TEXT NOT NULL, 
	"ref_AnatomicalEntity" TEXT NOT NULL, 
	FOREIGN KEY("ref_AnatomicalEntity") REFERENCES "AnatomicalEntity" (id)
);

CREATE TABLE "AnatomicalPartOfAssociation" (
	has_evidence TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT NOT NULL, 
	FOREIGN KEY(has_evidence) REFERENCES "Evidence" (id), 
	FOREIGN KEY(subject) REFERENCES "DomainElement" (id), 
	FOREIGN KEY(object) REFERENCES "AnatomicalEntity" (id)
);

CREATE TABLE "Association" (
	has_evidence TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT NOT NULL, 
	FOREIGN KEY(has_evidence) REFERENCES "Evidence" (id), 
	FOREIGN KEY(subject) REFERENCES "DomainElement" (id), 
	FOREIGN KEY(object) REFERENCES "Element" (id)
);

CREATE TABLE "BiologicalProcess_to_type_inferences" (
	type_inferences TEXT NOT NULL, 
	"ref_BiologicalProcess" TEXT NOT NULL, 
	FOREIGN KEY("ref_BiologicalProcess") REFERENCES "BiologicalProcess" (id)
);

CREATE TABLE "CausalAssociation" (
	has_evidence TEXT, 
	subject TEXT, 
	object TEXT NOT NULL, 
	predicate TEXT, 
	FOREIGN KEY(has_evidence) REFERENCES "Evidence" (id), 
	FOREIGN KEY(subject) REFERENCES "DomainElement" (id), 
	FOREIGN KEY(object) REFERENCES "ActivityOrProcess" (id)
);

CREATE TABLE "ChemicalEntity_to_type_inferences" (
	type_inferences TEXT NOT NULL, 
	"ref_ChemicalEntity" TEXT NOT NULL, 
	FOREIGN KEY("ref_ChemicalEntity") REFERENCES "ChemicalEntity" (id)
);

CREATE TABLE "DomainElement_to_type_inferences" (
	type_inferences TEXT NOT NULL, 
	"ref_DomainElement" TEXT NOT NULL, 
	FOREIGN KEY("ref_DomainElement") REFERENCES "DomainElement" (id)
);

CREATE TABLE "EnabledByAssociation" (
	has_evidence TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT NOT NULL, 
	FOREIGN KEY(has_evidence) REFERENCES "Evidence" (id), 
	FOREIGN KEY(subject) REFERENCES "DomainElement" (id), 
	FOREIGN KEY(object) REFERENCES "InformationBiomacromolecule" (id)
);

CREATE TABLE "Evidence_to_contributor" (
	contributor TEXT NOT NULL, 
	"ref_Evidence" TEXT NOT NULL, 
	FOREIGN KEY("ref_Evidence") REFERENCES "Evidence" (id)
);

CREATE TABLE "Evidence_to_reference" (
	reference TEXT NOT NULL, 
	"ref_Evidence" TEXT NOT NULL, 
	FOREIGN KEY("ref_Evidence") REFERENCES "Evidence" (id)
);

CREATE TABLE "Evidence_to_with_object" (
	with_object TEXT NOT NULL, 
	"ref_Evidence" TEXT NOT NULL, 
	FOREIGN KEY("ref_Evidence") REFERENCES "Evidence" (id)
);

CREATE TABLE "HappensDuringAssociation" (
	has_evidence TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT NOT NULL, 
	FOREIGN KEY(has_evidence) REFERENCES "Evidence" (id), 
	FOREIGN KEY(subject) REFERENCES "DomainElement" (id), 
	FOREIGN KEY(object) REFERENCES "ActivityOrProcess" (id)
);

CREATE TABLE "HasInputAssociation" (
	has_evidence TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT NOT NULL, 
	FOREIGN KEY(has_evidence) REFERENCES "Evidence" (id), 
	FOREIGN KEY(subject) REFERENCES "DomainElement" (id), 
	FOREIGN KEY(object) REFERENCES "Continuant" (id)
);

CREATE TABLE "HasPartAssociation" (
	has_evidence TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT NOT NULL, 
	FOREIGN KEY(has_evidence) REFERENCES "Evidence" (id), 
	FOREIGN KEY(subject) REFERENCES "DomainElement" (id), 
	FOREIGN KEY(object) REFERENCES "Element" (id)
);

CREATE TABLE "InformationBiomacromolecule_to_type_inferences" (
	type_inferences TEXT NOT NULL, 
	"ref_InformationBiomacromolecule" TEXT NOT NULL, 
	FOREIGN KEY("ref_InformationBiomacromolecule") REFERENCES "InformationBiomacromolecule" (id)
);

CREATE TABLE "MacromoleculeHasPartAssociation" (
	has_evidence TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT NOT NULL, 
	FOREIGN KEY(has_evidence) REFERENCES "Evidence" (id), 
	FOREIGN KEY(subject) REFERENCES "DomainElement" (id), 
	FOREIGN KEY(object) REFERENCES "Continuant" (id)
);

CREATE TABLE "Model" (
	id TEXT NOT NULL, 
	title TEXT, 
	contributor TEXT, 
	date TEXT, 
	state VARCHAR(11), 
	provided_by TEXT, 
	molecular_activity_set TEXT, 
	biological_process_set TEXT, 
	information_biomacromolecule_set TEXT, 
	chemical_entity_set TEXT, 
	ontology_class_set TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(molecular_activity_set) REFERENCES "MolecularActivity" (id), 
	FOREIGN KEY(biological_process_set) REFERENCES "BiologicalProcess" (id), 
	FOREIGN KEY(information_biomacromolecule_set) REFERENCES "InformationBiomacromolecule" (id), 
	FOREIGN KEY(chemical_entity_set) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY(ontology_class_set) REFERENCES "OntologyClass" (id)
);

CREATE TABLE "MolecularActivity_to_type_inferences" (
	type_inferences TEXT NOT NULL, 
	"ref_MolecularActivity" TEXT NOT NULL, 
	FOREIGN KEY("ref_MolecularActivity") REFERENCES "MolecularActivity" (id)
);

CREATE TABLE "OccursInAssociation" (
	has_evidence TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT NOT NULL, 
	FOREIGN KEY(has_evidence) REFERENCES "Evidence" (id), 
	FOREIGN KEY(subject) REFERENCES "DomainElement" (id), 
	FOREIGN KEY(object) REFERENCES "AnatomicalEntity" (id)
);

CREATE TABLE "PartOfAssociation" (
	has_evidence TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT NOT NULL, 
	FOREIGN KEY(has_evidence) REFERENCES "Evidence" (id), 
	FOREIGN KEY(subject) REFERENCES "DomainElement" (id), 
	FOREIGN KEY(object) REFERENCES "Element" (id)
);

CREATE TABLE "ProcessPartOfAssociation" (
	has_evidence TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT NOT NULL, 
	FOREIGN KEY(has_evidence) REFERENCES "Evidence" (id), 
	FOREIGN KEY(subject) REFERENCES "DomainElement" (id), 
	FOREIGN KEY(object) REFERENCES "ActivityOrProcess" (id)
);

CREATE TABLE "Model_to_contributor" (
	contributor TEXT NOT NULL, 
	"ref_Model" TEXT NOT NULL, 
	FOREIGN KEY("ref_Model") REFERENCES "Model" (id)
);

CREATE TABLE "Model_to_molecular_activity_set" (
	molecular_activity_set TEXT NOT NULL, 
	"ref_Model" TEXT NOT NULL, 
	FOREIGN KEY("ref_Model") REFERENCES "Model" (id)
);

CREATE TABLE "Model_to_biological_process_set" (
	biological_process_set TEXT NOT NULL, 
	"ref_Model" TEXT NOT NULL, 
	FOREIGN KEY("ref_Model") REFERENCES "Model" (id)
);

CREATE TABLE "Model_to_information_biomacromolecule_set" (
	information_biomacromolecule_set TEXT NOT NULL, 
	"ref_Model" TEXT NOT NULL, 
	FOREIGN KEY("ref_Model") REFERENCES "Model" (id)
);

CREATE TABLE "Model_to_chemical_entity_set" (
	chemical_entity_set TEXT NOT NULL, 
	"ref_Model" TEXT NOT NULL, 
	FOREIGN KEY("ref_Model") REFERENCES "Model" (id)
);

CREATE TABLE "Model_to_ontology_class_set" (
	ontology_class_set TEXT NOT NULL, 
	"ref_Model" TEXT NOT NULL, 
	FOREIGN KEY("ref_Model") REFERENCES "Model" (id)
);

