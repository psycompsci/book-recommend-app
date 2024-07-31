import axios from 'axios';

const PORT_NUMBER = 8000;

// connecting to FastAPI @ port 8000
const api = axios.create({
  baseURL: process.env.REACT_APP_CODESPACE_NAME ? "https://" + process.env.REACT_APP_CODESPACE_NAME + "-" + PORT_NUMBER + ".app.github.dev" : "random",
})

export default api;