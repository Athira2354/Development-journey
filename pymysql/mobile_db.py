from mysql import connector


class ListCreateUpdateRetrieveDelete:
    def __init__(self):
        try:
            self.connection=connector.connect(
                host="localhost",
                user="root",
                password="Athira@123",
                db="mobile_db"
            )
            self.cursor=self.connection.cursor()
            print("database connected successfully")
        except Exception  as e:
            print(e)
    def list(self):
       
        query= "select * from mobile"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            for row in records:
                print("row")
        else:
            print("no records found")

    def create(self,name=None,brand=None,specs=None,price=None):

        query="""
        insert into mobile(name,brand,specs,price)values(%s,%s,%s,%s)
        """
        data=(name ,brand ,specs,price)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("records inserted")


    




mobile_instance=ListCreateUpdateRetrieveDelete()
mobile_instance.create(name="Iphone 17 pro max",brand="Apple",specs="RAM:12 GB",price=200)
mobile_instance.list()



