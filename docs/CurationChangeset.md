# CurationChangeset

Stub changes applied together. A stub is named by its `id`. `index` is the place in the target column after the earlier changes in this changeset; 0 is the top and a negative index counts from the bottom (-1 is the last place). Added stubs without an `index` go to the top of their column in the order given.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **datetime** | the project&#39;s &#x60;updated_at&#x60; the client last saw; a project that has changed since is refused with 409 | [optional] 
**remove** | **List[str]** | ids of stubs to delete | [optional] 
**add** | [**List[CurationChangesetAddInner]**](CurationChangesetAddInner.md) |  | [optional] 
**update** | [**List[CurationStub]**](CurationStub.md) | each item names a stub by &#x60;id&#x60;; its other keys replace that stub&#39;s keys | [optional] 
**move** | [**List[CurationChangesetMoveInner]**](CurationChangesetMoveInner.md) |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.curation_changeset import CurationChangeset

# TODO update the JSON string below
json = "{}"
# create an instance of CurationChangeset from a JSON string
curation_changeset_instance = CurationChangeset.from_json(json)
# print the JSON string representation of the object
print(CurationChangeset.to_json())

# convert the object into a dict
curation_changeset_dict = curation_changeset_instance.to_dict()
# create an instance of CurationChangeset from a dict
curation_changeset_from_dict = CurationChangeset.from_dict(curation_changeset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


