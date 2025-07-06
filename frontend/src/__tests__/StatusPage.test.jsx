import { render, screen } from '@testing-library/react';
import StatusPage from '../StatusPage';

test('renders status page and loader', () => {
  render(<StatusPage />);
  expect(screen.getByText(/system status/i)).toBeInTheDocument();
  expect(screen.getByRole('status', { hidden: true })).toBeInTheDocument();
}); 