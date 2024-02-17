# neurosynth_compose_sdk.PostApi

All URIs are relative to *https://compose.neurosynth.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotations_post**](PostApi.md#annotations_post) | **POST** /annotations | Create a new Annotation
[**meta_analyses_post**](PostApi.md#meta_analyses_post) | **POST** /meta-analyses | Create a new meta-analysis
[**meta_analysis_results_post**](PostApi.md#meta_analysis_results_post) | **POST** /meta-analysis-results | 
[**neurostore_studies_post**](PostApi.md#neurostore_studies_post) | **POST** /neurostore-studies | 
[**neurovault_collections_post**](PostApi.md#neurovault_collections_post) | **POST** /neurovault-collections | Create neurovault collection
[**neurovault_files_post**](PostApi.md#neurovault_files_post) | **POST** /neurovault-files | 
[**projects_post**](PostApi.md#projects_post) | **POST** /projects | 
[**studysets_post**](PostApi.md#studysets_post) | **POST** /studysets | Create a new Studyset


# **annotations_post**
> AnnotationReturn annotations_post(annotation_post_body=annotation_post_body)

Create a new Annotation

create a new serialized/referenced annotation

### Example

* Bearer Authentication (JSON-Web-Token):
```python
import time
import os
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.annotation_post_body import AnnotationPostBody
from neurosynth_compose_sdk.models.annotation_return import AnnotationReturn
from neurosynth_compose_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://compose.neurosynth.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "https://compose.neurosynth.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurosynth_compose_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurosynth_compose_sdk.PostApi(api_client)
    annotation_post_body = neurosynth_compose_sdk.AnnotationPostBody() # AnnotationPostBody |  (optional)

    try:
        # Create a new Annotation
        api_response = api_instance.annotations_post(annotation_post_body=annotation_post_body)
        print("The response of PostApi->annotations_post:\n")
        pprint(api_response)
    except Exception as e:
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
> MetaAnalysisReturn meta_analyses_post(meta_analysis_post_body=meta_analysis_post_body)

Create a new meta-analysis

create a new specification, studyset, annotation bundle

### Example

* Bearer Authentication (JSON-Web-Token):
```python
import time
import os
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.meta_analysis_post_body import MetaAnalysisPostBody
from neurosynth_compose_sdk.models.meta_analysis_return import MetaAnalysisReturn
from neurosynth_compose_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://compose.neurosynth.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "https://compose.neurosynth.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurosynth_compose_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurosynth_compose_sdk.PostApi(api_client)
    meta_analysis_post_body = neurosynth_compose_sdk.MetaAnalysisPostBody() # MetaAnalysisPostBody |  (optional)

    try:
        # Create a new meta-analysis
        api_response = api_instance.meta_analyses_post(meta_analysis_post_body=meta_analysis_post_body)
        print("The response of PostApi->meta_analyses_post:\n")
        pprint(api_response)
    except Exception as e:
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
> ResultReturn meta_analysis_results_post(result_init=result_init)



### Example

* Bearer Authentication (JSON-Web-Token):
* Api Key Authentication (upload_key):
```python
import time
import os
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.result_init import ResultInit
from neurosynth_compose_sdk.models.result_return import ResultReturn
from neurosynth_compose_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://compose.neurosynth.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "https://compose.neurosynth.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurosynth_compose_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: upload_key
configuration.api_key['upload_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['upload_key'] = 'Bearer'

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurosynth_compose_sdk.PostApi(api_client)
    result_init = neurosynth_compose_sdk.ResultInit() # ResultInit |  (optional)

    try:
        # 
        api_response = api_instance.meta_analysis_results_post(result_init=result_init)
        print("The response of PostApi->meta_analysis_results_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->meta_analysis_results_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_init** | [**ResultInit**](ResultInit.md)|  | [optional] 

### Return type

[**ResultReturn**](ResultReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token), [upload_key](../README.md#upload_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurostore_studies_post**
> NeurostoreStudyReturn neurostore_studies_post()



### Example

* Bearer Authentication (JSON-Web-Token):
```python
import time
import os
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.neurostore_study_return import NeurostoreStudyReturn
from neurosynth_compose_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://compose.neurosynth.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "https://compose.neurosynth.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurosynth_compose_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurosynth_compose_sdk.PostApi(api_client)

    try:
        # 
        api_response = api_instance.neurostore_studies_post()
        print("The response of PostApi->neurostore_studies_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->neurostore_studies_post: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**NeurostoreStudyReturn**](NeurostoreStudyReturn.md)

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

# **neurovault_collections_post**
> neurovault_collections_post(neurovault_collection=neurovault_collection)

Create neurovault collection



### Example

* Bearer Authentication (JSON-Web-Token):
```python
import time
import os
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.neurovault_collection import NeurovaultCollection
from neurosynth_compose_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://compose.neurosynth.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "https://compose.neurosynth.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurosynth_compose_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurosynth_compose_sdk.PostApi(api_client)
    neurovault_collection = neurosynth_compose_sdk.NeurovaultCollection() # NeurovaultCollection |  (optional)

    try:
        # Create neurovault collection
        api_instance.neurovault_collections_post(neurovault_collection=neurovault_collection)
    except Exception as e:
        print("Exception when calling PostApi->neurovault_collections_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **neurovault_collection** | [**NeurovaultCollection**](NeurovaultCollection.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurovault_files_post**
> NeurovaultFileReturn neurovault_files_post(neurovault_file=neurovault_file)



### Example

* Bearer Authentication (JSON-Web-Token):
```python
import time
import os
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.neurovault_file import NeurovaultFile
from neurosynth_compose_sdk.models.neurovault_file_return import NeurovaultFileReturn
from neurosynth_compose_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://compose.neurosynth.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "https://compose.neurosynth.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurosynth_compose_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurosynth_compose_sdk.PostApi(api_client)
    neurovault_file = neurosynth_compose_sdk.NeurovaultFile() # NeurovaultFile |  (optional)

    try:
        # 
        api_response = api_instance.neurovault_files_post(neurovault_file=neurovault_file)
        print("The response of PostApi->neurovault_files_post:\n")
        pprint(api_response)
    except Exception as e:
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
> ProjectReturn projects_post(project=project)



### Example

* Bearer Authentication (JSON-Web-Token):
```python
import time
import os
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.project import Project
from neurosynth_compose_sdk.models.project_return import ProjectReturn
from neurosynth_compose_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://compose.neurosynth.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "https://compose.neurosynth.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurosynth_compose_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurosynth_compose_sdk.PostApi(api_client)
    project = neurosynth_compose_sdk.Project() # Project |  (optional)

    try:
        # 
        api_response = api_instance.projects_post(project=project)
        print("The response of PostApi->projects_post:\n")
        pprint(api_response)
    except Exception as e:
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

# **studysets_post**
> StudysetReturn studysets_post(studyset_post_body=studyset_post_body)

Create a new Studyset

create a new serialized/referenced studyset

### Example

* Bearer Authentication (JSON-Web-Token):
```python
import time
import os
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.studyset_post_body import StudysetPostBody
from neurosynth_compose_sdk.models.studyset_return import StudysetReturn
from neurosynth_compose_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://compose.neurosynth.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "https://compose.neurosynth.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurosynth_compose_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurosynth_compose_sdk.PostApi(api_client)
    studyset_post_body = neurosynth_compose_sdk.StudysetPostBody() # StudysetPostBody |  (optional)

    try:
        # Create a new Studyset
        api_response = api_instance.studysets_post(studyset_post_body=studyset_post_body)
        print("The response of PostApi->studysets_post:\n")
        pprint(api_response)
    except Exception as e:
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

