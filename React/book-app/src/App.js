// {useState, useEffect} --> React "hooks" that allow us to call API endpoints
import React, {useState, useEffect} from 'react' ;
import api from './api';

const App = () => {
  const [books, setBooks] = useState([]);
  const [formData, setFormData] = useState({
    book_id: '',
    title: '',
    authors: '', 
    original_publication_year: ''
  });

  const fetchBooks = async () => {
    const result = await api.get('/books/{book-id}/');
    setBooks(result.data);
  }

  useEffect(() => {
    fetchBooks();
  }, []);

  const handleInputChange = (event) => {
    // const value = event.target.type === 'checkbox' ? event.target.checked : event.target.value;
    setFormData({
      ...formData, 
      [event.target.name]: event.target.value
    });
  }

  const handleFormSubmit = async(event) => {
    event.preventDefault();
    await api.post('/books/{book-id}/', formData);
    fetchBooks();
    setFormData({
      book_id: '', 
      title: '', 
      authors: '', 
      original_publication_year: ''
    });
  };

  return (
    <div>
      <nav className='navbar navbar-dark bg-primary'>
        <div className='container-fluid'>
          <a className='navbar-brand' href='#'>Book App</a>
        </div>
      </nav>
      
      <p>Welcome to the book recommendation app!</p>
      
      <table className='table table-striped table-bordered table-hover'>
        <thead>
          <tr>
            <th>Book ID</th>
            <th>Title</th>
            <th>Author(s)</th>
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
  )
}

export default App;
