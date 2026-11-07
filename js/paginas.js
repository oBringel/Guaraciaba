// paginas.js — blocos que cada página monta a partir dos arquivos JSON.
// O HTML da página indica o que deve aparecer com data-render="nome-do-bloco".

import { esc, consultar, consultarTodos, juntar } from "./utilitarios.js";
import { acordeao, aviso, lista } from "./componentes.js";
import { destinos } from "./vinculos.js";

const numero = (indice) => String(indice + 1).padStart(2, "0");

export function cartoesAtribuicoes({ atribuicoes }) {
  const cartoes = atribuicoes
    .map(
      (atribuicao, indice) => `          <article class="cartao cartao--link">
            <span class="cartao__numero" aria-hidden="true">${numero(indice)}</span>
            <h3 class="cartao__titulo"><a href="${esc(atribuicao.arquivo)}">${esc(atribuicao.titulo)}</a></h3>
            <p>${esc(atribuicao.resumo)}</p>
            <p class="cartao__rodape"><a href="${esc(atribuicao.arquivo)}">Conhecer serviços &rarr;</a></p>
          </article>`
    )
    .join("\n");

  return `        <div class="grade grade--atribuicoes">
${cartoes}
        </div>`;
}

export function blocoContato(cartorio) {
  const { atendimento } = cartorio;

  const linhasHorario = atendimento.tabela
    .map(
      (linha) =>
        `              <tr><th scope="row">${esc(linha.dia)}</th><td>${esc(linha.horario)}</td></tr>`
    )
    .join("\n");

  return `      <div class="contato-grade">
        <div>
          <div class="painel painel--destaque">
            <h3 class="cartao__titulo" data-campo="nomeCurto"></h3>
            <address>
              <span data-campo="endereco"></span><br />
              <span data-campo="cidade"></span> – <span data-campo="uf"></span><br />
              CEP <span data-campo="cep"></span>
            </address>
            <dl class="dados">
              <dt>Telefone</dt>
              <dd><a data-link="telefone" data-texto="telefone"></a></dd>
              <dt>WhatsApp</dt>
              <dd><a data-link="whatsapp" data-texto="whatsapp"></a></dd>
              <dt>E-mail</dt>
              <dd><a data-link="email" data-texto="email"></a></dd>
              <dt>Instagram</dt>
              <dd><a data-link="instagram" data-texto="instagram"></a></dd>
            </dl>
            <div class="botoes">
              <a class="botao botao--principal" data-wa="duvida" rel="noopener" target="_blank">Falar no WhatsApp</a>
              <a class="botao botao--secundario" data-link="email">Enviar e-mail</a>
            </div>
          </div>

          <h3 class="secao__titulo espaco-acima">Horário de atendimento</h3>
          <table class="horarios">
            <caption>Atendimento ao público na sede da serventia.</caption>
            <tbody>
${linhasHorario}
            </tbody>
          </table>
          <p class="nota">${esc(atendimento.observacao)}</p>
        </div>

        <div class="mapa">
          <iframe
            src="${esc(destinos(cartorio).mapaEmbed)}"
            title="Mapa com a localização do cartório"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
      </div>`;
}

export function dadosServentia(cartorio, { atribuicoes }) {
  const nomes = atribuicoes.map((atribuicao) => esc(atribuicao.titulo)).join(" &middot; ");

  return `        <div class="painel">
          <dl class="dados">
            <dt>Denominação oficial</dt>
            <dd><span data-campo="nomeOficial"></span></dd>
            <dt>Titular</dt>
            <dd><span data-campo="titular"></span></dd>
            <dt>Código Nacional da Serventia (CNS)</dt>
            <dd><span data-campo="cns"></span></dd>
            <dt>Comarca</dt>
            <dd><span data-campo="comarca"></span> – <span data-campo="uf"></span></dd>
            <dt>Atribuições</dt>
            <dd>${nomes}</dd>
            <dt>Endereço</dt>
            <dd>
              <span data-campo="endereco"></span> &middot;
              <span data-campo="cidade"></span> –
              <span data-campo="uf"></span> &middot; CEP
              <span data-campo="cep"></span>
            </dd>
            <dt>Atendimento</dt>
            <dd><span data-campo="horario"></span></dd>
          </dl>
        </div>`;
}

export function blocoOuvidoria() {
  return `      <div class="painel painel--destaque">
        <dl class="dados">
          <dt>Responsável</dt>
          <dd><span data-campo="responsavelOuvidoria"></span></dd>
          <dt>E-mail</dt>
          <dd><a data-link="email" data-texto="email"></a></dd>
          <dt>Telefone</dt>
          <dd><a data-link="telefone" data-texto="telefone"></a></dd>
          <dt>Presencialmente</dt>
          <dd><span data-campo="enderecoCompleto"></span></dd>
          <dt>Horário</dt>
          <dd><span data-campo="horario"></span></dd>
        </dl>
      </div>`;
}

