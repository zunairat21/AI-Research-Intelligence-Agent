from src.intelligence.exceptions import (
    IntelligenceGenerationError,
    LLMClientError,
)
from src.intelligence.intelligence_service import IntelligenceService
from src.intelligence.llm_client import LLMClient


class FakeLLMClient(LLMClient):

    def generate(self, prompt: str) -> str:
        return """
        {
            "summary": "OpenAI introduced a new reasoning model with stronger performance on coding and mathematics tasks.",
            "key_points": [
                "The model showed improved coding performance.",
                "The model showed improved mathematical reasoning.",
                "The update focuses on stronger reasoning capabilities."
            ],
            "why_it_matters": "Improved reasoning performance could make AI systems more useful for complex technical and analytical tasks."
        }
        """


fake_client = FakeLLMClient()
service = IntelligenceService(fake_client)

clean_evidence = """
OpenAI introduced a new reasoning model.
The model showed improved performance on coding and mathematics.
"""

intelligence = service.generate(clean_evidence)


# -------------------------
# Empty evidence test
# -------------------------

try:
    service.generate(" ")

    assert False, "Expected IntelligenceGenerationError"

except IntelligenceGenerationError:
    print("Empty evidence test passed.")


# -------------------------
# Happy-path test
# -------------------------

assert intelligence.summary == (
    "OpenAI introduced a new reasoning model with stronger "
    "performance on coding and mathematics tasks."
)

assert intelligence.key_points == [
    "The model showed improved coding performance.",
    "The model showed improved mathematical reasoning.",
    "The update focuses on stronger reasoning capabilities.",
]

assert intelligence.why_it_matters == (
    "Improved reasoning performance could make AI systems "
    "more useful for complex technical and analytical tasks."
)

print("IntelligenceService happy-path test passed.")


# -------------------------
# LLM client failure test
# -------------------------

class FailingLLMClient(LLMClient):

    def generate(self, prompt: str) -> str:
        raise LLMClientError(
            "LLM provider request failed."
        )


failing_client = FailingLLMClient()

failing_service = IntelligenceService(
    failing_client
)

valid_evidence = "This is valid article evidence."

try:
    failing_service.generate(valid_evidence)

    assert False, "Expected IntelligenceGenerationError"

except IntelligenceGenerationError:
    print("LLM client failure test passed.")


# -------------------------
# Invalid JSON test
# -------------------------

class BadJSONLLMClient(LLMClient):

    def generate(self, prompt: str) -> str:
        return "This is not a valid JSON response."


bad_json_client = BadJSONLLMClient()

bad_json_service = IntelligenceService(
    bad_json_client
)

try:
    bad_json_service.generate(valid_evidence)

    assert False, "Expected IntelligenceGenerationError"

except IntelligenceGenerationError:
    print("LLM invalid JSON test passed.")


# -------------------------
# Invalid structure test
# -------------------------

class InvalidStructureLLMClient(LLMClient):

    def generate(self, prompt: str) -> str:
        return """
        {
            "summary": "A model was released.",
            "key_points": [],
            "why_it_matters": ""
        }
        """


invalid_structure_client = InvalidStructureLLMClient()

invalid_structure_service = IntelligenceService(
    invalid_structure_client
)

try:
    invalid_structure_service.generate(valid_evidence)
    assert False, "Expected IntelligenceGenerationError"

except IntelligenceGenerationError:
    print("LLM structure invalid test passed.")
