from src.ingestion.collector import Collector
from src.ingestion.sources.openai_source import OpenAISource
from typing import List
source = OpenAISource()
sources = [source]

collector = Collector(sources)
all_updates = collector.collect()
print(all_updates[:3])
print(f"Total updates:{len(all_updates)}")