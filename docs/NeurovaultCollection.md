# NeurovaultCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** |  | [optional] [readonly] 
**files** | [**NeurovaultCollectionFiles**](NeurovaultCollectionFiles.md) |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.neurovault_collection import NeurovaultCollection

# TODO update the JSON string below
json = "{}"
# create an instance of NeurovaultCollection from a JSON string
neurovault_collection_instance = NeurovaultCollection.from_json(json)
# print the JSON string representation of the object
print(NeurovaultCollection.to_json())

# convert the object into a dict
neurovault_collection_dict = neurovault_collection_instance.to_dict()
# create an instance of NeurovaultCollection from a dict
neurovault_collection_from_dict = NeurovaultCollection.from_dict(neurovault_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


