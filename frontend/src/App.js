import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [time, setTime] = useState(0.0);
  const [count, setCount] = useState(0.0);

  const handleSearch = () => {
    axios
      .get(`http://127.0.0.1:8000/search/search/?q=${query}`)
      .then((response) => {
        setResults(response.data.result);
        setTime(response.data.time);
        setCount(response.data.count);
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
        {
          count !== 0 ? (
            <h3>Generated {count.toFixed(2)} pages in {time} s</h3>
          ) : (
            <h3>Enter Query Above</h3>
          )
        }
        
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
