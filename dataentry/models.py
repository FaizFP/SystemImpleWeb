from django.db import models

class Project(models.Model):
    nama_project = models.CharField(primary_key=True, max_length=100)
    model = models.CharField(max_length=100)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama_project


class DataLingkungan(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='data_lingkungan')
    ram = models.CharField(max_length=100)
    database = models.CharField(max_length=100)
    cpu = models.CharField(max_length=100)
    os = models.CharField(max_length=100)


class CatatanPemeliharaan(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='catatan_pemeliharaan')
    suggest = models.TextField()
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=50)


class DataTransaksi(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='data_transaksi')
    deskripsi_data = models.TextField()
    input_file = models.FileField(upload_to='transaksi_files/')
