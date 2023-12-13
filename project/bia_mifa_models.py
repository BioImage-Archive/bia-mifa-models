# Auto generated from bia_mifa_models.yaml by pythongen.py version: 0.0.1
# Generation date: 2023-12-13T15:06:06
# Schema: bia-mifa-models
#
# id: https://w3id.org/BioImage-Archive/bia-mifa-models
# description: Schemas and models for working with the BioImage Archive's MIFA (Metadata, Incentives, Formats and Accessibility) metadata implementation
# license: CC0

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
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
from linkml_runtime.linkml_model.types import Datetime, Float, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DOI = CurieNamespace('DOI', 'https://doi.org/')
ORCID = CurieNamespace('ORCID', 'https://orcid.org/')
PMID = CurieNamespace('PMID', 'https://pubmed.ncbi.nlm.nih.gov/')
ROR = CurieNamespace('ROR', 'https://ror.org/')
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'https://www.wikidata.org/prop/')
BIA_MIFA_MODELS = CurieNamespace('bia_mifa_models', 'https://w3id.org/BioImage-Archive/bia-mifa-models/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = BIA_MIFA_MODELS


# Types

# Class references
class PublicationsPublicationDoi(URIorCURIE):
    pass


class GrantReferenceGrantId(extended_str):
    pass


class FileLevelMetadataAnnotationId(extended_str):
    pass


@dataclass
class Study(YAMLRoot):
    """
    General information about the study
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIA_MIFA_MODELS["Study"]
    class_class_curie: ClassVar[str] = "bia_mifa_models:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = BIA_MIFA_MODELS.Study

    title: str = None
    description: str = None
    keywords: Union[str, List[str]] = None
    license: Union[str, "LicenseType"] = None
    funding_statement: str = None
    link_url: Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]] = None
    ai_models_trained: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    acknowledgements: Optional[str] = None
    publications: Optional[Union[Dict[Union[str, PublicationsPublicationDoi], Union[dict, "Publications"]], List[Union[dict, "Publications"]]]] = empty_dict()
    authors: Optional[Union[Union[dict, "Author"], List[Union[dict, "Author"]]]] = empty_list()
    link_description: Optional[Union[str, List[str]]] = empty_list()
    grants: Optional[Union[Dict[Union[str, GrantReferenceGrantId], Union[dict, "GrantReference"]], List[Union[dict, "GrantReference"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.keywords):
            self.MissingRequiredField("keywords")
        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        if self._is_empty(self.license):
            self.MissingRequiredField("license")
        if not isinstance(self.license, LicenseType):
            self.license = LicenseType(self.license)

        if self._is_empty(self.funding_statement):
            self.MissingRequiredField("funding_statement")
        if not isinstance(self.funding_statement, str):
            self.funding_statement = str(self.funding_statement)

        if self._is_empty(self.link_url):
            self.MissingRequiredField("link_url")
        if not isinstance(self.link_url, list):
            self.link_url = [self.link_url] if self.link_url is not None else []
        self.link_url = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.link_url]

        if not isinstance(self.ai_models_trained, list):
            self.ai_models_trained = [self.ai_models_trained] if self.ai_models_trained is not None else []
        self.ai_models_trained = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.ai_models_trained]

        if self.acknowledgements is not None and not isinstance(self.acknowledgements, str):
            self.acknowledgements = str(self.acknowledgements)

        self._normalize_inlined_as_dict(slot_name="publications", slot_type=Publications, key_name="publication_doi", keyed=True)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, Author) else Author(**as_dict(v)) for v in self.authors]

        if not isinstance(self.link_description, list):
            self.link_description = [self.link_description] if self.link_description is not None else []
        self.link_description = [v if isinstance(v, str) else str(v) for v in self.link_description]

        self._normalize_inlined_as_list(slot_name="grants", slot_type=GrantReference, key_name="grant_id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Publications(YAMLRoot):
    """
    Information about any publications associated with the dataset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIA_MIFA_MODELS["Publications"]
    class_class_curie: ClassVar[str] = "bia_mifa_models:Publications"
    class_name: ClassVar[str] = "Publications"
    class_model_uri: ClassVar[URIRef] = BIA_MIFA_MODELS.Publications

    publication_doi: Union[str, PublicationsPublicationDoi] = None
    publication_title: str = None
    publication_authors: str = None
    publication_year: Optional[str] = None
    pubmed_id: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.publication_doi):
            self.MissingRequiredField("publication_doi")
        if not isinstance(self.publication_doi, PublicationsPublicationDoi):
            self.publication_doi = PublicationsPublicationDoi(self.publication_doi)

        if self._is_empty(self.publication_title):
            self.MissingRequiredField("publication_title")
        if not isinstance(self.publication_title, str):
            self.publication_title = str(self.publication_title)

        if self._is_empty(self.publication_authors):
            self.MissingRequiredField("publication_authors")
        if not isinstance(self.publication_authors, str):
            self.publication_authors = str(self.publication_authors)

        if self.publication_year is not None and not isinstance(self.publication_year, str):
            self.publication_year = str(self.publication_year)

        if self.pubmed_id is not None and not isinstance(self.pubmed_id, URIorCURIE):
            self.pubmed_id = URIorCURIE(self.pubmed_id)

        super().__post_init__(**kwargs)


