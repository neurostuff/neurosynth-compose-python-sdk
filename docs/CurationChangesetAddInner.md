# CurationChangesetAddInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stub** | [**CurationStub**](CurationStub.md) |  | 
**column_id** | **str** | the column to add to; the first column when absent | [optional] 
**index** | **int** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.curation_changeset_add_inner import CurationChangesetAddInner

# TODO update the JSON string below
json = "{}"
# create an instance of CurationChangesetAddInner from a JSON string
curation_changeset_add_inner_instance = CurationChangesetAddInner.from_json(json)
# print the JSON string representation of the object
print(CurationChangesetAddInner.to_json())

# convert the object into a dict
curation_changeset_add_inner_dict = curation_changeset_add_inner_instance.to_dict()
# create an instance of CurationChangesetAddInner from a dict
curation_changeset_add_inner_from_dict = CurationChangesetAddInner.from_dict(curation_changeset_add_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


