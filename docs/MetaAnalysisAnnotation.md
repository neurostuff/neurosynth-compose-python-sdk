# MetaAnalysisAnnotation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neurostore_id** | **str** | the id of the annotation on neurostore | [optional] 
**snapshot** | **object** | the snapshot taken of the annotation pending a successful run of the meta-analytic algorithm | [optional] 
**studyset** | **str** | The related studyset to this annotation. | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.meta_analysis_annotation import MetaAnalysisAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of MetaAnalysisAnnotation from a JSON string
meta_analysis_annotation_instance = MetaAnalysisAnnotation.from_json(json)
# print the JSON string representation of the object
print MetaAnalysisAnnotation.to_json()

# convert the object into a dict
meta_analysis_annotation_dict = meta_analysis_annotation_instance.to_dict()
# create an instance of MetaAnalysisAnnotation from a dict
meta_analysis_annotation_form_dict = meta_analysis_annotation.from_dict(meta_analysis_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


