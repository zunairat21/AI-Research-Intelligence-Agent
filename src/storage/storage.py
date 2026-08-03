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

    def get_updates_by_source(self, source :str):

      connection = get_connection()

      try:

        cursor = connection.cursor()

        cursor.execute(
           """
             SELECT 
                   title, 
                   source,
                   url,
                   date,
                   category,
                   summary, tags
                   FROM ai_updates WHERE source = ?

          """,

            (source,)
        )

        rows = cursor.fetchall()

        updates =[]

        for row in rows:
           
          
           update = AIUpdate(
              title=row[0],
              source= row[1],
              url=row[2],
              date=row[3],
              category=row[4],
              summary=row[5],
              tags=row[6]
           )

           updates.append(update)

        return updates
        
      finally:
         connection.close()


    def get_updates_by_category(self, category:str):

      connection = get_connection()

      try:

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
                  tags FROM ai_updates WHERE category = ?
            """ ,
               (category,)

              
         )

         rows = cursor.fetchall()

         updates = []

         for row in rows:

             update = AIUpdate(
                title= row[0],
                source = row[1],
                url = row[2],
                date = row[3],
                category=row[4],
                summary = row[5],
                tags = row[6]
             )

             updates.append(update)

         return updates

      finally :

         connection.close()

    def get_updates_by_date(self, date:str):

     connection = get_connection()

     try:

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
                    tags FROM ai_updates WHERE date = ?
          """,
             (date,)
        )

        rows = cursor.fetchall()

        updates = []

        for row in rows:

           update = AIUpdate(
              title=row[0],
              source=row[1],
              url=row[2],
              date = row[3],
              category=row[4],
              summary=row[5],
              tags=row[6]
           )

           updates.append(update)

        return updates

     finally:

      connection.close()


    def delete_update_by_url(self, url:str):

      connection = get_connection()

      try:

        cursor = connection.cursor()

        cursor.execute(
           """
              DELETE
                      FROM ai_updates  WHERE url = ?
           """ ,

            (url,)


      )

        connection.commit()


        if cursor.rowcount == 1:
           return True

        else:
           return False
        
      finally:

           connection.close()

           

    def update_aiupdate(self, update:AIUpdate):
    
         connection = get_connection()
    
         try:
    
             cursor = connection.cursor()
    
             cursor.execute(
                """
                   UPDATE  ai_updates
                    
                   SET 
                      
                       title =?,
                       source=?,
                       date=?,
                       category=?,
                       summary=?,
                       tags=?
                       
                       WHERE url=?
    
                   
    
                """ ,
                 
    
                     (update.title,
                      update.source,
                      update.date,
                      update.category,
                      update.summary,
                      update.tags,
                      update.url
                     )
    
                
                )
    
             connection.commit()

             if cursor.rowcount == 1:
                return True 
             else:
                return False 


         finally:

                connection.close()


            

            

         

         

         


       






      


