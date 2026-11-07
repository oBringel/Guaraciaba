// dados.js — leitura dos arquivos JSON que concentram o conteúdo do site.

const PASTA_DADOS = new URL("../dados/", import.meta.url);

async function lerArquivo(nome) {
  const resposta = await fetch(new URL(`${nome}.json`, PASTA_DADOS), {
    cache: "no-cache"
  });

  if (!resposta.ok) {
    throw new Error(`Falha ao carregar dados/${nome}.json (HTTP ${resposta.status}).`);
  }

  return resposta.json();
}

/**
 * Carrega as três fontes de conteúdo do site.
 * cartorio.json  → dados da serventia, contato, horários e links
 * servicos.json  → atribuições, serviços e documentação
 * conteudo.json  → avisos, portais, dúvidas, modelos e Agenda 2030
 */
export async function carregarDados() {
  const [cartorio, servicos, conteudo] = await Promise.all([
    lerArquivo("cartorio"),
    lerArquivo("servicos"),
    lerArquivo("conteudo")
  ]);

  return { cartorio, servicos, conteudo };
}
