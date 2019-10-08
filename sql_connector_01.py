from sqlalchemy import create_engine


def sql_connection(program):
    engine = create_engine("mssql+pyodbc://192.168.56.102:1433/CM_CN1?driver=SQL Server?trusted_connection=yes")
    conn = engine.connect()
    s = f'''
SELECT DISTINCT [CM_CN1].[dbo].[v_Add_Remove_Programs].ResourceID, User_Name0, Netbios_Name0, Operating_System_Name_and0 
FROM [CM_CN1].[dbo].[v_Add_Remove_Programs]
INNER JOIN [CM_CN1].[dbo].[v_R_System_Valid]
ON [CM_CN1].[dbo].[v_Add_Remove_Programs].ResourceID = [CM_CN1].[dbo].[v_R_System_Valid].ResourceID
WHERE [CM_CN1].[dbo].[v_Add_Remove_Programs].ResourceID NOT IN (SELECT ResourceID  FROM [CM_CN1].[dbo].[v_Add_Remove_Programs] 
WHERE DisplayName0 = '{program}')
'''
    result = conn.execute(s).fetchall()
    return result

print(sql_connection('Google Chrome'))


