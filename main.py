from conta import Conta

def main():
    # Para conseguir utilizar os valores e os
    # métodos da conta, primeiramente é 
    # necessário instância-la
    nova_conta = Conta()
    print('Uma nova conta foi criada')
    print(nova_conta.saldo)

    nova_conta.depositar(500)
    nova_conta.depositar(2000)   
    print(nova_conta.saldo)


main()