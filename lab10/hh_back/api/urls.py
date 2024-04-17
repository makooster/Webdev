from django.urls import path
from . import views
urlpatterns = [
    path('companies/', views.companyList, name = "companiesList"),
    path('companies/<int:id>/', views.companyListDetail, name = "companiesListDetail"),
    path('vacancies/', views.vacancyList, name = "vacanciesList"),
    path('vacancies/<int:id>/', views.vacancyListDetail, name = "vacanciesListDetail"),
    path('companies/create/', views.companyCreate, name = "companiesListDetail"),
    path('vacancies/create/', views.vacancyCreate, name = "vacanciesListDetail"),
    path('companies/update/<int:id>/', views.companyUpdate, name = "companiesUpdate"),
    path('vacancies/update/<int:id>/', views.vacancyUpdate, name = "vacanciesUpdate"),
    path('companies/delete/<int:id>/', views.companyDelete, name = "companiesDelete"),
    path('vacancies/delete/<int:id>/', views.vacancyDelete, name = "vacanciesDelete"),
]