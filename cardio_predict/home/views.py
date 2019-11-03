from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from sklearn.externals import joblib
from sklearn.neural_network import MLPClassifier

from .forms import CardioForm
from .models import CardioModel

import os


def welcome(request):
    return render(request, "home/welcome.html")


def bmi_calc(height, weight):
    bmi_val = round((weight / height / height) * 10000)
    if bmi_val < 19:
        val = 2
    elif bmi_val > 19 and bmi_val < 25:
        val = 1
    elif bmi_val > 25 and bmi_val < 30:
        val = 3
    else:
        val = 4
    return val


def bpc_calc(sbp, dbp):
    if sbp <= 120 and dbp <= 80:
        val = 1
    elif sbp > 120 and sbp < 130 and dbp < 80:
        val = 2
    elif sbp >= 130 and sbp < 140 or dbp > 80 and dbp < 89:
        val = 3
    elif sbp >= 140 and sbp < 180 or dbp >= 90 and dbp < 120:
        val = 4
    elif sbp >= 180 or dbp >= 120:
        val = 5
    return val


def age_calc(age):
    if age <= 30:
        val = 1
    elif age > 30 and age <= 40:
        val = 2
    elif age > 40 and age <= 50:
        val = 3
    else:
        val = 4
    return val


def hform(request):
    print("inside hform")
    if request.method == "POST":
        print("inside post")
        cardio_form = CardioForm(request.POST)
        if cardio_form.is_valid():
            print("valid form")
            try:
                # print(cardio_form, '--------------------------')
                data = cardio_form.save(commit=False)
                data.save()
                return HttpResponseRedirect(
                    reverse("predict_now", kwargs={"pk": data.pk})
                )
            except Exception as e:
                print("form error in db---------------", e)
                context = {"message": "an error happend"}
                cardio_form = CardioForm()
                return render(request, "home/hform.html", {"form": cardio_form})
        else:
            print("invalid form error")
            context = {"message": "form is not valid"}
            cardio_form = CardioForm()
            return render(request, "home/hform.html", {"form": cardio_form})
    else:
        print("pagge loading")
        cardio_form = CardioForm()
        return render(request, "home/hform.html", {"form": cardio_form})


def predict_now(request, pk):
    print("inside predict now")

    user = CardioModel.objects.get(pk=pk)
    user.bmi = bmi_calc(user.height, user.weight)
    user.age = age_calc(user.age)
    user.bpc = bpc_calc(user.sbp, user.dbp)
    user.save()

    model_path = os.getcwd() + "\home\cardio_model.pkl"
    model = joblib.load(model_path)
    y_val = [
        user.age,
        user.gender,
        user.gluc,
        user.smoke,
        user.bmi,
        user.bpc,
        user.cholesterol,
        user.alco,
        user.active,
    ]
    prediction = int(model.predict([y_val]))
    user.cardio = prediction
    user.save()
    context = {"user": user, "predicted": prediction}
    return render(request, "home/output.html", context)
