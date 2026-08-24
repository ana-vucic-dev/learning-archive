# Case Converter

> This is a freeCodeCamp certification workshop. The package was prepared for publication as part of the exercise but was not actually published to npm.

This package is used to convert strings to a specific case.

## Installation

```bash
npm install case-converter
```

## Usage

```js
import * as caseConverter from './index.js';
const str = 'hello free Code Camp!';
console.log(caseConverter.getUpperCase(str)); // HELLO FREE CODE CAMP!
console.log(caseConverter.getLowerCase(str)); // hello free code camp!
console.log(caseConverter.getSentenceCase(str)); // Hello free code camp!
console.log(caseConverter.getTitleCase(str)); // Hello Free Code Camp!
```

## License

This package is licensed under the MIT license.
