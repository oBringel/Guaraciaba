// componentes.js — peças de interface reaproveitadas pelas páginas.

import { esc } from "./utilitarios.js";

export function acordeao({ titulo, html }) {
  return `        <details class="acordeao">
          <summary>${esc(titulo)}</summary>
          <div class="acordeao__corpo">
${html}
          </div>
        </details>`;
}

export function lista(itens, classe = "lista-servicos") {
  const linhas = itens.map((item) => `            <li>${esc(item)}</li>`).join("\n");
  return `          <ul class="${classe}">
${linhas}
          </ul>`;
}

export function aviso({ titulo, html }) {
  return `        <div class="aviso">
          <p class="aviso__titulo">${esc(titulo)}</p>
          <p class="sem-margem">${html}</p>
        </div>`;
}

export function ctaWhatsApp({ titulo, texto, rotulo, intencao = "duvida" }) {
  return `        <div class="cta">
          <h2>${esc(titulo)}</h2>
          <p>${esc(texto)}</p>
          <p class="cta__acoes sem-margem">
            <a class="botao botao--contraste" data-wa="${esc(intencao)}" rel="noopener" target="_blank">${esc(rotulo)}</a>
          </p>
        </div>`;
}
