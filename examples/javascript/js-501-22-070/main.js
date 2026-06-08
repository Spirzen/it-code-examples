// Сегментация на слова
const wordSegmenter = new Intl.Segmenter("ru", { granularity: "word" });
const text = "Привет, мир! Как дела?";
const segments = wordSegmenter.segment(text);

for (const segment of segments) {
    console.log(segment.segment);
}
// "Привет"
// "мир"
// "Как"
// "дела"

// Сегментация на предложения
const sentenceSegmenter = new Intl.Segmenter("ru", { granularity: "sentence" });
const sentences = sentenceSegmenter.segment("Первое предложение. Второе предложение! Третье?");

for (const segment of sentences) {
    console.log(segment.segment);
}
// "Первое предложение."
// "Второе предложение!"
// "Третье?"
