import os #Biblioteca necessaria para limpar o terminal, permite interagir com o sistema operacional

SenhaAdmin = "9090"

BaseSocios = [
    {
        "email": "joao1981@outlook.com",
        "senha": "158965",
        "nome": "João Kleber",
        "renda" : 5300.00,
        "plano": "Ouro",
        "ativo": False
    },
    {
        "email": "junin12@",
        "senha": "booyah2345@",
        "nome": "Junior da Silva",
        "renda" : 4200.00,
        "plano": "Prata",
        "ativo": False
    },
    {
        "email": "matheus663@hotmail.com",
        "senha": "8891520",
        "nome": "Matheus Machado",
        "renda" : 4800.00,
        "plano": "Bronze",
        "ativo": True
    },
    {
        "email": "mariazinha2003@yahoo.com",
        "senha": "7992336",
        "nome": "Maria Pereira",
        "renda" : 2300.00,
        "plano": "Social",
        "ativo": True
    },
    {
        "email": "diegosilva@gmail.com",
        "senha": "Pd35jsfe@",
        "nome": "Diego Silva",
        "renda" : 1500.00,
        "plano": "Social",
        "ativo": True
    }
]


# O "LimparTerminal()"" é util para que o proximo usuario que for usar o programa não veja as infomaçoẽs dos usuarios anteriores. Garantindo que as informações fiquem protegidas
def LimparTerminal():
    if os.name == "posix": # "posix" se refere ao linux. Caso o usuario esteja no linux (ou no mac) o "LimparTerminal()" vai rodar "clear". Caso contrario, "cls"
        os.system("clear")
    else:
        os.system("cls")


def ExibirCabecalho():
    print("\n" + "=" * 40) # Exibe "=" 40 vezes
    print("   BOTAFOGO FUTEBOL CLUBE - GESTÃO")
    print("=" * 40)


def CalcularIngresso(ValorBase, Categoria):
    Planos = {"Ouro": 1.0, "Social": 0.8, "Prata": 0.5, "Bronze": 0.2}
    TaxaDesconto = Planos.get(Categoria, 0.0)
    return ValorBase * (1 - TaxaDesconto) # Os planos retiram uma parte do preço. Exmplo: Bronze = 0.2 (20%). Então o usuario paga o resto = 0.8 (80%)   


def PainelAdmin():
    while True:
        print("\n--- PAINEL ADMINISTRATIVO (GESTOR) ---")
        print("1 - Resumo de Planos (Quantidade)")
        print("2 - Relatório de Mensalidades")
        print("0 - Sair do Painel")
        
        Opcao = input("\nSelecione: ")
        
        if Opcao == "1":
            # Conta quantos sócios existem em cada categoria
            Contagem = {"Ouro": 0, "Prata": 0, "Bronze": 0, "Social": 0}
            for S in BaseSocios:
                Contagem[S['plano']] += 1
            
            TotalSocios = len(BaseSocios) # O ".len" é pra contar quantos elementos existem dentro da lista
             
            print("\n--- Relatório de Sócios ---")
            for Plano, Quantidade in Contagem.items():
                # Calcula a porcentagem (evita erro se a base estiver vazia)
                Porcentagem = (Quantidade / TotalSocios * 100) if TotalSocios > 0 else 0 # Só calcula a porcentagem se a quantiadade de socios for maior que 0
                print(f"Plano {Plano}: {Quantidade} sócios ({Porcentagem:.2f}%)")
            
            print(f"Total Geral: {TotalSocios}")

        elif Opcao == "2":
            print("\nRELATÓRIO DE STATUS FINANCEIRO:")
            if not BaseSocios:
                print("Nenhum sócio cadastrado.")
            for S in BaseSocios:
                Status = "EM DIA" if S['ativo'] else "ATRASADA"
                # O ":<" serve para deixar as colunas alinhadas
                print(f"Nome: {S['nome']:<20} |Renda: {S['renda']:<10.2f}| Plano: {S['plano']:<10} | Status: {Status}") 
                
        elif Opcao == "0":
            break


