from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel as BaseModel, ConfigDict, Field
import sys
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


metamodel_version = "None"
version = "None"

class WeakRefShimBaseModel(BaseModel):
   __slots__ = '__weakref__'

class ConfiguredBaseModel(WeakRefShimBaseModel,
                validate_assignment = True,
                validate_all = True,
                underscore_attrs_are_private = True,
                extra = 'forbid',
                arbitrary_types_allowed = True,
                use_enum_values = True):
    pass


class AnnotationType(str, Enum):
    
    # tags that identify specific features, patterns or classes in images
    class_labels = "class_labels"
    # rectangles completely enclosing a structure of interest within an image
    bounding_boxes = "bounding_boxes"
    # number of objects, such as cells, found in an image
    counts = "counts"
    # additional analytical data extracted from the images. For example, the image point spread function,the signal to noise ratio, focus information…
    derived_annotations = "derived_annotations"
    # polygons and shapes that outline a region of interest in the image. These can be geometrical primitives, 2D polygons, 3D meshes…
    geometrical_annotations = "geometrical_annotations"
    # graphical representations of the morphology, connectivity, or spatial arrangement of biological structures in an image. Graphs, such as skeletons or connectivity diagrams, typically consist of nodes and edges, where nodes represent individual elements or regions and edges represent the connections or interactions between them
    graphs = "graphs"
    # X, Y, and Z coordinates of a point of interest in an image (for example an object's centroid  or landmarks).
    point_annotations = "point_annotations"
    # an image, the same size as the source image, with the value of each pixel representing some biological identity or background region
    segmentation_mask = "segmentation_mask"
    # annotations marking the movement or trajectory of objects within a sequence of bioimages
    tracks = "tracks"
    # rough imprecise annotations that are fast to generate. These annotations are used, for example,  to detect an object without providing accurate boundaries
    weak_annotations = "weak_annotations"
    # other types of annotations, please specify in the annotation overview section
    other = "other"
    
    

class LicenseType(str, Enum):
    
    # No Copyright. You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.
    CC0 = "CC0"
    # You are free to: Share — copy and redistribute the material in any medium or format. Adapt — remix, transform, and build upon the material  for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.  You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
    CC_BY = "CC_BY"
    
    

class Publications(ConfiguredBaseModel):
    """
    Information about any publications associated with the dataset
    """
    publication_title: str = Field(..., description="""The title for a publication associated to the dataset""")
    publication_authors: str = Field(..., description="""Authors of associated publication""")
    publication_doi: str = Field(..., description="""Digital Object Identifier (DOI)""")
    publication_year: Optional[str] = Field(None, description="""Year of publication""")
    pubmed_id: Optional[str] = Field(None, description="""Identifier for journal articles/abstracts in PubMed""")
    

class PublicationsCollection(ConfiguredBaseModel):
    """
    A holder for Publications objects
    """
    publications: Optional[Dict[str, Publications]] = Field(default_factory=dict, description="""a collection of publications associated with a study""")
    

class AuthorCollection(ConfiguredBaseModel):
    """
    A holder for Author objects
    """
    authors: Optional[List[Author]] = Field(default_factory=list, description="""a collection of the authors of a study""")
    

class OrganisationInfo(ConfiguredBaseModel):
    """
    Information about the organisation the author is affiliated with
    """
    organisation_name: str = Field(..., description="""Organisation name""")
    address: Optional[str] = Field(None, description="""Organisation address""")
    ror_id: Optional[str] = Field(None, description="""Identifier for the Research Organization Registry""")
    

class OrganisationInfoCollection(ConfiguredBaseModel):
    """
    A holder for OrganisationInfo objects
    """
    organisation: Optional[List[OrganisationInfo]] = Field(default_factory=list, description="""a collection of the name and address of organisations authors are affiliated with""")
    

class Author(OrganisationInfoCollection):
    """
    Information about the authors
    """
    author_first_name: str = Field(..., description="""First name for an author""")
    author_last_name: str = Field(..., description="""Last name for an author""")
    email: Optional[str] = Field(None, description="""Email address of a person""", regex="^\S+@[\S+\.]+\S+")
    orcid_id: Optional[str] = Field(None, description="""A unique identifier for an author""")
    role: Optional[List[str]] = Field(default_factory=list, description="""Role of the author when creating the dataset""")
    organisation: Optional[List[OrganisationInfo]] = Field(default_factory=list, description="""a collection of the name and address of organisations authors are affiliated with""")
    

class GrantReference(ConfiguredBaseModel):
    """
    Information about grant ID and funding body that funded the study
    """
    grant_id: str = Field(..., description="""The identifier for the grant""")
    funder: str = Field(..., description="""The funding body provididing support""")
    

class GrantReferenceCollection(ConfiguredBaseModel):
    """
    A holder for GrantReference objects
    """
    grants: Optional[List[GrantReference]] = Field(default_factory=list, description="""a collection of grant ids and funder names associated with the study""")
    

