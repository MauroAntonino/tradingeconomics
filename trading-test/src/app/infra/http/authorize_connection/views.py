# Create your views here.
from django.views import View
from django.http import JsonResponse
from django.shortcuts import redirect, render
from app.infra.trading_api.trading_api import TradingOperations
from app.domain.entity.countries import Conutry

class GetSite(View):
    
    def get(self, request):
        try:
            try:
                country = request.GET["country"]
                country = Conutry.from_str(country)
            except:
                country = Conutry.MEXICO
            resp = TradingOperations().get_gdp(country)
            resp_2 = TradingOperations().get_population(country)
            resp_3 = TradingOperations().get_unemployment_rate(country)
            name = country.value
            country_name = "".join([name[:1].upper(), name[1:]])

            ctx = {
                'country': country_name,
                'labels': resp.label,
                'data': resp.value,
                'labels_2': resp_2.label,
                'data_2': resp_2.value,
                'labels_3': resp_3.label,
                'data_3': resp_3.value
            }
            return render(request, 'service/index.html', ctx)
        except Exception as ex:
            print(ex)
            return JsonResponse({"msg": "error"}, status=400)
