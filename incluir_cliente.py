import mysql.connector
from PyQt5.QtWidgets import *#QApplication, QLabel,QMainWindow,QPushButton,QToolTip,QLineEdit,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from getpass import getpass
import sys

def seq_cod():
    banco = mysql.connector.connect(
        host="localhost",
        port="4407",
        user="root",
        passwd="new_sql",
        database="sis_raul",
    )
    cursor = banco.cursor()

    select = "select cliente from sequencial"
    cursor.execute(select)
    valores_lidos = cursor.fetchall()
    convert = str(valores_lidos)
    x = (convert.replace('[', ''))
    x = (x.replace(']', ''))
    x = (x.replace('(', ''))
    x = (x.replace(')', ''))
    x = (x.replace(',', ''))
    seq_cod.antigo = x
    invertida = ' '.join(palavra[::-1] for palavra in x.split())
    x = invertida.ljust(6, "0")
    invertida2 = ' '.join(palavra[::-1] for palavra in x.split())
    seq_cod.z = int(invertida2) +1
    seq_cod.zt = str(seq_cod.z)
    invertida = ' '.join(palavra[::-1] for palavra in seq_cod.zt.split())
    x = invertida.ljust(6, "0")
    invertida2 = ' '.join(palavra[::-1] for palavra in x.split())
    seq_cod.zt2 = str(invertida2)

def seq_cod_serv():
    banco = mysql.connector.connect(
        host="localhost",
        port="4407",
        user="root",
        passwd="new_sql",
        database="sis_raul",
    )
    cursor = banco.cursor()

    select = "select servico from sequencial"
    cursor.execute(select)
    valores_lidos = cursor.fetchall()
    print(valores_lidos)
    convert = str(valores_lidos)
    print(valores_lidos)
    x = (convert.replace('[', ''))
    print(x)
    x = (x.replace(']', ''))
    x = (x.replace('(', ''))
    x = (x.replace(')', ''))
    x = (x.replace(',', ''))
    x = (x.replace("'", ""))
    print(x)
    print("AQUIIIIIIIIII")
    seq_cod.serv_antigo = int(x)
    invertida = ' '.join(palavra[::-1] for palavra in x.split())
    x = invertida.ljust(6, "0")
    invertida2 = ' '.join(palavra[::-1] for palavra in x.split())
    seq_cod_serv.z = int(invertida2)
    seq_cod_serv.z = seq_cod_serv.z + 1
    seq_cod_serv.zt = str(seq_cod_serv.z)
    invertida = ' '.join(palavra[::-1] for palavra in seq_cod_serv.zt.split())
    x = invertida.ljust(6, "0")
    invertida2 = ' '.join(palavra[::-1] for palavra in x.split())
    seq_cod_serv.zt2 = str(invertida2)
    #seq_cod_serv.zt2 = "nada"

