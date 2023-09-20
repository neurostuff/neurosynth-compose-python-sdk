# StudysetReferenceList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[StudysetReferenceReturn]**](StudysetReferenceReturn.md) |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.studyset_reference_list import StudysetReferenceList

# TODO update the JSON string below
json = "{}"
# create an instance of StudysetReferenceList from a JSON string
studyset_reference_list_instance = StudysetReferenceList.from_json(json)
# print the JSON string representation of the object
print StudysetReferenceList.to_json()

# convert the object into a dict
studyset_reference_list_dict = studyset_reference_list_instance.to_dict()
# create an instance of StudysetReferenceList from a dict
studyset_reference_list_form_dict = studyset_reference_list.from_dict(studyset_reference_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


