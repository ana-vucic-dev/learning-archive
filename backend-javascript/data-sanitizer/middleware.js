function inputCleaner(req, res, next) {
  const { username, comment } = req.body;

  if (username && typeof username === 'string' && username.trim().length) {
    req.body.username = username.toLowerCase();
  }

  if (comment && typeof comment === 'string') {
    req.body.comment = comment.trim().replace(/<\/?[^>]+(>|$)/g, '');
  }

  next();
}

function inputValidator(req, res, next) {
  const { username } = req.body;

  if (!username || typeof username !== 'string' || username.trim().length < 3) {
    res.redirect('/form?error=Username must be at least 3 characters.');
    return;
  }

  next();
}

export { inputCleaner, inputValidator };
