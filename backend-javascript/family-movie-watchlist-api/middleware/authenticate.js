import { verifyToken, hasBeenInvalidated } from '../utils/jwt.js';

export function authenticate(req, res, next) {
  const authHeader = req.headers.authorization;

  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'No token provided.' });
  }

  const token = authHeader.split(' ')[1];

  if (hasBeenInvalidated(token)) {
    return res.status(401).json({ error: 'Invalid or expired token.' });
  }

  const decodedUser = verifyToken(token);

  if (!decodedUser) {
    return res.status(401).json({ error: 'Invalid or expired token.' });
  }

  req.user = decodedUser;
  next();
}
