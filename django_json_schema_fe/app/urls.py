from django.urls import path
from app import generate
from app import validate
from app import main_views

urlpatterns = [
    path('', main_views.index, name="index"),
    # generate views
    path('generate', generate.index, name="index_generate"),
    path('insert', generate.insert_data, name="insert_data"),
    path('validate', validate.index, name="index_validate"),
    path('detail/<str:url_path>', validate.detail, name='detail_view'),
    path('/validateJson', validate.validateJson, name='validate_json')
    # path('generate_json_schema', generate.generate_json_schema, name="generate_json_schema")
    # validate views

]
