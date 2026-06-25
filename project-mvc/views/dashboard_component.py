def render_dashboard(data_list, is_loading=False):
    print("--- DASHBOARD APLIKASI ---")

    if is_loading:
        print("Mohon Tunggu...")
    elif not data_list:
        print("[!] Data Kosong. Silakan sinkronisasi dengan Backend.")
    else:
        for item in data_list:
            print(f"- Item ID: {item['id']} | Nama: {item['name']}")


def fetch_data_from_api(api_function):
    print("[System] Mencoba menghubungkan ke API...")

    try:
        response = api_function()

        if response["status"] == "success":
            print("[System] Integrasi berhasil.")
            return response["data"]

        else:
            error_message = response.get(
                "message",
                "Terjadi kesalahan pada server."
            )

            raise Exception(error_message)

    except Exception as e:
        print(f"[Error] Gagal Integrasi: {e}")
        print("[User] Data tidak dapat ditampilkan. Silakan coba lagi nanti.")
        return None