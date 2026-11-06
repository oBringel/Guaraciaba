#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador das páginas estáticas do site do cartório.
Executar: python3 build.py
Saída: arquivos .html na raiz do projeto.
"""

import html as _html
import os

# Entidades que devem permanecer escapadas no HTML final
_PROTEGIDAS = {
    "&amp;": "\x00A\x00",
    "&lt;": "\x00L\x00",
    "&gt;": "\x00G\x00",
    "&quot;": "\x00Q\x00",
}


def para_utf8(texto):
    """Converte entidades (&ccedil;, &atilde;...) em caracteres UTF-8 reais,
    preservando &amp;, &lt;, &gt; e &quot;."""
    for entidade, marca in _PROTEGIDAS.items():
        texto = texto.replace(entidade, marca)
    texto = _html.unescape(texto)
    for entidade, marca in _PROTEGIDAS.items():
        texto = texto.replace(marca, entidade)
    return texto

RAIZ = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Dados do cartório — trocar os valores entre colchetes pelos reais
# ---------------------------------------------------------------------------

NOME_CURTO = "Cartório Arquimedes Bucar"
DESCRITOR = "2º Ofício de Guaraciaba do Norte &middot; Serviços Notariais e Registrais"
NOME_OFICIAL = "[DENOMINAÇÃO OFICIAL DA SERVENTIA]"
TITULAR = "[NOME DO TABELIÃO/OFICIAL TITULAR]"
CNS = "[CNS]"
ENDERECO = "[Rua, número, bairro]"
CIDADE = "Guaraciaba do Norte &ndash; CE"
CEP = "[CEP]"
TELEFONE = "[(88) 0000-0000]"
TELEFONE_LINK = "+550000000000"
WHATSAPP = "[(88) 90000-0000]"
WHATSAPP_NUM = "5588900000000"
EMAIL = "[contato@dominio.com.br]"
HORARIO_CURTO = "Segunda a sexta, [08h &agrave;s 17h]"

WA_BASE = "https://wa.me/" + WHATSAPP_NUM
WA_PEDIDO = (
    WA_BASE
    + "?text=Ol%C3%A1%2C%20gostaria%20de%20consultar%20o%20andamento"
    + "%20do%20meu%20pedido.%20Protocolo%3A%20"
)
WA_DUVIDA = (
    WA_BASE + "?text=Ol%C3%A1%2C%20gostaria%20de%20tirar%20uma%20d%C3%BAvida."
)

INSTAGRAM_USUARIO = "@2cartorioguaraciaba"
INSTAGRAM_URL = "https://www.instagram.com/2cartorioguaraciaba"

# Consulta de selo digital do TJCE — substituir pelo endereço exato
SELO_URL = "https://www.tjce.jus.br/"

# Portais oficiais usados em mais de uma página
PORTAL_RI = "https://www.registrodeimoveis.org.br/"
PORTAL_MAPA_ONR = "https://mapa.onr.org.br/"
PORTAL_ENOTARIADO = "https://www.e-notariado.org.br/customer"
PORTAL_REGISTRO_CIVIL = "https://www.registrocivil.org.br/"
PORTAL_CENSEC = "https://www.censec.org.br/"
PORTAL_CENPROT = "https://www.protestodetitulos.org.br/"
PORTAL_JUSTICA_ABERTA = "https://www.cnj.jus.br/corregedoria/justica_aberta/"

# ---------------------------------------------------------------------------
# Navegação
# ---------------------------------------------------------------------------

NAV = [
    ("index.html", "In&iacute;cio"),
    ("o-cartorio.html", "O Cart&oacute;rio"),
    ("servicos.html", "Servi&ccedil;os"),
    ("certidoes.html", "Certid&otilde;es"),
    ("selo-digital.html", "Selo Digital"),
    ("emolumentos.html", "Emolumentos"),
    ("transparencia.html", "Transpar&ecirc;ncia"),
    ("agenda-2030.html", "Agenda 2030"),
    ("duvidas.html", "D&uacute;vidas"),
    ("contato.html", "Contato"),
]

ATRIBUICOES = [
    ("servicos-notas.html", "Tabelionato de Notas"),
    ("servicos-protesto.html", "Tabelionato de Protesto de T&iacute;tulos"),
    ("servicos-registro-imoveis.html", "Registro de Im&oacute;veis"),
    ("servicos-titulos-documentos.html", "Registro de T&iacute;tulos e Documentos"),
    ("servicos-pessoas-juridicas.html", "Registro Civil de Pessoas Jur&iacute;dicas"),
]


# ---------------------------------------------------------------------------
# Fragmentos
# ---------------------------------------------------------------------------


def navegacao(atual):
    itens = []
    for href, rotulo in NAV:
        marca = ' aria-current="page"' if href == atual else ""
        itens.append(
            '          <li><a class="navegacao__link" href="%s"%s>%s</a></li>'
            % (href, marca, rotulo)
        )
    return "\n".join(itens)


def cabecalho(atual):
    return """  <a class="pular-conteudo" href="#conteudo">Ir para o conte&uacute;do</a>

  <header class="cabecalho">
    <div class="container cabecalho__interno">
      <a class="marca" href="index.html">
        <span class="marca__nome">{nome_curto}</span>
        <span class="marca__desc">{descritor}</span>
      </a>

      <p class="cabecalho__contato">
        <a href="tel:{tel_link}">{telefone}</a><br />
        {horario}
      </p>

      <!-- Menu do celular: alternado apenas com CSS, sem JavaScript -->
      <input class="menu-alternador" type="checkbox" id="abrir-menu" />
      <label class="menu-rotulo" for="abrir-menu">
        <span class="menu-rotulo__icone" aria-hidden="true"></span>
        <span class="menu-rotulo__texto">Menu</span>
      </label>

      <nav class="navegacao" aria-label="Navega&ccedil;&atilde;o principal">
        <ul class="navegacao__lista">
{itens}
        </ul>
      </nav>
    </div>
  </header>""".format(
        nome_curto=NOME_CURTO,
        descritor=DESCRITOR,
        horario=HORARIO_CURTO,
        tel_link=TELEFONE_LINK,
        telefone=TELEFONE,
        itens=navegacao(atual),
    )


def rodape():
    links_atrib = "\n".join(
        '            <li><a href="%s">%s</a></li>' % (h, r) for h, r in ATRIBUICOES
    )
    return """  <footer class="rodape">
    <div class="container">
      <div class="rodape__grade">
        <div>
          <p class="rodape__titulo">{nome_curto}</p>
          <address>
            {endereco}<br />
            {cidade} &middot; CEP {cep}<br />
            Telefone: <a href="tel:{tel_link}">{telefone}</a><br />
            WhatsApp: <a href="{wa}">{whatsapp}</a><br />
            E-mail: <a href="mailto:{email}">{email}</a><br />
            Instagram: <a href="{instagram_url}" rel="external noopener" target="_blank">{instagram}</a>
          </address>
          <p class="sem-margem">{horario}</p>
        </div>

        <div>
          <p class="rodape__titulo">Atribui&ccedil;&otilde;es</p>
          <ul class="rodape__lista">
{links_atrib}
          </ul>
        </div>

        <div>
          <p class="rodape__titulo">Institucional</p>
          <ul class="rodape__lista">
            <li><a href="transparencia.html">Transpar&ecirc;ncia</a></li>
            <li><a href="modelos.html">Modelos e requerimentos</a></li>
            <li><a href="agenda-2030.html">Agenda 2030</a></li>
            <li><a href="privacidade.html">Aviso de Privacidade e LGPD</a></li>
            <li><a href="ouvidoria.html">Ouvidoria</a></li>
            <li>
              <a href="https://www.tjce.jus.br/" rel="external noopener" target="_blank">
                Corregedoria-Geral de Justi&ccedil;a do Cear&aacute;
              </a>
            </li>
          </ul>
        </div>
      </div>

      <div class="rodape__base">
        <p>{nome_oficial} &middot; CNS {cns} &middot; Titular: {titular}</p>
        <p>
          Os emolumentos dos servi&ccedil;os notariais e de registro s&atilde;o fixados por lei
          estadual e divulgados pelo Tribunal de Justi&ccedil;a do Cear&aacute;.
        </p>
      </div>
    </div>
  </footer>""".format(
        nome_curto=NOME_CURTO,
        nome_oficial=NOME_OFICIAL,
        endereco=ENDERECO,
        cidade=CIDADE,
        cep=CEP,
        tel_link=TELEFONE_LINK,
        telefone=TELEFONE,
        wa=WA_DUVIDA,
        whatsapp=WHATSAPP,
        email=EMAIL,
        instagram=INSTAGRAM_USUARIO,
        instagram_url=INSTAGRAM_URL,
        horario=HORARIO_CURTO,
        cns=CNS,
        titular=TITULAR,
        links_atrib=links_atrib,
    )


def trilha(itens):
    """itens: lista de tuplas (href|None, rotulo). O ultimo e a pagina atual."""
    partes = []
    for href, rotulo in itens:
        if href:
            partes.append("            <li><a href=\"%s\">%s</a></li>" % (href, rotulo))
        else:
            partes.append(
                '            <li><span aria-current="page">%s</span></li>' % rotulo
            )
    return """      <nav class="trilha" aria-label="Voc&ecirc; est&aacute; em">
        <ol class="trilha__lista">
%s
        </ol>
      </nav>""" % "\n".join(
        partes
    )


def topo_pagina(titulo, resumo, itens_trilha):
    return """  <div class="pagina-topo">
    <div class="container">
{trilha}
      <h1>{titulo}</h1>
      <p class="pagina-topo__resumo">{resumo}</p>
    </div>
  </div>""".format(
        trilha=trilha(itens_trilha), titulo=titulo, resumo=resumo
    )


def pagina(arquivo, titulo_aba, descricao, corpo, nav_atual=None):
    html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{titulo_aba} &ndash; {nome_curto}</title>
  <meta name="description" content="{descricao}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" />
  <link rel="stylesheet" href="css/base.css" />
  <link rel="stylesheet" href="css/layout.css" />
  <link rel="stylesheet" href="css/componentes.css" />
  <link rel="stylesheet" href="css/paginas.css" />
</head>
<body>
{cabecalho}

{corpo}

{rodape}
</body>
</html>
""".format(
        titulo_aba=titulo_aba,
        nome_curto=NOME_CURTO,
        descricao=descricao,
        cabecalho=cabecalho(nav_atual or arquivo),
        corpo=corpo,
        rodape=rodape(),
    )
    caminho = os.path.join(RAIZ, arquivo)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(para_utf8(html))
    return arquivo


def acordeao(titulo, corpo):
    return """        <details class="acordeao">
          <summary>{titulo}</summary>
          <div class="acordeao__corpo">
{corpo}
          </div>
        </details>""".format(
        titulo=titulo, corpo=corpo
    )


def lista(itens, classe="lista-servicos"):
    li = "\n".join("            <li>%s</li>" % i for i in itens)
    return '          <ul class="%s">\n%s\n          </ul>' % (classe, li)


def lista_simples(itens):
    li = "\n".join("              <li>%s</li>" % i for i in itens)
    return "            <ul>\n%s\n            </ul>" % li


