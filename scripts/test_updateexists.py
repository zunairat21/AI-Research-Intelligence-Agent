from src.storage.storage import Storage

storage = Storage()

#True Case :
duplicate_exist = storage.update_exists("https://example.com/meta/llama5-launch")

print(f"Duplicate exist {duplicate_exist}")

#False case 

duplicate_exist = storage.update_exists("https://example.com/google/gemini-3-release")

print(f"Duplicate exist {duplicate_exist}")
