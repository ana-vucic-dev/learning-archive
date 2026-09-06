import express from 'express';
import { authenticate } from '../middleware/authenticate.js';
import {
  getWatchlist,
  addMovie,
  updateMovie,
  deleteMovie
} from '../utils/db.js';
import { authorizeModification } from '../middleware/authorize.js';

const router = express.Router();

router.get('/:userId', authenticate, (req, res) => {
  const userId = Number(req.params.userId);
  const watchlist = getWatchlist(userId);

  if (!watchlist) {
    return res.status(404).json({ error: 'Watchlist not found.' });
  }

  return res.status(200).json({ watchlist });
});

router.post(
  '/:userId/movies',
  authenticate,
  authorizeModification,
  (req, res) => {
    const userId = Number(req.params.userId);
    const { title, genre } = req.body;

    if (!title || !title.trim().length || !genre || !genre.trim().length) {
      return res
        .status(400)
        .json({ error: 'Enter the movie title and genre.' });
    }

    const movie = addMovie(userId, { title, genre });

    if (!movie) {
      return res.status(404).json({ error: 'User not found.' });
    }

    return res.status(201).json({ message: `${title} added to watchlist.` });
  }
);

router.put(
  '/:userId/movies/:movieId',
  authenticate,
  authorizeModification,
  (req, res) => {
    const userId = Number(req.params.userId);
    const movieId = Number(req.params.movieId);

    const { updates } = req.body;
    const movie = updateMovie(userId, movieId, updates);

    if (!movie) {
      return res.status(404).json({ error: 'User or movie not found.' });
    }

    return res
      .status(200)
      .json({ message: `${movie.title} updated successfully.` });
  }
);

router.delete(
  '/:userId/movies/:movieId',
  authenticate,
  authorizeModification,
  (req, res) => {
    const userId = Number(req.params.userId);
    const movieId = Number(req.params.movieId);

    const isDeleted = deleteMovie(userId, movieId);

    if (!isDeleted) {
      return res.status(404).json({ error: 'User or movie not found.' });
    }

    return res.status(200).json({ message: 'Movie deleted.' });
  }
);

export default router;
