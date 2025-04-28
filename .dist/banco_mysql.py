import mysql.connector

class Banco:
    def conectar(self):
        return mysql.connector.connect(
            host = "paparella.com.br",
            user = "paparell_aluno_9",
            password = "@Senai2025",
            database = "paparell_python"
        )
    
    def criar_tabela(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        query = (""" 
                 create table if not exists dispositivos(
                     id int auto_increment primary key,
                     aluno varchar(255) not null,
                     dispositivo int not null,
                     valor decimal(10,2) not null )""")
        cursor.execute(query)
        conexao.commit()
        cursor.close()
        conexao.close()
        
    def inserir_atualizar(self, aluno, dispositivo, valor):
        conexao = self.conectar()
        cursor = conexao.cursor()
        query = """ INSERT INTO dispositivos(aluno, dispositivo, valor)
        VALUES(%s,%s,%s)
        ON DUPLICATE KEY UPDATE
        dispositivo = VALUES(dispositivo),
        valor = VALUES(valor)"""
        cursor.execute(query,(aluno, dispositivo, valor))
        print((f"VALOR; {valor} inserido/atualizar com sucesso no dispositivo {dispositivo}"))
        cursor.close()
        conexao.close()
        
        def listar(self):
            conexao = self.conectar()
            cursor = conexao.cursor()
            query = "SELECT * FROM dispositivos"
            cursor.execute(query)
            disp = cursor.fetchall()
            if not disp:
                print("dispositivos nao encontrados")
            else:
                print(f"ID: {disp[0]}| Aluno: {disp[1]} | Dispositivos: {disp[2]} | Valor: {disp[3]}")
                cursor.close()
                conexao.close()