# Site — Cartório Arquimedes Bucar

2º Ofício de Guaraciaba do Norte — CE

Site institucional estático. HTML5 semântico + CSS. **Sem JavaScript.**
Basta subir os arquivos para a hospedagem — não há build, banco ou dependência externa.

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

css/base.css          Variáveis (cores, fontes, espaçamento), reset, tipografia
css/layout.css        Container, cabeçalho, navegação, rodapé, seções
css/componentes.css   Botões, cartões, acordeão, avisos, tabelas, trilha
css/paginas.css       Estilos específicos de página (abertura, mapa, horários)

arquivos/             PDFs de requerimentos (a receber do cartório)
img/                  Logo e fotos (a receber do cartório)
img/ods/              Painel oficial dos 17 ODS (baixar no site da ONU)
build.py              Gerador das páginas — opcional, ver abaixo
```

## O que precisa ser preenchido

Todos os campos pendentes estão entre colchetes no HTML. Uma busca por `[`
nos arquivos localiza todos.

| Marcador | Onde aparece |
|---|---|
| `[DENOMINAÇÃO OFICIAL DA SERVENTIA]` | rodapé, o-cartorio.html |
| `[NOME DO TABELIÃO/OFICIAL TITULAR]` | rodapé, o-cartorio.html |
| `[CNS]` | rodapé, o-cartorio.html |
| `[Rua, número, bairro]` e `[CEP]` | cabeçalho, rodapé, contato, ouvidoria |
| `[(88) 0000-0000]` e `+550000000000` | cabeçalho, rodapé, contato, ouvidoria |
| `[(88) 90000-0000]` e `5588900000000` | links de WhatsApp em todas as páginas |
| `[contato@dominio.com.br]` | rodapé, contato, ouvidoria |
| `[08h às 17h]` | cabeçalho, rodapé, contato |
| `[TEXTO DA MISSÃO / VISÃO / VALORES]` | o-cartorio.html |
| `[NOME DO RESPONSÁVEL PELA OUVIDORIA]` | ouvidoria.html |
| `[NOME DO ENCARREGADO]` e `[DATA]` | privacidade.html |
| `[CONFIRMAR COM O CARTÓRIO: ...]` | duvidas.html — agendamento e formas de pagamento |

Outros ajustes pendentes:

- **Mapa** (contato.html): trocar `q=Guaraciaba%20do%20Norte%2C%20CE` pelo endereço exato.
- **Emolumentos**: substituir o link do TJCE pelo endereço direto da tabela vigente.
  Revisar todo mês de janeiro.
- **Modelos**: colocar os PDFs em `arquivos/` e remover da lista os que não existirem.
- **Logo**: quando houver arquivo vetorial, substituir o texto em `.marca` por `<img>`.
- **Selo digital** (selo-digital.html): trocar `SELO_URL` pelo endereço exato da
  consulta de selo do TJCE — o cliente vai enviar.
- **Painel dos ODS** (agenda-2030.html): baixar o painel oficial em português em
  un.org/sustainabledevelopment/news/communications-material e salvar como
  `img/ods/ods-17-objetivos.png`. Os ícones têm diretrizes de uso da ONU — usar
  sempre os arquivos oficiais.
- **Aviso de Privacidade**: o texto é um modelo de partida e precisa de revisão
  jurídica antes de publicar.
- **Denominação**: o site usa "Cartório Arquimedes Bucar" como nome curto, a
  partir do perfil oficial no Instagram. Confirmar com o cartório e ajustar
  `NOME_CURTO` e `DESCRITOR` no `build.py` se a grafia oficial for outra.

## Cores e fontes

Estilo de portal de serviços: fundo claro, faixas escuras em verde-petróleo com
gradientes diagonais (abertura, topo das páginas internas, chamadas e rodapé),
cantos bem arredondados e botões em formato de pílula.

Todas as cores vêm das variáveis no topo de `css/base.css`:

```
--primaria         #0D7F78   botões, links, ícones, destaques
--primaria-escura  #0A615C   hover
--primaria-clara   #5FD4C7   destaques sobre fundo escuro
--primaria-suave   #E7F4F2   fundos de realce (menu ativo, rótulos, ícones)
--escuro           #081C1D   base das faixas escuras e do rodapé
--fundo            #F4F7F7   fundo do site
--branco           #FFFFFF   cabeçalho, cartões, painéis
--texto            #1C2A2D   corpo de texto
--suave            #5C6B6E   textos secundários
--borda            #E2E9E9   bordas
--tom-*                      gradientes leves dos cartões clicáveis
--gradiente-escuro           fundo com faixas diagonais (abertura, topo, CTA)
```

Tipografia: **Plus Jakarta Sans** (400–700) em todo o site, via Google Fonts com
`preconnect` e `display=swap`; o fallback é system-ui.

Se quiser eliminar a dependência externa, baixe os `.woff2`, coloque em
`fonts/`, declare com `@font-face` no topo de `base.css` e remova as tags de
`fonts.googleapis.com` do `<head>` de cada página (ou do `build.py`).

### Elementos visuais

- Cabeçalho branco fixo no topo, com ícone da marca (SVG em `layout.css`,
  `.marca::before` — trocar por `<img>` quando houver logo) e telefone em pílula.
- Abertura centralizada; o SVG decorativo vira um emblema acima do título.
- A faixa de informações da home flutua sobre a abertura como cartão.
- Cartões clicáveis: área inteira clicável, seta em círculo no canto e tons
  alternados (lilás, pêssego, menta, azul, areia).
- Raio de borda 12–24px, sombras suaves, transições de 220ms.

## Sobre o build.py

As páginas compartilham cabeçalho e rodapé idênticos. O `build.py` gera as 18
páginas a partir de um único template, o que evita esquecer um arquivo ao mudar
o menu ou o rodapé.

Uso opcional: os HTML já estão prontos e podem ser editados diretamente. Se for
editar pelo gerador, alterar o `build.py` e rodar `python3 build.py`.
**Atenção:** rodar o script sobrescreve os .html — não misturar os dois métodos.

## Acessibilidade e boas práticas aplicadas

- `lang="pt-BR"`, `<meta name="description">` distinto por página.
- Marcação semântica: `header`, `nav`, `main`, `section`, `article`, `footer`,
  `address`, `dl`, `table` com `<th scope>`.
- Link "Ir para o conteúdo" para navegação por teclado.
- `aria-current="page"` no item de menu ativo, `aria-labelledby` nas seções.
- Acordeões em `<details>/<summary>` nativos — funcionam sem JavaScript.
- Menu do celular alternado por `<input type="checkbox">` + `<label>` (sem
  JavaScript). Quando houver JS, trocar por um `<button>` com `aria-expanded`
  para melhor suporte a leitores de tela.
- Foco visível, suporte a `prefers-reduced-motion` e folha de impressão.
- Mobile-first: media queries em `min-width` (48em e 64em). Sem rolagem
  horizontal em 390px.
