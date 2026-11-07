// utilitarios.js — funções pequenas usadas por todos os módulos.

const ENTIDADES = {
  "&": "&amp;",
  "<": "&lt;",
  ">": "&gt;",
  '"': "&quot;",
  "'": "&#39;"
};

/** Escapa texto vindo do JSON antes de inseri-lo no HTML. */
export function esc(valor) {
  return String(valor ?? "").replace(/[&<>"']/g, (caractere) => ENTIDADES[caractere]);
}

export function consultar(seletor, raiz = document) {
  return raiz.querySelector(seletor);
}

export function consultarTodos(seletor, raiz = document) {
  return Array.from(raiz.querySelectorAll(seletor));
}

/** Junta uma lista de trechos de HTML. */
export function juntar(trechos) {
  return trechos.filter(Boolean).join("\n");
}
