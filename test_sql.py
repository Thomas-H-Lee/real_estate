import sqlite3


%sql select "Id", "Name_of_Dog",\
    from dogs \
        where "Name_of_Dog"='Huggy'
        
