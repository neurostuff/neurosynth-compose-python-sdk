# ProjectTags

Tags associated with this project (use tag names or tag IDs). A name that does not match an existing tag creates a private tag owned by the caller.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from neurosynth_compose_sdk.models.project_tags import ProjectTags

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTags from a JSON string
project_tags_instance = ProjectTags.from_json(json)
# print the JSON string representation of the object
print(ProjectTags.to_json())

# convert the object into a dict
project_tags_dict = project_tags_instance.to_dict()
# create an instance of ProjectTags from a dict
project_tags_from_dict = ProjectTags.from_dict(project_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


