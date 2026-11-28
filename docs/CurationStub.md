# CurationStub

A study on a project's curation board, as the frontend writes it in `curationMetadata.columns[].stubStudies` (`id`, `title`, `authors`, `abstractText`, `exclusionTag`, `tags`, `neurostoreId` and so on).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.curation_stub import CurationStub

# TODO update the JSON string below
json = "{}"
# create an instance of CurationStub from a JSON string
curation_stub_instance = CurationStub.from_json(json)
# print the JSON string representation of the object
print(CurationStub.to_json())

# convert the object into a dict
curation_stub_dict = curation_stub_instance.to_dict()
# create an instance of CurationStub from a dict
curation_stub_from_dict = CurationStub.from_dict(curation_stub_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


