from src.ingestion.sources.openai_source import OpenAISource

source = OpenAISource()

response = source.fetch_raw_data()
    
parsed_updates = source.parse_response(response)
print(parsed_updates[:3])

ai_updates = source.convert_to_ai_updates(parsed_updates)
print(ai_updates[:3])