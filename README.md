# AI Research Intelligence Agent

## 📌 Project Overview

AI Research Intelligence Agent is a modular Python application that automatically collects AI news and research updates from trusted AI research organizations.

The system currently collects updates from:

- OpenAI
- Anthropic
- Google DeepMind

Each source has its own scraping logic, but all collected information is converted into a common `AIUpdate` data model before entering the shared processing pipeline.

The application validates and cleans incoming updates, prevents duplicate records, stores structured information in SQLite, and exposes the collected intelligence through a FastAPI REST API.

The API allows external clients to:

- Retrieve all stored AI research updates
- Filter updates by source
- Filter updates by category
- Combine source and category filters
- Trigger a fresh multi-source collection run
- Receive structured JSON responses
- Interact with automatically generated Swagger/OpenAPI documentation

The project follows a modular architecture where components have focused responsibilities and can be developed and tested independently.

---

# 🎯 Project Goals

- Collect AI news from multiple trusted sources
- Standardize source-specific information into a common data model
- Validate incoming research updates
- Clean inconsistent data
- Store structured AI updates
- Prevent duplicate news automatically
- Build a scalable multi-source ingestion pipeline
- Expose collected intelligence through a REST API
- Apply input validation and meaningful HTTP error handling
- Generate AI-powered summaries and research insights
- Detect trends across AI research updates
- Build an interactive AI research intelligence dashboard

---

# 📖 Development Approach

The project is being developed incrementally using a learning-first software engineering workflow.

For every major component:

1. Understand the problem
2. Design the expected behavior
3. Implement the component
4. Test it independently
5. Integrate it with the existing system
6. Perform end-to-end testing
7. Commit the completed milestone
8. Update project documentation

The goal is not only to build an AI application, but also to practice professional backend development, API design, modular architecture, testing, Git version control, and AI engineering principles.

---

# 🚀 Current Status

**Current Phase:** ✅ Phase 5 – FastAPI REST API Completed

## Completed Phases

- ✅ Phase 1 – Foundation
- ✅ Phase 2 – Storage Layer
- ✅ Phase 3 – End-to-End AI Research Pipeline
- ✅ Phase 4 – Multi-Source Collection
- ✅ Phase 5 – FastAPI REST API

## Next Phase

- 🚧 Phase 6 – AI Intelligence

---

# 🏗 System Architecture

```text
                     AI Research Sources
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
     OpenAI News       Anthropic News    DeepMind News
          │                 │                 │
          ▼                 ▼                 ▼
    OpenAISource      AnthropicSource    DeepMindSource
          │                 │                 │
          └─────────────────┼─────────────────┘
                            │
                            ▼
                   Common AIUpdate Model
                            │
                            ▼
                        Validator
                            │
                            ▼
                         Cleaner
                            │
                            ▼
                    Duplicate Detection
                            │
                            ▼
                       Storage Layer
                            │
                            ▼
                     SQLite Database
                            ▲
                            │
                ┌───────────┴───────────┐
                │                       │
                │                       │
         GET /updates             POST /refresh
                ▲                       │
                │                       ▼
           FastAPI API             Orchestrator
                ▲                       │
                │                       │
        Client / Swagger UI        AI Sources
```

The API does not directly contain database or scraping logic.

Responsibilities remain separated:

```text
GET /updates
     │
     ▼
FastAPI
     │
     ▼
Storage
     │
     ▼
SQLite
```

while:

```text
POST /refresh
     │
     ▼
FastAPI
     │
     ▼
Orchestrator
     │
     ▼
OpenAI + Anthropic + DeepMind
     │
     ▼
Validate
     │
     ▼
Clean
     │
     ▼
Duplicate Detection
     │
     ▼
Storage
     │
     ▼
SQLite
```

This keeps API routing, ingestion, orchestration, and database responsibilities separate.

---

# 🌐 Multi-Source Ingestion Architecture

Each research source implements the same ingestion workflow:

```text
fetch_raw_data()
        │
        ▼
parse_response()
        │
        ▼
convert_to_ai_updates()
        │
        ▼
List[AIUpdate]
```

The orchestrator loops through all configured sources and passes their updates through the shared pipeline.

```text
Source
  │
  ▼
Fetch
  │
  ▼
Parse
  │
  ▼
Convert to AIUpdate
  │
  ▼
Validate
  │
  ▼
Clean
  │
  ▼
Duplicate Check
  │
  ▼
Save
```

