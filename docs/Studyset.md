# Studyset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neurostore_id** | **str** | The id of the studyset on neurostore. | [optional] 
**snapshot** | **object** | The snapshot of the studyset pending a successful run of the meta-analysis. | [optional] 
**neurostore_url** | **str** |  | [optional] [readonly] 
**version** | **str** | A string representing a labeled version of this particular studyset. | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.studyset import Studyset

# TODO update the JSON string below
json = "{}"
# create an instance of Studyset from a JSON string
studyset_instance = Studyset.from_json(json)
# print the JSON string representation of the object
print(Studyset.to_json())

# convert the object into a dict
studyset_dict = studyset_instance.to_dict()
# create an instance of Studyset from a dict
studyset_from_dict = Studyset.from_dict(studyset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


