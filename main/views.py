from django.shortcuts import render,redirect
import json
from django.core.paginator import Paginator
import requests
from .models import Vacancy



def get_count_pages(keyword,code,empl,grap,sort,exp):
    url = "https://api.hh.ru/vacancies"
    params = {
        "text" : keyword,
        "area" : code,  # Specify the desired area ID (1 is Moscow)
        "per_page" : 50,  # Number of vacancies per page
        "page" : 1,
    }
    if grap !="":
        params["schedule"] = grap
    if empl !="":
        params["employment"] = empl
    if exp !="":
        params["experience"] = exp
    if sort !="":
        params["order_by"] = sort
    headers = {
        "User-Agent": "Your User Agent",  # Replace with your User-Agent header
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('pages')
    else:
        print(f"Request failed with status code: {response.status_code}")

def get_vacancies(keyword,page,code,empl,grap,sort,exp):
    url = "https://api.hh.ru/vacancies"
    params = {
        "text" : keyword,
        "area" : code,  # Specify the desired area ID (1 is Moscow)
        "per_page" : 50,  # Number of vacancies per page
        "page" : page,
    }
    if grap !="":
        params["schedule"] = grap
    if empl !="":
        params["employment"] = empl
    if exp !="":
        params["experience"] = exp
    if sort !="":
        params["order_by"] = sort
    headers = {
        "User-Agent": "Your User Agent",  # Replace with your User-Agent header
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        vacancies = data.get("items", [])

        # List to store the vacancy data
        vacancies_list = []

        for vacancy in vacancies:
            # Extract relevant information from the vacancy object
            vacancy_id = vacancy.get("id")
            vacancy_title = vacancy.get("name")
            vacancy_url = vacancy.get("alternate_url")
            company_name = vacancy.get("employer", {}).get("name")
            salary = vacancy.get("salary")
            salary2 = 'not specified'
            grafic = vacancy.get('schedule',{}).get('name')
            experience = vacancy.get('experience',{}).get('name')
            requirement = vacancy.get('snippet',{}).get('requirement')
            responsibility = vacancy.get('snippet',{}).get('responsibility')

            if requirement == None:
                requirement = 'not specified'
            if responsibility == None:
                responsibility = 'not specified'
            if experience == None:
                experience = 'not specified'
            if grafic == None:
                grafic = 'not specified'

            requirement = requirement.replace('<highlighttext>','')
            requirement = requirement.replace('</highlighttext>','')
            responsibility = responsibility.replace('<highlighttext>','')
            responsibility = responsibility.replace('</highlighttext>','')
            #print("-----------------------------")
            #print(data.get('pages'))
            #print("-----------------------------")
            if salary != None:
                if salary['from'] != None:
                    salary2 = 'from ' + str(salary['from'])
                    if salary['to'] != None:
                        salary2+=' to '+ str(salary['to']) #gross currency
                if salary['gross']:
                    salary2 += ' before taxes'
                if salary['currency'] !=None:
                    salary2 += ' '+str(salary['currency'])


            # Add vacancy data to the list
            vacancies_list.append({
                "id": vacancy_id,
                "title": vacancy_title,
                "company": company_name,
                "url": vacancy_url,
                "salary": salary2,
                "grafic": grafic,
                "experience": experience,
                "requirement": requirement,
                "responsibility": responsibility,
            })

        return vacancies_list
    else:
        print(f"Request failed with status code: {response.status_code}")




def get_code_regions():
    url = "https://api.hh.ru/areas"
    response = requests.get(url)
    data = response.json()
    areas = data[0].get("areas", [])
    codes =[]
    for i in areas:
        code = {
            'code': i.get('id'),
            'name': i.get('name'),

        }
        codes.append(code)
    return codes

def index(request):


    table_data =  Vacancy.objects.all()
    codes = get_code_regions()
    paginator = Paginator(table_data, 20)  # 20 строк на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    #print(paginator.get_page(1).object_list)
    #print(paginator.get_page(2).object_list)


    return render(request, 'main/index.html', {'table_data': page_obj,'codes':codes})




def pars(request):
    Vacancy.objects.all().delete()
    zap = request.POST.get('zap')
    code = request.POST.get('code')
    empl = request.POST.get('empl')
    grap = request.POST.get('grap')
    sort = request.POST.get('sort')
    exp = request.POST.get('exp')



    #print(zap)
    #print(code)
    #print('pars')
    for page in range(get_count_pages(zap,code,empl,grap,sort,exp)):
    #for page in range(2):
        vacancys = get_vacancies(zap, page,code,empl,grap,sort,exp)

        for vac in vacancys:
            vacancy = Vacancy(
                              id=vac['id'],
                              title = vac['title'],
                              company = vac['company'],
                              url = vac['url'],
                              salary = vac['salary'],
                              grafic = vac['grafic'],
                              experience = vac['experience'],
                              requirement = vac['requirement'],
                              responsibility = vac['responsibility'],
            )
            vacancy.save()
    return redirect('/', permanent=True)



