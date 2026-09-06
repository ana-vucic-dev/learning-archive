import express from 'express';
import bcrypt from 'bcryptjs';
import { findByUsername } from '../utils/db.js';
import { signToken, invalidateToken } from '../utils/jwt.js';
import { authenticate } from '../middleware/authenticate.js';

const router = express.Router();

router.post('/login', async (req, res) => {
  const { username, password } = req.body;

  if (!username || !password) {
    return res.status(400).json({ error: 'Enter your username and password.' });
  }

  const user = findByUsername(username);

  if (!user) {
    return res.status(401).json({ error: 'Invalid credentials.' });
  }

  const match = await bcrypt.compare(password, user.passwordHash);

  if (!match) {
    return res.status(401).json({ error: 'Invalid credentials.' });
  }

  const token = signToken({ id: user.id, username, role: user.role });
  return res
    .status(200)
    .json({ message: `Welcome back, ${user.name.split(' ')[0]}!`, token });
});

router.post('/logout', authenticate, (req, res) => {
  invalidateToken(req.headers.authorization.split(' ')[1]);
  return res.status(200).json({ message: 'Logout successful.' });
});

export default router;
