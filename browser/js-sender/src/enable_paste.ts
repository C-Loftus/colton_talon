const allowPaste = function(e: { stopImmediatePropagation: () => void; }){
  e.stopImmediatePropagation();
  return true;
};
document.addEventListener('paste', allowPaste, true);