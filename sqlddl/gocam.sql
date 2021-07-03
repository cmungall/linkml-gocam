

CREATE TABLE model (
	id TEXT NOT NULL, 
	title TEXT, 
	date TEXT, 
	state VARCHAR(11), 
	provided_by TEXT, 
	molecular_activity_set TEXT, 
	biological_process_set TEXT, 
	information_biomacromolecule_set TEXT, 
	ontology_class_set TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE ontology_class (
	id TEXT NOT NULL, 
	name TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE anatomical_entity (
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	type_inferences TEXT, 
	part_of TEXT, 
	category VARCHAR(24) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type) REFERENCES ontology_class (id)
);

CREATE TABLE biological_process (
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	type_inferences TEXT, 
	occurs_in TEXT, 
	happens_during TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type) REFERENCES ontology_class (id)
);

CREATE TABLE chemical_entity (
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	type_inferences TEXT, 
	model_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type) REFERENCES ontology_class (id), 
	FOREIGN KEY(model_id) REFERENCES model (id)
);

CREATE TABLE evidence (
	id TEXT NOT NULL, 
	date TEXT, 
	evidence_type TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(evidence_type) REFERENCES ontology_class (id)
);

CREATE TABLE information_biomacromolecule (
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	type_inferences TEXT, 
	has_part TEXT, 
	category VARCHAR(22) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type) REFERENCES ontology_class (id)
);

CREATE TABLE molecular_activity (
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	type_inferences TEXT, 
	happens_during TEXT, 
	part_of TEXT, 
	enabled_by TEXT, 
	has_input TEXT, 
	occurs_in TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type) REFERENCES ontology_class (id)
);

CREATE TABLE model_contributor (
	backref_id TEXT, 
	contributor TEXT, 
	PRIMARY KEY (backref_id, contributor), 
	FOREIGN KEY(backref_id) REFERENCES model (id)
);

CREATE TABLE activity_to_activity_causal_association (
	has_evidence TEXT, 
	predicate TEXT, 
	subject TEXT, 
	object TEXT NOT NULL, 
	molecular_activity_id TEXT, 
	PRIMARY KEY (has_evidence, predicate, subject, object, molecular_activity_id), 
	FOREIGN KEY(has_evidence) REFERENCES evidence (id), 
	FOREIGN KEY(subject) REFERENCES molecular_activity (id), 
	FOREIGN KEY(object) REFERENCES molecular_activity (id), 
	FOREIGN KEY(molecular_activity_id) REFERENCES molecular_activity (id)
);

CREATE TABLE activity_to_process_causal_association (
	has_evidence TEXT, 
	predicate TEXT, 
	subject TEXT, 
	object TEXT NOT NULL, 
	molecular_activity_id TEXT, 
	PRIMARY KEY (has_evidence, predicate, subject, object, molecular_activity_id), 
	FOREIGN KEY(has_evidence) REFERENCES evidence (id), 
	FOREIGN KEY(subject) REFERENCES molecular_activity (id), 
	FOREIGN KEY(object) REFERENCES biological_process (id), 
	FOREIGN KEY(molecular_activity_id) REFERENCES molecular_activity (id)
);

CREATE TABLE anatomical_part_of_association (
	has_evidence TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY (has_evidence, subject, predicate, object), 
	FOREIGN KEY(has_evidence) REFERENCES evidence (id), 
	FOREIGN KEY(object) REFERENCES anatomical_entity (id)
);

CREATE TABLE enabled_by_association (
	has_evidence TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY (has_evidence, subject, predicate, object), 
	FOREIGN KEY(has_evidence) REFERENCES evidence (id), 
	FOREIGN KEY(object) REFERENCES information_biomacromolecule (id)
);

CREATE TABLE happens_during_association (
	has_evidence TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY (has_evidence, subject, predicate, object), 
	FOREIGN KEY(has_evidence) REFERENCES evidence (id)
);

CREATE TABLE has_input_association (
	has_evidence TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY (has_evidence, subject, predicate, object), 
	FOREIGN KEY(has_evidence) REFERENCES evidence (id)
);

CREATE TABLE macromolecule_has_part_association (
	has_evidence TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY (has_evidence, subject, predicate, object), 
	FOREIGN KEY(has_evidence) REFERENCES evidence (id)
);

CREATE TABLE occurs_in_association (
	has_evidence TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY (has_evidence, subject, predicate, object), 
	FOREIGN KEY(has_evidence) REFERENCES evidence (id), 
	FOREIGN KEY(object) REFERENCES anatomical_entity (id)
);

CREATE TABLE process_part_of_association (
	has_evidence TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY (has_evidence, subject, predicate, object), 
	FOREIGN KEY(has_evidence) REFERENCES evidence (id), 
	FOREIGN KEY(object) REFERENCES biological_process (id)
);

CREATE TABLE process_to_activity_causal_association (
	has_evidence TEXT, 
	predicate TEXT, 
	subject TEXT, 
	object TEXT NOT NULL, 
	biological_process_id TEXT, 
	PRIMARY KEY (has_evidence, predicate, subject, object, biological_process_id), 
	FOREIGN KEY(has_evidence) REFERENCES evidence (id), 
	FOREIGN KEY(subject) REFERENCES biological_process (id), 
	FOREIGN KEY(object) REFERENCES molecular_activity (id), 
	FOREIGN KEY(biological_process_id) REFERENCES biological_process (id)
);

CREATE TABLE process_to_process_causal_association (
	has_evidence TEXT, 
	predicate TEXT, 
	subject TEXT, 
	object TEXT NOT NULL, 
	biological_process_id TEXT, 
	PRIMARY KEY (has_evidence, predicate, subject, object, biological_process_id), 
	FOREIGN KEY(has_evidence) REFERENCES evidence (id), 
	FOREIGN KEY(subject) REFERENCES biological_process (id), 
	FOREIGN KEY(object) REFERENCES biological_process (id), 
	FOREIGN KEY(biological_process_id) REFERENCES biological_process (id)
);

CREATE TABLE publication (
	id TEXT NOT NULL, 
	evidence_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(evidence_id) REFERENCES evidence (id)
);

CREATE TABLE evidence_contributor (
	backref_id TEXT, 
	contributor TEXT, 
	PRIMARY KEY (backref_id, contributor), 
	FOREIGN KEY(backref_id) REFERENCES evidence (id)
);

CREATE TABLE evidence_with_object (
	backref_id TEXT, 
	with_object TEXT, 
	PRIMARY KEY (backref_id, with_object), 
	FOREIGN KEY(backref_id) REFERENCES evidence (id)
);

