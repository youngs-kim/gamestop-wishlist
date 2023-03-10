import axios from 'axios';
import React, { useState } from 'react';
import ItemList from './ItemList';

const CustomForm = () => {
  const [itemList, setItemList] = useState([]);
  const [item, setItem] = useState('');

  const url = 'http://127.0.0.1:5000/gamestop';

  const handleFormSubmit = (e) => {
    e.preventDefault();
    // addItem({ title: item, id: Date.now() });
    // addItem({
    //   title: 'Fifa23',
    //   price: 27.99,
    //   condition: 'new',
    //   imgUrl: 'https://media.gamestop.com/i/gamestop/11206861-11206860?$pdp2x$',
    //   link: ' https://www.gamestop.com/search/?q=devil%20may%20cry&type=Primary&sort=BestMatch_Desc&p=1fif',
    //   id: Date.now(),
    // });

    // To backend - http://localhost:5000/gamestop?url=https:%2F%2Fwww.gamestop.com%2Fvideo-games%2Fproducts%2Ffifa-22---nint

    axios
      .get(url, {
        params: { url: item },
      })
      .then(function (response) {
        // console.log(response.data);
        addItem({
          title: response.data.title,
          price: response.data.price,
          condition: response.data.condition,
          imgUrl: response.data.image_link,
          link: response.data.url,
          id: Date.now(),
        });
      })
      .catch(function (error) {
        console.log(error);
      });

    setItem('');
  };

  const addItem = (item) => {
    setItemList((prevItem) => [item, ...prevItem]);
    // console.log(itemList);
  };

  const deleteItem = (id) => {
    setItemList((prevState) => prevState.filter((item) => item.id !== id));
  };

  return (
    <div>
      <form className="todo" onSubmit={handleFormSubmit}>
        <div className="wrapper">
          <input
            type="text"
            id="task"
            className="input"
            value={item}
            onInput={(e) => setItem(e.target.value)}
            required
            autoFocus
            autoComplete="off"
            placeholder="Enter Task"
          />
          <label htmlFor="task" className="label">
            Copy Link
          </label>
        </div>
        <button
          className="btn"
          // aria-label="Add Task"
          type="submit"
          title="Add Task"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            strokeWidth={1.5}
            stroke="currentColor"
            className="w-6 h-6"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M12 4.5v15m7.5-7.5h-15"
            />
          </svg>
        </button>
      </form>

      <ItemList itemList={itemList} deleteItem={deleteItem} />
    </div>
  );
};

export default CustomForm;
