from src.intelligence.llm_client import LLMClient

class FakeLLMClient(LLMClient):
    def generate(self, prompt:str) -> str:
        return "fake response"


client = FakeLLMClient()
response = client.generate("Summarizr the article")
print(response)