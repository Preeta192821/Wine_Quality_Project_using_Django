from django.shortcuts import render
from .quality import prediction

# Create your views here.
def Index(request):
	return render(request,'index.html')

def Prediction(request):
	if request.method == "POST":
		fixed_acidity = request.POST['fixed_acidity']
		volatile_acidity = request.POST['volatile_acidity']
		citric_acid = request.POST['citric_acid']
		residual_sugar = request.POST['residual_sugar']
		chlorides = request.POST['chlorides']
		free_sulfur_dioxide = request.POST['free_sulfur_dioxide']
		total_sulfur_dioxide = request.POST['total_sulfur_dioxide']
		density = request.POST['density']
		pH = request.POST['pH']
		sulphates = request.POST['sulphates']
		alcohol = request.POST['alcohol']

		quality = prediction(fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol)

		return render(request,'prediction.html',{'quality':quality})
	return render('request','prediction.html')

def Firstpage(request):
	return render(request,'firstpage.html')






























	