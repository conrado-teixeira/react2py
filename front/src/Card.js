import React from 'react';

function Card({ person }) {
  if (!person) {
    console.log("FALTOU PESSOA")
    return null; // Handle cases where person might be undefined or null
  }
  return (
    <div className="card">
      <h2>{person.name}</h2>
      <p>{person.company}</p>
    </div>
  );
}

export default Card;
