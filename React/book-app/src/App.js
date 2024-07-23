// {useState, useEffect} --> React "hooks" that allow us to call API endpoints
import React, {useState, useEffect} from 'react' ;
import api from './api';

const App = () => {
  const [books, setBooks] = useState([]);
  const [formData, setFormData] = useState({
    isbn: '',
    title: '',
    author: ''
  });

  const fetchBooks = async () => {
    const result = await api.get('/books/');
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
    await api.post('/books/', formData);
    fetchBooks();
    setFormData({
      isbn: '', 
      title: '', 
      author: ''
    });
  };

}

export default App;
