from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from solutions.models import Solution


def homepage(request):   #Present ALL data, not filtered and collect ALL clases available from DB.
    solutions = Solution.objects.all()
    Lista = []
    for row in solutions:
        Lista.append(row.clase)
    unique_list = list(sorted(set(Lista)))
    return render(request, 'index.html', {'dataFromsolutions': solutions, 'uniqueValues':unique_list})


def solution_filtered(request, tipos): #filtering data and collecting all clases form DB.
    tipo=tipos.capitalize()
    solution = Solution.objects.filter(clase=tipo)
    solutions = Solution.objects.all()
    Lista = []
    for row in solutions:
        Lista.append(row.clase)
    unique_list = list(sorted(set(Lista)))
    if tipos=="All":
        return render(request, 'index.html', {'dataFromsolutions': solutions, 'uniqueValues':unique_list})
    else:
        return render(request, 'filtered_data.html', {'filtrado': solution, 'uniqueValues':unique_list})


def about(request):
    return HttpResponse('about')
