from django.shortcuts import render
from AHPSPK.models import *
from AHPSPK.forms import *
from django.shortcuts import redirect
from django.contrib import messages
import numpy as np
# Create your views here.
def TambahLaptop(request):
    if request.POST:
        form = FormLaptop(request.POST)
        if form.is_valid():
            form.save()
            form = FormLaptop
            konteks = {
                'form':form,
            }
            return (redirect('index'))
    else:
        form = FormLaptop()
        konteks = {
            'form':form,
        }
        return render(request,'tambah_laptop.html',konteks)

def SHOWLaptop(request):
    laptops = Laptop.objects.all()

    konteks = {
        'laptop' : laptops,
    }
    return render(request, 'index.html', konteks)

def ubah_data(request, id_laptop):
    laptop = Laptop.objects.get(id = id_laptop)
    if request.POST:
        form = FormLaptop(request.POST,instance=laptop)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Diubah")
            return redirect('ubah',id_laptop=id_laptop)
    else:
        form = FormLaptop(instance=laptop)
        konteks = {
            'form':form,
            'laptop':laptop
        }
        return render(request,'ubah_data.html',konteks)

def hapus_data(request, id_laptop):
    laptop = Laptop.objects.filter(id=id_laptop)
    laptop.delete()
    return redirect('index')