def tela_incluir_cliente():
    seq_cod()
    #app = QtGui.QApplication([])
    app = QApplication(sys.argv)
    tela_incluir_cliente.win = QMainWindow()
    tela_incluir_cliente.win.setGeometry(1570, 70, 300, 500)  # onde aparecer na tela - eixo x, eixo y, largura  , altura
    tela_incluir_cliente.win.setWindowTitle("CADASTRO DE CLIENTE")

    # TEXTOS
    tela_incluir_cliente.nomedocara=QtWidgets.QLabel(tela_incluir_cliente.win)
    tela_incluir_cliente.nomedocara.setText("CADASTRO DE CLIENTE")
    tela_incluir_cliente.nomedocara.move(90,10)
    tela_incluir_cliente.nomedocara.resize(200, 10)

    tela_incluir_cliente.nomedocara=QtWidgets.QLabel(tela_incluir_cliente.win)
    tela_incluir_cliente.nomedocara.setText("CODIGO:")
    tela_incluir_cliente.nomedocara.move(30,60)

    tela_incluir_cliente.cod_cli = QtWidgets.QLabel(tela_incluir_cliente.win)
    tela_incluir_cliente.cod_cli.setText(seq_cod.zt2)
    tela_incluir_cliente.cod_cli.move(90, 60)

    tela_incluir_cliente.nomedocara = QtWidgets.QLabel(tela_incluir_cliente.win)
    tela_incluir_cliente.nomedocara.setText("DIGITE SEU NOME:")
    tela_incluir_cliente.nomedocara.move(30, 100)

    tela_incluir_cliente.nomedocara = QtWidgets.QLabel(tela_incluir_cliente.win)
    tela_incluir_cliente.nomedocara.setText("DIGITE SUA IDADE:")
    tela_incluir_cliente.nomedocara.move(30, 140)

    tela_incluir_cliente.nomedocara = QtWidgets.QLabel(tela_incluir_cliente.win)
    tela_incluir_cliente.nomedocara.setText("DIGITE SEU EMAIL:")
    tela_incluir_cliente.nomedocara.move(30, 180)

    tela_incluir_cliente.nomedocara = QtWidgets.QLabel(tela_incluir_cliente.win)
    tela_incluir_cliente.nomedocara.setText("DIGITE SEU EMAIL:")
    tela_incluir_cliente.nomedocara.move(30, 220)

    tela_incluir_cliente.nomedocara = QtWidgets.QLabel(tela_incluir_cliente.win)
    tela_incluir_cliente.nomedocara.setText("DIGITE SEU CPF:")
    tela_incluir_cliente.nomedocara.move(30, 260)

    tela_incluir_cliente.nomedocara = QtWidgets.QLabel(tela_incluir_cliente.win)
    tela_incluir_cliente.nomedocara.setText("DIGITE SEU NUMERO:")
    tela_incluir_cliente.nomedocara.move(30, 310)
    tela_incluir_cliente.nomedocara.resize(200, 10)

    tela_incluir_cliente.nomedocara = QtWidgets.QLabel(tela_incluir_cliente.win)
    tela_incluir_cliente.nomedocara.setText("DIGITE SEU NUMERO:")
    tela_incluir_cliente.nomedocara.move(30, 350)
    tela_incluir_cliente.nomedocara.resize(200, 10)

    #INPUTS
    tela_incluir_cliente.campo_NOME = QLineEdit(tela_incluir_cliente.win)
    tela_incluir_cliente.campo_NOME.move(150, 100)

    tela_incluir_cliente.campo_IDADE_old = QLineEdit(tela_incluir_cliente.win)
    tela_incluir_cliente.campo_IDADE_old.move(150, 140)

    tela_incluir_cliente.campo_EMAIL_1 = QLineEdit(tela_incluir_cliente.win)
    tela_incluir_cliente.campo_EMAIL_1.move(150, 180)

    tela_incluir_cliente.campo_EMAIL_2 = QLineEdit(tela_incluir_cliente.win)
    tela_incluir_cliente.campo_EMAIL_2.move(150, 220)

    tela_incluir_cliente.campo_CPF = QLineEdit(tela_incluir_cliente.win)
    tela_incluir_cliente.campo_CPF.move(150, 260)

    tela_incluir_cliente.campo_NUMERO_1 = QLineEdit(tela_incluir_cliente.win)
    tela_incluir_cliente.campo_NUMERO_1.move(150, 300)

    tela_incluir_cliente.campo_NUMERO_2 = QLineEdit(tela_incluir_cliente.win)
    tela_incluir_cliente.campo_NUMERO_2.move(150, 340)

    #BOTOES
    INCLUIR = QPushButton('INCLUIR', tela_incluir_cliente.win)
    INCLUIR.move(100, 400)
    INCLUIR.resize(100, 50)  # largura x altura
    INCLUIR.clicked.connect(inserir_no_banco)

    ### TELA INICIAL
    tela_incluir_cliente.win0 = QMainWindow()
    tela_incluir_cliente.win0.setGeometry(700, 300, 500,200)  # onde aparecer na tela - eixo x, eixo y, largura  , altura
    tela_incluir_cliente.win0.setWindowTitle("INICIAR")

    # BOTOES
    INCLUIR = QPushButton('INICIAR', tela_incluir_cliente.win0)
    INCLUIR.move(200, 30)
    INCLUIR.resize(100, 50)  # largura x altura
    INCLUIR.clicked.connect(iniciar2)

    INCLUIR = QPushButton('FECHAR TUDO', tela_incluir_cliente.win0)
    INCLUIR.move(200, 90)
    INCLUIR.resize(100, 50)  # largura x altura
    INCLUIR.clicked.connect(fecha_tudo)

    # ### SELECT CLIENTES
    # banco = mysql.connector.connect(
    #     host="localhost",
    #     port="4407",
    #     user="root",
    #     passwd="new_sql",
    #     database="sis_raul",
    # )
    # cursor = banco.cursor()
    # select_cliente = "select codigo from clientes "
    # cursor.execute(select_cliente)
    #
    # select_clientes_pronto = cursor.fetchall()
    # print(select_clientes_pronto)
    # converter = str(select_clientes_pronto)
    # print(converter)
    # x = (converter.replace('(', '"'))
    # x = (x.replace(')', '"'))
    # #x = (x.replace(', ', ''))
    # #x = (x.replace(',', ''))
    # x = (x.replace('[', ''))
    # x = (x.replace(']', ''))
    # x = (x.replace(' ', ''))
    # #x = ["1","2","3"]
    # print(x)
    # x = [eval(x)]
    # #x = [x]
    # print(x)
    # x = str(x)
    # print(x)
    # #x = (x.replace(',', ''))
    # x = (x.replace('(', ''))
    # x = (x.replace(')', ''))
    # tela_incluir_cliente.x = eval(x)
    # print(x)
    # print("bathe")
    #
    # ### SELECT CODIGO CLIENTE
    # select_cliente = "select nome from clientes "
    # cursor.execute(select_cliente)
    #
    # select_clientes_pronto = cursor.fetchall()
    # print(select_clientes_pronto)
    # converter_cli = str(select_clientes_pronto)
    # print(converter_cli)
    # c = (converter_cli.replace(', ', ''))
    # c = (c.replace('(', ''))
    # c = (c.replace(')', ''))
    # c = (c.replace(', ', ''))
    # # x = (x.replace(',', ''))
    # c = (c.replace('[', ''))
    # c = (c.replace(']', ''))
    # c = (c.replace(' ', ''))
    # # x = ["1","2","3"]
    # print(c)
    # c = [eval(c)]
    # # x = [x]
    # print(c)
    # c = str(c)
    # print(c)
    # # x = (x.replace(',', ''))
    # c = (c.replace('(', ''))
    # c = (c.replace(')', ''))
    # tela_incluir_cliente.c = eval(c)
    # print(c)
    # print(type(c))
    # print(type(x))
    # print(c[0])
    # print("bathe 2")
    #
    # #x = ['000123','000321','000567','123456']
    # banco.commit()
    atualizar_lista()

    tela_incluir_cliente.win3 = QMainWindow()
    tela_incluir_cliente.win3.setGeometry(50, 70, 500,900)  # onde aparecer na tela - eixo x, eixo y, largura  , altura
    tela_incluir_cliente.win3.setWindowTitle("CLIENTES CADASTRADOS")

    ### TEXTO
    tela_incluir_cliente.nomedocara = QtWidgets.QLabel(tela_incluir_cliente.win3)
    tela_incluir_cliente.nomedocara.setText("CODIGO:")
    tela_incluir_cliente.nomedocara.move(13, 20)

    tela_incluir_cliente.nomedocara = QtWidgets.QLabel(tela_incluir_cliente.win3)
    tela_incluir_cliente.nomedocara.setText("DESCRICAO:")
    tela_incluir_cliente.nomedocara.move(70, 20)

    ### LISTA
    tela_incluir_cliente.lista = QListWidget(tela_incluir_cliente.win3)
    tela_incluir_cliente.lista.setGeometry(10, 50, 50, 480)

    tela_incluir_cliente.lista_cli = QListWidget(tela_incluir_cliente.win3)
    tela_incluir_cliente.lista_cli.setGeometry(60, 50, 200, 480)

    #multi = 0
    #tela_incluir_cliente.incrementar_codigo_na_lista = True
    atualizar_lista()
    # while tela_incluir_cliente.incrementar_codigo_na_lista is True:
    #     try:
    #         tela_incluir_cliente.lista.addItem(x[multi])
    #         tela_incluir_cliente.lista_cli.addItem(c[multi])
    #         multi = multi + 1
    #     except:tela_incluir_cliente.incrementar_codigo_na_lista = False


    #tela_incluir_cliente.lista_cli.addItem(x[multi])
    #tela_incluir_cliente.lista_cli.addItem(c[0])

    ### TELA SERVICO
    seq_cod_serv()
    tela_incluir_cliente.win2 = QMainWindow()
    tela_incluir_cliente.win2.setGeometry(1000, 70, 500,500)  # onde aparecer na tela - eixo x, eixo y, largura  , altura
    tela_incluir_cliente.win2.setWindowTitle("CADASTRO DE SERVICO")

    # TEXTOS
    tela_incluir_cliente.nomedocara = QtWidgets.QLabel(tela_incluir_cliente.win2)
    tela_incluir_cliente.nomedocara.setText("CADASTRO DE SERVICO")
    tela_incluir_cliente.nomedocara.move(100, 10)
    tela_incluir_cliente.nomedocara.resize(200, 10)

    tela_incluir_cliente.nomedocara = QtWidgets.QLabel(tela_incluir_cliente.win2)
    tela_incluir_cliente.nomedocara.setText("CODIGO: ")
    tela_incluir_cliente.nomedocara.move(100, 30)
    tela_incluir_cliente.nomedocara.resize(200, 10)

    tela_incluir_cliente.seq_ser = QtWidgets.QLabel(tela_incluir_cliente.win2)
    tela_incluir_cliente.seq_ser.setText(seq_cod_serv.zt2)
    tela_incluir_cliente.seq_ser.move(150, 30)
    tela_incluir_cliente.seq_ser.resize(200, 10)

    tela_incluir_cliente.nomedocara = QtWidgets.QLabel(tela_incluir_cliente.win2)
    tela_incluir_cliente.nomedocara.setText("CLIENTE (COD): ")
    tela_incluir_cliente.nomedocara.move(100, 60)
    tela_incluir_cliente.nomedocara.resize(200, 10)

    tela_incluir_cliente.nomedocara = QtWidgets.QLabel(tela_incluir_cliente.win2)
    tela_incluir_cliente.nomedocara.setText("NOME DO SERVICO: ")
    tela_incluir_cliente.nomedocara.move(100, 100)
    tela_incluir_cliente.nomedocara.resize(200, 10)

    tela_incluir_cliente.nomedocara = QtWidgets.QLabel(tela_incluir_cliente.win2)
    tela_incluir_cliente.nomedocara.setText("VALOR DO SERVICO: ")
    tela_incluir_cliente.nomedocara.move(100, 150)
    tela_incluir_cliente.nomedocara.resize(200, 10)

    tela_incluir_cliente.nomedocara = QtWidgets.QLabel(tela_incluir_cliente.win2)
    tela_incluir_cliente.nomedocara.setText("PAGAMENTO: ")
    tela_incluir_cliente.nomedocara.move(100, 200)
    tela_incluir_cliente.nomedocara.resize(200, 10)

    tela_incluir_cliente.nomedocara = QtWidgets.QLabel(tela_incluir_cliente.win2)
    tela_incluir_cliente.nomedocara.setText("DESCRICAO: ")
    tela_incluir_cliente.nomedocara.move(100, 260)
    tela_incluir_cliente.nomedocara.resize(200, 10)

    # INPUTS
    tela_incluir_cliente.campo_SERVICO_COD_CLI = QLineEdit(tela_incluir_cliente.win2)
    tela_incluir_cliente.campo_SERVICO_COD_CLI.move(210, 50)
    tela_incluir_cliente.campo_SERVICO_COD_CLI.resize(50, 30)

    tela_incluir_cliente.campo_SERVICO_NOME = QLineEdit(tela_incluir_cliente.win2)
    tela_incluir_cliente.campo_SERVICO_NOME.move(210, 90)
    tela_incluir_cliente.campo_SERVICO_NOME.resize(190,30)

    tela_incluir_cliente.campo_SERVICO_VALOR = QLineEdit(tela_incluir_cliente.win2)
    tela_incluir_cliente.campo_SERVICO_VALOR.move(210, 140)
    tela_incluir_cliente.campo_SERVICO_VALOR.resize(50, 30)

    tela_incluir_cliente.campo_SERVICO_PAGAMENTO = QLineEdit(tela_incluir_cliente.win2)
    tela_incluir_cliente.campo_SERVICO_PAGAMENTO.move(210, 190)
    tela_incluir_cliente.campo_SERVICO_PAGAMENTO.resize(190, 30)

    tela_incluir_cliente.campo_SERVICO_DESCRICAO = QLineEdit(tela_incluir_cliente.win2)
    tela_incluir_cliente.campo_SERVICO_DESCRICAO.move(100, 280)
    tela_incluir_cliente.campo_SERVICO_DESCRICAO.resize(300, 100)

    # BOTOES
    INCLUIR = QPushButton('INCLUIR', tela_incluir_cliente.win2)
    INCLUIR.move(100, 400)
    INCLUIR.resize(100, 50)  # largura x altura
    INCLUIR.clicked.connect(inserir_no_banco_serv)

    tela_incluir_cliente.win0.show()
    sys.exit(app.exec())

