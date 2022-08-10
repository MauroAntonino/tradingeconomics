from pprint import pprint
from requests import get
from app.domain.entity.countries import Conutry
from app.domain.entity.data import Data
from datetime import datetime

class TradingOperations:
    
    def __init__(self) -> None:
        self.key = "a0633e553800497" # should be an env variable
        self.secret = "eneyxege75yezko"
        self.url_indicator = "https://api.tradingeconomics.com/historical/country/{country}/indicator/{indicator}/?client={KEY}:{SECRET}"
        self.all_countries = "https://api.tradingeconomics.com/country/mexico?client={KEY}:{SECRET}"
        self.proxyDict = {
            "http": "api.tradingeconomics.com"
        }
    
    def get_full_indicator_data(self, indicator, conutry):
        url = self.url_indicator.format(country=conutry.value, indicator=indicator, KEY=self.key , SECRET=self.secret)
        response_data = get(url, proxies=self.proxyDict).json()
        response_data = response_data[:len(response_data) - 1]
        data :Data  = Data(label=[], value=[])
        append_label = data.label.append
        append_valaue = data.value.append
        for item in response_data:
            datetime_object = datetime.strptime(str(item["DateTime"]), '%Y-%m-%dT%H:%M:%S')
            date = [str(datetime_object.year), " - ",  str(datetime_object.month), " - ",  str(datetime_object.day)]
            append_label("".join(date))
            append_valaue(str(item["Value"]))
        return data
    
    def get_partial_indicator_data(self, indicator, conutry):
        url = self.url_indicator.format(country=conutry.value, indicator=indicator, KEY=self.key , SECRET=self.secret)
        response_data = get(url, proxies=self.proxyDict).json() 
        response_data = response_data[:len(response_data) - 1]
        data :Data  = Data(label=[], value=[])
        append_label = data.label.append
        append_valaue = data.value.append
        for item in response_data:
            datetime_object = datetime.strptime(str(item["DateTime"]), '%Y-%m-%dT%H:%M:%S')
            date = [str(datetime_object.year)]
            append_label("".join(date))
            append_valaue(str(item["Value"]))
        return data
    
    def get_gdp(self, conutry: Conutry) -> Data:
        Indicator = "gdp"
        return self.get_full_indicator_data(Indicator, conutry)
    
    def get_population(self, conutry: Conutry) -> Data:
        Indicator = "Population"
        return self.get_partial_indicator_data(Indicator, conutry)
    
    def get_unemployment_rate(self, conutry: Conutry) -> Data:
        Indicator = "Unemployment Rate"
        return self.get_partial_indicator_data(Indicator, conutry)