// vinculos.js — liga os elementos marcados no HTML aos dados do JSON.
//
//   data-campo="telefone"   → substitui o texto do elemento
//   data-link="tjce"        → define o href do link
//   data-wa="pedido"        → monta um link do WhatsApp com a mensagem padrão
//   data-texto="telefone"   → preenche também o texto do link

import { consultarTodos } from "./utilitarios.js";

/** Textos simples que podem ser usados em data-campo / data-texto. */
export function valores(cartorio) {
  const { identificacao, endereco, contato, atendimento, responsaveis } = cartorio;

  return {
    nomeCurto: identificacao.nomeCurto,
    descritor: identificacao.descritor,
    nomeOficial: identificacao.nomeOficial,
    titular: identificacao.titular,
    cns: identificacao.cns,
    comarca: identificacao.comarca,
    cidade: endereco.cidade,
    uf: endereco.uf,
    endereco: endereco.logradouro,
    enderecoCompleto: `${endereco.logradouro} · ${endereco.cidade} – ${endereco.uf}`,
    cep: endereco.cep,
    telefone: contato.telefone,
    whatsapp: contato.whatsapp,
    email: contato.email,
    instagram: contato.instagram,
    horario: atendimento.resumo,
    responsavelOuvidoria: responsaveis.ouvidoria,
    encarregado: responsaveis.encarregado,
    privacidadeAtualizadoEm: responsaveis.privacidadeAtualizadoEm,
    ano: String(new Date().getFullYear())
  };
}

export function linkWhatsApp(cartorio, intencao = "duvida") {
  const numero = String(cartorio.contato.whatsappNumero).replace(/\D/g, "");
  const mensagem = cartorio.mensagens[intencao] || cartorio.mensagens.duvida;
  return `https://wa.me/${numero}?text=${encodeURIComponent(mensagem)}`;
}

export function destinos(cartorio) {
  const consulta =
    cartorio.endereco.consultaMapa ||
    `${cartorio.endereco.logradouro}, ${cartorio.endereco.cidade} - ${cartorio.endereco.uf}`;
  const enderecoCodificado = encodeURIComponent(consulta);

  return {
    telefone: `tel:${cartorio.contato.telefoneLink}`,
    whatsapp: linkWhatsApp(cartorio, "duvida"),
    email: `mailto:${cartorio.contato.email}`,
    instagram: cartorio.contato.instagramUrl,
    mapa: `https://www.google.com/maps?q=${enderecoCodificado}`,
    mapaEmbed: `https://www.google.com/maps?q=${enderecoCodificado}&output=embed`,
    ...cartorio.links
  };
}

export function preencherVinculos(cartorio, raiz = document) {
  const textos = valores(cartorio);
  const links = destinos(cartorio);

  consultarTodos("[data-campo]", raiz).forEach((elemento) => {
    const chave = elemento.dataset.campo;
    if (textos[chave] !== undefined) {
      elemento.textContent = textos[chave];
    }
  });

  consultarTodos("[data-link]", raiz).forEach((elemento) => {
    const url = links[elemento.dataset.link];
    if (!url) return;

    elemento.setAttribute("href", url);

    if (elemento.dataset.texto && textos[elemento.dataset.texto] !== undefined) {
      elemento.textContent = textos[elemento.dataset.texto];
    }

    if (/^https?:/i.test(url)) {
      elemento.setAttribute("target", "_blank");
      elemento.setAttribute("rel", "external noopener");
    }
  });

  consultarTodos("[data-wa]", raiz).forEach((elemento) => {
    elemento.setAttribute("href", linkWhatsApp(cartorio, elemento.dataset.wa));
    elemento.setAttribute("target", "_blank");
    elemento.setAttribute("rel", "noopener");
  });
}
