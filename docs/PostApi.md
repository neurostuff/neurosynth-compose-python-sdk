# neurosynth_compose_sdk.PostApi

All URIs are relative to *http://localhost:81/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotations_post**](PostApi.md#annotations_post) | **POST** /annotations | Create a new Annotation
[**meta_analyses_post**](PostApi.md#meta_analyses_post) | **POST** /meta-analyses | Create a new meta-analysis
[**meta_analysis_results_post**](PostApi.md#meta_analysis_results_post) | **POST** /meta-analysis-results | 
[**neurovault_collections_post**](PostApi.md#neurovault_collections_post) | **POST** /neurovault-collections | 
[**neurovault_files_post**](PostApi.md#neurovault_files_post) | **POST** /neurovault-files | 
[**projects_post**](PostApi.md#projects_post) | **POST** /projects | 
[**specifications_post**](PostApi.md#specifications_post) | **POST** /specifications | Create a Specification
[**studysets_post**](PostApi.md#studysets_post) | **POST** /studysets | Create a new Studyset


# **annotations_post**
> AnnotationReturn annotations_post()

Create a new Annotation

create a new serialized/referenced annotation

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import post_api
from neurosynth_compose_sdk.model.annotation_return import AnnotationReturn
from neurosynth_compose_sdk.model.inline_response400 import InlineResponse400
from neurosynth_compose_sdk.model.annotation_post_body import AnnotationPostBody
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
    api_instance = post_api.PostApi(api_client)
    annotation_post_body = AnnotationPostBody(None) # AnnotationPostBody |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new Annotation
        api_response = api_instance.annotations_post(annotation_post_body=annotation_post_body)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PostApi->annotations_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_post_body** | [**AnnotationPostBody**](AnnotationPostBody.md)|  | [optional]

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
**422** | form when a request goes wrong |  -  |
**500** | form when a request goes wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meta_analyses_post**
> MetaAnalysisReturn meta_analyses_post()

Create a new meta-analysis

create a new specification, studyset, annotation bundle

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import post_api
from neurosynth_compose_sdk.model.meta_analysis_post_body import MetaAnalysisPostBody
from neurosynth_compose_sdk.model.meta_analysis_return import MetaAnalysisReturn
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
    api_instance = post_api.PostApi(api_client)
    meta_analysis_post_body = MetaAnalysisPostBody(None) # MetaAnalysisPostBody |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new meta-analysis
        api_response = api_instance.meta_analyses_post(meta_analysis_post_body=meta_analysis_post_body)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PostApi->meta_analyses_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_analysis_post_body** | [**MetaAnalysisPostBody**](MetaAnalysisPostBody.md)|  | [optional]

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
**422** | form when a request goes wrong |  -  |
**500** | form when a request goes wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meta_analysis_results_post**
> ResultReturn meta_analysis_results_post()



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import post_api
from neurosynth_compose_sdk.model.result_return import ResultReturn
from neurosynth_compose_sdk.model.result import Result
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
    api_instance = post_api.PostApi(api_client)
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
    # and optional values
    try:
        api_response = api_instance.meta_analysis_results_post(result=result)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PostApi->meta_analysis_results_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result** | [**Result**](Result.md)|  | [optional]

### Return type

[**ResultReturn**](ResultReturn.md)

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

# **neurovault_collections_post**
> neurovault_collections_post()



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import post_api
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
    api_instance = post_api.PostApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.neurovault_collections_post()
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PostApi->neurovault_collections_post: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurovault_files_post**
> NeurovaultFileReturn neurovault_files_post()



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import post_api
from neurosynth_compose_sdk.model.neurovault_file_return import NeurovaultFileReturn
from neurosynth_compose_sdk.model.neurovault_file import NeurovaultFile
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
    api_instance = post_api.PostApi(api_client)
    neurovault_file = NeurovaultFile(
        collection_id="collection_id_example",
        exception="exception_example",
        traceback="traceback_example",
        status="status_example",
        file='YQ==',
        image_id="image_id_example",
        name="name_example",
        map_type="map_type_example",
        cognitive_contrast_cogatlas="cognitive_contrast_cogatlas_example",
        cognitive_contrast_cogatlas_id="cognitive_contrast_cogatlas_id_example",
        cognitive_paradigm_cogatlas="cognitive_paradigm_cogatlas_example",
        cognitive_paradigm_cogatlas_id="cognitive_paradigm_cogatlas_id_example",
    ) # NeurovaultFile |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.neurovault_files_post(neurovault_file=neurovault_file)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PostApi->neurovault_files_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **neurovault_file** | [**NeurovaultFile**](NeurovaultFile.md)|  | [optional]

### Return type

[**NeurovaultFileReturn**](NeurovaultFileReturn.md)

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

# **projects_post**
> ProjectReturn projects_post()



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import post_api
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
    api_instance = post_api.PostApi(api_client)
    project = Project(
        provenance={},
        meta_analyses=[
            None,
        ],
        name="name_example",
        description="description_example",
    ) # Project |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.projects_post(project=project)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PostApi->projects_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **specifications_post**
> SpecificationReturn specifications_post()

Create a Specification

create a new meta-analysis specification

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import post_api
from neurosynth_compose_sdk.model.specification_post_body import SpecificationPostBody
from neurosynth_compose_sdk.model.inline_response400 import InlineResponse400
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
    api_instance = post_api.PostApi(api_client)
    specification_post_body = SpecificationPostBody(None) # SpecificationPostBody |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Specification
        api_response = api_instance.specifications_post(specification_post_body=specification_post_body)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PostApi->specifications_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification_post_body** | [**SpecificationPostBody**](SpecificationPostBody.md)|  | [optional]

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
**422** | Unprocessable Entity (WebDAV) |  -  |
**500** | form when a request goes wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studysets_post**
> StudysetReturn studysets_post()

Create a new Studyset

create a new serialized/referenced studyset

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import post_api
from neurosynth_compose_sdk.model.studyset_post_body import StudysetPostBody
from neurosynth_compose_sdk.model.studyset_return import StudysetReturn
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
    api_instance = post_api.PostApi(api_client)
    studyset_post_body = StudysetPostBody(None) # StudysetPostBody |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new Studyset
        api_response = api_instance.studysets_post(studyset_post_body=studyset_post_body)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling PostApi->studysets_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studyset_post_body** | [**StudysetPostBody**](StudysetPostBody.md)|  | [optional]

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
**400** | form when a request goes wrong |  -  |
**422** | form when a request goes wrong |  -  |
**500** | form when a request goes wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

