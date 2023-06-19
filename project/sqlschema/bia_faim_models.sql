

CREATE TABLE "Annotations" (
	annotation_overview TEXT NOT NULL, 
	annotation_type VARCHAR(17) NOT NULL, 
	annotation_method TEXT NOT NULL, 
	annotation_criteria TEXT, 
	annotation_coverage TEXT, 
	source_image TEXT, 
	annotation_confidence_level TEXT, 
	spatial_information TEXT, 
	transformatons TEXT, 
	authors TEXT, 
	PRIMARY KEY (annotation_overview, annotation_type, annotation_method, annotation_criteria, annotation_coverage, source_image, annotation_confidence_level, spatial_information, transformatons, authors)
);

CREATE TABLE "Author" (
	author_first_name TEXT NOT NULL, 
	author_last_name TEXT NOT NULL, 
	email TEXT, 
	orcid_id TEXT NOT NULL, 
	PRIMARY KEY (orcid_id)
);

CREATE TABLE "FundingStatement" (
	funding_statement TEXT NOT NULL, 
	PRIMARY KEY (funding_statement)
);

CREATE TABLE "GrantReference" (
	grant_id TEXT NOT NULL, 
	funder TEXT NOT NULL, 
	PRIMARY KEY (grant_id)
);

CREATE TABLE "GrantReferenceCollection" (
	grants TEXT, 
	PRIMARY KEY (grants)
);

CREATE TABLE "OrganisationInfo" (
	organisation_name TEXT NOT NULL, 
	address TEXT, 
	PRIMARY KEY (organisation_name, address)
);

CREATE TABLE "OrganisationInfoCollection" (
	organisation TEXT, 
	PRIMARY KEY (organisation)
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
	funding TEXT NOT NULL, 
	publications TEXT, 
	authors TEXT, 
	link_url TEXT NOT NULL, 
	link_description TEXT, 
	PRIMARY KEY (title, description, keywords, license, ai_models_trained, acknowledgements, funding, publications, authors, link_url, link_description)
);

CREATE TABLE "Version" (
	version FLOAT NOT NULL, 
	timestamp DATETIME NOT NULL, 
	changes TEXT NOT NULL, 
	previous_version TEXT NOT NULL, 
	PRIMARY KEY (version, timestamp, changes, previous_version)
);

CREATE TABLE "OrganisationURL_ror_id" (
	backref_id TEXT, 
	ror_id TEXT NOT NULL, 
	PRIMARY KEY (ror_id), 
	FOREIGN KEY(backref_id) REFERENCES "OrganisationURL_ror_id" (ror_id)
);

CREATE TABLE "Author_affiliation" (
	backref_id TEXT, 
	affiliation TEXT NOT NULL, 
	PRIMARY KEY (backref_id, affiliation), 
	FOREIGN KEY(backref_id) REFERENCES "Author" (orcid_id)
);

CREATE TABLE "Author_role" (
	backref_id TEXT, 
	role TEXT NOT NULL, 
	PRIMARY KEY (backref_id, role), 
	FOREIGN KEY(backref_id) REFERENCES "Author" (orcid_id)
);
