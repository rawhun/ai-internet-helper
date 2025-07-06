import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import ChatWindow from '../ChatWindow';

test('renders chat window and sends message', async () => {
  render(<ChatWindow />);
  expect(screen.getByPlaceholderText(/type your message/i)).toBeInTheDocument();
  fireEvent.change(screen.getByPlaceholderText(/type your message/i), { target: { value: 'Hi' } });
  fireEvent.click(screen.getByText(/send/i));
  expect(screen.getByText('Hi')).toBeInTheDocument();
  await waitFor(() => expect(screen.getByText(/.../)).toBeInTheDocument());
}); 