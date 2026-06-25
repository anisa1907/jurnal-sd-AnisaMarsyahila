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