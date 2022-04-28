# SpecificationPostBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | the type of meta-analysis being run, typically either cbma or ibma, but others may become available in the future. | 
**estimator** | [**Estimator**](Estimator.md) |  | 
**mask** | **str, none_type** | a string representing a binary nifti file to select which voxels a user wants to include in the analysis. | [optional] 
**contrast** | **str, none_type** | underspecified selection of columns to contrast (TODO, make better). | [optional] 
**transformer** | **str, none_type** | A transformation applied to column(s) (e.g., binarize based on a threshold). This is likely to become deprecated. | [optional] 
**corrector** | [**Corrector**](Corrector.md) |  | [optional] 
**filter** | **str, none_type** | a boolean column from annotations selecting which analyses to include in the meta-analysis | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


