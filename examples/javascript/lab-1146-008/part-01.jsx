import { useId, useState } from 'react';

export function Tooltip({ label, children }) {
  const [open, setOpen] = useState(false);
  const tipId = useId();

  return (
    <span
      className="tooltip-wrap"
      onMouseEnter={() => setOpen(true)}
      onMouseLeave={() => setOpen(false)}
      onFocus={() => setOpen(true)}
      onBlur={() => setOpen(false)}
    >
      <span aria-describedby={open ? tipId : undefined}>{children}</span>
      {open && (
        <span id={tipId} role="tooltip" className="tooltip-bubble">
          {label}
        </span>
      )}
    </span>
  );
}
