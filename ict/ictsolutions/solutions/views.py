from django.shortcuts import render
from .models import Solution

def solution_list(request):
    solutions = Solution.objects.all().order_by('date')
    return render(request, "solutions/solution_list.html", {'dataFromsolutions': solutions})


def solution_filtered(request, clase):
    solution = Solution.objects.get(clase=clase)
    return render(request, 'solutions/filtered_data.html', {'filtrado': solution})