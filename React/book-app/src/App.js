// {useState, useEffect} --> React "hooks" that allow us to call API endpoints
import React, {useState, useEffect} from 'react'
import api from './api'

const App = () => {
  const [books, setBooks] = useState([]);
  const [error, setError] = useState(null);

  const fetchBooks = async () => {
    try {
      const result = await api.get('/books');
      setBooks(result.data);
    }
    catch (error) {
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
      <nav className='navbar navbar-dark bg-primary'>
        <div className='container-fluid'>
          <a className='navbar-brand' href='#top'>Book App</a>
        </div>
      </nav>

      <table className='table table-striped table-bordered table-hover'>
        <thead>
          <tr>
            <th>Book ID</th>
            <th>Title</th>
            <th>Author</th>
            <th>Original Publication Year</th>
          </tr>
        </thead>
        <tbody>
          {books.map((book) => (
            <tr key={book.book_id}>
              <td>{book.book_id}</td>
              <td>{book.title}</td>
              <td>{book.authors}</td>
              <td>{book.original_publication_year}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
