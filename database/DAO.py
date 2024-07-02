from database.DB_connect import DBConnect
from model.match import Match


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNodes(mese):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * 
from matches m 
where month (`Date`) = %s"""
        cursor.execute(query, (mese, ))
        for row in cursor:
            result.append(Match(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def nome2(mese, tempo):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select t1.m1 as m1, t2.m2 as m2, count(distinct t1.p1) as peso
from (select a.PlayerID as p1, m.MatchID as m1 
from matches m, actions a 
where month (`Date`) = %s
and a.TimePlayed > %s
and a.MatchId = m.MatchID) as t1, 
(select a.PlayerID as p2, m.MatchID as m2
from matches m, actions a 
where month (`Date`) = %s
and a.TimePlayed > %s
and a.MatchId = m.MatchID) as t2
where t1.m1 != t2.m2 and t1.p1 = t2.p2 and t1.m1 < t2.m2
group by t1.m1, t2.m2"""
        cursor.execute(query, (mese, tempo, mese, tempo))
        for row in cursor:
            result.append((row["m1"], row["m2"], row["peso"]))
            #Prodotto(**row)
        cursor.close()
        conn.close()
        print(result)
        return result

    @staticmethod
    def nome3():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """"""

        cursor.execute(query,)

        for row in cursor:
            result.append()

        cursor.close()
        conn.close()
        return result