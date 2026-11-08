# Site — Cartório Arquimedes Bucar

2º Ofício de Guaraciaba do Norte — CE

Site institucional estático com **HTML + CSS + JavaScript (módulos ES)** e o conteúdo
centralizado em arquivos **JSON**. Não há build, banco de dados nem dependências para
instalar: basta enviar os arquivos por FTP para a hospedagem (LocalWeb).

## Como atualizar as informações do cartório

Quase tudo que muda no dia a dia está em `dados/`. Depois de editar, envie os arquivos
alterados por FTP — todas as páginas passam a mostrar o novo conteúdo.

| Arquivo | O que contém |
|---|---|
| `dados/cartorio.json` | Nome, descritor, denominação oficial, CNS, titular, endereço, CEP, telefones, WhatsApp, e-mail, Instagram, horários, mensagens do WhatsApp, links oficiais e menu |
| `dados/servicos.json` | As cinco atribuições: título, resumo, lista de serviços e documentação de cada uma |
| `dados/conteudo.json` | Apresentação (quem somos), missão/visão/valores, aviso sobre registro civil, portais de certidões, perguntas frequentes, modelos para download e Agenda 2030 |

Regras simples ao editar o JSON:

- Os textos entre aspas devem continuar entre aspas. Vírgulas separam os itens.
- Para trocar um telefone, mude **os dois campos**: `telefone` (como aparece na tela) e
  `telefoneLink` (somente números, com `+55`). O mesmo vale para o WhatsApp:
  `whatsapp` e `whatsappNumero`.
- Use um validador de JSON (por exemplo, `jsonlint.com`) antes de enviar, ou abra o site
  e confira se o aviso "Não foi possível carregar as informações do site" não aparece.
- Campos que começam com `[PREENCHER` são pendências do cartório.

### O que ainda precisa ser preenchido

- `responsaveis.ouvidoria`, `responsaveis.encarregado`, `responsaveis.privacidadeAtualizadoEm`
- Em `conteudo.json`: as duas respostas de FAQ sobre agendamento e pagamento
- `links.seloDigital` e `links.tabelaEmolumentos` — trocar pelos endereços diretos do TJCE
  (revisar a tabela de emolumentos todo mês de janeiro)
- `arquivos/` — enviar os PDFs citados em `conteudo.json → modelos`

## Estrutura

```
index.html                        Início
o-cartorio.html                   Apresentação, missão/visão/valores, dados da serventia
servicos.html                     Índice das cinco atribuições
servicos-notas.html               Tabelionato de Notas
servicos-protesto.html            Tabelionato de Protesto de Títulos
servicos-registro-imoveis.html    Registro de Imóveis
servicos-titulos-documentos.html  Registro de Títulos e Documentos
servicos-pessoas-juridicas.html   Registro Civil de Pessoas Jurídicas
certidoes.html                    Portais oficiais + certidões da serventia
selo-digital.html                 Conferência de autenticidade pelo selo do TJCE
emolumentos.html                  Tabela do TJCE e atos gratuitos
transparencia.html                Dados oficiais, valores e fiscalização
agenda-2030.html                  ODS da ONU e atuação da serventia
privacidade.html                  Aviso de Privacidade / LGPD
modelos.html                      Downloads de requerimentos
duvidas.html                      Perguntas frequentes
ouvidoria.html                    Ouvidoria e Corregedoria
contato.html                      Endereço, horários e mapa

dados/cartorio.json               Informações da serventia (o arquivo do dia a dia)
dados/servicos.json               Atribuições, serviços e documentação
dados/conteudo.json               Demais conteúdos editáveis

js/app.js                         Ponto de entrada: carrega os dados e monta a página
js/dados.js                       Leitura dos JSON
js/layout.js                      Cabeçalho, rodapé e menu do celular
js/componentes.js                 Acordeão, lista e aviso
js/paginas.js                     Blocos de cada página (cartões, contato, FAQ, ODS...)
js/vinculos.js                    Preenche contatos e links marcados no HTML
js/transicao.js                   Fade curto ao trocar de página
js/utilitarios.js                 Funções pequenas (escape de HTML, seletores)

css/base.css                      Variáveis (cores, fontes, espaçamento), reset, tipografia
css/layout.css                    Container, cabeçalho, navegação, rodapé, seções
css/componentes.css               Botões, cartões, acordeão, avisos, tabelas, trilha
css/paginas.css                   Estilos específicos de página (abertura, mapa, horários)

arquivos/                         PDFs de requerimentos
img/                              Logo e fotos
img/ods/                          Painel oficial dos 17 ODS
```

