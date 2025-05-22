from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Project
from .forms import ProjectForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # nama URL ke dashboard kamu
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')


def catatanpemeliharaan(request):
    return render(request, 'catatanpemeliharaan.html')

def simpan_project(request):
    if request.method == 'POST':
        nama_project = request.POST.get('nama_project')
        model = request.POST.get('model')
        deskripsi = request.POST.get('deskripsi')

        Project.objects.create(
            nama_project=nama_project,
            model=model,
            deskripsi=deskripsi
        )

        return redirect('/')  # Ganti ke halaman yang kamu inginkan setelah menyimpan
    return render(request, 'form_project.html')  # Ganti ke nama template HTML kamu


def project_form_view(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'project_form.html', {'form': form})