import mysql.connector
schemata = str(input("NOME DO BANCO: "))
print(schemata)
rodando = True
while rodando is True:
    try:
        banco = mysql.connector.connect(
            host="localhost",
            port="4407",
            user="root",
            passwd="new_sql",
        )
        cursor = banco.cursor()

        criar_banco = str("CREATE DATABASE {}".format(schemata))
        cursor.execute(criar_banco)
        banco.commit()
    except:
        banco = mysql.connector.connect(
            host="localhost",
            port="4407",
            user="root",
            passwd="new_sql",
            database=schemata,
        )
        cursor = banco.cursor()
        usar = "use {}".format(schemata)

        cursor.execute(usar)
        banco.commit()
        cursor.execute("CREATE TABLE `clientes` (`CODIGO` INT(6) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT,`NOME` VARCHAR(255) NOT NULL,`IDADE` VARCHAR(3) NOT NULL,`EMAIL_1` VARCHAR(255) NOT NULL,`EMAIL_2` VARCHAR(255) NOT NULL,`CPF` VARCHAR(15) NOT NULL,`NUMERO_1` VARCHAR(45) NOT NULL,`NUMERO_2` VARCHAR(45) NOT NULL,PRIMARY KEY (`CODIGO`))ENGINE = InnoDB;")
        cursor.execute("CREATE TABLE `servicos` (`CODIGO` INT(6) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT,`DESCRICAO1` VARCHAR(45) NOT NULL,`DESCRICAO2` VARCHAR(255) NOT NULL,`VALOR` FLOAT(45) UNSIGNED ZEROFILL NOT NULL,`PAGAMENTO` VARCHAR(45) NOT NULL,`CODIGO_CLIENTE` VARCHAR(45) NOT NULL,`NOME_CLIENTE` VARCHAR(45) NOT NULL,`PAGO` VARCHAR(3) NOT NULL,  PRIMARY KEY (`CODIGO`)) ENGINE = InnoDB;")
        cursor.execute("CREATE TABLE `sequencial` (`CLIENTE` INT(6) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT,`SERVICO` VARCHAR(255) NOT NULL,PRIMARY KEY (`CLIENTE`))ENGINE = InnoDB;")
        banco.commit()
        print("Banco de dados criado com sucesso!!")
        break