This architecture allows additional AI research sources to be added later without redesigning the core processing pipeline.

---

# 🔄 Multi-Source Processing Flow

For every configured source, the orchestrator performs:

```text
Fetch Raw Data
      │
      ▼
Parse Source-Specific HTML
      │
      ▼
Convert to AIUpdate Objects
      │
      ▼
Validate Update
      │
      ▼
Clean Update
      │
      ▼
Check URL for Existing Record
      │
      ├── Exists ──► Skip
      │
      └── New
           │
           ▼
      Save to SQLite
```

The update URL is used for duplicate detection, preventing the same research update from being stored repeatedly across multiple pipeline runs.

---

# 🌐 FastAPI REST API

Phase 5 introduced a REST API built using FastAPI.

The API provides controlled access to the research intelligence stored in the application while reusing the existing Storage and Orchestrator components.

## Run the API

From the project root:

```bash
uvicorn src.api:app
```

The local API runs at:

```text
http://127.0.0.1:8000
```

Interactive Swagger documentation is automatically available at:

```text
http://127.0.0.1:8000/docs
```

---

# 🔌 API Endpoints

## `GET /`

Checks whether the API application is running.

### Example

```text
GET /
```

### Response

```json
{
  "message": "AI Research Intelligence Agent API is running"
}
```

### Status

```text
200 OK
```

---

## `GET /updates`

Returns all AI research updates currently stored in SQLite.

### Example

```text
GET /updates
```

### Flow

```text
Client
  │
  ▼
GET /updates
  │
  ▼
FastAPI
  │
  ▼
Storage.get_all_updates()
  │
  ▼
SQLite
  │
  ▼
AIUpdate Objects
  │
  ▼
FastAPI Serialization
  │
  ▼
JSON Response
```

---

# 🔎 Query Parameter Filtering

The `/updates` endpoint supports optional query parameters.

## Filter by Source

```text
GET /updates?source=OpenAI
```

Example supported values currently stored by the production ingestion pipeline include:

```text
OpenAI
Anthropic
DeepMind
```

The API does not hard-code these values as a whitelist.

If a valid source string matches no records, the API returns:

```json
[]
```

with:

```text
200 OK
```

because the request itself was valid.

---

## Filter by Category

```text
GET /updates?category=Product
```

Only updates matching the requested category are returned.

---

## Combined Source and Category Filtering

Multiple query parameters can be combined using `&`.

```text
GET /updates?source=OpenAI&category=Product
```

The Storage layer performs filtering using both conditions:

```text
source = OpenAI
AND
category = Product
```

Only records satisfying both conditions are returned.

---

# 🧹 Query Input Normalization

Query values are normalized before being sent to the Storage layer.

For example:

```text
"   OpenAI   "
      │
      ▼
    strip()
      │
      ▼
   "OpenAI"
```

Similarly:

```text
"   Product   "
      │
      ▼
    strip()
      │
      ▼
   "Product"
```

This prevents unnecessary leading or trailing whitespace from affecting database matching.

---

# 🛡 Input Validation and Error Handling

The FastAPI layer includes both automatic validation and application-level validation.

## `200 OK`

Returned when the request succeeds.

Examples:

```text
GET /updates
GET /updates?source=OpenAI
GET /updates?category=Product
POST /refresh
```

An empty result set is still considered successful:

```json
[]
```

---

## `400 Bad Request`

Used when the client provides a query parameter containing only whitespace.

Example:

```text
GET /updates?source=
```

After normalization:

```text
"   "
  │
  ▼
strip()
  │
  ▼
""
```

The API deliberately raises:

```text
400 Bad Request
```

Example response:

```json
{
  "detail": "Source can not be blank."
}
```

The same validation is applied to category values.

---

## `404 Not Found`

FastAPI automatically returns `404 Not Found` when the client requests an API route that does not exist.

Example:

```text
GET /abc
```

Response:

```json
{
  "detail": "Not Found"
}
```

---

## `422 Unprocessable Content`

FastAPI automatically validates the query parameters.

Both `source` and `category` use a minimum string length rule.

Example:

```text
GET /updates?source=
```

The empty value violates:

```text
min_length = 1
```

FastAPI rejects the request before the endpoint function executes.

---

## `500 Internal Server Error`

Unexpected server-side failures are handled separately from client validation errors.

