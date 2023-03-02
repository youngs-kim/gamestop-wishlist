import React from 'react';
import styles from './item.module.css';
import { TrashIcon } from '@heroicons/react/24/outline';

const Item = ({ item, deleteItem }) => {
  console.log(item);
  return (
    <li className={styles.task}>
      {/* <div className={styles['task-group']}>{item.name}</div> */}
      <div className={styles['task-group']}>
        <div className={styles.titleImg}>
          <a href={item.link}>{item.title} Playstation 5</a>
          <img src={item.imgUrl} style={{ width: 100 }} />
        </div>
        <div className={styles.addConPrice}>
          <div>Condition: {item.condition}</div>
          <div>Price: ${item.price}</div>
          <div className={styles.footer}>Added On: 3/1/2023</div>
        </div>
      </div>
      <div className={styles['task-group']}>
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
