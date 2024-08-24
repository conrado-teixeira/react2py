import './App.css';
import Card from './Card';
import React, { useEffect, useState } from 'react';

function App() {
  const [people, setPeople] = useState([]);

  useEffect(() => {
    //console.log("Teste")
    fetch('http://localhost:8000/buscar_vagas')  // Assuming the Python server runs on port 8000
      .then(response => response.json())
      .then(data => {
        console.log("Feteched data:" , data)
        setPeople(data)
      })
      .catch(error => console.error('Error fetching people:', error));
  }, []);

  return (
    <div className="App">
      <h1>Buscar Vagas</h1>
      <div className="card-list">
        {people.map((person, index) => (
          <Card key={index} person={person} />
        ))}
      </div>
    </div>
  );
}

export default App;
