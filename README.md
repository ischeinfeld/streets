# streets
CS224W Project

Structure
- /data/movement_data/quarterly - raw zipped quarterly Uber data
- /data/movement_data/hourly - raw zipped hourly Uber data
- /data/boeing_dataverse/states/

- /experiments
  - /preprocessed - graphML formatted network's with target data
    - /speed85/san_fransisco.graphml - networks with target speed85
    - /other_target - ...
  - /embeddings
    - /basic - just available edge features
    - /recursive - with RoleX feature
    - /node2vec - ...
    - /other_embeddings - ...
  - /targets
    - /speed85 - ...
    - /other_target - ...
