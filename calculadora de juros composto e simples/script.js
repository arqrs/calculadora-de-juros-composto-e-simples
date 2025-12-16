console.log('script.js carregado');

function jurosSimples(capital, taxaPercent, tempo) {
  const taxa = taxaPercent / 100.0;
  return capital * (1 + taxa * tempo);
}

function jurosCompostos(capital, taxaPercent, tempo, compPerYear = 1) {
  const taxa = taxaPercent / 100.0;
  const n = compPerYear;
  return capital * Math.pow(1 + taxa / n, n * tempo);
}

function formatCurrencyBR(value) {
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value);
}

document.addEventListener('DOMContentLoaded', () => {
  try {
  const form = document.getElementById('calcForm');
  const capitalEl = document.getElementById('capital');
  const taxaEl = document.getElementById('taxa');
  const tempoEl = document.getElementById('tempo');
  const periodosEl = document.getElementById('periodos');
  const periodosLabel = document.getElementById('periodosLabel');
  const resultado = document.getElementById('resultado');
  const submitBtn = document.getElementById('submitBtn');
  const errCapital = document.getElementById('err-capital');
  const errTaxa = document.getElementById('err-taxa');
  const errTempo = document.getElementById('err-tempo');
  const tipo = document.getElementById('tipo');
  const capitalOut = document.getElementById('capitalOut');
  const taxaOut = document.getElementById('taxaOut');
  const tempoOut = document.getElementById('tempoOut');
  const periodosOut = document.getElementById('periodosOut');
  const montanteOut = document.getElementById('montanteOut');
  const jurosOut = document.getElementById('jurosOut');
  const clearBtn = document.getElementById('clear');

  // debug: log clicks
  if (submitBtn) submitBtn.addEventListener('click', () => console.log('botao calcular clicado'));
  if (clearBtn) clearBtn.addEventListener('click', () => console.log('botao limpar clicado (debug)'));

  // mostrar/ocultar periodos dependendo do modo
  form.addEventListener('change', (ev) => {
    const modo = form.elements['modo'].value;
    if (modo === 'composto') {
      periodosLabel.style.display = '';
    } else {
      periodosLabel.style.display = 'none';
    }
    validateInputs();
  });

  // validar enquanto digita
  [capitalEl, taxaEl, tempoEl, periodosEl].forEach(el => {
    if (el) el.addEventListener('input', validateInputs);
  });

  function showError(el, msg) {
    if (!el) return;
    el.textContent = msg || '';
  }

  function validateInputs() {
    const C = parseFloat(capitalEl.value);
    const i = parseFloat(taxaEl.value);
    const t = parseFloat(tempoEl.value);
    let valid = true;

    if (isNaN(C) || C < 0) { showError(errCapital, 'Capital inválido'); valid = false; } else { showError(errCapital, ''); }
    if (isNaN(i) || i < 0) { showError(errTaxa, 'Taxa inválida'); valid = false; } else { showError(errTaxa, ''); }
    if (isNaN(t) || t <= 0) { showError(errTempo, 'Tempo deve ser > 0'); valid = false; } else { showError(errTempo, ''); }

    submitBtn.disabled = !valid;
    return valid;
  }

  form.addEventListener('submit', (ev) => {
    ev.preventDefault();
    doCalculate();
  });

  function doCalculate() {
    try {
      if (!validateInputs()) return;
      const C = parseFloat(capitalEl.value);
      const i = parseFloat(taxaEl.value);
      const t = parseFloat(tempoEl.value);
      const modo = form.elements['modo'].value;
      const n = parseInt(periodosEl.value) || 1;

      if (isNaN(C) || isNaN(i) || isNaN(t)) {
        alert('Preencha capital, taxa e tempo corretamente.');
        return;
      }

      let mont, juros;
      if (modo === 'simples') {
        mont = jurosSimples(C, i, t);
        tipo.textContent = 'Juros Simples';
        periodosOut.textContent = '';
      } else {
        mont = jurosCompostos(C, i, t, n);
        tipo.textContent = 'Juros Compostos';
        periodosOut.textContent = `Compostos por ano: ${n}`;
      }

      juros = mont - C;

      capitalOut.textContent = `Capital inicial: ${formatCurrencyBR(C)}`;
      taxaOut.textContent = `Taxa anual: ${i}%`;
      tempoOut.textContent = `Tempo: ${t} anos`;
      montanteOut.textContent = `Montante: ${formatCurrencyBR(mont)}`;
      jurosOut.textContent = `Juros: ${formatCurrencyBR(juros)}`;

      resultado.classList.remove('hidden');
    } catch (err) {
      console.error('Erro em doCalculate:', err);
    }
  }

  // ligar o clique do botão (agora type=button) para chamar doCalculate
  if (submitBtn) {
    submitBtn.removeEventListener('click', () => {});
    submitBtn.addEventListener('click', (ev) => {
      console.log('botao calcular clicado (handler)');
      doCalculate();
    });
  }

  clearBtn.addEventListener('click', () => {
    form.reset();
    resultado.classList.add('hidden');
    periodosLabel.style.display = '';
    showError(errCapital, '');
    showError(errTaxa, '');
    showError(errTempo, '');
    submitBtn.disabled = true;
  });

  // inicial
  periodosLabel.style.display = '';
  validateInputs();
  } catch (err) {
    console.error('Erro no script.js:', err);
  }
});
