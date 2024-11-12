import os
import glob
import rasterio
from rasterio.merge import merge
import re

def extract_timestamp(file_name:str) -> str:
    """
    Extracts the timestamp from a filename containing a 
    Sentinel-2 raster image.

    Args:
        file_name (str): The name of the file.

    Returns:
        str: The extracted timestamp.
    """
    m = re.search(r'-_([0-9]+)', file_name)
    return m.groups()[0]

def extract_band(file_name:str) -> str:
    """
    Extracts the band from a filename containing a 
    Sentinel-2 raster image.

    Args:
        file_name (str): The name of the file.

    Returns:
        str: The extracted band, one of B02, B03, B04, B06, B08, B11.
    """
    m = re.search(r'(B[0-9]+)', file_name)
    return m.groups()[0]


def merge_tifs(path1:str, path2:str, out_path:str, meta):
    """
    Merges two tif files.

    Args:
        path1 (str): The path to the first file.
        path2 (str): The path to the second file.
        out_path (str): The path to which the result will  be stored.
        meta (dict): The metadata object of the tif file.
    """
    try:
        arr, out = merge([path1, path2])
        meta_c = meta.copy()
        meta_c.update({
            "height": arr.shape[1],
            "width": arr.shape[2],
            "transform": out
        })
        with rasterio.open(out_path, "w", **meta_c) as dest:
            dest.write(arr)
    except Exception as e:
        print(e)


def merge_tiles(filepaths: list[str], meta, out_path_base:str = "./") -> None:
    """
    Merge the corresponding pairs of tif files spread across two tiles.

    Args:
        filepaths (list[str]): List of the filepaths.
        meta (dict): The metadata object of the tif file.
        out_path_base (str): Paht to directory where results will be stored.
    """
    # map the tiles to find corresponding pairs based on band and timestamp
    data_map = {}
    for f_name in filepaths:
        timestamp = extract_timestamp(f_name)
        band = extract_band(f_name)
        data_map[timestamp] = data_map.get(timestamp, {})
        data_map[timestamp][band] = data_map.get(timestamp).get(band, []) + [f_name]  
    
    for (year, bands) in data_map.items():
        for (band, files) in bands.items():
            assert len(files) == 2
            out_path = out_path_base + year + "_" + band + ".tif"
            merge_tifs(*files, out_path=out_path, meta=meta)


def main():
    dir_path = r"/home/e12331438/shared/datasets/rs/students/e12331438/Sentinel-2/EQUI7_EU010M/*"
    filepaths = glob.glob(os.path.join(dir_path, "*"))
    with rasterio.open(filepaths[0]) as src:
        meta = src.meta.copy()
    merge_tiles(filepaths, meta, './merged/')
    

if __name__ == "__main__":
    main()