def inserir_no_banco():
    try:
        idade_novo = int(tela_incluir_cliente.campo_IDADE_old.text())
        #print(idade_novo)
        if tela_incluir_cliente.campo_NOME.text() == "" or tela_incluir_cliente.campo_IDADE_old.text() == "" or tela_incluir_cliente.campo_EMAIL_1.text() == "" or tela_incluir_cliente.campo_EMAIL_2.text() == "" or tela_incluir_cliente.campo_CPF.text() == "" or tela_incluir_cliente.campo_NUMERO_1.text() == "" or tela_incluir_cliente.campo_NUMERO_2.text() == "":
            erro()
        else:
            try:
                seq_cod()
                banco = mysql.connector.connect(
                    host="localhost",
                    port="4407",
                    user="root",
                    passwd="new_sql",
                    database="sis_raul",
                )
                cursor = banco.cursor()
                perg_codigo = seq_cod.z
                print(seq_cod.z)
                perg_nome_old = tela_incluir_cliente.campo_NOME.text()
                perg_nome = perg_nome_old.upper()
                perg_idade = idade_novo
                perg_email_1 = tela_incluir_cliente.campo_EMAIL_1.text()
                perg_email_2 = tela_incluir_cliente.campo_EMAIL_2.text()
                perg_CPF = tela_incluir_cliente.campo_CPF.text()
                perg_numero_1 = tela_incluir_cliente.campo_NUMERO_1.text()
                perg_numero_2 = tela_incluir_cliente.campo_NUMERO_2.text()
                inserir = "INSERT INTO clientes (CODIGO,NOME,IDADE,EMAIL_1,EMAIL_2,CPF,NUMERO_1,NUMERO_2) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                dados = (perg_codigo, perg_nome, perg_idade, perg_email_1, perg_email_2, perg_CPF, perg_numero_1, perg_numero_2)
                cursor.execute(inserir, dados)
                banco.commit()

                aumentar_seq()
                limpar()
                seq_cod()
                atualizar_lista()
            except:erro_3()
    except:erro_2()

