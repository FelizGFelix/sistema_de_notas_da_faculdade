# notas do 1 semestre

import os

def clear_screen():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def valor1():
    resposta = float(input("Insira a sua nota: "))
    notas.append(resposta)
    return notas

def valor2():
    resposta = float(input("Insira o valor da nota: "))
    notas2.append(resposta)
    return notas2

def valor3():
    resposta = float(input("Insira o valor da nota: "))
    notas3.append(resposta)
    return notas3

def valor4():
    resposta = float(input("Insira o valor da nota: "))
    notas4.append(resposta)
    return notas4

def main():
    print("1 Eng de prompt de IA\n2 Eletroeletrônica\n3 Modelagem\n4 Programação\n5 acessar as notas")

def main4():
    print("1 Eng de prompt de IA\n2 Eletroeletrônica\n3 Modelagem\n4 Programação")


notas = []
notas2 = []
notas3 = []
notas4 = []

def main2():

    try:
        valor = int(input("Digite um dos valores para visitar: \n-> "))

        if valor == 1:
            valor1()
            print(notas)
            input("Digite qualquer tecla para voltar: ")
            clear_screen()
            main3()

        elif valor == 2:
            valor2()
            print(notas2)
            input("Digite qualquer tecla para voltar: ")
            clear_screen()
            main3()

        elif valor == 3:
            valor3()
            print(notas3)
            input("Digite qualquer tecla para voltar: ")
            clear_screen()
            main3()

        elif valor == 4:
            valor4()
            print(notas4)
            input("Digite qualquer tecla para voltar: ")
            clear_screen()
            main3()

        elif valor == 5:
            clear_screen()
            main4()
            resposta = int(input("Qual nota deseja acessar? "))
            if resposta == 1:
                print(notas)
                input("Digite qualquer tecla para voltar: ")
                clear_screen()
                main3()

            elif resposta == 2:
                print(notas2)
                input("Digite qualquer tecla para voltar: ")
                clear_screen()
                main3()

            elif resposta == 3:
                print(notas3)
                input("Digite qualquer tecla para voltar: ")
                clear_screen()
                main3()

            elif resposta == 4:
                print(notas4)
                input("Digite qualquer tecla para voltar: ")
                clear_screen()
                main3()
        
            elif resposta == 5:
                print("As notas já estão sendo acessadas")
                clear_screen()
                main3()

            else:
                print("Insira um valor válido")
                clear_screen()
                main3()


        else:
            print("Insira um valor válido")
            input("Digite qualquer tecla para voltar: ")
            clear_screen()
            main3()

    except:
        print("Insira um valor válido")
        input("Digite qualquer tecla para voltar: ")
        clear_screen()
        main3()

def main3():
    main()
    main2()

if __name__ == "__main__":
    main3()
