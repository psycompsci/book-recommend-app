import React, { useState, useEffect } from 'react';
import api from '../api';

export default function Home() {
  const [books, setBooks] = useState([]);
  const [error, setError] = useState(null);

  const fetchBooks = async () => {
    try {
      const result = await api.get('/books');
      setBooks(result.data);
    } catch (error) {
      setError('Error getting books');
    }
  };

  useEffect(() => {
    fetchBooks();
  }, []);

  if (error) {
    return <div><h1>{error}</h1></div>;
  }

  return (
    <div>
      <div className="container mt-4">
        <div className="row">
          {books.map((book) => (
            <div className="col-md-4 mb-4" key={book.book_id}>
              <div className="card">
                <img 
                  src={book.image_url} 
                  className="card-img-top" 
                  alt={book.title} 
                />
                <div className="card-body">
                  <h5 className="card-title">{book.title}</h5>
                  <p className="card-text">Author: {book.authors}</p>
                  <a href={`/books/${book.book_id}`} className="btn btn-primary">See More</a>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}