def inserir_no_banco_serv():
    try:
        if tela_incluir_cliente.campo_SERVICO_NOME.text() == "" or tela_incluir_cliente.campo_SERVICO_DESCRICAO.text() == "" or tela_incluir_cliente.campo_SERVICO_VALOR.text() == "" or tela_incluir_cliente.campo_SERVICO_COD_CLI.text() == "" or tela_incluir_cliente.campo_SERVICO_PAGAMENTO.text() =="":
            QMessageBox.about(tela_incluir_cliente.win2, "ALERTA", "Existe algum campo em branco!!")
        else:
            try:
                seq_cod_serv()
                banco = mysql.connector.connect(
                    host="localhost",
                    port="4407",
                    user="root",
                    passwd="new_sql",
                    database="sis_raul",
                )
                cursor = banco.cursor()
                print("Batata1")
                bus_cli = "SELECT nome FROM CLIENTES where codigo=(%s)"
                print("Batata1")
                dados = (tela_incluir_cliente.campo_SERVICO_COD_CLI.text(),)
                print("Batata1")
                cursor.execute(bus_cli, dados)
                print("Batata1")
                print("Batata5")
                valores_lidos = str(cursor.fetchall())
                print(valores_lidos)
                print("****************")
                nom = (valores_lidos.replace('[', ''))
                print("****************")
                nom = (nom.replace(']', ''))
                nom = (nom.replace('(', ''))
                nom = (nom.replace(')', ''))
                nom = (nom.replace(',', ''))
                nom = (nom.replace("'", ""))
                print(nom)
                banco.commit()
                servico_codigo = seq_cod_serv.z
                print(servico_codigo)
                servico_nome = tela_incluir_cliente.campo_SERVICO_NOME.text()
                print(servico_nome)
                servico_valor = tela_incluir_cliente.campo_SERVICO_VALOR.text()
                print(servico_valor)
                servico_desc = tela_incluir_cliente.campo_SERVICO_DESCRICAO.text()
                print(servico_desc)
                servico_pag = tela_incluir_cliente.campo_SERVICO_PAGAMENTO.text()
                print(servico_pag)
                servico_cod_cli = tela_incluir_cliente.campo_SERVICO_COD_CLI.text()
                print(servico_cod_cli)
                servico_nom_cli = nom
                print(servico_nom_cli)
                servico_pago = "nao"
                inserir = "INSERT INTO servicos (CODIGO,DESCRICAO1,DESCRICAO2,VALOR,PAGAMENTO,CODIGO_CLIENTE,NOME_CLIENTE,PAGO) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                dados = (servico_codigo, servico_nome, servico_desc,servico_valor,servico_pag,servico_cod_cli,servico_nom_cli,servico_pago)
                print("Batata1")
                cursor.execute(inserir, dados)
                print("Batata22")
                banco.commit()

                aumentar_seq_serv()
                limpar_serv()
                seq_cod_serv()
            except:QMessageBox.about(tela_incluir_cliente.win2, "ALERTA", "Não foi possível inserir os dados no banco (SERVICO) !!")
    except:erro_2()

