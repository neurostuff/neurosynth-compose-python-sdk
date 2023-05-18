# StudysetList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[StudysetReturn]**](StudysetReturn.md) |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.studyset_list import StudysetList

# TODO update the JSON string below
json = "{}"
# create an instance of StudysetList from a JSON string
studyset_list_instance = StudysetList.from_json(json)
# print the JSON string representation of the object
print StudysetList.to_json()

# convert the object into a dict
studyset_list_dict = studyset_list_instance.to_dict()
# create an instance of StudysetList from a dict
studyset_list_form_dict = studyset_list.from_dict(studyset_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