def coba(request):
    l = Laptop.objects.all()
    Kriteria = kriteria_nilai.objects.all()
    laptop=[]
    for x in l:
        laptop.append([x.Laptop,x.Harga,x.RAM,x.Processor.Nilai,x.Storage,x.Berat])
    kriteria = [Kriteria[0].kharga,Kriteria[0].kram,
            Kriteria[0].kprocessor,Kriteria[0].kstorage,
            Kriteria[0].kberat,]
    """
    kriteria = [
        1, 3, 2, 3, 3
    ]"""
    nama_kriteria=[
        "Harga","RAM","Processor","Storage","Berat"
    ]
    jadi = np.zeros([len(kriteria), len(kriteria)])
    jadi2 = np.zeros([len(kriteria), len(kriteria)])

    for x in range(len(kriteria)):
        for y in range(len(kriteria)):
            n1 = kriteria[x]
            n2 = kriteria[y]
            if n1 > n2:
                if n1 - n2 == 2:
                    jadi[x][y] = round(1 / 5, 2)
                elif n1 - n2 == 1:
                    jadi[x][y] = round(1 / 3, 2)
                elif n1 - n2 == 3:
                    jadi[x][y] = round(1 / 7, 2)
                elif n1 - n2 == 4:
                    jadi[x][y] = round(1 / 9, 2)

            elif n1 < n2:
                if n2 - n1 == 2:
                    jadi[x][y] = 5
                elif n2 - n1 == 1:
                    jadi[x][y] = 3
                elif n2 - n1 == 3:
                    jadi[x][y] = 7
                elif n2 - n1 == 4:
                    jadi[x][y] = 9

            elif n1 == n2:
                jadi[x][y] = 1

    T1 = jadi.sum(axis=0)

    for x in range(len(jadi)):
        for y in range(len(jadi[x])):
            ang = jadi[x][y]
            jadi2[x][y] = ang / T1[y]
    T2 = jadi2.sum(axis=0)
    for x in range(len(T2)):
        T2[x]= round(T2[x])

    putar = np.rot90(jadi2, 45)
    rata = putar.sum(axis=0)
    for y in range(len(rata)):
        rata[y] = rata[y] / len(putar)
    putar_rata = rata.reshape(len(rata), 1)
    kali = jadi.dot(putar_rata)
    bagi = np.zeros(len(kali))
    for x in range(len(kali)):
        bagi[x] = kali[x] / putar_rata[x]
    putar_bagi = bagi.reshape(len(bagi), 1)

    t = (1 / len(kriteria)) * putar_bagi.sum(axis=0)
    if (t<len(kriteria)):
        CI = (len(kriteria)-t) / (len(kriteria) - 1)
    else:
        CI = (t - len(kriteria)) / (len(kriteria) - 1)
    CR = CI / 1.12

    list_harga = []
    list_ram = []
    list_processor = []
    list_storage = []
    list_berat = []

    for x in laptop:
        list_harga.append(x[1])
        list_ram.append(x[2])
        list_processor.append(x[3])
        list_storage.append(x[4])
        list_berat.append(x[5])
    npharga = np.array(list_harga).reshape(len(list_harga), 1)
    min_harga = npharga.min(axis=0)
    rharga = np.array([float(min_harga / x) for x in npharga]).reshape(len(list_harga), 1)
    trasio_harga = rharga.sum(axis=0)
    normalisasi_harga = np.array([float(x / trasio_harga) for x in rharga]).reshape(len(list_harga), 1)
    # print("MIN=", min_harga)
    # print(rharga)
    # print(trasio_harga)

    npram = np.array(list_ram).reshape(len(list_ram), 1)
    total_ram = npram.sum(axis=0)
    # print(total_ram)
    normalisasi_ram = np.array([float(x / total_ram) for x in npram]).reshape(len(list_ram), 1)

    npprocessor = np.array(list_processor).reshape(len(list_processor), 1)
    total_processor = npprocessor.sum(axis=0)
    normalisasi_processor = np.array([float(x / total_processor) for x in npprocessor]).reshape(len(list_processor), 1)

    npstorage = np.array(list_storage).reshape(len(list_storage), 1)
    total_storage = npstorage.sum(axis=0)
    normalisasi_storage = np.array([float(x / total_storage) for x in npstorage]).reshape(len(list_storage), 1)


    npberat = np.array(list_berat).reshape(len(list_berat), 1)
    min_berat = npberat.min(axis=0)
    rberat = np.array([float(min_berat / x) for x in npberat]).reshape(len(list_berat), 1)
    trasio_berat = rberat.sum(axis=0)
    normalisasi_berat = np.array([float(x / trasio_berat) for x in rberat]).reshape(len(list_berat), 1)
    # print("MIN=", min_harga)
    # print(rharga)
    # print(trasio_harga)

    hasil = []
    for x in range(len(laptop)):
        hasil.append([float(normalisasi_harga[x]), float(normalisasi_ram[x]), float(normalisasi_processor[x]),
                      float(normalisasi_storage[x]), float(normalisasi_berat[x])])
    nphasil = np.array(hasil)
    rank = nphasil.dot(putar_rata)
    maxrank = rank.max(axis=0)

    hasil_akhir = []
    for x in range(len(laptop)):
        hasil_akhir.append(
            [laptop[x][0], float(normalisasi_harga[x]), float(normalisasi_ram[x]), float(normalisasi_processor[x]),
             float(normalisasi_storage[x]), float(normalisasi_berat[x]),float(rank[x])])


    hasil_akhir = sorted(hasil_akhir, key=lambda x: x[6], reverse=True)

    Tabel1_print =[]
    Tabel2_print = []
    for x in range(len(jadi)):
        Tabel1_print.append([nama_kriteria[x],jadi[x][0],jadi[x][1],jadi[x][2],jadi[x][3],jadi[x][4]])
        Tabel2_print.append([nama_kriteria[x], jadi2[x][0], jadi2[x][1], jadi2[x][2], jadi2[x][3], jadi2[x][4]])

    konteks={
        'laptop' : laptop,
        'jadi':Tabel1_print,
        'Tabel2':Tabel2_print,
        'T1':T1,
        'T2':T2,
        'ratarata':rata,
        'kriteria':nama_kriteria,
        't':t,
        'CI':CI,
        'CR':CR,
        'Hasilakhir':hasil_akhir,
    }

    return render(request,'hasil.html',konteks)

def testing(request):
    Kriteria = kriteria_nilai.objects.get(id=1)
    kriteria = [Kriteria.kharga, Kriteria.kram,
                Kriteria.kprocessor, Kriteria.kstorage,
                Kriteria.kberat, ]

    if request.POST:
        form = FormKriteria(request.POST, instance=Kriteria)
        if form.is_valid():
            form.save()
            return redirect('hasil')
    else:
        Kriteria = kriteria_nilai.objects.get(id=1)
        form = FormKriteria(instance=Kriteria)
        konteks = {
            'form': form,
            'kharga' : kriteria[0],
            'kram' : kriteria[1],
            'kprocessor' : kriteria[2],
            'kstorage' : kriteria[3],
            'kberat' :kriteria[4],
        }
        return render(request, 'testing.html', konteks)