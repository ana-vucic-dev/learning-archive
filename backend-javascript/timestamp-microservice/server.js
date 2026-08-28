import express from 'express';
import cors from 'cors';

const app = express();

app.use(cors({ optionsSuccessStatus: 200 }));

app.use(express.static('public'));

app.get('/', (_req, res) => {
  res.sendFile(__dirname + '/views/index.html');
});

// Do not change code above this line
app.get('/api{/:date}', (req, res) => {
  const dateString = req.params.date;

  if (!dateString) {
    const unix = Date.now();
    const utc = new Date(unix).toUTCString();
    res.status(200).json({ unix, utc });
    return;
  }

  if (!Number.isNaN(Number(dateString))) {
    const date = new Date(Number(dateString));
    res.status(200).json({ unix: date.getTime(), utc: date.toUTCString() });
    return;
  }

  const date = new Date(dateString);

  if (Number.isNaN(date.getTime())) {
    res.status(400).json({ error: 'Invalid Date' });
    return;
  }

  res.status(200).json({ unix: date.getTime(), utc: date.toUTCString() });
});
// Do not change code below this line

const PORT = 8000;
const listener = app.listen(PORT, function () {
  console.log('Your app is listening on port ' + listener.address().port);
});
