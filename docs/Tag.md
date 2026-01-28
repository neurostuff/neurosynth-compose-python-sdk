# Tag

A user-scoped or global label that can be attached to multiple resources. Tag groups are free-form categories (e.g., \"visibility\", \"topic\") used to segment tags across different resource types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Case-insensitive unique name within the tag scope (user or global). | 
**group** | **str** | Optional grouping key to categorize tags (case-insensitive exact match in queries). | [optional] 
**description** | **str** |  | [optional] 
**official** | **bool** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.tag import Tag

# TODO update the JSON string below
json = "{}"
# create an instance of Tag from a JSON string
tag_instance = Tag.from_json(json)
# print the JSON string representation of the object
print(Tag.to_json())

# convert the object into a dict
tag_dict = tag_instance.to_dict()
# create an instance of Tag from a dict
tag_from_dict = Tag.from_dict(tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


