from db import get_connection

'''try: 
    connection=get_connection
    with connection.cursor() as cursor:
        cursor.excute('call consulta_alumnos()')
        resultset=cursor.fetchall()
        for row in resultset:
            print(row)
except Exception as ex:
    print(ex)'''
    
try: 
    connection=get_connection
    with connection.cursor() as cursor:
        cursor.excute('call agregar_alumno(%s,%s,%s)',('Luis','Lopez','lopez@gmail.com'))
        connection.commit()
        connection.close()
        
except Exception as ex:
    print(ex)