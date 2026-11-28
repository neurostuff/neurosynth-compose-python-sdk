# CurationChangesetResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **datetime** |  | [optional] 
**removed** | **int** |  | [optional] 
**added** | **int** |  | [optional] 
**updated** | **int** |  | [optional] 
**moved** | **int** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.curation_changeset_result import CurationChangesetResult

# TODO update the JSON string below
json = "{}"
# create an instance of CurationChangesetResult from a JSON string
curation_changeset_result_instance = CurationChangesetResult.from_json(json)
# print the JSON string representation of the object
print(CurationChangesetResult.to_json())

# convert the object into a dict
curation_changeset_result_dict = curation_changeset_result_instance.to_dict()
# create an instance of CurationChangesetResult from a dict
curation_changeset_result_from_dict = CurationChangesetResult.from_dict(curation_changeset_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


