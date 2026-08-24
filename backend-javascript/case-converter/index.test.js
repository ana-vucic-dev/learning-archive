import { strictEqual } from 'node:assert/strict';
import * as caseConverter from './index.js';

strictEqual(
  caseConverter.getUpperCase('hello free Code Camp!'),
  'HELLO FREE CODE CAMP!'
);

strictEqual(
  caseConverter.getLowerCase('hello free Code Camp!'),
  'hello free code camp!'
);

strictEqual(
  caseConverter.getSentenceCase('hello free Code Camp!'),
  'Hello free code camp!'
);

strictEqual(
  caseConverter.getTitleCase('hello free Code Camp!'),
  'Hello Free Code Camp!'
);
