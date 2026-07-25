from src.storage.database import get_connection

def setup_database():
    """
    Create databse schema 
    """

    connection = get_connection()

    try:
         cursor = connection.cursor()
    
         cursor.execute("""
         CREATE TABLE IF NOT EXISTS ai_updates (
                   
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        source TEXT NOT NULL,
        url TEXT NOT NULL UNIQUE,
        date TEXT NOT NULL,
        category TEXT NOT NULL,
        summary TEXT ,
        tags TEXT ,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        
                  
         )
    """)
         
         connection.commit()

    finally:
    
        connection.close()

if __name__ == "__main__":
    setup_database()
    


