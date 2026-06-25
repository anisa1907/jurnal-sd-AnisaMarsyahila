from views.dashboard_component import render_dashboard


# Simulasi State
app_state = {
    "items": [],
    "is_loading": True
}


def update_state(new_data):
    app_state["items"] = new_data
    app_state["is_loading"] = False


if __name__ == "__main__":

    # Kondisi loading
    print("=== DATA SEDANG DIMUAT ===")
    render_dashboard(
        app_state["items"],
        app_state["is_loading"]
    )

    print("\nLoading data...\n")

    # Simulasi data masuk dari Backend
    mock_data = [
        {"id": 101, "name": "Produk A"},
        {"id": 102, "name": "Produk B"}
    ]

    update_state(mock_data)

    # Kondisi setelah loading selesai
    print("=== DATA BERHASIL DIMUAT ===")
    render_dashboard(
        app_state["items"],
        app_state["is_loading"]
    )