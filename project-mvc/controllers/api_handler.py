import random


def get_users():

    # Simulasi kadang berhasil, kadang gagal
    if random.choice([True, False]):
        return {
            "status": "success",
            "data": [
                {"id": 101, "name": "Produk A"},
                {"id": 102, "name": "Produk B"}
            ]
        }

    return {
        "status": "error",
        "message": "Server sedang sibuk. Silakan coba lagi."
    }