def cartoes_atribuicoes():
    resumos = {
        "servicos-notas.html": "Reconhecimento e abertura de firma, autentica&ccedil;&atilde;o de c&oacute;pias, escrituras, procura&ccedil;&otilde;es, invent&aacute;rio, testamento e atos eletr&ocirc;nicos.",
        "servicos-protesto.html": "Apresenta&ccedil;&atilde;o e protesto de t&iacute;tulos, pagamento, cancelamento e certid&otilde;es de protesto.",
        "servicos-registro-imoveis.html": "Registro de compra e venda, hipoteca, aliena&ccedil;&atilde;o fiduci&aacute;ria, averba&ccedil;&otilde;es e certid&otilde;es de matr&iacute;cula.",
        "servicos-titulos-documentos.html": "Registro de contratos em geral, notifica&ccedil;&atilde;o extrajudicial e conserva&ccedil;&atilde;o de documentos.",
        "servicos-pessoas-juridicas.html": "Registro de associa&ccedil;&otilde;es, funda&ccedil;&otilde;es, sociedades simples, atas e altera&ccedil;&otilde;es estatut&aacute;rias.",
    }
    blocos = []
    for indice, (href, rotulo) in enumerate(ATRIBUICOES, start=1):
        blocos.append(
            """          <article class="cartao cartao--link">
            <span class="cartao__numero" aria-hidden="true">{numero}</span>
            <h3 class="cartao__titulo"><a href="{href}">{rotulo}</a></h3>
            <p>{resumo}</p>
            <p class="cartao__rodape"><a href="{href}">Conhecer servi&ccedil;os &rarr;</a></p>
          </article>""".format(
                numero="%02d" % indice, href=href, rotulo=rotulo, resumo=resumos[href]
            )
        )
    return '        <div class="grade grade--atribuicoes">\n%s\n        </div>' % "\n".join(
        blocos
    )


AVISO_RCPN = """        <div class="aviso">
          <p class="aviso__titulo">Aten&ccedil;&atilde;o</p>
          <p class="sem-margem">
            Esta serventia <strong>n&atilde;o possui atribui&ccedil;&atilde;o de Registro Civil das Pessoas
            Naturais</strong>. Certid&otilde;es de nascimento, casamento e &oacute;bito n&atilde;o s&atilde;o
            emitidas aqui &mdash; veja em
            <a href="certidoes.html">Certid&otilde;es</a> onde solicit&aacute;-las.
          </p>
        </div>"""


def bloco_whatsapp(titulo, texto, rotulo_botao, url):
    return """        <div class="cta">
          <h2>{titulo}</h2>
          <p>{texto}</p>
          <p class="cta__acoes sem-margem">
            <a class="botao botao--contraste" href="{url}" rel="noopener" target="_blank">{rotulo}</a>
          </p>
        </div>""".format(
        titulo=titulo, texto=texto, url=url, rotulo=rotulo_botao
    )


FIGURA_ABERTURA = """        <div class="abertura__figura" aria-hidden="true">
          <!-- Elemento decorativo. Substituir por <img> quando houver foto da fachada. -->
          <svg viewBox="0 0 360 300" role="presentation" focusable="false">
            <g fill="none" stroke="currentColor" stroke-width="1.1">
              <path d="M20 280 V150 a40 40 0 0 1 80 0 V280" />
              <path d="M140 280 V150 a40 40 0 0 1 80 0 V280" />
              <path d="M260 280 V150 a40 40 0 0 1 80 0 V280" />
              <path d="M0 280 H360" />
              <path d="M8 268 H352" stroke-opacity="0.5" />
              <path d="M40 280 V170" stroke-opacity="0.45" />
              <path d="M80 280 V170" stroke-opacity="0.45" />
              <path d="M160 280 V170" stroke-opacity="0.45" />
              <path d="M200 280 V170" stroke-opacity="0.45" />
              <path d="M280 280 V170" stroke-opacity="0.45" />
              <path d="M320 280 V170" stroke-opacity="0.45" />
              <path d="M0 96 H360" stroke-opacity="0.6" />
              <path d="M0 104 H360" stroke-opacity="0.3" />
              <path d="M40 96 L180 24 L320 96" stroke-opacity="0.6" />
            </g>
          </svg>
        </div>"""


# ===========================================================================
# 1. Início
# ===========================================================================

corpo_index = """  <main id="conteudo">
    <section class="abertura" aria-labelledby="titulo-abertura">
      <div class="container abertura__grade">
        <div>
          <p class="abertura__olho">Comarca de Guaraciaba do Norte &middot; Cear&aacute;</p>
          <h1 id="titulo-abertura">{nome_curto}</h1>
          <p class="abertura__linha">
            Seguran&ccedil;a e confian&ccedil;a para seus atos notariais e registrais.
          </p>
          <p class="abertura__texto">
            Servi&ccedil;os prestados com f&eacute; p&uacute;blica, transpar&ecirc;ncia e aten&ccedil;&atilde;o a cada caso.
          </p>
          <div class="botoes">
            <a class="botao botao--contraste" href="servicos.html">Conhe&ccedil;a nossos servi&ccedil;os</a>
            <a class="botao botao--claro" href="{wa_duvida}" rel="noopener" target="_blank">Falar no WhatsApp</a>
          </div>
        </div>
{figura}
      </div>
    </section>

    <section class="faixa faixa--branca faixa--compacta" aria-label="Informa&ccedil;&otilde;es de atendimento">
      <div class="container informacoes">
        <div class="informacao">
          <svg class="icone" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
            <circle cx="12" cy="12" r="9" />
            <path d="M12 7v5l3.2 2" />
          </svg>
          <p>
            <span class="informacao__rotulo">Atendimento</span>
            <span class="informacao__valor">{horario}</span>
          </p>
        </div>
        <div class="informacao">
          <svg class="icone" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
            <path d="M12 21s7-5.7 7-11a7 7 0 1 0-14 0c0 5.3 7 11 7 11z" />
            <circle cx="12" cy="10" r="2.5" />
          </svg>
          <p>
            <span class="informacao__rotulo">Endere&ccedil;o</span>
            <span class="informacao__valor">{endereco}<br />{cidade}</span>
          </p>
        </div>
        <div class="informacao">
          <svg class="icone" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
            <path d="M4.5 5.5A1.5 1.5 0 0 1 6 4h2l1.5 4-2 1.5a12 12 0 0 0 5.5 5.5l1.5-2 4 1.5v2a1.5 1.5 0 0 1-1.5 1.5A16 16 0 0 1 4.5 5.5z" />
          </svg>
          <p>
            <span class="informacao__rotulo">Telefone</span>
            <span class="informacao__valor"><a href="tel:{tel_link}">{telefone}</a></span>
          </p>
        </div>
      </div>
    </section>

    <section class="faixa faixa--creme" aria-labelledby="titulo-atribuicoes">
      <div class="container">
        <div class="secao__cabecalho">
          <span class="secao__rotulo">Atribui&ccedil;&otilde;es</span>
          <h2 id="titulo-atribuicoes">Cinco especialidades em uma serventia</h2>
          <p class="secao__intro sem-margem">
            Selecione uma atribui&ccedil;&atilde;o para ver os servi&ccedil;os prestados e a documenta&ccedil;&atilde;o
            necess&aacute;ria em cada um.
          </p>
        </div>
{cartoes}
      </div>
    </section>

    <section class="faixa faixa--branca" aria-labelledby="titulo-sobre">
      <div class="container">
        <span class="secao__rotulo">O cart&oacute;rio</span>
        <h2 id="titulo-sobre">F&eacute; p&uacute;blica a servi&ccedil;o da comunidade</h2>
        <div class="prosa">
          <p>
            Os servi&ccedil;os notariais e de registro s&atilde;o exercidos por delega&ccedil;&atilde;o do Poder
            P&uacute;blico e fiscalizados pelo Poder Judici&aacute;rio. Cada ato praticado nesta
            serventia tem f&eacute; p&uacute;blica e produz efeitos perante qualquer pessoa, &oacute;rg&atilde;o ou
            institui&ccedil;&atilde;o do pa&iacute;s.
          </p>
          <p>
            Atendemos a popula&ccedil;&atilde;o de Guaraciaba do Norte e regi&atilde;o com orienta&ccedil;&atilde;o clara
            sobre cada procedimento, para que ningu&eacute;m precise voltar ao balc&atilde;o por falta
            de um documento.
          </p>
          <p class="sem-margem">
            <a class="botao botao--secundario" href="o-cartorio.html">Sobre a serventia</a>
          </p>
        </div>
        <div class="espaco-acima">
{aviso}
        </div>
      </div>
    </section>

    <section class="faixa faixa--creme" aria-labelledby="titulo-online">
      <div class="container">
        <div class="secao__cabecalho">
          <span class="secao__rotulo">Servi&ccedil;os on-line</span>
          <h2 id="titulo-online">Resolva sem sair de casa</h2>
        </div>
        <div class="grade">
          <article class="cartao cartao--link">
            <h3 class="cartao__titulo"><a href="certidoes.html">Pedidos de certid&atilde;o</a></h3>
            <p>Portais oficiais para solicitar certid&otilde;es pela internet.</p>
            <p class="cartao__rodape"><a href="certidoes.html">Acessar &rarr;</a></p>
          </article>
          <article class="cartao cartao--link">
            <h3 class="cartao__titulo"><a href="selo-digital.html">Selo digital</a></h3>
            <p>Confira a autenticidade de um documento expedido por n&oacute;s.</p>
            <p class="cartao__rodape"><a href="selo-digital.html">Conferir &rarr;</a></p>
          </article>
          <article class="cartao cartao--link">
            <h3 class="cartao__titulo"><a href="emolumentos.html">Tabela de emolumentos</a></h3>
            <p>Valores fixados por lei estadual e divulgados pelo TJCE.</p>
            <p class="cartao__rodape"><a href="emolumentos.html">Consultar &rarr;</a></p>
          </article>
          <article class="cartao cartao--link">
            <h3 class="cartao__titulo"><a href="modelos.html">Modelos e requerimentos</a></h3>
            <p>Formul&aacute;rios para preencher antes de vir ao cart&oacute;rio.</p>
            <p class="cartao__rodape"><a href="modelos.html">Baixar &rarr;</a></p>
          </article>
          <article class="cartao cartao--link">
            <h3 class="cartao__titulo"><a href="duvidas.html">D&uacute;vidas frequentes</a></h3>
            <p>As perguntas que mais chegam ao nosso atendimento.</p>
            <p class="cartao__rodape"><a href="duvidas.html">Ver respostas &rarr;</a></p>
          </article>
        </div>
      </div>
    </section>

    <section class="faixa faixa--navy" aria-labelledby="titulo-pedido">
      <div class="container">
        <span class="secao__rotulo">Acompanhamento</span>
        <h2 id="titulo-pedido">Consulte o andamento do seu pedido</h2>
        <p>
          Informe o n&uacute;mero do protocolo pelo WhatsApp e o atendimento retorna com a
          situa&ccedil;&atilde;o do seu pedido.
        </p>
        <p class="sem-margem">
          <a class="botao botao--contraste" href="{wa_pedido}" rel="noopener" target="_blank">Consultar meu pedido</a>
        </p>
      </div>
    </section>
  </main>""".format(
    nome_curto=NOME_CURTO,
    wa_duvida=WA_DUVIDA,
    wa_pedido=WA_PEDIDO,
    figura=FIGURA_ABERTURA,
    horario=HORARIO_CURTO,
    endereco=ENDERECO,
    cidade=CIDADE,
    tel_link=TELEFONE_LINK,
    telefone=TELEFONE,
    cartoes=cartoes_atribuicoes(),
    aviso=AVISO_RCPN,
)

# ===========================================================================
# 2. O Cartório
# ===========================================================================

