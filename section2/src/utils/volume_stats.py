"""
Contains various functions for computing statistics over 3D volumes
"""
import numpy as np

def Dice3d(a, b):
    """
    This will compute the Dice Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks -
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    intersection = np.sum((a>0) * (b>0))
    volumes = np.sum(a>0) + np.sum(b>0)

    if volumes == 0:
        return -1

    return 2.*float(intersection) / float(volumes)

def Jaccard3d(a, b):
    """
    This will compute the Jaccard Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks - 
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")
        
    intersection = sum([1 if (a[x, y, z] != 0 and b[x, y, z] != 0) else 0 for x in range(a.shape[0]) for y in range(a.shape[1]) for z in range(a.shape[2])])
    union = sum([1 if (a[x, y, z] != 0 or b[x, y, z] != 0) else 0 for x in range(a.shape[0]) for y in range(a.shape[1]) for z in range(a.shape[2])])
    
#     intersection = np.sum((a>0) * (b>0))
#     union = np.sum(((a>0) + (b>0))>0)
    
    if union == 0:
        return -1
    
    return float(intersection) / float(union)