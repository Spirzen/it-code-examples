
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect } from 'vitest';
import { Counter } from './Counter';

describe('Counter', () => {
  it('increments on click', async () => {
    const user = userEvent.setup();
    render(<Counter />);
    expect(screen.getByTestId('count')).toHaveTextContent('0');
    await user.click(screen.getByRole('button', { name: '+1' }));
    expect(screen.getByTestId('count')).toHaveTextContent('1');
  });
});
