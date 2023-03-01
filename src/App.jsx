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

// response = {
//   title: 'devil may cry',
//   price: 27.99,
//   condition: 'new',
//   imgUrl:
//     'https://media.gamestop.com/i/gamestop/11108956/Devil-May-Cry-5-Special-Edition---PlayStation-5?$pdp2x$$&fmt=webp',
//   link: ' https://www.gamestop.com/search/?q=devil%20may%20cry&type=Primary&sort=BestMatch_Desc&p=1fif',
// };