corpo_cartorio = """{topo}

  <main class="container conteudo" id="conteudo">
    <section class="secao" aria-labelledby="titulo-quem">
      <h2 class="secao__titulo" id="titulo-quem">Quem somos</h2>
      <div class="prosa">
        <p>[TEXTO DE APRESENTA&Ccedil;&Atilde;O DO CART&Oacute;RIO &mdash; hist&oacute;rico, tempo de atua&ccedil;&atilde;o e
        abrang&ecirc;ncia do atendimento.]</p>
      </div>
    </section>

    <section class="secao" aria-labelledby="titulo-mvv">
      <h2 class="secao__titulo" id="titulo-mvv">Miss&atilde;o, vis&atilde;o e valores</h2>
      <div class="grade">
        <article class="cartao">
          <h3 class="cartao__titulo">Miss&atilde;o</h3>
          <p>[TEXTO DA MISS&Atilde;O]</p>
        </article>
        <article class="cartao">
          <h3 class="cartao__titulo">Vis&atilde;o</h3>
          <p>[TEXTO DA VIS&Atilde;O]</p>
        </article>
        <article class="cartao">
          <h3 class="cartao__titulo">Valores</h3>
          <p>[TEXTO DOS VALORES]</p>
        </article>
      </div>
    </section>

    <section class="secao" aria-labelledby="titulo-dados">
      <h2 class="secao__titulo" id="titulo-dados">Dados da serventia</h2>
      <div class="painel">
        <dl class="dados">
          <dt>Denomina&ccedil;&atilde;o oficial</dt>
          <dd>{nome_oficial}</dd>
          <dt>Titular</dt>
          <dd>{titular}</dd>
          <dt>C&oacute;digo Nacional da Serventia (CNS)</dt>
          <dd>{cns}</dd>
          <dt>Comarca</dt>
          <dd>Guaraciaba do Norte &ndash; Cear&aacute;</dd>
          <dt>Atribui&ccedil;&otilde;es</dt>
          <dd>
            Tabelionato de Notas &middot; Tabelionato de Protesto de T&iacute;tulos &middot;
            Registro de Im&oacute;veis &middot; Registro de T&iacute;tulos e Documentos &middot;
            Registro Civil de Pessoas Jur&iacute;dicas
          </dd>
          <dt>Endere&ccedil;o</dt>
          <dd>{endereco} &middot; {cidade} &middot; CEP {cep}</dd>
          <dt>Atendimento</dt>
          <dd>{horario}</dd>
        </dl>
      </div>
    </section>

    <section class="secao" aria-label="Aviso sobre registro civil">
{aviso}
    </section>
  </main>""".format(
    topo=topo_pagina(
        "O Cart&oacute;rio",
        "Apresenta&ccedil;&atilde;o da serventia, suas atribui&ccedil;&otilde;es e os dados oficiais de "
        "identifica&ccedil;&atilde;o.",
        [("index.html", "In&iacute;cio"), (None, "O Cart&oacute;rio")],
    ),
    nome_oficial=NOME_OFICIAL,
    titular=TITULAR,
    cns=CNS,
    endereco=ENDERECO,
    cidade=CIDADE,
    cep=CEP,
    horario=HORARIO_CURTO,
    aviso=AVISO_RCPN,
)

# ===========================================================================
# 3. Serviços (hub)
# ===========================================================================

corpo_servicos = """{topo}

  <main class="container conteudo" id="conteudo">
    <section class="secao" aria-labelledby="titulo-lista">
      <h2 class="apenas-leitor" id="titulo-lista">Atribui&ccedil;&otilde;es</h2>
{cartoes}
    </section>

    <section class="secao" aria-label="Observa&ccedil;&otilde;es">
{aviso}
      <p class="nota">
        A documenta&ccedil;&atilde;o indicada em cada servi&ccedil;o &eacute; a exigida na maioria dos casos e
        pode variar conforme a situa&ccedil;&atilde;o concreta. Antes de vir ao cart&oacute;rio, confirme
        pelo telefone ou pelo WhatsApp.
      </p>
    </section>
  </main>""".format(
    topo=topo_pagina(
        "Servi&ccedil;os",
        "Servi&ccedil;os prestados pelas cinco atribui&ccedil;&otilde;es da serventia, com a "
        "documenta&ccedil;&atilde;o normalmente exigida em cada um.",
        [("index.html", "In&iacute;cio"), (None, "Servi&ccedil;os")],
    ),
    cartoes=cartoes_atribuicoes(),
    aviso=AVISO_RCPN,
)


# ===========================================================================
# 4. Páginas de atribuição
# ===========================================================================


def corpo_atribuicao(titulo, resumo, intro, servicos, acordeoes, extra=""):
    blocos = "\n".join(acordeao(t, c) for t, c in acordeoes)
    return """{topo}

  <main class="container conteudo" id="conteudo">
    <section class="secao" aria-labelledby="titulo-servicos">
      <h2 class="secao__titulo" id="titulo-servicos">Servi&ccedil;os prestados</h2>
      <p class="secao__intro">{intro}</p>
{lista}
    </section>

    <section class="secao" aria-labelledby="titulo-documentos">
      <h2 class="secao__titulo" id="titulo-documentos">O que levar</h2>
      <p class="secao__intro">
        Abra o servi&ccedil;o desejado para ver a documenta&ccedil;&atilde;o normalmente exigida.
      </p>
{blocos}
      <p class="nota">
        A rela&ccedil;&atilde;o acima atende &agrave; maioria dos casos e pode variar conforme a
        situa&ccedil;&atilde;o. Confirme com o atendimento antes de vir ao cart&oacute;rio.
      </p>
    </section>
{extra}
    <section class="secao" aria-label="Contato">
{bloco}
    </section>
  </main>""".format(
        topo=topo_pagina(
            titulo,
            resumo,
            [
                ("index.html", "In&iacute;cio"),
                ("servicos.html", "Servi&ccedil;os"),
                (None, titulo),
            ],
        ),
        intro=intro,
        lista=lista(servicos),
        blocos=blocos,
        extra=extra,
        bloco=bloco_whatsapp(
            "Ficou com d&uacute;vida sobre algum servi&ccedil;o?",
            "Fale com o atendimento pelo WhatsApp e confirme a documenta&ccedil;&atilde;o do seu caso "
            "antes de vir ao cart&oacute;rio.",
            "Falar no WhatsApp",
            WA_DUVIDA,
        ),
    )


# --- Notas ----------------------------------------------------------------

corpo_notas = corpo_atribuicao(
    "Tabelionato de Notas",
    "Atos notariais com f&eacute; p&uacute;blica: firmas, autentica&ccedil;&otilde;es, escrituras, "
    "procura&ccedil;&otilde;es, invent&aacute;rio, testamento e atos eletr&ocirc;nicos.",
    "O Tabelionato de Notas formaliza e d&aacute; f&eacute; p&uacute;blica a declara&ccedil;&otilde;es de vontade e "
    "a fatos jur&iacute;dicos, garantindo seguran&ccedil;a e validade aos documentos.",
    [
        "Abertura de firma",
        "Reconhecimento de firma",
        "Autentica&ccedil;&atilde;o de c&oacute;pias",
        "Atos eletr&ocirc;nicos (e-Notariado)",
        "Certificado digital do e-Notariado",
        "Autoriza&ccedil;&atilde;o de viagem para menores",
        "Procura&ccedil;&atilde;o e substabelecimento",
        "Escritura de compra e venda de bens",
        "Escritura de doa&ccedil;&atilde;o de bens",
        "Invent&aacute;rio e partilha extrajudicial",
        "Div&oacute;rcio e separa&ccedil;&atilde;o extrajudicial",
        "Uni&atilde;o est&aacute;vel",
        "Pacto antenupcial",
        "Testamento e planejamento sucess&oacute;rio",
        "Emancipa&ccedil;&atilde;o",
        "Usucapi&atilde;o extrajudicial",
        "Ata notarial",
    ],
    [
        (
            "Abertura e reconhecimento de firma",
            lista_simples(
                [
                    "Documento de identidade original com foto e assinatura (RG, CNH ou passaporte).",
                    "CPF.",
                    "Comparecimento pessoal do titular para a abertura da firma.",
                    "Para reconhecimento por autenticidade, quem assinou deve comparecer pessoalmente.",
                ]
            ),
        ),
        (
            "Procura&ccedil;&atilde;o",
            lista_simples(
                [
                    "Documento de identidade e CPF de quem outorga os poderes.",
                    "Dados completos do procurador: nome, CPF, estado civil, profiss&atilde;o e endere&ccedil;o.",
                    "Descri&ccedil;&atilde;o dos poderes a serem concedidos.",
                    "Se envolver im&oacute;vel, n&uacute;mero da matr&iacute;cula e dados do bem.",
                ]
            ),
        ),
        (
            "Escritura de compra e venda de im&oacute;vel",
            lista_simples(
                [
                    "Documentos de identidade e CPF de vendedores, compradores e respectivos c&ocirc;njuges.",
                    "Certid&atilde;o de casamento atualizada ou certid&atilde;o de nascimento, conforme o estado civil.",
                    "Certid&atilde;o de matr&iacute;cula atualizada do im&oacute;vel.",
                    "Certid&otilde;es exigidas em rela&ccedil;&atilde;o aos vendedores e ao im&oacute;vel.",
                    "Comprovante de recolhimento do ITBI.",
                    "Carn&ecirc; de IPTU ou certid&atilde;o de valor venal (im&oacute;vel urbano) ou CCIR e ITR (im&oacute;vel rural).",
                ]
            ),
        ),
        (
            "Escritura de doa&ccedil;&atilde;o",
            lista_simples(
                [
                    "Documentos de identidade e CPF do doador, do donat&aacute;rio e dos c&ocirc;njuges.",
                    "Certid&atilde;o de estado civil das partes.",
                    "Certid&atilde;o de matr&iacute;cula atualizada, no caso de im&oacute;vel.",
                    "Comprovante de recolhimento do ITCD.",
                ]
            ),
        ),
        (
            "Invent&aacute;rio e partilha extrajudicial",
            lista_simples(
                [
                    "Certid&atilde;o de &oacute;bito do falecido.",
                    "Documentos de identidade, CPF e certid&otilde;es de estado civil do falecido e dos herdeiros.",
                    "Documentos de todos os bens e direitos a partilhar.",
                    "Certid&atilde;o negativa de testamento (CENSEC).",
                    "Comprovante de recolhimento do ITCD.",
                    "Acompanhamento de advogado &mdash; exig&ecirc;ncia legal.",
                    "Todos os herdeiros devem ser maiores, capazes e estar de acordo.",
                ]
            ),
        ),
        (
            "Div&oacute;rcio e separa&ccedil;&atilde;o extrajudicial",
            lista_simples(
                [
                    "Certid&atilde;o de casamento atualizada.",
                    "Documentos de identidade e CPF de ambos os c&ocirc;njuges.",
                    "Pacto antenupcial, se houver.",
                    "Rela&ccedil;&atilde;o dos bens e defini&ccedil;&atilde;o da partilha.",
                    "Acompanhamento de advogado &mdash; exig&ecirc;ncia legal.",
                    "O casal n&atilde;o pode ter filhos menores ou incapazes.",
                ]
            ),
        ),
        (
            "Uni&atilde;o est&aacute;vel",
            lista_simples(
                [
                    "Documentos de identidade e CPF de ambos os companheiros.",
                    "Certid&atilde;o de nascimento ou de casamento com averba&ccedil;&atilde;o do div&oacute;rcio.",
                    "Defini&ccedil;&atilde;o do regime de bens a ser adotado.",
                ]
            ),
        ),
        (
            "Autoriza&ccedil;&atilde;o de viagem para menor",
            lista_simples(
                [
                    "Certid&atilde;o de nascimento ou documento de identidade do menor.",
                    "Documentos de identidade e CPF dos pais ou respons&aacute;veis.",
                    "Comparecimento de quem autoriza, ou firma reconhecida por autenticidade.",
                    "Dados do acompanhante e do destino da viagem.",
                ]
            ),
        ),
        (
            "Testamento",
            lista_simples(
                [
                    "Documento de identidade e CPF do testador, com comparecimento pessoal.",
                    "Rela&ccedil;&atilde;o dos bens e das disposi&ccedil;&otilde;es desejadas.",
                    "Duas testemunhas maiores e capazes, que n&atilde;o sejam benefici&aacute;rias do testamento.",
                ]
            ),
        ),
        (
            "Emancipa&ccedil;&atilde;o",
            lista_simples(
                [
                    "Certid&atilde;o de nascimento do menor, que deve ter 16 anos completos.",
                    "Documentos de identidade e CPF dos pais.",
                    "Comparecimento de ambos os pais e do menor.",
                ]
            ),
        ),
    ],
    extra="""
    <section class="secao" aria-labelledby="titulo-enotariado">
      <h2 class="secao__titulo" id="titulo-enotariado">Atos eletr&ocirc;nicos e e-Notariado</h2>
      <div class="painel">
        <p>
          Parte dos atos notariais pode ser praticada de forma eletr&ocirc;nica, por
          videoconfer&ecirc;ncia, pela plataforma e-Notariado, mantida pelo Col&eacute;gio Notarial
          do Brasil. Para isso &eacute; necess&aacute;rio possuir certificado digital notarizado,
          que tamb&eacute;m &eacute; emitido nesta serventia.
        </p>
        <p class="sem-margem">
          <a class="botao botao--secundario" href="https://www.e-notariado.org.br/"
             rel="external noopener" target="_blank">Acessar o e-Notariado</a>
        </p>
      </div>
    </section>
""",
)

