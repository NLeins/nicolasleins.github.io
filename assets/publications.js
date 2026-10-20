/* Citation copying for the publications page; no effect on the homepage feature. */
(function () {
  'use strict';

  var resetTimers = new WeakMap();

  function copyLegacy(text) {
    var previousFocus = document.activeElement;
    var textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.setAttribute('readonly', '');
    textarea.style.position = 'fixed';
    textarea.style.top = '-1000px';
    document.body.appendChild(textarea);
    try {
      textarea.select();
      if (!document.execCommand('copy')) {
        throw new Error('Clipboard copy failed');
      }
    } finally {
      document.body.removeChild(textarea);
      if (previousFocus && previousFocus.focus) {
        previousFocus.focus();
      }
    }
  }

  function copyText(text) {
    return Promise.resolve().then(function () {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        return navigator.clipboard.writeText(text);
      }
      return copyLegacy(text);
    }).catch(function (error) {
      // A denied modern clipboard request can still allow a legacy copy.
      if (navigator.clipboard && navigator.clipboard.writeText) {
        return copyLegacy(text);
      }
      throw error;
    });
  }

  document.addEventListener('click', function (event) {
    var button = event.target && event.target.closest
      ? event.target.closest('button.publication-cite') : null;
    if (!button || button.disabled || button.getAttribute('aria-busy') === 'true'
        || !button.closest('.publications-page')) return;

    var card = button.closest('.publication-card');
    var status = card && card.querySelector('.publication-copy-status');
    if (!status) return;

    window.clearTimeout(resetTimers.get(button));
    status.textContent = '';
    button.setAttribute('aria-busy', 'true');
    button.textContent = 'Copying…';

    copyText(button.getAttribute('data-bibtex') || '').then(function () {
      button.textContent = 'Copied';
      status.textContent = 'Citation copied.';
      resetTimers.set(button, window.setTimeout(function () {
        button.textContent = 'Cite';
        status.textContent = '';
      }, 4000));
    }).catch(function () {
      button.textContent = 'Try again';
      status.textContent = 'Could not copy the citation. Please try again.';
    }).then(function () {
      button.removeAttribute('aria-busy');
    });
  });
})();
