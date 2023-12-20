

CREATE TABLE "Annotations" (
	annotation_overview TEXT NOT NULL, 
	annotation_method TEXT NOT NULL, 
	annotation_criteria TEXT, 
	annotation_coverage TEXT, 
	annotation_confidence_level TEXT, 
	authors TEXT, 
	file_metadata TEXT, 
	PRIMARY KEY (annotation_overview, annotation_method, annotation_criteria, annotation_coverage, annotation_confidence_level, authors, file_metadata)
);

CREATE TABLE "Author" (
	author_first_name TEXT NOT NULL, 
	author_last_name TEXT NOT NULL, 
	email TEXT, 
	orcid_id TEXT, 
	role TEXT, 
	organisation TEXT, 
	PRIMARY KEY (author_first_name, author_last_name, email, orcid_id, role, organisation)
);

CREATE TABLE "FileLevelMetadata" (
	annotation_id TEXT NOT NULL, 
	source_image_id TEXT NOT NULL, 
	transformations TEXT, 
	spatial_information TEXT, 
	annotation_creation_time DATETIME, 
	PRIMARY KEY (annotation_id)
);

CREATE TABLE "GrantReference" (
	grant_id TEXT NOT NULL, 
	funder TEXT NOT NULL, 
	PRIMARY KEY (grant_id)
);

CREATE TABLE "OrganisationInfo" (
	organisation_name TEXT NOT NULL, 
	address TEXT, 
	ror_id TEXT, 
	PRIMARY KEY (organisation_name, address, ror_id)
);

CREATE TABLE "Publications" (
	publication_title TEXT NOT NULL, 
	publication_authors TEXT NOT NULL, 
	publication_doi TEXT NOT NULL, 
	publication_year TEXT, 
	pubmed_id TEXT, 
	PRIMARY KEY (publication_doi)
);

CREATE TABLE "Study" (
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	keywords TEXT NOT NULL, 
	license VARCHAR(5) NOT NULL, 
	ai_models_trained TEXT, 
	acknowledgements TEXT, 
	funding_statement TEXT NOT NULL, 
	publications TEXT, 
	authors TEXT, 
	link_url TEXT NOT NULL, 
	link_description TEXT, 
	grants TEXT, 
	PRIMARY KEY (title, description, keywords, license, ai_models_trained, acknowledgements, funding_statement, publications, authors, link_url, link_description, grants)
);

CREATE TABLE "Version" (
	version TEXT NOT NULL, 
	timestamp DATETIME NOT NULL, 
	changes TEXT, 
	previous_version TEXT, 
	PRIMARY KEY (version, timestamp, changes, previous_version)
);

CREATE TABLE "FileLevelMetadata_annotation_type" (
	backref_id TEXT, 
	annotation_type VARCHAR(23) NOT NULL, 
	PRIMARY KEY (backref_id, annotation_type), 
	FOREIGN KEY(backref_id) REFERENCES "FileLevelMetadata" (annotation_id)
);
