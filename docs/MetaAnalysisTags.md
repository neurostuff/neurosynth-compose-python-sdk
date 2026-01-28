# MetaAnalysisTags

Tags associated with this meta-analysis (use tag names or tag IDs).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from neurosynth_compose_sdk.models.meta_analysis_tags import MetaAnalysisTags

# TODO update the JSON string below
json = "{}"
# create an instance of MetaAnalysisTags from a JSON string
meta_analysis_tags_instance = MetaAnalysisTags.from_json(json)
# print the JSON string representation of the object
print(MetaAnalysisTags.to_json())

# convert the object into a dict
meta_analysis_tags_dict = meta_analysis_tags_instance.to_dict()
# create an instance of MetaAnalysisTags from a dict
meta_analysis_tags_from_dict = MetaAnalysisTags.from_dict(meta_analysis_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


