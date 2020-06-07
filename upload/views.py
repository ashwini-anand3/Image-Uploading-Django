from django.shortcuts import render
from .models import User

# Create your views here.
def home(request):
	if request.method=='POST':
		pic=request.FILES.get('image')
		# print(image)
		user = User.objects.create(image=pic)
		user.save()
	return render(request,'index.html')