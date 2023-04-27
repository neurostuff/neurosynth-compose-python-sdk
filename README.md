# neurosynth-compose-sdk
api to create a meta-analysis specification

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 0.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/jdkent](https://github.com/jdkent)

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


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

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import neurosynth_compose_sdk
from pprint import pprint
from neurosynth_compose_sdk.apis.tags import annotations_api
from neurosynth_compose_sdk.model.annotation_list import AnnotationList
from neurosynth_compose_sdk.model.annotation_post_body import AnnotationPostBody
from neurosynth_compose_sdk.model.annotation_return import AnnotationReturn
from neurosynth_compose_sdk.model.annotation_update import AnnotationUpdate
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = annotations_api.AnnotationsApi(api_client)
    
    try:
        # GET a list of annotations
        api_response = api_instance.annotations_get()
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling AnnotationsApi->annotations_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:81/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnnotationsApi* | [**annotations_get**](docs/apis/tags/AnnotationsApi.md#annotations_get) | **get** /annotations | GET a list of annotations
*AnnotationsApi* | [**annotations_id_get**](docs/apis/tags/AnnotationsApi.md#annotations_id_get) | **get** /annotations/{id} | GET information about an annotation
*AnnotationsApi* | [**annotations_id_put**](docs/apis/tags/AnnotationsApi.md#annotations_id_put) | **put** /annotations/{id} | Update an Annotation
*AnnotationsApi* | [**annotations_post**](docs/apis/tags/AnnotationsApi.md#annotations_post) | **post** /annotations | Create a new Annotation
*ComposeApi* | [**annotations_get**](docs/apis/tags/ComposeApi.md#annotations_get) | **get** /annotations | GET a list of annotations
*ComposeApi* | [**annotations_id_get**](docs/apis/tags/ComposeApi.md#annotations_id_get) | **get** /annotations/{id} | GET information about an annotation
*ComposeApi* | [**annotations_id_put**](docs/apis/tags/ComposeApi.md#annotations_id_put) | **put** /annotations/{id} | Update an Annotation
*ComposeApi* | [**annotations_post**](docs/apis/tags/ComposeApi.md#annotations_post) | **post** /annotations | Create a new Annotation
*ComposeApi* | [**meta_analyses_get**](docs/apis/tags/ComposeApi.md#meta_analyses_get) | **get** /meta-analyses | GET a list of meta-analyses
*ComposeApi* | [**meta_analyses_id_get**](docs/apis/tags/ComposeApi.md#meta_analyses_id_get) | **get** /meta-analyses/{id} | GET meta-analysis information
*ComposeApi* | [**meta_analyses_id_put**](docs/apis/tags/ComposeApi.md#meta_analyses_id_put) | **put** /meta-analyses/{id} | Update a meta-analysis
*ComposeApi* | [**meta_analyses_post**](docs/apis/tags/ComposeApi.md#meta_analyses_post) | **post** /meta-analyses | Create a new meta-analysis
*ComposeApi* | [**meta_analysis_results_get**](docs/apis/tags/ComposeApi.md#meta_analysis_results_get) | **get** /meta-analysis-results | Your GET endpoint
*ComposeApi* | [**meta_analysis_results_id_get**](docs/apis/tags/ComposeApi.md#meta_analysis_results_id_get) | **get** /meta-analysis-results/{id} | Your GET endpoint
*ComposeApi* | [**meta_analysis_results_id_put**](docs/apis/tags/ComposeApi.md#meta_analysis_results_id_put) | **put** /meta-analysis-results/{id} | 
*ComposeApi* | [**meta_analysis_results_post**](docs/apis/tags/ComposeApi.md#meta_analysis_results_post) | **post** /meta-analysis-results | 
*ComposeApi* | [**neurovault_collections_get**](docs/apis/tags/ComposeApi.md#neurovault_collections_get) | **get** /neurovault-collections | Get neurovault collections
*ComposeApi* | [**neurovault_collections_id_get**](docs/apis/tags/ComposeApi.md#neurovault_collections_id_get) | **get** /neurovault-collections/{id} | Your GET endpoint
*ComposeApi* | [**neurovault_collections_id_put**](docs/apis/tags/ComposeApi.md#neurovault_collections_id_put) | **put** /neurovault-collections/{id} | 
*ComposeApi* | [**neurovault_collections_post**](docs/apis/tags/ComposeApi.md#neurovault_collections_post) | **post** /neurovault-collections | Create neurovault collection
*ComposeApi* | [**neurovault_files_get**](docs/apis/tags/ComposeApi.md#neurovault_files_get) | **get** /neurovault-files | Your GET endpoint
*ComposeApi* | [**neurovault_files_id_get**](docs/apis/tags/ComposeApi.md#neurovault_files_id_get) | **get** /neurovault-files/{id} | Your GET endpoint
*ComposeApi* | [**neurovault_files_id_put**](docs/apis/tags/ComposeApi.md#neurovault_files_id_put) | **put** /neurovault-files/{id} | 
*ComposeApi* | [**neurovault_files_post**](docs/apis/tags/ComposeApi.md#neurovault_files_post) | **post** /neurovault-files | 
*ComposeApi* | [**projects_get**](docs/apis/tags/ComposeApi.md#projects_get) | **get** /projects | Your GET endpoint
*ComposeApi* | [**projects_id_get**](docs/apis/tags/ComposeApi.md#projects_id_get) | **get** /projects/{id} | Your GET endpoint
*ComposeApi* | [**projects_id_put**](docs/apis/tags/ComposeApi.md#projects_id_put) | **put** /projects/{id} | 
*ComposeApi* | [**projects_post**](docs/apis/tags/ComposeApi.md#projects_post) | **post** /projects | 
*ComposeApi* | [**specifications_get**](docs/apis/tags/ComposeApi.md#specifications_get) | **get** /specifications | Get a list of Specifications
*ComposeApi* | [**specifications_id_get**](docs/apis/tags/ComposeApi.md#specifications_id_get) | **get** /specifications/{id} | Get information about a Specification
*ComposeApi* | [**specifications_id_put**](docs/apis/tags/ComposeApi.md#specifications_id_put) | **put** /specifications/{id} | Update Meta-Analysis specification
*ComposeApi* | [**specifications_post**](docs/apis/tags/ComposeApi.md#specifications_post) | **post** /specifications | Create a Specification
*ComposeApi* | [**studysets_get**](docs/apis/tags/ComposeApi.md#studysets_get) | **get** /studysets | Get a list of Studysets
*ComposeApi* | [**studysets_id_get**](docs/apis/tags/ComposeApi.md#studysets_id_get) | **get** /studysets/{id} | Get information about a Studyset
*ComposeApi* | [**studysets_id_put**](docs/apis/tags/ComposeApi.md#studysets_id_put) | **put** /studysets/{id} | Update a Studyset
*ComposeApi* | [**studysets_post**](docs/apis/tags/ComposeApi.md#studysets_post) | **post** /studysets | Create a new Studyset
*DefaultApi* | [**neurostore_studies_get**](docs/apis/tags/DefaultApi.md#neurostore_studies_get) | **get** /neurostore-studies | Your GET endpoint
*DefaultApi* | [**neurostore_studies_id_get**](docs/apis/tags/DefaultApi.md#neurostore_studies_id_get) | **get** /neurostore-studies/{id} | Your GET endpoint
*DefaultApi* | [**neurostore_studies_id_put**](docs/apis/tags/DefaultApi.md#neurostore_studies_id_put) | **put** /neurostore-studies/{id} | 
*DefaultApi* | [**neurostore_studies_post**](docs/apis/tags/DefaultApi.md#neurostore_studies_post) | **post** /neurostore-studies | 
*GetApi* | [**annotations_get**](docs/apis/tags/GetApi.md#annotations_get) | **get** /annotations | GET a list of annotations
*GetApi* | [**annotations_id_get**](docs/apis/tags/GetApi.md#annotations_id_get) | **get** /annotations/{id} | GET information about an annotation
*GetApi* | [**meta_analyses_get**](docs/apis/tags/GetApi.md#meta_analyses_get) | **get** /meta-analyses | GET a list of meta-analyses
*GetApi* | [**meta_analyses_id_get**](docs/apis/tags/GetApi.md#meta_analyses_id_get) | **get** /meta-analyses/{id} | GET meta-analysis information
*GetApi* | [**meta_analysis_results_get**](docs/apis/tags/GetApi.md#meta_analysis_results_get) | **get** /meta-analysis-results | Your GET endpoint
*GetApi* | [**meta_analysis_results_id_get**](docs/apis/tags/GetApi.md#meta_analysis_results_id_get) | **get** /meta-analysis-results/{id} | Your GET endpoint
*GetApi* | [**neurovault_collections_get**](docs/apis/tags/GetApi.md#neurovault_collections_get) | **get** /neurovault-collections | Get neurovault collections
*GetApi* | [**neurovault_collections_id_get**](docs/apis/tags/GetApi.md#neurovault_collections_id_get) | **get** /neurovault-collections/{id} | Your GET endpoint
*GetApi* | [**neurovault_files_get**](docs/apis/tags/GetApi.md#neurovault_files_get) | **get** /neurovault-files | Your GET endpoint
*GetApi* | [**neurovault_files_id_get**](docs/apis/tags/GetApi.md#neurovault_files_id_get) | **get** /neurovault-files/{id} | Your GET endpoint
*GetApi* | [**projects_get**](docs/apis/tags/GetApi.md#projects_get) | **get** /projects | Your GET endpoint
*GetApi* | [**projects_id_get**](docs/apis/tags/GetApi.md#projects_id_get) | **get** /projects/{id} | Your GET endpoint
*GetApi* | [**specifications_get**](docs/apis/tags/GetApi.md#specifications_get) | **get** /specifications | Get a list of Specifications
*GetApi* | [**specifications_id_get**](docs/apis/tags/GetApi.md#specifications_id_get) | **get** /specifications/{id} | Get information about a Specification
*GetApi* | [**studysets_get**](docs/apis/tags/GetApi.md#studysets_get) | **get** /studysets | Get a list of Studysets
*GetApi* | [**studysets_id_get**](docs/apis/tags/GetApi.md#studysets_id_get) | **get** /studysets/{id} | Get information about a Studyset
*MetaAnalysesApi* | [**meta_analyses_get**](docs/apis/tags/MetaAnalysesApi.md#meta_analyses_get) | **get** /meta-analyses | GET a list of meta-analyses
*MetaAnalysesApi* | [**meta_analyses_id_get**](docs/apis/tags/MetaAnalysesApi.md#meta_analyses_id_get) | **get** /meta-analyses/{id} | GET meta-analysis information
*MetaAnalysesApi* | [**meta_analyses_id_put**](docs/apis/tags/MetaAnalysesApi.md#meta_analyses_id_put) | **put** /meta-analyses/{id} | Update a meta-analysis
*MetaAnalysesApi* | [**meta_analyses_post**](docs/apis/tags/MetaAnalysesApi.md#meta_analyses_post) | **post** /meta-analyses | Create a new meta-analysis
*MetaAnalysesApi* | [**meta_analysis_results_get**](docs/apis/tags/MetaAnalysesApi.md#meta_analysis_results_get) | **get** /meta-analysis-results | Your GET endpoint
*MetaAnalysesApi* | [**meta_analysis_results_id_get**](docs/apis/tags/MetaAnalysesApi.md#meta_analysis_results_id_get) | **get** /meta-analysis-results/{id} | Your GET endpoint
*MetaAnalysesApi* | [**meta_analysis_results_id_put**](docs/apis/tags/MetaAnalysesApi.md#meta_analysis_results_id_put) | **put** /meta-analysis-results/{id} | 
*MetaAnalysesApi* | [**meta_analysis_results_post**](docs/apis/tags/MetaAnalysesApi.md#meta_analysis_results_post) | **post** /meta-analysis-results | 
*NeurovaultApi* | [**neurovault_collections_get**](docs/apis/tags/NeurovaultApi.md#neurovault_collections_get) | **get** /neurovault-collections | Get neurovault collections
*NeurovaultApi* | [**neurovault_collections_id_get**](docs/apis/tags/NeurovaultApi.md#neurovault_collections_id_get) | **get** /neurovault-collections/{id} | Your GET endpoint
*NeurovaultApi* | [**neurovault_collections_id_put**](docs/apis/tags/NeurovaultApi.md#neurovault_collections_id_put) | **put** /neurovault-collections/{id} | 
*NeurovaultApi* | [**neurovault_collections_post**](docs/apis/tags/NeurovaultApi.md#neurovault_collections_post) | **post** /neurovault-collections | Create neurovault collection
*NeurovaultApi* | [**neurovault_files_get**](docs/apis/tags/NeurovaultApi.md#neurovault_files_get) | **get** /neurovault-files | Your GET endpoint
*NeurovaultApi* | [**neurovault_files_id_get**](docs/apis/tags/NeurovaultApi.md#neurovault_files_id_get) | **get** /neurovault-files/{id} | Your GET endpoint
*NeurovaultApi* | [**neurovault_files_id_put**](docs/apis/tags/NeurovaultApi.md#neurovault_files_id_put) | **put** /neurovault-files/{id} | 
*NeurovaultApi* | [**neurovault_files_post**](docs/apis/tags/NeurovaultApi.md#neurovault_files_post) | **post** /neurovault-files | 
*PostApi* | [**annotations_post**](docs/apis/tags/PostApi.md#annotations_post) | **post** /annotations | Create a new Annotation
*PostApi* | [**meta_analyses_post**](docs/apis/tags/PostApi.md#meta_analyses_post) | **post** /meta-analyses | Create a new meta-analysis
*PostApi* | [**meta_analysis_results_post**](docs/apis/tags/PostApi.md#meta_analysis_results_post) | **post** /meta-analysis-results | 
*PostApi* | [**neurovault_collections_post**](docs/apis/tags/PostApi.md#neurovault_collections_post) | **post** /neurovault-collections | Create neurovault collection
*PostApi* | [**neurovault_files_post**](docs/apis/tags/PostApi.md#neurovault_files_post) | **post** /neurovault-files | 
*PostApi* | [**projects_post**](docs/apis/tags/PostApi.md#projects_post) | **post** /projects | 
*PostApi* | [**specifications_post**](docs/apis/tags/PostApi.md#specifications_post) | **post** /specifications | Create a Specification
*PostApi* | [**studysets_post**](docs/apis/tags/PostApi.md#studysets_post) | **post** /studysets | Create a new Studyset
*ProjectsApi* | [**projects_get**](docs/apis/tags/ProjectsApi.md#projects_get) | **get** /projects | Your GET endpoint
*ProjectsApi* | [**projects_id_get**](docs/apis/tags/ProjectsApi.md#projects_id_get) | **get** /projects/{id} | Your GET endpoint
*ProjectsApi* | [**projects_id_put**](docs/apis/tags/ProjectsApi.md#projects_id_put) | **put** /projects/{id} | 
*ProjectsApi* | [**projects_post**](docs/apis/tags/ProjectsApi.md#projects_post) | **post** /projects | 
*PutApi* | [**annotations_id_put**](docs/apis/tags/PutApi.md#annotations_id_put) | **put** /annotations/{id} | Update an Annotation
*PutApi* | [**meta_analyses_id_put**](docs/apis/tags/PutApi.md#meta_analyses_id_put) | **put** /meta-analyses/{id} | Update a meta-analysis
*PutApi* | [**meta_analysis_results_id_put**](docs/apis/tags/PutApi.md#meta_analysis_results_id_put) | **put** /meta-analysis-results/{id} | 
*PutApi* | [**neurovault_collections_id_put**](docs/apis/tags/PutApi.md#neurovault_collections_id_put) | **put** /neurovault-collections/{id} | 
*PutApi* | [**neurovault_files_id_put**](docs/apis/tags/PutApi.md#neurovault_files_id_put) | **put** /neurovault-files/{id} | 
*PutApi* | [**projects_id_put**](docs/apis/tags/PutApi.md#projects_id_put) | **put** /projects/{id} | 
*PutApi* | [**specifications_id_put**](docs/apis/tags/PutApi.md#specifications_id_put) | **put** /specifications/{id} | Update Meta-Analysis specification
*PutApi* | [**studysets_id_put**](docs/apis/tags/PutApi.md#studysets_id_put) | **put** /studysets/{id} | Update a Studyset
*SpecificationsApi* | [**specifications_get**](docs/apis/tags/SpecificationsApi.md#specifications_get) | **get** /specifications | Get a list of Specifications
*SpecificationsApi* | [**specifications_id_get**](docs/apis/tags/SpecificationsApi.md#specifications_id_get) | **get** /specifications/{id} | Get information about a Specification
*SpecificationsApi* | [**specifications_id_put**](docs/apis/tags/SpecificationsApi.md#specifications_id_put) | **put** /specifications/{id} | Update Meta-Analysis specification
*SpecificationsApi* | [**specifications_post**](docs/apis/tags/SpecificationsApi.md#specifications_post) | **post** /specifications | Create a Specification
*StudysetsApi* | [**studysets_get**](docs/apis/tags/StudysetsApi.md#studysets_get) | **get** /studysets | Get a list of Studysets
*StudysetsApi* | [**studysets_id_get**](docs/apis/tags/StudysetsApi.md#studysets_id_get) | **get** /studysets/{id} | Get information about a Studyset
*StudysetsApi* | [**studysets_id_put**](docs/apis/tags/StudysetsApi.md#studysets_id_put) | **put** /studysets/{id} | Update a Studyset
*StudysetsApi* | [**studysets_post**](docs/apis/tags/StudysetsApi.md#studysets_post) | **post** /studysets | Create a new Studyset
*UsersApi* | [**users_get**](docs/apis/tags/UsersApi.md#users_get) | **get** /users | GET list of Users
*UsersApi* | [**users_id_get**](docs/apis/tags/UsersApi.md#users_id_get) | **get** /users/{id} | Get User Info by User ID
*UsersApi* | [**users_id_put**](docs/apis/tags/UsersApi.md#users_id_put) | **put** /users/{id} | Update User Information
*UsersApi* | [**users_post**](docs/apis/tags/UsersApi.md#users_post) | **post** /users | Create A New User

## Documentation For Models

 - [Annotation](docs/models/Annotation.md)
 - [AnnotationList](docs/models/AnnotationList.md)
 - [AnnotationPostBody](docs/models/AnnotationPostBody.md)
 - [AnnotationReturn](docs/models/AnnotationReturn.md)
 - [AnnotationUpdate](docs/models/AnnotationUpdate.md)
 - [Corrector](docs/models/Corrector.md)
 - [Estimator](docs/models/Estimator.md)
 - [MetaAnalysis](docs/models/MetaAnalysis.md)
 - [MetaAnalysisList](docs/models/MetaAnalysisList.md)
 - [MetaAnalysisPostBody](docs/models/MetaAnalysisPostBody.md)
 - [MetaAnalysisReturn](docs/models/MetaAnalysisReturn.md)
 - [NeurostoreAnalysis](docs/models/NeurostoreAnalysis.md)
 - [NeurostoreStudy](docs/models/NeurostoreStudy.md)
 - [NeurostoreStudyList](docs/models/NeurostoreStudyList.md)
 - [NeurostoreStudyReturn](docs/models/NeurostoreStudyReturn.md)
 - [NeurovaultCollection](docs/models/NeurovaultCollection.md)
 - [NeurovaultCollectionReturn](docs/models/NeurovaultCollectionReturn.md)
 - [NeurovaultFile](docs/models/NeurovaultFile.md)
 - [NeurovaultFileList](docs/models/NeurovaultFileList.md)
 - [NeurovaultFileReturn](docs/models/NeurovaultFileReturn.md)
 - [NeurovaultList](docs/models/NeurovaultList.md)
 - [Project](docs/models/Project.md)
 - [ProjectList](docs/models/ProjectList.md)
 - [ProjectReturn](docs/models/ProjectReturn.md)
 - [ReadOnly](docs/models/ReadOnly.md)
 - [Result](docs/models/Result.md)
 - [ResultInit](docs/models/ResultInit.md)
 - [ResultList](docs/models/ResultList.md)
 - [ResultReturn](docs/models/ResultReturn.md)
 - [Specification](docs/models/Specification.md)
 - [SpecificationList](docs/models/SpecificationList.md)
 - [SpecificationPostBody](docs/models/SpecificationPostBody.md)
 - [SpecificationReturn](docs/models/SpecificationReturn.md)
 - [Studyset](docs/models/Studyset.md)
 - [StudysetList](docs/models/StudysetList.md)
 - [StudysetPostBody](docs/models/StudysetPostBody.md)
 - [StudysetReturn](docs/models/StudysetReturn.md)
 - [User](docs/models/User.md)
 - [UserList](docs/models/UserList.md)
 - [UserReturn](docs/models/UserReturn.md)

## Documentation For Authorization


## JSON-Web-Token

- **Type**: Bearer authentication

 Authentication schemes defined for the API:
## run_key

- **Type**: API key
- **API key parameter name**: run_key
- **Location**: HTTP header


## Author

jamesdkent21@gmail.com
jamesdkent21@gmail.com
jamesdkent21@gmail.com
jamesdkent21@gmail.com
jamesdkent21@gmail.com
jamesdkent21@gmail.com
jamesdkent21@gmail.com
jamesdkent21@gmail.com
jamesdkent21@gmail.com
jamesdkent21@gmail.com
jamesdkent21@gmail.com
jamesdkent21@gmail.com

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in neurosynth_compose_sdk.apis and neurosynth_compose_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from neurosynth_compose_sdk.apis.default_api import DefaultApi`
- `from neurosynth_compose_sdk.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import neurosynth_compose_sdk
from neurosynth_compose_sdk.apis import *
from neurosynth_compose_sdk.models import *
```