# --- Protesto -------------------------------------------------------------

corpo_protesto = corpo_atribuicao(
    "Tabelionato de Protesto de T&iacute;tulos",
    "Protesto, pagamento, cancelamento e certid&otilde;es relativas a t&iacute;tulos e documentos "
    "de d&iacute;vida.",
    "O protesto &eacute; o ato formal que comprova o n&atilde;o pagamento de um t&iacute;tulo ou de outro "
    "documento de d&iacute;vida, servindo tanto como prova quanto como meio de cobran&ccedil;a.",
    [
        "Apresenta&ccedil;&atilde;o de t&iacute;tulos para protesto",
        "Pagamento de t&iacute;tulo protestado",
        "Cancelamento de protesto",
        "Certid&atilde;o positiva ou negativa de protesto",
        "Desist&ecirc;ncia e susta&ccedil;&atilde;o de protesto",
        "Anu&ecirc;ncia eletr&ocirc;nica",
    ],
    [
        (
            "Pagar um t&iacute;tulo protestado",
            lista_simples(
                [
                    "Documento de identidade do devedor ou de quem efetua o pagamento.",
                    "N&uacute;mero do protocolo constante na intima&ccedil;&atilde;o recebida.",
                    "Pagamento do valor do t&iacute;tulo acrescido dos emolumentos e demais despesas.",
                    "O pagamento dentro do prazo da intima&ccedil;&atilde;o evita a lavratura do protesto.",
                ]
            ),
        ),
        (
            "Cancelar um protesto j&aacute; lavrado",
            lista_simples(
                [
                    "T&iacute;tulo original quitado, ou carta de anu&ecirc;ncia do credor com firma reconhecida.",
                    "Documento de identidade de quem solicita o cancelamento.",
                    "Pagamento dos emolumentos de cancelamento.",
                ]
            ),
        ),
        (
            "Certid&atilde;o de protesto",
            lista_simples(
                [
                    "Nome completo e CPF ou CNPJ do pesquisado.",
                    "Documento de identidade do solicitante.",
                    "A certid&atilde;o pode ser positiva (com protestos) ou negativa (sem protestos).",
                ]
            ),
        ),
    ],
)

# --- Registro de Imóveis --------------------------------------------------

corpo_imoveis = corpo_atribuicao(
    "Registro de Im&oacute;veis",
    "Registro e averba&ccedil;&atilde;o de atos relativos a im&oacute;veis e emiss&atilde;o de certid&otilde;es de "
    "matr&iacute;cula.",
    "O Registro de Im&oacute;veis d&aacute; publicidade e seguran&ccedil;a jur&iacute;dica &agrave; propriedade "
    "imobili&aacute;ria. &Eacute; o registro, e n&atilde;o a escritura, que transfere a propriedade do im&oacute;vel.",
    [
        "Registro de escritura de compra e venda",
        "Registro de hipoteca e aliena&ccedil;&atilde;o fiduci&aacute;ria",
        "Averba&ccedil;&atilde;o de constru&ccedil;&atilde;o e demoli&ccedil;&atilde;o",
        "Averba&ccedil;&atilde;o de casamento, div&oacute;rcio e &oacute;bito",
        "Retifica&ccedil;&atilde;o de &aacute;rea",
        "Usucapi&atilde;o extrajudicial",
        "Adjudica&ccedil;&atilde;o compuls&oacute;ria extrajudicial",
        "Certid&atilde;o de matr&iacute;cula (inteiro teor)",
        "Certid&atilde;o de &ocirc;nus reais",
        "Certid&atilde;o negativa de propriedade",
        "Registro de loteamento e incorpora&ccedil;&atilde;o",
    ],
    [
        (
            "Certid&atilde;o de matr&iacute;cula",
            lista_simples(
                [
                    "N&uacute;mero da matr&iacute;cula do im&oacute;vel, quando conhecido.",
                    "Na falta do n&uacute;mero, endere&ccedil;o completo do im&oacute;vel e nome do propriet&aacute;rio.",
                    "Documento de identidade do solicitante.",
                ]
            ),
        ),
        (
            "Registro de escritura de compra e venda",
            lista_simples(
                [
                    "Via original da escritura p&uacute;blica ou do contrato registr&aacute;vel.",
                    "Comprovante de recolhimento do ITBI.",
                    "Documentos de identidade e CPF das partes.",
                    "Pagamento dos emolumentos conforme o valor do im&oacute;vel.",
                ]
            ),
        ),
        (
            "Averba&ccedil;&atilde;o de constru&ccedil;&atilde;o",
            lista_simples(
                [
                    "Certid&atilde;o de matr&iacute;cula atualizada do im&oacute;vel.",
                    "Habite-se ou certid&atilde;o equivalente emitida pela Prefeitura.",
                    "Certid&atilde;o negativa de d&eacute;bitos da obra (CND da obra), quando exigida.",
                    "Documentos de identidade e CPF do propriet&aacute;rio.",
                ]
            ),
        ),
    ],
)

# --- RTD ------------------------------------------------------------------

corpo_rtd = corpo_atribuicao(
    "Registro de T&iacute;tulos e Documentos",
    "Registro de contratos e documentos para conserva&ccedil;&atilde;o e efeitos perante terceiros, "
    "al&eacute;m de notifica&ccedil;&otilde;es extrajudiciais.",
    "O Registro de T&iacute;tulos e Documentos conserva documentos e d&aacute; a eles efeito contra "
    "terceiros, servindo tamb&eacute;m para notificar formalmente uma pessoa ou empresa.",
    [
        "Registro de contratos em geral",
        "Registro de documentos para conserva&ccedil;&atilde;o",
        "Notifica&ccedil;&atilde;o extrajudicial",
        "Registro de documentos estrangeiros traduzidos",
        "Certid&otilde;es de documentos registrados",
    ],
    [
        (
            "Notifica&ccedil;&atilde;o extrajudicial",
            lista_simples(
                [
                    "Texto da notifica&ccedil;&atilde;o, assinado pelo notificante.",
                    "Nome completo e endere&ccedil;o exato do notificado.",
                    "Documento de identidade e CPF ou CNPJ do notificante.",
                    "Pagamento dos emolumentos e das despesas de entrega.",
                ]
            ),
        ),
        (
            "Registro de contrato",
            lista_simples(
                [
                    "Via original do contrato, assinada por todas as partes.",
                    "Documento de identidade do apresentante.",
                    "Assinatura de duas testemunhas, quando o documento exigir.",
                ]
            ),
        ),
    ],
)

# --- RCPJ -----------------------------------------------------------------

corpo_rcpj = corpo_atribuicao(
    "Registro Civil de Pessoas Jur&iacute;dicas",
    "Constitui&ccedil;&atilde;o e altera&ccedil;&atilde;o de associa&ccedil;&otilde;es, funda&ccedil;&otilde;es, sociedades simples e "
    "organiza&ccedil;&otilde;es religiosas.",
    "O Registro Civil de Pessoas Jur&iacute;dicas d&aacute; personalidade jur&iacute;dica a entidades sem "
    "fins lucrativos e a sociedades simples, al&eacute;m de registrar jornais e editoras.",
    [
        "Registro de associa&ccedil;&otilde;es e ONGs",
        "Registro de funda&ccedil;&otilde;es",
        "Registro de sociedades simples",
        "Registro de organiza&ccedil;&otilde;es religiosas",
        "Registro de atas e altera&ccedil;&otilde;es estatut&aacute;rias",
        "Registro de jornais, revistas e editoras",
        "Certid&otilde;es de entidades registradas",
    ],
    [
        (
            "Constitui&ccedil;&atilde;o de associa&ccedil;&atilde;o",
            lista_simples(
                [
                    "Ata da assembleia de funda&ccedil;&atilde;o, com lista de presen&ccedil;a assinada.",
                    "Estatuto social assinado pelo presidente e pelos fundadores.",
                    "Documentos de identidade e CPF dos membros da diretoria eleita.",
                    "Visto de advogado com n&uacute;mero da OAB nos documentos.",
                ]
            ),
        ),
        (
            "Altera&ccedil;&atilde;o de estatuto ou de diretoria",
            lista_simples(
                [
                    "Ata da assembleia que aprovou a altera&ccedil;&atilde;o.",
                    "Estatuto consolidado, quando houver mudan&ccedil;a no texto.",
                    "Documentos de identidade e CPF da nova diretoria.",
                    "Visto de advogado com n&uacute;mero da OAB.",
                ]
            ),
        ),
    ],
    extra="""
    <section class="secao" aria-label="Aviso sobre empresas">
      <div class="aviso">
        <p class="aviso__titulo">Aten&ccedil;&atilde;o</p>
        <p class="sem-margem">
          Empresas com finalidade lucrativa &mdash; LTDA, sociedade an&ocirc;nima, empres&aacute;rio
          individual e MEI &mdash; s&atilde;o registradas na <strong>Junta Comercial do Estado do
          Cear&aacute; (JUCEC)</strong>, e n&atilde;o nesta serventia.
        </p>
      </div>
    </section>
""",
)


# ===========================================================================
# 5. Certidões
# ===========================================================================

