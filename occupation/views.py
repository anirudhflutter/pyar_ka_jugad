from rest_framework.decorators import api_view
from occupation.models import OccupationModel
from occupation.serializers import AddOccupationModelSerializer, GetAllOccupationSerializer
from rest_framework.response import Response
from response import Response as ResponseData
from rest_framework import status

@api_view(["POST"])
def addNewOccupation(request):
    """Function to add new occupation"""
    try:
        data = request.data
        serializer = AddOccupationModelSerializer(data=data)
        if serializer.is_valid():
            title = str(serializer.data["title"]).lower()
            occupation_exists = OccupationModel.objects.filter(title=title).exists()
            if occupation_exists:
                return Response(
                    ResponseData.error(
                        "This occupation already exists"),
                    status=status.HTTP_201_CREATED,
                )
            new_occupation = OccupationModel.objects.using('designation_db').create(
                title=title
            )
            new_occupation.save()
            return Response(
                ResponseData.success_without_data(
                    "Occupation added successfully"),
                status=status.HTTP_201_CREATED,
            )
        for error in serializer.errors:
            print(serializer.errors[error][0])
        return Response(
            ResponseData.error(serializer.errors[error][0]),
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception as exception:
        return Response(
            ResponseData.error(str(exception)), status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(["POST"])
def getAllOccupations(request):
    """Function to get all occupations"""
    try:
        data = request.data
        serializer = GetAllOccupationSerializer(data=data)
        if serializer.is_valid():
            occupation_data = OccupationModel.objects.using('designation_db').values().filter().all()
            for i in range(0,occupation_data.count()):
                occupation_data[i].pop('created_at')
                occupation_data[i].pop('updated_at')
            return Response(
                ResponseData.success(
                    occupation_data, "Designation details fetched successfully"),
                status=status.HTTP_201_CREATED)
        for error in serializer.errors:
            print(serializer.errors[error][0])
        return Response(
            ResponseData.error(serializer.errors[error][0]),
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception as exception:
        return Response(
            ResponseData.error(str(exception)), status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )