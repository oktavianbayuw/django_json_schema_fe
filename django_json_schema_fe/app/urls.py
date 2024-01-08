from django.urls import path
from app import generate
from app import validate
from app import main_views
from app import faq

urlpatterns = [
    path('', main_views.index, name="index"),
    path('generate/', generate.index, name="index_generate"),
    path('insert_data/', generate.insert_data, name="insert_data"),
    path('validate', validate.index, name="index_validate"),
    path('detail/<str:url_path>/', validate.detail, name='detail_view'),
    path('validateJson', validate.validateJson, name='validate_json'),
    path('generateJsonSchema/', generate.generate_json_schema),
    path('delete_data/<str:url_path>/', validate.delete_data, name='delete_data'),
    path('faq', faq.index, name="faq"),
]