The refresh endpoint executes the orchestration pipeline inside a `try / except` block.

Conceptually:

```text
POST /refresh
      │
      ▼
try
      │
      ▼
orchestrator.run()
      │
      ├── Success ──► 200 OK
      │
      └── Exception
             │
             ▼
       Server Error
             │
             ▼
            500
```

The server-side failure path was independently tested using a controlled exception.

---

# 🔄 `POST /refresh`

The refresh endpoint triggers the existing multi-source orchestration pipeline.

```text
POST /refresh
```

It does not manually insert records itself.

Instead:

```text
FastAPI
   │
   ▼
Orchestrator.run()
   │
   ├── OpenAI
   ├── Anthropic
   └── DeepMind
          │
          ▼
      Validation
          │
          ▼
       Cleaning
          │
          ▼
   Duplicate Detection
          │
          ▼
       Storage
          │
          ▼
        SQLite
```

### Example Successful Response

```json
{
  "message": "Refresh Completed",
  "saved_updates": 11
}
```

The `saved_updates` value represents the number of newly inserted research updates.

If the refresh succeeds but every collected update already exists:

```json
{
  "message": "Refresh Completed",
  "saved_updates": 0
}
```

This still returns:

```text
200 OK
```

because the refresh operation itself completed successfully.

Repeated refresh testing confirmed that duplicate updates are not inserted again.

---

# 📖 Swagger / OpenAPI Documentation

FastAPI automatically generates interactive API documentation using OpenAPI and Swagger UI.

Swagger is available locally at:

```text
http://127.0.0.1:8000/docs
```

Swagger allows developers to:

- View available endpoints
- Inspect HTTP methods
- Inspect query parameters
- Execute API requests
- View generated request URLs
- Inspect response bodies
- Inspect HTTP status codes
- Test the API interactively

The documentation is generated automatically from the FastAPI route definitions.

---

# 📸 API Demo

The screenshots below provide visual proof that the REST API is running and connected to the real project backend.

## Swagger API Documentation

Swagger UI displays the available FastAPI endpoints and allows interactive testing.

![FastAPI Swagger Documentation](docs/images/swagger-api.png)

---

## Retrieve Stored AI Updates

The `GET /updates` endpoint retrieves real AI research updates from SQLite and exposes them as JSON.

![GET Updates Response](docs/images/get-updates-response.png)

---

## Refresh AI Research Updates

The `POST /refresh` endpoint executes the full multi-source ingestion pipeline and returns the number of newly stored updates.

![POST Refresh Response](docs/images/post-refresh-response.png)

---

# 🧪 Phase 5 End-to-End API Testing

The following API scenarios were tested successfully:

```text
GET /
→ 200 OK

GET /updates
→ 200 OK + all stored updates

GET /updates?source=OpenAI
→ 200 OK + OpenAI updates

GET /updates?category=Product
→ 200 OK + Product updates

GET /updates?source=OpenAI&category=Product
→ 200 OK + records satisfying both filters

Query values with surrounding whitespace
→ normalized correctly

Whitespace-only source/category
→ 400 Bad Request

Empty validated query parameter
→ 422 validation error

Unknown API route
→ 404 Not Found

POST /refresh
→ 200 OK + saved_updates count

Immediate repeated POST /refresh
→ 200 OK + saved_updates: 0

Controlled backend failure
→ 500 Internal Server Error
```

This verifies the complete API flow from HTTP request through FastAPI, Storage or Orchestrator, SQLite, and back to the client as JSON.

---

# 📂 Project Structure

```text
AI-Research-Intelligence-Agent/
│
├── src/
│   │
│   ├── api.py
│   │
│   ├── orchestrator.py
│   │
│   ├── ingestion/
│   │   │
│   │   ├── sources/
│   │   │   ├── openai_source.py
│   │   │   ├── anthropic_source.py
│   │   │   └── deepmind_source.py
│   │   │
│   │   ├── models.py
│   │   ├── collector.py
│   │   ├── validator.py
│   │   └── cleaner.py
│   │
│   └── storage/
│       ├── database.py
│       └── storage.py
│
├── scripts/
│   ├── test_openai.py
│   ├── test_anthropic.py
│   ├── test_deepmind.py
│   ├── test_orchestrator.py
│   └── test_get_update_by_source_and_category.py
│
├── data/
│   └── ai_updates.db
│
├── requirements.txt
└── README.md
```

