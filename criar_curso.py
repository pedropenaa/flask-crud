from base import sql

mysql = sql.SQL("root", "root", "test")

comando = "DROP TABLE IF EXISTS tb_curso;"

if mysql.executar(comando, ()):
   print ("Tabela de curso excluída com sucesso!")


comando = "CREATE TABLE tb_curso (idt_curso INT AUTO_INCREMENT PRIMARY KEY, " + \
        "sigla_curso CHAR(10) NOT NULL, " + \
        "nme_curso VARCHAR(50) NOT NULL, " + \
        "data_abertura date NOT NULL, " + \
        "numero_total_creditos int NOT NULL, " + \
        "ementa text);"

if mysql.executar(comando, ()):
   print ("Tabela de curso criada com sucesso!")

