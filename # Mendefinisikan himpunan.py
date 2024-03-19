# Mendefinisikan himpunan
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Operasi himpunan
gabungan = A.union(B)  
irisan = A.intersection(B)  
selisih = A.difference(B)  
diferensi_simetris = A.symmetric_difference(B)  

# Menampilkan hasil
print("hasil gabungan himpunan A dan B : ", gabungan)
print("hasil irisan himpunan A dan B : ", irisan)
print("hasil selisih himpunan A dan B : ", selisih)
print("hasil diferensi simetris himpunan A dan B : ", diferensi_simetris)