def erro():
    QMessageBox.about(tela_incluir_cliente.win, "ALERTA", "Existe algum campo em branco")

def erro_2():
    QMessageBox.about(tela_incluir_cliente.win, "ALERTA", "O campo IDADE não é um número")

def erro_3():
    QMessageBox.about(tela_incluir_cliente.win, "ALERTA", "Não foi possível inserir os dados no banco!!")

def aumentar_seq():
    seq_cod()
    banco = mysql.connector.connect(
        host="localhost",
        port="4407",
        user="root",
        passwd="new_sql",
        database="sis_raul",
    )
    cursor = banco.cursor()
    inserir = ("update sequencial set cliente=(%s) where cliente=(%s)")
    dados = (seq_cod.z, seq_cod.antigo)
    cursor.execute(inserir, dados)
    banco.commit()
    seq_cod()
    tela_incluir_cliente.cod_cli.setText(seq_cod.zt2)

def aumentar_seq_serv():
    seq_cod_serv()
    banco = mysql.connector.connect(
        host="localhost",
        port="4407",
        user="root",
        passwd="new_sql",
        database="sis_raul",
    )
    cursor = banco.cursor()
    #select = ("update sequencial set servico = '1' where servico = '000000';")
    inserir = ("update sequencial set servico=(%s) where servico=(%s);")
    print(seq_cod_serv.z)
    print(seq_cod.serv_antigo)
    dados = (seq_cod_serv.z, seq_cod.serv_antigo)
    cursor.execute(inserir, dados)
    banco.commit()
    seq_cod_serv()
    tela_incluir_cliente.seq_ser.setText(seq_cod_serv.zt2)

