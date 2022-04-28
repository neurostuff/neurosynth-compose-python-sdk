# neurosynth-compose-sdk
api to create a meta-analysis specification

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 0.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/jdkent](https://github.com/jdkent)

## Requirements.

Python >=3.6

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
from neurosynth_compose_sdk.api import annotation_api
from neurosynth_compose_sdk.model.annotation_list import AnnotationList
from neurosynth_compose_sdk.model.annotation_return import AnnotationReturn
from neurosynth_compose_sdk.model.annotation_update import AnnotationUpdate
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)



# Enter a context with an instance of the API client
client = neurosynth_compose_sdk.ApiClient(configuration)

try:
    # Your GET endpoint
    api_response = client.annotation.get(
    
    )
    pprint(api_response)
except neurosynth_compose_sdk.ApiException as e:
    print("Exception when calling AnnotationApi->annotations_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:81/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnnotationApi* | [**annotations_get**](docs/AnnotationApi.md#annotations_get) | **GET** /annotations | Your GET endpoint
*AnnotationApi* | [**annotations_id_get**](docs/AnnotationApi.md#annotations_id_get) | **GET** /annotations/{id} | Your GET endpoint
*AnnotationApi* | [**annotations_id_put**](docs/AnnotationApi.md#annotations_id_put) | **PUT** /annotations/{id} | Update Annotation
*AnnotationApi* | [**annotations_post**](docs/AnnotationApi.md#annotations_post) | **POST** /annotations | Create Annotation
*BundleApi* | [**meta_analyses_get**](docs/BundleApi.md#meta_analyses_get) | **GET** /meta-analyses | Your GET endpoint
*BundleApi* | [**meta_analyses_id_get**](docs/BundleApi.md#meta_analyses_id_get) | **GET** /meta-analyses/{id} | Your GET endpoint
*BundleApi* | [**meta_analyses_id_put**](docs/BundleApi.md#meta_analyses_id_put) | **PUT** /meta-analyses/{id} | Update Bundle
*BundleApi* | [**meta_analyses_post**](docs/BundleApi.md#meta_analyses_post) | **POST** /meta-analyses | Create Bundle
*MetaAnalysisApi* | [**specifications_get**](docs/MetaAnalysisApi.md#specifications_get) | **GET** /specifications | Your GET endpoint
*MetaAnalysisApi* | [**specifications_id_get**](docs/MetaAnalysisApi.md#specifications_id_get) | **GET** /specifications/{id} | Your GET endpoint
*MetaAnalysisApi* | [**specifications_id_put**](docs/MetaAnalysisApi.md#specifications_id_put) | **PUT** /specifications/{id} | Update Meta-Analysis specification
*MetaAnalysisApi* | [**specifications_post**](docs/MetaAnalysisApi.md#specifications_post) | **POST** /specifications | 
*StudysetApi* | [**studysets_get**](docs/StudysetApi.md#studysets_get) | **GET** /studysets | Your GET endpoint
*StudysetApi* | [**studysets_id_get**](docs/StudysetApi.md#studysets_id_get) | **GET** /studysets/{id} | Your GET endpoint
*StudysetApi* | [**studysets_id_put**](docs/StudysetApi.md#studysets_id_put) | **PUT** /studysets/{id} | Update Studyset
*StudysetApi* | [**studysets_post**](docs/StudysetApi.md#studysets_post) | **POST** /studysets | Create Studyset
*UserApi* | [**users_get**](docs/UserApi.md#users_get) | **GET** /users | 
*UserApi* | [**users_id_get**](docs/UserApi.md#users_id_get) | **GET** /users/{id} | Get User Info by User ID
*UserApi* | [**users_id_put**](docs/UserApi.md#users_id_put) | **PUT** /users/{id} | Update User Information
*UserApi* | [**users_post**](docs/UserApi.md#users_post) | **POST** /users | Create A New User


## Documentation For Models

 - [Annotation](docs/Annotation.md)
 - [AnnotationList](docs/AnnotationList.md)
 - [AnnotationReturn](docs/AnnotationReturn.md)
 - [AnnotationUpdate](docs/AnnotationUpdate.md)
 - [AnnotationUpdateAllOf](docs/AnnotationUpdateAllOf.md)
 - [Corrector](docs/Corrector.md)
 - [Estimator](docs/Estimator.md)
 - [InlineResponse400](docs/InlineResponse400.md)
 - [MetaAnalysis](docs/MetaAnalysis.md)
 - [MetaAnalysisList](docs/MetaAnalysisList.md)
 - [MetaAnalysisReturn](docs/MetaAnalysisReturn.md)
 - [ReadOnly](docs/ReadOnly.md)
 - [Specification](docs/Specification.md)
 - [SpecificationList](docs/SpecificationList.md)
 - [SpecificationPostBody](docs/SpecificationPostBody.md)
 - [SpecificationReturn](docs/SpecificationReturn.md)
 - [Studyset](docs/Studyset.md)
 - [StudysetList](docs/StudysetList.md)
 - [StudysetReturn](docs/StudysetReturn.md)
 - [User](docs/User.md)
 - [UserList](docs/UserList.md)
 - [UserReturn](docs/UserReturn.md)


## Documentation For Authorization


## JSON-Web-Token

- **Type**: Bearer authentication


## Author

jamesdkent21@gmail.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in neurosynth_compose_sdk.apis and neurosynth_compose_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from neurosynth_compose_sdk.api.default_api import DefaultApi`
- `from neurosynth_compose_sdk.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import neurosynth_compose_sdk
from neurosynth_compose_sdk.apis import *
from neurosynth_compose_sdk.models import *
```

