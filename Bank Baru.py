import random as r
import pickle as p
import os.path as o

while True:
    print("-"*80)
    print("Banking System".center(80))
    print("-"*80)
    print("1.Admin Login\n2.Customer Login")
    choice=int(input("Select:"))
    if choice==1:
        admin_id=input("Enter Admin Id: ")
        password=input("Enter Admin Password: ")
        if (
            admin_id == "Dzakiy" or admin_id == "Matin" or admin_id == "Lenny"
            or admin_id == "Revalina" and password == "1234"
            ):
            while True:
                print("-"*80)
                print("Admin Panel".center(80))
                print("-"*80)
                print("1. Tambahkan akun baru")
                print("2. Hapus akun")
                print("3. Edit akun")
                print("4. Lihat semua akun")
                print("5. Cari akun")
                print("0. Keluar")
                
                choice=int(input("Select:"))
                if choice==1:
                    if o.isfile("Accounts.bat"):            
                        read_file=open("Accounts.bat","rb")
                        Accounts=p.load(read_file)
                        read_file.close()
                    else:
                        print("Data Tidak Tersedia")
                        Accounts = {}

                    ac_no=input("Masukkan nomor akun: ")
                    if ac_no in Accounts.keys():
                        print("Nomor ini sudah digunakan")
                        continue
                    name=input("Masukkan nama pemilik akun: ")
                    phone=input("Masukkan nomor ponsel: ")
                    address=input("Masukkan alamat: ")
                    gender=input("Masukkan jenis kelamin: ")
                    password=r.randint(100000,1000000)
                    balance=0

                    Accounts[ac_no]=[name,phone,address,gender,password,balance]

                    write_file=open("Accounts.bat","wb")
                    p.dump(Accounts,write_file)
                    write_file.close()
                    print("Akun berhasil dibuat")
                elif choice==2:
                    if o.isfile("Accounts.bat"):            
                        read_file=open("Accounts.bat","rb")
                        Accounts=p.load(read_file)
                        read_file.close()
                    else:
                        print("Data Tidak Tersedia")
                        continue

                    ac_no=input("Masukkan nomor akun: ")
                    if ac_no in Accounts.keys():
                        del Accounts[ac_no]
                        write_file=open("Accounts.bat","wb")
                        p.dump(Accounts,write_file)
                        write_file.close()
                        print("Akun berhasil dihapus")
                    else:
                        print("Akun tidak ditemukan")
                elif choice==3:
                    if o.isfile("Accounts.bat"):            
                        read_file=open("Accounts.bat","rb")
                        Accounts=p.load(read_file)
                        read_file.close()
                    else:
                        print("Data tidak tersedia")
                        continue

                    ac_no=input("Masukkan nomor akun: ")
                    if ac_no in Accounts.keys():
                        print("-"*80)
                        print("Nama pemilik     : ",Accounts[ac_no][0])
                        print("Nomor ponsel     : ",Accounts[ac_no][1])
                        print("Alamat           : ",Accounts[ac_no][2])
                        print("Jenis kelamin    : ",Accounts[ac_no][3])
                        print("PIN              : ",Accounts[ac_no][4])
                        print("Saldo            : Rp. ",Accounts[ac_no][5])
                        print("-"*80)
                        print("Apa yang ingin dirubah: ")
                        print("0. Nama pemilik")
                        print("1. Nomor ponsel")
                        print("2. Alamat")
                        print("3. Jenis kelmin")
                        choice=int(input())
                        if choice>=0 and choice<4:
                            v=input("Masukkan data baru: ")
                            if v!="":
                                Accounts[ac_no][choice]=v
                                write_file=open("Accounts.bat","wb")
                                p.dump(Accounts,write_file)
                                write_file.close()
                                print("Akun berhasil diperbaharui")
                            else:
                                print("Coba lagi...")
                        else:
                            print("Pilihan tidak tersedia")
                    else:
                        print("Akun tidak ditemukan")
                elif choice==4:
                    if o.isfile("Accounts.bat"):            
                        read_file=open("Accounts.bat","rb")
                        Accounts=p.load(read_file)
                        read_file.close()
                    else:
                        print("Data Tidak Tersedia")
                        continue

                    print("-"*80)
                    print("Account Table".center(80))
                    print("-"*80)
                    for account in Accounts:
                        print(account,Accounts[account])
                elif choice==5:
                    if o.isfile("Accounts.bat"):            
                        read_file=open("Accounts.bat","rb")
                        Accounts=p.load(read_file)
                        read_file.close()
                    else:
                        print("Data Tidak Tersedia")
                        continue

                    ac_no=input("Masukkan nomor akun: ")
                    if ac_no in Accounts.keys():
                        print("-"*80)
                        print("Nama pemilik     : ",Accounts[ac_no][0])
                        print("Nomor ponsel     : ",Accounts[ac_no][1])
                        print("Alamat           : ",Accounts[ac_no][2])
                        print("Jenis kelamin    : ",Accounts[ac_no][3])
                        print("PIN              : ",Accounts[ac_no][4])
                        print("Saldo            : Rp.",Accounts[ac_no][5])
                        print("-"*80)
                    else:
                        print("Akun tidak ditemukan")
                elif choice==0:
                    break
                input("Lanjut...")
        else:
            print("Nomor akun/PIN salah")
    elif choice==2:
        while True:
            if o.isfile("Accounts.bat"):            
                read_file=open("Accounts.bat","rb")
                Accounts=p.load(read_file)
                read_file.close()
            else:
                print("Data Tidak Ditemukan")
                break

            act_no=input("Masukkan nomor akun: ")
            if act_no in Accounts.keys():
                password=int(input("Masukkan PIN: "))
                if Accounts[act_no][4]==password:
                    while True:
                        print("-"*80)
                        print("Customer Panel".center(80))
                        print("-"*80)
                        print("1. Setor tunai")
                        print("2. Tarik tunai")
                        print("3. Cek saldo")
                        print("0. Keluar")
                        choice=int(input("Select:"))
                        if choice==1:
                            amount=int(input("Masukkan jumlah setor tunai: "))
                            Accounts[act_no][5]=int(Accounts[act_no][5])+amount
                            write_file=open("Accounts.bat","wb")
                            p.dump(Accounts,write_file)
                            write_file.close()
                            print("Setor tunai berhasil.")
                        elif choice==2:
                            amount=int(input("Masukkan jumlah saldo yang ingin ditarik: "))
                            if(Accounts[act_no][5]>amount):
                                Accounts[act_no][5]=int(Accounts[act_no][5])-amount
                                write_file=open("Accounts.bat","wb")
                                p.dump(Accounts,write_file)
                                write_file.close()
                                print("Saldo berhasil ditarik.")
                            else:
                                print("Penarikan gagal.")
                        elif choice==3:
                            print("Balance:Rp.",Accounts[act_no][5])
                        elif choice==0:
                            break
                        input("Lanjut...")
                else:
                    print("PIN salah")
            else:
                print("Akun tidak ditemukan")