---

# ✅ Completed Features

## Phase 1 – Foundation

- [x] `AIUpdate` data model
- [x] Collector module
- [x] Validator module
- [x] Cleaner module

---

## Phase 2 – Storage Layer

- [x] SQLite database
- [x] Database connection
- [x] Save update
- [x] Get update by URL
- [x] Get all updates
- [x] Get updates by source
- [x] Get updates by category
- [x] Get updates by date
- [x] Get updates by source and category
- [x] Update existing records
- [x] Delete records
- [x] Duplicate detection using unique URLs
- [x] Independent Storage testing

---

## Phase 3 – End-to-End Pipeline

- [x] Pipeline Orchestrator
- [x] Source integration
- [x] Validation integration
- [x] Cleaning integration
- [x] Duplicate detection integration
- [x] SQLite storage integration
- [x] End-to-end testing
- [x] Repeated-run duplicate prevention

---

## Phase 4 – Multi-Source Collection

- [x] OpenAI News source
- [x] Anthropic News source
- [x] Google DeepMind News source
- [x] Requests-based HTTP collection
- [x] BeautifulSoup HTML parsing
- [x] Source-specific parsing
- [x] Common `AIUpdate` conversion
- [x] Multi-source Orchestrator
- [x] Cross-source pipeline testing
- [x] Duplicate prevention across multiple sources

---

## Phase 5 – FastAPI REST API

- [x] FastAPI application
- [x] Uvicorn ASGI server
- [x] Root API endpoint
- [x] `GET /updates`
- [x] Source query filtering
- [x] Category query filtering
- [x] Combined source + category filtering
- [x] FastAPI → Storage integration
- [x] `POST /refresh`
- [x] FastAPI → Orchestrator integration
- [x] JSON API responses
- [x] Query parameter validation
- [x] Input normalization
- [x] Manual `400 Bad Request`
- [x] Automatic `422` validation
- [x] `404 Not Found` behavior
- [x] Unexpected `500` server-error handling
- [x] Swagger/OpenAPI documentation
- [x] End-to-end API testing
- [x] Duplicate refresh verification

---

# 🛠 Tech Stack

## Backend

- Python 3.10+
- FastAPI
- Uvicorn

## Data Collection

- Requests
- BeautifulSoup4

## Storage

- SQLite3

## Python Engineering

- Dataclasses
- Typing
- `Annotated`

## API Technologies

- REST
- HTTP
- JSON
- OpenAPI
- Swagger UI

## Development

- Git
- GitHub

---

# 📦 Dependencies

Runtime dependencies are defined in `requirements.txt`.

Current dependencies:

```text
requests==2.34.2
beautifulsoup4==4.15.0
fastapi==0.141.1
uvicorn==0.52.1
```

Install them using:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## Run the FastAPI Server

From the project root:

```bash
uvicorn src.api:app
```

Then open:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🗺 Roadmap

## Phase 1 – Foundation ✅

- [x] AIUpdate Data Model
- [x] Collector
- [x] Validator
- [x] Cleaner

---

## Phase 2 – Storage Layer ✅

- [x] SQLite Database
- [x] CRUD Operations
- [x] Query Operations
- [x] Duplicate Detection

---

## Phase 3 – End-to-End Pipeline ✅

- [x] Pipeline Orchestrator
- [x] Validation and Cleaning Integration
- [x] SQLite Storage Integration
- [x] End-to-End Testing

---

## Phase 4 – Multi-Source Collection ✅

- [x] OpenAI Source
- [x] Anthropic Source
- [x] Google DeepMind Source
- [x] Multi-Source Orchestrator
- [x] Cross-Source Testing
- [x] Duplicate Prevention

---

## Phase 5 – FastAPI REST API ✅

- [x] FastAPI Application
- [x] REST API Design
- [x] Root Endpoint
- [x] Get All Updates Endpoint
- [x] Source Filtering
- [x] Category Filtering
- [x] Combined Query Filtering
- [x] Query Validation
- [x] Input Normalization
- [x] HTTP Error Handling
- [x] Automatic Refresh Endpoint
- [x] Swagger/OpenAPI Documentation
- [x] End-to-End API Testing

---

## Phase 6 – AI Intelligence 🚧

Phase 6 transforms collected AI research updates into evidence-grounded intelligence.