def limpar():
    tela_incluir_cliente.campo_NOME.setText("")
    tela_incluir_cliente.campo_IDADE_old.setText("")
    tela_incluir_cliente.campo_EMAIL_1.setText("")
    tela_incluir_cliente.campo_EMAIL_2.setText("")
    tela_incluir_cliente.campo_CPF.setText("")
    tela_incluir_cliente.campo_NUMERO_1.setText("")
    tela_incluir_cliente.campo_NUMERO_2.setText("")
    tela_incluir_cliente.lista.clear()
    tela_incluir_cliente.lista_cli.clear()

def limpar_serv():
    tela_incluir_cliente.campo_SERVICO_NOME.setText("")
    tela_incluir_cliente.campo_SERVICO_DESCRICAO.setText("")
    tela_incluir_cliente.campo_SERVICO_VALOR.setText("")
    tela_incluir_cliente.campo_SERVICO_COD_CLI.setText("")
    tela_incluir_cliente.campo_SERVICO_PAGAMENTO.setText("")

def iniciar2():
    tela_incluir_cliente.win.show()
    tela_incluir_cliente.win2.show()
    tela_incluir_cliente.win3.show()

def fecha_tudo():
    tela_incluir_cliente.win0.close()
    tela_incluir_cliente.win.close()
    tela_incluir_cliente.win2.close()
    tela_incluir_cliente.win3.close()

