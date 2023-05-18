# NeurovaultList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[NeurovaultCollectionReturn]**](NeurovaultCollectionReturn.md) |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.neurovault_list import NeurovaultList

# TODO update the JSON string below
json = "{}"
# create an instance of NeurovaultList from a JSON string
neurovault_list_instance = NeurovaultList.from_json(json)
# print the JSON string representation of the object
print NeurovaultList.to_json()

# convert the object into a dict
neurovault_list_dict = neurovault_list_instance.to_dict()
# create an instance of NeurovaultList from a dict
neurovault_list_form_dict = neurovault_list.from_dict(neurovault_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