corpo_certidoes = """{topo}

  <main class="container conteudo" id="conteudo">
    <section class="secao" aria-label="Aviso">
{aviso}
    </section>

    <section class="secao" aria-labelledby="titulo-portais">
      <h2 class="secao__titulo" id="titulo-portais">Portais oficiais para pedidos on-line</h2>
      <p class="secao__intro">
        Os servi&ccedil;os extrajudiciais mant&ecirc;m plataformas nacionais para solicita&ccedil;&atilde;o de
        certid&otilde;es pela internet. Os links abaixo levam aos portais oficiais de cada
        especialidade.
      </p>
      <div class="painel">
        <ul class="lista-links">
          <li>
            <a href="{p_enotariado}" rel="external noopener" target="_blank">
              e-Notariado &mdash; portal nacional de Notas
              <span>Plataforma do Col&eacute;gio Notarial do Brasil. Atos por videoconfer&ecirc;ncia, certificado digital notarizado e certid&otilde;es de escrituras e procura&ccedil;&otilde;es.</span>
            </a>
          </li>
          <li>
            <a href="{p_ri}" rel="external noopener" target="_blank">
              Registro de Im&oacute;veis do Brasil &mdash; portal nacional do RI
              <span>Todos os servi&ccedil;os eletr&ocirc;nicos do Registro de Im&oacute;veis reunidos: certid&atilde;o de matr&iacute;cula, &ocirc;nus reais, pesquisa de bens e protocolo eletr&ocirc;nico.</span>
            </a>
          </li>
          <li>
            <a href="{p_mapa}" rel="external noopener" target="_blank">
              Mapa ONR &mdash; consulta territorial de im&oacute;veis
              <span>Visualiza&ccedil;&atilde;o geogr&aacute;fica de im&oacute;veis registrados, mantida pelo Operador Nacional do Registro de Im&oacute;veis.</span>
            </a>
          </li>
          <li>
            <a href="{p_cenprot}" rel="external noopener" target="_blank">
              CENPROT &mdash; consulta e certid&otilde;es de protesto
              <span>Central Nacional de Protesto. Consulta de protestos em &acirc;mbito nacional e emiss&atilde;o de certid&otilde;es.</span>
            </a>
          </li>
          <li>
            <a href="{p_censec}" rel="external noopener" target="_blank">
              CENSEC &mdash; busca de testamentos e escrituras
              <span>Central Nacional de Servi&ccedil;os Eletr&ocirc;nicos Compartilhados. Emite a certid&atilde;o de exist&ecirc;ncia de testamento exigida em invent&aacute;rios.</span>
            </a>
          </li>
          <li>
            <a href="{p_rcpn}" rel="external noopener" target="_blank">
              Registro Civil &mdash; nascimento, casamento e &oacute;bito
              <span>Portal do Registro Civil. Certid&otilde;es de qualquer cart&oacute;rio do pa&iacute;s &mdash; atribui&ccedil;&atilde;o que esta serventia n&atilde;o possui.</span>
            </a>
          </li>
        </ul>
      </div>
    </section>

    <section class="secao" aria-labelledby="titulo-selo">
      <h2 class="secao__titulo" id="titulo-selo">Conferir a autenticidade de um documento</h2>
      <p class="secao__intro">
        Todo ato praticado por esta serventia recebe um selo digital, que permite
        confirmar sua autenticidade no site do Tribunal de Justi&ccedil;a do Cear&aacute;.
      </p>
      <p class="sem-margem">
        <a class="botao botao--secundario" href="selo-digital.html">Como consultar o selo digital</a>
      </p>
    </section>

    <section class="secao" aria-labelledby="titulo-balcao">
      <h2 class="secao__titulo" id="titulo-balcao">Certid&otilde;es emitidas por esta serventia</h2>
      <p class="secao__intro">
        As certid&otilde;es abaixo podem ser solicitadas diretamente no balc&atilde;o do cart&oacute;rio.
      </p>
      <ul class="lista-servicos">
        <li>Certid&atilde;o de matr&iacute;cula de im&oacute;vel (inteiro teor)</li>
        <li>Certid&atilde;o de &ocirc;nus reais</li>
        <li>Certid&atilde;o negativa de propriedade</li>
        <li>Certid&atilde;o positiva ou negativa de protesto</li>
        <li>Certid&atilde;o de escritura lavrada nesta serventia</li>
        <li>Certid&atilde;o de documento registrado em T&iacute;tulos e Documentos</li>
        <li>Certid&atilde;o de entidade registrada em Pessoas Jur&iacute;dicas</li>
      </ul>
    </section>

    <section class="secao" aria-label="Solicitar certid&atilde;o">
{bloco}
    </section>
  </main>""".format(
    topo=topo_pagina(
        "Certid&otilde;es",
        "Onde solicitar cada tipo de certid&atilde;o, nos portais oficiais ou diretamente "
        "nesta serventia.",
        [("index.html", "In&iacute;cio"), (None, "Certid&otilde;es")],
    ),
    p_enotariado=PORTAL_ENOTARIADO,
    p_ri=PORTAL_RI,
    p_mapa=PORTAL_MAPA_ONR,
    p_cenprot=PORTAL_CENPROT,
    p_censec=PORTAL_CENSEC,
    p_rcpn=PORTAL_REGISTRO_CIVIL,
    aviso=AVISO_RCPN,
    bloco=bloco_whatsapp(
        "Solicitar uma certid&atilde;o",
        "Informe pelo WhatsApp qual certid&atilde;o voc&ecirc; precisa e os dados do registro. "
        "O atendimento retorna com o prazo e o valor.",
        "Solicitar pelo WhatsApp",
        WA_DUVIDA,
    ),
)

# ===========================================================================
# 6. Emolumentos
# ===========================================================================

corpo_emolumentos = """{topo}

  <main class="container conteudo" id="conteudo">
    <section class="secao" aria-labelledby="titulo-como">
      <h2 class="secao__titulo" id="titulo-como">Como os valores s&atilde;o definidos</h2>
      <div class="prosa">
        <p>
          Emolumentos s&atilde;o os valores cobrados pelos servi&ccedil;os notariais e de registro.
          Eles <strong>n&atilde;o s&atilde;o fixados pelo cart&oacute;rio</strong>: decorrem de lei estadual e
          s&atilde;o divulgados anualmente pelo Tribunal de Justi&ccedil;a do Cear&aacute;.
        </p>
        <p>
          Parte do valor pago n&atilde;o fica com a serventia &mdash; &eacute; destinada ao Estado e aos
          fundos previstos em lei. A tabela &eacute; p&uacute;blica e pode ser consultada por qualquer
          pessoa.
        </p>
      </div>
      <p>
        <a class="botao botao--principal" href="https://www.tjce.jus.br/"
           rel="external noopener" target="_blank">Consultar a tabela do TJCE</a>
      </p>
      <p class="nota">
        Substituir o endere&ccedil;o acima pelo link direto da tabela vigente publicada pelo
        Tribunal de Justi&ccedil;a do Cear&aacute;, e revisar o link no in&iacute;cio de cada ano.
      </p>
    </section>

    <section class="secao" aria-labelledby="titulo-gratuidade">
      <h2 class="secao__titulo" id="titulo-gratuidade">Atos gratuitos</h2>
      <div class="painel">
        <p class="sem-margem">
          A legisla&ccedil;&atilde;o prev&ecirc; gratuidade para determinados atos e para pessoas
          reconhecidamente pobres, mediante declara&ccedil;&atilde;o. Procure o atendimento para
          verificar se o seu caso se enquadra.
        </p>
      </div>
    </section>

    <section class="secao" aria-label="D&uacute;vidas sobre valores">
{bloco}
    </section>
  </main>""".format(
    topo=topo_pagina(
        "Emolumentos",
        "Os valores dos servi&ccedil;os s&atilde;o fixados por lei estadual e divulgados pelo "
        "Tribunal de Justi&ccedil;a do Cear&aacute;.",
        [("index.html", "In&iacute;cio"), (None, "Emolumentos")],
    ),
    bloco=bloco_whatsapp(
        "Quer saber o valor de um servi&ccedil;o espec&iacute;fico?",
        "Descreva o ato que voc&ecirc; precisa e o atendimento informa o valor conforme a "
        "tabela vigente.",
        "Consultar valor",
        WA_DUVIDA,
    ),
)

# ===========================================================================
# 7. Modelos e requerimentos
# ===========================================================================

corpo_modelos = """{topo}

  <main class="container conteudo" id="conteudo">
    <section class="secao" aria-labelledby="titulo-arquivos">
      <h2 class="secao__titulo" id="titulo-arquivos">Arquivos para download</h2>
      <p class="secao__intro">
        Baixe, preencha e traga o formul&aacute;rio impresso. Isso reduz o tempo de atendimento
        no balc&atilde;o.
      </p>
      <div class="painel">
        <ul class="lista-links">
          <li>
            <a href="arquivos/requerimento-certidao.pdf" download>
              Requerimento de certid&atilde;o
              <span>PDF &middot; preencher e assinar</span>
            </a>
          </li>
          <li>
            <a href="arquivos/declaracao-pobreza.pdf" download>
              Declara&ccedil;&atilde;o de hipossufici&ecirc;ncia
              <span>PDF &middot; para solicita&ccedil;&atilde;o de gratuidade</span>
            </a>
          </li>
          <li>
            <a href="arquivos/requerimento-cancelamento-protesto.pdf" download>
              Requerimento de cancelamento de protesto
              <span>PDF &middot; acompanhar de t&iacute;tulo quitado ou carta de anu&ecirc;ncia</span>
            </a>
          </li>
          <li>
            <a href="arquivos/carta-anuencia.pdf" download>
              Modelo de carta de anu&ecirc;ncia
              <span>PDF &middot; assinatura do credor com firma reconhecida</span>
            </a>
          </li>
          <li>
            <a href="arquivos/autorizacao-viagem-menor.pdf" download>
              Autoriza&ccedil;&atilde;o de viagem para menor
              <span>PDF &middot; modelo para preenchimento</span>
            </a>
          </li>
        </ul>
      </div>
      <p class="nota">
        Os arquivos devem ser colocados na pasta <code>arquivos/</code>. Enquanto os PDFs
        n&atilde;o forem enviados pelo cart&oacute;rio, os links desta p&aacute;gina n&atilde;o funcionar&atilde;o &mdash;
        ajustar a lista para conter apenas os modelos que existirem de fato.
      </p>
    </section>

    <section class="secao" aria-label="Ajuda com formul&aacute;rios">
{bloco}
    </section>
  </main>""".format(
    topo=topo_pagina(
        "Modelos e requerimentos",
        "Formul&aacute;rios e declara&ccedil;&otilde;es para preencher antes de vir ao cart&oacute;rio.",
        [("index.html", "In&iacute;cio"), (None, "Modelos e requerimentos")],
    ),
    bloco=bloco_whatsapp(
        "Ficou em d&uacute;vida no preenchimento?",
        "Fale com o atendimento antes de assinar. Formul&aacute;rio preenchido de forma "
        "incorreta precisa ser refeito.",
        "Tirar d&uacute;vida",
        WA_DUVIDA,
    ),
)

# ===========================================================================
# 8. Dúvidas frequentes
# ===========================================================================

faq = [
    (
        "Vocês emitem certidão de nascimento, casamento ou óbito?",
        """            <p>
              N&atilde;o. Esta serventia n&atilde;o possui a atribui&ccedil;&atilde;o de Registro Civil das Pessoas
              Naturais. Essas certid&otilde;es devem ser solicitadas no cart&oacute;rio de registro civil
              onde o ato foi lavrado, ou pela internet, no
              <a href="https://www.registrocivil.org.br/" rel="external noopener" target="_blank">Portal do Registro Civil</a>.
            </p>""",
    ),
    (
        "Como consulto o andamento do meu pedido?",
        """            <p>
              Envie o n&uacute;mero do protocolo pelo WhatsApp do cart&oacute;rio. O atendimento
              retorna com a situa&ccedil;&atilde;o do pedido.
            </p>
            <p class="sem-margem">
              <a class="botao botao--secundario" href="{wa}" rel="noopener" target="_blank">Consultar pelo WhatsApp</a>
            </p>""".format(
            wa=WA_PEDIDO
        ),
    ),
    (
        "O que é abertura de firma e por que preciso fazer isso?",
        """            <p>
              A abertura de firma &eacute; o cadastro da sua assinatura no cart&oacute;rio, feito uma
              &uacute;nica vez, com comparecimento pessoal e documento de identidade original.
              Sem esse cadastro pr&eacute;vio n&atilde;o &eacute; poss&iacute;vel reconhecer firma por semelhan&ccedil;a.
            </p>
            <p class="sem-margem">
              O cart&oacute;rio s&oacute; reconhece firmas de assinaturas cadastradas nesta serventia.
            </p>""",
    ),
    (
        "Quanto custa cada serviço?",
        """            <p class="sem-margem">
              Os valores s&atilde;o fixados por lei estadual e divulgados pelo Tribunal de
              Justi&ccedil;a do Cear&aacute;. Consulte a p&aacute;gina de
              <a href="emolumentos.html">emolumentos</a> ou fale com o atendimento.
            </p>""",
    ),
    (
        "Preciso agendar atendimento?",
        """            <p class="sem-margem">[CONFIRMAR COM O CART&Oacute;RIO: o atendimento &eacute; por ordem de
            chegada ou h&aacute; agendamento? Para quais servi&ccedil;os?]</p>""",
    ),
    (
        "Quais formas de pagamento são aceitas?",
        """            <p class="sem-margem">[CONFIRMAR COM O CART&Oacute;RIO: dinheiro, PIX, cart&atilde;o de
            d&eacute;bito, cart&atilde;o de cr&eacute;dito?]</p>""",
    ),
    (
        "Posso resolver algum ato sem ir ao cartório?",
        """            <p class="sem-margem">
              Sim. Parte dos atos notariais pode ser praticada por videoconfer&ecirc;ncia pela
              plataforma
              <a href="https://www.e-notariado.org.br/" rel="external noopener" target="_blank">e-Notariado</a>,
              desde que o interessado possua certificado digital notarizado &mdash; que
              tamb&eacute;m &eacute; emitido nesta serventia.
            </p>""",
    ),
    (
        "Como faço para abrir uma empresa?",
        """            <p class="sem-margem">
              Empresas com finalidade lucrativa (LTDA, sociedade an&ocirc;nima, empres&aacute;rio
              individual e MEI) s&atilde;o registradas na Junta Comercial do Estado do Cear&aacute;.
              Aqui s&atilde;o registradas associa&ccedil;&otilde;es, funda&ccedil;&otilde;es, organiza&ccedil;&otilde;es religiosas e
              sociedades simples &mdash; veja
              <a href="servicos-pessoas-juridicas.html">Registro Civil de Pessoas Jur&iacute;dicas</a>.
            </p>""",
    ),
    (
        "Perdi minha escritura. Como consigo outra via?",
        """            <p class="sem-margem">
              A escritura fica arquivada em livro pr&oacute;prio no cart&oacute;rio onde foi lavrada.
              Basta solicitar uma certid&atilde;o do ato, apresentando documento de identidade e
              os dados do neg&oacute;cio. Se a escritura foi lavrada aqui, fale com o atendimento.
            </p>""",
    ),
    (
        "Recebi uma intimação de protesto. O que devo fazer?",
        """            <p class="sem-margem">
              Procure o cart&oacute;rio dentro do prazo indicado na intima&ccedil;&atilde;o. O pagamento nesse
              prazo evita que o protesto seja lavrado. Se a cobran&ccedil;a for indevida, informe
              o atendimento e procure orienta&ccedil;&atilde;o jur&iacute;dica &mdash; veja
              <a href="servicos-protesto.html">Tabelionato de Protesto</a>.
            </p>""",
    ),
]

