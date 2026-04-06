from mysql import connector

class ListCreateUpdateRetrieveDelete:
    def __init__(self):
        try:
            self.connection=connector.connect(
            host="localhost",
            user="root",
            password="Athira@123",
            database="Book_db"
           
        )
            self.cursor=self.connection.cursor()
            print("database connected successfully")

        except Exception  as e:
            print(e)
    def list(self):
        query= "select * from book"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("no records found")


    def create(self,title=None,author=None,price=None,publisher=None,genere=None, year=None):
        query="""
                insert into book(title,author,price,publisher,genere,year)values(%s,%s,%s,%s,%s,%s)
        """
        data=(title,author,price,publisher,genere,year)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("records inserted")

    def retrieve(self,id=None):
        query=" select * from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        record= self.cursor.fetchone()
        print(record)

    def delete(self,id=None):
        query="delete from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("record deleted")

    def update(self,id=None,**kwargs):
        place_holder=""
        for k in kwargs.keys():
            place_holder += f"{k}=%s ,"
            print(place_holder)
        place_holder=place_holder.rstrip(",")
        print(place_holder)
        query=f"update book set { place_holder } where id={id}"
        data=[v for v in kwargs.values()]
        self.cursor.execute(query,data)
        self.connection.commit()
        print("record updated")
            



    

        
book_instance=ListCreateUpdateRetrieveDelete()
book_instance.update(id=1,title="paathummede aadu",price=300)
# book_instance.delete(id=1)
# book_instance.retrieve(id=1)
# book_instance.create(title="Wings of fire",author="MT Vasudevan nair",price=200, publisher="GHT", genere="fiction",year=2010)
# book_instance.create(title="Ram C/O Ananthi",author="Akhil p Dharmarajan ",price=200, publisher="GHT", genere="fiction",year=2023)
book_instance.list()







        