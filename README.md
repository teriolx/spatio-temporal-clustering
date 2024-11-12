# Spatial and Temporal Clustering of the Reed Belt of Lake Neusiedl Using Optical Remote Sensing Data

Remote sensing technology allows us to monitor the earth’s surface and observe the trends
and changes over time. This project aims to explore the potential of optical satellite images
captured by the Sentinel-2 satellite to distinguish different reed types (young, old, broken,
inundated) in the reed belt of Lake Neusiedl. Two unsupervised machine learning methods
are applied: temporal and spatial clustering. In the first approach, the data from images is
converted into time series by sampling random points from the observed area and extracting
features by calculating indices from the bands’ raw values. The second method operates with
the spatial layout of the values represented by the pixels of the images themselves to determine
the clusters based on the spatial context.

# Project Structure

- `merge_tiles.py` - script to merge multiple GeoTIFF files containing the rasters from the Sentinel-2 data, the file pairs to be merged represent adjacent tiles of the same observation identified by the timestamp
- `index_calculation.py` - implementation of the formulas to calculate the indices NDMI, NDVI, and EVI from the raw bands
- `temporal_clustering.ipynb` - temporal clustering of randomly sampled points along the reed belt using various algorithms/implementation
- `spatial_clustering.ipynb` - spatial clustering of all the points of the reed belt

# Data

The data used to obtain the cell outputs in the notebook is not part of this repository. In the environment where the results were obtained, the raw data was first preprocessed using the `merge_tiles.py` script and stored in the `merged` folder which was then used as the path to the data in the notebooks.


# Quick start

The necessary dependencies to run the code can be installed directly from the [`requirements.txt`](requirements.txt) file or using a virtual environment with conda.

```
conda create -n st-clustering python=3.10
conda activate st-clustering
pip install -r requirements.txt
```

From raw data which contains multiple tiles of the bands observed at different timestamps obtain merged GeoTIFF files by applying the `merge_tiles.py` script adjusted for actual paths of data and save the output to an output folder for example `merged`, which is then specified at the start of each notebook.

