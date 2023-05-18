# NeurovaultCollectionReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** |  | [optional] [readonly] 
**files** | [**List[NeurovaultCollectionFilesInner]**](NeurovaultCollectionFilesInner.md) |  | [optional] 
**result** | **str** |  | [optional] [readonly] 
**id** | **str** | the identifier for the resource. | [optional] 
**updated_at** | **datetime** | when the resource was last modified. | [optional] [readonly] 
**created_at** | **datetime** | When the resource was created. | [optional] [readonly] 
**user** | **str** | Who owns the resource. | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.neurovault_collection_return import NeurovaultCollectionReturn

# TODO update the JSON string below
json = "{}"
# create an instance of NeurovaultCollectionReturn from a JSON string
neurovault_collection_return_instance = NeurovaultCollectionReturn.from_json(json)
# print the JSON string representation of the object
print NeurovaultCollectionReturn.to_json()

# convert the object into a dict
neurovault_collection_return_dict = neurovault_collection_return_instance.to_dict()
# create an instance of NeurovaultCollectionReturn from a dict
neurovault_collection_return_form_dict = neurovault_collection_return.from_dict(neurovault_collection_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


