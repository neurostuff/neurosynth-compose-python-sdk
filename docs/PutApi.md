# neurosynth_compose_sdk.PutApi

All URIs are relative to *http://localhost:81/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotations_id_put**](PutApi.md#annotations_id_put) | **PUT** /annotations/{id} | Update an Annotation
[**meta_analyses_id_put**](PutApi.md#meta_analyses_id_put) | **PUT** /meta-analyses/{id} | Update a meta-analysis
[**meta_analysis_results_id_put**](PutApi.md#meta_analysis_results_id_put) | **PUT** /meta-analysis-results/{id} | 
[**neurovault_collections_id_put**](PutApi.md#neurovault_collections_id_put) | **PUT** /neurovault-collections/{id} | 
[**neurovault_files_id_put**](PutApi.md#neurovault_files_id_put) | **PUT** /neurovault-files/{id} | 
[**projects_id_put**](PutApi.md#projects_id_put) | **PUT** /projects/{id} | 
[**specifications_id_put**](PutApi.md#specifications_id_put) | **PUT** /specifications/{id} | Update Meta-Analysis specification
[**studysets_id_put**](PutApi.md#studysets_id_put) | **PUT** /studysets/{id} | Update a Studyset


# **annotations_id_put**
> AnnotationReturn annotations_id_put(id)

Update an Annotation

update an existing annotation

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import put_api
from neurosynth_compose_sdk.model.annotation_update import AnnotationUpdate
from neurosynth_compose_sdk.model.annotation_return import AnnotationReturn
from neurosynth_compose_sdk.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurosynth_compose_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = put_api.PutApi(api_client)
    id = "id_example" # str | 
    annotation_update = AnnotationUpdate(None) # AnnotationUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an Annotation
        api_response = api_instance.annotations_id_put(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PutApi->annotations_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an Annotation
        api_response = api_instance.annotations_id_put(id, annotation_update=annotation_update)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PutApi->annotations_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **annotation_update** | [**AnnotationUpdate**](AnnotationUpdate.md)|  | [optional]

### Return type

[**AnnotationReturn**](AnnotationReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | form when a request goes wrong |  -  |
**401** | form when a request goes wrong |  -  |
**404** | form when a request goes wrong |  -  |
**422** | form when a request goes wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meta_analyses_id_put**
> MetaAnalysisReturn meta_analyses_id_put(id)

Update a meta-analysis

update an existing meta-analysis (that has not yet been run)

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import put_api
from neurosynth_compose_sdk.model.meta_analysis_return import MetaAnalysisReturn
from neurosynth_compose_sdk.model.inline_response400 import InlineResponse400
from neurosynth_compose_sdk.model.meta_analysis import MetaAnalysis
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurosynth_compose_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = put_api.PutApi(api_client)
    id = "id_example" # str | 
    meta_analysis = MetaAnalysis(
        specification=None,
        studyset=None,
        annotation=None,
        name="name_example",
        description="description_example",
        internal_studyset_id="internal_studyset_id_example",
        internal_annotation_id="internal_annotation_id_example",
        results=[
            None,
        ],
        provenance={},
        project="project_example",
    ) # MetaAnalysis |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a meta-analysis
        api_response = api_instance.meta_analyses_id_put(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PutApi->meta_analyses_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a meta-analysis
        api_response = api_instance.meta_analyses_id_put(id, meta_analysis=meta_analysis)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PutApi->meta_analyses_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **meta_analysis** | [**MetaAnalysis**](MetaAnalysis.md)|  | [optional]

### Return type

[**MetaAnalysisReturn**](MetaAnalysisReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | form when a request goes wrong |  -  |
**401** | form when a request goes wrong |  -  |
**404** | form when a request goes wrong |  -  |
**422** | form when a request goes wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meta_analysis_results_id_put**
> ResultReturn meta_analysis_results_id_put(id)



### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import put_api
from neurosynth_compose_sdk.model.result_return import ResultReturn
from neurosynth_compose_sdk.model.result import Result
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = put_api.PutApi(api_client)
    id = "id_example" # str | 
    result = Result(
        images={},
        meta_analysis_id="meta_analysis_id_example",
        cli_version="cli_version_example",
        estimator=Estimator(
            type="MKDADensity",
            args={},
        ),
        neurostore_id="neurostore_id_example",
        neurovault_collection=NeurovaultCollection(
            files=[
                None,
            ],
        ),
    ) # Result |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.meta_analysis_results_id_put(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PutApi->meta_analysis_results_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.meta_analysis_results_id_put(id, result=result)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PutApi->meta_analysis_results_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **result** | [**Result**](Result.md)|  | [optional]

### Return type

[**ResultReturn**](ResultReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurovault_collections_id_put**
> NeurovaultCollectionReturn neurovault_collections_id_put(id)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import put_api
from neurosynth_compose_sdk.model.neurovault_collection_return import NeurovaultCollectionReturn
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurosynth_compose_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = put_api.PutApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.neurovault_collections_id_put(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PutApi->neurovault_collections_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**NeurovaultCollectionReturn**](NeurovaultCollectionReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurovault_files_id_put**
> NeurovaultFileReturn neurovault_files_id_put(id)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import put_api
from neurosynth_compose_sdk.model.neurovault_file_return import NeurovaultFileReturn
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurosynth_compose_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = put_api.PutApi(api_client)
    id = "id_example" # str | 
    collection_id = "collection_id_example" # str |  (optional)
    exception = "exception_example" # str, none_type |  (optional)
    traceback = "traceback_example" # str, none_type |  (optional)
    status = "status_example" # str |  (optional)
    file = 'YQ==' # str |  (optional)
    image_id = "image_id_example" # str, none_type |  (optional)
    name = "name_example" # str, none_type |  (optional)
    map_type = "map_type_example" # str, none_type |  (optional)
    cognitive_contrast_cogatlas = "cognitive_contrast_cogatlas_example" # str, none_type |  (optional)
    cognitive_contrast_cogatlas_id = "cognitive_contrast_cogatlas_id_example" # str, none_type |  (optional)
    cognitive_paradigm_cogatlas = "cognitive_paradigm_cogatlas_example" # str, none_type |  (optional)
    cognitive_paradigm_cogatlas_id = "cognitive_paradigm_cogatlas_id_example" # str, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.neurovault_files_id_put(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PutApi->neurovault_files_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.neurovault_files_id_put(id, collection_id=collection_id, exception=exception, traceback=traceback, status=status, file=file, image_id=image_id, name=name, map_type=map_type, cognitive_contrast_cogatlas=cognitive_contrast_cogatlas, cognitive_contrast_cogatlas_id=cognitive_contrast_cogatlas_id, cognitive_paradigm_cogatlas=cognitive_paradigm_cogatlas, cognitive_paradigm_cogatlas_id=cognitive_paradigm_cogatlas_id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PutApi->neurovault_files_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **collection_id** | **str**|  | [optional]
 **exception** | **str, none_type**|  | [optional]
 **traceback** | **str, none_type**|  | [optional]
 **status** | **str**|  | [optional]
 **file** | **str**|  | [optional]
 **image_id** | **str, none_type**|  | [optional]
 **name** | **str, none_type**|  | [optional]
 **map_type** | **str, none_type**|  | [optional]
 **cognitive_contrast_cogatlas** | **str, none_type**|  | [optional]
 **cognitive_contrast_cogatlas_id** | **str, none_type**|  | [optional]
 **cognitive_paradigm_cogatlas** | **str, none_type**|  | [optional]
 **cognitive_paradigm_cogatlas_id** | **str, none_type**|  | [optional]

### Return type

[**NeurovaultFileReturn**](NeurovaultFileReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_id_put**
> ProjectReturn projects_id_put(id)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import put_api
from neurosynth_compose_sdk.model.project import Project
from neurosynth_compose_sdk.model.project_return import ProjectReturn
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurosynth_compose_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = put_api.PutApi(api_client)
    id = "id_example" # str | 
    project = Project(
        provenance={},
        meta_analyses=[
            None,
        ],
        name="name_example",
        description="description_example",
    ) # Project |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.projects_id_put(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PutApi->projects_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.projects_id_put(id, project=project)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PutApi->projects_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **project** | [**Project**](Project.md)|  | [optional]

### Return type

[**ProjectReturn**](ProjectReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specifications_id_put**
> SpecificationReturn specifications_id_put(id)

Update Meta-Analysis specification

update an existing meta analysis specification

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import put_api
from neurosynth_compose_sdk.model.inline_response400 import InlineResponse400
from neurosynth_compose_sdk.model.specification import Specification
from neurosynth_compose_sdk.model.specification_return import SpecificationReturn
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurosynth_compose_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = put_api.PutApi(api_client)
    id = "id_example" # str | 
    specification = Specification(
        type="type_example",
        estimator=Estimator(
            type="MKDADensity",
            args={},
        ),
        mask="mask_example",
        contrast="contrast_example",
        transformer="transformer_example",
        corrector=Corrector(
            type="FWECorrector",
            args={},
        ),
        filter="filter_example",
    ) # Specification |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Meta-Analysis specification
        api_response = api_instance.specifications_id_put(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PutApi->specifications_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Meta-Analysis specification
        api_response = api_instance.specifications_id_put(id, specification=specification)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PutApi->specifications_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **specification** | [**Specification**](Specification.md)|  | [optional]

### Return type

[**SpecificationReturn**](SpecificationReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | form when a request goes wrong |  -  |
**401** | form when a request goes wrong |  -  |
**404** | form when a request goes wrong |  -  |
**422** | form when a request goes wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studysets_id_put**
> StudysetReturn studysets_id_put(id)

Update a Studyset

update an existing serialized/referenced studyset

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import put_api
from neurosynth_compose_sdk.model.studyset_return import StudysetReturn
from neurosynth_compose_sdk.model.inline_response400 import InlineResponse400
from neurosynth_compose_sdk.model.studyset import Studyset
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurosynth_compose_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = put_api.PutApi(api_client)
    id = "id_example" # str | 
    studyset = Studyset(
        neurostore_id="neurostore_id_example",
        snapshot={},
    ) # Studyset |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Studyset
        api_response = api_instance.studysets_id_put(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PutApi->studysets_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Studyset
        api_response = api_instance.studysets_id_put(id, studyset=studyset)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PutApi->studysets_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **studyset** | [**Studyset**](Studyset.md)|  | [optional]

### Return type

[**StudysetReturn**](StudysetReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | form when a request goes wrong |  -  |
**404** | form when a request goes wrong |  -  |
**422** | form when a request goes wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

