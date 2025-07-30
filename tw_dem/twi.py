"""Calculate Topographic Wetness Index."""

import numpy as np
import richdem as rd
import xarray as xr


def twi_deafrica(input_dem: xr.DataArray) -> xr.DataArray:
    """Calculate TWI using the methods developed for Digital Earth Africa.

    Args:
        input_dem: A dem

    Returns:
        TWI

    """
    filled_dem_rd = rd.rdarray(input_dem, no_data=-9999)

    # Compute slope and flow accumulation
    degrees_slope = rd.TerrainAttribute(filled_dem_rd, attrib="slope_radians")
    accum_d8 = rd.FlowAccumulation(filled_dem_rd, method="D8")

    # Compute Topographic Wetness Index (TWI)
    twi = np.log(accum_d8 / (np.tan(degrees_slope) + 0.01)).astype(np.float32)
    output = xr.zeros_like(input_dem)
    output.values = twi
    return output
