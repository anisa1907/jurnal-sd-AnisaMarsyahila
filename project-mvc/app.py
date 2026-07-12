import os

user_name = os.getenv("APP_USER", "Guest")
app_env = os.getenv("APP_ENV", "development")

from controllers.api_handler import get_users
from views.dashboard_component import (
    render_dashboard,
    fetch_data_from_api
)


# Simulasi State
app_state = {
    "items": [],
    "is_loading": True
}


def update_state(new_data):
    app_state["items"] = new_data
    app_state["is_loading"] = False


if __name__ == "__main__":

    print(f"Halo {user_name}!")
    print(f"Environment: {app_env}")
    print("=== VERSI 2.0 - STABIL ===")
    print("Aplikasi ini berjalan di dalam kontainer Docker.\n")

    print("=== DATA SEDANG DIMUAT ===")

    render_dashboard(
        app_state["items"],
        app_state["is_loading"]
    )

    print("\nLoading data...\n")

    data = fetch_data_from_api(get_users)

    if data:
        update_state(data)

        print("\n=== DATA BERHASIL DIMUAT ===")

        render_dashboard(
            app_state["items"],
            app_state["is_loading"]
        )

    else:
        print("\n=== DATA GAGAL DIMUAT ===")