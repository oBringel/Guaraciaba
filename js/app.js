// app.js — ponto de entrada. Carrega os dados, monta a moldura e o conteúdo.

import { carregarDados } from "./dados.js";
import { montarLayout, ativarMenu } from "./layout.js";
import { preencherVinculos } from "./vinculos.js";
import { renderizarConteudo } from "./paginas.js";
import { consultar } from "./utilitarios.js";

function atualizarTitulo(cartorio) {
  const { nomeCurto, descritor } = cartorio.identificacao;

  if (document.body.dataset.pagina === "index") {
    document.title = `${nomeCurto} – ${descritor}`;
    return;
  }

  const titulo = consultar("main h1, .pagina-topo h1");
  if (titulo) {
    document.title = `${titulo.textContent.trim()} – ${nomeCurto}`;
  }
}

function mostrarErro(erro) {
  console.error(erro);

  const mensagem = document.createElement("p");
  mensagem.className = "aviso-carregamento";
  mensagem.textContent =
    "Não foi possível carregar as informações do site. Recarregue a página ou entre em contato com o cartório.";
  document.body.prepend(mensagem);
}

async function iniciar() {
  try {
    const dados = await carregarDados();

    montarLayout(dados.cartorio, dados.servicos);
    renderizarConteudo(dados);
    preencherVinculos(dados.cartorio);
    ativarMenu();
    atualizarTitulo(dados.cartorio);

    document.documentElement.classList.add("site-pronto");
  } catch (erro) {
    mostrarErro(erro);
  }
}

iniciar();