corpo_duvidas = """{topo}

  <main class="container conteudo" id="conteudo">
    <section class="secao" aria-labelledby="titulo-faq">
      <h2 class="apenas-leitor" id="titulo-faq">Perguntas e respostas</h2>
{blocos}
    </section>

    <section class="secao" aria-label="Outras d&uacute;vidas">
{bloco}
    </section>
  </main>""".format(
    topo=topo_pagina(
        "D&uacute;vidas frequentes",
        "As perguntas que mais chegam ao atendimento do cart&oacute;rio.",
        [("index.html", "In&iacute;cio"), (None, "D&uacute;vidas frequentes")],
    ),
    blocos="\n".join(acordeao(p, r) for p, r in faq),
    bloco=bloco_whatsapp(
        "N&atilde;o encontrou sua d&uacute;vida?",
        "Envie sua pergunta pelo WhatsApp. O atendimento responde em hor&aacute;rio comercial.",
        "Perguntar no WhatsApp",
        WA_DUVIDA,
    ),
)

# ===========================================================================
# 9. Ouvidoria
# ===========================================================================

corpo_ouvidoria = """{topo}

  <main class="container conteudo" id="conteudo">
    <section class="secao" aria-labelledby="titulo-canal">
      <h2 class="secao__titulo" id="titulo-canal">Fale com a ouvidoria</h2>
      <div class="prosa">
        <p>
          A ouvidoria recebe elogios, sugest&otilde;es, reclama&ccedil;&otilde;es e den&uacute;ncias sobre o
          atendimento e os servi&ccedil;os prestados por esta serventia. As manifesta&ccedil;&otilde;es s&atilde;o
          analisadas e respondidas.
        </p>
      </div>
      <div class="painel painel--destaque">
        <dl class="dados">
          <dt>Respons&aacute;vel</dt>
          <dd>[NOME DO RESPONS&Aacute;VEL PELA OUVIDORIA]</dd>
          <dt>E-mail</dt>
          <dd><a href="mailto:{email}">{email}</a></dd>
          <dt>Telefone</dt>
          <dd><a href="tel:{tel_link}">{telefone}</a></dd>
          <dt>Presencialmente</dt>
          <dd>{endereco} &middot; {cidade}</dd>
          <dt>Hor&aacute;rio</dt>
          <dd>{horario}</dd>
        </dl>
      </div>
    </section>

    <section class="secao" aria-labelledby="titulo-corregedoria">
      <h2 class="secao__titulo" id="titulo-corregedoria">Corregedoria-Geral de Justi&ccedil;a</h2>
      <div class="prosa">
        <p>
          Os servi&ccedil;os notariais e de registro s&atilde;o fiscalizados pelo Poder Judici&aacute;rio.
          Caso a manifesta&ccedil;&atilde;o n&atilde;o seja resolvida pela ouvidoria da serventia, ela pode
          ser dirigida diretamente &agrave; Corregedoria-Geral de Justi&ccedil;a do Estado do Cear&aacute;.
        </p>
      </div>
      <p class="sem-margem">
        <a class="botao botao--secundario" href="https://www.tjce.jus.br/"
           rel="external noopener" target="_blank">Tribunal de Justi&ccedil;a do Cear&aacute;</a>
      </p>
    </section>
  </main>""".format(
    topo=topo_pagina(
        "Ouvidoria",
        "Canal para elogios, sugest&otilde;es, reclama&ccedil;&otilde;es e den&uacute;ncias sobre os servi&ccedil;os "
        "da serventia.",
        [("index.html", "In&iacute;cio"), (None, "Ouvidoria")],
    ),
    email=EMAIL,
    tel_link=TELEFONE_LINK,
    telefone=TELEFONE,
    endereco=ENDERECO,
    cidade=CIDADE,
    horario=HORARIO_CURTO,
)

# ===========================================================================
# 10. Contato
# ===========================================================================

corpo_contato = """{topo}

  <main class="container conteudo" id="conteudo">
    <section class="secao" aria-labelledby="titulo-contato">
      <h2 class="apenas-leitor" id="titulo-contato">Contato e localiza&ccedil;&atilde;o</h2>
      <div class="contato-grade">
        <div>
          <div class="painel painel--destaque">
            <h3 class="cartao__titulo">{nome_curto}</h3>
            <address>
              {endereco}<br />
              {cidade}<br />
              CEP {cep}
            </address>
            <dl class="dados">
              <dt>Telefone</dt>
              <dd><a href="tel:{tel_link}">{telefone}</a></dd>
              <dt>WhatsApp</dt>
              <dd><a href="{wa}" rel="noopener" target="_blank">{whatsapp}</a></dd>
              <dt>E-mail</dt>
              <dd><a href="mailto:{email}">{email}</a></dd>
              <dt>Instagram</dt>
              <dd><a href="{instagram_url}" rel="external noopener" target="_blank">{instagram}</a></dd>
            </dl>
            <div class="botoes">
              <a class="botao botao--principal" href="{wa}" rel="noopener" target="_blank">Falar no WhatsApp</a>
              <a class="botao botao--secundario" href="mailto:{email}">Enviar e-mail</a>
            </div>
          </div>

          <h3 class="secao__titulo espaco-acima">Hor&aacute;rio de atendimento</h3>
          <table class="horarios">
            <caption>Atendimento ao p&uacute;blico na sede da serventia.</caption>
            <tbody>
              <tr><th scope="row">Segunda a sexta</th><td>[08h &agrave;s 17h]</td></tr>
              <tr><th scope="row">S&aacute;bado</th><td>[Fechado]</td></tr>
              <tr><th scope="row">Domingo e feriados</th><td>Fechado</td></tr>
            </tbody>
          </table>
          <p class="nota">
            Em v&eacute;speras de feriado e em recessos o hor&aacute;rio pode ser reduzido. Confirme
            pelo telefone antes de se deslocar.
          </p>
        </div>

        <div class="mapa">
          <iframe
            src="https://www.google.com/maps?q=Guaraciaba%20do%20Norte%2C%20CE&amp;output=embed"
            title="Mapa com a localiza&ccedil;&atilde;o do cart&oacute;rio"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
      </div>
    </section>
  </main>""".format(
    topo=topo_pagina(
        "Contato e localiza&ccedil;&atilde;o",
        "Endere&ccedil;o, telefones, e-mail e hor&aacute;rio de atendimento da serventia.",
        [("index.html", "In&iacute;cio"), (None, "Contato")],
    ),
    nome_curto=NOME_CURTO,
    endereco=ENDERECO,
    cidade=CIDADE,
    cep=CEP,
    tel_link=TELEFONE_LINK,
    telefone=TELEFONE,
    wa=WA_DUVIDA,
    whatsapp=WHATSAPP,
    email=EMAIL,
    instagram=INSTAGRAM_USUARIO,
    instagram_url=INSTAGRAM_URL,
)


# ===========================================================================
# 11. Selo digital
# ===========================================================================

corpo_selo = """{topo}

  <main class="container conteudo" id="conteudo">
    <section class="secao" aria-labelledby="titulo-oque">
      <h2 class="secao__titulo" id="titulo-oque">O que &eacute; o selo digital</h2>
      <div class="prosa">
        <p>
          O selo digital &eacute; o c&oacute;digo impresso em todo ato praticado pelas serventias
          extrajudiciais do Cear&aacute;. Ele identifica o ato de forma &uacute;nica e permite que
          qualquer pessoa confirme, pela internet, que o documento foi realmente
          expedido por este cart&oacute;rio e n&atilde;o sofreu altera&ccedil;&atilde;o.
        </p>
        <p>
          A confer&ecirc;ncia &eacute; gratuita e pode ser feita por quem recebe o documento &mdash;
          banco, &oacute;rg&atilde;o p&uacute;blico, empresa ou pessoa f&iacute;sica.
        </p>
      </div>
      <p>
        <a class="botao botao--principal" href="{selo_url}" rel="external noopener" target="_blank">
          Consultar selo digital no TJCE
        </a>
      </p>
      <p class="nota">
        Substituir o endere&ccedil;o acima pelo link direto da consulta de selo digital do
        Tribunal de Justi&ccedil;a do Cear&aacute;.
      </p>
    </section>

    <section class="secao" aria-labelledby="titulo-como">
      <h2 class="secao__titulo" id="titulo-como">Como consultar</h2>
      <ol class="prosa">
        <li>Localize o selo digital no documento &mdash; em geral no rodap&eacute; ou no verso, com um c&oacute;digo alfanum&eacute;rico.</li>
        <li>Acesse a p&aacute;gina de consulta do Tribunal de Justi&ccedil;a do Cear&aacute;.</li>
        <li>Informe o c&oacute;digo do selo e, quando solicitado, o c&oacute;digo de seguran&ccedil;a que aparece na tela.</li>
        <li>Confira se os dados exibidos &mdash; serventia, tipo de ato e data &mdash; coincidem com o documento em m&atilde;os.</li>
      </ol>
      <div class="aviso">
        <p class="aviso__titulo">Se os dados n&atilde;o conferirem</p>
        <p class="sem-margem">
          Entre em contato imediatamente com esta serventia. Diverg&ecirc;ncia entre o
          documento e a consulta pode indicar falsifica&ccedil;&atilde;o.
        </p>
      </div>
    </section>

    <section class="secao" aria-label="Contato">
{bloco}
    </section>
  </main>""".format(
    topo=topo_pagina(
        "Selo Digital",
        "Confira a autenticidade de um documento expedido por esta serventia.",
        [("index.html", "In&iacute;cio"), (None, "Selo Digital")],
    ),
    selo_url=SELO_URL,
    bloco=bloco_whatsapp(
        "D&uacute;vida sobre um documento?",
        "Envie uma foto do documento pelo WhatsApp que o atendimento confirma a "
        "origem do ato.",
        "Falar no WhatsApp",
        WA_DUVIDA,
    ),
)