def CriarConta():
    print("\n--- CRIAR CONTA DE SÓCIO-TORCEDOR ---")
    
    # Validação do E-mail
    while True:
        Email = input("E-mail: ").strip().lower()
        if not Email:
            print("[!] O e-mail é obrigatório.")# Caso o usuario não digite nada, ele volta e obriga o usuario a digitar
            continue
        if any(S['email'] == Email for S in BaseSocios):# Garante que não existam e-mails duplicados
            print("[!] Este e-mail já está cadastrado. Tente outro.")
            continue
        break

    # Validação da Senha
    while True:
        SenhaUser = input("Crie uma senha: ").strip()
        if not SenhaUser:
            print("[!] A senha não pode ficar em branco.")
            continue
        break

    # Validação do Nome
    while True:
        Nome = input("Nome Completo: ").strip()# Nome e senha podem se repetir a vontade
        if not Nome:
            print("[!] O nome é obrigatório.")
            continue
        break
    
    # Validação da Renda
    while True:
        try:
            InserirRenda = input("Sua renda mensal (ex: 2500.00): ").strip()
            if not InserirRenda:
                print("[!] A renda é obrigatória para definir o plano.")
                continue
            Renda = float(InserirRenda)
            break
        except ValueError:
            print("[!] Erro: Digite apenas números e use ponto para decimais.")

    LimiteSocial = 3242.00 # Limite para plano Social (2 salários mínimos)
    EntraSocial = Renda <= LimiteSocial # Caso o usuario tenha uma renda menor que dois salarios minimos, o plano "Social" fica disponivel
    
    # Validação do Plano
    while True:
        print("\nPlanos Disponíveis: ")
        
        # Se o social estiver disponível, exibe só Social e Ouro
        if EntraSocial:
            print("Social - 80% de desconto")
            print("Ouro - 100% de desconto")
            OpcoesValidas = ["Social", "Ouro"]
        else:
            # Se não tiver social, exibe os demais
            print("Ouro - 100% de desconto")
            print("Prata - 50% de desconto")
            print("Bronze - 20% de desconto")
            OpcoesValidas = ["Ouro", "Prata", "Bronze"]
            
        # O ".capitalize()" deixa a primeira letra maiuscula e o resto minuscula e o ".strip()" remove espaços 
        Plano = input("\nEscolha seu plano: ").capitalize().strip() 
        
        if not Plano:
            print("[!] Você precisa escolher um plano.")
            continue
        
        # Verifica se o plano digitado está na lista de permitidos para aquele usuário
        if Plano not in OpcoesValidas:
            if Plano == "Social" and not EntraSocial:
                print("[!] Erro: Plano Social indisponível para sua renda.")
            else:
                print("[!] Plano inválido ou não recomendado para seu perfil.")
            continue
        break

    NovoSocio = {
        "email": Email,
        "senha": SenhaUser,
        "nome": Nome,
        "plano": Plano,
        "renda" : Renda,
        "ativo": False # Contas novas iniciam inativas por padrão para o usuario ter que pagar a primeira mensalidade
    }
    
    BaseSocios.append(NovoSocio) # Adiciona as informações do "NovoSocio" dentro de "BaseSocios"
    print("-" * 32)
    print(f"\n[OK] Conta criada com sucesso, {Nome}!")
    print(f"\n[+] Não esqueça seu e-mail e senha.")
    print("\n[+] Realize o pagamento na Área do Sócio para ativar sua conta.")
    input("\nPressione Enter para prosseguir....")
    LimparTerminal()


