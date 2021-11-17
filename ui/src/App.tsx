import React from 'react';
import { ChakraProvider } from '@chakra-ui/provider';
import logo from './logo.svg';
import './App.css';
import Layout from './components/Layout';
import ConnectButton from './components/ConnectButton';
import Count from './components/Count';
function App() {
  return (
    <ChakraProvider>
      <Layout>
      <p style={{ color: "white" }}>Hello, world!</p>
      <ConnectButton/>
      <Count />
      </Layout>
    </ChakraProvider>
  );
}

export default App;