@dataclass
class PublicationsCollection(YAMLRoot):
    """
    A holder for Publications objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIA_MIFA_MODELS["PublicationsCollection"]
    class_class_curie: ClassVar[str] = "bia_mifa_models:PublicationsCollection"
    class_name: ClassVar[str] = "PublicationsCollection"
    class_model_uri: ClassVar[URIRef] = BIA_MIFA_MODELS.PublicationsCollection

    publications: Optional[Union[Dict[Union[str, PublicationsPublicationDoi], Union[dict, Publications]], List[Union[dict, Publications]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="publications", slot_type=Publications, key_name="publication_doi", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Author(YAMLRoot):
    """
    Information about the authors
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIA_MIFA_MODELS["Author"]
    class_class_curie: ClassVar[str] = "bia_mifa_models:Author"
    class_name: ClassVar[str] = "Author"
    class_model_uri: ClassVar[URIRef] = BIA_MIFA_MODELS.Author

    author_first_name: str = None
    author_last_name: str = None
    email: Optional[str] = None
    orcid_id: Optional[Union[str, URIorCURIE]] = None
    role: Optional[Union[str, List[str]]] = empty_list()
    organisation: Optional[Union[Union[dict, "OrganisationInfo"], List[Union[dict, "OrganisationInfo"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.author_first_name):
            self.MissingRequiredField("author_first_name")
        if not isinstance(self.author_first_name, str):
            self.author_first_name = str(self.author_first_name)

        if self._is_empty(self.author_last_name):
            self.MissingRequiredField("author_last_name")
        if not isinstance(self.author_last_name, str):
            self.author_last_name = str(self.author_last_name)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.orcid_id is not None and not isinstance(self.orcid_id, URIorCURIE):
            self.orcid_id = URIorCURIE(self.orcid_id)

        if not isinstance(self.role, list):
            self.role = [self.role] if self.role is not None else []
        self.role = [v if isinstance(v, str) else str(v) for v in self.role]

        if not isinstance(self.organisation, list):
            self.organisation = [self.organisation] if self.organisation is not None else []
        self.organisation = [v if isinstance(v, OrganisationInfo) else OrganisationInfo(**as_dict(v)) for v in self.organisation]

        super().__post_init__(**kwargs)


@dataclass
class AuthorCollection(YAMLRoot):
    """
    A holder for Author objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIA_MIFA_MODELS["AuthorCollection"]
    class_class_curie: ClassVar[str] = "bia_mifa_models:AuthorCollection"
    class_name: ClassVar[str] = "AuthorCollection"
    class_model_uri: ClassVar[URIRef] = BIA_MIFA_MODELS.AuthorCollection

    authors: Optional[Union[Union[dict, Author], List[Union[dict, Author]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, Author) else Author(**as_dict(v)) for v in self.authors]

        super().__post_init__(**kwargs)


@dataclass
class OrganisationInfo(YAMLRoot):
    """
    Information about the organisation the author is affiliated with
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIA_MIFA_MODELS["OrganisationInfo"]
    class_class_curie: ClassVar[str] = "bia_mifa_models:OrganisationInfo"
    class_name: ClassVar[str] = "OrganisationInfo"
    class_model_uri: ClassVar[URIRef] = BIA_MIFA_MODELS.OrganisationInfo

    organisation_name: str = None
    address: Optional[str] = None
    ror_id: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.organisation_name):
            self.MissingRequiredField("organisation_name")
        if not isinstance(self.organisation_name, str):
            self.organisation_name = str(self.organisation_name)

        if self.address is not None and not isinstance(self.address, str):
            self.address = str(self.address)

        if self.ror_id is not None and not isinstance(self.ror_id, URIorCURIE):
            self.ror_id = URIorCURIE(self.ror_id)

        super().__post_init__(**kwargs)


@dataclass
class OrganisationInfoCollection(YAMLRoot):
    """
    A holder for OrganisationInfo objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIA_MIFA_MODELS["OrganisationInfoCollection"]
    class_class_curie: ClassVar[str] = "bia_mifa_models:OrganisationInfoCollection"
    class_name: ClassVar[str] = "OrganisationInfoCollection"
    class_model_uri: ClassVar[URIRef] = BIA_MIFA_MODELS.OrganisationInfoCollection

    organisation: Optional[Union[Union[dict, OrganisationInfo], List[Union[dict, OrganisationInfo]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.organisation, list):
            self.organisation = [self.organisation] if self.organisation is not None else []
        self.organisation = [v if isinstance(v, OrganisationInfo) else OrganisationInfo(**as_dict(v)) for v in self.organisation]

        super().__post_init__(**kwargs)


@dataclass
class GrantReference(YAMLRoot):
    """
    Information about grant ID and funding body that funded the study
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIA_MIFA_MODELS["GrantReference"]
    class_class_curie: ClassVar[str] = "bia_mifa_models:GrantReference"
    class_name: ClassVar[str] = "GrantReference"
    class_model_uri: ClassVar[URIRef] = BIA_MIFA_MODELS.GrantReference

    grant_id: Union[str, GrantReferenceGrantId] = None
    funder: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.grant_id):
            self.MissingRequiredField("grant_id")
        if not isinstance(self.grant_id, GrantReferenceGrantId):
            self.grant_id = GrantReferenceGrantId(self.grant_id)

        if self._is_empty(self.funder):
            self.MissingRequiredField("funder")
        if not isinstance(self.funder, str):
            self.funder = str(self.funder)

        super().__post_init__(**kwargs)


@dataclass
class GrantReferenceCollection(YAMLRoot):
    """
    A holder for GrantReference objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIA_MIFA_MODELS["GrantReferenceCollection"]
    class_class_curie: ClassVar[str] = "bia_mifa_models:GrantReferenceCollection"
    class_name: ClassVar[str] = "GrantReferenceCollection"
    class_model_uri: ClassVar[URIRef] = BIA_MIFA_MODELS.GrantReferenceCollection

    grants: Optional[Union[Dict[Union[str, GrantReferenceGrantId], Union[dict, GrantReference]], List[Union[dict, GrantReference]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="grants", slot_type=GrantReference, key_name="grant_id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Links(YAMLRoot):
    """
    Links related to the study
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIA_MIFA_MODELS["Links"]
    class_class_curie: ClassVar[str] = "bia_mifa_models:Links"
    class_name: ClassVar[str] = "Links"
    class_model_uri: ClassVar[URIRef] = BIA_MIFA_MODELS.Links

    link_url: Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]] = None
    link_description: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.link_url):
            self.MissingRequiredField("link_url")
        if not isinstance(self.link_url, list):
            self.link_url = [self.link_url] if self.link_url is not None else []
        self.link_url = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.link_url]

        if not isinstance(self.link_description, list):
            self.link_description = [self.link_description] if self.link_description is not None else []
        self.link_description = [v if isinstance(v, str) else str(v) for v in self.link_description]

        super().__post_init__(**kwargs)


