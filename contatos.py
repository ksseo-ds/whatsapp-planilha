import pandas as pd

def extrair_cod(contato):
    """
    Extrai o código e o nome do contato.
    
    Parâmetros:
    contato (str): String do contato no formato 'codigo nome completo'.

    Retorna:
    tuple: (código, nome)
    """
    cod = contato[:9]  # Extrai os 9 primeiros caracteres como código

    # Verifica se o código é uma sequência de 9 dígitos
    if cod.isdigit() and len(cod) == 9:
        partes = contato.split(' ', 1)  # Divide a string em código e nome
        if len(partes) > 1:
            nome_completo = partes[1]  # Obtém o nome completo
            nome = nome_completo.split(' ', 1)[0]  # Obtém o primeiro nome
            return cod, nome

    # Se o código não for válido, tratar o código como None e o nome completo
    return None, contato

def ajustar_telefone(telefone):
    """
    Ajusta o número de telefone conforme as regras especificadas.

    Parâmetros:
    telefone (str): Número de telefone a ser ajustado.

    Retorna:
    tuple: (telefone ajustado, status)
    """
    telefone = telefone.strip()  # Remove espaços em branco ao redor

    if len(telefone) < 9:
        return None, 'Inválido'  # Menos de 9 dígitos é inválido
    elif len(telefone) == 9:
        return '+5596' + telefone, 'Válido'  # 9 dígitos, adiciona '+5596'
    elif len(telefone) == 11:
        return '+55' + telefone, 'Válido'  # 11 dígitos, adiciona '+55'
    elif len(telefone) == 12:
        return '+55' + telefone[1:], 'Válido'  # 12 dígitos, exclui o primeiro dígito e adiciona '+55'
    elif len(telefone) == 13 and telefone.startswith('55'):
        return '+' + telefone, 'Válido'  # 13 dígitos começando com '55', adiciona '+'
    else:
        return None, 'Inválido'  # Mais de 13 dígitos ou não atende aos critérios

def criar_agenda_valida(contatoscsv):
    """
    Cria um DataFrame com os contatos válidos, incluindo telefone ajustado.

    Parâmetros:
    contatoscsv (str): Caminho para o arquivo CSV com os contatos.

    Retorna:
    DataFrame: DataFrame contendo contatos válidos com as colunas 'COD', 'Nome' e 'Telefone'.
    """
    # Carregar o DataFrame a partir do arquivo CSV
    df = pd.read_csv(contatoscsv)

    # Selecionar as colunas relevantes
    colunas = ['First Name', 'Phone 1 - Value']
    df = df[colunas].copy()

    # Inicializar listas para armazenar os códigos, nomes e telefones
    codigos = []
    nomes = []
    telefones = []
    status_tel = []

    # Aplicar a função extrair_cod para preencher as listas
    for contato, telefone in zip(df['First Name'], df['Phone 1 - Value']):
        cod, nome = extrair_cod(contato)
        codigos.append(cod)
        nomes.append(nome)
        telefone_ajustado, status = ajustar_telefone(telefone)
        telefones.append(telefone_ajustado)
        status_tel.append(status)

    # Adicionar as listas como novas colunas no DataFrame
    df['COD'] = codigos
    df['Nome'] = nomes
    df['Telefone'] = telefones
    df['Status_Telefone'] = status_tel

    # Manter apenas as colunas 'COD', 'Nome' e 'Telefone' com telefone válido
    df_valido = df[(df['COD'].notna()) & (df['Status_Telefone'] == 'Válido')]
    df_valido = df_valido[['COD', 'Nome', 'Telefone']]

    return df_valido

def criar_agenda_invalida(contatoscsv):
    """
    Cria um DataFrame com os contatos inválidos.

    Parâmetros:
    contatoscsv (str): Caminho para o arquivo CSV com os contatos.

    Retorna:
    DataFrame: DataFrame contendo contatos inválidos com as colunas originais 'First Name' e 'Phone 1 - Value'.
    """
    # Carregar o DataFrame a partir do arquivo CSV
    df = pd.read_csv(contatoscsv)

    # Selecionar as colunas relevantes
    colunas = ['First Name', 'Phone 1 - Value']
    df = df[colunas].copy()

    # Inicializar listas para armazenar os códigos, nomes e telefones
    codigos = []
    nomes = []
    telefones = []
    status_tel = []

    # Aplicar a função extrair_cod para preencher as listas
    for contato, telefone in zip(df['First Name'], df['Phone 1 - Value']):
        cod, nome = extrair_cod(contato)
        codigos.append(cod)
        nomes.append(nome)
        telefone_ajustado, status = ajustar_telefone(telefone)
        telefones.append(telefone_ajustado)
        status_tel.append(status)

    # Adicionar as listas como novas colunas no DataFrame
    df['COD'] = codigos
    df['Nome'] = nomes
    df['Telefone'] = telefones
    df['Status_Telefone'] = status_tel

    # Manter apenas os contatos que não têm um código válido ou telefone inválido
    df_invalido = df[(df['COD'].isna()) | (df['Status_Telefone'] == 'Inválido')]
    df_invalido = df_invalido[['First Name', 'Phone 1 - Value']]

    return df_invalido

### daqui pra baixo são testes pra ver o output

# Substitua 'contacts.csv' pelo caminho correto para o seu arquivo CSV
#agenda_valida = criar_agenda_valida('contacts.csv')
#agenda_invalida = criar_agenda_invalida('contacts.csv')
#
# Exibir os DataFrames resultantes
#print("Agenda Válida:")
#print(agenda_valida)
#
#print("\nAgenda Inválida:")
#print(agenda_invalida)
#
# Salvar os DataFrames em arquivos CSV, se necessário
#agenda_valida.to_csv('agenda_valida.csv', index=False)
#agenda_invalida.to_csv('agenda_invalida.csv', index=False)
