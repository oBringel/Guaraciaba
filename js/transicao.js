// transicao.js — saída suave ao trocar de página.
// Sem isso a troca é instantânea e o conteúdo montado pelo JS parece "piscar".

const DURACAO_SAIDA = 180; // mesmo tempo do transition em css/base.css

export function ativarTransicao() {
  const semMovimento = window.matchMedia("(prefers-reduced-motion: reduce)");
  let saindo = false;

  document.addEventListener("click", (evento) => {
    if (saindo || evento.defaultPrevented) return;
    if (evento.button !== 0) return;
    if (evento.metaKey || evento.ctrlKey || evento.shiftKey || evento.altKey) return;

    const link = evento.target.closest("a[href]");
    if (!link) return;
    if (link.target && link.target !== "_self") return;
    if (link.hasAttribute("download")) return;
    if (link.dataset.semTransicao !== undefined) return;
    if (semMovimento.matches) return;

    const url = new URL(link.href, window.location.href);
    if (url.origin !== window.location.origin) return;

    // Âncoras na mesma página e recarregamentos usam o comportamento normal.
    const mesmaPagina =
      url.pathname === window.location.pathname && url.search === window.location.search;
    if (mesmaPagina) return;

    evento.preventDefault();
    saindo = true;
    document.documentElement.classList.add("pagina-saindo");

    window.setTimeout(() => {
      window.location.href = url.href;
    }, DURACAO_SAIDA);
  });

  // Ao voltar pelo histórico (bfcache) a página pode reaparecer já apagada.
  window.addEventListener("pageshow", () => {
    saindo = false;
    document.documentElement.classList.remove("pagina-saindo");
  });
}
