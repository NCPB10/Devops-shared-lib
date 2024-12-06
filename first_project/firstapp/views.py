from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def calculate_profit(request):
    if request.method == "POST":
        try:
            errors = {}
            monthly_invest = float(request.POST.get('monthly_invest'))
            if not monthly_invest:
                errors['monthly_invest'] = "Enter the value of monthly invest."
            roi = float(request.POST.get('roi'))
            
            if not roi:
                errors['roi'] = "Enter the value of roi."
            tenure = int(request.POST.get('tenure'))
            if not tenure:
                errors['tenure'] = "Enter the value of tenure."           

            invest1 = monthly_invest
            for i in range(1, tenure):
                monthly_invest = monthly_invest + ((roi/100) * monthly_invest) + invest1

            overall_profit = monthly_invest
            return JsonResponse({"result": f"{overall_profit:.2f}"})
        except Exception as e:
            return JsonResponse({"error": str(e)})

    return render(request, 'investment/index.html')