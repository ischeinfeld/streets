# streets
CS224W Project

Structure
- /data
  - /movement_data/quarterly - raw zipped quarterly Uber data
  - /movement_data/hourly - raw zipped hourly Uber data
  - /boeing_dataverse/states/

- /experiments
  - /graphs - graphML formatted street networks with target data
    - /speed85/san_fransisco.graphml
  - /line_graphs - graphML formatted line graph with target data
    - /speed85/san_fransisco.graphml
  - /embeddings
    - /basic - just available edge features
      - /san_fransisco.graphml
    - /recursive - with RoleX feature
    - /node2vec - ...
    - /other_embeddings - ...
  - /targets
    - /speed85 - ...
    - /other_target - ...
