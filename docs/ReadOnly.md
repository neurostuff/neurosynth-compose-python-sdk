# ReadOnly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the identifier for the resource. | [optional] 
**updated_at** | **datetime** | when the resource was last modified. | [optional] [readonly] 
**created_at** | **datetime** | When the resource was created. | [optional] [readonly] 
**user** | **str** | The owner&#39;s Auth0 id, served only to the owner; null for anyone else, who sees &#x60;username&#x60;. | [optional] 
**username** | **str** |  | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.read_only import ReadOnly

# TODO update the JSON string below
json = "{}"
# create an instance of ReadOnly from a JSON string
read_only_instance = ReadOnly.from_json(json)
# print the JSON string representation of the object
print(ReadOnly.to_json())

# convert the object into a dict
read_only_dict = read_only_instance.to_dict()
# create an instance of ReadOnly from a dict
read_only_from_dict = ReadOnly.from_dict(read_only_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


