import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { ChakraProvider } from '@chakra-ui/react'  // Importa Chakra
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <ChakraProvider> {/* 👈 Envuelve la App */}
      <App />
    </ChakraProvider>
  </StrictMode>,
)
