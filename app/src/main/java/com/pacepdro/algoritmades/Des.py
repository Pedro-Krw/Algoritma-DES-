# des_encryption.py

def permute(input_bitstring, table):
    # Fungsi ini melakukan permutasi berdasarkan tabel yang diberikan
    return ''.join(input_bitstring[i-1] for i in table)

def key_schedule(key):
    # Generate 16 subkeys untuk tiap ronde DES
    return [key] * 16  # Sederhana, ini bisa dikembangkan lagi

def encrypt(plaintext, key):
    # Permutasi awal (simplifikasi)
    ip = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4]
    permuted_text = permute(plaintext, ip)

    # Split menjadi dua bagian
    left, right = permuted_text[:32], permuted_text[32:]

    # 16 ronde enkripsi
    subkeys = key_schedule(key)
    for i in range(16):
        # Di sini lakukan operasi DES pada left dan right
        left, right = right, left  # Hanya swap untuk contoh

    # Permutasi akhir
    final_perm = [40, 8, 48, 16, 56, 24, 64, 32]
    ciphertext = permute(left + right, final_perm)

    return ciphertext

def decrypt(ciphertext, key):
    # Dekripsi menggunakan kebalikan dari enkripsi
    return encrypt(ciphertext, key)  # Hanya contoh sederhana