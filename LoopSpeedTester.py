import os
from time import sleep
from datetime import datetime
from random import randint
# | xargs | sed \'s/ /\\n/g\' > ...
def fechar():
    print('Fechando Chrome')
    # os.execl('fecha_chrome.sh', ' ')
    try:
        arquivo = os.popen('ps ax | grep chrome | cut -f 1 -d " "') # > /tmp/chrome-conexao.tmp') #&& TESTE=\"`cat /tmp/chrome-conexao.tmp`\" && kill -9 $TESTE')
        #arquivo = open('/tmp/chrome-conexao.tmp', 'r')
    except OSError as e:
        print('Erro lib OS 1: '+str(e))
    except Exception as e:
        print('Erro fechar 1: '+str(e))

    else:
        print('Tudo deu certo por enquanto #001/003')
        for linha in arquivo:
            if linha.strip().isnumeric():
                linha = linha.strip()
                print('matando processo #001: '+ linha)
                try:
                    os.system('kill -9 '+linha)
                except OSError as e:
                     print('Erro lib OS #001: '+str(e))
                except Exception as e:
                    print('Erro kill #001: '+str(e))
    finally:
        #arquivo.close()
        try:
            arquivo = os.popen('ps ax | grep chrome | cut -f 2 -d " "')
 
        except OSError as e:
            print('Erro lib OS 2: '+str(e))
        except Exception as e:
            print('Erro fechar 2: '+str(e))
        else:
            print('Tudo certo por enquanto #002/003')
            for linha in arquivo:
                if linha.strip().isnumeric():
                    linha = linha.strip()    
                    print('matando processo #002: '+ linha)
                    try:
                        os.system('kill -9 '+linha)
                    except OSError as e:
                         print('Erro lib OS #002: '+str(e))
                    except Exception as e:
                        print('Erro kill #002: '+str(e))
                    else:
                        print('Tudo certo por enquanto #003/003')
        finally:
            try:
                arquivo = os.popen('ps ax | grep chrome | cut -f 3 -d " "') 

            except OSError as e:
                print('Erro lib OS 1: '+str(e))
            except Exception as e:
                print('Erro fechar 1: '+str(e))

            else:
                print('Tudo deu certo por enquanto #001/003')
                for linha in arquivo:
                    if linha.strip().isnumeric():
                        linha = linha.strip()
                        print('matando processo #001: '+ linha)
                        try:
                            os.system('kill -9 '+linha)
                        except OSError as e:
                            print('Erro lib OS #001: '+str(e))
                        except Exception as e:
                            print('Erro kill #001: '+str(e))

                try:
                    validar = os.popen('ps ax | grep chrome | cut -f 1 -d " "')
                    counter = 0
                    print('VALIDANDO')
                    for linha in validar:
                        if linha.strip().isnumeric():
                            if counter >= 2:
                                return fechar() 
                        counter+=1
                    validar = os.popen('ps ax | grep chrome | cut -f 2 -d " "')
                    counter = 0
                    for linha in validar:
                        if linha.strip().isnumeric():
                            if counter >= 2:
                                return fechar()
                        counter+=1
                    validar = os.popen('ps ax | grep chrome | cut -f 3 -d " "')
                    counter = 0
                    for linha in validar:
                        if linha.strip().isnumeric():
                            if counter >= 2:
                                return fechar()
                        counter+=1


                except Exception as e:
                    print('Erro validar: '+str(e))
                else:
                    print('Resultado GREP 1:\n\n')
                    os.system('ps ax | grep chrome | cut -f 1 -d " "')
                    print('Resultado GREP 2:\n\n')
                    os.system('ps ax | grep chrome | cut -f 2 -d " "')
                    print('Resultado GREP 3:\n\n')
                    os.system('ps ax | grep chrome | cut -f 3 -d " "')


def abrir():
    print('Abrindo Chrome')
    # os.execl('abre_chrome.sh', ' ')
    try:
        os.system('google-chrome --incognito --app=https://www.minhaconexao.com.br &')
    except OSError as e:
        print('Erro lib OS: '+str(e))
    except Exception as e:
        print('Erro abrir: '+str(e))


def arquivar():
    try:
        arquivo = open('/var/log/app-script-log/arquivo.log', 'a')
        arquivo.write('Novo teste as '+str(datetime.now())+'\n')
    except Exception as e:
        print('Erro arquivar: '+str(e))
    else:
        print('ARQUIVADO')
    finally:
        arquivo.close()


while True:
    print('Checkpoint 0 em '+str(datetime.now()))
    abrir()
    print('Checkpoint 1 em '+str(datetime.now()))
    tempo = randint(1, 30)
    sleep(130 + tempo)
    print('Checkpoint 2 em '+str(datetime.now()))
    fechar()
    print('Checkpoint 3 em '+str(datetime.now()))
    arquivar()	

    

