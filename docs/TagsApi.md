# neurosynth_compose_sdk.TagsApi

All URIs are relative to *https://compose.neurosynth.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tags_get**](TagsApi.md#tags_get) | **GET** /tags | Get a list of Tags
[**tags_id_get**](TagsApi.md#tags_id_get) | **GET** /tags/{id} | Get information about a Tag
[**tags_post**](TagsApi.md#tags_post) | **POST** /tags | Create a new Tag


# **tags_get**
> TagList tags_get(ids=ids, page=page, page_size=page_size, name=name, search=search, filter=filter, description=description, group=group, official=official, sort=sort, desc=desc, user_id=user_id)

Get a list of Tags

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.tag_list import TagList
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
    api_instance = neurosynth_compose_sdk.TagsApi(api_client)
    ids = ['ids_example'] # List[str] | choose the specific ids you wish to get (optional)
    page = 56 # int | page of results (optional)
    page_size = 56 # int | number of elements to return on a page (optional)
    name = 'name_example' # str | search the name field for a term (optional)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    filter = 'filter_example' # str | alias for search when filtering tags (optional)
    description = 'description_example' # str | search description field for a term (optional)
    group = 'group_example' # str | filter tags by group (optional)
    official = True # bool | filter tags by official flag (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    user_id = 'user_id_example' # str | user id you want to filter on (optional)

    try:
        # Get a list of Tags
        api_response = api_instance.tags_get(ids=ids, page=page, page_size=page_size, name=name, search=search, filter=filter, description=description, group=group, official=official, sort=sort, desc=desc, user_id=user_id)
        print("The response of TagsApi->tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[str]**](str.md)| choose the specific ids you wish to get | [optional] 
 **page** | **int**| page of results | [optional] 
 **page_size** | **int**| number of elements to return on a page | [optional] 
 **name** | **str**| search the name field for a term | [optional] 
 **search** | **str**| search for entries that contain the substring | [optional] 
 **filter** | **str**| alias for search when filtering tags | [optional] 
 **description** | **str**| search description field for a term | [optional] 
 **group** | **str**| filter tags by group | [optional] 
 **official** | **bool**| filter tags by official flag | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **user_id** | **str**| user id you want to filter on | [optional] 

### Return type

[**TagList**](TagList.md)

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

# **tags_id_get**
> TagReturn tags_id_get(id)

Get information about a Tag

### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.tag_return import TagReturn
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
    api_instance = neurosynth_compose_sdk.TagsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get information about a Tag
        api_response = api_instance.tags_id_get(id)
        print("The response of TagsApi->tags_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TagReturn**](TagReturn.md)

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

# **tags_post**
> TagReturn tags_post(tag=tag)

Create a new Tag

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.tag import Tag
from neurosynth_compose_sdk.models.tag_return import TagReturn
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
    api_instance = neurosynth_compose_sdk.TagsApi(api_client)
    tag = neurosynth_compose_sdk.Tag() # Tag |  (optional)

    try:
        # Create a new Tag
        api_response = api_instance.tags_post(tag=tag)
        print("The response of TagsApi->tags_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | [**Tag**](Tag.md)|  | [optional] 

### Return type

[**TagReturn**](TagReturn.md)

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

