# **MANIPULADOR DE PDF**


### DESCRIÇÃO GERAL
> Em resumo o manipulador de pdfs, é responsável, por renomeia pdfs , vários tipos de arquivo, (arquivos mapeados) obj principal: 
> renomear nota fiscal e boleto. de preifeturas como Fortalez eusebio vitória , etc.


### FUNÇÕES

#### DOCUMENTOS DE ADIMISSÃO:
>  Abre o arquivo, procura o nome do colaborador e renomeia o 
> arquivo do colaborador com o nome do colaborador 


#### DOCUMENTOS DE RECISSÃO:
>  Abre o arquivo, procura o nome do colaborador e renomeia o arquivo
> do colaborador com o nome do colaborador.


#### BOLETOS BMP:
>  Abre o arquivo, procura o nome do cliente e renomeia o arquivo
>do cliente com o nome do cliente


#### BOLETOS DE COBRANÇA:
>  Terá duas opções de boleto para o cliente escolher e definir o boleto , enumeradas sendo:
>0. Definir boleto como adm
>1. para despesa
>2. Para nenhum 
>
>Ao final da execução ele vai renomear o bleto seguindo padrão, no qual, se a pessoa escolher entre 0 e 1 , o arquivo vcem nomeado como: 
>prefixo-condomínio-cnpj.pdf , caso o usuário escolher o número 2, o arquivo vem nomeado como: condomínio-cnpj.pdf.

#### FICHAS DE REGISTRO:

>  Abre o arquivo, procura o nome do colaborador e renomeia o
>arquivo do colaborador com o nome do colaborador.

#### FOLHA DE PAGAMENTO, FÉRIAS E RECISSÃO:

>  Ele vai ler o arquivo, vai verificar se o arquivo será folha de pagamento, listagem de férias ou listagem de recissão.
> Dependendo do que o arqivo for, ele vai nomea-lo como : Tipo/lotação-cnpj.

>#### RE FGTS:
>  Ele renomeia o arquivo, colocando o cnpj do cliente.

#### LISTAGEM DE CONFERÊNCIA:
>  O pdf será renomeado como lotação do colaborador

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

#### RENDIMENTO PROTHEUS:
> Abre os arquivos PDF, identifica nome e CPF no texto, agrupa as páginas duas a duas e
> gera arquivos PDF separados por pessoa.

#### RENDIMENTOS FORTES:
>Abre arquivos PDF, identifica o início de um novo funcionário, extrai nome,
>CPF e CNPJ, agrupa as páginas por funcionário e salva arquivos PDF nomeados com nome, CPF e CNPJ.
    
##### PLANOS DE SAÚDE:
>Abre arquivos PDF, extrai dados de empresa, lotação, operador, plano, funcionários e dependentes, calcula
> valores e totais e gera planilhas Excel com o detalhamento e os consolidados.

#### FOLHA POR CENTRO DE CUSTO PROTHEUS:
>Abre PDFs, extrai centro de custo e código, cruza as informações com uma tabela
>Excel para obter o CNPJ e gera arquivos PDF separados por centro de custo.

####  RECIBOS DE PAGAMENTOS PROTHEUS:
>   Separa todos os arquivos .pdf que sejam recibos de pagamento emitidos pelo sistema
> Protheus com base no funcionário, criando um arquivo individual para cada novo funcionário.

#### NFS CAMAÇARI:
> Abre o arquivo, extrai nome e CNPJ e renomeia o arquivo.

#### NFS LAURO DE FREITAS;
> Abre o arquivo, extrai nome e CNPJ e renomeia o arquivo.

#### NFS BALNEÁRIO CAMBURIU:
> Abre o arquivo, extrai nome e CNPJ e renomeia o arquivo.

#### NFS VITÓRIA
>Abre o arquivo PDF, identifica o tipo de nota,
>extrai nome do cliente e número da NF e renomeia o arquivo.

#### BOLETOS SANTANDER
>Processa PDFs de boletos, classifica por tipo (ADM ou Despesa),
>extrai dados do pagador e organiza os arquivos em pasta própria.

#### NFS CURITIBA
> Abre o PDF, verifica se é uma DANFSe, captura o nome do cliente
> e salva o arquivo com nome único.

#### NFS SÃO PAULO
>Abre o arquivo, captura data e nome, e renomeia a nota fiscal 
>
#### BOLETOS VITÓRIA
> Abre o PDF, identifica o boleto e renomeia com cliente e CNPJ.

### LOCAL DE EXECUÇÃO


### SETOR ALVO

### DESENVOLVEDOR DO PROJETO
> * LUIZ GUSTAVO
> * JOAQUIM OLIVEIRA

