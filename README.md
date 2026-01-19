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

#### FICHAS DE REGISTRO:

> Abre o arquivo, procura o nome do colaborador e renomeia o
>arquivo do colaborador com o nome do colaborador.

#### FOLHA DE PAGAMENTO, FÉRIAS E RECISSÃO:

> Ele vai ler o arquivo, vai verificar se o arquivo será folha de pagamento, listagem de férias ou listagem de recissão.
> Dependendo do que o arqivo for, ele vai nomea-lo como : Tipo/lotação-cnpj.

>####RE FGTS:
>Ele renomeia o arquivo, colocando o cnpj do cliente.

#### LISTAGEM DE CONFERÊNCIA:
> O pdf será renomeado como lotação do colaborador

#### RECIBOS DE PAGAMENTO FORTES:
>Ao executar o robô , o usuário terá duas opções para escolher sendo :
>Separar por funcionário
>Separar por lotação
>Se a ecolha do usuário for igual a 1: 
>Os arquivos serão separados como : lotação-nome-cnpj, caso contrário o arquivo será nomeado por lotação, como mostrado no modelo a seguir

#### RECIBOS FOLK:
> Abre o arquivo, identifica o nome do cliente e salva o arquivo com o nome do cliente.
> 
#### RELATÓRIO DE SERVIÇOS ADMINISTRATIVOS:
> Abre os arquivos PDF, identifica a lotação no texto da página e salva
> cada página em um PDF separado com o nome da lotação.

#### RESUMO GERAL MÊS/PERÍODO: 
> Abre os arquivos PDF, extrai o nome da empresa e o CNPJ, consolida as páginas por
> empresa e gera arquivos PDF separados por empresa.

#### NFS FORTALEZA:
> Abre PDFs de notas fiscais, identifica o layout do documento, extrai razão social, CNPJ e
> número da nota e renomeia o arquivo conforme o tipo definido (Adm ou Despesa).

#### DEMONSTRATIVO DE FÉRIAS:
>Abre os arquivos PDF, identifica o nome da empresa no demonstrativo e gera
>arquivos individuais por página com o nome identificado.

#### NFS EUSÉBIO:
> Abre PDFs de notas fiscais, extrai o nome do prestador e o CNPJ,
>  aplica o prefixo definido e renomeia os arquivos.

#### CARTAS SINGULAR:
>Abre os arquivos PDF, identifica a quebra de cartas pelo conteúdo,
>extrai o nome do destinatário e salva cada carta em um PDF individual.

#### Rendimentos Protheus: RENDIMENTO 
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
