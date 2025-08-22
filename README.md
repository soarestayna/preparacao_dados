# Preparação de Dados

Este repositório reúne os notebooks desenvolvidos durante o módulo de 
**Preparação de Dados** do curso de Análise de Dados – EBAC.  
O foco foi transformar dados brutos em conjuntos limpos, consistentes e 
prontos para análise, utilizando técnicas de tratamento, limpeza e 
otimização com Python.

---

## Objetivo

Demonstrar como preparar dados de forma eficiente e confiável, garantindo que 
estejam prontos para análises estatísticas, visualizações e modelagens.  
As atividades envolveram identificação de inconsistências, tratamento de 
valores nulos, padronização de formatos e enriquecimento de dados.

---

## Conteúdo dos Notebooks


### 1. **Tratamento de Dados com Pandas**

- Identificação e remoção de duplicatas
- Detecção e tratamento de valores nulos
- Conversão de tipos de dados (strings, datas, numéricos)
- Padronização de nomes de colunas e formatos


### 2. **Limpeza de Dados Textuais**

- Remoção de espaços, símbolos e caracteres especiais
- Normalização de textos (lowercase, strip, replace)
- Separação e junção de colunas textuais
- Aplicação de expressões regulares para limpeza avançada


### 3. **Enriquecimento de Dados**

- Criação de novas colunas derivadas (ex: ano, faixa etária, categorias)
- Agrupamentos e segmentações por critérios específicos
- Categorização de variáveis contínuas
- Integração com dados externos para complementar informações


### 4. **Exportação e Validação**


- Exportação dos dados limpos para CSV, Excel e JSON
- Verificação final de consistência e estrutura
- Documentação do processo de limpeza para reprodutibilidade



## Conteúdo dos Scripts Python

Além dos notebooks interativos, este repositório inclui scripts `.py` que replicam as etapas da preparação de dados de forma automatizada.

Esses scripts são úteis para:

- Executar o pré-processamento em ambientes fora do Jupyter
- Integrar a preparação de dados em pipelines ou aplicações
- Reutilizar funções e lógicas de preparação com maior eficiência


## Componentes do Projeto

- `pandas` – manipulação e limpeza de dados  
- `numpy` – tratamento de valores nulos e operações vetoriais  
- `sklearn` - para aplicar transformações nos dados
- `openpyxl` e `json` – exportação de arquivos

---

## Aprendizados


- Dados limpos são a base de qualquer análise confiável.  
- A preparação exige olhar crítico, paciência e domínio técnico.  
- Automatizar o processo de limpeza reduz erros e aumenta a escalabilidade.  
- Documentar cada etapa é essencial para replicar e justificar decisões.

---

### Como usar este repositório

Este repositório foi estruturado para facilitar o aprendizado.

Você pode explorá-lo de duas formas:

#### Notebooks
Os notebooks estão organizados por etapas e podem ser executados individualmente em ambiente Jupyter. 
Cada um contém explicações detalhadas, células comentadas e exemplos práticos.

#### Scripts Python
Os scripts `.py` replicam o conteúdo dos notebooks de forma automatizada.

Para executar:

```
python scripts/1_preparacao_dados.py 
```
Os arquivos .csv utilizados e gerados estão na pasta data/, e podem ser reproduzidos conforme o fluxo de tratamento.
Requisitos
Antes de executar os scripts, instale as dependências:
```
pip install -r requirements.txt
```

---

### Sobre mim

Sou estudante de Análise de Dados e este módulo representa minha 
evolução na transformação de dados brutos em informações úteis.  

