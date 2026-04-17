# MetaAnalysisNeurostoreAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neurostore_id** | **str** | the id of the annotation on neurostore | [optional] 
**snapshot** | **object** | the snapshot taken of the annotation pending a successful run of the meta-analytic algorithm | [optional] 
**snapshot_studyset** | [**StudysetSnapshotSummary**](StudysetSnapshotSummary.md) |  | [optional] 
**neurostore_url** | **str** |  | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.meta_analysis_neurostore_annotation import MetaAnalysisNeurostoreAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of MetaAnalysisNeurostoreAnnotation from a JSON string
meta_analysis_neurostore_annotation_instance = MetaAnalysisNeurostoreAnnotation.from_json(json)
# print the JSON string representation of the object
print(MetaAnalysisNeurostoreAnnotation.to_json())

# convert the object into a dict
meta_analysis_neurostore_annotation_dict = meta_analysis_neurostore_annotation_instance.to_dict()
# create an instance of MetaAnalysisNeurostoreAnnotation from a dict
meta_analysis_neurostore_annotation_from_dict = MetaAnalysisNeurostoreAnnotation.from_dict(meta_analysis_neurostore_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


