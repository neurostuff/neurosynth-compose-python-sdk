# neurosynth_compose_sdk.ProjectsApi

All URIs are relative to *https://compose.neurosynth.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_get**](ProjectsApi.md#projects_get) | **GET** /projects | Your GET endpoint
[**projects_id_delete**](ProjectsApi.md#projects_id_delete) | **DELETE** /projects/{id} | 
[**projects_id_get**](ProjectsApi.md#projects_id_get) | **GET** /projects/{id} | Your GET endpoint
[**projects_id_put**](ProjectsApi.md#projects_id_put) | **PUT** /projects/{id} | 
[**projects_post**](ProjectsApi.md#projects_post) | **POST** /projects | 


# **projects_get**
> ProjectList projects_get(page=page, page_size=page_size, name=name, search=search, description=description, sort=sort, desc=desc, user_id=user_id)

Your GET endpoint

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.project_list import ProjectList
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
    api_instance = neurosynth_compose_sdk.ProjectsApi(api_client)
    page = 56 # int | page of results (optional)
    page_size = 56 # int | number of elements to return on a page (optional)
    name = 'name_example' # str | search the name field for a term (optional)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    description = 'description_example' # str | search description field for a term (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    user_id = 'user_id_example' # str | user id you want to filter on (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.projects_get(page=page, page_size=page_size, name=name, search=search, description=description, sort=sort, desc=desc, user_id=user_id)
        print("The response of ProjectsApi->projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page of results | [optional] 
 **page_size** | **int**| number of elements to return on a page | [optional] 
 **name** | **str**| search the name field for a term | [optional] 
 **search** | **str**| search for entries that contain the substring | [optional] 
 **description** | **str**| search description field for a term | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **user_id** | **str**| user id you want to filter on | [optional] 

### Return type

[**ProjectList**](ProjectList.md)

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

# **projects_id_delete**
> projects_id_delete(id)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
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
    api_instance = neurosynth_compose_sdk.ProjectsApi(api_client)
    id = 'id_example' # str | 

    try:
        # 
        api_instance.projects_id_delete(id)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_id_get**
> ProjectReturn projects_id_get(id, info=info)

Your GET endpoint

### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.project_return import ProjectReturn
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
    api_instance = neurosynth_compose_sdk.ProjectsApi(api_client)
    id = 'id_example' # str | 
    info = True # bool | display additional information about a nested relationship without displaying fully nested object (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.projects_id_get(id, info=info)
        print("The response of ProjectsApi->projects_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **info** | **bool**| display additional information about a nested relationship without displaying fully nested object | [optional] 

### Return type

[**ProjectReturn**](ProjectReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_id_put**
> ProjectReturn projects_id_put(id, project=project)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
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
    api_instance = neurosynth_compose_sdk.ProjectsApi(api_client)
    id = 'id_example' # str | 
    project = neurosynth_compose_sdk.Project() # Project |  (optional)

    try:
        # 
        api_response = api_instance.projects_id_put(id, project=project)
        print("The response of ProjectsApi->projects_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_id_put: %s\n" % e)
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

# **projects_post**
> ProjectReturn projects_post(source_id=source_id, copy_annotations=copy_annotations, project=project)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
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
    api_instance = neurosynth_compose_sdk.ProjectsApi(api_client)
    source_id = 'source_id_example' # str | clone an existing project when creating a new project (optional)
    copy_annotations = True # bool | when cloning via `source_id`, also duplicate associated annotations (optional)
    project = neurosynth_compose_sdk.Project() # Project |  (optional)

    try:
        # 
        api_response = api_instance.projects_post(source_id=source_id, copy_annotations=copy_annotations, project=project)
        print("The response of ProjectsApi->projects_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| clone an existing project when creating a new project | [optional] 
 **copy_annotations** | **bool**| when cloning via &#x60;source_id&#x60;, also duplicate associated annotations | [optional] 
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

