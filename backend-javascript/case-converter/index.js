function getUpperCase(str) {
  return str.toUpperCase();
}

function getLowerCase(str) {
  return str.toLowerCase();
}

function getSentenceCase(str) {
  return str[0].toUpperCase() + str.slice(1).toLowerCase();
}

function getTitleCase(str) {
  const words = str.split(' ');
  const result = [];

  for (let i = 0; i < words.length; i++) {
    result.push(words[i][0].toUpperCase() + words[i].slice(1).toLowerCase());
  }

  return result.join(' ');
}

export { getUpperCase, getLowerCase, getSentenceCase, getTitleCase };
