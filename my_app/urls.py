from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('shoes/', views.shoe_index, name='shoe_index'),
  path('shoes/<int:shoe_id>',views.shoe_detail, name='shoe_detail'),
  path('shoes/create', views.ShoeCreate.as_view(), name='shoe_create'),
  path('shoes/<int:pk>/update', views.ShoeUpdate.as_view(), name='shoe_update'),
  path('shoes/<int:pk>/delete', views.ShoeDelete.as_view(), name='shoe_delete'),
  path('laces/create', views.LaceCreate.as_view(), name='lace_create'),
  path('laces/<int:pk>', views.LaceDetail.as_view(), name='lace_detail'),
  path('laces/', views.LaceList.as_view(), name='lace_index'),
  path('laces/<int:pk>/update/', views.LaceUpdate.as_view(), name='lace_update'),
  path('laces/<int:pk>/delete/', views.LaceDelete.as_view(), name='lace_delete'),
  path('laces/<int:pk>/delete/', views.LaceDelete.as_view(), name='lace_delete'),
  path('shoes/<int:shoe_id>/associate-lace/<int:lace_id>/', views.associate_lace, name='associate_lace'),
  path('shoes/<int:shoe_id>/disassociate-lace/<int:lace_id>/', views.disassociate_lace, name='disassociate_lace'),
  path('accounts/signup/', views.signup, name='signup'),
]