def verificar():
    if tela_incluir_cliente.senha.text() == "SIM":
        print("aew")
    else:
        QMessageBox.about(tela_incluir_cliente.win000, "ALERTA", "Senha incorreta")

def password():
    passwordt = getpass('Password:')
    if passwordt == "sim":
        tela_incluir_cliente()
    else:
        print("INCORRETO")

def atualizar_lista():
    ### SELECT CLIENTES
    banco = mysql.connector.connect(
        host="localhost",
        port="4407",
        user="root",
        passwd="new_sql",
        database="sis_raul",
    )
    cursor = banco.cursor()
    select_cliente = "select codigo from clientes "
    cursor.execute(select_cliente)
    select_clientes_pronto = cursor.fetchall()
    banco.commit()
    print(select_clientes_pronto)
    converter = str(select_clientes_pronto)
    print(converter)
    x = (converter.replace('(', '"'))
    x = (x.replace(')', '"'))
    # x = (x.replace(', ', ''))
    # x = (x.replace(',', ''))
    x = (x.replace('[', ''))
    x = (x.replace(']', ''))
    x = (x.replace(' ', ''))
    # x = ["1","2","3"]
    print(x)
    x = [eval(x)]
    # x = [x]
    print(x)
    x = str(x)
    print(x)
    # x = (x.replace(',', ''))
    x = (x.replace('(', ''))
    x = (x.replace(')', ''))
    tela_incluir_cliente.x = eval(x)
    print(x)
    print("bathe")

    ### SELECT CODIGO CLIENTE
    select_cliente = "select nome from clientes "
    cursor.execute(select_cliente)

    select_clientes_pronto = cursor.fetchall()
    print(select_clientes_pronto)
    converter_cli = str(select_clientes_pronto)
    print(converter_cli)
    c = (converter_cli.replace(', ', ''))
    c = (c.replace('(', ''))
    c = (c.replace(')', ''))
    c = (c.replace(', ', ''))
    # x = (x.replace(',', ''))
    c = (c.replace('[', ''))
    c = (c.replace(']', ''))
    c = (c.replace(' ', ''))
    # x = ["1","2","3"]
    print(c)
    c = [eval(c)]
    # x = [x]
    print(c)
    c = str(c)
    print(c)
    # x = (x.replace(',', ''))
    c = (c.replace('(', ''))
    c = (c.replace(')', ''))
    tela_incluir_cliente.c = eval(c)
    print(c)
    print(type(c))
    print(type(x))
    print(c[0])
    print("bathe 2")

    # x = ['000123','000321','000567','123456']
    banco.commit()

    multi = 0
    tela_incluir_cliente.incrementar_codigo_na_lista = True
    while tela_incluir_cliente.incrementar_codigo_na_lista is True:
        try:
            tela_incluir_cliente.lista.addItem(tela_incluir_cliente.x[multi])
            tela_incluir_cliente.lista_cli.addItem(tela_incluir_cliente.c[multi])
            multi = multi + 1
        except:tela_incluir_cliente.incrementar_codigo_na_lista = False

#password()
tela_incluir_cliente()
#aumentar_seq()