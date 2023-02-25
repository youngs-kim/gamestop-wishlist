import React from 'react';
import styles from './ItemList.module.css';
import Item from './Item';

const ItemList = ({ itemList, deleteItem }) => {
  return (
    <ul className={styles.task}>
      {itemList.map((item) => {
        return <Item key={item.id} item={item} deleteItem={deleteItem} />;
      })}
    </ul>
  );
};

export default ItemList;
