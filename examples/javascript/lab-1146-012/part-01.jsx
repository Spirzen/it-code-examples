import { useState } from 'react';

function Modal({ open, title, children, onClose }) {
  if (!open) return null;

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <div
        className="modal"
        role="dialog"
        aria-modal="true"
        onClick={(e) => e.stopPropagation()}
      >
        <header>
          <h2>{title}</h2>
          <button type="button" aria-label="Закрыть" onClick={onClose}>×</button>
        </header>
        <div className="modal-body">{children}</div>
      </div>
    </div>
  );
}

export default function App() {
  const [open, setOpen] = useState(false);

  return (
    <div className="app">
      <button type="button" onClick={() => setOpen(true)}>Открыть окно</button>
      <Modal open={open} title="Подтверждение" onClose={() => setOpen(false)}>
        <p>Вы уверены, что хотите продолжить?</p>
        <button type="button" onClick={() => setOpen(false)}>OK</button>
      </Modal>
    </div>
  );
}
