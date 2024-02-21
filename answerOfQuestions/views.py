from rest_framework.decorators import api_view
from rest_framework.response import Response
from answerOfQuestions.models import AnswersOfFemalesModel, AnswersOfMalesModel
from answerOfQuestions.serializers import AddAnswersOfFemaleSerializer, AddAnswersOfMaleSerializer
from question.models import QuestionForFemaleModel, QuestionForMaleModel
from rest_framework import status
from questionOption.models import QuestionOptionsForFemalesModel, QuestionOptionsForMalesModel

from user.models import UserModel

# Create your views here.
@api_view(["POST"])
def add_answers_of_girls(request):
    """Function to add answers of girls"""
    serializer = AddAnswersOfFemaleSerializer(data=request.data)
    if serializer.is_valid():
        # Extract data from serializer
        user_id = serializer.data["user_id"]
        answers = serializer.data["answers"]

        # Check if the user exists
        try:
            user = UserModel.objects.get(id=user_id,is_active=True,is_verified=True)
        except UserModel.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        answers_to_create = []
        for answer in answers:
            question_id, selected_option_id = answer.split(',')
            question_id, selected_option_id = answer.split(',')

            try:
                question = QuestionForFemaleModel.objects.get(id=question_id,is_active=True)
            except QuestionForFemaleModel.DoesNotExist:
                return Response({"message": f"Question with ID {question_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
            
            try:
                selected_option = QuestionOptionsForFemalesModel.objects.get(id=selected_option_id,question_id = question_id,is_active=True)
            except QuestionOptionsForFemalesModel.DoesNotExist:
                return Response({"message": f"Option with ID {selected_option_id} does not exist or is not the option of question with ID {question_id}"}, status=status.HTTP_404_NOT_FOUND)

            # Check if an answer for this question already exists for the user
            if AnswersOfFemalesModel.objects.filter(user=user, question=question,is_active=True).exists():
                return Response({"message": f"Answer for question with ID {question_id} already exists for this user"}, status=status.HTTP_400_BAD_REQUEST)

            answers_to_create.append(AnswersOfFemalesModel(
                question=question,
                user=user,
                selected_option=selected_option
            ))

        # Bulk create answers
        AnswersOfFemalesModel.objects.bulk_create(answers_to_create)

        return Response({"message": "Answers added successfully"}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def update_answers_of_girls(request):
    """Function to update answers of girls"""
    serializer = AddAnswersOfFemaleSerializer(data=request.data)
    if serializer.is_valid():
        # Extract data from serializer
        user_id = serializer.data["user_id"]
        answers = serializer.data["answers"]

        # Check if the user exists and is active and verified
        try:
            user = UserModel.objects.get(id=user_id, is_active=True, is_verified=True)
        except UserModel.DoesNotExist:
            return Response({"message": "User does not exist or is not active/verified"}, status=status.HTTP_404_NOT_FOUND)
        
        answers_to_create = []
        for answer in answers:
            question_id, selected_option_id = answer.split(',')
            try:
                question = QuestionForFemaleModel.objects.get(id=question_id,is_active=True)
            except QuestionForFemaleModel.DoesNotExist:
                return Response({"message": f"Question with ID {question_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
            
            try:
                selected_option = QuestionOptionsForFemalesModel.objects.get(id=selected_option_id,is_active=True)
            except QuestionOptionsForFemalesModel.DoesNotExist:
                return Response({"message": f"Option with ID {selected_option_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

            try:
                existing_answer = AnswersOfFemalesModel.objects.get(user=user, question=question,is_active=True)
            except AnswersOfFemalesModel.DoesNotExist:
                return Response({"message": f"Answer for this question with ID {question_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

            # Check if an answer for this question already exists for the user
            if existing_answer:
                if existing_answer.selected_option.id == selected_option.id:
                    # If existing answer matches the selected option, skip this answer
                    continue
                else:
                    # If existing answer doesn't match the selected option, update it and create a new answer
                    existing_answer.is_active = False
                    existing_answer.save()

            # Create the new answer
            answers_to_create.append(AnswersOfFemalesModel(
                question=question,
                user=user,
                selected_option=selected_option
            ))

        # Bulk create answers
        AnswersOfFemalesModel.objects.bulk_create(answers_to_create)

        return Response({"message": "Answers updated successfully"}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
@api_view(["POST"])
def add_answers_of_boys(request):
    """Function to add answers of boys"""
    serializer = AddAnswersOfMaleSerializer(data=request.data)
    if serializer.is_valid():
        # Extract data from serializer
        user_id = serializer.data["user_id"]
        answers = serializer.data["answers"]

        # Check if the user exists
        try:
            user = UserModel.objects.get(id=user_id,is_active=True,is_verified=True)
        except UserModel.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        answers_to_create = []
        for answer in answers:
            question_id, selected_option_id = answer.split(',')

            try:
                question = QuestionForMaleModel.objects.get(id=question_id)
            except QuestionForMaleModel.DoesNotExist:
                return Response({"message": f"Question with ID {question_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
            
            try:
                selected_option = QuestionOptionsForMalesModel.objects.get(id=selected_option_id,question_id = question_id)
            except QuestionOptionsForMalesModel.DoesNotExist:
                return Response({"message": f"Option with ID {selected_option_id} does not exist or is not the option of question with ID {question_id}"}, status=status.HTTP_404_NOT_FOUND)

            # Check if an answer for this question already exists for the user
            if AnswersOfMalesModel.objects.filter(user=user, question=question).exists():
                return Response({"message": f"Answer for question with ID {question_id} already exists for this user"}, status=status.HTTP_400_BAD_REQUEST)

            answers_to_create.append(AnswersOfMalesModel(
                question=question,
                user=user,
                selected_option=selected_option
            ))

        # Bulk create answers
        AnswersOfMalesModel.objects.bulk_create(answers_to_create)

        return Response({"message": "Answers added successfully"}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def update_answers_of_boys(request):
    """Function to update answers of boys"""
    serializer = AddAnswersOfMaleSerializer(data=request.data)
    if serializer.is_valid():
        # Extract data from serializer
        user_id = serializer.data["user_id"]
        answers = serializer.data["answers"]

        # Check if the user exists and is active and verified
        try:
            user = UserModel.objects.get(id=user_id, is_active=True, is_verified=True)
        except UserModel.DoesNotExist:
            return Response({"message": "User does not exist or is not active/verified"}, status=status.HTTP_404_NOT_FOUND)
        
        answers_to_create = []
        for answer in answers:
            question_id, selected_option_id = answer.split(',')
            try:
                question = QuestionForMaleModel.objects.get(id=question_id,is_active=True)
            except QuestionForMaleModel.DoesNotExist:
                return Response({"message": f"Question with ID {question_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
            
            try:
                selected_option = QuestionOptionsForMalesModel.objects.get(id=selected_option_id,is_active=True)
            except QuestionOptionsForMalesModel.DoesNotExist:
                return Response({"message": f"Option with ID {selected_option_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

            try:
                existing_answer = AnswersOfMalesModel.objects.get(user=user, question=question,is_active=True)
            except AnswersOfMalesModel.DoesNotExist:
                return Response({"message": f"Answer for this question with ID {question_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

            # Check if an answer for this question already exists for the user
            if existing_answer:
                if existing_answer.selected_option.id == selected_option.id:
                    # If existing answer matches the selected option, skip this answer
                    continue
                else:
                    # If existing answer doesn't match the selected option, update it and create a new answer
                    existing_answer.is_active = False
                    existing_answer.save()

            # Create the new answer
            answers_to_create.append(AnswersOfMalesModel(
                question=question,
                user=user,
                selected_option=selected_option
            ))

        # Bulk create answers
        AnswersOfMalesModel.objects.bulk_create(answers_to_create)

        return Response({"message": "Answers updated successfully"}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)