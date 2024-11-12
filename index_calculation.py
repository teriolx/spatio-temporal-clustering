def ndmi(B08, B11):
    """
    Calculates the NDMI from the bands implementing the formula
    from https://custom-scripts.sentinel-hub.com/custom-scripts/sentinel-2/ndmi/.

    Args:
        B08 (float/df): Value(s) of the band 8.
        B11 (float/df): Value(s) of the band 11.

    Returns:
        float/df: The calculated NDMI.
    """
    return (B08 - B11) / (B08 + B11)


def ndvi(B08, B04):
    """
    Calculates the NDVI from the bands implementing the formula
    from https://custom-scripts.sentinel-hub.com/custom-scripts/sentinel-2/ndvi/.

    Args:
        B08 (float/df): Value(s) of the band 8.
        B04 (float/df): Value(s) of the band 4.

    Returns:
        float/df: The calculated NDVI.
    """
    return (B08 - B04) / (B08 + B04)


def evi(B08, B04, B02):
    """
    Calculates the NDVI from the bands implementing the formula
    from https://custom-scripts.sentinel-hub.com/sentinel-2/evi/.

    Args:
        B08 (float/df): Value(s) of the band 8.
        B04 (float/df): Value(s) of the band 4.
        B02 (float/df): Value(s) of the band 2.

    Returns:
        float/df: The calculated EVI.
    """
    return 2.5 * (B08 - B04) / ((B08 + 6.0 * B04 - 7.5 * B02) + 1.0)