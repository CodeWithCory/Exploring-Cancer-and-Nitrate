

def testFunc():
  print("Called!")
def testFunc2():
  def testFunc3():
    testFunc2()

testFunc2()

## Code Graveyard

# print("\nStarting Script")

# import geopandas as gp

# df = gp.GeoDataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]}, index=list('abc'))
# # s = gp.Series([6], index=[0])

# print(df)

# df['test'] = [6, 7, 8]

# print(df)
# print(type(df["A"]))

# print("\nScript Done\n")

# import rasterio

# # with rasterio.open('data/working/nitrate_interpolated.tif') as src:
# with rasterio.open('data/working/well_nitrate.shp') as src:
#     print(src.width, src.height)
#     print(src.crs)
#     print(src.transform)
#     print(src.count)
#     print(src.indexes)


# # import gdal
# # from datetime import datetime
# # from random import getrandbits

# # #* Make a unique tag for this process
# # timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
# # randomNumber = getrandbits(32)
# # uniqueTag = f'{timestamp}{randomNumber}'

# # #* Perform IDW interpolation on well data
# # currentIdwFilePath = f'data/working/nitrate_interpolation_{uniqueTag}.tif'
# # power = 2
# # output = gdal.Grid(currentIdwFilePath,'data/working/well_nitrate.shp', algorithm=f'invdist:power={power}', zfield='nitr_con', outputBounds=[-92.90, 47.32, -86.75, 42.48])

# # print("output", output)

# import rasterio

# tif = 'data/working/nitrate_interpolation_20200223155231204838397322666.tif'

# rasterio.open(tif, 'r')
