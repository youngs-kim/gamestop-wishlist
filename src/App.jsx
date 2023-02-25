import { useState } from 'react';
import CustomForm from './components/CustomForm';

function App() {
  return (
    <div className="container">
      <header>
        <h1>GameStop Wishlist</h1>
      </header>
      <CustomForm />
    </div>
  );
}

export default App;
