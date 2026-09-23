from login import login
from profile import display_profile
from dashboard import show_dashboard


print("Git Branching Demo")
print("Welcome to the Learning Platform")

print("\n=== Login ===")
print(login("admin", "1234"))

print("\n=== Profile ===")
display_profile("Rahul", "rahul@gmail.com")

print("\n=== Dashboard ===")
show_dashboard()
