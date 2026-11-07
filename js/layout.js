// layout.js — cabeçalho, rodapé e menu do celular.
// O HTML das páginas guarda só o conteúdo; a moldura é montada aqui.

import { esc, consultar } from "./utilitarios.js";

export function cabecalhoHtml(cartorio, paginaAtual) {
  const itens = cartorio.navegacao
    .map((item) => {
      const atual = item.arquivo === paginaAtual ? ' aria-current="page"' : "";
      return `          <li><a class="navegacao__link" href="${esc(item.arquivo)}"${atual}>${esc(item.rotulo)}</a></li>`;
    })
    .join("\n");

  return `  <a class="pular-conteudo" href="#conteudo">Ir para o conteúdo</a>

  <header class="cabecalho">
    <div class="container cabecalho__interno">
      <a class="marca" href="index.html">
        <span class="marca__nome" data-campo="nomeCurto"></span>
        <span class="marca__desc" data-campo="descritor"></span>
      </a>

      <p class="cabecalho__contato">
        <a data-link="telefone" data-texto="telefone"></a><br />
        <span data-campo="horario"></span>
      </p>

      <button
        class="menu-botao"
        type="button"
        id="menu-botao"
        aria-expanded="false"
        aria-controls="menu-principal"
      >
        <span class="menu-botao__icone" aria-hidden="true"></span>
        <span class="menu-botao__texto">Menu</span>
      </button>

      <nav class="navegacao" id="menu-principal" aria-label="Navegação principal">
        <ul class="navegacao__lista">
${itens}
        </ul>
      </nav>
    </div>
  </header>`;
}

export function rodapeHtml(cartorio, servicos) {
  const atribuicoes = servicos.atribuicoes
    .map(
      (item) =>
        `            <li><a href="${esc(item.arquivo)}">${esc(item.titulo)}</a></li>`
    )
    .join("\n");

  return `  <footer class="rodape">
    <div class="container">
      <div class="rodape__grade">
        <div>
          <p class="rodape__titulo" data-campo="nomeCurto"></p>
          <address>
            <span data-campo="endereco"></span><br />
            <span data-campo="cidade"></span> – <span data-campo="uf"></span> ·
            CEP <span data-campo="cep"></span><br />
            Telefone: <a data-link="telefone" data-texto="telefone"></a><br />
            WhatsApp: <a data-link="whatsapp" data-texto="whatsapp"></a><br />
            E-mail: <a data-link="email" data-texto="email"></a><br />
            Instagram: <a data-link="instagram" data-texto="instagram"></a>
          </address>
          <p class="sem-margem" data-campo="horario"></p>
        </div>

        <div>
          <p class="rodape__titulo">Atribuições</p>
          <ul class="rodape__lista">
${atribuicoes}
          </ul>
        </div>

        <div>
          <p class="rodape__titulo">Institucional</p>
          <ul class="rodape__lista">
            <li><a href="transparencia.html">Transparência</a></li>
            <li><a href="modelos.html">Modelos e requerimentos</a></li>
            <li><a href="agenda-2030.html">Agenda 2030</a></li>
            <li><a href="privacidade.html">Aviso de Privacidade e LGPD</a></li>
            <li><a href="ouvidoria.html">Ouvidoria</a></li>
            <li><a data-link="tjce">Corregedoria-Geral de Justiça do Ceará</a></li>
          </ul>
        </div>
      </div>

      <div class="rodape__base">
        <p>
          <span data-campo="nomeOficial"></span> · CNS
          <span data-campo="cns"></span> · Titular:
          <span data-campo="titular"></span>
        </p>
        <p>
          Os emolumentos dos serviços notariais e de registro são fixados por lei
          estadual e divulgados pelo Tribunal de Justiça do Ceará.
        </p>
      </div>
    </div>
  </footer>`;
}

/** Injeta cabeçalho e rodapé em todas as páginas. */
export function montarLayout(cartorio, servicos) {
  const paginaAtual = document.body.dataset.nav || `${document.body.dataset.pagina}.html`;

  const cabecalho = consultar("#site-cabecalho");
  if (cabecalho) cabecalho.innerHTML = cabecalhoHtml(cartorio, paginaAtual);

  const rodape = consultar("#site-rodape");
  if (rodape) rodape.innerHTML = rodapeHtml(cartorio, servicos);
}

/** Menu do celular com aria-expanded, fechando por Escape e ao escolher um item. */
export function ativarMenu() {
  const botao = consultar("#menu-botao");
  const menu = consultar("#menu-principal");
  if (!botao || !menu) return;

  const estaAberto = () => botao.getAttribute("aria-expanded") === "true";

  const fechar = () => {
    botao.setAttribute("aria-expanded", "false");
    menu.classList.remove("esta-aberto");
  };

  botao.addEventListener("click", () => {
    const abrir = !estaAberto();
    botao.setAttribute("aria-expanded", String(abrir));
    menu.classList.toggle("esta-aberto", abrir);
  });

  menu.addEventListener("click", (evento) => {
    if (evento.target.closest("a")) fechar();
  });

  document.addEventListener("keydown", (evento) => {
    if (evento.key === "Escape" && estaAberto()) {
      fechar();
      botao.focus();
    }
  });
}