# ===========================================================================
# 12. Transparência
# ===========================================================================

corpo_transparencia = """{topo}

  <main class="container conteudo" id="conteudo">
    <section class="secao" aria-labelledby="titulo-identificacao">
      <h2 class="secao__titulo" id="titulo-identificacao">Identifica&ccedil;&atilde;o da serventia</h2>
      <div class="painel">
        <dl class="dados">
          <dt>Denomina&ccedil;&atilde;o oficial</dt>
          <dd>{nome_oficial}</dd>
          <dt>Titular</dt>
          <dd>{titular}</dd>
          <dt>C&oacute;digo Nacional da Serventia (CNS)</dt>
          <dd>{cns}</dd>
          <dt>Comarca</dt>
          <dd>Guaraciaba do Norte &ndash; Cear&aacute;</dd>
          <dt>Atribui&ccedil;&otilde;es</dt>
          <dd>
            Tabelionato de Notas &middot; Tabelionato de Protesto de T&iacute;tulos &middot;
            Registro de Im&oacute;veis &middot; Registro de T&iacute;tulos e Documentos &middot;
            Registro Civil de Pessoas Jur&iacute;dicas
          </dd>
          <dt>Endere&ccedil;o</dt>
          <dd>{endereco} &middot; {cidade} &middot; CEP {cep}</dd>
          <dt>Atendimento ao p&uacute;blico</dt>
          <dd>{horario}</dd>
        </dl>
      </div>
    </section>

    <section class="secao" aria-labelledby="titulo-valores">
      <h2 class="secao__titulo" id="titulo-valores">Valores cobrados</h2>
      <div class="prosa">
        <p>
          Os emolumentos s&atilde;o fixados por lei estadual e divulgados pelo Tribunal de
          Justi&ccedil;a do Cear&aacute;. A serventia n&atilde;o define, n&atilde;o reajusta e n&atilde;o concede
          descontos sobre esses valores. Parte do que &eacute; pago &eacute; repassada ao Estado e
          aos fundos previstos em lei.
        </p>
        <p class="sem-margem">
          <a class="botao botao--secundario" href="emolumentos.html">Ver tabela de emolumentos</a>
        </p>
      </div>
    </section>

    <section class="secao" aria-labelledby="titulo-fiscalizacao">
      <h2 class="secao__titulo" id="titulo-fiscalizacao">Fiscaliza&ccedil;&atilde;o e presta&ccedil;&atilde;o de contas</h2>
      <div class="prosa">
        <p>
          Os servi&ccedil;os notariais e de registro s&atilde;o exercidos por delega&ccedil;&atilde;o do Poder
          P&uacute;blico e fiscalizados pelo Poder Judici&aacute;rio. Dados cadastrais e estat&iacute;sticos
          das serventias de todo o pa&iacute;s ficam dispon&iacute;veis no sistema Justi&ccedil;a Aberta,
          do Conselho Nacional de Justi&ccedil;a, de consulta livre.
        </p>
      </div>
      <div class="painel">
        <ul class="lista-links">
          <li>
            <a href="{justica_aberta}" rel="external noopener" target="_blank">
              Justi&ccedil;a Aberta &mdash; CNJ
              <span>Consulta p&uacute;blica de dados das serventias extrajudiciais.</span>
            </a>
          </li>
          <li>
            <a href="https://www.tjce.jus.br/" rel="external noopener" target="_blank">
              Corregedoria-Geral de Justi&ccedil;a do Cear&aacute;
              <span>&Oacute;rg&atilde;o respons&aacute;vel pela fiscaliza&ccedil;&atilde;o desta serventia.</span>
            </a>
          </li>
          <li>
            <a href="ouvidoria.html">
              Ouvidoria da serventia
              <span>Canal direto para elogios, sugest&otilde;es, reclama&ccedil;&otilde;es e den&uacute;ncias.</span>
            </a>
          </li>
        </ul>
      </div>
    </section>

    <section class="secao" aria-labelledby="titulo-gratuidades">
      <h2 class="secao__titulo" id="titulo-gratuidades">Gratuidades</h2>
      <div class="aviso">
        <p class="sem-margem">
          A legisla&ccedil;&atilde;o assegura gratuidade em determinados atos e para pessoas
          reconhecidamente pobres, mediante declara&ccedil;&atilde;o. Procure o atendimento para
          verificar se o seu caso se enquadra &mdash; a solicita&ccedil;&atilde;o n&atilde;o precisa ser
          justificada al&eacute;m da declara&ccedil;&atilde;o prevista em lei.
        </p>
      </div>
    </section>
  </main>""".format(
    topo=topo_pagina(
        "Transpar&ecirc;ncia",
        "Dados oficiais da serventia, valores cobrados e canais de fiscaliza&ccedil;&atilde;o.",
        [("index.html", "In&iacute;cio"), (None, "Transpar&ecirc;ncia")],
    ),
    nome_oficial=NOME_OFICIAL,
    titular=TITULAR,
    cns=CNS,
    endereco=ENDERECO,
    cidade=CIDADE,
    cep=CEP,
    horario=HORARIO_CURTO,
    justica_aberta=PORTAL_JUSTICA_ABERTA,
)

# ===========================================================================
# 13. Agenda 2030 / ODS
# ===========================================================================

ODS_ATUACAO = [
    (
        "ODS 16",
        "Paz, justi&ccedil;a e institui&ccedil;&otilde;es eficazes",
        "&Eacute; o objetivo mais diretamente ligado &agrave; atividade extrajudicial. Cada ato "
        "praticado com f&eacute; p&uacute;blica previne conflitos e evita que demandas cheguem ao "
        "Judici&aacute;rio.",
        [
            "Invent&aacute;rio, partilha e div&oacute;rcio extrajudiciais",
            "Usucapi&atilde;o e adjudica&ccedil;&atilde;o compuls&oacute;ria extrajudiciais",
            "Ata notarial como meio de prova",
            "Autentica&ccedil;&atilde;o de documentos e reconhecimento de firma",
        ],
    ),
    (
        "ODS 1",
        "Erradica&ccedil;&atilde;o da pobreza",
        "As gratuidades previstas em lei garantem acesso aos servi&ccedil;os a quem n&atilde;o "
        "pode arcar com os emolumentos.",
        [
            "Atos gratuitos a pessoas reconhecidamente pobres, mediante declara&ccedil;&atilde;o",
            "Orienta&ccedil;&atilde;o sobre direitos sem custo",
        ],
    ),
    (
        "ODS 10",
        "Redu&ccedil;&atilde;o das desigualdades",
        "O atendimento &eacute; universal e o mesmo para todos, independentemente da "
        "condi&ccedil;&atilde;o social de quem procura a serventia.",
        [
            "Atendimento presencial sem necessidade de intermedi&aacute;rio",
            "Orienta&ccedil;&atilde;o em linguagem acess&iacute;vel sobre cada procedimento",
        ],
    ),
    (
        "ODS 11",
        "Cidades e comunidades sustent&aacute;veis",
        "A regulariza&ccedil;&atilde;o imobili&aacute;ria d&aacute; seguran&ccedil;a jur&iacute;dica &agrave; moradia e organiza o "
        "territ&oacute;rio do munic&iacute;pio.",
        [
            "Registro de im&oacute;veis e averba&ccedil;&atilde;o de constru&ccedil;&otilde;es",
            "Usucapi&atilde;o extrajudicial e retifica&ccedil;&atilde;o de &aacute;rea",
            "Registro de loteamentos e incorpora&ccedil;&otilde;es",
        ],
    ),
    (
        "ODS 17",
        "Parcerias e meios de implementa&ccedil;&atilde;o",
        "O registro de entidades sem fins lucrativos viabiliza a atua&ccedil;&atilde;o organizada "
        "da sociedade civil.",
        [
            "Registro de associa&ccedil;&otilde;es, funda&ccedil;&otilde;es e organiza&ccedil;&otilde;es religiosas",
            "Registro de atas e altera&ccedil;&otilde;es estatut&aacute;rias",
        ],
    ),
]


def blocos_ods():
    partes = []
    for codigo, titulo, texto, itens in ODS_ATUACAO:
        partes.append(
            """          <article class="cartao">
            <span class="cartao__numero" aria-hidden="true">{codigo}</span>
            <h3 class="cartao__titulo">{titulo}</h3>
            <p>{texto}</p>
            <ul>
{itens}
            </ul>
          </article>""".format(
                codigo=codigo,
                titulo=titulo,
                texto=texto,
                itens="\n".join("              <li>%s</li>" % i for i in itens),
            )
        )
    return '        <div class="grade grade--larga">\n%s\n        </div>' % "\n".join(
        partes
    )


corpo_agenda = """{topo}

  <main class="container conteudo" id="conteudo">
    <section class="secao" aria-labelledby="titulo-oque">
      <h2 class="secao__titulo" id="titulo-oque">O que &eacute; a Agenda 2030</h2>
      <div class="prosa">
        <p>
          A Agenda 2030 &eacute; o plano de a&ccedil;&atilde;o aprovado pelos pa&iacute;ses-membros da
          Organiza&ccedil;&atilde;o das Na&ccedil;&otilde;es Unidas, formado por 17 Objetivos de Desenvolvimento
          Sustent&aacute;vel (ODS). O Conselho Nacional de Justi&ccedil;a adotou esses objetivos como
          pol&iacute;tica do Poder Judici&aacute;rio brasileiro e estendeu essa diretriz aos servi&ccedil;os
          notariais e de registro.
        </p>
        <p class="sem-margem">
          Na pr&aacute;tica, isso significa relacionar cada atividade da serventia ao objetivo
          que ela ajuda a cumprir. Abaixo est&atilde;o os objetivos em que este cart&oacute;rio atua
          diretamente.
        </p>
      </div>
    </section>

    <section class="secao" aria-labelledby="titulo-atuacao">
      <h2 class="secao__titulo" id="titulo-atuacao">Nossa atua&ccedil;&atilde;o</h2>
{blocos}
    </section>

    <section class="secao" aria-labelledby="titulo-painel">
      <h2 class="secao__titulo" id="titulo-painel">Os 17 Objetivos de Desenvolvimento Sustent&aacute;vel</h2>
      <div class="painel">
        <p>
          <img src="img/ods/ods-17-objetivos.png"
               alt="Painel com os 17 Objetivos de Desenvolvimento Sustent&aacute;vel da Agenda 2030 da ONU"
               width="1200" height="620" />
        </p>
        <p class="sem-margem">
          <a class="botao botao--secundario"
             href="https://brasil.un.org/pt-br/sdgs"
             rel="external noopener" target="_blank">Conhe&ccedil;a os 17 objetivos</a>
        </p>
      </div>
      <p class="nota">
        Baixar o painel oficial em portugu&ecirc;s no site da ONU e salvar como
        <code>img/ods/ods-17-objetivos.png</code>. Os &iacute;cones t&ecirc;m diretrizes de uso
        pr&oacute;prias &mdash; usar sempre os arquivos oficiais, nunca c&oacute;pias de outros sites.
      </p>
    </section>
  </main>""".format(
    topo=topo_pagina(
        "Agenda 2030",
        "Como os servi&ccedil;os desta serventia se relacionam com os Objetivos de "
        "Desenvolvimento Sustent&aacute;vel da ONU.",
        [("index.html", "In&iacute;cio"), (None, "Agenda 2030")],
    ),
    blocos=blocos_ods(),
)

# ===========================================================================
# 14. Aviso de Privacidade / LGPD
# ===========================================================================

