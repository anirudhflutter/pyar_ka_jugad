from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user.models import UserModel
from .serializers import UserSignUpSerializer
from django.core.files.storage import FileSystemStorage

# Create your views here.
@api_view(["POST"])
def signup(request):
    serializer = UserSignUpSerializer(data=request.data)
    if serializer.is_valid():
        # Extract data from serializer
        first_name = serializer.data["first_name"]
        last_name = serializer.data["last_name"]
        phone_number = serializer.data["phone_number"]
        gender = serializer.data["gender"]
        birth_date = serializer.data["birth_date"]
        country_id = serializer.data["country"]
        state_id = serializer.data["state"]
        city_id = serializer.data["city"]
        images = request.FILES.getlist('images')
        height = serializer.data["height"]
        weight = serializer.data["weight"]
        instagram_id = serializer.data["instagram_id"]
        instagram_account_link = serializer.data["instagram_account_link"]
        designation = serializer.data["designation"]
        occupation = serializer.data["occupation"]

        # Check if the phone number already exists in the database
        if UserModel.objects.filter(phone_number=phone_number).exists():
            return Response({"message": "This phone number already exists in the database"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create User object
        user = UserModel.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            gender=gender,
            birth_date=birth_date,
            country_id=country_id,
            state_id=state_id,
            city_id=city_id,
            height=height,
            weight=weight,
            instagram_id=instagram_id,
            instagram_account_link=instagram_account_link,
            designation=designation,
            occupation=occupation
        )
        
        # Save profile pics and store paths in database
        pic_paths = ""
        for idx, pic in enumerate(images, start=1):
            pic_path = f"static/profile_pics/{user.id}_{idx}.jpg"  # Assuming JPEG format
            fs = FileSystemStorage(location='static/profile_pics/')
            fs.save(pic.name, pic)
            pic_paths+=pic_path + ","
        print(f"pic_paths {pic_paths}")
        # Update user with profile pic paths
        user.images = pic_paths
        user.save()
        
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
