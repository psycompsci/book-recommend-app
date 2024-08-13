import React, { useState, useEffect } from 'react';
import api from '../api';
import Modal from './Modal'; // Adjust the path if necessary

export default function Home() {
  const [books, setBooks] = useState([]);
  const [error, setError] = useState(null);
  const [selectedBook, setSelectedBook] = useState(null);
  const [showModal, setShowModal] = useState(false);

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

  const handleShowModal = (book) => {
    setSelectedBook(book);
    setShowModal(true);
  };

  const handleCloseModal = () => {
    setShowModal(false);
    setSelectedBook(null);
  };

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
                  <button 
                    className="btn btn-primary" 
                    onClick={() => handleShowModal(book)}
                  >
                    See More
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      <Modal 
        show={showModal} 
        handleClose={handleCloseModal} 
        book={selectedBook} 
      />
    </div>
  );
}