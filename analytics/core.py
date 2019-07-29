class FIRMS_MODIS_RegionDataUrl:
    Regions = {
    'World' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_Global_24h.csv',
    'Canada' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_Canada_24h.csv',
    'CentralAmerica' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_Central_America_24h.csv',
    'SouthAmerica' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_South_America_24h.csv',
    'Europe' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_Europe_24h.csv',
    'NorthAndCentralAfrica' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_Northern_and_Central_Africa_24h.csv',
    'SouthernAfrica' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_Southern_Africa_24h.csv',
    'RussiaAndAsia' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_Russia_and_Asia_24h.csv',
    'SouthAsia' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_South_Asia_24h.csv',
    'SouthEastAsia' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_SouthEast_Asia_24h.csv',
    'AustraliaAndNewZealand' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_Australia_and_New_Zealand_24h.csv',
    }

class FIRMS_VIIRS_RegionDataUrl:

    Regions = {
    'World' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/csv/VNP14IMGTDL_NRT_Global_24h.csv',
    'Canada' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/csv/VNP14IMGTDL_NRT_Canada_24h.csv',
    'CentralAmerica' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/csv/VNP14IMGTDL_NRT_Central_America_24h.csv',
    'SouthAmerica' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/csv/VNP14IMGTDL_NRT_South_America_24h.csv',
    'Europe' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/csv/VNP14IMGTDL_NRT_Europe_24h.csv',
    'NorthAndCentralAfrica' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/csv/VNP14IMGTDL_NRT_Northern_and_Central_Africa_24h.csv',
    'SouthernAfrica' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/csv/VNP14IMGTDL_NRT_Southern_Africa_24h.csv',
    'RussiaAndAsia' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/csv/VNP14IMGTDL_NRT_Russia_and_Asia_24h.csv',
    'SouthAsia' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/csv/VNP14IMGTDL_NRT_South_Asia_24h.csv',
    'SouthEastAsia' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/csv/VNP14IMGTDL_NRT_SouthEast_Asia_24h.csv',
    'AustraliaAndNewZealand' : 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/csv/VNP14IMGTDL_NRT_Australia_and_New_Zealand_24h.csv'
    }


class FIRMSDataProductNames:

    VIIRS = 'VIIRS'
    MODIS = 'MODIS'

class FIRMSTimeWindows:

    H_24 = 24
    H_48 = 48
    H_72 = 72


class FIRMSDatasetUrlFactory:
    pass