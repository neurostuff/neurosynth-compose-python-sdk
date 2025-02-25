# NeurostoreStudyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[NeurostoreStudyReturn]**](NeurostoreStudyReturn.md) |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.neurostore_study_list import NeurostoreStudyList

# TODO update the JSON string below
json = "{}"
# create an instance of NeurostoreStudyList from a JSON string
neurostore_study_list_instance = NeurostoreStudyList.from_json(json)
# print the JSON string representation of the object
print(NeurostoreStudyList.to_json())

# convert the object into a dict
neurostore_study_list_dict = neurostore_study_list_instance.to_dict()
# create an instance of NeurostoreStudyList from a dict
neurostore_study_list_from_dict = NeurostoreStudyList.from_dict(neurostore_study_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


