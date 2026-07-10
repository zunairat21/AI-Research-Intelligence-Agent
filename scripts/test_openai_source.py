from src.ingestion.sources.openai_source import OpenAISource

source = OpenAISource()

response = source.fetch_raw_data()
print(response.status_code) 
print(response.url)
print(response.headers.get("content-type"))
print(response.text[:1000])
    
updates = source.parse_response(response)
print(updates[:3])

ai_updates = source.convert_to_ai_updates(updates)
print(ai_updates[:3])