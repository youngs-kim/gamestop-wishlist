import React from 'react';
import styles from './item.module.css';
import { TrashIcon } from '@heroicons/react/24/outline';

const Item = ({ item, deleteItem }) => {
  return (
    <li className={styles.task}>
      <div className={styles.taskGroup}>
        <div className={styles.titleImg}>
          <div className={styles.gameImgDiv}>
            <img src={item.imgUrl} style={{ width: 150 }} />
          </div>
          <a href={item.link} style={{ fontSize: 20 }}>{item.title}</a>
        </div>
        <div className={styles.addConPrice}>
          <div>Condition: {item.condition}</div>
          <div>Price: {item.price}</div>
          <div className={styles.footer}>Added On: {item.date}</div>
        </div>
      </div>
      <div className={styles.taskButton}>
        <button
          className={`btn ${styles.delete}`}
          onClick={() => deleteItem(item.id)}
        >
          <TrashIcon width={24} height={24} />
        </button>
      </div>
    </li>
  );
};

export default Item;
