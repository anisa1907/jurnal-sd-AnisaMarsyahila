from views.dashboard_component import show_dashboard

state = {
    "user": "Admin",
    "score": 0
}


def tambah_score():
    state["score"] += 10


print("State awal:")
show_dashboard(state["user"], state["score"])

tambah_score()

print("\nState setelah update:")
show_dashboard(state["user"], state["score"])