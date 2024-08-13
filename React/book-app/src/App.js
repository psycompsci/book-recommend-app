import React, { useState, useEffect } from 'react';
import Navbar from './Navbar';
import Home from './pages/Home';
import SignIn from './pages/SignIn';
import Register from './pages/Register';
import api from './api';

function App() {
    let Component;
    switch (window.location.pathname) {
        case "/":
            Component = Home;
            break;
        case "/home":
            Component = Home;
            break;
        case "/signin":
            Component = SignIn;
            break;
        case"/register":
            Component = Register;
            break;
        default:
            Component = Home; // Default to Home if the path doesn't match
            break;
    }

    return (
        <>
            <Navbar />
            <Component />
        </>
    );
}

export default App;
/*
import React from 'react';
import Navbar from './Navbar';
import Home from './pages/Home';
import SignIn from './pages/SignIn';

function App() {
    let Component;
    
    switch (window.location.pathname) {
        case "/":
        case "/signin": // Set both "/" and "/signin" to load the SignIn component
            Component = SignIn;
            break;
        case "/home":
            Component = Home;
            break;
        default:
            Component = SignIn; // Default to SignIn if the path doesn't match
            break;
    }

    return (
        <>
            <Navbar />
            <Component />
        </>
    );
}

export default App;
*/

// export default function App() {
//   const [books, setBooks] = useState([]);
//   const [error, setError] = useState(null);

//   const fetchBooks = async () => {
//     try {
//       const result = await api.get('/books');
//       setBooks(result.data);
//     } catch (error) {
//       setError(error);
//     }
//   };

//   useEffect(() => {
//     fetchBooks();
//   }, []);

//   return(
//     <div>
//       <BrowserRouter>
//         <Routes>
//           <Route index element={<Home books={books} error={error} />} />
//           <Route path="/home" element={<Home books={books} error={error} />} />
//           <Route path="/signin" element={<SignIn />} />
//         </Routes>
//       </BrowserRouter>
//     </div>
//   );
// }

// const App = () => {
//   const [books, setBooks] = useState([]);
//   const [error, setError] = useState(null);

//   const fetchBooks = async () => {
//     try {
//       const result = await api.get('/books');
//       setBooks(result.data);
//     } catch (error) {
//       setError('Error getting books');
//     }
//   };

//   useEffect(() => {
//     fetchBooks();
//   }, []);

//   if (error) {
//     return <div><h1>{error}</h1></div>;
//   }

//   return (
//     <div>
//       <nav className='navbar navbar-dark bg-primary'>
//         <div className='container-fluid'>
//           <a className='navbar-brand' href='#top'>Book App</a>
//         </div>
//       </nav>
      
//       <div className="container mt-4">
//         <div className="row">
//           {books.map((book) => (
//             <div className="col-md-4 mb-4" key={book.book_id}>
//               <div className="card">
//                 <img 
//                   src={book.image_url} 
//                   className="card-img-top" 
//                   alt={book.title} 
//                 />
//                 <div className="card-body">
//                   <h5 className="card-title">{book.title}</h5>
//                   <p className="card-text">Author: {book.authors}</p>
//                   <a href={`/books/${book.book_id}`} className="btn btn-primary">See More</a>
//                 </div>
//               </div>
//             </div>
//           ))}
//         </div>
//       </div>
//     </div>
//   );
// }

// export default App;