corpo_privacidade = """{topo}

  <main class="container conteudo" id="conteudo">
    <section class="secao" aria-label="Aviso preliminar">
      <div class="aviso">
        <p class="aviso__titulo">Documento a revisar</p>
        <p class="sem-margem">
          Este texto &eacute; um modelo de partida. Antes de publicar, deve ser revisado pelo
          respons&aacute;vel jur&iacute;dico da serventia e ajustado &agrave;s pr&aacute;ticas reais de tratamento
          de dados do cart&oacute;rio.
        </p>
      </div>
    </section>

    <section class="secao" aria-labelledby="titulo-compromisso">
      <h2 class="secao__titulo" id="titulo-compromisso">Nosso compromisso</h2>
      <div class="prosa">
        <p>
          Esta serventia trata dados pessoais no exerc&iacute;cio da fun&ccedil;&atilde;o p&uacute;blica que lhe
          foi delegada, em conformidade com a Lei Geral de Prote&ccedil;&atilde;o de Dados Pessoais
          (Lei n&ordm; 13.709/2018) e com as normas do Conselho Nacional de Justi&ccedil;a e da
          Corregedoria-Geral de Justi&ccedil;a do Cear&aacute;.
        </p>
      </div>
    </section>

    <section class="secao" aria-labelledby="titulo-detalhes">
      <h2 class="secao__titulo" id="titulo-detalhes">Como tratamos seus dados</h2>

      <details class="acordeao">
        <summary>Quais dados s&atilde;o tratados</summary>
        <div class="acordeao__corpo">
          <ul>
            <li>Dados de identifica&ccedil;&atilde;o: nome, CPF, documento de identidade, estado civil, profiss&atilde;o e endere&ccedil;o.</li>
            <li>Dados de contato: telefone e e-mail informados no atendimento.</li>
            <li>Dados constantes dos documentos apresentados para a pr&aacute;tica dos atos.</li>
          </ul>
          <p class="sem-margem">
            Este site &eacute; institucional e n&atilde;o coleta dados de navega&ccedil;&atilde;o, n&atilde;o utiliza
            cookies de rastreamento e n&atilde;o possui formul&aacute;rios de cadastro.
          </p>
        </div>
      </details>

      <details class="acordeao">
        <summary>Com que finalidade</summary>
        <div class="acordeao__corpo">
          <p class="sem-margem">
            Exclusivamente para a pr&aacute;tica dos atos notariais e de registro solicitados,
            para a guarda e conserva&ccedil;&atilde;o dos livros e arquivos e para o cumprimento das
            obriga&ccedil;&otilde;es legais e regulamentares da serventia.
          </p>
        </div>
      </details>

      <details class="acordeao">
        <summary>Com que base legal</summary>
        <div class="acordeao__corpo">
          <p class="sem-margem">
            O tratamento decorre do cumprimento de obriga&ccedil;&atilde;o legal e regulat&oacute;ria e do
            exerc&iacute;cio regular de compet&ecirc;ncia p&uacute;blica, nos termos do artigo 7&ordm; da LGPD.
            Na maior parte dos casos, portanto, n&atilde;o depende de consentimento.
          </p>
        </div>
      </details>

      <details class="acordeao">
        <summary>Com quem os dados s&atilde;o compartilhados</summary>
        <div class="acordeao__corpo">
          <p class="sem-margem">
            Apenas nas hip&oacute;teses previstas em lei: com o Poder Judici&aacute;rio e &oacute;rg&atilde;os de
            fiscaliza&ccedil;&atilde;o, com as centrais eletr&ocirc;nicas dos servi&ccedil;os extrajudiciais e com
            autoridades p&uacute;blicas quando houver requisi&ccedil;&atilde;o legal. Os dados n&atilde;o s&atilde;o
            vendidos nem utilizados para fins comerciais.
          </p>
        </div>
      </details>

      <details class="acordeao">
        <summary>Por quanto tempo s&atilde;o guardados</summary>
        <div class="acordeao__corpo">
          <p class="sem-margem">
            Os livros e documentos das serventias extrajudiciais t&ecirc;m guarda permanente ou
            por prazos definidos em normas espec&iacute;ficas. Por isso, o pedido de exclus&atilde;o de
            dados constantes de atos j&aacute; praticados n&atilde;o pode ser atendido &mdash; a
            conserva&ccedil;&atilde;o &eacute; exig&ecirc;ncia legal e garante a seguran&ccedil;a jur&iacute;dica dos atos.
          </p>
        </div>
      </details>

      <details class="acordeao">
        <summary>Seus direitos</summary>
        <div class="acordeao__corpo">
          <p>
            Voc&ecirc; pode solicitar confirma&ccedil;&atilde;o da exist&ecirc;ncia de tratamento, acesso aos seus
            dados, corre&ccedil;&atilde;o de informa&ccedil;&otilde;es incompletas ou desatualizadas e informa&ccedil;&atilde;o
            sobre compartilhamentos, observadas as restri&ccedil;&otilde;es legais aplic&aacute;veis aos atos
            j&aacute; praticados.
          </p>
          <p class="sem-margem">
            As solicita&ccedil;&otilde;es devem ser feitas pelos canais indicados abaixo, com
            identifica&ccedil;&atilde;o do solicitante.
          </p>
        </div>
      </details>
    </section>

    <section class="secao" aria-labelledby="titulo-encarregado">
      <h2 class="secao__titulo" id="titulo-encarregado">Encarregado pelo tratamento de dados</h2>
      <div class="painel">
        <dl class="dados">
          <dt>Encarregado (DPO)</dt>
          <dd>[NOME DO ENCARREGADO]</dd>
          <dt>E-mail</dt>
          <dd><a href="mailto:{email}">{email}</a></dd>
          <dt>Telefone</dt>
          <dd><a href="tel:{tel_link}">{telefone}</a></dd>
          <dt>Presencialmente</dt>
          <dd>{endereco} &middot; {cidade} &middot; {horario}</dd>
        </dl>
      </div>
      <p class="nota">
        &Uacute;ltima atualiza&ccedil;&atilde;o: [DATA]. Atualizar esta data sempre que o texto for revisado.
      </p>
    </section>
  </main>""".format(
    topo=topo_pagina(
        "Aviso de Privacidade",
        "Como esta serventia trata dados pessoais, com que finalidade e quais s&atilde;o "
        "os seus direitos.",
        [("index.html", "In&iacute;cio"), (None, "Aviso de Privacidade")],
    ),
    email=EMAIL,
    tel_link=TELEFONE_LINK,
    telefone=TELEFONE,
    endereco=ENDERECO,
    cidade=CIDADE,
    horario=HORARIO_CURTO,
)


# ===========================================================================
# Geração
# ===========================================================================

if __name__ == "__main__":
    gerados = [
        pagina(
            "index.html",
            "In&iacute;cio",
            "Cart&oacute;rio Arquimedes Bucar, 2&ordm; Of&iacute;cio de Guaraciaba do Norte &ndash; CE. Notas, Protesto, "
            "Registro de Im&oacute;veis, T&iacute;tulos e Documentos e Pessoas Jur&iacute;dicas.",
            corpo_index,
        ),
        pagina(
            "o-cartorio.html",
            "O Cart&oacute;rio",
            "Apresenta&ccedil;&atilde;o, miss&atilde;o, valores e dados oficiais da serventia de Guaraciaba "
            "do Norte.",
            corpo_cartorio,
        ),
        pagina(
            "servicos.html",
            "Servi&ccedil;os",
            "Servi&ccedil;os das cinco atribui&ccedil;&otilde;es da serventia e a documenta&ccedil;&atilde;o exigida em "
            "cada um.",
            corpo_servicos,
        ),
        pagina(
            "servicos-notas.html",
            "Tabelionato de Notas",
            "Firmas, autentica&ccedil;&otilde;es, escrituras, procura&ccedil;&otilde;es, invent&aacute;rio, div&oacute;rcio, "
            "testamento e atos eletr&ocirc;nicos.",
            corpo_notas,
            nav_atual="servicos.html",
        ),
        pagina(
            "servicos-protesto.html",
            "Tabelionato de Protesto de T&iacute;tulos",
            "Protesto, pagamento, cancelamento e certid&otilde;es de protesto de t&iacute;tulos.",
            corpo_protesto,
            nav_atual="servicos.html",
        ),
        pagina(
            "servicos-registro-imoveis.html",
            "Registro de Im&oacute;veis",
            "Registro de compra e venda, hipoteca, averba&ccedil;&otilde;es, usucapi&atilde;o extrajudicial e "
            "certid&otilde;es de matr&iacute;cula.",
            corpo_imoveis,
            nav_atual="servicos.html",
        ),
        pagina(
            "servicos-titulos-documentos.html",
            "Registro de T&iacute;tulos e Documentos",
            "Registro de contratos, notifica&ccedil;&atilde;o extrajudicial e conserva&ccedil;&atilde;o de "
            "documentos.",
            corpo_rtd,
            nav_atual="servicos.html",
        ),
        pagina(
            "servicos-pessoas-juridicas.html",
            "Registro Civil de Pessoas Jur&iacute;dicas",
            "Registro de associa&ccedil;&otilde;es, funda&ccedil;&otilde;es, sociedades simples, atas e "
            "altera&ccedil;&otilde;es estatut&aacute;rias.",
            corpo_rcpj,
            nav_atual="servicos.html",
        ),
        pagina(
            "certidoes.html",
            "Certid&otilde;es",
            "Portais oficiais para pedidos de certid&atilde;o on-line e certid&otilde;es emitidas por "
            "esta serventia.",
            corpo_certidoes,
        ),
        pagina(
            "selo-digital.html",
            "Selo Digital",
            "Como conferir a autenticidade de um documento expedido por esta "
            "serventia pelo selo digital do TJCE.",
            corpo_selo,
        ),
        pagina(
            "transparencia.html",
            "Transpar&ecirc;ncia",
            "Dados oficiais da serventia, valores cobrados e canais de "
            "fiscaliza&ccedil;&atilde;o e ouvidoria.",
            corpo_transparencia,
        ),
        pagina(
            "agenda-2030.html",
            "Agenda 2030",
            "Os Objetivos de Desenvolvimento Sustent&aacute;vel da ONU e a atua&ccedil;&atilde;o "
            "desta serventia em cada um deles.",
            corpo_agenda,
        ),
        pagina(
            "privacidade.html",
            "Aviso de Privacidade",
            "Tratamento de dados pessoais nesta serventia, conforme a Lei Geral de "
            "Prote&ccedil;&atilde;o de Dados.",
            corpo_privacidade,
            nav_atual="transparencia.html",
        ),
        pagina(
            "emolumentos.html",
            "Emolumentos",
            "Valores dos servi&ccedil;os notariais e de registro, fixados por lei estadual e "
            "divulgados pelo TJCE.",
            corpo_emolumentos,
        ),
        pagina(
            "modelos.html",
            "Modelos e requerimentos",
            "Formul&aacute;rios e declara&ccedil;&otilde;es para download.",
            corpo_modelos,
            nav_atual="servicos.html",
        ),
        pagina(
            "duvidas.html",
            "D&uacute;vidas frequentes",
            "Respostas &agrave;s perguntas mais comuns do atendimento do cart&oacute;rio.",
            corpo_duvidas,
        ),
        pagina(
            "ouvidoria.html",
            "Ouvidoria",
            "Canal de elogios, sugest&otilde;es, reclama&ccedil;&otilde;es e den&uacute;ncias.",
            corpo_ouvidoria,
            nav_atual="contato.html",
        ),
        pagina(
            "contato.html",
            "Contato e localiza&ccedil;&atilde;o",
            "Endere&ccedil;o, telefone, WhatsApp, e-mail e hor&aacute;rio de atendimento.",
            corpo_contato,
        ),
    ]
    for arquivo in gerados:
        print("gerado:", arquivo)
    print("\ntotal:", len(gerados), "paginas")
