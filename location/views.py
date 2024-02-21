import csv
from datetime import datetime
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from location.models import (
    CitiesModel,
    CountriesDialCodeModel,
    CountriesModel,
    StatesModel,
)
from response import Response as ResponseData

# Create your views here.


@api_view(["POST"])
# @authentication_classes(
#     [
#         ApiKeyAuthentication,
#     ]
# )
def addCountryDialCodes(request):
    """Function to add new cities,states,countries"""
    try:
        data = request.data
        for i in range(0, data.count()):
            data_exist_or_not = CountriesDialCodeModel.objects.filter(
                country_code=data[i]["code"]
            ).first()
            if data_exist_or_not is None:
                new_country = CountriesDialCodeModel.objects.create(
                    country_dial_code=data[i]["dial_code"],
                    country_code=data[i]["code"],
                    country_name=data[i]["name"],
                )
                new_country.save()
        return Response(
            ResponseData.success([], "Data added successfully"),
            status=status.HTTP_201_CREATED,
        )
    except Exception as exception:
        return Response(
            ResponseData.error(str(exception)),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def get_all_countries(request):
    """Function to get all countries details"""
    try:
        # send_to_firebase()
        countries_data = CountriesModel.objects.values().filter().all()
        for i in range(0, len(countries_data)):
            countries_data[i].pop("created_at")
            countries_data[i].pop("updated_at")
        return Response(
            ResponseData.success(
                countries_data, "Countries details fetched successfully"
            ),
            status=status.HTTP_201_CREATED,
        )
    except Exception as exception:
        return Response(
            ResponseData.error(str(exception)),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

@api_view(["POST"])
def add_all_countries(request):
    """Function to add all countries details"""
    try:
        file_path = 'location_countries.csv'
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row if exists
            for row in reader:
                id, country_code, country_name, created_at_str, updated_at_str = row
                created_at = datetime.strptime(created_at_str, '%Y-%m-%d %H:%M:%S.%f%z')
                updated_at = datetime.strptime(updated_at_str, '%Y-%m-%d %H:%M:%S.%f%z')
                
                # Check if the country already exists in the database
                if not CountriesModel.objects.filter(country_code=country_code).exists():
                    CountriesModel.objects.create(
                        id=id,  
                        country_code=country_code,
                        country_name=country_name,
                        created_at=created_at,
                        updated_at=updated_at
                    )
                else:
                    return Response(
            ResponseData.success_without_data(
                "Countries details already exists"
            ),
            status=status.HTTP_201_CREATED,
        )
        return Response(
            ResponseData.success_without_data(
                "Countries details added successfully"
            ),
            status=status.HTTP_201_CREATED,
        )
    except Exception as exception:
        return Response(
            ResponseData.error(str(exception)),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def add_all_states_of_country(request):
    """Function to add all states of all countries details"""
    try:
        file_path = 'location_states.csv'
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row if exists
            for row in reader:
                id, state_code, country_id,state_name, created_at_str, updated_at_str = row
                created_at = datetime.strptime(created_at_str, '%Y-%m-%d %H:%M:%S.%f%z')
                updated_at = datetime.strptime(updated_at_str, '%Y-%m-%d %H:%M:%S.%f%z')
                
                # Check if the country already exists in the database
                if not StatesModel.objects.filter(id=id).exists():
                    StatesModel.objects.create(
                        id=id,  
                        state_code=state_code,
                        country_id=country_id,
                        state_name=state_name,
                        created_at=created_at,
                        updated_at=updated_at
                    )
                else:
                    return Response(
            ResponseData.success_without_data(
                "States details already exists"
            ),
            status=status.HTTP_201_CREATED,
        )
        return Response(
            ResponseData.success_without_data(
                "States details added successfully"
            ),
            status=status.HTTP_201_CREATED,
        )
    except Exception as exception:
        return Response(
            ResponseData.error(str(exception)),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    
@api_view(["POST"])
def get_all_states_of_country(request):
    """Function to get all states details of a country"""
    try:
        country_id = request.data["id"]
        state_data = StatesModel.objects.values().filter(country_id=country_id).all()
        for i in range(0, len(state_data)):
            state_data[i].pop("created_at")
            state_data[i].pop("updated_at")
        return Response(
            ResponseData.success(state_data, "State details fetched successfully"),
            status=status.HTTP_201_CREATED,
        )
    except Exception as exception:
        return Response(
            ResponseData.error(str(exception)),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def get_all_cities_of_state(request):
    """Function to get all cities details of a state"""
    try:
        state_id = request.data["id"]
        cities_data = CitiesModel.objects.values().filter(state_id=state_id).all()
        for i in range(0, len(cities_data)):
            cities_data[i].pop("created_at")
            cities_data[i].pop("updated_at")
        return Response(
            ResponseData.success(cities_data, "Cities details fetched successfully"),
            status=status.HTTP_201_CREATED,
        )
    except Exception as exception:
        return Response(
            ResponseData.error(str(exception)),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

@api_view(["POST"])
def add_all_cities_of_state(request):
    """Function to add all cities of all states details"""
    try:
        file_path = 'location_cities.csv'
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            cities_to_create = []
            next(reader)  # Skip the header row if exists
            for row in reader:
                id, name,created_at, updated_at, state_id = row
                created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S.%f%z')
                updated_at = datetime.strptime(updated_at, '%Y-%m-%d %H:%M:%S.%f%z')
                print(f"sdvdvdsv {id}")
                # Check if the country already exists in the database
                if not CitiesModel.objects.filter(id=id).exists():
                    cities_to_create.append(
                    CitiesModel(
                        id=id,  
                        name=name,
                        created_at=created_at,
                        updated_at=updated_at,
                        state_id=state_id
                    )
                )
                else:
                    return Response(
            ResponseData.success_without_data(
                "Cities details already exists"
            ),
            status=status.HTTP_201_CREATED,
        )
        CitiesModel.objects.bulk_create(cities_to_create, batch_size=1000)
        return Response(
            ResponseData.success_without_data(
                "Cities details added successfully"
            ),
            status=status.HTTP_201_CREATED,
        )
    except Exception as exception:
        return Response(
            ResponseData.error(str(exception)),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )