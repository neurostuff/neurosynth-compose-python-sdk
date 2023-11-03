# neurosynth-compose-sdk
api to create a meta-analysis specification

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 0.0.1
- Build package: org.openapitools.codegen.languages.PythonNextgenClientCodegen
For more information, please visit [https://github.com/jdkent](https://github.com/jdkent)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import neurosynth_compose_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import neurosynth_compose_sdk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://compose.neurosynth.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "https://compose.neurosynth.org/api"
)



# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurosynth_compose_sdk.AnnotationsApi(api_client)

    try:
        # GET a list of annotations
        api_response = api_instance.annotations_get()
        print("The response of AnnotationsApi->annotations_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnotationsApi->annotations_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://compose.neurosynth.org/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnnotationsApi* | [**annotations_get**](docs/AnnotationsApi.md#annotations_get) | **GET** /annotations | GET a list of annotations
*AnnotationsApi* | [**annotations_id_get**](docs/AnnotationsApi.md#annotations_id_get) | **GET** /annotations/{id} | GET information about an annotation
*AnnotationsApi* | [**annotations_id_put**](docs/AnnotationsApi.md#annotations_id_put) | **PUT** /annotations/{id} | Update an Annotation
*AnnotationsApi* | [**annotations_post**](docs/AnnotationsApi.md#annotations_post) | **POST** /annotations | Create a new Annotation
*ComposeApi* | [**annotations_get**](docs/ComposeApi.md#annotations_get) | **GET** /annotations | GET a list of annotations
*ComposeApi* | [**annotations_id_get**](docs/ComposeApi.md#annotations_id_get) | **GET** /annotations/{id} | GET information about an annotation
*ComposeApi* | [**annotations_id_put**](docs/ComposeApi.md#annotations_id_put) | **PUT** /annotations/{id} | Update an Annotation
*ComposeApi* | [**annotations_post**](docs/ComposeApi.md#annotations_post) | **POST** /annotations | Create a new Annotation
*ComposeApi* | [**meta_analyses_get**](docs/ComposeApi.md#meta_analyses_get) | **GET** /meta-analyses | GET a list of meta-analyses
*ComposeApi* | [**meta_analyses_id_get**](docs/ComposeApi.md#meta_analyses_id_get) | **GET** /meta-analyses/{id} | GET meta-analysis information
*ComposeApi* | [**meta_analyses_id_put**](docs/ComposeApi.md#meta_analyses_id_put) | **PUT** /meta-analyses/{id} | Update a meta-analysis
*ComposeApi* | [**meta_analyses_post**](docs/ComposeApi.md#meta_analyses_post) | **POST** /meta-analyses | Create a new meta-analysis
*ComposeApi* | [**meta_analysis_results_get**](docs/ComposeApi.md#meta_analysis_results_get) | **GET** /meta-analysis-results | Your GET endpoint
*ComposeApi* | [**meta_analysis_results_id_get**](docs/ComposeApi.md#meta_analysis_results_id_get) | **GET** /meta-analysis-results/{id} | Your GET endpoint
*ComposeApi* | [**meta_analysis_results_id_put**](docs/ComposeApi.md#meta_analysis_results_id_put) | **PUT** /meta-analysis-results/{id} | 
*ComposeApi* | [**meta_analysis_results_post**](docs/ComposeApi.md#meta_analysis_results_post) | **POST** /meta-analysis-results | 
*ComposeApi* | [**neurovault_collections_get**](docs/ComposeApi.md#neurovault_collections_get) | **GET** /neurovault-collections | Get neurovault collections
*ComposeApi* | [**neurovault_collections_id_get**](docs/ComposeApi.md#neurovault_collections_id_get) | **GET** /neurovault-collections/{id} | Your GET endpoint
*ComposeApi* | [**neurovault_collections_id_put**](docs/ComposeApi.md#neurovault_collections_id_put) | **PUT** /neurovault-collections/{id} | 
*ComposeApi* | [**neurovault_collections_post**](docs/ComposeApi.md#neurovault_collections_post) | **POST** /neurovault-collections | Create neurovault collection
*ComposeApi* | [**neurovault_files_get**](docs/ComposeApi.md#neurovault_files_get) | **GET** /neurovault-files | Your GET endpoint
*ComposeApi* | [**neurovault_files_id_get**](docs/ComposeApi.md#neurovault_files_id_get) | **GET** /neurovault-files/{id} | Your GET endpoint
*ComposeApi* | [**neurovault_files_id_put**](docs/ComposeApi.md#neurovault_files_id_put) | **PUT** /neurovault-files/{id} | 
*ComposeApi* | [**neurovault_files_post**](docs/ComposeApi.md#neurovault_files_post) | **POST** /neurovault-files | 
*ComposeApi* | [**projects_get**](docs/ComposeApi.md#projects_get) | **GET** /projects | Your GET endpoint
*ComposeApi* | [**projects_id_delete**](docs/ComposeApi.md#projects_id_delete) | **DELETE** /projects/{id} | 
*ComposeApi* | [**projects_id_get**](docs/ComposeApi.md#projects_id_get) | **GET** /projects/{id} | Your GET endpoint
*ComposeApi* | [**projects_id_put**](docs/ComposeApi.md#projects_id_put) | **PUT** /projects/{id} | 
*ComposeApi* | [**projects_post**](docs/ComposeApi.md#projects_post) | **POST** /projects | 
*ComposeApi* | [**specifications_get**](docs/ComposeApi.md#specifications_get) | **GET** /specifications | Get a list of Specifications
*ComposeApi* | [**specifications_id_get**](docs/ComposeApi.md#specifications_id_get) | **GET** /specifications/{id} | Get information about a Specification
*ComposeApi* | [**specifications_id_put**](docs/ComposeApi.md#specifications_id_put) | **PUT** /specifications/{id} | Update Meta-Analysis specification
*ComposeApi* | [**specifications_post**](docs/ComposeApi.md#specifications_post) | **POST** /specifications | Create a Specification
*ComposeApi* | [**studysets_get**](docs/ComposeApi.md#studysets_get) | **GET** /studysets | Get a list of Studysets
*ComposeApi* | [**studysets_id_get**](docs/ComposeApi.md#studysets_id_get) | **GET** /studysets/{id} | Get information about a Studyset
*ComposeApi* | [**studysets_id_put**](docs/ComposeApi.md#studysets_id_put) | **PUT** /studysets/{id} | Update a Studyset
*ComposeApi* | [**studysets_post**](docs/ComposeApi.md#studysets_post) | **POST** /studysets | Create a new Studyset
*DefaultApi* | [**meta_analyses_id_delete**](docs/DefaultApi.md#meta_analyses_id_delete) | **DELETE** /meta-analyses/{id} | 
*DefaultApi* | [**neurostore_studies_get**](docs/DefaultApi.md#neurostore_studies_get) | **GET** /neurostore-studies | Your GET endpoint
*DefaultApi* | [**neurostore_studies_id_get**](docs/DefaultApi.md#neurostore_studies_id_get) | **GET** /neurostore-studies/{id} | Your GET endpoint
*DefaultApi* | [**neurostore_studies_id_put**](docs/DefaultApi.md#neurostore_studies_id_put) | **PUT** /neurostore-studies/{id} | 
*DefaultApi* | [**neurostore_studies_post**](docs/DefaultApi.md#neurostore_studies_post) | **POST** /neurostore-studies | 
*DefaultApi* | [**studyset_references_get**](docs/DefaultApi.md#studyset_references_get) | **GET** /studyset-references | Your GET endpoint
*DefaultApi* | [**studyset_references_id_get**](docs/DefaultApi.md#studyset_references_id_get) | **GET** /studyset-references/{id} | Your GET endpoint
*GetApi* | [**annotations_get**](docs/GetApi.md#annotations_get) | **GET** /annotations | GET a list of annotations
*GetApi* | [**annotations_id_get**](docs/GetApi.md#annotations_id_get) | **GET** /annotations/{id} | GET information about an annotation
*GetApi* | [**meta_analyses_get**](docs/GetApi.md#meta_analyses_get) | **GET** /meta-analyses | GET a list of meta-analyses
*GetApi* | [**meta_analyses_id_get**](docs/GetApi.md#meta_analyses_id_get) | **GET** /meta-analyses/{id} | GET meta-analysis information
*GetApi* | [**meta_analysis_results_get**](docs/GetApi.md#meta_analysis_results_get) | **GET** /meta-analysis-results | Your GET endpoint
*GetApi* | [**meta_analysis_results_id_get**](docs/GetApi.md#meta_analysis_results_id_get) | **GET** /meta-analysis-results/{id} | Your GET endpoint
*GetApi* | [**neurovault_collections_get**](docs/GetApi.md#neurovault_collections_get) | **GET** /neurovault-collections | Get neurovault collections
*GetApi* | [**neurovault_collections_id_get**](docs/GetApi.md#neurovault_collections_id_get) | **GET** /neurovault-collections/{id} | Your GET endpoint
*GetApi* | [**neurovault_files_get**](docs/GetApi.md#neurovault_files_get) | **GET** /neurovault-files | Your GET endpoint
*GetApi* | [**neurovault_files_id_get**](docs/GetApi.md#neurovault_files_id_get) | **GET** /neurovault-files/{id} | Your GET endpoint
*GetApi* | [**projects_get**](docs/GetApi.md#projects_get) | **GET** /projects | Your GET endpoint
*GetApi* | [**projects_id_get**](docs/GetApi.md#projects_id_get) | **GET** /projects/{id} | Your GET endpoint
*GetApi* | [**specifications_get**](docs/GetApi.md#specifications_get) | **GET** /specifications | Get a list of Specifications
*GetApi* | [**specifications_id_get**](docs/GetApi.md#specifications_id_get) | **GET** /specifications/{id} | Get information about a Specification
*GetApi* | [**studysets_get**](docs/GetApi.md#studysets_get) | **GET** /studysets | Get a list of Studysets
*GetApi* | [**studysets_id_get**](docs/GetApi.md#studysets_id_get) | **GET** /studysets/{id} | Get information about a Studyset
*MetaAnalysesApi* | [**meta_analyses_get**](docs/MetaAnalysesApi.md#meta_analyses_get) | **GET** /meta-analyses | GET a list of meta-analyses
*MetaAnalysesApi* | [**meta_analyses_id_get**](docs/MetaAnalysesApi.md#meta_analyses_id_get) | **GET** /meta-analyses/{id} | GET meta-analysis information
*MetaAnalysesApi* | [**meta_analyses_id_put**](docs/MetaAnalysesApi.md#meta_analyses_id_put) | **PUT** /meta-analyses/{id} | Update a meta-analysis
*MetaAnalysesApi* | [**meta_analyses_post**](docs/MetaAnalysesApi.md#meta_analyses_post) | **POST** /meta-analyses | Create a new meta-analysis
*MetaAnalysesApi* | [**meta_analysis_results_get**](docs/MetaAnalysesApi.md#meta_analysis_results_get) | **GET** /meta-analysis-results | Your GET endpoint
*MetaAnalysesApi* | [**meta_analysis_results_id_get**](docs/MetaAnalysesApi.md#meta_analysis_results_id_get) | **GET** /meta-analysis-results/{id} | Your GET endpoint
*MetaAnalysesApi* | [**meta_analysis_results_id_put**](docs/MetaAnalysesApi.md#meta_analysis_results_id_put) | **PUT** /meta-analysis-results/{id} | 
*MetaAnalysesApi* | [**meta_analysis_results_post**](docs/MetaAnalysesApi.md#meta_analysis_results_post) | **POST** /meta-analysis-results | 
*NeurovaultApi* | [**neurovault_collections_get**](docs/NeurovaultApi.md#neurovault_collections_get) | **GET** /neurovault-collections | Get neurovault collections
*NeurovaultApi* | [**neurovault_collections_id_get**](docs/NeurovaultApi.md#neurovault_collections_id_get) | **GET** /neurovault-collections/{id} | Your GET endpoint
*NeurovaultApi* | [**neurovault_collections_id_put**](docs/NeurovaultApi.md#neurovault_collections_id_put) | **PUT** /neurovault-collections/{id} | 
*NeurovaultApi* | [**neurovault_collections_post**](docs/NeurovaultApi.md#neurovault_collections_post) | **POST** /neurovault-collections | Create neurovault collection
*NeurovaultApi* | [**neurovault_files_get**](docs/NeurovaultApi.md#neurovault_files_get) | **GET** /neurovault-files | Your GET endpoint
*NeurovaultApi* | [**neurovault_files_id_get**](docs/NeurovaultApi.md#neurovault_files_id_get) | **GET** /neurovault-files/{id} | Your GET endpoint
*NeurovaultApi* | [**neurovault_files_id_put**](docs/NeurovaultApi.md#neurovault_files_id_put) | **PUT** /neurovault-files/{id} | 
*NeurovaultApi* | [**neurovault_files_post**](docs/NeurovaultApi.md#neurovault_files_post) | **POST** /neurovault-files | 
*PostApi* | [**annotations_post**](docs/PostApi.md#annotations_post) | **POST** /annotations | Create a new Annotation
*PostApi* | [**meta_analyses_post**](docs/PostApi.md#meta_analyses_post) | **POST** /meta-analyses | Create a new meta-analysis
*PostApi* | [**meta_analysis_results_post**](docs/PostApi.md#meta_analysis_results_post) | **POST** /meta-analysis-results | 
*PostApi* | [**neurovault_collections_post**](docs/PostApi.md#neurovault_collections_post) | **POST** /neurovault-collections | Create neurovault collection
*PostApi* | [**neurovault_files_post**](docs/PostApi.md#neurovault_files_post) | **POST** /neurovault-files | 
*PostApi* | [**projects_post**](docs/PostApi.md#projects_post) | **POST** /projects | 
*PostApi* | [**specifications_post**](docs/PostApi.md#specifications_post) | **POST** /specifications | Create a Specification
*PostApi* | [**studysets_post**](docs/PostApi.md#studysets_post) | **POST** /studysets | Create a new Studyset
*ProjectsApi* | [**projects_get**](docs/ProjectsApi.md#projects_get) | **GET** /projects | Your GET endpoint
*ProjectsApi* | [**projects_id_delete**](docs/ProjectsApi.md#projects_id_delete) | **DELETE** /projects/{id} | 
*ProjectsApi* | [**projects_id_get**](docs/ProjectsApi.md#projects_id_get) | **GET** /projects/{id} | Your GET endpoint
*ProjectsApi* | [**projects_id_put**](docs/ProjectsApi.md#projects_id_put) | **PUT** /projects/{id} | 
*ProjectsApi* | [**projects_post**](docs/ProjectsApi.md#projects_post) | **POST** /projects | 
*PutApi* | [**annotations_id_put**](docs/PutApi.md#annotations_id_put) | **PUT** /annotations/{id} | Update an Annotation
*PutApi* | [**meta_analyses_id_put**](docs/PutApi.md#meta_analyses_id_put) | **PUT** /meta-analyses/{id} | Update a meta-analysis
*PutApi* | [**meta_analysis_results_id_put**](docs/PutApi.md#meta_analysis_results_id_put) | **PUT** /meta-analysis-results/{id} | 
*PutApi* | [**neurovault_collections_id_put**](docs/PutApi.md#neurovault_collections_id_put) | **PUT** /neurovault-collections/{id} | 
*PutApi* | [**neurovault_files_id_put**](docs/PutApi.md#neurovault_files_id_put) | **PUT** /neurovault-files/{id} | 
*PutApi* | [**projects_id_put**](docs/PutApi.md#projects_id_put) | **PUT** /projects/{id} | 
*PutApi* | [**specifications_id_put**](docs/PutApi.md#specifications_id_put) | **PUT** /specifications/{id} | Update Meta-Analysis specification
*PutApi* | [**studysets_id_put**](docs/PutApi.md#studysets_id_put) | **PUT** /studysets/{id} | Update a Studyset
*SpecificationsApi* | [**specifications_get**](docs/SpecificationsApi.md#specifications_get) | **GET** /specifications | Get a list of Specifications
*SpecificationsApi* | [**specifications_id_get**](docs/SpecificationsApi.md#specifications_id_get) | **GET** /specifications/{id} | Get information about a Specification
*SpecificationsApi* | [**specifications_id_put**](docs/SpecificationsApi.md#specifications_id_put) | **PUT** /specifications/{id} | Update Meta-Analysis specification
*SpecificationsApi* | [**specifications_post**](docs/SpecificationsApi.md#specifications_post) | **POST** /specifications | Create a Specification
*StudysetsApi* | [**studysets_get**](docs/StudysetsApi.md#studysets_get) | **GET** /studysets | Get a list of Studysets
*StudysetsApi* | [**studysets_id_get**](docs/StudysetsApi.md#studysets_id_get) | **GET** /studysets/{id} | Get information about a Studyset
*StudysetsApi* | [**studysets_id_put**](docs/StudysetsApi.md#studysets_id_put) | **PUT** /studysets/{id} | Update a Studyset
*StudysetsApi* | [**studysets_post**](docs/StudysetsApi.md#studysets_post) | **POST** /studysets | Create a new Studyset
*UsersApi* | [**users_get**](docs/UsersApi.md#users_get) | **GET** /users | GET list of Users
*UsersApi* | [**users_id_get**](docs/UsersApi.md#users_id_get) | **GET** /users/{id} | Get User Info by User ID
*UsersApi* | [**users_id_put**](docs/UsersApi.md#users_id_put) | **PUT** /users/{id} | Update User Information
*UsersApi* | [**users_post**](docs/UsersApi.md#users_post) | **POST** /users | Create A New User


## Documentation For Models

 - [Annotation](docs/Annotation.md)
 - [AnnotationList](docs/AnnotationList.md)
 - [AnnotationPostBody](docs/AnnotationPostBody.md)
 - [AnnotationReturn](docs/AnnotationReturn.md)
 - [AnnotationUpdate](docs/AnnotationUpdate.md)
 - [AnnotationUpdateAllOf](docs/AnnotationUpdateAllOf.md)
 - [Corrector](docs/Corrector.md)
 - [Estimator](docs/Estimator.md)
 - [MetaAnalysesGet400Response](docs/MetaAnalysesGet400Response.md)
 - [MetaAnalysis](docs/MetaAnalysis.md)
 - [MetaAnalysisAnnotation](docs/MetaAnalysisAnnotation.md)
 - [MetaAnalysisList](docs/MetaAnalysisList.md)
 - [MetaAnalysisPostBody](docs/MetaAnalysisPostBody.md)
 - [MetaAnalysisResults](docs/MetaAnalysisResults.md)
 - [MetaAnalysisReturn](docs/MetaAnalysisReturn.md)
 - [MetaAnalysisSpecification](docs/MetaAnalysisSpecification.md)
 - [MetaAnalysisStudyset](docs/MetaAnalysisStudyset.md)
 - [NeurostoreAnalysis](docs/NeurostoreAnalysis.md)
 - [NeurostoreStudy](docs/NeurostoreStudy.md)
 - [NeurostoreStudyList](docs/NeurostoreStudyList.md)
 - [NeurostoreStudyReturn](docs/NeurostoreStudyReturn.md)
 - [NeurovaultCollection](docs/NeurovaultCollection.md)
 - [NeurovaultCollectionFiles](docs/NeurovaultCollectionFiles.md)
 - [NeurovaultCollectionReturn](docs/NeurovaultCollectionReturn.md)
 - [NeurovaultFile](docs/NeurovaultFile.md)
 - [NeurovaultFileList](docs/NeurovaultFileList.md)
 - [NeurovaultFileReturn](docs/NeurovaultFileReturn.md)
 - [NeurovaultList](docs/NeurovaultList.md)
 - [Project](docs/Project.md)
 - [ProjectList](docs/ProjectList.md)
 - [ProjectMetaAnalyses](docs/ProjectMetaAnalyses.md)
 - [ProjectReturn](docs/ProjectReturn.md)
 - [ReadOnly](docs/ReadOnly.md)
 - [Result](docs/Result.md)
 - [ResultInit](docs/ResultInit.md)
 - [ResultList](docs/ResultList.md)
 - [ResultListResults](docs/ResultListResults.md)
 - [ResultReturn](docs/ResultReturn.md)
 - [Specification](docs/Specification.md)
 - [SpecificationConditions](docs/SpecificationConditions.md)
 - [SpecificationList](docs/SpecificationList.md)
 - [SpecificationPostBody](docs/SpecificationPostBody.md)
 - [SpecificationReturn](docs/SpecificationReturn.md)
 - [Studyset](docs/Studyset.md)
 - [StudysetList](docs/StudysetList.md)
 - [StudysetPostBody](docs/StudysetPostBody.md)
 - [StudysetReference](docs/StudysetReference.md)
 - [StudysetReferenceList](docs/StudysetReferenceList.md)
 - [StudysetReferenceReturn](docs/StudysetReferenceReturn.md)
 - [StudysetReferenceSnapshotsInner](docs/StudysetReferenceSnapshotsInner.md)
 - [StudysetReturn](docs/StudysetReturn.md)
 - [User](docs/User.md)
 - [UserList](docs/UserList.md)
 - [UserReturn](docs/UserReturn.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="JSON-Web-Token"></a>
### JSON-Web-Token

- **Type**: Bearer authentication

<a id="upload_key"></a>
### upload_key

- **Type**: API key
- **API key parameter name**: Compose-Upload-Key
- **Location**: HTTP header


## Author

jamesdkent21@gmail.com


