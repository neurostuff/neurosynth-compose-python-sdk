# TagReturn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Case-insensitive unique name within the tag scope (user or global). | 
**group** | **str** | Optional grouping key to categorize tags (case-insensitive exact match in queries). | [optional] 
**description** | **str** |  | [optional] 
**official** | **bool** |  | [optional] 
**id** | **str** | the identifier for the resource. | [optional] 
**updated_at** | **datetime** | when the resource was last modified. | [optional] [readonly] 
**created_at** | **datetime** | When the resource was created. | [optional] [readonly] 
**user** | **str** | Who owns the resource. | [optional] 
**username** | **str** |  | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.tag_return import TagReturn

# TODO update the JSON string below
json = "{}"
# create an instance of TagReturn from a JSON string
tag_return_instance = TagReturn.from_json(json)
# print the JSON string representation of the object
print(TagReturn.to_json())

# convert the object into a dict
tag_return_dict = tag_return_instance.to_dict()
# create an instance of TagReturn from a dict
tag_return_from_dict = TagReturn.from_dict(tag_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


