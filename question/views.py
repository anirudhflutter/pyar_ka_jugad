from rest_framework.decorators import api_view
from rest_framework.response import Response
from question.models import QuestionForFemaleModel, QuestionForMaleModel
from rest_framework import status
from question.serializers import AddNewQuestionForFemaleSerializer, AddNewQuestionForMalesSerializer
from questionOption.models import QuestionOptionsForFemalesModel, QuestionOptionsForMalesModel

# Create your views here.
@api_view(["POST"])
def add_question_for_girls(request):
    """Function to add a question to ask girls"""
    serializer = AddNewQuestionForFemaleSerializer(data=request.data)
    if serializer.is_valid():
        # Extract data from serializer
        title = serializer.data["title"]

        # Check if the same question title already exists in the database
        if QuestionForFemaleModel.objects.filter(title=title).exists():
            return Response({"message": "This question already exists in the database"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create User object
        question = QuestionForFemaleModel.objects.create(
            title=title,
        )
        question.save()
        
        return Response({"message": "Question added successfully"}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
@api_view(["POST"])
def add_question_for_boys(request):
    """Function to add a question to ask boys"""
    serializer = AddNewQuestionForMalesSerializer(data=request.data)
    if serializer.is_valid():
        # Extract data from serializer
        title = serializer.data["title"]

        # Check if the same question title already exists in the database
        if QuestionForMaleModel.objects.filter(title=title).exists():
            return Response({"message": "This question already exists in the database"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create User object
        question = QuestionForMaleModel.objects.create(
            title=title,
        )
        question.save()
        
        return Response({"message": "Question added successfully"}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def get_questions_with_options_for_girls(request):
    """Function to fetch questions with options for girls"""
    questions_with_options = []

    # Get all questions for females
    questions = QuestionForFemaleModel.objects.filter(is_active=True).all()

    for question in questions:
        # Get options for each question
        options = QuestionOptionsForFemalesModel.objects.filter(question=question,is_active=True)
        option_data = [{"question_option_id": option.id, "question_option_title": option.title} for option in options]

        questions_with_options.append({
            "question_id": question.id,
            "question_title": question.title,
            "question_options": option_data
        })

    return Response({"message": "Data fetched successfully", "Data": questions_with_options}, status=status.HTTP_200_OK)


@api_view(["POST"])
def get_questions_with_options_for_boys(request):
    """Function to fetch questions with options for boys"""
    questions_with_options = []

    # Get all questions for females
    questions = QuestionForMaleModel.objects.filter(is_active=True).all()

    for question in questions:
        # Get options for each question
        options = QuestionOptionsForMalesModel.objects.filter(question=question,is_active=True)
        option_data = [{"question_option_id": option.id, "question_option_title": option.title} for option in options]

        questions_with_options.append({
            "question_id": question.id,
            "question_title": question.title,
            "question_options": option_data
        })

    return Response({"message": "Data fetched successfully", "Data": questions_with_options}, status=status.HTTP_200_OK)
