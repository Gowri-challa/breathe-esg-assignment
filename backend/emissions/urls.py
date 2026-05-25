from django.urls import path

from .views import (
    home,
    upload_file,
    get_records,
    approve_record,
    reject_record
)

urlpatterns = [

    path('', home),

    path('upload/', upload_file),

    path('records/', get_records),

    path('approve/<int:id>/', approve_record),

    path('reject/<int:id>/', reject_record),
]