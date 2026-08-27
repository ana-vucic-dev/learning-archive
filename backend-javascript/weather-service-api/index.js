import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';
import weatherRouter from './weather.js';

const app = express();
const PORT = 3000;

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.get('/api/info', (req, res) => {
  res.status(200).json({
    name: 'Weather Service API',
    version: '1.0.0',
    description: 'Developer-friendly weather service API with real-time data',
    endpoints: ['/api/weather/:city', '/api/greet/:name', '/api/data']
  });
});

app.get('/api/status', (req, res) => {
  res.status(200).json({ status: 'online' });
});

app.get('/docs', (req, res) => {
  res.redirect('/api/info');
});

app.get('/api/greet/:name', (req, res) => {
  const name = req.params.name;
  res.status(200).json({ user: name });
});

app.get('/api/data', (req, res) => {
  res.status(200).json({
    message: 'Weather data is available through the city-specific endpoints.'
  });
});

app.use('/api/weather', weatherRouter);

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