Instead of generating summaries from only a title, category, or metadata, the system first retrieves the original article, extracts meaningful content, removes source-specific webpage noise, and prepares clean evidence for downstream AI reasoning.

### Phase 6A – Evidence-Based Article Intelligence 🚧

#### Evidence Pipeline ✅

The article evidence pipeline retrieves and prepares the original research content before any LLM-based intelligence is generated.

- [x] Article fetching from stored source URLs
- [x] HTTP request timeout and error handling
- [x] Character encoding detection and correction
- [x] Source-aware article extraction
- [x] OpenAI article extraction
- [x] Anthropic article extraction
- [x] Google DeepMind article extraction
- [x] Removal of source-specific webpage noise
- [x] Removal of table-of-contents components
- [x] Removal of share controls
- [x] Removal of related-content and recommendation sections
- [x] Removal of newsletter components
- [x] Removal of script and style elements
- [x] Article whitespace normalization
- [x] Focused ArticleCleaner testing
- [x] Focused ArticleExtractor testing
- [x] Cross-source Fetch → Extract → Clean validation

#### Evidence Pipeline Architecture

```text
Stored AIUpdate
      │
      │ URL + source
      ▼
ArticleFetcher
      │
      │ HTTP GET
      ▼
Raw HTML
      │
      ▼
ArticleExtractor
      │
      ├── OpenAI-specific cleanup
      ├── Anthropic-specific cleanup
      └── DeepMind-specific cleanup
      │
      ▼
Extracted Article Text
      │
      ▼
ArticleCleaner
      │
      ▼
Clean Article Evidence
      │
      ▼
IntelligenceService
      │
      ▼
LLM
      │
      ▼
Structured Article Intelligence

The evidence pipeline has been validated against live articles from OpenAI, Anthropic, and Google DeepMind.

This ensures that future AI-generated intelligence is grounded in the actual source article rather than inferred only from metadata.

#### Structured AI Intelligence ⏳

The next step is to build the `IntelligenceService`, which will use cleaned article evidence to generate structured, evidence-grounded intelligence.

Target output:

```json
{
  "summary": "Concise evidence-grounded summary of the article.",
  "key_points": [
    "Important finding or announcement",
    "Important technical or research detail",
    "Important implication"
  ],
  "why_it_matters": "Explanation of why the development matters for AI research, industry, or practitioners."
  }

## Planned work:

- [ ] Design `IntelligenceService`
- [ ] Select and integrate an LLM
- [ ] Design evidence-grounded prompts
- [ ] Generate article summaries
- [ ] Extract key research points
- [ ] Generate `why_it_matters`
- [ ] Enforce structured output
- [ ] Validate generated intelligence against source evidence
- [ ] Handle LLM failures and malformed responses
---

## Phase 7 – Dashboard

- [ ] Streamlit dashboard
- [ ] Search and filter research updates
- [ ] Analytics dashboard
- [ ] AI research intelligence view
- [ ] API-powered frontend integration

---

# 🔮 Future Extensions

The modular architecture allows additional functionality to be introduced without redesigning the existing system.

Potential future improvements include:

- Date-based API query filtering
- Pagination for large result sets
- Additional query filters
- Pydantic response models
- Structured application logging
- API authentication
- Background refresh jobs
- Scheduled research collection
- Async source collection
- Improved text normalization
- Database migration support
- Production deployment
- Containerized API deployment
- Extended automated testing

Potential future research sources include:

- Microsoft Research
- Hugging Face
- Meta AI
- Additional AI laboratories
- AI research publications
- Academic AI research feeds

---

# 🧠 Engineering Concepts Practiced

This project demonstrates practical understanding of:

- Object-oriented programming
- Modular software architecture
- Separation of concerns
- Repository/storage pattern
- SQLite CRUD operations
- SQL filtering
- HTTP client/server communication
- REST API design
- HTTP methods
- Path and query parameters
- JSON serialization
- FastAPI
- Uvicorn
- ASGI
- OpenAPI
- Swagger UI
- Input validation
- HTTP status codes
- Exception handling
- Multi-source web scraping
- Duplicate detection
- End-to-end integration testing
- Git-based incremental development

---

# 👩‍💻 Author

**Zunaira**

Developed as an AI engineering project focused on building a modular, scalable AI Research Intelligence Agent while applying professional software engineering, backend development, API design, and AI engineering practices.

