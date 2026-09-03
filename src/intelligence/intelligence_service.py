from src.intelligence.llm_client import LLMClient
from src.intelligence.models import ArticleIntelligence
from src.intelligence.exceptions import IntelligenceGenerationError,LLMClientError
from pydantic import ValidationError
import json


class IntelligenceService:

    def __init__(self, llm_client:LLMClient):
        self.llm_client = llm_client

    def _build_prompt(self, clean_evidence:str) -> str:
        prompt = f"""
        You are an AI research intelligence analyst.

        Use only the provided article evidence.
        Do not invent unsupported information.

        Your task:
       - Produce a concise summary.
       - Extract the key research points.
       - Explain why the development matters.

        Return only valid JSON with these fields:
       {{
         "summary": "string",
         "key_points": ["string", "string", "string"],
         "why_it_matters": "string"
        }}

       ARTICLE EVIDENCE:
       {clean_evidence}
    """
        return prompt

    def generate(self, clean_evidence:str) -> ArticleIntelligence:

        if not clean_evidence.strip():
          raise IntelligenceGenerationError(
             "Clean article evidence is empty"
          )

        prompt = self._build_prompt(clean_evidence)




        try:
           raw_response = self.llm_client.generate(prompt)

        except LLMClientError as exc:
           raise IntelligenceGenerationError(
              "LLM client failed during intelligence generation."
           ) from exc

        try:
         parsed_response = json.loads(raw_response)

        except json.JSONDecodeError as exc:
             raise IntelligenceGenerationError(
                 "LLM return invalid json."
             ) from exc

        try:
         intelligence = ArticleIntelligence.model_validate(parsed_response)
        except  ValidationError as exc:
           raise IntelligenceGenerationError(
              "LLM returned invalid intelligence structure. "
           ) from exc
        return intelligence
