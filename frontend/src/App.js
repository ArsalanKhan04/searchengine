import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = () => {
    axios
      .get(`http://127.0.0.1:8000/search/search/?q=${query}`)
      .then((response) => {
        setResults(response.data);
      })
      .catch((error) => {
        console.error('Error fetching search results:', error);
      });
  };

  return (
    <div>
      <h1>Search App</h1>
      <div>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Enter your search query"
        />
        <button onClick={handleSearch}>Search</button>
      </div>
      <div>
        <h2>Search Results:</h2>
        <ul>
          {results.map((result, index) => (
            <li key={index}>
              <a href={result.url}>{result.title}</a>
              <p>Date: {result.date}</p>
              <p>{result.chars500}</p>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