@dataclass
class FileLevelMetadata(YAMLRoot):
    """
    metadata atributes that must be detailed at the file level
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIA_MIFA_MODELS["FileLevelMetadata"]
    class_class_curie: ClassVar[str] = "bia_mifa_models:FileLevelMetadata"
    class_name: ClassVar[str] = "FileLevelMetadata"
    class_model_uri: ClassVar[URIRef] = BIA_MIFA_MODELS.FileLevelMetadata

    annotation_id: Union[str, FileLevelMetadataAnnotationId] = None
    annotation_type: Union[Union[str, "AnnotationType"], List[Union[str, "AnnotationType"]]] = None
    source_image_id: str = None
    transformations: Optional[str] = None
    spatial_information: Optional[str] = None
    annotation_creation_time: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.annotation_id):
            self.MissingRequiredField("annotation_id")
        if not isinstance(self.annotation_id, FileLevelMetadataAnnotationId):
            self.annotation_id = FileLevelMetadataAnnotationId(self.annotation_id)

        if self._is_empty(self.annotation_type):
            self.MissingRequiredField("annotation_type")
        if not isinstance(self.annotation_type, list):
            self.annotation_type = [self.annotation_type] if self.annotation_type is not None else []
        self.annotation_type = [v if isinstance(v, AnnotationType) else AnnotationType(v) for v in self.annotation_type]

        if self._is_empty(self.source_image_id):
            self.MissingRequiredField("source_image_id")
        if not isinstance(self.source_image_id, str):
            self.source_image_id = str(self.source_image_id)

        if self.transformations is not None and not isinstance(self.transformations, str):
            self.transformations = str(self.transformations)

        if self.spatial_information is not None and not isinstance(self.spatial_information, str):
            self.spatial_information = str(self.spatial_information)

        if self.annotation_creation_time is not None and not isinstance(self.annotation_creation_time, XSDDateTime):
            self.annotation_creation_time = XSDDateTime(self.annotation_creation_time)

        super().__post_init__(**kwargs)


@dataclass
class FileLevelMetadataCollection(YAMLRoot):
    """
    A holder for FileLevelMetadata objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIA_MIFA_MODELS["FileLevelMetadataCollection"]
    class_class_curie: ClassVar[str] = "bia_mifa_models:FileLevelMetadataCollection"
    class_name: ClassVar[str] = "FileLevelMetadataCollection"
    class_model_uri: ClassVar[URIRef] = BIA_MIFA_MODELS.FileLevelMetadataCollection

    file_metadata: Optional[Union[Dict[Union[str, FileLevelMetadataAnnotationId], Union[dict, FileLevelMetadata]], List[Union[dict, FileLevelMetadata]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="file_metadata", slot_type=FileLevelMetadata, key_name="annotation_id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Annotations(YAMLRoot):
    """
    A set of annotations for an AI-ready dataset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIA_MIFA_MODELS["Annotations"]
    class_class_curie: ClassVar[str] = "bia_mifa_models:Annotations"
    class_name: ClassVar[str] = "Annotations"
    class_model_uri: ClassVar[URIRef] = BIA_MIFA_MODELS.Annotations

    annotation_overview: str = None
    annotation_method: str = None
    annotation_criteria: Optional[str] = None
    annotation_coverage: Optional[str] = None
    annotation_confidence_level: Optional[str] = None
    authors: Optional[Union[Union[dict, Author], List[Union[dict, Author]]]] = empty_list()
    file_metadata: Optional[Union[Dict[Union[str, FileLevelMetadataAnnotationId], Union[dict, FileLevelMetadata]], List[Union[dict, FileLevelMetadata]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.annotation_overview):
            self.MissingRequiredField("annotation_overview")
        if not isinstance(self.annotation_overview, str):
            self.annotation_overview = str(self.annotation_overview)

        if self._is_empty(self.annotation_method):
            self.MissingRequiredField("annotation_method")
        if not isinstance(self.annotation_method, str):
            self.annotation_method = str(self.annotation_method)

        if self.annotation_criteria is not None and not isinstance(self.annotation_criteria, str):
            self.annotation_criteria = str(self.annotation_criteria)

        if self.annotation_coverage is not None and not isinstance(self.annotation_coverage, str):
            self.annotation_coverage = str(self.annotation_coverage)

        if self.annotation_confidence_level is not None and not isinstance(self.annotation_confidence_level, str):
            self.annotation_confidence_level = str(self.annotation_confidence_level)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, Author) else Author(**as_dict(v)) for v in self.authors]

        self._normalize_inlined_as_list(slot_name="file_metadata", slot_type=FileLevelMetadata, key_name="annotation_id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Version(YAMLRoot):
    """
    Information about the dataset version
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIA_MIFA_MODELS["Version"]
    class_class_curie: ClassVar[str] = "bia_mifa_models:Version"
    class_name: ClassVar[str] = "Version"
    class_model_uri: ClassVar[URIRef] = BIA_MIFA_MODELS.Version

    version: float = None
    timestamp: Union[str, XSDDateTime] = None
    changes: Optional[str] = None
    previous_version: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, float):
            self.version = float(self.version)

        if self._is_empty(self.timestamp):
            self.MissingRequiredField("timestamp")
        if not isinstance(self.timestamp, XSDDateTime):
            self.timestamp = XSDDateTime(self.timestamp)

        if self.changes is not None and not isinstance(self.changes, str):
            self.changes = str(self.changes)

        if self.previous_version is not None and not isinstance(self.previous_version, URIorCURIE):
            self.previous_version = URIorCURIE(self.previous_version)

        super().__post_init__(**kwargs)


# Enumerations
class AnnotationType(EnumDefinitionImpl):

    class_labels = PermissibleValue(
        text="class_labels",
        description="tags that identify specific features, patterns or classes in images")
    bounding_boxes = PermissibleValue(
        text="bounding_boxes",
        description="rectangles completely enclosing a structure of interest within an image")
    counts = PermissibleValue(
        text="counts",
        description="number of objects, such as cells, found in an image")
    derived_annotations = PermissibleValue(
        text="derived_annotations",
        description="""additional analytical data extracted from the images. For example, the image point spread function,the signal to noise ratio, focus information…""")
    geometrical_annotations = PermissibleValue(
        text="geometrical_annotations",
        description="""polygons and shapes that outline a region of interest in the image. These can be geometrical primitives, 2D polygons, 3D meshes…""")
    graphs = PermissibleValue(
        text="graphs",
        description="""graphical representations of the morphology, connectivity, or spatial arrangement of biological structures in an image. Graphs, such as skeletons or connectivity diagrams, typically consist of nodes and edges, where nodes represent individual elements or regions and edges represent the connections or interactions between them""")
    point_annotations = PermissibleValue(
        text="point_annotations",
        description="""X, Y, and Z coordinates of a point of interest in an image (for example an object's centroid  or landmarks).""")
    segmentation_mask = PermissibleValue(
        text="segmentation_mask",
        description="""an image, the same size as the source image, with the value of each pixel representing some biological identity or background region""")
    tracks = PermissibleValue(
        text="tracks",
        description="annotations marking the movement or trajectory of objects within a sequence of bioimages")
    weak_annotations = PermissibleValue(
        text="weak_annotations",
        description="""rough imprecise annotations that are fast to generate. These annotations are used, for example,  to detect an object without providing accurate boundaries""")
    other = PermissibleValue(
        text="other",
        description="other types of annotations, please specify in the annotation overview section")

    _defn = EnumDefinition(
        name="AnnotationType",
    )

class LicenseType(EnumDefinitionImpl):

    CC0 = PermissibleValue(
        text="CC0",
        description="""No Copyright. You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.""",
        meaning=None)
    CC_BY = PermissibleValue(
        text="CC_BY",
        description="""You are free to: Share — copy and redistribute the material in any medium or format. Adapt — remix, transform, and build upon the material  for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.  You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.""",
        meaning=None)

    _defn = EnumDefinition(
        name="LicenseType",
    )

# Slots
class slots:
    pass

slots.title = Slot(uri=SCHEMA.title, name="title", curie=SCHEMA.curie('title'),
                   model_uri=BIA_MIFA_MODELS.title, domain=None, range=str)

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=BIA_MIFA_MODELS.description, domain=None, range=str)

slots.keywords = Slot(uri=SCHEMA.keywords, name="keywords", curie=SCHEMA.curie('keywords'),
                   model_uri=BIA_MIFA_MODELS.keywords, domain=None, range=Union[str, List[str]])

slots.license = Slot(uri=SCHEMA.license, name="license", curie=SCHEMA.curie('license'),
                   model_uri=BIA_MIFA_MODELS.license, domain=None, range=Union[str, "LicenseType"])

slots.ai_models_trained = Slot(uri=BIA_MIFA_MODELS.ai_models_trained, name="ai_models_trained", curie=BIA_MIFA_MODELS.curie('ai_models_trained'),
                   model_uri=BIA_MIFA_MODELS.ai_models_trained, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.funding_statement = Slot(uri=BIA_MIFA_MODELS.funding_statement, name="funding_statement", curie=BIA_MIFA_MODELS.curie('funding_statement'),
                   model_uri=BIA_MIFA_MODELS.funding_statement, domain=None, range=str)

slots.grant_id = Slot(uri=SCHEMA.identifier, name="grant_id", curie=SCHEMA.curie('identifier'),
                   model_uri=BIA_MIFA_MODELS.grant_id, domain=None, range=URIRef)

slots.funder = Slot(uri=SCHEMA.funder, name="funder", curie=SCHEMA.curie('funder'),
                   model_uri=BIA_MIFA_MODELS.funder, domain=None, range=str)

slots.publication_title = Slot(uri=SCHEMA.title, name="publication_title", curie=SCHEMA.curie('title'),
                   model_uri=BIA_MIFA_MODELS.publication_title, domain=None, range=str)

slots.publication_authors = Slot(uri=SCHEMA.author, name="publication_authors", curie=SCHEMA.curie('author'),
                   model_uri=BIA_MIFA_MODELS.publication_authors, domain=None, range=str)

slots.publication_doi = Slot(uri=WIKIDATA_PROPERTY.P356, name="publication_doi", curie=WIKIDATA_PROPERTY.curie('P356'),
                   model_uri=BIA_MIFA_MODELS.publication_doi, domain=None, range=URIRef)

slots.publication_year = Slot(uri=BIA_MIFA_MODELS.publication_year, name="publication_year", curie=BIA_MIFA_MODELS.curie('publication_year'),
                   model_uri=BIA_MIFA_MODELS.publication_year, domain=None, range=Optional[str])

slots.pubmed_id = Slot(uri=WIKIDATA_PROPERTY.P698, name="pubmed_id", curie=WIKIDATA_PROPERTY.curie('P698'),
                   model_uri=BIA_MIFA_MODELS.pubmed_id, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.link_url = Slot(uri=BIA_MIFA_MODELS.link_url, name="link_url", curie=BIA_MIFA_MODELS.curie('link_url'),
                   model_uri=BIA_MIFA_MODELS.link_url, domain=None, range=Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]])

slots.link_description = Slot(uri=BIA_MIFA_MODELS.link_description, name="link_description", curie=BIA_MIFA_MODELS.curie('link_description'),
                   model_uri=BIA_MIFA_MODELS.link_description, domain=None, range=Optional[Union[str, List[str]]])

slots.acknowledgements = Slot(uri=BIA_MIFA_MODELS.acknowledgements, name="acknowledgements", curie=BIA_MIFA_MODELS.curie('acknowledgements'),
                   model_uri=BIA_MIFA_MODELS.acknowledgements, domain=None, range=Optional[str])

slots.orcid_id = Slot(uri=WIKIDATA_PROPERTY.P496, name="orcid_id", curie=WIKIDATA_PROPERTY.curie('P496'),
                   model_uri=BIA_MIFA_MODELS.orcid_id, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.author_first_name = Slot(uri=SCHEMA.name, name="author_first_name", curie=SCHEMA.curie('name'),
                   model_uri=BIA_MIFA_MODELS.author_first_name, domain=None, range=str)

slots.author_last_name = Slot(uri=SCHEMA.name, name="author_last_name", curie=SCHEMA.curie('name'),
                   model_uri=BIA_MIFA_MODELS.author_last_name, domain=None, range=str)

slots.email = Slot(uri=SCHEMA.email, name="email", curie=SCHEMA.curie('email'),
                   model_uri=BIA_MIFA_MODELS.email, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))

slots.organisation_name = Slot(uri=SCHEMA.name, name="organisation_name", curie=SCHEMA.curie('name'),
                   model_uri=BIA_MIFA_MODELS.organisation_name, domain=None, range=str)

slots.ror_id = Slot(uri=WIKIDATA_PROPERTY.P6782, name="ror_id", curie=WIKIDATA_PROPERTY.curie('P6782'),
                   model_uri=BIA_MIFA_MODELS.ror_id, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.address = Slot(uri=SCHEMA.name, name="address", curie=SCHEMA.curie('name'),
                   model_uri=BIA_MIFA_MODELS.address, domain=None, range=Optional[str])

slots.role = Slot(uri=SCHEMA.roleName, name="role", curie=SCHEMA.curie('roleName'),
                   model_uri=BIA_MIFA_MODELS.role, domain=None, range=Optional[Union[str, List[str]]])

slots.annotation_overview = Slot(uri=BIA_MIFA_MODELS.annotation_overview, name="annotation_overview", curie=BIA_MIFA_MODELS.curie('annotation_overview'),
                   model_uri=BIA_MIFA_MODELS.annotation_overview, domain=None, range=str)

slots.annotation_type = Slot(uri=BIA_MIFA_MODELS.annotation_type, name="annotation_type", curie=BIA_MIFA_MODELS.curie('annotation_type'),
                   model_uri=BIA_MIFA_MODELS.annotation_type, domain=None, range=Union[Union[str, "AnnotationType"], List[Union[str, "AnnotationType"]]])

slots.annotation_method = Slot(uri=BIA_MIFA_MODELS.annotation_method, name="annotation_method", curie=BIA_MIFA_MODELS.curie('annotation_method'),
                   model_uri=BIA_MIFA_MODELS.annotation_method, domain=None, range=str)

slots.annotation_criteria = Slot(uri=BIA_MIFA_MODELS.annotation_criteria, name="annotation_criteria", curie=BIA_MIFA_MODELS.curie('annotation_criteria'),
                   model_uri=BIA_MIFA_MODELS.annotation_criteria, domain=None, range=Optional[str])

slots.annotation_coverage = Slot(uri=BIA_MIFA_MODELS.annotation_coverage, name="annotation_coverage", curie=BIA_MIFA_MODELS.curie('annotation_coverage'),
                   model_uri=BIA_MIFA_MODELS.annotation_coverage, domain=None, range=Optional[str])

slots.source_image_id = Slot(uri=BIA_MIFA_MODELS.source_image_id, name="source_image_id", curie=BIA_MIFA_MODELS.curie('source_image_id'),
                   model_uri=BIA_MIFA_MODELS.source_image_id, domain=None, range=str)

slots.annotation_id = Slot(uri=SCHEMA.identifier, name="annotation_id", curie=SCHEMA.curie('identifier'),
                   model_uri=BIA_MIFA_MODELS.annotation_id, domain=None, range=URIRef)

slots.annotation_confidence_level = Slot(uri=BIA_MIFA_MODELS.annotation_confidence_level, name="annotation_confidence_level", curie=BIA_MIFA_MODELS.curie('annotation_confidence_level'),
                   model_uri=BIA_MIFA_MODELS.annotation_confidence_level, domain=None, range=Optional[str])

slots.spatial_information = Slot(uri=BIA_MIFA_MODELS.spatial_information, name="spatial_information", curie=BIA_MIFA_MODELS.curie('spatial_information'),
                   model_uri=BIA_MIFA_MODELS.spatial_information, domain=None, range=Optional[str])

slots.transformations = Slot(uri=BIA_MIFA_MODELS.transformations, name="transformations", curie=BIA_MIFA_MODELS.curie('transformations'),
                   model_uri=BIA_MIFA_MODELS.transformations, domain=None, range=Optional[str])

slots.annotation_creation_time = Slot(uri=PAV.authoredOn, name="annotation_creation_time", curie=PAV.curie('authoredOn'),
                   model_uri=BIA_MIFA_MODELS.annotation_creation_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.version = Slot(uri=PAV.version, name="version", curie=PAV.curie('version'),
                   model_uri=BIA_MIFA_MODELS.version, domain=None, range=float)

slots.timestamp = Slot(uri=PAV.authoredOn, name="timestamp", curie=PAV.curie('authoredOn'),
                   model_uri=BIA_MIFA_MODELS.timestamp, domain=None, range=Union[str, XSDDateTime])

slots.changes = Slot(uri=BIA_MIFA_MODELS.changes, name="changes", curie=BIA_MIFA_MODELS.curie('changes'),
                   model_uri=BIA_MIFA_MODELS.changes, domain=None, range=Optional[str])

slots.previous_version = Slot(uri=PAV.previousVersion, name="previous_version", curie=PAV.curie('previousVersion'),
                   model_uri=BIA_MIFA_MODELS.previous_version, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.publicationsCollection__publications = Slot(uri=BIA_MIFA_MODELS.publications, name="publicationsCollection__publications", curie=BIA_MIFA_MODELS.curie('publications'),
                   model_uri=BIA_MIFA_MODELS.publicationsCollection__publications, domain=None, range=Optional[Union[Dict[Union[str, PublicationsPublicationDoi], Union[dict, Publications]], List[Union[dict, Publications]]]])

slots.authorCollection__authors = Slot(uri=BIA_MIFA_MODELS.authors, name="authorCollection__authors", curie=BIA_MIFA_MODELS.curie('authors'),
                   model_uri=BIA_MIFA_MODELS.authorCollection__authors, domain=None, range=Optional[Union[Union[dict, Author], List[Union[dict, Author]]]])

slots.organisationInfoCollection__organisation = Slot(uri=BIA_MIFA_MODELS.organisation, name="organisationInfoCollection__organisation", curie=BIA_MIFA_MODELS.curie('organisation'),
                   model_uri=BIA_MIFA_MODELS.organisationInfoCollection__organisation, domain=None, range=Optional[Union[Union[dict, OrganisationInfo], List[Union[dict, OrganisationInfo]]]])

slots.grantReferenceCollection__grants = Slot(uri=BIA_MIFA_MODELS.grants, name="grantReferenceCollection__grants", curie=BIA_MIFA_MODELS.curie('grants'),
                   model_uri=BIA_MIFA_MODELS.grantReferenceCollection__grants, domain=None, range=Optional[Union[Dict[Union[str, GrantReferenceGrantId], Union[dict, GrantReference]], List[Union[dict, GrantReference]]]])

slots.fileLevelMetadataCollection__file_metadata = Slot(uri=BIA_MIFA_MODELS.file_metadata, name="fileLevelMetadataCollection__file_metadata", curie=BIA_MIFA_MODELS.curie('file_metadata'),
                   model_uri=BIA_MIFA_MODELS.fileLevelMetadataCollection__file_metadata, domain=None, range=Optional[Union[Dict[Union[str, FileLevelMetadataAnnotationId], Union[dict, FileLevelMetadata]], List[Union[dict, FileLevelMetadata]]]])