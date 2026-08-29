import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';
import { inputCleaner, inputValidator } from './middleware.js';

const app = express();
const PORT = 3000;

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

app.get('/', (req, res) => {
  res.redirect('/form');
});

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

app.get('/form', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/submit', inputCleaner, inputValidator, (req, res) => {
  const { username, comment } = req.body;
  res.status(200).json({ username, comment });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
