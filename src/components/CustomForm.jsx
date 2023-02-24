import React from 'react';
import { BeakerIcon } from '@heroicons/react/24/solid';

const CustomForm = () => {
  const handleFormSubmit = (e) => {
    e.preventDefault();
    console.log(e);
  };

  return (
    <form className="todo" onSubmit={handleFormSubmit}>
      <div className="wrapper">
        <input
          type="text"
          id="task"
          className="input"
          //   value={task}
          //   onInput={(e) => setTask(e.target.value)}
          required
          autoFocus
          maxLength={60}
          placeholder="Enter Task"
        />
        <label htmlfor="task" className="label">
          Copy Link
        </label>
      </div>
      <button className="btn" aria-label="Add Task" type="submit">
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
  );
};

export default CustomForm;
