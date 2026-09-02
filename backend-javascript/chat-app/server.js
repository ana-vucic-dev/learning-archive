import http from 'http';
import fs from 'fs';
import { WebSocketServer, WebSocket } from 'ws';

const PORT = 3001;

const server = http.createServer((req, res) => {
  const files = {
    '/': { path: './public/index.html', contentType: 'text/html' },
    '/index.html': { path: './public/index.html', contentType: 'text/html' },
    '/script.js': { path: './public/script.js', contentType: 'text/javascript' }
  };

  const file = files[req.url];

  if (!file) {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('404 Not Found');
    return;
  }

  fs.readFile(file.path, (err, content) => {
    if (err) {
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.end('Internal Server Error');
      return;
    } else {
      res.writeHead(200, { 'Content-Type': file.contentType });
      res.end(content);
    }
  });
});

const wss = new WebSocketServer({ server });

wss.on('connection', (socket, req) => {
  const username = new URL(req.url, 'http://localhost').searchParams.get(
    'username'
  );

  wss.clients.forEach(client => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(
        JSON.stringify({ type: 'system', text: `${username} joined` })
      );
    }
  });

  socket.on('message', message => {
    const { username, text } = JSON.parse(message);

    wss.clients.forEach(client => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(JSON.stringify({ type: 'chat', username, text }));
      }
    });
  });

  socket.on('close', () => {
    wss.clients.forEach(client => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(
          JSON.stringify({ type: 'system', text: `${username} left` })
        );
      }
    });
  });
});

server.listen(PORT, () => {
  console.log(`Chat server running at http://localhost:${PORT}`);
});
