from src.orchestrator import Orchestrator

orchestrator = Orchestrator()

save_updates = orchestrator.run()

print(f"Saved {save_updates} AI Updates.")

