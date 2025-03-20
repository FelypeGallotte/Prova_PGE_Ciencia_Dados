from conexao import criar_conexao, fechar_conexao

def consultar_cliente(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM cliente")  
    resultado = cursor.fetchall()  
    print("Clientes: ")
    for row in resultado:
        print(row)      
    cursor.close()

def consultar_procurador(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM procurador")  
    resultado = cursor.fetchall()  
    print("\nProcuradores: ")
    for row in resultado:
        print(row)      
    cursor.close()  

def consultar_processo(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM processo")  
    resultado = cursor.fetchall()  
    print("\nProcessos: ")
    for row in resultado:
        print(row)      
    cursor.close()  

def consultar_prazo(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM prazo")  
    resultado = cursor.fetchall()  
    print("\nPrazos: ")
    for row in resultado:
        print(row)      
    cursor.close()  

def consultar_documentos(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM documentos")  
    resultado = cursor.fetchall()  
    print("\nDocumentos: ")
    for row in resultado:
        print(row)      
    cursor.close()  

def consultar_processo_procurador(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM processo_procurador")  
    resultado = cursor.fetchall()  
    print("\nProcessos e Procuradores: ")
    for row in resultado:
        print(row)      
    cursor.close()  


def main():
    con = criar_conexao("localhost", "root", "", "db_juridico")
    consultar_cliente(con)
    consultar_procurador(con)
    consultar_processo(con)
    consultar_prazo(con)
    consultar_documentos(con)
    consultar_processo_procurador(con)
    fechar_conexao(con)

if __name__ == "__main__":
    main()