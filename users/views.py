from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit
from django.contrib.auth import get_user_model
from django.db.models import Count, Q


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes([AllowAny])
def api_update_habit(request, pk):
    try:
        habit = Habit.objects.get(pk=pk)
        habit.is_done = True

        description = request.data.get('description')
        if description:
            habit.description = description

        habit.save()
        return Response({"status": "success"})
    except Habit.DoesNotExist:
        return Response({"status": "error"}, status=404)




# 1. Dashboard (Asosiy sahifa)
def my_habits(request):
    habits = Habit.objects.filter(user=request.user)
    # Eco Score hisoblash: Har bir Done uchun 10 ball
    done_count = habits.filter(is_done=True).count()
    eco_score = done_count * 10

    return render(request, 'users/habits/my_habits.html', {'habits': habits, 'eco_score': eco_score})




# Add habit qoshish
def add_habit(request,):
    if request.method == "POST":
        name = request.POST.get('name')
        Habit.objects.create(user=request.user, name=name)
        return redirect('my_habits')
    return render(request, "users/habits/habit_form.html",{'title': 'Add New Habit'})




# 3. Edit Habit (Tahrirlash)
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk, user=request.user)
    if request.method == "POST":
        habit.name = request.POST.get('name')
        habit.save()
        return redirect('my_habits')
    return render(request, "users/habits/habit_form.html", {'habit': habit, 'title': 'Edit Habit'})




# 4. Delete Habit (O'chirish)
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk, user=request.user)
    habit.delete()
    return redirect('my_habits')






# 5. Toggle (Done/Undo tugmasi)
def toggle_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk, user=request.user)
    habit.is_done = not habit.is_done
    habit.save()
    return redirect('my_habits')



# 6. Leaderboard (Reyting)
User = get_user_model()



def leaderboard(request):
    User = get_user_model()

    users_list = User.objects.annotate(
        done_count=Count('habit', filter=Q(habit__is_done=True))
    ).order_by('-done_count')

    # Har bir user uchun scoreni hisoblaymiz (10 ga ko'paytirib)
    for u in users_list:
        u.score = u.done_count * 10

    print(users_list)
    return render(request, 'users/habits/leaderboard.html', {
        'users_list': users_list
    })

