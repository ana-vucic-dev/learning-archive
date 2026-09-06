import jwt from 'jsonwebtoken';

const tokens = new Set();

export function signToken(payload) {
  return jwt.sign(payload, process.env.JWT_SECRET, { expiresIn: '1d' });
}

export function verifyToken(token) {
  try {
    return jwt.verify(token, process.env.JWT_SECRET);
  } catch (error) {
    return null;
  }
}

export function invalidateToken(token) {
  tokens.add(token);
  return;
}

export function hasBeenInvalidated(token) {
  return tokens.has(token);
}
