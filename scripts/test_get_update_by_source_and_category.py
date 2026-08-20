from src.storage.storage import Storage

storage = Storage()

updates= storage.get_update_by_source_and_category("DeepMind", "Models")

print(updates[:3])
