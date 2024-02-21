from rest_framework.decorators import api_view
from rest_framework.response import Response
from question.models import QuestionForFemaleModel, QuestionForMaleModel
from rest_framework import status
from questionOption.models import QuestionOptionsForFemalesModel, QuestionOptionsForMalesModel
from questionOption.serializers import AddNewQuestionOptionsForFemaleSerializer, AddNewQuestionOptionsForMaleSerializer

# Create your views here.
@api_view(["POST"])
def add_question_options_for_girls(request):
    """Function to add question options for girls"""
    serializer = AddNewQuestionOptionsForFemaleSerializer(data=request.data)
    if serializer.is_valid():
        # Extract data from serializer
        question_id = serializer.data["question_id"]
        titles = serializer.data["titles"]
        # Check if the question exists
        try:
            question = QuestionForFemaleModel.objects.get(id=question_id)
        except QuestionForFemaleModel.DoesNotExist:
            return Response({"message": "Question does not exist"}, status=status.HTTP_404_NOT_FOUND)

        options_to_create = []
        existing_titles = QuestionOptionsForFemalesModel.objects.filter(question=question).values_list('title', flat=True)
        for title in titles:
            if title in existing_titles:
                return Response({"message": f"Title '{title}' already exists in the database"}, status=status.HTTP_400_BAD_REQUEST)
            options_to_create.append(QuestionOptionsForFemalesModel(title=title, question=question))

        # Use bulk_create to create all options at once
        QuestionOptionsForFemalesModel.objects.bulk_create(options_to_create)


        return Response({"message": "Question options added successfully"}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
@api_view(["POST"])
def add_question_options_for_boys(request):
    """Function to add question options for boys"""
    serializer = AddNewQuestionOptionsForMaleSerializer(data=request.data)
    if serializer.is_valid():
        # Extract data from serializer
        question_id = serializer.data["question_id"]
        titles = serializer.data["titles"]
        # Check if the question exists
        try:
            question = QuestionForMaleModel.objects.get(id=question_id)
        except QuestionForMaleModel.DoesNotExist:
            return Response({"message": "Question does not exist"}, status=status.HTTP_404_NOT_FOUND)

        options_to_create = []
        existing_titles = QuestionOptionsForMalesModel.objects.filter(question=question).values_list('title', flat=True)
        for title in titles:
            if title in existing_titles:
                return Response({"message": f"Title '{title}' already exists in the database"}, status=status.HTTP_400_BAD_REQUEST)
            options_to_create.append(QuestionOptionsForMalesModel(title=title, question=question))

        # Use bulk_create to create all options at once
        QuestionOptionsForMalesModel.objects.bulk_create(options_to_create)


        return Response({"message": "Question options added successfully"}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
