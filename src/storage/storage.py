from src.storage.database import get_connection
from src.ingestion.validator import AIUpdate


class Storage :


    def save_update (self,update:AIUpdate) :

      connection = get_connection()
        

      try: 

        cursor = connection.cursor()

        cursor.execute(
           
        """
        INSERT INTO ai_updates(
           title, 
           source,
            url, 
            date, 
            category,
            summary, 
            tags)

        VALUES (?,?,?,?,?,?,?)
        """,

            (
               update.title,
               update.source,
               update.url,
               update.date,
               update.category,
               update.summary,
               update.tags
            )
                   
           

        )

        connection.commit()


      finally:

           connection.close()



    def get_all_updates(self):

        connection = get_connection()
    
    
        try :
    
            
            cursor = connection.cursor()
    
            cursor.execute(
              """
                SELECT title,
                       source,
                       url,
                       date,
                       category,
                       summary,
                       tags  FROM ai_updates
                
              """
            )
    
            rows = cursor.fetchall()
    
            updates = []
    
            for row in rows:
    
               ai_update = AIUpdate(
                   title=row[0],
                   source=row[1],
                   url = row[2],
                   date=row[3],
                   category=row[4],
                   summary=row[5],
                   tags=row[6]

               )

               updates.append(ai_update)

        finally:

               connection.close()   
           
        return updates

    def get_update_by_url(self, url:str):

      connection = get_connection()

      try :

        cursor = connection.cursor()

        cursor.execute(
            """
              SELECT 
                title,
                source,
                url,
                date,
                category,
                summary,
                tags FROM ai_updates WHERE url = ?
              
            """ ,
            (url,)
             
        )

        row = cursor.fetchone()

        if row is None:
            return None
        else:
            update = AIUpdate(
                title=row[0],
                source=row[1],
                url= row[2],
                date = row[3],
                category=row[4],
                summary=row[5],
                tags=row[6]
            )

            return update

      finally:
          connection.close()

        
            
