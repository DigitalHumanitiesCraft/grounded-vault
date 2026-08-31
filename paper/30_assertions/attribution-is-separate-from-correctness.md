---
type: assertion
topics: ["[[Verification]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
grounding:
  - "[[20_distillates/publications/rashkin-2023-measuring-attribution#^s1]]"
  - "[[20_distillates/publications/rashkin-2023-measuring-attribution#^s2]]"
  - "[[20_distillates/publications/rashkin-2023-measuring-attribution#^s8]]"
  - "[[20_distillates/documents/gao-2023-llms-generate-text-with-citations#^s7]]"
  - "[[20_distillates/documents/gao-2023-llms-generate-text-with-citations#^s8]]"
contested-with: []
created: 2026-08-10
updated: 2026-08-10
---

# Attribution is separate from correctness

## Statement

Attribution is the accurate use of source documents to support generated text, and the AIS framework checks generated output about the external world against an independent source supplied with the output. That framework declines any absolute verdict on the factuality of the statement. Automatic evaluation of generated text with citations follows the same cut and scores correctness, meaning whether the answer is accurate and covers all aspects of interest, on a different axis from citation quality, meaning support of the answer by the cited passages.

## Support

- [[20_distillates/publications/rashkin-2023-measuring-attribution#^s1]] — presents AIS as checking generated output against an independent source supplied with the output.
- [[20_distillates/publications/rashkin-2023-measuring-attribution#^s2]] — defines attribution as the accurate use of source documents to support generated text, which fixes the relation as one between text and source.
- [[20_distillates/publications/rashkin-2023-measuring-attribution#^s8]] — records that the framework avoids absolute judgments about the factuality of utterances, which keeps truth outside the attribution verdict.
- [[20_distillates/documents/gao-2023-llms-generate-text-with-citations#^s7]] — defines correctness as whether the answer is accurate and covers all aspects of interest.
- [[20_distillates/documents/gao-2023-llms-generate-text-with-citations#^s8]] — defines citation quality as whether the answer is well supported by the cited passages, which is the second and independent axis.

## Related

- [[30_assertions/generated-citations-often-fail-to-support-their-sentences]]
- [[30_assertions/historical-method-separates-origin-check-from-credibility]]