export function blocoPrivacidade() {
  return `      <div class="painel">
        <dl class="dados">
          <dt>Encarregado (DPO)</dt>
          <dd><span data-campo="encarregado"></span></dd>
          <dt>E-mail</dt>
          <dd><a data-link="email" data-texto="email"></a></dd>
          <dt>Telefone</dt>
          <dd><a data-link="telefone" data-texto="telefone"></a></dd>
          <dt>Presencialmente</dt>
          <dd>
            <span data-campo="enderecoCompleto"></span> &middot;
            <span data-campo="horario"></span>
          </dd>
        </dl>
      </div>`;
}

export function portaisCertidoes({ portaisCertidoes }) {
  const itens = portaisCertidoes
    .map(
      (portal) => `          <li>
            <a data-link="${esc(portal.link)}">
              ${esc(portal.titulo)}
              <span>${esc(portal.descricao)}</span>
            </a>
          </li>`
    )
    .join("\n");

  return `        <div class="painel">
          <ul class="lista-links">
${itens}
          </ul>
        </div>`;
}

export function certidoesBalcao({ certidoesBalcao }) {
  return lista(certidoesBalcao);
}

export function faq({ faq }) {
  return juntar(faq.map((item) => acordeao({ titulo: item.pergunta, html: item.html })));
}

export function modelos({ modelos }) {
  const itens = modelos
    .map(
      (modelo) => `          <li>
            <a href="${esc(modelo.arquivo)}" download>
              ${esc(modelo.titulo)}
              <span>${esc(modelo.descricao)}</span>
            </a>
          </li>`
    )
    .join("\n");

  return `        <div class="painel">
          <ul class="lista-links">
${itens}
          </ul>
        </div>`;
}

export function sobreApresentacao({ sobre }) {
  return `<div class="prosa">${sobre.apresentacao}</div>`;
}

export function sobreMissaoVisaoValores({ sobre }) {
  const cartao = (titulo, texto) => `        <article class="cartao">
          <h3 class="cartao__titulo">${esc(titulo)}</h3>
          <p>${esc(texto)}</p>
        </article>`;

  return `      <div class="grade">
${cartao("Missão", sobre.missao)}
${cartao("Visão", sobre.visao)}
${cartao("Valores", sobre.valores)}
      </div>`;
}

export function ods({ ods }) {
  const cartoes = ods
    .map(
      (objetivo) => `          <article class="cartao">
            <span class="cartao__numero" aria-hidden="true">${esc(objetivo.codigo)}</span>
            <h3 class="cartao__titulo">${esc(objetivo.titulo)}</h3>
            <p>${esc(objetivo.texto)}</p>
            <ul>
${objetivo.itens.map((item) => `              <li>${esc(item)}</li>`).join("\n")}
            </ul>
          </article>`
    )
    .join("\n");

  return `        <div class="grade grade--larga">
${cartoes}
        </div>`;
}

/** Preenche os blocos data-render da página atual. */
export function renderizarConteudo({ cartorio, servicos, conteudo }) {
  const blocos = {
    "cartoes-atribuicoes": () => cartoesAtribuicoes(servicos),
    "aviso-rcpn": () => aviso(conteudo.avisoRegistroCivil),
    apresentacao: () => sobreApresentacao(conteudo),
    "missao-visao-valores": () => sobreMissaoVisaoValores(conteudo),
    "dados-serventia": () => dadosServentia(cartorio, servicos),
    contato: () => blocoContato(cartorio),
    "portais-certidoes": () => portaisCertidoes(conteudo),
    "certidoes-balcao": () => certidoesBalcao(conteudo),
    faq: () => faq(conteudo),
    modelos: () => modelos(conteudo),
    ods: () => ods(conteudo),
    ouvidoria: () => blocoOuvidoria(),
    "privacidade-responsavel": () => blocoPrivacidade()
  };

  consultarTodos("[data-render]").forEach((alvo) => {
    const bloco = blocos[alvo.dataset.render];
    if (bloco) alvo.innerHTML = bloco();
  });

  const idServico = document.body.dataset.servico;
  if (idServico) preencherServico(servicos, idServico);
}

/** Monta a lista de serviços e os acordeões de documentos de uma atribuição. */
export function preencherServico({ atribuicoes }, id) {
  const atribuicao = atribuicoes.find((item) => item.id === id);
  if (!atribuicao) return;

  const intro = consultar('[data-servico="intro"]');
  if (intro) intro.textContent = atribuicao.intro;

  const listaServicos = consultar('[data-servico="lista"]');
  if (listaServicos) listaServicos.innerHTML = lista(atribuicao.servicos);

  const documentos = consultar('[data-servico="documentos"]');
  if (documentos) {
    documentos.innerHTML = juntar(
      atribuicao.documentos.map((documento) =>
        acordeao({
          titulo: documento.titulo,
          html: `            <ul>\n${documento.itens
            .map((item) => `              <li>${esc(item)}</li>`)
            .join("\n")}\n            </ul>`
        })
      )
    );
  }

  const blocoAviso = consultar('[data-servico="aviso"]');
  if (blocoAviso && atribuicao.aviso) blocoAviso.innerHTML = aviso(atribuicao.aviso);
}
