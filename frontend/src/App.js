import React, { useState } from 'react';
import axios from 'axios';
import { Button, Navbar, Container, Row, Col } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';


const SearchApp = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [time, setTime] = useState(0.0);
  const [count, setCount] = useState(0);
  const [currentPage, setCurrentPage] = useState(1);
  const resultsPerPage = 10; // Set the number of results to display per page
  const totalPages = Math.ceil(results.length / resultsPerPage);

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
      <Container>
        {currentResults.map((result, index) => (
          <Row key={index} className="mb-3">
            <Col>
              <h4><a href={result.url}>{result.title}</a></h4>
              <p>Date: {result.date}</p>
              <p>{result.chars500}</p>
            </Col>
          </Row>
        ))}
      </Container>
    );
  };

  const handlePageChange = (newPage) => {
    setCurrentPage(newPage);
  };

  return (
    <div>
      <Navbar bg="dark" variant="dark">
        <Navbar.Brand href="#">Search Engine</Navbar.Brand>
        <Navbar.Toggle aria-controls="navbar-nav" />
        <Navbar.Collapse id="navbar-nav">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Enter your search query"
            className="mr-2 form-control"
          />
          <Button onClick={handleSearch}>Search</Button>
        </Navbar.Collapse>
      </Navbar>

      <Container className="mt-4">
        {/* Display search statistics */}
        {count !== 0 ? (
          <div>
            <Row>
              <Col>

                <h2>Search Results:</h2>
              </Col>
              <Col className="text-right">
              <p >Generated {count} pages in {time.toFixed(2)} s</p>
             
                 </Col>
            </Row>
            

            <br/>
            <br/>
          </div>
        ) : (
          <br/>
        )}


        {/* Render current page results */}
        {renderResults()}

        {/* Pagination controls */}
        {
          count === 0 ? (<br></br>) :
          (<div className="text-center mt-4">
          <Button
            variant="primary"
            disabled={currentPage === 1}
            onClick={() => handlePageChange(currentPage - 1)}
          >
            Previous
          </Button>
          <span className="mx-3"> Page {currentPage} of {totalPages} </span>
          <Button
            variant="primary"
            disabled={currentPage === totalPages}
            onClick={() => handlePageChange(currentPage + 1)}
          >
            Next
          </Button>
        </div>)
        }
        
      </Container>
    </div>
  );
};

export default SearchApp;