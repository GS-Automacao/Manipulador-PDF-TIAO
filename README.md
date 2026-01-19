# **MANIPULADOR DE PDF**


### DESCRIÇÃO GERAL
> Em resumo o manipulador de pdfs, é responsável, por renomeia pdfs , vários tipos de arquivo, (arquivos mapeados) obj principal: 
> renomear nota fiscal e boleto. de preifeturas como Fortalez eusebio vitória , etc.

### FUNÇÕES

#### DOCUMENTOS DE ADIMISSÃO:
> Abre o arquivo, procura o nome do colaborador e renomeia o 
> arquivo do colaborador com o nome do colaborador 


#### DOCUMENTOS DE RECISSÃO:
> Abre o arquivo, procura o nome do colaborador e renomeia o arquivo
> do colaborador com o nome do colaborador.


#### BOLETOS BMP:
> Abre o arquivo, procura o nome do cliente e renomeia o arquivo
>do cliente com o nome do cliente


#### BOLETOS DE COBRANÇA:
> Terá duas opções de boleto para o cliente escolher e definir o boleto , enumeradas sendo:
>0. Definir boleto como adm
>1. para despesa
>2. Para nenhum 
>
>Ao final da execução ele vai renomear o bleto seguindo padrão, no qual, se a pessoa escolher entre 0 e 1 , o arquivo vcem nomeado como: 
>prefixo-condomínio-cnpj.pdf , caso o usuário escolher o número 2, o arquivo vem nomeado como: condomínio-cnpj.pdf.

#### Fichas de Registro:

> Abre o arquivo, procura o nome do colaborador e renomeia o
>arquivo do colaborador com o nome do colaborador.

####FOLHA DE PAGAMENTO, FÉRIAS E RECISSÃO:

> Ele vai ler o arquivo, vai verificar se o arquivo será folha de pagamento, listagem de férias ou listagem de recissão.
> Dependendo do que o arqivo for, ele vai nomea-lo como : Tipo/lotação-cnpj.

>####RE FGTS:

>Ele renomeia o arquivo, colocando o cnpj do cliente.

8: 'Listagem de Conferência:
O pdf será renomeado como lotação do colaborador

9: 'Recibos de Pagamento Fortes':
Ao executar o robô , o usuário terá duas opções para escolher sendo :
Separar por funcionário
Separar por lotação
Se a ecolha do usuário for igual a 1: 
Os arquivos serão separados como : lotação-nome-cnpj, caso contrário o arquivo será nomeado por lotação, como mostrado no modelo a seguir
    10: 'Recibos FOLK',
    11: 'Relatório de Serviços Administrativos',
    12: 'Resumo Geral Mês/Período',
    13: 'NFs Fortaleza',
    14: 'Demonstrativo de Férias',
    15: 'NFs Eusébio',
    16: 'Cartas Singular',
    17: 'Rendimentos Protheus',
    18: 'Rendimentos Fortes',
    19: 'Planos de Saúde',
    20: 'Folha por Centro de Custo Protheus',
    21: 'Recibos de Pagamento Protheus',
    22: 'NFs Camaçari',
    23: 'NFs Lauro de Freitas',
    24: 'NFs Balneário Camburiu',
    25: 'NFs Vitória',
    26: 'Boletos Santander',
    27: 'NFs Curitiba',
    28: 'NFs São Paulo',
    29: 'Boletos Vitoria'
