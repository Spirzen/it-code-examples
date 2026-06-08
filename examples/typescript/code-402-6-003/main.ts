
import styled from 'styled-components';

const PrimaryButton = styled.button`
  background-color: ${props => props.theme.primary};
  color: white;
  padding: 12px 24px;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  cursor: pointer;

  &:hover {
    opacity: 0.9;
  }
`;

// Использование
<PrimaryButton>Submit</PrimaryButton>
