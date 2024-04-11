from rest_framework.decorators import api_view
# from rest_framework.decorators import csrf_exempt
from rest_framework.response import Response
from .serializers import CompanySerializer, VacancySerializer
from .models import Company, Vacancy


@api_view(['GET'])
def companyList(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many = True)
    return Response(serializer.data)

# @api_view(['GET'])
# def companiesAndVacancies(request):
#     companies = Company.objects.all()
#     serializer = CompanySerializer(companies, many = True)
#     return Response(serializer.data)

@api_view(['GET'])
def companyListDetail(request, id):
    companies = Company.objects.get(pk = id)
    serializer = CompanySerializer(companies, many = False)
    return Response(serializer.data)

@api_view(['GET'])
def vacancyList(request):
    vacancies = Vacancy.objects.all()
    serializer = VacancySerializer(vacancies, many = True)
    return Response(serializer.data)

# I replaced places of pk and id, if it won't work i should change it. and should also change urls file

@api_view(['GET'])
def vacancyListDetail(request, id):
    vacancies = Vacancy.objects.get(pk = id)
    serializer = VacancySerializer(vacancies, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def vacancyCreate(request):
    serializer = VacancySerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def companyCreate(request):
    serializer = CompanySerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def companyUpdate(request, id):
    company = Company.objects.get(pk = id)
    serializer = CompanySerializer(instance = company, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def vacancyUpdate(request, id):
    vacancy = Vacancy.objects.get(pk = id)
    serializer = VacancySerializer(instance = vacancy, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def companyDelete(request, id):
    company = Company.objects.get(pk = id)
    company.delete()
    return Response('Company successfully deleted!')

@api_view(['DELETE'])
def vacancyDelete(request, id):
    vacancy = Vacancy.objects.get(pk = id)
    vacancy.delete()
    return Response('Vacancy succesfully deleted!')

# class VacancyTopTen(APIView):
#     def get(self,request):
#         ten_top = Vacancy.objects.all().order_by('-salary')[:10]
#         serializer = VacancySerializer(ten_top, many=True)
#         return Response(serializer.data)
