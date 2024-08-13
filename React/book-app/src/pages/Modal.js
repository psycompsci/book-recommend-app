import React from 'react';

function Modal({ show, handleClose, book }) {
  if (!show) return null;

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <button className="modal-close" onClick={handleClose}>X</button>
        {book && (
          <>
            <h2>{book.title}</h2>
            <img src={book.image_url} alt={book.title} className="modal-image" />
            <p><strong>Author:</strong> {book.authors}</p>
            <p><strong>Description:</strong> {book.description}</p>
          </>
        )}
      </div>
    </div>
  );
}

export default Modal;