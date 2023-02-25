import React from 'react';
import styles from './item.module.css';
import { TrashIcon } from '@heroicons/react/24/outline';

const Item = ({ item, deleteItem }) => {
  return (
    <li className={styles.task}>
      <div className={styles['task-group']}>{item.name}</div>
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
