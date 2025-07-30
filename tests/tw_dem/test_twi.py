import numpy as np
import xarray as xr

from tw_dem.twi import twi_deafrica


class TestTWIDeafrica:
    def test_types(self):
        x = np.arange(100)
        y = np.arange(100)
        dem = xr.DataArray(
            np.random.rand(100, 100),
            coords={"y": y, "x": x},
            dims=["y", "x"],
        )
        assert isinstance(twi_deafrica(dem), xr.DataArray)
