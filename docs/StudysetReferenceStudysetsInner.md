# StudysetReferenceStudysetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Compose snapshot studyset identifier. | [optional] 
**md5** | **str** | Canonical md5 hash of the snapshot payload. | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.studyset_reference_studysets_inner import StudysetReferenceStudysetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of StudysetReferenceStudysetsInner from a JSON string
studyset_reference_studysets_inner_instance = StudysetReferenceStudysetsInner.from_json(json)
# print the JSON string representation of the object
print(StudysetReferenceStudysetsInner.to_json())

# convert the object into a dict
studyset_reference_studysets_inner_dict = studyset_reference_studysets_inner_instance.to_dict()
# create an instance of StudysetReferenceStudysetsInner from a dict
studyset_reference_studysets_inner_from_dict = StudysetReferenceStudysetsInner.from_dict(studyset_reference_studysets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


