# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from . import LogicProgram
from forms import Document
from models import *

# Create your views here.

def home(request):
    desc_post = table_post_description.objects.all().order_by('-id')
    return render (request, 'home/home.html', {'desc_post':desc_post})

@login_required(login_url='login')
def upload_file_csv(request):
    global url

    if request.method == 'POST':
        form = Document(request.POST, request.FILES)
        if form.is_valid():
            save = form.save()
            id = save.id
            setData = LogicProgram.Data(id)
            setData.ambil_data()
            setData.set_regresi_korelasi()
            url = reverse('home')
        return HttpResponseRedirect(url)
    else:
        form = Document()
    return render (request, 'home/upload_file_csv.html', {'form' : form})

def post(request, id):
    from sklearn.naive_bayes import GaussianNB
    import numpy as np
    global a, tahun


    X = np.array([[0, 0.199], [0.2, 0.399], [0.4, 0.599], [0.6, 0.799], [0.8, 1]])
    Y = np.array(['Sangat Rendah', 'Rendah', 'sedang', 'kuat', 'Sangat Kuat'])

    clf = GaussianNB()

    clf.fit(X, Y)

    post_desc = table_post_description.objects.get(id = id)
    regkor = regresi_korelasi.objects.get(post_id = id)
    data = Import_Nilai.objects.filter(post_id=id)
    tahunp = Import_Nilai.objects.filter(post_id=id)
    for i in tahunp :
        tahun = i.tahun

    hasil = clf.predict([regkor.hasil_korelasi, regkor.hasil_korelasi])

    return render(request, 'home/post.html', {'post_desc': post_desc, 'regkor':regkor, 'data':data, 'id' : id, 'hasil':hasil, 'tahun' : tahun})

def chart(request, img_id):
    import django

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure

    fig = Figure()
    ax = fig.add_subplot(3,1,1)
    bx = fig.add_subplot(3,1,2)
    cx = fig.add_subplot(3,1,3)
    data = Import_Nilai.objects.filter(post_id=img_id)

    data_regresi = regresi_korelasi.objects.get(post_id=img_id)
    a = data_regresi.hasil_regresi_a
    b = data_regresi.hasil_regresi_b
    Y = []

    x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y=[]
    y2=[]
    xticst = ['january', 'February', 'Maret', 'april', 'mei', 'june', 'july', 'agustus', 'september', 'oktober', 'november', 'desember']
    for i in data:
        y.append(i.berat)
        y2.append(i.nilai)
        Y.append(a + (b * i.nilai))

    ax.plot(x,y,'-', label='berat (Kg)')
    bx.plot(x, y2, 'r-', label='Nilai (Rp)')
    cx.plot(x, Y, 'g-', label='Regresi (Nilai)')
    ax.set_xticks(x, minor=False)
    ax.set_xticklabels(xticst, fontdict=None, minor=False, fontsize = 8, rotation=30)
    bx.set_xticks(x, minor=False)
    bx.set_xticklabels(xticst, fontdict=None, minor=False, fontsize=4, rotation=30)
    cx.set_xticks(x, minor=False)
    cx.set_xticklabels(xticst, fontdict=None, minor=False, fontsize=10, rotation=20)
    ax.legend()
    bx.legend()
    cx.legend()
    ax.xaxis.set_visible(False)
    bx.xaxis.set_visible(False)
    canvas = FigureCanvas(fig)
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

@login_required(login_url='login')
def delete_post(request, id):

    table_post_description.objects.filter(id = id).delete()


    return redirect(home)


