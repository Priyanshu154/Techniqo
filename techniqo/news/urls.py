from django.urls import path,include
from . import views


urlpatterns = [
   path('', views.index),
   path('industry',views.industry),

   path('auto/auto_news', views.auto_news),
   path('auto/cars', views.auto_cars),
   path('auto/two_n_three_wheel', views.auto_two_three),
   path('auto/lcv_n_hcv', views.auto_lcv_hcv),
   path('auto/auto_components', views.auto_components),
   path('auto/tyres', views.auto_tyres),

   path('banking/banking', views.banking_banking),
   path('banking/finance', views.banking_finance),
   path('banking/insure', views.banking_insure),

   path('cons/durables', views.cons_durables),
   path('cons/electronics', views.cons_electronics),
   path('cons/fmcg', views.cons_fmcg),
   path('cons/food', views.cons_food),
   path('cons/garments_textiles', views.cons_garments_textiles),
   path('cons/liquor', views.cons_liquor),
   path('cons/paints', views.cons_paints),
   path('cons/tobacco', views.cons_tobacco),
   path('cons/fashion_cosmetics_jewellery', views.cons_fas_cos_jew),

   path('energy/power', views.energy_power),
   path('energy/oil_n_gas', views.energy_oil_n_gas),

   path('indgood/cons', views.indgood_cons),
   path('indgood/eng', views.indgood_eng),
   path('indgood/cement', views.indgood_cement),
   path('indgood/chem_fertilisers', views.indgood_chem_fertilisers),
   path('indgood/metals_n_mining', views.indgood_metals_n_mining),
   path('indgood/pack', views.indgood_pack),
   path('indgood/pwgpm', views.indgood_pwgpm),
   path('indgood/petrochem', views.indgood_petrochem),
   path('indgood/steel', views.indgood_steel),

   path('health/healthcare', views.health_healthcare),
   path('health/bio', views.health_bio),
   path('health/pharm', views.health_pharm),


   path('services/advertising', views.services_advertising),
   path('services/consultancy_audit', views.services_consultancy_audit),
   path('services/education', views.services_education),
   path('services/hotels_restaurants', views.services_hotels_restaurants),
   path('services/property_cons', views.services_property_cons),
   path('services/retail', views.services_retail),
   path('services/travel', views.services_travel),

   path('more/entertainment', views.more_entertainment),
   path('more/media', views.more_media),
   path('more/railways', views.more_railways),
   path('more/airlines_aviation', views.more_airlines_aviation),
   path('more/shipping_transport', views.more_shipping_transport),
   path('more/roadways', views.more_roadways),
   path('more/tel_news', views.more_tel_news),
   path('more/tel_policy', views.more_tel_policy),
   path('more/csr_initiatives', views.more_csr_initiatives),
   path('more/csr_policy', views.more_csr_policy),
   path('more/tech', views.more_tech),
   path('more/misc', views.more_misc),
   path('more/env', views.more_env),

]