### Como as páginas funcionam

Cada HTML tem apenas o conteúdo próprio daquela página, com dois pontos de montagem:

- `<div id="site-cabecalho"></div>` e `<div id="site-rodape"></div>` — preenchidos por
  `js/layout.js` a partir do JSON (menu e rodapé existem em um único lugar).
- `data-render="nome-do-bloco"` — bloco montado por `js/paginas.js` (cartões, contato,
  FAQ, modelos, ODS, dados da serventia).
- `data-campo="telefone"`, `data-link="tjce"`, `data-wa="pedido"` — textos e links
  preenchidos por `js/vinculos.js` com os dados de `cartorio.json`.

Para editar textos corridos (quem somos, privacidade, emolumentos, selo digital), edite o
HTML da página. Para dados repetidos, edite o JSON.

### Adicionar uma página

1. Copie um HTML simples (por exemplo `modelos.html`) e ajuste `<title>`, a descrição,
   a trilha, o `<h1>` e o `data-pagina`.
2. Inclua `{ "arquivo": "nova-pagina.html", "rotulo": "Nova página" }` em
   `cartorio.json → navegacao`.
3. Crie o conteúdo ou peça um bloco em `js/paginas.js`.

## Publicar por FTP (LocalWeb)

1. Conecte no painel da LocalWeb (FileZilla ou o gerenciador de arquivos do painel).
2. Envie **todo o conteúdo** da raiz do projeto para a pasta pública do domínio
   (`public_html` ou `www`), mantendo as pastas `css/`, `js/`, `dados/`, `img/` e
   `arquivos/`.
3. Confira `https://seudominio.com.br/index.html` e abra também uma página interna para
   confirmar que o menu e o rodapé aparecem.
4. Ao alterar apenas o JSON, basta reenviar o arquivo de `dados/` correspondente.

Não envie `.git/`, `.github/` nem arquivos de sistema (`desktop.ini`, `Thumbs.db`).

## Publicar no GitHub

O repositório é o mesmo do projeto. Fluxo simples:

```bash
git add .
git commit -m "Atualiza dados do cartório"
git push
```

Se preferir automatizar o envio por FTP a cada `push`, crie em
**Settings → Secrets and variables → Actions** as variáveis `FTP_SERVIDOR`, `FTP_USUARIO`
e `FTP_SENHA` e um workflow que rode `lftp`/`ftp-deploy`. As credenciais ficam nos
segredos do GitHub, nunca no código.

## Boas práticas aplicadas

- `lang="pt-BR"`, `<meta name="description">` distinto por página, `<title>` montado a
  partir do JSON.
- Marcação semântica: `header`, `nav`, `main`, `section`, `article`, `footer`, `address`,
  `dl`, `table` com `<th scope>`.
- Link "Ir para o conteúdo", `aria-current="page"` no menu, `aria-labelledby` nas seções.
- Menu do celular em `<button aria-expanded>`, fecha com `Esc` e ao escolher um item.
- Acordeões em `<details>/<summary>` nativos.
- Foco visível, `prefers-reduced-motion` e folha de impressão.
- Mobile-first, media queries em `min-width` (48em e 64em).
- Dados centralizados e escapados antes de entrar no HTML; nenhuma dependência externa
  além da fonte Plus Jakarta Sans (Google Fonts).

## Cores e fontes

Todas as cores vêm das variáveis no topo de `css/base.css`:

```
--primaria         #0D7F78   botões, links, ícones, destaques
--primaria-escura  #0A615C   hover
--primaria-clara   #5FD4C7   destaques sobre fundo escuro
--primaria-suave   #E7F4F2   fundos de realce
--escuro           #081C1D   faixas escuras e rodapé
--fundo            #F4F7F7   fundo do site
--texto            #1C2A2D   corpo de texto
--suave            #5C6B6E   textos secundários
--borda            #E2E9E9   bordas
```

Tipografia: **Plus Jakarta Sans** (400–700) via Google Fonts, fallback `system-ui`.
Para remover a dependência externa, baixe os `.woff2`, coloque em `fonts/`, declare com
`@font-face` em `base.css` e remova as tags do Google Fonts do `<head>` das páginas.
