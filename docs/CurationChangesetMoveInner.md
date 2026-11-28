# CurationChangesetMoveInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**column_id** | **str** |  | 
**index** | **int** |  | [optional] [default to 0]

## Example

```python
from neurosynth_compose_sdk.models.curation_changeset_move_inner import CurationChangesetMoveInner

# TODO update the JSON string below
json = "{}"
# create an instance of CurationChangesetMoveInner from a JSON string
curation_changeset_move_inner_instance = CurationChangesetMoveInner.from_json(json)
# print the JSON string representation of the object
print(CurationChangesetMoveInner.to_json())

# convert the object into a dict
curation_changeset_move_inner_dict = curation_changeset_move_inner_instance.to_dict()
# create an instance of CurationChangesetMoveInner from a dict
curation_changeset_move_inner_from_dict = CurationChangesetMoveInner.from_dict(curation_changeset_move_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


