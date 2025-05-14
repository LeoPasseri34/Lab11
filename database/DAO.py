from database.DB_connect import DBConnect
from model.product import Product


class DAO():
    def __init__(self):
        pass


    @staticmethod
    def get_anno():
        conn = DBConnect.get_connection()
        cursor = conn.cursor()
        res = []
        query = """Select distinct Year(Date) From go_daily_sales"""
        cursor.execute(query,)

        for row in cursor:
            res.append(row[0])

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def get_colors():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []
        query = """select distinct gp.Product_color as colors 
                from go_products gp """
        cursor.execute(query, )

        for row in cursor:
            res.append(row['colors'])

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getAllProducts():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []
        query = """select distinct *
                    from go_products """
        cursor.execute(query,)

        for row in cursor:
            res.append(Product(**row))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getEdges():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []
        query = """select distinct *
                       from go_products """
        cursor.execute(query, )

        for row in cursor:
            res.append(Product(**row))

        cursor.close()
        conn.close()
        return res
