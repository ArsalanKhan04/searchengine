import React, { useState } from 'react';
import axios from 'axios';


const SearchApp = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [time, setTime] = useState(0.0);
  const [count, setCount] = useState(0.0);
  const [currentPage, setCurrentPage] = useState(1);
  const resultsPerPage = 10; // Set the number of results to display per page

  const handleSearch = () => {
    axios
      .get(`http://127.0.0.1:8000/search/search/?q=${query}`)
      .then((response) => {
        setResults(response.data.result);
        setTime(response.data.time);
        setCount(response.data.count);
        setCurrentPage(1); // Reset current page after search
      })
      .catch((error) => {
        console.error('Error fetching search results:', error);
      });
  };

  const renderResults = () => {
    const startIndex = (currentPage - 1) * resultsPerPage;
    const endIndex = startIndex + resultsPerPage;
    const currentResults = results.slice(startIndex, endIndex);
    
    return (
      <ul>
        {currentResults.map((result, index) => (
          <li key={index}>
            <a href={result.url}>{result.title}</a>
            <p>Date: {result.date}</p>
            <p>{result.chars500}</p>
          </li>
        ))}
      </ul>
    );
  };

  const handlePageChange = (newPage) => {
    setCurrentPage(newPage);
  };
  const totalPages = Math.ceil(results.length / resultsPerPage);
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
        {/* Display search statistics */}
        {count !== 0 ? (
          <h3>Generated {count.toFixed(2)} pages in {time} s</h3>
        ) : (
          <h3>Enter Query Above</h3>
        )}

        <h2>Search Results:</h2>

        {/* Render current page results */}
        {renderResults()}

        {/* Pagination controls */}
        <div>
          <button disabled={currentPage === 1} onClick={() => handlePageChange(currentPage - 1)}>
            Previous
          </button>
          <span> Page {currentPage} of {totalPages} </span>
          <button disabled={currentPage === totalPages} onClick={() => handlePageChange(currentPage + 1)}>
            Next
          </button>
        </div>
      </div>
    </div>
  );
};

export default SearchApp;