def LoginTorcedor():
    print("\n--- LOGIN DO TORCEDOR ---")
    Email = input("E-mail: ").strip().lower() # O ".strip()" serve para remover espaços e o ".lower()" serve para deixar todos os caracteres minusculos
    Senha = input("Senha: ").strip()
    
    for Socio in BaseSocios: # Ele percorre a lista verificando um por um
        if Socio['email'] == Email and Socio['senha'] == Senha:
            return Socio
    
    print("[!] E-mail ou senha incorretos.")
    input("Pressione Enter para tentar novamente...")
    return None # Caso as informações não batam, ele retona nada


def AreaSocio(Socio):
    while True:
        print(f"\n--- ÁREA DO SÓCIO | BEM-VINDO, {Socio['nome']} ---")
        print(f"\nPLANO ATUAL: {Socio['plano']}")
        
     
        StatusFinanceiro = "EM DIA" if Socio['ativo'] else "PENDENTE (PAGAR MENSALIDADE)"
        print(f"Status: {StatusFinanceiro}")
        
        print("\n1 - Simular Compra de Ingresso")
        print("2 - Pagar Mensalidade") 
        print("0 - Sair da conta")
        
        OpcaoUsuario = input("\nOpção: ")
        
        if OpcaoUsuario == "1":
            if Socio['ativo']:
                ValorFinal = CalcularIngresso(95.00, Socio['plano'])
                print('\n' * 2)
                print("-" * 35)
                print(f"TICKET GERADO PARA: {Socio['nome'].upper()}")
                print(f"CATEGORIA: {Socio['plano']}")
                print(f"MENSALIDADE EM DIA: {Socio['ativo']}") 
                print(f"VALOR FINAL: R$ {ValorFinal:.2f}")
                print("STATUS: QR CODE DISPONÍVEL NO APP (Simulação)")
                print("-" * 35)
                print('\n')
                input("Pressione Enter para continuar.....\n")
            else:
                print("\n[!] Acesso bloqueado: Regularize sua mensalidade na opção 2.")
                input("Pressione Enter para voltar.....")
        
        elif OpcaoUsuario == "2":
            if Socio['ativo']:
                print("\n[OK] Sua mensalidade já está em dia! Não há boletos pendentes.")
            else:
                print(f"\n--- SIMULAÇÃO DE PAGAMENTO ---")
                print(f"\nPlano: {Socio['plano']}")
                Confirmar = input("Deseja confirmar o pagamento da mensalidade? (S/N): ").upper().strip()
                
                if Confirmar == "S":
                    Socio['ativo'] = True
                    print("\n[+] Pagamento realizado com sucesso! Sua conta agora está ATIVA.")
                else:
                    print("\n[!] Pagamento cancelado.")
            input("\nPressione Enter para continuar...")

        elif OpcaoUsuario == "0":
            LimparTerminal()
            break


def Menu():
    while True:
        LimparTerminal()# Limpa o terminal antes de exibir o menu
        ExibirCabecalho()
        print("1 - Criar Minha Conta de Sócio")
        print("2 - Entrar (Login)")
        print("3 - Painel de Administrador (Área restrita)")
        print("0 - Encerrar")
        
        Opcao = input("\nEscolha: ")
        
        if Opcao == "1":
            CriarConta()
        elif Opcao == "2":
            Usuario = LoginTorcedor()
            if Usuario:
                AreaSocio(Usuario)
        elif Opcao == "3":
            TentarSenha = input("Digite a senha: ")
            if TentarSenha == SenhaAdmin: #Verifica se a senha que o usuario digitou é a senha confidencial do admin
                PainelAdmin()
            else:
                print("Senha Incorreta")
                input("Pressione Enter para voltar. ")
        elif Opcao == "0":
            LimparTerminal()
            print("-" * 36)
            print("Saudações Botafoguense! Até logo.")
            break # Quebra o while
# Caso o usuario digite algo que não seja 0, 1, 2 ou 3 o programa apenas retorna ao Menu()

Menu() 

#GitHub: https://github.com/Raul-Lima322/Trabalho-Socio-Torcedor.git