class Links(ConfiguredBaseModel):
    """
    Links related to the study
    """
    link_url: List[str] = Field(default_factory=list, description="""URL of relevant link""")
    link_description: Optional[List[str]] = Field(default_factory=list, description="""The description of the linked content""")
    

class Study(Links, GrantReferenceCollection, AuthorCollection, PublicationsCollection):
    """
    General information about the study
    """
    title: str = Field(..., description="""The title for your dataset. This will be displayed when search results including your data are shown. Often this will be the same as an associated publication.""")
    description: str = Field(..., description="""Brief description of the detaset. Must contain the biological application of the dataset""")
    keywords: List[str] = Field(default_factory=list, description="""Keywords or tags used to describe the dataset""")
    license: LicenseType = Field(..., description="""The license under which the data are available""")
    ai_models_trained: Optional[List[str]] = Field(default_factory=list, description="""Link to the models that have been trained with this dataset (if any). This could be links to GitHub or repositories like the BioImage Zoo.""")
    acknowledgements: Optional[str] = Field(None, description="""Any people or groups that should be acknowledged as part of the dataset""")
    funding_statement: str = Field(..., description="""Description of how the study was funded""")
    publications: Optional[Dict[str, Publications]] = Field(default_factory=dict, description="""a collection of publications associated with a study""")
    authors: Optional[List[Author]] = Field(default_factory=list, description="""a collection of the authors of a study""")
    link_url: List[str] = Field(default_factory=list, description="""URL of relevant link""")
    link_description: Optional[List[str]] = Field(default_factory=list, description="""The description of the linked content""")
    grants: Optional[List[GrantReference]] = Field(default_factory=list, description="""a collection of grant ids and funder names associated with the study""")
    

class FileLevelMetadata(ConfiguredBaseModel):
    """
    metadata atributes that must be detailed at the file level
    """
    annotation_id: str = Field(..., description="""The identifier for the annotation""")
    annotation_type: List[AnnotationType] = Field(default_factory=list, description="""Annotation type, for example class labels, segmentation masks, counts...""")
    source_image_id: str = Field(..., description="""identifier of the source image from which the annotation originated""")
    transformations: Optional[str] = Field(None, description="""Any transformations required to link the images to the annotations""")
    spatial_information: Optional[str] = Field(None, description="""Spatial information for non-pixel annotations""")
    annotation_creation_time: Optional[datetime ] = Field(None, description="""Date and time when the annotation was created""")
    

class FileLevelMetadataCollection(ConfiguredBaseModel):
    """
    A holder for FileLevelMetadata objects
    """
    file_metadata: Optional[List[FileLevelMetadata]] = Field(default_factory=list, description="""a collection of the file level metadata for each annotation""")
    

class Annotations(FileLevelMetadataCollection, AuthorCollection):
    """
    A set of annotations for an AI-ready dataset
    """
    annotation_overview: str = Field(..., description="""Short descriptive summary indicating the type of annotation and how it was generated""")
    annotation_type: List[AnnotationType] = Field(default_factory=list, description="""Annotation type, for example class labels, segmentation masks, counts...""")
    annotation_method: str = Field(..., description="""Description of how the annotations were created. For example, were the annotations crowdsourced or expertly annotated,  produced by  a human or software, what software was used, when were the annotations created,  protocols used for consensus and quality assurance""")
    annotation_criteria: Optional[str] = Field(None, description="""Rules used to generate annotations""")
    annotation_coverage: Optional[str] = Field(None, description="""Which images from the dataset were annotated, and what percentage of the data has been annotated from what is available""")
    annotation_confidence_level: Optional[str] = Field(None, description="""Confidence on annotation accuracy""")
    authors: Optional[List[Author]] = Field(default_factory=list, description="""a collection of the authors of a study""")
    file_metadata: Optional[List[FileLevelMetadata]] = Field(default_factory=list, description="""a collection of the file level metadata for each annotation""")
    

class Version(ConfiguredBaseModel):
    """
    Information about the dataset version
    """
    version: str = Field(..., description="""Unique version number""")
    timestamp: datetime  = Field(..., description="""Date and time when the version was created""")
    changes: Optional[str] = Field(None, description="""Textual description of changes compared to previous version""")
    previous_version: Optional[str] = Field(None, description="""Pointer to previous version""")
    


# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
Publications.update_forward_refs()
PublicationsCollection.update_forward_refs()
AuthorCollection.update_forward_refs()
OrganisationInfo.update_forward_refs()
OrganisationInfoCollection.update_forward_refs()
Author.update_forward_refs()
GrantReference.update_forward_refs()
GrantReferenceCollection.update_forward_refs()
Links.update_forward_refs()
Study.update_forward_refs()
FileLevelMetadata.update_forward_refs()
FileLevelMetadataCollection.update_forward_refs()
Annotations.update_forward_refs()
Version.update_forward_refs()

