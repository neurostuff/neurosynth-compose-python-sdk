# StudysetPostBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neurostore_id** | **str** | The id of the studyset on neurostore. | 
**snapshot** | **object** | The snapshot of the studyset pending a successful run of the meta-analysis. | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.studyset_post_body import StudysetPostBody

# TODO update the JSON string below
json = "{}"
# create an instance of StudysetPostBody from a JSON string
studyset_post_body_instance = StudysetPostBody.from_json(json)
# print the JSON string representation of the object
print StudysetPostBody.to_json()

# convert the object into a dict
studyset_post_body_dict = studyset_post_body_instance.to_dict()
# create an instance of StudysetPostBody from a dict
studyset_post_body_form_dict = studyset_post_body.from_dict(studyset_post_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


