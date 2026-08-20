from typing import Annotated

from fastapi import FastAPI, Query, HTTPException

from src.storage.storage import Storage
from src.orchestrator import Orchestrator


app = FastAPI()
storage = Storage()
orchestrator = Orchestrator()


@app.get("/")
def app_working():
    return {"message": "AI Research Intelligence Agent API is running"}


@app.get("/updates")
def get_updates(source:Annotated[str | None,Query(min_length=1)] =None, 
                category:Annotated[str | None,Query(min_length=1)]=None
):
   if source is not None:
        source = source.strip()
        if source == "":
         raise HTTPException(
         status_code=400,
         detail="Source can not be blank."
        )  
           
   if category is not None:
        category = category.strip()
        if category == "":
         raise HTTPException(
         status_code=400,
         detail="Category can't be blank."
        )
   if source is not None  and category is not None:

      return storage.get_update_by_source_and_category(source, category)
   if source is None and category is not None:
      return storage.get_updates_by_category(category)

   if source is not None and category is None:
      return storage.get_updates_by_source(source)

   return storage.get_all_updates()

@app.post("/refresh")
def refresh_updates():
   try:
    saved_updates = orchestrator.run()

    return {
        "message":"Refresh Completed",
         "saved_updates": saved_updates
         }
   

   except Exception as e:

    print(e)

    raise 
  

      

     

