from conexao import criar_conexao, fechar_conexao

def inserir_cliente(con, nome, cpf):
    cursor = con.cursor()
    sql = "INSERT INTO Cliente (Nome, CPF) VALUES (%s, %s)"
    valores = (nome, cpf)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def inserir_procurador(con, nome_procurador, numero_oab):
    cursor = con.cursor()
    sql = "INSERT INTO Procurador (Nome_Procurador, Numero_OAB) VALUES (%s, %s)"
    valores = (nome_procurador, numero_oab)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def inserir_processo(con, numero_processo, status, orgao_responsavel, assunto, id_cliente):
    cursor = con.cursor()
    sql = """
    INSERT INTO Processo (Numero_Processo, Status, Orgao_Responsavel, Assunto, Id_Cliente)
    VALUES (%s, %s, %s, %s, %s)
    """
    valores = (numero_processo, status, orgao_responsavel, assunto, id_cliente)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def inserir_processo_procurador(con, id_processo, id_procurador, data_inicio, data_fim=None):
    cursor = con.cursor()
    if data_fim:
        sql = "INSERT INTO Processo_Procurador (Id_Processo, Id_Procurador, Data_Inicio, Data_Fim) VALUES (%s, %s, %s, %s)"
        valores = (id_processo, id_procurador, data_inicio, data_fim)
    else:
        sql = "INSERT INTO Processo_Procurador (Id_Processo, Id_Procurador, Data_Inicio) VALUES (%s, %s, %s)"
        valores = (id_processo, id_procurador, data_inicio)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def inserir_documento(con, id_processo, tipo_documento, nome_documento):
    cursor = con.cursor()
    sql = "INSERT INTO Documentos (Id_Processo, Tipo_Documento, Nome_Documento) VALUES (%s, %s, %s)"
    valores = (id_processo, tipo_documento, nome_documento)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def inserir_prazo(con, id_processo, tipo_prazo, data_vencimento, status):
    cursor = con.cursor()
    sql = "INSERT INTO Prazo (Id_Processo, Tipo_Prazo, Data_Vencimento, Status) VALUES (%s, %s, %s, %s)"
    valores = (id_processo, tipo_prazo, data_vencimento, status)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def atualizar_data_fim(con, id_processo, id_procurador, data_fim):
    cursor = con.cursor()
    sql = "UPDATE Processo_Procurador SET Data_Fim = %s WHERE Id_Processo = %s AND Id_Procurador = %s AND Data_Fim IS NULL"
    valores = (data_fim, id_processo, id_procurador)
    cursor.execute(sql, valores)
    con.commit()
    cursor.close()

def main():
    con = criar_conexao("localhost", "root", "", "db_juridico")
    
    # Inserir Clientes
    inserir_cliente(con, "Henrique Moreira", "99403143029")
    
    # Inserir Procuradores
    inserir_procurador(con, "Ana Souza", "678143-PR")
    
    # Inserir Processos
    inserir_processo(con, "1004", "Em andamento", "Tribunal Federal", "Ação Trabalhista", 4)

    #update Processo_Procurador
    atualizar_data_fim(con, 1, 2, "2025-03-09")

    # Inserir Processo_Procurador
    inserir_processo_procurador(con, 1,4, "2025-03-10", "")
    inserir_processo_procurador(con, 4, 2, "2025-03-15", "")


    # Inserir Documentos
    inserir_documento(con, 4, "Contrato", "Contrato_Aluguel.pdf")
    
    # Inserir Prazos
    inserir_prazo(con, 4, "Entrega de Documentos", "2025-04-01", "Pendente")
    
    fechar_conexao(con)

if __name__ == "__main__":
    main()
