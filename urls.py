from django.urls import path, include

from . import views
from .views import *

from .cloud_practitioner_modules import cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8, cp9, cp10

cloud_practitioner_patterns = [
    path('', CPView.as_view(), name='pcep_home'),
    path('random/', RandomModuleView.as_view(modules = (cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8, cp9, cp10)), name = 'random_aws_cp'),
    path('cp1/', RandomModuleView.as_view(modules = (cp1,)), name = 'introduction'),
    path('cp2/', RandomModuleView.as_view(modules = (cp2,)), name = 'compute_in_the_cloud'),
    path('cp3/', RandomModuleView.as_view(modules = (cp3,)), name = 'global_infrastructure_and_reliability'),
    path('cp4/', RandomModuleView.as_view(modules = (cp4,)), name = 'networking'),
    path('cp5/', RandomModuleView.as_view(modules = (cp5,)), name = 'storage_and_databases'),
    path('cp6/', RandomModuleView.as_view(modules = (cp6,)), name = 'security'),
    path('cp7/', RandomModuleView.as_view(modules = (cp7,)), name = 'monitoring_and_analytics'),
    path('cp8/', RandomModuleView.as_view(modules = (cp8,)), name = 'pricing_and_support'),
    path('cp9/', RandomModuleView.as_view(modules = (cp9,)), name = 'migration_and_innovation'),
    path('cp10/', RandomModuleView.as_view(modules = (cp10,)), name = 'cloud_journey'),
    path('<str:module_str>/<str:key>/', SpecificAreaView, name='specific_area_view'),
]

urlpatterns = [
    path('', HomeView.as_view(), name='cloud_practitioner_home'),
    path('cp/', include(cloud_practitioner_patterns)),
    #path('drill/', include(drill_patterns)),
    path('test/', test_question, name='test_view'),
    path('report/', ReportView.as_view(), name='report')
] 
