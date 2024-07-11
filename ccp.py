import requests
import random
import time

# Fungsi untuk membaca user_id dari file data.txt
def read_user_id():
    with open('data.txt', 'r') as file:
        user_ids = file.read().splitlines()
    return user_ids

# Fungsi untuk mengirim permintaan POST dengan data acak
def send_post_request(user_id, point_range):
    url = "https://api3.chaincrops.io/app/increment_point"
    point_taped = random.randint(point_range[0], point_range[1])
    payload = {
        "user_id": user_id,
        "point_taped": str(point_taped),
        "level_name": "Basic",
        "level_limit": "2000"
    }
    response = requests.post(url, json=payload)
    return response.status_code, response.json()

# Fungsi untuk hitung mundur
def countdown(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        hrs, mins = divmod(mins, 60)
        timeformat = f'{hrs:02}:{mins:02}:{secs:02}'
        print(f'Countdown: {timeformat}', end='\r')
        time.sleep(1)
        total_seconds -= 1
    print('Countdown: 00:00:00')

# Fungsi utama untuk menjalankan proses
def main(point_range):
    user_ids = read_user_id()
    total_users = len(user_ids)
    print(f"Total akun: {total_users}")
    
    for index, user_id in enumerate(user_ids, start=1):
        status_code, response_data = send_post_request(user_id, point_range)
        print(f"Proses akun {index}/{total_users} | User ID: {user_id} | Status Code: {status_code} | Response: {response_data}")
        time.sleep(1)  # Memberikan jeda 1 detik antar permintaan
    
    # Hitung mundur 2 jam setelah semua permintaan selesai
    print("Menunggu selama 2 jam sebelum menjalankan proses berikutnya...")
    countdown(2, 0, 0)

if __name__ == "__main__":
    # Meminta pengguna memasukkan rentang angka point_taped
    point_range_start = int(input("Masukkan angka awal untuk rentang point_taped: "))
    point_range_end = int(input("Masukkan angka akhir untuk rentang point_taped: "))
    point_range = (point_range_start, point_range_end)
    
    # Menjalankan fungsi utama
    main(point_range)
