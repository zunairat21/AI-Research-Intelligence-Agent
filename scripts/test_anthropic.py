from src.ingestion.sources.anthropic_source import AnthropicSource

source = AnthropicSource()

response = source.fetch_raw_data()

parsed_response = source.parse_response(response)

print(parsed_response[:3])

ai_updates  = source.convert_to_ai_updates(parsed_response)
print(ai_updates[:3])

