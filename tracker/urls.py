from django.urls import path, include
from .views import *

app_name = 'tracker'

urlpatterns = [
        path('', index, name='index'),
        path('well/<int:id>', well_info, name='well_info'),
        path('well-history/<int:id>', well_history, name='well_history'),
        path('well-history-add/<int:id>', add_event, name='add_event'),
        path('well/events/<int:id>', delete_event, name='delete_event'),
        path('well/events/edit/<int:id>', edit_event, name='edit_event'),
        path('well/add', add_well, name='add_well'),
        path('field/add', add_field, name='add_field'),

]