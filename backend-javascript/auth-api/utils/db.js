import path from 'path';
import fs from 'fs';

const DB_PATH = path.join(import.meta.dirname, '../data/users.json');

export function readUsers() {
  const users = fs.readFileSync(DB_PATH, 'utf-8').trim();

  if (!users.length) {
    return [];
  }

  return JSON.parse(users);
}

export function writeUsers(users) {
  fs.writeFileSync(DB_PATH, JSON.stringify(users, null, 2));
}

export function findByEmail(email) {
  return readUsers().find(user => user.email === email) || null;
}

export function findById(id) {
  return readUsers().find(user => user.id === id) || null;
}
